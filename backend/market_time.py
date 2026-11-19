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


# --- Day 127: bars with no close price ------------------------------------
# Yahoo sometimes returns a row with open/high/low/close all empty but a normal-looking volume (15 cached
# tickers on Nov 18). Left in, `df['close'].iloc[-1]` is NaN and /api/sr answers with invalid JSON. Plan:
# docs/claude/design/EMPTY_PRICE_ROW_PLAN_DAY127.md. The CACHE stays raw (the audit and the Data Sources tab
# must be able to SEE the empty row); the rows are dropped when a frame is SERVED (orchestrator._deliver and
# split_adjust.fix_frame, which together cover every route and every direct-Yahoo fallback).
def _close_column(df):
    return next((c for c in df.columns if str(c).lower() == 'close'), None)


def newest_close_missing(df):
    """True when the newest row has no close price. Never raises."""
    try:
        if df is None or len(df) == 0:
            return False
        col = _close_column(df)
        return col is not None and bool(df[col].isna().iloc[-1])
    except Exception:  # noqa: BLE001 - a helper for logging/expiry must never break a request
        return False


def drop_empty_close(df, ticker=''):
    """Return `df` without rows whose close is empty (NaN), with one log line naming the dates. Never mutates
    `df`, never raises (on any problem the frame comes back unchanged). Works with any column case."""
    try:
        if df is None or len(df) == 0:
            return df
        col = _close_column(df)
        if col is None:
            return df
        bad = df[col].isna().to_numpy()          # by POSITION: a duplicated date index must not misalign the filter
        if not bool(bad.any()):
            return df
        dates = [str(d)[:10] for d in df.index[bad]]
        shown = dates[:5] + (['...'] if len(dates) > 5 else [])
        print(f"⚠️ {ticker or '?'}: dropped {len(dates)} bar(s) with no close price: {shown}")
        return df.iloc[~bad]
    except Exception as exc:  # noqa: BLE001
        print(f"⚠️ {ticker or '?'}: could not check for empty price rows: {exc}")
        return df


# --- Day 126: session of a quote, from the quote's OWN trade time ----------
# No exchange calendar exists in STA, so none is invented. A trade that is not
# from today (New York date) or is outside the usual extended hours means the
# market is "closed" - weekends and holidays fall out of this without a table.
# Known limit (documented): on an early-close day the session reads "regular"
# until the last trade is older than the staleness limit in live_quote.py.
PRE_OPEN = (4, 0)
REG_OPEN = (9, 30)
REG_CLOSE = (16, 0)
POST_CLOSE = (20, 0)


def session_for(trade_time, now=None):
    """'pre' | 'regular' | 'post' | 'closed' for a tz-aware trade time.
    Toronto listings trade on the same clock, so one rule serves both."""
    now_et = (now or datetime.now(MARKET_TZ)).astimezone(MARKET_TZ)
    t = trade_time.astimezone(MARKET_TZ)
    if t.date() != now_et.date() or now_et.weekday() >= 5:
        return 'closed'
    hm = (t.hour, t.minute)
    if PRE_OPEN <= hm < REG_OPEN:
        return 'pre'
    if REG_OPEN <= hm < REG_CLOSE:
        return 'regular'
    if REG_CLOSE <= hm < POST_CLOSE:
        return 'post'
    return 'closed'
