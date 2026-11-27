"""Tests for data_quality.price_freshness and the orchestrator's stale marker (Day 135, plan STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md).
Run: cd backend && venv/bin/python test_price_freshness.py"""
import os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data_quality as dq
from market_time import MARKET_TZ

passed = failed = 0
def ok(cond, name):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print('FAIL', name)

def frame(dates, closes=None):
    idx = pd.to_datetime(dates)
    return pd.DataFrame({'close': closes or [10.0] * len(idx)}, index=idx)

NOW = pd.Timestamp('2026-11-25 18:00', tz=MARKET_TZ)          # Wednesday evening, after the close
# current frame
r = dq.price_freshness(frame(['2026-11-24', '2026-11-25']), now=NOW)
ok(r['newestDate'] == '2026-11-25' and r['sessionsBehind'] == 0 and r['behindLevel'] == 'PASS' and not r['servedFromStaleCache'], 'current frame: 0 behind, PASS')
# one and two sessions behind are explained by a holiday: no warning level
r = dq.price_freshness(frame(['2026-11-23', '2026-11-24']), now=NOW)
ok(r['sessionsBehind'] == 1 and r['behindLevel'] == 'PASS', '1 behind: PASS (a holiday can explain it)')
r = dq.price_freshness(frame(['2026-11-20', '2026-11-23']), now=NOW)
ok(r['sessionsBehind'] == 2 and r['behindLevel'] == 'PASS', '2 behind: PASS (same rule as the tab)')
r = dq.price_freshness(frame(['2026-11-19', '2026-11-20']), now=NOW)
ok(r['sessionsBehind'] == 3 and r['behindLevel'] == 'WARN', '3 behind: WARN (the tab rule)')
r = dq.price_freshness(frame(['2026-11-10', '2026-11-11']), now=NOW)
ok(r['behindLevel'] == 'FAIL', '6+ behind: FAIL')
# stale flag travels through; a stale copy that is fully current still says its date
r = dq.price_freshness(frame(['2026-11-24', '2026-11-25']), served_stale=True, now=NOW)
ok(r['servedFromStaleCache'] and r['newestDate'] == '2026-11-25' and r['behindLevel'] == 'PASS', 'stale copy that is current: flag true, date fact kept')
# partial bar: copy written before the close of its own last bar's day
r = dq.price_freshness(frame(['2026-11-24']), served_stale=True, cached_at='2026-11-24T11:00:00-05:00', now=NOW)
ok(r['maybePartial'] is True, 'saved at 11:00 on the bar day: may hold a partial bar')
r = dq.price_freshness(frame(['2026-11-24']), served_stale=True, cached_at='2026-11-24T17:00:00-05:00', now=NOW)
ok(r['maybePartial'] is False, 'saved at 17:00 on the bar day: complete')
r = dq.price_freshness(frame(['2026-11-24']), served_stale=True, cached_at='2026-11-24T11:00:00', now=NOW)
ok(r['maybePartial'] is True, 'naive cached_at is read as New York time')
r = dq.price_freshness(frame(['2026-11-24']), served_stale=False, cached_at='2026-11-24T11:00:00-05:00', now=NOW)
ok(r['maybePartial'] is False, 'not stale: never partial')
# edge cases: never raises
for name, df in [('None', None), ('empty', frame([])), ('no close column', pd.DataFrame({'x': [1]}, index=pd.to_datetime(['2026-11-24']))),
                 ('all NaN', frame(['2026-11-24'], [np.nan])), ('one row', frame(['2026-11-25']))]:
    r = dq.price_freshness(df, now=NOW)
    ok(isinstance(r, dict) and 'newestDate' in r, f'{name}: returns a dict')
ok(dq.price_freshness(None, now=NOW)['newestDate'] is None, 'None frame: no date')
ok(dq.price_freshness(frame(['2026-11-24'], [np.nan]), now=NOW)['newestDate'] is None, 'all-NaN closes: no date')
# last valid close is used (empty newest row)
r = dq.price_freshness(frame(['2026-11-24', '2026-11-25'], [10.0, np.nan]), now=NOW)
ok(r['newestDate'] == '2026-11-24', 'an empty newest row does not count as a fresh bar')
# tz-aware index
tz = frame(['2026-11-25']); tz.index = tz.index.tz_localize('America/New_York')
ok(dq.price_freshness(tz, now=NOW)['newestDate'] == '2026-11-25', 'tz-aware index')
# Saturday: expected session is Friday
SAT = pd.Timestamp('2026-11-28 12:00', tz=MARKET_TZ)
ok(dq.price_freshness(frame(['2026-11-27']), now=SAT)['sessionsBehind'] == 0, 'Saturday: Friday bar is current')

# orchestrator: the stale marker rides on the frame, set inside the locked fetch
# Day 136: the orchestrator now writes an attempt record; keep it in a throwaway DB (never the live provider_state.db)
import tempfile as _tf
from providers import attempt_log as _al
_al.DB_PATH = os.path.join(_tf.mkdtemp(prefix='attempt_test_'), 'state.db'); _al._initialized = False
import providers.orchestrator as orch
class FakeCache:
    def get_cached_ohlcv(self, t, p=None): return None
    def read_ohlcv_entry(self, t):
        df = frame(['2026-11-21', '2026-11-24'])
        for c in ('open', 'high', 'low', 'volume'): df[c] = 1.0
        return df, {'period': '2y', 'rows': 600, 'source': 'yfinance', 'cached_at': '2026-11-24T18:00:00-05:00', 'expires_at': '2026-11-24T19:00:00-05:00', 'expired': True}
    def _period_to_min_rows(self, p): return 400
    OHLCV_ROW_TOLERANCE = 0.9
class Boom:
    name = 'yfinance'
    def get_ohlcv(self, t, p): raise orch.ProviderError('yfinance', 'Rate limit exceeded', t)
o = orch.DataProvider.__new__(orch.DataProvider)
import threading
o._ohlcv_locks, o._ohlcv_locks_guard, o._last_source, o._ohlcv_chain = {}, threading.Lock(), {}, [Boom()]
orch.cache_manager = FakeCache(); orch.CACHE_AVAILABLE = True
df = o.get_ohlcv('VFV.TO', '2y')
ok(df.attrs.get('served_from') == 'stale_cache' and df.attrs.get('cached_at') == '2026-11-24T18:00:00-05:00', 'orchestrator: stale frame carries the marker and cached_at')
ok(o._last_source['VFV.TO_ohlcv'] == 'stale_cache', 'orchestrator: _last_source still says stale_cache')
print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
