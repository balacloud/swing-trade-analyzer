#!/usr/bin/env python3
"""
Comprehensive Backend API Test - Day 29
Tests all APIs with 30 diverse stocks to validate data quality.
"""

import requests
import json
from datetime import datetime
import time

BASE_URL = "http://localhost:5001"

# 30 diverse stocks across sectors
TEST_STOCKS = [
    # Tech
    "AAPL", "NVDA", "MSFT", "GOOGL", "META", "AMZN", "NFLX", "PLTR",
    # Financials
    "JPM", "BAC", "GS", "V", "MA",
    # Healthcare
    "JNJ", "UNH", "PFE", "ABBV",
    # Consumer
    "WMT", "COST", "HD", "NKE",
    # Energy
    "XOM", "CVX", "OXY",
    # Industrials
    "CAT", "BA", "GE",
    # ETFs (should handle specially)
    "SPY", "QQQ", "IWM"
]

def test_health():
    """Test health endpoint"""
    print("\n" + "="*60)
    print("HEALTH CHECK")
    print("="*60)
    try:
        r = requests.get(f"{BASE_URL}/api/health", timeout=10)
        data = r.json()
        print(f"Status: {data.get('status')}")
        print(f"Version: {data.get('version')}")
        print(f"Cache Size: {data.get('cache_size')}")
        print(f"DefeatBeta: {data.get('defeatbeta_available')}")
        print(f"S&R Engine: {data.get('sr_engine_available')}")
        return True
    except Exception as e:
        print(f"FAILED: {e}")
        return False

def test_stock_api(ticker):
    """Test /api/stock/<ticker>"""
    try:
        r = requests.get(f"{BASE_URL}/api/stock/{ticker}", timeout=30)
        if r.status_code != 200:
            return {"error": f"HTTP {r.status_code}"}
        data = r.json()
        return {
            "price": data.get("currentPrice"),
            "52w_high": data.get("fiftyTwoWeekHigh"),
            "52w_low": data.get("fiftyTwoWeekLow"),
            "name": data.get("name", "")[:30],
            "has_history": len(data.get("priceHistory", [])) > 0
        }
    except Exception as e:
        return {"error": str(e)}

def test_fundamentals_api(ticker):
    """Test /api/fundamentals/<ticker>"""
    try:
        r = requests.get(f"{BASE_URL}/api/fundamentals/{ticker}", timeout=30)
        if r.status_code != 200:
            return {"error": f"HTTP {r.status_code}"}
        data = r.json()
        return {
            "source": data.get("source"),
            "roe": data.get("roe"),
            "eps_growth": data.get("epsGrowth"),
            "revenue_growth": data.get("revenueGrowth"),
            "debt_equity": data.get("debtToEquity"),
            "pe": data.get("peRatio") or data.get("pe")
        }
    except Exception as e:
        return {"error": str(e)}

def test_sr_api(ticker):
    """Test /api/sr/<ticker>"""
    try:
        r = requests.get(f"{BASE_URL}/api/sr/{ticker}", timeout=30)
        if r.status_code != 200:
            return {"error": f"HTTP {r.status_code}"}
        data = r.json()
        return {
            "price": data.get("currentPrice"),
            "method": data.get("method"),
            "support_count": len(data.get("support", [])),
            "resistance_count": len(data.get("resistance", [])),
            "entry": data.get("suggestedEntry"),
            "stop": data.get("suggestedStop"),
            "target": data.get("suggestedTarget"),
            "rr": data.get("riskReward"),
            "viable": data.get("meta", {}).get("tradeViability", {}).get("viable")
        }
    except Exception as e:
        return {"error": str(e)}

def test_market_apis():
    """Test SPY and VIX market endpoints"""
    print("\n" + "="*60)
    print("MARKET DATA APIs")
    print("="*60)

    results = {}
    for endpoint in ["spy", "vix"]:
        try:
            r = requests.get(f"{BASE_URL}/api/market/{endpoint}", timeout=30)
            if r.status_code == 200:
                data = r.json()
                if endpoint == "spy":
                    results["spy"] = {
                        "price": data.get("currentPrice"),
                        "above_200sma": data.get("aboveSma200")
                    }
                else:
                    results["vix"] = {
                        "current": data.get("current"),
                        "level": data.get("level")
                    }
                print(f"{endpoint.upper()}: OK - {results[endpoint]}")
            else:
                results[endpoint] = {"error": f"HTTP {r.status_code}"}
                print(f"{endpoint.upper()}: FAILED - HTTP {r.status_code}")
        except Exception as e:
            results[endpoint] = {"error": str(e)}
            print(f"{endpoint.upper()}: FAILED - {e}")

    return results

def run_comprehensive_test():
    """Run all tests"""
    print("\n" + "="*60)
    print(f"COMPREHENSIVE BACKEND TEST - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

    # Test health
    if not test_health():
        print("Backend not healthy, aborting tests")
        return

    # Test market APIs
    test_market_apis()

    # Test all stocks
    print("\n" + "="*60)
    print(f"TESTING {len(TEST_STOCKS)} STOCKS")
    print("="*60)

    results = []

    for i, ticker in enumerate(TEST_STOCKS, 1):
        print(f"\n[{i}/{len(TEST_STOCKS)}] Testing {ticker}...")

        stock_result = test_stock_api(ticker)
        fund_result = test_fundamentals_api(ticker)
        sr_result = test_sr_api(ticker)

        result = {
            "ticker": ticker,
            "stock": stock_result,
            "fundamentals": fund_result,
            "sr": sr_result
        }
        results.append(result)

        # Print summary
        if "error" in stock_result:
            print(f"  Stock API: FAILED - {stock_result['error']}")
        else:
            print(f"  Stock API: OK - Price ${stock_result['price']}")

        if "error" in fund_result:
            print(f"  Fundamentals: FAILED - {fund_result['error']}")
        else:
            has_data = any([
                fund_result.get('roe'),
                fund_result.get('eps_growth'),
                fund_result.get('pe')
            ])
            print(f"  Fundamentals: {'OK' if has_data else 'MISSING'} - ROE={fund_result.get('roe')}, EPS={fund_result.get('eps_growth')}")

        if "error" in sr_result:
            print(f"  S&R API: FAILED - {sr_result['error']}")
        else:
            has_setup = sr_result.get('entry') and sr_result.get('stop')
            print(f"  S&R API: {'OK' if has_setup else 'PARTIAL'} - Entry=${sr_result.get('entry')}, R:R={sr_result.get('rr')}")

        # Small delay to avoid rate limiting
        time.sleep(0.5)

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    stock_ok = sum(1 for r in results if "error" not in r["stock"])
    fund_ok = sum(1 for r in results if "error" not in r["fundamentals"] and (r["fundamentals"].get("roe") or r["fundamentals"].get("pe")))
    sr_ok = sum(1 for r in results if "error" not in r["sr"] and r["sr"].get("entry"))

    print(f"Stock API: {stock_ok}/{len(results)} successful")
    print(f"Fundamentals API: {fund_ok}/{len(results)} with data")
    print(f"S&R API: {sr_ok}/{len(results)} with trade setup")

    # Identify problem tickers
    problem_tickers = []
    for r in results:
        issues = []
        if "error" in r["stock"]:
            issues.append("stock")
        if "error" in r["fundamentals"] or not (r["fundamentals"].get("roe") or r["fundamentals"].get("pe")):
            issues.append("fundamentals")
        if "error" in r["sr"] or not r["sr"].get("entry"):
            issues.append("sr")
        if issues:
            problem_tickers.append((r["ticker"], issues))

    if problem_tickers:
        print(f"\nProblem tickers ({len(problem_tickers)}):")
        for ticker, issues in problem_tickers:
            print(f"  {ticker}: {', '.join(issues)}")

    # Save results
    output_file = f"test_results_day29_{datetime.now().strftime('%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_stocks": len(results),
            "stock_ok": stock_ok,
            "fund_ok": fund_ok,
            "sr_ok": sr_ok,
            "results": results
        }, f, indent=2)
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    run_comprehensive_test()
