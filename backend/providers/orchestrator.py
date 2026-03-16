"""
Data Provider Orchestrator - v4.14 Multi-Source Data Intelligence

THE CORE: Routes data requests through fallback chains with:
  - Cache-first strategy (uses existing SQLite cache_manager)
  - Provider fallback chains per data type
  - Field-level merge for fundamentals
  - Stale cache fallback when all providers fail
  - Provenance tracking (which provider supplied which data)

Fallback Chains:
  OHLCV:         TwelveData → yfinance → Stooq
  Intraday:      TwelveData → yfinance
  Fundamentals:  Finnhub → AlphaVantage (growth gaps) → yfinance  (field-level merge)
  Quote (VIX):   yfinance → Finnhub
  Stock Info:    yfinance (only source for name/sector/52wk)
  Earnings:      yfinance (only source)

Note: FMP (Financial Modeling Prep) v3 was deprecated Aug 31 2025 for non-legacy accounts.
AlphaVantage replaces FMP's growth role (revenueGrowth, epsGrowth) using existing key in .env.
"""

import os
import sys
import traceback
import pandas as pd
from datetime import datetime
from typing import Optional, Dict, Any, List

from .base import (
    OHLCVResult, FundamentalsResult, QuoteResult, StockInfoResult, EarningsResult,
    FUNDAMENTALS_SCHEMA
)
from .exceptions import ProviderError

# Import providers
from .twelvedata_provider import TwelveDataProvider
from .finnhub_provider import FinnhubProvider
from .fmp_provider import FMPProvider
from .alphavantage_provider import AlphaVantageProvider
from .yfinance_provider import YFinanceProvider
from .stooq_provider import StooqProvider

# Import existing cache_manager (add parent to path if needed)
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)

try:
    import cache_manager
    CACHE_AVAILABLE = True
except ImportError:
    CACHE_AVAILABLE = False
    print("⚠️ cache_manager not available - DataProvider running without cache")


class DataProvider:
    """
    Singleton orchestrator that routes all data requests through
    fallback chains with cache integration.
    """

    def __init__(self):
        # Initialize providers
        self.twelvedata   = TwelveDataProvider()
        self.finnhub      = FinnhubProvider()
        self.fmp          = FMPProvider()          # kept for future paid plan upgrade
        self.alphavantage = AlphaVantageProvider() # replaces FMP's growth role
        self.yfinance     = YFinanceProvider()
        self.stooq        = StooqProvider()

        # Fallback chain definitions
        self._ohlcv_chain         = [self.twelvedata, self.yfinance, self.stooq]
        self._intraday_chain      = [self.twelvedata, self.yfinance]
        self._fundamentals_chain  = [self.finnhub, self.alphavantage, self.yfinance]
        self._quote_chain         = [self.yfinance, self.finnhub]
        self._stock_info_chain    = [self.yfinance]
        self._earnings_chain      = [self.yfinance]

        # Track last provider used per data type for provenance
        self._last_source: Dict[str, str] = {}

        print("🔌 DataProvider initialized with multi-source fallback chains:")
        print(f"   OHLCV:        {' → '.join(p.name for p in self._ohlcv_chain)}")
        print(f"   Intraday:     {' → '.join(p.name for p in self._intraday_chain)}")
        print(f"   Fundamentals: {' → '.join(p.name for p in self._fundamentals_chain)}")
        print(f"   Quote:        {' → '.join(p.name for p in self._quote_chain)}")
        print(f"   Stock Info:   {' → '.join(p.name for p in self._stock_info_chain)}")
        print(f"   Earnings:     {' → '.join(p.name for p in self._earnings_chain)}")

    # =========================================================================
    # OHLCV (Daily Price Data)
    # =========================================================================

    def get_ohlcv(self, ticker: str, period: str = '2y') -> pd.DataFrame:
        """
        Get OHLCV data with cache-first strategy and provider fallback.
        Returns DataFrame with lowercase columns (open, high, low, close, volume).

        Strategy: Cache → TwelveData → yfinance → Stooq → Stale Cache → Error
        """
        ticker = ticker.upper()

        # 1. Check fresh cache
        if CACHE_AVAILABLE:
            cached = cache_manager.get_cached_ohlcv(ticker)
            if cached is not None and not cached.empty:
                self._last_source[f'{ticker}_ohlcv'] = 'cache'
                return cached

        # 2. Try provider chain
        errors = []
        for provider in self._ohlcv_chain:
            try:
                result = provider.get_ohlcv(ticker, period)
                df = result.df

                # Ensure lowercase columns
                df.columns = [c.lower() for c in df.columns]

                # Cache the result with source provenance
                if CACHE_AVAILABLE:
                    cache_manager.set_cached_ohlcv(ticker, df, period, source=result.source)

                self._last_source[f'{ticker}_ohlcv'] = result.source
                print(f"✅ OHLCV for {ticker}: {result.source} ({result.rows} bars)")
                return df

            except ProviderError as e:
                errors.append(f"{e.provider}: {str(e)}")
                print(f"⚠️ OHLCV {e.provider} failed for {ticker}: {e}")
                continue

        # 3. Stale cache fallback (serve expired data with warning)
        if CACHE_AVAILABLE:
            stale = self._get_stale_ohlcv(ticker)
            if stale is not None:
                self._last_source[f'{ticker}_ohlcv'] = 'stale_cache'
                print(f"📦 OHLCV for {ticker}: serving STALE cache (all providers failed)")
                return stale

        # 4. All failed
        error_summary = '; '.join(errors)
        raise ProviderError('all', f"All OHLCV providers failed: {error_summary}", ticker)

    # =========================================================================
    # INTRADAY (for 4H RSI calculation)
    # =========================================================================

    def get_intraday_ohlcv(self, ticker: str, interval: str = '1h', period: str = '60d') -> pd.DataFrame:
        """
        Get intraday OHLCV data. Not cached (too frequent).
        Returns DataFrame with lowercase columns.

        Strategy: TwelveData → yfinance → None (non-critical)
        """
        ticker = ticker.upper()

        for provider in self._intraday_chain:
            try:
                result = provider.get_intraday(ticker, interval, period)
                df = result.df
                df.columns = [c.lower() for c in df.columns]
                self._last_source[f'{ticker}_intraday'] = result.source
                return df
            except ProviderError as e:
                print(f"⚠️ Intraday {e.provider} failed for {ticker}: {e}")
                continue

        # Intraday failure is non-critical (4H RSI is supplementary)
        return None

    # =========================================================================
    # FUNDAMENTALS (Field-Level Merge)
    # =========================================================================

    def get_fundamentals(self, ticker: str) -> Optional[Dict[str, Any]]:
        """
        Get fundamentals with field-level merge and cache.

        Strategy:
          1. Cache (if fresh)
          2. Finnhub (most fields) → check for gaps → AlphaVantage fills epsGrowth/revenueGrowth
          3. If Finnhub fails: AlphaVantage (growth) → yfinance fills remaining gaps
          4. If all fail: yfinance (all fields)
          5. Stale cache as absolute last resort

        Returns dict matching existing backend.py format for backward compatibility.
        """
        ticker = ticker.upper()

        # 1. Check fresh cache
        if CACHE_AVAILABLE:
            cached = cache_manager.get_cached_fundamentals(ticker)
            if cached:
                self._last_source[f'{ticker}_fundamentals'] = 'cache'
                return cached

        # 2. Field-level merge approach
        merged_data = {field: None for field in FUNDAMENTALS_SCHEMA}
        field_sources = {}
        primary_source = None

        # Try Finnhub first (best coverage except growth)
        try:
            finnhub_result = self.finnhub.get_fundamentals(ticker)
            for field, value in finnhub_result.data.items():
                if value is not None and field in merged_data:
                    merged_data[field] = value
                    field_sources[field] = 'finnhub'
            primary_source = 'finnhub'
            print(f"📊 Fundamentals {ticker}: Finnhub provided {len(field_sources)} fields")
        except ProviderError as e:
            print(f"⚠️ Finnhub fundamentals failed for {ticker}: {e}")

        # Check for gaps - specifically epsGrowth and revenueGrowth
        gaps = [f for f in ['epsGrowth', 'revenueGrowth'] if merged_data.get(f) is None]

        # Fill growth gaps from AlphaVantage (epsGrowth, revenueGrowth)
        if gaps or primary_source is None:
            try:
                growth = self.alphavantage.get_growth_only(ticker)
                filled = 0
                for field, value in growth.items():
                    if value is not None and merged_data.get(field) is None:
                        merged_data[field] = value
                        field_sources[field] = 'alphavantage'
                        filled += 1
                if primary_source is None and filled > 0:
                    primary_source = 'alphavantage'
                print(f"📊 Fundamentals {ticker}: AlphaVantage filled {filled} growth fields")
            except ProviderError as e:
                print(f"⚠️ AlphaVantage fundamentals failed for {ticker}: {e}")

        # Fill remaining gaps from yfinance
        still_missing = [f for f in FUNDAMENTALS_SCHEMA if merged_data.get(f) is None]
        if still_missing or primary_source is None:
            try:
                yf_result = self.yfinance.get_fundamentals(ticker)
                for field, value in yf_result.data.items():
                    if value is not None and merged_data.get(field) is None:
                        merged_data[field] = value
                        field_sources[field] = 'yfinance'
                if primary_source is None:
                    primary_source = 'yfinance'
                filled = sum(1 for f, s in field_sources.items() if s == 'yfinance')
                print(f"📊 Fundamentals {ticker}: yfinance filled {filled} remaining fields")
            except ProviderError as e:
                print(f"⚠️ yfinance fundamentals failed for {ticker}: {e}")

        # Check if we got anything useful
        if all(v is None for v in merged_data.values()):
            # Try stale cache
            if CACHE_AVAILABLE:
                stale = self._get_stale_fundamentals(ticker)
                if stale:
                    self._last_source[f'{ticker}_fundamentals'] = 'stale_cache'
                    return stale
            return None

        # Add metadata for backend.py compatibility
        merged_data['source'] = primary_source or 'multi'
        merged_data['_field_sources'] = field_sources

        # Cache the merged result
        if CACHE_AVAILABLE:
            cache_manager.set_cached_fundamentals(ticker, merged_data, source=primary_source or 'multi')

        self._last_source[f'{ticker}_fundamentals'] = primary_source or 'multi'
        return merged_data

    # =========================================================================
    # QUOTE (VIX, etc.)
    # =========================================================================

    def get_quote(self, ticker: str) -> Optional[QuoteResult]:
        """
        Get real-time quote (primarily for VIX).
        Strategy: yfinance → Finnhub → stale cache
        """
        for provider in self._quote_chain:
            try:
                result = provider.get_quote(ticker)
                self._last_source[f'{ticker}_quote'] = result.source
                return result
            except ProviderError as e:
                print(f"⚠️ Quote {e.provider} failed for {ticker}: {e}")
                continue

        return None

    # =========================================================================
    # STOCK INFO (Name, Sector, 52wk)
    # =========================================================================

    def get_stock_info(self, ticker: str) -> Optional[StockInfoResult]:
        """
        Get stock metadata. Only yfinance has this.
        Strategy: yfinance → return defaults
        """
        for provider in self._stock_info_chain:
            try:
                result = provider.get_stock_info(ticker)
                self._last_source[f'{ticker}_info'] = result.source
                return result
            except ProviderError as e:
                print(f"⚠️ StockInfo {e.provider} failed for {ticker}: {e}")
                continue

        return None

    # =========================================================================
    # EARNINGS
    # =========================================================================

    def get_earnings(self, ticker: str) -> Optional[EarningsResult]:
        """
        Get next earnings date. Only yfinance has this.
        Strategy: yfinance → return None (non-critical)
        """
        for provider in self._earnings_chain:
            try:
                result = provider.get_earnings(ticker)
                self._last_source[f'{ticker}_earnings'] = result.source
                return result
            except ProviderError as e:
                print(f"⚠️ Earnings {e.provider} failed for {ticker}: {e}")
                continue

        return None

    # =========================================================================
    # STALE CACHE HELPERS
    # =========================================================================

    def _get_stale_ohlcv(self, ticker: str) -> Optional[pd.DataFrame]:
        """Get OHLCV from cache even if expired (stale fallback)"""
        if not CACHE_AVAILABLE:
            return None
        try:
            conn = cache_manager.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT data FROM ohlcv_cache WHERE ticker = ?", (ticker.upper(),))
            row = cursor.fetchone()
            conn.close()

            if row:
                import json
                data_dict = json.loads(row['data'])
                df = pd.DataFrame.from_dict(data_dict, orient='index')
                df.index = pd.to_datetime(df.index)
                df = df.sort_index()
                df.columns = [c.lower() for c in df.columns]
                return df
        except Exception:
            pass
        return None

    def _get_stale_fundamentals(self, ticker: str) -> Optional[Dict[str, Any]]:
        """Get fundamentals from cache even if expired (stale fallback)"""
        if not CACHE_AVAILABLE:
            return None
        try:
            conn = cache_manager.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT data FROM fundamentals_cache WHERE ticker = ?", (ticker.upper(),))
            row = cursor.fetchone()
            conn.close()

            if row:
                import json
                return json.loads(row['data'])
        except Exception:
            pass
        return None

    # =========================================================================
    # DIAGNOSTICS
    # =========================================================================

    def get_provider_status(self) -> Dict[str, Any]:
        """Get status of all providers for health check endpoint"""
        from .circuit_breaker import all_breaker_status, get_breaker
        from .rate_limiter import all_limiter_status, get_limiter

        def _provider_health(name: str) -> str:
            """Returns 'ok' | 'open' | 'degraded' based on circuit breaker state"""
            try:
                state = get_breaker(name).state.value
                if state == 'closed':
                    return 'ok'
                if state == 'half_open':
                    return 'degraded'
                return 'open'
            except Exception:
                return 'ok'

        def _daily_remaining(name: str):
            try:
                return get_limiter(name).remaining_daily
            except Exception:
                return -1

        providers = {
            'twelvedata': {
                'configured': bool(self.twelvedata.api_key),
                'type': 'OHLCV + Intraday',
                'role': 'primary',
                'health': _provider_health('twelvedata'),
                'daily_remaining': _daily_remaining('twelvedata'),
            },
            'finnhub': {
                'configured': bool(self.finnhub.api_key),
                'type': 'Fundamentals (core fields)',
                'role': 'primary',
                'health': _provider_health('finnhub'),
                'daily_remaining': -1,  # unlimited
            },
            'alphavantage': {
                'configured': bool(self.alphavantage.api_key),
                'type': 'Fundamentals (growth metrics)',
                'role': 'growth',
                'health': _provider_health('alphavantage'),
                'daily_remaining': _daily_remaining('alphavantage'),
            },
            'fmp': {
                'configured': bool(self.fmp.api_key),
                'type': 'Fundamentals (deprecated v3)',
                'role': 'legacy',
                'health': _provider_health('fmp'),
                'daily_remaining': -1,
            },
            'yfinance': {
                'configured': True,
                'type': 'All data types (fallback)',
                'role': 'fallback',
                'health': _provider_health('yfinance'),
                'daily_remaining': -1,  # unlimited
            },
            'stooq': {
                'configured': True,
                'type': 'OHLCV (last resort)',
                'role': 'fallback',
                'health': _provider_health('stooq'),
                'daily_remaining': -1,
            },
        }

        # Derive active source per data type (most recent per type across all tickers)
        # key format: "{TICKER}_{type}" e.g. "AAPL_ohlcv" → type = "ohlcv"
        active_sources = {}
        for key, source in self._last_source.items():
            parts = key.rsplit('_', 1)
            if len(parts) == 2:
                active_sources[parts[1]] = source  # overwrite → last used wins

        return {
            'providers': providers,
            'active_sources': active_sources,   # e.g. {ohlcv: 'twelvedata', fundamentals: 'finnhub', ...}
            'circuit_breakers': all_breaker_status(),
            'rate_limiters': all_limiter_status(),
            'last_sources': dict(self._last_source),
        }


# =============================================================================
# SINGLETON
# =============================================================================

_instance: Optional[DataProvider] = None


def get_data_provider() -> DataProvider:
    """Get or create the singleton DataProvider instance"""
    global _instance
    if _instance is None:
        _instance = DataProvider()
    return _instance
