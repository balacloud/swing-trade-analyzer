"""
Persistent Cache Manager - Day 36
SQLite-based caching for yfinance data with intelligent TTL

Design Principles:
1. Cache OHLCV and fundamentals separately (different TTLs)
2. Market-aware TTL: OHLCV expires after next market close
3. Fundamentals expire after 7 days (quarterly data)
4. All indicators (SMA, RSI, ATR, S&R) calculated from cached OHLCV
5. Survives restarts - SQLite persistence

Author: Claude Code
"""

import sqlite3
import json
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
import pytz

# Database location
DB_PATH = Path(__file__).parent / "data" / "cache.db"

# TTL Constants
OHLCV_TTL_HOURS = 24  # Will be adjusted to market close
FUNDAMENTALS_TTL_DAYS = 7
SPY_VIX_TTL_HOURS = 24

# Schema version — increment when field_maps.py transforms change
# Day 61: Added to prevent stale cache serving wrong format after transform updates
# v1 = original transforms, v2 = Day 60 _growth_to_pct + Day 61 NaN sanitization
FUNDAMENTALS_SCHEMA_VERSION = 2

# US Eastern timezone for market hours
ET = pytz.timezone('US/Eastern')


def get_db_connection():
    """Get SQLite connection, creating DB and tables if needed"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), timeout=10)
    conn.row_factory = sqlite3.Row
    _init_tables(conn)
    return conn


def _init_tables(conn):
    """Initialize cache tables if they don't exist"""
    cursor = conn.cursor()

    # OHLCV cache - stores time series data as JSON blob for simplicity
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ohlcv_cache (
            ticker TEXT PRIMARY KEY,
            data TEXT NOT NULL,           -- JSON: {date: {open, high, low, close, volume}}
            period TEXT DEFAULT '2y',     -- Period fetched (e.g., '2y', '1y')
            rows INTEGER,                 -- Number of data points
            source TEXT DEFAULT 'yfinance', -- Day 51: Data provider source
            cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL
        )
    """)

    # Day 51: Add source column to existing ohlcv_cache tables (migration)
    try:
        cursor.execute("ALTER TABLE ohlcv_cache ADD COLUMN source TEXT DEFAULT 'yfinance'")
    except Exception:
        pass  # Column already exists

    # Fundamentals cache
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fundamentals_cache (
            ticker TEXT PRIMARY KEY,
            data TEXT NOT NULL,           -- JSON blob of all fundamentals
            source TEXT DEFAULT 'yfinance',
            cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL
        )
    """)

    # Day 61: Add schema_version column (migration for existing DBs)
    try:
        cursor.execute("ALTER TABLE fundamentals_cache ADD COLUMN schema_version INTEGER DEFAULT 1")
    except Exception:
        pass  # Column already exists

    # Market data cache (SPY, VIX)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_cache (
            symbol TEXT PRIMARY KEY,
            data TEXT NOT NULL,           -- JSON blob
            cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL
        )
    """)

    # Cache statistics
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cache_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT,              -- 'hit', 'miss', 'expire', 'store'
            data_type TEXT,               -- 'ohlcv', 'fundamentals', 'market'
            ticker TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()


def get_next_market_close() -> datetime:
    """
    Get the next market close time (4:00 PM ET).
    If current time is after 4pm ET, return tomorrow's 4pm.
    If weekend, return Monday's 4pm.
    """
    now = datetime.now(ET)
    today_close = now.replace(hour=16, minute=0, second=0, microsecond=0)

    # If it's after market close, use tomorrow
    if now >= today_close:
        next_close = today_close + timedelta(days=1)
    else:
        next_close = today_close

    # Skip weekends
    while next_close.weekday() >= 5:  # Saturday=5, Sunday=6
        next_close += timedelta(days=1)

    return next_close


def calculate_ohlcv_expiry() -> datetime:
    """Calculate when OHLCV cache should expire (next market close + buffer)"""
    next_close = get_next_market_close()
    # Add 30 min buffer for data propagation
    return next_close + timedelta(minutes=30)


def calculate_fundamentals_expiry() -> datetime:
    """Calculate fundamentals expiry (7 days from now)"""
    return datetime.now(ET) + timedelta(days=FUNDAMENTALS_TTL_DAYS)


# =============================================================================
# OHLCV CACHE OPERATIONS
# =============================================================================

def get_cached_ohlcv(ticker: str) -> Optional[pd.DataFrame]:
    """
    Get OHLCV data from cache if not expired.
    Returns DataFrame or None if cache miss/expired.
    """
    ticker = ticker.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT data, expires_at, cached_at, rows
            FROM ohlcv_cache
            WHERE ticker = ?
        """, (ticker,))

        row = cursor.fetchone()
        if not row:
            _log_cache_event(conn, 'miss', 'ohlcv', ticker)
            return None

        expires_at = datetime.fromisoformat(row['expires_at'])
        now = datetime.now(ET)

        if now >= expires_at:
            _log_cache_event(conn, 'expire', 'ohlcv', ticker)
            print(f"⏰ OHLCV cache expired for {ticker}")
            return None

        # Cache hit - deserialize
        data_dict = json.loads(row['data'])
        df = pd.DataFrame.from_dict(data_dict, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()

        # Ensure correct column names (lowercase)
        df.columns = [c.lower() for c in df.columns]

        age_hours = (now - datetime.fromisoformat(row['cached_at']).replace(tzinfo=ET)).total_seconds() / 3600
        print(f"📦 OHLCV cache HIT for {ticker} ({row['rows']} rows, {age_hours:.1f}h old)")
        _log_cache_event(conn, 'hit', 'ohlcv', ticker)

        return df

    finally:
        conn.close()


def set_cached_ohlcv(ticker: str, df: pd.DataFrame, period: str = '2y', source: str = 'yfinance'):
    """Store OHLCV data in cache. Day 51: Added source parameter for provenance."""
    ticker = ticker.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Serialize DataFrame to JSON
        df_copy = df.copy()
        df_copy.index = df_copy.index.strftime('%Y-%m-%d')
        data_json = df_copy.to_dict(orient='index')

        expires_at = calculate_ohlcv_expiry()

        cursor.execute("""
            INSERT OR REPLACE INTO ohlcv_cache (ticker, data, period, rows, source, cached_at, expires_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            ticker,
            json.dumps(data_json),
            period,
            len(df),
            source,
            datetime.now(ET).isoformat(),
            expires_at.isoformat()
        ))

        conn.commit()
        _log_cache_event(conn, 'store', 'ohlcv', ticker)
        print(f"💾 Cached OHLCV for {ticker} ({len(df)} rows, expires {expires_at.strftime('%Y-%m-%d %H:%M')} ET)")

    finally:
        conn.close()


# =============================================================================
# FUNDAMENTALS CACHE OPERATIONS
# =============================================================================

def get_cached_fundamentals(ticker: str) -> Optional[Dict[str, Any]]:
    """Get fundamentals from cache if not expired and schema version matches"""
    ticker = ticker.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT data, expires_at, cached_at, source, schema_version
            FROM fundamentals_cache
            WHERE ticker = ?
        """, (ticker,))

        row = cursor.fetchone()
        if not row:
            _log_cache_event(conn, 'miss', 'fundamentals', ticker)
            return None

        # Day 61: Check schema version — reject stale format entries
        cached_version = row['schema_version'] if 'schema_version' in row.keys() else 1
        if cached_version != FUNDAMENTALS_SCHEMA_VERSION:
            print(f"🔄 Fundamentals cache STALE for {ticker} (schema v{cached_version} != v{FUNDAMENTALS_SCHEMA_VERSION})")
            # Delete the stale entry
            cursor.execute("DELETE FROM fundamentals_cache WHERE ticker = ?", (ticker,))
            conn.commit()
            _log_cache_event(conn, 'expire', 'fundamentals', ticker)
            return None

        expires_at = datetime.fromisoformat(row['expires_at'])
        now = datetime.now(ET)

        if now >= expires_at:
            _log_cache_event(conn, 'expire', 'fundamentals', ticker)
            print(f"⏰ Fundamentals cache expired for {ticker}")
            return None

        data = json.loads(row['data'])
        age_days = (now - datetime.fromisoformat(row['cached_at']).replace(tzinfo=ET)).total_seconds() / 86400
        print(f"📦 Fundamentals cache HIT for {ticker} ({age_days:.1f} days old, schema v{cached_version})")
        _log_cache_event(conn, 'hit', 'fundamentals', ticker)

        return data

    finally:
        conn.close()


def set_cached_fundamentals(ticker: str, data: Dict[str, Any], source: str = 'yfinance'):
    """Store fundamentals in cache with current schema version"""
    ticker = ticker.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        expires_at = calculate_fundamentals_expiry()

        cursor.execute("""
            INSERT OR REPLACE INTO fundamentals_cache (ticker, data, source, cached_at, expires_at, schema_version)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            ticker,
            json.dumps(data),
            source,
            datetime.now(ET).isoformat(),
            expires_at.isoformat(),
            FUNDAMENTALS_SCHEMA_VERSION
        ))

        conn.commit()
        _log_cache_event(conn, 'store', 'fundamentals', ticker)
        print(f"💾 Cached fundamentals for {ticker} (schema v{FUNDAMENTALS_SCHEMA_VERSION}, expires {expires_at.strftime('%Y-%m-%d')})")

    finally:
        conn.close()


# =============================================================================
# MARKET DATA CACHE (SPY, VIX)
# =============================================================================

def get_cached_market(symbol: str) -> Optional[Dict[str, Any]]:
    """Get market data (SPY/VIX) from cache"""
    symbol = symbol.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT data, expires_at, cached_at
            FROM market_cache
            WHERE symbol = ?
        """, (symbol,))

        row = cursor.fetchone()
        if not row:
            _log_cache_event(conn, 'miss', 'market', symbol)
            return None

        expires_at = datetime.fromisoformat(row['expires_at'])
        now = datetime.now(ET)

        if now >= expires_at:
            _log_cache_event(conn, 'expire', 'market', symbol)
            return None

        _log_cache_event(conn, 'hit', 'market', symbol)
        return json.loads(row['data'])

    finally:
        conn.close()


def set_cached_market(symbol: str, data: Dict[str, Any]):
    """Store market data in cache"""
    symbol = symbol.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        expires_at = calculate_ohlcv_expiry()  # Same TTL as OHLCV

        cursor.execute("""
            INSERT OR REPLACE INTO market_cache (symbol, data, cached_at, expires_at)
            VALUES (?, ?, ?, ?)
        """, (
            symbol,
            json.dumps(data),
            datetime.now(ET).isoformat(),
            expires_at.isoformat()
        ))

        conn.commit()
        _log_cache_event(conn, 'store', 'market', symbol)

    finally:
        conn.close()


# =============================================================================
# CACHE MANAGEMENT
# =============================================================================

def clear_cache(ticker: str = None, cache_type: str = None):
    """
    Clear cache entries.
    - ticker=None, cache_type=None: Clear everything
    - ticker='AAPL': Clear all cache for AAPL
    - cache_type='ohlcv': Clear all OHLCV cache
    - ticker='AAPL', cache_type='fundamentals': Clear AAPL fundamentals only
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        tables = {
            'ohlcv': 'ohlcv_cache',
            'fundamentals': 'fundamentals_cache',
            'market': 'market_cache'
        }

        if cache_type and cache_type in tables:
            table = tables[cache_type]
            if ticker:
                col = 'symbol' if cache_type == 'market' else 'ticker'
                cursor.execute(f"DELETE FROM {table} WHERE {col} = ?", (ticker.upper(),))
            else:
                cursor.execute(f"DELETE FROM {table}")
        elif ticker:
            # Clear all cache types for this ticker
            cursor.execute("DELETE FROM ohlcv_cache WHERE ticker = ?", (ticker.upper(),))
            cursor.execute("DELETE FROM fundamentals_cache WHERE ticker = ?", (ticker.upper(),))
            cursor.execute("DELETE FROM market_cache WHERE symbol = ?", (ticker.upper(),))
        else:
            # Clear everything
            cursor.execute("DELETE FROM ohlcv_cache")
            cursor.execute("DELETE FROM fundamentals_cache")
            cursor.execute("DELETE FROM market_cache")

        conn.commit()
        print(f"🗑️ Cache cleared (ticker={ticker}, type={cache_type})")

    finally:
        conn.close()


def get_cache_stats() -> Dict[str, Any]:
    """Get cache statistics"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        stats = {
            'ohlcv': {'count': 0, 'entries': []},
            'fundamentals': {'count': 0, 'entries': []},
            'market': {'count': 0, 'entries': []},
            'total_size_kb': 0
        }

        # OHLCV stats
        cursor.execute("""
            SELECT ticker, rows, source, cached_at, expires_at
            FROM ohlcv_cache
            ORDER BY ticker
        """)
        for row in cursor.fetchall():
            now = datetime.now(ET)
            expires = datetime.fromisoformat(row['expires_at'])
            is_expired = now >= expires
            stats['ohlcv']['entries'].append({
                'ticker': row['ticker'],
                'rows': row['rows'],
                'source': row['source'] if 'source' in row.keys() else 'yfinance',
                'cached_at': row['cached_at'],
                'expires_in': str(expires - now) if not is_expired else 'EXPIRED',
                'expired': is_expired
            })
        stats['ohlcv']['count'] = len(stats['ohlcv']['entries'])

        # Fundamentals stats
        cursor.execute("""
            SELECT ticker, source, cached_at, expires_at
            FROM fundamentals_cache
            ORDER BY ticker
        """)
        for row in cursor.fetchall():
            now = datetime.now(ET)
            expires = datetime.fromisoformat(row['expires_at'])
            is_expired = now >= expires
            stats['fundamentals']['entries'].append({
                'ticker': row['ticker'],
                'source': row['source'],
                'cached_at': row['cached_at'],
                'expires_in': str(expires - now) if not is_expired else 'EXPIRED',
                'expired': is_expired
            })
        stats['fundamentals']['count'] = len(stats['fundamentals']['entries'])

        # Market stats
        cursor.execute("""
            SELECT symbol, cached_at, expires_at
            FROM market_cache
            ORDER BY symbol
        """)
        for row in cursor.fetchall():
            now = datetime.now(ET)
            expires = datetime.fromisoformat(row['expires_at'])
            is_expired = now >= expires
            stats['market']['entries'].append({
                'symbol': row['symbol'],
                'cached_at': row['cached_at'],
                'expires_in': str(expires - now) if not is_expired else 'EXPIRED',
                'expired': is_expired
            })
        stats['market']['count'] = len(stats['market']['entries'])

        # Database size
        if DB_PATH.exists():
            stats['total_size_kb'] = round(DB_PATH.stat().st_size / 1024, 2)

        return stats

    finally:
        conn.close()


def _log_cache_event(conn, event_type: str, data_type: str, ticker: str):
    """Log cache event for analytics (optional)"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cache_stats (event_type, data_type, ticker)
            VALUES (?, ?, ?)
        """, (event_type, data_type, ticker))
        conn.commit()
    except:
        pass  # Don't fail on logging errors


def get_cache_hit_rate(hours: int = 24) -> Dict[str, float]:
    """Calculate cache hit rate for the last N hours"""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        since = (datetime.now(ET) - timedelta(hours=hours)).isoformat()

        cursor.execute("""
            SELECT data_type, event_type, COUNT(*) as cnt
            FROM cache_stats
            WHERE timestamp >= ?
            GROUP BY data_type, event_type
        """, (since,))

        results = {}
        counts = {}

        for row in cursor.fetchall():
            dtype = row['data_type']
            if dtype not in counts:
                counts[dtype] = {'hit': 0, 'miss': 0}
            counts[dtype][row['event_type']] = row['cnt']

        for dtype, c in counts.items():
            total = c['hit'] + c['miss']
            results[dtype] = round(c['hit'] / total * 100, 1) if total > 0 else 0.0

        return results

    finally:
        conn.close()


# =============================================================================
# PROVENANCE FUNCTIONS
# =============================================================================

def get_ticker_cache_info(ticker: str, cache_type: str) -> Optional[Dict[str, Any]]:
    """
    Get cache metadata for a specific ticker without the full data.
    Used by the Data Sources tab for provenance display.

    Args:
        ticker: Stock ticker symbol
        cache_type: 'ohlcv' or 'fundamentals'

    Returns:
        Dict with cached_at, expires_at, source (if fundamentals), expired status
        or None if not cached
    """
    ticker = ticker.upper()
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        now = datetime.now(ET)

        if cache_type == 'ohlcv':
            cursor.execute("""
                SELECT cached_at, expires_at, rows, period, source
                FROM ohlcv_cache WHERE ticker = ?
            """, (ticker,))
            row = cursor.fetchone()
            if not row:
                return None

            expires = datetime.fromisoformat(row['expires_at'])
            cached = datetime.fromisoformat(row['cached_at']).replace(tzinfo=ET)
            is_expired = now >= expires

            return {
                'cached_at': row['cached_at'],
                'expires_at': row['expires_at'],
                'rows': row['rows'],
                'period': row['period'],
                'source': row['source'] if 'source' in row.keys() else 'yfinance',
                'expired': is_expired,
                'age_hours': round((now - cached).total_seconds() / 3600, 1),
                'expires_in': str(expires - now) if not is_expired else 'EXPIRED'
            }

        elif cache_type == 'fundamentals':
            cursor.execute("""
                SELECT cached_at, expires_at, source
                FROM fundamentals_cache WHERE ticker = ?
            """, (ticker,))
            row = cursor.fetchone()
            if not row:
                return None

            expires = datetime.fromisoformat(row['expires_at'])
            cached = datetime.fromisoformat(row['cached_at']).replace(tzinfo=ET)
            is_expired = now >= expires

            return {
                'cached_at': row['cached_at'],
                'expires_at': row['expires_at'],
                'source': row['source'],
                'expired': is_expired,
                'age_days': round((now - cached).total_seconds() / 86400, 1),
                'expires_in': str(expires - now) if not is_expired else 'EXPIRED'
            }

        return None

    finally:
        conn.close()


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def warm_cache(tickers: list, fetch_func):
    """
    Pre-warm cache for a list of tickers.
    Useful for batch operations.

    Args:
        tickers: List of ticker symbols
        fetch_func: Function that takes ticker and returns (ohlcv_df, fundamentals_dict)
    """
    print(f"🔥 Warming cache for {len(tickers)} tickers...")

    for i, ticker in enumerate(tickers, 1):
        try:
            # Check if already cached and valid
            cached_ohlcv = get_cached_ohlcv(ticker)
            cached_fund = get_cached_fundamentals(ticker)

            if cached_ohlcv is not None and cached_fund is not None:
                print(f"  [{i}/{len(tickers)}] {ticker}: Already cached")
                continue

            # Fetch and cache
            ohlcv_df, fundamentals = fetch_func(ticker)

            if ohlcv_df is not None and not ohlcv_df.empty:
                set_cached_ohlcv(ticker, ohlcv_df)

            if fundamentals:
                set_cached_fundamentals(ticker, fundamentals)

            print(f"  [{i}/{len(tickers)}] {ticker}: Cached")

        except Exception as e:
            print(f"  [{i}/{len(tickers)}] {ticker}: ERROR - {e}")

    print("✅ Cache warming complete")


if __name__ == "__main__":
    # Test the cache manager
    print("Testing Cache Manager...")

    # Test market-aware expiry
    print(f"\nNext market close: {get_next_market_close()}")
    print(f"OHLCV expiry: {calculate_ohlcv_expiry()}")
    print(f"Fundamentals expiry: {calculate_fundamentals_expiry()}")

    # Test cache stats
    stats = get_cache_stats()
    print(f"\nCache stats: {json.dumps(stats, indent=2, default=str)}")
