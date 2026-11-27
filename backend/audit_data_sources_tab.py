#!/usr/bin/env python3
"""Statement Audit for the Data Sources tab (Day 136). Plan: docs/claude/design/DATA_SOURCES_PROVENANCE_PLAN_DAY136.md Part C.

Step 1 (frontend/scripts/dump_data_sources_tab.js) saved what the TAB showed. This reads each shown statement and recomputes it
from a source the tab did not use: the cache database rows, the provider state database (breaker, limiter, attempt log),
reference/provider_coverage.json and the orchestrator's real chains. Verdicts as in the Statement Audit: PASS / WRONG /
MISLEADING / UNVERIFIED (with why). Read-only: never calls a provider, never writes to any database.

Usage: venv/bin/python audit_data_sources_tab.py OUT_DIR        (OUT_DIR holds dump_<TICKER>.json; writes REPORT_DATASOURCES_TAB.md)
"""
import glob, json, os, re, sqlite3, sys
from datetime import datetime
from typing import List, NamedTuple

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cache_manager as cm
from providers import attempt_log, circuit_breaker, rate_limiter

SEV = {'PASS': '', 'WRONG': 'CRITICAL', 'MISLEADING': 'HIGH', 'UNVERIFIED': 'INFO'}
LABEL = {'alpaca': 'Alpaca', 'twelvedata': 'Twelve Data', 'yfinance': 'Yahoo (yfinance)', 'tradier': 'Tradier', 'finnhub': 'Finnhub',
         'alphavantage': 'Alpha Vantage', 'fmp': 'FMP', 'stooq': 'Stooq', 'eodhd': 'EODHD'}
HEALTH_TEXT = {'closed': 'ok', 'half_open': 'degraded', 'open': 'circuit open'}


class Row(NamedTuple):
    ticker: str; sid: str; claim: str; shown: str; expected: str; verdict: str; note: str = ''


def breaker_states() -> dict:
    """Read the shared breaker table directly (not through get_breaker, which would create rows)."""
    out = {}
    try:
        c = sqlite3.connect(f'file:{circuit_breaker.DB_PATH}?mode=ro', uri=True, timeout=2)
        for p, s in c.execute('select provider, state from circuit_breaker_state'): out[p] = s
        c.close()
    except Exception as e:
        out['_error'] = type(e).__name__
    return out


class Audit:
    def __init__(self, dump, rows, breakers, cov, chains):
        self.d, self.t, self.rows = dump, dump['ticker'], rows
        self.p, self.tab = dump['payloads'], dump['tab']
        self.breakers, self.cov, self.chains = breakers, cov, chains

    def add(self, sid, claim, shown, expected, verdict, note=''):
        self.rows.append(Row(self.t, sid, claim, shown, expected, verdict, note))

    def eq(self, sid, claim, shown, expected, note=''):
        self.add(sid, claim, shown, expected, 'PASS' if str(shown) == str(expected) else 'WRONG', note)

    def run(self):
        for k in ('stock', 'provenance', 'health', 'coverage', 'cache'):
            if k not in self.p or self.p[k]['status'] != 200:
                self.add('DS-0', f'payload {k} reached the tab', self.p.get(k, {}).get('status', 'missing'), '200', 'WRONG')
        if self.tab.get('error'):
            self.add('DS-0', 'tab shows an error state', self.tab['error'], 'no error', 'WRONG'); return self
        self.identity(); self.quality(); self.fundamentals(); self.chain_rows(); self.details()
        return self

    # ---- A. identity
    def identity(self):
        tab, stock = self.tab, self.p['stock']['body']
        self.eq('DS-1', 'Symbol', tab['symbol'], self.t)
        self.eq('DS-2', 'Exchange / currency / class equal what /api/stock sent',
                f"{tab['exchange']} / {tab['currency']} / {tab['cls']}", f"{stock.get('exchange') or 'unknown'} / {stock.get('currency') or 'unknown'} / {stock.get('instrumentClass') or 'Unknown'}")
        self.add('DS-2b', 'Exchange, currency and fund type are TRUE (vs the broker)', f"{tab['exchange']} / {tab['currency']}", 'IBKR contract', 'UNVERIFIED',
                 'needs the broker contract record; the IBKR truth run covered closes, not these fields')
        info = cm.get_ticker_cache_info(self.t, 'ohlcv')
        src = info.get('source') if info else None
        self.eq('DS-3', '"Data from" = the source stored on the cache row', tab['dataFrom'], LABEL.get(src, src) if src else 'unknown', 'read straight from ohlcv_cache.source')
        # cache label recomputed from the row's own dates
        if info is None: exp = 'not cached, will fetch on next analysis'
        elif info.get('expired'): exp = 'expired, will refetch on next analysis'
        else: exp = 'cached'
        shown = tab['cacheState']
        self.eq('DS-4', 'Cache state label', shown, exp, 'recomputed from the row\'s own expiry (Day 136: "just fetched" was removed, it was a guess from cache age)')
        self.add('DS-4b', 'The label never claims a fetch it cannot know about', shown, 'not "just fetched"', 'PASS' if shown != 'just fetched' else 'MISLEADING',
                 '"just fetched" was guessed from cache age under 5 minutes; the attempt line (DS-5) now says when a provider really answered')
        # attempt line: recomputed from the attempt log table read directly (not through the route)
        att = attempt_log.read(self.t, 'ohlcv'); txt = tab.get('attempt') or ''
        if att['error']: want = 'could not be read'
        elif att['state'] == 'never': want = 'no provider check recorded by this app yet'
        elif att['state'] == 'ok': want = f"answered by {LABEL.get(att['last_ok_provider'], att['last_ok_provider'])}" if att['last_ok_provider'] else 'answered'
        else: want = 'failed'
        pa = self.p['provenance']['body']['ohlcv'].get('attempt') or {}
        self.add('DS-5', 'Attempt line = the attempt log row', txt, f"Prices: ... {want} ...", 'PASS' if want in txt and txt.startswith('Prices:') else 'WRONG',
                 f"log row: state={att['state']}, period={att['period']}; route sent state={pa.get('state')}")
        self.add('DS-5c', 'The attempt line is a CHECK RECORD, not proof the prices are right', txt, 'data-quality rows', 'UNVERIFIED',
                 'it says a provider answered (or failed) and when; whether the bars are correct is the quality rows and the C-checks')
        self.add('DS-5d', 'No old "this session" sentence remains', 'present' if 'this session' in (tab['identityText'] or '') else 'gone', 'gone', 'PASS' if 'this session' not in (tab['identityText'] or '') else 'WRONG')

    # ---- B. quality
    def quality(self):
        tab = self.tab; prov = self.p['provenance']['body']; q = prov.get('quality') or {}
        if q.get('state') == 'not_cached':
            self.add('DS-6', 'Quality block for an uncached ticker', tab['qualityBoxText'], 'says nothing cached', 'PASS' if 'Nothing is cached' in (tab['qualityBoxText'] or '') else 'WRONG'); return
        try:
            import data_quality
            fresh = data_quality.cached_quality(self.t)
        except Exception as e:
            self.add('DS-6', 'Quality recomputed', 'error', type(e).__name__, 'UNVERIFIED', 'builder raised'); return
        self.eq('DS-6', 'Verdict pill = verdict of the quality builder run again on the cached bars', tab['qualityVerdict'], fresh.get('level'),
                'same builder as the tab (shared on purpose, Day 135); the builder\'s own maths is graded by the C-checks in audit_data_sources.py, not here')
        f = fresh.get('facts') or {}
        h = tab['qualityHeader'] or ''
        ok = f"Checked {f.get('bars')} bars" in h and (not f.get('last_date') or f"last bar {f['last_date']}" in h) and f"period {fresh.get('period')}" in h
        self.add('DS-7', 'Header: bars, period and last bar date', h, f"Checked {f.get('bars')} bars (period {fresh.get('period')}) ... last bar {f.get('last_date')}", 'PASS' if ok else 'WRONG')
        bad = [n for n, c in (fresh.get('checks') or {}).items() if c.get('level') in ('WARN', 'FAIL')]
        self.add('DS-8', 'Rows listed = the checks at WARN or FAIL', f"{len(tab['qualityRows'])} rows", f'{len(bad)} ({", ".join(bad) or "none"})',
                 'PASS' if len(tab['qualityRows']) == len(bad) else 'WRONG')
        if not bad:
            n = len(fresh.get('checks') or {})
            self.eq('DS-9', '"All N checks passed"', tab['allPass'], f'All {n} checks passed.')
        a = prov.get('audit') or {}
        if tab['audit']:
            self.add('DS-10', 'Last-audit line equals the reference file entry', tab['audit'], a.get('line'), 'PASS' if (a.get('line') or '') in tab['audit'] else 'WRONG')

    def fundamentals(self):
        tab = self.tab; stock = self.p['stock']['body']
        if tab['fundamentals'] is None:
            self.add('DS-11', 'Fundamentals line', 'not shown', '-', 'UNVERIFIED', 'quality block not ok'); return
        if stock.get('quoteType') == 'ETF':
            self.eq('DS-11', 'Fundamentals line for a fund', tab['fundamentals'], 'No fundamentals for a fund.'); return
        try:
            data, meta = cm.read_fundamentals_entry(self.t)
        except Exception as e:
            self.add('DS-11', 'Fundamentals line', tab['fundamentals'], 'cache row', 'UNVERIFIED', type(e).__name__); return
        if data is None: want = 'Fundamentals not loaded yet.'
        else:
            has = any(v is not None for k, v in data.items() if k not in ('source', '_field_sources'))
            if not has: want = 'No fundamentals on file (the cached record is empty).'
            else:
                src = (meta or {}).get('source') or data.get('source')
                want = f'Fundamentals from {LABEL.get(src, src)}'
        self.add('DS-11', 'Fundamentals line', tab['fundamentals'], want, 'PASS' if tab['fundamentals'].startswith(want.rstrip('.')) else 'WRONG')

    # ---- C. chains
    def chain_rows(self):
        tab, health = self.tab, (self.p['health']['body'].get('providers', {}) or {}).get('providers', {})   # /api/health -> providers -> providers{name}
        price_shown = [r['provider'] for r in tab['chainRows'] if r['group'] == 'price']
        fund_shown = [r['provider'] for r in tab['chainRows'] if r['group'] == 'fundamentals']
        self.eq('DS-12', 'Price chain order', ' → '.join(price_shown), ' → '.join(self.chains['ohlcv']), 'orchestrator._ohlcv_chain built fresh')
        self.eq('DS-13', 'Fundamentals chain order', ' → '.join(fund_shown), ' → '.join(self.chains['fundamentals']))
        cov = self.cov
        for r in tab['chainRows']:
            name = r['provider']; txt = r['text']; ph = health.get(name, {})
            st = self.breakers.get(name, 'closed' if '_error' not in self.breakers else None)
            if self.breakers.get('_error'):
                self.add(f'DS-14-{name}', f'{name} health dot', txt, 'breaker table', 'UNVERIFIED', 'breaker DB not readable'); continue
            want = HEALTH_TEXT.get(st, 'ok')
            if want == 'ok' and ph.get('configured') is False: want = 'no key'   # Day 136: a keyless provider is not "ok"
            m = re.search(r'(no key|ok|degraded|circuit open|unknown)', txt)
            got = m.group(1) if m else 'none'
            # an OPEN breaker whose timeout passed becomes half-open on the next read: tolerate open -> degraded
            self.add(f'DS-14-{name}', f'{LABEL.get(name, name)} health word = circuit breaker state', got, want,
                     'PASS' if got == want or (want == 'circuit open' and got == 'degraded') else 'WRONG', f'breaker table state: {st}')
            if got == 'ok' and ph.get('configured') is False:
                self.add(f'DS-15-{name}', f'{LABEL.get(name, name)} "ok" means it works', 'ok', 'no API key set', 'MISLEADING',
                         '"ok" only means the breaker is closed; this provider has no key, so it can never answer')
            elif got == 'no key':
                self.add(f'DS-15-{name}', f'{LABEL.get(name, name)} shows "no key" when it has no API key', 'no key', 'configured = false', 'PASS' if ph.get('configured') is False else 'WRONG')
            elif got == 'ok':
                self.add(f'DS-15-{name}', f'{LABEL.get(name, name)} "ok" means it has answered', 'ok', 'breaker closed', 'UNVERIFIED',
                         'a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists')
            # calls left
            m = re.search(r'(\d+) calls left today', txt)
            if name in ('twelvedata', 'alphavantage', 'tradier'):
                try: left = rate_limiter.get_limiter(name).remaining_daily
                except Exception as e: left = None
                if left is None: self.add(f'DS-16-{name}', f'{name} calls left', txt, 'limiter', 'UNVERIFIED', 'limiter unreadable')
                else:
                    shown = int(m.group(1)) if m else None
                    exp_ok = (left < 0 and shown is None) or (left >= 0 and shown is not None and abs(shown - left) <= 10)
                    self.add(f'DS-16-{name}', f'{LABEL.get(name, name)} calls left today (within 10: the count moves)', shown, left if left >= 0 else 'none shown', 'PASS' if exp_ok else 'WRONG')
            elif m:
                self.add(f'DS-16-{name}', f'{name} shows a calls-left number', m.group(0), 'none (no daily cap)', 'WRONG')
            # coverage chips
            if r['group'] == 'price':
                want_chips = [f"{mk}: {cov['providers'].get(name, {}).get(mk, 'not tested')}" for mk in cov['markets']]
                miss = [c for c in want_chips if c not in txt]
                self.add(f'DS-17-{name}', f'{LABEL.get(name, name)} coverage chips = provider_coverage.json', 'all present' if not miss else f'missing {miss}', ', '.join(want_chips), 'PASS' if not miss else 'WRONG')
        line = tab['coverageLine'] or ''
        self.add('DS-18', 'Coverage line: tested date and report', line, f"as tested on {cov.get('tested')} ({cov.get('report')})", 'PASS' if (cov.get('tested') in line and cov.get('report') in line) else 'WRONG')
        self.add('DS-18b', 'Coverage chips are CURRENT truth', cov.get('tested'), 'a re-test', 'UNVERIFIED', 'a hand-kept file dated by its own test run; not re-measured here (Alpaca "works" was measured 2026-11-21)')
        dis = [LABEL.get(n, n) for n, p in health.items() if isinstance(p, dict) and p.get('role') == 'disabled']
        want = f"Disabled: {', '.join(dis)} (not in any chain)." if dis else None
        self.add('DS-19', 'Disabled line', tab['disabledLine'], want, 'PASS' if tab['disabledLine'] == want else 'WRONG')

    # ---- D. details
    def details(self):
        tab = self.tab
        st = self.p['cache']['body']
        con = sqlite3.connect(str(cm.DB_PATH)); n = con.execute('select count(*) from ohlcv_cache').fetchone()[0]; con.close()
        g = ' | '.join(tab['cacheGrid'])
        self.add('DS-20', 'OHLCV entries = rows in ohlcv_cache', g, n, 'PASS' if f'{n} OHLCV entries' in g or f'{n}OHLCV entries' in g.replace(' ', '') or str(n) in g else 'WRONG',
                 'the cache moves while the audit runs; a small difference is expected')
        self.add('DS-21', 'Hit rate (24h) is computed from cache_stats events', g, '-', 'UNVERIFIED', 'not traced')

    # (the static cache-lifetime sentence is graded once for the whole cache, see static_rows)


def static_rows(dump) -> List[Row]:
    rows = []
    line = dump['tab'].get('staticCacheLine') or ''
    con = sqlite3.connect(str(cm.DB_PATH))
    data = con.execute('select ticker, cached_at, expires_at, source from ohlcv_cache').fetchall(); con.close()
    short = []
    for t, c, e, s in data:
        try:
            cd = datetime.fromisoformat(c); ed = datetime.fromisoformat(e)
            cd = cd.replace(tzinfo=None); ed = ed.replace(tzinfo=None)
            mins = (ed - cd).total_seconds() / 60
            if mins in (30.0, 45.0) or (mins < 60 and mins > 0): short.append((t, s, round(mins)))
        except Exception:
            pass
    ok = 'Prices are cached until the next market close (4pm ET + 30 min)' in line
    says_sooner = 'expires sooner' in line
    if short and not says_sooner:
        by = {}
        for t, s, m in short: by.setdefault((s, m), []).append(t)
        detail = '; '.join(f'{s} {m} min: {len(v)} rows' for (s, m), v in sorted(by.items()))
        rows.append(Row('-', 'DS-22', 'Static line: "Prices are cached until the next market close (4pm ET + 30 min)"', line, f'{len(short)} of {len(data)} cached rows expire 30-45 min after they were stored ({detail})', 'MISLEADING',
                        'cache_manager.py: TRADIER_OHLCV_TTL_MIN = 45, EMPTY_NEWEST_BAR_TTL_MIN = 30, forming-bar cap 16:30 ET; the line is a fixed sentence, not read from any row'))
    else:
        rows.append(Row('-', 'DS-22', 'Static line: cache lifetime', line, 'rule in cache_manager (TTL 30 empty bar / 45 Tradier / forming-bar cap)',
                        'PASS' if ok and says_sooner else ('PASS' if ok and not short else 'MISLEADING'),
                        f'{len(short)} of {len(data)} cached rows are short-lived; the line names the exception' if says_sooner else 'no short-lived rows right now, but the code has three exceptions the line does not name'))
    ttl = re.search(r'Fundamentals for (\d+) days', line)
    rows.append(Row('-', 'DS-23', 'Static line: "Fundamentals for 7 days"', ttl.group(0) if ttl else line, f'FUNDAMENTALS_TTL_DAYS = {cm.FUNDAMENTALS_TTL_DAYS}', 'PASS' if ttl and int(ttl.group(1)) == cm.FUNDAMENTALS_TTL_DAYS else 'WRONG'))
    return rows


def main():
    out = sys.argv[1]
    dumps = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(out, 'dump_*.json')))]
    if not dumps: print('no dumps in', out); return 2
    from providers import orchestrator
    dp = orchestrator.DataProvider()
    chains = {'ohlcv': [p.name for p in dp._ohlcv_chain], 'fundamentals': [p.name for p in dp._fundamentals_chain]}
    cov = json.load(open(os.path.join(HERE, 'reference', 'provider_coverage.json')))
    breakers = breaker_states()
    rows: List[Row] = static_rows(dumps[0])
    for d in dumps: rows = Audit(d, rows, breakers, cov, chains).run().rows
    counts = {k: sum(1 for r in rows if r.verdict == k) for k in SEV}
    lines = ['# Data Sources tab Statement Audit', '', f"Run: {datetime.now().isoformat(timespec='minutes')} · dumps: {', '.join(d['ticker'] for d in dumps)}", '',
             f"Verdicts: PASS {counts['PASS']} · WRONG {counts['WRONG']} · MISLEADING {counts['MISLEADING']} · UNVERIFIED {counts['UNVERIFIED']}", '',
             'Method: the tab\'s own text (read from the page) against the cache DB, the provider state DB (breaker, limiter), provider_coverage.json and the orchestrator\'s chains. Read-only.', '',
             '| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |', '|---|---|---|---|---|---|---|---|']
    order = {'WRONG': 0, 'MISLEADING': 1, 'UNVERIFIED': 2, 'PASS': 3}
    esc = lambda s: str(s).replace('|', '/').replace('\n', ' ')
    for r in sorted(rows, key=lambda r: (order[r.verdict], r.ticker, r.sid)):
        lines.append(f'| {r.ticker} | {r.sid} | {esc(r.claim)} | {esc(r.shown)} | {esc(r.expected)} | {r.verdict} | {SEV[r.verdict]} | {esc(r.note)} |')
    path = os.path.join(out, 'REPORT_DATASOURCES_TAB.md')
    open(path, 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[:6])); print('report:', path)
    return 1 if counts['WRONG'] else 0


if __name__ == '__main__':
    sys.exit(main())
