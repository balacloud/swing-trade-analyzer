"""
Breakout Detection Engine for Swing Trade Analyzer (STA).

Day 125 rewrite: simple, widely agreed trader rules (O'Neil / Minervini / Darvas
conventions as repeated across trading education), NOT a tested edge. The user
chose not to backtest these ("it's a rabbit hole"); the Analyze card says
"Common trader rules, not tested." Plan + Fable review:
docs/claude/design/ANALYZE_CLEANUP_PLAN_DAY125.md §7.1.

Before Day 125 this module mirrored pine/sta_breakout_companion.pine (8 states,
RS/candle/ATR gates). It no longer does; the Pine file is kept as history.

It describes a state; it is never a buy signal (BREAKOUT_ENGINE_SPEC.md §15).

All rules run on COMPLETED daily bars (the caller drops today's forming bar via
prepare_breakout_frame). t = last completed bar.

- Pivot P      = highest high of bars t-69 .. t-10 (the 60-day ceiling that
                 stood before the last 10 days, so it never contains the
                 breakout bars and doesn't drift during the breakout).
- Breakout b   = first bar in t-9 .. t that closed above P.
- Volume V     = volume[b] / mean(volume of the 50 bars before b); None when
                 fewer than 40 of those 50 are known or the mean is 0.

States, in priority order:
  FAILED_BREAKOUT        b exists and close[t] < P
  EXTENDED_CHASE_RISK    b exists and close[t] more than 5% above P
  RETEST_ENTRY           b exists, t > b, low[t] within 1% above P, close[t] > P
  BREAKOUT_CONFIRMED     b exists, V >= 1.5, close[t] within P .. P+5%
  BREAKOUT_LIGHT_VOLUME  b exists, V < 1.5 or unknown, same band
  BREAKOUT_WATCH         no b and close[t] within 3% under P
  NOT_READY              otherwise
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any, Dict, Optional, Tuple

import pandas as pd

from market_time import drop_forming_bar

logger = logging.getLogger(__name__)

PIVOT_BARS = 60          # ceiling lookback
EPISODE_BARS = 10        # how long a breakout stays "recent"
VOLUME_BARS = 50         # average volume lookback (breakout day excluded)
MIN_VOLUME_BARS = 40     # known volumes needed out of VOLUME_BARS
RVOL_CONFIRM = 1.5       # 50% above average
MAX_EXTENSION_PCT = 5.0  # don't chase above this
RETEST_PCT = 1.0
WATCH_PCT = 3.0
MIN_BARS = 80            # PIVOT_BARS + EPISODE_BARS = 70, plus slack

OHLCV = ['open', 'high', 'low', 'close', 'volume']

HUMAN_ACTION = {
    'FAILED_BREAKOUT': 'Broke above the 60-day high, then closed back below it. The breakout failed.',
    'EXTENDED_CHASE_RISK': 'More than 5% above the 60-day high. Common rule: don\'t chase; wait for a pullback.',
    'RETEST_ENTRY': 'Came back down to the old 60-day high and closed above it. The retest is holding.',
    'BREAKOUT_CONFIRMED': 'Closed above the 60-day high on heavy volume (1.5x normal or more).',
    'BREAKOUT_LIGHT_VOLUME': 'Closed above the 60-day high on light volume. Not confirmed.',
    'BREAKOUT_WATCH': 'Within 3% under the 60-day high. Watch for a close above it on heavy volume.',
    'NOT_READY': 'More than 3% under the 60-day high.',
}


def prepare_breakout_frame(hist: pd.DataFrame, now=None) -> Tuple[pd.DataFrame, bool]:
    """Lowercase OHLCV columns, keep only OHLCV, drop today's forming bar.

    Returns (frame, dropped). Raises ValueError when a column is missing.
    """
    if hist is None or len(hist) == 0:
        raise ValueError('No OHLCV data provided')
    out = hist.copy()
    out.columns = [str(c).lower() for c in out.columns]
    missing = [c for c in OHLCV if c not in out.columns]
    if missing:
        raise ValueError(f'Missing OHLCV columns: {missing}')
    out = out[OHLCV]
    return drop_forming_bar(out, now=now)


def _pct(a: float, b: float) -> float:
    """Percent a is above b, rounded to 4 dp so exact boundaries (5.0, -3.0) compare cleanly."""
    return round((a - b) / b * 100.0, 4)


def _date(idx) -> str:
    return str(idx)[:10]


def detect_breakout(ohlcv: pd.DataFrame, ticker: Optional[str] = None) -> Dict[str, Any]:
    """Breakout state for a frame of COMPLETED daily bars (lowercase OHLCV)."""
    if ohlcv is None or len(ohlcv) == 0:
        raise ValueError('No OHLCV data provided')
    df = ohlcv.copy()
    df.columns = [str(c).lower() for c in df.columns]

    before = len(df)
    df = df.dropna(subset=['high', 'low', 'close'])
    if len(df) < before:
        logger.warning('breakout %s: dropped %d bars with missing price', ticker, before - len(df))
    if len(df) < MIN_BARS:
        raise ValueError(f'Need at least {MIN_BARS} bars, got {len(df)}')

    high, low, close, volume = df['high'], df['low'], df['close'], df['volume']
    n = len(df)
    t = n - 1

    pivot = float(high.iloc[t - (PIVOT_BARS + EPISODE_BARS) + 1: t - EPISODE_BARS + 1].max())
    c = float(close.iloc[t])

    b = None
    for i in range(t - EPISODE_BARS + 1, t + 1):
        if float(close.iloc[i]) > pivot:
            b = i
            break

    rvol = None
    if b is not None:
        prior = volume.iloc[max(0, b - VOLUME_BARS): b].dropna()
        vb = volume.iloc[b]
        if len(prior) >= MIN_VOLUME_BARS and pd.notna(vb) and prior.mean() > 0:
            rvol = round(float(vb) / float(prior.mean()), 2)

    pct = _pct(c, pivot)
    if b is not None:
        if c < pivot:
            status = 'FAILED_BREAKOUT'
        elif pct > MAX_EXTENSION_PCT:
            status = 'EXTENDED_CHASE_RISK'
        elif t > b and _pct(float(low.iloc[t]), pivot) <= RETEST_PCT and c > pivot:
            status = 'RETEST_ENTRY'
        elif rvol is not None and rvol >= RVOL_CONFIRM:
            status = 'BREAKOUT_CONFIRMED'
        else:
            status = 'BREAKOUT_LIGHT_VOLUME'
    elif pct >= -WATCH_PCT:
        status = 'BREAKOUT_WATCH'
    else:
        status = 'NOT_READY'

    action = HUMAN_ACTION[status]
    if status == 'BREAKOUT_LIGHT_VOLUME' and rvol is None:
        action = 'Closed above the 60-day high; volume unknown, so not confirmed.'

    return {
        'status': status,
        'humanAction': action,
        'asOfDate': _date(df.index[t]),
        'currentPrice': round(c, 2),
        'breakoutLevel': round(pivot, 2),
        'pctFromLevel': round(pct, 2),
        'breakoutDate': _date(df.index[b]) if b is not None else None,
        'breakoutAge': (t - b) if b is not None else None,
        'rvol': rvol,
        'timestamp': datetime.now().isoformat(),
    }
