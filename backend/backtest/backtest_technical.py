"""
Backtest Technical Scoring Criteria
===================================
Day 27: Phase 2 - Testing if our technical scoring system works
Day 39: Added structural stop comparison (swing low - ATR)

Hypothesis: Stocks scoring ≥30/40 on technical criteria achieve +10%
before -7% with >55% win rate within 60 trading days.

Entry Criteria (30+ points required):
- Trend Structure (15 pts): Price > 50 SMA > 200 SMA
- Short-term (10 pts): Price > 8 EMA > 21 EMA
- Volume (5 pts): Recent volume > 50-day average
- RS (10 pts): Outperforming SPY

Trade Parameters:
- Entry: Close price on signal day
- Target: +10%
- Stop: -7% (fixed) OR swing_low - 2*ATR (structural)
- Max Hold: 60 trading days

Usage:
    python backtest_technical.py
    python backtest_technical.py --compare-stops  # Compare stop methods
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


def calculate_sma(prices, period):
    """Calculate Simple Moving Average"""
    if len(prices) < period:
        return None
    return prices[-period:].mean()


def calculate_ema(prices, period):
    """Calculate Exponential Moving Average"""
    if len(prices) < period:
        return None
    ema_series = prices.ewm(span=period, adjust=False).mean()
    return ema_series.iloc[-1]


# =============================================================================
# DAY 41: MARKET REGIME FILTER (TIER 1 Fix #1)
# =============================================================================

def check_bull_regime(spy_df, date_idx, ema_period=200):
    """
    Check if market is in bull regime (SPY > 200-EMA).

    Research finding: 85%+ of pullback trades fail in bear markets.
    This filter prevents entries when SPY is below its 200-day EMA.

    Args:
        spy_df: SPY DataFrame with Close prices
        date_idx: Index of the date to check
        ema_period: EMA period (default 200)

    Returns:
        tuple: (is_bull, spy_close, spy_ema)
    """
    if date_idx < ema_period:
        return False, None, None

    # Get prices up to this date
    prices = spy_df['Close'].iloc[:date_idx + 1]

    # Calculate 200-day EMA
    ema_series = prices.ewm(span=ema_period, adjust=False).mean()
    spy_ema = ema_series.iloc[-1]
    spy_close = prices.iloc[-1]

    # Bull regime: SPY close > 200-EMA
    is_bull = spy_close > spy_ema

    return is_bull, spy_close, spy_ema


# =============================================================================
# DAY 41: EARNINGS BLACKOUT (TIER 1 Fix #3)
# =============================================================================

def get_earnings_dates_cached(ticker, cache={}):
    """
    Get historical earnings dates for a ticker with caching.

    Uses yfinance earnings calendar. Returns empty list if unavailable.
    Cache prevents repeated API calls for the same ticker.

    Args:
        ticker: Stock ticker symbol
        cache: Internal cache dictionary

    Returns:
        list: List of earnings dates (pd.Timestamp)
    """
    if ticker in cache:
        return cache[ticker]

    try:
        stock = yf.Ticker(ticker)
        # Get earnings dates (includes historical)
        earnings = stock.get_earnings_dates(limit=50)  # ~12.5 years of quarterly earnings

        if earnings is not None and not earnings.empty:
            # Extract just the dates
            dates = list(earnings.index)
            cache[ticker] = dates
            return dates
        else:
            cache[ticker] = []
            return []
    except Exception:
        cache[ticker] = []
        return []


def check_earnings_blackout(entry_date, earnings_dates, blackout_days=5):
    """
    Check if entry date is within blackout period of any earnings date.

    Research finding: Earnings can gap 8-15% overnight.
    Professional standard: Skip entries within ±5 days of earnings.

    Args:
        entry_date: Date of proposed entry (pd.Timestamp)
        earnings_dates: List of earnings dates
        blackout_days: Days before/after earnings to avoid (default 5)

    Returns:
        tuple: (is_in_blackout, nearest_earnings, days_to_earnings)
    """
    if not earnings_dates:
        return False, None, None  # No earnings data = allow entry

    entry_date = pd.Timestamp(entry_date)
    nearest_earnings = None
    min_days = float('inf')

    for earn_date in earnings_dates:
        earn_date = pd.Timestamp(earn_date)
        days_diff = abs((entry_date - earn_date).days)

        if days_diff < min_days:
            min_days = days_diff
            nearest_earnings = earn_date

    # In blackout if within ±5 days of earnings
    is_in_blackout = min_days <= blackout_days

    return is_in_blackout, nearest_earnings, min_days


# =============================================================================
# DAY 41: VOLUME CONFIRMATION (TIER 1 Fix #2)
# =============================================================================

def check_volume_confirmation(stock_df, date_idx, ma_period=50):
    """
    Check if current volume is above 50-day moving average.

    Research finding: 30-40% of breakouts fail without volume confirmation.
    With volume filter: failure rate drops to 15-20%.

    Args:
        stock_df: Stock DataFrame with Volume column
        date_idx: Index of the date to check
        ma_period: Moving average period (default 50)

    Returns:
        tuple: (has_volume, current_vol, vol_ma, vol_ratio)
    """
    if date_idx < ma_period:
        return False, None, None, None

    # Get volume data up to this date
    volumes = stock_df['Volume'].iloc[:date_idx + 1]

    # Current day's volume
    current_vol = volumes.iloc[-1]

    # 50-day simple moving average of volume
    vol_ma = volumes.iloc[-ma_period:].mean()

    if vol_ma == 0:
        return False, current_vol, vol_ma, None

    # Volume ratio
    vol_ratio = current_vol / vol_ma

    # Confirmation: Current volume > 50-day MA
    has_volume = current_vol > vol_ma

    return has_volume, current_vol, vol_ma, vol_ratio


# =============================================================================
# DAY 39: STRUCTURAL STOP CALCULATIONS
# =============================================================================

def calculate_atr(high, low, close, period=14):
    """Calculate Average True Range using Wilder's smoothing"""
    if len(close) < period + 1:
        return None

    # True Range
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # ATR with Wilder's smoothing
    atr = tr.ewm(alpha=1/period, min_periods=period).mean()
    return atr.iloc[-1]


def find_swing_low(df, lookback=20, date_idx=None):
    """
    Find the most recent swing low (local minimum) before the entry date.

    A swing low is a bar where the low is lower than the lows of
    the surrounding bars (at least 2 bars on each side).
    """
    if date_idx is None:
        date_idx = len(df) - 1

    # Look at data before entry
    start_idx = max(0, date_idx - lookback)
    lows = df['Low'].iloc[start_idx:date_idx]

    if len(lows) < 5:
        return None

    # Find local minima (swing lows)
    swing_lows = []
    for i in range(2, len(lows) - 2):
        if (lows.iloc[i] < lows.iloc[i-1] and
            lows.iloc[i] < lows.iloc[i-2] and
            lows.iloc[i] < lows.iloc[i+1] and
            lows.iloc[i] < lows.iloc[i+2]):
            swing_lows.append(lows.iloc[i])

    if swing_lows:
        # Return the most recent swing low
        return swing_lows[-1]
    else:
        # Fallback: return minimum of lookback period
        return lows.min()


def calculate_structural_stop(entry_price, swing_low, atr, multiplier=2.0):
    """
    Calculate structural stop loss: swing_low - (ATR * multiplier)

    This is market-structure based, not an arbitrary percentage.
    """
    if swing_low is None or atr is None:
        # Fallback to 7% stop
        return entry_price * 0.93

    structural_stop = swing_low - (atr * multiplier)

    # Sanity check: stop shouldn't be too tight (< 1 ATR) or too wide (> 15%)
    min_stop = entry_price - atr  # At least 1 ATR
    max_stop = entry_price * 0.85  # Max 15% loss

    if structural_stop > entry_price - atr:
        structural_stop = min_stop
    if structural_stop < max_stop:
        structural_stop = max_stop

    return structural_stop


def simulate_trade_structural(stock_df, entry_idx, target_pct=0.10, atr_mult=2.0, max_hold=60):
    """
    Simulate a trade using STRUCTURAL stop (swing low - ATR buffer)
    instead of fixed percentage stop.

    Returns:
        result: 'WIN', 'LOSS', 'EXPIRED'
        exit_price: final exit price
        days_held: number of days position was held
        return_pct: percentage return
        stop_pct: actual stop loss percentage used
    """
    entry_price = stock_df['Close'].iloc[entry_idx]
    target_price = entry_price * (1 + target_pct)

    # Calculate structural stop
    lookback_start = max(0, entry_idx - 50)
    high = stock_df['High'].iloc[lookback_start:entry_idx]
    low = stock_df['Low'].iloc[lookback_start:entry_idx]
    close = stock_df['Close'].iloc[lookback_start:entry_idx]

    atr = calculate_atr(high, low, close, period=14)
    swing_low = find_swing_low(stock_df, lookback=20, date_idx=entry_idx)
    stop_price = calculate_structural_stop(entry_price, swing_low, atr, atr_mult)

    # Calculate actual stop percentage for reporting
    stop_pct = (entry_price - stop_price) / entry_price

    # Simulate each day
    for days in range(1, max_hold + 1):
        check_idx = entry_idx + days

        if check_idx >= len(stock_df):
            return 'EXPIRED', stock_df['Close'].iloc[-1], days - 1, \
                   (stock_df['Close'].iloc[-1] / entry_price - 1) * 100, stop_pct * 100

        high_day = stock_df['High'].iloc[check_idx]
        low_day = stock_df['Low'].iloc[check_idx]

        # Check stop loss first
        if low_day <= stop_price:
            return 'LOSS', stop_price, days, -stop_pct * 100, stop_pct * 100

        # Check target
        if high_day >= target_price:
            return 'WIN', target_price, days, target_pct * 100, stop_pct * 100

    # Max hold reached
    final_price = stock_df['Close'].iloc[entry_idx + max_hold]
    return_pct = (final_price / entry_price - 1) * 100

    if return_pct > 0:
        return 'EXPIRED_PROFIT', final_price, max_hold, return_pct, stop_pct * 100
    else:
        return 'EXPIRED_LOSS', final_price, max_hold, return_pct, stop_pct * 100


def compare_stop_methods(tickers, start_date='2020-01-01', end_date='2024-12-31',
                         min_score=30, target_pct=0.10, max_hold=60):
    """
    Compare structural stops (swing low - ATR) vs fixed percentage stops.

    This validates the hypothesis that structural stops result in:
    1. Smaller average losses
    2. Similar or better win rate

    Returns comparison summary.
    """
    print(f"\n{'='*70}")
    print("STOP LOSS METHOD COMPARISON: Structural vs Fixed %")
    print(f"{'='*70}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Entry Criteria: Technical Score >= {min_score}/40")
    print(f"Target: +{target_pct*100:.0f}%")
    print(f"Fixed Stop: -7%")
    print(f"Structural Stop: swing_low - 2×ATR")
    print(f"Max Hold: {max_hold} days")
    print(f"{'='*70}\n")

    # Download SPY data
    print("Downloading SPY data...")
    spy_df = yf.download('SPY', start=start_date, end=end_date, progress=False)
    if spy_df.empty:
        print("ERROR: Could not download SPY data")
        return None

    if isinstance(spy_df.columns, pd.MultiIndex):
        spy_df.columns = spy_df.columns.get_level_values(0)

    fixed_trades = []
    structural_trades = []

    for ticker in tickers:
        print(f"\nProcessing {ticker}...")

        try:
            buffer_start = (datetime.strptime(start_date, '%Y-%m-%d') -
                          timedelta(days=400)).strftime('%Y-%m-%d')

            stock_df = yf.download(ticker, start=buffer_start, end=end_date, progress=False)

            if stock_df.empty:
                continue

            if isinstance(stock_df.columns, pd.MultiIndex):
                stock_df.columns = stock_df.columns.get_level_values(0)

            common_dates = stock_df.index.intersection(spy_df.index)
            stock_df = stock_df.loc[common_dates]
            spy_aligned = spy_df.loc[common_dates]

            cooldown = 0

            for i in range(200, len(stock_df) - max_hold):
                if cooldown > 0:
                    cooldown -= 1
                    continue

                date = stock_df.index[i]
                if date < pd.Timestamp(start_date):
                    continue

                score, _ = get_technical_score(stock_df, spy_aligned, i)

                if score and score >= min_score:
                    # Simulate with FIXED 7% stop
                    result_fixed, exit_fixed, days_fixed, ret_fixed = simulate_trade(
                        stock_df, i, target_pct, stop_pct=0.07, max_hold=max_hold
                    )
                    fixed_trades.append({
                        'ticker': ticker,
                        'date': date,
                        'result': result_fixed,
                        'return_pct': ret_fixed,
                        'days_held': days_fixed,
                        'stop_pct': 7.0
                    })

                    # Simulate with STRUCTURAL stop
                    result_struct, exit_struct, days_struct, ret_struct, stop_used = simulate_trade_structural(
                        stock_df, i, target_pct, atr_mult=2.0, max_hold=max_hold
                    )
                    structural_trades.append({
                        'ticker': ticker,
                        'date': date,
                        'result': result_struct,
                        'return_pct': ret_struct,
                        'days_held': days_struct,
                        'stop_pct': stop_used
                    })

                    cooldown = max(days_fixed, days_struct) + 5

        except Exception as e:
            print(f"  Error: {e}")
            continue

    # Calculate summaries
    if not fixed_trades or not structural_trades:
        print("\nNo trades to compare!")
        return None

    fixed_df = pd.DataFrame(fixed_trades)
    struct_df = pd.DataFrame(structural_trades)

    # Summary stats
    def calc_stats(df, name):
        total = len(df)
        wins = len(df[df['result'] == 'WIN'])
        losses = len(df[df['result'] == 'LOSS'])
        win_rate = (wins + len(df[df['result'] == 'EXPIRED_PROFIT'])) / total * 100
        avg_return = df['return_pct'].mean()
        avg_loss = df[df['return_pct'] < 0]['return_pct'].mean() if losses > 0 else 0
        avg_stop = df['stop_pct'].mean()
        return {
            'name': name,
            'total': total,
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate,
            'avg_return': avg_return,
            'avg_loss': avg_loss,
            'avg_stop_pct': avg_stop
        }

    fixed_stats = calc_stats(fixed_df, 'Fixed 7%')
    struct_stats = calc_stats(struct_df, 'Structural')

    # Print comparison
    print(f"\n{'='*70}")
    print("COMPARISON RESULTS")
    print(f"{'='*70}")
    print(f"{'Metric':<25} {'Fixed 7%':>15} {'Structural':>15} {'Winner':>12}")
    print(f"{'-'*70}")

    print(f"{'Total Trades':<25} {fixed_stats['total']:>15} {struct_stats['total']:>15}")
    print(f"{'Win Rate':<25} {fixed_stats['win_rate']:>14.1f}% {struct_stats['win_rate']:>14.1f}% "
          f"{'STRUCT' if struct_stats['win_rate'] > fixed_stats['win_rate'] else 'FIXED':>12}")
    print(f"{'Avg Return':<25} {fixed_stats['avg_return']:>14.2f}% {struct_stats['avg_return']:>14.2f}% "
          f"{'STRUCT' if struct_stats['avg_return'] > fixed_stats['avg_return'] else 'FIXED':>12}")
    print(f"{'Avg Loss':<25} {fixed_stats['avg_loss']:>14.2f}% {struct_stats['avg_loss']:>14.2f}% "
          f"{'STRUCT' if struct_stats['avg_loss'] > fixed_stats['avg_loss'] else 'FIXED':>12}")
    print(f"{'Avg Stop %':<25} {fixed_stats['avg_stop_pct']:>14.1f}% {struct_stats['avg_stop_pct']:>14.1f}%")

    print(f"\n{'='*70}")
    print("VALIDATION GATE G1: Structural Stops")
    print(f"{'='*70}")
    print(f"Criteria: Avg loss with structural < avg loss with fixed")
    print(f"Fixed avg loss: {fixed_stats['avg_loss']:.2f}%")
    print(f"Structural avg loss: {struct_stats['avg_loss']:.2f}%")

    if struct_stats['avg_loss'] > fixed_stats['avg_loss']:  # Less negative = better
        print(f"\n✅ GATE PASSED: Structural stops reduce avg loss by "
              f"{fixed_stats['avg_loss'] - struct_stats['avg_loss']:.2f}%")
    else:
        print(f"\n❌ GATE FAILED: Structural stops did not improve avg loss")

    print(f"{'='*70}\n")

    return {
        'fixed': fixed_stats,
        'structural': struct_stats,
        'fixed_trades': fixed_df,
        'structural_trades': struct_df
    }


def get_technical_score(stock_df, spy_df, date_idx):
    """
    Calculate technical score for a specific date
    Returns score out of 40 and individual components
    """
    # Need at least 200 days of data before the signal date
    if date_idx < 200:
        return None, {}

    # Get data up to (but not including future) the signal date
    stock_prices = stock_df['Close'].iloc[:date_idx+1]
    stock_volumes = stock_df['Volume'].iloc[:date_idx+1]
    spy_prices = spy_df['Close'].iloc[:date_idx+1]

    current_price = stock_prices.iloc[-1]
    scores = {
        'trend_structure': 0,
        'short_term': 0,
        'volume': 0,
        'rs': 0
    }

    # 1. Trend Structure (15 points): Price > 50 SMA > 200 SMA
    sma50 = calculate_sma(stock_prices, 50)
    sma200 = calculate_sma(stock_prices, 200)

    if sma50 and sma200:
        if current_price > sma50 and sma50 > sma200:
            scores['trend_structure'] = 15
        elif current_price > sma200:
            scores['trend_structure'] = 5

    # 2. Short-term Trend (10 points): Price > 8 EMA > 21 EMA
    ema8 = calculate_ema(stock_prices, 8)
    ema21 = calculate_ema(stock_prices, 21)

    if ema8 and ema21:
        if current_price > ema8 and ema8 > ema21:
            scores['short_term'] = 10
        elif current_price > ema21:
            scores['short_term'] = 3

    # 3. Volume (5 points): Recent volume vs 50-day average
    avg_vol_50 = stock_volumes.iloc[-50:].mean()
    recent_vol = stock_volumes.iloc[-5:].mean()

    if avg_vol_50 > 0:
        vol_ratio = recent_vol / avg_vol_50
        if vol_ratio >= 1.5:
            scores['volume'] = 5
        elif vol_ratio >= 1.0:
            scores['volume'] = 2

    # 4. Relative Strength (10 points): Stock vs SPY performance
    if len(stock_prices) >= 252 and len(spy_prices) >= 252:
        stock_return_52w = (stock_prices.iloc[-1] / stock_prices.iloc[-252]) - 1
        spy_return_52w = (spy_prices.iloc[-1] / spy_prices.iloc[-252]) - 1

        if spy_return_52w != 0:
            rs_ratio = (1 + stock_return_52w) / (1 + spy_return_52w)

            if rs_ratio >= 1.5:
                scores['rs'] = 10
            elif rs_ratio >= 1.2:
                scores['rs'] = 7
            elif rs_ratio >= 1.0:
                scores['rs'] = 4
            elif rs_ratio >= 0.8:
                scores['rs'] = 1

    total_score = sum(scores.values())
    return total_score, scores


def simulate_trade(stock_df, entry_idx, target_pct=0.10, stop_pct=0.07, max_hold=60):
    """
    Simulate a single trade from entry date

    Returns:
        result: 'WIN', 'LOSS', 'EXPIRED'
        exit_price: final exit price
        days_held: number of days position was held
        return_pct: percentage return
    """
    entry_price = stock_df['Close'].iloc[entry_idx]
    target_price = entry_price * (1 + target_pct)
    stop_price = entry_price * (1 - stop_pct)

    # Simulate each day
    for days in range(1, max_hold + 1):
        check_idx = entry_idx + days

        # Check if we ran out of data
        if check_idx >= len(stock_df):
            return 'EXPIRED', stock_df['Close'].iloc[-1], days - 1, \
                   (stock_df['Close'].iloc[-1] / entry_price - 1) * 100

        high = stock_df['High'].iloc[check_idx]
        low = stock_df['Low'].iloc[check_idx]
        close = stock_df['Close'].iloc[check_idx]

        # Check stop loss first (conservative assumption - stop hit if low touches)
        if low <= stop_price:
            return 'LOSS', stop_price, days, -stop_pct * 100

        # Check target (hit if high touches)
        if high >= target_price:
            return 'WIN', target_price, days, target_pct * 100

    # Max hold reached - exit at close
    final_price = stock_df['Close'].iloc[entry_idx + max_hold]
    return_pct = (final_price / entry_price - 1) * 100

    if return_pct > 0:
        return 'EXPIRED_PROFIT', final_price, max_hold, return_pct
    else:
        return 'EXPIRED_LOSS', final_price, max_hold, return_pct


def run_backtest(tickers, start_date='2020-01-01', end_date='2024-12-31',
                 min_score=30, target_pct=0.10, stop_pct=0.07, max_hold=60):
    """
    Run backtest on a list of tickers

    Args:
        tickers: List of stock tickers to test
        start_date: Start of backtest period
        end_date: End of backtest period
        min_score: Minimum technical score to trigger entry (30 out of 40)
        target_pct: Target profit percentage (0.10 = 10%)
        stop_pct: Stop loss percentage (0.07 = 7%)
        max_hold: Maximum days to hold position

    Returns:
        results_df: DataFrame with all trades
        summary: Dictionary with summary statistics
    """
    print(f"\n{'='*60}")
    print("BACKTEST: Technical Scoring System")
    print(f"{'='*60}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Entry Criteria: Technical Score >= {min_score}/40")
    print(f"Target: +{target_pct*100:.0f}%")
    print(f"Stop Loss: -{stop_pct*100:.0f}%")
    print(f"Max Hold: {max_hold} days")
    print(f"TIER 1 Fix #1: Market Regime Filter (SPY > 200-EMA) ACTIVE")
    print(f"TIER 1 Fix #2: Volume Confirmation (Vol > 50-day MA) ACTIVE")
    print(f"TIER 1 Fix #3: Earnings Blackout (±5 days) ACTIVE")
    print(f"{'='*60}\n")

    # Download SPY data (benchmark)
    print("Downloading SPY data for RS calculation...")
    spy_df = yf.download('SPY', start=start_date, end=end_date, progress=False)
    if spy_df.empty:
        print("ERROR: Could not download SPY data")
        return None, None

    # Flatten multi-level columns if present
    if isinstance(spy_df.columns, pd.MultiIndex):
        spy_df.columns = spy_df.columns.get_level_values(0)

    print(f"SPY data: {len(spy_df)} days\n")

    all_trades = []

    for ticker in tickers:
        print(f"\nProcessing {ticker}...")

        try:
            # Download stock data with buffer for SMA calculations
            buffer_start = (datetime.strptime(start_date, '%Y-%m-%d') -
                          timedelta(days=400)).strftime('%Y-%m-%d')

            stock_df = yf.download(ticker, start=buffer_start, end=end_date, progress=False)

            if stock_df.empty:
                print(f"  No data available for {ticker}")
                continue

            # Flatten multi-level columns if present
            if isinstance(stock_df.columns, pd.MultiIndex):
                stock_df.columns = stock_df.columns.get_level_values(0)

            # Align with SPY dates
            common_dates = stock_df.index.intersection(spy_df.index)
            stock_df = stock_df.loc[common_dates]
            spy_aligned = spy_df.loc[common_dates]

            print(f"  Data: {len(stock_df)} days")

            # DAY 41: Fetch earnings dates once per ticker (TIER 1 Fix #3)
            earnings_dates = get_earnings_dates_cached(ticker)
            if earnings_dates:
                print(f"  Earnings dates loaded: {len(earnings_dates)} quarters")

            # Find signal days
            signal_count = 0
            cooldown = 0  # Prevent re-entry for X days after a trade

            for i in range(200, len(stock_df) - max_hold):  # Need 200 days before and max_hold after
                if cooldown > 0:
                    cooldown -= 1
                    continue

                date = stock_df.index[i]

                # Only check dates within our backtest period
                if date < pd.Timestamp(start_date):
                    continue

                # DAY 41: TIER 1 Fix #1 - Market Regime Filter
                # Skip entries when SPY is below 200-EMA (bear market)
                spy_idx = spy_aligned.index.get_loc(date)
                is_bull, spy_close, spy_ema = check_bull_regime(spy_aligned, spy_idx)
                if not is_bull:
                    continue  # Skip this entry - bear market

                # DAY 41: TIER 1 Fix #2 - Volume Confirmation
                # Skip entries when volume is below 50-day MA
                has_volume, curr_vol, vol_ma, vol_ratio = check_volume_confirmation(stock_df, i)
                if not has_volume:
                    continue  # Skip this entry - insufficient volume

                # DAY 41: TIER 1 Fix #3 - Earnings Blackout
                # Skip entries within ±5 days of earnings (gap risk)
                in_blackout, nearest_earn, days_to_earn = check_earnings_blackout(date, earnings_dates)
                if in_blackout:
                    continue  # Skip this entry - earnings blackout

                score, score_details = get_technical_score(stock_df, spy_aligned, i)

                if score and score >= min_score:
                    # Found a signal - simulate trade
                    result, exit_price, days_held, return_pct = simulate_trade(
                        stock_df, i, target_pct, stop_pct, max_hold
                    )

                    entry_price = stock_df['Close'].iloc[i]
                    exit_date = stock_df.index[min(i + days_held, len(stock_df) - 1)]

                    trade = {
                        'ticker': ticker,
                        'entry_date': date.strftime('%Y-%m-%d'),
                        'exit_date': exit_date.strftime('%Y-%m-%d'),
                        'entry_price': entry_price,
                        'exit_price': exit_price,
                        'days_held': days_held,
                        'return_pct': return_pct,
                        'result': result,
                        'score': score,
                        'trend_score': score_details['trend_structure'],
                        'short_term_score': score_details['short_term'],
                        'volume_score': score_details['volume'],
                        'rs_score': score_details['rs']
                    }

                    all_trades.append(trade)
                    signal_count += 1

                    # Set cooldown to prevent overlapping trades
                    cooldown = days_held + 5

            print(f"  Signals found: {signal_count}")

        except Exception as e:
            print(f"  Error processing {ticker}: {str(e)}")
            continue

    if not all_trades:
        print("\nNo trades generated!")
        return None, None

    # Create results DataFrame
    results_df = pd.DataFrame(all_trades)

    # Calculate summary statistics
    total_trades = len(results_df)
    wins = len(results_df[results_df['result'] == 'WIN'])
    losses = len(results_df[results_df['result'] == 'LOSS'])
    expired_profit = len(results_df[results_df['result'] == 'EXPIRED_PROFIT'])
    expired_loss = len(results_df[results_df['result'] == 'EXPIRED_LOSS'])

    win_rate = (wins + expired_profit) / total_trades * 100 if total_trades > 0 else 0

    avg_return = results_df['return_pct'].mean()
    avg_win = results_df[results_df['return_pct'] > 0]['return_pct'].mean() if wins > 0 else 0
    avg_loss = results_df[results_df['return_pct'] < 0]['return_pct'].mean() if losses > 0 else 0

    avg_days_held = results_df['days_held'].mean()

    # Calculate profit factor
    gross_profits = results_df[results_df['return_pct'] > 0]['return_pct'].sum()
    gross_losses = abs(results_df[results_df['return_pct'] < 0]['return_pct'].sum())
    profit_factor = gross_profits / gross_losses if gross_losses > 0 else float('inf')

    # Calculate expectancy
    expectancy = (win_rate/100 * avg_win) + ((100-win_rate)/100 * avg_loss) if avg_loss != 0 else avg_win

    summary = {
        'total_trades': total_trades,
        'wins': wins,
        'losses': losses,
        'expired_profit': expired_profit,
        'expired_loss': expired_loss,
        'win_rate': win_rate,
        'avg_return': avg_return,
        'avg_win': avg_win,
        'avg_loss': avg_loss,
        'avg_days_held': avg_days_held,
        'profit_factor': profit_factor,
        'expectancy': expectancy,
        'gross_profits': gross_profits,
        'gross_losses': gross_losses
    }

    # Print summary
    print(f"\n{'='*60}")
    print("BACKTEST RESULTS SUMMARY")
    print(f"{'='*60}")
    print(f"Total Trades: {total_trades}")
    print(f"  - Wins (hit +{target_pct*100:.0f}%): {wins}")
    print(f"  - Losses (hit -{stop_pct*100:.0f}%): {losses}")
    print(f"  - Expired Profitable: {expired_profit}")
    print(f"  - Expired at Loss: {expired_loss}")
    print(f"\nWin Rate: {win_rate:.1f}%")
    print(f"Average Return: {avg_return:.2f}%")
    print(f"Average Win: +{avg_win:.2f}%")
    print(f"Average Loss: {avg_loss:.2f}%")
    print(f"Average Days Held: {avg_days_held:.1f}")
    print(f"\nProfit Factor: {profit_factor:.2f}")
    print(f"Expectancy: {expectancy:.2f}%")
    print(f"{'='*60}")

    # Hypothesis test
    print(f"\n{'='*60}")
    print("HYPOTHESIS TEST")
    print(f"{'='*60}")
    print(f"H0: Win rate <= 55%")
    print(f"H1: Win rate > 55%")
    print(f"\nObserved Win Rate: {win_rate:.1f}%")

    if win_rate >= 55:
        print(f"\n✅ HYPOTHESIS SUPPORTED: Win rate ({win_rate:.1f}%) >= 55%")
    else:
        print(f"\n❌ HYPOTHESIS REJECTED: Win rate ({win_rate:.1f}%) < 55%")

    # Additional validation
    print(f"\nAdditional Validation:")
    print(f"  - Profit Factor {'✅ >1.0' if profit_factor > 1 else '❌ <1.0'}: {profit_factor:.2f}")
    print(f"  - Expectancy {'✅ Positive' if expectancy > 0 else '❌ Negative'}: {expectancy:.2f}%")
    print(f"{'='*60}\n")

    return results_df, summary


def main():
    """Main entry point"""
    import sys

    # Test universe - mix of large caps and mid caps
    test_tickers = [
        # Large Cap Tech
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
        # Large Cap Other
        'JPM', 'V', 'MA', 'UNH', 'JNJ', 'PG', 'HD', 'DIS',
        # Mid Cap Growth (as of 2020)
        'CRM', 'NOW', 'SHOP', 'SQ', 'ROKU', 'DDOG', 'ZM',
        # Traditional
        'WMT', 'KO', 'PEP', 'MCD', 'NKE', 'COST'
    ]

    # Check for --compare-stops argument
    if '--compare-stops' in sys.argv:
        print("\n" + "="*70)
        print("SWING TRADE ANALYZER - STOP METHOD COMPARISON")
        print("Day 39: Validating Structural vs Fixed % Stops")
        print("="*70)
        print(f"\nTest Universe: {len(test_tickers)} stocks")

        # Run smaller universe for faster testing
        quick_test = test_tickers[:10]  # First 10 tickers
        print(f"Quick test: {', '.join(quick_test)}")

        comparison = compare_stop_methods(
            tickers=quick_test,
            start_date='2022-01-01',  # Shorter period for faster testing
            end_date='2024-12-31',
            min_score=30,
            target_pct=0.10,
            max_hold=60
        )

        if comparison:
            print("\n✅ Comparison complete! Check results above for Gate G1 validation.")
        return

    # Regular backtest (original behavior)
    print("\n" + "="*60)
    print("SWING TRADE ANALYZER - BACKTEST")
    print("Day 27: Testing Technical Scoring Hypothesis")
    print("="*60)
    print(f"\nTest Universe: {len(test_tickers)} stocks")
    print(f"Tickers: {', '.join(test_tickers)}")

    results_df, summary = run_backtest(
        tickers=test_tickers,
        start_date='2020-01-01',
        end_date='2024-12-31',
        min_score=30,
        target_pct=0.10,
        stop_pct=0.07,
        max_hold=60
    )

    if results_df is not None:
        output_file = 'backtest_results.csv'
        results_df.to_csv(output_file, index=False)
        print(f"\nResults saved to: {output_file}")

        print(f"\n{'='*60}")
        print("SAMPLE TRADES (Last 10)")
        print(f"{'='*60}")
        print(results_df.tail(10)[['ticker', 'entry_date', 'result', 'return_pct', 'days_held', 'score']].to_string())

        print(f"\n{'='*60}")
        print("BREAKDOWN BY SCORE LEVEL")
        print(f"{'='*60}")
        for score_range in [(30, 34), (35, 39), (40, 40)]:
            subset = results_df[(results_df['score'] >= score_range[0]) &
                               (results_df['score'] <= score_range[1])]
            if len(subset) > 0:
                wr = len(subset[subset['return_pct'] > 0]) / len(subset) * 100
                avg_ret = subset['return_pct'].mean()
                print(f"Score {score_range[0]}-{score_range[1]}: {len(subset)} trades, "
                      f"Win Rate: {wr:.1f}%, Avg Return: {avg_ret:.2f}%")


if __name__ == '__main__':
    main()
