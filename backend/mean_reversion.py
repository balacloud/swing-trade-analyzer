"""
Mean-Reversion Engine — Connors RSI(2) Approach

Entry: RSI(2) < 10 AND Price > 200 SMA
Exit: RSI(2) > 70 OR time-based (max 10 days)
Stop: 3-5% below entry (tighter than momentum stops)

Only active when: ADX < 20 (range-bound) or as secondary signal alongside momentum

Source: Larry Connors "Short Term Trading Strategies That Work" (2009)
Validated by: 4-LLM audit (PLAUSIBLE 3/4, MISLEADING on RSI(14) vs RSI(2))

Tier 3A (Day 69): NEW file — zero impact on existing code.
"""

import pandas as pd
import numpy as np


def calculate_rsi_short(closes, period=2):
    """RSI with very short period (Connors approach).

    IMPORTANT (self-review round 4): Uses Wilder's EMA (ewm), NOT SMA (rolling).
    Both backend.py:247 and backtest_holistic.py:105 use ewm(alpha=1/period).
    For RSI(2): alpha = 1/2 = 0.5. Using SMA would give different values.
    """
    if len(closes) < period + 1:
        return pd.Series(dtype=float)

    delta = closes.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_atr(high, low, close, period=14):
    """Calculate Average True Range (same logic as pattern_detection.py)."""
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()


def calculate_adx(high, low, close, period=14):
    """Calculate Average Directional Index for range-bound detection."""
    if len(close) < period * 2:
        return None

    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.ewm(alpha=1/period, min_periods=period).mean()
    plus_di = 100 * (plus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)
    minus_di = 100 * (minus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)

    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(alpha=1/period, min_periods=period).mean()
    return adx


def detect_mr_signal(df):
    """
    Detect mean-reversion entry signal.

    Conditions:
    1. RSI(2) < 10 (oversold on short timeframe)
    2. Price > 200 SMA (long-term uptrend intact — don't catch falling knives)
    3. Price > $5 (liquidity filter)
    4. Volume > 500K avg (tradeable)

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV DataFrame with columns: Close, High, Low, Volume (capitalized)

    Returns
    -------
    dict
        Signal details including entry, stop, target, conditions
    """
    if df is None or len(df) < 200:
        return {'signal': False, 'reason': 'Insufficient data (need 200+ bars)'}

    close = df['Close']
    high = df['High']
    low = df['Low']

    rsi2_series = calculate_rsi_short(close, period=2)
    if rsi2_series.empty:
        return {'signal': False, 'reason': 'RSI(2) calculation failed'}

    rsi2 = float(rsi2_series.iloc[-1])
    sma200 = float(close.rolling(200).mean().iloc[-1])
    current_price = float(close.iloc[-1])
    avg_volume = float(df['Volume'].rolling(20).mean().iloc[-1])

    # ADX for range-bound context
    adx_series = calculate_adx(high, low, close)
    adx_value = float(adx_series.iloc[-1]) if adx_series is not None else None

    conditions = {
        'rsi2_oversold': rsi2 < 10,
        'above_200sma': current_price > sma200,
        'price_filter': current_price > 5,
        'volume_filter': avg_volume > 500000,
    }

    signal = all(conditions.values())

    # MR-specific risk params (tighter than momentum)
    atr_series = calculate_atr(high, low, close)
    atr_val = float(atr_series.iloc[-1]) if not atr_series.empty else current_price * 0.02

    # Stop: 5% max or 1.5x ATR, whichever is tighter (higher price)
    stop = max(current_price * 0.95, current_price - (atr_val * 1.5))

    # Target: slightly above 200 SMA (the "mean" to revert to)
    # If price is already above SMA (it should be), target = entry + 2x ATR
    if current_price > sma200:
        target = current_price + (atr_val * 2)
    else:
        target = sma200 * 1.02

    return {
        'signal': signal,
        'strategy': 'mean_reversion',
        'rsi2': round(rsi2, 2),
        'sma200': round(sma200, 2),
        'current_price': round(current_price, 2),
        'adx': round(adx_value, 2) if adx_value is not None else None,
        'range_bound': adx_value is not None and adx_value < 20,
        'avg_volume': int(avg_volume),
        'conditions': conditions,
        'stop': round(stop, 2),
        'target': round(target, 2),
        'atr': round(atr_val, 2),
        'max_hold_days': 10,
        'exit_rule': 'RSI(2) > 70 OR 10 days max',
    }


def scan_universe_for_mr(tickers, fetch_data_fn):
    """
    Scan a list of tickers for MR signals.

    Parameters
    ----------
    tickers : list of str
        Ticker symbols to scan
    fetch_data_fn : callable
        Function that takes (ticker, period) and returns a DataFrame with OHLCV data.
        Should return None on failure.

    Returns
    -------
    list of dict
        List of signal dicts for tickers with active MR signals
    """
    signals = []
    for ticker in tickers:
        try:
            df = fetch_data_fn(ticker, '1y')
            if df is None or df.empty:
                continue
            result = detect_mr_signal(df)
            if result.get('signal'):
                result['ticker'] = ticker
                signals.append(result)
        except Exception as e:
            print(f"MR scan error for {ticker}: {e}")
            continue

    # Sort by RSI(2) ascending (most oversold first)
    signals.sort(key=lambda x: x.get('rsi2', 100))
    return signals
