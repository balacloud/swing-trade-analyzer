"""
Swing Trade Analyzer - Backend API v1.0
Day 1: Real data integration via yfinance (Yahoo Finance wrapper)
Note: This will be replaced with Defeat Beta API in future iterations
"""

from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

app = Flask(__name__)
CORS(app)

def fetch_stock_data(ticker, period="1y"):
    """
    Fetch stock data using yfinance library
    
    Args:
        ticker: Stock symbol (e.g., AAPL)
        period: Time period (1y, 2y, etc.)
        
    Returns:
        yfinance Ticker object or None
    """
    try:
        stock = yf.Ticker(ticker)
        
        # Test if ticker is valid by trying to fetch info
        info = stock.info
        if not info or 'symbol' not in info:
            print(f"❌ Invalid ticker: {ticker}")
            return None
            
        print(f"✅ Successfully connected to {ticker}")
        return stock
        
    except Exception as e:
        print(f"❌ Error fetching {ticker}: {str(e)}")
        return None

def get_price_history(stock, period="1y"):
    """
    Get historical price data
    
    Args:
        stock: yfinance Ticker object
        period: Time period
        
    Returns:
        pandas DataFrame with price history
    """
    try:
        hist = stock.history(period=period)
        
        if hist.empty:
            print(f"❌ No price history available")
            return None
        
        print(f"✅ Fetched {len(hist)} days of price data")
        return hist
        
    except Exception as e:
        print(f"❌ Error getting price history: {str(e)}")
        return None

def get_fundamentals(stock):
    """
    Extract fundamental data from stock info
    
    Args:
        stock: yfinance Ticker object
        
    Returns:
        Dictionary of fundamental data
    """
    try:
        info = stock.info
        
        fundamentals = {
            'marketCap': info.get('marketCap', 0),
            'trailingPE': info.get('trailingPE', 0),
            'forwardPE': info.get('forwardPE', 0),
            'epsTrailing': info.get('trailingEps', 0),
            'epsForward': info.get('forwardEps', 0),
            'bookValue': info.get('bookValue', 0),
            'priceToBook': info.get('priceToBook', 0),
            'dividendYield': (info.get('dividendYield', 0) * 100) if info.get('dividendYield') else 0,
            'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 0),
            'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 0),
            'averageVolume': info.get('averageVolume', 0),
            'beta': info.get('beta', 0),
            'profitMargins': (info.get('profitMargins', 0) * 100) if info.get('profitMargins') else 0,
            'revenueGrowth': (info.get('revenueGrowth', 0) * 100) if info.get('revenueGrowth') else 0,
            # Placeholders for Defeat Beta integration later
            'epsGrowth': 0,
            'roe': 0,
            'roic': 0,
            'debtToEquity': 0
        }
        
        print(f"✅ Extracted fundamentals")
        return fundamentals
        
    except Exception as e:
        print(f"⚠️  Error extracting fundamentals: {str(e)}")
        return {}

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Swing Trade Analyzer API v1.0",
        "timestamp": datetime.now().isoformat(),
        "data_source": "yfinance (Yahoo Finance)",
        "note": "Will be upgraded to Defeat Beta API",
        "version": "1.0.0"
    })

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock(ticker):
    """
    Fetch complete stock data for analysis
    
    Args:
        ticker: Stock symbol (e.g., AAPL, NVDA)
        
    Returns:
        JSON with price history, fundamentals, and metadata
    """
    try:
        ticker = ticker.upper().strip()
        
        # Validate ticker format
        if not ticker or len(ticker) > 10:
            return jsonify({
                "error": "Invalid ticker format",
                "message": "Ticker must be 1-10 characters"
            }), 400
        
        print(f"\n{'='*60}")
        print(f"📊 Processing request for {ticker}")
        print(f"{'='*60}")
        
        # Fetch stock data
        stock = fetch_stock_data(ticker, period="1y")
        
        if stock is None:
            return jsonify({
                "error": f"Unable to fetch data for {ticker}",
                "message": "Ticker may be invalid or data temporarily unavailable",
                "ticker": ticker
            }), 404
        
        # Get price history
        hist = get_price_history(stock, period="1y")
        
        if hist is None or len(hist) < 50:
            return jsonify({
                "error": f"Insufficient data for {ticker}",
                "message": f"Need at least 50 days of data",
                "ticker": ticker
            }), 404
        
        # Get fundamentals
        fundamentals = get_fundamentals(stock)
        
        # Prepare data for response
        current_price = float(hist['Close'].iloc[-1])
        
        # FIXED: Get last 260 days (covers full 52 weeks of trading)
        # Previously was 200 which only covered ~40 weeks
        hist_data = hist.tail(260)
        
        response = {
            "ticker": ticker,
            "currentPrice": round(current_price, 2),
            "priceHistory": [round(float(x), 2) for x in hist_data['Close'].tolist()],
            "highs": [round(float(x), 2) for x in hist_data['High'].tolist()],
            "lows": [round(float(x), 2) for x in hist_data['Low'].tolist()],
            "volumes": [int(x) for x in hist_data['Volume'].tolist()],
            "dates": hist_data.index.strftime('%Y-%m-%d').tolist(),
            "fundamentals": fundamentals,
            "avgVolume": int(hist_data['Volume'].mean()),
            "dataPoints": len(hist_data),
            "dataSource": "yfinance",
            "lastUpdated": datetime.now().isoformat()
        }
        
        print(f"✅ Successfully prepared response for {ticker}")
        print(f"   Current Price: ${current_price:.2f}")
        print(f"   Data Points: {len(hist_data)}")
        print(f"   Market Cap: ${fundamentals.get('marketCap', 0):,.0f}")
        
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error processing {ticker}: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": str(e),
            "ticker": ticker
        }), 500

@app.route('/api/market/spy', methods=['GET'])
def get_spy_data():
    """
    Fetch S&P 500 (SPY) data for Relative Strength calculation
    
    Returns:
        JSON with current price, 52-week ago price, and 13-week ago price
    """
    try:
        print(f"\n{'='*60}")
        print(f"📊 Fetching SPY data for RS calculation")
        print(f"{'='*60}")
        
        # Fetch SPY data
        spy = fetch_stock_data('SPY', period="2y")
        
        if spy is None:
            return jsonify({
                "error": "Unable to fetch SPY data",
                "message": "S&P 500 data temporarily unavailable"
            }), 503
        
        # Get price history
        hist = get_price_history(spy, period="2y")
        
        if hist is None or len(hist) < 260:
            return jsonify({
                "error": "Insufficient SPY data",
                "message": f"Need at least 260 days, got {len(hist) if hist is not None else 0}"
            }), 503
        
        # Extract prices
        current_price = float(hist['Close'].iloc[-1])
        
        # 52 weeks ago (approximately 252 trading days)
        try:
            price_52w_ago = float(hist['Close'].iloc[-252])
        except:
            price_52w_ago = float(hist['Close'].iloc[0])
        
        # 13 weeks ago (approximately 65 trading days)
        try:
            price_13w_ago = float(hist['Close'].iloc[-65])
        except:
            price_13w_ago = current_price
        
        response = {
            "ticker": "SPY",
            "currentPrice": round(current_price, 2),
            "price52wAgo": round(price_52w_ago, 2),
            "price13wAgo": round(price_13w_ago, 2),
            "dataPoints": len(hist),
            "lastUpdated": datetime.now().isoformat()
        }
        
        print(f"✅ SPY data fetched successfully")
        print(f"   Current: ${current_price:.2f}")
        print(f"   52w ago: ${price_52w_ago:.2f}")
        print(f"   13w ago: ${price_13w_ago:.2f}")
        
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error fetching SPY: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Endpoint not found",
        "message": "The requested endpoint does not exist"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 SWING TRADE ANALYZER API v1.0")
    print("="*60)
    print("Server: http://localhost:5001")
    print("\n📡 Available endpoints:")
    print("  GET  /api/health          - Health check")
    print("  GET  /api/stock/<ticker>  - Get stock data")
    print("  GET  /api/market/spy      - Get S&P 500 data")
    print("\n💡 Current data source: yfinance (Yahoo Finance)")
    print("📝 Next: Will integrate Defeat Beta API for enhanced data")
    print("\n⌨️  Press Ctrl+C to stop")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)

    