#!/usr/bin/env python3
"""
yfinance Reliability Diagnostic - Day 34
Phase 0 Validation: Test actual yfinance failure rate before architectural decisions

Tests:
1. Batch download reliability (50 stocks)
2. Individual fetch reliability
3. Error pattern analysis
4. Rate limit detection
"""

import sys
import time
import yfinance as yf
from datetime import datetime
from collections import defaultdict

# Test universe: Mix of stock types
TEST_TICKERS = [
    # Mega-cap Tech (10)
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO", "ORCL", "CRM",
    # Financials (10)
    "JPM", "BAC", "WFC", "GS", "MS", "C", "BLK", "SCHW", "AXP", "USB",
    # Healthcare (10)
    "UNH", "JNJ", "PFE", "ABBV", "MRK", "LLY", "TMO", "ABT", "DHR", "BMY",
    # Consumer (10)
    "WMT", "PG", "KO", "PEP", "COST", "MCD", "NKE", "SBUX", "TGT", "HD",
    # TSX 60 Samples (5)
    "RY.TO", "TD.TO", "BNS.TO", "BMO.TO", "ENB.TO",
    # Small/Mid-cap (5)
    "SOFI", "PLTR", "RIVN", "LCID", "HOOD"
]

def test_batch_download():
    """Test yfinance batch download capability"""
    print("\n" + "="*60)
    print("TEST 1: Batch Download (50 tickers at once)")
    print("="*60)

    start = time.time()
    try:
        # Batch download - this is how we'd ideally fetch data
        data = yf.download(
            TEST_TICKERS,
            period="1mo",  # Just 1 month for speed
            progress=False,
            group_by='ticker',
            threads=True
        )
        elapsed = time.time() - start

        # Check which tickers succeeded
        success = []
        failed = []
        for ticker in TEST_TICKERS:
            try:
                if ticker in data.columns.get_level_values(0):
                    ticker_data = data[ticker]
                    if not ticker_data['Close'].dropna().empty:
                        success.append(ticker)
                    else:
                        failed.append((ticker, "Empty data"))
                else:
                    failed.append((ticker, "Not in response"))
            except Exception as e:
                failed.append((ticker, str(e)))

        print(f"\nResults:")
        print(f"  Success: {len(success)}/{len(TEST_TICKERS)} ({len(success)/len(TEST_TICKERS)*100:.1f}%)")
        print(f"  Failed: {len(failed)}")
        print(f"  Time: {elapsed:.2f}s")

        if failed:
            print(f"\n  Failed tickers:")
            for ticker, reason in failed[:10]:  # Show first 10
                print(f"    - {ticker}: {reason}")

        return {"success": len(success), "failed": len(failed), "time": elapsed, "failures": failed}

    except Exception as e:
        print(f"\n  BATCH DOWNLOAD FAILED: {e}")
        return {"success": 0, "failed": len(TEST_TICKERS), "error": str(e)}


def test_individual_downloads():
    """Test individual ticker fetches with delays"""
    print("\n" + "="*60)
    print("TEST 2: Individual Downloads (with 0.5s delay)")
    print("="*60)

    # Test subset for speed
    test_subset = TEST_TICKERS[:20]

    results = {"success": [], "failed": [], "errors": defaultdict(list)}
    start = time.time()

    for i, ticker in enumerate(test_subset):
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1mo")

            if hist.empty:
                results["failed"].append(ticker)
                results["errors"]["empty_data"].append(ticker)
            else:
                results["success"].append(ticker)

        except Exception as e:
            results["failed"].append(ticker)
            error_type = type(e).__name__
            results["errors"][error_type].append(ticker)

        # Progress indicator
        if (i + 1) % 5 == 0:
            print(f"  Progress: {i+1}/{len(test_subset)}")

        time.sleep(0.5)  # Rate limit protection

    elapsed = time.time() - start

    print(f"\nResults:")
    print(f"  Success: {len(results['success'])}/{len(test_subset)} ({len(results['success'])/len(test_subset)*100:.1f}%)")
    print(f"  Failed: {len(results['failed'])}")
    print(f"  Time: {elapsed:.2f}s")

    if results["errors"]:
        print(f"\n  Error breakdown:")
        for error_type, tickers in results["errors"].items():
            print(f"    - {error_type}: {len(tickers)} ({', '.join(tickers[:5])})")

    return results


def test_fundamentals():
    """Test fundamental data fetch (stock.info)"""
    print("\n" + "="*60)
    print("TEST 3: Fundamentals Fetch (stock.info)")
    print("="*60)

    # Required fields from our codebase
    REQUIRED_FIELDS = [
        'trailingPE', 'forwardPE', 'pegRatio', 'marketCap',
        'returnOnEquity', 'returnOnAssets', 'earningsGrowth',
        'revenueGrowth', 'debtToEquity', 'profitMargins',
        'operatingMargins', 'beta', 'dividendYield'
    ]

    test_subset = ["AAPL", "MSFT", "JPM", "RY.TO", "SOFI"]
    results = {}

    for ticker in test_subset:
        print(f"\n  Testing {ticker}...")
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Check which fields are available
            available = []
            missing = []
            for field in REQUIRED_FIELDS:
                if field in info and info[field] is not None:
                    available.append(field)
                else:
                    missing.append(field)

            results[ticker] = {
                "available": len(available),
                "missing": missing,
                "total": len(REQUIRED_FIELDS)
            }

            print(f"    Available: {len(available)}/{len(REQUIRED_FIELDS)}")
            if missing:
                print(f"    Missing: {', '.join(missing[:5])}")

            time.sleep(0.5)

        except Exception as e:
            results[ticker] = {"error": str(e)}
            print(f"    ERROR: {e}")

    return results


def test_tsx_support():
    """Test TSX ticker support specifically"""
    print("\n" + "="*60)
    print("TEST 4: TSX Ticker Support")
    print("="*60)

    tsx_tickers = ["RY.TO", "TD.TO", "BNS.TO", "BMO.TO", "ENB.TO"]
    results = {}

    for ticker in tsx_tickers:
        print(f"\n  Testing {ticker}...")
        try:
            stock = yf.Ticker(ticker)

            # Test OHLCV
            hist = stock.history(period="1mo")
            ohlcv_ok = not hist.empty

            # Test fundamentals
            info = stock.info
            fundamentals_ok = 'marketCap' in info and info['marketCap'] is not None

            results[ticker] = {
                "ohlcv": "OK" if ohlcv_ok else "FAILED",
                "fundamentals": "OK" if fundamentals_ok else "LIMITED",
                "rows": len(hist) if ohlcv_ok else 0
            }

            print(f"    OHLCV: {'OK' if ohlcv_ok else 'FAILED'} ({len(hist)} rows)")
            print(f"    Fundamentals: {'OK' if fundamentals_ok else 'LIMITED'}")

            time.sleep(0.5)

        except Exception as e:
            results[ticker] = {"error": str(e)}
            print(f"    ERROR: {e}")

    return results


def main():
    print("\n" + "="*60)
    print(" yfinance Reliability Diagnostic")
    print(f" Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(" Phase 0 Validation - Day 34")
    print("="*60)

    all_results = {}

    # Run all tests
    all_results["batch"] = test_batch_download()
    all_results["individual"] = test_individual_downloads()
    all_results["fundamentals"] = test_fundamentals()
    all_results["tsx"] = test_tsx_support()

    # Summary
    print("\n" + "="*60)
    print(" SUMMARY")
    print("="*60)

    batch = all_results["batch"]
    individual = all_results["individual"]

    batch_rate = batch.get("success", 0) / len(TEST_TICKERS) * 100 if "success" in batch else 0
    individual_rate = len(individual.get("success", [])) / 20 * 100

    print(f"""
  Batch Download Success Rate: {batch_rate:.1f}%
  Individual Download Success Rate: {individual_rate:.1f}%

  TSX Support: {'WORKING' if all([r.get('ohlcv') == 'OK' for r in all_results['tsx'].values() if 'ohlcv' in r]) else 'PARTIAL/FAILED'}

  ASSESSMENT:
  -----------
  """)

    if batch_rate >= 95 and individual_rate >= 95:
        print("  yfinance is WORKING WELL in current environment.")
        print("  Recommendation: Keep as primary, add fallbacks for edge cases.")
    elif batch_rate >= 80 or individual_rate >= 80:
        print("  yfinance is PARTIALLY RELIABLE.")
        print("  Recommendation: Keep as primary, implement robust fallback system.")
    else:
        print("  yfinance has SIGNIFICANT ISSUES.")
        print("  Recommendation: Consider alternative as primary source.")

    print("\n" + "="*60)

    return all_results


if __name__ == "__main__":
    results = main()
