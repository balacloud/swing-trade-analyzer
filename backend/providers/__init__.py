"""
Multi-Source Data Intelligence Provider Package - v4.14
Swing Trade Analyzer

Usage in backend.py:
    from providers import get_data_provider
    dp = get_data_provider()
    ohlcv_df = dp.get_ohlcv('AAPL', '2y')
    fundamentals = dp.get_fundamentals('AAPL')
"""

from .orchestrator import get_data_provider

__all__ = ['get_data_provider']
