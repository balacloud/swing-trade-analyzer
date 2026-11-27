"""Tests for the attempt log (Day 136, plan DATA_SOURCES_PROVENANCE_PLAN_DAY136.md).
Everything runs on throwaway databases: the live provider_state.db and the live cache are never touched.
Run: cd backend && venv/bin/python test_attempt_log.py"""
import glob, io, os, re, sys, tempfile, threading
from contextlib import redirect_stdout
from pathlib import Path
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cache_manager as cm
from providers import attempt_log as al
from providers import orchestrator as orch
from providers.base import FUNDAMENTALS_SCHEMA
from providers.exceptions import ProviderError, RateLimitError

REAL_DB = al.DB_PATH
passed = failed = 0
def ok(cond, msg):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print(f'FAIL {msg}')

def quiet(fn, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf): out = fn(*a, **k)
    return out, buf.getvalue()

_n = 0
def fresh_db():
    global _n; _n += 1
    d = tempfile.mkdtemp(prefix='attempt_log_test_')
    al.DB_PATH = os.path.join(d, f'state_{_n}.db'); al._initialized = False
    assert al.DB_PATH != REAL_DB
    return al.DB_PATH

cm.DB_PATH = Path(tempfile.mkdtemp()) / 'cache.db'
for _name in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _name): getattr(cm, _name)(); break

# ---- basic states
fresh_db()
ok(al.read('AAPL', 'ohlcv')['state'] == 'never', 'no row = never')
ok(al.read('', 'ohlcv')['state'] == 'never' and al.read(None, 'ohlcv')['state'] == 'never', 'empty / None ticker = never, no crash')
al.record_ok('aapl', 'ohlcv', 'alpaca', '2y')
r = al.read('AAPL', 'ohlcv')
ok(r['state'] == 'ok' and r['last_ok_provider'] == 'alpaca' and r['period'] == '2y' and r['last_ok_ts'], 'ok recorded, ticker upper-cased')
ok(al.read('AAPL', 'fundamentals')['state'] == 'never', 'data types are separate rows')
al.record_fail('AAPL', 'ohlcv', 'alpaca:RateLimitError; yfinance:ProviderError', '2y')
r = al.read('AAPL', 'ohlcv')
ok(r['state'] == 'failed' and 'alpaca:RateLimitError' in r['detail'] and r['last_ok_ts'], 'ok then fail = failed, last ok kept')
ok(r['served_stale'] is False, 'plain failure is not "served stale"')
al.record_fail('AAPL', 'ohlcv', 'alpaca:X', '2y', served_stale=True)
ok(al.read('AAPL', 'ohlcv')['served_stale'] is True, 'stale served flag set')
al.record_ok('AAPL', 'ohlcv', 'yfinance', '2y')
r = al.read('AAPL', 'ohlcv')
ok(r['state'] == 'ok' and r['served_stale'] is False and r['last_ok_provider'] == 'yfinance', 'a later success clears served_stale and flips to ok')
al.record_fail('NEWT', 'ohlcv', 'twelvedata:ProviderError')
r = al.read('NEWT', 'ohlcv')
ok(r['state'] == 'failed' and r['last_ok_ts'] is None, 'fail with no earlier success = failed, no last ok')
al.record_ok('VFV.TO', 'ohlcv', 'yfinance', '1y')
ok(al.read('vfv.to', 'ohlcv')['state'] == 'ok', 'Canadian suffix works')

# ---- one row per (ticker, type): upsert, no growth
import sqlite3
for _ in range(20): al.record_ok('AAPL', 'ohlcv', 'alpaca', '2y')
c = sqlite3.connect(al.DB_PATH); cnt = c.execute("select count(*) from fetch_attempts where ticker='AAPL'").fetchone()[0]; c.close()
ok(cnt == 1, '20 writes, one row')

# ---- never raises, never leaks
bad = os.path.join(tempfile.mkdtemp(), 'afile')
open(bad, 'w').write('not a directory')
al.DB_PATH = os.path.join(bad, 'sub', 'state.db'); al._initialized = False       # parent is a file: every open fails
(res, out) = quiet(al.record_ok, 'AAPL', 'ohlcv', 'alpaca')
ok(res is False and 'attempt_log record_ok failed for AAPL' in out, 'unwritable DB: returns False, prints one line with the ticker, no exception')
corrupt = os.path.join(tempfile.mkdtemp(), 'corrupt.db'); open(corrupt, 'w').write('this is not a sqlite database' * 50)
al.DB_PATH = corrupt; al._initialized = False
(r, out) = quiet(al.read, 'AAPL', 'ohlcv')
ok(r['state'] == 'never' and r['error'], 'unreadable (corrupt) DB: state never BUT error is set (unreadable is not the same as never fetched)')
fresh_db()
exc = ProviderError('twelvedata', 'HTTPError 429 for url https://api.x/?apikey=SECRETKEY123', 'AAPL')
d = al.describe_error(exc.provider, exc)
ok(d == 'twelvedata:ProviderError' and 'SECRETKEY' not in d and 'apikey' not in d, 'describe_error: provider + class only, no message text')
ok(al.describe_error('we ird/prov;ider', RateLimitError('x', 'y')) == 'weirdprovider:RateLimitError', 'odd characters stripped from names')
al.record_fail('AAPL', 'ohlcv', 'x' * 1000)
ok(len(al.read('AAPL', 'ohlcv')['detail']) <= al.DETAIL_MAX_CHARS, 'detail length capped')
# a held write lock must not stall the caller (short timeout)
import time
fresh_db(); al.record_ok('AAPL', 'ohlcv', 'alpaca')
blocker = sqlite3.connect(al.DB_PATH, timeout=5); blocker.execute('BEGIN EXCLUSIVE')
t0 = time.time(); (res, _) = quiet(al.record_ok, 'AAPL', 'ohlcv', 'alpaca'); dt = time.time() - t0
blocker.rollback(); blocker.close()
ok(res is False and dt < 2.0, f'locked DB: gives up in under 2 s ({dt:.2f}s), no exception')

# ---- two threads
fresh_db()
ths = [threading.Thread(target=lambda i=i: al.record_ok(f'T{i % 3}', 'ohlcv', 'alpaca')) for i in range(30)]
[t.start() for t in ths]; [t.join() for t in ths]
c = sqlite3.connect(al.DB_PATH); cnt = c.execute('select count(*) from fetch_attempts').fetchone()[0]; c.close()
ok(cnt == 3, f'30 concurrent writers on 3 tickers: 3 rows ({cnt})')

# ---- orchestrator integration (fake providers)
def frame(n=504, end='2026-11-19'):
    idx = pd.bdate_range(end=end, periods=n); c = 100 + np.arange(n, dtype=float)
    return pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': 1000}, index=idx)
class Res:
    def __init__(self, df, src): self.df, self.source, self.rows = df, src, len(df)
class Fake:
    def __init__(self, name, mode='ok'): self.name, self.mode = name, mode
    def get_ohlcv(self, t, period):
        if self.mode == 'ok': return Res(frame(), self.name)
        if self.mode == 'limit': raise RateLimitError(self.name, 'HTTP 429 https://x/?apikey=SECRETKEY123', t)
        if self.mode == 'boom': raise RuntimeError('unexpected')
        raise ProviderError(self.name, 'down', t)
def make(*provs):
    dp = orch.DataProvider.__new__(orch.DataProvider)
    dp._ohlcv_locks = {}; dp._ohlcv_locks_guard = threading.Lock(); dp._last_source = {}
    dp._ohlcv_chain = list(provs); dp._deliver = lambda t, df: df
    return dp

fresh_db()
quiet(make(Fake('twelvedata', 'limit'), Fake('yfinance', 'ok')).get_ohlcv, 'OKT', '2y')
r = al.read('OKT', 'ohlcv')
ok(r['state'] == 'ok' and r['last_ok_provider'] == 'yfinance' and r['period'] == '2y', 'chain: first failed, second answered = ok from the second')
quiet(make(Fake('twelvedata', 'ok')).get_ohlcv, 'OKT', '2y')       # now a cache hit: records nothing new
t_before = al.read('OKT', 'ohlcv')['last_ok_ts']
quiet(make(Fake('twelvedata', 'down')).get_ohlcv, 'OKT', '2y')
ok(al.read('OKT', 'ohlcv')['last_ok_ts'] == t_before, 'a cache hit records nothing (last_ok_ts unchanged)')

dp = make(Fake('twelvedata', 'limit'), Fake('yfinance', 'down'))
try: quiet(dp.get_ohlcv, 'DEADT', '2y'); got = 'served'
except ProviderError: got = 'error'
r = al.read('DEADT', 'ohlcv')
ok(got == 'error' and r['state'] == 'failed' and r['detail'] == 'twelvedata:RateLimitError; yfinance:ProviderError' and not r['served_stale'], 'all providers fail, no cache: failed, names only')
ok('SECRETKEY' not in (r['detail'] or ''), 'no key text in the stored detail')

cm.set_cached_ohlcv('STALET', frame(504), '2y', 'yfinance')
c = sqlite3.connect(str(cm.DB_PATH)); c.execute("update ohlcv_cache set expires_at = '2000-01-01T00:00:00-05:00' where ticker='STALET'"); c.commit(); c.close()
quiet(make(Fake('twelvedata', 'limit')).get_ohlcv, 'STALET', '2y')
r = al.read('STALET', 'ohlcv')
ok(r['state'] == 'failed' and r['served_stale'] is True, 'expired cache served after every provider failed: failed + served_stale')

try: quiet(make(Fake('twelvedata', 'boom')).get_ohlcv, 'BOOMT', '2y')
except RuntimeError: pass
r = al.read('BOOMT', 'ohlcv')
ok(r['state'] == 'failed' and r['detail'] == 'internal:RuntimeError', 'a non-provider exception is recorded too, then re-raised')

# blocked ticker repeat memo: second call within 60 s makes no provider call and records nothing new
orch._chain_failures.clear()
quiet_ts = None
try: quiet(make(Fake('twelvedata', 'down')).get_ohlcv, 'NVDL', '2y')
except ProviderError: pass
ts1 = al.read('NVDL', 'ohlcv')['last_fail_ts']
try: quiet(make(Fake('twelvedata', 'down')).get_ohlcv, 'NVDL', '2y')
except ProviderError: pass
ok(al.read('NVDL', 'ohlcv')['last_fail_ts'] == ts1, 'repeat-memo answer records nothing (no provider was called)')
orch._chain_failures.clear()

# ---- fundamentals: ok / partial / failed
class FRes:
    def __init__(self, data): self.data = data
class FProv:
    def __init__(self, data=None, raises=False, growth=None):
        self.data, self.raises, self.growth = data or {}, raises, growth or {}
    def get_fundamentals(self, t):
        if self.raises: raise ProviderError('finnhub', 'down', t)
        return FRes(dict(self.data))
    def get_growth_only(self, t):
        if self.raises: raise ProviderError('alphavantage', 'down', t)
        return dict(self.growth)
def fund(fin, av, yf):
    dp = orch.DataProvider.__new__(orch.DataProvider)
    dp._last_source = {}; dp.finnhub, dp.alphavantage, dp.yfinance = fin, av, yf
    return dp
k = FUNDAMENTALS_SCHEMA[0]
fresh_db()
r_, _ = quiet(fund(FProv({k: 1.0}), FProv(), FProv({k: 2.0})).get_fundamentals, 'FUNOK')
r = al.read('FUNOK', 'fundamentals')
ok(r['state'] == 'ok' and r['last_ok_provider'] == 'finnhub' and not r['last_ok_detail'], 'fundamentals: provider answered = ok')
quiet(fund(FProv(raises=True), FProv(raises=True), FProv({k: 2.0})).get_fundamentals, 'FUNPART')
r = al.read('FUNPART', 'fundamentals')
ok(r['state'] == 'ok' and r['last_ok_provider'] == 'yfinance' and 'partial' in (r['last_ok_detail'] or '') and 'finnhub:ProviderError' in r['last_ok_detail'], 'fundamentals: two providers raised, one answered = ok with a partial note')
r_, _ = quiet(fund(FProv(raises=True), FProv(raises=True), FProv(raises=True)).get_fundamentals, 'FUNDEAD')
r = al.read('FUNDEAD', 'fundamentals')
ok(r_ is None and r['state'] == 'failed' and 'finnhub:ProviderError' in r['detail'], 'fundamentals: all raised, nothing cached = failed, returns None')
r_, _ = quiet(fund(FProv({}), FProv(), FProv({})).get_fundamentals, 'FUNEMPTY')
r = al.read('FUNEMPTY', 'fundamentals')
ok(r['state'] == 'failed' and r['detail'] == 'all_providers_empty', 'fundamentals: every provider answered empty = failed (all_providers_empty)')

# ---- guard: every test that runs the real fetch code must redirect the attempt log (Opus review, Day 136)
offenders = []
for f in sorted(glob.glob(os.path.join(HERE, 'test_*.py')) + glob.glob(os.path.join(HERE, 'backtest', 'test_*.py'))):
    if os.path.basename(f) == 'test_attempt_log.py': continue
    s = open(f, encoding='utf-8').read()
    if re.search(r'\.get_ohlcv\(|\.get_fundamentals\(', s) and re.search(r'orchestrator|DataProvider', s) and 'attempt_log' not in s \
            and not re.search(r'_get_ohlcv_locked', s) and 'get_data_provider' not in s and 'DataProvider.__new__' in s:
        offenders.append(os.path.basename(f))
ok(not offenders, f'tests that run the real orchestrator fetch must redirect attempt_log.DB_PATH: {offenders}')
al.DB_PATH = REAL_DB
if os.path.exists(REAL_DB):
    c = sqlite3.connect(REAL_DB)
    has = c.execute("select count(*) from sqlite_master where name='fetch_attempts'").fetchone()[0]
    if has:
        leaked = c.execute("select ticker from fetch_attempts where ticker in ('OKT','DEADT','STALET','BOOMT','FUNOK','FUNPART','FUNDEAD','FUNEMPTY','NEWT','LOCKT','STALE1','STALE2')").fetchall()
        ok(not leaked, f'no test ticker leaked into the live provider_state.db: {leaked}')
    c.close()

print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
