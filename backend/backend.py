"""
Swing Trade Analyzer Backend - v2.5
Flask API server with yfinance (prices) + Defeat Beta (fundamentals) + TradingView Screener (scanning) + S&R Engine

Day 6: Fixed numpy type serialization issues
Day 8: Fixed Defeat Beta .data attribute usage
Day 11: Added TradingView screener integration for batch scanning
Day 13: Added Support & Resistance engine endpoint
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf
from datetime import datetime, timedelta
import traceback
import pandas as pd
import numpy as np

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
        'version': '2.5',
        'defeatbeta_available': DEFEATBETA_AVAILABLE,
        'tradingview_available': TRADINGVIEW_AVAILABLE,
        'sr_engine_available': SR_ENGINE_AVAILABLE
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
# ============================================

@app.route('/api/sr/<ticker>', methods=['GET'])
def get_support_resistance(ticker):
    """
    Get Support & Resistance levels for a ticker
    
    Uses multi-method approach with failover:
    1. Pivot-based (primary) - Local highs/lows
    2. KMeans clustering (secondary) - Price bands
    3. Volume Profile (tertiary) - High-volume zones
    
    Returns:
    - support: List of support levels (below current price)
    - resistance: List of resistance levels (above current price)
    - method: Which method was used (pivot/kmeans/volume_profile)
    - currentPrice: Current stock price
    - suggestedEntry: Nearest support level (potential entry)
    - suggestedStop: Below nearest support (stop loss)
    - suggestedTarget: Nearest resistance (profit target)
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
        
        # Calculate suggested trade levels
        suggested_entry = None
        suggested_stop = None
        suggested_target = None
        
        # Entry: Nearest support below current price
        if sr_levels.support:
            supports_below = [s for s in sr_levels.support if s < current_price]
            if supports_below:
                suggested_entry = round(max(supports_below), 2)  # Nearest support
                # Stop: 2-3% below entry or next lower support
                suggested_stop = round(suggested_entry * 0.97, 2)  # 3% below entry
        
        # Target: Nearest resistance above current price
        if sr_levels.resistance:
            resistances_above = [r for r in sr_levels.resistance if r > current_price]
            if resistances_above:
                suggested_target = round(min(resistances_above), 2)  # Nearest resistance
        
        # Calculate risk/reward if we have all levels
        risk_reward = None
        if suggested_entry and suggested_stop and suggested_target:
            risk = suggested_entry - suggested_stop
            reward = suggested_target - suggested_entry
            if risk > 0:
                risk_reward = round(reward / risk, 2)
        
        # Round all levels to 2 decimal places
        support_levels = [round(s, 2) for s in sr_levels.support]
        resistance_levels = [round(r, 2) for r in sr_levels.resistance]
        
        response = {
            'ticker': ticker,
            'currentPrice': round(current_price, 2),
            'method': sr_levels.method,
            'support': support_levels,
            'resistance': resistance_levels,
            'suggestedEntry': suggested_entry,
            'suggestedStop': suggested_stop,
            'suggestedTarget': suggested_target,
            'riskReward': risk_reward,
            'dataPoints': len(df),
            'timestamp': datetime.now().isoformat(),
            'meta': {
                'methodUsed': sr_levels.method,
                'supportCount': len(support_levels),
                'resistanceCount': len(resistance_levels)
            }
        }
        
        print(f"✅ S&R for {ticker}: {sr_levels.method} method")
        print(f"   Support: {support_levels}")
        print(f"   Resistance: {resistance_levels}")
        print(f"   Entry: {suggested_entry}, Stop: {suggested_stop}, Target: {suggested_target}")
        
        return jsonify(response)
        
    except SRFailure as e:
        print(f"S&R calculation failed for {ticker}: {e}")
        return jsonify({'error': str(e)}), 400
        
    except Exception as e:
        print(f"Error computing S&R for {ticker}: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# ============================================
# TRADINGVIEW SCREENER ENDPOINTS (Day 11)
# ============================================

@app.route('/api/scan/tradingview', methods=['GET'])
def scan_tradingview():
    """
    Scan for swing trade candidates using TradingView screener
    
    Query Parameters:
    - strategy: 'reddit' (default), 'minervini', 'momentum', 'value'
    - limit: max results (default 50, max 100)
    
    Reddit Strategy Filters (from r/swingtrading):
    - Price > $5 (avoid penny stocks)
    - Market Cap > $300M (liquidity)
    - Average Volume > 500K (tradeable)
    - Price > 50 SMA (uptrend)
    - Price > 200 SMA (long-term uptrend)
    - Relative Volume > 1.0 (activity)
    
    Returns pre-filtered candidates for further analysis
    """
    if not TRADINGVIEW_AVAILABLE:
        return jsonify({
            'error': 'TradingView Screener not installed',
            'message': 'Install with: pip install tradingview-screener'
        }), 503
    
    try:
        # Get query parameters
        strategy = request.args.get('strategy', 'reddit').lower()
        limit = min(int(request.args.get('limit', 50)), 100)  # Cap at 100
        
        print(f"🔍 TradingView Scan: strategy={strategy}, limit={limit}")
        
        # Build query based on strategy
        if strategy == 'reddit':
            # Reddit r/swingtrading strategy - REFINED
            # Focus: Liquid, institutional-quality uptrending stocks
            query = (
                Query()
                .select(
                    'name', 'close', 'volume', 'market_cap_basic',
                    'relative_volume_10d_calc', 'price_52_week_high',
                    'SMA50', 'SMA200', 'EMA20', 'RSI', 'change',
                    'average_volume_10d_calc', 'sector', 'industry'
                )
                .where(
                    col('close') > 10,                        # Price > $10 (no penny stocks)
                    col('market_cap_basic') > 2_000_000_000,  # Market cap > $2B (mid-cap+)
                    col('volume') > 500_000,                  # Volume > 500K
                    col('average_volume_10d_calc') > 500_000, # Avg volume > 500K (consistent liquidity)
                    col('close') > col('SMA50'),             # Price > 50 SMA (uptrend)
                    col('close') > col('SMA200'),            # Price > 200 SMA (long-term)
                    col('SMA50') > col('SMA200'),            # 50 > 200 (Stage 2 confirmed)
                    col('relative_volume_10d_calc') > 1.0,   # Relative volume > 1x
                    col('RSI') > 40,                          # Not oversold
                    col('RSI') < 75,                          # Not overbought (avoid chasing)
                    col('exchange').isin(['NASDAQ', 'NYSE', 'AMEX']),  # Major exchanges only
                    col('is_primary') == True,
                    col('type') == 'stock',
                )
                .order_by('relative_volume_10d_calc', ascending=False)
                .limit(limit)
            )
            
        elif strategy == 'minervini':
            # Mark Minervini SEPA-style filters - REFINED
            # Focus: Stage 2 leaders near 52-week highs, institutional quality
            query = (
                Query()
                .select(
                    'name', 'close', 'volume', 'market_cap_basic',
                    'relative_volume_10d_calc', 'price_52_week_high',
                    'SMA50', 'SMA200', 'EMA20', 'RSI', 'change',
                    'Perf.1M', 'Perf.3M', 'average_volume_10d_calc',
                    'sector', 'industry'
                )
                .where(
                    col('close') > 15,                        # Price > $15
                    col('market_cap_basic') > 5_000_000_000,  # Market cap > $5B (large-cap)
                    col('volume') > 500_000,
                    col('average_volume_10d_calc') > 500_000,
                    col('close') > col('SMA50'),             # Price > 50 SMA
                    col('SMA50') > col('SMA200'),            # 50 > 200 (Stage 2)
                    col('close') > col('SMA200'),            # Price > 200 SMA
                    col('RSI') > 50,                          # RSI > 50 (momentum)
                    col('RSI') < 75,                          # RSI < 75 (not overbought)
                    col('exchange').isin(['NASDAQ', 'NYSE']), # Major exchanges only
                    col('is_primary') == True,
                    col('type') == 'stock',
                )
                .order_by('Perf.1M', ascending=False)  # Best recent performers
                .limit(limit)
            )
            
        elif strategy == 'momentum':
            # Pure momentum - REFINED
            # Focus: Strong but sustainable momentum, not moonshots
            query = (
                Query()
                .select(
                    'name', 'close', 'volume', 'market_cap_basic',
                    'relative_volume_10d_calc', 'price_52_week_high',
                    'SMA50', 'SMA200', 'EMA20', 'RSI', 'change',
                    'Perf.W', 'Perf.1M', 'Perf.3M',
                    'average_volume_10d_calc', 'sector', 'industry'
                )
                .where(
                    col('close') > 15,
                    col('market_cap_basic') > 5_000_000_000,   # $5B+ (institutional)
                    col('volume') > 500_000,
                    col('average_volume_10d_calc') > 500_000,
                    col('close') > col('SMA50'),
                    col('close') > col('SMA200'),
                    col('SMA50') > col('SMA200'),              # Stage 2
                    col('RSI') > 50,
                    col('RSI') < 70,                           # Tighter RSI cap
                    col('Perf.1M') > 5,                        # Up at least 5% in month
                    col('Perf.1M') < 50,                       # But not moonshots (< 50%)
                    col('exchange').isin(['NASDAQ', 'NYSE']),
                    col('is_primary') == True,
                    col('type') == 'stock',
                )
                .order_by('Perf.1M', ascending=False)
                .limit(limit)
            )
            
        elif strategy == 'value':
            # Value + momentum combo - REFINED
            # Focus: Quality companies at reasonable valuations, in uptrends
            query = (
                Query()
                .select(
                    'name', 'close', 'volume', 'market_cap_basic',
                    'relative_volume_10d_calc', 'price_52_week_high',
                    'SMA50', 'SMA200', 'EMA20', 'RSI', 'change',
                    'price_earnings_ttm', 'price_sales_ratio',
                    'average_volume_10d_calc', 'sector', 'industry'
                )
                .where(
                    col('close') > 15,
                    col('market_cap_basic') > 10_000_000_000,  # $10B+ (large-cap)
                    col('volume') > 500_000,
                    col('average_volume_10d_calc') > 1_000_000, # High liquidity
                    col('close') > col('SMA50'),
                    col('close') > col('SMA200'),
                    col('SMA50') > col('SMA200'),              # Stage 2
                    col('price_earnings_ttm') > 5,             # P/E > 5 (avoid distressed)
                    col('price_earnings_ttm') < 25,            # P/E < 25 (reasonable)
                    col('RSI') > 45,
                    col('RSI') < 70,
                    col('exchange').isin(['NASDAQ', 'NYSE']),
                    col('is_primary') == True,
                    col('type') == 'stock',
                )
                .order_by('market_cap_basic', ascending=False)  # Largest first
                .limit(limit)
            )
            
        else:
            return jsonify({
                'error': f'Unknown strategy: {strategy}',
                'available': ['reddit', 'minervini', 'momentum', 'value']
            }), 400
        
        # Execute query
        count, results_df = query.get_scanner_data()
        
        print(f"📊 Found {count} total matches, returning {len(results_df)} results")
        
        # Convert to list of dicts
        candidates = []
        for _, row in results_df.iterrows():
            candidate = {
                'ticker': row.get('ticker', '').replace('NASDAQ:', '').replace('NYSE:', '').replace('AMEX:', ''),
                'name': row.get('name', ''),
                'price': safe_float(row.get('close')),
                'volume': safe_int(row.get('volume')),
                'marketCap': safe_int(row.get('market_cap_basic')),
                'relativeVolume': safe_float(row.get('relative_volume_10d_calc')),
                'high52w': safe_float(row.get('price_52_week_high')),
                'sma50': safe_float(row.get('SMA50')),
                'sma200': safe_float(row.get('SMA200')),
                'ema20': safe_float(row.get('EMA20')),
                'rsi': safe_float(row.get('RSI')),
                'changePercent': safe_float(row.get('change')),
                'sector': row.get('sector', ''),
                'industry': row.get('industry', ''),
            }
            
            # Add performance metrics if available (momentum strategy)
            if 'Perf.W' in row:
                candidate['perfWeek'] = safe_float(row.get('Perf.W'))
            if 'Perf.1M' in row:
                candidate['perf1Month'] = safe_float(row.get('Perf.1M'))
            if 'Perf.3M' in row:
                candidate['perf3Month'] = safe_float(row.get('Perf.3M'))
            
            # Add valuation metrics if available (value strategy)
            if 'price_earnings_ttm' in row:
                candidate['pe'] = safe_float(row.get('price_earnings_ttm'))
            if 'price_sales_ratio' in row:
                candidate['ps'] = safe_float(row.get('price_sales_ratio'))
            
            # Calculate % from 52-week high
            if candidate['price'] and candidate['high52w']:
                candidate['pctFrom52wHigh'] = round(
                    ((candidate['price'] - candidate['high52w']) / candidate['high52w']) * 100, 2
                )
            
            candidates.append(candidate)
        
        return jsonify({
            'strategy': strategy,
            'totalMatches': count,
            'returned': len(candidates),
            'limit': limit,
            'timestamp': datetime.now().isoformat(),
            'candidates': candidates
        })
        
    except Exception as e:
        print(f"Error in TradingView scan: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/api/scan/strategies', methods=['GET'])
def get_scan_strategies():
    """
    List available scanning strategies and their descriptions
    """
    strategies = {
        'reddit': {
            'name': 'Reddit Swing Trading (Refined)',
            'description': 'Price>$10, MarketCap>$2B, Stage 2 uptrend (50>200 SMA), RSI 40-75, RelVolume>1x, Major exchanges only',
            'focus': 'Liquid mid-cap+ stocks in confirmed uptrends with unusual activity',
            'typical_results': '20-60 candidates'
        },
        'minervini': {
            'name': 'Minervini SEPA Style',
            'description': 'Price>$15, MarketCap>$5B, Stage 2 (50>200 SMA), RSI 50-75, sorted by 1-month performance',
            'focus': 'Large-cap momentum leaders in Stage 2 uptrends',
            'typical_results': '15-40 candidates'
        },
        'momentum': {
            'name': 'Sustainable Momentum',
            'description': 'MarketCap>$5B, Stage 2 uptrend, RSI 50-70, 1-month gain 5-50% (no moonshots)',
            'focus': 'Strong but sustainable momentum, avoiding overbought/parabolic moves',
            'typical_results': '10-30 candidates'
        },
        'value': {
            'name': 'Value + Momentum',
            'description': 'MarketCap>$10B, Stage 2 uptrend, P/E 5-25, RSI 45-70, high liquidity',
            'focus': 'Large-cap quality companies at reasonable valuations in uptrends',
            'typical_results': '20-50 candidates'
        }
    }
    
    return jsonify({
        'tradingview_available': TRADINGVIEW_AVAILABLE,
        'sr_engine_available': SR_ENGINE_AVAILABLE,
        'strategies': strategies,
        'usage': 'GET /api/scan/tradingview?strategy=reddit&limit=50',
        'notes': 'All strategies filter for NYSE/NASDAQ only (no OTC), require Stage 2 uptrend, and cap RSI to avoid chasing'
    })


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