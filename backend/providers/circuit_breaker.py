"""
Circuit Breaker - v4.14 Multi-Source Data Intelligence
SQLite-backed (Day 82, data-source audit follow-up)

Per-provider circuit breaker to avoid hammering providers that are down.

Day 82: state persisted to SQLite (backend/data/provider_state.db, same
file as rate_limiter.py) instead of in-process memory — same reasoning as
the rate limiter: the Flask server, the launchd daily job, and any CLI
script previously had independent breaker state, so one process tripping
a breaker (3 consecutive TwelveData failures, say) was invisible to every
other process, which would keep hammering a provider already known to be
down. Public API (CircuitBreaker, CircuitState, get_breaker,
is_provider_available, all_breaker_status) is unchanged.

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

import os
import sqlite3
import time
import threading
from enum import Enum
from typing import Dict

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'provider_state.db'
)

_init_lock = threading.Lock()
_initialized = False


class CircuitState(Enum):
    CLOSED = 'closed'
    OPEN = 'open'
    HALF_OPEN = 'half_open'


def _get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def _ensure_schema():
    global _initialized
    if _initialized:
        return
    with _init_lock:
        if _initialized:
            return
        conn = _get_conn()
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS circuit_breaker_state (
                    provider TEXT PRIMARY KEY,
                    state TEXT NOT NULL DEFAULT 'closed',
                    failure_count INTEGER NOT NULL DEFAULT 0,
                    success_count INTEGER NOT NULL DEFAULT 0,
                    last_failure_time REAL
                )
            ''')
            conn.commit()
        finally:
            conn.close()
        _initialized = True


class CircuitBreaker:
    """Circuit breaker for a single provider. State lives in SQLite, shared
    across every process."""

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
        _ensure_schema()

    def _read_state(self, conn) -> dict:
        row = conn.execute(
            'SELECT state, failure_count, success_count, last_failure_time '
            'FROM circuit_breaker_state WHERE provider = ?',
            (self.provider,)
        ).fetchone()
        if row is None:
            return {'state': 'closed', 'failure_count': 0, 'success_count': 0,
                    'last_failure_time': None}
        return dict(row)

    def _write_state(self, conn, s: dict):
        conn.execute('''
            INSERT INTO circuit_breaker_state
                (provider, state, failure_count, success_count, last_failure_time)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(provider) DO UPDATE SET
                state=excluded.state, failure_count=excluded.failure_count,
                success_count=excluded.success_count, last_failure_time=excluded.last_failure_time
        ''', (self.provider, s['state'], s['failure_count'], s['success_count'], s['last_failure_time']))

    def _auto_transition(self, s: dict) -> dict:
        """OPEN -> HALF_OPEN once recovery_timeout has elapsed since the last failure."""
        if s['state'] == 'open' and s['last_failure_time'] is not None:
            elapsed = time.time() - s['last_failure_time']
            if elapsed >= self.recovery_timeout:
                s['state'] = 'half_open'
                s['success_count'] = 0
                print(f"🔄 Circuit breaker [{self.provider}]: OPEN → HALF_OPEN (recovery probe)")
        return s

    @property
    def state(self) -> CircuitState:
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            s = self._auto_transition(self._read_state(conn))
            self._write_state(conn, s)
            conn.commit()
            return CircuitState(s['state'])
        finally:
            conn.close()

    def allow_request(self) -> bool:
        """Can we send a request through this circuit?"""
        current = self.state  # Triggers auto-transition check
        if current == CircuitState.CLOSED:
            return True
        if current == CircuitState.HALF_OPEN:
            return True  # Allow probe request
        return False  # OPEN -> block

    def record_success(self):
        """Record a successful request."""
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            s = self._read_state(conn)
            if s['state'] == 'half_open':
                s['success_count'] += 1
                if s['success_count'] >= self.success_threshold:
                    s['state'] = 'closed'
                    s['failure_count'] = 0
                    s['success_count'] = 0
                    print(f"✅ Circuit breaker [{self.provider}]: HALF_OPEN → CLOSED (recovered)")
            else:
                s['failure_count'] = 0
            self._write_state(conn, s)
            conn.commit()
        finally:
            conn.close()

    def record_failure(self):
        """Record a failed request."""
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            s = self._read_state(conn)
            if s['state'] == 'half_open':
                s['state'] = 'open'
                s['last_failure_time'] = time.time()
                s['success_count'] = 0
                print(f"❌ Circuit breaker [{self.provider}]: HALF_OPEN → OPEN (probe failed)")
            else:
                s['failure_count'] += 1
                if s['failure_count'] >= self.failure_threshold:
                    s['state'] = 'open'
                    s['last_failure_time'] = time.time()
                    print(f"🔴 Circuit breaker [{self.provider}]: CLOSED → OPEN "
                          f"({s['failure_count']} consecutive failures)")
            self._write_state(conn, s)
            conn.commit()
        finally:
            conn.close()

    def trip(self):
        """Immediately open the circuit breaker (permanent failure, e.g. deprecated API plan)."""
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            s = {'state': 'open', 'failure_count': self.failure_threshold,
                 'success_count': 0, 'last_failure_time': time.time()}
            self._write_state(conn, s)
            conn.commit()
            print(f"⛔ Circuit breaker [{self.provider}]: tripped permanently (deprecated/auth failure)")
        finally:
            conn.close()

    def reset(self):
        """Manually reset circuit to CLOSED."""
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            s = {'state': 'closed', 'failure_count': 0, 'success_count': 0, 'last_failure_time': None}
            self._write_state(conn, s)
            conn.commit()
        finally:
            conn.close()

    def status(self) -> Dict:
        """Current circuit breaker status for diagnostics."""
        current = self.state
        conn = _get_conn()
        try:
            s = self._read_state(conn)
        finally:
            conn.close()
        return {
            'state': current.value,
            'failure_count': s['failure_count'],
            'success_count': s['success_count'],
            'failure_threshold': self.failure_threshold,
            'recovery_timeout_sec': self.recovery_timeout,
        }


# =============================================================================
# GLOBAL CIRCUIT BREAKERS (one lightweight object per provider per process;
# underlying state is shared across all processes via SQLite)
# =============================================================================

_breakers: Dict[str, CircuitBreaker] = {}
_global_lock = threading.Lock()


def get_breaker(provider: str) -> CircuitBreaker:
    """Get or create circuit breaker for a provider (thread-safe singleton per process)."""
    with _global_lock:
        if provider not in _breakers:
            _breakers[provider] = CircuitBreaker(provider)
        return _breakers[provider]


def is_provider_available(provider: str) -> bool:
    """Quick check: is this provider's circuit allowing requests?"""
    return get_breaker(provider).allow_request()


def all_breaker_status() -> Dict[str, Dict]:
    """Get status of all circuit breakers touched by this process."""
    return {name: breaker.status() for name, breaker in _breakers.items()}
