"""
TwelveData Provider - v4.14 Multi-Source Data Intelligence

Primary OHLCV provider. Reliable, fast, well-documented API.
Free tier: 8 requests/min, 800 requests/day.

Endpoints used:
  GET /time_series?symbol={}&interval=1day&outputsize={}&apikey={}
  GET /time_series?symbol={}&interval=1h&outputsize={}&apikey={}
"""

import os
import requests
import pandas as pd
from datetime import datetime

from .base import OHLCVProvider, IntradayProvider, OHLCVResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError, InsufficientDataError,
    RateLimitError, AuthenticationError
)
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


BASE_URL = 'https://api.twelvedata.com'

# Map period strings to TwelveData outputsize (number of bars)
PERIOD_TO_OUTPUTSIZE = {
    '2y':  504,    # ~2 years of trading days
    '1y':  252,    # ~1 year
    '6mo': 126,    # ~6 months
    '3mo': 63,     # ~3 months
    '1mo': 22,     # ~1 month
    '5d':  5,
}


class TwelveDataProvider(OHLCVProvider, IntradayProvider):
    """TwelveData - primary OHLCV provider"""
    name = 'twelvedata'

    def __init__(self):
        self.api_key = os.environ.get('TWELVEDATA_API_KEY', '')

    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        """Fetch daily OHLCV time series"""
        self._check_availability()

        outputsize = PERIOD_TO_OUTPUTSIZE.get(period, 504)

        data = self._fetch_time_series(
            ticker=ticker,
            interval='1day',
            outputsize=outputsize
        )

        df = self._parse_ohlcv(data, ticker)

        if len(df) < 10:
            raise InsufficientDataError(self.name, f"Only {len(df)} bars", ticker)

        return OHLCVResult(df=df, source=self.name, ticker=ticker, period=period)

    def get_intraday(self, ticker: str, interval: str = '1h', period: str = '60d') -> OHLCVResult:
        """Fetch intraday OHLCV (for 4H RSI calculation)"""
        self._check_availability()

        # Map period to approximate outputsize for intraday
        # 60d of 1h data ≈ 60 * 7h/day = 420 bars
        intraday_sizes = {
            '60d': 420,
            '30d': 210,
            '7d':  49,
            '5d':  35,
        }
        outputsize = intraday_sizes.get(period, 420)

        data = self._fetch_time_series(
            ticker=ticker,
            interval=interval,
            outputsize=outputsize
        )

        df = self._parse_ohlcv(data, ticker, intraday=True)

        return OHLCVResult(df=df, source=self.name, ticker=ticker, period=period)

    def _fetch_time_series(self, ticker: str, interval: str, outputsize: int) -> dict:
        """Make the API call to TwelveData /time_series endpoint"""
        breaker = get_breaker(self.name)

        try:
            url = f"{BASE_URL}/time_series"
            params = {
                'symbol': ticker,
                'interval': interval,
                'outputsize': outputsize,
                'apikey': self.api_key,
                'format': 'JSON',
            }

            resp = requests.get(url, params=params, timeout=15)

            # Handle HTTP errors
            if resp.status_code == 429:
                breaker.record_failure()
                raise RateLimitError(self.name, "HTTP 429 - rate limited", ticker)
            if resp.status_code == 401:
                breaker.record_failure()
                raise AuthenticationError(self.name, "Invalid API key", ticker)
            if resp.status_code >= 500:
                breaker.record_failure()
                raise ProviderUnavailableError(self.name, f"HTTP {resp.status_code}", ticker)

            resp.raise_for_status()
            data = resp.json()

            # TwelveData returns errors in JSON body
            if data.get('status') == 'error':
                code = data.get('code', 0)
                message = data.get('message', 'Unknown error')
                if code == 429:
                    breaker.record_failure()
                    raise RateLimitError(self.name, message, ticker)
                if code == 401:
                    breaker.record_failure()
                    raise AuthenticationError(self.name, message, ticker)
                if code == 404 or 'not found' in message.lower():
                    breaker.record_failure()
                    raise DataNotFoundError(self.name, message, ticker)
                breaker.record_failure()
                raise ProviderUnavailableError(self.name, message, ticker)

            breaker.record_success()
            return data

        except (RateLimitError, AuthenticationError, DataNotFoundError, ProviderUnavailableError):
            raise
        except requests.exceptions.Timeout:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, "Request timeout", ticker)
        except requests.exceptions.ConnectionError:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, "Connection failed", ticker)
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def _parse_ohlcv(self, data: dict, ticker: str, intraday: bool = False) -> pd.DataFrame:
        """Parse TwelveData JSON response into DataFrame with lowercase columns"""
        values = data.get('values', [])
        if not values:
            raise DataNotFoundError(self.name, "No values in response", ticker)

        rows = []
        for v in values:
            rows.append({
                'datetime': v['datetime'],
                'open': float(v['open']),
                'high': float(v['high']),
                'low': float(v['low']),
                'close': float(v['close']),
                'volume': int(v['volume']),
            })

        df = pd.DataFrame(rows)

        if intraday:
            df['datetime'] = pd.to_datetime(df['datetime'])
        else:
            df['datetime'] = pd.to_datetime(df['datetime']).dt.tz_localize(None)

        df = df.set_index('datetime').sort_index()
        return df

    def _check_availability(self):
        """Check API key, rate limit, and circuit breaker"""
        if not self.api_key:
            raise AuthenticationError(self.name, "TWELVEDATA_API_KEY not set")

        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded")
