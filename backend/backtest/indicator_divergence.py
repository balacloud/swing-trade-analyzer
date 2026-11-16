"""
How far apart are the ATR and RSI implementations on real bars? (Day 126; plan §3.4)
Reads the golden snapshot (no network). Run: venv/bin/python backtest/indicator_divergence.py [snapshot_name]
Prints a 3-line summary, writes docs/test/Indicators_20261114/REPORT.md with per-ticker numbers.
"""
import json, os, sys, statistics as st
BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
name = sys.argv[1] if len(sys.argv) > 1 else 'after'
snap = json.load(open(os.path.join(BACKEND, 'validation_results', f'indicator_golden_{name}.json')))
rows, atr_js, atr_paper, atr_leg, rsi = [], [], [], [], []
for sym in sorted(snap['frames']):
    j, p = snap['js'][sym], snap['python'][sym]
    live = p['atr_simple_sr_live']
    if not live:
        continue
    d_js = (j['atr14'] / live - 1) * 100 if j['atr14'] else None
    d_pa = (p['atr_trade_simulator_51'] / live - 1) * 100 if p['atr_trade_simulator_51'] else None
    d_lg = (p['atr_legacy_260'] / live - 1) * 100 if p['atr_legacy_260'] else None
    d_rs = (j['rsi14'] - p['rsi14_backend']) if j['rsi14'] is not None and p['rsi14_backend'] is not None else None
    rows.append((sym, snap['frames'][sym]['bars'], d_js, d_pa, d_lg, d_rs))
    if d_js is not None: atr_js.append(abs(d_js))
    if d_pa is not None: atr_paper.append(abs(d_pa))
    if d_lg is not None: atr_leg.append(abs(d_lg))
    if d_rs is not None: rsi.append(abs(d_rs))
f = lambda x, n=2: '' if x is None else f'{x:+.{n}f}'
summary = [
    f'ATR: the JS simple-mean copy (no consumer) is median {st.median(atr_js):.1f}% / max {max(atr_js):.1f}% away from the live Wilder ATR.',
    f'ATR: the paper-trading stop ATR (51-bar window) is median {st.median(atr_paper):.2f}% / max {max(atr_paper):.2f}% away from it.',
    f'RSI: JS (drives the verdict) vs backend RSI differ by at most {max(rsi):.2f} points at the last bar across {len(rsi)} tickers.',
]
out = os.path.join(REPO, 'docs', 'test', 'Indicators_20261114'); os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'REPORT.md'), 'w') as fh:
    fh.write('# Indicator divergence (Day 126)\n\nSource: `backend/validation_results/indicator_golden_%s.json` (saved audit frames, no network).\n\n' % name)
    fh.write('\n'.join(f'- {s}' for s in summary) + '\n\n| Ticker | Bars | ATR JS vs live % | ATR paper-51 vs live % | ATR legacy vs live % | RSI JS - backend |\n|---|---|---|---|---|---|\n')
    for r in rows:
        fh.write(f'| {r[0]} | {r[1]} | {f(r[2])} | {f(r[3])} | {f(r[4], 3)} | {f(r[5], 2)} |\n')
print('\n'.join(summary)); print('report:', os.path.join(out, 'REPORT.md'))
