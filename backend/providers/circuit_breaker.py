"""
Circuit Breaker - v4.14 Multi-Source Data Intelligence

Per-provider circuit breaker to avoid hammering providers that are down.

States:
  CLOSED    → Normal operation. Requests pass through.
  OPEN      → Provider is down. All requests fail fast (no API call).
  HALF_OPEN → Recovery probe. Allow ONE request through to test.

Transitions:
  CLOSED → OPEN:      After `failure_threshold` consecutive failures (default 3)
  OPEN → HALF_OPEN:   After `recovery_timeout` seconds (default 300 = 5 min)
  HALF_OPEN → CLOSED: After `success_threshold` consecutive successes (default 2)
  HALF_OPEN → OPEN:   On any failure (back to waiting)
"""

import time
import threading
from enum import Enum
from typing import Dict, Optional


class CircuitState(Enum):
    CLOSED = 'closed'
    OPEN = 'open'
    HALF_OPEN = 'half_open'


class CircuitBreaker:
    """Thread-safe circuit breaker for a single provider"""

    def __init__(
        self,
        provider: str,
        failure_threshold: int = 3,
        recovery_timeout: float = 300.0,
        success_threshold: int = 2
    ):
        self.provider = provider
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold

        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._success_count = 0
        self._last_failure_time: Optional[float] = None
        self._lock = threading.Lock()

    @property
    def state(self) -> CircuitState:
        with self._lock:
            # Auto-transition OPEN → HALF_OPEN after recovery timeout
            if self._state == CircuitState.OPEN and self._last_failure_time:
                elapsed = time.monotonic() - self._last_failure_time
                if elapsed >= self.recovery_timeout:
                    self._state = CircuitState.HALF_OPEN
                    self._success_count = 0
                    print(f"🔄 Circuit breaker [{self.provider}]: OPEN → HALF_OPEN (recovery probe)")
            return self._state

    def allow_request(self) -> bool:
        """Can we send a request through this circuit?"""
        current = self.state  # Triggers auto-transition check
        if current == CircuitState.CLOSED:
            return True
        if current == CircuitState.HALF_OPEN:
            return True  # Allow probe request
        return False  # OPEN → block

    def record_success(self):
        """Record a successful request"""
        with self._lock:
            if self._state == CircuitState.HALF_OPEN:
                self._success_count += 1
                if self._success_count >= self.success_threshold:
                    self._state = CircuitState.CLOSED
                    self._failure_count = 0
                    self._success_count = 0
                    print(f"✅ Circuit breaker [{self.provider}]: HALF_OPEN → CLOSED (recovered)")
            else:
                # Normal success in CLOSED state - reset failure counter
                self._failure_count = 0

    def record_failure(self):
        """Record a failed request"""
        with self._lock:
            if self._state == CircuitState.HALF_OPEN:
                # Probe failed - go back to OPEN
                self._state = CircuitState.OPEN
                self._last_failure_time = time.monotonic()
                self._success_count = 0
                print(f"❌ Circuit breaker [{self.provider}]: HALF_OPEN → OPEN (probe failed)")
            else:
                self._failure_count += 1
                if self._failure_count >= self.failure_threshold:
                    self._state = CircuitState.OPEN
                    self._last_failure_time = time.monotonic()
                    print(f"🔴 Circuit breaker [{self.provider}]: CLOSED → OPEN "
                          f"({self._failure_count} consecutive failures)")

    def reset(self):
        """Manually reset circuit to CLOSED"""
        with self._lock:
            self._state = CircuitState.CLOSED
            self._failure_count = 0
            self._success_count = 0
            self._last_failure_time = None

    def status(self) -> Dict:
        """Current circuit breaker status for diagnostics"""
        current = self.state
        return {
            'state': current.value,
            'failure_count': self._failure_count,
            'success_count': self._success_count,
            'failure_threshold': self.failure_threshold,
            'recovery_timeout_sec': self.recovery_timeout,
        }


# =============================================================================
# GLOBAL CIRCUIT BREAKERS (singleton per provider)
# =============================================================================

_breakers: Dict[str, CircuitBreaker] = {}
_global_lock = threading.Lock()


def get_breaker(provider: str) -> CircuitBreaker:
    """Get or create circuit breaker for a provider (thread-safe singleton)"""
    with _global_lock:
        if provider not in _breakers:
            _breakers[provider] = CircuitBreaker(provider)
        return _breakers[provider]


def is_provider_available(provider: str) -> bool:
    """Quick check: is this provider's circuit allowing requests?"""
    return get_breaker(provider).allow_request()


def all_breaker_status() -> Dict[str, Dict]:
    """Get status of all circuit breakers"""
    return {name: breaker.status() for name, breaker in _breakers.items()}
