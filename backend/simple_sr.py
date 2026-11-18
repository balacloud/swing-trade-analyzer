"""
Simple support/resistance (Day 126) — the levels most traders would draw by hand.

Plan: docs/claude/design/SIMPLE_SR_PLAN_DAY125.md §2, with §8 (Fable review) and
§9 (Reddit check) overriding. Common trader rules, NOT backtested (same user
decision as the Day 125 breakout rules). Replaces support_resistance.py for the
Analyze page only when constants.SR_ENGINE == 'simple'; the old engine stays for
backtest_holistic.py and the discontinued paper_trading/live_signals.py.

The rules, in plain words:
  1. A level is a swing high or swing low: a bar whose high (low) is the highest
     (lowest) of the 5 bars on each side. Last 252 daily bars.
  2. Swings close together are one zone: merge neighbours less than 0.5 ATR
     apart, but never let a zone grow wider than 1 ATR.
  3. Nearest only: support = the zone just below price (or the one price is
     inside), resistance = the zone just above. Same 20% below / 30% above
     window as before. Nothing in the window -> none. No projected,
     ATR or Fibonacci levels, no fallback methods.
  Each zone reports how many times price turned there (`swings`); the user
  judges whether one turn is enough. (Day 126: the weekly ★ and the "prefer
  2+ turns" rule were removed: ★ was on 89% of nearest zones, so it carried
  no information.)

Blind spot (standard for this method): the last 5 daily bars can't be
confirmed swings yet. `confirmedThrough` says up to which date.
All on completed bars (market_time.drop_forming_bar); the live price only
decides which side of price a zone is on.
"""
import logging

import numpy as np
import pandas as pd

from constants import SUPPORT_PROXIMITY_PCT, RESISTANCE_PROXIMITY_PCT
from market_time import drop_forming_bar

logger = logging.getLogger(__name__)

MIN_BARS = 60            # completed daily bars needed, else an error (never a guess)
ATR_PERIOD = 14
DAILY_WING = 5           # bars each side for a daily swing
DAILY_LOOKBACK = 252     # about one year of daily swings
MERGE_ATR = 0.5          # neighbours closer than this join one zone...
MAX_ZONE_ATR = 1.0       # ...unless the zone would get wider than this
NEAR_HIGH_PCT = 0.03     # no resistance and within 3% of the 252-bar high -> "at its 52-week high"


class SimpleSRError(Exception):
    """Not enough clean data to draw levels. The route turns this into a 400."""


def wilder_atr(df, period=ATR_PERIOD):
    """Wilder ATR(14): SMA seed over the first `period` true ranges, then
    (prev × 13 + TR) / 14. Same formula as support_resistance._calculate_atr,
    kept here so the new engine doesn't import the sklearn module. None when
    there are fewer than period + 1 bars."""
    if df is None or len(df) < period + 1:
        return None
    high = df['high'].to_numpy(dtype=float)
    low = df['low'].to_numpy(dtype=float)
    close = df['close'].to_numpy(dtype=float)
    tr = np.empty(len(df))
    tr[0] = high[0] - low[0]
    tr[1:] = np.maximum(high[1:] - low[1:],
                        np.maximum(np.abs(high[1:] - close[:-1]), np.abs(low[1:] - close[:-1])))
    atr = tr[:period].mean()
    for x in tr[period:]:
        atr = (atr * (period - 1) + x) / period
    return float(atr)


def _swings(frame, wing, lookback):
    """Swing highs/lows as [{price, kind, pos, date}], oldest first.

    Vectorised centred rolling max/min (Fable #20). `>=` so a flat top still
    counts; equal prices within one window (2*wing+1 bars) count once, keeping
    the later date (Fable #10). Swings are found on the whole frame so the
    first bars of the lookback aren't blind, then only the last `lookback`
    bars are kept (Fable #9)."""
    n = len(frame)
    win = 2 * wing + 1
    first_kept = max(0, n - lookback)
    out = []
    for kind, col, roll in (('high', 'high', 'max'), ('low', 'low', 'min')):
        s = frame[col]
        ext = getattr(s.rolling(win, center=True), roll)()   # NaN in the first/last `wing` bars
        hit = (s >= ext) if kind == 'high' else (s <= ext)
        positions = np.flatnonzero(hit.to_numpy() & ext.notna().to_numpy())
        kept = []
        for p in positions:
            if p < first_kept:
                continue
            price = float(s.iloc[p])
            if kept and round(kept[-1]['price'], 2) == round(price, 2) and p - kept[-1]['pos'] < win:
                kept[-1].update(pos=int(p), date=str(frame.index[p].date()))   # same turn, later date
                continue
            kept.append({'price': price, 'kind': kind, 'pos': int(p), 'date': str(frame.index[p].date())})
        out.extend(kept)
    return out


def _zones(swings, atr):
    """Merge swing prices (highs and lows together, so a role flip counts as 2
    turns) into zones. Neighbour gap <= 0.5 ATR AND resulting width <= 1 ATR
    (Fable #4: without the width cap, a staircase of swings chains into one
    giant zone)."""
    zones = []
    for s in sorted(swings, key=lambda x: x['price']):
        z = zones[-1] if zones else None
        if (z is not None and s['price'] - z['_last'] <= MERGE_ATR * atr
                and s['price'] - z['low'] <= MAX_ZONE_ATR * atr):
            z['high'] = s['price']
            z['_last'] = s['price']
            z['_members'].append(s)
        else:
            zones.append({'low': s['price'], 'high': s['price'], '_last': s['price'], '_members': [s]})
    return zones


def compute_simple_sr(df, current_price=None, now=None,
                      support_pct=SUPPORT_PROXIMITY_PCT, resistance_pct=RESISTANCE_PROXIMITY_PCT):
    """
    Args:
        df: daily OHLC frame, lowercase columns, DatetimeIndex. Pass the full
            2-year fetch, not a 260-bar tail (the switch plan reads a full year of swings).
        current_price: the live price the route shows. Decides which side of
            price each zone is on. Default: last completed close.
        now: injectable clock for the forming-bar rule (tests).

    Returns a dict:
        support / resistance: zone edges nearest to price, nearest first
            (the zone price is INSIDE counts as distance 0, Day 127; support -> zone HIGH, resistance -> zone LOW; Fable #1, so the Buy
            price is the same everywhere, except that sr_plan.plan_entry uses the last completed close as the Buy when that close is already inside the nearest support zone, Day 127). Every zone in the window on that side,
            whatever its turn count (the nearest one is flagged `nearest`).
        allSupport / allResistance: every zone's edge on that side, no window.
        zones: every zone inside the window, with low/high/mid/swings/highs/
            lows/side/insideZone/nearest/lastSwingDate.
        atr, high52w, nearHigh52w, confirmedThrough {daily},
        barsUsed, droppedFormingBar, nanRowsDropped.

    Raises SimpleSRError when fewer than MIN_BARS clean completed bars remain.
    """
    if df is None or len(df) == 0:
        raise SimpleSRError('No price data')
    if not isinstance(df.index, pd.DatetimeIndex):
        raise SimpleSRError('Price data has no dates (a DatetimeIndex is required)')

    frame = df[['high', 'low', 'close']].astype(float)
    if frame.index.tz is not None:                 # Golden Rule 40: one tz convention before resampling
        frame = frame.tz_localize(None)
    frame, dropped = drop_forming_bar(frame, now=now)
    nan_rows = int(frame.isna().any(axis=1).sum())
    if nan_rows:
        logger.warning('simple_sr: dropped %d rows with missing high/low/close', nan_rows)
        frame = frame.dropna()
    if len(frame) < MIN_BARS:
        raise SimpleSRError(f'Need at least {MIN_BARS} completed daily bars, got {len(frame)}')

    atr = wilder_atr(frame)
    if atr is None or atr <= 0:
        raise SimpleSRError('ATR unavailable, so swings cannot be grouped into zones')

    price = float(current_price) if current_price is not None and np.isfinite(current_price) \
        else float(frame['close'].iloc[-1])

    daily = _swings(frame, DAILY_WING, DAILY_LOOKBACK)

    support_floor = price * (1 - support_pct)
    resistance_ceiling = price * (1 + resistance_pct)

    all_support, all_resistance, in_window = [], [], []
    for z in _zones(daily, atr):
        members = z['_members']
        inside = z['low'] <= price <= z['high']
        side = 'resistance' if z['low'] > price else 'support'   # inside a zone -> it's the support (Fable #11)
        edge = z['low'] if side == 'resistance' else z['high']
        zone = {
            'low': round(z['low'], 2),
            'high': round(z['high'], 2),
            'mid': round((z['low'] + z['high']) / 2, 2),
            'swings': len(members),
            'highs': sum(1 for m in members if m['kind'] == 'high'),
            'lows': sum(1 for m in members if m['kind'] == 'low'),
            'side': side,
            'insideZone': inside,
            'nearest': False,
            'lastSwingDate': max(m['date'] for m in members),
            '_edge': edge,
        }
        (all_resistance if side == 'resistance' else all_support).append(round(edge, 2))
        in_win = (support_floor <= edge) if side == 'support' else (edge <= resistance_ceiling)
        if in_win:
            in_window.append(zone)

    def distance(z):
        # Day 127 (Statement Audit, PLD): the zone price is INSIDE is the support (rule 3, Fable #11), so it is distance 0. Before, every zone was
        # ranked by the distance to its edge (the HIGH for support), so a lower zone whose high was nearer won and the Buy (the inside zone's high)
        # disagreed with the "nearest" Support row. Zones never overlap, so at most one zone holds the price.
        return 0.0 if z['insideZone'] else abs(z['_edge'] - price)

    def pick(side):
        cands = [z for z in in_window if z['side'] == side]
        cands.sort(key=distance)
        if cands:
            cands[0]['nearest'] = True
        return [round(z['_edge'], 2) for z in cands]

    support = pick('support')
    resistance = pick('resistance')

    high52w = float(frame['high'].iloc[-DAILY_LOOKBACK:].max())
    near_high = not resistance and price >= high52w * (1 - NEAR_HIGH_PCT)

    in_window.sort(key=distance)
    for z in in_window:
        del z['_edge']

    return {
        'support': support,
        'resistance': resistance,
        'allSupport': sorted(all_support, reverse=True),
        'allResistance': sorted(all_resistance),
        'zones': in_window,
        'atr': round(atr, 4),
        'high52w': round(high52w, 2),
        'nearHigh52w': bool(near_high),
        'confirmedThrough': {'daily': str(frame.index[-1 - DAILY_WING].date())},
        'currentPrice': round(price, 2),
        'barsUsed': len(frame),
        'droppedFormingBar': bool(dropped),
        'nanRowsDropped': nan_rows,
    }
