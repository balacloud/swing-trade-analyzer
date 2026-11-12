"""
Checks for breakout_detection.detect_breakout — simple trader-consensus rules (Day 125).
Plan: docs/claude/design/ANALYZE_CLEANUP_PLAN_DAY125.md §7.1.
Run: cd backend && venv/bin/python backtest/test_breakout_rules.py
"""
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from breakout_detection import detect_breakout, prepare_breakout_frame, MIN_BARS
from market_time import MARKET_TZ

passed = 0


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


def frame(n=120, base=100.0, vol=1_000_000, end='2026-11-11'):
    """Flat base: every bar high=base, low=base-2, close=base-1, volume=vol."""
    idx = pd.bdate_range(end=end, periods=n)
    return pd.DataFrame({
        'open': [base - 1.0] * n,
        'high': [base] * n,
        'low': [base - 2.0] * n,
        'close': [base - 1.0] * n,
        'volume': [float(vol)] * n,
    }, index=idx)


def set_bar(df, pos, close, high=None, low=None, volume=None):
    """Set bar at position `pos` (negative = from the end)."""
    i = df.index[pos]
    df.loc[i, 'close'] = close
    df.loc[i, 'open'] = close
    df.loc[i, 'high'] = high if high is not None else close
    df.loc[i, 'low'] = low if low is not None else close
    if volume is not None:
        df.loc[i, 'volume'] = float(volume)


# P (pivot) = highest high of bars t-69 .. t-10 = 100.0 in the flat base.

# --- NOT_READY / WATCH -----------------------------------------------------------
df = frame()
for k in range(1, 11):
    set_bar(df, -k, 90.0, high=91.0, low=89.0)
r = detect_breakout(df)
check('far below the ceiling -> NOT_READY', r['status'] == 'NOT_READY')
check('pivot is the 60-day ceiling before the last 10 days', r['breakoutLevel'] == 100.0)
check('no breakout -> no breakout date', r['breakoutDate'] is None)

df = frame()
r = detect_breakout(df)
check('close 1% under the ceiling -> BREAKOUT_WATCH', r['status'] == 'BREAKOUT_WATCH')
df = frame()
for k in range(1, 11):
    set_bar(df, -k, 96.9, high=97.0, low=96.0)
check('close 3.1% under -> NOT_READY', detect_breakout(df)['status'] == 'NOT_READY')
df = frame()
for k in range(1, 11):
    set_bar(df, -k, 97.0, high=97.5, low=96.0)
check('close exactly 3% under -> BREAKOUT_WATCH', detect_breakout(df)['status'] == 'BREAKOUT_WATCH')

# --- CONFIRMED / LIGHT_VOLUME (breakout today) -------------------------------------
df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=1_600_000)
r = detect_breakout(df)
check('close above on 1.6x volume -> BREAKOUT_CONFIRMED', r['status'] == 'BREAKOUT_CONFIRMED')
check('rvol measured on the breakout bar', r['rvol'] == 1.6)
check('breakout date is the last bar', r['breakoutDate'] == '2026-11-11')
check('breakout age 0', r['breakoutAge'] == 0)

df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=1_400_000)
r = detect_breakout(df)
check('close above on 1.4x volume -> BREAKOUT_LIGHT_VOLUME', r['status'] == 'BREAKOUT_LIGHT_VOLUME')
check('light volume action says not confirmed', 'not confirmed' in r['humanAction'].lower())

df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=1_500_000)
check('exactly 1.5x -> confirmed', detect_breakout(df)['status'] == 'BREAKOUT_CONFIRMED')

# --- volume is judged on the breakout bar, not today (Fable #6) ---------------------
df = frame()
set_bar(df, -4, 102.0, high=102.5, low=101.0, volume=2_000_000)   # breakout 3 bars ago, heavy
for k in (1, 2, 3):
    set_bar(df, -k, 103.0, high=103.5, low=102.0, volume=500_000)  # quiet days since
r = detect_breakout(df)
check('heavy breakout bar + quiet days since -> still CONFIRMED', r['status'] == 'BREAKOUT_CONFIRMED')
check('rvol is the breakout bar\'s (2.0)', r['rvol'] == 2.0)
check('breakout age 3', r['breakoutAge'] == 3)
check('pivot does not drift with the breakout bars (Fable #5)', r['breakoutLevel'] == 100.0)

# --- day after a healthy breakout is NOT "failed" (Fable #5) ------------------------
df = frame()
set_bar(df, -2, 104.0, high=104.5, low=101.0, volume=2_000_000)
set_bar(df, -1, 103.5, high=104.0, low=102.5, volume=900_000)
check('day after breakout, still above P -> CONFIRMED (not FAILED)',
      detect_breakout(df)['status'] == 'BREAKOUT_CONFIRMED')

# --- FAILED -------------------------------------------------------------------------
df = frame()
set_bar(df, -3, 102.0, high=102.5, low=101.0, volume=2_000_000)
set_bar(df, -1, 99.0, high=100.5, low=98.5)
r = detect_breakout(df)
check('broke out, now closed below P -> FAILED_BREAKOUT', r['status'] == 'FAILED_BREAKOUT')

# --- EXTENDED -----------------------------------------------------------------------
df = frame()
set_bar(df, -2, 103.0, high=103.5, low=101.0, volume=2_000_000)
set_bar(df, -1, 105.5, high=106.0, low=104.0)
check('more than 5% above P -> EXTENDED_CHASE_RISK', detect_breakout(df)['status'] == 'EXTENDED_CHASE_RISK')
df = frame()
set_bar(df, -1, 105.0, high=105.0, low=99.5, volume=2_000_000)
check('exactly 5% above on heavy volume -> CONFIRMED', detect_breakout(df)['status'] == 'BREAKOUT_CONFIRMED')
df = frame()
set_bar(df, -1, 106.0, high=106.0, low=99.5, volume=3_000_000)
check('breakout day itself 6% above -> EXTENDED (priority over confirmed)',
      detect_breakout(df)['status'] == 'EXTENDED_CHASE_RISK')

# --- RETEST -------------------------------------------------------------------------
df = frame()
set_bar(df, -3, 103.0, high=103.5, low=101.0, volume=2_000_000)
set_bar(df, -2, 104.0, high=104.5, low=103.0)
set_bar(df, -1, 101.5, high=102.0, low=100.8)   # low within 1% of P, close above P
check('pulled back to within 1% of P, closed above -> RETEST_ENTRY', detect_breakout(df)['status'] == 'RETEST_ENTRY')
df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=2_000_000)
check('breakout day low below P is not a retest (age 0)', detect_breakout(df)['status'] == 'BREAKOUT_CONFIRMED')

# --- the episode ends when the breakout leaves the 10-day window --------------------
df = frame()
set_bar(df, -11, 102.0, high=102.5, low=101.0, volume=2_000_000)  # 10 bars before t
r = detect_breakout(df)
check('breakout 10+ days ago is part of the new ceiling', r['breakoutLevel'] == 102.5)
check('old breakout no longer an episode -> judged fresh vs new P (99 is 3.4% under 102.5)', r['status'] == 'NOT_READY')
check('old breakout -> no breakout date', r['breakoutDate'] is None)

# --- volume unknown -----------------------------------------------------------------
df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=3_000_000)
for k in range(2, 31):
    df.loc[df.index[-k], 'volume'] = np.nan          # only 21 of the 50 prior volumes known
r = detect_breakout(df)
check('fewer than 40 known volumes before the breakout -> rvol None', r['rvol'] is None)
check('unknown volume never confirms -> LIGHT_VOLUME', r['status'] == 'BREAKOUT_LIGHT_VOLUME')
check('unknown volume is said, not hidden', 'volume unknown' in r['humanAction'].lower())

df = frame()
set_bar(df, -1, 102.0, high=102.5, low=99.0, volume=2_000_000)
df.loc[df.index[-1], 'volume'] = np.nan
r = detect_breakout(df)
check('NaN breakout-bar volume -> rvol None, LIGHT_VOLUME', r['rvol'] is None and r['status'] == 'BREAKOUT_LIGHT_VOLUME')

# --- bad input ----------------------------------------------------------------------
try:
    detect_breakout(frame(n=MIN_BARS - 1))
    check('too little history raises', False)
except ValueError:
    check('too little history raises ValueError', True)
try:
    detect_breakout(None)
    check('None raises', False)
except ValueError:
    check('None raises ValueError', True)

df = frame()
df.loc[df.index[-1], 'close'] = np.nan
r = detect_breakout(df)
check('NaN last close is dropped, previous bar used', r['asOfDate'] == '2026-11-10')

# --- output fields ------------------------------------------------------------------
df = frame()
r = detect_breakout(df)
check('as-of is the last bar used', r['asOfDate'] == '2026-11-11')
check('no unread high60 field (Fable code review #6)', 'high60' not in r)
check('pctFromLevel signed', r['pctFromLevel'] == -1.0)
for gone in ('checks', 'warnings', 'evidence', 'supportLevel', 'invalidation'):
    check(f'old field {gone} removed', gone not in r)

# --- forming bar dropped (Fable #10) ------------------------------------------------
INTRADAY = datetime(2026, 11, 11, 11, 0, tzinfo=MARKET_TZ)
AFTER_CLOSE = datetime(2026, 11, 11, 18, 0, tzinfo=MARKET_TZ)
raw = frame().rename(columns=str.capitalize)
f, dropped = prepare_breakout_frame(raw, now=INTRADAY)
check('intraday: today\'s bar dropped', dropped and str(f.index[-1])[:10] == '2026-11-10')
check('columns normalized to lowercase', list(f.columns) == ['open', 'high', 'low', 'close', 'volume'])
f, dropped = prepare_breakout_frame(raw, now=AFTER_CLOSE)
check('after 16:30 ET: bar kept', not dropped and str(f.index[-1])[:10] == '2026-11-11')

# --- steady climber (Fable #15): every close is a new high -> extended or confirmed, stated
df = frame()
for k in range(10, 0, -1):
    c = 100.0 + (11 - k) * 1.0
    set_bar(df, -k, c, high=c + 0.2, low=c - 0.5, volume=1_000_000)
r = detect_breakout(df)
check('steady climber 10% above P -> EXTENDED (documented)', r['status'] == 'EXTENDED_CHASE_RISK')

print(f'\n{passed} checks passed')
