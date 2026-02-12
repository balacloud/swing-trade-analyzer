"""
Provider Exception Hierarchy - v4.14 Multi-Source Data Intelligence

All provider-specific errors inherit from ProviderError.
The orchestrator catches these to decide whether to failover or serve stale cache.
"""


class ProviderError(Exception):
    """Base exception for all provider errors"""

    def __init__(self, provider: str, message: str, ticker: str = None):
        self.provider = provider
        self.ticker = ticker
        super().__init__(f"[{provider}] {message}" + (f" (ticker={ticker})" if ticker else ""))


class RateLimitError(ProviderError):
    """Provider rate limit exceeded - skip to next provider immediately"""
    pass


class AuthenticationError(ProviderError):
    """Invalid or missing API key - provider unusable until key is fixed"""
    pass


class DataNotFoundError(ProviderError):
    """Ticker not found or no data available from this provider"""
    pass


class ProviderUnavailableError(ProviderError):
    """Provider is down or unreachable (network error, 5xx, timeout)"""
    pass


class InsufficientDataError(ProviderError):
    """Provider returned data but not enough for our needs (e.g., < 150 bars)"""
    pass
