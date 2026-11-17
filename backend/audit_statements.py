#!/usr/bin/env python3
"""Statement Audit (Day 126). Plan: docs/claude/design/STATEMENT_AUDIT_PLAN_DAY126.md. Protocol: MASTER_AUDIT_FRAMEWORK.md (Statement Audit).

  S1 source named, S2 number recomputed from raw bars (audit_ref.py, no app code), S3 words match the number (window dictionary + code constants),
  S4 outside reference (reported as UNVERIFIED unless one exists), S5 same claim, same value across cards.
Verdicts (framework labels): PASS | WRONG (number wrong, CRITICAL) | MISLEADING (number right, words wrong, HIGH) | UNVERIFIED.
Every number token on the Technical Read card text is claimed by a statement below or listed UNVERIFIED (exhaustive, Day 50 lesson).

Usage:  node ../frontend/scripts/dump_page_statements.js OUT TICKER...   then   venv/bin/python audit_statements.py OUT
"""
import json, os, re, sys, glob
from datetime import datetime
from typing import List
import audit_ref as R

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND = os.path.join(REPO, 'backend')

# ---------------------------------------------------------------- S3: window dictionary (counting rule: N-day = N bars; "N bars back" = iloc[-(N+1)])
def window_ok(words: str, bars_back: int, span_bars: int = None) -> bool:
    """Do the WORDS fit the window the code really uses? bars_back = how many bars before the last bar the comparison point is."""
    w = words.lower()
    m = re.search(r'(\d+)\s*(?:trading\s*)?(?:-day|days|sessions|bars)', w)
    if re.search(r'\ba month\b|1 month|one month|month ago', w) and not m:
        return 20 <= bars_back <= 23
    if re.search(r'past year|1-year|a year|52-week|52w|year ago', w):
        return 250 <= (span_bars if span_bars is not None else bars_back + 1) <= 253 or 250 <= bars_back <= 253
    if re.search(r'quarter|13-week|13w', w):
        return 62 <= bars_back <= 64
    if m:
        n = int(m.group(1))
        return bars_back == n or (span_bars is not None and span_bars == n)
    return False

# ---------------------------------------------------------------- helpers
class Row:
    def __init__(self, ticker, sid, card, claim, shown, expected, verdict, sev, note=''):
        self.ticker, self.sid, self.card, self.claim = ticker, sid, card, claim
        self.shown, self.expected, self.verdict, self.sev, self.note = shown, expected, verdict, sev, note

SEV = {'PASS': '', 'WRONG': 'CRITICAL', 'MISLEADING': 'HIGH', 'UNVERIFIED': 'INFO'}
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fnum = lambda s: float(s.rstrip('.').replace('−', '-').replace(',', '').replace('+', '').replace('$', '').replace('%', ''))
f2 = lambda x: 'n/a' if x is None else f'{x:.2f}'
from decimal import Decimal, ROUND_HALF_UP
def fm(x):
    """The page's one money format (frontend/src/utils/formatMoney.js): two decimals, half-up, thousands commas."""
    return f"{Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP):,}"
def near(a, b, tol): return a is not None and b is not None and abs(a - b) <= tol
def dlabel(d): y, m, dd = d.split('-'); return f"{MONTHS[int(m) - 1]} {int(dd)}"


class Audit:
    def __init__(self, dump):
        self.d = dump; self.t = dump['ticker']; self.rows: List[Row] = []
        p = dump['payloads']
        self.stock = (p.get('stock') or {}).get('body') or {}
        self.sr = (p.get('sr') or {}).get('body') or {}
        self.pat = (p.get('patterns') or {}).get('body') or {}
        self.quote = (p.get('quote') or {}).get('body') or {}
        self.spy = (p.get('spy') or {}).get('body') or {}
        ph = self.stock.get('priceHistory') or []
        self.dates = [b['date'] for b in ph]; self.c = [b['close'] for b in ph]; self.h = [b['high'] for b in ph]
        self.l = [b['low'] for b in ph]; self.v = [float(b['volume']) for b in ph]
        self.text = (dump.get('tr') or {}).get('text', '').replace('−', '-')
        self.work = self.text   # claimed spans are blanked out of this copy; what is left is scanned for number tokens

    def add(self, sid, claim, shown, expected, verdict, note='', card='Technical Read', sev=None):
        self.rows.append(Row(self.t, sid, card, claim, shown, expected, verdict, sev or SEV[verdict], note))

    def find(self, pattern, flags=0):
        m = re.search(pattern, self.text, flags)
        if m: self.work = self.work.replace(m.group(0), ' § ', 1)
        return m

    # ------------------------------------------------------------ the statements
    def run(self):
        if not self.text: self.add('X0', 'Technical Read card', 'not found', 'card text', 'UNVERIFIED', 'card did not render'); return
        c, h, l, v, n = self.c, self.h, self.l, self.v, len(self.c)
        if n < 30: self.add('X1', 'price history', f'{n} bars', 'at least 30', 'UNVERIFIED', 'too short to recompute'); return
        last = c[-1]
        tt = (self.pat.get('trendTemplate') or self.pat.get('trend_template') or {})

        # T1 trend checks N / 8
        m = self.find(r'Trend checks (\d) / (\d)')
        if m:
            shown = int(m.group(1))
            if n >= 252:
                s50, s150, s200 = R.sma(c, 50), R.sma(c, 150), R.sma(c, 200)
                s200ago = R.sma(c, 200, 30)
                hi, lo = max(h[-252:]), min(l[-252:])
                crit = [last > s50, last > s150, last > s200, s50 > s150, s150 > s200, s200 > s200ago, last >= lo * 1.30, last >= hi * 0.75]
                self.add('T1', 'Trend checks N / 8 (S1 pattern_detection.check_trend_template)', f'{shown} / {m.group(2)}', f'{sum(crit)} / 8',
                         'PASS' if shown == sum(crit) and m.group(2) == '8' else 'WRONG', 'recomputed all 8 criteria from the bars')
            else:
                self.add('T1', 'Trend checks N / 8', f'{shown} / {m.group(2)}', 'needs 252 bars', 'UNVERIFIED', f'only {n} bars')
        # T2 RSI
        m = self.find(r'Momentum \(RSI\) ([\d.]+)')
        if m:
            e = R.wilder_rsi(c)
            self.add('T2', 'RSI 14 (S1 frontend technicalIndicators RSI)', m.group(1), f'{e:.1f}', 'PASS' if near(float(m.group(1)), e, 0.3) else 'WRONG', 'Wilder 14 from closes (tolerance 0.3: 2-decimal closes)')
        # T3 vs S&P, "past year"
        m = self.find(r'vs S&P 500 ([+-]?[\d.]+)% vs ([+-]?[\d.]+)%')
        if m:
            sc = [b['close'] for b in (self.spy.get('priceHistory') or [])]
            def yr(cs): i = len(cs) - 252 if len(cs) >= 252 else (0 if len(cs) > 200 else None); return None if i is None else (pct(cs[-1], cs[i]), len(cs) - 1 - i)
            a, b = yr(c), yr(sc) if sc else None
            if a and b:
                ok = near(float(m.group(1)), a[0], 0.15) and near(float(m.group(2)), b[0], 0.15)
                self.add('T3', 'Stock vs S&P 500 return over the "past year" (S1 api.stock.price52wAgo + spy)', f'{m.group(1)}% vs {m.group(2)}%', f'{a[0]:.1f}% vs {b[0]:.1f}%', 'PASS' if ok else 'WRONG')
                span = [a[1] + 1, b[1] + 1]
                wok = all(window_ok('past year', s - 1, s) for s in span)
                self.add('T3w', 'words "past year" vs the window used', f'{a[1]} / {b[1]} bars back', '250-253 bars', 'PASS' if wok else 'MISLEADING',
                         '' if wok else 'history shorter than a year: the first bar stands in for the year-ago price (backend.py price52wAgo fallback)')
            else:
                self.add('T3', 'Stock vs S&P 500', f'{m.group(1)}% vs {m.group(2)}%', 'needs >200 bars each', 'UNVERIFIED')
        # T4 ADX
        m = self.find(r'Trend strength \(ADX\): ([\d.]+) · (20 or more|below 20)')
        if m:
            e = R.wilder_adx(h, l, c)
            cd = (self.sr.get('meta') or {}).get('candle') or {}
            e_forming = None
            if cd.get('barComplete') is False and self.sr.get('currentPrice') and cd.get('high') is not None:
                e_forming = R.wilder_adx(h + [cd['high']], l + [cd['low']], c + [self.sr['currentPrice']])
            shown_adx = float(m.group(1))
            if e is not None and near(shown_adx, e, 0.15):
                self.add('T4', 'ADX 14 (S1 /api/sr meta.adx)', m.group(1), f'{e:.1f}', 'PASS', 'Wilder, completed bars')
            elif e_forming is not None and near(shown_adx, e_forming, 0.15):
                self.add('T4', 'ADX 14 (S1 /api/sr meta.adx)', m.group(1), f'{e:.1f} on completed bars, {e_forming:.1f} with the forming bar', 'MISLEADING',
                         'math is right but it includes today\'s UNFINISHED bar (known Low: /api/sr keeps it); the trend rows below use the last close', sev='LOW')
                e = e_forming
            else:
                self.add('T4', 'ADX 14 (S1 /api/sr meta.adx)', m.group(1), f'{e:.1f}' if e is not None else 'n/a', 'WRONG', 'matches neither the completed-bar nor the forming-bar Wilder ADX')
            words_ok = (e is not None) and ((e >= 20) == m.group(2).startswith('20 or more'))
            edge = (not words_ok) and e is not None and abs(e - 20) < 0.05 and abs(shown_adx - 20) < 0.051
            self.add('T4w', 'words "20 or more / below 20"', m.group(2), f'ADX {e:.1f}' if e is not None else 'n/a', 'PASS' if words_ok else 'MISLEADING',
                     f'display rounding at the 20 line: ADX is {e:.2f}, the backend rounds it to 1 decimal before the card compares it' if edge else '', sev='LOW' if edge else None)
        # T5 counted at the last close
        m = self.find(r'counted at the last close \(\$([\d,.]+), ([A-Z][a-z]{2} \d+)\)')
        if m:
            ok = near(fnum(m.group(1)), last, 0.0051) and m.group(2) == dlabel(self.dates[-1])
            cent = (not ok) and near(fnum(m.group(1)), last, 0.0111) and m.group(2) == dlabel(self.dates[-1])
            self.add('T5', '"counted at the last close ($X, date)" = last completed bar', f'${m.group(1)}, {m.group(2)}', f'${last:.2f}, {dlabel(self.dates[-1])}', 'PASS' if ok else ('MISLEADING' if cent else 'WRONG'),
                     'one-cent disagreement between two data providers for the same close (e.g. Twelve Data 25.025 vs Yahoo 25.03); the header/quote path and the price bars can read different providers' if cent else '', sev='LOW' if cent else None)
        # T6-T8 averages rows
        for sid, nday, word in (('T6', 200, '200-day'), ('T7', 50, '50-day')):
            m = self.find(rf'(Above|Below) its {word} average.*?\$([\d,.]+) vs \$([\d,.]+) · ([+-]?[\d.]+)%')
            if m:
                s = R.sma(c, nday)
                ok = near(fnum(m.group(3)), s, 0.02) and near(fnum(m.group(2)), last, 0.0051) and near(float(m.group(4)), R.pct(last, s), 0.1)   # 0.1: the app divides by the 2-dp ROUNDED average (F: -12.745 vs -12.80 unrounded)
                self.add(sid, f'price vs {word} average (S1 pattern sma values)', f'${m.group(2)} vs ${m.group(3)} · {m.group(4)}%', f'${last:.2f} vs ${s:.2f} · {R.pct(last, s):.1f}%', 'PASS' if ok else 'WRONG')
                self.add(sid + 'w', f'word "{m.group(1)}"', m.group(1), 'Above' if last > s else 'Below', 'PASS' if (m.group(1) == 'Above') == (last > s) else 'MISLEADING')
        m = self.find(r'The 200-day average is (still rising|not rising).*?([+-]?[\d.]+)% over (\d+) trading days')
        if m:
            nb = int(m.group(3)); now, ago = R.sma(c, 200), R.sma(c, 200, nb)
            if ago:
                e = R.pct(now, ago)
                self.add('T8', '200-day average change over N trading days (S1 pattern sma_200_30d_ago)', f'{m.group(2)}% over {nb} td', f'{e:+.1f}% over {nb} td', 'PASS' if near(float(m.group(2)), e, 0.15) else 'WRONG')
                code_bars = 30   # pattern_detection.py: iloc[-31] (checked in the static S3 test below)
                self.add('T8w', 'words "N trading days" vs the bars back the code uses', f'{nb}', f'{code_bars}', 'PASS' if window_ok(f'{nb} trading days', code_bars) else 'MISLEADING')
                self.add('T8r', 'word "rising"', m.group(1), 'rising' if e > 0 else 'not rising', 'PASS' if (m.group(1) == 'still rising') == (e > 0) else 'MISLEADING')
        m = self.find(r'(Within 25% of|More than 25% below) its 1-year high.*?([\d.]+)% below the \$([\d,.]+) high')
        if m:
            hi = max(h[-252:]); pcth = (1 - last / hi) * 100
            self.add('T9', '1-year high = highest INTRADAY high of the last 252 bars (S1 pattern_detection high_52w)', f'{m.group(2)}% below ${m.group(3)}', f'{pcth:.1f}% below ${hi:.2f}',
                     'PASS' if near(fnum(m.group(3)), hi, 0.02) and near(float(m.group(2)), pcth, 0.06) else 'WRONG', 'closing high would be %.2f' % max(c[-252:]))
            self.add('T9w', 'words "Within 25% / More than 25%" vs the real gap', m.group(1), f'{pcth:.1f}% below', 'PASS' if (m.group(1).startswith('Within')) == (pcth <= 25) else 'MISLEADING')
            sh = self.stock.get('fiftyTwoWeekHigh')
            self.add('T9x', 'S5: same "1-year high" on Technical Read vs Price Data card (api fiftyTwoWeekHigh)', f'${m.group(3)}', f'${sh}', 'PASS' if near(fnum(m.group(3)), sh, 0.02) else 'MISLEADING', 'two different sources for the same word; Technical Read uses the max of the dividend-ADJUSTED bar highs, Price Data uses the raw Yahoo 52-week high (checked: F raw 17.78 vs adjusted 17.38)', card='Technical Read vs Price Data')

        # Entry checks: gauge + ladder
        g = self.d.get('gauge') or {}
        sent = (g.get('sentence') or '').replace('−', '-')
        m = re.search(r'\$([\d,.]+) \(([^)]+)\) is ([\d.]+)% (below|above) its 21-day average \(\$([\d,.]+)\)', sent) or re.search(r'\$([\d,.]+) \(([^)]+)\) is right at its 21-day average \(\$([\d,.]+)\)', sent)
        atr = None
        if m and len(c) >= 40:
            self.work = self.work.replace(sent.replace('-', '-'), ' § ')
            self.work = re.sub(r'\$[\d,.]+ \([^)]+\) is [^$]*? its 21-day average \(\$[\d,.]+\)', ' § ', self.work)
            q = self.quote
            live_ok = q.get('available') is True and q.get('session') != 'closed' and isinstance(q.get('price'), (int, float)) and q.get('price') > 0
            price = q['price'] if live_ok else last
            e21 = R.ema(c, 21); atr = R.wilder_atr(h, l, c)
            shown_p = fnum(m.group(1)); shown_e = fnum(m.group(m.lastindex))
            self.add('E1', 'compared price = live quote payload, else the last close (S1 api.quote.price); exact text in the one money format', f'${m.group(1)}', f'${fm(price)}', 'PASS' if m.group(1) == fm(price) else 'WRONG')
            hdr = (self.d.get('header') or {}).get('live-price') or ''
            mh = re.search(r'\$([\d,.]+)', hdr)
            if live_ok and mh:
                self.add('S5-price', 'S5: the same live price reads the same on the header and the Entry block', f'header ${mh.group(1)} / entry ${m.group(1)}', 'identical text', 'PASS' if mh.group(1) == m.group(1) else 'MISLEADING', 'two money formats used to disagree on half-cent prices', card='Header vs Technical Read')
            self.add('E2', '21-day average (EMA span 21 over closes; S1 frontend calculateEMA)', f'${shown_e}', f'${e21:.2f}', 'PASS' if near(shown_e, e21, 0.03) else 'WRONG', 'an EMA, so "21-day" is its span, not a 21-bar window')
            if m.lastindex >= 5:
                pe = R.pct(price, e21)
                self.add('E3', 'percent from the 21-day average', f'{m.group(3)}% {m.group(4)}', f'{abs(pe):.1f}% {"below" if pe < 0 else "above"}', 'PASS' if near(float(m.group(3)), abs(pe), 0.06) and m.group(4) == ('below' if pe < 0 else 'above') else 'WRONG')
            lbl = m.group(2)
            q_state = q.get('session') if live_ok else 'close'
            want = 'last close' if not live_ok else None
            if want: self.add('E3w', 'basis label when no usable live price', f'({lbl})', '(last close)', 'PASS' if lbl == 'last close' else 'MISLEADING')
            else: self.add('E3w', 'basis label for a live price (now / pre-market / after hours / last trade ...)', f'({lbl})', f'session={q_state}', 'PASS' if lbl != 'last close' else 'MISLEADING')
            sub = (g.get('sub') or '')
            ms = re.search(r'That is ([\d.]+) of a normal day.s move (below|above)? ?it\. A normal day.s move here is \$([\d,.]+)', sub.replace('−', '-'))
            if ms:
                self.work = re.sub(r"That is [\d.]+ of a normal day's move[^$]*?\$[\d,.]+\.", ' § ', self.work)
                du = abs(price - e21) / atr
                srv = (self.sr.get('meta') or {}).get('atr')
                self.add('E4', 'ATR ("a normal day\'s move"): Wilder 14 (S1 api.sr.meta.atr)', f'${ms.group(3).rstrip(".")}', f'${atr:.2f} (sr={srv})', 'PASS' if near(fnum(ms.group(3)), atr, 0.03) else 'WRONG', 'Wilder ATR14')
                self.add('E5', 'distance in normal day-moves', ms.group(1), f'{du:.1f}', 'PASS' if near(float(ms.group(1)), du, 0.06) else 'WRONG', 'gauge dot note uses the same number: ' + (g.get('dotNote') or ''))
        # ladder
        lad = g.get('ladder') or []
        if lad and m:
            for r in lad:
                nd = {'sma50': 50, 'sma200': 200, 'ema21': None}[r['key']]
                exp = R.sma(c, nd) if nd else R.ema(c, 21)
                gap = (price / exp - 1) * 100 if exp else None
                okp = near(float(r['price']), exp, 0.03)
                okg = r['gap'] not in ('', None) and near(float(r['gap']), gap, 0.11)
                self.add('L-' + r['key'], f'ladder row {r["key"]}: price and gap = price vs average', f'${r["price"]}, {r["gap"]}%', f'${exp:.2f}, {gap:.1f}%', 'PASS' if okp and okg else 'WRONG')
            now = g.get('now') or {}
            self.add('L-now', 'ladder price row = compared price; name = the basis label', f'${now.get("price")} "{now.get("name")}"', f'${price:.2f} "{(m.group(2) or "").lower()}"',
                     'PASS' if near(float(now.get('price', 0)), price, 0.0051) and (now.get('name') or '').lower() == m.group(2).lower() else 'MISLEADING')
            cn = g.get('closeNote')
            if cn:
                good = cn.startswith(f'Last close ${last:.2f}') and dlabel(self.dates[-1]) in cn
                mc = re.match(r'Last close \$([\d,.]+)', cn)
                cent = (not good) and mc and near(fnum(mc.group(1)), last, 0.0111) and dlabel(self.dates[-1]) in cn
                self.add('L-note', '"Last close $X · date" note = last completed bar', cn, f'${last:.2f} · {dlabel(self.dates[-1])}', 'PASS' if good else ('MISLEADING' if cent else 'WRONG'),
                         'one-cent disagreement between two data providers for the same close' if cent else '', sev='LOW' if cent else None)
            # ladder text in the card, claim all
            self.work = re.sub(r'Line Price Price against it.*?(?=why\? ⓘ)', ' § ', self.work, flags=re.S)
            self.work = re.sub(r'\[Gauge:[^\]]*\]', ' § ', self.work)
            self.work = re.sub(r'\$[\d,.]+ · [\d.]+ day-moves (?:below|above|from it)', ' § ', self.work)
            self.work = re.sub(r'Last close \$[\d,.]+ · [A-Z][a-z]{2} \d+', ' § ', self.work)
            self.work = re.sub(r"A \"day's move\" is the stock's ATR \(\$[\d,.]+ here\)", ' § ', self.work)
        # Volume signals
        i = len(c) - 1
        lastbar_complete = (self.sr.get('meta') or {}).get('candle', {}).get('barComplete') is not False
        vi = i if lastbar_complete else i  # the page's /api/stock already ends at the last completed bar (Day 126)
        chg = R.pct(c[vi], c[vi - 1]); loc = (c[vi] - l[vi]) / (h[vi] - l[vi]) if h[vi] > l[vi] else None
        avg50 = sum(v[vi - 49:vi + 1]) / 50 if vi >= 49 else None
        rv = v[vi] / avg50 if avg50 else None
        m = self.find(r'(\d) volume signals?: (?:(\d) up)?,? ?(?:(\d) down)?,? ?(?:(\d) flat)?')
        obv = R.obv_trend(c[:vi + 1], v[:vi + 1])
        votes = []
        if abs(chg) > 0.0 and True:
            votes.append(1 if chg > 0.1 else -1 if chg < -0.1 else 0)   # the app's flat band is +/-0.1% (volumeThresholds DAY_CHANGE_FLAT_PCT)
        if loc is not None: votes.append(1 if loc >= 0.75 else -1 if loc <= 0.25 else 0)
        if obv: votes.append(1 if obv == 'rising' else -1 if obv == 'falling' else 0)
        if m:
            sh = f'{m.group(1)} signals, {m.group(2) or 0} up, {m.group(3) or 0} down, {m.group(4) or 0} flat'
            ex = f'{len(votes)} signals, {votes.count(1)} up, {votes.count(-1)} down, {votes.count(0)} flat'
            vr = list(votes)
            if loc is not None and len(vr) >= 2:      # the app compares the 2-decimal close location to the 0.25 / 0.75 thresholds
                rl = round(loc + 1e-9, 2); vr[1 if abs(chg) > 0 else 0] = 1 if rl >= 0.75 else -1 if rl <= 0.25 else 0
            exr = f'{len(vr)} signals, {vr.count(1)} up, {vr.count(-1)} down, {vr.count(0)} flat'
            if sh == ex: self.add('V1', 'volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead)', sh, ex, 'PASS', f'change {chg:.2f}%, close location {f2(loc)}, OBV {obv}')
            elif sh == exr: self.add('V1', 'volume signal tally', sh, ex, 'MISLEADING', f'borderline: close location {loc:.4f} is just above 0.25 but the app rounds it to 0.25 before comparing (display rounding at a threshold)', sev='LOW')
            else: self.add('V1', 'volume signal tally from the last completed bar (S1 volumeThresholds.getVolumeDirectionRead)', sh, ex, 'WRONG', f'change {chg:.2f}%, close location {f2(loc)}, OBV {obv}')
        m = self.find(r'closed (up|down) ([\d.]+)%')
        self.work = re.sub(r'closed (up|down) [\d.]+%', ' § ', self.work)   # the Lean line repeats it
        if m: self.add('V2', 'day change of the last completed bar', f'{m.group(1)} {m.group(2)}%', f'{chg:+.2f}%', 'PASS' if near(float(m.group(2)) * (1 if m.group(1) == 'up' else -1), chg, 0.06) else 'WRONG')
        m = self.find(r"(settled near the day's high|near the day's low)")
        if m:
            good = loc is not None and (('high' in m.group(1)) == (loc >= 0.75) and ('low' in m.group(1)) == (loc <= 0.25))
            borderline = loc is not None and not good and (('high' in m.group(1)) == (round(loc + 1e-9, 2) >= 0.75) and ('low' in m.group(1)) == (round(loc + 1e-9, 2) <= 0.25))
            self.add('V3', 'close location words (>=0.75 high, <=0.25 low)', m.group(1), f'close location {f2(loc)}' + (f' (raw {loc:.4f})' if loc is not None else ''),
                     'UNVERIFIED' if loc is None else ('PASS' if good else 'MISLEADING'), 'display rounding at the threshold: raw value is just outside' if borderline else '', sev='LOW' if borderline else None)
        # no real volume history (same rule as the app: fewer than 40 of the last 50 completed bars with volume > 0)
        days_with = sum(1 for x in v[-50:] if x and x > 0)
        no_volume = len(v) >= 1 and days_with < 40
        mnv = re.search(r'No volume data: the data source reports no shares traded on (\d+) of the last (\d+) days', self.text)
        shows_numbers = any(re.search(p, self.text) for p in (r'× normal volume', r'volume signals?:', r'Last session \(', r'Last \d+ days · green up day'))
        if no_volume:
            if mnv and not shows_numbers:
                ok_n = int(mnv.group(1)) == 50 - days_with
                self.add('Z1', 'no volume data: the card says so (and the count of empty days is right) and shows no volume numbers', f'{mnv.group(1)} of {mnv.group(2)} days empty', f'{50 - days_with} of 50 days empty', 'PASS' if ok_n else 'WRONG')
                self.work = self.work.replace(mnv.group(0), ' § ')
                self.work = re.sub(r'Volume behind the move.*?left out\.', ' § ', self.work)
            else:
                self.add('Z1', 'volume statements shown although fewer than 40 of the last 50 completed days have volume', 'volume numbers shown', 'volume unavailable', 'WRONG', 'see TechnicalRead.jsx pickVolumeBar / backend meta.volume', sev='CRITICAL')
        elif mnv:
            self.add('Z1', '"No volume data" shown although the bars have volume', mnv.group(0), f'{days_with} of 50 days have volume', 'WRONG')
        m = self.find(r'OBV (rising|falling|flat)')
        if m:
            srt = ((self.sr.get('meta') or {}).get('obv') or {}).get('trend')
            self.add('V4', 'OBV direction (20-bar OBV vs its average, +/-2% band)', m.group(1), f'{obv} (sr says {srt})', 'PASS' if obv == m.group(1) else 'WRONG')
        m = self.find(r'([\d.]+)× normal volume · from the ([\d-]+) session')
        if m:
            self.add('V5', 'relative volume = last bar volume / mean of the last 50 bars (S1 sr.meta.rvol)', f'{m.group(1)}× from {m.group(2)}', f'{f2(rv)}× from {self.dates[vi]}', 'PASS' if rv is not None and near(float(m.group(1)), rv, 0.06) and m.group(2) == self.dates[vi] else 'WRONG', 'window "50 bars" includes the bar itself')
        m = self.find(r'Last session \(([\d-]+)\): ([\d.]+)× the 50-day average')
        if m: self.add('V6', 'Volume detail: last session date and RVOL', f'{m.group(1)} {m.group(2)}×', f'{self.dates[vi]} {f2(rv)}×', 'PASS' if rv is not None and m.group(1) == self.dates[vi] and near(float(m.group(2)), rv, 0.011) else 'WRONG')
        m = self.find(r'Effort vs\. result: ([\d.]+)× volume for ([\d.]+)× its own ATR')
        if m:
            atrs = (self.sr.get('meta') or {}).get('atr') or atr
            prog = abs(chg) / (atrs / last * 100) if atrs else None
            self.add('V7', 'effort vs result: RVOL and |day change| / (ATR / price)', f'{m.group(1)}× / {m.group(2)}×', f'{f2(rv)}× / {f2(prog)}×', 'PASS' if rv is not None and near(float(m.group(1)), rv, 0.011) and prog and near(float(m.group(2)), prog, 0.03) else 'WRONG', 'ATR % uses the sr price (may be a partial bar)')
        # 20 volume bars (titles)
        bars = re.findall(r'\[(\d{4}-\d{2}-\d{2}): ([\d,]+)\]', self.text)
        if bars:
            self.work = re.sub(r'\[\d{4}-\d{2}-\d{2}: [\d,]+\]', ' ', self.work)
            exp = list(zip(self.dates[-20:], [int(x) for x in v[-20:]]))
            got = [(d, int(x.replace(',', ''))) for d, x in bars]
            self.add('V8', '"Last 20 days" volume bars = the last 20 completed bars (dates and volumes)', f'{len(got)} bars, last {got[-1]}', f'20 bars, last {exp[-1]}', 'PASS' if got == exp else 'WRONG')
        for mm in re.finditer(r'(21d|50d|200d)\s*[◂▸]?\s*([+-]\d+\.\d)', self.text):
            key = {'21d': 'ema21', '50d': 'sma50', '200d': 'sma200'}[mm.group(1)]
            avg = R.ema(c, 21) if key == 'ema21' else R.sma(c, 50 if key == 'sma50' else 200)
            if atr and avg:
                du = (avg - R.ema(c, 21)) / atr
                self.add('E6', f'off-scale gauge label {mm.group(1)}: real distance in day-moves from the 21-day average', mm.group(2), f'{du:+.1f}', 'PASS' if near(float(mm.group(2)), du, 0.06) else 'WRONG')
        self.work = re.sub(r'(21d|50d|200d)\s*[◂▸]?\s*[+-]\d+\.\d', ' § ', self.work)
        mm = re.search(r'last completed session, (\d{4}-\d{2}-\d{2})', self.text)
        if mm:
            self.add('V10', '"last completed session, <date>" = the last completed bar', mm.group(1), self.dates[-1], 'PASS' if mm.group(1) == self.dates[-1] else 'WRONG')
            self.work = self.work.replace(mm.group(0), ' § ')
        # statements with a word-claim whose rule is not mirrored yet
        for pat, why in ((r'Heavy volume while On-Balance Volume is falling[^.]*\.', 'condition: RVOL >= 1.5 and OBV falling'),
                         (r'Last 20 days: [^—]*— [^D]*?(?=Direction|$)', 'OBV 20-day divergence sentence (backend calculate_obv signal text)'),
                         (r'Effort vs\. result:.*?not backtested\)', 'effort/result wording thresholds 0.5 / 1.0 ATR and 1.5x RVOL')):
            mm = re.search(pat, self.text, re.S)
            if mm:
                if 'Heavy volume' in pat:
                    ok = (rv or 0) >= 1.5 and obv == 'falling'
                    self.add('V9', 'caution sentence "heavy volume while OBV is falling" fires only when RVOL >= 1.5 and OBV falling', f'shown, RVOL {f2(rv)}, OBV {obv}', 'condition true' if ok else 'condition false', 'PASS' if ok else 'MISLEADING')
                    self.work = self.work.replace(mm.group(0), ' § ')
                else:
                    self.add('V-effort' if 'Effort' in pat else 'V-obv20', why, 'shown', 'rule not mirrored in the audit yet', 'UNVERIFIED', 'sentence logic not recomputed; the numbers inside it are claimed above where possible')
        # dates in copy
        # ---------------------------------------------------------------- unclaimed numbers (exhaustive scan)
        EXEMPT = [r'rule of thumb: \d\+', r'50–70', r'between 50 and 70', r'20 or more', r'Below 20', r'the 4 below plus 4 more', r'the 4 listed', r'the other 4', r'Why only 4 checks',
                  r'8 checks', r'at least 7 of 8', r'7 of 8', r'the 21, 50 and 200-day', r'21, 50 and 200-day averages', r'21-day', r'50-day', r'200-day', r'1-year', r'20-day', r'3 day',
                  r'about a month', r'Is it in an uptrend\?', r'8 trend', r'6 of 8', r'first-principles', r'Wyckoff', r'O.Neil', r'Livermore', r'Minervini', r'Day \d+', r'rule of thumb',
                  r'Trend, momentum', r'The three', r'the 3 ', r'S&P 500', r'ATR', r'\b3 volume', r'20 sessions', r'20 days', r'\b21d\b|\b50d\b|\b200d\b', r'ADX measures', r'25%', r'a day.s move']
        rest = self.work
        for e in EXEMPT: rest = re.sub(e, ' ', rest, flags=re.I)
        toks = [t for t in re.findall(r'-?\$?\d[\d,]*\.?\d*%?×?', rest)]
        toks = [t for t in toks if t.strip('-$,.%×')]
        self.rest_debug = rest
        if toks: self.add('U1', 'numbers on the card no statement above claimed (exhaustive scan)', ' '.join(toks[:40]) + (' ...' if len(toks) > 40 else ''), 'each one claimed or exempt', 'UNVERIFIED', f'{len(toks)} unclaimed number token(s): add a statement or an exempt rule')
        return self


def static_s3() -> List[Row]:
    """S3-static: the words in the UI vs the constants in the code (fails for every ticker, every day, if wrong)."""
    rows = []
    def src(p): return open(os.path.join(REPO, p), encoding='utf-8').read()
    pd_src, tr_src, be = src('backend/pattern_detection.py'), src('frontend/src/utils/technicalReadChecks.js'), src('backend/backend.py')
    m = re.search(r'sma_200_30d_ago\s*=\s*calculate_sma\(close, 200\)\.iloc\[-(\d+)\]', pd_src)
    bars_back = int(m.group(1)) - 1 if m else None
    mw = re.search(r'over (\d+) trading days', tr_src)
    ui_n = int(mw.group(1)) if mw else None
    ok = bars_back is not None and ui_n is not None and window_ok(f'{ui_n} trading days', bars_back)
    rows.append(Row('-', 'S3-1', 'Technical Read', '200-day rising: UI words vs code window', f'UI says {ui_n} trading days', f'code iloc[-{bars_back+1}] = {bars_back} bars back', 'PASS' if ok else 'MISLEADING', SEV['PASS' if ok else 'MISLEADING']))
    rows.append(Row('-', 'S3-2', 'Technical Read', 'REGRESSION: "a month ago" next to 30 bars back must be rejected', 'window_ok("a month ago", 30)', 'False', 'PASS' if not window_ok('a month ago', 30) else 'WRONG', SEV['PASS' if not window_ok('a month ago', 30) else 'WRONG']))
    ui_has_month = bool(re.search(r"from a month ago|over a month|a month ago", tr_src))
    rows.append(Row('-', 'S3-3', 'Technical Read', 'no "a month" wording left in technicalReadChecks.js next to the 30-bar window', 'found' if ui_has_month else 'none', 'none', 'PASS' if not ui_has_month else 'MISLEADING', SEV['PASS' if not ui_has_month else 'MISLEADING']))
    m = re.search(r'high_52w = df\[.High.\]\.tail\((\d+)\)\.max\(\)', pd_src)
    rows.append(Row('-', 'S3-4', 'Technical Read', '"1-year high": code window', f'tail({m.group(1) if m else "?"})', '250-253 bars', 'PASS' if m and window_ok('1-year high', int(m.group(1))-1, int(m.group(1))) else 'MISLEADING', SEV['PASS' if m and window_ok('1-year high', int(m.group(1))-1, int(m.group(1))) else 'MISLEADING']))
    m = re.search(r'price_52w_ago = round\(float\(_val\), 2\)[^\n]*\n[^\n]*\n[^\n]*\n[^\n]*', be)
    m2 = re.search(r'_closes\.iloc\[-(\d+)\]', be)   # Day 126: the year-ago close is now read from the non-NaN closes
    rows.append(Row('-', 'S3-5', 'Technical Read', '"past year" return: year-ago bar', f'iloc[-{m2.group(1) if m2 else "?"}]', '250-253 bars span', 'PASS' if m2 and window_ok('past year', int(m2.group(1)) - 1, int(m2.group(1))) else 'MISLEADING', SEV['PASS' if m2 and window_ok('past year', int(m2.group(1)) - 1, int(m2.group(1))) else 'MISLEADING']))
    m = re.search(r'def calculate_obv\(close[^)]*lookback: int = (\d+)', be)
    rows.append(Row('-', 'S3-6', 'Technical Read', '"Last 20 days" / "20-day On-Balance Volume": OBV lookback', f'lookback={m.group(1) if m else "?"}', '20 bars', 'PASS' if m and m.group(1) == '20' else 'MISLEADING', SEV['PASS' if m and m.group(1) == '20' else 'MISLEADING']))
    doc = re.search(r'200-day SMA trending up for at least 1 month', pd_src)
    rows.append(Row('-', 'S3-7', 'Docs (pattern_detection.py docstring)', '"at least 1 month" vs the 30-trading-day code', 'docstring says 1 month' if doc else 'fixed', '30 trading days', 'MISLEADING' if doc else 'PASS', SEV['MISLEADING' if doc else 'PASS'], 'not page text; logged for the Coherence audit'))
    return rows


def main():
    out = sys.argv[1]
    dumps = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(out, 'dump_*.json')))]
    rows: List[Row] = static_s3()
    for d in dumps: rows += Audit(d).run().rows
    counts = {k: sum(1 for r in rows if r.verdict == k) for k in SEV}
    lines = [f"# Statement Audit report", '', f"Run: {datetime.now().isoformat(timespec='minutes')} · dumps: {', '.join(d['ticker'] for d in dumps)} · ET at first dump: {dumps[0].get('etNow') if dumps else 'n/a'}", '',
             f"Verdicts: PASS {counts['PASS']} · WRONG {counts['WRONG']} (CRITICAL) · MISLEADING {counts['MISLEADING']} (HIGH) · UNVERIFIED {counts['UNVERIFIED']} (INFO)", '',
             'Scope: Technical Read card (full text scan) + the gauge and ladder + header price lines via the card text. NOT YET COVERED: earnings badge, sector badge, Trade Setup, Breakout, S&R levels, MR Read, Price Data, Relative Strength, Fundamentals, Market backdrop, Data Sources.',
             'S4 (outside reference): none run here; closes vs IBKR/other providers belong to the data-source audit (C3/C9) and are UNVERIFIED for these tickers unless listed there.', '',
             '| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |', '|---|---|---|---|---|---|---|---|']
    for r in sorted(rows, key=lambda r: ({'WRONG': 0, 'MISLEADING': 1, 'UNVERIFIED': 2, 'PASS': 3}[r.verdict], r.ticker, r.sid)):
        esc = lambda s: str(s).replace('|', '/')
        lines.append(f"| {r.ticker} | {r.sid} | {esc(r.claim)} | {esc(r.shown)} | {esc(r.expected)} | {r.verdict} | {r.sev} | {esc(r.note)} |")
    open(os.path.join(out, 'REPORT.md'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[:6])); print(f'report: {os.path.join(out, "REPORT.md")}')
    return 1 if counts['WRONG'] or counts['MISLEADING'] else 0


def pct(a, b): return (a / b - 1) * 100

if __name__ == '__main__':
    sys.exit(main())
