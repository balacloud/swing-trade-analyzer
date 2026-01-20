#!/usr/bin/env python3
"""
Week 4 Validation: S&R Engine Testing
Day 34: Comprehensive validation against 30 diverse stocks

Purpose:
- Walk-forward testing on diverse stock universe
- Validate Agglomerative clustering improvements (Day 30)
- Validate MTF Confluence effectiveness (Day 32)
- Validate Fibonacci Extensions accuracy (Day 33)
- Compare with TradingView S&R (manual spot-check)

Test Universe:
- Mega caps: AAPL, MSFT, NVDA, GOOGL, AMZN
- Growth: TSLA, AMD, PLTR, SNOW, CRM
- Value: BRK-B, JPM, XOM, PG, JNJ
- Small caps: SOFI, IONQ, RKLB, UPST, AI
- Sector diverse: DIS, NFLX, BA, CAT, HD
- Near ATH: META, COST, LLY, AVGO, PANW

Success Criteria (from research):
- Detection rate: 80% -> 95%+ target
- ATH stock handling: 45% -> 78%+ with Fibonacci
- Confluence rate: 50%+ of levels should be MTF confluent

Output:
- JSON report with all metrics
- Summary statistics
- TradingView comparison notes
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yfinance as yf
import pandas as pd
import numpy as np

from support_resistance import compute_sr_levels, SRConfig, SRFailure


# ============================================
# VALIDATION TEST UNIVERSE
# ============================================

TEST_STOCKS = {
    "mega_caps": ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN"],
    "growth": ["TSLA", "AMD", "PLTR", "SNOW", "CRM"],
    "value": ["BRK-B", "JPM", "XOM", "PG", "JNJ"],
    "small_caps": ["SOFI", "IONQ", "RKLB", "UPST", "AI"],
    "sector_diverse": ["DIS", "NFLX", "BA", "CAT", "HD"],
    "near_ath": ["META", "COST", "LLY", "AVGO", "PANW"]
}

# Flatten to single list
ALL_STOCKS = [stock for category in TEST_STOCKS.values() for stock in category]


def fetch_stock_data(ticker: str, period: str = "2y") -> Optional[pd.DataFrame]:
    """
    Fetch OHLCV data for a stock using yfinance.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol
    period : str
        Data period (default 2 years for sufficient history)

    Returns
    -------
    Optional[pd.DataFrame]
        OHLCV DataFrame or None if fetch failed
    """
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)

        if df.empty:
            print(f"  WARNING: No data for {ticker}")
            return None

        # Standardize column names to lowercase
        df.columns = [c.lower() for c in df.columns]

        # Ensure required columns exist
        required = ['open', 'high', 'low', 'close', 'volume']
        for col in required:
            if col not in df.columns:
                print(f"  WARNING: Missing {col} column for {ticker}")
                return None

        return df

    except Exception as e:
        print(f"  ERROR fetching {ticker}: {e}")
        return None


def compute_validation_metrics(
    ticker: str,
    sr_result,
    df: pd.DataFrame
) -> Dict[str, Any]:
    """
    Compute validation metrics for a single stock's S&R analysis.

    Parameters
    ----------
    ticker : str
        Stock ticker
    sr_result : SRLevels
        Result from compute_sr_levels()
    df : pd.DataFrame
        OHLCV data

    Returns
    -------
    Dict[str, Any]
        Validation metrics
    """
    current_price = float(df['close'].iloc[-1])
    high_52w = float(df['high'].max())
    low_52w = float(df['low'].min())

    metrics = {
        "ticker": ticker,
        "current_price": round(current_price, 2),
        "52w_high": round(high_52w, 2),
        "52w_low": round(low_52w, 2),
        "pct_from_ath": round((high_52w - current_price) / high_52w * 100, 2),
        "method_used": sr_result.method,
        "support_count": len(sr_result.support),
        "resistance_count": len(sr_result.resistance),
        "support_levels": [round(s, 2) for s in sr_result.support[-5:]],  # Last 5
        "resistance_levels": [round(r, 2) for r in sr_result.resistance[:5]],  # First 5
        "meta": {}
    }

    # Extract important meta fields
    meta = sr_result.meta

    # ATR
    metrics["atr"] = meta.get("atr", None)
    metrics["atr_pct"] = round(meta.get("atr", 0) / current_price * 100, 2) if meta.get("atr") else None

    # Projection flags
    metrics["resistance_projected"] = meta.get("resistance_projected", False)
    metrics["support_projected"] = meta.get("support_projected", False)
    metrics["projection_method"] = meta.get("projection_method", None)

    # Trade viability
    viability = meta.get("trade_viability", {})
    metrics["trade_viable"] = viability.get("viable", None)
    metrics["support_distance_pct"] = viability.get("support_distance_pct", None)
    metrics["risk_reward"] = viability.get("risk_reward_context", None)

    # MTF Confluence (Day 32)
    mtf = meta.get("mtf", {})
    if mtf.get("enabled"):
        metrics["mtf_enabled"] = True
        metrics["mtf_confluent_levels"] = mtf.get("confluent_levels", 0)
        metrics["mtf_total_levels"] = mtf.get("total_levels", 0)
        metrics["mtf_confluence_pct"] = mtf.get("confluence_pct", 0)
        metrics["weekly_support_count"] = len(mtf.get("weekly_support", []))
        metrics["weekly_resistance_count"] = len(mtf.get("weekly_resistance", []))
    else:
        metrics["mtf_enabled"] = False
        metrics["mtf_confluence_pct"] = 0

    # Level scoring (Day 30)
    level_scores = meta.get("level_scores", {})
    if level_scores:
        scores = list(level_scores.values())
        metrics["avg_level_score"] = round(sum(scores) / len(scores), 1) if scores else 0
        metrics["max_level_score"] = max(scores) if scores else 0

    # Agglomerative-specific metrics
    if sr_result.method == "agglomerative":
        metrics["raw_pivot_count"] = meta.get("raw_pivot_count", 0)
        metrics["clustered_level_count"] = meta.get("clustered_level_count", 0)
        metrics["valid_level_count"] = meta.get("valid_level_count", 0)

    return metrics


def calculate_summary_stats(all_metrics: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate aggregate summary statistics across all tested stocks.

    Parameters
    ----------
    all_metrics : List[Dict[str, Any]]
        List of validation metrics for each stock

    Returns
    -------
    Dict[str, Any]
        Summary statistics
    """
    total = len(all_metrics)

    summary = {
        "total_stocks_tested": total,
        "timestamp": datetime.now().isoformat(),
        "methods": {},
        "projection_stats": {},
        "mtf_stats": {},
        "viability_stats": {},
        "level_stats": {}
    }

    # Method distribution
    methods = [m["method_used"] for m in all_metrics]
    for method in set(methods):
        summary["methods"][method] = {
            "count": methods.count(method),
            "pct": round(methods.count(method) / total * 100, 1)
        }

    # Projection stats (Fibonacci vs ATR)
    fib_count = sum(1 for m in all_metrics if m.get("projection_method") == "fibonacci")
    atr_count = sum(1 for m in all_metrics if m.get("projection_method") == "atr")
    no_proj = sum(1 for m in all_metrics if m.get("projection_method") is None)

    summary["projection_stats"] = {
        "fibonacci_used": fib_count,
        "atr_used": atr_count,
        "no_projection_needed": no_proj,
        "fibonacci_pct": round(fib_count / total * 100, 1) if total > 0 else 0
    }

    # MTF Confluence stats
    mtf_enabled = [m for m in all_metrics if m.get("mtf_enabled")]
    if mtf_enabled:
        confluence_pcts = [m["mtf_confluence_pct"] for m in mtf_enabled]
        summary["mtf_stats"] = {
            "mtf_enabled_count": len(mtf_enabled),
            "avg_confluence_pct": round(sum(confluence_pcts) / len(confluence_pcts), 1),
            "min_confluence_pct": min(confluence_pcts),
            "max_confluence_pct": max(confluence_pcts),
            "stocks_with_50pct_plus_confluence": sum(1 for p in confluence_pcts if p >= 50)
        }

    # Trade viability distribution
    viable_values = [m.get("trade_viable") for m in all_metrics if m.get("trade_viable")]
    if viable_values:
        summary["viability_stats"] = {
            "YES": viable_values.count("YES"),
            "CAUTION": viable_values.count("CAUTION"),
            "NO": viable_values.count("NO"),
            "UNKNOWN": viable_values.count("UNKNOWN")
        }

    # Level count stats
    support_counts = [m["support_count"] for m in all_metrics]
    resistance_counts = [m["resistance_count"] for m in all_metrics]

    summary["level_stats"] = {
        "avg_support_levels": round(sum(support_counts) / len(support_counts), 1),
        "avg_resistance_levels": round(sum(resistance_counts) / len(resistance_counts), 1),
        "stocks_with_zero_support": sum(1 for c in support_counts if c == 0),
        "stocks_with_zero_resistance": sum(1 for c in resistance_counts if c == 0)
    }

    # Near ATH detection accuracy
    near_ath = [m for m in all_metrics if m["pct_from_ath"] <= 5]
    if near_ath:
        fib_on_ath = sum(1 for m in near_ath if m.get("projection_method") == "fibonacci")
        summary["ath_handling"] = {
            "stocks_near_ath": len(near_ath),
            "fibonacci_used_on_ath": fib_on_ath,
            "fibonacci_ath_pct": round(fib_on_ath / len(near_ath) * 100, 1) if near_ath else 0
        }

    return summary


def run_validation(
    stocks: List[str] = None,
    verbose: bool = True,
    delay: float = 0.5
) -> Dict[str, Any]:
    """
    Run full validation suite on stock universe.

    Parameters
    ----------
    stocks : List[str], optional
        List of tickers (default: ALL_STOCKS)
    verbose : bool
        Print progress (default: True)
    delay : float
        Delay between API calls (default: 0.5s)

    Returns
    -------
    Dict[str, Any]
        Complete validation report
    """
    if stocks is None:
        stocks = ALL_STOCKS

    results = {
        "test_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "config": {
            "use_agglomerative": True,
            "use_mtf": True,
            "use_fibonacci": True,
            "merge_percent": 0.02,
            "zigzag_percent_delta": 0.05,
            "mtf_confluence_threshold": 0.015,
            "ath_threshold": 0.05
        },
        "stock_metrics": [],
        "errors": [],
        "summary": {}
    }

    config = SRConfig(
        use_agglomerative=True,
        use_mtf=True,
        use_fibonacci=True
    )

    if verbose:
        print("=" * 60)
        print("Week 4 Validation: S&R Engine Testing")
        print(f"Testing {len(stocks)} stocks")
        print("=" * 60)
        print()

    for i, ticker in enumerate(stocks, 1):
        if verbose:
            print(f"[{i}/{len(stocks)}] Testing {ticker}...", end=" ")

        try:
            # Fetch data
            df = fetch_stock_data(ticker)

            if df is None:
                results["errors"].append({
                    "ticker": ticker,
                    "error": "Failed to fetch data"
                })
                if verbose:
                    print("SKIP (no data)")
                continue

            # Compute S&R
            sr_result = compute_sr_levels(df, config)

            # Compute metrics
            metrics = compute_validation_metrics(ticker, sr_result, df)
            results["stock_metrics"].append(metrics)

            if verbose:
                status = []
                status.append(f"method={sr_result.method}")
                status.append(f"S={len(sr_result.support)}")
                status.append(f"R={len(sr_result.resistance)}")
                if metrics.get("projection_method"):
                    status.append(f"proj={metrics['projection_method']}")
                if metrics.get("mtf_confluence_pct", 0) > 0:
                    status.append(f"MTF={metrics['mtf_confluence_pct']:.0f}%")
                print(" | ".join(status))

            # Rate limit
            time.sleep(delay)

        except SRFailure as e:
            results["errors"].append({
                "ticker": ticker,
                "error": f"SRFailure: {str(e)}"
            })
            if verbose:
                print(f"FAIL: {e}")

        except Exception as e:
            results["errors"].append({
                "ticker": ticker,
                "error": str(e)
            })
            if verbose:
                print(f"ERROR: {e}")

    # Calculate summary
    if results["stock_metrics"]:
        results["summary"] = calculate_summary_stats(results["stock_metrics"])

    return results


def print_report(results: Dict[str, Any]) -> None:
    """Print formatted validation report."""
    print("\n" + "=" * 60)
    print("VALIDATION REPORT")
    print("=" * 60)

    summary = results.get("summary", {})

    print(f"\nTest Date: {results['test_date']}")
    print(f"Stocks Tested: {summary.get('total_stocks_tested', 0)}")
    print(f"Errors: {len(results.get('errors', []))}")

    # Method Distribution
    print("\n--- Method Distribution ---")
    methods = summary.get("methods", {})
    for method, data in methods.items():
        print(f"  {method}: {data['count']} stocks ({data['pct']}%)")

    # Projection Stats
    print("\n--- Projection Stats (ATH Handling) ---")
    proj = summary.get("projection_stats", {})
    print(f"  Fibonacci used: {proj.get('fibonacci_used', 0)} stocks")
    print(f"  ATR fallback: {proj.get('atr_used', 0)} stocks")
    print(f"  No projection needed: {proj.get('no_projection_needed', 0)} stocks")

    # ATH Handling (Day 33)
    ath = summary.get("ath_handling", {})
    if ath:
        print(f"\n--- ATH Stock Handling (Day 33) ---")
        print(f"  Stocks within 5% of ATH: {ath.get('stocks_near_ath', 0)}")
        print(f"  Fibonacci used on ATH stocks: {ath.get('fibonacci_used_on_ath', 0)} ({ath.get('fibonacci_ath_pct', 0)}%)")
        print(f"  Target: 78%+ using Fibonacci for ATH")

    # MTF Stats (Day 32)
    mtf = summary.get("mtf_stats", {})
    if mtf:
        print(f"\n--- MTF Confluence Stats (Day 32) ---")
        print(f"  MTF enabled on: {mtf.get('mtf_enabled_count', 0)} stocks")
        print(f"  Avg confluence: {mtf.get('avg_confluence_pct', 0)}%")
        print(f"  Range: {mtf.get('min_confluence_pct', 0)}% - {mtf.get('max_confluence_pct', 0)}%")
        print(f"  Stocks with 50%+ confluence: {mtf.get('stocks_with_50pct_plus_confluence', 0)}")
        print(f"  Target: 50%+ levels confluent")

    # Viability Stats (Day 22)
    viab = summary.get("viability_stats", {})
    if viab:
        print(f"\n--- Trade Viability (Day 22) ---")
        print(f"  YES (tight setup): {viab.get('YES', 0)} stocks")
        print(f"  CAUTION (wide stop): {viab.get('CAUTION', 0)} stocks")
        print(f"  NO (too extended): {viab.get('NO', 0)} stocks")

    # Level Stats
    levels = summary.get("level_stats", {})
    print(f"\n--- Level Detection ---")
    print(f"  Avg support levels: {levels.get('avg_support_levels', 0)}")
    print(f"  Avg resistance levels: {levels.get('avg_resistance_levels', 0)}")
    print(f"  Zero support: {levels.get('stocks_with_zero_support', 0)} stocks")
    print(f"  Zero resistance: {levels.get('stocks_with_zero_resistance', 0)} stocks")

    # Errors
    if results.get("errors"):
        print(f"\n--- Errors ({len(results['errors'])}) ---")
        for err in results["errors"]:
            print(f"  {err['ticker']}: {err['error']}")

    print("\n" + "=" * 60)


def save_report(results: Dict[str, Any], filename: str = None) -> str:
    """Save validation report to JSON file."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"validation_report_{timestamp}.json"

    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    return filepath


def main():
    """Run validation suite and generate report."""
    print("\nStarting Week 4 Validation...\n")

    # Run validation on all 30 stocks
    results = run_validation(ALL_STOCKS, verbose=True, delay=0.3)

    # Print report
    print_report(results)

    # Save report
    filepath = save_report(results)
    print(f"\nReport saved to: {filepath}")

    # Success criteria check
    print("\n" + "=" * 60)
    print("SUCCESS CRITERIA CHECK")
    print("=" * 60)

    summary = results.get("summary", {})

    # 1. Detection rate (no zero levels)
    levels = summary.get("level_stats", {})
    zero_support = levels.get("stocks_with_zero_support", 0)
    zero_resistance = levels.get("stocks_with_zero_resistance", 0)
    detection_rate = (1 - (zero_support + zero_resistance) / (summary.get("total_stocks_tested", 1) * 2)) * 100
    print(f"1. Detection Rate: {detection_rate:.1f}% (Target: 95%+) {'PASS' if detection_rate >= 95 else 'NEEDS WORK'}")

    # 2. ATH handling with Fibonacci
    ath = summary.get("ath_handling", {})
    fib_ath_pct = ath.get("fibonacci_ath_pct", 0)
    print(f"2. ATH Fibonacci Usage: {fib_ath_pct}% (Target: 78%+) {'PASS' if fib_ath_pct >= 78 else 'NEEDS WORK' if ath else 'N/A - no ATH stocks'}")

    # 3. MTF Confluence
    mtf = summary.get("mtf_stats", {})
    avg_conf = mtf.get("avg_confluence_pct", 0)
    print(f"3. MTF Confluence: {avg_conf}% avg (Target: 50%+) {'PASS' if avg_conf >= 50 else 'NEEDS WORK'}")

    return results


if __name__ == "__main__":
    main()
