"""
Backtest Adapter - v4.14 Multi-Source Data Intelligence

Drop-in replacement for yf.download() in backtest scripts.
Routes through DataProvider with full fallback chain + caching.

Usage in backtest scripts:
    # OLD: df = yf.download(ticker, start=start, end=end)
    # NEW:
    from providers.backtest_adapter import download_ohlcv
    df = download_ohlcv(ticker, start=start, end=end)
"""

import os
import sys
import pandas as pd
from datetime import datetime

# Ensure backend dir is in path
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)

# Load API keys
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(_backend_dir, '.env'))
except ImportError:
    pass


def download_ohlcv(ticker: str, start: str = None, end: str = None, period: str = '2y') -> pd.DataFrame:
    """
    Drop-in replacement for yf.download().
    Returns DataFrame with capitalized columns (Open, High, Low, Close, Volume)
    to match yf.download() convention.

    Args:
        ticker: Stock symbol (e.g., 'AAPL')
        start: Start date string (e.g., '2024-01-01') - optional
        end: End date string (e.g., '2026-01-01') - optional
        period: Period string if start/end not provided (e.g., '2y')

    Returns:
        pd.DataFrame with capitalized OHLCV columns
    """
    from .orchestrator import get_data_provider

    dp = get_data_provider()

    try:
        # If start/end span > 2 years, we need yfinance directly (TwelveData free = 5000 bars max)
        # DataProvider.get_ohlcv caches 2y by default which is ~504 bars
        if start and end:
            from datetime import datetime as dt
            span_days = (pd.to_datetime(end) - pd.to_datetime(start)).days
            if span_days > 600:
                # Need more than 2y of data - use yfinance directly for backtest
                try:
                    import yfinance as yf
                    result_df = yf.download(ticker, start=start, end=end, progress=False)
                    if result_df is not None and not result_df.empty:
                        if isinstance(result_df.columns, pd.MultiIndex):
                            result_df.columns = result_df.columns.get_level_values(0)
                        # Already capitalized from yf.download
                        if result_df.index.tz is not None:
                            result_df.index = result_df.index.tz_localize(None)
                        return result_df
                except Exception:
                    pass  # Fall through to DataProvider

        result_df = dp.get_ohlcv(ticker, period)

        if result_df is None or result_df.empty:
            print(f"⚠️ No data for {ticker}")
            return pd.DataFrame()

        # Ensure timezone-naive index for consistent comparison
        if result_df.index.tz is not None:
            result_df.index = result_df.index.tz_localize(None)

        # Filter by date range if provided
        if start:
            start_dt = pd.to_datetime(start)
            result_df = result_df[result_df.index >= start_dt]
        if end:
            end_dt = pd.to_datetime(end)
            result_df = result_df[result_df.index <= end_dt]

        # Capitalize columns to match yf.download() convention
        result_df.columns = [c.capitalize() for c in result_df.columns]

        return result_df

    except Exception as e:
        print(f"❌ download_ohlcv failed for {ticker}: {e}")
        return pd.DataFrame()
