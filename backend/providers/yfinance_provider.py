"""
yfinance Provider - v4.14 Multi-Source Data Intelligence

Wraps ALL existing yfinance patterns from backend.py into the provider interface.
This is the "known working" baseline that we're upgrading from.

Implements: OHLCVProvider, IntradayProvider, FundamentalsProvider,
            QuoteProvider, StockInfoProvider, EarningsProvider
"""

import yfinance as yf
import pandas as pd
from datetime import datetime

from .base import (
    OHLCVProvider, IntradayProvider, FundamentalsProvider,
    QuoteProvider, StockInfoProvider, EarningsProvider,
    OHLCVResult, FundamentalsResult, QuoteResult, StockInfoResult, EarningsResult
)
from .exceptions import (
    DataNotFoundError, ProviderUnavailableError, InsufficientDataError
)
from .field_maps import YFINANCE_FUNDAMENTALS, YFINANCE_STOCK_INFO, apply_field_map
from .rate_limiter import check_rate_limit
from .circuit_breaker import get_breaker


def _safe_float(value, default=None):
    """Safely convert to float (copied from backend.py for independence)"""
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return float(value.item())
        return float(value)
    except (TypeError, ValueError):
        return default


def _safe_int(value, default=None):
    """Safely convert to int"""
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return int(value.item())
        return int(value)
    except (TypeError, ValueError):
        return default


class YFinanceProvider(
    OHLCVProvider, IntradayProvider, FundamentalsProvider,
    QuoteProvider, StockInfoProvider, EarningsProvider
):
    """
    yfinance provider - wraps the unofficial Yahoo Finance scraper.
    Implements all 6 interfaces since yfinance can do everything.
    """
    name = 'yfinance'

    def get_ohlcv(self, ticker: str, period: str = '2y') -> OHLCVResult:
        """Fetch daily OHLCV from yfinance"""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)

            if hist is None or hist.empty:
                breaker.record_failure()
                raise DataNotFoundError(self.name, f"No OHLCV data returned", ticker)

            # Normalize to lowercase columns
            hist.columns = [c.lower() for c in hist.columns]

            # Keep only OHLCV columns
            ohlcv_cols = [c for c in ['open', 'high', 'low', 'close', 'volume'] if c in hist.columns]
            hist = hist[ohlcv_cols]

            if len(hist) < 10:
                breaker.record_failure()
                raise InsufficientDataError(self.name, f"Only {len(hist)} bars returned", ticker)

            breaker.record_success()
            return OHLCVResult(df=hist, source=self.name, ticker=ticker, period=period)

        except (DataNotFoundError, InsufficientDataError):
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_intraday(self, ticker: str, interval: str = '1h', period: str = '60d') -> OHLCVResult:
        """Fetch intraday OHLCV from yfinance (for 4H RSI calculation)"""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period, interval=interval)

            if hist is None or hist.empty:
                breaker.record_failure()
                raise DataNotFoundError(self.name, f"No intraday data returned", ticker)

            # Normalize to lowercase
            hist.columns = [c.lower() for c in hist.columns]

            ohlcv_cols = [c for c in ['open', 'high', 'low', 'close', 'volume'] if c in hist.columns]
            hist = hist[ohlcv_cols]

            breaker.record_success()
            return OHLCVResult(df=hist, source=self.name, ticker=ticker, period=period)

        except DataNotFoundError:
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_fundamentals(self, ticker: str) -> FundamentalsResult:
        """
        Fetch fundamentals from yfinance.
        Replicates the logic from get_fundamentals_yfinance() in backend.py.
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            if not info or info.get('quoteType') is None:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No info data returned", ticker)

            # Apply field map for basic fields
            data = apply_field_map(info, YFINANCE_FUNDAMENTALS)

            # Enhance with calculated fields
            # Calculate YoY growth from quarterly financials (same-quarter year-over-year)
            # Day 60 fix: was QoQ (iloc[0] vs iloc[1]), now YoY (iloc[0] vs iloc[4])
            try:
                financials = stock.quarterly_financials
                if financials is not None and len(financials.columns) >= 5:
                    # Revenue Growth YoY (same quarter, year-over-year)
                    if 'Total Revenue' in financials.index and data.get('revenueGrowth') is None:
                        current_rev = _safe_float(financials.loc['Total Revenue'].iloc[0])
                        year_ago_rev = _safe_float(financials.loc['Total Revenue'].iloc[4])
                        if current_rev and year_ago_rev and year_ago_rev != 0:
                            data['revenueGrowth'] = round(((current_rev - year_ago_rev) / abs(year_ago_rev)) * 100, 2)

                    # EPS Growth YoY (same quarter, year-over-year)
                    if data.get('epsGrowth') is None:
                        eps_field = None
                        for f in ['Diluted EPS', 'Basic EPS']:
                            if f in financials.index:
                                eps_field = f
                                break
                        if eps_field:
                            current_eps = _safe_float(financials.loc[eps_field].iloc[0])
                            year_ago_eps = _safe_float(financials.loc[eps_field].iloc[4])
                            if current_eps and year_ago_eps and year_ago_eps != 0:
                                data['epsGrowth'] = round(((current_eps - year_ago_eps) / abs(year_ago_eps)) * 100, 2)
                        elif 'Net Income' in financials.index:
                            current_ni = _safe_float(financials.loc['Net Income'].iloc[0])
                            year_ago_ni = _safe_float(financials.loc['Net Income'].iloc[4])
                            if current_ni and year_ago_ni and year_ago_ni != 0:
                                data['epsGrowth'] = round(((current_ni - year_ago_ni) / abs(year_ago_ni)) * 100, 2)
            except Exception:
                pass

            # Calculate ROE/ROA from balance sheet if not in info
            try:
                balance = stock.quarterly_balance_sheet
                if balance is not None and len(balance.columns) >= 1:
                    net_income = None
                    try:
                        qf = stock.quarterly_financials
                        if qf is not None and 'Net Income' in qf.index:
                            net_income = _safe_float(qf.loc['Net Income'].iloc[0])
                    except Exception:
                        pass

                    equity = None
                    total_assets = None
                    total_debt = None

                    if 'Stockholders Equity' in balance.index:
                        equity = _safe_float(balance.loc['Stockholders Equity'].iloc[0])
                    elif 'Total Stockholder Equity' in balance.index:
                        equity = _safe_float(balance.loc['Total Stockholder Equity'].iloc[0])

                    if 'Total Assets' in balance.index:
                        total_assets = _safe_float(balance.loc['Total Assets'].iloc[0])

                    if 'Total Debt' in balance.index:
                        total_debt = _safe_float(balance.loc['Total Debt'].iloc[0])

                    if net_income and equity and equity != 0 and data.get('roe') is None:
                        data['roe'] = round((net_income / equity) * 100, 2)
                    if net_income and total_assets and total_assets != 0 and data.get('roa') is None:
                        data['roa'] = round((net_income / total_assets) * 100, 2)
                    if total_debt and equity and equity != 0 and data.get('debtToEquity') is None:
                        data['debtToEquity'] = round(total_debt / equity, 2)
            except Exception:
                pass

            # Calculate PEG ratio if missing
            if data.get('pegRatio') is None:
                pe = data.get('pe')
                eps_growth = data.get('epsGrowth')
                if pe is not None and eps_growth is not None and eps_growth > 0:
                    data['pegRatio'] = round(pe / (eps_growth * 100), 2)

            data['source'] = self.name

            # Track which fields came from yfinance
            field_sources = {k: self.name for k, v in data.items() if v is not None and k != 'source'}

            breaker.record_success()
            return FundamentalsResult(
                data=data, source=self.name, ticker=ticker, field_sources=field_sources
            )

        except DataNotFoundError:
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_quote(self, ticker: str) -> QuoteResult:
        """Fetch current price quote (used for VIX)"""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            price = info.get('regularMarketPrice')
            previous_close = info.get('previousClose')

            # Fallback to history if info doesn't have current price
            if price is None:
                hist = stock.history(period='5d')
                if hist is None or hist.empty:
                    breaker.record_failure()
                    raise DataNotFoundError(self.name, "No quote data", ticker)
                price = float(hist.iloc[-1]['Close'])

            breaker.record_success()
            return QuoteResult(
                price=round(float(price), 2),
                previous_close=round(float(previous_close), 2) if previous_close else None,
                source=self.name,
                ticker=ticker
            )

        except DataNotFoundError:
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_stock_info(self, ticker: str) -> StockInfoResult:
        """Fetch stock metadata (name, sector, 52wk, avg volume)"""
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            if not info:
                breaker.record_failure()
                raise DataNotFoundError(self.name, "No stock info returned", ticker)

            data = apply_field_map(info, YFINANCE_STOCK_INFO)
            # Fill defaults for missing fields
            data['name'] = data.get('name') or ticker
            data['sector'] = data.get('sector') or 'Unknown'
            data['industry'] = info.get('industry', 'Unknown')

            breaker.record_success()
            return StockInfoResult(data=data, source=self.name, ticker=ticker)

        except DataNotFoundError:
            raise
        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def get_earnings(self, ticker: str) -> EarningsResult:
        """
        Fetch next earnings date using 3-method approach from backend.py.
        Method 1: .calendar
        Method 2: .earnings_dates
        Method 3: .info earningsTimestamp
        """
        self._check_availability()

        breaker = get_breaker(self.name)
        try:
            stock = yf.Ticker(ticker)
            earnings_date = None
            source_method = None

            # Method 1: Try .calendar
            try:
                calendar = stock.calendar
                if calendar is not None and not calendar.empty:
                    if 'Earnings Date' in calendar.index:
                        ed = calendar.loc['Earnings Date']
                        if hasattr(ed, 'iloc'):
                            ed = ed.iloc[0]
                        earnings_date = ed
                        source_method = 'calendar'
            except Exception:
                pass

            # Method 2: Try .earnings_dates
            if earnings_date is None:
                try:
                    earnings_dates = stock.earnings_dates
                    if earnings_dates is not None and len(earnings_dates) > 0:
                        now = datetime.now()
                        future_dates = [d for d in earnings_dates.index if d.to_pydatetime() > now]
                        if future_dates:
                            earnings_date = min(future_dates)
                            source_method = 'earnings_dates'
                except Exception:
                    pass

            # Method 3: Try info dict
            if earnings_date is None:
                try:
                    info = stock.info
                    if info and 'earningsTimestamp' in info:
                        ts = info['earningsTimestamp']
                        if ts:
                            earnings_date = datetime.fromtimestamp(ts)
                            source_method = 'info'
                except Exception:
                    pass

            # Convert to datetime if needed
            if earnings_date is not None:
                if hasattr(earnings_date, 'to_pydatetime'):
                    earnings_date = earnings_date.to_pydatetime()
                elif isinstance(earnings_date, str):
                    earnings_date = datetime.fromisoformat(earnings_date.replace('Z', '+00:00'))
                # Make timezone-naive
                if hasattr(earnings_date, 'tzinfo') and earnings_date.tzinfo is not None:
                    earnings_date = earnings_date.replace(tzinfo=None)

            breaker.record_success()
            return EarningsResult(
                earnings_date=earnings_date,
                source=source_method or 'none',
                ticker=ticker
            )

        except Exception as e:
            breaker.record_failure()
            raise ProviderUnavailableError(self.name, str(e), ticker) from e

    def _check_availability(self):
        """Check rate limit and circuit breaker before making request"""
        breaker = get_breaker(self.name)
        if not breaker.allow_request():
            raise ProviderUnavailableError(self.name, "Circuit breaker OPEN")

        if not check_rate_limit(self.name):
            from .exceptions import RateLimitError
            raise RateLimitError(self.name, "Rate limit exceeded")
