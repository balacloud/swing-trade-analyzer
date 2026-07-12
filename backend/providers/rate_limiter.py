"""
Token-Bucket Rate Limiter - v4.14 Multi-Source Data Intelligence
SQLite-backed (Day 82, data-source audit follow-up)

Per-provider rate limiting to stay within free tier quotas.
Uses token bucket algorithm: tokens refill at a steady rate,
each request consumes one token.

Day 82: state persisted to SQLite (backend/data/provider_state.db) instead
of in-process memory. Previously every process (the Flask server, the
launchd daily job, any CLI script) had its own independent in-memory
TokenBucket — AlphaVantage's 25/day cap, for example, was only ever
enforced within whichever process happened to make the call, not truly
25/day project-wide. Public API (TokenBucket, get_limiter, check_rate_limit,
all_limiter_status) is unchanged, so no provider file needs to change.

Free tier limits (Feb 2026):
  TwelveData:     8/min  + 800/day
  Finnhub:        60/min (unlimited daily on free)
  FMP:            10/min + 250/day
  yfinance:       ~30/min (unofficial, conservative)
  Stooq:          ~5/min  (very conservative) — disabled Day 82, see orchestrator.py
  Alpha Vantage:  5/min  + 25/day (nearly useless)
"""

import os
import sqlite3
import time
import threading
from typing import Dict

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'provider_state.db'
)

_init_lock = threading.Lock()
_initialized = False


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
                CREATE TABLE IF NOT EXISTS rate_limit_state (
                    provider TEXT PRIMARY KEY,
                    tokens REAL NOT NULL,
                    last_refill REAL NOT NULL,
                    daily_count INTEGER NOT NULL DEFAULT 0,
                    daily_reset_at REAL NOT NULL
                )
            ''')
            conn.commit()
        finally:
            conn.close()
        _initialized = True


class TokenBucket:
    """
    Token bucket for rate limiting a single provider. State lives in
    SQLite, not process memory, so it's shared across every process that
    touches this provider.
    """

    def __init__(self, provider: str, rate_per_minute: int, daily_limit: int = 0):
        self.provider = provider
        self.rate_per_minute = rate_per_minute
        self.daily_limit = daily_limit
        self.max_tokens = rate_per_minute
        self.refill_interval = 60.0 / rate_per_minute
        _ensure_schema()

    def _read_state(self, conn) -> dict:
        row = conn.execute(
            'SELECT tokens, last_refill, daily_count, daily_reset_at '
            'FROM rate_limit_state WHERE provider = ?',
            (self.provider,)
        ).fetchone()
        now = time.time()
        if row is None:
            return {'tokens': float(self.max_tokens), 'last_refill': now,
                    'daily_count': 0, 'daily_reset_at': now}
        return dict(row)

    def _refill(self, state: dict, now: float) -> dict:
        elapsed = now - state['last_refill']
        new_tokens = elapsed / self.refill_interval
        if new_tokens >= 1:
            state['tokens'] = min(self.max_tokens, state['tokens'] + int(new_tokens))
            state['last_refill'] = now
        if now - state['daily_reset_at'] >= 86400:
            state['daily_count'] = 0
            state['daily_reset_at'] = now
        return state

    def _write_state(self, conn, state: dict):
        conn.execute('''
            INSERT INTO rate_limit_state (provider, tokens, last_refill, daily_count, daily_reset_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(provider) DO UPDATE SET
                tokens=excluded.tokens, last_refill=excluded.last_refill,
                daily_count=excluded.daily_count, daily_reset_at=excluded.daily_reset_at
        ''', (self.provider, state['tokens'], state['last_refill'],
              state['daily_count'], state['daily_reset_at']))

    def acquire(self) -> bool:
        """
        Try to acquire a token. Returns True if allowed, False if rate-limited.
        Atomic across processes: BEGIN IMMEDIATE takes a write lock before
        reading, so two processes racing to acquire the last token can't
        both succeed.
        """
        conn = _get_conn()
        try:
            conn.execute('BEGIN IMMEDIATE')
            state = self._refill(self._read_state(conn), time.time())

            allowed = True
            if self.daily_limit > 0 and state['daily_count'] >= self.daily_limit:
                allowed = False
            if state['tokens'] < 1:
                allowed = False

            if allowed:
                state['tokens'] -= 1
                state['daily_count'] += 1

            self._write_state(conn, state)
            conn.commit()
            return allowed
        finally:
            conn.close()

    def wait_time(self) -> float:
        """How many seconds until next token is available (read-only)."""
        conn = _get_conn()
        try:
            state = self._refill(self._read_state(conn), time.time())
            return 0.0 if state['tokens'] >= 1 else self.refill_interval
        finally:
            conn.close()

    @property
    def remaining_daily(self) -> int:
        """Remaining daily quota (-1 = unlimited)."""
        if self.daily_limit == 0:
            return -1
        conn = _get_conn()
        try:
            state = self._refill(self._read_state(conn), time.time())
            return max(0, self.daily_limit - state['daily_count'])
        finally:
            conn.close()

    def status(self) -> Dict:
        """Current rate limiter status for diagnostics."""
        conn = _get_conn()
        try:
            state = self._refill(self._read_state(conn), time.time())
            daily_remaining = (max(0, self.daily_limit - state['daily_count'])
                                if self.daily_limit else 'unlimited')
            return {
                'tokens_available': state['tokens'],
                'max_per_minute': self.rate_per_minute,
                'daily_used': state['daily_count'],
                'daily_limit': self.daily_limit or 'unlimited',
                'daily_remaining': daily_remaining,
            }
        finally:
            conn.close()


# =============================================================================
# PRE-CONFIGURED LIMITERS (one lightweight object per provider per process;
# underlying quota state is shared across all processes via SQLite)
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
    """Get or create rate limiter for a provider (thread-safe singleton per process)."""
    with _global_lock:
        if provider not in _limiters:
            limits = PROVIDER_LIMITS.get(provider, {'rate_per_minute': 10, 'daily_limit': 0})
            _limiters[provider] = TokenBucket(provider, **limits)
        return _limiters[provider]


def check_rate_limit(provider: str) -> bool:
    """Quick check: can we make a request to this provider right now?"""
    return get_limiter(provider).acquire()


def all_limiter_status() -> Dict[str, Dict]:
    """Get status of all rate limiters touched by this process."""
    return {name: limiter.status() for name, limiter in _limiters.items()}
