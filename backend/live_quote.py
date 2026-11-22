"""
live_quote.py - display-only live price for the Analyze header (Day 126).

Plan: docs/claude/design/LIVE_QUOTE_PLAN_DAY126.md (v2, Opus-reviewed).

Rules
  * Display only. Indicators, verdicts, stops and backtests stay on completed
    daily bars and never see this price.
  * Source order: US tickers Tradier -> Yahoo 1-minute -> Finnhub; Canadian
    tickers (.TO .NE .V) Yahoo 1-minute only (the only Canadian source).
    Every miss is printed with ticker, provider and reason.
  * One staleness rule: in the regular session a trade older than
    MAX_TRADE_AGE_MIN is treated as a miss (try the next source); if nothing
    fresher exists the answer is available=False "no recent trades". Newer
    trades are shown with their real age, so 15-minute-delayed feeds pass and
    are labelled honestly. Pre/post-market has no age limit (thin by nature).
  * Session comes from the trade's own time (market_time.session_for); a
    trade that is not from today means "closed" and no live price is shown.
  * `last_close` = last COMPLETED daily bar (market_time.drop_forming_bar);
    change / change_pct are computed here once, for every source. Provider
    prevclose values are ignored.
  * Never a guessed price: failure returns {'available': False, 'reason': ...}.
"""
import math
from datetime import datetime

import market_time
from providers.exceptions import DataNotFoundError

MAX_TRADE_AGE_MIN = 20       # regular session: older than this = "no recent trades"
LIVE_LABEL_MAX_MIN = 2       # at or under this reads "Live"
FUTURE_SKEW_MIN = 2          # a trade stamped further ahead than this is a bad clock
from providers.coverage import CANADIAN_SUFFIXES   # Day 129: one copy of the Canada rule (adds .NEO, .CN)
CACHE_TTL_HOURS = 45 / 3600.0   # 45 seconds


def is_canadian(ticker):
    return ticker.upper().endswith(CANADIAN_SUFFIXES)


def _unavailable(reason, ticker=None):
    out = {'available': False, 'reason': reason}
    if ticker:
        out['ticker'] = ticker
    return out


def _good_price(p):
    return isinstance(p, (int, float)) and math.isfinite(p) and p > 0


def _last_close(dp, ticker, now):
    """(price, 'YYYY-MM-DD') of the last completed daily bar, or (None, None)."""
    try:
        df = dp.get_ohlcv(ticker, '2y')
    except Exception as e:  # noqa: BLE001 - any provider failure means "no close", logged
        print(f"⚠️ live quote {ticker}: no daily bars for last close ({e})")
        return None, None
    if df is None or len(df) == 0:
        return None, None
    df, _ = market_time.drop_forming_bar(df, now=now)
    if df is None or len(df) == 0:
        return None, None
    col = 'close' if 'close' in df.columns else 'Close'
    price = df[col].iloc[-1]
    if not _good_price(float(price)):
        return None, None
    return float(price), str(df.index[-1])[:10]


def _chain(dp, ticker):
    if is_canadian(ticker):
        return [('yfinance', dp.yfinance)]
    return [('tradier', dp.tradier), ('yfinance', dp.yfinance), ('finnhub', dp.finnhub)]


def build_live_quote(ticker, dp, now=None):
    """Fetch and judge one live quote. `now` (tz-aware) is injectable for tests."""
    ticker = ticker.upper()
    now_et = (now or datetime.now(market_time.MARKET_TZ)).astimezone(market_time.MARKET_TZ)
    misses = []
    not_found = 0      # sources that answered "I don't know this ticker"
    chosen = None
    for name, prov in _chain(dp, ticker):
        try:
            raw = prov.get_live_raw(ticker)
        except Exception as e:  # noqa: BLE001 - ProviderError or anything else: log, next source
            reason = f'{type(e).__name__}: {e}'
            print(f"⚠️ live quote {ticker}: {name} failed - {reason}")
            misses.append(f'{name}: {reason}')
            if isinstance(e, DataNotFoundError):
                not_found += 1
            continue
        price, tt = raw.get('price'), raw.get('trade_time')
        if not _good_price(price):
            print(f"⚠️ live quote {ticker}: {name} gave a bad price {price!r}")
            misses.append(f'{name}: bad price')
            continue
        if tt is None or getattr(tt, 'tzinfo', None) is None:
            print(f"⚠️ live quote {ticker}: {name} gave no usable trade time")
            misses.append(f'{name}: no trade time')
            continue
        age_min = (now_et - tt.astimezone(market_time.MARKET_TZ)).total_seconds() / 60.0
        if age_min < -FUTURE_SKEW_MIN:
            print(f"⚠️ live quote {ticker}: {name} trade time is {-age_min:.0f} min in the future")
            misses.append(f'{name}: trade time in the future')
            continue
        session = market_time.session_for(tt, now=now_et)
        if session == 'regular' and age_min > MAX_TRADE_AGE_MIN:
            print(f"⚠️ live quote {ticker}: {name} last trade {age_min:.0f} min old")
            misses.append(f'{name}: last trade {age_min:.0f} min old')
            continue
        chosen = (name, raw['source'], float(price), tt, max(age_min, 0.0), session)
        break

    if chosen is None:
        # Nothing fresh. If a source answered with a stale regular-session trade
        # the honest reason is "no recent trades"; otherwise the sources are down.
        stale = any('min old' in m for m in misses)
        if not stale and not_found == len(misses) and misses:
            return _unavailable('no live price for this ticker', ticker)
        return _unavailable('no recent trades' if stale else 'live price source unavailable', ticker)

    _, source, price, tt, age_min, session = chosen
    lc_price, lc_date = _last_close(dp, ticker, now_et)
    # Day 126: 2 dp like /api/stock's bars, so the header and the cards show the same cent (SMCI 25.025 read $25.02 vs $25.03)
    last_close = {'price': round(lc_price, 2), 'date': lc_date} if lc_price is not None else None

    if session == 'closed':
        # Weekend, holiday or overnight: no live price, the close line speaks.
        return {'available': True, 'ticker': ticker, 'session': 'closed', 'price': None,
                'last_trade_at': tt.astimezone(market_time.MARKET_TZ).isoformat(),
                'age_minutes': round(age_min, 1), 'change': None, 'change_pct': None,
                'last_close': last_close, 'source': source}

    change = change_pct = None
    if lc_price is not None:
        change = round(price - lc_price, 4)
        change_pct = round(change / lc_price * 100.0, 2)
    return {'available': True, 'ticker': ticker, 'session': session, 'price': round(price, 4),
            'last_trade_at': tt.astimezone(market_time.MARKET_TZ).isoformat(),
            'age_minutes': round(age_min, 1), 'change': change, 'change_pct': change_pct,
            'last_close': last_close, 'source': source}


def get_live_quote(ticker, dp, now=None, cache=None):
    """build_live_quote behind a 45-second per-ticker cache. `cache` is the
    cache_manager module (injectable); `now` is for tests."""
    ticker = ticker.upper()
    key = f'LIVEQUOTE_{ticker}'
    if cache is not None:
        try:
            hit = cache.get_cached_market(key)
        except Exception as e:  # noqa: BLE001 - a cache problem must not hide a price
            print(f"⚠️ live quote {ticker}: cache read failed ({e})")
            hit = None
        if hit:
            if hit.get('available') and hit.get('last_trade_at'):
                now_et = (now or datetime.now(market_time.MARKET_TZ)).astimezone(market_time.MARKET_TZ)
                tt = datetime.fromisoformat(hit['last_trade_at'])
                hit = dict(hit, age_minutes=round(max((now_et - tt).total_seconds() / 60.0, 0.0), 1))
            return hit
    out = build_live_quote(ticker, dp, now=now)
    if cache is not None:
        try:
            cache._set_cached_market_ttl(key, out, ttl_hours=CACHE_TTL_HOURS)
        except Exception as e:  # noqa: BLE001
            print(f"⚠️ live quote {ticker}: cache write failed ({e})")
    return out
