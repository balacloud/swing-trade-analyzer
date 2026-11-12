"""
Market-time helpers (Day 123).

One definition of "is the last daily bar today's still-forming bar?" for the
live Flask routes. Same rule as paper_trading/live_signals._prepare_ohlcv
(Day 99), which is left untouched because that program is discontinued and
frozen.

Cutoff is 16:30 ET, not the bell: cache_manager.calculate_ohlcv_expiry()
keeps an intraday-fetched OHLCV frame until the close + 30 minutes, so
between 16:00 and 16:30 a cached frame can still hold a partial bar. Treating
today's bar as forming until 16:30 keeps that partial bar out (Fable review,
Day 123). Early-close days are treated as forming until 16:30 too, a known,
accepted limitation.
"""
from datetime import datetime
from zoneinfo import ZoneInfo

MARKET_TZ = ZoneInfo('America/New_York')
MARKET_CLOSE_HOUR, MARKET_CLOSE_MIN = 16, 30  # see docstring: matches the OHLCV cache expiry


def is_forming_bar(last_bar_date, now=None):
    """True when `last_bar_date` (YYYY-MM-DD) is today in New York and the
    session hasn't closed yet. `now` is injectable for tests."""
    now_et = now or datetime.now(MARKET_TZ)
    return (str(last_bar_date)[:10] == now_et.strftime('%Y-%m-%d')
            and (now_et.hour, now_et.minute) < (MARKET_CLOSE_HOUR, MARKET_CLOSE_MIN))


def drop_forming_bar(df, now=None):
    """Return (df without today's forming bar, dropped: bool). Never mutates df."""
    if df is None or len(df) == 0:
        return df, False
    if is_forming_bar(str(df.index[-1])[:10], now=now):
        return df.iloc[:-1], True
    return df, False
