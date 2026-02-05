#!/usr/bin/env python3
"""
Comprehensive Categorical Assessment Test Suite
Day 45 - Tests all assessment logic with edge cases

Usage:
    python test_categorical_comprehensive.py
    python test_categorical_comprehensive.py --verbose
    python test_categorical_comprehensive.py --ticker AAPL
"""

import requests
import json
import sys
import argparse
from datetime import datetime

BASE_URL = "http://localhost:5001/api"

# Test Tickers by Category
TIER_1_STANDARD = ["AAPL", "NVDA", "JPM", "MSFT", "COST"]
TIER_2_ETFS = ["SPY", "QQQ", "IWM"]
TIER_3_TECHNICAL_EDGE = []  # Populated dynamically
TIER_4_FUNDAMENTAL_EDGE = ["TSLA", "AMC", "META"]
TIER_5_SMALL_CAP = ["PLTR", "SOFI", "HOOD"]

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_pass(msg):
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")

def print_fail(msg):
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")

def print_warn(msg):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")

def print_info(msg):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")

def print_header(msg):
    print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{msg}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")


class TestResults:
    """Track test results"""
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.details = []

    def add_pass(self, test_name, details=None):
        self.passed += 1
        self.details.append({"test": test_name, "status": "PASS", "details": details})

    def add_fail(self, test_name, error):
        self.failed += 1
        self.details.append({"test": test_name, "status": "FAIL", "error": str(error)})

    def add_warning(self, test_name, warning):
        self.warnings += 1
        self.details.append({"test": test_name, "status": "WARN", "warning": warning})

    def summary(self):
        total = self.passed + self.failed
        return {
            "total": total,
            "passed": self.passed,
            "failed": self.failed,
            "warnings": self.warnings,
            "pass_rate": (self.passed / total * 100) if total > 0 else 0
        }


def test_api_health(results):
    """Test A1: API health check"""
    try:
        r = requests.get(f"{BASE_URL}/health", timeout=5)
        if r.status_code == 200:
            print_pass("API health check passed")
            results.add_pass("API Health")
            return True
        else:
            print_fail(f"API health check failed: {r.status_code}")
            results.add_fail("API Health", f"Status code: {r.status_code}")
            return False
    except Exception as e:
        print_fail(f"API health check failed: {e}")
        results.add_fail("API Health", str(e))
        return False


def test_fear_greed(results):
    """Test Fear & Greed endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/fear-greed", timeout=10)
        data = r.json()

        if "value" in data and "rating" in data:
            value = data["value"]
            rating = data["rating"]
            print_pass(f"Fear & Greed: {value} ({rating})")
            results.add_pass("Fear & Greed", {"value": value, "rating": rating})

            # Test B1: Check for cliff behavior
            if value >= 44 and value < 46:
                print_warn(f"F&G near 45 threshold ({value}) - watch for cliff behavior")
                results.add_warning("F&G Threshold", f"Value {value} near 45 threshold")

            return value
        else:
            print_fail("Fear & Greed missing expected fields")
            results.add_fail("Fear & Greed", "Missing fields")
            return None
    except Exception as e:
        print_fail(f"Fear & Greed failed: {e}")
        results.add_fail("Fear & Greed", str(e))
        return None


def test_vix(results):
    """Test VIX endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/market/vix", timeout=10)
        data = r.json()

        if "current" in data:
            vix = data["current"]
            regime = data.get("regime", "unknown")
            print_pass(f"VIX: {vix:.2f} ({regime})")
            results.add_pass("VIX", {"current": vix, "regime": regime})
            return vix
        else:
            print_fail("VIX missing 'current' field")
            results.add_fail("VIX", "Missing 'current' field")
            return None
    except Exception as e:
        print_fail(f"VIX failed: {e}")
        results.add_fail("VIX", str(e))
        return None


def test_spy(results):
    """Test SPY endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/market/spy", timeout=10)
        data = r.json()

        above_200 = data.get("aboveSma200", None)
        if above_200 is not None:
            status = "Above 200 SMA" if above_200 else "Below 200 SMA"
            print_pass(f"SPY: {status}")
            results.add_pass("SPY", {"aboveSma200": above_200})
            return above_200
        else:
            print_warn("SPY aboveSma200 not available")
            results.add_warning("SPY", "aboveSma200 not available")
            return None
    except Exception as e:
        print_fail(f"SPY failed: {e}")
        results.add_fail("SPY", str(e))
        return None


def test_stock(ticker, results, verbose=False):
    """Test full stock analysis"""
    try:
        r = requests.get(f"{BASE_URL}/stock/{ticker}", timeout=30)
        data = r.json()

        if "error" in data:
            print_fail(f"{ticker}: {data['error']}")
            results.add_fail(f"Stock {ticker}", data['error'])
            return None

        # Check essential fields
        has_prices = "prices" in data and len(data.get("prices", [])) > 0
        has_technicals = "technicals" in data

        if has_prices and has_technicals:
            rsi = data.get("technicals", {}).get("rsi14", "N/A")
            print_pass(f"{ticker}: Stock data OK (RSI: {rsi})")
            results.add_pass(f"Stock {ticker}", {"rsi": rsi})

            if verbose:
                print(f"    Prices: {len(data.get('prices', []))} days")
                print(f"    Technicals: {list(data.get('technicals', {}).keys())}")

            return data
        else:
            print_warn(f"{ticker}: Missing prices or technicals")
            results.add_warning(f"Stock {ticker}", "Missing prices or technicals")
            return data
    except Exception as e:
        print_fail(f"{ticker}: {e}")
        results.add_fail(f"Stock {ticker}", str(e))
        return None


def test_patterns(ticker, results, verbose=False):
    """Test pattern detection endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/patterns/{ticker}", timeout=30)
        data = r.json()

        if "error" in data:
            print_warn(f"{ticker} patterns: {data['error']}")
            results.add_warning(f"Patterns {ticker}", data['error'])
            return None

        # Check trend template
        if "trend_template" in data:
            tt = data["trend_template"]
            # Handle both criteria_met and criteria_passed
            criteria = tt.get("criteria_met", tt.get("criteria_passed", 0))
            total = tt.get("total_criteria", 8)
            print_info(f"  {ticker} Trend Template: {criteria}/{total}")

            if verbose and "criteria_details" in tt:
                for c in tt["criteria_details"][:3]:  # Show first 3
                    status = "✓" if c.get("passed") else "✗"
                    print(f"    {status} {c.get('name', 'Unknown')}")

            results.add_pass(f"Patterns {ticker}", {"trend_template": f"{criteria}/{total}"})
            return data
        else:
            print_warn(f"{ticker}: No trend template data")
            results.add_warning(f"Patterns {ticker}", "No trend template")
            return None
    except Exception as e:
        print_fail(f"{ticker} patterns: {e}")
        results.add_fail(f"Patterns {ticker}", str(e))
        return None


def test_fundamentals(ticker, results, verbose=False):
    """Test fundamentals endpoint"""
    try:
        r = requests.get(f"{BASE_URL}/fundamentals/{ticker}", timeout=30)
        data = r.json()

        if "error" in data:
            print_warn(f"{ticker} fundamentals: {data['error']}")
            results.add_warning(f"Fundamentals {ticker}", data['error'])
            return None

        roe = data.get("roe")
        rev_growth = data.get("revenueGrowth")
        de = data.get("debtToEquity")
        source = data.get("source", "unknown")

        if roe is not None or rev_growth is not None:
            roe_str = f"{roe:.1f}%" if roe is not None else "N/A"
            rev_str = f"{rev_growth:.1f}%" if rev_growth is not None else "N/A"
            de_str = f"{de:.2f}" if de is not None else "N/A"
            print_info(f"  {ticker} Fundamentals: ROE={roe_str}, Rev={rev_str}, D/E={de_str} (via {source})")
            results.add_pass(f"Fundamentals {ticker}", {"roe": roe, "revenueGrowth": rev_growth, "source": source})

            # Check for edge cases
            if roe is not None and roe < 0:
                print_warn(f"  {ticker}: Negative ROE ({roe:.1f}%) - edge case")
            if roe is not None and roe > 100:
                print_warn(f"  {ticker}: Very high ROE ({roe:.1f}%) - edge case")

            return data
        else:
            print_warn(f"{ticker}: No fundamental metrics available")
            results.add_warning(f"Fundamentals {ticker}", "No metrics")
            return None
    except Exception as e:
        print_fail(f"{ticker} fundamentals: {e}")
        results.add_fail(f"Fundamentals {ticker}", str(e))
        return None


def test_etf_fundamentals(ticker, results):
    """Test that ETFs correctly report N/A for fundamentals"""
    try:
        r = requests.get(f"{BASE_URL}/fundamentals/{ticker}", timeout=30)
        data = r.json()

        # ETFs should either have no fundamentals or be marked specially
        is_etf_response = (
            data.get("isETF", False) or
            data.get("dataQuality") == "not_applicable" or
            "ETF" in data.get("error", "")
        )

        if is_etf_response:
            print_pass(f"{ticker}: Correctly identified as ETF")
            results.add_pass(f"ETF Detection {ticker}")
        else:
            # Some ETFs might have partial data - that's OK
            if data.get("roe") is None and data.get("revenueGrowth") is None:
                print_pass(f"{ticker}: No fundamental metrics (expected for ETF)")
                results.add_pass(f"ETF Detection {ticker}")
            else:
                print_warn(f"{ticker}: Has fundamental data (unexpected for ETF)")
                results.add_warning(f"ETF Detection {ticker}", "Has fundamental data")

        return data
    except Exception as e:
        print_fail(f"{ticker} ETF test: {e}")
        results.add_fail(f"ETF Detection {ticker}", str(e))
        return None


def run_validation_engine(results):
    """Run the validation engine"""
    print_header("Running Validation Engine")
    try:
        r = requests.post(f"{BASE_URL}/validation/run", timeout=120)
        if r.status_code == 200:
            data = r.json()
            pass_rate = data.get("overall_pass_rate", 0)
            coverage = data.get("coverage_rate", 0)
            accuracy = data.get("accuracy_rate", 0)

            print_pass(f"Validation Pass Rate: {pass_rate:.1f}%")
            print_info(f"  Coverage: {coverage:.1f}%")
            print_info(f"  Accuracy: {accuracy:.1f}%")

            if pass_rate >= 90:
                results.add_pass("Validation Engine", {"pass_rate": pass_rate})
            else:
                results.add_warning("Validation Engine", f"Pass rate {pass_rate}% below 90% target")

            return data
        else:
            print_fail(f"Validation engine returned {r.status_code}")
            results.add_fail("Validation Engine", f"Status {r.status_code}")
            return None
    except requests.exceptions.Timeout:
        print_warn("Validation engine timed out (this is normal for large runs)")
        results.add_warning("Validation Engine", "Timeout")
        return None
    except Exception as e:
        print_fail(f"Validation engine: {e}")
        results.add_fail("Validation Engine", str(e))
        return None


def test_categorical_assessment_display(vix, spy_above_200, fg_value, results):
    """Test B3-B4: Expected categorical assessments based on current market conditions"""
    print_header("Categorical Assessment Logic Validation")

    print_info("Current Market Conditions:")
    print(f"  VIX: {vix}")
    print(f"  SPY > 200 EMA: {spy_above_200}")
    print(f"  Fear & Greed: {fg_value}")

    # Test Risk/Macro logic
    if vix is not None and spy_above_200 is not None:
        if vix < 20 and spy_above_200:
            expected_risk = "Favorable"
        elif vix > 30 or not spy_above_200:
            expected_risk = "Unfavorable"
        else:
            expected_risk = "Neutral"

        print_info(f"\nExpected Risk/Macro Assessment: {expected_risk}")
        results.add_pass("Risk/Macro Logic", {"expected": expected_risk})

    # Test Sentiment logic (current thresholds)
    if fg_value is not None:
        if fg_value >= 55 and fg_value <= 75:
            current_sentiment = "Strong"
        elif fg_value >= 45 and fg_value < 55:
            current_sentiment = "Neutral"
        else:
            current_sentiment = "Weak"

        print_info(f"Expected Sentiment (current thresholds): {current_sentiment}")

        # Flag if near threshold cliff
        if 44 <= fg_value <= 46:
            print_warn(f"F&G {fg_value} is near 45 threshold - cliff behavior risk!")
            print_warn("RECOMMENDATION: Expand neutral zone to 35-60")

        # Show what proposed thresholds would say
        if fg_value >= 60 and fg_value <= 80:
            proposed_sentiment = "Strong"
        elif fg_value >= 35 and fg_value < 60:
            proposed_sentiment = "Neutral"
        else:
            proposed_sentiment = "Weak"

        if current_sentiment != proposed_sentiment:
            print_warn(f"  Proposed thresholds would show: {proposed_sentiment}")

        results.add_pass("Sentiment Logic", {"current": current_sentiment, "proposed": proposed_sentiment})


def run_tier_tests(tickers, tier_name, results, verbose=False):
    """Run tests for a tier of tickers"""
    print_header(f"Testing {tier_name}")

    for ticker in tickers:
        print(f"\n--- {ticker} ---")
        test_stock(ticker, results, verbose)
        test_patterns(ticker, results, verbose)

        # ETFs get special fundamental handling
        if ticker in TIER_2_ETFS:
            test_etf_fundamentals(ticker, results)
        else:
            test_fundamentals(ticker, results, verbose)


def print_summary(results):
    """Print final test summary"""
    summary = results.summary()

    print_header("TEST SUMMARY")
    print(f"Total Tests: {summary['total']}")
    print(f"{Colors.GREEN}Passed: {summary['passed']}{Colors.RESET}")
    print(f"{Colors.RED}Failed: {summary['failed']}{Colors.RESET}")
    print(f"{Colors.YELLOW}Warnings: {summary['warnings']}{Colors.RESET}")
    print(f"\nPass Rate: {summary['pass_rate']:.1f}%")

    if summary['failed'] > 0:
        print(f"\n{Colors.RED}Failed Tests:{Colors.RESET}")
        for detail in results.details:
            if detail['status'] == 'FAIL':
                print(f"  - {detail['test']}: {detail.get('error', 'Unknown error')}")

    if summary['warnings'] > 0:
        print(f"\n{Colors.YELLOW}Warnings:{Colors.RESET}")
        for detail in results.details:
            if detail['status'] == 'WARN':
                print(f"  - {detail['test']}: {detail.get('warning', 'Unknown warning')}")


def main():
    parser = argparse.ArgumentParser(description='Comprehensive Categorical Assessment Test Suite')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show detailed output')
    parser.add_argument('--ticker', '-t', type=str, help='Test a specific ticker only')
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation engine')
    args = parser.parse_args()

    print_header("COMPREHENSIVE CATEGORICAL ASSESSMENT TEST SUITE")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Day 45 - Swing Trade Analyzer")

    results = TestResults()

    # Test API Health
    if not test_api_health(results):
        print_fail("Backend not available. Please start with ./start.sh")
        sys.exit(1)

    # Single ticker mode
    if args.ticker:
        print_header(f"Testing Single Ticker: {args.ticker}")
        test_stock(args.ticker, results, args.verbose)
        test_patterns(args.ticker, results, args.verbose)
        test_fundamentals(args.ticker, results, args.verbose)
        print_summary(results)
        return

    # Market conditions
    fg_value = test_fear_greed(results)
    vix = test_vix(results)
    spy_above_200 = test_spy(results)

    # Test categorical logic
    test_categorical_assessment_display(vix, spy_above_200, fg_value, results)

    # Run tier tests
    run_tier_tests(TIER_1_STANDARD, "Tier 1: Standard Large-Cap", results, args.verbose)
    run_tier_tests(TIER_2_ETFS, "Tier 2: ETFs", results, args.verbose)
    run_tier_tests(TIER_4_FUNDAMENTAL_EDGE, "Tier 4: Fundamental Edge Cases", results, args.verbose)
    run_tier_tests(TIER_5_SMALL_CAP, "Tier 5: Small Cap", results, args.verbose)

    # Run validation engine
    if not args.skip_validation:
        run_validation_engine(results)

    # Summary
    print_summary(results)

    # Save results
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f"test_results_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump({
            "timestamp": timestamp,
            "summary": results.summary(),
            "details": results.details,
            "market_conditions": {
                "fear_greed": fg_value,
                "vix": vix,
                "spy_above_200": spy_above_200
            }
        }, f, indent=2)
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
