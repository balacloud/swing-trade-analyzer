"""
Stooq Provider - v4.14 Multi-Source Data Intelligence

Last-resort OHLCV provider via pandas_datareader.
No API key needed, but very low rate limits.
Does NOT support intraday data.

Uses: pandas_datareader.data.DataReader(ticker, 'stooq')
"""

import pandas as pd
from datetime import datetime, timedelta

from .base import OHLCVProvider, OHLCVResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError, InsufficientDataError
)
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker

# Stooq via pandas_datareader - optional dependency
try:
    import pandas_datareader.data as pdr
    STOOQ_AVAILABLE = True
except ImportError:
    STOOQ_AVAILABLE = False

# Map period to days back from today
PERIOD_TO_DAYS = {
    '2y':  730,
    '1y':  365,
    '6mo': 180,
    '3mo': 90,
    '1mo': 30,
    '5d':  5,
}


class StooqProvider(OHLCVProvider):
    """Stooq - last resort OHLCV provider (no API key needed)"""
    name = 'stooq'

    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        """Fetch daily OHLCV from Stooq via pandas_datareader"""
        if not STOOQ_AVAILABLE:
            raise ProviderUnavailableError(self.name, "pandas_datareader not installed")

        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            days = PERIOD_TO_DAYS.get(period, 730)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)

            df = pdr.DataReader(ticker, 'stooq', start=start_date, end=end_date)

            if df is None or df.empty:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No data returned", ticker)

            # Stooq returns columns: Open, High, Low, Close, Volume (capitalized)
            # Normalize to lowercase
            df.columns = [c.lower() for c in df.columns]

            # Ensure we have OHLCV columns
            required = ['open', 'high', 'low', 'close', 'volume']
            missing = [c for c in required if c not in df.columns]
            if missing:
                breaker.record_failure()
                raise DataNotFoundError(self.name, f"Missing columns: {missing}", ticker)

            df = df[required].sort_index()

            if len(df) < 10:
                breaker.record_failure()
                raise InsufficientDataError(self.name, f"Only {len(df)} bars", ticker)

            breaker.record_success()
            return OHLCVResult(df=df, source=self.name, ticker=ticker, period=period)

        except (DataNotFoundError, InsufficientDataError, ProviderUnavailableError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def _check_availability(self):
        """Check rate limit and circuit breaker"""
        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            from .exceptions import RateLimitError
            raise RateLimitError(self.name, "Rate limit exceeded")
