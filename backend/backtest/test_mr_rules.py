"""
MR rule checks (Day 123, Analyze redesign Step 5).

1. mean_reversion.MR_RULES equals the frozen copies in mr_simulator and
   daily_job (one rule; the frozen code keeps its own literals).
2. detect_mr_signal: signal / no signal / missing inputs reported as None,
   never read as a fail; no stop/target/atr in the output.
3. market_time.drop_forming_bar before/after the 16:05 ET cutoff.

Run: cd backend && venv/bin/python backtest/test_mr_rules.py
"""
import inspect
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

import mean_reversion as mr
from market_time import MARKET_TZ, drop_forming_bar, is_forming_bar
from backtest import mr_simulator
from paper_trading import daily_job

passed = 0


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


# 1. Rule parity with frozen code
sig = inspect.signature(mr_simulator.simulate_mr_trade).parameters
check('stop_pct == simulator default', sig['stop_pct'].default == mr.MR_RULES['stop_pct'])
check('max_days == simulator default', sig['max_days'].default == mr.MR_RULES['max_hold_days'])
check('stop_pct == daily_job', daily_job.MR_STOP_PCT == mr.MR_RULES['stop_pct'])
check('max_days == daily_job', daily_job.MR_MAX_DAYS == mr.MR_RULES['max_hold_days'])
check('rsi2 exit literal == 70 in simulator', f"bar_rsi2 > {mr.MR_RULES['rsi2_exit']}" in inspect.getsource(mr_simulator.simulate_mr_trade))
check('cooldown == backtest default', inspect.signature(mr_simulator.backtest_mr_strategy).parameters['cooldown'].default == mr.MR_RULES['cooldown_days'])


# 2. detect_mr_signal
def frame(closes, volume=5_000_000):
    idx = pd.bdate_range('2025-01-01', periods=len(closes))
    c = pd.Series(closes, index=idx, dtype=float)
    return pd.DataFrame({'Open': c, 'High': c * 1.01, 'Low': c * 0.99, 'Close': c,
                         'Volume': pd.Series(volume, index=idx, dtype=float)})

up = list(np.linspace(50, 100, 250))
dip = up[:-2] + [96.0, 92.0]                      # sharp 2-day drop, still above the 200-day
r = mr.detect_mr_signal(frame(dip))
check('dip in uptrend -> signal', r['signal'] is True and r['rsi2'] < 10 and not r['missing'])
check('no stop/target/atr keys', not ({'stop', 'target', 'atr'} & set(r)))
check('rules attached', r['rules'] == mr.MR_RULES)
check('pct_above_sma200 positive', r['pct_above_sma200'] > 0)

r = mr.detect_mr_signal(frame(up))
check('steady rise -> no signal (RSI2 high)', r['signal'] is False and r['conditions']['rsi2_oversold'] is False)

df = frame(dip)
df.loc[df.index[-5:], 'Volume'] = np.nan
r = mr.detect_mr_signal(df)
check('NaN volume -> None condition, listed missing, no signal',
      r['conditions']['volume_filter'] is None and 'volume_filter' in r['missing'] and r['signal'] is False)

flat = [100.0] * 250
r = mr.detect_mr_signal(frame(flat))
check('flat closes -> RSI2 missing, not a fail', r['conditions']['rsi2_oversold'] is None and r['rsi2'] is None)

r = mr.detect_mr_signal(frame(dip[:150]))
check('<200 bars -> reason + bars', r['signal'] is False and r['bars'] == 150)

r = mr.detect_mr_signal(frame(dip, volume=100_000))  # ~$9M/day
check('thin trading -> volume rule fails', r['conditions']['volume_filter'] is False and r['signal'] is False)

# 3. forming bar
today = datetime(2026, 11, 11, 11, 0, tzinfo=MARKET_TZ)
after = datetime(2026, 11, 11, 16, 31, tzinfo=MARKET_TZ)
cached = datetime(2026, 11, 11, 16, 20, tzinfo=MARKET_TZ)
check('today 11:00 ET is forming', is_forming_bar('2026-11-11', now=today))
check('today 16:31 ET is complete', not is_forming_bar('2026-11-11', now=after))
check('today 16:20 ET still forming (cache window)', is_forming_bar('2026-11-11', now=cached))
check('yesterday never forming', not is_forming_bar('2026-11-10', now=today))
idx = pd.to_datetime(['2026-11-09', '2026-11-10', '2026-11-11'])
d = pd.DataFrame({'Close': [1, 2, 3]}, index=idx)
out, dropped = drop_forming_bar(d, now=today)
check('drop_forming_bar drops today intraday', dropped and len(out) == 2 and len(d) == 3)
out, dropped = drop_forming_bar(d, now=after)
check('drop_forming_bar keeps today after close', not dropped and len(out) == 3)

print(f"\n{passed} checks passed")
