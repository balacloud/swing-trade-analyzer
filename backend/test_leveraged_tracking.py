"""Tests for the leveraged-fund work (Day 135, plan STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md):
data_quality.tracking_facts / leveraged_reference, the audit's C11 (facts only) and the Tradier-blocked chain rule.
Run: cd backend && venv/bin/python test_leveraged_tracking.py"""
import json, os, sys, tempfile
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backtest'))
import data_quality as dq
import audit_data_sources as A

passed = failed = 0
def ok(cond, name):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print('FAIL', name)

rng = np.random.default_rng(7)
N = 300
dates = pd.bdate_range('2025-01-01', periods=N)
ref_ret = rng.normal(0, 0.02, N)
ref = pd.Series(100 * np.cumprod(1 + ref_ret), index=dates)
fund_ret = 2 * ref_ret
fund = pd.Series(50 * np.cumprod(1 + fund_ret), index=dates)

# ---- tracking_facts
f = dq.tracking_facts(fund, ref, 2)
ok(f['state'] == 'ok' and f['corr'] == 1.0 and abs(f['beta'] - 2.0) < 0.01 and f['n'] == N - 1, 'a perfect 2x fund: corr 1.0, beta 2.0')
ok(all(abs(w['gap_pct']) < 0.01 for w in f['worst']), 'a perfect 2x fund: no gap to the declared move')
# one bad day in the fund (a data error) is the biggest gap, with its date
bad = fund.copy(); k = 150; bad.iloc[k:] = bad.iloc[k:] * 1.16            # +16% step on one day
f = dq.tracking_facts(bad, ref, 2)
ok(f['worst'][0]['date'] == str(dates[k].date()) and 15 < f['worst'][0]['gap_pct'] < 17, 'a 16% data step is the biggest gap and carries its date')
# jump date shows fund move beside multiple x reference move
j = dq.tracking_facts(fund, ref, 2, jump_dates=[dates[10]])
ok(len(j['jumps']) == 1 and abs(j['jumps'][0]['fund_pct'] - j['jumps'][0]['expected_pct']) < 0.01, 'a jump date lists fund move beside multiple x reference move')
ok(dq.tracking_facts(fund, ref, 2, jump_dates=['1999-01-01'])['jumps'] == [], 'a jump date outside the data is skipped')
# dates are joined FIRST: a missing day in the reference must not misalign the moves
gap_ref = ref.drop(dates[100])
f2 = dq.tracking_facts(fund, gap_ref, 2)
ok(f2['state'] == 'ok' and f2['corr'] > 0.99 and abs(f2['beta'] - 2.0) < 0.05, 'a day missing in one series does not misalign the moves')
# declared multiple unknown: corr and beta only, no gap list
f3 = dq.tracking_facts(fund, ref, None)
ok(f3['state'] == 'ok' and f3['worst'] == [] and f3['multiple'] is None, 'no declared multiple: facts only, no gap list')
# beta is shown, not used: a 3x declared on a 2x fund shows the mismatch in the gaps
f4 = dq.tracking_facts(fund, ref, 3)
ok(abs(f4['beta'] - 2.0) < 0.01 and abs(f4['worst'][0]['gap_pct']) > 1.0, 'wrong declared multiple: beta 2.0 shown, large gaps shown')
# edge cases: never raise
for name, a, b in [('empty fund', fund.iloc[:0], ref), ('empty ref', fund, ref.iloc[:0]), ('None', None, ref), ('one row', fund.iloc[:1], ref.iloc[:1]),
                   ('no overlap', fund, pd.Series(ref.values, index=ref.index + pd.Timedelta(days=1000))),
                   ('flat fund', pd.Series(10.0, index=dates), ref), ('NaN fund', pd.Series(np.nan, index=dates), ref)]:
    r = dq.tracking_facts(a, b, 2)
    ok(r['state'] == 'error' and r.get('reason'), f'{name}: error with a reason, no exception')
tz = fund.copy(); tz.index = tz.index.tz_localize('America/New_York')
ok(dq.tracking_facts(tz, ref, 2)['state'] == 'ok', 'tz-aware fund index joins a naive reference')
dup = pd.concat([fund, fund.iloc[-1:]]); ok(dq.tracking_facts(dup, ref, 2)['state'] == 'ok', 'duplicate dates are tolerated')
nanrow = fund.copy(); nanrow.iloc[50] = np.nan; ok(dq.tracking_facts(nanrow, ref, 2)['state'] == 'ok', 'a NaN close row is dropped, not propagated')

# ---- leveraged_reference
ok(dq.leveraged_reference('NVDL')['reference'] == 'NVDA' and dq.leveraged_reference('nvdl')['multiple'] == 2, 'map: NVDL follows NVDA at 2x (case-insensitive)')
ok(dq.leveraged_reference('SOXL')['reference'] == 'SOXX' and dq.leveraged_reference('SOXL')['multiple'] == 3, 'map: SOXL is followed through SOXX at 3x, not SMH')
ok(dq.leveraged_reference('SOXL.NE')['reference'] == 'SOXL', 'map: SOXL.NE follows SOXL')
ok(dq.leveraged_reference('QPUX')['reference'] is None, 'map: QPUX has NO reference (never guessed)')
ok(dq.leveraged_reference('AAPL') is None and dq.leveraged_reference(None) is None, 'map: a plain stock and None are not leveraged funds')
ok(dq.leveraged_reference('NVDL', path='/nonexistent/x.json') is None, 'map: an unreadable file returns None, no exception')
bad_json = os.path.join(tempfile.mkdtemp(), 'x.json'); open(bad_json, 'w').write('{not json')
ok(dq.leveraged_reference('NVDL', path=bad_json) is None, 'map: invalid JSON returns None, no exception')
ok(all(isinstance(v, dict) and 'reference' in v for k, v in json.load(open(dq.LEVERAGED_MAP)).items() if not k.startswith('_')), 'map: every entry has a reference key')

# ---- one list of leveraged funds (Golden Rule 59): the underlying map and the Tradier-blocked list must name the same funds
from providers.fallback_policy import NO_TRADIER
mapped = {k for k in json.load(open(dq.LEVERAGED_MAP)) if not k.startswith('_')}
ok(mapped <= set(NO_TRADIER), f'every mapped fund is Tradier-blocked (missing: {sorted(mapped - set(NO_TRADIER))})')
ok(set(NO_TRADIER) - {'GDXU'} <= mapped, f'every Tradier-blocked fund is in the underlying map (missing: {sorted(set(NO_TRADIER) - {"GDXU"} - mapped)})')

# ---- chain_sources: Tradier is not part of the chain for a fund the app never serves from Tradier
ok('tradier' not in A.chain_sources('NVDL') and 'tradier' not in A.chain_sources('QPUX') and 'tradier' not in A.chain_sources('SOXL'), 'chain: Tradier dropped for blocked leveraged funds')
ok(A.chain_sources('AAPL') == ['alpaca', 'twelvedata', 'yfinance', 'tradier'], 'chain: a plain US stock keeps all four sources')
ok(A.chain_sources('SOXL.NE') == ['yfinance'] and A.chain_sources('VFV.TO') == ['yfinance'], 'chain: Canada stays Yahoo only')

# ---- grade(): the same Tradier-only error fails a plain stock but not a blocked fund
def ohlcv(closes):
    c = pd.Series(closes, index=dates)
    return pd.DataFrame({'open': c, 'high': c * 1.001, 'low': c * 0.999, 'close': c, 'volume': 1_000_000.0}, index=dates)
good = ohlcv(fund.values)
tr = fund.copy(); tr.iloc[150:] = tr.iloc[150:] * 2.9          # Tradier-only +190% step (a split error)
frames = {'alpaca': good, 'twelvedata': good.copy(), 'yfinance': good.copy(), 'tradier': ohlcv(tr.values)}
NOW = pd.Timestamp(dates[-1] + pd.Timedelta(days=1), tz='America/New_York').replace(hour=18)
A.TODAY = NOW.to_pydatetime()
g_plain = A.grade('AAPU' if False else 'ZZZZ', frames, None)
ok(g_plain['C5'][0] == 'FAIL', 'a plain stock with a Tradier-only +190% step FAILS C5')
g_lev = A.grade('NVDL', frames, None, all_frames={'NVDL': frames, 'NVDA': {'alpaca': ohlcv(ref.values)}})
ok(g_lev['C5'][0] != 'FAIL', 'the same step on a Tradier-blocked fund does NOT fail C5 (it can never be served)')
ok(g_lev['used'] == 'alpaca', 'the fund is graded on the source the app uses')
# a real problem in a served source still fails a blocked fund
bad_al = fund.copy(); bad_al.iloc[150:] = bad_al.iloc[150:] * 2.9
frames_bad = {'alpaca': ohlcv(bad_al.values), 'twelvedata': good.copy(), 'yfinance': good.copy(), 'tradier': good.copy()}
ok(A.grade('NVDL', frames_bad, None)['C5'][0] == 'FAIL', 'a blocked fund with a real step in a SERVED source still fails C5')

# ---- C11 compares the copy the app uses: a split the app's table corrects must not show as a fake gap (SOXL.NE 3:1 on 2026-05-25)
sd = pd.bdate_range('2026-05-01', '2026-06-30'); sr = rng.normal(0, 0.02, len(sd))
sref = pd.Series(100 * np.cumprod(1 + sr), index=sd)
true_fund = pd.Series(50 * np.cumprod(1 + sr), index=sd)                 # same moves as the reference (x1), already split-adjusted
raw_fund = true_fund.copy(); raw_fund[raw_fund.index < pd.Timestamp('2026-05-25')] *= 3     # Yahoo left the older bars unadjusted
raw_df = pd.DataFrame({'open': raw_fund, 'high': raw_fund * 1.001, 'low': raw_fund * 0.999, 'close': raw_fund, 'volume': 1e6}, index=sd)
ref_df = pd.DataFrame({'open': sref, 'high': sref, 'low': sref, 'close': sref, 'volume': 1e6}, index=sd)
ck = A.tracking_check('SOXL.NE', raw_df, {'SOXL': {'alpaca': ref_df}})['C11'][1]
ok('corr 1.0' in ck, 'C11: the app split table is applied first (corr 1.0, not a 60% fake gap) on SOXL.NE')
raw_only = dq.tracking_facts(raw_df['close'], sref, 1)
ok(raw_only['worst'][0]['gap_pct'] < -50, 'without the split adjustment the same data shows a fake gap of more than 50% (the problem this avoids)')

# ---- C11 is facts only and never a grade
ok(g_lev['C11'][0] == 'NA' and 'corr' in g_lev['C11'][1] and 'facts only' in g_lev['C11'][1] and 'NVDA' in g_lev['C11'][1], 'C11: not graded, note carries corr, beta, reference')
ok('C11' not in g_plain, 'C11: absent for a ticker that is not a mapped fund')
ok(A.tracking_check('QPUX', good, {})['C11'][1].startswith('no reference price'), 'C11: QPUX says it has no reference (not guessed)')
ok('not in this audit run' in A.tracking_check('NVDL', good, {'NVDL': frames})['C11'][1], 'C11: reference missing from the run is said plainly')
ok(A.tracking_check('NVDL', None, {})['C11'][0] == 'NA', 'C11: no fund data -> NA, no exception')
# C11 must never change the worst level used by the tab
ok(dq.worst([g_lev[k][0] for k in ('C2', 'C4', 'C5', 'C6', 'C11')]) == dq.worst([g_lev[k][0] for k in ('C2', 'C4', 'C5', 'C6')]), 'C11 (NA) does not change the rolled-up level')
# ---- annotate_jumps: the reference's own move beside "needs IBKR" (Day 135, plan NVDL_JUMP_NOTE_PLAN_DAY135.md)
NVDL_SEG = '2026-11-23 +62%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR)'
JMP = [{'date': '2026-11-23', 'expected_pct': 63.0, 'reference': 'NVDA', 'multiple': 2}]
a1 = dq.annotate_jumps('alpaca: ' + NVDL_SEG, JMP)
ok(a1 == 'alpaca: 2026-11-23 +62%: also in twelvedata,yfinance,tradier (real move, or unadjusted everywhere: needs IBKR; NVDA x2 that day: +63.0%)', 'the exact NVDL note gains the reference move (and keeps "needs IBKR")')
ok(dq.annotate_jumps(a1, JMP) == a1, 'idempotent: a second pass changes nothing')
two = 'alpaca: ' + NVDL_SEG + ' || twelvedata: ' + NVDL_SEG.replace('twelvedata,yfinance,tradier', 'alpaca,yfinance,tradier')
ok(dq.annotate_jumps(two, JMP).count('NVDA x2 that day: +63.0%') == 2, 'two sources with the same exact date: both segments annotated')
shifted = 'twelvedata: 2026-11-24 +62%: also in alpaca (real move, or unadjusted everywhere: needs IBKR)'
ok(dq.annotate_jumps(shifted, JMP) == shifted, 'a segment one day off is NOT annotated (exact date only)')
split_err = '2026-11-23 +62%: ONLY here; alpaca are continuous -> tradier has a split error'
ok(dq.annotate_jumps(split_err, JMP) == split_err, 'a split-error (FAIL) segment is never annotated')
lonely = '2026-11-23 +62%: no other source to compare'
ok(dq.annotate_jumps(lonely, JMP) == lonely, 'a "no other source to compare" segment is not annotated')
ok(dq.annotate_jumps('| '.join([NVDL_SEG, NVDL_SEG.replace('2026-11-23', '2026-06-25')]), JMP).count('NVDA x2') == 1, 'only the matching date of two jumps is annotated')
ok(dq.annotate_jumps(NVDL_SEG, [{'date': '2026-11-23', 'expected_pct': None, 'reference': 'NVDA', 'multiple': 2}]) == NVDL_SEG, 'no reference move that day: unchanged')
ok(dq.annotate_jumps(NVDL_SEG, [{'date': '2026-11-23', 'expected_pct': 63.0, 'reference': 'GDX', 'multiple': None}]) == NVDL_SEG, 'multiple unknown: unchanged')
ok(dq.annotate_jumps(NVDL_SEG, []) == NVDL_SEG and dq.annotate_jumps(NVDL_SEG, None) == NVDL_SEG, 'no jumps: unchanged')
ok(dq.annotate_jumps(None, JMP) is None, 'a None note does not raise')
ok('x2 that day' in dq.annotate_jumps(NVDL_SEG, [dict(JMP[0], multiple=2.0)]) and 'x2.0' not in dq.annotate_jumps(NVDL_SEG, [dict(JMP[0], multiple=2.0)]), 'a float multiple prints as x2, never x2.0')
ok('SOXL x1 that day: +1.0%' in dq.annotate_jumps(NVDL_SEG, [{'date': '2026-11-23', 'expected_pct': 1.04, 'reference': 'SOXL', 'multiple': 1}]), 'multiple 1 (SOXL.NE twin) reads "SOXL x1 that day"')
ok('-33.5%' in dq.annotate_jumps(NVDL_SEG, [dict(JMP[0], expected_pct=-33.5)]), 'a negative move keeps its sign')
# the tab line keeps the number: longest realistic case (BRK-B reference, 4 sources with eodhd, negative sign)
long_seg = 'alpaca: 2026-11-23 -62%: also in twelvedata,yfinance,tradier,eodhd (real move, or unadjusted everywhere: needs IBKR)'
long_note = dq.annotate_jumps(long_seg, [{'date': '2026-11-23', 'expected_pct': -63.0, 'reference': 'BRK-B', 'multiple': 2}])
long_chk = os.path.join(tempfile.mkdtemp(), 'a.json')
dq.update_audit_reference('truth_free', '2026-11-24T17:00', 'r.md', {'ZZ': [('C5', 'WARN', long_note)]}, path=long_chk)
line = json.load(open(long_chk))['tickers']['ZZ']['truth_free']['line']
ok('-63.0%' in line and len(line) <= 150, f'the longest realistic tab line keeps the reference number within 150 chars ({len(line)})')

# grade() end to end: annotates C5, keeps its LEVEL, and never leaks the private '_jumps' key
def step_frame(base, k, mult):
    v = base.values.copy(); v[k:] = v[k:] * mult
    return ohlcv(v)
k = 150
stepped = fund.copy(); stepped.iloc[k:] = stepped.iloc[k:] * 1.8                                    # all four sources share one +80% day
ref_step = ref.copy(); ref_step.iloc[k:] = ref_step.iloc[k:] * 1.4                                 # the reference moves +40% that day
fr = {'alpaca': ohlcv(stepped.values), 'twelvedata': ohlcv(stepped.values), 'yfinance': ohlcv(stepped.values), 'tradier': ohlcv(stepped.values)}
g2 = A.grade('NVDL', fr, None, all_frames={'NVDL': fr, 'NVDA': {'alpaca': ohlcv(ref_step.values)}})
ok('_jumps' not in g2 and '_tracking' in g2, "grade(): the private '_jumps' key never reaches the result ('_tracking' is the caller's)")
ok(g2['C5'][0] == 'WARN' and 'needs IBKR; NVDA x2 that day: +' in g2['C5'][1], 'grade(): a shared jump gets the reference move and the level stays WARN')
g3 = A.grade('NVDL', {}, None, all_frames={})
ok('_jumps' not in g3 and g3['C5'][0] == 'FAIL', "grade(): the no-data path has no '_jumps' either and still FAILs")
g4 = A.grade('NVDL', fr, None, all_frames={'NVDL': fr})
ok('NVDA x2' not in g4['C5'][1] and g4['C5'][0] == 'WARN', 'grade(): reference missing from the run: C5 text unchanged')

print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
