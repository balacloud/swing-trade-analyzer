"""
Swing Trade Analyzer Backend - v2.0
Flask API server with yfinance (prices) + Defeat Beta (fundamentals)

Day 5: Added Defeat Beta integration for rich fundamental data
- ROE, ROIC, ROA
- EPS Growth, Revenue Growth
- PEG Ratio, Debt/Equity
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
        return ((current - previous) / abs(previous)) * 100
    except:
        return None


def get_fundamentals_defeatbeta(ticker_symbol):
    """
    Get rich fundamental data from Defeat Beta
    Returns ROE, ROIC, ROA, EPS growth, revenue growth, etc.
    """
    if not DEFEATBETA_AVAILABLE:
        return None
    
    try:
        ticker = DBTicker(ticker_symbol)
        
        # Get financial statements
        try:
            income_stmt = ticker.quarterly_income_statement()
            income_df = income_stmt.to_df() if hasattr(income_stmt, 'to_df') else None
        except:
            income_df = None
            
        try:
            balance_sheet = ticker.quarterly_balance_sheet()
            balance_df = balance_sheet.to_df() if hasattr(balance_sheet, 'to_df') else None
        except:
            balance_df = None
        
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
            'pegRatio': None,
            'raw_data': {}
        }
        
        # Try to get annual statements for YoY calculations
        try:
            annual_income = ticker.annual_income_statement()
            if hasattr(annual_income, 'to_df'):
                annual_df = annual_income.to_df()
                result['raw_data']['annual_income'] = True
                
                # Calculate EPS Growth (YoY)
                # Look for Basic EPS or Diluted EPS rows
                if annual_df is not None and len(annual_df.columns) >= 2:
                    # Get last 2 years of data
                    cols = list(annual_df.columns)
                    if len(cols) >= 2:
                        current_year = cols[0]  # Most recent
                        prev_year = cols[1]     # Previous year
                        
                        # Try to find EPS
                        for idx in annual_df.index:
                            if 'Diluted EPS' in str(idx) or 'Basic EPS' in str(idx):
                                try:
                                    current_eps = float(annual_df.loc[idx, current_year])
                                    prev_eps = float(annual_df.loc[idx, prev_year])
                                    if prev_eps != 0:
                                        result['epsGrowth'] = ((current_eps - prev_eps) / abs(prev_eps)) * 100
                                except:
                                    pass
                                break
                        
                        # Calculate Revenue Growth
                        for idx in annual_df.index:
                            if 'Total Revenue' in str(idx) or 'Operating Revenue' in str(idx):
                                try:
                                    current_rev = float(annual_df.loc[idx, current_year])
                                    prev_rev = float(annual_df.loc[idx, prev_year])
                                    if prev_rev != 0:
                                        result['revenueGrowth'] = ((current_rev - prev_rev) / abs(prev_rev)) * 100
                                except:
                                    pass
                                break
                        
                        # Calculate Profit Margin
                        for idx in annual_df.index:
                            if 'Net Income' in str(idx):
                                try:
                                    net_income = float(annual_df.loc[idx, current_year])
                                    # Find revenue
                                    for rev_idx in annual_df.index:
                                        if 'Total Revenue' in str(rev_idx):
                                            revenue = float(annual_df.loc[rev_idx, current_year])
                                            if revenue != 0:
                                                result['profitMargin'] = (net_income / revenue) * 100
                                            break
                                except:
                                    pass
                                break
        except Exception as e:
            print(f"Error getting annual income: {e}")
        
        # Try to get balance sheet for ROE, ROIC, Debt/Equity
        try:
            annual_balance = ticker.annual_balance_sheet()
            if hasattr(annual_balance, 'to_df'):
                balance_df = annual_balance.to_df()
                result['raw_data']['annual_balance'] = True
                
                if balance_df is not None and len(balance_df.columns) >= 1:
                    current_col = list(balance_df.columns)[0]
                    
                    total_equity = None
                    total_assets = None
                    total_debt = None
                    current_debt = None
                    long_term_debt = None
                    
                    for idx in balance_df.index:
                        idx_str = str(idx)
                        try:
                            if 'Total Stockholder Equity' in idx_str or 'Stockholders Equity' in idx_str:
                                total_equity = float(balance_df.loc[idx, current_col])
                            elif 'Total Assets' in idx_str and total_assets is None:
                                total_assets = float(balance_df.loc[idx, current_col])
                            elif 'Total Debt' in idx_str:
                                total_debt = float(balance_df.loc[idx, current_col])
                            elif 'Current Debt' in idx_str or 'Short Term Debt' in idx_str:
                                current_debt = float(balance_df.loc[idx, current_col])
                            elif 'Long Term Debt' in idx_str:
                                long_term_debt = float(balance_df.loc[idx, current_col])
                        except:
                            pass
                    
                    # Calculate Debt to Equity
                    if total_equity and total_equity != 0:
                        if total_debt:
                            result['debtToEquity'] = total_debt / total_equity
                        elif current_debt or long_term_debt:
                            total_debt = (current_debt or 0) + (long_term_debt or 0)
                            result['debtToEquity'] = total_debt / total_equity
                    
                    # Store for ROE/ROA calculation
                    result['raw_data']['total_equity'] = total_equity
                    result['raw_data']['total_assets'] = total_assets
                    
                    # Calculate ROE = Net Income / Shareholders Equity
                    if total_equity and total_equity != 0 and 'profitMargin' in result:
                        # We need net income - try to get from annual income
                        pass  # Will calculate below
                    
                    # Calculate ROA = Net Income / Total Assets
                    if total_assets and total_assets != 0:
                        pass  # Will calculate below
                        
        except Exception as e:
            print(f"Error getting balance sheet: {e}")
        
        # Calculate ROE and ROA using combined data
        try:
            annual_income = ticker.annual_income_statement()
            if hasattr(annual_income, 'to_df'):
                income_df = annual_income.to_df()
                if income_df is not None and len(income_df.columns) >= 1:
                    current_col = list(income_df.columns)[0]
                    net_income = None
                    
                    for idx in income_df.index:
                        if 'Net Income' in str(idx) and 'Non' not in str(idx):
                            try:
                                net_income = float(income_df.loc[idx, current_col])
                                break
                            except:
                                pass
                    
                    if net_income:
                        # ROE = Net Income / Total Equity
                        total_equity = result['raw_data'].get('total_equity')
                        if total_equity and total_equity != 0:
                            result['roe'] = (net_income / total_equity) * 100
                        
                        # ROA = Net Income / Total Assets
                        total_assets = result['raw_data'].get('total_assets')
                        if total_assets and total_assets != 0:
                            result['roa'] = (net_income / total_assets) * 100
                        
                        # ROIC = NOPAT / Invested Capital (simplified)
                        # ROIC ≈ (Net Income + Interest*(1-tax)) / (Equity + Debt)
                        # Simplified: Use Net Income / (Equity + Debt)
                        total_debt_calc = result.get('debtToEquity', 0) * (total_equity or 0) if total_equity else 0
                        invested_capital = (total_equity or 0) + total_debt_calc
                        if invested_capital != 0:
                            result['roic'] = (net_income / invested_capital) * 100
        except Exception as e:
            print(f"Error calculating ROE/ROA: {e}")
        
        # Clean up raw_data before returning
        result.pop('raw_data', None)
        
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
        try:
            financials = stock.quarterly_financials
            if financials is not None and len(financials.columns) >= 2:
                # Revenue growth
                if 'Total Revenue' in financials.index:
                    current_rev = financials.loc['Total Revenue'].iloc[0]
                    prev_rev = financials.loc['Total Revenue'].iloc[1]
                    rev_growth = calculate_growth_rate(current_rev, prev_rev)
                else:
                    rev_growth = None
                    
                # Net income for calculations
                if 'Net Income' in financials.index:
                    net_income = financials.loc['Net Income'].iloc[0]
                else:
                    net_income = None
            else:
                rev_growth = None
                net_income = None
        except:
            rev_growth = None
            net_income = None
        
        # Get balance sheet for ROE calculation
        try:
            balance = stock.quarterly_balance_sheet
            if balance is not None and len(balance.columns) >= 1:
                if 'Stockholders Equity' in balance.index:
                    equity = balance.loc['Stockholders Equity'].iloc[0]
                elif 'Total Stockholder Equity' in balance.index:
                    equity = balance.loc['Total Stockholder Equity'].iloc[0]
                else:
                    equity = None
                    
                if 'Total Assets' in balance.index:
                    total_assets = balance.loc['Total Assets'].iloc[0]
                else:
                    total_assets = None
                    
                if 'Total Debt' in balance.index:
                    total_debt = balance.loc['Total Debt'].iloc[0]
                else:
                    total_debt = None
            else:
                equity = None
                total_assets = None
                total_debt = None
        except:
            equity = None
            total_assets = None
            total_debt = None
        
        # Calculate ROE
        roe = None
        if net_income and equity and equity != 0:
            roe = (net_income / equity) * 100
        
        # Calculate ROA  
        roa = None
        if net_income and total_assets and total_assets != 0:
            roa = (net_income / total_assets) * 100
        
        # Calculate Debt/Equity
        debt_to_equity = None
        if total_debt and equity and equity != 0:
            debt_to_equity = total_debt / equity
        
        return {
            'source': 'yfinance',
            'pe': safe_get(info, 'trailingPE'),
            'forwardPe': safe_get(info, 'forwardPE'),
            'pegRatio': safe_get(info, 'pegRatio'),
            'marketCap': safe_get(info, 'marketCap'),
            'roe': roe or safe_get(info, 'returnOnEquity'),
            'roa': roa or safe_get(info, 'returnOnAssets'),
            'roic': None,  # Not available in yfinance
            'epsGrowth': safe_get(info, 'earningsGrowth'),  # Usually None
            'revenueGrowth': rev_growth or safe_get(info, 'revenueGrowth'),
            'debtToEquity': debt_to_equity or safe_get(info, 'debtToEquity'),
            'profitMargin': safe_get(info, 'profitMargins'),
            'operatingMargin': safe_get(info, 'operatingMargins'),
            'beta': safe_get(info, 'beta'),
            'dividendYield': safe_get(info, 'dividendYield'),
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
        'version': '2.0',
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
                'open': round(row['Open'], 2),
                'high': round(row['High'], 2),
                'low': round(row['Low'], 2),
                'close': round(row['Close'], 2),
                'volume': int(row['Volume'])
            })
        
        # Get 52-week ago price (approximately 252 trading days)
        price_52w_ago = None
        if len(hist_data) >= 252:
            price_52w_ago = round(hist_data.iloc[-252]['Close'], 2)
        elif len(hist_data) > 200:
            price_52w_ago = round(hist_data.iloc[0]['Close'], 2)
        
        # Get 13-week ago price (approximately 63 trading days)
        price_13w_ago = None
        if len(hist_data) >= 63:
            price_13w_ago = round(hist_data.iloc[-63]['Close'], 2)
        
        # Current price
        current_price = round(hist_data.iloc[-1]['Close'], 2)
        
        # Basic fundamentals from yfinance (for backward compatibility)
        fundamentals = {
            'pe': safe_get(info, 'trailingPE'),
            'forwardPe': safe_get(info, 'forwardPE'),
            'marketCap': safe_get(info, 'marketCap'),
            'beta': safe_get(info, 'beta'),
            'dividendYield': safe_get(info, 'dividendYield'),
            'epsGrowth': 0,  # Placeholder - use /api/fundamentals for rich data
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
            'fiftyTwoWeekHigh': safe_get(info, 'fiftyTwoWeekHigh'),
            'fiftyTwoWeekLow': safe_get(info, 'fiftyTwoWeekLow'),
            'avgVolume': safe_get(info, 'averageVolume'),
            'avgVolume10d': safe_get(info, 'averageVolume10days'),
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
    
    Returns:
    - ROE, ROIC, ROA
    - EPS Growth, Revenue Growth
    - Debt/Equity, Profit Margins
    - PEG Ratio
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
        
        # Current price
        current_price = round(hist_data.iloc[-1]['Close'], 2)
        
        # 52-week ago price
        price_52w_ago = None
        if len(hist_data) >= 252:
            price_52w_ago = round(hist_data.iloc[-252]['Close'], 2)
        elif len(hist_data) > 200:
            price_52w_ago = round(hist_data.iloc[0]['Close'], 2)
        
        # 13-week ago price
        price_13w_ago = None
        if len(hist_data) >= 63:
            price_13w_ago = round(hist_data.iloc[-63]['Close'], 2)
        
        # Prepare price history
        price_history = []
        for date, row in hist_data.iterrows():
            price_history.append({
                'date': date.strftime('%Y-%m-%d'),
                'close': round(row['Close'], 2),
                'volume': int(row['Volume'])
            })
        
        # Calculate 200 SMA for market regime
        sma_200 = round(hist_data['Close'].tail(200).mean(), 2)
        
        response = {
            'ticker': 'SPY',
            'currentPrice': current_price,
            'price52wAgo': price_52w_ago,
            'price13wAgo': price_13w_ago,
            'sma200': sma_200,
            'aboveSma200': current_price > sma_200,
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
        
        current_vix = round(hist.iloc[-1]['Close'], 2)
        
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
            'isRisky': current_vix > 30
        })
        
    except Exception as e:
        print(f"Error fetching VIX: {e}")
        return jsonify({'error': str(e)}), 500


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Swing Trade Analyzer Backend v2.0")
    print("="*50)
    print(f"Defeat Beta: {'✅ Available' if DEFEATBETA_AVAILABLE else '❌ Not installed'}")
    print("Starting server on port 5001...")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5001)
