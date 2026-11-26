"""Tests for the Analyze header data notes (Day 135, plan DATA_NOTES_PLAN_DAY135.md): data_quality.cached_quality / data_notes / read_tracking,
update_audit_reference(tracking=...), and that the page (/api/stock) and the tab (/api/provenance) quote the SAME integrity text.
Run: cd backend && venv/bin/python test_data_notes.py"""
import json, os, sys, tempfile
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data_quality as dq
import cache_manager

passed = failed = 0
def ok(cond, name):
    global passed, failed
    if cond: passed += 1
    else:
        failed += 1; print('FAIL', name)

N = 300
dates = pd.bdate_range('2025-01-01', periods=N)
rng = np.random.default_rng(3)
def frame(flat_pct=0.0, bad_rows=0, nan_newest=False):
    c = pd.Series(100 * np.cumprod(1 + rng.normal(0, 0.01, N)), index=dates)
    df = pd.DataFrame({'open': c, 'high': c * 1.002, 'low': c * 0.998, 'close': c, 'volume': 1_000_000.0}, index=dates)
    k = int(N * flat_pct)
    if k:
        df.iloc[:k, df.columns.get_loc('high')] = df['low'].iloc[:k]; df.iloc[:k, df.columns.get_loc('volume')] = 0.0
        df.iloc[:k, df.columns.get_loc('open')] = df['low'].iloc[:k]; df.iloc[:k, df.columns.get_loc('close')] = df['low'].iloc[:k]
    for i in range(bad_rows):
        df.iloc[100 + i, df.columns.get_loc('high')] = df['close'].iloc[100 + i] * 0.9     # high below the close: malformed
    if nan_newest:
        df.iloc[-1, df.columns.get_loc('close')] = np.nan
    return df

META = {'period': '2y', 'rows': N, 'source': 'yfinance', 'cached_at': '2026-11-25T18:00:00-05:00', 'expires_at': '2026-11-26T18:00:00-05:00', 'expired': False}
def with_cache(df, meta=META):
    cache_manager.read_ohlcv_entry = lambda t: (df, meta)

real_read = cache_manager.read_ohlcv_entry
# ---- cached_quality / data_notes on planted frames
with_cache(frame())
n = dq.data_notes('ZZTEST')
ok(n['integrity'] is None, 'a clean frame: no integrity note')
with_cache(frame(flat_pct=0.8))
n = dq.data_notes('ZZTEST')
ok(n['integrity'] and n['integrity']['level'] == 'FAIL' and '80% of bars flat with zero volume' in n['integrity']['note'], '80% flat zero-volume bars: FAIL with the tab wording')
ok(n['integrity']['bars'] == N and n['integrity']['since'] == str(dates[0].date()), 'the note says which saved bars it covers')
with_cache(frame(bad_rows=25))
n = dq.data_notes('ZZTEST')
ok(n['integrity'] and '25 malformed bars' in n['integrity']['note'], 'malformed bars are counted in the note')
with_cache(frame(nan_newest=True))
q = dq.cached_quality('ZZTEST')
ok(q['state'] == 'ok' and 'NEWEST bar has no price' in q['checks']['integrity']['note'], 'raw frame: an empty newest row is counted (the served frame would hide it)')
# the note equals the tab's block for the same frame: ONE builder
with_cache(frame(flat_pct=0.3))
ok(dq.data_notes('ZZTEST')['integrity']['note'] == dq.cached_quality('ZZTEST')['checks']['integrity']['note'], 'data_notes quotes cached_quality unchanged')
# states that must give NO integrity note (never an invented FAIL)
cache_manager.read_ohlcv_entry = lambda t: (None, None)
ok(dq.cached_quality('ZZTEST') == {'state': 'not_cached'} and dq.data_notes('ZZTEST')['integrity'] is None, 'not cached: no note')
with_cache(frame().iloc[:0])
ok(dq.data_notes('ZZTEST')['integrity'] is None, 'empty frame: no note')
with_cache(frame().iloc[:1])
ok(isinstance(dq.data_notes('ZZTEST'), dict), 'one row: returns a dict, no exception')
def boom(t): raise RuntimeError('db locked')
cache_manager.read_ohlcv_entry = boom
q = dq.cached_quality('ZZTEST')
ok(q['state'] == 'error' and 'db locked' in q['reason'] and dq.data_notes('ZZTEST')['integrity'] is None, 'a cache error: state error, no note, no exception')
no_vol = frame().drop(columns=['volume']); with_cache(no_vol)
ok(dq.data_notes('ZZTEST')['integrity'] is None, 'no volume column: error state, no note')
cache_manager.read_ohlcv_entry = real_read

# ---- update_audit_reference(tracking=...) and read_tracking
tmp = os.path.join(tempfile.mkdtemp(), 'audit.json'); mp = os.path.join(os.path.dirname(tmp), 'map.json')
json.dump({'NVDL': {'reference': 'NVDA', 'multiple': 2}, 'SOXL': {'reference': 'SOXX', 'multiple': 3}}, open(mp, 'w'))
chk = {'NVDL': [('C5', 'WARN', 'x')], 'SOXL': [('C5', 'PASS', '')], 'AAPL': [('C5', 'PASS', '')]}
trk = {'NVDL': {'reference': 'NVDA', 'multiple': 2, 'corr': 1.0, 'beta': 1.98, 'n': 503}, 'SOXL': {'reference': 'SOXX', 'multiple': 3, 'corr': 0.999, 'beta': 2.96, 'n': 503}}
dq.update_audit_reference('truth_free', '2026-11-24T17:00', 'r.md', chk, path=tmp, tracking=trk)
ok((dq.read_tracking('NVDL', path=tmp, map_path=mp) or {}).get('corr') == 1.0 and (dq.read_tracking('nvdl', path=tmp, map_path=mp) or {}).get('date') == '2026-11-24', 'tracking written with the run date, read case-insensitively')
ok(dq.read_tracking('AAPL', path=tmp, map_path=mp) is None, 'a ticker without tracking: None')
ok(dq.read_audit_summary('NVDL', path=tmp)['level'] == 'WARN' and dq.read_audit_summary('NVDL', path=tmp)['section'] == 'truth_free', 'read_audit_summary ignores the tracking entry (no level key)')
ok(dq.read_audit_summary('SOXL', path=tmp) is None, 'a ticker whose sections all pass still reads as None with a tracking entry present')
# tracking=None leaves stored entries alone (the IBKR audit calls without it)
dq.update_audit_reference('vs_ibkr', '2026-11-25T09:00', 'i.md', chk, path=tmp)
ok(dq.read_tracking('NVDL', path=tmp, map_path=mp) is not None, 'tracking=None leaves the stored entry alone')
# an explicit dict deletes entries for symbols missing from it
dq.update_audit_reference('truth_free', '2026-11-26T09:00', 'r.md', chk, path=tmp, tracking={'NVDL': trk['NVDL']})
ok(dq.read_tracking('SOXL', path=tmp, map_path=mp) is None and dq.read_tracking('NVDL', path=tmp, map_path=mp) is not None, 'a symbol missing from an explicit dict loses its stored entry')
ok(dq.read_tracking('NVDL', path=tmp, map_path=mp)['date'] == '2026-11-26', 'a fresh run replaces the stored entry')
# a stored entry does not outlive the map
json.dump({'NVDL': {'reference': 'AAPL', 'multiple': 2}}, open(mp, 'w'))
ok(dq.read_tracking('NVDL', path=tmp, map_path=mp) is None, 'the map now names another reference: stored entry hidden')
json.dump({}, open(mp, 'w'))
ok(dq.read_tracking('NVDL', path=tmp, map_path=mp) is None, 'fund removed from the map: stored entry hidden')
ok(dq.read_tracking('NVDL', path='/nonexistent/a.json', map_path=mp) is None, 'a missing audit file: None, no exception')
bad = os.path.join(os.path.dirname(tmp), 'bad.json'); open(bad, 'w').write('{nope')
ok(dq.read_tracking('NVDL', path=bad, map_path=mp) is None, 'an invalid audit file: None, no exception')

# ---- the page and the tab quote the SAME text (real cache; the tickers with an integrity note today)
import backend as B
c = B.app.test_client()
checked = 0
for t in ('XDRV.TO', 'CARS.TO', 'FINN.NE', 'SOXL.NE'):
    q = dq.cached_quality(t)
    if q.get('state') != 'ok':
        continue
    tab = c.get(f'/api/provenance/{t}').get_json()['quality']['checks']['integrity']
    page = dq.data_notes(t)['integrity']
    if tab['level'] in ('WARN', 'FAIL'):
        checked += 1
        ok(page is not None and page['note'] == tab['note'] and page['level'] == tab['level'], f'{t}: the page note is the tab note, word for word')
    else:
        ok(page is None, f'{t}: tab PASS gives no page note')
ok(checked >= 1, 'at least one real thin ticker was compared (page vs tab)')
print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
