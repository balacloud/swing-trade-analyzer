"""
HUB-65 Mean-Reversion Backtest — Day 97

Runs the existing, UNCHANGED Connors RSI(2) MR engine (mean_reversion.py /
mr_simulator.py's backtest_mr_strategy()) against the curated HUB_UNIVERSE
watchlist (backend/mean_reversion.py) instead of DEFAULT_MR_UNIVERSE or the
survivorship-free random sample. No new trading rule — same gate, different
universe. See docs/claude/design/ (Day 97 plan) for the full design writeup.

============================================================================
IMPORTANT — READ BEFORE QUOTING ANY NUMBER THIS SCRIPT PRINTS:

This backtest is SELECTION-BIASED BY CONSTRUCTION and its results are NOT
comparable to backtest_survivorship_free.py's random-400-ticker baseline
(PF 1.16, Sharpe 1.30). HUB_UNIVERSE is a 2026 watchlist of names picked
BECAUSE they already look structurally strong (semis, uranium/nuclear,
momentum growth) — backtesting a trend-filtered dip-buy strategy over
2020-2025 on names selected in 2026 for having trended up is a milder
version of the exact survivorship bias that knocked the original hand-picked
60-ticker momentum backtest down once corrected (PF 1.61 -> 1.40, Day 79).

Treat this script's output as "how would MR have looked on today's already-
identified winners" — useful for sizing expectations on THIS specific
watchlist, not evidence of a clean, generalizable edge.
============================================================================

Usage:
    python backend/backtest/backtest_hub_mr.py                  # full 64 tickers
    python backend/backtest/backtest_hub_mr.py --smoke-test      # first 5 tickers only
"""
import os
import sys
import json
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from backtest_survivorship_free import run_mr_on_universe, _translate_mr_trades_for_metrics
from metrics import compute_metrics
from mean_reversion import HUB_UNIVERSE, HUB_THEME_MAP


def _theme_breakdown(trades):
    """
    Per-theme trade count + PF, computed here (never in the frozen
    metrics.py) — with ~4 dominant themes in HUB_UNIVERSE (semis,
    uranium/nuclear, fintech, China-EV), a single sector-wide event (e.g. a
    semis selloff tripping RSI(2)<10 across ANET/QCOM/AMAT/LRCX/KLAC/ASML/
    LSCC/SMH/SOXX in the same week) would otherwise silently multi-count as
    independent wins/losses in the headline PF.
    """
    by_theme = {}
    for t in trades:
        theme = HUB_THEME_MAP.get(t.get('ticker'), 'Unknown')
        by_theme.setdefault(theme, []).append(t)

    breakdown = {}
    for theme, theme_trades in sorted(by_theme.items(), key=lambda kv: -len(kv[1])):
        gross_win = sum(t.get('pnl_pct_net', t.get('pnl_pct', 0)) for t in theme_trades
                         if t.get('pnl_pct_net', t.get('pnl_pct', 0)) > 0)
        gross_loss = abs(sum(t.get('pnl_pct_net', t.get('pnl_pct', 0)) for t in theme_trades
                              if t.get('pnl_pct_net', t.get('pnl_pct', 0)) < 0))
        pf = round(gross_win / gross_loss, 3) if gross_loss > 0 else (float('inf') if gross_win > 0 else 0)
        breakdown[theme] = {'trades': len(theme_trades), 'profit_factor': pf}
    return breakdown


def _distinct_entry_months(trades):
    """
    Same grouping key metrics.py's own _compute_block_bootstrap_pvalue()
    uses internally (entry_date[:7], 'YYYY-MM') — surfaced here so the
    reader can judge how much the block-bootstrap p-value should be trusted.
    64 concentrated names produce fewer distinct entry-months than the
    survivorship-free run's 400 diversified names, so the same-looking
    p-value is less trustworthy here even when the number itself looks fine.
    """
    months = set()
    for t in trades:
        entry = t.get('entry_date')
        months.add(entry[:7] if entry else 'unknown')
    return sorted(months)


def main():
    parser = argparse.ArgumentParser(description='HUB-65 Mean-Reversion Backtest (Day 97)')
    parser.add_argument('--smoke-test', action='store_true', help='Run on first 5 tickers only')
    parser.add_argument('--start', default='2020-01-01')
    parser.add_argument('--end', default='2025-12-31')
    args = parser.parse_args()

    universe = HUB_UNIVERSE[:5] if args.smoke_test else HUB_UNIVERSE

    print("=" * 70)
    print("  HUB-65 MEAN-REVERSION BACKTEST (Day 97)")
    print("  *** SELECTION-BIASED — see this file's module docstring ***")
    print("=" * 70)
    print(f"\n  Universe: {len(universe)} tickers"
          f"{' (SMOKE TEST — first 5 only)' if args.smoke_test else ''}")

    trades, skipped = run_mr_on_universe(universe, args.start, args.end)
    metrics = compute_metrics(_translate_mr_trades_for_metrics(trades))
    theme_breakdown = _theme_breakdown(trades)
    entry_months = _distinct_entry_months(trades)

    print(f"\n{'=' * 70}\n  RESULTS\n{'=' * 70}")
    print(f"  Total trades:       {metrics['total_trades']}")
    print(f"  Win rate:           {metrics['win_rate']}%")
    print(f"  Profit Factor:      {metrics['profit_factor']}")
    print(f"  Sharpe:             {metrics['sharpe_ratio']}")
    print(f"  Block-bootstrap p:  {metrics.get('t_pvalue_block_bootstrap')}"
          f"  (from {len(entry_months)} distinct entry-months — fewer blocks"
          f" than the survivorship-free run's 400-ticker sample, so trust"
          f" this p-value less than the number alone suggests)")
    print(f"  Skipped tickers:    {len(skipped)}/{len(universe)} -> {skipped}")

    print(f"\n{'=' * 70}\n  PER-THEME BREAKDOWN (watch for one theme dominating the headline PF)\n{'=' * 70}")
    for theme, stats in theme_breakdown.items():
        print(f"  {theme:<20} {stats['trades']:>4} trades   PF {stats['profit_factor']}")

    print(f"\n  *** REMINDER: this universe was hand-picked in 2026 because these names")
    print(f"      already looked strong — NOT comparable to the survivorship-free")
    print(f"      random-400-ticker baseline (PF 1.16, Sharpe 1.30). Read as an upper")
    print(f"      bound on this specific watchlist, not a generalizable edge. ***\n")

    output_dir = os.path.join(os.path.dirname(__file__), '..', 'backtest_results_holistic')
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    result_path = os.path.join(output_dir, f'hub_mr_{timestamp}.json')

    with open(result_path, 'w') as f:
        json.dump({
            'meta': {
                'universe_size': len(universe),
                'universe': universe,
                'smoke_test': args.smoke_test,
                'skipped': skipped,
                'start': args.start,
                'end': args.end,
                'distinct_entry_months': entry_months,
                'timestamp': datetime.now().isoformat(),
                'caveat': (
                    'SELECTION-BIASED: HUB_UNIVERSE is a hand-picked 2026 watchlist of '
                    'names chosen because they already looked structurally strong. This '
                    'result is NOT comparable to backtest_survivorship_free.py\'s random-'
                    '400-ticker baseline (PF 1.16, Sharpe 1.30). Treat as an upper bound '
                    'on this specific watchlist, not a generalizable edge.'
                ),
            },
            'metrics': metrics,
            'theme_breakdown': theme_breakdown,
        }, f, indent=2, default=str)

    print(f"  Results saved to: {result_path}")
    print(f"{'=' * 70}\n")

    return metrics


if __name__ == '__main__':
    main()
