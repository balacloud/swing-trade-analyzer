"""Tests for live_quote.py + market_time.session_for (Day 126). Mocked providers, fixed clocks.
Run: venv/bin/python test_live_quote.py"""
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd

import live_quote
import market_time
from providers.exceptions import ProviderUnavailableError, DataNotFoundError

ET = ZoneInfo('America/New_York')
passed = failed = 0


def check(name, cond, detail=''):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        print(f'FAIL {name} {detail}')


def et(y, m, d, h, mi):
    return datetime(y, m, d, h, mi, tzinfo=ET)


class Prov:
    def __init__(self, name, raw=None, exc=None):
        self.name, self.raw, self.exc, self.calls = name, raw, exc, 0

    def get_live_raw(self, t):
        self.calls += 1
        if self.exc:
            raise self.exc
        return self.raw


class DP:
    def __init__(self, tradier=None, yf=None, finnhub=None, bars=None, ohlcv_exc=None):
        self.tradier = tradier or Prov('tradier', exc=ProviderUnavailableError('tradier', 'down'))
        self.yfinance = yf or Prov('yfinance', exc=ProviderUnavailableError('yfinance_live', 'down'))
        self.finnhub = finnhub or Prov('finnhub', exc=ProviderUnavailableError('finnhub', 'down'))
        self._bars, self._exc = bars, ohlcv_exc

    def get_ohlcv(self, t, period='2y'):
        if self._exc:
            raise self._exc
        return self._bars


def bars(rows):
    return pd.DataFrame({'close': [c for _, c in rows]}, index=[d for d, _ in rows])


def raw(price, when, src='tradier'):
    return {'price': price, 'trade_time': when.astimezone(timezone.utc), 'source': src}


NOW = et(2026, 11, 16, 14, 55)   # Monday, mid-session
# Yahoo daily history holds today's forming bar mid-session (the bug the plan guards against)
NVDA_BARS = bars([('2026-11-12', 171.0), ('2026-11-13', 162.85), ('2026-11-16', 156.175)])

# ---- session_for -------------------------------------------------------------
sess = lambda h, m, now=NOW: market_time.session_for(et(2026, 11, 16, h, m), now=now.replace(hour=h, minute=m) if False else now)
n = lambda h, m: et(2026, 11, 16, h, m)
for (h, m, want) in [(3, 59, 'closed'), (4, 0, 'pre'), (9, 29, 'pre'), (9, 30, 'regular'), (15, 59, 'regular'),
                     (16, 0, 'post'), (19, 59, 'post'), (20, 0, 'closed')]:
    check(f'session {h}:{m:02d}', market_time.session_for(n(h, m), now=n(h, m)) == want,
          market_time.session_for(n(h, m), now=n(h, m)))
check('session weekend', market_time.session_for(et(2026, 11, 14, 11, 0), now=et(2026, 11, 14, 11, 5)) == 'closed')
check('session yesterday trade', market_time.session_for(et(2026, 11, 13, 15, 0), now=n(11, 0)) == 'closed')
check('session tz-aware UTC input', market_time.session_for(n(11, 0).astimezone(timezone.utc), now=n(11, 5)) == 'regular')

# ---- happy path: Tradier first, change from COMPLETED close (162.85, not 156.175) --
tr = Prov('tradier', raw(156.05, et(2026, 11, 16, 14, 51)))
yf_ = Prov('yfinance', raw(1.0, et(2026, 11, 16, 14, 54), 'yfinance'))
q = live_quote.build_live_quote('NVDA', DP(tradier=tr, yf=yf_, bars=NVDA_BARS), now=NOW)
check('available', q['available'] and q['source'] == 'tradier', q)
check('last_close ignores forming bar', q['last_close'] == {'price': 162.85, 'date': '2026-11-13'}, q['last_close'])
check('change vs completed close', abs(q['change'] - (156.05 - 162.85)) < 1e-6, q['change'])
check('change_pct -4.18', q['change_pct'] == -4.18, q['change_pct'])
check('age 4 min', abs(q['age_minutes'] - 4.0) < 0.01, q['age_minutes'])
check('session regular', q['session'] == 'regular')
check('yahoo not called when tradier works', yf_.calls == 0)
check('trade time ET iso', q['last_trade_at'].endswith('-05:00'), q['last_trade_at'])

# ---- fallthrough with logging ------------------------------------------------
yfp = Prov('yfinance', raw(156.2, et(2026, 11, 16, 14, 54), 'yfinance'))
q = live_quote.build_live_quote('NVDA', DP(yf=yfp, bars=NVDA_BARS), now=NOW)
check('tradier down -> yahoo', q['available'] and q['source'] == 'yfinance', q)
q = live_quote.build_live_quote('NVDA', DP(finnhub=Prov('finnhub', raw(156.3, et(2026, 11, 16, 14, 50), 'finnhub')), bars=NVDA_BARS), now=NOW)
check('tradier+yahoo down -> finnhub', q['available'] and q['source'] == 'finnhub', q)
q = live_quote.build_live_quote('NVDA', DP(bars=NVDA_BARS), now=NOW)
check('all down -> unavailable', q == {'available': False, 'reason': 'live price source unavailable', 'ticker': 'NVDA'}, q)

# ---- Canadian: Yahoo only ----------------------------------------------------
tr2 = Prov('tradier', raw(12.0, et(2026, 11, 16, 14, 50)))
fh2 = Prov('finnhub', raw(12.0, et(2026, 11, 16, 14, 50), 'finnhub'))
yc = Prov('yfinance', raw(12.8, et(2026, 11, 16, 14, 54), 'yfinance'))
cbars = bars([('2026-11-13', 14.69), ('2026-11-16', 12.7)])
q = live_quote.build_live_quote('SOXL.NE', DP(tradier=tr2, yf=yc, finnhub=fh2, bars=cbars), now=NOW)
check('canadian uses yahoo only', q['source'] == 'yfinance' and tr2.calls == 0 and fh2.calls == 0, q)
check('canadian change vs 14.69', q['last_close']['price'] == 14.69 and q['change_pct'] == round((12.8 - 14.69) / 14.69 * 100, 2), q)
for sfx in ('.TO', '.NE', '.V'):
    check(f'is_canadian {sfx}', live_quote.is_canadian('abc' + sfx))
check('US not canadian', not live_quote.is_canadian('NVDA'))
q = live_quote.build_live_quote('SOXL.NE', DP(tradier=tr2, bars=cbars), now=NOW)
check('canadian yahoo down -> unavailable (no US fallback)', not q['available'] and tr2.calls == 0, q)

# ---- staleness rule ----------------------------------------------------------
old = Prov('tradier', raw(150.0, et(2026, 11, 16, 14, 30)))        # 25 min old
q = live_quote.build_live_quote('THIN', DP(tradier=old, bars=NVDA_BARS), now=NOW)
check('25 min old regular trade -> no recent trades', q == {'available': False, 'reason': 'no recent trades', 'ticker': 'THIN'}, q)
ok15 = Prov('tradier', raw(150.0, et(2026, 11, 16, 14, 40)))       # 15 min old: delayed feed passes
q = live_quote.build_live_quote('NVDA', DP(tradier=ok15, bars=NVDA_BARS), now=NOW)
check('15 min delayed passes with real age', q['available'] and abs(q['age_minutes'] - 15) < 0.01, q)
b20 = Prov('tradier', raw(150.0, et(2026, 11, 16, 14, 35)))        # exactly 20
check('exactly 20 min passes', live_quote.build_live_quote('NVDA', DP(tradier=b20, bars=NVDA_BARS), now=NOW)['available'])
b21 = Prov('tradier', raw(150.0, et(2026, 11, 16, 14, 34)))        # 21
check('21 min fails', not live_quote.build_live_quote('NVDA', DP(tradier=b21, bars=NVDA_BARS), now=NOW)['available'])
# stale from tradier, fresh from yahoo -> yahoo wins
q = live_quote.build_live_quote('NVDA', DP(tradier=old, yf=yfp, bars=NVDA_BARS), now=NOW)
check('stale tradier, fresh yahoo -> yahoo', q['available'] and q['source'] == 'yfinance', q)

# ---- bad inputs rejected -----------------------------------------------------
for label, bad in [('zero', 0.0), ('negative', -3.0), ('nan', float('nan')), ('inf', float('inf')), ('None', None), ('string', '12')]:
    q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(bad, et(2026, 11, 16, 14, 54))), bars=NVDA_BARS), now=NOW)
    check(f'bad price {label} rejected', not q['available'], q)
naive = Prov('tradier', {'price': 150.0, 'trade_time': datetime(2026, 11, 16, 14, 54), 'source': 'tradier'})
check('naive trade time rejected', not live_quote.build_live_quote('NVDA', DP(tradier=naive, bars=NVDA_BARS), now=NOW)['available'])
none_t = Prov('tradier', {'price': 150.0, 'trade_time': None, 'source': 'tradier'})
check('missing trade time rejected', not live_quote.build_live_quote('NVDA', DP(tradier=none_t, bars=NVDA_BARS), now=NOW)['available'])
fut = Prov('tradier', raw(150.0, et(2026, 11, 16, 15, 30)))
check('future trade time rejected', not live_quote.build_live_quote('NVDA', DP(tradier=fut, bars=NVDA_BARS), now=NOW)['available'])
nf = Prov('tradier', exc=DataNotFoundError('tradier', 'unmatched', 'ZZZZ'))
allnf = DP(tradier=nf, yf=Prov('yfinance', exc=DataNotFoundError('yfinance_live', 'none')),
           finnhub=Prov('finnhub', exc=DataNotFoundError('finnhub', 'none')), bars=NVDA_BARS)
q = live_quote.build_live_quote('ZZZZ', allnf, now=NOW)
check('unknown everywhere -> own reason', q == {'available': False, 'reason': 'no live price for this ticker', 'ticker': 'ZZZZ'}, q)
check('unmatched at one source, others down -> source unavailable',
      live_quote.build_live_quote('ZZZZ', DP(tradier=nf, bars=NVDA_BARS), now=NOW)['reason'] == 'live price source unavailable')

# ---- sessions on live quotes -------------------------------------------------
pre_now = et(2026, 11, 16, 8, 10)
q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(160.0, et(2026, 11, 16, 7, 40))),
                                           bars=bars([('2026-11-13', 162.85)])), now=pre_now)
check('pre-market 30 min old trade still shown (no age limit)', q['available'] and q['session'] == 'pre', q)
check('pre-market change vs Friday close', q['last_close']['date'] == '2026-11-13' and q['change_pct'] == round((160 - 162.85) / 162.85 * 100, 2), q)
post_now = et(2026, 11, 16, 17, 45)
q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(158.0, et(2026, 11, 16, 17, 40))),
                                           bars=bars([('2026-11-13', 162.85), ('2026-11-16', 157.0)])), now=post_now)
check('after hours session', q['session'] == 'post' and q['last_close'] == {'price': 157.0, 'date': '2026-11-16'}, q)
check('after hours change from today close', q['change_pct'] == round((158 - 157) / 157 * 100, 2), q)
# 16:00-16:30 ET: the existing rule still treats today's bar as forming -> measure from the previous close
mid = et(2026, 11, 16, 16, 10)
q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(157.5, et(2026, 11, 16, 16, 8))), bars=NVDA_BARS), now=mid)
check('16:10 uses previous close until 16:30', q['last_close']['date'] == '2026-11-13' and q['session'] == 'post', q)
# weekend / holiday: last trade is an older date -> closed, no live price
sat = et(2026, 11, 14, 11, 0)
q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(162.85, et(2026, 11, 13, 16, 0))),
                                           bars=bars([('2026-11-13', 162.85)])), now=sat)
check('weekend -> closed, no live price', q['available'] and q['session'] == 'closed' and q['price'] is None and q['change_pct'] is None, q)
check('weekend keeps the close line', q['last_close'] == {'price': 162.85, 'date': '2026-11-13'}, q)
# holiday on a weekday: trade from the previous day
hol = et(2026, 11, 26, 11, 0)   # Thanksgiving
q = live_quote.build_live_quote('NVDA', DP(tradier=Prov('tradier', raw(170.0, et(2026, 11, 25, 16, 0))),
                                           bars=bars([('2026-11-25', 170.0)])), now=hol)
check('holiday -> closed', q['session'] == 'closed' and q['price'] is None, q)

# ---- last close problems -----------------------------------------------------
q = live_quote.build_live_quote('NVDA', DP(tradier=tr, ohlcv_exc=RuntimeError('boom')), now=NOW)
check('no daily bars -> price shown, no change', q['available'] and q['change'] is None and q['last_close'] is None, q)
q = live_quote.build_live_quote('NVDA', DP(tradier=tr, bars=bars([('2026-11-16', 156.1)])), now=NOW)
check('only forming bar -> no close, no change', q['last_close'] is None and q['change_pct'] is None, q)

# ---- cache -------------------------------------------------------------------
class FakeCache:
    def __init__(self):
        self.store, self.ttls = {}, []

    def get_cached_market(self, k):
        return self.store.get(k)

    def _set_cached_market_ttl(self, k, d, ttl_hours):
        self.store[k] = d
        self.ttls.append(ttl_hours)


c = FakeCache()
trc = Prov('tradier', raw(156.05, et(2026, 11, 16, 14, 51)))
dp = DP(tradier=trc, bars=NVDA_BARS)
a = live_quote.get_live_quote('nvda', dp, now=NOW, cache=c)
b = live_quote.get_live_quote('NVDA', dp, now=NOW + timedelta(seconds=30), cache=c)
check('cache hit within window: one provider call', trc.calls == 1, trc.calls)
check('cache TTL is 45 s', abs(c.ttls[0] - 45 / 3600) < 1e-9, c.ttls)
check('cached age recomputed', b['age_minutes'] > a['age_minutes'], (a['age_minutes'], b['age_minutes']))
c.store.clear()
live_quote.get_live_quote('NVDA', dp, now=NOW, cache=c)
check('cache miss refetches', trc.calls == 2)
class BadCache(FakeCache):
    def get_cached_market(self, k):
        raise RuntimeError('db locked')
check('cache read failure does not hide the price', live_quote.get_live_quote('NVDA', dp, now=NOW, cache=BadCache())['available'])

# ---- source of truth: the 16:30 rule is the one in market_time ---------------
check('forming-bar rule unchanged (16:29 forming)', market_time.is_forming_bar('2026-11-16', now=et(2026, 11, 16, 16, 29)))
check('forming-bar rule unchanged (16:30 done)', not market_time.is_forming_bar('2026-11-16', now=et(2026, 11, 16, 16, 30)))

print(f'{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
