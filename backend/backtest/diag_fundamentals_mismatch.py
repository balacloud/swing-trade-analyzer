"""
Fundamentals Data-Source Mismatch Diagnostic — Day 78 (Fable Remediation Task 3.2)

Backtest fundamentals come from SimFin (ROE = quarterly net income x4 /
equity, YoY = same-quarter-prior-year comparison, both point-in-time via
Publish Date). Live fundamentals come from Finnhub -> AlphaVantage ->
yfinance TTM data via DataProvider. Same stock, same day, can get a
DIFFERENT categorical label (Strong/Decent/Weak) from each source — meaning
"live Config C" is not literally the same thing as "backtested Config C."

This script fetches both for ~20 liquid tickers, runs assess_fundamental()
(the same function categorical_engine.py uses) on each set of values, and
reports how often the resulting label disagrees.

Units check (verified before writing this script, not assumed):
  - roe: whole percent on both sides (Finnhub raw roeTTM converted x100 if
    fractional; SimFin computed as (net_income*4/equity)*100). Same convention.
  - revenue_growth: whole percent on both sides (AlphaVantage/yfinance decimal
    converted via _growth_to_pct; SimFin computed as YoY% directly). Same convention.
  - debt_equity: raw ratio (no percent conversion) on both sides. Same convention.

Usage:
    python backend/backtest/diag_fundamentals_mismatch.py
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))                    # backend/backtest/

from providers import get_data_provider
from simfin_loader import get_fundamentals_at_date
from categorical_engine import assess_fundamental

# 20 liquid tickers spanning sectors (subset of the holistic backtest universe)
TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
    'JPM', 'V', 'MA', 'GS', 'BAC',
    'UNH', 'JNJ', 'LLY',
    'PG', 'HD', 'WMT', 'KO', 'XOM',
]

DISAGREEMENT_FLAG_THRESHOLD = 20.0  # percent


def get_live_fundamentals(dp, ticker):
    result = dp.get_fundamentals(ticker)
    if not result:
        return None
    return {
        'roe': result.get('roe'),
        'revenue_growth': result.get('revenueGrowth'),
        'debt_equity': result.get('debtToEquity'),
    }


def get_simfin_fundamentals(ticker, as_of_date):
    result = get_fundamentals_at_date(ticker, as_of_date)
    if not result:
        return None
    return {
        'roe': result.get('roe'),
        'revenue_growth': result.get('revenue_growth_yoy'),
        'debt_equity': result.get('debt_equity'),
        'publish_date': result.get('publish_date'),
        'fiscal_period': result.get('fiscal_period'),
        'fiscal_year': result.get('fiscal_year'),
    }


def main():
    print("=" * 70)
    print("  Fundamentals Data-Source Mismatch Diagnostic (Day 78, Task 3.2)")
    print("=" * 70)

    dp = get_data_provider()
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\n  Comparing live (Finnhub/DataProvider, as of now) vs SimFin")
    print(f"  (latest published quarter as of {today})\n")

    rows = []
    for ticker in TICKERS:
        print(f"  {ticker}...", end=' ', flush=True)
        try:
            live = get_live_fundamentals(dp, ticker)
        except Exception as e:
            print(f"SKIP (live fetch error: {e})")
            continue
        try:
            simfin = get_simfin_fundamentals(ticker, today)
        except Exception as e:
            print(f"SKIP (SimFin fetch error: {e})")
            continue

        if live is None:
            print("SKIP: no live fundamentals available")
            continue
        if simfin is None:
            print("SKIP: no SimFin fundamentals available")
            continue

        live_assessment = assess_fundamental(
            roe=live['roe'], revenue_growth=live['revenue_growth'], debt_equity=live['debt_equity']
        )
        simfin_assessment = assess_fundamental(
            roe=simfin['roe'], revenue_growth=simfin['revenue_growth'], debt_equity=simfin['debt_equity']
        )

        live_label = live_assessment['assessment']
        simfin_label = simfin_assessment['assessment']
        match = live_label == simfin_label

        print("MATCH" if match else "MISMATCH")
        print(f"    Live:   ROE={live['roe']}, RevGrowth={live['revenue_growth']}, D/E={live['debt_equity']} -> {live_label}")
        print(f"    SimFin: ROE={simfin['roe']}, RevGrowth={simfin['revenue_growth']}, D/E={simfin['debt_equity']} "
              f"(as of {simfin.get('publish_date')}, {simfin.get('fiscal_year')} {simfin.get('fiscal_period')}) -> {simfin_label}")

        rows.append({
            'ticker': ticker, 'live': live, 'simfin': simfin,
            'live_label': live_label, 'simfin_label': simfin_label, 'match': match,
        })

    n = len(rows)
    n_match = sum(1 for r in rows if r['match'])
    n_mismatch = n - n_match
    disagreement_rate = (n_mismatch / n * 100) if n > 0 else 0

    print(f"\n{'=' * 70}")
    print("  SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Tickers compared:   {n} (of {len(TICKERS)} attempted)")
    print(f"  Matching labels:    {n_match}")
    print(f"  Mismatched labels:  {n_mismatch}")
    print(f"  Disagreement rate:  {disagreement_rate:.1f}%")

    if n_mismatch > 0:
        print(f"\n  Mismatched tickers:")
        for r in rows:
            if not r['match']:
                print(f"    {r['ticker']}: live={r['live_label']} vs simfin={r['simfin_label']}")

    if disagreement_rate > DISAGREEMENT_FLAG_THRESHOLD:
        print(f"\n  FLAG: disagreement rate exceeds {DISAGREEMENT_FLAG_THRESHOLD}% threshold.")
        print("  'Live Config C' meaningfully differs from 'backtested Config C' for the")
        print("  Fundamental category. Mitigation is a user decision:")
        print("    (a) align live computation to annualized-quarterly (match SimFin's method), or")
        print("    (b) re-run the backtest with TTM-style fundamentals (match live's method).")
    else:
        print(f"\n  Disagreement rate is within the {DISAGREEMENT_FLAG_THRESHOLD}% threshold —")
        print("  not flagged as urgent, but the underlying data-source difference exists")
        print("  and should be documented (see KNOWN_ISSUES).")

    print(f"{'=' * 70}\n")

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diag_fundamentals_mismatch_result.json')
    with open(output_path, 'w') as f:
        json.dump({
            'run_date': today,
            'n_compared': n,
            'n_match': n_match,
            'n_mismatch': n_mismatch,
            'disagreement_rate_pct': round(disagreement_rate, 1),
            'rows': rows,
        }, f, indent=2, default=str)
    print(f"  Full results saved to: {output_path}\n")


if __name__ == '__main__':
    main()
