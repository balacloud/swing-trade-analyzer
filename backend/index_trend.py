"""
Index trend facts for the Analyze page's Market backdrop card (Day 124, redesign Step 7).

Display only: nothing here feeds assessRiskMacro() or any verdict. Facts are computed on
completed daily bars (market_time.drop_forming_bar), because the OHLCV cache can hold a
morning partial bar until 16:30 ET and it would otherwise read as "now" all day.
No thresholds: the biggest drop is always reported, however small.
"""
import pandas as pd

from market_time import drop_forming_bar

DROP_WINDOW = 10  # sessions


def _pct(a, b):
    """One-day % change, rounded to 2 dp. Ties and the "since" search compare these
    rounded values on purpose: two drops within 0.01pp read as equal, as shown."""
    if pd.isna(a) or pd.isna(b) or b == 0:
        return None
    return round((a / b - 1) * 100, 2)


def index_trend_facts(hist, now=None):
    """Return the card's facts for one index from a daily OHLCV frame (needs 'Close'),
    or None when there is no usable data. Missing pieces are None, never a fake number."""
    if hist is None or len(hist) == 0 or 'Close' not in hist:
        return None
    hist, _ = drop_forming_bar(hist, now=now)
    raw = hist['Close'].astype(float)
    closes = raw.dropna()
    if len(closes) == 0:
        return None
    nan_closes = int(raw.isna().sum())
    if nan_closes:
        print(f"⚠️ index_trend_facts: {nan_closes} NaN close(s); one-day changes across them are skipped")

    close = float(closes.iloc[-1])
    sma50 = float(closes.iloc[-50:].mean()) if len(closes) >= 50 else None
    sma200 = float(closes.iloc[-200:].mean()) if len(closes) >= 200 else None

    facts = {
        'asOfDate': str(closes.index[-1])[:10],
        'close': round(close, 2),
        'sma50': round(sma50, 2) if sma50 is not None else None,
        'aboveSma50': (close > sma50) if sma50 is not None else None,
        'pctVsSma50': round((close / sma50 - 1) * 100, 1) if sma50 is not None else None,
        'sma200': round(sma200, 2) if sma200 is not None else None,
        'aboveSma200': (close > sma200) if sma200 is not None else None,
        'pctVsSma200': round((close / sma200 - 1) * 100, 1) if sma200 is not None else None,
        'biggestDrop10d': None,
        'biggestDrop10dSince': None,
        'searchedFrom': None,
        'nanCloses': nan_closes,
    }

    if len(raw) < DROP_WINDOW + 1:
        return facts

    # Changes on the un-dropped series, so a NaN close never merges two sessions
    # into one fake "1-day" move (Fable code review, Day 124).
    changes = [_pct(raw.iloc[i], raw.iloc[i - 1]) for i in range(1, len(raw))]
    dates = [str(d)[:10] for d in raw.index[1:]]
    facts['searchedFrom'] = dates[0]  # the span the "since" search really covers
    window_start = len(changes) - DROP_WINDOW

    worst = None
    for i in range(window_start, len(changes)):
        if changes[i] is None:
            continue
        if worst is None or changes[i] <= changes[worst]:  # <= : the most recent of equal drops wins
            worst = i
    if worst is None:
        return facts  # no known one-day change in the window
    if changes[worst] >= 0:
        facts['biggestDrop10d'] = {'noDownDay': True}
        return facts

    facts['biggestDrop10d'] = {'date': dates[worst], 'pct': changes[worst]}
    for i in range(worst - 1, -1, -1):  # strictly before, over the whole frame
        if changes[i] is not None and changes[i] <= changes[worst]:
            facts['biggestDrop10dSince'] = dates[i]
            break
    return facts
