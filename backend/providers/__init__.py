"""
Multi-Source Data Intelligence Provider Package - v4.14
Swing Trade Analyzer

Usage in backend.py:
    from providers import get_data_provider
    dp = get_data_provider()
    ohlcv_df = dp.get_ohlcv('AAPL', '2y')
    fundamentals = dp.get_fundamentals('AAPL')
"""
# Day 95: .env loading was previously only explicit in backend.py (the Flask
# app) — every other consumer (paper_trading/daily_job.py, live_signals.py,
# ad-hoc scripts) only got API keys loaded as a side-effect of transitively
# importing backtest/simfin_loader.py or providers/backtest_adapter.py,
# whichever happened to run first. That's fragile: a future refactor that
# drops that import chain would silently break every provider's API key with
# no warning. Load it here instead, once, for every consumer of this package.
from env_loader import load_env  # Day 135: .env wins over a stale launch environment
load_env()

from .orchestrator import get_data_provider

__all__ = ['get_data_provider']
