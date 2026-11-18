"""
Old-vs-new support/resistance table (Day 126, one-off).
Plan: docs/claude/design/SIMPLE_SR_PLAN_DAY125.md §4 + §8 #5.

Asks the RUNNING backend's /api/sr/<t>?engine=legacy and ?engine=simple, so both
columns come from the route's own arithmetic (since Day 127 the Buy can be the last close when it is inside the support zone, so a re-run is not comparable with the Day-126 table) (sr_plan.trade_plan), not a second
copy. The only logic here is the Simple Checklist's criteria 3 and 4, copied
from frontend/src/utils/simplifiedScoring.js (same arithmetic, one-off, for
this table only). That checklist was removed Day 126, so these two columns are
historical: they show what the switch would have done to it:
  3 Setup: stop % below entry <= 7 (cap >= $10B) / 9 (>= $2B) / 10 (smaller
           or unknown, e.g. ETFs); no entry -> fail; entry but no stop -> fail.
  4 R:R:   riskReward >= 2.0 passes (1.5-2.0 "acceptable" still fails).

Writes:
  docs/claude/design/SIMPLE_SR_COMPARISON_DAY126.md  (table for the user)
  <out_dir>/sr_compare.json                          (data for the review page)

Run (backend must be up on :5001):
  cd backend && venv/bin/python backtest/compare_sr_engines.py --out <dir>
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime

import requests

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BACKEND)

from market_time import drop_forming_bar  # noqa: E402

API = 'http://localhost:5001/api'
REPO = os.path.dirname(BACKEND)
DOC = os.path.join(REPO, 'docs', 'claude', 'design', 'SIMPLE_SR_COMPARISON_DAY126.md')

# 5 page-checker tickers + 25 across sectors, price levels and volatility.
# ETFs: SMH SPY QQQ XLE IWM. Near highs: AAPL WMT COST. Falling: UNH NKE INTC.
# Cheap/volatile: RIVN SOFI F PLTR.
TICKERS = ['AAPL', 'NVDA', 'SMH', 'JPM', 'RIVN',
           'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'AVGO', 'COST', 'WMT', 'KO', 'XOM',
           'UNH', 'LLY', 'PFE', 'BA', 'CAT', 'HD', 'NKE', 'INTC', 'PLTR', 'SOFI',
           'F', 'SPY', 'QQQ', 'XLE', 'IWM']


def max_stop_pct(cap):
    if cap is None:
        return 10
    return 7 if cap >= 10e9 else 9 if cap >= 2e9 else 10


def criteria(sr, cap):
    """simplifiedScoring.js criteria 3 and 4 on one /api/sr payload."""
    cap_max = max_stop_pct(cap)
    entry, stop = sr.get('suggestedEntry'), sr.get('suggestedStop')
    if entry and stop:
        stop_pct = (entry - stop) / entry * 100
        c3 = 0 < stop_pct <= cap_max
    elif entry and stop is None:
        stop_pct, c3 = None, False
    elif sr.get('support'):
        nearest = max(sr['support'])
        stop_pct = (sr['currentPrice'] - nearest) / sr['currentPrice'] * 100
        c3 = 0 < stop_pct <= cap_max
    else:
        stop_pct, c3 = None, False
    rr = sr.get('riskReward')
    c4 = rr is not None and rr >= 2.0
    return {'stopPct': stop_pct, 'capMax': cap_max, 'c3': c3, 'rr': rr, 'c4': c4}


def nearest_info(sr):
    """What the Trade Setup rows would show for each engine."""
    m = sr.get('meta') or {}
    price = sr['currentPrice']
    out = {}
    if m.get('engine') == 'simple':
        for side in ('support', 'resistance'):
            z = next((z for z in m.get('zones', []) if z['nearest'] and z['side'] == side), None)
            out[side] = None if z is None else {
                'low': z['low'], 'high': z['high'], 'swings': z['swings'],
                'inside': z['insideZone'], 'widthPct': (z['high'] - z['low']) / price * 100}
        out['zonesInWindow'] = len(m.get('zones', []))
    else:
        scores = m.get('levelScores') or {}
        cmap = ((m.get('mtf') or {}).get('confluence_map')) or {}
        for side, arr, fn in (('support', sr.get('support') or [], max), ('resistance', sr.get('resistance') or [], min)):
            if not arr:
                out[side] = None
                continue
            lv = fn(arr)
            key = f'{lv:.2f}'
            out[side] = {'low': lv * 0.995, 'high': lv * 1.005, 'daysNear': scores.get(key),
                         'projected': m.get('supportProjected' if side == 'support' else 'resistanceProjected') is True}
        out['zonesInWindow'] = len(sr.get('support') or []) + len(sr.get('resistance') or [])
    return out


def market_caps(tickers):
    """All caps in one TradingView request (US listings; largest if a symbol
    is on several). yfinance fast_info returned None for all 30 under rate
    limiting without raising, which silently put every stock on the 10% tier.
    Every missing cap is printed; ETFs legitimately have none (the app's
    Simple Checklist puts them on the 10% tier too)."""
    from tradingview_screener import Query, col
    _, df = (Query().select('name', 'market_cap_basic', 'exchange')
             .where(col('name').isin(list(tickers)), col('exchange').isin(['NASDAQ', 'NYSE', 'AMEX']))
             .limit(200).get_scanner_data())
    caps = {}
    for _, row in df.iterrows():
        v = row['market_cap_basic']
        if v == v and v is not None:  # not NaN
            caps[row['name']] = max(caps.get(row['name'], 0), float(v))
    for t in tickers:
        if t not in caps:
            print(f'   ⚠️ {t}: no market cap (ETF or lookup miss) -> 10% stop tier, as in the app')
    return caps


def ohlc_for_page(t):
    """Completed daily bars, last 252, for the review page's small chart."""
    from providers import get_data_provider
    hist = get_data_provider().get_ohlcv(t, '2y')
    hist.columns = [c.lower() for c in hist.columns]
    hist, _ = drop_forming_bar(hist)
    hist = hist[['high', 'low', 'close']].dropna().tail(252)  # same rows simple_sr drops (logged there)
    return {'dates': [str(d.date()) for d in hist.index],
            'high': [round(float(x), 2) for x in hist['high']],
            'low': [round(float(x), 2) for x in hist['low']],
            'close': [round(float(x), 2) for x in hist['close']]}


def fmt(x, nd=2, pre='$'):
    return '—' if x is None else f'{pre}{x:,.{nd}f}'


def zone_txt(z, engine):
    if z is None:
        return 'none'
    rng = f"{fmt(z['low'])}–{fmt(z['high'])}"
    if engine == 'simple':
        bits = [f"{z['swings']}×", 'inside' if z['inside'] else '']
    else:
        bits = [f"{z['daysNear']}d" if z.get('daysNear') is not None else '',
                'PROJECTED' if z.get('projected') else '']
    return rng + ' ' + ' '.join(b for b in bits if b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True, help='folder for sr_compare.json')
    ap.add_argument('--tickers', nargs='*', default=TICKERS)
    ap.add_argument('--from-json', action='store_true',
                    help='rebuild caps, criteria and the table from <out>/sr_compare.json without calling /api/sr again')
    args = ap.parse_args()

    if args.from_json:
        saved = json.load(open(os.path.join(args.out, 'sr_compare.json')))
        rows, errors = saved['rows'], saved['errors']
        caps = market_caps([r['ticker'] for r in rows])
        for r in rows:
            r['cap'] = caps.get(r['ticker'])
            for eng in ('legacy', 'simple'):
                r[eng + 'Crit'] = criteria(r[eng], r['cap'])
        report(rows, errors, args.out, saved['generated'])
        return

    caps = market_caps(args.tickers)
    rows, errors = [], []
    for t in args.tickers:
        rec = {'ticker': t}
        try:
            for eng in ('legacy', 'simple'):
                r = requests.get(f'{API}/sr/{t}', params={'engine': eng}, timeout=90)
                body = r.json()
                if r.status_code != 200:
                    raise RuntimeError(f"{eng}: HTTP {r.status_code} {body.get('error')} {body.get('message', '')}")
                rec[eng] = body
            rec['cap'] = caps.get(t)
            rec['ohlc'] = ohlc_for_page(t)
        except Exception as e:
            print(f'❌ {t}: {e}')
            errors.append({'ticker': t, 'error': str(e)})
            continue
        for eng in ('legacy', 'simple'):
            rec[eng + 'Crit'] = criteria(rec[eng], rec['cap'])
            rec[eng + 'Near'] = nearest_info(rec[eng])
        rows.append(rec)
        lc, sc = rec['legacyCrit'], rec['simpleCrit']
        print(f"{t:6} old entry {fmt(rec['legacy']['suggestedEntry'])} R:R {lc['rr']}  |  "
              f"new entry {fmt(rec['simple']['suggestedEntry'])} R:R {sc['rr']}")
        time.sleep(0.5)

    generated = datetime.now().isoformat(timespec='minutes')
    os.makedirs(args.out, exist_ok=True)
    slim = [{k: v for k, v in r.items() if k not in ('legacy', 'simple')} |
            {'legacy': {k: r['legacy'][k] for k in ('currentPrice', 'support', 'resistance', 'suggestedEntry',
                                                     'suggestedStop', 'suggestedTarget', 'riskReward', 'method')},
             'simple': {k: r['simple'][k] for k in ('currentPrice', 'support', 'resistance', 'suggestedEntry',
                                                     'suggestedStop', 'suggestedTarget', 'riskReward')}
             | {'zones': r['simple']['meta']['zones'], 'atr': r['simple']['meta']['atr'],
                'nearHigh52w': r['simple']['meta']['nearHigh52w'], 'high52w': r['simple']['meta']['high52w']}}
            for r in rows]
    with open(os.path.join(args.out, 'sr_compare.json'), 'w') as f:
        json.dump({'generated': generated, 'rows': slim, 'errors': errors}, f)
    report(slim, errors, args.out, generated)


def report(rows, errors, out_dir, generated):
    """Markdown table for the user, and the caps/criteria written back into the JSON."""
    with open(os.path.join(out_dir, 'sr_compare.json'), 'w') as f:
        json.dump({'generated': generated, 'rows': rows, 'errors': errors}, f)
    n = len(rows)
    def count(pred):
        return sum(1 for r in rows if pred(r))
    flips3 = [r['ticker'] for r in rows if r['legacyCrit']['c3'] != r['simpleCrit']['c3']]
    flips4 = [r['ticker'] for r in rows if r['legacyCrit']['c4'] != r['simpleCrit']['c4']]
    near_sides = sum(1 for r in rows for s in ('support', 'resistance') if r['simpleNear'][s])
    widths = sorted(r['simpleNear'][s]['widthPct'] for r in rows for s in ('support', 'resistance') if r['simpleNear'][s])
    one_turn = sum(1 for r in rows for s in ('support', 'resistance') if r['simpleNear'][s] and r['simpleNear'][s]['swings'] == 1)
    projected_old = count(lambda r: any(r['legacyNear'][s] and r['legacyNear'][s].get('projected') for s in ('support', 'resistance')))

    L = []
    L.append('# Simple vs old support/resistance — comparison (Day 126)\n')
    L.append(f"Data from {generated.replace('T', ' ')} by `backend/backtest/compare_sr_engines.py` from the live "
             "`/api/sr` route (`?engine=legacy` vs `?engine=simple`). Same buy/stop/target arithmetic for both "
             "(`sr_plan.trade_plan`). Criteria 3/4 = same arithmetic as `simplifiedScoring.js`, one-off.\n")
    L.append('Plan: `SIMPLE_SR_PLAN_DAY125.md`. Common trader rules, **not tested**. The switch is the user\'s decision.\n')
    L.append('## Summary\n')
    L.append(f'- Stocks compared: **{n}**' + (f' ({len(errors)} failed: ' + ', '.join(e["ticker"] for e in errors) + ')' if errors else ''))
    L.append(f'- Checklist #3 (stop within cap) passes: old **{count(lambda r: r["legacyCrit"]["c3"])}**, new **{count(lambda r: r["simpleCrit"]["c3"])}**; changes on {len(flips3)}: {", ".join(flips3) or "none"}')
    L.append(f'- Checklist #4 (R:R ≥ 2) passes: old **{count(lambda r: r["legacyCrit"]["c4"])}**, new **{count(lambda r: r["simpleCrit"]["c4"])}**; changes on {len(flips4)}: {", ".join(flips4) or "none"}')
    L.append(f'- No support shown: old {count(lambda r: not r["legacyNear"]["support"])}, new {count(lambda r: not r["simpleNear"]["support"])}. '
             f'No resistance: old {count(lambda r: not r["legacyNear"]["resistance"])}, new {count(lambda r: not r["simpleNear"]["resistance"])}.')
    L.append(f'- Old engine used a projected (made-up) level on {projected_old} stocks; new engine never does.')
    if widths:
        L.append(f'- New zone width (nearest zones): median {widths[len(widths)//2]:.2f}% of price, widest {widths[-1]:.2f}%.')
    L.append(f'- New nearest zones with only 1 turn: {one_turn} of {near_sides}.')
    L.append('')
    L.append('## Per stock\n')
    L.append('Zone: price range · turns (new) or "near it on N days" (old) · stop % is vs the cap (7/9/10%). ✅/❌ = checklist #3 / #4.\n')
    L.append('| Stock | Price | Engine | Support zone | Resistance zone | Buy | Stop (%/cap) | Target | R:R | #3 | #4 |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for r in rows:
        for eng, label in (('legacy', 'old'), ('simple', 'new')):
            sr, c, nr = r[eng], r[eng + 'Crit'], r[eng + 'Near']
            stop_txt = fmt(sr['suggestedStop']) + (f" ({c['stopPct']:.1f}%/{c['capMax']}%)" if c['stopPct'] is not None else '')
            L.append(f"| {r['ticker'] if eng == 'legacy' else ''} | {fmt(sr['currentPrice']) if eng == 'legacy' else ''} | {label} | "
                     f"{zone_txt(nr['support'], eng)} | {zone_txt(nr['resistance'], eng)} | {fmt(sr['suggestedEntry'])} | {stop_txt} | "
                     f"{fmt(sr['suggestedTarget'])} | {'—' if c['rr'] is None else c['rr']} | {'✅' if c['c3'] else '❌'} | {'✅' if c['c4'] else '❌'} |")
    if errors:
        L.append('\n## Failed\n')
        for e in errors:
            L.append(f"- {e['ticker']}: {e['error']}")
    with open(DOC, 'w') as f:
        f.write('\n'.join(L) + '\n')
    print(f'\nWrote {DOC} and {os.path.join(out_dir, "sr_compare.json")} ({n} ok, {len(errors)} failed)')


if __name__ == '__main__':
    main()
