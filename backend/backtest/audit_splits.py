"""
Split sweep (Day 126; plan docs/claude/design/SPLIT_MECHANISM_PLAN_DAY126.md §2.4/§9 item 11).
Reads EVERY cached price history with the side-effect-free reader (no provider calls, no cache events), lists each one-day close move over 40%,
and says whether it looks like a split (exact whole-number factor), is covered by backend/reference/known_splits.json, or matches a split IBKR
reported (data_audit_vs_ibkr_*.json). Anything that looks like a split and is not covered needs a source check before it enters the table.
Run: cd backend && venv/bin/python backtest/audit_splits.py     Writes docs/test/Splits_<date>/REPORT.md
"""
import datetime, glob, json, os, sqlite3, sys
BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
sys.path.insert(0, BACKEND)
import cache_manager, data_quality, split_adjust

def cached_symbols():
    con = sqlite3.connect(os.path.join(BACKEND, 'data', 'cache.db'))
    try:
        return [r[0] for r in con.execute('SELECT ticker FROM ohlcv_cache ORDER BY ticker')]
    finally:
        con.close()

def ibkr_splits():
    out = {}
    for path in sorted(glob.glob(os.path.join(BACKEND, 'validation_results', 'data_audit_vs_ibkr_*.json')))[-1:]:
        for r in json.load(open(path)):
            for s in r.get('ibkr_splits') or []:
                out.setdefault(r['symbol'], []).append(f"{s['date']} x{s['value']:g}")
    return out

def main():
    syms, ib, rows, empty = cached_symbols(), ibkr_splits(), [], []
    for t in syms:
        df, meta = cache_manager.read_ohlcv_entry(t)
        if df is None or len(df) < 2:
            empty.append(t); continue
        table_rows = split_adjust.rows_for(t)[0]
        for d, v in data_quality.jump_moves(df).items():
            k = split_adjust.possible_split_k(1 + v)
            covered = str(d.date()) in {str(split_adjust.classify(df, r).get('bar_date'))[:10] for r in table_rows}
            rows.append((t, str(d.date()), v * 100, k, covered, len(df)))
    needs = [r for r in rows if r[3] and not r[4]]
    out = os.path.join(REPO, 'docs', 'test', f'Splits_{datetime.date.today():%Y%m%d}'); os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'REPORT.md'), 'w') as fh:
        fh.write(f'# Split sweep\n\nCached histories read: {len(syms) - len(empty)} of {len(syms)} (side-effect-free reader). One-day moves over 40%: {len(rows)}. '
                 f'Look like a split and NOT in known_splits.json: **{len(needs)}**.\n\n')
        fh.write('| Ticker | Date | Move | Looks like | In table | Bars |\n|---|---|---|---|---|---|\n')
        for t, d, pct, k, cov, n in rows:
            kind = '' if not k else (f'{k}-for-1' if k > 0 else f'1-for-{-k}')
            fh.write(f'| {t} | {d} | {pct:+.1f}% | {kind or "a real move (not an exact factor)"} | {"yes" if cov else "no"} | {n} |\n')
        fh.write('\nIBKR-reported splits in the last year (the providers had already adjusted these unless listed above): '
                 + ('; '.join(f'{s}: {", ".join(v)}' for s, v in sorted(ib.items())) or 'none') + '\n')
        if empty:
            fh.write(f'\nNo usable cached history: {", ".join(empty)}\n')
    print(f'{len(syms)} cached, {len(rows)} big moves, {len(needs)} split-like not in the table. Report: {out}/REPORT.md')
    for r in needs: print('  NEEDS A SOURCE CHECK:', r[:4])

if __name__ == '__main__':
    main()
