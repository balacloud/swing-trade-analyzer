"""
Tradier Provider - v4.14 Multi-Source Data Intelligence (Day 83 addition)

Third-tier OHLCV/quote fallback, added as a reliability upgrade after Day 82
removed Stooq from the active OHLCV chain (bot-blocked). This is the LAST
entry in both _ohlcv_chain and _quote_chain — TwelveData/yfinance stay
primary; Tradier only gets called when both of those have already failed.

Reliability-only, per the Day 83 UI Code Quality Fix Plan (Task D1): this
does NOT integrate Tradier's options-chain or fundamentals endpoints. Options
data belongs to OptionsIQ (separate repo, in build stage) — STA is in
feature freeze. Fundamentals are Tradier-beta-tier and confirmed (via 12 live
API calls during the Day 82 evaluation) to be MISSING roic/revenueGrowth/
epsGrowth/margins/marketCap — they would not close STA's actual fundamentals
gaps, so there is no FundamentalsProvider implementation here.

Verified facts this implementation is built against (Day 82 evaluation):
  - Configured token is PRODUCTION tier (api.tradier.com, not sandbox),
    confirmed via /v1/user/profile returning a real active margin account.
  - Rate limit observed: 120 requests/min on market-data endpoints.
  - OHLCV (/v1/markets/history): split-adjusted but NOT dividend-adjusted —
    acceptable for a last-resort fallback, not for anything that needs to
    match a dividend-adjusted primary source exactly.
  - Quotes (/v1/markets/quotes): VIX works as the plain symbol 'VIX' (not
    '$VIX.X', which is unmatched) — same '^' stripping convention
    finnhub_provider.py already uses.
  - Every request needs BOTH an Authorization header and Accept: application/json
    (Tradier defaults to XML without the Accept header).

Endpoints used:
  GET /v1/markets/history?symbol={}&interval=daily&start={}&end={}  → OHLCV
  GET /v1/markets/quotes?symbols={}                                  → Quote
"""

import os
import requests
from datetime import datetime, timedelta
import pandas as pd

from .base import OHLCVProvider, QuoteProvider, OHLCVResult, QuoteResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError, InsufficientDataError,
    RateLimitError, AuthenticationError
)
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


BASE_URL = 'https://api.tradier.com/v1'

# Map period strings to a lookback window in days (Tradier's history endpoint
# takes start/end dates, not an outputsize/bar-count like TwelveData).
PERIOD_TO_DAYS = {
    '2y':  730,
    '1y':  365,
    '6mo': 183,
    '3mo': 92,
    '1mo': 31,
    '5d':  7,
}


class TradierProvider(OHLCVProvider, QuoteProvider):
    """Tradier - last-resort OHLCV/quote fallback (production brokerage tier)"""
    name = 'tradier'

    def __init__(self):
        self.api_key = os.environ.get('TRADIER_ACCESS_TOKEN', '')

    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        """Fetch daily OHLCV from /v1/markets/history. NOT dividend-adjusted."""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            days = PERIOD_TO_DAYS.get(period, 730)
            end = datetime.now().date()
            start = end - timedelta(days=days)

            url = f"{BASE_URL}/markets/history"
            params = {
                'symbol': ticker,
                'interval': 'daily',
                'start': start.isoformat(),
                'end': end.isoformat(),
            }
            resp = requests.get(url, params=params, headers=self._headers(), timeout=15)
            self._handle_http_errors(resp, ticker)

            data = resp.json()
            history = (data or {}).get('history')
            if not history or not history.get('day'):
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No history returned", ticker)

            day = history['day']
            # Tradier returns a dict (not a list) when only one bar comes back
            if isinstance(day, dict):
                day = [day]

            df = self._parse_ohlcv(day, ticker)

            if len(df) < 10:
                breaker.record_failure()
                raise InsufficientDataError(self.name, f"Only {len(df)} bars", ticker)

            breaker.record_success()
            return OHLCVResult(df=df, source=self.name, ticker=ticker, period=period)

        except (DataNotFoundError, RateLimitError, AuthenticationError,
                ProviderUnavailableError, InsufficientDataError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_quote(self, ticker: str) -> QuoteResult:
        """Fetch current price + previous close from /v1/markets/quotes."""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            # Tradier doesn't use '^' index syntax — VIX is the plain symbol 'VIX'
            tradier_ticker = ticker.replace('^', '')

            url = f"{BASE_URL}/markets/quotes"
            params = {'symbols': tradier_ticker}
            resp = requests.get(url, params=params, headers=self._headers(), timeout=10)
            self._handle_http_errors(resp, ticker)

            data = resp.json()
            quotes = (data or {}).get('quotes') or {}
            quote = quotes.get('quote')

            if not quote or quotes.get('unmatched_symbols'):
                breaker.record_failure()
                raise DataNotFoundError(self.name, "Symbol unmatched", ticker)

            # A multi-symbol response would return a list; we only ever pass one.
            if isinstance(quote, list):
                quote = quote[0] if quote else None
            if not quote:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "Empty quote", ticker)

            price = quote.get('last')
            previous_close = quote.get('prevclose')
            if price is None:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No price in quote", ticker)

            breaker.record_success()
            return QuoteResult(
                price=round(float(price), 2),
                previous_close=round(float(previous_close), 2) if previous_close is not None else None,
                source=self.name,
                ticker=ticker
            )

        except (DataNotFoundError, RateLimitError, AuthenticationError, ProviderUnavailableError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def _parse_ohlcv(self, day_rows: list, ticker: str) -> pd.DataFrame:
        """Parse Tradier's history.day rows into a DataFrame with lowercase columns."""
        rows = []
        for d in day_rows:
            rows.append({
                'datetime': d['date'],
                'open': float(d['open']),
                'high': float(d['high']),
                'low': float(d['low']),
                'close': float(d['close']),
                'volume': int(d['volume']),
            })

        if not rows:
            raise DataNotFoundError(self.name, "No parseable rows", ticker)

        df = pd.DataFrame(rows)
        df['datetime'] = pd.to_datetime(df['datetime']).dt.tz_localize(None)
        df = df.set_index('datetime').sort_index()
        return df

    def _headers(self) -> dict:
        # Tradier defaults to XML without an explicit Accept header.
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json',
        }

    def _handle_http_errors(self, resp, ticker: str):
        """Handle HTTP-level errors consistently"""
        breaker = get_breaker(self.name)
        if resp.status_code == 429:
            breaker.record_failure()
            raise RateLimitError(self.name, "HTTP 429", ticker)
        if resp.status_code == 401 or resp.status_code == 403:
            breaker.record_failure()
            raise AuthenticationError(self.name, f"HTTP {resp.status_code}", ticker)
        if resp.status_code >= 500:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, f"HTTP {resp.status_code}", ticker)
        resp.raise_for_status()

    def _check_availability(self):
        """Check API key, rate limit, and circuit breaker"""
        if not self.api_key:
            raise AuthenticationError(self.name, "TRADIER_ACCESS_TOKEN not set")

        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded")
