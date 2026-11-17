"""Day 126 price-basis plan tests. Run: cd backend && venv/bin/python test_price_basis.py
Cache hit rule, no short-over-long overwrite, Tradier TTL, per-ticker lock (one fetch for concurrent callers), Twelve Data daily request carries adjust=all."""
import os, sys, tempfile, threading, time
from datetime import datetime, timedelta
from unittest import mock
import numpy as np
import pandas as pd
import cache_manager as cm

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1; print(f'ok {m}')
    else: failed += 1; print(f'FAIL {m}')

def frame(n, end='2026-11-16'):
    idx = pd.bdate_range(end=end, periods=n)
    c = 100 + np.arange(n, dtype=float)
    return pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': 1000}, index=idx)

# an isolated cache database
tmp = tempfile.mkdtemp()
from pathlib import Path
cm.DB_PATH = Path(tmp) / 'cache.db'      # an isolated database; the real cache is never touched
for _n in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _n): getattr(cm, _n)(); break

# ---- row table
ok(cm._period_to_min_rows('2y') == 504 and cm._period_to_min_rows('1y') == 252 and cm._period_to_min_rows('6mo') == 126, 'period -> expected rows table unchanged')
ok(int(504 * cm.OHLCV_ROW_TOLERANCE) == 478 and int(252 * cm.OHLCV_ROW_TOLERANCE) == 239, '95% tolerance: 2y = 478 rows, 1y = 239 rows')

# ---- hit rule
cm.set_cached_ohlcv('TST1', frame(501), '2y', 'yfinance')
ok(cm.get_cached_ohlcv('TST1', '2y') is not None, 'a Yahoo-sized 2y entry (501 rows) is a HIT (was a miss: 501 < 504)')
cm.set_cached_ohlcv('TST2', frame(300), '2y', 'yfinance')
ok(cm.get_cached_ohlcv('TST2', '2y') is not None, 'a young fund fetched for 2y (300 rows) is a HIT: the stored period covers the request')
cm.set_cached_ohlcv('TST3', frame(251), '1y', 'yfinance')
ok(cm.get_cached_ohlcv('TST3', '2y') is None, 'Day-82 protection: a 1y entry (251 rows) is still a MISS for a 2y request')
ok(cm.get_cached_ohlcv('TST3', '1y') is not None, 'a 1y entry serves a 1y request')
ok(cm.get_cached_ohlcv('TST1', '1y') is not None, 'a 2y entry serves a 1y request (it covers it)')
ok(cm.get_cached_ohlcv('NOSUCH', '2y') is None, 'unknown ticker: miss')

# ---- a short fetch must not replace a fresh longer entry
cm.set_cached_ohlcv('TST1', frame(251), '1y', 'yfinance')
df, meta = cm.read_ohlcv_entry('TST1')
ok(meta['period'] == '2y' and len(df) == 501, 'a 1y write does NOT overwrite a fresh 2y entry')
cm.set_cached_ohlcv('TST3', frame(501), '2y', 'yfinance')
df, meta = cm.read_ohlcv_entry('TST3')
ok(meta['period'] == '2y' and len(df) == 501, 'a longer write DOES replace a shorter entry')

# ---- Tradier TTL
cm.set_cached_ohlcv('TST4', frame(501), '2y', 'tradier')
df, meta = cm.read_ohlcv_entry('TST4')
exp = datetime.fromisoformat(meta['expires_at']); now = datetime.now(exp.tzinfo)
ok(exp - now <= timedelta(minutes=cm.TRADIER_OHLCV_TTL_MIN + 1), f'a Tradier entry expires within {cm.TRADIER_OHLCV_TTL_MIN} minutes (not the end-of-day expiry)')
cm.set_cached_ohlcv('TST5', frame(501), '2y', 'twelvedata')
_, meta5 = cm.read_ohlcv_entry('TST5')
ok(datetime.fromisoformat(meta5['expires_at']) >= exp, 'other sources keep the normal expiry')

# ---- per-ticker lock: concurrent cold-cache callers cause ONE provider fetch
from providers import orchestrator as orch
calls = []
class FakeResult:
    def __init__(self, df): self.df, self.source, self.rows = df, 'twelvedata', len(df)
class FakeProv:
    name = 'twelvedata'
    def get_ohlcv(self, t, period):
        calls.append(t); time.sleep(0.3); return FakeResult(frame(504))
dp = orch.DataProvider.__new__(orch.DataProvider)
dp._ohlcv_locks = {}; dp._ohlcv_locks_guard = threading.Lock(); dp._last_source = {}; dp._ohlcv_chain = [FakeProv()]
dp._deliver = lambda t, df: df
out = []
ths = [threading.Thread(target=lambda: out.append(dp.get_ohlcv('LOCKT', '2y'))) for _ in range(5)]
[t.start() for t in ths]; [t.join() for t in ths]
ok(len(out) == 5 and all(len(o) == 504 for o in out), 'five concurrent callers all get a frame')
ok(len(calls) == 1, f'five concurrent cold-cache callers cause ONE provider fetch (got {len(calls)})')
calls.clear(); dp.get_ohlcv('LOCKT', '2y')
ok(len(calls) == 0, 'the next caller is a cache hit (no provider call)')
calls.clear(); dp.get_ohlcv('LOCKT', '1y')
ok(len(calls) == 0, 'a 1y request after a 2y fetch is served from the cache')

# ---- Twelve Data: the daily request asks for adjust=all, the intraday one does not
from providers.twelvedata_provider import TwelveDataProvider
seen = []
class FakeResp:
    status_code = 200
    def raise_for_status(self): pass
    def json(self): return {'status': 'ok', 'values': [{'datetime': '2026-11-16', 'open': '1', 'high': '2', 'low': '1', 'close': '1.5', 'volume': '10'}], 'meta': {}}
def fake_get(url, params=None, timeout=None): seen.append(dict(params)); return FakeResp()
tdp = TwelveDataProvider(); tdp.api_key = 'x'
with mock.patch('requests.get', fake_get):
    try: tdp._fetch_time_series('DUK', '1day', 504)
    except Exception as e: print('  (daily parse not needed here)', type(e).__name__)
    try: tdp._fetch_time_series('DUK', '1h', 420)
    except Exception as e: pass
ok(seen and seen[0].get('adjust') == 'all', 'the daily Twelve Data request carries adjust=all')
ok(len(seen) > 1 and 'adjust' not in seen[1], 'the intraday request does not (not part of this change)')

# ---- stale fallback must not hand a short entry to a longer request (universe run: 51 of 117 stock responses were 1y frames)
from providers.exceptions import ProviderError
class FailProv:
    name = 'twelvedata'
    def get_ohlcv(self, t, period): raise ProviderError('twelvedata', 'rate limited', t)
cm.set_cached_ohlcv('STALE1', frame(251), '1y', 'yfinance')
dp2 = orch.DataProvider.__new__(orch.DataProvider)
dp2._ohlcv_locks = {}; dp2._ohlcv_locks_guard = threading.Lock(); dp2._last_source = {}; dp2._ohlcv_chain = [FailProv()]; dp2._deliver = lambda t, df: df
try:
    dp2.get_ohlcv('STALE1', '2y'); served = True
except ProviderError:
    served = False
ok(not served, 'all providers fail for a 2y request: a short 1y cache entry is NOT served as the stale fallback (an explicit error instead)')
ok(len(dp2.get_ohlcv('STALE1', '1y')) == 251, 'the same short entry still serves a 1y request')
cm.set_cached_ohlcv('STALE2', frame(501), '2y', 'yfinance')
ok(len(dp2.get_ohlcv('STALE2', '2y')) == 501, 'a full 2y entry is served normally')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
