#!/usr/bin/env python3
"""
Scan Market Test Script - Day 26
Tests all 4 scan strategies and analyzes results

Strategies:
1. reddit - Mid-cap+, high relative volume, momentum stocks
2. minervini - Large-cap momentum leaders in Stage 2 uptrend
3. momentum - Sustainable gains, RSI 50-75 (not overbought)
4. value - Quality stocks above 200 SMA at fair RSI levels
"""

import requests
import json
from datetime import datetime
import time

BASE_URL = "http://localhost:5001"

def test_scan_strategies():
    """Test the /api/scan/strategies endpoint"""
    print("=" * 70)
    print("TESTING: /api/scan/strategies")
    print("=" * 70)

    try:
        response = requests.get(f"{BASE_URL}/api/scan/strategies", timeout=30)

        if response.status_code == 200:
            data = response.json()
            strategies = data.get('strategies', [])
            print(f"✅ Found {len(strategies)} strategies:\n")

            for s in strategies:
                print(f"  [{s['id']}] {s['name']}")
                print(f"      {s['description']}")
                print()

            return [s['id'] for s in strategies]
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return []

    except Exception as e:
        print(f"❌ Exception: {e}")
        return []


def test_scan(strategy, limit=20):
    """Test a single scan strategy"""
    print("=" * 70)
    print(f"TESTING: /api/scan/tradingview?strategy={strategy}&limit={limit}")
    print("=" * 70)

    try:
        start_time = time.time()
        response = requests.get(
            f"{BASE_URL}/api/scan/tradingview",
            params={'strategy': strategy, 'limit': limit},
            timeout=60
        )
        elapsed = time.time() - start_time

        if response.status_code == 200:
            data = response.json()
            candidates = data.get('candidates', [])
            total_matches = data.get('totalMatches', 0)
            returned = data.get('returned', 0)

            print(f"✅ Scan completed in {elapsed:.1f}s")
            print(f"   Strategy: {data.get('strategy', strategy)}")
            print(f"   Total matches: {total_matches}")
            print(f"   Returned: {returned}")
            print()

            if candidates:
                print("   Top 10 Results:")
                print("   " + "-" * 60)
                print(f"   {'Ticker':<8} {'Name':<25} {'Price':>10} {'Change':>8} {'Volume':>12}")
                print("   " + "-" * 60)

                for stock in candidates[:10]:
                    name = stock.get('name', 'N/A')[:24]
                    price = stock.get('price', 0)  # Day 26: Fixed - API returns 'price' not 'close'
                    change = stock.get('change')
                    volume = stock.get('volume', 0)
                    vol_str = f"{volume/1e6:.1f}M" if volume else "N/A"
                    change_str = f"{change:>+7.1f}%" if change is not None else "    N/A"

                    print(f"   {stock.get('ticker', 'N/A'):<8} {name:<25} ${price:>9.2f} {change_str:>9} {vol_str:>10}")

                print()
            else:
                print("   ⚠️ No candidates returned")
                print()

            return {
                'strategy': strategy,
                'status': 'success',
                'total_matches': total_matches,
                'returned': returned,
                'candidates': candidates,
                'elapsed': elapsed
            }

        elif response.status_code == 503:
            print(f"❌ Service unavailable (503)")
            print(f"   TradingView library may not be available")
            return {
                'strategy': strategy,
                'status': 'unavailable',
                'error': 'Service unavailable'
            }
        else:
            print(f"❌ Error: {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Error: {error_data.get('error', 'Unknown')}")
            except:
                print(f"   Response: {response.text[:200]}")

            return {
                'strategy': strategy,
                'status': 'error',
                'error': response.text
            }

    except requests.exceptions.Timeout:
        print(f"❌ Timeout after 60s")
        return {'strategy': strategy, 'status': 'timeout'}

    except Exception as e:
        print(f"❌ Exception: {e}")
        return {'strategy': strategy, 'status': 'exception', 'error': str(e)}


def analyze_results(results):
    """Analyze scan results across all strategies"""
    print("\n" + "=" * 70)
    print("SCAN MARKET ANALYSIS SUMMARY")
    print("=" * 70)

    successful = [r for r in results if r.get('status') == 'success']
    failed = [r for r in results if r.get('status') != 'success']

    print(f"\n📊 Overall Results:")
    print(f"   Successful scans: {len(successful)}/{len(results)}")
    print(f"   Failed scans: {len(failed)}/{len(results)}")

    if failed:
        print(f"\n⚠️ Failed Strategies:")
        for r in failed:
            print(f"   - {r['strategy']}: {r.get('status')} - {r.get('error', 'Unknown')}")

    if successful:
        print(f"\n📈 Results by Strategy:")
        print(f"   {'Strategy':<12} {'Matches':>10} {'Returned':>10} {'Time':>8}")
        print("   " + "-" * 45)

        for r in successful:
            print(f"   {r['strategy']:<12} {r['total_matches']:>10} {r['returned']:>10} {r['elapsed']:>7.1f}s")

        # Find overlapping tickers
        all_tickers = {}
        for r in successful:
            for c in r.get('candidates', []):
                ticker = c.get('ticker')
                if ticker:
                    if ticker not in all_tickers:
                        all_tickers[ticker] = []
                    all_tickers[ticker].append(r['strategy'])

        # Tickers appearing in multiple strategies
        multi_strategy = {t: s for t, s in all_tickers.items() if len(s) > 1}

        if multi_strategy:
            print(f"\n🔥 Stocks appearing in multiple strategies:")
            for ticker, strategies in sorted(multi_strategy.items(), key=lambda x: -len(x[1])):
                print(f"   {ticker}: {', '.join(strategies)}")

        # Unique tickers per strategy
        print(f"\n📋 Unique stocks by strategy:")
        for r in successful:
            tickers = [c.get('ticker') for c in r.get('candidates', []) if c.get('ticker')]
            unique = [t for t in tickers if len(all_tickers.get(t, [])) == 1]
            print(f"   {r['strategy']}: {len(tickers)} total, {len(unique)} unique")

    return {
        'successful': len(successful),
        'failed': len(failed),
        'results': results
    }


def main():
    print("\n")
    print("🔍 SWING TRADE ANALYZER - SCAN MARKET TEST")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    # Check backend health first
    try:
        health = requests.get(f"{BASE_URL}/api/health", timeout=5).json()
        print(f"✅ Backend healthy - Version: {health.get('version', 'unknown')}")

        if not health.get('tradingviewAvailable'):
            print("⚠️ WARNING: TradingView library not available")
            print("   Scan endpoints may not work")
    except Exception as e:
        print(f"❌ Backend not responding: {e}")
        return

    print()

    # Test strategies endpoint
    strategies = test_scan_strategies()

    if not strategies:
        print("⚠️ No strategies found, using defaults")
        strategies = ['reddit', 'minervini', 'momentum', 'value']

    # Test each scan strategy
    results = []
    for strategy in strategies:
        result = test_scan(strategy, limit=25)
        results.append(result)
        time.sleep(1)  # Brief pause between scans

    # Analyze results
    summary = analyze_results(results)

    # Save results
    timestamp = datetime.now().strftime('%H%M%S')
    output_file = f"scan_test_results_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'successful': summary['successful'],
                'failed': summary['failed']
            },
            'results': results
        }, f, indent=2)

    print(f"\n💾 Results saved to: {output_file}")
    print("\n✅ Scan market test complete!")


if __name__ == "__main__":
    main()
