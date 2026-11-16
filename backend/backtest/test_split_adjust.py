"""
Split mechanism tests (Day 126). Plan: docs/claude/design/SPLIT_MECHANISM_PLAN_DAY126.md (v2 §9).
Run: cd backend && venv/bin/python backtest/test_split_adjust.py
Synthetic cases + the REAL frames saved in validation_results/data_audit_cache_20261114.json (SOXL.NE unadjusted; QPUX/SOXX/GDXU.TO/AMD.TO/MU.TO
already adjusted by providers, QPUX on Tradier adjusted the wrong way).
"""
import io
import json
import os
import sys
import tempfile

import numpy as np
import pandas as pd

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BACKEND)
import split_adjust as S
import data_quality as Q

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
        print(f'FAIL {name} {detail}')


def frame(n=80, split_at=None, ratio=3.0, real_move=1.0, seed=1, start='2026-03-02'):
    """Business-day frame. If split_at is given, bars BEFORE it are x ratio too high (the provider did NOT adjust), and the split-day bar also
    carries `real_move` (a genuine move on top of the split)."""
    r = np.random.default_rng(seed)
    c = 50 * np.exp(np.cumsum(r.normal(0, .01, n)))
    if split_at is not None:
        c = c.copy()
        c[:split_at] = c[:split_at] * ratio
        c[split_at:] = c[split_at:] * real_move
    h, l = c * 1.005, c * 0.995
    return pd.DataFrame({'open': c, 'high': h, 'low': l, 'close': c, 'volume': np.full(n, 1_000_000.0)}, index=pd.bdate_range(start, periods=n))


def table(rows):
    f = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False)
    json.dump(rows, f)
    f.close()
    return f.name


def row(sym, date, ratio, url='https://example.com/notice'):
    return {'symbol': sym, 'date': date, 'ratio': ratio, 'source_url': url}


def date_at(df, i):
    return str(df.index[i].date())


# ---------------------------------------------------------------- 1. synthetic cases
f = frame(split_at=40, ratio=3.0)
t = table([row('AAA', date_at(f, 40), 3)])
before = f.copy()
a, ev = S.adjust_for_splits(f, 'AAA', t)
check('3:1 unadjusted: applied', ev and ev[0]['status'] == 'unadjusted' and ev[0]['applied'], str(ev))
check('3:1: bars before the split divided by 3', np.allclose(a.close.iloc[:40].to_numpy(), f.close.iloc[:40].to_numpy() / 3))
check('3:1: high/low/open divided too', np.allclose(a.high.iloc[:40], f.high.iloc[:40] / 3) and np.allclose(a.low.iloc[:40], f.low.iloc[:40] / 3) and np.allclose(a.open.iloc[:40], f.open.iloc[:40] / 3))
check('3:1: volume before the split multiplied by 3', np.allclose(a.volume.iloc[:40], 3_000_000.0))
check('3:1: bars on/after the split untouched', a.iloc[40:].equals(f.iloc[40:]))
check('input frame not modified (a copy is returned)', f.equals(before))
check('the series is continuous after adjusting (no 40% step)', not Q.jump_moves(a))
a2, ev2 = S.adjust_for_splits(a, 'AAA', t)
check('idempotent: adjusting twice == once', a2.equals(a) and ev2[0]['status'] == 'already_adjusted' and not ev2[0]['applied'])

# reverse 1-for-25 (ratio 0.04): old prices are 25x too LOW
r = frame(split_at=40, ratio=0.04)
a, ev = S.adjust_for_splits(r, 'BBB', table([row('BBB', date_at(r, 40), 0.04)]))
check('1:25 reverse: applied and old prices x25', ev[0]['applied'] and np.allclose(a.close.iloc[:40], r.close.iloc[:40] * 25))
check('1:25 reverse: volume divided by 25', np.allclose(a.volume.iloc[:40], 1_000_000 / 25))

# provider already adjusted: no step at all
g = frame()
a, ev = S.adjust_for_splits(g, 'AAA', table([row('AAA', date_at(g, 40), 3)]))
check('already adjusted by the provider: nothing done', ev[0]['status'] == 'already_adjusted' and a.equals(g))

# step one bar off the table date (issuer and provider dates differ)
f = frame(split_at=40)
a, ev = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 41), 3)]))
check('step one bar BEFORE the table date: still applied, at the real bar', ev[0]['applied'] and ev[0]['bar_date'] == date_at(f, 40), str(ev))
a, ev = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 39), 3)]))
check('step one bar AFTER the table date: still applied, at the real bar', ev[0]['applied'] and ev[0]['bar_date'] == date_at(f, 40), str(ev))

# table date on a weekend / holiday with no bar: first bar on/after
f = frame(split_at=40)
sat = str((f.index[40] - pd.Timedelta(days=2)).date())      # a weekend before the step bar
check('table date on a non-trading day uses the next bar', S.adjust_for_splits(f, 'AAA', table([row('AAA', sat, 3)]))[1][0]['applied'])

# a real move on split day
f = frame(split_at=40, real_move=1.2)
check('3:1 split with a real +20% move that day: applied', S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 3)]))[1][0]['applied'])
f = frame(split_at=40, real_move=1.55)
ev = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 3)]))[1][0]
check('3:1 split with a huge +55% move that day: NOT guessed (ambiguous, not applied)', ev['status'] == 'ambiguous' and not ev['applied'], str(ev))

# adjusted the wrong way (QPUX on Tradier looked like this): reverse 1:3, step x0.31 instead of x3
f = frame()
f.iloc[40:, :4] = f.iloc[40:, :4] * 0.3129
ev = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 1 / 3)]))[1][0]
check('wrong-way adjustment: FAIL status, not adjusted', ev['status'] == 'wrong_way' and not ev['applied'], str(ev))

# dates outside the frame
g = frame()
check('split date before the first bar: not applicable', S.adjust_for_splits(g, 'AAA', table([row('AAA', '2020-01-02', 3)]))[1][0]['status'] == 'not_applicable')
check('split date after the last bar: pending', S.adjust_for_splits(g, 'AAA', table([row('AAA', '2030-01-02', 3)]))[1][0]['status'] == 'pending')

# two splits in one history
two = frame(n=120)
two.iloc[:50, :4] *= 3.0 * 2.0
two.iloc[50:90, :4] *= 2.0
a, ev = S.adjust_for_splits(two, 'AAA', table([row('AAA', date_at(two, 50), 3), row('AAA', date_at(two, 90), 2)]))
check('two splits in one history: both applied, series continuous', all(e['applied'] for e in ev) and not Q.jump_moves(a) and len(ev) == 2, str(ev))

# 3:2 split uses the exact bar only
f = frame(split_at=40, ratio=1.5)
check('3:2 split: applied on the exact bar', S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 1.5)]))[1][0]['applied'])
f = frame(split_at=40, ratio=1.5)
check('3:2 split one bar off: not guessed', not S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 41), 1.5)]))[1][0]['applied'])

# Yahoo returns timezone-aware indexes (this broke the first live run); results must be identical to the naive case
f = frame(split_at=40)
ft = f.copy(); ft.index = ft.index.tz_localize('America/Toronto')
at, evt = S.adjust_for_splits(ft, 'AAA', table([row('AAA', date_at(f, 40), 3)]))
an, evn = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 3)]))
check('timezone-aware index (Yahoo, America/Toronto): applied, same numbers as the naive frame', evt[0]['applied'] and np.allclose(at.close.to_numpy(), an.close.to_numpy()) and str(at.index.tz) == 'America/Toronto', str(evt))
check('timezone-aware index: the returned frame keeps its timezone-aware index', at.index.equals(ft.index))
fu = f.copy(); fu.index = fu.index.tz_localize('UTC')
check('UTC-aware index also works', S.adjust_for_splits(fu, 'AAA', table([row('AAA', date_at(f, 40), 3)]))[1][0]['applied'])
check('data_quality accepts a timezone-aware frame', Q.check_history(ft, ticker='AAA')['state'] == 'ok')

# ---------------------------------------------------------------- 2. the table itself
check('empty frame / None never crash', S.adjust_for_splits(None, 'AAA')[0] is None and len(S.adjust_for_splits(pd.DataFrame(), 'AAA')[0]) == 0)
bad = table([row('A', '2026-01-02', 0), row('B', '2026-01-02', 1), {'symbol': 'C', 'date': '2026-01-02', 'ratio': 3}, row('D', 'not a date', 3),
             row('E', '2026-01-02', 3), row('E', '2026-01-02', 2)])
rows, errs = S.load_table(bad)
check('table validation: ratio 0, ratio 1, no source, bad date and duplicate are all rejected with a reason', len(rows) == 1 and len(errs) == 5, f'{len(rows)} rows {errs}')
rows, errs = S.load_table('/nonexistent/known_splits.json')
check('missing table: no rows and a reason, no exception', rows == [] and errs)
junk = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False); junk.write('{not json'); junk.close()
rows, errs = S.load_table(junk.name)
check('unreadable table: no rows and a reason, no exception', rows == [] and errs)
f = frame(split_at=40)
a, ev = S.adjust_for_splits(f, 'AAA', table([row('AAA', date_at(f, 40), 0)]))
check('a malformed row is reported and nothing is adjusted', a.equals(f) and any(e['status'] == 'table_error' for e in ev))
check('the live table loads clean and has SOXL.NE', S.rows_for('SOXL.NE')[0] and not S.rows_for('SOXL.NE')[1])
check('symbols match exactly (SOXL.TO is not SOXL.NE)', not S.rows_for('SOXL.TO')[0] and not S.rows_for('SOXL')[0])
check('describe(): forward and reverse wording', S.describe({'ratio': 3.0, 'date': pd.Timestamp('2026-05-25')}) == '3-for-1 on 2026-05-25'
      and S.describe({'ratio': 0.04, 'date': pd.Timestamp('2026-05-25')}) == '1-for-25 on 2026-05-25')

# ---------------------------------------------------------------- 3. detector signature
check('detector: exact 1/3 step is a possible 3-for-1', S.possible_split_k(47.24 / 141.84) == 3)
check('detector: exact x25 step is a possible 1-for-25 reverse', S.possible_split_k(25.0) == -25)
for name, st in [('SOXL +54.8% (2025-04-09)', 1.548), ('QPUX +47.6%', 1.476), ('SPCL +56.6%', 1.566), ('^VIX +69.7%', 1.697), ('a -50% crash', 0.5), ('-40%', 0.6), ('Tradier QPUX wrong-way x0.3129', 0.3129)]:
    check(f'detector: real move is not a split signature: {name}', S.possible_split_k(st) is None)
check('detector: junk input is safe', S.possible_split_k(None) is None and S.possible_split_k(0) is None and S.possible_split_k(float('nan')) is None)

# ---------------------------------------------------------------- 4. real frames
raw = json.load(open(os.path.join(BACKEND, 'validation_results', 'data_audit_cache_20261114.json')))


def real(sym, src):
    v = raw[sym][src]
    f = pd.read_csv(io.StringIO(v['csv']), index_col=0, parse_dates=True)
    f.columns = [c.lower() for c in f.columns]
    f.index = pd.to_datetime(f.index).normalize()
    return f[['open', 'high', 'low', 'close', 'volume']].astype(float)


fz = real('SOXL.NE', 'yfinance'); fzt = fz.copy(); fzt.index = fzt.index.tz_localize('America/Toronto')
check('has_split_in_window: SOXL.NE yes (naive and timezone-aware index)', S.has_split_in_window(fz, 'SOXL.NE') and S.has_split_in_window(fzt, 'SOXL.NE'))
check('has_split_in_window: other tickers and a split before the first bar are no', not S.has_split_in_window(fz, 'GDXU.TO') and not S.has_split_in_window(fz.loc['2026-06-01':], 'SOXL.NE') and not S.has_split_in_window(None, 'SOXL.NE'))

# broken frames fail loudly (review pass 3): never a silent "already adjusted"
fz2 = real('SOXL.NE', 'yfinance')
x = fz2.copy(); x.loc['2026-05-25', 'close'] = np.nan
ev = S.adjust_for_splits(x, 'SOXL.NE')[1][0]
check('NaN close on the split day: ambiguous (not a silent "already adjusted"), not adjusted', ev['status'] == 'ambiguous' and not ev['applied'], str(ev))
x = fz2.copy(); x.loc['2026-05-22', 'close'] = np.nan
check('NaN close the day before the split: ambiguous, not adjusted', S.adjust_for_splits(x, 'SOXL.NE')[1][0]['status'] == 'ambiguous')
ev = S.adjust_for_splits(fz2.sample(frac=1, random_state=1), 'SOXL.NE')[1][0]
check('unsorted history: ambiguous, not adjusted', ev['status'] == 'ambiguous' and not ev['applied'])
dup = pd.concat([fz2, fz2.iloc[-3:]]).sort_index(kind='stable')
check('frame with duplicate dates (still in date order) adjusts; one appended out of order does not', S.adjust_for_splits(dup, 'SOXL.NE')[1][0]['applied'] and S.adjust_for_splits(pd.concat([fz2, fz2.iloc[-3:]]), 'SOXL.NE')[1][0]['status'] == 'ambiguous')
check('no volume column: prices still adjusted', S.adjust_for_splits(fz2.drop(columns=['volume']), 'SOXL.NE')[1][0]['applied'])

for src in ('yfinance', 'eodhd'):
    f = real('SOXL.NE', src)
    a, ev = S.adjust_for_splits(f, 'SOXL.NE')
    check(f'real SOXL.NE ({src}): applied at 2026-05-25', ev[0]['applied'] and ev[0]['bar_date'] == '2026-05-25', str(ev))
    check(f'real SOXL.NE ({src}): no one-day move over 40% left', not Q.jump_moves(a))
    check(f'real SOXL.NE ({src}): last pre-split close 141.84 -> 47.28', abs(a.close['2026-05-22'] - 47.28) < 0.01 and abs(f.close['2026-05-22'] - 141.84) < 0.01)
    check(f'real SOXL.NE ({src}): bars from the split on are untouched', a.loc['2026-05-25':].equals(f.loc['2026-05-25':]))
    hi, lo = S.adjusted_52w(a)
    check(f'real SOXL.NE ({src}): adjusted 52-week high is below the raw pre-split 141.84', hi is not None and hi < 100 and lo is not None and lo < hi, f'{hi} {lo}')

sys.path.insert(0, os.path.join(BACKEND, 'backtest'))
import simple_sr
f = real('SOXL.NE', 'yfinance')
a, _ = S.adjust_for_splits(f, 'SOXL.NE')
atr_raw, atr_adj = simple_sr.wilder_atr(f), simple_sr.wilder_atr(a)
check('real SOXL.NE: ATR is smaller after adjusting (the raw one was inflated by the x3 old prices)', atr_adj < atr_raw, f'{atr_raw} {atr_adj}')

# providers that already adjusted: the table row must be a no-op on their real frames
noop = [('QPUX', 'yfinance', '2026-03-23', 1 / 3), ('QPUX', 'twelvedata', '2026-03-23', 1 / 3), ('SOXX', 'twelvedata', '2026-11-05', 3), ('SOXX', 'yfinance', '2026-11-05', 3),
        ('GDXU.TO', 'yfinance', '2026-05-25', 3), ('AMD.TO', 'yfinance', '2026-10-16', 7), ('MU.TO', 'yfinance', '2026-03-10', 5)]
for sym, src, date, ratio in noop:
    f = real(sym, src)
    a, ev = S.adjust_for_splits(f, sym, table([row(sym, date, ratio)]))
    check(f'real {sym} ({src}) already adjusted by the provider: no change', a.equals(f) and ev[0]['status'] == 'already_adjusted', str(ev))
f = real('QPUX', 'tradier')
ev = S.adjust_for_splits(f, 'QPUX', table([row('QPUX', '2026-03-23', 1 / 3)]))[1][0]
check('real QPUX on Tradier (adjusted the wrong way, one bar early): flagged, not adjusted', ev['status'] == 'wrong_way' and not ev['applied'], str(ev))

# ---------------------------------------------------------------- 5. data_quality integration
f = real('SOXL.NE', 'yfinance')
q = Q.quality_level(Q.check_history(f, ticker='SOXL.NE'))
check('data_quality: SOXL.NE jump is explained by the table (jumps PASS)', q['checks']['jumps']['level'] == 'PASS', str(q['checks']['jumps']))
facts = Q.check_history(f, ticker='SOXL.NE')
check('data_quality: facts carry the split for the tab', facts['splits'] and facts['splits'][0]['status'] == 'unadjusted' and facts['splits'][0]['text'] == '3-for-1 on 2026-05-25')
q2 = Q.quality_level(Q.check_history(f, ticker='SOXL.TO'))
check('data_quality: the same jump on a ticker NOT in the table is a FAIL', q2['checks']['jumps']['level'] == 'FAIL' and 'possible 3-for-1' in q2['checks']['jumps']['note'], str(q2['checks']['jumps']))
check('data_quality: SOXL.NE overall stays FAIL (100% flat zero-volume bars)', q['level'] == 'FAIL')
tf = real('QPUX', 'tradier')
real_move = frame(n=80)
real_move.iloc[40:, :4] *= 1.55
q3 = Q.quality_level(Q.check_history(real_move, ticker='ZZZ'))
check('data_quality: a real +55% move stays a WARN, not a FAIL', q3['checks']['jumps']['level'] == 'WARN', str(q3['checks']['jumps']))
check('data_quality: no ticker given still works', Q.check_history(real_move)['state'] == 'ok')

# ---------------------------------------------------------------- 6. orchestrator delivery
from providers.orchestrator import DataProvider
src_frame = real('SOXL.NE', 'yfinance')
out = DataProvider._deliver(None, 'SOXL.NE', src_frame)
check('orchestrator _deliver: SOXL.NE comes out adjusted and the input is untouched', abs(out.close['2026-05-22'] - 47.28) < 0.01 and abs(src_frame.close['2026-05-22'] - 141.84) < 0.01)
other = real('GDXU.TO', 'yfinance')
check('orchestrator _deliver: a ticker not in the table is returned equal', DataProvider._deliver(None, 'GDXU.TO', other).equals(other))
check('orchestrator _deliver: None passes through', DataProvider._deliver(None, 'X', None) is None)
real_fn = S.adjust_for_splits
S.adjust_for_splits = lambda *a, **k: (_ for _ in ()).throw(RuntimeError('boom'))
safe = DataProvider._deliver(None, 'SOXL.NE', src_frame)
S.adjust_for_splits = real_fn
check('orchestrator _deliver: an adjuster failure serves the unadjusted frame, no exception', safe.equals(src_frame))
check('fix_frame: any column case works and names come back', list(S.fix_frame(src_frame.rename(columns=str.title), 'SOXL.NE').columns) == [c.title() for c in src_frame.columns]
      and abs(S.fix_frame(src_frame.rename(columns=str.title), 'SOXL.NE')['Close']['2026-05-22'] - 47.28) < 0.01)

print(f'\n{PASS} passed, {FAIL} failed')
sys.exit(1 if FAIL else 0)
