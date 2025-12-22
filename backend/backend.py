"""
Swing Trade Analyzer Backend - v2.5
Flask API server with yfinance (prices) + Defeat Beta (fundamentals) + TradingView Screener (scanning) + S&R Engine

Day 6: Fixed numpy type serialization issues
Day 8: Fixed Defeat Beta .data attribute usage
Day 11: Added TradingView screener integration for batch scanning
Day 13: Added Support & Resistance engine endpoint
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



def get_fundamentals_defeatbeta(ticker_symbol):
    """
    Get rich fundamental data from Defeat Beta
    Returns ROE, ROIC, ROA, EPS growth, revenue growth, etc.
    
    Day 8 FIX: Use .data attribute instead of .to_df()
    DataFrame structure: Columns = ['Breakdown', '2024-10-31', '2023-10-31', ...]
    Values are in rows with labels in 'Breakdown' column
    """
    if not DEFEATBETA_AVAILABLE:
        return None
    
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
        
        return {
            'source': 'yfinance',
            'pe': safe_float(safe_get(info, 'trailingPE')),
            'forwardPe': safe_float(safe_get(info, 'forwardPE')),
            'pegRatio': safe_float(safe_get(info, 'pegRatio')),
            'marketCap': safe_int(safe_get(info, 'marketCap')),
            'roe': roe or safe_float(safe_get(info, 'returnOnEquity')),
            'roa': roa or safe_float(safe_get(info, 'returnOnAssets')),
            'roic': None,
            'epsGrowth': safe_float(safe_get(info, 'earningsGrowth')),
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

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.6',
        'defeatbeta_available': DEFEATBETA_AVAILABLE,
        'tradingview_available': TRADINGVIEW_AVAILABLE,
        'sr_engine_available': SR_ENGINE_AVAILABLE,
        'validation_available': VALIDATION_AVAILABLE
    })


@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    """
    Get stock data for analysis
    Uses yfinance for price data (real-time)
    """
    try:
        ticker = ticker.upper()
        stock = yf.Ticker(ticker)
        
        # Get historical data (260 trading days for 52-week calculations)
        hist = stock.history(period='2y')
        
        if hist.empty:
            return jsonify({'error': f'No data found for {ticker}'}), 404
        
        # FIXED: Get last 260 days (covers full 52 weeks of trading)
        hist_data = hist.tail(260)
        
        # Get stock info
        info = stock.info
        
        # Prepare price history
        price_history = []
        for date, row in hist_data.iterrows():
            price_history.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': round(float(row['Open']), 2),
                'high': round(float(row['High']), 2),
                'low': round(float(row['Low']), 2),
                'close': round(float(row['Close']), 2),
                'volume': int(row['Volume'])
            })
        
        # Get 52-week ago price (approximately 252 trading days)
        price_52w_ago = None
        if len(hist_data) >= 252:
            price_52w_ago = round(float(hist_data.iloc[-252]['Close']), 2)
        elif len(hist_data) > 200:
            price_52w_ago = round(float(hist_data.iloc[0]['Close']), 2)
        
        # Get 13-week ago price (approximately 63 trading days)
        price_13w_ago = None
        if len(hist_data) >= 63:
            price_13w_ago = round(float(hist_data.iloc[-63]['Close']), 2)
        
        # Current price
        current_price = round(float(hist_data.iloc[-1]['Close']), 2)
        
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


@app.route('/api/fundamentals/<ticker>', methods=['GET'])
def get_fundamentals(ticker):
    """
    Get rich fundamental data for scoring
    Tries Defeat Beta first, falls back to yfinance
    """
    try:
        ticker = ticker.upper()
        
        # Try Defeat Beta first (richer data)
        fundamentals = None
        if DEFEATBETA_AVAILABLE:
            fundamentals = get_fundamentals_defeatbeta(ticker)
        
        # Fallback to yfinance
        if fundamentals is None:
            fundamentals = get_fundamentals_yfinance(ticker)
        
        if fundamentals is None:
            return jsonify({'error': f'Could not get fundamentals for {ticker}'}), 404
        
        # Add ticker to response
        fundamentals['ticker'] = ticker
        fundamentals['timestamp'] = datetime.now().isoformat()
        
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
                'proximityFilter': {
                    'supportFloor': round(support_floor, 2),
                    'resistanceCeiling': round(resistance_ceiling, 2),
                    'supportPct': SUPPORT_PROXIMITY_PCT,
                    'resistancePct': RESISTANCE_PROXIMITY_PCT
                }
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
# VALIDATION ENGINE ENDPOINTS (Day 15)
# Add these to backend.py after the S&R endpoint
# ============================================

# ============================================
# VALIDATION ENGINE ENDPOINTS (Day 15)
# 
# HOW TO USE:
# Copy everything below and paste into backend.py 
# AFTER the /api/scan/strategies endpoint
# BEFORE the # MAIN section
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