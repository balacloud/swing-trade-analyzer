"""
Data-source audit, step 1 (truth-free checks).
Plan: docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md  §3.3 / §4 step 1.

For each Wave-1 ticker it fetches the daily history from EVERY source that can serve it, then checks:
  C2  Fresh        last bar is the last completed session (not stale, not a forming bar)
  C4  Integrity    high >= open/close, low <= open/close; share of flat zero-volume bars
  C5  Jumps        every one-day move over 40%: shared by all sources (real move, or unadjusted
                   everywhere: needs IBKR) or only in one source (that source has a split error)
  C6  History      bars and first date; under 252 days flagged; one source shorter than another
  C8  Tab honest   what the Data Sources tab says (source, rows) vs what we measured
  C9  Cross-source last 20 closes of the source STA uses vs each other source; volume ratio
Not here (needs IBKR truth, step 2): C1 identity, C3 close accuracy vs broker, C7 volume vs broker.

"STA uses" = the first source in STA's real chain that returned data: US Twelve Data -> Yahoo -> Tradier;
Canada Yahoo (Twelve Data and Tradier have no Canada).
Rate limits (Golden Rule 25): Twelve Data 8/min, EODHD free 20/day (budget read live), Alpha Vantage not used.
Raw frames are cached on disk, so a re-run costs no provider calls.

Run: cd backend && venv/bin/python backtest/audit_data_sources.py [--eodhd-budget N]
Writes: docs/test/DataSources_<date>/REPORT.md and backend/validation_results/data_audit_<date>.json
"""
import argparse
import json
import os
import io
import sys
import time
import urllib.request
from datetime import datetime

import numpy as np
import pandas as pd

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(BACKEND)
sys.path.insert(0, BACKEND)

from market_time import MARKET_TZ  # noqa: E402
import data_quality as dq  # noqa: E402  (Day 126: the checks live in ONE place, shared with the Data Sources tab)

TODAY = datetime.now(MARKET_TZ)
STAMP = TODAY.strftime('%Y%m%d')
CACHE = os.path.join(BACKEND, 'validation_results', f'data_audit_cache_{STAMP}.json')   # plain JSON + CSV text, no pickle


def configure(date=None, now=None):
    """--date picks the cache/report stamp, --now fixes the clock (expected last session, forming bar). Both exist so a
    saved audit can be replayed on another day with identical results (plan §7.3)."""
    global TODAY, STAMP, CACHE
    if now:
        t = datetime.fromisoformat(now)
        TODAY = t.astimezone(MARKET_TZ) if t.tzinfo else t.replace(tzinfo=MARKET_TZ)
    STAMP = date or TODAY.strftime('%Y%m%d')
    CACHE = os.path.join(BACKEND, 'validation_results', f'data_audit_cache_{STAMP}.json')

CLOSE_WARN, CLOSE_FAIL = dq.CLOSE_WARN, dq.CLOSE_FAIL   # cross-source close disagreement (last 20 sessions)

# class, STA symbol, why it is here
UNIVERSE = [
    ('US stock', 'JPM', ''), ('US stock', 'CAT', ''), ('US stock', 'BRK-B', 'dash symbol'),
    ('US ETF', 'SMH', 'no fundamentals'), ('US ETF', 'SOXX', ''), ('US ETF', 'GDX', ''),
    ('US leveraged', 'QPUX', '1:3 reverse split 2026-03-23'), ('US leveraged', 'DRAL', '~100 days'),
    ('US leveraged', 'SPCL', '~154 days'), ('US leveraged', 'UBOT', 'control'),
    ('CA stock', 'RY.TO', ''), ('CA stock', 'CNR.TO', ''), ('CA stock', 'ATD.TO', ''), ('CA stock', 'CSU.TO', 'CAD 3,000+'),
    ('CA ETF', 'XEQT.TO', ''), ('CA ETF', 'VFV.TO', ''), ('CA ETF', 'HXQ.TO', ''), ('CA ETF', 'XCHP.TO', ''),
    ('CA leveraged', 'GDXU.TO', 'control (3:1 split 2026-05-25)'), ('CA leveraged', 'SOXL.NE', 'known bad: Cboe Canada only'),
    ('CDR', 'AMD.TO', ''), ('CDR', 'AVGO.TO', ''), ('CDR', 'MU.TO', ''), ('CDR', 'SNDK.TO', 'short history'),
]
# Highest value first, for the EODHD free budget (20 calls a day)
EODHD_PRIORITY = ['SOXL.NE', 'GDXU.TO', 'SNDK.TO', 'MU.TO', 'AMD.TO', 'AVGO.TO', 'RY.TO', 'CSU.TO', 'XEQT.TO', 'VFV.TO',
                  'HXQ.TO', 'XCHP.TO', 'CNR.TO', 'ATD.TO']


CLASS_CACHE = os.path.join(BACKEND, 'validation_results', 'instrument_class_cache.json')   # {sym: {quote_type, name}}, so a re-run costs no calls


def lookup_class(sym, dp=None, offline=False):
    """Matrix class for any ticker: Yahoo quote type + name through data_quality.audit_class. Cached on disk.
    No answer (offline, or Yahoo has nothing) -> 'US other' / 'CA other', never a guess at the kind."""
    try:
        cache = json.load(open(CLASS_CACHE))
    except (OSError, ValueError):
        cache = {}
    if sym not in cache and not offline and dp is not None:
        info = None
        for attempt in range(3):          # Yahoo throttles bursts: back off, then try again (a failure is never cached)
            info = dp.get_stock_info(sym)
            if info is not None:
                break
            time.sleep(4.0 * (attempt + 1))
        d = getattr(info, 'data', None) or {}
        if d.get('quoteType'):            # cache real answers only; a failed lookup is retried on the next run
            cache[sym] = {'quote_type': d.get('quoteType'), 'name': d.get('shortName') or d.get('name')}
            json.dump(cache, open(CLASS_CACHE, 'w'), indent=1)
        else:
            print(f'  class lookup {sym}: no answer, left as other')
        time.sleep(1.0)
    c = cache.get(sym) or {}
    return dq.audit_class(sym, c.get('quote_type'), c.get('name'))


def universe_from_file(path, offline=False):
    """[(class, symbol, why)] for every ticker in the file. The curated 24 keep their class and note; the rest are
    classified from Yahoo. Order = file order, duplicates dropped."""
    curated = {s: (c, w) for c, s, w in UNIVERSE}
    dp = None
    if not offline:
        from providers import get_data_provider
        dp = get_data_provider()
    out, seen = [], set()
    for line in open(path):
        sym = line.split('#')[0].strip()
        if not sym or sym in seen:
            continue
        seen.add(sym)
        c, w = curated.get(sym) or (lookup_class(sym, dp, offline), '')
        out.append((c, sym, w))
    return out


def is_ca(sym):
    return sym.endswith(('.TO', '.NE', '.V'))


def norm(df):
    """Lower-case OHLCV, tz-naive sorted index, numeric."""
    h = df.copy()
    h.columns = [str(c).lower() for c in h.columns]
    if getattr(h.index, 'tz', None) is not None:
        h.index = h.index.tz_localize(None)
    h.index = pd.to_datetime(h.index).normalize()
    h = h[~h.index.duplicated(keep='last')].sort_index()
    for c in ('open', 'high', 'low', 'close', 'volume'):
        if c not in h.columns:
            h[c] = np.nan
        h[c] = pd.to_numeric(h[c], errors='coerce')
    return h[['open', 'high', 'low', 'close', 'volume']]


def eodhd_fetch(sym, key):
    base, suf = sym.rsplit('.', 1)
    code = {'TO': 'TO', 'NE': 'NEO', 'V': 'V'}[suf]
    url = f'https://eodhd.com/api/eod/{base}.{code}?api_token={key}&fmt=json&from=2024-11-01'
    with urllib.request.urlopen(url, timeout=40) as r:
        rows = json.loads(r.read().decode())
    df = pd.DataFrame(rows)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    f = df['adjusted_close'] / df['close'].replace(0, np.nan)      # EODHD adjusts for splits AND dividends
    out = pd.DataFrame({'open': df['open'] * f, 'high': df['high'] * f, 'low': df['low'] * f,
                        'close': df['adjusted_close'], 'volume': df['volume']})
    return norm(out)


def load_cache():
    """{sym: {source: DataFrame | error text}} from the JSON cache (frames stored as CSV text)."""
    try:
        raw = json.load(open(CACHE))
    except Exception:
        return {}
    out = {}
    for sym, srcs in raw.items():
        out[sym] = {}
        for src, v in srcs.items():
            out[sym][src] = (pd.read_csv(io.StringIO(v['csv']), index_col=0, parse_dates=True) if isinstance(v, dict) else v)
    return out


def save_cache(cache):
    raw = {sym: {src: ({'csv': v.to_csv()} if isinstance(v, pd.DataFrame) else v) for src, v in srcs.items()}
           for sym, srcs in cache.items()}
    json.dump(raw, open(CACHE, 'w'))


def fetch_all(budget, offline=False):
    """{sym: {source: DataFrame | 'error text'}}, cached on disk."""
    cache = load_cache()
    from providers import get_data_provider
    dp = get_data_provider()
    key = os.environ.get('EODHD_API_KEY', '')
    td_last = [0.0]
    spent = 0
    for cls, sym, _ in UNIVERSE:
        got = cache.setdefault(sym, {})
        plan = []
        if is_ca(sym):
            plan = [('yfinance', sym)]
            if sym in EODHD_PRIORITY[:max(budget, 0)] or 'eodhd' in got:
                plan.append(('eodhd', sym))
        else:
            plan = [('twelvedata', sym.replace('-', '.')), ('yfinance', sym), ('tradier', sym.replace('-', '/'))]
        for src, s in plan:
            if src in got:
                continue
            if offline:        # replay mode: never touch a provider
                continue
            try:
                if src == 'twelvedata':
                    wait = 8.0 - (time.time() - td_last[0])
                    if wait > 0:
                        time.sleep(wait)
                    td_last[0] = time.time()
                    got[src] = norm(dp.twelvedata.get_ohlcv(s, '2y').df)
                elif src == 'yfinance':
                    got[src] = norm(dp.yfinance.get_ohlcv(s, '2y').df); time.sleep(0.3)
                elif src == 'tradier':
                    got[src] = norm(dp.tradier.get_ohlcv(s, '2y').df); time.sleep(0.3)
                elif src == 'eodhd':
                    got[src] = eodhd_fetch(s, key); spent += 1
            except Exception as e:
                got[src] = f'ERROR: {str(e)[:100]}'
            print(f'  {sym:8} {src:10} ' + (f'{len(got[src])} bars' if isinstance(got[src], pd.DataFrame) else got[src]))
        save_cache(cache)
    return cache


jumps = dq.jump_moves     # shared helper (cross-source jump matching)
worst = dq.worst
ORDER = dq.ORDER
ICON = dq.ICON


def chain_sources(sym):
    """Every source that STA's real chain can fall through to for this ticker. Any of them can serve a request
    (Twelve Data is rate-limited all day, so Yahoo and Tradier serve most US fetches), so ALL must be clean."""
    return ['yfinance'] if is_ca(sym) else ['twelvedata', 'yfinance', 'tradier']


def source_checks(name, h, others):
    """C2, C4, C5, C6 for ONE source's frame `h`, compared with the other sources' frames in `others`."""
    res = {}
    f0 = dq.check_history(h, now=TODAY, ticker=name)
    if f0.get('state') != 'ok':
        bad = ('FAIL', f"no usable history: {f0.get('reason')}")
        return {'C2': bad, 'C4': bad, 'C5': bad, 'C6': bad}
    lag = f0['sessions_behind']
    lv2 = dq.level_freshness(lag, f0['forming_bar_dropped'], tolerant=False)
    note = f"last bar {f0['last_date']}, expected {f0['expected_last_date']}"
    if f0['forming_bar_dropped']:
        res['C2'] = ('WARN', 'last bar is today and the session is still open')
    elif lv2 == 'FAIL':
        res['C2'] = ('FAIL', note + f' ({lag} sessions stale)')
    elif lag == 1:
        res['C2'] = ('WARN', note + ' (1 session behind)')
    else:
        res['C2'] = ('PASS', note)
    parts = [f"flat zero-volume {f0['flat_zero_volume_pct']:.0f}%", f"bad OHLC rows {f0['bad_rows']}", f"zero-volume in last 5: {f0['zero_volume_last5']}"]
    if f0['nan_closes']:
        parts.append(f"{f0['nan_closes']} NaN closes")
    res['C4'] = (dq.level_integrity(f0['flat_zero_volume_pct'], f0['bad_rows'], f0['zero_volume_last5'], f0['nan_closes']), '; '.join(parts))
    ju = jumps(h)
    notes, lv = [], 'PASS'
    for d, v in ju.items():
        shared = [o for o, f in others.items() if any(abs(dd - d).days <= 1 for dd in jumps(f))]
        lacking = [o for o, f in others.items() if d in f.index and not any(abs(dd - d).days <= 1 for dd in jumps(f))]
        if lacking and not shared:
            notes.append(f'{d.date()} {v*100:+.0f}%: ONLY here; {",".join(lacking)} are continuous -> {name} has a split error')
            lv = 'FAIL'
        elif shared:
            notes.append(f'{d.date()} {v*100:+.0f}%: also in {",".join(shared)} (real move, or unadjusted everywhere: needs IBKR)')
            lv = worst([lv, 'WARN'])
        else:
            notes.append(f'{d.date()} {v*100:+.0f}%: no other source to compare')
            lv = worst([lv, 'WARN'])
    res['C5'] = (lv, ' | '.join(notes) if notes else 'no one-day move over 40%')
    n = f0['bars']
    notes6 = [f'{n} bars from {h.index[0].date()}']
    lv6 = dq.level_history(n)
    for o, f in others.items():
        if (h.index[0] - f.index[0]).days > 3:
            notes6.append(f'starts {(h.index[0] - f.index[0]).days} days after {o} ({f.index[0].date()}, {len(f)} bars)')
            lv6 = worst([lv6, 'WARN'])
    res['C6'] = (lv6, '; '.join(notes6))
    return res


def grade(sym, frames, tab):
    """Returns {check: (level, note)} plus 'used' (the source the tab says served it, else the first in the chain)."""
    chain = [s for s in chain_sources(sym) if isinstance(frames.get(s), pd.DataFrame) and len(frames[s])]
    if not chain:
        return {'used': None, **{k: ('FAIL', 'no source returned data') for k in ('C2', 'C4', 'C5', 'C6', 'C8', 'C9')}}
    extras = {s: f for s, f in frames.items() if isinstance(f, pd.DataFrame) and len(f)}   # incl. EODHD, a comparison only
    per = {s: source_checks(s, extras[s], {o: f for o, f in extras.items() if o != s}) for s in chain}
    res = {}
    for k in ('C2', 'C4', 'C5', 'C6'):
        lv = worst([per[s][k][0] for s in chain])
        bad = [f'{s}: {per[s][k][1]}' for s in chain if per[s][k][0] != 'PASS']
        res[k] = (lv, ' || '.join(bad) if bad else per[chain[0]][k][1] + (f' (all {len(chain)} sources in the chain)' if len(chain) > 1 else ''))
    tab_src = (tab or {}).get('source')
    used = tab_src if tab_src in extras else chain[0]
    h = extras[used]
    others = {s: f for s, f in extras.items() if s != used}
    # C9 cross-source, close and volume
    if not others:
        res['C9'] = ('NA', 'only one source available')
    else:
        notes, lv = [], 'PASS'
        for s, f in others.items():
            common = h.index.intersection(f.index)[-20:]
            if len(common) < 5:
                notes.append(f'{s}: under 5 common days'); lv = worst([lv, 'WARN']); continue
            diff = ((h['close'].reindex(common) / f['close'].reindex(common)) - 1).abs().max()
            vs, fs = h['volume'].reindex(common).sum(), f['volume'].reindex(common).sum()
            vr = (vs / fs) if fs and fs > 0 else float('nan')
            lvl = 'FAIL' if diff > CLOSE_FAIL else 'WARN' if diff > CLOSE_WARN else 'PASS'
            vtxt = ''
            if not is_ca(sym) and s in chain and used in chain and vr == vr and not (0.8 <= vr <= 1.25):
                lvl = worst([lvl, 'WARN']); vtxt = ' (volume ratio outside 0.8-1.25)'
            notes.append(f'{used} vs {s}: max close diff {diff*100:.2f}%, volume x{vr:.2f}{vtxt}')
            lv = worst([lv, lvl])
        res['C9'] = (lv, ' | '.join(notes))
    # C8 tab honesty
    if tab:
        claim = f"tab says {tab.get('source')} / {tab.get('rows')} rows / {tab.get('status')}"
        q = per.get(used)
        fails = [k for k in ('C4', 'C5') if q and q[k][0] == 'FAIL']
        fails_any = [f'{s} {k}' for s in chain for k in ('C4', 'C5') if per[s][k][0] == 'FAIL']
        if fails:
            res['C8'] = ('FAIL', claim + f' but {used} fails {"/".join(fails)}: the tab shows no warning')
        elif tab_src and tab_src != chain[0]:
            res['C8'] = ('WARN', claim + f'; the chain order says {chain[0]} first, so STA fell through to {tab_src} (every source in the chain matters)'
                         + (f'; a source later in the chain fails: {", ".join(fails_any)}' if fails_any else ''))
        elif fails_any:
            res['C8'] = ('WARN', claim + f'; but another source STA can fall back to fails: {", ".join(fails_any)}; the tab would not warn')
        elif tab.get('rows') is not None and abs(tab['rows'] - len(h)) > 2:
            res['C8'] = ('WARN', claim + f' but we measured {len(h)} bars from {used}')
        else:
            res['C8'] = ('PASS', claim)
    else:
        res['C8'] = ('NA', 'tab not queried')
    res['used'] = used
    res['per_source'] = {s: {k: per[s][k][0] for k in per[s]} for s in per}
    return res


def tab_claim(sym, saved=None):
    if saved is not None:          # offline replay: use the tab claim saved by the original run
        return saved.get(sym)
    try:
        urllib.request.urlopen(f'http://localhost:5001/api/stock/{sym}', timeout=60).read()
        with urllib.request.urlopen(f'http://localhost:5001/api/provenance/{sym}', timeout=30) as r:
            return json.loads(r.read())['ohlcv']
    except Exception as e:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--eodhd-budget', type=int, default=None, help='EODHD calls to spend (default: remaining free quota minus 1)')
    ap.add_argument('--date', default=None, help='YYYYMMDD stamp of the cache/report to use (default: today)')
    ap.add_argument('--now', default=None, help='fix the clock, ISO time (New York if no zone), for a reproducible replay')
    ap.add_argument('--offline', action='store_true', help='replay: no provider calls, no backend calls; tab claims come from the saved JSON')
    ap.add_argument('--update-reference', action='store_true', help='write this run into backend/reference/data_audit_latest.json (read by the Data Sources tab)')
    ap.add_argument('--tickers-file', default=None, help='one ticker per line (e.g. backend/audit_universe.txt); default: the curated 24')
    ap.add_argument('--suffix', default=None, help="output name suffix (default '' online, '_offline' offline) so a replay never overwrites the saved run")
    args = ap.parse_args()
    configure(args.date, args.now)
    global UNIVERSE
    if args.tickers_file:
        UNIVERSE = universe_from_file(args.tickers_file, offline=args.offline)
        print(f'Universe: {len(UNIVERSE)} tickers from {args.tickers_file}')
    suffix = args.suffix if args.suffix is not None else ('_offline' if args.offline else '')
    saved_tabs = None
    if args.offline:
        args.eodhd_budget = 0
        saved = json.load(open(os.path.join(BACKEND, 'validation_results', f'data_audit_{STAMP}.json')))
        saved_tabs = {r['symbol']: r.get('tab') for r in saved['rows']}
    key = os.environ.get('EODHD_API_KEY', '')
    if args.eodhd_budget is None:
        try:
            with urllib.request.urlopen(f'https://eodhd.com/api/user?api_token={key}', timeout=20) as r:
                u = json.loads(r.read().decode())
            args.eodhd_budget = max(0, int(u['dailyRateLimit']) - int(u['apiRequests']) - 1)
        except Exception:
            args.eodhd_budget = 0
    print(f"{'OFFLINE replay' if args.offline else 'EODHD budget: %d calls. Fetching' % args.eodhd_budget} ...")
    cache = fetch_all(args.eodhd_budget, offline=args.offline)
    print('Reading what the Data Sources tab says ...' if not args.offline else 'Using the saved tab claims ...')
    rows = []
    for cls, sym, why in UNIVERSE:
        tab = tab_claim(sym, saved_tabs)
        g = grade(sym, cache.get(sym, {}), tab)
        ps = g.pop('per_source', {})
        rows.append({'class': cls, 'symbol': sym, 'why': why, 'used': g.pop('used'), 'tab': tab, 'per_source': ps,
                     'sources': {s: (len(f) if isinstance(f, pd.DataFrame) else f) for s, f in cache.get(sym, {}).items()},
                     'checks': {k: {'level': v[0], 'note': v[1]} for k, v in g.items()}})
    stamp_dir = os.path.join(REPO, 'docs', 'test', f'DataSources_{STAMP}')
    os.makedirs(stamp_dir, exist_ok=True)
    json.dump({'generated': TODAY.isoformat(timespec='minutes'), 'rows': rows}, open(os.path.join(BACKEND, 'validation_results', f'data_audit_{STAMP}{suffix}.json'), 'w'), indent=1, default=str)
    write_report(rows, stamp_dir, suffix)
    if args.update_reference:
        dq.update_audit_reference('truth_free', TODAY.isoformat(timespec='minutes'), f"docs/test/DataSources_{STAMP}/{'REPORT.md' if args.offline else f'REPORT{suffix}.md'}",   # a replay is the same result as the saved run
                                  {r['symbol']: [(k, v['level'], v['note']) for k, v in r['checks'].items()] for r in rows})
        print('Updated backend/reference/data_audit_latest.json (truth_free)')
    print('Wrote', os.path.join(stamp_dir, f'REPORT{suffix}.md'))


def write_report(rows, d, suffix=''):
    L = [f'# Data source audit: truth-free checks ({TODAY:%Y-%m-%d})\n',
         'Plan: `docs/claude/design/DATA_SOURCE_TESTING_PLAN_DAY126.md` step 1. Script: `backend/backtest/audit_data_sources.py`.',
         'Checks C2 fresh, C4 integrity, C5 jumps, C6 history, C8 tab honest, C9 cross-source. **Not yet checked (needs IBKR, step 2): identity, close accuracy vs broker, volume vs broker.**',
         '"STA uses" = the first source in the real chain that returned data. ✅ pass ⚠️ warn ❌ fail — not applicable.\n',
         '## Matrix\n', '| Class | Ticker | STA uses | Bars | C2 | C4 | C5 | C6 | C8 | C9 |', '|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        c = r['checks']
        n = r['sources'].get(r['used']) if r['used'] else '—'
        L.append(f"| {r['class']} | `{r['symbol']}` | {r['used'] or '—'} | {n} | " + ' | '.join(ICON[c[k]['level']] for k in ('C2', 'C4', 'C5', 'C6', 'C8', 'C9')) + ' |')
    L.append('\n## Verdict per class\n')
    by = {}
    for r in rows:
        by.setdefault(r['class'], []).append(r)
    for cls, rs in by.items():
        fails = [f"{r['symbol']} {k}" for r in rs for k, v in r['checks'].items() if v['level'] == 'FAIL']
        warns = [f"{r['symbol']} {k}" for r in rs for k, v in r['checks'].items() if v['level'] == 'WARN']
        L.append(f"- **{cls}** ({len(rs)}): " + ('no failures' if not fails else 'FAILS: ' + ', '.join(fails)) + (f"; warnings: {', '.join(warns)}" if warns else ''))
    L.append('\n## Every finding (warn and fail), with evidence\n')
    for r in rows:
        items = [(k, v) for k, v in r['checks'].items() if v['level'] in ('WARN', 'FAIL')]
        if items:
            L.append(f"**{r['symbol']}** ({r['class']}{', ' + r['why'] if r['why'] else ''}); sources {r['sources']}")
            for k, v in items:
                L.append(f"- {ICON[v['level']]} {k}: {v['note']}")
            L.append('')
    L.append('\n## Source errors (a source that could not serve a ticker)\n')
    for r in rows:
        errs = {s: v for s, v in r['sources'].items() if isinstance(v, str)}
        if errs:
            L.append(f"- `{r['symbol']}`: " + '; '.join(f'{s}: {v}' for s, v in errs.items()))
    L.append('''
## Known limits of this audit (read before trusting the matrix)

- **Agreement is not accuracy.** If two sources share the same defect they agree (SOXL.NE on Yahoo and EODHD are both close-only), so C9 passes. Only the IBKR truth step (step 2) can settle those; C5 marks them "needs IBKR".
- **"STA uses" comes from the tab.** The tab's source was read right after this script spent Twelve Data credits on the same key, so some "fell through to Yahoo" results may be partly self-inflicted. Either way, every source in the chain is graded, because any of them can serve a request.
- **Canada has one source for most tickers.** Only the tickers listed with EODHD had a second opinion (free quota: 20 calls a day). The rest show `—` in C9, which means unchecked, not clean.
- **Freshness ignores market holidays** (it uses weekdays).
- **Tradier is not dividend-adjusted**, so its old closes differ slightly from Yahoo's on ex-dividend days; the close check only looks at the last 20 sessions.
- Not run: identity/currency (C1), close accuracy vs the broker (C3), volume vs the broker (C7), fundamentals and classification (C10), Alpha Vantage.
''')
    open(os.path.join(d, f'REPORT{suffix}.md'), 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv(os.path.join(BACKEND, '.env'))
    main()

