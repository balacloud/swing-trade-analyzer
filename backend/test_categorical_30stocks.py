#!/usr/bin/env python3
"""
Test Categorical Assessment System with 30 Diverse Stocks
Day 44 - v4.5 Implementation Validation

Tests the categorical assessment verdicts across different:
- Sectors (Tech, Healthcare, Finance, Consumer, Energy, etc.)
- Market caps (Large, Mid, Small)
- Conditions (Uptrending, Sideways, Downtrending)
"""

import requests
import json
from datetime import datetime
import numpy as np

API_BASE = "http://localhost:5001/api"

# 30 Diverse Test Stocks
TEST_STOCKS = [
    # Tech Giants
    "AAPL", "MSFT", "NVDA", "GOOGL", "META",
    # Tech Growth
    "PLTR", "SNOW", "NET", "CRWD", "DDOG",
    # Semiconductors
    "AMD", "MU", "AVGO", "QCOM", "INTC",
    # Healthcare
    "JNJ", "UNH", "LLY", "PFE", "ABBV",
    # Finance
    "JPM", "BAC", "GS", "V", "MA",
    # Consumer/Retail
    "AMZN", "COST", "WMT", "HD", "NKE"
]

def calculate_rsi(prices, period=14):
    """Calculate RSI from price list"""
    if len(prices) < period + 1:
        return 50  # Default if not enough data

    prices = np.array(prices)
    deltas = np.diff(prices)

    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 1)

def fetch_analysis(ticker):
    """Fetch full analysis data for a ticker"""
    try:
        # Fetch stock data
        stock_resp = requests.get(f"{API_BASE}/stock/{ticker}", timeout=30)
        if stock_resp.status_code != 200:
            return None, f"Stock API error: {stock_resp.status_code}"
        stock_data = stock_resp.json()

        # Calculate RSI from price history
        price_history = stock_data.get('priceHistory', [])
        if price_history:
            closes = [p['close'] for p in price_history]
            stock_data['rsi'] = calculate_rsi(closes)
        else:
            stock_data['rsi'] = 50

        # Fetch patterns (for trend template)
        patterns_resp = requests.get(f"{API_BASE}/patterns/{ticker}", timeout=30)
        patterns_data = patterns_resp.json() if patterns_resp.status_code == 200 else {}

        # Fetch S&R for trade viability
        sr_resp = requests.get(f"{API_BASE}/sr/{ticker}", timeout=30)
        sr_data = sr_resp.json() if sr_resp.status_code == 200 else {}

        return {
            'stock': stock_data,
            'patterns': patterns_data,
            'sr': sr_data
        }, None

    except Exception as e:
        return None, str(e)

def assess_technical(patterns_data, stock_data):
    """Simplified technical assessment matching frontend logic"""
    trend_template = patterns_data.get('trend_template', {})
    # API returns criteria_met, not criteria_passed
    pass_count = trend_template.get('criteria_met', trend_template.get('criteria_passed', 0))

    rsi = stock_data.get('rsi', 50)

    if pass_count >= 7 and 50 <= rsi <= 70:
        return 'Strong'
    elif pass_count >= 5 and 40 <= rsi <= 80:
        return 'Decent'
    return 'Weak'

def assess_viability(sr_data):
    """Get trade viability from S&R data"""
    meta = sr_data.get('meta', {})
    viability = meta.get('tradeViability', {})
    return viability.get('viable', 'Unknown')

def get_recommendation(verdict, viability):
    """Determine actionable recommendation"""
    if verdict == 'BUY':
        if viability == 'YES':
            return 'READY TO TRADE'
        elif viability == 'CAUTION':
            return 'ADD TO WATCHLIST'
        else:
            return 'WAIT FOR PULLBACK'
    elif verdict == 'HOLD':
        if viability == 'YES':
            return 'WATCHLIST - MONITOR'
        else:
            return 'NOT NOW - PATIENCE'
    else:
        return 'SKIP THIS ONE'

def main():
    print("=" * 80)
    print("Categorical Assessment System - 30 Stock Test")
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Fetch Fear & Greed for sentiment
    try:
        fg_resp = requests.get(f"{API_BASE}/fear-greed", timeout=10)
        fg_data = fg_resp.json() if fg_resp.status_code == 200 else {'value': 50, 'rating': 'Neutral'}
        print(f"\nFear & Greed Index: {fg_data.get('value')} ({fg_data.get('rating')})")
    except:
        fg_data = {'value': 50, 'rating': 'Neutral'}
        print("\nFear & Greed: Using default (50)")

    # Fetch SPY for regime
    try:
        spy_resp = requests.get(f"{API_BASE}/stock/SPY", timeout=30)
        spy_data = spy_resp.json() if spy_resp.status_code == 200 else {}
        spy_price = spy_data.get('currentPrice', 0)
        spy_200ema = spy_data.get('indicators', {}).get('ema200', 0)
        spy_regime = 'Bull' if spy_price > spy_200ema else 'Bear'
        print(f"SPY Regime: {spy_regime} (Price: ${spy_price:.2f}, 200 EMA: ${spy_200ema:.2f})")
    except:
        spy_regime = 'Unknown'
        print("SPY Regime: Unknown")

    # Fetch VIX
    try:
        vix_resp = requests.get(f"{API_BASE}/stock/%5EVIX", timeout=30)
        vix_data = vix_resp.json() if vix_resp.status_code == 200 else {}
        vix_value = vix_data.get('currentPrice', 20)
        print(f"VIX: {vix_value:.2f}")
    except:
        vix_value = 20
        print("VIX: Using default (20)")

    print("\n" + "-" * 80)
    print(f"{'Ticker':<8} {'Price':>10} {'Trend':>6} {'RSI':>6} {'Tech':>8} {'Viable':>8} {'Verdict':>8} {'Recommendation':<20}")
    print("-" * 80)

    results = {
        'BUY': [],
        'HOLD': [],
        'AVOID': []
    }

    recommendations = {
        'READY TO TRADE': [],
        'ADD TO WATCHLIST': [],
        'WAIT FOR PULLBACK': [],
        'WATCHLIST - MONITOR': [],
        'NOT NOW - PATIENCE': [],
        'SKIP THIS ONE': []
    }

    for ticker in TEST_STOCKS:
        data, error = fetch_analysis(ticker)

        if error:
            print(f"{ticker:<8} {'ERROR':>10} {'-':>6} {'-':>6} {'-':>8} {'-':>8} {'-':>8} {error[:20]}")
            continue

        stock = data['stock']
        patterns = data['patterns']
        sr = data['sr']

        price = stock.get('currentPrice', 0)
        trend_template = patterns.get('trend_template', {})
        # API returns criteria_met, not criteria_passed
        criteria_met = trend_template.get('criteria_met', trend_template.get('criteria_passed', 0))
        trend_score = f"{criteria_met}/8"
        rsi = stock.get('rsi', 50)  # RSI calculated from price history

        # Assess technical
        tech_assessment = assess_technical(patterns, stock)

        # Get viability
        viability = assess_viability(sr)

        # Determine verdict (simplified logic matching frontend)
        # Strong technical + favorable regime = potential BUY
        # Weak technical = AVOID
        # Otherwise = HOLD
        if tech_assessment == 'Weak':
            verdict = 'AVOID'
        elif tech_assessment == 'Strong' and vix_value < 25 and spy_regime == 'Bull':
            verdict = 'BUY'
        else:
            verdict = 'HOLD'

        # Get recommendation
        recommendation = get_recommendation(verdict, viability)

        # Track results
        results[verdict].append(ticker)
        recommendations[recommendation].append(ticker)

        print(f"{ticker:<8} ${price:>9.2f} {trend_score:>6} {rsi:>6.1f} {tech_assessment:>8} {viability:>8} {verdict:>8} {recommendation:<20}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print(f"\nVerdict Distribution:")
    for verdict, tickers in results.items():
        print(f"  {verdict}: {len(tickers)} stocks - {', '.join(tickers) if tickers else 'None'}")

    print(f"\nRecommendation Distribution:")
    for rec, tickers in recommendations.items():
        if tickers:
            print(f"  {rec}: {len(tickers)} stocks - {', '.join(tickers)}")

    print("\n" + "=" * 80)
    print("Test Complete")
    print("=" * 80)

if __name__ == "__main__":
    main()
