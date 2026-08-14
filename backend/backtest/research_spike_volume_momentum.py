"""
Day 106 Research Spike — Volume Confirmation & Dual Momentum

Backtest-only research question, not a live change: do two additive filters
(Config F = volume confirmation, Config G = absolute/dual momentum) improve
on Config C's own canonical numbers? Runs on the SAME unbiased, survivorship-
free universe/seed as backtest_survivorship_free.py, but as a standalone
script so the existing frozen survivorship-free script is never touched.

Golden Rule 20 discipline (same as the Day 79-80 MR liquidity gate
re-test): both filters were pre-committed BEFORE running this (see
backtest_holistic.py's Config F/G comments) — run once, report the result
honestly regardless of outcome, do not iterate thresholds afterward.

Usage:
    python backend/backtest/research_spike_volume_momentum.py --sample-size 30   # smoke test
    python backend/backtest/research_spike_volume_momentum.py --sample-size 400  # real run
"""

import os
import sys
import json
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backtest_survivorship_free import build_unbiased_universe
from backtest_holistic import run_holistic_backtest


def main():
    parser = argparse.ArgumentParser(description='Day 106 research spike: Config F/G vs. Config C')
    parser.add_argument('--sample-size', type=int, default=400)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--start', default='2020-01-01')
    parser.add_argument('--end', default='2025-12-31')
    parser.add_argument('--scan-interval', type=int, default=2)
    args = parser.parse_args()

    print("=" * 70)
    print("  DAY 106 RESEARCH SPIKE — VOLUME CONFIRMATION & DUAL MOMENTUM")
    print("=" * 70)

    universe, total_coverage = build_unbiased_universe(args.sample_size, args.seed)
    print(f"\n  Universe: {len(universe)} tickers (random sample, seed={args.seed}, "
          f"from {total_coverage} SimFin-covered US tickers — same seed as the "
          f"canonical survivorship-free run)")

    results = run_holistic_backtest(
        universe, start=args.start, end=args.end,
        holding_periods=['standard'], configs=['C', 'F', 'G'],
        scan_interval=args.scan_interval, verbose=True,
    )

    c = results['results'].get('C_standard', {})
    f = results['results'].get('F_standard', {})
    g = results['results'].get('G_standard', {})

    print(f"\n{'=' * 70}")
    print("  COMPARISON — C (baseline) vs. F (+ volume confirm) vs. G (+ dual momentum)")
    print(f"{'=' * 70}")
    header = f"  {'Metric':<18}{'Config C':>14}{'Config F':>14}{'Config G':>14}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for label, key in [
        ('Total trades', 'total_trades'), ('Win rate %', 'win_rate'),
        ('Profit Factor', 'profit_factor'), ('Sharpe', 'sharpe_ratio'),
        ('Avg R-multiple', 'avg_r_multiple'), ('Bootstrap p', 'bootstrap_p_value'),
    ]:
        cv = c.get(key); fv = f.get(key); gv = g.get(key)
        cv = 'n/a' if cv is None else cv
        fv = 'n/a' if fv is None else fv
        gv = 'n/a' if gv is None else gv
        print(f"  {label:<18}{str(cv):>14}{str(fv):>14}{str(gv):>14}")

    # Sanity check per the plan's verification step — F/G are strictly
    # additive filters on top of C, so their trade counts must never exceed C's.
    c_trades = c.get('total_trades', 0)
    f_trades = f.get('total_trades', 0)
    g_trades = g.get('total_trades', 0)
    if f_trades > c_trades or g_trades > c_trades:
        print(f"\n  ⚠ SANITY CHECK FAILED: F ({f_trades}) or G ({g_trades}) trades exceed "
              f"C ({c_trades}) — F/G are supposed to be strict subsets of C. Do not trust "
              f"these numbers until this is investigated.")
    else:
        print(f"\n  ✓ Sanity check passed: F ({f_trades}) and G ({g_trades}) are both "
              f"subsets of C ({c_trades}), as expected for purely additive filters.")

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'backtest_results_holistic')
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_path = os.path.join(output_dir, f'research_spike_volume_momentum_{timestamp}.json')
    with open(result_path, 'w') as fh:
        json.dump({
            'meta': {
                'universe_size': len(universe), 'sample_seed': args.seed,
                'start': args.start, 'end': args.end, 'timestamp': datetime.now().isoformat(),
            },
            'config_c': c, 'config_f': f, 'config_g': g,
        }, fh, indent=2, default=str)
    print(f"\n  Results saved to: {result_path}")
    print(f"{'=' * 70}\n")


if __name__ == '__main__':
    main()
