#!/usr/bin/env python3
"""
TradingView Comparison Helper
Day 34: Generate S&R levels for manual TradingView comparison

Usage:
    python tradingview_comparison.py AAPL MSFT NVDA

This outputs our S&R levels in a format easy to compare with TradingView's
built-in Support & Resistance indicator.

Comparison Protocol:
1. Run this script to get our levels
2. Open TradingView chart for the same stock
3. Add "Support and Resistance" indicator (or look at obvious levels)
4. Compare nearest S&R levels (within 2% tolerance)
5. Mark as MATCH, PARTIAL (within 5%), or MISS
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yfinance as yf
from support_resistance import compute_sr_levels, SRConfig


def get_levels_for_comparison(ticker: str) -> dict:
    """
    Get S&R levels formatted for TradingView comparison.
    Now includes major historical levels (>20% from current price).
    """
    try:
        # Fetch data
        stock = yf.Ticker(ticker)
        df = stock.history(period="2y")

        if df.empty:
            return {"error": f"No data for {ticker}"}

        # Standardize columns
        df.columns = [c.lower() for c in df.columns]

        # Compute S&R
        config = SRConfig(
            use_agglomerative=True,
            use_mtf=True,
            use_fibonacci=True
        )
        sr = compute_sr_levels(df, config)

        current_price = float(df['close'].iloc[-1])

        # Get nearest levels
        support = sorted(sr.support, reverse=True)  # Descending (nearest first)
        resistance = sorted(sr.resistance)  # Ascending (nearest first)

        # Calculate distances for NEAREST 5 levels
        support_with_dist = []
        for s in support[:5]:
            dist_pct = round((current_price - s) / current_price * 100, 2)
            support_with_dist.append({
                "level": round(s, 2),
                "distance_pct": dist_pct
            })

        resistance_with_dist = []
        for r in resistance[:5]:
            dist_pct = round((r - current_price) / current_price * 100, 2)
            resistance_with_dist.append({
                "level": round(r, 2),
                "distance_pct": dist_pct
            })

        # NEW: Major Historical Levels (>25% from current price)
        # These are important for understanding the bigger picture
        # Include round number levels and levels >35% away
        major_support = []
        for s in support[5:]:  # Skip first 5 (already shown)
            dist_pct = round((current_price - s) / current_price * 100, 2)
            level_rounded = round(s, 2)
            # Include if: >25% away, OR at a round number (divisible by 50 or 100)
            is_round_number = (level_rounded % 100 < 5) or (level_rounded % 50 < 3)
            if dist_pct >= 25 or (dist_pct >= 20 and is_round_number):
                major_support.append({
                    "level": level_rounded,
                    "distance_pct": dist_pct,
                    "is_round": is_round_number
                })

        major_resistance = []
        for r in resistance[5:]:  # Skip first 5 (already shown)
            dist_pct = round((r - current_price) / current_price * 100, 2)
            level_rounded = round(r, 2)
            is_round_number = (level_rounded % 100 < 5) or (level_rounded % 50 < 3)
            if dist_pct >= 25 or (dist_pct >= 20 and is_round_number):
                major_resistance.append({
                    "level": level_rounded,
                    "distance_pct": dist_pct,
                    "is_round": is_round_number
                })

        # MTF confluence info
        mtf = sr.meta.get("mtf", {})
        confluence_map = mtf.get("confluence_map", {})

        # Mark which levels are confluent
        for s in support_with_dist:
            key = str(s["level"])
            s["confluent"] = confluence_map.get(key, {}).get("confluent", False)

        for r in resistance_with_dist:
            key = str(r["level"])
            r["confluent"] = confluence_map.get(key, {}).get("confluent", False)

        # Mark major levels confluence too
        for s in major_support:
            key = str(s["level"])
            s["confluent"] = confluence_map.get(key, {}).get("confluent", False)

        for r in major_resistance:
            key = str(r["level"])
            r["confluent"] = confluence_map.get(key, {}).get("confluent", False)

        return {
            "ticker": ticker,
            "current_price": round(current_price, 2),
            "method": sr.method,
            "projection_method": sr.meta.get("projection_method"),
            "support": support_with_dist,
            "resistance": resistance_with_dist,
            "major_support": major_support,  # NEW
            "major_resistance": major_resistance,  # NEW
            "total_support_levels": len(sr.support),  # NEW
            "total_resistance_levels": len(sr.resistance),  # NEW
            "mtf_confluence_pct": mtf.get("confluence_pct", 0),
            "atr": sr.meta.get("atr"),
            "atr_pct": round(sr.meta.get("atr", 0) / current_price * 100, 2)
        }

    except Exception as e:
        return {"error": str(e)}


def print_comparison_card(data: dict):
    """
    Print a comparison card for manual TradingView validation.
    Now includes Major Historical Levels section.
    """
    if "error" in data:
        print(f"ERROR: {data['error']}")
        return

    print()
    print("=" * 60)
    print(f"  {data['ticker']} - TradingView Comparison Card")
    print("=" * 60)
    print(f"  Current Price: ${data['current_price']}")
    print(f"  Method: {data['method']}")
    if data.get('projection_method'):
        print(f"  Projection: {data['projection_method']}")
    print(f"  MTF Confluence: {data['mtf_confluence_pct']}%")
    print(f"  ATR: ${data['atr']} ({data['atr_pct']}%)")
    print(f"  Total Levels: {data.get('total_support_levels', '?')} support, {data.get('total_resistance_levels', '?')} resistance")
    print("-" * 60)

    print()
    print("  RESISTANCE LEVELS (targets above):")
    print("  " + "-" * 50)
    for i, r in enumerate(data['resistance'], 1):
        conf = " [MTF]" if r['confluent'] else ""
        print(f"  R{i}: ${r['level']:>10}  (+{r['distance_pct']:>5}%){conf}")
        print(f"      TV Match: [ ]  Level: $________")

    print()
    print("  SUPPORT LEVELS (stops below):")
    print("  " + "-" * 50)
    for i, s in enumerate(data['support'], 1):
        conf = " [MTF]" if s['confluent'] else ""
        print(f"  S{i}: ${s['level']:>10}  (-{s['distance_pct']:>5}%){conf}")
        print(f"      TV Match: [ ]  Level: $________")

    # NEW: Major Historical Levels section
    major_support = data.get('major_support', [])
    major_resistance = data.get('major_resistance', [])

    if major_support or major_resistance:
        print()
        print("  MAJOR HISTORICAL LEVELS (>25% from current):")
        print("  " + "-" * 50)

        if major_resistance:
            for i, r in enumerate(major_resistance[:5], 1):  # Show up to 5
                conf = " [MTF]" if r.get('confluent') else ""
                round_marker = " *" if r.get('is_round') else ""
                print(f"  MR{i}: ${r['level']:>9}  (+{r['distance_pct']:>5}%){conf}{round_marker}")

        if major_support:
            for i, s in enumerate(major_support[:5], 1):  # Show up to 5
                conf = " [MTF]" if s.get('confluent') else ""
                round_marker = " *" if s.get('is_round') else ""
                print(f"  MS{i}: ${s['level']:>9}  (-{s['distance_pct']:>5}%){conf}{round_marker}")

    print()
    print("  COMPARISON NOTES:")
    print("  " + "-" * 50)
    print("  Match Criteria: Within 2% = MATCH, 2-5% = PARTIAL, >5% = MISS")
    print("  [MTF] = Confluent (daily + weekly timeframe)")
    print("  MS/MR = Major historical levels (for context)")
    print("  * = Round number level (psychological importance)")
    print()
    print("  Summary: ___ MATCH, ___ PARTIAL, ___ MISS, ___ TV-ONLY")
    print("=" * 60)
    print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python tradingview_comparison.py TICKER [TICKER2 ...]")
        print("Example: python tradingview_comparison.py AAPL NVDA GOOGL")
        sys.exit(1)

    tickers = sys.argv[1:]

    print("\n" + "=" * 60)
    print("TradingView S&R Comparison Tool")
    print("Day 34 - Week 4 Validation")
    print("=" * 60)

    for ticker in tickers:
        print(f"\nFetching {ticker}...", end=" ")
        data = get_levels_for_comparison(ticker.upper())
        print("Done")
        print_comparison_card(data)


if __name__ == "__main__":
    main()
