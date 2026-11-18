"""Day 126 (Statement Audit fixes): /api/sr volume availability, completed-bar ADX/OBV, unrounded closeLocation; /api/stock 52-week high/low from the bars.
Run: cd backend && venv/bin/python test_sr_volume_unavailable.py   (fake provider, frozen clock, no network)"""
import sys
from datetime import datetime
from types import SimpleNamespace
import numpy as np
import pandas as pd
import backend
import market_time
from market_time import MARKET_TZ
from breakout_detection import MIN_VOLUME_BARS

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1; print(f'ok {m}')
    else: failed += 1; print(f'FAIL {m}')

def frame(last='2026-11-17', n=260, vol=1_000_000, vol_days=None, seed=3):
    r = np.random.default_rng(seed)
    idx = pd.bdate_range(end=last, periods=n)
    c = 100 + np.cumsum(r.normal(0, 1, n))
    h, l = c + np.abs(r.normal(0, .8, n)) + .1, c - np.abs(r.normal(0, .8, n)) - .1
    v = np.full(n, float(vol))
    if vol_days is not None:               # only the last `vol_days` COMPLETED days (the forming bar excluded) carry volume
        v[:] = 0.0; v[n - 1 - vol_days: n - 1] = vol
    return pd.DataFrame({'open': c, 'high': h, 'low': l, 'close': c, 'volume': v}, index=idx)

class FakeDP:
    def __init__(self, df, info=None): self.df, self.info = df, info or {'shortName': 'Fake', 'fiftyTwoWeekHigh': 999.0, 'fiftyTwoWeekLow': 1.0}
    def get_ohlcv(self, t, p): return self.df.copy()
    def get_stock_info(self, t): return SimpleNamespace(data=dict(self.info))

def at(h, m): return datetime(2026, 11, 17, h, m, tzinfo=MARKET_TZ)
def with_clock(now):
    real = market_time.is_forming_bar
    market_time.is_forming_bar = lambda d, now=None, _real=real, _c=now: _real(d, now=_c)
    return lambda: setattr(market_time, 'is_forming_bar', real)

client = backend.app.test_client(); backend.DATA_PROVIDER_AVAILABLE = True
backend.calculate_rsi_4h = lambda t: None            # no network
def get(path, df, now, **kw):
    backend.get_data_provider = lambda: FakeDP(df, **kw)
    undo = with_clock(now)
    try: return client.get(path)
    finally: undo()

def sr(df, now): r = get('/api/sr/FAKE', df, now); return r, (r.get_json() or {})

ok(MIN_VOLUME_BARS == 40, 'the availability rule imports the breakout constant (40 of 50)')

# --- normal fund, mid-session: volume available, closeLocation not rounded to 2 dp
r, j = sr(frame(), at(11, 0)); m = j.get('meta', {})
ok(r.status_code == 200 and m.get('volume') == {'available': True, 'daysWithVolume': 50, 'windowBars': 50}, 'normal fund: volume available (50 of 50 days)')
ok(m.get('rvol') is not None and m.get('obv') is not None and m['prevBar']['rvol'] is not None, 'normal fund: RVOL, OBV and prior-bar RVOL are present')
cl = m['candle']['closeLocation']; ok(cl is None or abs(cl * 100 - round(cl * 100)) > 1e-9 or cl in (0, 1), 'candle closeLocation is not rounded to 2 decimals')

# --- zero-volume fund
r, j = sr(frame(vol=0), at(11, 0)); m = j['meta']
ok(m['volume']['available'] is False and m['volume']['daysWithVolume'] == 0, 'zero volume on every completed day: unavailable')
ok(m['rvol'] is None and m['rvol_display'] is None and m['obv'] is None and m['prevBar']['rvol'] is None, 'zero-volume: RVOL, its display text, OBV and the prior-bar RVOL are all None')
# today's forming bar has volume but history is all zero: still unavailable (the SOXL.NE 50x case)
d = frame(vol=0); d.iloc[-1, d.columns.get_loc('volume')] = 1_827_022.0
r, j = sr(d, at(11, 0)); m = j['meta']
ok(m['volume']['available'] is False and m['rvol'] is None, 'a partial bar with volume over a zero history does NOT produce a 50x RVOL')

# --- the threshold: 40 vs 39 completed days with volume
r, j = sr(frame(vol_days=40), at(11, 0)); ok(j['meta']['volume']['available'] is True and j['meta']['volume']['daysWithVolume'] == 40, '40 of the last 50 completed days with volume: available')
r, j = sr(frame(vol_days=39), at(11, 0)); ok(j['meta']['volume']['available'] is False and j['meta']['rvol'] is None, '39 days: unavailable')
r, j = sr(frame(vol_days=1), at(11, 0)); ok(j['meta']['volume']['available'] is False, 'a single day with volume: unavailable (thin fund)')
d = frame(); d.iloc[-30:-1, d.columns.get_loc('volume')] = np.nan
r, j = sr(d, at(11, 0)); ok(j['meta']['volume']['available'] is False, 'NaN volume counts as missing')
# the day AFTER: the earlier forming bar is now stored with volume; completed history still thin -> still unavailable
d = frame(vol=0); d.iloc[-1, d.columns.get_loc('volume')] = 1_827_022.0
r, j = sr(d, at(16, 45)); ok(j['meta']['volume']['available'] is False, 'after the close with one stored volume day: still unavailable (no 50x tomorrow)')

# --- ADX and OBV on completed bars
df = frame()
r_mid, j_mid = sr(df, at(11, 0)); r_after, j_after = sr(df, at(16, 45))
done = df.iloc[:-1]
exp_mid = backend.calculate_adx(pd.Series(done['high'].values), pd.Series(done['low'].values), pd.Series(done['close'].values))['adx']
exp_after = backend.calculate_adx(pd.Series(df['high'].values), pd.Series(df['low'].values), pd.Series(df['close'].values))['adx']
ok(j_mid['meta']['adx']['adx'] == exp_mid, f'mid-session ADX = ADX on completed bars ({exp_mid})')
ok(j_after['meta']['adx']['adx'] == exp_after, f'after the close ADX includes today\'s final bar ({exp_after})')
ok(exp_mid != exp_after, 'the two differ, so the test can tell them apart')
obv_done = backend.calculate_obv(pd.Series(done['close'].values), pd.Series(done['volume'].values))
ok(j_mid['meta']['obv']['obv'] == obv_done['obv'], 'mid-session OBV is computed on completed bars')
ok(j_mid['currentPrice'] == round(float(df['close'].iloc[-1]), 2) or abs(j_mid['currentPrice'] - float(df['close'].iloc[-1])) < 0.01, 'currentPrice stays live (today\'s bar) on purpose')

# --- /api/stock 52-week high/low: from the bars, never Yahoo's number (Golden Rule 63)
df = frame(last='2026-11-16')
backend.get_data_provider = lambda: FakeDP(df, info={'shortName': 'Fake', 'fiftyTwoWeekHigh': 999.0, 'fiftyTwoWeekLow': 1.0})
undo = with_clock(at(9, 15))
try: js = client.get('/api/stock/FAKE').get_json()
finally: undo()
ok(abs(js['fiftyTwoWeekHigh'] - float(df['high'].tail(252).max())) < 1e-9 and abs(js['fiftyTwoWeekLow'] - float(df['low'].tail(252).min())) < 1e-9, '/api/stock 52-week high/low come from the 252 bars, not Yahoo\'s info (999 / 1)')
# ---- Day 127: /api/sr Buy when the last COMPLETED close is inside the nearest support zone
import sr_plan
def planted(zone_low, zone_high, inside_flag=True):
    z = [{'low': zone_low, 'high': zone_high, 'mid': (zone_low + zone_high) / 2, 'swings': 3, 'highs': 1, 'lows': 2, 'side': 'support', 'insideZone': inside_flag, 'nearest': True, 'lastSwingDate': 'x'}]
    return lambda hist, current_price=None, **k: {'support': [round(zone_high, 2)], 'resistance': [round(zone_high + 20, 2)], 'allSupport': [round(zone_high, 2)], 'allResistance': [round(zone_high + 20, 2)],
        'zones': z, 'atr': 1.0, 'high52w': 999.0, 'nearHigh52w': False, 'confirmedThrough': {'daily': 'x'}, 'currentPrice': round(float(current_price or 0), 2), 'barsUsed': 250, 'droppedFormingBar': False, 'nanRowsDropped': 0}
real_csr = backend.compute_simple_sr
try:
    d = frame()
    lc = round(float(d['close'].iloc[-1]), 2)          # after the close the last bar is completed
    backend.compute_simple_sr = planted(lc - 0.5, lc + 1.0)
    r, j = sr(d, at(16, 45)); m = j['meta']
    ok(r.status_code == 200 and j['suggestedEntry'] == lc and m['entryBasis'] == 'last_close_inside_zone', f'close inside the zone: suggestedEntry is the last close ({lc}), entryBasis says so')
    ok(j['suggestedStop'] == round(lc - 2.0, 2) and j['riskReward'] is not None, 'the stop is 2 ATR below that Buy and R:R follows')
    ok(j['suggestedEntry'] <= j['currentPrice'] + 1e-9, 'the Buy is not above the market (after the close the last close is the price)')
    backend.compute_simple_sr = planted(lc - 3.0, lc - 1.5, inside_flag=False)
    r, j = sr(d, at(16, 45)); m = j['meta']
    ok(j['suggestedEntry'] == round(lc - 1.5, 2) and m['entryBasis'] == 'zone_high', 'price above the zone: the Buy is the zone high, entryBasis zone_high (unchanged)')
    # mid-session: the forming bar is dropped, the Buy follows the last COMPLETED close, not the live bar
    lc2 = round(float(d['close'].iloc[-2]), 2)
    backend.compute_simple_sr = planted(lc2 - 0.05, lc2 + 0.05)
    r, j = sr(d, at(11, 0)); m = j['meta']
    ok(j['suggestedEntry'] == lc2 and m['entryBasis'] == 'last_close_inside_zone', 'mid-session: the Buy is the last COMPLETED close, not the live bar')
    # a NaN last completed close falls back to the zone high
    dn = frame(); dn.iloc[-1, dn.columns.get_loc('close')] = np.nan
    backend.compute_simple_sr = planted(lc - 0.5, lc + 1.0)
    r, j = sr(dn, at(16, 45))
    ok(r.status_code in (200, 400) and (r.status_code != 200 or j['meta']['entryBasis'] in ('zone_high', 'last_close_inside_zone')), 'a NaN close does not crash the route')
finally:
    backend.compute_simple_sr = real_csr

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
