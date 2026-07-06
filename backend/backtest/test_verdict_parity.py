"""
JS <-> Python Verdict Parity Grid Test — Day 78 (Fable Remediation Task 2.4)

Verdict logic exists twice: categoricalAssessment.js (live truth, what ships
to users) and categorical_engine.py (the version that was actually
backtested). Parity was previously held by only 5 hand-written vectors in
categorical_engine.py's _verify_parity() — nowhere near enough to cover a
9-rule verdict tree across 3 holding periods.

This script:
  1. Generates a grid of inputs (~thousands of combos, cheap pure functions).
  2. Runs every combo through categorical_engine.run_assessment() (Python).
  3. Invokes verdict_grid.mjs, which runs the SAME grid through
     categoricalAssessment.js (JS) via Node's native ESM loader.
  4. Compares row-by-row. Reports every mismatch — does NOT auto-fix
     anything. Per the remediation plan: every mismatch is a real bug in one
     of the two implementations, and must be triaged before either side is
     changed.

Usage:
    python backend/backtest/test_verdict_parity.py
"""

import os
import sys
import json
import subprocess
from itertools import product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from categorical_engine import run_assessment

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'verdict_grid_inputs.json')
PY_OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'verdict_grid_py_output.json')
JS_OUTPUT_PATH = os.path.join(REPO_ROOT, 'frontend', 'scripts', 'verdict_grid_js_output.json')
JS_SCRIPT_PATH = os.path.join(REPO_ROOT, 'frontend', 'scripts', 'verdict_grid.mjs')

# ─── Grid Definition (per Fable Remediation Plan Task 2.4) ──────────────────

TT_VALUES = [3, 5, 6, 7, 8]
RSI_VALUES = [25, 45, 55, 65, 75, 85]
RS_VALUES = [0.7, 0.95, 1.0, 1.05, 1.2]
ADX_VALUES = [15, 22, 28]
VIX_VALUES = [15, 25, 35, None]
SPY_ABOVE_VALUES = [True, False]
SPY_DECLINING_VALUES = [True, False]
HOLDING_PERIODS = ['quick', 'standard', 'position']

FUNDAMENTAL_SETS = {
    'strong': {'roe': 20, 'revenue_growth': 15, 'debt_equity': 0.5},
    'decent': {'roe': 10, 'revenue_growth': 5, 'debt_equity': 1.5},
    'weak': {'roe': 5, 'revenue_growth': -5, 'debt_equity': 3.0},
    'all_none': {'roe': None, 'revenue_growth': None, 'debt_equity': None},
}


def generate_grid():
    """Full Cartesian product of all dimensions. Returns list of input dicts."""
    grid = []
    for tt, rsi, rs, adx, vix, spy_above, spy_declining, fund_key, hp in product(
        TT_VALUES, RSI_VALUES, RS_VALUES, ADX_VALUES, VIX_VALUES,
        SPY_ABOVE_VALUES, SPY_DECLINING_VALUES, FUNDAMENTAL_SETS.keys(), HOLDING_PERIODS
    ):
        fund = FUNDAMENTAL_SETS[fund_key]
        grid.append({
            'tt': tt, 'rsi': rsi, 'rs': rs, 'adx': adx, 'vix': vix,
            'spy_above': spy_above, 'spy_declining': spy_declining,
            'fund_key': fund_key,
            'roe': fund['roe'], 'revenue_growth': fund['revenue_growth'], 'debt_equity': fund['debt_equity'],
            'holding_period': hp,
        })
    return grid


def run_python_side(grid):
    """Run every combo through categorical_engine.run_assessment()."""
    results = []
    for row in grid:
        result = run_assessment(
            trend_template_score=row['tt'],
            rsi=row['rsi'],
            rs_52w=row['rs'],
            adx=row['adx'],
            vix=row['vix'],
            spy_above_200sma=row['spy_above'],
            spy_50sma_declining=row['spy_declining'],
            roe=row['roe'],
            revenue_growth=row['revenue_growth'],
            debt_equity=row['debt_equity'],
            eps_growth=None,
            holding_period=row['holding_period'],
            # rs_blended intentionally omitted — disabled for verdicts (Tier 2B)
        )
        results.append({
            'technical': result['technical']['assessment'],
            'fundamental': result['fundamental']['assessment'],
            'risk_macro': result['risk_macro']['assessment'],
            'verdict': result['verdict']['verdict'],
        })
    return results


def run_js_side(grid):
    """Write inputs to disk, invoke verdict_grid.mjs, read its output back."""
    with open(INPUTS_PATH, 'w') as f:
        json.dump(grid, f)

    print(f"  Invoking {JS_SCRIPT_PATH} on {len(grid)} combos...")
    proc = subprocess.run(
        ['node', JS_SCRIPT_PATH, INPUTS_PATH, JS_OUTPUT_PATH],
        capture_output=True, text=True, cwd=os.path.dirname(JS_SCRIPT_PATH),
    )
    if proc.returncode != 0:
        print("  JS SIDE FAILED:")
        print(proc.stdout)
        print(proc.stderr)
        raise RuntimeError("verdict_grid.mjs failed — see output above")

    with open(JS_OUTPUT_PATH) as f:
        return json.load(f)


def compare(grid, py_results, js_results):
    """Row-by-row comparison. Returns list of mismatch dicts."""
    mismatches = []
    field_mismatch_counts = {'technical': 0, 'fundamental': 0, 'risk_macro': 0, 'verdict': 0}

    for i, (inputs, py, js) in enumerate(zip(grid, py_results, js_results)):
        row_mismatches = {}
        for field in ('technical', 'fundamental', 'risk_macro', 'verdict'):
            if py[field] != js[field]:
                row_mismatches[field] = {'python': py[field], 'js': js[field]}
                field_mismatch_counts[field] += 1
        if row_mismatches:
            mismatches.append({'index': i, 'inputs': inputs, 'mismatches': row_mismatches})

    return mismatches, field_mismatch_counts


def main():
    print("=" * 70)
    print("  JS <-> Python Verdict Parity Grid Test (Day 78, Task 2.4)")
    print("=" * 70)

    grid = generate_grid()
    print(f"\n  Grid size: {len(grid)} combinations")

    print("\n  Running Python side (categorical_engine.py)...")
    py_results = run_python_side(grid)

    with open(PY_OUTPUT_PATH, 'w') as f:
        json.dump(py_results, f)

    print("\n  Running JS side (categoricalAssessment.js via Node)...")
    js_results = run_js_side(grid)

    if len(js_results) != len(py_results):
        print(f"\n  FATAL: result count mismatch — Python {len(py_results)}, JS {len(js_results)}")
        sys.exit(1)

    print("\n  Comparing...")
    mismatches, field_counts = compare(grid, py_results, js_results)

    print(f"\n{'=' * 70}")
    print(f"  RESULTS")
    print(f"{'=' * 70}")
    print(f"  Total combos:     {len(grid)}")
    print(f"  Matching rows:    {len(grid) - len(mismatches)}")
    print(f"  Mismatched rows:  {len(mismatches)}")
    print(f"\n  Mismatches by field:")
    for field, count in field_counts.items():
        print(f"    {field:12s}: {count}")

    if mismatches:
        print(f"\n  First 20 mismatches (of {len(mismatches)}):")
        for m in mismatches[:20]:
            print(f"\n  Row {m['index']}: {m['inputs']}")
            for field, diff in m['mismatches'].items():
                print(f"    {field}: python={diff['python']!r}  js={diff['js']!r}")

        mismatch_report_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'verdict_parity_mismatches.json'
        )
        with open(mismatch_report_path, 'w') as f:
            json.dump(mismatches, f, indent=2)
        print(f"\n  Full mismatch list ({len(mismatches)} rows) saved to:")
        print(f"    {mismatch_report_path}")
        print(f"\n  ACTION REQUIRED: report these to the user before fixing anything.")
        print(f"  Each mismatch is a real bug in one implementation — do not guess which.")
    else:
        print(f"\n  ALL {len(grid)} COMBINATIONS MATCH. JS and Python are in parity.")

    print(f"{'=' * 70}\n")

    return len(mismatches) == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
