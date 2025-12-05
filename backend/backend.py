"""
Swing Trade Analyzer Backend - v2.1
Flask API server with yfinance (prices) + Defeat Beta (fundamentals)

Day 6: Fixed numpy type serialization issues
- VIX endpoint: bool() and float() conversions
- Fundamentals endpoint: DataFrame value conversions
"""

from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
from datetime import datetime, timedelta
import traceback

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
        'version': '2.1',
        'defeatbeta_available': DEFEATBETA_AVAILABLE
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
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Swing Trade Analyzer Backend v2.1")
    print("="*50)
    print(f"Defeat Beta: {'✅ Available' if DEFEATBETA_AVAILABLE else '❌ Not installed'}")
    print("Starting server on port 5001...")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5001)