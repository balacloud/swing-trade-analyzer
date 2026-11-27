"""Real forced state for the Data Sources tab backend (Day 136, plan DATA_SOURCES_PROVENANCE_PLAN_DAY136.md Part D).
Flask test_client with EVERY database redirected to a throwaway folder (cache, breaker, limiter, attempt log): the live app on
port 5001 and its files are never touched. Run: cd backend && venv/bin/python test_provenance_route.py"""
import io, os, sys, tempfile, threading
from contextlib import redirect_stdout
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cache_manager as cm
from providers import attempt_log, circuit_breaker, rate_limiter, orchestrator as orch
from providers.exceptions import ProviderError

tmp = tempfile.mkdtemp(prefix='prov_route_test_')
state_db = os.path.join(tmp, 'state.db')
LIVE = circuit_breaker.DB_PATH
for mod in (attempt_log, circuit_breaker, rate_limiter):
    mod.DB_PATH = state_db; mod._initialized = False
circuit_breaker._breakers.clear(); rate_limiter._limiters.clear()
assert circuit_breaker.DB_PATH != LIVE and attempt_log.DB_PATH != LIVE
cm.DB_PATH = Path(tmp) / 'cache.db'
for _n in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _n): getattr(cm, _n)(); break

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1
    else:
        failed += 1; print(f'FAIL {m}')

def quiet(fn, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf): out = fn(*a, **k)
    return out

import backend   # imported AFTER the redirects: its module-level singletons then use the throwaway files
client = backend.app.test_client()
prov = lambda t: client.get(f'/api/provenance/{t}').get_json()

def frame(n=504, end='2026-11-19'):
    idx = pd.bdate_range(end=end, periods=n); c = 100 + np.arange(n, dtype=float)
    return pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': 1000}, index=idx)

class Down:
    name = 'twelvedata'
    def get_ohlcv(self, t, period): raise ProviderError('twelvedata', 'HTTP 429 https://x/?apikey=SECRETKEY123', t)
class Up:
    name = 'yfinance'
    def get_ohlcv(self, t, period):
        class R: pass
        r = R(); r.df, r.source, r.rows = frame(), 'yfinance', 504; return r
def make(*provs):
    dp = orch.DataProvider.__new__(orch.DataProvider)
    dp._ohlcv_locks = {}; dp._ohlcv_locks_guard = threading.Lock(); dp._last_source = {}
    dp._ohlcv_chain = list(provs); dp._deliver = lambda t, df: df
    return dp

# never seen
d = prov('FORCE1')
ok(d['ohlcv']['attempt']['state'] == 'never' and d['fundamentals']['attempt']['state'] == 'never', 'unknown ticker: attempt = never for both data types')
ok(d['quality']['state'] == 'not_cached' and d['ohlcv']['status'] == 'live', 'unknown ticker: nothing cached, frozen keys unchanged')

# a real failed fetch through the real orchestrator code, no saved copy
try: quiet(make(Down()).get_ohlcv, 'FORCE1', '2y')
except ProviderError: pass
d = prov('FORCE1')
a = d['ohlcv']['attempt']
ok(a['state'] == 'failed' and a['detail'] == 'twelvedata:ProviderError' and not a['served_stale'] and a['last_ok_ts'] is None, 'failed fetch: route says failed with the provider and error CLASS')
ok('SECRETKEY' not in str(d) and 'apikey' not in str(d), 'no key text anywhere in the provenance answer')
ok(d['quality']['state'] == 'not_cached', 'failed fetch with no data: still not cached (a failure never invents data)')

# then a real success: failed -> ok, and the cache is filled
quiet(make(Down(), Up()).get_ohlcv, 'FORCE1', '2y')
d = prov('FORCE1')
ok(d['ohlcv']['attempt']['state'] == 'ok' and d['ohlcv']['attempt']['last_ok_provider'] == 'yfinance' and d['ohlcv']['source'] == 'yfinance', 'later success: ok from yfinance, cache source agrees')
ok(d['ohlcv']['attempt']['last_fail_ts'] is not None, 'the earlier failure time is still kept')

# expired cache + every provider down = served stale
c = __import__('sqlite3').connect(str(cm.DB_PATH)); c.execute("update ohlcv_cache set expires_at = '2000-01-01T00:00:00-05:00' where ticker='FORCE1'"); c.commit(); c.close()
quiet(make(Down()).get_ohlcv, 'FORCE1', '2y')
a = prov('FORCE1')['ohlcv']['attempt']
ok(a['state'] == 'failed' and a['served_stale'] is True and a['last_ok_ts'], 'expired cache served after a failure: failed + served_stale + the last success kept')

# a real tripped breaker shows in /api/health (this test's own state file)
circuit_breaker.get_breaker('twelvedata').trip()
h = client.get('/api/health').get_json()['providers']['providers']['twelvedata']
ok(h['health'] == 'open', 'breaker tripped in the throwaway state file: /api/health says open')
circuit_breaker.get_breaker('twelvedata').reset()
ok(client.get('/api/health').get_json()['providers']['providers']['twelvedata']['health'] == 'ok', 'reset: back to ok')

# the live files were not touched
import sqlite3
if os.path.exists(LIVE):
    c = sqlite3.connect(LIVE)
    has = c.execute("select count(*) from sqlite_master where name='fetch_attempts'").fetchone()[0]
    leaked = c.execute("select count(*) from fetch_attempts where ticker='FORCE1'").fetchone()[0] if has else 0
    c.close()
    ok(leaked == 0, 'the live provider_state.db has no FORCE1 row')

print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
