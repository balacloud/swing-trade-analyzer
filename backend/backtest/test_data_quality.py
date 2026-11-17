"""
Checks for data_quality.py and the side-effect-free cache readers (Day 126).
Plan: docs/claude/design/DATA_SOURCES_TAB_V2_PLAN_DAY126.md §7.1-7.2.
Run: cd backend && venv/bin/python backtest/test_data_quality.py
"""
import os
import sqlite3
import sys
from datetime import datetime

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

import data_quality as dq
from market_time import MARKET_TZ

passed = 0
NOW = datetime(2026, 11, 14, 12, 0, tzinfo=MARKET_TZ)         # Saturday noon: last session was Friday 2026-11-13
INTRADAY = datetime(2026, 11, 13, 11, 0, tzinfo=MARKET_TZ)    # Friday 11:00, session still open


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


def frame(n=300, end='2026-11-13', start=100.0, step=0.05):
    idx = pd.bdate_range(end=end, periods=n)
    c = start + step * np.arange(n)
    return pd.DataFrame({'open': c, 'high': c + 0.5, 'low': c - 0.5, 'close': c, 'volume': np.full(n, 1e6)}, index=idx)


def facts(df, now=NOW):
    return dq.check_history(df, now=now, ticker='TEST')


# ---------------------------------------------------------------- a clean stock
f = facts(frame())
check('clean stock: ok state', f['state'] == 'ok')
check('clean stock: 300 bars, last 2026-11-13, 0 sessions behind', f['bars'] == 300 and f['last_date'] == '2026-11-13' and f['sessions_behind'] == 0)
check('clean stock: no flat bars, no malformed bars, no jumps', f['flat_zero_volume_pct'] == 0 and f['bad_rows'] == 0 and f['jumps'] == [])
q = dq.quality_level(f)
check('clean stock: PASS on all four checks', q['level'] == 'PASS' and all(v['level'] == 'PASS' for v in q['checks'].values()))

# ---------------------------------------------------------------- SOXL.NE shape: close-only history (the bug the tab could not see)
d = frame(311)
d['open'] = d['high'] = d['low'] = d['close']
d['volume'] = 0.0
f = facts(d)
check('close-only history: 100% flat zero-volume', f['flat_zero_volume_pct'] == 100.0)
check('close-only history: integrity FAIL and overall FAIL', dq.quality_level(f)['checks']['integrity']['level'] == 'FAIL' and dq.quality_level(f)['level'] == 'FAIL')

# ---------------------------------------------------------------- an unadjusted 3:1 split
d = frame(300)
d.iloc[:150] = d.iloc[:150] * 3
f = facts(d)
check('3x split step: one jump found, about -67%', len(f['jumps']) == 1 and -70 < f['jumps'][0]['pct'] < -60)
check('3x split step: the jump is inside the last 260 bars', f['jumps'][0]['in_last_260'] is True)
q = dq.quality_level(f)
# Day 126 (split mechanism, plan §9 item 8): an exact whole-number step in the last 260 bars that known_splits.json does not cover is now a FAIL
check('3x split step not in the table: FAIL (possible 3-for-1 split)', q['checks']['jumps']['level'] == 'FAIL' and 'possible 3-for-1' in q['checks']['jumps']['note'] and q['level'] == 'FAIL')
d2 = frame(300)
d2.iloc[150:] = d2.iloc[150:] * 1.55
q2 = dq.quality_level(facts(d2))
check('a real +55% move is still only a WARN (not an exact factor)', q2['checks']['jumps']['level'] == 'WARN')
d = frame(400)
d.iloc[:60] = d.iloc[:60] * 3
check('old jump is marked as older than the last 260 bars', facts(d)['jumps'][0]['in_last_260'] is False)

# ---------------------------------------------------------------- short history
check('100 bars: history WARN', dq.quality_level(facts(frame(100)))['checks']['history']['level'] == 'WARN')
check('50 bars: history FAIL', dq.quality_level(facts(frame(50)))['checks']['history']['level'] == 'FAIL')
check('exactly 252 bars: history PASS', dq.quality_level(facts(frame(252)))['checks']['history']['level'] == 'PASS')

# ---------------------------------------------------------------- freshness (audit rule vs tab rule)
f = facts(frame(300, end='2026-11-12'))
check('one session behind: audit rule WARN', dq.level_freshness(f['sessions_behind'], f['forming_bar_dropped'], tolerant=False) == 'WARN')
check('one session behind: tab rule PASS with a holiday note', dq.quality_level(f)['checks']['freshness']['level'] == 'PASS'
      and 'holiday' in dq.quality_level(f)['checks']['freshness']['note'])
f = facts(frame(300, end='2026-11-06'))
check('five sessions behind: audit FAIL, tab WARN', dq.level_freshness(f['sessions_behind'], False, False) == 'FAIL'
      and dq.quality_level(f)['checks']['freshness']['level'] == 'WARN')
f = facts(frame(300, end='2026-10-30'))
check('nine sessions behind: tab FAIL', dq.quality_level(f)['checks']['freshness']['level'] == 'FAIL')

# ---------------------------------------------------------------- forming intraday bar
d = frame(300, end='2026-11-13')
d.iloc[-1, d.columns.get_loc('volume')] = 0.0        # a partial bar with no volume yet
f = facts(d, now=INTRADAY)
check('forming bar: dropped and reported', f['forming_bar_dropped'] is True and f['bars'] == 299 and f['last_date'] == '2026-11-12')
check('forming bar: does not trigger the zero-volume check', f['zero_volume_last5'] == 0)
check('forming bar: audit rule WARN, tab rule not', dq.level_freshness(f['sessions_behind'], True, False) == 'WARN'
      and dq.quality_level(f)['checks']['freshness']['level'] == 'PASS')

# ---------------------------------------------------------------- rounding vs a real malformed bar
d = frame(300)
d.iloc[100, d.columns.get_loc('low')] = d['close'].iloc[100] + 0.01            # close one cent below the low
check('one-cent rounding does not count as malformed', facts(d)['bad_rows'] == 0)
d.iloc[101, d.columns.get_loc('low')] = d['close'].iloc[101] + 1.0             # close 1.00 below the low
check('a real malformed bar is counted', facts(d)['bad_rows'] == 1)
check('one malformed bar: integrity WARN', dq.quality_level(facts(d))['checks']['integrity']['level'] == 'WARN')

# ---------------------------------------------------------------- NaN rows, empty, bad input (never raises)
d = frame(300)
d.iloc[5, d.columns.get_loc('close')] = np.nan
check('NaN close is counted and warns', facts(d)['nan_closes'] == 1 and dq.quality_level(facts(d))['checks']['integrity']['level'] == 'WARN')
check('empty frame -> error state, no raise', dq.check_history(pd.DataFrame(), now=NOW)['state'] == 'error')
check('None -> error state, no raise', dq.check_history(None, now=NOW)['state'] == 'error')
check('missing columns -> error state', dq.check_history(frame(300)[['close']], now=NOW)['state'] == 'error')
check('error facts -> quality FAIL with the reason', dq.quality_level({'state': 'error', 'reason': 'x'})['level'] == 'FAIL')
check('tz-aware index is accepted', facts(frame(300).tz_localize('America/New_York'))['state'] == 'ok')
d = frame(300); d = pd.concat([d, d.iloc[[-1]]])
check('duplicate dates are collapsed', facts(d)['bars'] == 300)

# ---------------------------------------------------------------- expected_last_session
check('Saturday -> Friday', str(dq.expected_last_session(NOW).date()) == '2026-11-13')
check('Sunday -> Friday', str(dq.expected_last_session(datetime(2026, 11, 15, 9, tzinfo=MARKET_TZ)).date()) == '2026-11-13')
check('Tuesday -> Tuesday', str(dq.expected_last_session(datetime(2026, 11, 10, 9, tzinfo=MARKET_TZ)).date()) == '2026-11-10')

# ---------------------------------------------------------------- jump_moves shared helper
check('jump_moves matches check_history', len(dq.jump_moves(frame(300).assign(close=lambda x: x['close'] * np.where(np.arange(len(x)) < 150, 3, 1)))) == 1)

# ---------------------------------------------------------------- class rules, on REAL Yahoo names (checked Day 126)
C = dq.classify_instrument
check('stock', C('EQUITY', 'Apple Inc.')['class'] == 'Stock')
check('stock (Canadian)', C('EQUITY', 'ROYAL BANK OF CANADA')['class'] == 'Stock')
check('plain ETF', C('ETF', 'VanEck Semiconductor ETF')['class'] == 'ETF')
check('plain ETF (Canadian)', C('ETF', 'ISHARES CORE EQUITY ETF')['class'] == 'ETF')
for nm in ['ADVANCED MICRO DEVICES CDR (CAD', 'MICRON CDR (CAD HEDGED)', 'BROADCOM CDR (CAD HEDGED)', 'SANDISK CDR (CAD HEDGED)', 'WESTERN DIGITAL CDR (CAD HEDGED']:
    check(f'CDR: {nm}', C('ETF' if 'ADVANCED' not in nm else 'EQUITY', nm)['class'] == 'CDR')
for nm in ['BETAPRO 3X SEMICONDUCTOR DAILY ', 'BETAPRO CDN GOLD MINERS 2X DLY ', 'Defiance 2X Daily Long Pure Qua', 'Defiance Daily Target 2X Long D',
           'Defiance Pure Space Daily 2X St', 'Direxion Daily Robotics, Artifi', 'Direxion Daily Uranium Industry', 'Direxion Daily Semiconductor Bu',
           'Defiance Daily Target 2X Long C']:
    check(f'leveraged: {nm}', C('ETF', nm)['class'] == 'Leveraged ETF')
check('BetaPro name without 2X/3X/Daily is still leveraged (the safety-net keyword)', C('ETF', 'BETAPRO NASDAQ-100 INVERSE ETF')['class'] == 'Leveraged ETF')
check('missing quote type and name -> Unknown', C(None, None)['class'] == 'Unknown')
check('name but no quote type -> Unknown with a basis', C(None, 'Something')['class'] == 'Unknown' and 'no quote type' in C(None, 'Something')['basis'])
check('odd quote type -> Unknown', C('FUTURE', 'x')['class'] == 'Unknown')
check('every class result carries a basis', all(C(q, n)['basis'] for q, n in [('EQUITY', 'a'), ('ETF', 'b'), ('ETF', 'x 2X'), ('ETF', 'y CDR'), (None, None)]))

# ---------------------------------------------------------------- worst()
check('worst picks FAIL', dq.worst(['PASS', 'WARN', 'FAIL']) == 'FAIL')
check('worst ignores NA', dq.worst(['NA', 'PASS']) == 'PASS' and dq.worst(['NA']) == 'NA' and dq.worst([]) == 'NA')

# ---------------------------------------------------------------- the cache readers (need the real cache.db; skipped if absent)
import cache_manager  # noqa: E402

db = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'cache.db')
if os.path.exists(db):
    def stats_count():
        return sqlite3.connect(db).execute('select count(*) from cache_stats').fetchone()[0]
    short = sqlite3.connect(db).execute('select ticker from ohlcv_cache where rows < 504 and rows > 60 limit 1').fetchone()
    if short:
        before = stats_count()
        df, meta = cache_manager.read_ohlcv_entry(short[0])
        check('reader: returns a cached frame under 504 rows (the old reader hides it)', df is not None and len(df) < 504)
        check('reader: meta has period, rows, source, cached_at, expired', all(k in meta for k in ('period', 'rows', 'source', 'cached_at', 'expired')))
        check('reader: writes no cache_stats event', stats_count() == before)
        # Day 126: the gate now serves a young fund fetched for 2y (stored period covers the request) and any entry with >= 95% of 504 rows,
        # so the "hidden" case is an entry stored for a SHORTER period with too few rows
        hid = sqlite3.connect(db).execute("select ticker from ohlcv_cache where rows < 478 and period != '2y' limit 1").fetchone()
        if hid:
            check('reader: the gated reader still hides a short entry stored for a shorter period', cache_manager.get_cached_ohlcv(hid[0], '2y') is None)
        cols = list(df.columns)
        check('reader: lowercase OHLCV columns', cols[:5] == ['open', 'high', 'low', 'close', 'volume'])
    check('reader: unknown ticker -> (None, None)', cache_manager.read_ohlcv_entry('ZZZZZZ9') == (None, None))
    check('fundamentals reader: unknown ticker -> (None, None)', cache_manager.read_fundamentals_entry('ZZZZZZ9') == (None, None))
    fr = sqlite3.connect(db).execute('select ticker from fundamentals_cache limit 1').fetchone()
    if fr:
        n0 = sqlite3.connect(db).execute('select count(*) from fundamentals_cache').fetchone()[0]
        data, meta = cache_manager.read_fundamentals_entry(fr[0])
        check('fundamentals reader: returns data and meta with schema_ok', isinstance(data, dict) and 'schema_ok' in meta)
        check('fundamentals reader: deletes nothing', sqlite3.connect(db).execute('select count(*) from fundamentals_cache').fetchone()[0] == n0)
else:
    print('(cache.db not found: cache reader checks skipped)')

print(f'\n{passed} checks passed')
