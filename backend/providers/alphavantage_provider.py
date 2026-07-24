"""
Alpha Vantage Provider - Growth Metrics (revenueGrowth, epsGrowth)

Replaces FMP's growth role since FMP v3 was deprecated Aug 2025.
Alpha Vantage key is already in .env — no new account needed.

Free tier: 5 req/min, 25 req/day.
Each ticker = 2 API calls (INCOME_STATEMENT + EARNINGS).
Fundamentals cached 7 days → ~12 fresh tickers/day before hitting daily limit.

Endpoints:
  INCOME_STATEMENT → quarterly revenue → YoY revenueGrowth (Q[0] vs Q[4])
  EARNINGS         → quarterly EPS     → YoY epsGrowth    (Q[0] vs Q[4])
"""

import os
import requests

from .base import FundamentalsProvider, FundamentalsResult
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError,
    RateLimitError, AuthenticationError, ProviderError
)
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


BASE_URL = 'https://www.alphavantage.co/query'


def _safe_float(val):
    try:
        if val is None or val == 'None' or val == 'N/A':
            return None
        return float(val)
    except (TypeError, ValueError):
        return None


class AlphaVantageProvider(FundamentalsProvider):
    """
    Alpha Vantage — provides revenueGrowth + epsGrowth YoY only.
    Used to fill the growth gaps that Finnhub leaves, same role FMP played.
    """
    name = 'alphavantage'

    def __init__(self):
        self.api_key = os.environ.get('ALPHAVANTAGE_API_KEY', '')

    def get_fundamentals(self, ticker: str) -> FundamentalsResult:
        """
        Fetch growth metrics from Alpha Vantage.
        Returns only epsGrowth + revenueGrowth — that's all AV is used for.
        """
        self._check_availability()
        breaker = get_breaker(self.name)

        data = {}

        # Fetch revenue growth (1 API call)
        try:
            data['revenueGrowth'] = self._fetch_revenue_growth(ticker)
        except ProviderError:
            pass  # EPS fetch still attempted even if this fails

        # Fetch EPS growth (1 API call)
        try:
            data['epsGrowth'] = self._fetch_eps_growth(ticker)
        except ProviderError:
            pass

        if not any(v is not None for v in data.values()):
            # Ticker-specific, not a health signal — don't count it (Day 95).
            raise DataNotFoundError(self.name, "No growth data returned", ticker)

        breaker.record_success()
        data['source'] = self.name
        field_sources = {k: self.name for k, v in data.items() if v is not None and k != 'source'}

        return FundamentalsResult(
            data=data, source=self.name, ticker=ticker, field_sources=field_sources
        )

    def get_growth_only(self, ticker: str) -> dict:
        """
        Alias used by orchestrator's gap-filling path. Returns only the
        actual growth fields — excludes the 'source' metadata key that
        get_fundamentals() embeds in the same dict.

        Day 82 data-source audit fix: that 'source' key was leaking through
        the orchestrator's merge loop (backend/providers/orchestrator.py's
        get_fundamentals()) as if it were a real fundamentals field —
        merged_data.get('source') is None (not in FUNDAMENTALS_SCHEMA), so
        the loop happily set merged_data['source']='alphavantage' and
        field_sources['source']='alphavantage', inflating the "AlphaVantage
        filled N growth fields" log count by one and adding a spurious,
        confusing entry to the _field_sources provenance dict (later
        silently overwritten by the real source value, so no data
        corruption — just noisy/wrong provenance metadata).
        """
        result = self.get_fundamentals(ticker)
        return {k: v for k, v in result.data.items() if k != 'source'}

    # -------------------------------------------------------------------------
    # Private fetch helpers
    # -------------------------------------------------------------------------

    def _fetch_revenue_growth(self, ticker: str):
        """
        Calls INCOME_STATEMENT endpoint.
        YoY = (Q[0].totalRevenue - Q[4].totalRevenue) / abs(Q[4].totalRevenue) * 100
        """
        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded", ticker)

        resp = requests.get(BASE_URL, params={
            'function': 'INCOME_STATEMENT',
            'symbol': ticker,
            'apikey': self.api_key,
        }, timeout=15)
        self._handle_http_errors(resp, ticker)

        data = resp.json()
        self._check_av_response(data, ticker)

        quarters = data.get('quarterlyReports', [])
        if len(quarters) < 5:
            return None

        current  = _safe_float(quarters[0].get('totalRevenue'))
        year_ago = _safe_float(quarters[4].get('totalRevenue'))
        if current and year_ago and year_ago != 0:
            return round(((current - year_ago) / abs(year_ago)) * 100, 2)
        return None

    def _fetch_eps_growth(self, ticker: str):
        """
        Calls EARNINGS endpoint.
        YoY = (Q[0].reportedEPS - Q[4].reportedEPS) / abs(Q[4].reportedEPS) * 100
        """
        if not check_rate_limit(self.name):
            raise RateLimitError(self.name, "Rate limit exceeded", ticker)

        resp = requests.get(BASE_URL, params={
            'function': 'EARNINGS',
            'symbol': ticker,
            'apikey': self.api_key,
        }, timeout=15)
        self._handle_http_errors(resp, ticker)

        data = resp.json()
        self._check_av_response(data, ticker)

        quarters = data.get('quarterlyEarnings', [])
        if len(quarters) < 5:
            return None

        current  = _safe_float(quarters[0].get('reportedEPS'))
        year_ago = _safe_float(quarters[4].get('reportedEPS'))
        if current and year_ago and year_ago != 0:
            return round(((current - year_ago) / abs(year_ago)) * 100, 2)
        return None

    def _check_av_response(self, data: dict, ticker: str):
        """Detect AV-specific soft errors (rate limit in body, unknown symbol)."""
        if 'Note' in data:
            # AV returns rate limit messages in body with HTTP 200
            get_breaker(self.name).record_failure()
            raise RateLimitError(self.name, data['Note'][:100], ticker)
        if 'Information' in data:
            msg = data['Information']
            get_breaker(self.name).record_failure()
            raise RateLimitError(self.name, msg[:100], ticker)
        if 'Error Message' in data:
            raise DataNotFoundError(self.name, data['Error Message'][:80], ticker)

    def _handle_http_errors(self, resp, ticker: str):
        """Handle HTTP-level errors."""
        breaker = get_breaker(self.name)
        if resp.status_code == 429:
            breaker.record_failure()
            raise RateLimitError(self.name, "HTTP 429", ticker)
        if resp.status_code in (401, 403):
            breaker.record_failure()
            raise AuthenticationError(self.name, f"HTTP {resp.status_code}", ticker)
        if resp.status_code >= 500:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, f"HTTP {resp.status_code}", ticker)
        resp.raise_for_status()

    def _check_availability(self):
        """
        Key + circuit-breaker check only — does NOT consume a rate-limit
        token. Day 82 data-source audit fix: this used to also call
        check_rate_limit(), which acquires a real token even though no HTTP
        request happens here. get_fundamentals() makes 2 real calls
        (_fetch_revenue_growth, _fetch_eps_growth), each of which already
        does its own check_rate_limit() right before its request — the
        third check here was spending 3 tokens for 2 real calls, self-
        throttling AlphaVantage's 25/day free tier to ~8 tickers/day
        instead of the ~12 it should support.
        """
        if not self.api_key:
            raise AuthenticationError(self.name, "ALPHAVANTAGE_API_KEY not set")
        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")
