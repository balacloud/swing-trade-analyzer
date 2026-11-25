"""Tests for the Alpaca provider, the Twelve Data fixes and the forming-bar cache cap (Day 129, plan ALPACA_PROVIDER_PLAN_DAY129.md).
All HTTP is faked. Breaker and limiter state go to a throwaway file (Golden Rule 22), the cache to a throwaway database.
Run: venv/bin/python test_alpaca_provider.py"""
import io, os, sys, tempfile, threading
from contextlib import redirect_stdout
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['STA_ENV_OVERRIDE'] = '0'   # Day 135: keep the fake test keys below; .env must not replace them
os.environ['ALPACA_API_KEY'] = 'AKTESTNOTREAL'
os.environ['ALPACA_SECRET_KEY'] = 'secret-not-real'
os.environ['TWELVEDATA_API_KEY'] = 'td-key-not-real'
os.environ['ALPACA_DATA_FEED'] = 'iex'          # must be ignored
from providers import circuit_breaker, rate_limiter, orchestrator as orch
from providers import alpaca_provider as ap
from providers import twelvedata_provider as tdp
from providers.coverage import is_us_symbol, is_canadian
from providers.exceptions import (DataNotFoundError, ProviderError, ProviderUnavailableError, RateLimitError,
                                  AuthenticationError, InsufficientDataError)
import cache_manager as cm

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

_TMP = tempfile.mkdtemp(prefix='alpaca_test_'); _n = 0
def fresh(cls):
    global _n; _n += 1
    path = os.path.join(_TMP, f'state_{_n}.db')
    for mod in (circuit_breaker, rate_limiter): mod.DB_PATH = path; mod._initialized = False
    circuit_breaker._breakers.clear(); rate_limiter._limiters.clear()
    assert circuit_breaker.DB_PATH.startswith(_TMP)
    return cls()
def fails(name): return circuit_breaker.get_breaker(name).status()['failure_count']
def tokens_used(name):
    lim = rate_limiter.get_limiter(name); return lim

class Resp:
    def __init__(self, status=200, text='', headers=None, payload=None):
        self.status_code, self.text, self.headers, self._p = status, text, headers or {}, payload
    def json(self):
        if self._p is None: raise ValueError('no json')
        return self._p
    def raise_for_status(self):
        if self.status_code >= 400: raise requests.HTTPError(f'{self.status_code} Client Error: for url: https://x/?apikey=SECRETKEY123')

def bars(n=40, last='2026-11-20', start_hour='05'):
    idx = pd.bdate_range(end=last, periods=n)
    return [{'t': f'{d.strftime("%Y-%m-%d")}T{start_hour}:00:00Z', 'o': 100 + i, 'h': 101 + i, 'l': 99 + i, 'c': 100.5 + i, 'v': 1000 + i, 'n': 5, 'vw': 100} for i, d in enumerate(idx)]

seen = []
def fake_get(resp_fn):
    def g(url, params=None, headers=None, timeout=None):
        seen.append({'url': url, 'params': dict(params or {}), 'headers': dict(headers or {})}); return resp_fn(len(seen))
    return g

# ---------------------------------------------------------------- coverage helper
ok(is_us_symbol('AAPL') and is_us_symbol('BRK-B') and is_us_symbol('brk.b'), 'US symbols (incl. class shares) are US')
ok(not any(is_us_symbol(x) for x in ('RY.TO', 'XDRV.TO', 'SOXL.NE', 'X.NEO', 'ABC.V', 'FOO.CN', '^VIX', '', None, '  ')), 'Canadian, index, empty and None are not US')
ok(is_canadian('ry.to') and not is_canadian('AAPL'), 'is_canadian is case-insensitive')

# ---------------------------------------------------------------- parse, request shape
p = fresh(ap.AlpacaProvider)
payload = {'bars': {'AAPL': bars(600)}, 'next_page_token': None}
with __import__('unittest.mock', fromlist=['patch']).patch.object(ap.requests, 'get', fake_get(lambda n: Resp(200, payload=payload))):
    seen.clear(); r, _ = quiet(p.get_ohlcv, 'AAPL', '2y')
df = r.df
ok(r.source == 'alpaca' and list(df.columns) == ['open', 'high', 'low', 'close', 'volume'], 'result carries source alpaca and lowercase columns')
ok(len(df) == 504, f'2y keeps 504 bars (got {len(df)})')
ok(df.index.tz is None and (df.index == df.index.normalize()).all() and df.index.is_monotonic_increasing, 'index is tz-naive, midnight, sorted')
q = seen[0]['params']
ok(q['adjustment'] == 'all' and q['feed'] == 'sip' and q['timeframe'] == '1Day', 'request asks adjustment=all, feed=sip, 1Day')
ok('end' not in q, 'request never sends `end` (a 15-minute-old end is mandatory on the free plan)')
ok(seen[0]['headers'].get('APCA-API-KEY-ID') == 'AKTESTNOTREAL', 'keys go in headers, not in the URL')
ok(q['symbols'] == 'AAPL', 'symbol sent as is')
# the data feed in the environment is ignored
ok(q['feed'] == 'sip', 'ALPACA_DATA_FEED=iex in the environment is ignored')
# date convention: 04:00Z (summer) and 05:00Z (winter) both give the New York day
d4 = ap.AlpacaProvider._parse_ohlcv(bars(3, last='2026-07-15', start_hour='04'))
d5 = ap.AlpacaProvider._parse_ohlcv(bars(3, last='2026-11-20', start_hour='05'))
ok(d4.index[-1] == pd.Timestamp('2026-07-15') and d5.index[-1] == pd.Timestamp('2026-11-20'), '04:00Z and 05:00Z stamps both give the right trading date')
late = ap.AlpacaProvider._parse_ohlcv([{'t': '2026-11-21T02:00:00Z', 'o': 1, 'h': 2, 'l': 1, 'c': 1.5, 'v': 9}])
ok(late.index[0] == pd.Timestamp('2026-11-20'), 'a stamp after 7pm New York (UTC next day) stays on the New York date')
dup = ap.AlpacaProvider._parse_ohlcv(bars(2) + bars(2)[-1:])
ok(not dup.index.duplicated().any(), 'a duplicated date is removed')

# ---------------------------------------------------------------- pagination, symbol map
p = fresh(ap.AlpacaProvider); pages = [{'bars': {'BRK.B': bars(30, last='2026-10-01')}, 'next_page_token': 'tok1'}, {'bars': {'BRK.B': bars(20, last='2026-11-20')}, 'next_page_token': None}]
with __import__('unittest.mock', fromlist=['patch']).patch.object(ap.requests, 'get', fake_get(lambda n: Resp(200, payload=pages[n - 1]))):
    seen.clear(); r, _ = quiet(p.get_ohlcv, 'BRK-B', '2y')
ok(len(seen) == 2 and seen[1]['params'].get('page_token') == 'tok1', 'pagination follows next_page_token')
ok(seen[0]['params']['symbols'] == 'BRK.B', 'BRK-B is sent as BRK.B')
ok(len(r.df) == 50 or len(r.df) == len(r.df[~r.df.index.duplicated()]), 'pages are joined')

# ---------------------------------------------------------------- not covered: no request, no token, no breaker failure
p = fresh(ap.AlpacaProvider)
with __import__('unittest.mock', fromlist=['patch']).patch.object(ap.requests, 'get', fake_get(lambda n: Resp(200, payload={'bars': {}}))):
    seen.clear()
    for sym in ('RY.TO', 'XDRV.TO', 'SOXL.NE', '^VIX', ''):
        try: quiet(p.get_ohlcv, sym, '2y'); raised = None
        except DataNotFoundError: raised = 'nf'
        ok(raised == 'nf', f'{sym!r}: DataNotFoundError')
ok(len(seen) == 0, 'no HTTP request for any of them')
ok(fails('alpaca') == 0, 'no breaker failure for them')

# ---------------------------------------------------------------- error mapping (each case a fresh breaker)
def run(status, text='', payload=None, headers=None, exc=None):
    p = fresh(ap.AlpacaProvider)
    def g(url, params=None, headers=None, timeout=None):
        if exc: raise exc
        return Resp(status, text, headers or {}, payload)
    buf = io.StringIO()
    with __import__('unittest.mock', fromlist=['patch']).patch.object(ap.requests, 'get', g), redirect_stdout(buf):
        try: p.get_ohlcv('AAPL', '2y'); return 'ok', fails('alpaca'), buf.getvalue(), None
        except Exception as e: return type(e).__name__, fails('alpaca'), buf.getvalue(), e
k, f, _, _ = run(401, 'forbidden');                                   ok(k == 'AuthenticationError' and f == 1, f'401 -> AuthenticationError + breaker failure ({k},{f})')
k, f, _, _ = run(403, '{"message":"forbidden."}');                    ok(k == 'AuthenticationError' and f == 1, f'plain 403 -> AuthenticationError + breaker failure ({k},{f})')
k, f, log, _ = run(403, '{"message":"subscription does not permit querying recent SIP data"}')
ok(k == 'ProviderError' and f == 0 and 'plan limit' in log, f'403 "subscription does not permit" -> loud ProviderError, NO breaker failure ({k},{f})')
k, f, _, _ = run(429, 'slow down', headers={'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1'});  ok(k == 'RateLimitError' and f == 1, f'429 -> RateLimitError + breaker failure ({k},{f})')
k, f, _, _ = run(500, 'oops');                                        ok(k == 'ProviderUnavailableError' and f == 1, f'500 -> ProviderUnavailableError + breaker failure ({k},{f})')
k, f, _, _ = run(400, '{"message":"invalid symbol: ZZ"}');            ok(k == 'DataNotFoundError' and f == 0, f'400 invalid symbol -> DataNotFoundError, no breaker failure ({k},{f})')
k, f, log, _ = run(400, '{"message":"invalid timeframe: 9Days"}');    ok(k == 'ProviderError' and f == 0 and 'rejected' in log, f'other 400 -> loud ProviderError, no breaker failure ({k},{f})')
k, f, log, _ = run(422, 'unprocessable');                              ok(k == 'ProviderError' and f == 0, f'422 (undocumented) -> loud ProviderError, no breaker failure ({k},{f})')
k, f, _, _ = run(200, payload={'bars': {}, 'next_page_token': None});  ok(k == 'DataNotFoundError' and f == 0, f'200 with empty bars (unknown symbol) -> DataNotFoundError ({k},{f})')
k, f, _, _ = run(200, payload={'bars': {'AAPL': bars(5)}});            ok(k == 'InsufficientDataError' and f == 0, f'5 bars -> InsufficientDataError ({k},{f})')
k, f, _, e = run(200, exc=requests.exceptions.ConnectionError('HTTPSConnectionPool url https://data.alpaca.markets/?APCA-API-KEY-ID=AKTESTNOTREAL'))
ok(k == 'ProviderUnavailableError' and f == 1, f'connection error -> ProviderUnavailableError + breaker failure ({k},{f})')
ok('AKTESTNOTREAL' not in str(e) and 'http' not in str(e).lower(), 'the error text carries neither the key nor the URL')
# breaker open / missing keys
p = fresh(ap.AlpacaProvider); b = circuit_breaker.get_breaker('alpaca')
for _ in range(20): b.record_failure()
try: quiet(p.get_ohlcv, 'AAPL', '2y'); k = 'ok'
except Exception as e: k = type(e).__name__
ok(k == 'ProviderUnavailableError', f'open breaker -> ProviderUnavailableError ({k})')
p = fresh(ap.AlpacaProvider); p.key_id = ''
try: quiet(p.get_ohlcv, 'AAPL', '2y'); k = 'ok'
except Exception as e: k = type(e).__name__
ok(k == 'AuthenticationError', f'missing keys -> AuthenticationError ({k})')

# ---------------------------------------------------------------- Twelve Data fixes
from unittest import mock
def td_run(ticker, resp=None, exc=None, intraday=False):
    t = fresh(tdp.TwelveDataProvider); calls = []
    def g(url, params=None, timeout=None):
        calls.append(dict(params or {}))
        if exc: raise exc
        return resp
    with mock.patch.object(tdp.requests, 'get', g):
        try:
            (t.get_intraday if intraday else t.get_ohlcv)(ticker); res = 'ok'
        except Exception as e: res = e
    return res, calls
for sym in ('RY.TO', 'SOXL.NE', '^VIX', ''):
    res, calls = td_run(sym, Resp(200, payload={}))
    ok(isinstance(res, DataNotFoundError) and not calls, f'Twelve Data {sym!r}: DataNotFoundError, no call')
    ok(fails('twelvedata') == 0, f'Twelve Data {sym!r}: no breaker failure')
res, calls = td_run('RY.TO', Resp(200, payload={}), intraday=True)
ok(isinstance(res, DataNotFoundError) and not calls, 'Twelve Data intraday also skips Canada')
res, calls = td_run('XYZ', Resp(404, 'not found'))
ok(isinstance(res, DataNotFoundError) and fails('twelvedata') == 0, 'Twelve Data HTTP 404 -> DataNotFoundError, no breaker failure')
res, calls = td_run('BRK-B', Resp(404, 'not found'))
ok(calls and calls[0]['symbol'] == 'BRK.B', 'Twelve Data gets BRK.B for BRK-B')
res, calls = td_run('XYZ', Resp(400, 'bad'))
ok(isinstance(res, ProviderUnavailableError) and fails('twelvedata') == 1, 'Twelve Data other HTTP error -> ProviderUnavailableError + breaker failure')
ok('SECRETKEY123' not in str(res) and 'apikey' not in str(res).lower() and 'http' not in str(res).lower().replace('httperror', ''), 'Twelve Data error text has no URL or key')
ok(getattr(res, '__cause__', None) is None, 'the exception chain is dropped (no traceback with the URL)')

# ---------------------------------------------------------------- chain order and routing (fake providers)
class Res:
    def __init__(self, df, src): self.df, self.source, self.rows = df, src, len(df)
class Fake:
    def __init__(self, name, fail=False, us_only=False): self.name, self.fail, self.us_only, self.calls = name, fail, us_only, 0
    def get_ohlcv(self, t, period):
        if self.us_only and not is_us_symbol(t): raise DataNotFoundError(self.name, 'not us', t)
        self.calls += 1
        if self.fail: raise ProviderError(self.name, 'down', t)
        idx = pd.bdate_range(end='2026-11-19', periods=504)
        return Res(pd.DataFrame({'open': 1.0, 'high': 2.0, 'low': 0.5, 'close': 1.5, 'volume': 1e6}, index=idx), self.name)
def chain(al_fail=False, td_fail=False):
    dp = orch.DataProvider.__new__(orch.DataProvider)
    dp._ohlcv_locks = {}; dp._ohlcv_locks_guard = threading.Lock(); dp._last_source = {}; dp._deliver = lambda t, df: df
    dp.al, dp.td, dp.yf, dp.tr = Fake('alpaca', al_fail, True), Fake('twelvedata', td_fail, True), Fake('yfinance'), Fake('tradier')
    dp._ohlcv_chain = [dp.al, dp.td, dp.yf, dp.tr]; return dp
tmpdb = tempfile.mkdtemp(); cm.DB_PATH = Path(tmpdb) / 'cache.db'
for _n2 in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _n2): getattr(cm, _n2)(); break
orch._chain_failures.clear()
dp = chain(); quiet(dp.get_ohlcv, 'AAPL', '2y')
ok(dp._last_source['AAPL_ohlcv'] == 'alpaca' and dp.td.calls == 0, 'US ticker: Alpaca serves first, Twelve Data is not asked')
dp = chain(al_fail=True); quiet(dp.get_ohlcv, 'MSFT', '2y')
ok(dp._last_source['MSFT_ohlcv'] == 'twelvedata', 'Alpaca down -> Twelve Data serves')
dp = chain(al_fail=True, td_fail=True); quiet(dp.get_ohlcv, 'KO', '2y')
ok(dp._last_source['KO_ohlcv'] == 'yfinance', 'Alpaca and Twelve Data down -> Yahoo')
dp = chain(); quiet(dp.get_ohlcv, 'RY.TO', '2y')
ok(dp._last_source['RY.TO_ohlcv'] == 'yfinance' and dp.al.calls == 0 and dp.td.calls == 0, 'Canadian ticker goes to Yahoo; Alpaca and Twelve Data never serve it')
dp = chain(al_fail=True, td_fail=True); dp.yf.fail = True
try: quiet(dp.get_ohlcv, 'NVDL', '2y'); got = 'served'
except ProviderError: got = 'error'
ok(got == 'error' and dp.tr.calls == 0, 'leveraged fund with Alpaca, Twelve Data, Yahoo all down: error, Tradier still never asked (Day 129 rule holds)')
dp = chain(al_fail=True, td_fail=True); dp.yf.fail = True; quiet(dp.get_ohlcv, 'XYZ1', '2y')
ok(dp._last_source['XYZ1_ohlcv'] == 'tradier', 'plain ticker with everything else down: Tradier is still the last resort')
real = orch.DataProvider()
ok([x.name for x in real._ohlcv_chain] == ['alpaca', 'twelvedata', 'yfinance', 'tradier'], 'the REAL chain order is Alpaca, Twelve Data, Yahoo, Tradier')
st = real.get_provider_status()['providers'] if 'providers' in real.get_provider_status() else real.get_provider_status()
ok('alpaca' in st and st['alpaca']['role'] == 'primary' and 'intraday' in st['twelvedata']['role'], 'provider status lists Alpaca as primary and Twelve Data as fallback (OHLCV) / primary (intraday)')
ok(real._intraday_chain[0].name == 'twelvedata', 'the intraday chain still starts with Twelve Data')

# ---------------------------------------------------------------- forming-bar expiry cap (every source)
ET = ZoneInfo('America/New_York')
def frame(last):
    idx = pd.bdate_range(end=last, periods=300)
    return pd.DataFrame({'open': 1.0, 'high': 2.0, 'low': 0.5, 'close': 1.5, 'volume': 1e6}, index=idx)
def exp_of(sym):
    _, meta = cm.read_ohlcv_entry(sym); return datetime.fromisoformat(meta['expires_at'])
thu = datetime(2026, 11, 19, 12, 0, tzinfo=ET)
for hh, mm, label in ((16, 5, '16:05'), (16, 20, '16:20'), (11, 0, '11:00')):
    now = thu.replace(hour=hh, minute=mm); sym = 'CAP' + label.replace(':', '')
    quiet(cm.set_cached_ohlcv, sym, frame('2026-11-19'), '2y', 'alpaca', now)
    e = exp_of(sym)
    ok(e.astimezone(ET).strftime('%Y-%m-%d %H:%M') == '2026-11-19 16:30', f'today bar fetched at {label}: expires at 16:30 today (got {e})')
now = thu.replace(hour=16, minute=35)
quiet(cm.set_cached_ohlcv, 'CAP1635', frame('2026-11-19'), '2y', 'alpaca', now)
ok(exp_of('CAP1635').astimezone(ET).strftime('%Y-%m-%d') != '2026-11-19', 'fetched after 16:30: not capped (expires at the next close)')
quiet(cm.set_cached_ohlcv, 'CAPOLD', frame('2026-11-18'), '2y', 'alpaca', thu.replace(hour=16, minute=5))
ok(exp_of('CAPOLD').astimezone(ET) > thu.replace(hour=16, minute=30), 'a frame whose newest bar is not today is not capped by this rule')

print(f'{passed} passed, {failed} failed')
sys.exit(0 if failed == 0 else 1)
