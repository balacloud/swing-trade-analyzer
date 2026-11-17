#!/usr/bin/env python3
"""Statement Audit phase 2 (Day 126): Trade Setup (+ key levels), Breakout, Price Data, Relative Strength, header badges.
Plan: docs/claude/design/STATEMENT_AUDIT_PHASE2_PLAN_DAY126.md (§5 = Opus review applied). Protocol: MASTER_AUDIT_FRAMEWORK Part 7.
A subclass of the phase-1 Audit: its machinery (rows, verdicts, claimed-span scan) is reused and phase-1 code is untouched.

Usage: venv/bin/python audit_cards.py OUT_DIR      (reads OUT_DIR/dump_*.json from dump_page_statements.js, writes OUT_DIR/REPORT_CARDS.md)
"""
import glob, json, os, re, sys
from datetime import datetime
import audit_ref as R
import audit_statements as A
from audit_statements import Audit, fm, near, f2, dlabel, MONTHS
fnum_ = lambda t: float(str(t).replace(',', '').replace('$', ''))

SW = 5            # swing wing (bars each side), simple_sr.DAILY_WING
LOOK = 252        # swing lookback, simple_sr.DAILY_LOOKBACK
MERGE, MAXZ = 0.5, 1.0   # ATR multiples, simple_sr.MERGE_ATR / MAX_ZONE_ATR
NEAR_HIGH = 3.0   # percent, simple_sr.NEAR_HIGH_PCT


# ------------------------------------------------------------------ reference: support/resistance from the plain-words rules (simple_sr docstring)
def ref_swings(h, l, dates):
    """Loop-based, from the words: a bar whose high (low) is the highest (lowest) of the 5 bars each side (ties count); equal 2-dp prices
    within 11 bars count once, keeping the later date; only the last 252 bars are kept."""
    n, out = len(h), []
    first_kept = max(0, n - LOOK)
    for kind, arr, pick in (('high', h, max), ('low', l, min)):
        kept = []
        for p in range(SW, n - SW):
            if p < first_kept:
                continue
            win = arr[p - SW:p + SW + 1]
            if (arr[p] >= pick(win)) if kind == 'high' else (arr[p] <= pick(win)):
                if kept and round(kept[-1]['price'], 2) == round(arr[p], 2) and p - kept[-1]['pos'] < 2 * SW + 1:
                    kept[-1].update(pos=p, date=dates[p]); continue
                kept.append({'price': arr[p], 'kind': kind, 'pos': p, 'date': dates[p]})
        out += kept
    return out


def ref_zones(swings, atr):
    zones = []
    for s in sorted(swings, key=lambda x: x['price']):
        z = zones[-1] if zones else None
        if z and s['price'] - z['last'] <= MERGE * atr and s['price'] - z['low'] <= MAXZ * atr:
            z['high'] = z['last'] = s['price']; z['members'].append(s)
        else:
            zones.append({'low': s['price'], 'high': s['price'], 'last': s['price'], 'members': [s]})
    return zones


def state_words(price, res, sup, tt, adx, atr, res_pct, sup_pct, inside):
    """The key-levels one-line price state, re-derived from the numbers (frontend/src/utils/keyLevels.js deriveStructureState)."""
    if price is None or tt is None: return None
    above = [x for x in res if x > price]; below = [x for x in sup if x < price]
    R1 = min(above) if above else None
    S1 = price if inside else (max(below) if below else None)
    near_ = lambda lv: lv is not None and atr and abs(price - lv) <= 2.0 * atr
    if R1 is None and S1 is None: return 'Insufficient data'
    if R1 is None: return f'No resistance within {res_pct}% above · {tt} of 8 trend checks pass'
    if S1 is None: return f'No support within {sup_pct}% below'
    if near_(R1) and near_(S1): return 'Close to both support and resistance'
    if tt >= 7: return 'Uptrend testing resistance' if near_(R1) else 'Uptrend pulling back to support' if near_(S1) else 'Uptrend — between levels'
    if tt >= 4: return 'Weakening trend — testing support' if near_(S1) else 'Transitioning — testing resistance' if near_(R1) else 'Mixed trend — between levels'
    if adx is None: return None
    return f'{tt} of 8 trend checks pass · ADX {adx:.1f}, under 15' if adx < 15 else f'{tt} of 8 trend checks pass · ADX {adx:.1f}'


class CardAudit(Audit):
    def __init__(self, dump):
        super().__init__(dump)
        self.cards = dump.get('cardTexts') or {}
        self.coverage = {}            # card -> [claimed tokens, unclaimed tokens]

    # --------------------------------------------------------------- per-card text handling
    def use(self, card_id):
        self.cur = card_id
        self.text = (self.cards.get(card_id) or '').replace('−', '-')
        self.work = self.text
        return bool(self.text)

    def addc(self, sid, claim, shown, expected, verdict, note='', sev=None):
        names = {'card-trade-setup': 'Trade Setup', 'card-breakout': 'Breakout', 'card-price-data': 'Price Data',
                 'card-relative-strength': 'Relative Strength', 'card-stock-header': 'Header'}
        self.add(sid, claim, shown, expected, verdict, note, card=names.get(self.cur, self.cur), sev=sev)

    def unclaimed(self, exempt, label):
        rest = self.work
        for e in exempt: rest = re.sub(e, ' ', rest, flags=re.I)
        toks = [t for t in re.findall(r'-?\$?\d[\d,]*\.?\d*%?×?', rest) if t.strip('-$,.%×')]
        self.coverage[self.cur] = (len(re.findall('§', self.work)), len(toks))
        if toks:
            self.addc('U-' + label, 'numbers on the card no statement claimed (exhaustive scan)', ' '.join(toks[:30]) + (' ...' if len(toks) > 30 else ''),
                      'each one claimed or exempt', 'UNVERIFIED', f'{len(toks)} unclaimed number token(s)')

    # --------------------------------------------------------------- entry point
    def run_cards(self):
        c = self.c
        if len(c) < 60:
            self.add('X1', 'cards', f'{len(c)} bars', 'at least 60', 'UNVERIFIED', 'too short to recompute', card='all'); return self
        self.trade_setup(); self.breakout(); self.price_data(); self.relative_strength(); self.header()
        return self

    # --------------------------------------------------------------- Trade Setup + key levels
    def trade_setup(self):
        sr, meta = self.sr, (self.sr.get('meta') or {})
        have_payload = bool(sr) and isinstance(sr.get('support'), list)
        if not self.use('card-trade-setup'):
            if have_payload: self.addc('TS0', 'Trade Setup card present when /api/sr answered', 'card not found', 'card text', 'WRONG')
            return
        c, h, l, v = self.c, self.h, self.l, self.v
        price = sr.get('currentPrice'); atr_p = meta.get('atr'); zones = meta.get('zones') or []
        sup = [x for x in (sr.get('support') or []) if isinstance(x, (int, float))]
        last_close = c[-1]
        atr_ref = R.wilder_atr(h, l, c)
        self.addc('TS-atr', 'ATR in the payload = Wilder ATR14 from the bars (the stop uses the payload value exactly)', f'{atr_p}', f'{atr_ref:.4f}', 'PASS' if atr_p and near(atr_p, atr_ref, 0.02) else 'WRONG')

        # The card measures from the last COMPLETED close (Day 126 fix); /api/sr's currentPrice is today's live bar and only decides which side of price a zone is on
        if price is not None and not near(price, last_close, 0.005):
            self.addc('TS-live-side', 'levels are placed on a side of price using /api/sr currentPrice (today\'s live bar), the card\'s words use the last close', f'sr price ${fm(price)}', f'last close ${fm(last_close)}', 'UNVERIFIED',
                      'a zone between the two prices can sit on a different side than the words say; mid-session only (known Low)')
        price_card = last_close

        if not sup:
            m = re.search(r"No support level below|no pullback plan", self.text)
            self.addc('TS1', 'no support level: the card says there is no plan', 'says so' if m else 'no such sentence', 'says so', 'PASS' if m else 'WRONG')
        else:
            entry = max(sup)
            m = re.search(r'BUY \$([\d,.]+)(?: CLOSE)? \$([\d,.]+)(?: \$([\d,.]+))?', self.text)
            mb = re.search(r'Buy \$([\d,.]+) (support, ([\d.]+)% (below|above) the last close|top of the support zone; price is inside it at the last close)', self.text)
            if mb:
                self.work = self.work.replace(mb.group(0), ' § ', 1)
                self.addc('TS1', 'Buy = the nearest support edge (S1 /api/sr support, max)', f'${mb.group(1)}', f'${fm(entry)}', 'PASS' if mb.group(1) == fm(entry) else 'WRONG')
                nearest_sup = next((z for z in zones if z.get('nearest') and z.get('side') == 'support'), None)
                if nearest_sup:
                    ok = near(nearest_sup['high'], entry, 0.005)
                    self.addc('TS1b', 'S5: the Buy equals the edge of the zone flagged nearest (Support row)', f'buy {entry}, nearest zone high {nearest_sup["high"]}', 'equal', 'PASS' if ok else 'WRONG',
                              '' if ok else 'the Buy and the Support row disagree (inside-zone + width-cap split)')
                if mb.group(3):
                    pe = (entry - price_card) / price_card * 100
                    exp = f'{abs(pe):.1f}% {"below" if pe <= 0 else "above"}'
                    self.addc('TS2', '"x% below/above the last close" = distance from the buy to the last COMPLETED close (S5 with the header)', f'{mb.group(3)}% {mb.group(4)}', exp, 'PASS' if pe is not None and near(float(mb.group(3)), abs(pe), 0.06) and mb.group(4) == ('below' if pe <= 0 else 'above') else 'WRONG')
                else:
                    ins = any(z.get('insideZone') and z.get('nearest') for z in zones)
                    self.addc('TS2', '"price is inside it" = a nearest support zone with insideZone', 'inside wording', f'insideZone={ins}', 'PASS' if ins else 'MISLEADING')
            else:
                self.addc('TS1', 'Buy box not found although a support exists', 'missing', f'${fm(entry)}', 'WRONG')
            if m:
                self.work = self.work.replace(m.group(0), ' § ', 1)
                self.addc('TS1c', 'S5: the Buy on the bar = the Buy in the box', f'${m.group(1)}', f'${fm(entry)}', 'PASS' if m.group(1) == fm(entry) else 'WRONG')
            if atr_p and atr_p > 0:
                stop_raw = max(0.01, entry - 2 * atr_p)
                ms = re.search(r'Stop \$([\d,.]+) ([+-][\d.]+)% from the buy · (2 ATR below|floored at \$0\.01)', self.text)
                if ms:
                    self.work = self.work.replace(ms.group(0), ' § ', 1)
                    ok = ms.group(1) == fm(stop_raw) and near(float(ms.group(2)), (stop_raw - entry) / entry * 100, 0.06)
                    self.addc('TS3', 'Stop = buy - 2 x ATR (floored at $0.01) and its % from the buy', f'${ms.group(1)} {ms.group(2)}%', f'${fm(stop_raw)} {(stop_raw - entry) / entry * 100:+.1f}%', 'PASS' if ok else 'WRONG')
                    self.addc('TS3w', 'words "2 ATR below" vs "floored"', ms.group(3), 'floored' if stop_raw <= 0.01 else '2 ATR below', 'PASS' if (ms.group(3).startswith('floored')) == (stop_raw <= 0.01) else 'MISLEADING')
                elif entry:
                    self.addc('TS3', 'Stop box not found', 'missing', f'${fm(stop_raw)}', 'WRONG')
                tgt = sr.get('suggestedTarget')
                mt = re.search(r'Target \$([\d,.]+) ([+-][\d.]+)% from the buy · nearest resistance', self.text)
                mnt = re.search(r'Target — (no resistance above, the stock is (?:at|near) its 52-week high(?: \(within 3%\))?|no resistance within (\d+)% above)', self.text)
                if tgt is not None and mt:
                    self.work = self.work.replace(mt.group(0), ' § ', 1)
                    self.addc('TS4', 'Target = nearest resistance edge and its % from the buy', f'${mt.group(1)} {mt.group(2)}%', f'${fm(tgt)} {(tgt - entry) / entry * 100:+.1f}%',
                              'PASS' if mt.group(1) == fm(tgt) and near(float(mt.group(2)), (tgt - entry) / entry * 100, 0.06) else 'WRONG')
                elif tgt is None and mnt:
                    self.work = self.work.replace(mnt.group(0), ' § ', 1)
                    hi52 = max(h[-252:]); gap = (1 - price_card / hi52) * 100
                    if ' 52-week high' in mnt.group(1):
                        at_word = 'at its 52-week high' in mnt.group(1)
                        ok = gap <= (1.0 if at_word else NEAR_HIGH + 0.05)
                        self.addc('TS4w', 'words "at/near its 52-week high" vs the real gap to the 252-bar high', 'at' if at_word else 'near, within 3%', f'{gap:.1f}% below the high ${fm(hi52)}',
                                  'PASS' if ok else 'MISLEADING', '' if ok else 'the rule is "within 3%" (simple_sr NEAR_HIGH_PCT); "at" overstates, and Price Data shows the real gap')
                    else:
                        self.addc('TS4', '"no resistance within N% above" vs the proximity filter', mnt.group(2) + '%', f"{round((meta.get('proximityFilter') or {}).get('resistancePct', .3) * 100)}%", 'PASS')
                elif tgt is not None and not mt:
                    self.addc('TS4', 'Target box not found although a resistance exists', 'missing', f'${fm(tgt)}', 'WRONG')
                rr = ((tgt - entry) / (entry - stop_raw)) if (tgt is not None and entry - stop_raw > 0) else None
                mr = re.search(r'(?:reward : risk|—|[\d.]+ : 1 reward : risk)', self.text)
                mrr = re.search(r'([\d.]+) : 1 reward : risk', self.text)
                if rr is not None:
                    self.addc('TS5', 'reward : risk = (target - buy) / (buy - stop)', f'{mrr.group(1)} : 1' if mrr else 'none', f'{rr:.1f} : 1', 'PASS' if mrr and near(float(mrr.group(1)), rr, 0.06) else 'WRONG')
                    if mrr: self.work = self.work.replace(mrr.group(0), ' § ', 1)
                elif mrr:
                    self.addc('TS5', 'reward : risk shown although there is no target', mrr.group(0), 'none', 'WRONG')
                risk = entry - stop_raw
                mk = re.search(r'Risk \$([\d,.]+) to make \$([\d,.]+) a share|Risk \$([\d,.]+) a share', self.text)
                if mk:
                    self.work = self.work.replace(mk.group(0), ' § ', 1)
                    r_txt = mk.group(1) or mk.group(3)
                    ok = r_txt == fm(risk) and (tgt is None or (mk.group(2) == fm(tgt - entry)))
                    self.addc('TS6', 'Risk $ (and reward $ per share)', mk.group(0), f'Risk ${fm(risk)}' + (f' to make ${fm(tgt - entry)}' if tgt is not None else ''), 'PASS' if ok else 'WRONG')
        # key levels
        self.work = re.sub(r'\$[\d,.]+(?: CLOSE)? \$[\d,.]+ (?:\$[\d,.]+)?', ' § ', self.work)
        res_pct = round((meta.get('proximityFilter') or {}).get('resistancePct', .3) * 100); sup_pct = round((meta.get('proximityFilter') or {}).get('supportPct', .2) * 100)
        for side, label in (('resistance', 'Resistance'), ('support', 'Support')):
            z = next((q for q in zones if q.get('nearest') and q.get('side') == side), None)
            m1 = re.search(rf'{label} (\$[\d,.]+(?: – \$[\d,.]+)?) (?:· price is inside this zone|· ([\d.]+)% (above|below))(?: · turned here (\d+)×)?', self.text)
            m2 = re.search(rf'{label} None within {res_pct if side == "resistance" else sup_pct}% (above|below)\.( The stock is (?:at|near) its 52-week high[^.]*\.)?', self.text)
            if z and m1:
                self.work = self.work.replace(m1.group(0), ' § ', 1)
                lo, hi = fm(z['low']), fm(z['high'])
                exp_rng = f'${lo}' if lo == hi else f'${lo} – ${hi}'
                edge = z['low'] if side == 'resistance' else z['high']
                pa = 0 if z.get('insideZone') and side == 'support' else abs((edge - price) / price) * 100
                ok = m1.group(1) == exp_rng and (m1.group(2) is None or near(float(m1.group(2)), pa, 0.06)) and (m1.group(4) is None or int(m1.group(4)) == z['swings'])
                self.addc(f'KL-{side}', f'{label} row: zone range, % away, turned-here count (S1 meta.zones nearest {side})', m1.group(0), f'{exp_rng} · {pa:.1f}% · {z["swings"]}×', 'PASS' if ok else 'WRONG',
                          '' if lo == hi or True else '', )
                if not near(float(m1.group(2)) if m1.group(2) else 0, pa, 0.06) or m1.group(1) != exp_rng:
                    pass
                if m1.group(1) != exp_rng.replace('$', '$'):
                    pass
            elif not z and m2:
                self.work = self.work.replace(m2.group(0), ' § ', 1)
                self.addc(f'KL-{side}', f'{label} row: none in the window, and the payload has no nearest {side} zone', m2.group(0), 'no zone', 'PASS')
            else:
                self.addc(f'KL-{side}', f'{label} row matches the nearest {side} zone', m1.group(0) if m1 else (m2.group(0) if m2 else 'row not found'), 'present' if z else 'none', 'WRONG')
            if m2 and m2.group(2):
                hi52 = max(h[-252:]); gap = (1 - price_card / hi52) * 100
                at = 'at its 52-week high' in m2.group(2)
                self.addc('KL-high', f'"{m2.group(2).strip()}" vs the real gap to the 252-bar high', f'{gap:.1f}% below ${fm(hi52)}', 'within 1% if "at"; within 3% if "near"',
                          'PASS' if (gap <= 1.0 if at else gap <= NEAR_HIGH + 0.05) else 'MISLEADING', 'the rule is "within 3%" (simple_sr NEAR_HIGH_PCT)' if at else '')
        tt = (self.pat.get('trendTemplate') or self.pat.get('trend_template') or {}).get('criteria_met')
        adx = (meta.get('adx') or {}).get('adx')
        ms = re.search(r'Price is (.*?)(?= Resistance )', self.text)
        if ms and ms.group(1).strip():
            insid = any(z.get('insideZone') and z.get('nearest') for z in zones if z.get('side') == 'support')
            res_all = sr.get('resistance') or []
            exp = state_words(price, res_all, sup, tt, adx, atr_p, res_pct, sup_pct, insid)
            self.work = self.work.replace(ms.group(0), ' § ', 1)
            self.addc('KL-state', 'one-line price state re-derived from the numbers (levels, trend checks, ADX, ATR)', ms.group(1).strip(), exp or 'n/a', 'PASS' if exp and ms.group(1).strip() == exp else ('UNVERIFIED' if exp is None else 'WRONG'))
            if re.search(r'strong trend|weak trend|Compression|Downtrend|Choppy', ms.group(1)):
                self.addc('KL-state-words', 'verdict-style words in the price state ("strong/weak trend", "Compression", "Downtrend", "Choppy")', ms.group(1).strip(), 'facts, not verdicts', 'MISLEADING', 'Day 126 rule: cards show numbers, not verdict words', sev='LOW')
        # structural invariants + independent zones
        self.levels_invariants(zones, sr, meta)
        self.unclaimed([r'rule of thumb', r'2×', r'7–8%', r"O'Neil", r'last 5 trading days', r'Turtles', r'Minervini', r'Livermore', r'2 ATR', r'1 ATR', r'Day \d+', r'the last \d+ days', r'30% above', r'20% below',
                        r'last year', r'N×', r'Turned here', r'swing highs', r'\b5 trading\b', r'\b5\b trading', r'2\s*ATR', r'52-week', r'\(within 3%\)'], 'TS')

    def levels_invariants(self, zones, sr, meta):
        price, atr = sr.get('currentPrice'), meta.get('atr')
        if not zones or price is None or not atr: return
        bad = []
        for z in zones:
            if z['low'] > z['high'] + 1e-9: bad.append(f'low>high {z}')
            if z['high'] - z['low'] > atr + 0.011: bad.append(f'zone wider than 1 ATR {z["low"]}-{z["high"]}')
            if z['swings'] != z['highs'] + z['lows'] or z['swings'] < 1: bad.append(f'swings != highs+lows {z}')
            if z['side'] == 'resistance' and not z['low'] > price: bad.append(f'resistance not above price {z["low"]}')
            if z['insideZone'] != (z['low'] <= price <= z['high']): bad.append(f'insideZone wrong {z}')
            if z['side'] == 'support' and z['low'] > price: bad.append(f'support above price {z["low"]}')
        for side in ('support', 'resistance'):
            if sum(1 for z in zones if z['side'] == side and z.get('nearest')) > 1: bad.append(f'two nearest {side}')
            cand = [z for z in zones if z['side'] == side]
            if cand and not any(z.get('nearest') for z in cand): bad.append(f'no nearest {side}')
            if cand:
                edge = (lambda z: z['low']) if side == 'resistance' else (lambda z: z['high'])
                near_z = min(cand, key=lambda z: abs(edge(z) - price))
                if not near_z.get('nearest'): bad.append(f'nearest {side} flag is not on the closest zone')
        floor, ceil = price * (1 - (meta.get('proximityFilter') or {}).get('supportPct', .2)), price * (1 + (meta.get('proximityFilter') or {}).get('resistancePct', .3))
        for z in zones:
            e = z['low'] if z['side'] == 'resistance' else z['high']
            if (z['side'] == 'support' and e < floor - 0.011) or (z['side'] == 'resistance' and e > ceil + 0.011): bad.append(f'zone outside the window {z}')
        self.addc('TS-inv', 'structural invariants on the zones (low<=high, width<=1 ATR, swings=highs+lows, sides, one nearest per side = closest, window, insideZone)', f'{len(zones)} zones', 'all hold', 'PASS' if not bad else 'WRONG', '; '.join(bad[:3]))
        # independent zones from the bars (the audit's frame is /api/stock's 260 bars at 2 dp, so a mismatch is borderline, not WRONG)
        sw = ref_swings(self.h, self.l, self.dates)
        for label, a in (('payload ATR', atr), ('recomputed ATR', R.wilder_atr(self.h, self.l, self.c))):
            ref = ref_zones(sw, a)
            miss = []
            for z in zones:
                if not any(near(z['low'], q['low'], 0.02) and near(z['high'], q['high'], 0.02) and z['swings'] == len(q['members']) for q in ref):
                    miss.append(f'{z["low"]}-{z["high"]} x{z["swings"]}')
            if not miss:
                self.addc('TS-ref', f'zones in the payload = zones rebuilt from the bars by the plain-words rules (swings, merge 0.5 ATR, width 1 ATR; using {label})', f'{len(zones)} zones match', 'match', 'PASS'); return
        self.addc('TS-ref', 'zones in the payload = zones rebuilt from the bars by the plain-words rules', f'{len(miss)} of {len(zones)} differ: ' + ', '.join(miss[:3]), 'match', 'UNVERIFIED',
                  'borderline: the audit frame is /api/stock\'s 260 two-decimal bars; a merge decision near the 0.5/1.0 ATR cut or a 2-dp tie can differ. Inspect before trusting.')

    # --------------------------------------------------------------- Breakout
    def breakout(self):
        bo = (self.d['payloads'].get('breakout') or {}).get('body') or {}
        if not self.use('card-breakout'):
            if bo and not bo.get('error'): self.addc('BO0', 'Breakout card present when /api/breakout answered', 'card not found', 'card text', 'WRONG')
            return
        if bo.get('error') or not bo:
            m = re.search(r'Breakout check unavailable', self.text)
            self.addc('BO0', 'error state is said out loud', 'says so' if m else 'silent', 'says so', 'PASS' if m else 'WRONG'); return
        c, h, v = self.c, self.h, self.v
        t = len(c) - 1
        if bo.get('asOfDate') != self.dates[-1]:
            self.addc('BO-S5', 'S5: the breakout card\'s last bar = the stock\'s last completed bar', bo.get('asOfDate'), self.dates[-1], 'MISLEADING', 'the breakout card fetched its own bars', sev='LOW'); return
        piv = max(h[t - 69:t - 9])        # high of bars t-69..t-10
        cc = c[t]
        pct = round((cc - piv) / piv * 100, 4)
        b = next((i for i in range(t - 9, t + 1) if c[i] > piv), None)
        rv = None
        if b is not None:
            prior = [x for x in v[max(0, b - 50):b]]
            if len(prior) >= 40 and sum(prior) / len(prior) > 0: rv = round(v[b] / (sum(prior) / len(prior)), 2)
        self.addc('BO1', '60-day high = highest high of the 60 bars that end 10 bars before the last bar (S1 breakout_detection)', f'${bo["breakoutLevel"]}', f'${fm(piv)}', 'PASS' if near(bo['breakoutLevel'], piv, 0.011) else 'WRONG')
        self.addc('BO2', 'close % from the 60-day high (tolerance 0.06: the audit bars are rounded to 2 dp, the breakout route uses its own unrounded bars)', f'{bo["pctFromLevel"]}%', f'{pct:.2f}%', 'PASS' if near(bo['pctFromLevel'], pct, 0.06) else 'WRONG')
        exp_date = self.dates[b] if b is not None else None
        self.addc('BO3', 'breakout day = first close above the 60-day high within the last 10 bars', f'{bo.get("breakoutDate")}', f'{exp_date}', 'PASS' if bo.get('breakoutDate') == exp_date else 'WRONG')
        self.addc('BO4', 'volume on the breakout day / mean of the 50 bars before it (that day excluded)', f'{bo.get("rvol")}', f'{rv}', 'PASS' if (bo.get('rvol') is None and rv is None) or (bo.get('rvol') is not None and rv is not None and near(bo['rvol'], rv, 0.011)) else 'WRONG')
        low = float(self.l[t]); rv_ok = rv is not None and rv >= 1.5
        if b is not None:
            st = 'FAILED_BREAKOUT' if cc < piv else 'EXTENDED_CHASE_RISK' if pct > 5.0 else 'RETEST_ENTRY' if (t > b and round((low - piv) / piv * 100, 4) <= 1.0 and cc > piv) else 'BREAKOUT_CONFIRMED' if rv_ok else 'BREAKOUT_LIGHT_VOLUME'
        else:
            st = 'BREAKOUT_WATCH' if pct >= -3.0 else 'NOT_READY'
        self.addc('BO5', 'status badge re-derived from the numbers (thresholds 5% extension, 1.5x volume, 1% retest, 3% watch)', bo['status'], st, 'PASS' if bo['status'] == st else 'WRONG')
        m = re.search(r'60-day high \$([\d,.]+) · close ([\d.]+)% (above|below)(?: · broke out ([A-Z][a-z]{2} \d+)(?: on ([\d.]+)× its prior 50-day average volume| \(volume unknown\))?)?(?: · ([A-Z][a-z]{2} \d+) close)?', self.text)
        if m:
            self.work = self.work.replace(m.group(0), ' § ', 1)
            ok = m.group(1) == fm(bo['breakoutLevel']) and near(float(m.group(2)) * (1 if m.group(3) == 'above' else -1), bo['pctFromLevel'], 0.0051) \
                and (m.group(4) is None or m.group(4) == dlabel(bo['breakoutDate'])) and (m.group(5) is None or near(float(m.group(5)), bo['rvol'] or -99, 0.0051)) \
                and (m.group(6) is None or m.group(6) == dlabel(bo['asOfDate']))
            self.addc('BO6', 'card line = the payload (level, % and side, breakout date, volume ratio, as-of date) in the page money format', m.group(0), 'payload values', 'PASS' if ok else 'WRONG')
        else:
            self.addc('BO6', 'card line with the level, % and dates found', 'not found', 'present', 'WRONG')
        if b is not None and bo.get('breakoutAge') is not None and bo['breakoutAge'] <= 9 and not (cc < piv):
            pass
        if re.search(r're-qualifies about every 10 days', self.text):
            self.addc('BO7', 'copy: "a stock that keeps climbing re-qualifies about every 10 days"', 'old copy', 'the breakout date slides forward daily for a steady climber', 'MISLEADING', sev='LOW')
        elif re.search(r'moves forward each day', self.text):
            self.addc('BO7', 'copy says the breakout date (first close above the high in the last 10 days) moves forward each day for a climber', 'honest copy', 'matches breakout_detection.py b = first close above in t-9..t', 'PASS')
        if re.search(r'× normal volume', self.text):
            self.addc('BO8', 'S3: "x normal volume" here excludes the breakout day from the 50-bar mean; the Technical Read\'s includes the bar itself', 'two definitions of one phrase', 'one definition', 'MISLEADING', sev='LOW')
        elif re.search(r'prior 50-day average volume', self.text):
            self.addc('BO8', 'the breakout volume ratio is named for its window ("its prior 50-day average volume", breakout day excluded)', 'named window', 'prior 50 bars', 'PASS')
        self.unclaimed([r'60-day', r'1\.5×', r'\b5%', r'10 days', r'Common trader rules', r'More than 3% under', r'Within 3% of', r'1\.5× its 50-day', r'50-day'], 'BO')

    # --------------------------------------------------------------- Price Data + Relative Strength
    def price_data(self):
        have = bool(self.stock)
        if not self.use('card-price-data'):
            if have: self.addc('PD0', 'Price Data card present (Price & Relative Strength opened)', 'card not found', 'card text', 'WRONG')
            return
        c, h, l, v = self.c, self.h, self.l, self.v
        last = c[-1]
        m = re.search(r'Last close: \$([\d,.]+) 52-Week High: \$([\d,.]+) 52-Week Low: \$([\d,.]+) % from High: ([+-]?[\d.]+)%', self.text)
        if m:
            self.work = self.work.replace(m.group(0), ' § ', 1)
            hi, lo = max(h[-252:]), min(l[-252:])
            self.addc('PD1', '"Last close" = the last COMPLETED close (the header\'s live "Now" is separate; S5 with the header and the plan)', f'${m.group(1)}', f'${fm(last)}', 'PASS' if m.group(1) == fm(last) else 'WRONG')
            self.addc('PD2', '52-Week High / Low = extremes of the 252 completed bars (S1 /api/stock, same bars as the Technical Read)', f'${m.group(2)} / ${m.group(3)}', f'${fm(hi)} / ${fm(lo)}', 'PASS' if m.group(2) == fm(hi) and m.group(3) == fm(lo) else ('MISLEADING' if near(fnum_(m.group(2)), hi, 0.0111) and near(fnum_(m.group(3)), lo, 0.0111) else 'WRONG'), 'one-cent difference: the card rounds the high of the adjusted frame, the audit the 2-dp bars' if m.group(2) != fm(hi) or m.group(3) != fm(lo) else '', sev='LOW' if (m.group(2) != fm(hi) or m.group(3) != fm(lo)) else None)
            self.addc('PD3', '% from High', f'{m.group(4)}%', f'{(last / hi - 1) * 100:.1f}%', 'PASS' if near(float(m.group(4)), (last / hi - 1) * 100, 0.11) else 'WRONG')
            tr_high = re.search(r'([\d.]+)% below the \$([\d,.]+) high', (self.d.get('tr') or {}).get('text', ''))
            if tr_high: self.addc('PD-S5', 'S5: Price Data 52-week high = the Technical Read\'s 1-year high', f'${m.group(2)}', f'${tr_high.group(2)}', 'PASS' if m.group(2) == tr_high.group(2) else 'MISLEADING')
        else:
            self.addc('PD1', 'Price Data lines found', 'not found', 'present', 'WRONG')
        ml = re.search(r'Liquidity \(Daily \$\): (\S+(?: \(no volume data\))?)', self.text)
        if ml:
            self.work = self.work.replace(ml.group(0), ' § ', 1)
            days = sum(1 for x in v[-50:] if x and x > 0)
            if days < 40:
                self.addc('PD4', 'S5: liquidity when the bars have no volume (the Technical Read says so)', ml.group(1), 'N/A', 'PASS' if ml.group(1).startswith('N/A') else 'MISLEADING', 'a Yahoo avgVolume figure would contradict the "No volume data" line')
            else:
                bars_dv = sum(v[-50:]) / 50 * last
                txt = ml.group(1)
                mm = re.match(r'\$([\d.]+)([KMBT]?)', txt)
                mult = {'': 1, 'K': 1e3, 'M': 1e6, 'B': 1e9, 'T': 1e12}
                shown = float(mm.group(1)) * mult[mm.group(2)] if mm else None
                ok = shown is not None and 0.75 <= shown / bars_dv <= 1.33
                self.addc('PD4', 'Liquidity (daily $) = provider average volume x price; checked against the 50-bar average dollar volume (two sources, 25% band)', txt, f'bars: ${bars_dv:,.0f}', 'PASS' if ok else 'MISLEADING',
                          '' if ok else 'the Yahoo figure and the price bars disagree; the label states no window', sev='LOW')
        self.unclaimed([r'52-Week', r'Daily \$'], 'PD')

    def relative_strength(self):
        if not self.use('card-relative-strength'):
            if self.stock: self.addc('RS0', 'Relative Strength card present', 'card not found', 'card text', 'WRONG')
            return
        c = self.c
        sc = [b['close'] for b in (self.spy.get('priceHistory') or [])]
        if len(sc) < 201:
            self.addc('RS-X', 'SPY history', f'{len(sc)} bars', 'over 200', 'UNVERIFIED'); return
        def at(cs, back): i = len(cs) - back; return None if i < 0 else cs[i]
        def span(cs): return 252 if len(cs) >= 252 else None
        i_s = len(c) - 252 if len(c) >= 252 else (0 if len(c) > 200 else None)
        s52 = c[i_s] if i_s is not None else None
        p52 = sc[len(sc) - 252] if len(sc) >= 252 else (sc[0] if len(sc) > 200 else None)
        m = re.search(r'RS vs S&P 500: ([\d.]+|N/A) Stock 52W Return: ([+-]?[\d.]+)% S&P 52W Return: ([+-]?[\d.]+)%', self.text)
        if m and s52 and p52:
            self.work = self.work.replace(m.group(0), ' § ', 1)
            rs = (c[-1] / s52) / (sc[-1] / p52); sr_, pr_ = (c[-1] / s52 - 1) * 100, (sc[-1] / p52 - 1) * 100
            self.addc('RS1', 'RS vs S&P 500 = (stock / stock a year ago) / (SPY / SPY a year ago) (S1 rsCalculator.js)', m.group(1), f'{rs:.2f}', 'PASS' if m.group(1) != 'N/A' and near(float(m.group(1)), rs, 0.011) else 'WRONG')
            self.addc('RS2', 'Stock 52W Return and S&P 52W Return', f'{m.group(2)}% / {m.group(3)}%', f'{sr_:+.1f}% / {pr_:+.1f}%', 'PASS' if near(float(m.group(2)), sr_, 0.06) and near(float(m.group(3)), pr_, 0.06) else 'WRONG')
            same = (len(c) >= 252) == (len(sc) >= 252)
            self.addc('RS3w', 'S3: both returns cover the same period ("52 weeks")', f'stock {len(c) - 1 - i_s} bars, SPY {len(sc) - 1 - (len(sc) - 252 if len(sc) >= 252 else 0)} bars', 'equal', 'PASS' if same else 'MISLEADING',
                      '' if same else 'short history: the stock\'s year-ago price is its FIRST bar while SPY uses 252 bars, so RS compares different periods')
            mr = re.search(r'RS Rating \(scaled, not a percentile\): (\d+|N/A)', self.text)
            if mr:
                self.work = self.work.replace(mr.group(0), ' § ', 1)
                rr = min(99, max(1, round((rs - 0.5) * 80 + 10)))
                self.addc('RS4', 'RS rating = clamp(round((RS - 0.5) x 80 + 10), 1, 99)', mr.group(1), f'{rr}', 'PASS' if mr.group(1) != 'N/A' and abs(int(mr.group(1)) - rr) <= 1 else 'WRONG', 'tolerance 1: the page rounds the 3-dp RS')
            # interpretation words vs bands + trend suffix
            bands = [(1.3, 'Well ahead of the market'), (1.2, 'Ahead of the market'), (1.1, 'Somewhat ahead of the market'), (1.0, 'Slightly ahead of the market'),
                     (0.9, 'Slightly behind the market'), (0.8, 'Behind the market'), (-9, 'Well behind the market')]
            base = next(w for lim, w in bands if round(rs, 3) >= lim)
            c13, s13 = at(c, 63), at(sc, 63)
            suffix = ''
            if c13 and s13:
                rs13 = (c[-1] / c13) / (sc[-1] / s13)
                suffix = ' (momentum accelerating)' if rs13 > rs * 1.05 else ' (momentum fading)' if rs13 < rs * 0.95 else ''
            mi = re.search(r'(Well ahead of the market|Somewhat ahead of the market|Slightly ahead of the market|Ahead of the market|Slightly behind the market|Well behind the market|Behind the market|Exceptional strength - Top tier performer|Strong outperformance vs market|Good relative strength|Performing in-line with market|Slight underperformance|Underperforming - Caution advised|Significant laggard - Avoid for swing trades)( \(momentum (?:accelerating|fading)\))?', self.text)
            if mi:
                self.work = self.work.replace(mi.group(0), ' § ', 1)
                got = mi.group(1) + (mi.group(2) or '')
                self.addc('RS5', 'interpretation sentence = the band of RS (+ 13-week vs 52-week trend)', got, base + suffix, 'PASS' if got == base + suffix else 'WRONG')
                if re.search(r'Exceptional|Caution advised|Avoid for swing trades|Top tier', got):
                    self.addc('RS5v', 'verdict words on the card ("Top tier", "Caution advised", "Avoid for swing trades")', got, 'facts, not verdicts', 'MISLEADING', 'Day 126 rule', sev='LOW')
                if 'in-line' in got and rs >= 1.05:
                    self.addc('RS5w', 'words "performing in-line with market" vs the number', f'RS {rs:.2f}', 'within about 5% of 1.00', 'MISLEADING', 'the band 1.00-1.099 reads "in-line" up to 10% outperformance', sev='LOW')
            ma = re.search(r'Absolute momentum \(info only\): ([+-][\d.]+)% over the past year — (negative in absolute terms|positive, but under the 5% cash proxy|clears the 5% cash proxy)[^.]*\.', self.text)
            if ma:
                self.work = self.work.replace(ma.group(0), ' § ', 1)
                word = 'negative' if sr_ < 0 else 'under' if sr_ <= 5.0 else 'clears'
                got = 'negative' if ma.group(2).startswith('negative') else 'under' if ma.group(2).startswith('positive') else 'clears'
                ok = near(float(ma.group(1)), sr_, 0.06) and got == word
                self.addc('RS6', 'absolute momentum: the return and its words (negative / positive but under the 5% cash proxy / clears it)', f'{ma.group(1)}% {got}', f'{sr_:+.1f}% {word}', 'PASS' if ok else 'WRONG')
        elif not m:
            self.addc('RS1', 'Relative Strength lines found', 'not found', 'present', 'WRONG')
        if re.search(r'it does not affect any score or the verdict', self.text):
            self.addc('RS-copy', 'stale copy: "does not affect any score or the verdict" (there is no verdict on the page since Day 123)', 'stale', 'current wording', 'MISLEADING', sev='LOW')
        self.unclaimed([r'5%', r'Day \d+', r'Antonacci', r'2014', r'S&P 500', r'52W', r'RS Rating', r'T-bill'], 'RS')
        # the collapsed toggle line
        tg = self.d.get('priceRsToggle') or ''
        mt = re.search(r'\$([\d,.]+) \| RS ([\d.]+)', tg)
        if mt and m:
            self.addc('RS-toggle', 'S5: the collapsed line "$price | RS x" = the cards', f'${mt.group(1)} | RS {mt.group(2)}', f'${fm(c[-1])} | RS {rs:.2f}', 'PASS' if mt.group(1) == fm(c[-1]) and abs(float(mt.group(2)) - rs) <= 0.0101 else 'WRONG', 'RS is rounded to 3 dp and then 2 dp by the page' if mt.group(2) != f'{rs:.2f}' else '')

    # --------------------------------------------------------------- header badges
    def header(self):
        if not self.use('card-stock-header'): return
        ms = re.search(r'\[([^\]]*?) \((\w+)\) — RS: ([\d.]+) \| Mom: ([+-]?[\d.]+) \| Rank: (\d+)/(\d+)\] (\w+) (LEADING|IMPROVING|WEAKENING|LAGGING)', self.text)
        rows = []
        for e in (self.d['payloads'].get('sectors_all') or []):
            rows = (e.get('body') or {}).get('sectors') or rows
            if rows: break
        if ms:
            row = next((r for r in rows if r.get('etf') == ms.group(2)), None)
            if row:
                ok = near(float(ms.group(3)), row['rsRatio'], 0.0051) and near(float(ms.group(4)), row['rsMomentum'], 0.0051) and int(ms.group(5)) == row['rank'] and int(ms.group(6)) == len(rows)
                self.addc('HB1', 'sector badge numbers = the sector rotation payload (RS ratio, momentum, rank n/11)', ms.group(0)[:70], f'RS {row["rsRatio"]} Mom {row["rsMomentum"]} Rank {row["rank"]}/{len(rows)}', 'PASS' if ok else 'WRONG')
                q = ('Leading' if row['rsMomentum'] > 0 else 'Weakening') if row['rsRatio'] > 100 else ('Improving' if row['rsMomentum'] > 0 else 'Lagging')
                self.addc('HB2', 'S3: quadrant word vs RS ratio (above/below 100) and momentum (above/below 0)', ms.group(8), q.upper(), 'PASS' if ms.group(8) == q.upper() else 'MISLEADING')
            else:
                self.addc('HB1', 'sector badge ETF found in the payload', ms.group(2), 'present', 'UNVERIFIED', 'ETF not in /api/sectors/rotation')
        e = (self.d['payloads'].get('earnings') or {}).get('body') or {}
        warn = (e.get('warning') or '').strip()
        mt = re.search(r'Earnings Date: ([\d-]+) Days Until: (-?\d+)', self.text)
        if e.get('has_upcoming') and warn:
            shown = warn in self.text
            self.addc('HB3', 'earnings badge text = the backend warning (S1 /api/earnings), shown when earnings are upcoming', warn if shown else 'no badge', warn, 'PASS' if shown else 'WRONG')
            if mt: self.addc('HB3d', 'earnings badge tooltip: date and calendar days until', f'{mt.group(1)}, {mt.group(2)} days', f'{e.get("earnings_date")}, {e.get("days_until")} days', 'PASS' if mt.group(1) == e.get('earnings_date') and int(mt.group(2)) == e.get('days_until') else 'WRONG')
            m_in = re.search(r'IN (\d+) DAYS?', warn)
            if m_in and e.get('days_until') is not None: self.addc('HB3w', 'S3: "in N days" in the warning = calendar days to the earnings date', m_in.group(0), f'{e["days_until"]}', 'PASS' if int(m_in.group(1)) == e['days_until'] else 'MISLEADING')
            if re.search(r'HIGH RISK|CAUTION -|AWARE -|Consider waiting|Consider exiting|Size position smaller', self.text):
                self.addc('HB3v', 'advice words in the earnings tooltip ("HIGH RISK", "Consider waiting", "Size position smaller")', 'advice words', 'facts, not verdicts', 'MISLEADING', 'Day 126 rule; backend /api/earnings recommendation text', sev='LOW')
        elif not e.get('has_upcoming'):
            self.addc('HB3', 'no earnings badge when none is upcoming', 'none' if 'EARNINGS' not in self.text.upper().replace('EARNINGS DATE', '') else 'badge shown', 'none', 'PASS' if 'EARNINGS' not in self.text.upper().replace('EARNINGS DATE', '') else 'WRONG')
        mp = re.search(r'Now \$([\d,.]+)', self.text); ml = re.search(r'Last close \$([\d,.]+) · ([A-Z][a-z]{2} \d+)', self.text)
        if ml:
            good = ml.group(1) == fm(self.c[-1]) and ml.group(2) == dlabel(self.dates[-1])
            cent = (not good) and near(float(ml.group(1).replace(',', '')), self.c[-1], 0.0111) and ml.group(2) == dlabel(self.dates[-1])
            self.addc('HB4', 'header "Last close $X · date" = the last completed bar (S5 with Price Data and the plan)', ml.group(0), f'${fm(self.c[-1])} · {dlabel(self.dates[-1])}', 'PASS' if good else ('MISLEADING' if cent else 'WRONG'),
                      'one-cent disagreement between two data providers for the same close (header/quote path vs price bars)' if cent else '', sev='LOW' if cent else None)


def main():
    out = sys.argv[1]
    dumps = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(out, 'dump_*.json')))]
    rows, cov = [], {}
    for d in dumps:
        ca = CardAudit(d).run_cards(); rows += ca.rows
        for k, v in ca.coverage.items(): cov.setdefault(k, [0, 0]); cov[k][0] += v[0]; cov[k][1] += v[1]
    counts = {k: sum(1 for r in rows if r.verdict == k) for k in A.SEV}
    L = ['# Statement Audit phase 2 report (Trade Setup, key levels, Breakout, Price Data, Relative Strength, header badges)', '',
         f"Run: {datetime.now().isoformat(timespec='minutes')} · dumps: {', '.join(d['ticker'] for d in dumps)}", '',
         f"Verdicts: PASS {counts['PASS']} · WRONG {counts['WRONG']} (CRITICAL) · MISLEADING {counts['MISLEADING']} (HIGH/LOW per row) · UNVERIFIED {counts['UNVERIFIED']} (INFO)", '',
         '## Coverage (honest)', '| Card | statements claimed (spans) | number tokens left unclaimed |', '|---|---|---|']
    for k, (a, b) in sorted(cov.items()): L.append(f'| {k} | {a} | {b} |')
    L += ['', 'Recomputed from bars: ATR, Stop, Target %, R:R, 52-week high/low, % from high, RS, RS rating, returns, 60-day high, breakout day and volume ratio, status, zones (independent plain-words reference).',
          'Arithmetic only (payload to text): Buy, Target price, zone ranges. Structural only: zone invariants. UNVERIFIED: levels the reference cannot reproduce (borderline), provider fields (liquidity, earnings date).',
          'NOT YET COVERED: Fundamentals, Market backdrop, Data Sources, MR Read, the other tabs; branches not reached by these tickers (no_atr, inside-zone, earnings badge, each breakout state) unless listed above.', '',
          '| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |', '|---|---|---|---|---|---|---|---|']
    esc = lambda s: str(s).replace('|', '/')
    for r in sorted(rows, key=lambda r: ({'WRONG': 0, 'MISLEADING': 1, 'UNVERIFIED': 2, 'PASS': 3}[r.verdict], r.card, r.ticker, r.sid)):
        L.append(f'| {r.ticker} | {r.sid} | {esc(r.claim)} | {esc(r.shown)} | {esc(r.expected)} | {r.verdict} | {r.sev} | {esc(r.note)} |')
    open(os.path.join(out, 'REPORT_CARDS.md'), 'w').write('\n'.join(L) + '\n')
    print('\n'.join(L[:6])); print('report:', os.path.join(out, 'REPORT_CARDS.md'))
    return 1 if counts['WRONG'] else 0


if __name__ == '__main__':
    sys.exit(main())
