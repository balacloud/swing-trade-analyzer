"""
Attempt log (Day 136, Data Sources tab provenance). Plan: docs/claude/design/DATA_SOURCES_PROVENANCE_PLAN_DAY136.md

The tab used to read only the cache, so "never fetched" and "just failed" looked the same. This keeps ONE row per
(ticker, data_type): when a real provider last answered, when the chain last failed, and whether saved prices were served.

Rules (Opus review, Day 136):
- Best-effort. A logging problem must NEVER break or slow a fetch: short SQLite timeout, every error caught and printed
  with the ticker, nothing raised.
- Detail text holds provider names and exception CLASS names only, never str(e) (a URL in an error text can carry a key).
- A cache hit records nothing: a cache hit is not a check. "last_ok" means a real provider answered.
- Same shared file as circuit_breaker.py / rate_limiter.py (provider_state.db), so the server, the launchd job and CLI
  scripts all see one record. The journal mode of that shared file is NOT changed here.
- Tests redirect DB_PATH (and reset _initialized); a guard test fails if a test writes the real path.
"""

import os
import re
import sqlite3
import threading
import time
from typing import Optional

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'provider_state.db'
)
WRITE_TIMEOUT_SECONDS = 0.5   # a locked DB must not stall an Analyze load (the shared file's own timeout is 10 s)
DETAIL_MAX_CHARS = 200

_init_lock = threading.Lock()
_initialized = False

_SAFE = re.compile(r'[^A-Za-z0-9_.\-]')


def _clean(text) -> str:
    """Names only: strip anything that is not a plain identifier character."""
    return _SAFE.sub('', str(text or ''))[:60]


def describe_error(provider, exc) -> str:
    """'provider:ExceptionClass'. Never the message text (Golden Rule 67)."""
    return f"{_clean(provider) or 'unknown'}:{_clean(type(exc).__name__)}"


def _join_detail(parts) -> str:
    return '; '.join(p for p in parts if p)[:DETAIL_MAX_CHARS]


def _conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH, timeout=WRITE_TIMEOUT_SECONDS)


def _ensure_schema(conn) -> None:
    global _initialized
    if _initialized:
        return
    with _init_lock:
        if _initialized:
            return
        conn.execute('''
            CREATE TABLE IF NOT EXISTS fetch_attempts (
                ticker TEXT NOT NULL,
                data_type TEXT NOT NULL,
                period TEXT,
                last_ok_ts REAL,
                last_ok_provider TEXT,
                last_ok_detail TEXT,
                last_fail_ts REAL,
                last_fail_detail TEXT,
                served_stale INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (ticker, data_type)
            )
        ''')
        conn.commit()
        _initialized = True


def _write(sql: str, params: tuple, ticker: str, what: str, data_type: str) -> bool:
    try:
        conn = _conn()
        try:
            _ensure_schema(conn)
            conn.execute(sql, params)
            conn.commit()
        finally:
            conn.close()
        return True
    except Exception as e:   # never raise into a fetch; say so loudly (no message text: keep keys out of logs)
        print(f"⚠️ attempt_log {what} failed for {ticker} ({data_type}): {type(e).__name__}")
        return False


def record_ok(ticker: str, data_type: str, provider: str, period: Optional[str] = None, detail: str = '') -> bool:
    """A real provider answered. Clears served_stale. `detail` is for partial answers (names only)."""
    ticker = (ticker or '').upper()
    return _write(
        '''INSERT INTO fetch_attempts (ticker, data_type, period, last_ok_ts, last_ok_provider, last_ok_detail, served_stale)
           VALUES (?, ?, ?, ?, ?, ?, 0)
           ON CONFLICT(ticker, data_type) DO UPDATE SET
               period = excluded.period, last_ok_ts = excluded.last_ok_ts,
               last_ok_provider = excluded.last_ok_provider, last_ok_detail = excluded.last_ok_detail,
               served_stale = 0''',
        (ticker, data_type, period, time.time(), _clean(provider), _join_detail([detail])),
        ticker, 'record_ok', data_type)


def record_fail(ticker: str, data_type: str, detail: str, period: Optional[str] = None, served_stale: bool = False) -> bool:
    """The chain gave no fresh answer. `detail` = names only (use describe_error)."""
    ticker = (ticker or '').upper()
    return _write(
        '''INSERT INTO fetch_attempts (ticker, data_type, period, last_fail_ts, last_fail_detail, served_stale)
           VALUES (?, ?, ?, ?, ?, ?)
           ON CONFLICT(ticker, data_type) DO UPDATE SET
               period = excluded.period, last_fail_ts = excluded.last_fail_ts,
               last_fail_detail = excluded.last_fail_detail, served_stale = excluded.served_stale''',
        (ticker, data_type, period, time.time(), _join_detail([detail]), 1 if served_stale else 0),
        ticker, 'record_fail', data_type)


def read(ticker: str, data_type: str) -> dict:
    """state: 'never' (no row, or the log could not be read: say which in `error`), 'ok', or 'failed'.
    'failed' = the last fail is newer than the last ok. Times are epoch UTC; the screen formats them."""
    ticker = (ticker or '').upper()
    out = {'state': 'never', 'last_ok_ts': None, 'last_ok_provider': None, 'last_ok_detail': None,
           'last_fail_ts': None, 'detail': None, 'served_stale': False, 'period': None, 'error': None}
    try:
        if not os.path.exists(DB_PATH):
            return out
        conn = _conn()
        try:
            _ensure_schema(conn)
            conn.row_factory = sqlite3.Row
            row = conn.execute('SELECT * FROM fetch_attempts WHERE ticker = ? AND data_type = ?',
                               (ticker, data_type)).fetchone()
        finally:
            conn.close()
    except Exception as e:
        print(f"⚠️ attempt_log read failed for {ticker} ({data_type}): {type(e).__name__}")
        out['error'] = type(e).__name__   # unreadable is NOT the same as never fetched
        return out
    if row is None:
        return out
    ok_ts, fail_ts = row['last_ok_ts'], row['last_fail_ts']
    out.update(last_ok_ts=ok_ts, last_ok_provider=row['last_ok_provider'], last_ok_detail=row['last_ok_detail'] or None,
               last_fail_ts=fail_ts, detail=row['last_fail_detail'], served_stale=bool(row['served_stale']),
               period=row['period'])
    out['state'] = 'failed' if (fail_ts is not None and (ok_ts is None or fail_ts > ok_ts)) else 'ok'
    return out
