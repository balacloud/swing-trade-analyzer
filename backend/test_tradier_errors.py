"""Tests for Tradier HTTP-error handling (Day 127, plan TRADIER_ERROR_HANDLING_PLAN_DAY127.md).
Tradier answers a quota violation AND a bad request with HTTP 400 (never 429), with a plain-text body.
Rules under test: quota 400 -> RateLimitError + breaker failure; "symbol not found" 400 -> DataNotFoundError, no
breaker failure (Golden Rule 36); any other 400 -> loud ProviderError, no breaker failure; empty symbol -> no request.

The breaker and the rate limiter keep their state in a REAL shared file (data/provider_state.db, Golden Rule 22).
Every case below points both modules at a throwaway file first, so this test can never open the live breaker.
Run: venv/bin/python test_tradier_errors.py"""
import os
import sys
import tempfile

import requests

from providers import circuit_breaker, rate_limiter
from providers import tradier_provider as tp
from providers.exceptions import (
    DataNotFoundError, ProviderError, ProviderUnavailableError, RateLimitError, AuthenticationError,
)

os.environ['TRADIER_ACCESS_TOKEN'] = 'test-token-not-real'
passed = failed = 0
_REAL_GET = requests.get   # restored at the end; the cases below swap tp.requests.get (the same module object)
_TMP = tempfile.mkdtemp(prefix='tradier_test_')
_n = 0


def check(name, cond, detail=''):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        print(f'FAIL {name} {detail}')


class Resp:
    def __init__(self, status=200, text='', headers=None, payload=None):
        self.status_code = status
        self.text = text
        self.headers = headers or {}
        self._payload = payload

    def json(self):
        if self._payload is None:
            raise ValueError('no json')
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f'{self.status_code} Client Error')


def fresh():
    """A brand-new state file and a brand-new breaker for each case."""
    global _n
    _n += 1
    path = os.path.join(_TMP, f'state_{_n}.db')
    for mod in (circuit_breaker, rate_limiter):
        mod.DB_PATH = path
        mod._initialized = False
    circuit_breaker._breakers.clear()
    rate_limiter._limiters.clear()
    # Safety: never run against the shared live state file.
    assert circuit_breaker.DB_PATH.startswith(_TMP) and rate_limiter.DB_PATH.startswith(_TMP)
    return tp.TradierProvider()


def failures():
    return circuit_breaker.get_breaker('tradier').status()['failure_count']


def state():
    return circuit_breaker.get_breaker('tradier').status()['state']


def with_response(resp_or_exc):
    """Make requests.get return (or raise) what we want, and count the calls."""
    calls = {'n': 0}

    def fake_get(*a, **k):
        calls['n'] += 1
        if isinstance(resp_or_exc, Exception):
            raise resp_or_exc
        return resp_or_exc
    tp.requests.get = fake_get
    return calls


def expect(call, exc):
    try:
        call()
    except exc as e:
        return e
    except Exception as e:  # noqa: BLE001
        return e
    return None


BARS = {'history': {'day': [{'date': f'2026-11-{d:02d}', 'open': 1, 'high': 2, 'low': 1, 'close': 1.5, 'volume': 100}
                            for d in range(1, 13)]}}
QUOTE = {'quotes': {'quote': {'last': 10.0, 'prevclose': 9.5, 'trade_date': 1763560000000}}}
UNMATCHED = {'quotes': {'unmatched_symbols': {'symbol': 'ZZZZ'}}}

ENDPOINTS = {
    'history': lambda p: p.get_ohlcv('AAPL'),
    'quote': lambda p: p.get_quote('AAPL'),
    'live_raw': lambda p: p.get_live_raw('AAPL'),
}

# ---- happy paths still work ----
p = fresh(); with_response(Resp(200, payload=BARS))
r = ENDPOINTS['history'](p); check('history 200 ok', len(r.df) == 12 and failures() == 0)
p = fresh(); with_response(Resp(200, payload=QUOTE))
check('quote 200 ok', ENDPOINTS['quote'](p).price == 10.0 and failures() == 0)
p = fresh(); with_response(Resp(200, payload=QUOTE))
check('live_raw 200 ok', ENDPOINTS['live_raw'](p)['price'] == 10.0 and failures() == 0)

# ---- the three 400 cases, on every endpoint ----
for ep, call in ENDPOINTS.items():
    p = fresh(); with_response(Resp(400, 'Quota Violation: too many requests'))
    e = expect(lambda: call(p), RateLimitError)
    check(f'{ep}: 400 quota -> RateLimitError', isinstance(e, RateLimitError), repr(e))
    check(f'{ep}: 400 quota -> breaker failure +1', failures() == 1, failures())

    p = fresh(); with_response(Resp(400, '', headers={'X-Ratelimit-Available': '0'}))
    e = expect(lambda: call(p), RateLimitError)
    check(f'{ep}: 400 empty body + Available 0 -> quota', isinstance(e, RateLimitError) and failures() == 1, repr(e))

    p = fresh(); with_response(Resp(400, 'Invalid parameter, ZZZZ: symbol not found.', headers={'X-Ratelimit-Available': '50'}))
    e = expect(lambda: call(p), DataNotFoundError)
    check(f'{ep}: 400 symbol not found -> DataNotFoundError', isinstance(e, DataNotFoundError), repr(e))
    check(f'{ep}: symbol not found -> breaker failure +0', failures() == 0, failures())

    p = fresh(); with_response(Resp(400, 'Invalid parameter, end: must be on or after 2026-11-19'))
    e = expect(lambda: call(p), ProviderError)
    check(f'{ep}: other 400 -> ProviderError (loud)', isinstance(e, ProviderError) and not isinstance(e, (DataNotFoundError, RateLimitError, ProviderUnavailableError)), repr(e))
    check(f'{ep}: other 400 -> breaker failure +0', failures() == 0, failures())

    p = fresh(); with_response(Resp(400, ''))
    e = expect(lambda: call(p), ProviderError)
    check(f'{ep}: empty-body 400 -> ProviderError, not "no data"', isinstance(e, ProviderError) and not isinstance(e, DataNotFoundError), repr(e))
    check(f'{ep}: empty-body 400 -> breaker failure +0', failures() == 0, failures())

# ---- edge cases (three-pass review) ----
p = fresh(); with_response(Resp(400, 'Invalid parameter, QUOTA: symbol not found.'))
e = expect(lambda: p.get_ohlcv('QUOTA'), DataNotFoundError)
check('ticker spelled "QUOTA" (symbol not found) is NOT a quota hit', isinstance(e, DataNotFoundError) and failures() == 0, repr(e))
p = fresh(); with_response(Resp(400, 'Invalid parameter, ZZZZ: symbol not found.', headers={'X-Ratelimit-Available': '0'}))
e = expect(lambda: p.get_ohlcv('ZZZZ'), DataNotFoundError)
check('symbol-not-found wins over Available "0"', isinstance(e, DataNotFoundError) and failures() == 0, repr(e))
p = fresh(); with_response(Resp(400, None))
e = expect(lambda: p.get_ohlcv('AAPL'), ProviderError)
check('body None (no text at all) -> loud ProviderError, no crash', isinstance(e, ProviderError) and failures() == 0, repr(e))
p = fresh(); with_response(Resp(400, 'x' * 5000 + ' quota'))
e = expect(lambda: p.get_ohlcv('AAPL'), ProviderError)
check('huge body is cut to 200 chars (a "quota" word past the cut is not seen)', isinstance(e, ProviderError) and not isinstance(e, RateLimitError) and len(str(e)) < 400, len(str(e)))
p = fresh(); with_response(Resp(400, 'QUOTA VIOLATION'))
check('quota matching ignores case', isinstance(expect(lambda: p.get_ohlcv('AAPL'), RateLimitError), RateLimitError))
for bad in (None,):
    p = fresh(); calls = with_response(Resp(200, payload=QUOTE))
    e = expect(lambda: p.get_quote(bad), DataNotFoundError)
    check('ticker None -> DataNotFoundError, no request', isinstance(e, DataNotFoundError) and calls['n'] == 0, repr(e))

# ---- Golden Rule 36: unknown tickers must never open the breaker ----
p = fresh(); with_response(Resp(400, 'Invalid parameter, X: symbol not found.'))
for _ in range(5):
    expect(lambda: p.get_ohlcv('NOPE'), DataNotFoundError)
check('5 unknown tickers in a row leave the breaker closed', state() == 'closed' and failures() == 0, (state(), failures()))

# ---- real health failures still count ----
for status, exc in ((429, RateLimitError), (401, AuthenticationError), (403, AuthenticationError), (500, ProviderUnavailableError), (503, ProviderUnavailableError)):
    p = fresh(); with_response(Resp(status, 'x'))
    e = expect(lambda: p.get_ohlcv('AAPL'), exc)
    check(f'HTTP {status} -> {exc.__name__}', isinstance(e, exc), repr(e))
    check(f'HTTP {status} -> breaker failure +1', failures() == 1, failures())
p = fresh(); with_response(requests.exceptions.ReadTimeout('timed out'))
e = expect(lambda: p.get_ohlcv('AAPL'), ProviderUnavailableError)
check('timeout -> ProviderUnavailableError, failure +1', isinstance(e, ProviderUnavailableError) and failures() == 1, repr(e))
p = fresh(); with_response(requests.exceptions.ReadTimeout('timed out'))
for _ in range(3):
    expect(lambda: p.get_ohlcv('AAPL'), ProviderUnavailableError)
check('3 timeouts open the breaker (unchanged)', state() == 'open', state())

# ---- quote endpoint unknown symbol: HTTP 200 + unmatched_symbols (measured Day 127) ----
p = fresh(); with_response(Resp(200, payload=UNMATCHED))
e = expect(lambda: p.get_quote('ZZZZ'), DataNotFoundError)
check('quote unmatched (200) -> DataNotFoundError, no failure', isinstance(e, DataNotFoundError) and failures() == 0, repr(e))

# ---- empty symbol: no request is sent at all ----
for bad in ('^', '', '  ', '^^'):
    for name, fn in (('get_quote', lambda p, t: p.get_quote(t)), ('get_live_raw', lambda p, t: p.get_live_raw(t))):
        p = fresh(); calls = with_response(Resp(200, payload=QUOTE))
        e = expect(lambda: fn(p, bad), DataNotFoundError)
        check(f'{name}({bad!r}) -> DataNotFoundError, no request, no failure',
              isinstance(e, DataNotFoundError) and calls['n'] == 0 and failures() == 0, (repr(e), calls['n']))
p = fresh(); calls = with_response(Resp(200, payload={'quotes': {'quote': {'last': 17.0, 'prevclose': 16.0}}}))
check('VIX written as "^VIX" still sends a request', p.get_quote('^VIX').price == 17.0 and calls['n'] == 1)

# ---- live quote chain with the REAL Tradier provider (Opus review, blast radius) ----
import live_quote  # noqa: E402
from types import SimpleNamespace  # noqa: E402


class _NF:
    def get_live_raw(self, t):
        raise DataNotFoundError('other', 'unmatched', t)


p = fresh(); with_response(Resp(200, payload=UNMATCHED))
q = live_quote.build_live_quote('ZZZZ', SimpleNamespace(tradier=p, yfinance=_NF(), finnhub=_NF()))
check('live quote: Tradier unmatched + others not-found -> "no live price for this ticker"',
      q.get('available') is False and q.get('reason') == 'no live price for this ticker', q)
p = fresh(); with_response(Resp(400, 'Quota Violation'))
q = live_quote.build_live_quote('ZZZZ', SimpleNamespace(tradier=p, yfinance=_NF(), finnhub=_NF()))
check('live quote: Tradier quota hit is a SOURCE problem, not "no such ticker"',
      q.get('available') is False and q.get('reason') == 'live price source unavailable', q)

requests.get = _REAL_GET
print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
