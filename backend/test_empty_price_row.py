"""Day 127: rows with no close price (Yahoo gave 15 cached tickers an empty newest bar on Nov 18).
Plan: docs/claude/design/EMPTY_PRICE_ROW_PLAN_DAY127.md (Opus review applied).
Rules under test: the CACHE keeps the raw row (short expiry); a SERVED frame never carries it (orchestrator._deliver,
split_adjust.fix_frame); the audit/tab reads "last bar" as the last bar WITH a price and FAILs an empty newest bar;
/api/sr and /api/stock answer with valid JSON and a real price; no fake 0.
Run: cd backend && venv/bin/python test_empty_price_row.py   (isolated cache database, fake provider, no network)"""
import io
import json
import os
import sys
import tempfile
from contextlib import redirect_stdout
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd

import backend
import cache_manager as cm
import data_quality as dq
import market_time
import split_adjust
from market_time import MARKET_TZ, drop_empty_close, newest_close_missing
from providers.orchestrator import DataProvider

passed = failed = 0


def ok(cond, msg):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        print(f'FAIL {msg}')


def frame(n=260, last='2026-11-17', seed=3, upper=False):
    r = np.random.default_rng(seed)
    idx = pd.bdate_range(end=last, periods=n)
    c = 100 + np.cumsum(r.normal(0, 1, n))
    df = pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': np.full(n, 1_000_000.0)}, index=idx)
    if upper:
        df.columns = [x.title() for x in df.columns]
    return df


def with_empty(df, which):
    """Blank open/high/low/close on the given row positions, keep volume (what Yahoo sent)."""
    out = df.copy()
    cols = [c for c in out.columns if str(c).lower() in ('open', 'high', 'low', 'close')]
    for w in which:
        out.iloc[w, [out.columns.get_loc(c) for c in cols]] = np.nan
    return out


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with redirect_stdout(buf):
        out = fn(*a, **k)
    return out, buf.getvalue()


# ---------------------------------------------------------------- helpers
base = frame()
bad_last = with_empty(base, [-1])
out, log = quiet(drop_empty_close, bad_last, 'NVDA')
ok(len(out) == len(base) - 1 and out.index[-1] == base.index[-2], 'NaN last row is dropped')
ok('NVDA' in log and '2026-11-17' in log, 'the log names the ticker and the dropped date')
ok(len(bad_last) == len(base) and bad_last['close'].isna().iloc[-1], 'the input frame is not mutated')
out, _ = quiet(drop_empty_close, with_empty(base, [0]), 'SO')
ok(len(out) == len(base) - 1 and out.index[0] == base.index[1], 'NaN FIRST row is dropped (the Yahoo leading-row artifact)')
out, _ = quiet(drop_empty_close, with_empty(base, [100, 101, 102]), 'X')
ok(len(out) == len(base) - 3, 'NaN rows in the middle are dropped')
out, log = quiet(drop_empty_close, base, 'X')
ok(out is base and log == '', 'a clean frame comes back unchanged and silent')
up = with_empty(frame(upper=True), [-1])
out, _ = quiet(drop_empty_close, up, 'X')
ok(len(out) == len(up) - 1 and list(out.columns) == list(up.columns), 'capitalised columns work and keep their names')
one = with_empty(frame(n=1), [0])
out, _ = quiet(drop_empty_close, one, 'X')
ok(len(out) == 0, 'a one-row frame with no price becomes empty, no crash')
alln = with_empty(frame(n=20), list(range(20)))
out, _ = quiet(drop_empty_close, alln, 'X')
ok(len(out) == 0, 'an all-empty frame becomes empty, no crash')
ok(drop_empty_close(None, 'X') is None, 'None passes through')
empty = base.iloc[:0]
ok(drop_empty_close(empty, 'X') is empty, 'an empty frame passes through')
nocol = base.drop(columns=['close'])
ok(drop_empty_close(nocol, 'X') is nocol, 'a frame without a close column passes through')
dup = with_empty(base, [-1]); dup = pd.concat([dup.iloc[:5], dup.iloc[:5], dup.iloc[5:]])   # duplicated dates + an empty last row
out, _ = quiet(drop_empty_close, dup, 'X')
ok(len(out) == len(dup) - 1 and not out['close'].isna().any(), 'a duplicated date index does not misalign the filter')
many = with_empty(base, list(range(10)))
_, log = quiet(drop_empty_close, many, 'X')
ok('...' in log, 'a long list of dropped dates is cut in the log')
ok(newest_close_missing(bad_last) and not newest_close_missing(base) and not newest_close_missing(None)
   and not newest_close_missing(empty) and newest_close_missing(up), 'newest_close_missing: true, false, None, empty, capitalised')

# ---------------------------------------------------------------- the served frame (the real orchestrator code)
served, _ = quiet(DataProvider._deliver, None, 'NVDA', bad_last)
ok(len(served) == len(base) - 1 and not served['close'].isna().any(), '_deliver serves no empty-price row')
served, _ = quiet(DataProvider._deliver, None, 'NVDA', with_empty(base, [0, -1]))
ok(len(served) == len(base) - 2 and not served['close'].isna().any(), '_deliver drops first and last together')
served, _ = quiet(DataProvider._deliver, None, 'NVDA', alln)
ok(len(served) == 0, '_deliver on an all-empty frame returns an empty frame (callers answer 404/503)')
ok(DataProvider._deliver(None, 'X', None) is None, '_deliver(None) is None')
fixed, _ = quiet(split_adjust.fix_frame, up, 'NVDA')
ok(len(fixed) == len(up) - 1 and list(fixed.columns) == list(up.columns) and not fixed['Close'].isna().any(),
   'fix_frame (direct-Yahoo fallbacks) drops the row and keeps column names')
fixed, _ = quiet(split_adjust.fix_frame, alln, 'X')
ok(len(fixed) == 0, 'fix_frame on an all-empty frame returns empty, no crash')

# ---------------------------------------------------------------- the cache keeps it raw, but briefly
tmp = tempfile.mkdtemp()
cm.DB_PATH = Path(tmp) / 'cache.db'                  # isolated; the real cache is never touched
for _n in ('init_database', 'init_db', 'initialize_database', 'init_cache'):
    if hasattr(cm, _n):
        getattr(cm, _n)()
        break
t0 = datetime.now(cm.ET)
quiet(cm.set_cached_ohlcv, 'BADLAST', bad_last, '2y', 'yfinance')
quiet(cm.set_cached_ohlcv, 'GOOD', base, '2y', 'yfinance')
df_bad, meta_bad = cm.read_ohlcv_entry('BADLAST')
df_ok, meta_ok = cm.read_ohlcv_entry('GOOD')
exp_bad = datetime.fromisoformat(meta_bad['expires_at'])
exp_ok = datetime.fromisoformat(meta_ok['expires_at'])
ok(exp_bad <= t0 + timedelta(minutes=cm.EMPTY_NEWEST_BAR_TTL_MIN, seconds=30), 'empty newest bar: the cache entry lives at most ~30 minutes')
ok(exp_ok >= exp_bad, 'a normal frame keeps the normal (longer or equal) expiry')
ok(abs((exp_ok - cm.calculate_ohlcv_expiry()).total_seconds()) < 5, 'a normal frame still expires at the next close + 30 min')
ok(len(df_bad) == len(base) and df_bad['close'].isna().iloc[-1], 'the CACHE keeps the raw row (audit and tab can still see it)')
ok(meta_bad['rows'] == len(base), 'the rows column matches the raw frame')
hit, _ = quiet(cm.get_cached_ohlcv, 'BADLAST', '2y')
ok(hit is not None and hit['close'].isna().iloc[-1], 'a cache hit is the raw frame (no refetch loop, no extra provider call)')
served, _ = quiet(DataProvider._deliver, None, 'BADLAST', hit)
ok(len(served) == len(base) - 1 and not served['close'].isna().any(), 'and what the app serves from that hit has no empty row')
shorter, _ = quiet(cm.get_cached_ohlcv, 'BADLAST', '1y')
ok(shorter is not None, 'a 1y request against the 2y entry is a hit, not a refetch loop')

# ---------------------------------------------------------------- audit / Data Sources tab reading
NOW = datetime(2026, 11, 19, 12, 0, tzinfo=MARKET_TZ)           # Thursday noon
f_bad = dq.check_history(bad_last, now=NOW)
f_ok = dq.check_history(base, now=NOW)
ok(f_bad['state'] == 'ok' and f_bad['newest_close_missing'] is True and not f_ok['newest_close_missing'], 'check_history flags an empty newest bar')
ok(f_bad['last_date'] == '2026-11-16' and f_ok['last_date'] == '2026-11-17', '"last bar" is the last bar WITH a price')
ok(f_bad['sessions_behind'] == f_ok['sessions_behind'] + 1, 'freshness counts the missing day as behind, not "current"')
q_bad = dq.quality_level(f_bad)
ok(q_bad['checks']['integrity']['level'] == 'FAIL' and 'NEWEST bar has no price' in q_bad['checks']['integrity']['note'],
   'the tab grades an empty newest bar FAIL and says why')
ok(dq.quality_level(f_ok)['checks']['integrity']['level'] == 'PASS', 'a clean frame still PASSes integrity')
f_first = dq.check_history(with_empty(base, [0]), now=NOW)
ok(dq.quality_level(f_first)['checks']['integrity']['level'] == 'WARN' and not f_first['newest_close_missing'],
   'an empty FIRST row is only a WARN (known Yahoo artifact)')
f_all = dq.check_history(alln, now=NOW)
ok(f_all['state'] == 'error' and 'no row has a close price' in f_all['reason'], 'a frame with no price in any row is an error, not a pass')
ok(dq.level_integrity(0, 0, 0, 0) == 'PASS' and dq.level_integrity(0, 0, 0, 0, True) == 'FAIL', 'level_integrity: old 4-argument calls still work')

# ---------------------------------------------------------------- the routes
class FakeDP:
    """Serves what the real orchestrator serves: _deliver() applied to the (raw) frame."""
    def __init__(self, df):
        self.df = df

    def get_ohlcv(self, t, p):
        return DataProvider._deliver(None, t, self.df.copy())

    def get_stock_info(self, t):
        return SimpleNamespace(data={'shortName': 'Fake', 'sector': 'S', 'industry': 'I'})


def strict_json(resp):
    def _no_nan(c):
        raise ValueError(f'invalid JSON constant {c}')
    return json.loads(resp.get_data(as_text=True), parse_constant=_no_nan)


def with_clock(now):
    real = market_time.is_forming_bar
    market_time.is_forming_bar = lambda d, now=None, _real=real, _c=now: _real(d, now=_c)
    return lambda: setattr(market_time, 'is_forming_bar', real)


client = backend.app.test_client()
backend.DATA_PROVIDER_AVAILABLE = True
backend.calculate_rsi_4h = lambda t: None            # no network
AFTER_CLOSE = datetime(2026, 11, 17, 17, 0, tzinfo=MARKET_TZ)


def get(path, df):
    backend.get_data_provider = lambda: FakeDP(df)
    undo = with_clock(AFTER_CLOSE)
    try:
        with redirect_stdout(io.StringIO()):
            return client.get(path)
    finally:
        undo()


prev_close = round(float(base['close'].iloc[-2]), 2)
r = get('/api/sr/FAKE', bad_last)
try:
    j = strict_json(r)
    valid = True
except Exception as e:  # noqa: BLE001
    j, valid = {}, False
    print('  /api/sr invalid JSON:', e)
ok(r.status_code == 200 and valid, '/api/sr on an empty newest bar: 200 and STRICT valid JSON (no NaN)')
ok(valid and j.get('currentPrice') == prev_close, '/api/sr currentPrice is the last real close, not NaN')
ok(valid and j.get('change') is not None and j['change'] == j['change'], '/api/sr change is a real number')
r = get('/api/sr/FAKE', base)
ok(r.status_code == 200 and strict_json(r)['currentPrice'] == round(float(base['close'].iloc[-1]), 2), '/api/sr on a clean frame is unchanged')

r = get('/api/stock/FAKE', bad_last)
j = strict_json(r)
ok(r.status_code == 200 and j['currentPrice'] == prev_close and j['newestDate'] == str(base.index[-2].date()),
   '/api/stock on an empty newest bar: price and newest date are the last real day')
ok(all(p['close'] == p['close'] and p['close'] > 0 for p in j['priceHistory']), '/api/stock price history has no NaN or fake zero')
r = get('/api/stock/FAKE', alln)
ok(r.status_code in (404, 503) and 'error' in strict_json(r), '/api/stock with no price in any row: a clean error, never a fake price of 0')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
