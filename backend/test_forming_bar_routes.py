"""Day 126: /api/stock, /api/market/spy and /api/patterns leave today's unfinished bar out (completed bars only).
Run: cd backend && venv/bin/python test_forming_bar_routes.py
The data provider is faked and the clock is faked by patching market_time.is_forming_bar's `now`."""
import sys
from datetime import datetime
from types import SimpleNamespace
import numpy as np
import pandas as pd
import backend
import market_time
from market_time import MARKET_TZ

passed = failed = 0
def ok(cond, msg):
    global passed, failed
    if cond: passed += 1; print(f"ok {msg}")
    else: failed += 1; print(f"FAIL {msg}")

def frame(last_date, n=260, tz=False):
    idx = pd.bdate_range(end=last_date, periods=n)
    if tz: idx = idx.tz_localize('America/New_York')
    c = 100 + np.arange(n, dtype=float)
    return pd.DataFrame({'open': c, 'high': c + 1, 'low': c - 1, 'close': c, 'volume': np.full(n, 1000)}, index=idx)

class FakeDP:
    def __init__(self, df): self.df = df
    def get_ohlcv(self, t, period): return self.df.copy()
    def get_stock_info(self, t): return SimpleNamespace(data={'shortName': 'Fake', 'sector': 'S', 'industry': 'I'})

def at(y, m, d, h, mi):
    return datetime(y, m, d, h, mi, tzinfo=MARKET_TZ)

def with_clock(now):
    real = market_time.is_forming_bar
    market_time.is_forming_bar = lambda d, now=None, _real=real, _clock=now: _real(d, now=_clock)
    return lambda: setattr(market_time, 'is_forming_bar', real)

client = backend.app.test_client()
backend.DATA_PROVIDER_AVAILABLE = True

def get(path, df, now):
    backend.get_data_provider = lambda: FakeDP(df)
    undo = with_clock(now)
    try: return client.get(path)
    finally: undo()

TUE = '2026-11-17'                      # a Tuesday
df_today = frame(TUE)                   # last bar = today
r = get('/api/stock/FAKE', df_today, at(2026, 11, 17, 11, 0))
j = r.get_json()
ok(r.status_code == 200 and j['formingBarDropped'] is True, 'mid-session: the forming bar is dropped and flagged')
ok(j['newestDate'] == '2026-11-16' and j['priceHistory'][-1]['date'] == '2026-11-16', 'mid-session: the last bar is yesterday')
ok(j['currentPrice'] == round(float(df_today['close'].iloc[-2]), 2), 'mid-session: currentPrice is yesterday\'s completed close')
ok(j['dataPoints'] == len(j['priceHistory']), 'dataPoints matches the history')

r = get('/api/stock/FAKE', df_today, at(2026, 11, 17, 16, 45))
j = r.get_json()
ok(j['formingBarDropped'] is False and j['newestDate'] == TUE, 'after 16:30 ET: today\'s bar is final and kept')
r = get('/api/stock/FAKE', df_today, at(2026, 11, 17, 16, 15))
ok(r.get_json()['formingBarDropped'] is True, '16:15 ET: still treated as forming (the cache can hold a partial bar until 16:30)')
r = get('/api/stock/FAKE', frame('2026-11-16'), at(2026, 11, 17, 9, 15))
ok(r.get_json()['formingBarDropped'] is False and r.get_json()['newestDate'] == '2026-11-16', 'pre-market: no bar for today, nothing dropped')
r = get('/api/stock/FAKE', frame('2026-11-13'), at(2026, 11, 14, 12, 0))
ok(r.get_json()['formingBarDropped'] is False and r.get_json()['newestDate'] == '2026-11-13', 'Saturday: nothing dropped')
r = get('/api/stock/FAKE', frame(TUE, tz=True), at(2026, 11, 17, 11, 0))
ok(r.get_json()['formingBarDropped'] is True and r.get_json()['newestDate'] == '2026-11-16', 'tz-aware index (Yahoo / Toronto style) drops too')

one = frame(TUE, n=1)
r = get('/api/stock/FAKE', one, at(2026, 11, 17, 11, 0))
ok(r.status_code == 404 and 'completed trading day' in r.get_json()['error'], 'an IPO with only today\'s bar: clear 404, no crash')
r = get('/api/stock/FAKE', frame(TUE, n=2), at(2026, 11, 17, 11, 0))
ok(r.status_code == 200 and r.get_json()['dataPoints'] == 1, 'two bars, one dropped: one left')
ok(len(df_today) == 260, 'the provider frame was not mutated')

# SPY: the same last date as the stock mid-session (relative strength compares the same days)
spy_df = frame(TUE).rename(columns=str.capitalize)
backend._index_history = lambda t: spy_df.copy()
undo = with_clock(at(2026, 11, 17, 11, 0))
try: rs = client.get('/api/market/spy'); js = rs.get_json()
finally: undo()
ok(rs.status_code == 200 and js['priceHistory'][-1]['date'] == '2026-11-16', 'SPY mid-session: last bar is yesterday, same as the stock')
ok(js['currentPrice'] == round(float(spy_df['Close'].iloc[-2]), 2), 'SPY currentPrice is the completed close')

# Patterns: completed bars only, and the 100-bar check counts completed bars
seen = {}
real_detect = backend.detect_patterns
backend.detect_patterns = lambda d: (seen.setdefault('n', len(d)), seen.setdefault('last', str(d.index[-1])[:10]), {})[2]
try:
    r = get('/api/patterns/FAKE', frame(TUE, n=300), at(2026, 11, 17, 11, 0))
    ok(seen.get('last') == '2026-11-16' and seen.get('n') == 299, 'patterns: the forming bar is not given to the detector')
    r = get('/api/patterns/FAKE', frame(TUE, n=100), at(2026, 11, 17, 11, 0))
    ok(r.status_code == 400, 'patterns: 100 bars with today forming = 99 completed, short-history 400')
finally:
    backend.detect_patterns = real_detect

# ---- price52wAgo with a leading NaN row (a 1-year Yahoo frame starts empty): must come from the first real close, not None
nanf = frame('2026-11-16', n=252)
nanf.iloc[0, nanf.columns.get_loc('close')] = np.nan
r = get('/api/stock/FAKE', nanf, at(2026, 11, 17, 9, 15)); j = r.get_json()
ok(r.status_code == 200 and j['price52wAgo'] is not None and j['price13wAgo'] is not None, 'a leading NaN row does not blank price52wAgo / price13wAgo (RS card N/A bug)')
ok(j['price52wAgo'] == round(float(nanf['close'].dropna().iloc[0]), 2) or j['price52wAgo'] == round(float(nanf['close'].dropna().iloc[-252]), 2), 'price52wAgo is the first real close of the window')

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
