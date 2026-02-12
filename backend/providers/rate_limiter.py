"""
Token-Bucket Rate Limiter - v4.14 Multi-Source Data Intelligence

Per-provider rate limiting to stay within free tier quotas.
Uses token bucket algorithm: tokens refill at a steady rate,
each request consumes one token.

Free tier limits (Feb 2026):
  TwelveData:     8/min  + 800/day
  Finnhub:        60/min (unlimited daily on free)
  FMP:            10/min + 250/day
  yfinance:       ~30/min (unofficial, conservative)
  Stooq:          ~5/min  (very conservative)
  Alpha Vantage:  5/min  + 25/day (nearly useless)
"""

import time
import threading
from typing import Dict


class TokenBucket:
    """Thread-safe token bucket for rate limiting"""

    def __init__(self, rate_per_minute: int, daily_limit: int = 0):
        """
        Args:
            rate_per_minute: Max requests per minute
            daily_limit: Max requests per day (0 = unlimited)
        """
        self.rate_per_minute = rate_per_minute
        self.daily_limit = daily_limit

        # Token bucket state
        self.tokens = rate_per_minute
        self.max_tokens = rate_per_minute
        self.refill_interval = 60.0 / rate_per_minute  # seconds between refills
        self.last_refill = time.monotonic()

        # Daily counter
        self.daily_count = 0
        self.daily_reset_time = time.monotonic()

        self._lock = threading.Lock()

    def _refill(self):
        """Refill tokens based on elapsed time"""
        now = time.monotonic()
        elapsed = now - self.last_refill
        new_tokens = elapsed / self.refill_interval
        if new_tokens >= 1:
            self.tokens = min(self.max_tokens, self.tokens + int(new_tokens))
            self.last_refill = now

        # Reset daily counter every 24 hours
        if now - self.daily_reset_time >= 86400:
            self.daily_count = 0
            self.daily_reset_time = now

    def acquire(self) -> bool:
        """
        Try to acquire a token. Returns True if allowed, False if rate-limited.
        Non-blocking - caller decides what to do on failure.
        """
        with self._lock:
            self._refill()

            # Check daily limit
            if self.daily_limit > 0 and self.daily_count >= self.daily_limit:
                return False

            # Check per-minute tokens
            if self.tokens < 1:
                return False

            self.tokens -= 1
            self.daily_count += 1
            return True

    def wait_time(self) -> float:
        """How many seconds until next token is available"""
        with self._lock:
            self._refill()
            if self.tokens >= 1:
                return 0.0
            return self.refill_interval

    @property
    def remaining_daily(self) -> int:
        """Remaining daily quota (0 = unlimited/exhausted)"""
        if self.daily_limit == 0:
            return -1  # Unlimited
        return max(0, self.daily_limit - self.daily_count)

    def status(self) -> Dict:
        """Current rate limiter status for diagnostics"""
        with self._lock:
            self._refill()
            return {
                'tokens_available': self.tokens,
                'max_per_minute': self.rate_per_minute,
                'daily_used': self.daily_count,
                'daily_limit': self.daily_limit or 'unlimited',
                'daily_remaining': self.remaining_daily if self.daily_limit else 'unlimited',
            }


# =============================================================================
# PRE-CONFIGURED LIMITERS (singleton per provider)
# =============================================================================

_limiters: Dict[str, TokenBucket] = {}
_global_lock = threading.Lock()


PROVIDER_LIMITS = {
    'twelvedata':    {'rate_per_minute': 8,  'daily_limit': 800},
    'finnhub':       {'rate_per_minute': 60, 'daily_limit': 0},
    'fmp':           {'rate_per_minute': 10, 'daily_limit': 250},
    'yfinance':      {'rate_per_minute': 30, 'daily_limit': 0},
    'stooq':         {'rate_per_minute': 5,  'daily_limit': 0},
    'alphavantage':  {'rate_per_minute': 5,  'daily_limit': 25},
}


def get_limiter(provider: str) -> TokenBucket:
    """Get or create rate limiter for a provider (thread-safe singleton)"""
    with _global_lock:
        if provider not in _limiters:
            limits = PROVIDER_LIMITS.get(provider, {'rate_per_minute': 10, 'daily_limit': 0})
            _limiters[provider] = TokenBucket(**limits)
        return _limiters[provider]


def check_rate_limit(provider: str) -> bool:
    """Quick check: can we make a request to this provider right now?"""
    return get_limiter(provider).acquire()


def all_limiter_status() -> Dict[str, Dict]:
    """Get status of all active rate limiters"""
    return {name: limiter.status() for name, limiter in _limiters.items()}
