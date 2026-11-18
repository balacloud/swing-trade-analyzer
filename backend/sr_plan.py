"""
Buy / stop / target / reward:risk from support and resistance prices (Day 126).

One place for this arithmetic (SIMPLE_SR_PLAN_DAY125.md §8 #5): the /api/sr
route uses it for both engines, and backtest/compare_sr_engines.py uses it for
the old-vs-new table, so the table can't become a second scoring engine.
Trade Setup (riskRewardCalc.js) reads the levels from the API and shows the
plan with no grade. (The Simple Checklist that graded stop width and R:R from
these values was removed Day 126: R:R is the user's judgment.)
"""


def legacy_actionable(support, resistance, current_price, support_pct, resistance_pct):
    """The old route's proximity filter (Day 15), unchanged: support within
    `support_pct` below and strictly below price, resistance strictly above and
    within `resistance_pct`. Order preserved. Used only for the legacy engine;
    the simple engine applies its own window on zone edges."""
    floor = current_price * (1 - support_pct)
    ceiling = current_price * (1 + resistance_pct)
    return ([s for s in support if s >= floor and s < current_price],
            [r for r in resistance if r > current_price and r <= ceiling])


def plan_entry(zones, last_close):
    """Day 127 (persona + Opus review): ONE place decides the Buy.
    Returns (entry_override, basis).
      - the nearest SUPPORT zone holds the last COMPLETED close  -> the Buy is that close ("price is already at support"):
        ('last_close_inside_zone'). Before, the Buy was the zone's HIGH, which is above the market whenever price sits inside the zone
        (SOXL.NE +8.9%, AMD +5.3%): a "wait for a dip" plan whose Buy fills immediately, with risk and reward measured from a price you cannot get.
      - otherwise (price above the zone, or no zone) -> no override: trade_plan's default, the zone HIGH ('zone_high'), as before.
      - no zone information at all (legacy engine) -> 'nearest_support'.
    No clamping: the live price (which decides insideZone) and the last close can sit on different sides of a zone edge during the day;
    the Buy is the close only when the CLOSE is inside, so the label is always true. A NaN close falls back to the zone high."""
    z = next((q for q in (zones or []) if q.get('nearest') and q.get('side') == 'support'), None)
    if z is None:
        return None, 'nearest_support'
    try:
        lc = float(last_close)
    except (TypeError, ValueError):
        lc = float('nan')
    if lc == lc and z['low'] <= lc <= z['high']:      # lc == lc is False for NaN
        return round(lc, 2), 'last_close_inside_zone'
    return None, 'zone_high'


def trade_plan(support, resistance, atr, entry_override=None):
    """Buy at the nearest support (or `entry_override`, see plan_entry), stop 2×ATR below it (floored at $0.01),
    target the nearest resistance. Missing input -> None for what depends on
    it, never a made-up number (Day 123). Rounding matches the old route."""
    entry = entry_override if entry_override is not None else (round(max(support), 2) if support else None)
    stop = None
    if entry is not None and atr is not None and atr > 0:
        stop = max(0.01, round(entry - 2 * atr, 2))
    target = round(min(resistance), 2) if resistance else None
    rr = None
    if entry is not None and stop is not None and target is not None and entry - stop > 0:
        rr = round((target - entry) / (entry - stop), 2)
    return {'entry': entry, 'stop': stop, 'target': target, 'riskReward': rr}
