"""
Swing Trade Analyzer Backend - v2.12
Flask API server with yfinance (prices) + Defeat Beta (fundamentals) + TradingView Screener (scanning) + S&R Engine

Day 6: Fixed numpy type serialization issues
Day 8: Fixed Defeat Beta .data attribute usage
Day 11: Added TradingView screener integration for batch scanning
Day 13: Added Support & Resistance engine endpoint
Day 20: Added TradingView scan endpoint, fixed API syntax for tradingview-screener library
Day 25: Added auto-refresh cache for Defeat Beta data (TTL-based)
Day 36: Upgraded to SQLite persistent cache (survives restarts, intelligent TTL)
Day 39: Added local RSI, ADX, and 4H RSI calculations (Dual Entry Strategy)
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf
from datetime import datetime, timedelta
import traceback
import pandas as pd
import numpy as np
import sys

sys.path.insert(0, os.path.dirname(__file__))

try:
    from validation import ValidationEngine, ForwardTestTracker, SignalType
    VALIDATION_AVAILABLE = True
    print("✅ Validation Engine loaded successfully")
except ImportError as e:
    VALIDATION_AVAILABLE = False
    print(f"⚠️ Validation Engine not available: {e}")

# Try to import defeatbeta - graceful fallback if not installed
try:
    import defeatbeta_api
    from defeatbeta_api.data.ticker import Ticker as DBTicker
    DEFEATBETA_AVAILABLE = True
    print("✅ Defeat Beta loaded successfully")
except ImportError:
    DEFEATBETA_AVAILABLE = False
    print("⚠️  Defeat Beta not installed - using yfinance fallback for fundamentals")
    print("   Install with: pip install defeatbeta-api")

# Try to import tradingview-screener - graceful fallback if not installed
try:
    from tradingview_screener import Query, col
    TRADINGVIEW_AVAILABLE = True
    print("✅ TradingView Screener loaded successfully")
except ImportError:
    TRADINGVIEW_AVAILABLE = False
    print("⚠️  TradingView Screener not installed - batch scanning unavailable")
    print("   Install with: pip install tradingview-screener")

# Try to import support_resistance engine - graceful fallback
try:
    from support_resistance import compute_sr_levels, SRConfig, SRFailure
    SR_ENGINE_AVAILABLE = True
    print("✅ Support & Resistance Engine loaded successfully")
except ImportError:
    SR_ENGINE_AVAILABLE = False
    print("⚠️  S&R Engine not available - place support_resistance.py in backend folder")

app = Flask(__name__)
CORS(app)

# ============================================
# CACHE CONFIGURATION (Day 36 - SQLite Persistent)
# ============================================
# SQLite-based cache that survives restarts
# OHLCV: Expires at next market close
# Fundamentals: 7-day TTL (quarterly data)

try:
    import cache_manager
    SQLITE_CACHE_AVAILABLE = True
    print("✅ SQLite Cache Manager loaded successfully")
except ImportError as e:
    SQLITE_CACHE_AVAILABLE = False
    print(f"⚠️ SQLite Cache not available: {e}")

# Wrapper functions for backward compatibility
def get_cached_fundamentals(ticker_symbol):
    """Get fundamentals from SQLite cache if not expired"""
    if SQLITE_CACHE_AVAILABLE:
        return cache_manager.get_cached_fundamentals(ticker_symbol)
    return None

def set_cached_fundamentals(ticker_symbol, data):
    """Store fundamentals in SQLite cache"""
    if SQLITE_CACHE_AVAILABLE:
        cache_manager.set_cached_fundamentals(ticker_symbol, data)

def clear_fundamentals_cache(ticker_symbol=None):
    """Clear SQLite cache"""
    if SQLITE_CACHE_AVAILABLE:
        cache_manager.clear_cache(ticker=ticker_symbol, cache_type='fundamentals')

def get_cached_ohlcv(ticker_symbol):
    """Get OHLCV from SQLite cache if not expired"""
    if SQLITE_CACHE_AVAILABLE:
        return cache_manager.get_cached_ohlcv(ticker_symbol)
    return None

def set_cached_ohlcv(ticker_symbol, df):
    """Store OHLCV in SQLite cache"""
    if SQLITE_CACHE_AVAILABLE:
        cache_manager.set_cached_ohlcv(ticker_symbol, df)

# ============================================
# HELPER FUNCTIONS
# ============================================

def safe_float(value, default=None):
    """Safely convert numpy/pandas types to Python float"""
    try:
        if value is None:
            return default
        # Handle pandas/numpy types
        if hasattr(value, 'item'):
            return float(value.item())
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_int(value, default=None):
    """Safely convert numpy/pandas types to Python int"""
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return int(value.item())
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_bool(value, default=False):
    """Safely convert numpy bool to Python bool"""
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return bool(value.item())
        return bool(value)
    except (TypeError, ValueError):
        return default


def safe_get(data, key, default=None):
    """Safely get a value from a dictionary"""
    try:
        value = data.get(key, default)
        if value is None:
            return default
        return value
    except:
        return default


def calculate_growth_rate(current, previous):
    """Calculate percentage growth rate"""
    try:
        if previous is None or previous == 0:
            return None
        current = safe_float(current)
        previous = safe_float(previous)
        if current is None or previous is None or previous == 0:
            return None
        return ((current - previous) / abs(previous)) * 100
    except:
        return None


# =============================================================================
# LOCAL INDICATOR CALCULATIONS (Day 39 - Dual Entry Strategy)
# =============================================================================

def calculate_rsi(closes: pd.Series, period: int = 14) -> float:
    """
    Calculate RSI (Relative Strength Index) using Wilder's smoothing.

    This provides independence from TradingView for RSI calculations.
    Formula: RSI = 100 - (100 / (1 + RS))
    where RS = Average Gain / Average Loss over the period

    Parameters
    ----------
    closes : pd.Series
        Series of closing prices
    period : int
        RSI period (default 14)

    Returns
    -------
    float
        Current RSI value (0-100), or None if insufficient data
    """
    try:
        if len(closes) < period + 1:
            return None

        # Calculate price changes
        delta = closes.diff()

        # Separate gains and losses
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        # Use Wilder's smoothing (exponential with alpha = 1/period)
        avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
        avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()

        # Avoid division by zero
        if avg_loss.iloc[-1] == 0:
            return 100.0 if avg_gain.iloc[-1] > 0 else 50.0

        rs = avg_gain.iloc[-1] / avg_loss.iloc[-1]
        rsi = 100 - (100 / (1 + rs))

        return round(float(rsi), 2)

    except Exception as e:
        print(f"RSI calculation error: {e}")
        return None


def calculate_adx(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> dict:
    """
    Calculate ADX (Average Directional Index) using Wilder's method.

    ADX measures trend strength (0-100):
    - < 20: No trend (choppy)
    - 20-25: Weak trend developing
    - 25-40: Strong trend
    - > 40: Very strong trend

    Parameters
    ----------
    high : pd.Series
        High prices
    low : pd.Series
        Low prices
    close : pd.Series
        Close prices
    period : int
        ADX period (default 14)

    Returns
    -------
    dict
        {
            'adx': float,           # ADX value (0-100)
            'di_plus': float,       # +DI value
            'di_minus': float,      # -DI value
            'trend_strength': str   # 'choppy'/'weak'/'strong'/'very_strong'
        }
    """
    try:
        if len(close) < period * 2:
            return None

        # True Range
        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

        # Directional Movement
        up_move = high - high.shift(1)
        down_move = low.shift(1) - low

        # +DM and -DM
        plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0)
        minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0)

        # Wilder's smoothing
        atr = tr.ewm(alpha=1/period, min_periods=period).mean()
        plus_di = 100 * (plus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)
        minus_di = 100 * (minus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)

        # DX and ADX
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di + 1e-10)
        adx = dx.ewm(alpha=1/period, min_periods=period).mean()

        adx_value = round(float(adx.iloc[-1]), 1)

        # Determine trend strength
        if adx_value < 20:
            trend = 'choppy'
        elif adx_value < 25:
            trend = 'weak'
        elif adx_value < 40:
            trend = 'strong'
        else:
            trend = 'very_strong'

        return {
            'adx': adx_value,
            'di_plus': round(float(plus_di.iloc[-1]), 1),
            'di_minus': round(float(minus_di.iloc[-1]), 1),
            'trend_strength': trend
        }

    except Exception as e:
        print(f"ADX calculation error: {e}")
        return None


def calculate_rsi_4h(ticker_symbol: str, period: int = 14) -> dict:
    """
    Calculate RSI on 4H timeframe using yfinance hourly data.

    Fetches 60 days of 1H data, resamples to 4H, then calculates RSI.
    This provides momentum confirmation for the Dual Entry Strategy.

    Parameters
    ----------
    ticker_symbol : str
        Stock ticker symbol
    period : int
        RSI period (default 14)

    Returns
    -------
    dict
        {
            'rsi_4h': float,          # RSI value (0-100)
            'bars_available': int,     # Number of 4H bars used
            'momentum': str,           # 'oversold'/'weak'/'neutral'/'strong'/'overbought'
            'entry_signal': bool       # True if RSI > 40 (momentum confirmation)
        }
    """
    try:
        stock = yf.Ticker(ticker_symbol)

        # Fetch 60 days of 1H data (yfinance limit for intraday)
        df_1h = stock.history(period='60d', interval='1h')

        if df_1h.empty or len(df_1h) < 20:
            return None

        # Resample 1H to 4H
        df_4h = df_1h.resample('4h').agg({
            'Open': 'first',
            'High': 'max',
            'Low': 'min',
            'Close': 'last',
            'Volume': 'sum'
        }).dropna()

        if len(df_4h) < period + 1:
            return None

        # Calculate RSI on 4H closes
        closes = df_4h['Close']
        delta = closes.diff()

        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
        avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()

        if avg_loss.iloc[-1] == 0:
            rsi_value = 100.0 if avg_gain.iloc[-1] > 0 else 50.0
        else:
            rs = avg_gain.iloc[-1] / avg_loss.iloc[-1]
            rsi_value = 100 - (100 / (1 + rs))

        rsi_value = round(float(rsi_value), 1)

        # Determine momentum state
        if rsi_value < 30:
            momentum = 'oversold'
        elif rsi_value < 40:
            momentum = 'weak'
        elif rsi_value < 60:
            momentum = 'neutral'
        elif rsi_value < 70:
            momentum = 'strong'
        else:
            momentum = 'overbought'

        # Entry signal: RSI > 40 indicates momentum is turning positive
        entry_signal = rsi_value > 40

        return {
            'rsi_4h': rsi_value,
            'bars_available': len(df_4h),
            'momentum': momentum,
            'entry_signal': entry_signal
        }

    except Exception as e:
        print(f"4H RSI calculation error for {ticker_symbol}: {e}")
        return None


def get_fundamentals_defeatbeta(ticker_symbol):
    """
    Get rich fundamental data from Defeat Beta
    Returns ROE, ROIC, ROA, EPS growth, revenue growth, etc.

    Day 8 FIX: Use .data attribute instead of .to_df()
    Day 25: Added TTL cache to prevent stale data (auto-refresh after 1 hour)
    DataFrame structure: Columns = ['Breakdown', '2024-10-31', '2023-10-31', ...]
    Values are in rows with labels in 'Breakdown' column
    """
    if not DEFEATBETA_AVAILABLE:
        return None

    # Day 25: Check cache first
    cached = get_cached_fundamentals(ticker_symbol)
    if cached:
        return cached

    try:
        ticker = DBTicker(ticker_symbol)
        
        # Initialize result
        result = {
            'source': 'defeatbeta',
            'roe': None,
            'roic': None,
            'roa': None,
            'epsGrowth': None,
            'revenueGrowth': None,
            'debtToEquity': None,
            'profitMargin': None,
            'operatingMargin': None,
            'pegRatio': None
        }
        
        # Track data we've collected
        net_income = None
        total_equity = None
        total_assets = None
        total_debt = None
        total_revenue = None
        
        # Try to get annual income statement for growth calculations
        try:
            annual_income = ticker.annual_income_statement()
            
            # DAY 8 FIX: Use .data instead of .to_df()
            if hasattr(annual_income, 'data'):
                annual_df = annual_income.data
                
                if annual_df is not None and 'Breakdown' in annual_df.columns:
                    # Get date columns (exclude 'Breakdown')
                    date_cols = [c for c in annual_df.columns if c != 'Breakdown']
                    
                    if len(date_cols) >= 2:
                        current_year = date_cols[0]  # Most recent (e.g., '2024-10-31')
                        prev_year = date_cols[1]     # Previous year (e.g., '2023-10-31')
                        
                        # Iterate through rows to find values
                        for _, row in annual_df.iterrows():
                            breakdown = str(row.get('Breakdown', ''))
                            
                            # Get Diluted EPS for EPS Growth
                            if breakdown == 'Diluted EPS':
                                try:
                                    current_eps = safe_float(row.get(current_year))
                                    prev_eps = safe_float(row.get(prev_year))
                                    if current_eps is not None and prev_eps is not None and prev_eps != 0:
                                        result['epsGrowth'] = round(((current_eps - prev_eps) / abs(prev_eps)) * 100, 2)
                                except:
                                    pass
                            
                            # Get Total Revenue for Revenue Growth
                            if breakdown == 'Total Revenue':
                                try:
                                    current_rev = safe_float(row.get(current_year))
                                    prev_rev = safe_float(row.get(prev_year))
                                    total_revenue = current_rev  # Save for profit margin
                                    if current_rev is not None and prev_rev is not None and prev_rev != 0:
                                        result['revenueGrowth'] = round(((current_rev - prev_rev) / abs(prev_rev)) * 100, 2)
                                except:
                                    pass
                            
                            # Get Net Income Common Stockholders for ROE/ROA
                            if breakdown == 'Net Income Common Stockholders':
                                try:
                                    net_income = safe_float(row.get(current_year))
                                except:
                                    pass
                            
                            # Get Operating Income for Operating Margin
                            if breakdown == 'Operating Income':
                                try:
                                    operating_income = safe_float(row.get(current_year))
                                    if operating_income is not None and total_revenue is not None and total_revenue != 0:
                                        result['operatingMargin'] = round((operating_income / total_revenue) * 100, 2)
                                except:
                                    pass
                        
                        # Calculate Profit Margin
                        if net_income is not None and total_revenue is not None and total_revenue != 0:
                            result['profitMargin'] = round((net_income / total_revenue) * 100, 2)
                            
        except Exception as e:
            print(f"Error getting annual income: {e}")
            traceback.print_exc()
        
        # Try to get balance sheet for ROE, ROIC, Debt/Equity
        try:
            annual_balance = ticker.annual_balance_sheet()
            
            # DAY 8 FIX: Use .data instead of .to_df()
            if hasattr(annual_balance, 'data'):
                balance_df = annual_balance.data
                
                if balance_df is not None and 'Breakdown' in balance_df.columns:
                    # Get date columns (exclude 'Breakdown')
                    date_cols = [c for c in balance_df.columns if c != 'Breakdown']
                    
                    if len(date_cols) >= 1:
                        current_col = date_cols[0]  # Most recent
                        
                        # Iterate through rows to find values
                        for _, row in balance_df.iterrows():
                            breakdown = str(row.get('Breakdown', ''))
                            
                            # Get Total Assets
                            if breakdown == 'Total Assets':
                                try:
                                    total_assets = safe_float(row.get(current_col))
                                except:
                                    pass
                            
                            # Get Stockholders' Equity
                            if breakdown == "Stockholders' Equity":
                                try:
                                    total_equity = safe_float(row.get(current_col))
                                except:
                                    pass
                            
                            # Get Total Debt
                            if breakdown == 'Total Debt':
                                try:
                                    total_debt = safe_float(row.get(current_col))
                                except:
                                    pass
                        
                        # Calculate Debt to Equity
                        if total_equity and total_equity != 0 and total_debt:
                            result['debtToEquity'] = round(total_debt / total_equity, 2)
                        
                        # Calculate ROE = Net Income / Shareholders Equity
                        if net_income and total_equity and total_equity != 0:
                            result['roe'] = round((net_income / total_equity) * 100, 2)
                        
                        # Calculate ROA = Net Income / Total Assets
                        if net_income and total_assets and total_assets != 0:
                            result['roa'] = round((net_income / total_assets) * 100, 2)
                        
                        # Calculate ROIC (simplified) = Net Income / (Equity + Debt)
                        invested_capital = (total_equity or 0) + (total_debt or 0)
                        if net_income and invested_capital != 0:
                            result['roic'] = round((net_income / invested_capital) * 100, 2)
                        
        except Exception as e:
            print(f"Error getting balance sheet: {e}")
            traceback.print_exc()
        
        # Debug output
        print(f"📊 Defeat Beta fundamentals for {ticker_symbol}:")
        print(f"   ROE: {result['roe']}%, ROA: {result['roa']}%, ROIC: {result['roic']}%")
        print(f"   EPS Growth: {result['epsGrowth']}%, Revenue Growth: {result['revenueGrowth']}%")
        print(f"   Debt/Equity: {result['debtToEquity']}, Profit Margin: {result['profitMargin']}%")

        # Day 25: Cache the result
        set_cached_fundamentals(ticker_symbol, result)

        return result
        
    except Exception as e:
        print(f"Error in get_fundamentals_defeatbeta: {e}")
        traceback.print_exc()
        return None


def get_fundamentals_yfinance(ticker_symbol):
    """
    Fallback: Get basic fundamental data from yfinance
    Limited data but always available
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        
        # Get financials for growth calculations
        rev_growth = None
        net_income = None
        try:
            financials = stock.quarterly_financials
            if financials is not None and len(financials.columns) >= 2:
                if 'Total Revenue' in financials.index:
                    current_rev = safe_float(financials.loc['Total Revenue'].iloc[0])
                    prev_rev = safe_float(financials.loc['Total Revenue'].iloc[1])
                    if current_rev and prev_rev and prev_rev != 0:
                        rev_growth = round(((current_rev - prev_rev) / abs(prev_rev)) * 100, 2)
                        
                if 'Net Income' in financials.index:
                    net_income = safe_float(financials.loc['Net Income'].iloc[0])
        except:
            pass
        
        # Get balance sheet for ROE calculation
        roe = None
        roa = None
        debt_to_equity = None
        try:
            balance = stock.quarterly_balance_sheet
            if balance is not None and len(balance.columns) >= 1:
                equity = None
                total_assets = None
                total_debt = None
                
                if 'Stockholders Equity' in balance.index:
                    equity = safe_float(balance.loc['Stockholders Equity'].iloc[0])
                elif 'Total Stockholder Equity' in balance.index:
                    equity = safe_float(balance.loc['Total Stockholder Equity'].iloc[0])
                    
                if 'Total Assets' in balance.index:
                    total_assets = safe_float(balance.loc['Total Assets'].iloc[0])
                    
                if 'Total Debt' in balance.index:
                    total_debt = safe_float(balance.loc['Total Debt'].iloc[0])
                
                # Calculate metrics
                if net_income and equity and equity != 0:
                    roe = round((net_income / equity) * 100, 2)
                if net_income and total_assets and total_assets != 0:
                    roa = round((net_income / total_assets) * 100, 2)
                if total_debt and equity and equity != 0:
                    debt_to_equity = round(total_debt / equity, 2)
        except:
            pass
        
        # Day 36: Calculate pegRatio locally if not provided by yfinance
        pe = safe_float(safe_get(info, 'trailingPE'))
        eps_growth = safe_float(safe_get(info, 'earningsGrowth'))
        peg_ratio = safe_float(safe_get(info, 'pegRatio'))

        # Fallback: Calculate PEG = PE / (EPS Growth * 100)
        # earningsGrowth from yfinance is decimal (0.15 = 15%), so multiply by 100
        # Only calculate for positive growth (negative PEG is not meaningful)
        if peg_ratio is None and pe is not None and eps_growth is not None and eps_growth > 0:
            peg_ratio = round(pe / (eps_growth * 100), 2)

        return {
            'source': 'yfinance',
            'pe': pe,
            'forwardPe': safe_float(safe_get(info, 'forwardPE')),
            'pegRatio': peg_ratio,
            'marketCap': safe_int(safe_get(info, 'marketCap')),
            'roe': roe or safe_float(safe_get(info, 'returnOnEquity')),
            'roa': roa or safe_float(safe_get(info, 'returnOnAssets')),
            'roic': None,
            'epsGrowth': eps_growth,
            'revenueGrowth': rev_growth or safe_float(safe_get(info, 'revenueGrowth')),
            'debtToEquity': debt_to_equity or safe_float(safe_get(info, 'debtToEquity')),
            'profitMargin': safe_float(safe_get(info, 'profitMargins')),
            'operatingMargin': safe_float(safe_get(info, 'operatingMargins')),
            'beta': safe_float(safe_get(info, 'beta')),
            'dividendYield': safe_float(safe_get(info, 'dividendYield')),
        }
        
    except Exception as e:
        print(f"Error in get_fundamentals_yfinance: {e}")
        return None


# ============================================
# API ROUTES
# ============================================

def _check_defeatbeta_status():
    """
    Day 33: Quick health check for Defeat Beta API
    Tests with a known ticker (AAPL) to see if API is responding
    Returns: dict with 'working', 'error', 'last_checked'
    """
    if not DEFEATBETA_AVAILABLE:
        return {'working': False, 'error': 'Library not installed', 'last_checked': datetime.now().isoformat()}

    try:
        ticker = DBTicker('AAPL')
        annual_income = ticker.annual_income_statement()

        if hasattr(annual_income, 'data') and annual_income.data is not None:
            # Check if we actually got data
            if len(annual_income.data) > 0:
                return {'working': True, 'error': None, 'last_checked': datetime.now().isoformat()}

        return {'working': False, 'error': 'API returned empty data', 'last_checked': datetime.now().isoformat()}
    except Exception as e:
        error_msg = str(e)
        if 'TProtocolException' in error_msg:
            error_msg = 'API connection error (TProtocolException)'
        return {'working': False, 'error': error_msg, 'last_checked': datetime.now().isoformat()}


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint - Day 33: Added Defeat Beta live status"""
    # Day 33: Check if we should do a live Defeat Beta check
    check_defeatbeta = request.args.get('check_defeatbeta', 'false').lower() == 'true'

    # Get cache stats if available
    cache_stats = {}
    if SQLITE_CACHE_AVAILABLE:
        try:
            stats = cache_manager.get_cache_stats()
            cache_stats = {
                'ohlcv_count': stats['ohlcv']['count'],
                'fundamentals_count': stats['fundamentals']['count'],
                'market_count': stats['market']['count'],
                'cache_size_kb': stats['total_size_kb']
            }
        except Exception:
            cache_stats = {'error': 'Could not get cache stats'}

    response = {
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.9',
        'defeatbeta_available': DEFEATBETA_AVAILABLE,
        'tradingview_available': TRADINGVIEW_AVAILABLE,
        'sr_engine_available': SR_ENGINE_AVAILABLE,
        'validation_available': VALIDATION_AVAILABLE,
        'sqlite_cache_available': SQLITE_CACHE_AVAILABLE,
        'cache': cache_stats
    }

    # Only do live check if requested (avoids slowing down regular health checks)
    if check_defeatbeta:
        response['defeatbeta_status'] = _check_defeatbeta_status()

    return jsonify(response)


@app.route('/api/cache/clear', methods=['POST'])
def clear_cache():
    """
    Clear cache - Day 36 (SQLite)
    POST /api/cache/clear - clears all cache
    POST /api/cache/clear?ticker=AAPL - clears specific ticker
    POST /api/cache/clear?type=ohlcv - clears specific cache type
    """
    ticker = request.args.get('ticker')
    cache_type = request.args.get('type')  # 'ohlcv', 'fundamentals', or None for all

    if SQLITE_CACHE_AVAILABLE:
        cache_manager.clear_cache(ticker=ticker.upper() if ticker else None, cache_type=cache_type)
        stats = cache_manager.get_cache_stats()
        return jsonify({
            'status': 'success',
            'message': f'Cache cleared (ticker={ticker}, type={cache_type})',
            'cache': {
                'ohlcv_count': stats['ohlcv']['count'],
                'fundamentals_count': stats['fundamentals']['count'],
                'size_kb': stats['total_size_kb']
            }
        })
    else:
        return jsonify({'status': 'error', 'message': 'SQLite cache not available'}), 500


@app.route('/api/cache/status', methods=['GET'])
def cache_status():
    """Get detailed cache status - Day 36 (SQLite)"""
    if SQLITE_CACHE_AVAILABLE:
        stats = cache_manager.get_cache_stats()
        hit_rates = cache_manager.get_cache_hit_rate(hours=24)
        return jsonify({
            'status': 'healthy',
            'storage': 'sqlite',
            'database_size_kb': stats['total_size_kb'],
            'ohlcv': {
                'count': stats['ohlcv']['count'],
                'hit_rate_24h': hit_rates.get('ohlcv', 0),
                'entries': stats['ohlcv']['entries'][:20]  # Limit to 20 for response size
            },
            'fundamentals': {
                'count': stats['fundamentals']['count'],
                'hit_rate_24h': hit_rates.get('fundamentals', 0),
                'entries': stats['fundamentals']['entries'][:20]
            },
            'market': {
                'count': stats['market']['count'],
                'entries': stats['market']['entries']
            }
        })
    else:
        return jsonify({'status': 'error', 'message': 'SQLite cache not available'}), 500


@app.route('/api/provenance/<ticker>', methods=['GET'])
def get_data_provenance(ticker):
    """
    Get detailed data source provenance for a ticker.
    Shows where each data point comes from, cache status, and calculation formulas.
    Day 38: Data Sources tab support
    """
    ticker = ticker.upper()

    # Get cache info for this specific ticker
    ohlcv_cache = None
    fund_cache = None

    if SQLITE_CACHE_AVAILABLE:
        ohlcv_cache = cache_manager.get_ticker_cache_info(ticker, 'ohlcv')
        fund_cache = cache_manager.get_ticker_cache_info(ticker, 'fundamentals')

    # Build provenance response
    provenance = {
        'ticker': ticker,
        'timestamp': datetime.now().isoformat(),
        'ohlcv': {
            'source': 'yfinance',
            'cached': ohlcv_cache is not None,
            'cached_at': ohlcv_cache.get('cached_at') if ohlcv_cache else None,
            'expires_at': ohlcv_cache.get('expires_at') if ohlcv_cache else None,
            'expires_in': ohlcv_cache.get('expires_in') if ohlcv_cache else None,
            'rows': ohlcv_cache.get('rows') if ohlcv_cache else None,
            'age_hours': ohlcv_cache.get('age_hours') if ohlcv_cache else None,
            'status': 'cached' if ohlcv_cache and not ohlcv_cache.get('expired') else 'live'
        },
        'fundamentals': {
            'source': fund_cache.get('source', 'yfinance') if fund_cache else 'yfinance',
            'cached': fund_cache is not None,
            'cached_at': fund_cache.get('cached_at') if fund_cache else None,
            'expires_at': fund_cache.get('expires_at') if fund_cache else None,
            'expires_in': fund_cache.get('expires_in') if fund_cache else None,
            'age_days': fund_cache.get('age_days') if fund_cache else None,
            'status': 'cached' if fund_cache and not fund_cache.get('expired') else 'live'
        },
        'indicators': [
            {'name': 'SMA 50', 'source': 'local', 'formula': 'Sum(Close, 50) / 50'},
            {'name': 'SMA 200', 'source': 'local', 'formula': 'Sum(Close, 200) / 200'},
            {'name': 'EMA 8', 'source': 'local', 'formula': 'Price * k + EMA_prev * (1-k), k=2/(8+1)'},
            {'name': 'EMA 21', 'source': 'local', 'formula': 'Price * k + EMA_prev * (1-k), k=2/(21+1)'},
            {'name': 'ATR 14', 'source': 'local', 'formula': 'EMA(TrueRange, 14) where TR=max(H-L, |H-Cp|, |L-Cp|)'},
            {'name': 'RSI 14', 'source': 'local', 'formula': '100 - 100/(1 + AvgGain/AvgLoss) [Wilder smoothing]'},
            {'name': 'Avg Volume 20', 'source': 'local', 'formula': 'Sum(Volume, 20) / 20'},
            {'name': 'Avg Volume 50', 'source': 'local', 'formula': 'Sum(Volume, 50) / 50'},
            {'name': 'RS 52W', 'source': 'local', 'formula': 'Stock 52W Return / SPY 52W Return'},
            {'name': 'RS Price Ratio', 'source': 'local', 'formula': 'Stock Price / SPY Price'},
            {'name': 'PEG Ratio', 'source': 'local', 'formula': 'PE / (EPS Growth * 100)'}
        ],
        'data_sources': {
            'prices': {'name': 'Yahoo Finance (yfinance)', 'status': 'available'},
            'fundamentals_primary': {
                'name': 'Defeat Beta API',
                'status': 'available' if DEFEATBETA_AVAILABLE else 'unavailable'
            },
            'fundamentals_fallback': {'name': 'Yahoo Finance (yfinance)', 'status': 'available'},
            'market_data': {'name': 'Yahoo Finance (SPY, VIX)', 'status': 'available'},
            'scanning': {
                'name': 'TradingView Screener',
                'status': 'available' if TRADINGVIEW_AVAILABLE else 'unavailable'
            }
        }
    }

    return jsonify(provenance)


@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    """
    Get stock data for analysis
    Uses SQLite cache (Day 36) + yfinance fallback
    """
    try:
        ticker = ticker.upper()

        # Day 36: Check SQLite cache first for OHLCV
        cached_hist = get_cached_ohlcv(ticker)

        if cached_hist is not None and not cached_hist.empty:
            hist = cached_hist
            print(f"📦 Using cached OHLCV for {ticker}")
        else:
            # Cache miss - fetch from yfinance
            stock = yf.Ticker(ticker)
            hist = stock.history(period='2y')

            if hist.empty:
                return jsonify({'error': f'No data found for {ticker}'}), 404

            # Normalize column names to lowercase
            hist.columns = [c.lower() for c in hist.columns]

            # Cache the full 2-year data
            set_cached_ohlcv(ticker, hist)

        # Get last 260 days (covers full 52 weeks of trading)
        hist_data = hist.tail(260)

        # Normalize column names for consistent access (handles both cached and fresh data)
        hist_data.columns = [c.lower() for c in hist_data.columns]

        # Get stock info (always fresh - used for fundamentals, not OHLCV)
        stock = yf.Ticker(ticker)
        info = stock.info

        # Prepare price history (using lowercase column names)
        price_history = []
        for date, row in hist_data.iterrows():
            price_history.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': round(float(row['open']), 2),
                'high': round(float(row['high']), 2),
                'low': round(float(row['low']), 2),
                'close': round(float(row['close']), 2),
                'volume': int(row['volume'])
            })

        # Get 52-week ago price (approximately 252 trading days)
        price_52w_ago = None
        if len(hist_data) >= 252:
            price_52w_ago = round(float(hist_data.iloc[-252]['close']), 2)
        elif len(hist_data) > 200:
            price_52w_ago = round(float(hist_data.iloc[0]['close']), 2)

        # Get 13-week ago price (approximately 63 trading days)
        price_13w_ago = None
        if len(hist_data) >= 63:
            price_13w_ago = round(float(hist_data.iloc[-63]['close']), 2)

        # Current price
        current_price = round(float(hist_data.iloc[-1]['close']), 2)
        
        # Basic fundamentals from yfinance (for backward compatibility)
        fundamentals = {
            'pe': safe_float(safe_get(info, 'trailingPE')),
            'forwardPe': safe_float(safe_get(info, 'forwardPE')),
            'marketCap': safe_int(safe_get(info, 'marketCap')),
            'beta': safe_float(safe_get(info, 'beta')),
            'dividendYield': safe_float(safe_get(info, 'dividendYield')),
            'epsGrowth': 0,
            'revenueGrowth': 0,
            'roe': 0,
            'roic': 0,
            'debtToEquity': 0
        }
        
        response = {
            'ticker': ticker,
            'name': safe_get(info, 'shortName', ticker),
            'sector': safe_get(info, 'sector', 'Unknown'),
            'industry': safe_get(info, 'industry', 'Unknown'),
            'currentPrice': current_price,
            'price52wAgo': price_52w_ago,
            'price13wAgo': price_13w_ago,
            'fiftyTwoWeekHigh': safe_float(safe_get(info, 'fiftyTwoWeekHigh')),
            'fiftyTwoWeekLow': safe_float(safe_get(info, 'fiftyTwoWeekLow')),
            'avgVolume': safe_int(safe_get(info, 'averageVolume')),
            'avgVolume10d': safe_int(safe_get(info, 'averageVolume10days')),
            'priceHistory': price_history,
            'fundamentals': fundamentals,
            'dataPoints': len(price_history),
            'oldestDate': price_history[0]['date'] if price_history else None,
            'newestDate': price_history[-1]['date'] if price_history else None
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


def _is_fundamentals_empty(data):
    """Check if fundamentals data has all null key fields (Defeat Beta failed)"""
    if data is None:
        return True
    key_fields = ['roe', 'epsGrowth', 'revenueGrowth', 'debtToEquity']
    return all(data.get(field) is None for field in key_fields)


@app.route('/api/fundamentals/<ticker>', methods=['GET'])
def get_fundamentals(ticker):
    """
    Get rich fundamental data for scoring
    Tries Defeat Beta first, falls back to yfinance if Defeat Beta returns empty data

    Day 31: Fixed fallback logic - now checks if key fields are null, not just if dict exists
    """
    try:
        ticker = ticker.upper()

        # Try Defeat Beta first (richer data)
        fundamentals = None
        data_quality = 'none'
        fallback_used = False

        if DEFEATBETA_AVAILABLE:
            fundamentals = get_fundamentals_defeatbeta(ticker)

            # Day 31: Check if Defeat Beta actually returned useful data
            if _is_fundamentals_empty(fundamentals):
                print(f"⚠️ Defeat Beta returned empty data for {ticker}, trying yfinance fallback...")
                yf_fundamentals = get_fundamentals_yfinance(ticker)

                if yf_fundamentals and not _is_fundamentals_empty(yf_fundamentals):
                    fundamentals = yf_fundamentals
                    data_quality = 'yfinance_fallback'
                    fallback_used = True
                    print(f"✅ yfinance fallback successful for {ticker}")
                else:
                    # Both failed - keep defeatbeta empty response but mark quality
                    data_quality = 'unavailable'
                    print(f"❌ Both Defeat Beta and yfinance failed for {ticker}")
            else:
                data_quality = 'rich'

        # Primary fallback to yfinance if Defeat Beta not available
        if fundamentals is None:
            fundamentals = get_fundamentals_yfinance(ticker)
            data_quality = 'yfinance' if fundamentals else 'unavailable'

        if fundamentals is None:
            return jsonify({
                'error': f'Could not get fundamentals for {ticker}',
                'dataQuality': 'unavailable',
                'fallbackUsed': False
            }), 404

        # Add metadata to response
        fundamentals['ticker'] = ticker
        fundamentals['timestamp'] = datetime.now().isoformat()
        fundamentals['dataQuality'] = data_quality
        fundamentals['fallbackUsed'] = fallback_used

        return jsonify(fundamentals)
        
    except Exception as e:
        print(f"Error fetching fundamentals for {ticker}: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/market/spy', methods=['GET'])
def get_spy_data():
    """
    Get SPY (S&P 500 ETF) data for relative strength calculations
    """
    try:
        spy = yf.Ticker('SPY')
        hist = spy.history(period='2y')
        
        if hist.empty:
            return jsonify({'error': 'No SPY data found'}), 404
        
        # Get last 260 days
        hist_data = hist.tail(260)
        
        # Current price - ensure Python float
        current_price = round(float(hist_data.iloc[-1]['Close']), 2)
        
        # 52-week ago price
        price_52w_ago = None
        if len(hist_data) >= 252:
            price_52w_ago = round(float(hist_data.iloc[-252]['Close']), 2)
        elif len(hist_data) > 200:
            price_52w_ago = round(float(hist_data.iloc[0]['Close']), 2)
        
        # 13-week ago price
        price_13w_ago = None
        if len(hist_data) >= 63:
            price_13w_ago = round(float(hist_data.iloc[-63]['Close']), 2)
        
        # Prepare price history
        price_history = []
        for date, row in hist_data.iterrows():
            price_history.append({
                'date': date.strftime('%Y-%m-%d'),
                'close': round(float(row['Close']), 2),
                'volume': int(row['Volume'])
            })
        
        # Calculate 200 SMA for market regime
        sma_200 = round(float(hist_data['Close'].tail(200).mean()), 2)
        
        response = {
            'ticker': 'SPY',
            'currentPrice': current_price,
            'price52wAgo': price_52w_ago,
            'price13wAgo': price_13w_ago,
            'sma200': sma_200,
            'aboveSma200': bool(current_price > sma_200),  # FIX: Convert to Python bool
            'priceHistory': price_history,
            'dataPoints': len(price_history)
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error fetching SPY: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/market/vix', methods=['GET'])
def get_vix_data():
    """
    Get VIX (Volatility Index) data for risk assessment
    """
    try:
        vix = yf.Ticker('^VIX')
        hist = vix.history(period='1mo')
        
        if hist.empty:
            return jsonify({'error': 'No VIX data found'}), 404
        
        # FIX: Convert numpy float to Python float
        current_vix = float(hist.iloc[-1]['Close'])
        current_vix = round(current_vix, 2)
        
        # VIX levels interpretation
        if current_vix < 15:
            regime = 'low_volatility'
        elif current_vix < 20:
            regime = 'normal'
        elif current_vix < 25:
            regime = 'elevated'
        elif current_vix < 30:
            regime = 'high'
        else:
            regime = 'extreme'
        
        return jsonify({
            'ticker': 'VIX',
            'current': current_vix,
            'regime': regime,
            # FIX: Convert numpy.bool_ to Python bool
            'isRisky': bool(current_vix > 30)
        })
        
    except Exception as e:
        print(f"Error fetching VIX: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# ============================================
# SUPPORT & RESISTANCE ENDPOINT (Day 13)
# Day 15 Fix: Added proximity filter for actionable levels
# ============================================

@app.route('/api/sr/<ticker>', methods=['GET'])
def get_support_resistance(ticker):
    """
    Get Support & Resistance levels for a ticker
    
    Uses multi-method approach with failover:
    1. Pivot-based (primary) - Local highs/lows
    2. KMeans clustering (secondary) - Price bands
    3. Volume Profile (tertiary) - High-volume zones
    
    Day 15 Enhancement: Proximity filter ensures only actionable levels
    are used for trade setup (within 20% for support, 30% for resistance)
    
    Returns:
    - support: List of ACTIONABLE support levels (within range)
    - resistance: List of ACTIONABLE resistance levels (within range)
    - allSupport: All historical support levels (for reference)
    - allResistance: All historical resistance levels (for reference)
    - method: Which method was used (pivot/kmeans/volume_profile)
    - currentPrice: Current stock price
    - suggestedEntry: Nearest actionable support (potential entry)
    - suggestedStop: Below nearest support (stop loss)
    - suggestedTarget: Nearest actionable resistance (profit target)
    """
    if not SR_ENGINE_AVAILABLE:
        return jsonify({
            'error': 'S&R Engine not available',
            'message': 'Place support_resistance.py in backend folder and install scikit-learn'
        }), 503
    
    try:
        ticker = ticker.upper()
        print(f"🎯 Computing S&R levels for {ticker}...")
        
        # Fetch price data from yfinance
        stock = yf.Ticker(ticker)
        hist = stock.history(period='2y')
        
        if hist.empty:
            return jsonify({'error': f'No data found for {ticker}'}), 404
        
        # Get last 260 days (enough for S&R calculation)
        hist_data = hist.tail(260)
        
        if len(hist_data) < 150:
            return jsonify({
                'error': f'Insufficient data for {ticker}',
                'message': f'Need at least 150 bars, got {len(hist_data)}'
            }), 400
        
        # Prepare DataFrame for S&R engine (lowercase columns required)
        df = pd.DataFrame({
            'open': hist_data['Open'].values,
            'high': hist_data['High'].values,
            'low': hist_data['Low'].values,
            'close': hist_data['Close'].values,
            'volume': hist_data['Volume'].values
        })
        
        # Compute S&R levels
        sr_levels = compute_sr_levels(df)
        
        # Get current price
        current_price = float(df['close'].iloc[-1])

        # ============================================
        # Day 39: Calculate ADX (trend strength) and 4H RSI (momentum)
        # ============================================
        adx_data = calculate_adx(
            pd.Series(df['high'].values),
            pd.Series(df['low'].values),
            pd.Series(df['close'].values)
        )

        rsi_4h_data = calculate_rsi_4h(ticker)

        # Daily RSI for comparison
        daily_rsi = calculate_rsi(pd.Series(df['close'].values))

        # ============================================
        # PROXIMITY FILTER (Day 15 Fix)
        # Filter S&R levels to actionable range for swing trading
        # Support: within 20% below current price
        # Resistance: within 30% above current price
        # This fixes the bug where ancient support levels (e.g., $85 on $256 stock)
        # were being suggested as entry points
        # ============================================
        SUPPORT_PROXIMITY_PCT = 0.20    # 20% below current price max
        RESISTANCE_PROXIMITY_PCT = 0.30  # 30% above current price max
        
        support_floor = current_price * (1 - SUPPORT_PROXIMITY_PCT)
        resistance_ceiling = current_price * (1 + RESISTANCE_PROXIMITY_PCT)
        
        # Filter support levels to actionable range
        actionable_support = [s for s in sr_levels.support if s >= support_floor and s < current_price]
        
        # Filter resistance levels to actionable range  
        actionable_resistance = [r for r in sr_levels.resistance if r > current_price and r <= resistance_ceiling]
        
        # Calculate suggested trade levels using ACTIONABLE levels only
        suggested_entry = None
        suggested_stop = None
        suggested_target = None
        
        # Entry: Nearest ACTIONABLE support below current price
        if actionable_support:
            suggested_entry = round(max(actionable_support), 2)  # Nearest support
            # Stop: 3% below entry
            suggested_stop = round(suggested_entry * 0.97, 2)
        
        # Target: Nearest ACTIONABLE resistance above current price
        if actionable_resistance:
            suggested_target = round(min(actionable_resistance), 2)  # Nearest resistance
        
        # Calculate risk/reward if we have all levels
        risk_reward = None
        if suggested_entry and suggested_stop and suggested_target:
            risk = suggested_entry - suggested_stop
            reward = suggested_target - suggested_entry
            if risk > 0:
                risk_reward = round(reward / risk, 2)
        
        # Round all levels to 2 decimal places
        # Return ALL levels for display, but mark which are actionable
        all_support_levels = [round(s, 2) for s in sr_levels.support]
        all_resistance_levels = [round(r, 2) for r in sr_levels.resistance]
        actionable_support_levels = [round(s, 2) for s in actionable_support]
        actionable_resistance_levels = [round(r, 2) for r in actionable_resistance]
        
        response = {
            'ticker': ticker,
            'currentPrice': round(current_price, 2),
            'method': sr_levels.method,
            'support': actionable_support_levels,        # Only actionable levels
            'resistance': actionable_resistance_levels,  # Only actionable levels
            'allSupport': all_support_levels,            # All historical levels (for reference)
            'allResistance': all_resistance_levels,      # All historical levels (for reference)
            'suggestedEntry': suggested_entry,
            'suggestedStop': suggested_stop,
            'suggestedTarget': suggested_target,
            'riskReward': risk_reward,
            'dataPoints': len(df),
            'timestamp': datetime.now().isoformat(),
            'meta': {
                'methodUsed': sr_levels.method,
                'supportCount': len(actionable_support_levels),
                'resistanceCount': len(actionable_resistance_levels),
                'allSupportCount': len(all_support_levels),
                'allResistanceCount': len(all_resistance_levels),
                'atr': sr_levels.meta.get('atr'),
                'resistanceProjected': sr_levels.meta.get('resistance_projected', False),
                'supportProjected': sr_levels.meta.get('support_projected', False),
                'tradeViability': sr_levels.meta.get('trade_viability'),
                'proximityFilter': {
                    'supportFloor': round(support_floor, 2),
                    'resistanceCeiling': round(resistance_ceiling, 2),
                    'supportPct': SUPPORT_PROXIMITY_PCT,
                    'resistancePct': RESISTANCE_PROXIMITY_PCT
                },
                # Day 33: Add MTF confluence data
                'mtf': sr_levels.meta.get('mtf'),
                # Day 39: Add trend strength and momentum indicators
                'adx': adx_data,
                'rsi_4h': rsi_4h_data,
                'rsi_daily': daily_rsi
            }
        }
        
        print(f"✅ S&R for {ticker}: {sr_levels.method} method")
        print(f"   All Support: {all_support_levels} | Actionable: {actionable_support_levels}")
        print(f"   All Resistance: {all_resistance_levels} | Actionable: {actionable_resistance_levels}")
        print(f"   Entry: {suggested_entry}, Stop: {suggested_stop}, Target: {suggested_target}")
        if not actionable_support_levels:
            print(f"   ⚠️ No actionable support within {SUPPORT_PROXIMITY_PCT*100}% of current price")
        if not actionable_resistance_levels:
            print(f"   ⚠️ No actionable resistance within {RESISTANCE_PROXIMITY_PCT*100}% of current price")
        if sr_levels.meta.get('resistance_projected'):
            print(f"   ⚠️ Resistance levels are PROJECTED (ATR-based)")
        
        return jsonify(response)
        
    except SRFailure as e:
        print(f"S&R calculation failed for {ticker}: {e}")
        return jsonify({'error': str(e)}), 400
        
    except Exception as e:
        print(f"Error computing S&R for {ticker}: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# ============================================
# TRADINGVIEW SCREENER ENDPOINT (Day 11 / Fixed Day 20)
# Batch scanning for trading opportunities
# ============================================

@app.route('/api/scan/tradingview', methods=['GET'])
def scan_tradingview():
    """
    Scan for trading opportunities using TradingView screener.
    
    Day 20 Fix v3: Filter by exchange to exclude OTC stocks
    """
    if not TRADINGVIEW_AVAILABLE:
        return jsonify({
            'error': 'TradingView Screener not available',
            'message': 'Install with: pip install tradingview-screener'
        }), 503
    
    try:
        strategy = request.args.get('strategy', 'reddit').lower()
        limit = int(request.args.get('limit', 50))
        
        print(f"🔍 TradingView Scan: strategy={strategy}, limit={limit}")
        
        # Build query
        query = (Query()
            .set_markets('america')
            .select('name', 'close', 'volume', 'market_cap_basic',
                    'price_52_week_high', 'price_52_week_low',
                    'SMA50', 'SMA200', 'RSI', 'relative_volume_10d_calc',
                    'sector', 'change', 'exchange')
        )
        
        # Day 21 Fix: Consolidate ALL filters into single .where() call
        # Multiple .where() calls may replace filters instead of appending in v3.0.0
        # This was causing the exchange filter to be lost, returning OTC stocks
        
        # Strategy-specific filters - ALL filters in ONE .where() call
        if strategy == 'reddit':
            query = query.where(
                col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
                col('market_cap_basic') >= 2_000_000_000,
                col('relative_volume_10d_calc') >= 1.5,
                col('close') > col('SMA50'),
                col('SMA50') > col('SMA200')
            )
        elif strategy == 'minervini':
            query = query.where(
                col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
                col('market_cap_basic') >= 10_000_000_000,
                col('close') > col('SMA50'),
                col('SMA50') > col('SMA200'),
                col('change|1W') >= 0,
                col('change|1M') >= 0
            )
        elif strategy == 'momentum':
            query = query.where(
                col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
                col('market_cap_basic') >= 1_000_000_000,
                col('close') > col('SMA50'),
                col('SMA50') > col('SMA200'),
                col('RSI') >= 50,
                col('RSI') <= 75
            )
        elif strategy == 'value':
            query = query.where(
                col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
                col('market_cap_basic') >= 5_000_000_000,
                col('close') > col('SMA200'),
                col('RSI') <= 60
            )
        elif strategy == 'best':
            # Day 26: "Best Candidates" - strictest criteria matching our scoring system
            # Designed to find stocks most likely to get BUY verdict (score >= 60)
            query = query.where(
                col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
                col('market_cap_basic') >= 10_000_000_000,  # Large-cap quality
                col('close') > col('SMA50'),                # Price > 50 SMA
                col('SMA50') > col('SMA200'),               # 50 SMA > 200 SMA (Stage 2)
                col('RSI') >= 50,                           # Bullish momentum
                col('RSI') <= 75,                           # Not overbought (matches momentum strategy)
                col('relative_volume_10d_calc') >= 1.0,     # At least average volume
                col('change|1W') >= 0,                      # Positive weekly
                col('change|1M') >= 0                       # Positive monthly
            )
            # Sort by relative volume (highest interest first)
            query = query.order_by('relative_volume_10d_calc', ascending=False)
        else:
            return jsonify({'error': f'Unknown strategy: {strategy}'}), 400
        
        query = query.order_by('relative_volume_10d_calc', ascending=False)
        query = query.limit(limit)
        
        # Execute
        count, results = query.get_scanner_data()
        
        # Format results
        candidates = []
        for _, row in results.iterrows():
            try:
                ticker = row.get('ticker', '')
                if ':' in str(ticker):
                    ticker = str(ticker).split(':')[-1]

                # Day 26: Filter out non-common stocks
                # Skip preferred stocks (contain "/"), SPAC units (end in U), warrants (end in W)
                if '/' in ticker:
                    continue  # Preferred stock (e.g., BAC/PL, KKR/PD)
                if len(ticker) >= 4 and ticker.endswith('U'):
                    continue  # SPAC unit (e.g., BTSGU)
                if len(ticker) >= 4 and ticker.endswith('W'):
                    continue  # Warrant (e.g., SPFRW)
                if len(ticker) >= 5 and ticker.endswith('WS'):
                    continue  # Warrant series (e.g., ABCDWS)
                if len(ticker) >= 5 and ticker[-1] in 'PMNOL' and ticker[-2].isupper():
                    continue  # Preferred stock series (e.g., CNOBP, VLYPP, FTAIM)
                # Skip commodity ETFs/trusts
                if ticker in ['PHYS', 'PSLV', 'GLD', 'SLV', 'IAU', 'GLDM', 'SGOL', 'SIVR']:
                    continue  # Commodity trusts - not equities

                current = row.get('close')
                high52w = row.get('price_52_week_high')
                pct_from_high = None
                if current and high52w and high52w > 0:
                    pct_from_high = round(((current - high52w) / high52w) * 100, 1)
                
                candidates.append({
                    'ticker': ticker,
                    'name': row.get('name', ''),
                    'price': safe_float(row.get('close')),
                    'change': safe_float(row.get('change')),  # Day 26: Added change field
                    'volume': safe_int(row.get('volume')),
                    'marketCap': safe_int(row.get('market_cap_basic')),
                    'high52w': safe_float(row.get('price_52_week_high')),
                    'low52w': safe_float(row.get('price_52_week_low')),
                    'sma50': safe_float(row.get('SMA50')),
                    'sma200': safe_float(row.get('SMA200')),
                    'rsi': safe_float(row.get('RSI')),
                    'relativeVolume': safe_float(row.get('relative_volume_10d_calc')),
                    'sector': row.get('sector', 'N/A'),
                    'pctFromHigh': pct_from_high,
                    'exchange': row.get('exchange', 'N/A')
                })
            except Exception as e:
                print(f"Error parsing row: {e}")
                continue
        
        print(f"✅ TradingView Scan complete: {len(candidates)} candidates from {count} matches")
        
        return jsonify({
            'strategy': strategy,
            'totalMatches': count,
            'returned': len(candidates),
            'candidates': candidates,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"❌ TradingView scan error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500



@app.route('/api/scan/strategies', methods=['GET'])
def get_scan_strategies():
    """Return available scan strategies."""
    return jsonify({
        'strategies': [
            {
                'id': 'reddit',
                'name': 'Reddit Style',
                'description': 'Mid-cap+, high relative volume, momentum stocks'
            },
            {
                'id': 'minervini',
                'name': 'Minervini SEPA',
                'description': 'Large-cap momentum leaders in Stage 2 uptrend'
            },
            {
                'id': 'momentum',
                'name': 'Momentum',
                'description': 'Sustainable gains, RSI 50-75 (not overbought)'
            },
            {
                'id': 'value',
                'name': 'Value',
                'description': 'Quality stocks above 200 SMA at fair RSI levels'
            },
            {
                'id': 'best',
                'name': 'Best Candidates',
                'description': 'Large-cap Stage 2 stocks matching all scoring criteria (most likely BUY)'
            }
        ]
    })




# ============================================
# VALIDATION ENGINE ENDPOINTS (Day 15)
# ============================================

@app.route('/api/validation/run', methods=['POST'])
def run_validation():
    """
    Run validation suite for specified tickers.
    
    Request body (optional):
    {
        "tickers": ["AAPL", "NVDA", "JPM", "MU", "COST"]
    }
    """
    if not VALIDATION_AVAILABLE:
        return jsonify({
            'error': 'Validation Engine not available',
            'message': 'Ensure validation/ folder exists with all required files'
        }), 503
    
    try:
        data = request.get_json() or {}
        tickers = data.get('tickers', ['AAPL', 'NVDA', 'JPM', 'MU', 'COST'])
        
        print(f"🔍 Running validation for: {tickers}")
        
        engine = ValidationEngine(tickers=tickers)
        report = engine.run_validation()
        
        result = {
            'run_id': report.run_id,
            'timestamp': report.timestamp,
            'tickers': report.tickers,
            'overall_pass_rate': report.overall_pass_rate,
            'summary': report.summary,
            'ticker_results': []
        }
        
        for tv in report.ticker_results:
            tv_dict = {
                'ticker': tv.ticker,
                'overall_status': tv.overall_status.value,
                'pass_count': tv.pass_count,
                'fail_count': tv.fail_count,
                'warning_count': tv.warning_count,
                'results': []
            }
            for r in tv.results:
                tv_dict['results'].append({
                    'metric': r.metric,
                    'our_value': r.our_value,
                    'external_value': r.external_value,
                    'external_source': r.external_source,
                    'variance_pct': r.variance_pct,
                    'tolerance_pct': r.tolerance_pct,
                    'status': r.status.value,
                    'notes': r.notes
                })
            result['ticker_results'].append(tv_dict)
        
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Validation error: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/validation/results', methods=['GET'])
def get_validation_results():
    """Get the latest validation results."""
    if not VALIDATION_AVAILABLE:
        return jsonify({'error': 'Validation Engine not available'}), 503
    
    try:
        results_dir = os.path.join(os.path.dirname(__file__), 'validation_results')
        run_id = request.args.get('run_id')
        
        if run_id:
            filepath = os.path.join(results_dir, f'validation_{run_id}.json')
        else:
            if not os.path.exists(results_dir):
                return jsonify({'error': 'No validation results found'}), 404
            
            files = [f for f in os.listdir(results_dir) if f.startswith('validation_') and f.endswith('.json')]
            if not files:
                return jsonify({'error': 'No validation results found'}), 404
            
            files.sort(reverse=True)
            filepath = os.path.join(results_dir, files[0])
        
        if not os.path.exists(filepath):
            return jsonify({'error': 'Validation results not found'}), 404
        
        with open(filepath, 'r') as f:
            results = json.load(f)
        
        return jsonify(results)
        
    except Exception as e:
        print(f"❌ Error fetching validation results: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/validation/history', methods=['GET'])
def get_validation_history():
    """Get list of all validation runs."""
    if not VALIDATION_AVAILABLE:
        return jsonify({'error': 'Validation Engine not available'}), 503
    
    try:
        results_dir = os.path.join(os.path.dirname(__file__), 'validation_results')
        
        if not os.path.exists(results_dir):
            return jsonify({'runs': []})
        
        limit = int(request.args.get('limit', 10))
        
        files = [f for f in os.listdir(results_dir) if f.startswith('validation_') and f.endswith('.json')]
        files.sort(reverse=True)
        files = files[:limit]
        
        runs = []
        for filename in files:
            filepath = os.path.join(results_dir, filename)
            with open(filepath, 'r') as f:
                data = json.load(f)
                runs.append({
                    'run_id': data['run_id'],
                    'timestamp': data['timestamp'],
                    'overall_pass_rate': data['overall_pass_rate'],
                    'summary': data['summary']
                })
        
        return jsonify({'runs': runs})
        
    except Exception as e:
        print(f"❌ Error fetching validation history: {e}")
        return jsonify({'error': str(e)}), 500


# ============================================
# FORWARD TEST ENDPOINTS
# ============================================

@app.route('/api/forward-test/record', methods=['POST'])
def record_forward_test_signal():
    """
    Record a trading signal for forward testing.
    
    Request body:
    {
        "ticker": "AAPL",
        "signal_type": "BUY",
        "score": 65,
        "price_at_signal": 250.00,
        "entry_price": 245.00,
        "stop_price": 238.00,
        "target_price": 270.00,
        "risk_reward": 3.57,
        "verdict_reason": "Strong score with good RS"
    }
    """
    if not VALIDATION_AVAILABLE:
        return jsonify({'error': 'Forward Test Tracker not available'}), 503
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body required'}), 400
        
        required = ['ticker', 'signal_type', 'score', 'price_at_signal']
        for field in required:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        signal_map = {'BUY': SignalType.BUY, 'HOLD': SignalType.HOLD, 'AVOID': SignalType.AVOID}
        signal_type = signal_map.get(data['signal_type'].upper())
        if not signal_type:
            return jsonify({'error': f'Invalid signal_type: {data["signal_type"]}'}), 400
        
        tracker = ForwardTestTracker()
        signal_id = tracker.record_signal(
            ticker=data['ticker'].upper(),
            signal_type=signal_type,
            score=data['score'],
            price_at_signal=data['price_at_signal'],
            entry_price=data.get('entry_price'),
            stop_price=data.get('stop_price'),
            target_price=data.get('target_price'),
            risk_reward=data.get('risk_reward'),
            verdict_reason=data.get('verdict_reason', ''),
            notes=data.get('notes', '')
        )
        
        return jsonify({
            'success': True,
            'signal_id': signal_id,
            'message': f'Recorded {signal_type.value} signal for {data["ticker"]}'
        })
        
    except Exception as e:
        print(f"❌ Error recording signal: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/forward-test/signals', methods=['GET'])
def get_forward_test_signals():
    """Get recent forward test signals."""
    if not VALIDATION_AVAILABLE:
        return jsonify({'error': 'Forward Test Tracker not available'}), 503
    
    try:
        days = int(request.args.get('days', 30))
        limit = int(request.args.get('limit', 50))
        ticker = request.args.get('ticker')
        
        tracker = ForwardTestTracker()
        
        if ticker:
            signals = tracker.get_signal_by_ticker(ticker.upper())
        else:
            signals = tracker.get_recent_signals(days=days, limit=limit)
        
        return jsonify({'count': len(signals), 'signals': signals})
        
    except Exception as e:
        print(f"❌ Error fetching signals: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/forward-test/performance', methods=['GET'])
def get_forward_test_performance():
    """Get forward test performance summary (win rate, avg P&L, etc.)."""
    if not VALIDATION_AVAILABLE:
        return jsonify({'error': 'Forward Test Tracker not available'}), 503
    
    try:
        tracker = ForwardTestTracker()
        summary = tracker.get_performance_summary()
        return jsonify(summary)
        
    except Exception as e:
        print(f"❌ Error fetching performance: {e}")
        return jsonify({'error': str(e)}), 500

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Swing Trade Analyzer Backend v2.5")
    print("="*50)
    print(f"Defeat Beta: {'✅ Available' if DEFEATBETA_AVAILABLE else '❌ Not installed'}")
    print(f"TradingView: {'✅ Available' if TRADINGVIEW_AVAILABLE else '❌ Not installed'}")
    print(f"S&R Engine:  {'✅ Available' if SR_ENGINE_AVAILABLE else '❌ Not installed'}")
    print("Starting server on port 5001...")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5001)