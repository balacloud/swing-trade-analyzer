"""
Trade Simulator — v4.16 Holistic Backtest

Three exit models per holding period:
  Quick (1-5 days):    Fixed 7% target / 5% stop / max 5 days
  Standard (5-15 days): Structural stop (swing low - 2×ATR) / 8% target / max 15 days
                        + 10 EMA trailing stop (activates day 5 when gain >= 3%)
                        + Breakeven stop (ratchets up when gain >= 5%)
  Position (15-45 days): Trailing 21 EMA stop (activates day 5) / 15% target / max 45 days

Also provides market regime classification and helper functions.
Reuses ATR/swing low logic from backtest_technical.py.
"""

import pandas as pd
import numpy as np


# ─── ATR & Swing Low (rewritten here to avoid circular imports) ─────────────

def calculate_atr_series(high, low, close, period=14):
    """
    Calculate ATR as a Series (Wilder's smoothing).
    Returns full Series aligned to input index.
    """
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1 / period, min_periods=period).mean()
    return atr


def calculate_atr_at(high, low, close, period=14):
    """Calculate ATR at the last bar of the input series."""
    atr_series = calculate_atr_series(high, low, close, period)
    if atr_series.empty or atr_series.isna().all():
        return None
    return atr_series.iloc[-1]


def find_swing_low(df, lookback=20, date_idx=None):
    """
    Find the most recent swing low before date_idx.
    Swing low = bar where low < 2 bars on each side.
    """
    if date_idx is None:
        date_idx = len(df) - 1

    start_idx = max(0, date_idx - lookback)
    lows = df['Low'].iloc[start_idx:date_idx]

    if len(lows) < 5:
        return None

    swing_lows = []
    for i in range(2, len(lows) - 2):
        if (lows.iloc[i] < lows.iloc[i - 1] and
                lows.iloc[i] < lows.iloc[i - 2] and
                lows.iloc[i] < lows.iloc[i + 1] and
                lows.iloc[i] < lows.iloc[i + 2]):
            swing_lows.append(lows.iloc[i])

    return swing_lows[-1] if swing_lows else lows.min()


# ─── Market Regime Classification ────────────────────────────────────────────

def classify_market_regime(spy_df, vix_value, date_idx):
    """
    Classify market regime at a specific date.

    Bull:     SPY > 200 SMA AND 50 SMA rising
    Bear:     SPY < 200 SMA
    Sideways: SPY > 200 SMA AND 50 SMA flat (±1%)
    Crisis:   VIX > 35 (overrides above)

    Args:
        spy_df: SPY DataFrame with Close column
        vix_value: VIX value at the date (float or None)
        date_idx: integer index into spy_df

    Returns:
        str: 'bull', 'bear', 'sideways', or 'crisis'
    """
    # Crisis check first
    if vix_value is not None and vix_value > 35:
        return 'crisis'

    if date_idx < 200:
        return 'unknown'

    close = spy_df['Close'].iloc[:date_idx + 1]

    sma200 = close.iloc[-200:].mean()
    current_price = close.iloc[-1]

    if current_price < sma200:
        return 'bear'

    # SPY above 200 SMA — check 50 SMA slope
    sma50_now = close.iloc[-50:].mean()
    sma50_20d_ago = close.iloc[-70:-20].mean() if date_idx >= 70 else sma50_now

    if sma50_20d_ago != 0:
        sma50_change = (sma50_now - sma50_20d_ago) / sma50_20d_ago * 100
    else:
        sma50_change = 0

    if sma50_change > 1.0:
        return 'bull'
    elif sma50_change < -1.0:
        return 'bear'  # falling 50 SMA even above 200 — early bear
    else:
        return 'sideways'


def is_spy_above_200sma(spy_df, date_idx):
    """Simple check: is SPY above its 200-day SMA at date_idx?"""
    if date_idx < 200:
        return True  # Not enough data, assume bull

    close = spy_df['Close'].iloc[:date_idx + 1]
    sma200 = close.iloc[-200:].mean()
    return close.iloc[-1] > sma200


def is_spy_50sma_declining(spy_df, date_idx):
    """
    Day 56: Check if SPY 50 SMA is declining (leading bear indicator).
    Compares current 50 SMA vs 50 SMA from 20 days ago.
    Returns True if decline > 1% (same threshold as classify_market_regime).
    """
    if date_idx < 70:
        return False  # Not enough data

    close = spy_df['Close'].iloc[:date_idx + 1]
    sma50_now = close.iloc[-50:].mean()
    sma50_20d_ago = close.iloc[-70:-20].mean()

    if sma50_20d_ago == 0:
        return False

    sma50_change = (sma50_now - sma50_20d_ago) / sma50_20d_ago * 100
    return sma50_change < -1.0


# ─── Trade Simulation ────────────────────────────────────────────────────────

def simulate_trade(stock_df, entry_idx, holding_period,
                   entry_price=None, stop_price=None, target_price=None):
    """
    Simulate a trade with exit strategy based on holding period.

    Quick (1-5 days):
      Fixed target: +7% | Fixed stop: -5% | Max hold: 5 days

    Standard (5-15 days):
      Structural stop (swing low - 2×ATR) | Target +8% | Max hold: 15 days
      + 10 EMA trailing stop (day 5+, gain >= 3%) | Breakeven stop (gain >= 5%)

    Position (15-45 days):
      Trailing 21 EMA stop (activates after day 5) | Target +15% | Max hold: 45 days

    Args:
        stock_df: DataFrame with OHLCV
        entry_idx: index of entry bar
        holding_period: 'quick', 'standard', or 'position'
        entry_price: override entry price (default: close at entry_idx)
        stop_price: override stop price (default: computed from holding_period)
        target_price: override target price (default: computed from holding_period)

    Returns:
        dict with result, exit_price, exit_date, days_held, return_pct,
             return_r, exit_reason, max_favorable_excursion, max_adverse_excursion
    """
    if entry_price is None:
        entry_price = stock_df['Close'].iloc[entry_idx]

    # Compute ATR for structural calculations
    lookback_start = max(0, entry_idx - 50)
    atr = calculate_atr_at(
        stock_df['High'].iloc[lookback_start:entry_idx + 1],
        stock_df['Low'].iloc[lookback_start:entry_idx + 1],
        stock_df['Close'].iloc[lookback_start:entry_idx + 1],
    )

    # Set defaults per holding period
    if holding_period == 'quick':
        max_hold = 5
        if target_price is None:
            target_price = entry_price * 1.07  # +7%
        if stop_price is None:
            stop_price = entry_price * 0.95    # -5%

    elif holding_period == 'position':
        max_hold = 45
        if target_price is None:
            target_price = entry_price * 1.15  # +15%
        if stop_price is None:
            # Structural stop: swing low - 2×ATR
            swing_low = find_swing_low(stock_df, lookback=20, date_idx=entry_idx)
            if swing_low is not None and atr is not None:
                stop_price = swing_low - (atr * 2)
                # Clamp: min 3%, max 12%
                stop_price = max(stop_price, entry_price * 0.88)
                stop_price = min(stop_price, entry_price * 0.97)
            else:
                stop_price = entry_price * 0.92  # Fallback -8%

    else:  # standard
        max_hold = 15
        if target_price is None:
            target_price = entry_price * 1.08  # +8% (lowered from 10%, data shows 0 MFE >= 10%)
        if stop_price is None:
            # Structural stop: swing low - 2×ATR
            swing_low = find_swing_low(stock_df, lookback=20, date_idx=entry_idx)
            if swing_low is not None and atr is not None:
                stop_price = swing_low - (atr * 2)
                # Clamp: min 3%, max 10%
                stop_price = max(stop_price, entry_price * 0.90)
                stop_price = min(stop_price, entry_price * 0.97)
            else:
                stop_price = entry_price * 0.93  # Fallback -7%

    # Initial risk for R-multiple calculation
    initial_risk = entry_price - stop_price
    if initial_risk <= 0:
        initial_risk = entry_price * 0.05  # Fallback 5%

    # Tracking excursions
    max_favorable = 0  # Max favorable excursion (MFE)
    max_adverse = 0    # Max adverse excursion (MAE)

    # Trailing EMA stops
    # Position: 21 EMA trail (activates day 5, exits after 2 closes below)
    # Standard: 10 EMA trail (activates day 5 when gain >= 3%)
    ema_trail_series = None
    if holding_period == 'position':
        ema_trail_series = stock_df['Close'].ewm(span=21, adjust=False).mean()
    elif holding_period == 'standard':
        ema_trail_series = stock_df['Close'].ewm(span=10, adjust=False).mean()
    consecutive_below_ema = 0

    # Simulate day by day
    for day in range(1, max_hold + 1):
        check_idx = entry_idx + day

        if check_idx >= len(stock_df):
            # Ran out of data
            exit_price = stock_df['Close'].iloc[-1]
            return _build_result(
                entry_price, exit_price, initial_risk, day - 1,
                stock_df.index[entry_idx], stock_df.index[-1],
                'data_end', max_favorable, max_adverse
            )

        high_day = stock_df['High'].iloc[check_idx]
        low_day = stock_df['Low'].iloc[check_idx]
        close_day = stock_df['Close'].iloc[check_idx]

        # Track excursions
        favorable = (high_day - entry_price) / entry_price * 100
        adverse = (entry_price - low_day) / entry_price * 100
        max_favorable = max(max_favorable, favorable)
        max_adverse = max(max_adverse, adverse)

        # Check STOP LOSS first (conservative: assume stop hit if low touches)
        if low_day <= stop_price:
            return _build_result(
                entry_price, stop_price, initial_risk, day,
                stock_df.index[entry_idx], stock_df.index[check_idx],
                'stop_hit', max_favorable, max_adverse
            )

        # Check TARGET
        if high_day >= target_price:
            return _build_result(
                entry_price, target_price, initial_risk, day,
                stock_df.index[entry_idx], stock_df.index[check_idx],
                'target_hit', max_favorable, max_adverse
            )

        # Standard: trailing 10 EMA stop (activates day 5 when gain >= 3%)
        # Also: breakeven stop when gain >= 5%
        if holding_period == 'standard' and day >= 5 and ema_trail_series is not None:
            unrealized_gain_pct = (close_day - entry_price) / entry_price * 100

            # Breakeven stop: once gain hits 5%, never let it become a loss
            if unrealized_gain_pct >= 5.0:
                stop_price = max(stop_price, entry_price)  # Ratchet up only

            # 10 EMA trail: activate when gain >= 3%
            if unrealized_gain_pct >= 3.0 or max_favorable >= 5.0:
                ema10_val = ema_trail_series.iloc[check_idx]
                if close_day < ema10_val:
                    consecutive_below_ema += 1
                    if consecutive_below_ema >= 2:
                        return _build_result(
                            entry_price, close_day, initial_risk, day,
                            stock_df.index[entry_idx], stock_df.index[check_idx],
                            'trailing_ema_exit', max_favorable, max_adverse
                        )
                else:
                    consecutive_below_ema = 0

        # Position: trailing 21 EMA stop (activates after day 5)
        if holding_period == 'position' and day >= 5 and ema_trail_series is not None:
            ema21_val = ema_trail_series.iloc[check_idx]
            if close_day < ema21_val:
                consecutive_below_ema += 1
                if consecutive_below_ema >= 2:
                    return _build_result(
                        entry_price, close_day, initial_risk, day,
                        stock_df.index[entry_idx], stock_df.index[check_idx],
                        'trailing_ema_exit', max_favorable, max_adverse
                    )
            else:
                consecutive_below_ema = 0

    # Max hold reached — exit at close
    exit_idx = min(entry_idx + max_hold, len(stock_df) - 1)
    exit_price = stock_df['Close'].iloc[exit_idx]
    return _build_result(
        entry_price, exit_price, initial_risk, max_hold,
        stock_df.index[entry_idx],
        stock_df.index[exit_idx],
        'max_hold', max_favorable, max_adverse
    )


def _build_result(entry_price, exit_price, initial_risk, days_held,
                  entry_date, exit_date, exit_reason,
                  max_favorable, max_adverse):
    """Build standardized trade result dict."""
    return_pct = (exit_price - entry_price) / entry_price * 100
    return_r = (exit_price - entry_price) / initial_risk if initial_risk > 0 else 0

    if return_pct > 0.5:
        result = 'win'
    elif return_pct < -0.5:
        result = 'loss'
    else:
        result = 'breakeven'

    return {
        'result': result,
        'entry_price': round(entry_price, 2),
        'exit_price': round(exit_price, 2),
        'entry_date': str(entry_date.date()) if hasattr(entry_date, 'date') else str(entry_date),
        'exit_date': str(exit_date.date()) if hasattr(exit_date, 'date') else str(exit_date),
        'days_held': days_held,
        'return_pct': round(return_pct, 4),
        'return_r': round(return_r, 4),
        'exit_reason': exit_reason,
        'max_favorable_excursion': round(max_favorable, 4),
        'max_adverse_excursion': round(max_adverse, 4),
        'initial_risk_pct': round((initial_risk / entry_price) * 100, 4) if initial_risk else 0,
    }


# ─── Quick self-test ─────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Trade Simulator — Self Test")
    print("=" * 50)

    # Create a synthetic stock DataFrame (20 days)
    dates = pd.date_range('2024-01-01', periods=80, freq='B')
    np.random.seed(42)

    # Simulate uptrending stock: starts at 100, drifts up
    close = [100.0]
    for i in range(79):
        change = np.random.normal(0.3, 2.0)  # slight upward drift
        close.append(max(close[-1] + change, 50))

    close = np.array(close)
    high = close * (1 + np.random.uniform(0, 0.02, 80))
    low = close * (1 - np.random.uniform(0, 0.02, 80))
    volume = np.random.randint(1000000, 5000000, 80)

    df = pd.DataFrame({
        'Open': close * 0.999,
        'High': high,
        'Low': low,
        'Close': close,
        'Volume': volume,
    }, index=dates)

    # Test each holding period
    for period in ['quick', 'standard', 'position']:
        result = simulate_trade(df, entry_idx=30, holding_period=period)
        print(f"\n  {period.upper()}: {result['result']} ({result['exit_reason']})")
        print(f"    Entry: ${result['entry_price']} → Exit: ${result['exit_price']}")
        print(f"    Return: {result['return_pct']:.2f}% | R: {result['return_r']:.2f}")
        print(f"    Days: {result['days_held']} | MFE: {result['max_favorable_excursion']:.2f}% | MAE: {result['max_adverse_excursion']:.2f}%")

    # Test regime classification
    spy_df = df.copy()
    regime = classify_market_regime(spy_df, vix_value=18, date_idx=60)
    print(f"\n  Regime at idx 60: {regime}")

    above = is_spy_above_200sma(spy_df, date_idx=60)
    print(f"  SPY above 200 SMA: {above}")

    print("\nSelf-test complete")
