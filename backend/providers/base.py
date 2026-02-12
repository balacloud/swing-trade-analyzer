"""
Provider Abstract Interfaces & Result Dataclasses - v4.14 Multi-Source Data Intelligence

Defines the contract every provider must implement.
Result dataclasses carry data + provenance metadata.

Canonical fundamentals schema ensures all providers normalize to the same field names.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from datetime import datetime
import pandas as pd


# =============================================================================
# CANONICAL FUNDAMENTALS SCHEMA
# Every provider normalizes to these exact field names.
# The orchestrator merges fields from multiple providers into this shape.
# =============================================================================

FUNDAMENTALS_SCHEMA = [
    'pe',               # Trailing P/E ratio
    'forwardPe',        # Forward P/E ratio
    'pegRatio',         # PEG ratio (PE / EPS growth)
    'marketCap',        # Market capitalization
    'roe',              # Return on Equity (%)
    'roa',              # Return on Assets (%)
    'roic',             # Return on Invested Capital (%)
    'epsGrowth',        # EPS growth rate (decimal or %)
    'revenueGrowth',    # Revenue growth rate (decimal or %)
    'debtToEquity',     # Debt to Equity ratio
    'profitMargin',     # Net profit margin (decimal)
    'operatingMargin',  # Operating margin (decimal)
    'beta',             # Stock beta
    'dividendYield',    # Dividend yield (decimal)
]


# =============================================================================
# RESULT DATACLASSES
# =============================================================================

@dataclass
class OHLCVResult:
    """Result of fetching OHLCV price data"""
    df: pd.DataFrame            # Columns: open, high, low, close, volume (lowercase)
    source: str                 # Provider name (e.g., 'twelvedata', 'yfinance')
    ticker: str
    period: str                 # Requested period (e.g., '2y')
    rows: int = 0
    fetched_at: str = ''

    def __post_init__(self):
        self.rows = len(self.df) if self.df is not None else 0
        self.fetched_at = self.fetched_at or datetime.now().isoformat()


@dataclass
class FundamentalsResult:
    """Result of fetching fundamental data"""
    data: Dict[str, Any]        # Normalized to FUNDAMENTALS_SCHEMA keys
    source: str                 # Primary source provider
    ticker: str
    field_sources: Dict[str, str] = field(default_factory=dict)  # field_name -> provider
    fetched_at: str = ''

    def __post_init__(self):
        self.fetched_at = self.fetched_at or datetime.now().isoformat()


@dataclass
class QuoteResult:
    """Result of fetching a real-time quote (VIX, etc.)"""
    price: float
    previous_close: Optional[float]
    source: str
    ticker: str
    fetched_at: str = ''

    def __post_init__(self):
        self.fetched_at = self.fetched_at or datetime.now().isoformat()


@dataclass
class StockInfoResult:
    """Result of fetching stock metadata (name, sector, 52wk, etc.)"""
    data: Dict[str, Any]
    source: str
    ticker: str
    fetched_at: str = ''

    def __post_init__(self):
        self.fetched_at = self.fetched_at or datetime.now().isoformat()


@dataclass
class EarningsResult:
    """Result of fetching earnings calendar"""
    earnings_date: Optional[datetime]
    source: str                 # Method that found it (calendar/earnings_dates/info)
    ticker: str
    fetched_at: str = ''

    def __post_init__(self):
        self.fetched_at = self.fetched_at or datetime.now().isoformat()


# =============================================================================
# ABSTRACT PROVIDER INTERFACES
# =============================================================================

class OHLCVProvider(ABC):
    """Interface for providers that supply OHLCV price data"""
    name: str = 'base'

    @abstractmethod
    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        """Fetch daily OHLCV data. Returns DataFrame with lowercase columns."""
        pass


class IntradayProvider(ABC):
    """Interface for providers that supply intraday data"""
    name: str = 'base'

    @abstractmethod
    def get_intraday(self, ticker: str, interval: str = '1h', period: str = '60d') -> OHLCVResult:
        """Fetch intraday OHLCV. Returns DataFrame with lowercase columns."""
        pass


class FundamentalsProvider(ABC):
    """Interface for providers that supply fundamental data"""
    name: str = 'base'

    @abstractmethod
    def get_fundamentals(self, ticker: str) -> FundamentalsResult:
        """Fetch fundamentals normalized to FUNDAMENTALS_SCHEMA."""
        pass


class QuoteProvider(ABC):
    """Interface for providers that supply real-time quotes"""
    name: str = 'base'

    @abstractmethod
    def get_quote(self, ticker: str) -> QuoteResult:
        """Fetch current price + previous close."""
        pass


class StockInfoProvider(ABC):
    """Interface for providers that supply stock metadata"""
    name: str = 'base'

    @abstractmethod
    def get_stock_info(self, ticker: str) -> StockInfoResult:
        """Fetch name, sector, industry, 52wk high/low, avg volume."""
        pass


class EarningsProvider(ABC):
    """Interface for providers that supply earnings calendar"""
    name: str = 'base'

    @abstractmethod
    def get_earnings(self, ticker: str) -> EarningsResult:
        """Fetch next earnings date."""
        pass
