"""
Data-source audit, step 2: compare every source's history with the broker's (IBKR) truth.
Plan: docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md §3.3 (C1, C3, C5-truth, C7).

Input 1: backend/validation_results/ibkr_truth_<date>.json, written from IBKR MCP calls on the user's own contracts
         (contract ids from the user's watchlists, Golden Rule 58): last 5 daily closes + volumes, three month-end
         closes (IBKR history is split-adjusted), and corporate actions (splits).
Input 2: backend/validation_results/data_audit_cache_<date>.json, the frames step 1 fetched from every source.

Checks per (ticker, source):
  C3  Close accuracy   last 5 closes vs IBKR. PASS <= 0.3%, WARN <= 1%, FAIL above (also catches a wrong instrument or currency).
  C5  Split / level    each IBKR month-end close vs the source's close on that date. Within 6% = adjusted
                       (dividend adjustment explains a few %); a ratio near an IBKR split factor, or off by over 1.5x = unadjusted.
  C7  Volume           source volume / IBKR volume over the last 5 sessions. IBKR counts a subset of trades, so a ratio above 1 is
                       normal (Day 122: Twelve Data and Yahoo are about 1.5-2.2x IBKR). Flag zero volume and ratios above 5 or below 0.8.
Volume is never expected to be equal; the check is plausibility, never equality.

Run: cd backend && venv/bin/python backtest/audit_vs_ibkr.py [--date YYYYMMDD]
Writes docs/test/DataSources_<date>/REPORT_vs_IBKR.md and backend/validation_results/data_audit_vs_ibkr_<date>.json
"""
import argparse
import io
import json
import os

import numpy as np
import pandas as pd

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
import sys  # noqa: E402
sys.path.insert(0, BACKEND)
import data_quality as dq  # noqa: E402  (Day 126: thresholds, worst() and icons live in ONE place)

CLOSE_WARN, CLOSE_FAIL = dq.CLOSE_WARN, dq.CLOSE_FAIL
LEVEL_OK = 0.06            # dividend adjustment + rounding; Tradier is not dividend-adjusted
LEVEL_BAD = 1.5            # a ratio beyond this is a split, not a dividend
VOL_LOW, VOL_HIGH = 0.8, 5.0

CLASS = {'JPM': 'US stock', 'CAT': 'US stock', 'BRK-B': 'US stock', 'SMH': 'US ETF', 'SOXX': 'US ETF', 'GDX': 'US ETF',
         'QPUX': 'US leveraged', 'DRAL': 'US leveraged', 'SPCL': 'US leveraged', 'UBOT': 'US leveraged',
         'RY.TO': 'CA stock', 'CNR.TO': 'CA stock', 'ATD.TO': 'CA stock', 'CSU.TO': 'CA stock',
         'XEQT.TO': 'CA ETF', 'VFV.TO': 'CA ETF', 'HXQ.TO': 'CA ETF', 'XCHP.TO': 'CA ETF',
         'GDXU.TO': 'CA leveraged', 'SOXL.NE': 'CA leveraged', 'AMD.TO': 'CDR', 'AVGO.TO': 'CDR', 'MU.TO': 'CDR', 'SNDK.TO': 'CDR'}
ICON, ORDER, worst = dq.ICON, dq.ORDER, dq.worst


def load_frames(path):
    raw = json.load(open(path))
    out = {}
    for sym, srcs in raw.items():
        out[sym] = {}
        for src, v in srcs.items():
            if isinstance(v, dict):
                f = pd.read_csv(io.StringIO(v['csv']), index_col=0, parse_dates=True)
                f.index = pd.to_datetime(f.index).normalize()
                out[sym][src] = f
    return out


def month_end(ym):
    return pd.Period(ym, 'M').end_time.normalize()


def check_source(sym, src, f, t):
    """Returns {'C3': (level, note), 'C5': ..., 'C7': ...} for one source's frame f against IBKR truth t."""
    res = {}
    dates = pd.to_datetime(t['dates'])
    # C3 closes
    # IBKR marks Canadian and some other contracts "delayed 900s", and its FINAL history bar can then be a 15-minute-old
    # price (SOXL.NE 2026-11-13: history bar 14.10, the user's own watchlist 14.72, which Yahoo 14.69 and EODHD 14.72 match).
    # So the graded check uses the four settled days; the final day is reported and can only WARN.
    settled = [(d, c) for d, c in list(zip(dates, t['close']))[:-1] if d in f.index]
    if len(settled) < 3:
        res['C3'] = ('FAIL', f'only {len(settled)} of 4 settled days present (last bar {f.index[-1].date()})')
    else:
        mx = max(abs(f['close'].loc[d] / c - 1) for d, c in settled)
        lv = 'FAIL' if mx > CLOSE_FAIL else 'WARN' if mx > CLOSE_WARN else 'PASS'
        note = f'max close diff {mx*100:.2f}% over the {len(settled)} settled days'
        last_d, last_c = dates[-1], t['close'][-1]
        if last_d in f.index:
            ld = abs(f['close'].loc[last_d] / last_c - 1)
            note += f'; last day {ld*100:.2f}% (IBKR final history bar can be 15 min stale)'
            if ld > CLOSE_FAIL and lv == 'PASS':
                lv = 'WARN'
        res['C3'] = (lv, note)
    # C5 levels at month-ends (and split proximity)
    def levels(frame):
        notes, lv = [], 'PASS'
        for ym, ib in t['monthly'].items():
            me = month_end(ym)
            sub = frame[frame.index <= me]
            if sub.empty or (me - sub.index[-1]).days > 6:
                notes.append(f'{ym}: no data'); continue
            r = sub['close'].iloc[-1] / ib
            if abs(r - 1) <= LEVEL_OK:
                continue
            flag = 'FAIL' if (r > LEVEL_BAD or r < 1 / LEVEL_BAD) else 'WARN'
            lv = worst([lv, flag])
            notes.append(f'{ym}: {src} {sub["close"].iloc[-1]:.2f} vs IBKR {ib:.2f} (x{r:.2f})')
        return lv, notes
    notes_raw_lv, notes = levels(f)
    lv = notes_raw_lv
    # Day 126 (split mechanism): STA adjusts splits listed in known_splits.json before the app sees prices, so also report what the app sees.
    # The cell's level is the AFTER-STA one (what the user gets); the raw result stays in the note so the audit never hides the provider's defect.
    import split_adjust
    adj, ev = split_adjust.adjust_for_splits(f, sym)
    if any(e.get('applied') for e in ev):
        lv_adj, notes_adj = levels(adj)
        raw_txt = '; '.join(notes) if notes else 'matches'
        notes = [f'raw {src}: {raw_txt}', 'after STA split adjustment (' + ', '.join(e['text'] for e in ev if e.get('applied')) + '): '
                 + ('; '.join(notes_adj) if notes_adj else 'month-end levels match IBKR')]
        lv = lv_adj
    sp = ', '.join(f"{s['date']} x{s['value']:g}" for s in t['splits'])
    first = f.index[0]
    pre = [s for s in t['splits'] if pd.Timestamp(s['date']) > first]
    res['C5'] = (lv, ('; '.join(notes) if notes else 'month-end levels match IBKR (adjusted)') + (f' | IBKR splits in range: {sp}' if pre else ''))
    # C7 volume
    vs = [f['volume'].loc[d] for d in dates if d in f.index]
    vi = [v for d, v in zip(dates, t['volume']) if d in f.index]
    if not vs:
        res['C7'] = ('NA', 'no overlapping days')
    elif sum(vs) == 0:
        res['C7'] = ('FAIL', 'source volume is zero')
    else:
        ratio = sum(vs) / sum(vi)
        res['C7'] = ('WARN' if (ratio > VOL_HIGH or ratio < VOL_LOW) else 'PASS', f'volume {src}/IBKR x{ratio:.2f}')
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default='20261114')
    a = ap.parse_args()
    truth = json.load(open(os.path.join(BACKEND, 'validation_results', f'ibkr_truth_{a.date}.json')))
    frames = load_frames(os.path.join(BACKEND, 'validation_results', f'data_audit_cache_{a.date}.json'))
    rows = []
    for sym, t in truth.items():
        per = {}
        for src, f in frames.get(sym, {}).items():
            per[src] = check_source(sym, src, f, t)
        rows.append({'symbol': sym, 'class': CLASS.get(sym, '?'), 'conid': t['conid'], 'ibkr': t['ibkr_description'],
                     'ibkr_splits': t['splits'], 'per_source': {s: {k: {'level': v[0], 'note': v[1]} for k, v in r.items()} for s, r in per.items()}})
    json.dump(rows, open(os.path.join(BACKEND, 'validation_results', f'data_audit_vs_ibkr_{a.date}.json'), 'w'), indent=1)
    d = os.path.join(REPO, 'docs', 'test', f'DataSources_{a.date}')
    os.makedirs(d, exist_ok=True)
    L = [f'# Data source audit vs IBKR truth ({a.date})\n',
         'Script `backend/backtest/audit_vs_ibkr.py`. Truth: IBKR (user\'s own contracts), last 5 daily closes and volumes, three month-end closes (split-adjusted) and corporate actions. '
         'Sources graded: every source step 1 fetched (Twelve Data, Yahoo, Tradier for US; Yahoo for Canada; EODHD where the free quota allowed).',
         '**C3** close accuracy (last 5 days), **C5** history level vs IBKR month-ends (catches unadjusted splits), **C7** volume plausibility. '
         'Volume is not expected to equal IBKR\'s (it counts a subset of trades); only zero or wildly off volume is flagged.\n',
         '## Matrix (worst result across the sources that can serve the ticker)\n',
         '| Class | Ticker | IBKR splits in the last year | Source | C3 close | C5 level | C7 volume |', '|---|---|---|---|---|---|---|']
    for r in sorted(rows, key=lambda x: (list(dict.fromkeys(CLASS.values())).index(x['class']), x['symbol'])):
        sp = ', '.join(f"{s['date']} ×{s['value']:g}" for s in r['ibkr_splits']) or '—'
        first = True
        for src, c in r['per_source'].items():
            L.append(f"| {r['class'] if first else ''} | {('`'+r['symbol']+'`') if first else ''} | {sp if first else ''} | {src} | "
                     f"{ICON[c['C3']['level']]} | {ICON[c['C5']['level']]} | {ICON[c['C7']['level']]} |")
            first = False
    L.append('\n## Findings (warn and fail), with evidence\n')
    for r in rows:
        items = [(src, k, v) for src, cs in r['per_source'].items() for k, v in cs.items() if v['level'] in ('WARN', 'FAIL')]
        if items:
            L.append(f"**{r['symbol']}** ({r['class']}; IBKR contract {r['conid']}, {r['ibkr']})")
            for src, k, v in items:
                L.append(f"- {ICON[v['level']]} {src} {k}: {v['note']}")
            L.append('')
    L.append('## Volume ratios (source ÷ IBKR, last 5 sessions)\n')
    L.append('| Class | Ticker | ' + ' | '.join(['twelvedata', 'yfinance', 'tradier', 'eodhd']) + ' |')
    L.append('|---|---|---|---|---|---|')
    for r in rows:
        cells = []
        for s in ['twelvedata', 'yfinance', 'tradier', 'eodhd']:
            n = r['per_source'].get(s, {}).get('C7', {}).get('note', '')
            cells.append(n.split('x')[-1] if 'x' in n else '—')
        L.append(f"| {r['class']} | `{r['symbol']}` | " + ' | '.join(cells) + ' |')
    open(os.path.join(d, 'REPORT_vs_IBKR.md'), 'w').write('\n'.join(L) + '\n')
    from datetime import datetime as _dt
    dq.update_audit_reference('vs_ibkr', _dt.now().isoformat(timespec='minutes'), f'docs/test/DataSources_{a.date}/REPORT_vs_IBKR.md',
                              {r['symbol']: [(f'{src} {k}', v['level'], v['note']) for src, cs in r['per_source'].items() for k, v in cs.items()] for r in rows})
    print('Wrote', os.path.join(d, 'REPORT_vs_IBKR.md'))


if __name__ == '__main__':
    main()
