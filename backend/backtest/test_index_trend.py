"""
Checks for index_trend.index_trend_facts (Day 124, redesign Step 7 — Market backdrop card).
Run: cd backend && venv/bin/python backtest/test_index_trend.py
"""
import os
import sys
from datetime import datetime

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from index_trend import index_trend_facts
from market_time import MARKET_TZ

passed = 0


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


def frame(closes, end='2026-11-11'):
    idx = pd.bdate_range(end=end, periods=len(closes))
    return pd.DataFrame({'Close': closes}, index=idx)


AFTER_CLOSE = datetime(2026, 11, 11, 18, 0, tzinfo=MARKET_TZ)   # Nov 11 bar is complete
INTRADAY = datetime(2026, 11, 11, 11, 0, tzinfo=MARKET_TZ)      # Nov 11 bar is still forming

# --- SMAs, distances, as-of ---------------------------------------------------
closes = [100.0] * 199 + [110.0]
f = index_trend_facts(frame(closes), now=AFTER_CLOSE)
check('as-of is the last completed bar', f['asOfDate'] == '2026-11-11')
check('close is the last completed close', f['close'] == 110.0)
check('sma50 exact (2 dp)', f['sma50'] == round((100 * 49 + 110) / 50, 2))
check('sma200 exact (2 dp)', f['sma200'] == round((100 * 199 + 110) / 200, 2))
check('above both', f['aboveSma50'] is True and f['aboveSma200'] is True)
check('pctVsSma50 1 decimal', f['pctVsSma50'] == round((110 / f['sma50'] - 1) * 100, 1))

# --- short history -> nulls, never a fake number -------------------------------
f = index_trend_facts(frame([100.0] * 40), now=AFTER_CLOSE)
check('<50 bars: sma50 / aboveSma50 / pct null', f['sma50'] is None and f['aboveSma50'] is None and f['pctVsSma50'] is None)
check('<200 bars: sma200 null', f['sma200'] is None and f['aboveSma200'] is None and f['pctVsSma200'] is None)
f = index_trend_facts(frame([100.0] * 10), now=AFTER_CLOSE)
check('<11 bars: biggestDrop10d null', f['biggestDrop10d'] is None and f['biggestDrop10dSince'] is None)

# --- forming bar is dropped ----------------------------------------------------
closes = [100.0] * 250 + [50.0]   # a -50% "bar" that is only today's partial
f = index_trend_facts(frame(closes), now=INTRADAY)
check('intraday: forming bar dropped from as-of', f['asOfDate'] == '2026-11-10')
check('intraday: forming bar not counted as a drop', f['biggestDrop10d'] == {'noDownDay': True})
f = index_trend_facts(frame(closes), now=AFTER_CLOSE)
check('after 16:30: same bar counts', f['asOfDate'] == '2026-11-11' and f['biggestDrop10d']['pct'] == -50.0)

# --- biggest drop in the last 10 completed sessions ----------------------------
up = [100.0 + i for i in range(300)]
f = index_trend_facts(frame(up), now=AFTER_CLOSE)
check('no down day -> noDownDay', f['biggestDrop10d'] == {'noDownDay': True} and f['biggestDrop10dSince'] is None)

closes = [100.0] * 296 + [95.0, 95.0, 90.25, 90.25]   # -5% on bar -4, -5% on bar -2: tie
df = frame(closes)
f = index_trend_facts(df, now=AFTER_CLOSE)
check('tie: most recent of equal drops wins', f['biggestDrop10d']['date'] == str(df.index[-2].date()))
check('tie: drop pct', f['biggestDrop10d']['pct'] == -5.0)
check('tie: since = the earlier equal drop (strictly before)', f['biggestDrop10dSince'] == str(df.index[-4].date()))

# --- "since" searches the full frame, strictly before the drop ------------------
closes = [100.0] * 500
closes[20] = 90.0      # -10% very early (outside a 260-bar tail)
closes[21] = 100.0
closes[-3] = 93.0      # -7% recently
df = frame(closes)
f = index_trend_facts(df, now=AFTER_CLOSE)
check('recent drop found', f['biggestDrop10d'] == {'date': str(df.index[-3].date()), 'pct': -7.0})
check('since searches beyond 260 bars', f['biggestDrop10dSince'] == str(df.index[20].date()))

closes = [100.0] * 500
closes[-3] = 93.0
f = index_trend_facts(frame(closes), now=AFTER_CLOSE)
check('nothing larger before -> since null', f['biggestDrop10dSince'] is None)
check('searchedFrom = first date with a 1-day change (the span actually searched)',
      f['searchedFrom'] == str(frame(closes).index[1].date()))

# --- a NaN close mid-series must not turn a 2-session move into a "1-day drop" ----
closes = [100.0] * 300
closes[-5] = float('nan')
closes[-4] = 90.0      # 100 -> NaN -> 90: no single-day change is known here
closes[-3] = 90.0
closes[-2] = 90.0
closes[-1] = 90.0
f = index_trend_facts(frame(closes), now=AFTER_CLOSE)
check('NaN gap: no fake -10% one-day drop', f['biggestDrop10d'] == {'noDownDay': True})
check('NaN gap: reported', f['nanCloses'] == 1)

# --- SMAs are rounded for the payload ---------------------------------------------
f = index_trend_facts(frame([100.0] * 199 + [110.0]), now=AFTER_CLOSE)
check('sma50 rounded to 2 dp', f['sma50'] == round(f['sma50'], 2))

# --- bad input -----------------------------------------------------------------
check('None frame -> None', index_trend_facts(None, now=AFTER_CLOSE) is None)
check('empty frame -> None', index_trend_facts(frame([]), now=AFTER_CLOSE) is None)
nan_closes = [100.0] * 260
nan_closes[-1] = float('nan')
f = index_trend_facts(frame(nan_closes), now=AFTER_CLOSE)
check('NaN closes are dropped, not propagated', f['close'] == 100.0)

print(f'\n{passed} checks passed')
