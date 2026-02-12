"""
FMP (Financial Modeling Prep) Provider - v4.14 Multi-Source Data Intelligence

Fills growth metrics that Finnhub lacks (epsGrowth, revenueGrowth).
Also serves as secondary fundamentals provider.
Free tier: 10 requests/min, 250 requests/day.

Endpoints used:
  GET /api/v3/key-metrics-ttm/{ticker}?apikey={}           → Core metrics
  GET /api/v3/financial-growth/{ticker}?period=annual&limit=1&apikey={}  → Growth rates
"""

import os
import requests

from .base import FundamentalsProvider, FundamentalsResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError,
    RateLimitError, AuthenticationError
)
from .field_maps import FMP_FUNDAMENTALS, FMP_GROWTH, apply_field_map
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


BASE_URL = 'https://financialmodelingprep.com/api/v3'


class FMPProvider(FundamentalsProvider):
    """Financial Modeling Prep - growth metrics + secondary fundamentals"""
    name = 'fmp'

    def __init__(self):
        self.api_key = os.environ.get('FMP_API_KEY', '')

    def get_fundamentals(self, ticker: str) -> FundamentalsResult:
        """
        Fetch fundamentals from FMP: key-metrics-ttm + financial-growth.
        Makes 2 API calls per ticker to get complete data.
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            # Call 1: Core metrics (PE, ROE, margins, etc.)
            metrics_data = self._fetch_key_metrics(ticker)

            # Call 2: Growth rates (epsGrowth, revenueGrowth)
            growth_data = self._fetch_growth(ticker)

            # Merge: metrics as base, growth fills gaps
            normalized = apply_field_map(metrics_data, FMP_FUNDAMENTALS)
            growth_normalized = apply_field_map(growth_data, FMP_GROWTH)

            # Fill growth fields
            for field, value in growth_normalized.items():
                if value is not None and normalized.get(field) is None:
                    normalized[field] = value

            normalized['source'] = self.name

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

    def get_growth_only(self, ticker: str) -> dict:
        """
        Fetch ONLY growth metrics (epsGrowth, revenueGrowth).
        Used by orchestrator to fill gaps left by Finnhub.
        Costs 1 API call instead of 2.
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            growth_data = self._fetch_growth(ticker)
            normalized = apply_field_map(growth_data, FMP_GROWTH)
            breaker.record_success()
            return normalized
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def _fetch_key_metrics(self, ticker: str) -> dict:
        """GET /key-metrics-ttm/{ticker}"""
        url = f"{BASE_URL}/key-metrics-ttm/{ticker}"
        params = {'apikey': self.api_key}

        resp = requests.get(url, params=params, timeout=10)
        self._handle_http_errors(resp, ticker)

        data = resp.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        if isinstance(data, dict):
            return data

        raise DataNotFoundError(self.name, "Empty key-metrics response", ticker)

    def _fetch_growth(self, ticker: str) -> dict:
        """GET /financial-growth/{ticker}?period=annual&limit=1"""
        # Check rate limit again for the second call
        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit on 2nd call")

        url = f"{BASE_URL}/financial-growth/{ticker}"
        params = {
            'period': 'annual',
            'limit': 1,
            'apikey': self.api_key,
        }

        resp = requests.get(url, params=params, timeout=10)
        self._handle_http_errors(resp, ticker)

        data = resp.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        if isinstance(data, dict):
            return data

        # Growth data not available is not fatal - return empty
        return {}

    def _handle_http_errors(self, resp, ticker: str):
        """Handle HTTP-level errors"""
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
            raise AuthenticationError(self.name, "FMP_API_KEY not set")

        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded")
