"""
Checks for simple_sr.py (simple support/resistance engine) and sr_plan.py (Day 126).
Plan: docs/claude/design/SIMPLE_SR_PLAN_DAY125.md §2, with §8 (Fable) and §9 (Reddit) overriding.
Run: cd backend && venv/bin/python backtest/test_simple_sr.py

Synthetic frames: a steady uptrend (+0.05 a bar, high/low = close ± 0.5, ATR ≈ 1).
A rising line has no swing highs or lows on its own, so every swing in a test is
one we put there on purpose:
  - major_high / major_low: a spike far outside the line (a daily swing)
  - minor_high / minor_low: just past 5 bars of drift (a smaller daily swing)
"""
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from simple_sr import compute_simple_sr, wilder_atr, SimpleSRError, MIN_BARS
from sr_plan import trade_plan, legacy_actionable, plan_entry
from market_time import MARKET_TZ

passed = 0
STEP = 0.05
NOW = datetime(2026, 11, 12, 20, 0, tzinfo=MARKET_TZ)  # after the close; frames end 2026-11-10


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


def base(n=300, start=100.0, step=STEP, end='2026-11-10'):
    idx = pd.bdate_range(end=end, periods=n)
    c = start + step * np.arange(n)
    return pd.DataFrame({'open': c, 'high': c + 0.5, 'low': c - 0.5, 'close': c,
                         'volume': np.full(n, 1e6)}, index=idx)


def major_high(df, pos, price):
    df.iloc[pos, df.columns.get_loc('high')] = price


def major_low(df, pos, price):
    df.iloc[pos, df.columns.get_loc('low')] = price


def minor_high(df, pos):
    c = df['close'].iloc[pos]
    df.iloc[pos, df.columns.get_loc('high')] = round(c + 0.5 + 0.27, 4)
    return df['high'].iloc[pos]


def minor_low(df, pos):
    c = df['close'].iloc[pos]
    df.iloc[pos, df.columns.get_loc('low')] = round(c - 0.5 - 0.27, 4)
    return df['low'].iloc[pos]


def zone_at(res, price, tol=0.01):
    for z in res['zones']:
        if z['low'] - tol <= price <= z['high'] + tol:
            return z
    return None


def run(df, price=None, now=NOW):
    return compute_simple_sr(df, current_price=price, now=now)


# ---------------------------------------------------------------- ATR
flat = base(n=40, step=0.0)
check('ATR of a constant 1.00 range is 1.00', abs(wilder_atr(flat) - 1.0) < 1e-9)
check('ATR needs 15 bars, else None', wilder_atr(base(n=14)) is None)

# ---------------------------------------------------------------- min bars
try:
    run(base(n=MIN_BARS - 1))
    check('fewer than 60 completed bars -> error', False)
except SimpleSRError:
    check('fewer than 60 completed bars -> error', True)
check('exactly 60 bars -> works', run(base(n=MIN_BARS))['barsUsed'] == MIN_BARS)

# ---------------------------------------------------------------- forming bar
today = base(n=200, end='2026-11-12')
r = run(today, now=datetime(2026, 11, 12, 11, 0, tzinfo=MARKET_TZ))
check('intraday: today\'s forming bar dropped', r['droppedFormingBar'] is True and r['barsUsed'] == 199)
r = run(today, now=datetime(2026, 11, 12, 17, 0, tzinfo=MARKET_TZ))
check('after 16:30 ET: today\'s bar kept', r['droppedFormingBar'] is False and r['barsUsed'] == 200)

# ---------------------------------------------------------------- NaN rows
df = base()
df.iloc[[10, 20, 30], df.columns.get_loc('close')] = np.nan
r = run(df)
check('NaN rows dropped and counted', r['nanRowsDropped'] == 3 and r['barsUsed'] == 297)
df = base(n=62)
df.iloc[[1, 2, 3], df.columns.get_loc('high')] = np.nan
try:
    run(df)
    check('NaN drop below 60 bars -> error, not a guess', False)
except SimpleSRError:
    check('NaN drop below 60 bars -> error, not a guess', True)

# ---------------------------------------------------------------- nothing there
r = run(base())
check('plain uptrend: no swings, no zones', r['zones'] == [] and r['support'] == [] and r['resistance'] == [])
check('plain uptrend: at its 52-week high, flagged as a fact', r['nearHigh52w'] is True)
check('high52w = highest high of the last 252 bars', abs(r['high52w'] - round(base()['high'].iloc[-252:].max(), 2)) < 1e-9)

# ---------------------------------------------------------------- edges (Fable #9)
df = base()
major_high(df, -3, 130.0)
r = run(df)
check('a peak inside the last 5 bars is not a confirmed swing', zone_at(r, 130.0) is None)
check('confirmedThrough.daily = 6th bar from the end', r['confirmedThrough']['daily'] == str(df.index[-6].date()) and 'weekly' not in r['confirmedThrough'])
df = base()
major_high(df, -6, 130.0)
r = run(df)
check('a peak exactly 5 bars back is a swing', zone_at(r, 130.0) is not None)

# ---------------------------------------------------------------- flat tops (Fable #10)
df = base()
major_high(df, -50, 130.0)
major_high(df, -53, 130.0)
z = zone_at(run(df), 130.0)
check('two equal highs 3 bars apart count once', z is not None and z['swings'] == 1)
df = base()
major_high(df, -50, 130.0)
major_high(df, -100, 130.0)
z = zone_at(run(df), 130.0)
check('two equal highs 50 bars apart count twice', z is not None and z['swings'] == 2)

# ---------------------------------------------------------------- role flip
df = base()
major_high(df, -200, 110.0)
major_low(df, -60, 110.0)
z = zone_at(run(df), 110.0)
check('a swing high and a swing low at one price = 2 turns', z is not None and z['swings'] == 2
      and z['highs'] == 1 and z['lows'] == 1)

# ---------------------------------------------------------------- chain cap (Fable #4)
df = base()
atr0 = 1.0
prices = [100.0 + 0.4 * atr0 * k for k in range(6)]
for k, p in enumerate(prices):
    major_low(df, -60 - 15 * k, p)
r = run(df)
atr = r['atr']
chain = [z for z in r['zones'] if 99.9 <= z['mid'] <= 102.1]
check('6 swings 0.4 ATR apart do not chain into one zone', len(chain) >= 2)
check('no zone is wider than 1 ATR', all(z['high'] - z['low'] <= 1.0 * atr + 1e-9 for z in r['zones']))
check('all 6 swings are kept across the zones', sum(z['swings'] for z in chain) == 6)

# ---------------------------------------------------------------- live price decides the side (Fable #3)
df = base()
major_low(df, -100, 105.0)
major_high(df, -80, 118.0)
r = run(df)  # price = last close, 114.95
check('below price -> support, above -> resistance', r['support'][:1] == [105.0] and r['resistance'][:1] == [118.0])
r = run(df, price=119.0)
check('live price above 118: 118 becomes the nearest support', r['support'][0] == 118.0 and r['resistance'] == [])
check('support array is nearest first', r['support'] == sorted(r['support'], reverse=True))

# ---------------------------------------------------------------- straddle (Fable #11)
df = base()
major_low(df, -40, 112.0)
major_high(df, -120, 112.3)
major_high(df, -80, 118.0)
r = run(df, price=112.15)
nz = [z for z in r['zones'] if z['nearest'] and z['side'] == 'support'][0]
check('price inside a zone: it is the support, edge = zone high', r['support'][0] == 112.3 and nz['insideZone'] is True)
check('price inside a zone: resistance is the next zone above', r['resistance'][0] == 118.0)

# ---------------------------------------------------------------- nearest wins, whatever the turn count (Day 126)
df = base()
weak = minor_low(df, -30)
major_low(df, -100, 105.0)
major_low(df, -150, 105.0)
r = run(df)
check('nearer 1-turn zone is the support, not the farther 2-turn zone', abs(r['support'][0] - round(weak, 2)) < 1e-9)
check('the farther 2-turn zone is still listed, not nearest', zone_at(r, 105.0)['nearest'] is False and zone_at(r, 105.0)['swings'] == 2)
check('turn count is reported on every zone', zone_at(r, weak)['swings'] == 1 and zone_at(r, 105.0)['swings'] == 2)
check('exactly one nearest zone per side', sum(1 for z in r['zones'] if z['nearest'] and z['side'] == 'support') == 1)

# ---------------------------------------------------------------- window (20% below / 30% above)
df = base()
major_low(df, -100, 85.0)       # 26% below 114.95
major_high(df, -80, 160.0)      # 39% above
r = run(df)
check('support more than 20% below is left out', r['support'] == [] and 85.0 in r['allSupport'])
check('resistance more than 30% above is left out', r['resistance'] == [] and 160.0 in r['allResistance'])
check('out-of-window zones are not in meta zones', zone_at(r, 85.0) is None and zone_at(r, 160.0) is None)
check('no resistance in window but 160 high -> not at the 52-week high', r['nearHigh52w'] is False)

# ---------------------------------------------------------------- zone fields
df = base()
major_low(df, -100, 105.0)
z = zone_at(run(df), 105.0)
check('zone has low/high/mid/swings/side/lastSwingDate, and no weekly field',
      'weekly' not in z and all(k in z for k in ('low', 'high', 'mid', 'swings', 'side', 'lastSwingDate', 'insideZone', 'nearest')))
check('lastSwingDate is the swing bar\'s date', z['lastSwingDate'] == str(df.index[-100].date()))

# ---------------------------------------------------------------- sr_plan.trade_plan
p = trade_plan([95.0, 90.0], [110.0, 120.0], atr=2.0)
check('entry = nearest support, stop 2 ATR below, target = nearest resistance',
      p['entry'] == 95.0 and p['stop'] == 91.0 and p['target'] == 110.0)
check('R:R = (110-95)/(95-91) = 3.75', p['riskReward'] == 3.75)
p = trade_plan([95.0], [], atr=2.0)
check('no resistance: no target, no R:R', p['target'] is None and p['riskReward'] is None and p['stop'] == 91.0)
p = trade_plan([95.0], [110.0], atr=None)
check('no ATR: no stop, no R:R (no made-up 3%)', p['stop'] is None and p['riskReward'] is None)
p = trade_plan([1.0], [2.0], atr=5.0)
check('stop floored at $0.01', p['stop'] == 0.01)
p = trade_plan([], [110.0], atr=2.0)
check('no support: no entry, no stop', p['entry'] is None and p['stop'] is None and p['target'] == 110.0)

# ---------------------------------------------------------------- sr_plan.legacy_actionable (old route's filter, unchanged)
s, rr = legacy_actionable([79.0, 80.0, 95.0, 105.0], [99.0, 104.0, 131.0], 100.0, 0.20, 0.30)
check('legacy filter: support in [80, 100), resistance in (100, 130]', s == [80.0, 95.0] and rr == [104.0])

# ---------------------------------------------------------------- the zone price is INSIDE is the nearest support, even when a lower zone's edge is nearer (Day 127, PLD)
# Zone B = three lows 109.0 / 109.45 / 109.9 (one zone, width 0.9); zone A = one low at 108.2 (its high is 0.8 below price, B's high is 0.9 above it).
def pld_shape(price):
    df = base()
    major_low(df, -40, 109.0)
    major_low(df, -55, 109.45)
    major_low(df, -70, 109.9)
    major_low(df, -85, 108.2)
    return run(df, price=price)

r = pld_shape(109.0)
zB = zone_at(r, 109.45)
zA = zone_at(r, 108.2)
check('PLD shape: two separate support zones exist, price inside the upper one', zA is not None and zB is not None and zA is not zB and zB['insideZone'] is True and zA['insideZone'] is False)
check('PLD shape: the zone price is inside is the nearest support (flag on it, not on the lower zone)', zB['nearest'] is True and zA['nearest'] is False)
check('PLD shape: support[0] is the inside zone high, and the list is sorted nearest first (descending)', r['support'][0] == zB['high'] and r['support'] == sorted(r['support'], reverse=True))
check('PLD shape: meta.zones lists the inside zone first (nearest first)', r['zones'][0] is zB or r['zones'][0]['low'] == zB['low'])
check('PLD shape: exactly one nearest per side', sum(1 for z in r['zones'] if z['nearest'] and z['side'] == 'support') == 1)
# price exactly at the inside zone's low and exactly at its high: still inside, still the nearest
for edge_price, label in ((109.0, 'low'), (109.9, 'high')):
    rr_ = pld_shape(edge_price)
    zb = zone_at(rr_, 109.45)
    check(f'price exactly at the inside zone {label}: still inside and nearest', zb['insideZone'] is True and zb['nearest'] is True)
# no inside zone: unchanged (nearest by edge distance)
r = pld_shape(110.6)
zb = zone_at(r, 109.45)
check('price above the zone (not inside): the nearest edge wins as before', zb['insideZone'] is False and zb['nearest'] is True)
# trade_plan's DEFAULT Buy is max(support), the inside zone high (the route now overrides it with the last close when that close is inside, see plan_entry)
check('Buy = max(support) = the inside zone high', trade_plan(r['support'], r['resistance'], r['atr'])['entry'] == round(max(r['support']), 2))
r = pld_shape(109.0)
check('Buy = max(support) = the nearest zone high when price is inside', trade_plan(r['support'], r['resistance'], r['atr'])['entry'] == r['support'][0])
# resistance side is untouched by an inside support zone
check('resistance flag/order unchanged when price is inside a support zone', all(z['side'] == 'support' or z['insideZone'] is False for z in r['zones']))

# ---------------------------------------------------------------- the Buy when the last COMPLETED close is already inside the nearest support zone (Day 127)
Z = [{'nearest': True, 'side': 'support', 'low': 125.38, 'high': 127.82, 'insideZone': True}, {'nearest': True, 'side': 'resistance', 'low': 131.85, 'high': 132.6, 'insideZone': False}]
check('close inside the nearest support zone: the Buy is that close', plan_entry(Z, 125.56) == (125.56, 'last_close_inside_zone'))
check('close exactly at the zone low and at its high: still inside', plan_entry(Z, 125.38)[1] == 'last_close_inside_zone' and plan_entry(Z, 127.82)[1] == 'last_close_inside_zone')
check('close above the zone (live price came down into it): no override, the zone high', plan_entry(Z, 128.9) == (None, 'zone_high'))
check('close below the zone (a gap up into it): no override, the zone high; the label never says "last close"', plan_entry(Z, 124.0) == (None, 'zone_high'))
check('a NaN or missing close falls back to the zone high', plan_entry(Z, float('nan')) == (None, 'zone_high') and plan_entry(Z, None) == (None, 'zone_high'))
check('no zones (legacy engine) or no nearest support zone: the default rule', plan_entry(None, 100.0) == (None, 'nearest_support') and plan_entry([], 100.0) == (None, 'nearest_support') and plan_entry([Z[1]], 100.0) == (None, 'nearest_support'))
p1 = trade_plan([127.82, 124.69], [131.85], atr=2.5, entry_override=125.56)
check('override: entry is the override, stop = entry - 2 ATR, target and R:R follow', p1['entry'] == 125.56 and p1['stop'] == 120.56 and p1['target'] == 131.85 and p1['riskReward'] == round((131.85 - 125.56) / 5.0, 2))
p2 = trade_plan([127.82, 124.69], [131.85], atr=2.5)
check('no override: unchanged (max(support), the zone high)', p2['entry'] == 127.82 and p2['stop'] == 122.82)
check('override without ATR: entry kept, no stop, no R:R (never a made-up number)', trade_plan([127.82], [131.85], None, entry_override=125.56)['stop'] is None)
check('the stop is always below the inside zone (zones are at most 1 ATR wide, the stop is 2 ATR under a close inside the zone)', p1['stop'] < 125.38 - 1.0)

print(f'\n{passed} checks passed')
