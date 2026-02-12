"""
Finnhub Provider - v4.14 Multi-Source Data Intelligence

Primary fundamentals provider. Reliable, generous free tier.
Free tier: 60 requests/min (unlimited daily).

Endpoints used:
  GET /stock/metric?symbol={}&metric=all   → Fundamentals
  GET /quote?symbol={}                      → Real-time quote (VIX)

IMPORTANT: Finnhub LACKS epsGrowth and revenueGrowth.
The orchestrator fills these gaps from FMP.
"""

import os
import requests

from .base import FundamentalsProvider, QuoteProvider, FundamentalsResult, QuoteResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError,
    RateLimitError, AuthenticationError
)
from .field_maps import FINNHUB_FUNDAMENTALS, apply_field_map
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


BASE_URL = 'https://finnhub.io/api/v1'


class FinnhubProvider(FundamentalsProvider, QuoteProvider):
    """Finnhub - primary fundamentals provider + VIX quote"""
    name = 'finnhub'

    def __init__(self):
        self.api_key = os.environ.get('FINNHUB_API_KEY', '')

    def get_fundamentals(self, ticker: str) -> FundamentalsResult:
        """
        Fetch fundamentals from Finnhub /stock/metric endpoint.
        Returns all fields it can; epsGrowth and revenueGrowth will be None.
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            url = f"{BASE_URL}/stock/metric"
            params = {
                'symbol': ticker,
                'metric': 'all',
                'token': self.api_key,
            }

            resp = requests.get(url, params=params, timeout=10)
            self._handle_http_errors(resp, ticker)

            data = resp.json()
            metric = data.get('metric', {})

            if not metric:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "Empty metric data", ticker)

            # Apply field normalization
            normalized = apply_field_map(metric, FINNHUB_FUNDAMENTALS)
            normalized['source'] = self.name

            # Track which fields we actually got
            field_sources = {k: self.name for k, v in normalized.items() if v is not None and k != 'source'}

            breaker.record_success()
            return FundamentalsResult(
                data=normalized, source=self.name, ticker=ticker, field_sources=field_sources
            )

        except (DataNotFoundError, RateLimitError, AuthenticationError, ProviderUnavailableError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_quote(self, ticker: str) -> QuoteResult:
        """
        Fetch real-time quote from Finnhub /quote endpoint.
        Used for VIX when yfinance is down.
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            # Finnhub doesn't support ^VIX syntax, needs different symbol
            finnhub_ticker = ticker.replace('^', '')  # ^VIX → VIX

            url = f"{BASE_URL}/quote"
            params = {
                'symbol': finnhub_ticker,
                'token': self.api_key,
            }

            resp = requests.get(url, params=params, timeout=10)
            self._handle_http_errors(resp, ticker)

            data = resp.json()
            price = data.get('c')  # Current price
            previous_close = data.get('pc')  # Previous close

            if price is None or price == 0:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No price in quote", ticker)

            breaker.record_success()
            return QuoteResult(
                price=round(float(price), 2),
                previous_close=round(float(previous_close), 2) if previous_close else None,
                source=self.name,
                ticker=ticker
            )

        except (DataNotFoundError, RateLimitError, AuthenticationError, ProviderUnavailableError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

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
            raise AuthenticationError(self.name, "FINNHUB_API_KEY not set")

        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded")
