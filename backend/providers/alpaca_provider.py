"""
Alpaca Provider - first US daily-price source (Day 129, plan docs/claude/design/ALPACA_PROVIDER_PLAN_DAY129.md)

Free "Basic" plan: 200 calls a minute, daily bars since 2016, consolidated (SIP) history older than 15 minutes. Tested Day 129 against
Twelve Data and Yahoo: closes within 0.04% over the whole 2y history (dividend- and split-adjusted with adjustment=all), no split error on
NVDL or QPUX. US only (Canada comes back as "no bars").

Facts this code is built on (docs.alpaca.markets + real probes, Day 129):
  - GET https://data.alpaca.markets/v2/stocks/bars?symbols=&timeframe=1Day&start=&adjustment=all&feed=sip&limit=10000
  - NEVER send `end`: the default end is 15 minutes ago; an `end` inside the last 15 minutes is HTTP 403 "subscription does not permit
    querying recent SIP data" on the free plan.
  - feed is hard-coded to `sip`. The .env has ALPACA_DATA_FEED=iex; it is NOT read (IEX volume is a different, much smaller basis).
  - Unknown symbol (ZZZZQ) and Canadian symbol (RY.TO): HTTP 200 with {"bars": {}}. Malformed (^VIX, BRK-B, empty): HTTP 400
    "invalid symbol: X". Class shares use a dot: BRK.B works, BRK-B does not (STA writes BRK-B, so '-' is mapped to '.').
  - Daily bars are stamped at the New York trading day start (04:00Z or 05:00Z); a bar is only emitted when traded volume is non-zero, so a
    thin fund can miss whole sessions instead of showing zero-volume bars.
  - 422 is undocumented: it is treated as our own request bug (loud ProviderError, not "no data").
"""

import os
import requests
from datetime import datetime, timedelta
import pandas as pd

from .base import OHLCVProvider, OHLCVResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError, InsufficientDataError,
    RateLimitError, AuthenticationError, ProviderError
)
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker
from .coverage import is_us_symbol

BASE_URL = 'https://data.alpaca.markets/v2/stocks/bars'
FEED = 'sip'        # hard-coded on purpose, see the module docstring

# calendar days to ask for (with a margin) and how many bars to keep, same counts as Twelve Data's PERIOD_TO_OUTPUTSIZE
PERIOD_TO_DAYS = {'2y': 740, '1y': 372, '6mo': 190, '3mo': 98, '1mo': 36, '5d': 12}
PERIOD_TO_BARS = {'2y': 504, '1y': 252, '6mo': 126, '3mo': 63, '1mo': 22, '5d': 5}
NY = 'America/New_York'


class AlpacaProvider(OHLCVProvider):
    """Alpaca market data - first source for US daily OHLCV"""
    name = 'alpaca'

    def __init__(self):
        self.key_id = os.environ.get('ALPACA_API_KEY', '').strip()
        self.secret = os.environ.get('ALPACA_SECRET_KEY', '').strip()

    @property
    def api_key(self):          # the status endpoint reads `.api_key` on every provider
        return self.key_id

    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        if not is_us_symbol(ticker):
            # Not a health signal and not a request: no limiter token, no breaker failure.
            raise DataNotFoundError(self.name, 'not a US symbol (Alpaca covers US only)', ticker)
        self._check_availability()

        breaker = get_breaker(self.name)
        symbol = ticker.upper().replace('-', '.')
        start = (datetime.now().date() - timedelta(days=PERIOD_TO_DAYS.get(period, 740))).isoformat()
        headers = {'APCA-API-KEY-ID': self.key_id, 'APCA-API-SECRET-KEY': self.secret}
        rows, token = [], None
        try:
            for _ in range(20):                       # a 2y daily request is one page; the cap only guards against a loop
                params = {'symbols': symbol, 'timeframe': '1Day', 'start': start, 'adjustment': 'all', 'feed': FEED, 'limit': 10000}
                if token:
                    params['page_token'] = token
                resp = requests.get(BASE_URL, params=params, headers=headers, timeout=15)
                self._handle_http_errors(resp, ticker)
                data = resp.json() or {}
                rows += (data.get('bars') or {}).get(symbol) or []
                token = data.get('next_page_token')
                if not token:
                    break

            if not rows:
                raise DataNotFoundError(self.name, 'no bars returned', ticker)       # unknown symbol: a 200 with an empty list
            df = self._parse_ohlcv(rows)
            df = df.tail(PERIOD_TO_BARS.get(period, 504))
            if len(df) < 10:
                raise InsufficientDataError(self.name, f'Only {len(df)} bars', ticker)

            breaker.record_success()
            return OHLCVResult(df=df, source=self.name, ticker=ticker, period=period)

        except (DataNotFoundError, RateLimitError, AuthenticationError, ProviderUnavailableError,
                InsufficientDataError, ProviderError):
            raise
        except Exception as e:
            breaker.record_failure()
            # str(e) from `requests` can carry the full URL; never log or raise it (Day 129: Twelve Data's key leaked into backend.log that way)
            raise ProviderUnavailableError(self.name, f'{type(e).__name__} while fetching bars', ticker) from None

    @staticmethod
    def _parse_ohlcv(rows):
        """Alpaca bar dicts -> lowercase OHLCV, index = New York trading date at midnight, no timezone."""
        df = pd.DataFrame(rows)
        idx = pd.to_datetime(df['t'], utc=True).dt.tz_convert(NY).dt.tz_localize(None).dt.normalize()
        out = pd.DataFrame({'open': df['o'].astype(float), 'high': df['h'].astype(float), 'low': df['l'].astype(float),
                            'close': df['c'].astype(float), 'volume': df['v'].astype(float)})
        out.index = pd.DatetimeIndex(idx, name='datetime')
        return out[~out.index.duplicated(keep='last')].sort_index()

    def _handle_http_errors(self, resp, ticker):
        breaker = get_breaker(self.name)
        code = resp.status_code
        if code == 200:
            return
        body = (resp.text or '').strip()[:200]
        low = body.lower()
        remaining, reset = resp.headers.get('X-RateLimit-Remaining'), resp.headers.get('X-RateLimit-Reset')
        if code == 429:
            print(f"⚠️ Alpaca rate limit for {ticker}: remaining={remaining} reset={reset}")
            breaker.record_failure()
            raise RateLimitError(self.name, 'HTTP 429', ticker)
        if code == 401:
            print(f"🛑 Alpaca rejected the keys (HTTP 401): check ALPACA_API_KEY / ALPACA_SECRET_KEY")
            breaker.record_failure()
            raise AuthenticationError(self.name, 'HTTP 401', ticker)
        if code == 403:
            if 'subscription' in low or 'permit' in low:
                # Our request asked for something the free plan does not allow (for example recent SIP data): our bug, not a health signal.
                print(f"🛑 Alpaca refused the request for {ticker} (plan limit): HTTP 403 {body!r}")
                raise ProviderError(self.name, f'HTTP 403 plan limit: {body}', ticker)
            print(f"🛑 Alpaca forbids the keys (HTTP 403): {body!r}")
            breaker.record_failure()
            raise AuthenticationError(self.name, 'HTTP 403', ticker)
        if code >= 500:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, f'HTTP {code}', ticker)
        if code == 400 and 'invalid symbol' in low:
            raise DataNotFoundError(self.name, body, ticker)             # ticker-specific, not a health signal (Golden Rule 36)
        # any other 400 / 404 / 422: most likely OUR request bug. Loud, and kept out of the breaker.
        print(f"🛑 Alpaca rejected the request for {ticker}: HTTP {code} {body!r}")
        raise ProviderError(self.name, f'HTTP {code} bad request: {body or "(empty)"}', ticker)

    def _check_availability(self):
        if not (self.key_id and self.secret):
            raise AuthenticationError(self.name, 'ALPACA_API_KEY / ALPACA_SECRET_KEY not set')
        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, 'Circuit breaker OPEN')
        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, 'Rate limit exceeded')
