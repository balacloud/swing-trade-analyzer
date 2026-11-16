"""
Indicator formula tests (Day 126). Plan: docs/claude/design/INDICATOR_FORMULA_AUDIT_PLAN_DAY126.md §3.2.
Run: cd backend && venv/bin/python backtest/test_indicators.py
Independent textbook references written here, compared to the real production functions (Python and, via node, JS).
Also: catalog honesty (names resolve, unique), an inventory test (a new indicator copy must be catalogued), provenance failure state.
"""
import json
import os
import re
import subprocess
import sys

import numpy as np
import pandas as pd

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
sys.path.insert(0, BACKEND)

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
        print(f'FAIL {name} {detail}')


def close(a, b, tol=1e-9):
    return a is not None and b is not None and abs(a - b) <= tol * max(1.0, abs(b))


# ---------------- textbook references (written from the definitions, not from the production code) ----------------
def ref_wilder_atr(h, l, c, n=14):
    # the first bar has no previous close, so its range is high - low (simple_sr.wilder_atr does the same)
    tr = [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, len(c))]
    a = sum(tr[:n]) / n
    for t in tr[n:]:
        a = (a * (n - 1) + t) / n
    return a


def ref_wilder_rsi(c, n=14):
    d = [c[i] - c[i - 1] for i in range(1, len(c))]
    g = [max(x, 0) for x in d]
    lo = [max(-x, 0) for x in d]
    ag, al = sum(g[:n]) / n, sum(lo[:n]) / n
    for i in range(n, len(d)):
        ag = (ag * (n - 1) + g[i]) / n
        al = (al * (n - 1) + lo[i]) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def ref_ema(c, n):
    k = 2 / (n + 1)
    e = c[0]
    for x in c[1:]:
        e = x * k + e * (1 - k)
    return e


def walk(n, seed=1, start=100.0, vol=0.012):
    r = np.random.default_rng(seed)
    c = start * np.exp(np.cumsum(r.normal(0, vol, n)))
    h = c * (1 + np.abs(r.normal(0, .006, n)))
    l = c * (1 - np.abs(r.normal(0, .006, n)))
    v = r.integers(1_000_000, 5_000_000, n).astype(float)
    return pd.DataFrame({'open': c, 'high': h, 'low': l, 'close': c, 'volume': v},
                        index=pd.bdate_range('2025-01-01', periods=n))


# ---------------- 1. Python production vs textbook ----------------
import backend as B
import simple_sr
import mean_reversion
from backtest import trade_simulator

for n, label in [(300, '300 bars'), (100, '100 bars'), (60, '60 bars')]:
    f = walk(n, seed=n)
    h, l, c = f.high.tolist(), f.low.tolist(), f.close.tolist()
    check(f'wilder_atr == textbook ({label})', close(simple_sr.wilder_atr(f), ref_wilder_atr(h, l, c), 1e-9))
    # backend RSI is pandas ewm(adjust=True): same as Wilder up to the seed; only claim a tight match on long histories
    tol = {300: 0.01, 100: 0.1, 60: 1.5}[n]
    check(f'backend RSI ~ textbook ({label}, tol {tol})', abs(B.calculate_rsi(f.close) - ref_wilder_rsi(c)) <= tol,
          f'{B.calculate_rsi(f.close)} vs {ref_wilder_rsi(c)}')

# trade_simulator ATR (paper stops): pandas ewm on a 51-bar window. Pin that it is NOT the same as Wilder on the full history.
f = walk(300, seed=7)
t51 = f.tail(51)
paper = trade_simulator.calculate_atr_at(t51.high, t51.low, t51.close)
live = simple_sr.wilder_atr(f)
check('paper-stop ATR (51-bar ewm) is close to live Wilder but not identical', 0 < abs(paper - live) / live < 0.10, f'{paper} vs {live}')

# ---------------- 2. ADX: backend vs mean_reversion copy differ on tie bars only ----------------
f = walk(300, seed=3)
a1 = B.calculate_adx(f.high, f.low, f.close)
a2 = mean_reversion.calculate_adx(f.high, f.low, f.close).iloc[-1]
a1v = a1['adx'] if isinstance(a1, dict) else a1
check('ADX copies agree on a history with no tie bars', abs(float(a1v) - float(a2)) < 0.01, f'{a1v} vs {a2}')
tie = f.copy()
# make bar 150 a tie: high rises by x and low falls by x
for k in range(270, 290, 2):                      # ten tie bars near the end so the gap is large enough to see after rounding
    tie.iloc[k, tie.columns.get_loc('high')] = tie.high.iloc[k - 1] + 1.0
    tie.iloc[k, tie.columns.get_loc('low')] = tie.low.iloc[k - 1] - 1.0
b1 = B.calculate_adx(tie.high, tie.low, tie.close)
b1v = b1['adx'] if isinstance(b1, dict) else b1
b2 = mean_reversion.calculate_adx(tie.high, tie.low, tie.close).iloc[-1]
check('ADX copies differ when a tie bar exists (pinned, plan D3)', abs(float(b1v) - float(b2)) > 0.05, f'{b1v} vs {b2}')

# ---------------- 3. JS vs textbook, and JS vs Python (real JS via node) ----------------
def run_js(cases):
    p = subprocess.run(['node', os.path.join(REPO, 'frontend', 'scripts', 'indicator_grid.mjs')],
                       input=json.dumps({'cases': cases}), capture_output=True, text=True, cwd=os.path.join(REPO, 'frontend'))
    if p.returncode != 0:
        raise RuntimeError(p.stderr[-300:])
    return json.loads(p.stdout)


def case(id_, f, round2=False):
    r = f.round(2) if round2 else f
    return {'id': id_, 'high': r.high.tolist(), 'low': r.low.tolist(), 'close': r.close.tolist(), 'volume': r.volume.tolist()}


f300 = walk(300, seed=11)
f100 = walk(100, seed=12)
flat = pd.DataFrame({'open': 50.0, 'high': 50.0, 'low': 50.0, 'close': 50.0, 'volume': 1e6}, index=pd.bdate_range('2025-01-01', periods=120))
low_px = walk(260, seed=13, start=0.8, vol=0.03)          # sub-$1 fund, prices rounded to 2 dp like /api/stock sends them
js = run_js([case('a', f300), case('b', f100), case('flat', flat), case('low', low_px, True)])

c300 = f300.close.tolist()
check('JS SMA50 == textbook', close(js['a']['sma50'], float(np.mean(c300[-50:]))))
check('JS SMA200 == textbook', close(js['a']['sma200'], float(np.mean(c300[-200:]))))
check('JS EMA8 == textbook', close(js['a']['ema8'], ref_ema(c300, 8)))
check('JS EMA21 == textbook', close(js['a']['ema21'], ref_ema(c300, 21)))
check('JS RSI14 == textbook Wilder (rounded to 2 dp by the JS)', abs(js['a']['rsi14'] - ref_wilder_rsi(c300)) < 0.006)
check('JS RSI14 == textbook Wilder (100 bars)', abs(js['b']['rsi14'] - ref_wilder_rsi(f100.close.tolist())) < 0.006)
check('JS RSI vs backend RSI within 0.05 on 300 bars', abs(js['a']['rsi14'] - B.calculate_rsi(f300.close)) < 0.05)
check('flat history: JS RSI = 100 (pinned; backend says 50)', js['flat']['rsi14'] == 100 and B.calculate_rsi(flat.close) == 50.0,
      f"{js['flat']['rsi14']} / {B.calculate_rsi(flat.close)}")
check('JS ATR is a SIMPLE mean (dead code, pinned)', close(js['a']['atr14'], float(np.mean([max(f300.high.iloc[i] - f300.low.iloc[i], abs(f300.high.iloc[i] - f300.close.iloc[i - 1]), abs(f300.low.iloc[i] - f300.close.iloc[i - 1])) for i in range(len(f300) - 14, len(f300))]))))
check('JS avgVolume50 includes the last bar', close(js['a']['avgVolume50'], float(f300.volume.tail(50).mean())))
lp = low_px.round(2)
check('sub-$1 fund on 2-dp prices: JS RSI within 0.5 of the unrounded textbook', abs(js['low']['rsi14'] - ref_wilder_rsi(low_px.close.tolist())) < 0.5)
check('getIndicators returns null under 50 bars', run_js([case('s', walk(40, seed=2))])['s']['getIndicators'] is None)

# ---------------- 4. Catalog honesty ----------------
import indicator_catalog as IC
rows = IC.build_indicator_rows()
names = [r['name'] for r in rows]
check('catalog names unique', len(set(names)) == len(names))
check('catalog has 8 rows (decision-fatigue cap)', len(rows) == 8, str(len(rows)))
check('every row has name/source/formula/kind', all(all(r.get(k) for k in ('name', 'source', 'formula', 'kind')) for r in rows))
import importlib
for e in IC.CATALOG:
    for ref in e['computed_in']:
        kind, path, name = ref.split(':', 2) if ref.count(':') == 2 else (None, None, None)
        if kind == 'py':
            try:
                ok = hasattr(importlib.import_module(path), name)
            except Exception:
                ok = False
        elif kind == 'js':
            fp = os.path.join(REPO, path)
            ok = os.path.exists(fp) and re.search(r'export\s+(async\s+)?(function|const)\s+' + re.escape(name) + r'\b', open(fp).read()) is not None
        else:
            ok = False
        check(f'computed_in resolves: {ref}', ok)

# Inventory: any file with an indicator signature must be in the catalog or the frozen-research allowlist.
SIGNATURES = [r'ewm\(\s*alpha\s*=\s*1\s*/', r'def\s+(calculate_)?(rsi|adx|atr)\w*\(', r'function\s+(calculate)?(RSI|ATR|ADX)\w*\(', r'ta\.(atr|rsi|ema|sma)\(']
ALLOWED = {
    # catalogued (see indicator_catalog.py copies)
    'backend/backend.py', 'backend/simple_sr.py', 'backend/support_resistance.py', 'backend/pattern_detection.py', 'backend/mean_reversion.py',
    'backend/backtest/trade_simulator.py', 'frontend/src/utils/technicalIndicators.js', 'frontend/src/utils/rsCalculator.js',
    # frozen research / backtests (results are records; not edited)
    'backend/backtest/gate5_combined.py', 'backend/backtest/nirmal_validation.py', 'backend/backtest/parameter_stability.py',
    'backend/backtest/backtest_holistic.py', 'backend/backtest/backtest_adx_rsi_thresholds.py', 'backend/backtest/backtest_technical.py',
    'backend/backtest/srps_gate0.py', 'backend/backtest/test_indicators.py', 'backend/backtest/indicator_golden.py',
    'backend/backtest/indicator_divergence.py', 'backend/indicator_catalog.py',
    # external
    'pine/sta_breakout_companion.pine', 'docs/claude/design/LEVERAGED_ETF_BOARD.html',
}
found = set()
for root in ('backend', 'frontend/src', 'pine'):
    for dp, dn, fn in os.walk(os.path.join(REPO, root)):
        dn[:] = [d for d in dn if d not in ('venv', 'node_modules', '__pycache__', 'validation_results', 'data', 'backtest_results_holistic')]
        for x in fn:
            if not x.endswith(('.py', '.js', '.jsx', '.pine')):
                continue
            rel = os.path.relpath(os.path.join(dp, x), REPO)
            try:
                txt = open(os.path.join(REPO, rel), errors='ignore').read()
            except OSError:
                continue
            if any(re.search(s, txt) for s in SIGNATURES):
                found.add(rel)
new = sorted(found - ALLOWED)
check('inventory: no uncatalogued indicator file', not new, f'NEW FILES: {new}')

# ---------------- 5. Provenance survives a catalog failure ----------------
import builtins
real_build = IC.build_indicator_rows
IC.build_indicator_rows = lambda: (_ for _ in ()).throw(ValueError('boom'))
blk = B._indicator_block()
IC.build_indicator_rows = real_build
check('catalog failure -> indicators None + reason, no exception', blk['indicators'] is None and 'boom' in (blk['indicators_error'] or ''))
check('catalog ok -> indicators_error None', B._indicator_block()['indicators_error'] is None)

print(f'\n{PASS} passed, {FAIL} failed')
sys.exit(1 if FAIL else 0)
