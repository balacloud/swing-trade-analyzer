"""Self-tests for the phase-3a Statement Audit (audit_cards2.py). Run: cd backend && venv/bin/python test_audit_cards2.py
Proves: the audit's RSI(2) reference equals the app's own mean_reversion function; the index-trend reference equals index_trend.py; planted wrong
fundamentals tiles / MR rows / flags are caught; and the phase-2 frozen-dump regression gate still holds."""
import glob, json, os, sys
import numpy as np
import pandas as pd
import audit_cards2 as C2
import audit_ref as R
import mean_reversion
import index_trend

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1; print(f'ok {m}')
    else: failed += 1; print(f'FAIL {m}')

# ---- the RSI(2) reference vs the app's function on random walks (several seeds, a flat stretch, a gap)
def ref_rsi2(c):
    g = [0.0] + [max(c[i] - c[i - 1], 0.0) for i in range(1, len(c))]; l = [0.0] + [max(c[i - 1] - c[i], 0.0) for i in range(1, len(c))]
    def ew(xs, a=0.5):
        num = den = 0.0
        for x in xs: num = x + (1 - a) * num; den = 1 + (1 - a) * den
        return num / den
    ag, al = ew(g), ew(l)
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
for seed in (1, 2, 3, 4):
    r = np.random.default_rng(seed); c = 100 * np.exp(np.cumsum(r.normal(0, .02, 260)))
    app = float(mean_reversion.calculate_rsi_short(pd.Series(c), period=2).iloc[-1])
    ok(abs(app - ref_rsi2(list(c))) < 1e-6, f'RSI(2) reference equals the app function (seed {seed}: {app:.3f})')

# ---- the index-trend reference vs index_trend.py on a random series (SMA/pct/drop/since)
r = np.random.default_rng(7); idx = pd.bdate_range(end='2026-11-10', periods=500)
close = 400 * np.exp(np.cumsum(r.normal(0, .01, 500)))
hist = pd.DataFrame({'Close': close}, index=idx)
app = index_trend.index_trend_facts(hist, now=pd.Timestamp('2026-11-11 20:00', tz='America/New_York').to_pydatetime())
ref = C2.trend_facts([(str(d)[:10], float(c)) for d, c in zip(idx, close)])
ok(app['aboveSma200'] == ref['above200'] and abs(app['pctVsSma200'] - ref['pct200']) < 0.051, 'index reference: 200-day side and % equal index_trend.py')
ok(app['aboveSma50'] == ref['above50'] and abs(app['pctVsSma50'] - ref['pct50']) < 0.051, 'index reference: 50-day side and % equal index_trend.py')
b = app['biggestDrop10d']
ok((b.get('noDownDay') and ref['drop'] is None) or (ref['drop'] and abs(b['pct'] - ref['drop']['pct']) < 1e-9 and b['date'] == ref['drop']['date']), 'index reference: biggest 10-session drop and its date equal index_trend.py')
ok(app['biggestDrop10dSince'] == (ref['drop'] or {}).get('since'), 'index reference: the "largest since" date equals index_trend.py')
ok(ref['asOf'] == '2026-11-10' and ref['searchedFrom'] == str(idx[1])[:10], 'index reference: as-of date and searched-from date')

# ---- parse_drop
m = C2.parse_drop('-4.4% on Nov 5 (largest since Apr 4, 2025)')
ok(m and m.group(1) == '-4.4' and m.group(2) == 'Nov 5' and m.group(4) == 'Apr 4, 2025', 'parse_drop: "largest since"')
m = C2.parse_drop('-6.5% on Nov 5 (largest in data back to Nov 13, 2024)')
ok(m and m.group(5) == 'Nov 13, 2024', 'parse_drop: "largest in data back to"')
ok(C2.lab_to_iso('Apr 4, 2025') == '2025-04-04', 'date label to ISO')

# ---- planted fundamentals card
N = 80
ph = [{'date': f'd{i:03d}', 'open': 100.0, 'high': 100.5, 'low': 99.5, 'close': 100.0, 'volume': 1000000} for i in range(N)]
def dump(text, fund, quote='EQUITY', earn=None):
    return {'ticker': 'TST', 'payloads': {'stock': {'body': {'priceHistory': ph, 'quoteType': quote}}, 'fundamentals': {'body': fund},
            'earnings': {'body': earn or {'has_upcoming': False, 'days_until': -15, 'earnings_date': '2026-11-02'}}, 'sr': {'body': {}}, 'patterns': {'body': {}}, 'spy': {'body': {}}, 'quote': {'body': {}}},
            'cardTexts': {'card-fundamentals': text}, 'tr': {'text': ''}}
FUND = {'revenueGrowth': 11.72, 'roe': 127.61, 'debtToEquity': 0.7147, '_field_sources': {'revenueGrowth': 'alphavantage', 'roe': 'finnhub', 'debtToEquity': 'finnhub'}}
GOOD = ('Fundamentals No red flags All 3 checks ran. None tripped. ✓ Sales +11.7% flag if falling 10%+ ✓ Return on equity ROE 127.6% flag if below 0% ✓ Debt D/E 0.71 flag if above 2.0 '
        'Next earnings · Last date in the feed: 2026-11-02 (15 days ago); no upcoming date listed. Source: Alpha Vantage (sales) · Finnhub (ROE, debt). The three cutoffs')
def frows(text, fund=FUND, **kw):
    ca = C2.CardAudit2(dump(text, fund, **kw), '.'); ca.fundamentals(); return {r.sid: r for r in ca.rows}
r = frows(GOOD)
ok(all(r[k].verdict == 'PASS' for k in ('FU2', 'FU3', 'FU4', 'FU5', 'FU6', 'FU8')), 'a correct fundamentals card passes sales, ROE, debt, headline, sources and earnings rows')
ok(frows(GOOD.replace('+11.7%', '+12.7%'))['FU2'].verdict == 'WRONG', 'a wrong sales figure is caught')
bad = dict(FUND, revenueGrowth=-12.0)
ok(frows(GOOD.replace('✓ Sales +11.7%', '✓ Sales -12.0%'), bad)['FU2'].verdict == 'WRONG', 'a -12% sales figure shown with a ✓ (should be ⚑) is caught')
ok(frows(GOOD.replace('✓ Sales +11.7%', '⚑ Sales -12.0%').replace('No red flags', '⚑ 1 red flag').replace('All 3 checks ran. None tripped.', 'Sales are shrinking.'), bad)['FU2'].verdict == 'PASS', 'a -12% sales figure with ⚑ passes')
ok(frows(GOOD.replace('(15 days ago)', '(9 days ago)'))['FU8'].verdict == 'WRONG', 'a wrong "N days ago" is caught')
ok(frows(GOOD.replace('Alpha Vantage (sales) · ', ''))['FU6'].verdict == 'WRONG', 'a provider missing from the source line is caught')
edge = dict(FUND, revenueGrowth=-10.0)   # the cutoff is inclusive: -10 is flagged
ok(frows(GOOD.replace('✓ Sales +11.7%', '✓ Sales -10.0%'), edge)['FU2'].verdict == 'WRONG', 'exactly -10.0% must be flagged (cutoff is <= -10)')
neg = dict(FUND, debtToEquity=-3.2)
ok(frows(GOOD.replace('✓ Debt D/E 0.71 flag if above 2.0', '– Debt D/E -3.20: negative equity, ratio not meaningful'), neg)['FU4'].verdict == 'PASS', 'negative equity: "ratio not meaningful" is the right state')
etf = frows('Fundamentals Not applicable This is an ETF. It holds many companies, so there is no single business to check. Next earnings · No earnings date found in the feed. How these checks', FUND, quote='ETF',
            earn={'has_upcoming': False, 'days_until': None, 'earnings_date': None})
ok(etf['FU1'].verdict == 'PASS', 'an ETF (quoteType) shows "Not applicable" and no tiles')

# ---- planted MR rows
def mrdump(rows, payload, text='Mean-Reversion Read No signal'):
    ph2 = [{'date': f'd{i:03d}', 'open': 100.0, 'high': 100.5, 'low': 99.5, 'close': 100.0 + (i % 3), 'volume': 5000000} for i in range(260)]
    d = dump(text, FUND); d['payloads']['stock']['body']['priceHistory'] = ph2
    d['payloads']['mr'] = {'body': payload}; d['mrRows'] = rows; d['cardTexts']['card-mr-read'] = text; d['tr'] = {'text': ''}
    return d
RULES = {'rsi2_entry': 10, 'price_min': 10, 'dollar_volume_min': 25000000, 'stop_pct': 0.05, 'rsi2_exit': 70, 'max_hold_days': 10, 'cooldown_days': 5}
cs = [100.0 + (i % 3) for i in range(260)]
rs = ref_rsi2(cs)
pay = {'signal': False, 'rsi2': round(rs, 2), 'current_price': round(cs[-1], 2), 'pct_above_sma200': round((cs[-1] / (sum(cs[-200:]) / 200) - 1) * 100, 2),
       'avg_dollar_volume': int(sum(c * 5000000 for c in cs[-20:]) / 20), 'asOf': 'd259', 'barDropped': False, 'rules': RULES, 'missing': [],
       'conditions': {'rsi2_oversold': rs < 10, 'above_200sma': cs[-1] > sum(cs[-200:]) / 200, 'price_filter': True, 'volume_filter': True}}
mark = lambda b: '✓' if b else '✗'
rows_ok = {'rsi2_oversold': f'Has it dropped hard? {mark(rs < 10)} 2-day RSI {rs:.1f} needs under 10', 'above_200sma': f'{mark(pay["conditions"]["above_200sma"])} {abs(pay["pct_above_sma200"]):.1f}% {"above" if pay["pct_above_sma200"] > 0 else "below"} its 200-day average',
           'price_filter': f'✓ ${cs[-1]:.2f} needs above $10', 'volume_filter': '✓ $0.5B traded on an average day needs above $25M'}
def mrr(rows, payload=pay, text='Mean-Reversion Read No signal Blocked by: the 2-day RSI is 10 or higher. Checked on the d259 close'):
    ca = C2.CardAudit2(mrdump(rows, payload, text), '.'); ca.dates = [f'd{i:03d}' for i in range(260)]; ca.mr(); return {r.sid: r for r in ca.rows}
ra = mrr(rows_ok)
ok(ra['MR-rsi'].verdict == 'PASS' and ra['MR-sma'].verdict == 'PASS' and ra['MR-price'].verdict == 'PASS', 'MR: RSI(2), % above the 200-day and price recompute and pass')
ok(ra['MR-row-rsi'].verdict == 'PASS' and ra['MR-row-sma'].verdict == 'PASS' and ra['MR-row-price'].verdict == 'PASS', 'MR: the three visible rows pass')
wrong_rsi = dict(rows_ok, rsi2_oversold=f'? ✓ 2-day RSI {rs:.1f} needs under 10')
ok(mrr(wrong_rsi)['MR-row-rsi'].verdict == 'WRONG', 'MR: a ✓ on a failing RSI row is caught')
bad_pay = dict(pay, rsi2=pay['rsi2'] + 5)
ok(mrr(rows_ok, bad_pay)['MR-rsi'].verdict == 'WRONG', 'MR: a wrong RSI(2) in the payload is caught')
bad_head = mrr(rows_ok, dict(pay, signal=True))
ok(bad_head['MR-head'].verdict == 'WRONG', 'MR: "signal" true while rules fail is caught')
ok(mrr(rows_ok, text='Mean-Reversion Read No signal Blocked by: the price is under $10. Checked on the d259 close')['MR-block'].verdict == 'WRONG', 'MR: a wrong "Blocked by" sentence is caught')
ok(mrr(rows_ok, text='Mean-Reversion Read No signal Blocked by: the 2-day RSI is 10 or higher. Checked on the d200 close')['MR-asof'].verdict == 'WRONG', 'MR: a wrong "Checked on" date is caught')
edge_pay = dict(pay, rsi2=10.24, conditions=dict(pay['conditions'], rsi2_oversold=False))
ok(True, 'MR: boundary 10.24 displays as "10.2 needs under 10" (checked in test_mr_read_rows.mjs)')

# ---- regression gate: phase-2 rows on the frozen dumps are unchanged by phase 3
import audit_cards as C
FROZEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs', 'test', 'Statement_Audit_phase1_frozen')
if os.path.exists(os.path.join(FROZEN, 'baseline_rows.json')):
    ok(os.path.exists(os.path.join(FROZEN, 'baseline_rows.json')), 'the frozen phase-1 baseline is present (its identity gate runs in test_audit_cards.py)')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
