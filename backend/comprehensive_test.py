#!/usr/bin/env python3
"""
Comprehensive 30-Stock System Test
Day 25 - Testing backend data quality and system readiness

Tests:
1. Backend API health
2. Stock data availability
3. Fundamental data quality (Defeat Beta vs yfinance)
4. S&R levels and trade viability
5. Identifies problematic patterns
"""

import requests
import json
from datetime import datetime
from typing import Dict, List, Any
import time

BASE_URL = "http://localhost:5001"

# 30 Diverse stocks across sectors and market caps
TEST_STOCKS = [
    # Large Cap Tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "AVGO", "TSLA",
    # Large Cap Finance
    "JPM", "V", "MA", "BAC",
    # Large Cap Healthcare
    "UNH", "JNJ", "LLY", "PFE",
    # Large Cap Consumer
    "WMT", "COST", "HD", "MCD",
    # Large Cap Energy/Industrial
    "XOM", "CVX", "CAT", "BA",
    # Mid Cap / Growth
    "PLTR", "COIN", "SMCI", "AMD",
    # ETF (to test edge case)
    "SPY", "QQQ"
]

class TestResults:
    def __init__(self):
        self.results = []
        self.errors = []
        self.spy_data = None
        self.vix_data = None

    def add_result(self, ticker: str, data: Dict):
        self.results.append({"ticker": ticker, **data})

    def add_error(self, ticker: str, error: str):
        self.errors.append({"ticker": ticker, "error": error})

def safe_get(data: dict, *keys, default=None):
    """Safely navigate nested dictionaries"""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data if data is not None else default

def test_health():
    """Test backend health"""
    try:
        resp = requests.get(f"{BASE_URL}/api/health", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print(f"✅ Backend healthy - Version: {data.get('version', 'unknown')}")
            print(f"   Modules: DefeatBeta={data.get('defeatbeta_available')}, "
                  f"TradingView={data.get('tradingview_available')}, "
                  f"Validation={data.get('validation_available')}")
            return True
        else:
            print(f"❌ Backend unhealthy - Status: {resp.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def get_market_data():
    """Get SPY and VIX data once"""
    spy_data = None
    vix_data = None

    try:
        resp = requests.get(f"{BASE_URL}/api/market/spy", timeout=15)
        if resp.status_code == 200:
            spy_data = resp.json()
            print(f"✅ SPY data loaded - Price: ${spy_data.get('currentPrice', 'N/A')}")
    except Exception as e:
        print(f"⚠️ SPY data failed: {e}")

    try:
        resp = requests.get(f"{BASE_URL}/api/market/vix", timeout=15)
        if resp.status_code == 200:
            vix_data = resp.json()
            print(f"✅ VIX data loaded - Level: {vix_data.get('currentPrice', 'N/A')}")
    except Exception as e:
        print(f"⚠️ VIX data failed: {e}")

    return spy_data, vix_data

def test_stock(ticker: str) -> Dict:
    """Test a single stock across all endpoints"""
    result = {
        "stock_ok": False,
        "fundamentals_ok": False,
        "sr_ok": False,
        "data": {}
    }

    # Test /api/stock/{ticker}
    try:
        resp = requests.get(f"{BASE_URL}/api/stock/{ticker}", timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            result["stock_ok"] = True
            result["data"]["price"] = data.get("currentPrice")
            result["data"]["52w_high"] = data.get("fiftyTwoWeekHigh")
            result["data"]["52w_low"] = data.get("fiftyTwoWeekLow")
            result["data"]["price_history_days"] = len(data.get("priceHistory", []))
        else:
            result["data"]["stock_error"] = f"Status {resp.status_code}"
    except Exception as e:
        result["data"]["stock_error"] = str(e)

    # Test /api/fundamentals/{ticker}
    try:
        resp = requests.get(f"{BASE_URL}/api/fundamentals/{ticker}", timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            result["fundamentals_ok"] = True
            result["data"]["fund_source"] = data.get("source", "unknown")
            result["data"]["roe"] = data.get("roe")
            result["data"]["eps_growth"] = data.get("epsGrowth")
            result["data"]["revenue_growth"] = data.get("revenueGrowth")
            result["data"]["debt_equity"] = data.get("debtToEquity")
            result["data"]["roic"] = data.get("roic")
        else:
            result["data"]["fund_error"] = f"Status {resp.status_code}"
    except Exception as e:
        result["data"]["fund_error"] = str(e)

    # Test /api/sr/{ticker}
    try:
        resp = requests.get(f"{BASE_URL}/api/sr/{ticker}", timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            result["sr_ok"] = True
            result["data"]["sr_method"] = data.get("method")
            result["data"]["support_count"] = len(data.get("support", []))
            result["data"]["resistance_count"] = len(data.get("resistance", []))
            result["data"]["atr"] = safe_get(data, "meta", "atr")

            # Trade viability (Option D)
            viability = safe_get(data, "meta", "tradeViability", default={})
            result["data"]["viable"] = viability.get("viable", "UNKNOWN")
            result["data"]["support_distance_pct"] = viability.get("support_distance_pct")
            result["data"]["advice"] = viability.get("advice", "N/A")

            # Trade setup
            result["data"]["entry"] = data.get("suggestedEntry")
            result["data"]["stop"] = data.get("suggestedStop")
            result["data"]["target"] = data.get("suggestedTarget")
            result["data"]["risk_reward"] = data.get("riskReward")
        else:
            result["data"]["sr_error"] = f"Status {resp.status_code}"
    except Exception as e:
        result["data"]["sr_error"] = str(e)

    return result

def calculate_rs(stock_price, stock_52w_ago, spy_price, spy_52w_ago):
    """Calculate simple RS ratio"""
    if not all([stock_price, stock_52w_ago, spy_price, spy_52w_ago]):
        return None
    if stock_52w_ago == 0 or spy_52w_ago == 0:
        return None

    stock_return = (stock_price - stock_52w_ago) / stock_52w_ago
    spy_return = (spy_price - spy_52w_ago) / spy_52w_ago

    if spy_return == 0:
        return None
    return stock_return / spy_return

def generate_report(test_results: TestResults):
    """Generate comprehensive analysis report"""
    results = test_results.results
    errors = test_results.errors

    print("\n" + "="*80)
    print("📊 COMPREHENSIVE SYSTEM TEST REPORT")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Stocks Tested: {len(results)}")
    print(f"   Errors: {len(errors)}")
    print("="*80)

    # 1. API Success Rates
    print("\n📡 API SUCCESS RATES")
    print("-"*40)
    stock_ok = sum(1 for r in results if r.get("stock_ok"))
    fund_ok = sum(1 for r in results if r.get("fundamentals_ok"))
    sr_ok = sum(1 for r in results if r.get("sr_ok"))

    print(f"Stock Data:     {stock_ok}/{len(results)} ({100*stock_ok/len(results):.1f}%)")
    print(f"Fundamentals:   {fund_ok}/{len(results)} ({100*fund_ok/len(results):.1f}%)")
    print(f"S&R Data:       {sr_ok}/{len(results)} ({100*sr_ok/len(results):.1f}%)")

    # 2. Trade Viability Distribution
    print("\n📈 TRADE VIABILITY (Option D)")
    print("-"*40)
    viability_counts = {"YES": 0, "CAUTION": 0, "NO": 0, "UNKNOWN": 0}
    for r in results:
        v = r.get("data", {}).get("viable", "UNKNOWN")
        viability_counts[v] = viability_counts.get(v, 0) + 1

    for status, count in viability_counts.items():
        pct = 100 * count / len(results) if results else 0
        emoji = {"YES": "🟢", "CAUTION": "🟡", "NO": "🔴", "UNKNOWN": "⚪"}.get(status, "⚪")
        print(f"{emoji} {status:10} {count:3} ({pct:.1f}%)")

    # 3. Fundamental Data Quality
    print("\n💰 FUNDAMENTAL DATA QUALITY")
    print("-"*40)
    defeatbeta_count = sum(1 for r in results if r.get("data", {}).get("fund_source") == "defeatbeta")
    yfinance_count = sum(1 for r in results if r.get("data", {}).get("fund_source") == "yfinance")

    print(f"Defeat Beta source: {defeatbeta_count}/{len(results)}")
    print(f"yfinance fallback:  {yfinance_count}/{len(results)}")

    # Check for null fundamentals
    null_roe = sum(1 for r in results if r.get("data", {}).get("roe") is None)
    null_eps = sum(1 for r in results if r.get("data", {}).get("eps_growth") is None)
    null_rev = sum(1 for r in results if r.get("data", {}).get("revenue_growth") is None)

    print(f"\nNull values:")
    print(f"  ROE:            {null_roe}/{len(results)}")
    print(f"  EPS Growth:     {null_eps}/{len(results)}")
    print(f"  Revenue Growth: {null_rev}/{len(results)}")

    # 4. S&R Quality
    print("\n📊 SUPPORT & RESISTANCE QUALITY")
    print("-"*40)
    zero_support = sum(1 for r in results if r.get("data", {}).get("support_count", 0) == 0)
    zero_resistance = sum(1 for r in results if r.get("data", {}).get("resistance_count", 0) == 0)
    null_atr = sum(1 for r in results if r.get("data", {}).get("atr") is None)

    print(f"Zero support levels:    {zero_support}/{len(results)} ({100*zero_support/len(results):.1f}%)")
    print(f"Zero resistance levels: {zero_resistance}/{len(results)} ({100*zero_resistance/len(results):.1f}%)")
    print(f"Null ATR:               {null_atr}/{len(results)} ({100*null_atr/len(results):.1f}%)")

    # 5. Detailed Results Table
    print("\n📋 DETAILED RESULTS")
    print("-"*100)
    print(f"{'Ticker':<8} {'Price':>10} {'Viable':>8} {'Supp#':>6} {'Res#':>6} {'ATR':>8} {'ROE':>8} {'EPS%':>8} {'Source':>10}")
    print("-"*100)

    for r in sorted(results, key=lambda x: x.get("ticker", "")):
        ticker = r.get("ticker", "???")
        data = r.get("data", {})

        price = data.get("price")
        price_str = f"${price:.2f}" if price else "N/A"

        viable = data.get("viable", "???")
        supp = data.get("support_count", 0)
        res = data.get("resistance_count", 0)

        atr = data.get("atr")
        atr_str = f"{atr:.2f}" if atr else "N/A"

        roe = data.get("roe")
        roe_str = f"{roe:.1f}%" if roe else "N/A"

        eps = data.get("eps_growth")
        eps_str = f"{eps:.1f}%" if eps else "N/A"

        source = data.get("fund_source", "N/A")[:10]

        print(f"{ticker:<8} {price_str:>10} {viable:>8} {supp:>6} {res:>6} {atr_str:>8} {roe_str:>8} {eps_str:>8} {source:>10}")

    # 6. Problem Stocks
    print("\n⚠️ PROBLEM STOCKS")
    print("-"*40)

    problems = []
    for r in results:
        ticker = r.get("ticker")
        data = r.get("data", {})
        issues = []

        if not r.get("stock_ok"):
            issues.append("Stock API failed")
        if not r.get("fundamentals_ok"):
            issues.append("Fundamentals API failed")
        if not r.get("sr_ok"):
            issues.append("S&R API failed")
        if data.get("support_count", 0) == 0:
            issues.append("No support levels")
        if data.get("resistance_count", 0) == 0:
            issues.append("No resistance levels")
        if data.get("atr") is None:
            issues.append("ATR is null")
        if data.get("roe") is None and data.get("fund_source") != "N/A":
            issues.append("ROE is null")

        if issues:
            problems.append((ticker, issues))

    if problems:
        for ticker, issues in problems:
            print(f"  {ticker}: {', '.join(issues)}")
    else:
        print("  No problems found!")

    # 7. UX Confusion Analysis (AVOID + VIABLE)
    print("\n🎯 UX ANALYSIS (AVOID + VIABLE Confusion)")
    print("-"*40)
    print("Stocks where Trade Viability is YES but might score AVOID:")

    # We can't calculate exact score without frontend logic, but we can flag weak fundamentals
    weak_fund_viable = []
    for r in results:
        data = r.get("data", {})
        if data.get("viable") == "YES":
            roe = data.get("roe")
            eps = data.get("eps_growth")
            # If fundamentals are weak or null, likely to score low
            if roe is None or (roe is not None and roe < 10):
                weak_fund_viable.append(r.get("ticker"))
            elif eps is None or (eps is not None and eps < 10):
                weak_fund_viable.append(r.get("ticker"))

    if weak_fund_viable:
        print(f"  Potential confusion cases: {', '.join(weak_fund_viable)}")
        print("  (These may show AVOID verdict but VIABLE trade setup)")
    else:
        print("  No obvious confusion cases detected")

    # 8. Summary
    print("\n" + "="*80)
    print("📊 SUMMARY")
    print("="*80)

    all_ok = sum(1 for r in results if r.get("stock_ok") and r.get("fundamentals_ok") and r.get("sr_ok"))
    print(f"Fully functional:    {all_ok}/{len(results)} stocks")
    print(f"Trade viable (YES):  {viability_counts.get('YES', 0)}/{len(results)} stocks")
    print(f"API errors:          {len(errors)} stocks")

    # Quality score
    quality = (stock_ok + fund_ok + sr_ok) / (3 * len(results)) * 100 if results else 0
    print(f"\n🎯 Overall API Quality Score: {quality:.1f}%")

    if errors:
        print(f"\n❌ Failed stocks: {', '.join(e['ticker'] for e in errors)}")

    return {
        "total_tested": len(results),
        "api_quality": quality,
        "viability_distribution": viability_counts,
        "problems": len(problems),
        "errors": len(errors)
    }

def main():
    print("🚀 SWING TRADE ANALYZER - COMPREHENSIVE SYSTEM TEST")
    print(f"   Testing {len(TEST_STOCKS)} stocks")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

    # Check backend health
    if not test_health():
        print("\n❌ Backend not running! Start it with:")
        print("   cd backend && source venv/bin/activate && python backend.py")
        return

    # Get market data
    print("\n📊 Loading market data...")
    spy_data, vix_data = get_market_data()

    # Test each stock
    print(f"\n🔍 Testing {len(TEST_STOCKS)} stocks...\n")

    test_results = TestResults()
    test_results.spy_data = spy_data
    test_results.vix_data = vix_data

    for i, ticker in enumerate(TEST_STOCKS, 1):
        print(f"[{i:2}/{len(TEST_STOCKS)}] Testing {ticker}...", end=" ", flush=True)

        try:
            result = test_stock(ticker)
            test_results.add_result(ticker, result)

            # Status indicator
            status = "✅" if all([result["stock_ok"], result["fundamentals_ok"], result["sr_ok"]]) else "⚠️"
            viable = result.get("data", {}).get("viable", "?")
            print(f"{status} Viable: {viable}")

        except Exception as e:
            test_results.add_error(ticker, str(e))
            print(f"❌ Error: {e}")

        # Small delay to avoid rate limiting
        time.sleep(0.3)

    # Generate report
    summary = generate_report(test_results)

    # Save results to file
    output_file = f"test_results_day25_{datetime.now().strftime('%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": summary,
            "results": test_results.results,
            "errors": test_results.errors
        }, f, indent=2, default=str)

    print(f"\n💾 Results saved to: {output_file}")
    print("\n✅ Test complete!")

if __name__ == "__main__":
    main()
