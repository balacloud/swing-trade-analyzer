"""
Golden snapshot of every live indicator number, for a before/after proof (Day 126).
Plan: docs/claude/design/INDICATOR_FORMULA_AUDIT_PLAN_DAY126.md §3.3.

Why: the 86,400-case verdict parity feeds indicators in as INPUTS, so it cannot detect an indicator change. This records what
each indicator implementation returns on FIXED frames (the saved audit cache, never live data) so a later run can assert the
numbers are bit-identical. Frontend values come from the REAL JS code through frontend/scripts/indicator_grid.mjs, fed prices
rounded to 2 dp exactly as /api/stock sends them to the page (backend.py:1105-1110).

Run:
  cd backend && venv/bin/python backtest/indicator_golden.py --snapshot before
  ... make the change ...
  venv/bin/python backtest/indicator_golden.py --snapshot after
  venv/bin/python backtest/indicator_golden.py --compare before after      # exits 1 on any difference
"""
import argparse
import io
import json
import os
import subprocess
import sys

import numpy as np
import pandas as pd

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
sys.path.insert(0, BACKEND)

CACHE = os.path.join(BACKEND, 'validation_results', 'data_audit_cache_20261114.json')
GRID = os.path.join(REPO, 'frontend', 'scripts', 'indicator_grid.mjs')


def out_path(name):
    return os.path.join(BACKEND, 'validation_results', f'indicator_golden_{name}.json')


def load_frames():
    """{symbol: DataFrame(open, high, low, close, volume)}: the first source with data, in a fixed order."""
    raw = json.load(open(CACHE))
    frames = {}
    for sym, srcs in raw.items():
        for src in ('yfinance', 'twelvedata', 'tradier', 'eodhd'):
            v = srcs.get(src)
            if isinstance(v, dict):
                f = pd.read_csv(io.StringIO(v['csv']), index_col=0, parse_dates=True)
                f.index = pd.to_datetime(f.index).normalize()
                f.columns = [c.lower() for c in f.columns]
                frames[sym] = f[['open', 'high', 'low', 'close', 'volume']].astype(float)
                break
    return frames


def num(x):
    """JSON-safe float (None for NaN/None)."""
    if x is None:
        return None
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return None if np.isnan(x) else x


def js_values(frames):
    cases = []
    for sym, f in frames.items():
        r = f.round(2)                                    # what /api/stock sends the page
        r['volume'] = r['volume'].fillna(0)
        r['high'] = r['high'].fillna(r['close'])
        r['low'] = r['low'].fillna(r['close'])
        cases.append({'id': sym, 'high': r['high'].tolist(), 'low': r['low'].tolist(), 'close': r['close'].tolist(), 'volume': r['volume'].tolist()})
    p = subprocess.run(['node', GRID], input=json.dumps({'cases': cases}), capture_output=True, text=True, cwd=os.path.join(REPO, 'frontend'))
    if p.returncode != 0:
        raise RuntimeError(f'indicator_grid.mjs failed: {p.stderr[-400:]}')
    return json.loads(p.stdout)


def python_values(frames):
    import backend as B                                    # live RSI/ADX/OBV
    import simple_sr
    import support_resistance
    import pattern_detection
    import mean_reversion
    from backtest import trade_simulator
    out = {}
    for sym, f in frames.items():
        h, l, c, v = f['high'], f['low'], f['close'], f['volume']
        adx = B.calculate_adx(h, l, c)
        obv = B.calculate_obv(c, v)
        tail51 = f.tail(51)
        out[sym] = {
            'rsi14_backend': num(B.calculate_rsi(c)),
            'adx_backend': adx,
            'obv_backend': obv,
            'rvol_backend': num(v.iloc[-1] / v.tail(50).mean()) if v.tail(50).mean() > 0 else None,
            'atr_simple_sr_live': num(simple_sr.wilder_atr(f[['open', 'high', 'low', 'close', 'volume']])),
            'atr_legacy_260': num(support_resistance._calculate_atr(f.tail(260))),
            'atr_pattern_detection': num(pattern_detection.calculate_atr(h, l, c).iloc[-1]),
            'atr_trade_simulator_51': num(trade_simulator.calculate_atr_at(tail51['high'], tail51['low'], tail51['close'])),
            'rsi2_mean_reversion': num(mean_reversion.calculate_rsi_short(c).iloc[-1]),
            'adx_mean_reversion': num(mean_reversion.calculate_adx(h, l, c).iloc[-1]),
        }
    return out


def snapshot(name):
    frames = load_frames()
    snap = {'frames': {s: {'bars': len(f), 'last': str(f.index[-1].date())} for s, f in frames.items()},
            'js': js_values(frames), 'python': python_values(frames)}
    json.dump(snap, open(out_path(name), 'w'), indent=1, sort_keys=True)
    print(f'snapshot "{name}": {len(frames)} tickers -> {out_path(name)}')


def flatten(d, prefix=''):
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            yield from flatten(v, f'{prefix}{k}.')
        else:
            yield f'{prefix}{k}', v


def compare(a, b):
    A = dict(flatten(json.load(open(out_path(a)))))
    B_ = dict(flatten(json.load(open(out_path(b)))))
    keys = sorted(set(A) | set(B_))
    diffs = [k for k in keys if A.get(k) != B_.get(k)]
    print(f'compared {len(keys)} values: {len(diffs)} differences')
    for k in diffs[:20]:
        print(f'  {k}: {A.get(k)!r} -> {B_.get(k)!r}')
    return 1 if diffs else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--snapshot')
    ap.add_argument('--compare', nargs=2)
    a = ap.parse_args()
    if a.snapshot:
        snapshot(a.snapshot)
    elif a.compare:
        sys.exit(compare(*a.compare))
    else:
        ap.print_help()
