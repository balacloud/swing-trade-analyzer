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


def trade_plan(support, resistance, atr):
    """Buy at the nearest support, stop 2×ATR below it (floored at $0.01),
    target the nearest resistance. Missing input -> None for what depends on
    it, never a made-up number (Day 123). Rounding matches the old route."""
    entry = round(max(support), 2) if support else None
    stop = None
    if entry is not None and atr is not None and atr > 0:
        stop = max(0.01, round(entry - 2 * atr, 2))
    target = round(min(resistance), 2) if resistance else None
    rr = None
    if entry is not None and stop is not None and target is not None and entry - stop > 0:
        rr = round((target - entry) / (entry - stop), 2)
    return {'entry': entry, 'stop': stop, 'target': target, 'riskReward': rr}
