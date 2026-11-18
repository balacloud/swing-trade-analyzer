"""Self-tests for the phase-2 Statement Audit (audit_cards.py). Run: cd backend && venv/bin/python test_audit_cards.py
Proves the auditor catches a planted wrong Buy / Stop / R:R / zone invariant / state sentence, and that the independent support-resistance reference
reproduces a hand-built zig-zag."""
import sys
import audit_cards as C
import audit_ref as R

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1; print(f'ok {m}')
    else: failed += 1; print(f'FAIL {m}')

# ---- reference swings and zones on a hand-built series: lows at 90 (twice, 20 bars apart) and 91, a high at 110
n = 80
h = [100.0] * n; l = [99.0] * n; dates = [f'd{i:03d}' for i in range(n)]
for i, v in ((20, 90.0), (40, 90.2), (60, 91.5)): l[i] = v
h[30] = 110.0
sw = C.ref_swings(h, l, dates)
lows = sorted(round(s['price'], 1) for s in sw if s['kind'] == 'low' and s['price'] < 95)
ok(lows == [90.0, 90.2, 91.5], 'reference swings: three separated lows found')
ok(any(s['kind'] == 'high' and s['price'] == 110.0 for s in sw), 'reference swings: the 110 high is found')
zs = C.ref_zones([s for s in sw if s['price'] < 95 or s['price'] == 110.0], atr=1.0)
low_zones = [z for z in zs if z['low'] < 95]
ok(all(z['high'] - z['low'] <= 1.0 + 1e-9 for z in low_zones), 'reference zones: no zone is wider than 1 ATR')
ok(sum(len(z['members']) for z in low_zones) == 3, 'reference zones: every swing is in exactly one zone')

# ---- the key-levels price state
ok(C.state_words(100, [], [95], 7, 25, 1, 30, 20, False) == 'No resistance within 30% above · 7 of 8 trend checks pass', 'state words: no resistance quotes the trend-check count')
ok(C.state_words(100, [101], [99.5], 7, 25, 1, 30, 20, False) == 'Close to both support and resistance', 'state words: near both levels')
ok(C.state_words(100, [120], [90], 2, 30, 1, 30, 20, False) == '2 of 8 trend checks pass · ADX 30.0', 'state words: few trend checks quotes the numbers')
ok(C.state_words(100, [120], [], 5, 20, 1, 30, 20, False) == 'No support within 20% below', 'state words: no support')

# ---- a planted Trade Setup card
N = 120
close = [100.0] * N
ph = [{'date': f'2026-01-{1 + i // 28:02d}-x', 'open': 100.0, 'high': 100.5, 'low': 99.5, 'close': 100.0, 'volume': 1000000} for i in range(N)]
for i, b in enumerate(ph): b['date'] = f'd{i:03d}'
ZONES = [
    {'low': 98.0, 'high': 98.5, 'mid': 98.25, 'swings': 3, 'highs': 1, 'lows': 2, 'side': 'support', 'insideZone': False, 'nearest': True, 'lastSwingDate': 'd010'},
    {'low': 104.0, 'high': 104.4, 'mid': 104.2, 'swings': 2, 'highs': 2, 'lows': 0, 'side': 'resistance', 'insideZone': False, 'nearest': True, 'lastSwingDate': 'd020'},
]
def dump(text, zones=None, support=(98.5,), atr=1.0, price=100.0, basis=None):
    return {'ticker': 'TST', 'payloads': {
        'stock': {'body': {'priceHistory': ph, 'fiftyTwoWeekHigh': 100.5}},
        'sr': {'body': {'currentPrice': price, 'support': list(support), 'resistance': [104.0], 'suggestedTarget': 104.0,
                        'meta': {'atr': atr, 'zones': zones if zones is not None else ZONES, 'proximityFilter': {'resistancePct': 0.3, 'supportPct': 0.2}, 'nearHigh52w': False, 'adx': {'adx': 22}, **({'entryBasis': basis} if basis else {})}}},
        'patterns': {'body': {'trendTemplate': {'criteria_met': 6}}}, 'spy': {'body': {'priceHistory': ph}}, 'quote': {'body': {'available': False}}},
        'cardTexts': {'card-trade-setup': text}, 'tr': {'text': ''}}
GOOD = ('Pullback plan 2.8 : 1 reward : risk BUY $98.50 $96.50 $104.00 Buy $98.50 support, 1.5% below the last close Stop $96.50 -2.0% from the buy · 2 ATR below '
        'Target $104.00 +5.6% from the buy · nearest resistance Risk $2.00 to make $5.50 a share. Size this plan →')
def rows(text, **kw):
    ca = C.CardAudit(dump(text, **kw)); ca.use('card-trade-setup'); ca.trade_setup(); return {r.sid: r for r in ca.rows}
r = rows(GOOD)
ok(all(r[k].verdict == 'PASS' for k in ('TS1', 'TS1c', 'TS2', 'TS3', 'TS3w', 'TS4', 'TS5', 'TS6')), 'a correct plan passes every arithmetic row')
ok(r['TS-inv'].verdict == 'PASS', 'the planted zones satisfy the structural invariants')
ok(rows(GOOD.replace('Buy $98.50 support', 'Buy $98.00 support'))['TS1'].verdict == 'WRONG', 'a wrong Buy is caught')
ok(rows(GOOD.replace('Stop $96.50', 'Stop $96.00'))['TS3'].verdict == 'WRONG', 'a stop that is not 2 ATR below the Buy is caught')
ok(rows(GOOD.replace('2.8 : 1', '3.5 : 1'))['TS5'].verdict == 'WRONG', 'a wrong reward : risk is caught')
ok(rows(GOOD.replace('Risk $2.00 to make $5.50', 'Risk $2.00 to make $6.50'))['TS6'].verdict == 'WRONG', 'a wrong reward in "Risk to make" is caught')
ok(rows(GOOD.replace('1.5% below', '3.0% below'))['TS2'].verdict == 'WRONG', 'a wrong "% below the last close" is caught')
ok(rows(GOOD.replace('1.5% below', '1.5% above'))['TS2'].verdict == 'WRONG', 'the wrong side ("above") is caught')
# structural: support above price, two nearest zones, a zone wider than 1 ATR, nearest flag on the wrong zone
bad_zone = [dict(ZONES[0], low=101.0, high=101.5, side='support')] + [ZONES[1]]
ok(rows(GOOD, zones=bad_zone)['TS-inv'].verdict == 'WRONG', 'a support zone above the price fails the invariants')
wide = [dict(ZONES[0], low=95.0, high=98.5)] + [ZONES[1]]
ok(rows(GOOD, zones=wide)['TS-inv'].verdict == 'WRONG', 'a zone wider than 1 ATR fails the invariants')
two = [ZONES[0], dict(ZONES[0], low=90.0, high=90.4, nearest=True), ZONES[1]]
ok(rows(GOOD, zones=two)['TS-inv'].verdict == 'WRONG', 'two zones flagged nearest on one side fail the invariants')
far_flag = [dict(ZONES[0], nearest=False), dict(ZONES[0], low=90.0, high=90.4, nearest=True), ZONES[1]]
ok(rows(GOOD, zones=far_flag)['TS-inv'].verdict == 'WRONG', 'the nearest flag on a farther zone fails the invariants')
# Day 127: an inside zone flagged nearest while an outside zone's edge is nearer is CORRECT (PLD): invariants and the Buy check pass
inside_z = [dict(ZONES[0], low=99.95, high=100.95, insideZone=True, nearest=True), dict(ZONES[0], low=98.9, high=99.3, insideZone=False, nearest=False), ZONES[1]]
ri = rows(GOOD.replace('Buy $98.50', 'Buy $100.95').replace('BUY $98.50', 'BUY $100.95'), zones=inside_z, support=(100.95, 99.3))
ok(ri['TS-inv'].verdict == 'PASS', 'an inside zone flagged nearest, with a lower zone whose edge is nearer, passes the invariants (engine rule: inside = distance 0)')
ok(ri['TS1b'].verdict == 'PASS', 'and the Buy equals that inside zone high')
inside_wrong = [dict(inside_z[0], nearest=False), dict(inside_z[1], nearest=True), ZONES[1]]
ok(rows(GOOD, zones=inside_wrong)['TS-inv'].verdict == 'WRONG', 'the nearest flag on the outside zone while the price is inside another zone fails the invariants')
# Day 127: the Buy is the last COMPLETED close when it is inside the nearest support zone (the payload says so in meta.entryBasis; the audit re-derives it)
INSIDE_TXT = GOOD.replace('Buy $98.50 support, 1.5% below the last close', 'Buy $100.00 the last close, inside the support zone').replace('BUY $98.50', 'BUY $100.00')
rb = rows(INSIDE_TXT, zones=inside_z, support=(100.95, 99.3), basis='last_close_inside_zone')
ok(rb['TS-basis'].verdict == 'PASS' and rb['TS1'].verdict == 'PASS' and rb['TS1b'].verdict == 'PASS' and rb['TS1d'].verdict == 'PASS' and rb['TS2'].verdict == 'PASS', 'close inside the zone: entryBasis, the Buy (= the close), the zone check and the "not above the market" check all pass')
ok(rows(INSIDE_TXT.replace('$100.00', '$100.95'), zones=inside_z, support=(100.95, 99.3), basis='last_close_inside_zone')['TS1'].verdict == 'WRONG', 'close inside the zone but the card still shows the zone high as the Buy: caught')
ok(rows(INSIDE_TXT, zones=inside_z, support=(100.95, 99.3), basis='zone_high')['TS-basis'].verdict == 'WRONG', 'the payload says zone_high while the close is inside the zone: caught')
ok(rows(INSIDE_TXT, zones=[dict(inside_z[0], low=100.2, high=101.0), inside_z[1]], support=(101.0, 99.3), basis='last_close_inside_zone')['TS-basis'].verdict == 'WRONG', 'the payload says last_close_inside_zone while the close is below the zone: caught')
# the latent engine bug the review named: the Buy (max support edge) disagrees with the zone flagged nearest
disagree = [dict(ZONES[0], high=97.0, low=96.5), ZONES[1]]
ok(rows(GOOD, zones=disagree)['TS1b'].verdict == 'WRONG', 'the Buy and the Support row disagreeing (Buy != nearest zone high) is caught')
# wording overstatement: "at its 52-week high" while 2.2% below the high is MISLEADING; "near ... (within 3%)" passes
txt = ('Pullback plan BUY $98.50 $96.50 Buy $98.50 support, 1.5% below the last close Stop $96.50 -2.0% from the buy · 2 ATR below '
       'Target — no resistance above, the stock is at its 52-week high Risk $2.00 a share.')
d = dump(txt); d['payloads']['sr']['body']['suggestedTarget'] = None; d['payloads']['sr']['body']['resistance'] = []
d['payloads']['stock']['body']['priceHistory'] = [dict(b, high=104.0) for b in ph[:5]] + ph[5:]
ca = C.CardAudit(d); ca.use('card-trade-setup'); ca.trade_setup()
ok({x.sid: x for x in ca.rows}['TS4w'].verdict == 'MISLEADING', '"at its 52-week high" while the price is 4% below the high is flagged')
ca = C.CardAudit(d); ca.cards['card-trade-setup'] = txt.replace('is at its 52-week high', 'is near its 52-week high (within 3%)'); ca.use('card-trade-setup'); ca.trade_setup()
ok({x.sid: x for x in ca.rows}['TS4w'].verdict == 'MISLEADING', '"near (within 3%)" is also flagged when the real gap is 4%')

# ---- breakout status re-derivation on a planted climb
bo_close = [100.0 + 0.1 * i for i in range(120)]
bph = [{'date': f'd{i:03d}', 'open': x, 'high': x + 0.5, 'low': x - 0.5, 'close': x, 'volume': 1000000 if i != 115 else 3000000} for i, x in enumerate(bo_close)]
t = len(bo_close) - 1
piv = max(b['high'] for b in bph[t - 69:t - 9])
bo = {'status': 'BREAKOUT_CONFIRMED', 'asOfDate': f'd{t:03d}', 'breakoutLevel': round(piv, 2), 'pctFromLevel': round((bo_close[t] - piv) / piv * 100, 2), 'breakoutDate': f'd{t - 9:03d}', 'rvol': 1.0}
bd = {'ticker': 'TST', 'payloads': {'stock': {'body': {'priceHistory': bph}}, 'sr': {'body': {}}, 'patterns': {'body': {}}, 'spy': {'body': {}}, 'quote': {'body': {}}, 'breakout': {'body': bo}},
      'cardTexts': {'card-breakout': 'Breakout 60-day high'}, 'tr': {'text': ''}}
ca = C.CardAudit(bd); ca.use('card-breakout'); ca.breakout(); br = {x.sid: x for x in ca.rows}
ok(br['BO1'].verdict == 'PASS' and br['BO2'].verdict == 'PASS', 'breakout: the 60-day high (bars t-69..t-10) and the % are recomputed')
ok(br['BO5'].verdict in ('PASS', 'WRONG') and br['BO5'].expected in ('EXTENDED_CHASE_RISK', 'BREAKOUT_LIGHT_VOLUME', 'BREAKOUT_CONFIRMED', 'RETEST_ENTRY', 'FAILED_BREAKOUT'), 'breakout: a status is re-derived from the numbers')
bo2 = dict(bo, status='NOT_READY'); bd['payloads']['breakout']['body'] = bo2
ca = C.CardAudit(bd); ca.use('card-breakout'); ca.breakout()
ok({x.sid: x for x in ca.rows}['BO5'].verdict == 'WRONG', 'breakout: a wrong status badge is caught')
bo3 = dict(bo, breakoutLevel=round(piv + 1, 2)); bd['payloads']['breakout']['body'] = bo3
ca = C.CardAudit(bd); ca.use('card-breakout'); ca.breakout()
ok({x.sid: x for x in ca.rows}['BO1'].verdict == 'WRONG', 'breakout: a wrong 60-day high is caught')

# ---- regression gate: the phase-1 Technical Read rows on the FROZEN dumps must equal the frozen baseline (id, shown, expected, verdict)
import glob, json, os
import audit_statements as A
FROZEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'test', 'Statement_Audit_phase1_frozen')
if os.path.exists(os.path.join(FROZEN, 'baseline_rows.json')):
    base = json.load(open(os.path.join(FROZEN, 'baseline_rows.json')))
    now = []
    for pth in sorted(glob.glob(os.path.join(FROZEN, 'dump_*.json'))):
        for r in A.Audit(json.load(open(pth))).run().rows: now.append([r.ticker, r.sid, r.shown, r.expected, r.verdict])
    ok(now == base, f'phase-1 Technical Read rows are identical to the frozen baseline ({len(base)} rows)')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
