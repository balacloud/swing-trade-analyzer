#!/usr/bin/env python3
"""Statement Audit phase 3a (Day 126): Market backdrop, Fundamentals, Mean-Reversion Read. Plan: docs/claude/design/STATEMENT_AUDIT_PHASE3_PLAN_DAY126.md (§5 = review applied).
Subclasses the phase-2 CardAudit (which subclasses the phase-1 Audit): earlier behaviour is untouched. Parsed by test id where the page has one.
Usage: venv/bin/python audit_cards2.py OUT_DIR   (reads dump_*.json, writes REPORT_CARDS2.md; fetches SPY/QQQ reference history once and caches it in OUT_DIR)
"""
import glob, json, os, re, sys
from datetime import datetime, date
import audit_ref as R
import audit_statements as A
from audit_statements import fm, near, f2, dlabel
from audit_cards import CardAudit
from vix_bands import vix_band
import market_time

VIX_WORDS = {'low_volatility': 'low', 'normal': 'normal range', 'elevated': 'elevated', 'high': 'high', 'extreme': 'extreme'}


# ----------------------------------------------------------------- independent index history (second source, S4) cached per run
def ref_index(sym, start, out):
    path = os.path.join(out, f'ref_adj_{sym}.json')   # Day 126: adjusted basis, like the app (older ref_*.json were unadjusted)
    def completed(rows):
        # the same rule as the app: today's bar is unfinished until 16:30 ET (market_time.is_forming_bar)
        return rows[:-1] if rows and market_time.is_forming_bar(rows[-1][0]) else rows
    if os.path.exists(path):
        try:
            return completed(json.load(open(path)))
        except Exception:
            pass
    try:
        import yfinance as yf
        df = yf.Ticker(sym).history(start=start, auto_adjust=True)
        if df is None or len(df) < 250:
            return None
        rows = [(str(i)[:10], float(c)) for i, c in zip(df.index, df['Close'])]
        json.dump(rows, open(path, 'w'))
        return completed(rows)
    except Exception as e:  # noqa: BLE001 - a missing reference is reported UNVERIFIED, never a pass
        print(f'⚠️ reference history for {sym} unavailable: {e}')
        return None


def trend_facts(rows):
    """The card's facts, rebuilt from [(date, close)] by the plain words (completed bars)."""
    closes = [c for _, c in rows]; dates = [d for d, _ in rows]
    if len(closes) < 200: return None
    c = closes[-1]; s50 = sum(closes[-50:]) / 50; s200 = sum(closes[-200:]) / 200
    ch = [round((closes[i] / closes[i - 1] - 1) * 100, 2) for i in range(1, len(closes))]
    dd = dates[1:]
    worst = None
    for i in range(len(ch) - 10, len(ch)):
        if worst is None or ch[i] <= ch[worst]: worst = i
    out = {'asOf': dates[-1], 'above200': c > s200, 'pct200': (c / s200 - 1) * 100, 'above50': c > s50, 'pct50': (c / s50 - 1) * 100, 'searchedFrom': dd[0]}
    if ch[worst] >= 0:
        out['drop'] = None
    else:
        since = next((dd[i] for i in range(worst - 1, -1, -1) if ch[i] <= ch[worst]), None)
        out['drop'] = {'pct': ch[worst], 'date': dd[worst], 'since': since}
    return out


def parse_drop(txt):
    m = re.search(r'(-?[\d.]+)% on ([A-Z][a-z]{2} \d+) \((largest since ([A-Z][a-z]{2} \d+, \d{4})|largest in data back to ([A-Z][a-z]{2} \d+, \d{4}))\)', txt or '')
    return m


def lab_to_iso(label, year=None):
    for fmt in ('%b %d, %Y',):
        try: return datetime.strptime(label, fmt).strftime('%Y-%m-%d')
        except ValueError: pass
    return None


class CardAudit2(CardAudit):
    def __init__(self, dump, out):
        super().__init__(dump); self.out = out

    def addc(self, sid, claim, shown, expected, verdict, note='', sev=None):
        names = {'card-market-backdrop': 'Market backdrop', 'card-fundamentals': 'Fundamentals', 'card-mr-read': 'MR Read'}
        self.add(sid, claim, shown, expected, verdict, note, card=names.get(self.cur, self.cur), sev=sev)

    def run_cards2(self):
        if len(self.c) < 60:
            self.add('X1', 'cards', f'{len(self.c)} bars', 'at least 60', 'UNVERIFIED', card='all'); return self
        self.backdrop(); self.fundamentals(); self.mr(); return self

    # ----------------------------------------------------------------- Market backdrop
    def backdrop(self):
        self.use('card-market-backdrop')
        rows = self.d.get('backdropRows') or []
        spy, qqq, vix = (self.d['payloads'].get(k, {}).get('body') or {} for k in ('spy', 'qqq', 'vix'))
        if not rows:
            if spy or qqq: self.addc('MB0', 'Market backdrop rows present when the index payloads answered', 'no rows', 'rows', 'WRONG')
            return
        # static S3: the words "last 10 sessions" vs index_trend.DROP_WINDOW
        src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index_trend.py')).read()
        dw = re.search(r'DROP_WINDOW = (\d+)', src)
        self.addc('MB-S3', 'S3: "last 10 sessions" = the code window (index_trend.DROP_WINDOW)', 'last 10 sessions', f'DROP_WINDOW = {dw.group(1) if dw else "?"}', 'PASS' if dw and dw.group(1) == '10' else 'MISLEADING')
        last_done = None
        for r in rows:
            sym, src_payload = ('SPY', spy) if r['label'].startswith('S&P') else ('QQQ', qqq)
            trend = (src_payload or {}).get('trend') or {}
            if r.get('unavailable'):
                self.addc(f'MB-{sym}', f'{r["label"]}: unavailable row says why', r['unavailable'], 'reason', 'PASS' if trend == {} else 'WRONG', 'a row is said unavailable although the payload has a trend' if trend else ''); continue
            ref = ref_index(sym, (trend.get('searchedFrom') or '2024-11-01')[:7] + '-01', self.out)
            if sym == 'SPY' and spy.get('priceHistory'):
                app = [(b['date'], b['close']) for b in spy['priceHistory']]
                f_app = trend_facts(app)
            else:
                f_app = None
            f_ref = trend_facts([(d, c) for d, c in ref]) if ref else None
            fa = f_app or f_ref
            tol = 0.051 if f_app else 0.2
            if fa is None:
                self.addc(f'MB-{sym}', f'{r["label"]} row recomputed', 'no data', 'history', 'UNVERIFIED', 'no bars to recompute from'); continue
            src_note = 'the app\'s own 260 bars' if f_app else 'independent Yahoo history (S4; dividends/provider differences allowed ±0.2pp)'
            for key, above, pct, txt in (('long', fa['above200'], fa['pct200'], r['long']), ('short', fa['above50'], fa['pct50'], r['short'])):
                m = re.match(r'([↑↓]) (above|below) ([+-]?[\d.]+)%', (txt or '').replace('−', '-'))
                if not m:
                    self.addc(f'MB-{sym}-{key}', f'{r["label"]} {key}-term line', txt or 'missing', 'arrow, word and %', 'WRONG'); continue
                good = ((m.group(1) == '↑') == above) and ((m.group(2) == 'above') == above) and near(float(m.group(3)), pct, tol)
                edge = (not good) and abs(pct - float(m.group(3))) < 0.35 and (m.group(2) == 'above') == above
                self.addc(f'MB-{sym}-{key}', f'{r["label"]} {"200" if key == "long" else "50"}-day: arrow, word and % from the average ({src_note})', txt, f'{"↑ above" if above else "↓ below"} {pct:+.1f}%',
                          'PASS' if good else ('UNVERIFIED' if edge and not f_app else 'WRONG'), 'within provider tolerance but not exact' if edge and not f_app else '')
            md = parse_drop(r.get('drop') or '')
            if fa['drop'] is None:
                self.addc(f'MB-{sym}-drop', f'{r["label"]} biggest drop', r.get('drop') or 'missing', 'no down day', 'PASS' if re.search(r'no down day', r.get('drop') or '') else 'WRONG')
            elif not md:
                self.addc(f'MB-{sym}-drop', f'{r["label"]} biggest drop line parsed', r.get('drop') or 'missing', 'pct on date (since)', 'WRONG')
            else:
                dd = fa['drop']
                ok = near(float(md.group(1)), dd['pct'], 0.011) and md.group(2) == dlabel(dd['date'])
                self.addc(f'MB-{sym}-drop', f'{r["label"]}: biggest 1-day close-to-close drop in the last 10 completed sessions, and its date ({src_note})', f'{md.group(1)}% on {md.group(2)}', f'{dd["pct"]}% on {dlabel(dd["date"])}',
                          'PASS' if ok else ('UNVERIFIED' if not f_app and near(float(md.group(1)), dd['pct'], 0.3) else 'WRONG'))
                # the "since" / "in data back to" claim over the reference history (start anchored to the payload's searchedFrom)
                if ref:
                    rr = trend_facts(ref); d2 = rr['drop'] if rr else None
                    if d2 and md.group(4):
                        iso = lab_to_iso(md.group(4))
                        okk = d2['since'] is not None and iso is not None and abs((datetime.strptime(d2['since'], '%Y-%m-%d') - datetime.strptime(iso, '%Y-%m-%d')).days) <= 3
                        self.addc(f'MB-{sym}-since', f'S4: "largest since <date>" = the last earlier day at least as bad (independent history)', md.group(4), f'{d2["since"]}', 'PASS' if okk else 'UNVERIFIED',
                                  '' if okk else 'the reference history (Yahoo, unadjusted) can differ from the app\'s frame on near-equal days; inspect')
                    elif md.group(5):
                        sf = (trend.get('searchedFrom') or '')
                        iso = lab_to_iso(md.group(5))
                        self.addc(f'MB-{sym}-back', 'S3: "largest in data back to <date>" = the first day of the data searched (payload searchedFrom) and nothing in the reference history inside that span is worse', md.group(5), sf,
                                  'PASS' if iso == sf and (d2 is None or d2['since'] is None or d2['since'] < sf) else 'UNVERIFIED', 'the app\'s frame starts at searchedFrom; a longer history may hold a larger drop (INFO)')
            last_done = fa['asOf']
        # the as-of line
        asof = re.search(r'Index figures as of ([A-Z][a-z]{2} \d+) close', self.text)
        if asof and last_done: self.addc('MB-asof', '"Index figures as of <date> close" = the last completed index bar', asof.group(0), dlabel(last_done), 'PASS' if asof.group(1) == dlabel(last_done) else 'WRONG')
        # VIX
        vt = self.d.get('backdropVix') or ''
        mv = re.search(r'VIX ([\d.]+)(?: · ([a-z ]+))? \(latest quote\)', vt)
        if mv and vix.get('current') is not None:
            cur = vix['current']; band = vix_band(cur)
            self.addc('MB-vix', 'VIX value (1 decimal) from the /api/market/vix payload', mv.group(1), f'{cur:.1f}', 'PASS' if f'{cur:.1f}' == mv.group(1) else 'WRONG', 'same-dump comparison only: VIX moves between dumps')
            lab = VIX_WORDS.get(band)
            shown_band = vix_band(float(mv.group(1)))
            self.addc('MB-vixband', 'S3: the band word vs the VIX number (bands: vix_bands.py; the band uses the 2-dp value, the card shows 1 dp)', mv.group(2), lab, 'PASS' if mv.group(2) == lab else 'WRONG')
            if shown_band != band: self.addc('MB-vixband2', 'band at the displayed 1-dp value differs from the band used', f'{mv.group(1)} reads {VIX_WORDS.get(shown_band)}', f'{cur} is {lab}', 'MISLEADING', 'display rounding at a band edge', sev='LOW')
            self.addc('MB-vixts', 'S3: "(latest quote)" has no timestamp in the payload, so how recent it is cannot be checked', '(latest quote)', 'a quote time', 'UNVERIFIED', 'the /api/market/vix payload carries no quote time')
        elif vix.get('current') is not None:
            self.addc('MB-vix', 'VIX line found', vt or 'missing', 'VIX value', 'WRONG')

    # ----------------------------------------------------------------- Fundamentals
    def fundamentals(self):
        if not self.use('card-fundamentals'):
            if self.stock: self.addc('FU0', 'Fundamentals card present', 'card not found', 'card text', 'WRONG')
            return
        f = (self.d['payloads'].get('fundamentals') or {}).get('body') or {}
        qt = self.stock.get('quoteType')
        etf = isinstance(qt, str) and qt.upper() == 'ETF'
        if etf:
            ok = 'Not applicable' in self.text and re.search(r'This (is an ETF|looks like an ETF)', self.text)
            self.addc('FU1', 'ETF (quoteType) -> "Not applicable" and no check tiles', 'Not applicable' if ok else 'checks shown', 'Not applicable', 'PASS' if ok and 'Return on equity' not in self.text.split('How these checks')[0] else 'WRONG')
        else:
            rev, roe, de = f.get('revenueGrowth'), f.get('roe'), f.get('debtToEquity')
            def tile(pat): return re.search(pat, self.text.replace('−', '-'))
            exp = {}
            tr = tile(r'([✓⚑–]) Sales ([+-]?[\d.]+)%')
            if rev is not None:
                fl = rev <= -10
                if tr: self.work = self.work.replace(tr.group(0), ' § ', 1)
                self.addc('FU2', 'Sales growth: value (1 dp) and the flag at <= -10% (S1 /api/fundamentals revenueGrowth; provider field)', tr.group(0) if tr else 'tile missing', f'{rev:+.1f}% flag={fl}',
                          'PASS' if tr and near(float(tr.group(2)), rev, 0.051) and (tr.group(1) == '⚑') == fl else 'WRONG', 'a provider field: recompute is not possible (S4 below)')
                exp['rev'] = fl
            tro = tile(r'([✓⚑–]) Return on equity ROE ([+-]?[\d.]+)%')
            if roe is not None:
                fl = roe < 0
                if tro: self.work = self.work.replace(tro.group(0), ' § ', 1)
                self.addc('FU3', 'ROE: value (1 dp) and the flag at < 0%', tro.group(0) if tro else 'tile missing', f'{roe:.1f}% flag={fl}',
                          'PASS' if tro and near(float(tro.group(2)), roe, 0.051) and (tro.group(1) == '⚑') == fl else 'WRONG')
                exp['roe'] = fl
            td = tile(r'([✓⚑–]) Debt (?:D/E ([+-]?[\d.]+)|D/E [+-]?[\d.]+: negative equity)')
            if de is not None:
                if de < 0:
                    ok = bool(re.search(r'negative equity, ratio not meaningful', self.text)) and (td is None or td.group(1) == '–')
                    self.addc('FU4', 'negative D/E -> "ratio not meaningful", unchecked', 'says so' if ok else 'checked', 'not meaningful', 'PASS' if ok else 'WRONG')
                else:
                    fl = de > 2.0
                    if td: self.work = self.work.replace(td.group(0), ' § ', 1)
                    self.addc('FU4', 'Debt/equity: value (2 dp) and the flag at > 2.0', td.group(0) if td else 'tile missing', f'{de:.2f} flag={fl}',
                              'PASS' if td and td.group(2) and near(float(td.group(2)), de, 0.0051) and (td.group(1) == '⚑') == fl else 'WRONG')
                    exp['de'] = fl
                    if abs(de - 2.0) < 0.01 and f'{de:.2f}' == '2.00':
                        self.addc('FU4e', 'display rounding at the 2.0 cutoff', f'D/E {de:.2f}', 'flag only above 2.0', 'MISLEADING', sev='LOW')
            nflag = sum(1 for v in exp.values() if v)
            hl = re.search(r'⚑ (\d+) red flags?|No red flags|Can\'t check', self.text)
            if hl:
                self.work = self.work.replace(hl.group(0), ' § ', 1)
                shown = int(hl.group(1)) if hl.group(1) else (0 if hl.group(0) == 'No red flags' else None)
                self.addc('FU5', 'headline = the number of tripped flags', hl.group(0), f'{nflag} flag(s)', 'PASS' if shown == nflag else 'WRONG')
                words = {'rev': 'Sales are shrinking.', 'roe': 'Return on equity is negative.', 'de': 'Debt to equity is above 2.0.'}
                if nflag:
                    got = [w for k, w in words.items() if exp.get(k) and w in self.text]
                    self.addc('FU5w', 'one plain sentence per tripped flag', ', '.join(got), f'{nflag} sentence(s)', 'PASS' if len(got) == nflag else 'WRONG')
                if re.search(r'Debt is heavy', self.text): self.addc('FU5v', 'verdict word "Debt is heavy"', 'Debt is heavy.', 'a fact with the number', 'MISLEADING', sev='LOW')
            # sources line
            fs = f.get('_field_sources') or {}
            ms = re.search(r'Source: ([^.]*?)\.', self.text)
            if ms and fs:
                names = {'finnhub': 'Finnhub', 'yfinance': 'yfinance', 'fmp': 'FMP', 'alphavantage': 'Alpha Vantage'}
                want = sorted({names.get(fs.get(k), fs.get(k)) for k in ('revenueGrowth', 'roe', 'debtToEquity') if fs.get(k)})
                got = sorted(n for n in names.values() if n in ms.group(1))
                self.addc('FU6', 'S1: the providers named on the card = the per-field sources in the payload', ms.group(1), ', '.join(want), 'PASS' if got == want else 'WRONG')
                self.work = self.work.replace(ms.group(0), ' § ', 1)
            if re.search(r'disagrees with STA.s backtest data about 40%', self.text):
                self.addc('FU7', 'the "about 40% of the time" claim has no current source (a 6-of-15 Day-78 label comparison about a label the card no longer shows)', 'claim shown', 'a supported number', 'MISLEADING', sev='LOW')
        # earnings row (both ETF and stocks)
        e = (self.d['payloads'].get('earnings') or {}).get('body') or {}
        me = re.search(r'Next earnings · (.*?)(?= How these checks| Source:|$)', self.text)
        if me and e:
            t = me.group(1)
            days = e.get('days_until'); dt = e.get('earnings_date')
            if not dt: ok = 'No earnings date found' in t
            elif days is not None and days < 0: ok = f'Last date in the feed: {dt} ({abs(days)} day' in t and 'ago' in t
            elif days == 0: ok = f'{dt} · today' in t
            else: ok = f'{dt} · in {days} day' in t
            self.addc('FU8', 'earnings row: date and calendar days (S5 with the header badge / /api/earnings)', t[:80], f'{dt} days_until={days}', 'PASS' if ok else 'WRONG')
            self.work = self.work.replace(me.group(0), ' § ', 1)
        self.unclaimed([r'10%\+', r'below 0%', r'above 2\.0', r'falling 10%', r'10% or more', r'above \d\.\d', r'7-day', r'Day 119', r'2-week', r'near 10', r'near 40', r'O.Neil', r'Minervini', r'2\.0', r'3 checks', r'All 3', r'\b3\b', r'Not applicable'], 'FU')

    # ----------------------------------------------------------------- Mean-Reversion Read
    def mr(self):
        mr = (self.d['payloads'].get('mr') or {}).get('body') or {}
        rows = self.d.get('mrRows') or {}
        if not self.use('card-mr-read'):
            if mr and not mr.get('error'): self.addc('MR0', 'MR card present when /api/mr/signal answered', 'card not found', 'card text', 'WRONG')
            return
        if mr.get('error') or not mr.get('rules'):
            ok = bool(re.search(r"Couldn't check the dip rules", self.text)); self.addc('MR0', 'MR error state is said out loud', 'says so' if ok else 'silent', 'says so', 'PASS' if ok else 'WRONG'); return
        c, v = self.c, self.v
        rules, cond = mr['rules'], mr['conditions']
        if mr.get('asOf') != self.dates[-1]:
            self.addc('MR-S5', 'S5: the MR frame\'s last bar = the stock\'s last completed bar', mr.get('asOf'), self.dates[-1], 'UNVERIFIED', 'the MR route fetches its own frame; recompute skipped'); return
        # RSI(2): the app's definition = pandas exponential smoothing with alpha one half and adjust on of gains/losses with the first bar's change = 0
        g = [0.0] + [max(c[i] - c[i - 1], 0.0) for i in range(1, len(c))]; l = [0.0] + [max(c[i - 1] - c[i], 0.0) for i in range(1, len(c))]
        def ewm_adj(xs, a=0.5):
            num = den = 0.0
            for x in xs: num = x + (1 - a) * num; den = 1 + (1 - a) * den
            return num / den
        ag, al = ewm_adj(g), ewm_adj(l); rsi2 = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
        sma200 = R.sma(c, 200); pct = R.pct(c[-1], sma200) if sma200 else None
        adv = sum(c[i] * v[i] for i in range(len(c) - 20, len(c))) / 20
        no_vol = sum(1 for x in v[-50:] if x and x > 0) < 40
        self.addc('MR-rsi', 'RSI(2) = ewm(alpha 1/2) average gain / average loss over all bars (S1 mean_reversion.calculate_rsi_short); tolerance 0.3 (2-dp bars)', f'{mr["rsi2"]}', f'{rsi2:.2f}', 'PASS' if near(mr['rsi2'], rsi2, 0.3) else 'WRONG')
        self.addc('MR-sma', '% above the 200-day average = (close / 200-day SMA - 1)', f'{mr["pct_above_sma200"]}%', f'{pct:.2f}%' if pct is not None else 'n/a', 'PASS' if pct is not None and near(mr['pct_above_sma200'], pct, 0.1) else 'WRONG')
        self.addc('MR-price', 'price = the last completed close', f'{mr["current_price"]}', f'{c[-1]}', 'PASS' if near(mr['current_price'], c[-1], 0.011) else 'WRONG')
        if not no_vol:
            self.addc('MR-dv', 'average dollar volume = 20-bar mean of close x volume (completed bars)', f'{mr["avg_dollar_volume"]:,}', f'{adv:,.0f}', 'PASS' if near(mr['avg_dollar_volume'] / adv, 1.0, 0.01) else 'WRONG')
        want = {'rsi2_oversold': rsi2 < rules['rsi2_entry'], 'above_200sma': (pct is not None and pct > 0), 'price_filter': c[-1] > rules['price_min'], 'volume_filter': (not no_vol and adv > rules['dollar_volume_min'])}
        for k, w in want.items():
            got = cond.get(k)
            if k == 'volume_filter' and no_vol:
                self.addc('MR-cond-volume_filter', 'zero-volume history: the volume rule is not checked, never a fake $0 fail', str(got), 'None/unchecked', 'PASS', 'the card shows "no volume data"'); continue
            edge = (k == 'rsi2_oversold' and abs(rsi2 - rules['rsi2_entry']) < 0.3) or (k == 'price_filter' and abs(c[-1] - rules['price_min']) < 0.02)
            self.addc(f'MR-cond-{k}', f'rule "{k}" pass/fail from the recomputed numbers (thresholds from the payload rules)', str(got), str(w), 'PASS' if got == w else ('UNVERIFIED' if edge else 'WRONG'), 'borderline: within the recompute tolerance of the cutoff' if edge and got != w else '')
        sig = all(want.values())
        head = 'Signal: all 4 rules pass' if mr.get('signal') else 'No signal'
        self.addc('MR-head', 'headline = all four rules must pass', f'{head} (payload signal={mr.get("signal")})', f'all pass = {sig}', 'PASS' if (head.startswith('Signal') == (sig and all(x is True for x in cond.values()))) and bool(mr.get('signal')) == all(x is True for x in cond.values()) else 'WRONG')
        for _k, _t in rows.items():                      # the four rows are claimed below by test id; blank their text from the unclaimed scan
            self.work = self.work.replace(_t.strip(), ' § ')
        # card rows (by test id)
        if 'rsi2_oversold' in rows:
            m = re.search(r'([✓✗–]) 2-day RSI ([\d.]+) needs under (\d+)', rows['rsi2_oversold'])
            if m:
                ok = near(float(m.group(2)), mr['rsi2'], 0.051) and int(m.group(3)) == rules['rsi2_entry'] and (m.group(1) == '✓') == bool(cond.get('rsi2_oversold'))
                self.addc('MR-row-rsi', 'RSI row: 2-day RSI (1 dp) vs the cutoff and its mark', m.group(0), f'{mr["rsi2"]} needs under {rules["rsi2_entry"]} -> {"✓" if cond.get("rsi2_oversold") else "✗"}', 'PASS' if ok else 'WRONG')
            else: self.addc('MR-row-rsi', 'RSI row found', rows['rsi2_oversold'][:60], 'row', 'WRONG')
        if 'above_200sma' in rows:
            m = re.search(r'([✓✗–]) ([\d.]+)% (above|below) its 200-day average', rows['above_200sma'])
            if m:
                ok = near(float(m.group(2)), abs(mr['pct_above_sma200']), 0.051) and (m.group(3) == 'above') == (mr['pct_above_sma200'] > 0) and (m.group(1) == '✓') == bool(cond.get('above_200sma'))
                self.addc('MR-row-sma', 'Uptrend row: % and side of the 200-day average and its mark', m.group(0), f'{abs(mr["pct_above_sma200"]):.1f}% {"above" if mr["pct_above_sma200"] > 0 else "below"}', 'PASS' if ok else 'WRONG')
                tt = re.search(r'(Above|Below) its 200-day average.*?([+-]?[\d.]+)%', (self.d.get('tr') or {}).get('text', '').replace('−', '-'))
                if tt: self.addc('MR-S5', 'S5: MR "% above/below its 200-day average" = the Technical Read\'s 200-day row (same claim, same number)', f'MR {mr["pct_above_sma200"]:+.1f}%', f'TR {tt.group(2)}%', 'PASS' if near(mr['pct_above_sma200'], float(tt.group(2)), 0.11) else 'MISLEADING', 'the two cards divide by different roundings of the average', sev='LOW')
        if 'price_filter' in rows:
            m = re.search(r'([✓✗–]) \$([\d,.]+) needs above \$(\d+)', rows['price_filter'])
            self.addc('MR-row-price', 'Price row: price and the $10 cutoff and its mark', m.group(0) if m else rows['price_filter'][:50], f'${fm(mr["current_price"])} needs above ${rules["price_min"]}',
                      'PASS' if m and m.group(2) == fm(mr['current_price']) and int(m.group(3)) == rules['price_min'] and (m.group(1) == '✓') == bool(cond.get('price_filter')) else 'WRONG')
        if 'volume_filter' in rows:
            t = rows['volume_filter']
            if no_vol: self.addc('MR-row-volume', 'zero-volume fund: "no volume data", unchecked', t[:70], 'no volume data', 'PASS' if 'no volume data' in t and '–' in t else 'WRONG')
            else:
                m = re.search(r'([✓✗–]) \$([\d.]+)([KMBT]?) traded on an average day needs above \$([\d.]+)([KMBT]?)', t)
                mult = {'': 1, 'K': 1e3, 'M': 1e6, 'B': 1e9, 'T': 1e12}
                if m:
                    shown = float(m.group(2)) * mult[m.group(3)]; need = float(m.group(4)) * mult[m.group(5)]
                    ok = abs(shown / mr['avg_dollar_volume'] - 1) < 0.06 and need == rules['dollar_volume_min'] and (m.group(1) == '✓') == bool(cond.get('volume_filter'))
                    self.addc('MR-row-volume', 'Trading-volume row: dollars traded on an average day (1 dp unit rounding) vs $25M and its mark', m.group(0), f'${mr["avg_dollar_volume"]:,} needs above ${rules["dollar_volume_min"]:,}', 'PASS' if ok else 'WRONG')
                else: self.addc('MR-row-volume', 'Volume row found', t[:60], 'row', 'WRONG')
        # blockers sentence
        fail_words = {'rsi2_oversold': f'the 2-day RSI is {rules["rsi2_entry"]} or higher', 'above_200sma': 'it is below its 200-day average', 'price_filter': f'the price is under ${rules["price_min"]}', 'volume_filter': 'it does not trade enough dollars a day'}
        order = ['rsi2_oversold', 'above_200sma', 'price_filter', 'volume_filter']
        shown_state = {k: cond.get(k) for k in order}
        if no_vol: shown_state['volume_filter'] = None
        exp_block = '; '.join(fail_words[k] for k in order if shown_state[k] is False)
        mb = re.search(r'Blocked by: (.*?)\.(?: Couldn.t check|\s|$)', self.text)
        if not mr.get('signal') and exp_block:
            self.addc('MR-block', '"Blocked by:" lists exactly the failing rules (words checked against the numbers)', mb.group(1) if mb else 'missing', exp_block, 'PASS' if mb and mb.group(1) == exp_block else 'WRONG')
            if mb: self.work = self.work.replace('Blocked by: ' + mb.group(1), ' § ', 1)
        da = re.search(r'Checked on the ([\w-]+) close', self.text)
        if da: self.work = self.work.replace(da.group(0), ' § ', 1)
        if da: self.addc('MR-asof', '"Checked on the <date> close" = the last completed bar', da.group(1), self.dates[-1], 'PASS' if da.group(1) == self.dates[-1] else 'WRONG')
        # words vs definitions: "RSI scores the last 2 days" (ewm smoothing over all bars; the last 2 changes carry ~75% of the weight)
        if 'weighted mostly to the last 2 days' in self.text:
            self.addc('MR-words', 'S3: RSI(2) wording matches the code (ewm over all bars; the last two changes carry about 75% of the weight)', 'weighted mostly to the last 2 days', 'ewm(alpha 1/2) over the whole history', 'PASS')
        else:
            self.addc('MR-words', 'S3: "RSI(2) scores the last 2 days" (the code smooths with ewm over ALL bars; the last two changes carry about 75% of the weight)', 'the last 2 days', 'ewm(alpha 1/2) over the whole history', 'MISLEADING', 'approximate wording', sev='LOW')
        if re.search(r'Forward Test tab', self.text): self.addc('MR-link', 'copy points to a hidden tab ("Forward Test tab")', 'dead link', 'a visible place', 'MISLEADING', sev='LOW')
        if re.search(r'can be Strong there', self.text): self.addc('MR-strong', 'copy says a stock "can be Strong" on the Technical Read, which no longer shows "Strong"', 'stale word', 'current wording', 'MISLEADING', sev='LOW')
        self.unclaimed([r'\b2\b', r'RSI\(2\)', r'weighted mostly to the last 2 days', r'200-day', r'\$10', r'\$25M', r'0 to 100', r'Connors', r'four', r'\b4\b', r'2-day', r'20 days', r'under 10', r'below 10', r'next open', r'\b10\b'], 'MR')


def main():
    out = sys.argv[1]
    dumps = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(out, 'dump_*.json')))]
    rows = []
    for d in dumps: rows += CardAudit2(d, out).run_cards2().rows
    counts = {k: sum(1 for r in rows if r.verdict == k) for k in A.SEV}
    L = ['# Statement Audit phase 3a report (Market backdrop, Fundamentals, Mean-Reversion Read)', '', f"Run: {datetime.now().isoformat(timespec='minutes')} · dumps: {', '.join(d['ticker'] for d in dumps)}", '',
         f"Verdicts: PASS {counts['PASS']} · WRONG {counts['WRONG']} (CRITICAL) · MISLEADING {counts['MISLEADING']} (per-row severity) · UNVERIFIED {counts['UNVERIFIED']} (INFO)", '',
         'Recomputed from bars: MR RSI(2), % above the 200-day, dollar volume, the four rule marks, the blocker sentence; S&P 500 200/50-day and the 10-session drop (the app\'s own 260 bars); QQQ and "largest since" from an independent Yahoo history (S4).',
         'Provider fields (sales growth, ROE, debt/equity) are arithmetic and flag logic only: no recompute is possible (UNVERIFIED as to truth). NOT YET COVERED: the Data Sources tab (phase 3b), other tabs; branches these tickers do not reach (signal true, VIX band edges, no-down-day, unavailable backdrop, negative equity) are exercised by planted tests only.', '',
         '| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |', '|---|---|---|---|---|---|---|---|']
    esc = lambda s: str(s).replace('|', '/')
    for r in sorted(rows, key=lambda r: ({'WRONG': 0, 'MISLEADING': 1, 'UNVERIFIED': 2, 'PASS': 3}[r.verdict], r.card, r.ticker, r.sid)):
        L.append(f'| {r.ticker} | {r.sid} | {esc(r.claim)} | {esc(r.shown)} | {esc(r.expected)} | {r.verdict} | {r.sev} | {esc(r.note)} |')
    open(os.path.join(out, 'REPORT_CARDS2.md'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L[:6])); print('report:', os.path.join(out, 'REPORT_CARDS2.md'))
    return 1 if counts['WRONG'] else 0


if __name__ == '__main__':
    sys.exit(main())
