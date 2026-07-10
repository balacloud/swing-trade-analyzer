"""
Survivorship-Free Re-Validation — Day 79 (Fable Remediation Task 4.1)

The original 60-ticker Config C backtest (PF 1.61) was hand-picked in 2026
and is dominated by 2020-2025 hindsight winners (NVDA, LLY, AVGO, PLTR,
CRWD, COIN...). A momentum-BUY filter tested on hindsight-selected momentum
winners looks good almost by construction. This is the single biggest
threat to PF 1.61 being real.

This script rebuilds the universe from SimFin's own point-in-time coverage
(3,788 US tickers as of Day 79) via random sampling, seeded for
reproducibility — no hand-picking. Liquidity filtering happens PER-DATE
inside the backtest itself (see backtest_holistic.check_entry_signals'
liquidity gate: price > $5, 20d avg dollar volume > $5M), not as a
pre-selection step, since pre-filtering to "currently liquid" names would
reintroduce hindsight bias of its own.

Runs Config C (momentum, standard period) and the MR strategy on the SAME
unbiased universe, using the already-fixed simulators (Phase 2: transaction
costs, gap-aware fills; Task 2.3 statistics).

Usage:
    python backend/backtest/backtest_survivorship_free.py --sample-size 400
    python backend/backtest/backtest_survivorship_free.py --sample-size 30   # smoke test
"""

import os
import sys
import json
import random
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simfin_loader import get_available_tickers
from backtest_holistic import run_holistic_backtest, download_data
from mr_simulator import backtest_mr_strategy
from metrics import compute_metrics


def build_unbiased_universe(sample_size=400, seed=42):
    """
    Random sample from SimFin's full US ticker coverage — no hand-picking.

    Liquidity filtering happens per-date INSIDE the backtest (the gate in
    check_entry_signals), not here — pre-filtering to "currently liquid"
    tickers would just be a different flavor of hindsight bias.
    """
    all_tickers = sorted(get_available_tickers())
    rng = random.Random(seed)
    sample = rng.sample(all_tickers, min(sample_size, len(all_tickers)))
    return sorted(sample), len(all_tickers)


def _translate_mr_trades_for_metrics(mr_trades):
    """
    mr_simulator.py's trade dicts use different field names than
    metrics.compute_metrics() expects (that function was built for the
    momentum system's _build_result() shape). Without this translation,
    compute_metrics() silently finds none of its expected keys ('result',
    'return_pct_net', 'return_r') and defaults everything to 0/missing —
    producing nonsense like "0% win rate, PF inf" instead of an error.

    Translate: 'win' (bool) -> 'result' ('win'/'loss'/'breakeven', using the
    same +/-0.5% threshold as the momentum system's _build_result()),
    'pnl_pct'/'pnl_pct_net' -> 'return_pct'/'return_pct_net',
    'pnl_r_net' -> 'return_r'. MR doesn't compute a regime label — default
    'unknown' so compute_metrics()'s regime breakdown doesn't KeyError.
    """
    translated = []
    for t in mr_trades:
        pnl_net = t.get('pnl_pct_net', t.get('pnl_pct', 0))
        if pnl_net > 0.5:
            result = 'win'
        elif pnl_net < -0.5:
            result = 'loss'
        else:
            result = 'breakeven'
        translated.append({
            **t,
            'result': result,
            'return_pct': t.get('pnl_pct', 0),
            'return_pct_net': pnl_net,
            'return_r': t.get('pnl_r_net', t.get('pnl_r', 0)),
            'regime': t.get('regime', 'unknown'),
        })
    return translated


def run_mr_on_universe(tickers, start, end, verbose=True):
    """Run MR strategy on the same universe (mirrors gate5_combined.py's per-ticker pattern)."""
    all_trades = []
    skipped = []
    for i, ticker in enumerate(tickers, 1):
        if verbose:
            print(f"  [{i}/{len(tickers)}] MR: {ticker}...", end=' ', flush=True)
        try:
            stock_df = download_data(ticker, start, end)
        except Exception as e:
            if verbose:
                print(f"SKIP (download error: {e})")
            skipped.append(ticker)
            continue
        if stock_df is None or len(stock_df) < 200:
            if verbose:
                print("SKIP (insufficient data)")
            skipped.append(ticker)
            continue
        result = backtest_mr_strategy(stock_df, ticker=ticker)
        trades = result.get('trades', [])
        all_trades.extend(trades)
        if verbose:
            print(f"{len(trades)} trades")
    return all_trades, skipped


def main():
    parser = argparse.ArgumentParser(description='Survivorship-Free Re-Validation (Task 4.1)')
    parser.add_argument('--sample-size', type=int, default=400)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--start', default='2020-01-01')
    parser.add_argument('--end', default='2025-12-31')
    parser.add_argument('--scan-interval', type=int, default=2)
    parser.add_argument('--mr-only', action='store_true',
                        help='Skip Config C (momentum) — re-test MR alone on the same universe/seed, e.g. after an MR-specific change')
    args = parser.parse_args()

    print("=" * 70)
    print("  SURVIVORSHIP-FREE RE-VALIDATION (Day 79, Task 4.1)")
    print("=" * 70)

    universe, total_coverage = build_unbiased_universe(args.sample_size, args.seed)
    print(f"\n  Universe: {len(universe)} tickers (random sample, seed={args.seed}, "
          f"from {total_coverage} SimFin-covered US tickers)")
    print(f"  First 15: {universe[:15]}")

    if args.mr_only:
        print("\n  --mr-only: skipping Config C (momentum unchanged since the last full run)")
        momentum_c = None
        momentum_tickers_processed = None
        momentum_tickers_skipped = None
    else:
        # --- Config C (momentum) — reuses run_holistic_backtest unchanged ---
        print(f"\n{'=' * 70}\n  RUNNING CONFIG C (momentum, standard period)\n{'=' * 70}")
        momentum_results = run_holistic_backtest(
            universe, start=args.start, end=args.end,
            holding_periods=['standard'], configs=['C'],
            scan_interval=args.scan_interval, verbose=True,
        )

        momentum_tickers_processed = momentum_results['meta']['tickers_processed']
        momentum_tickers_skipped = len(universe) - momentum_tickers_processed
        momentum_c = momentum_results['results'].get('C_standard', {})

    # --- MR ---
    print(f"\n{'=' * 70}\n  RUNNING MEAN-REVERSION\n{'=' * 70}")
    mr_trades, mr_skipped = run_mr_on_universe(universe, args.start, args.end)
    mr_metrics = compute_metrics(_translate_mr_trades_for_metrics(mr_trades))

    print(f"\n{'=' * 70}\n  MR RESULTS\n{'=' * 70}")
    print(f"  Total trades:    {mr_metrics['total_trades']}")
    print(f"  Win rate:        {mr_metrics['win_rate']}%")
    print(f"  Profit Factor:   {mr_metrics['profit_factor']}")
    print(f"  Sharpe:          {mr_metrics['sharpe_ratio']}")
    print(f"  Skipped:         {len(mr_skipped)}/{len(universe)}")

    if momentum_c is not None:
        print(f"\n{'=' * 70}\n  CONFIG C RESULTS\n{'=' * 70}")
        print(f"  Total trades:    {momentum_c.get('total_trades')}")
        print(f"  Win rate:        {momentum_c.get('win_rate')}%")
        print(f"  Profit Factor:   {momentum_c.get('profit_factor')}")
        print(f"  Sharpe:          {momentum_c.get('sharpe_ratio')}")
        print(f"  Skipped:         {momentum_tickers_skipped}/{len(universe)}")

    # --- Save combined results ---
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'backtest_results_holistic')
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    combined = {
        'meta': {
            'universe_size': len(universe),
            'universe': universe,
            'sample_seed': args.seed,
            'simfin_total_coverage': total_coverage,
            'momentum_tickers_processed': momentum_tickers_processed,
            'momentum_tickers_skipped': momentum_tickers_skipped,
            'mr_tickers_skipped': len(mr_skipped),
            'mr_skipped_list': mr_skipped,
            'start': args.start,
            'end': args.end,
            'scan_interval': args.scan_interval,
            'timestamp': datetime.now().isoformat(),
        },
        'momentum_config_c': momentum_c,
        'mr': mr_metrics,
    }

    result_path = os.path.join(output_dir, f'survivorship_free_{timestamp}.json')
    with open(result_path, 'w') as f:
        json.dump(combined, f, indent=2, default=str)

    print(f"\n  Combined results saved to: {result_path}")
    print(f"{'=' * 70}\n")

    return combined


if __name__ == '__main__':
    main()
