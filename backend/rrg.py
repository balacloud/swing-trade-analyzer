"""
rrg.py - Relative Rotation Graph (RRG) numbers, built to the public description
of Julius de Kempenaer's JdK RS-Ratio / RS-Momentum (the version Bloomberg and
StockCharts show). Pure functions, no Flask, no network.

The exact JdK maths is proprietary, so this is a close approximation, not a copy
(the common public one, built from moving averages so the trail is smooth):

  1. Relative strength  RS = fund close / SPY close, on WEEKLY (Friday) closes.
  2. RS-Ratio    = 100 * (10-week average of RS) / (26-week average of RS)
                   above 100 = recent strength is above its own longer-run level.
  3. RS-Momentum = 100 * RS-Ratio / RS-Ratio four weeks ago
                   above 100 = the ratio is rising.
  4. Corners cut at 100 / 100:
        Leading   ratio >= 100, momentum >= 100
        Weakening ratio >= 100, momentum <  100
        Lagging   ratio <  100, momentum <  100
        Improving ratio <  100, momentum >= 100

API compatibility: STA already stores momentum centred on 0, so `rs_momentum`
here is (momentum - 100). A cut at 0 is the same cut as the standard 100.
`tail` holds the last TAIL_WEEKS weekly points (the RRG "trail").

Thin history (a young fund) shrinks the long window (and the short one in
proportion) and sets `thin` = True instead of inventing a number. Under
MIN_LONG_WINDOW long-window weeks it raises ValueError.
"""

import math

import pandas as pd

LONG_WINDOW = 26       # weeks, the "own longer-run level"
SHORT_WINDOW = 10      # weeks, the "recent strength"
MOM_WEEKS = 4          # momentum = ratio now vs this many weeks ago
MIN_LONG_WINDOW = 12   # fewest long-window weeks we accept
TAIL_WEEKS = 5


def quadrant_for(rs_ratio, rs_momentum):
    """rs_ratio is 100-centred, rs_momentum is 0-centred (STA convention)."""
    if rs_ratio >= 100 and rs_momentum >= 0:
        return 'Leading'
    if rs_ratio >= 100:
        return 'Weakening'
    if rs_momentum < 0:
        return 'Lagging'
    return 'Improving'


def weekly_rs(target_close, spy_close):
    """Weekly (Friday) fund/SPY series on the dates both have. tz-naive safe."""
    t = target_close.dropna()
    s = spy_close.dropna()
    for ser in (t, s):
        if getattr(ser.index, 'tz', None) is not None:
            ser.index = ser.index.tz_localize(None)
    common = t.index.intersection(s.index)
    if len(common) == 0:
        raise ValueError('no dates in common with SPY')
    rs = (t.loc[common] / s.loc[common]).replace([float('inf'), float('-inf')], float('nan')).dropna()
    return rs.resample('W-FRI').last().dropna()


def compute_rrg(target_close, spy_close):
    """
    Returns dict: rs_ratio (100-centred), rs_momentum (0-centred), quadrant,
    tail [{rs_ratio, rs_momentum}], weeks (weekly bars used), thin (bool).
    Raises ValueError if there is too little history.
    """
    rs = weekly_rs(target_close, spy_close)
    n = len(rs)
    long_w = min(LONG_WINDOW, n - MOM_WEEKS)
    if long_w < MIN_LONG_WINDOW:
        raise ValueError(f'only {n} weekly bars; need at least {MIN_LONG_WINDOW + MOM_WEEKS}')
    short_w = SHORT_WINDOW if long_w == LONG_WINDOW else max(3, round(long_w * SHORT_WINDOW / LONG_WINDOW))

    ratio = 100.0 * rs.rolling(short_w).mean() / rs.rolling(long_w).mean()
    mom = 100.0 * ratio / ratio.shift(MOM_WEEKS)
    both = pd.DataFrame({'r': ratio, 'm': mom}).replace([float('inf'), float('-inf')], float('nan')).dropna()
    if both.empty:
        raise ValueError('no weekly point has both ratio and momentum')

    rs_ratio = float(both['r'].iloc[-1])
    rs_mom = float(both['m'].iloc[-1]) - 100.0
    if not (math.isfinite(rs_ratio) and math.isfinite(rs_mom)):
        raise ValueError('non-finite RS values')

    tail = []
    for r, m in zip(both['r'].iloc[-TAIL_WEEKS:], both['m'].iloc[-TAIL_WEEKS:]):
        t_ratio, t_mom = round(float(r), 2), round(float(m) - 100.0, 2)
        # each trail point carries its own corner so the UI never re-implements the rule
        tail.append({'rs_ratio': t_ratio, 'rs_momentum': t_mom, 'quadrant': quadrant_for(t_ratio, t_mom)})
    rs_ratio, rs_mom = round(rs_ratio, 2), round(rs_mom, 2)
    return {
        'rs_ratio': rs_ratio,
        'rs_momentum': rs_mom,
        'quadrant': quadrant_for(rs_ratio, rs_mom),
        'tail': tail,
        'weeks': n,
        'thin': long_w < LONG_WINDOW,
    }
