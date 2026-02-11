"""
Backtest ADX/RSI Thresholds - Research Validation
==================================================
Day 51: Testing Perplexity research findings on ADX-based RSI interpretation

RESEARCH HYPOTHESES TO TEST:
1. ADX < 20 + RSI > 70: Mean reversion expected (pullback within 5-10 days)
2. ADX > 25 + RSI > 70: Momentum continuation (RSI is confirmation, not sell signal)
3. RSI > 80: 68% probability of 5%+ pullback within 14 days (any ADX)
4. RSI > 80 + ADX > 25 (strong trend): Does pullback rate decrease?

METRICS TO REPORT:
- Signal count
- Pullback rate (5%+ decline within holding period)
- Average days to pullback
- Win rate if buying the signal
- False positive rate

Usage:
    python backtest_adx_rsi_thresholds.py
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


def calculate_rsi(prices, period=14):
    """Calculate RSI using Wilder's smoothing"""
    if len(prices) < period + 1:
        return None

    deltas = prices.diff()
    gains = deltas.where(deltas > 0, 0)
    losses = -deltas.where(deltas < 0, 0)

    avg_gain = gains.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = losses.ewm(alpha=1/period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]


def calculate_adx(high, low, close, period=14):
    """Calculate ADX (Average Directional Index)"""
    if len(close) < period * 2:
        return None

    # True Range
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    # +DM and -DM
    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0)

    # Smoothed averages
    atr = tr.ewm(alpha=1/period, min_periods=period).mean()
    plus_di = 100 * (plus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)
    minus_di = 100 * (minus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)

    # DX and ADX
    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(alpha=1/period, min_periods=period).mean()

    return adx.iloc[-1]


def check_pullback(stock_df, entry_idx, threshold_pct=5.0, max_days=14):
    """
    Check if a 5%+ pullback occurs within max_days after entry.

    Returns:
        tuple: (had_pullback, days_to_pullback, max_drawdown_pct)
    """
    entry_price = stock_df['Close'].iloc[entry_idx]

    for days in range(1, min(max_days + 1, len(stock_df) - entry_idx)):
        check_idx = entry_idx + days
        low = stock_df['Low'].iloc[check_idx]
        drawdown_pct = (entry_price - low) / entry_price * 100

        if drawdown_pct >= threshold_pct:
            return True, days, drawdown_pct

    # Calculate max drawdown even if threshold not hit
    if entry_idx + max_days < len(stock_df):
        lows = stock_df['Low'].iloc[entry_idx + 1:entry_idx + max_days + 1]
        max_drawdown = (entry_price - lows.min()) / entry_price * 100
        return False, None, max_drawdown

    return False, None, None


def check_continuation(stock_df, entry_idx, target_pct=5.0, max_days=14):
    """
    Check if price continues upward by target_pct within max_days.

    Returns:
        tuple: (had_continuation, days_to_target, max_gain_pct)
    """
    entry_price = stock_df['Close'].iloc[entry_idx]
    target_price = entry_price * (1 + target_pct / 100)

    for days in range(1, min(max_days + 1, len(stock_df) - entry_idx)):
        check_idx = entry_idx + days
        high = stock_df['High'].iloc[check_idx]

        if high >= target_price:
            return True, days, (high - entry_price) / entry_price * 100

    # Calculate max gain even if target not hit
    if entry_idx + max_days < len(stock_df):
        highs = stock_df['High'].iloc[entry_idx + 1:entry_idx + max_days + 1]
        max_gain = (highs.max() - entry_price) / entry_price * 100
        return False, None, max_gain

    return False, None, None


def run_adx_rsi_backtest(tickers, start_date='2020-01-01', end_date='2024-12-31'):
    """
    Test ADX/RSI threshold hypotheses from Perplexity research.
    """
    print(f"\n{'='*70}")
    print("BACKTEST: ADX/RSI Threshold Validation")
    print("Day 51: Testing Perplexity Research Findings")
    print(f"{'='*70}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Tickers: {len(tickers)}")
    print(f"{'='*70}\n")

    # Hypothesis buckets
    results = {
        # RSI > 70 signals by ADX regime
        'adx_below_20_rsi_above_70': [],  # Weak trend + overbought
        'adx_20_to_25_rsi_above_70': [],  # Transitional
        'adx_above_25_rsi_above_70': [],  # Strong trend + overbought

        # RSI > 80 signals (extreme)
        'rsi_above_80_all': [],           # All RSI > 80
        'rsi_above_80_adx_below_20': [],  # RSI > 80 in weak trend
        'rsi_above_80_adx_above_25': [],  # RSI > 80 in strong trend
    }

    for ticker in tickers:
        print(f"Processing {ticker}...")

        try:
            # Download with buffer for indicator calculations
            buffer_start = (datetime.strptime(start_date, '%Y-%m-%d') -
                          timedelta(days=100)).strftime('%Y-%m-%d')

            stock_df = yf.download(ticker, start=buffer_start, end=end_date, progress=False)

            if stock_df.empty or len(stock_df) < 100:
                print(f"  Insufficient data for {ticker}")
                continue

            # Flatten multi-level columns if present
            if isinstance(stock_df.columns, pd.MultiIndex):
                stock_df.columns = stock_df.columns.get_level_values(0)

            signals_found = 0

            # Scan for signals
            for i in range(50, len(stock_df) - 15):  # Need 14 days after signal
                date = stock_df.index[i]

                # Only check dates within our backtest period
                if date < pd.Timestamp(start_date):
                    continue

                # Calculate indicators
                prices = stock_df['Close'].iloc[:i+1]
                high = stock_df['High'].iloc[:i+1]
                low = stock_df['Low'].iloc[:i+1]

                rsi = calculate_rsi(prices, period=14)
                adx = calculate_adx(high, low, prices, period=14)

                if rsi is None or adx is None:
                    continue

                # Check RSI > 70 signals
                if rsi > 70:
                    had_pullback, days_to_pullback, max_drawdown = check_pullback(
                        stock_df, i, threshold_pct=5.0, max_days=14
                    )
                    had_continuation, days_to_target, max_gain = check_continuation(
                        stock_df, i, target_pct=5.0, max_days=14
                    )

                    signal_data = {
                        'ticker': ticker,
                        'date': date,
                        'rsi': rsi,
                        'adx': adx,
                        'had_pullback': had_pullback,
                        'days_to_pullback': days_to_pullback,
                        'max_drawdown': max_drawdown,
                        'had_continuation': had_continuation,
                        'days_to_target': days_to_target,
                        'max_gain': max_gain
                    }

                    # Categorize by ADX regime
                    if adx < 20:
                        results['adx_below_20_rsi_above_70'].append(signal_data)
                    elif adx <= 25:
                        results['adx_20_to_25_rsi_above_70'].append(signal_data)
                    else:
                        results['adx_above_25_rsi_above_70'].append(signal_data)

                    # RSI > 80 extreme signals
                    if rsi > 80:
                        results['rsi_above_80_all'].append(signal_data)
                        if adx < 20:
                            results['rsi_above_80_adx_below_20'].append(signal_data)
                        elif adx > 25:
                            results['rsi_above_80_adx_above_25'].append(signal_data)

                    signals_found += 1

            print(f"  Found {signals_found} RSI > 70 signals")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    # Analyze results
    print(f"\n{'='*70}")
    print("HYPOTHESIS TEST RESULTS")
    print(f"{'='*70}\n")

    def analyze_bucket(signals, name):
        if not signals:
            print(f"\n{name}: No signals found")
            return None

        df = pd.DataFrame(signals)
        total = len(df)
        pullback_count = df['had_pullback'].sum()
        continuation_count = df['had_continuation'].sum()
        pullback_rate = pullback_count / total * 100
        continuation_rate = continuation_count / total * 100

        avg_rsi = df['rsi'].mean()
        avg_adx = df['adx'].mean()
        avg_max_drawdown = df['max_drawdown'].mean()
        avg_max_gain = df['max_gain'].mean()

        # Average days to pullback (only for signals that had pullback)
        pullback_signals = df[df['had_pullback']]
        avg_days_to_pullback = pullback_signals['days_to_pullback'].mean() if len(pullback_signals) > 0 else None

        print(f"\n{'='*70}")
        print(f"BUCKET: {name}")
        print(f"{'='*70}")
        print(f"Total Signals: {total}")
        print(f"Avg RSI: {avg_rsi:.1f}")
        print(f"Avg ADX: {avg_adx:.1f}")
        print(f"\nPullback Analysis (5%+ decline in 14 days):")
        print(f"  - Pullback Rate: {pullback_rate:.1f}% ({pullback_count}/{total})")
        print(f"  - Avg Days to Pullback: {avg_days_to_pullback:.1f}" if avg_days_to_pullback else "  - Avg Days to Pullback: N/A")
        print(f"  - Avg Max Drawdown: {avg_max_drawdown:.1f}%")
        print(f"\nContinuation Analysis (5%+ gain in 14 days):")
        print(f"  - Continuation Rate: {continuation_rate:.1f}% ({continuation_count}/{total})")
        print(f"  - Avg Max Gain: {avg_max_gain:.1f}%")

        return {
            'name': name,
            'total': total,
            'pullback_rate': pullback_rate,
            'continuation_rate': continuation_rate,
            'avg_rsi': avg_rsi,
            'avg_adx': avg_adx,
            'avg_max_drawdown': avg_max_drawdown,
            'avg_max_gain': avg_max_gain,
            'avg_days_to_pullback': avg_days_to_pullback
        }

    # Analyze each bucket
    summaries = {}

    print("\n" + "="*70)
    print("HYPOTHESIS 1: ADX < 20 + RSI > 70 = Mean Reversion Expected")
    print("="*70)
    summaries['weak_trend'] = analyze_bucket(
        results['adx_below_20_rsi_above_70'],
        "ADX < 20 + RSI > 70 (Weak Trend + Overbought)"
    )

    print("\n" + "="*70)
    print("HYPOTHESIS 2: ADX > 25 + RSI > 70 = Momentum Confirmation")
    print("="*70)
    summaries['strong_trend'] = analyze_bucket(
        results['adx_above_25_rsi_above_70'],
        "ADX > 25 + RSI > 70 (Strong Trend + Overbought)"
    )

    print("\n" + "="*70)
    print("HYPOTHESIS 3: RSI > 80 = 68% Pullback Rate (Research Claim)")
    print("="*70)
    summaries['rsi_80_all'] = analyze_bucket(
        results['rsi_above_80_all'],
        "RSI > 80 (All ADX levels)"
    )

    print("\n" + "="*70)
    print("HYPOTHESIS 4: RSI > 80 + Strong Trend = Lower Pullback Rate?")
    print("="*70)
    summaries['rsi_80_weak'] = analyze_bucket(
        results['rsi_above_80_adx_below_20'],
        "RSI > 80 + ADX < 20 (Weak Trend)"
    )
    summaries['rsi_80_strong'] = analyze_bucket(
        results['rsi_above_80_adx_above_25'],
        "RSI > 80 + ADX > 25 (Strong Trend)"
    )

    # Final validation summary
    print("\n" + "="*70)
    print("RESEARCH VALIDATION SUMMARY")
    print("="*70)

    # Hypothesis 1: Weak trend should have HIGHER pullback rate
    if summaries.get('weak_trend') and summaries.get('strong_trend'):
        weak_pullback = summaries['weak_trend']['pullback_rate']
        strong_pullback = summaries['strong_trend']['pullback_rate']

        print(f"\nH1: Weak trend (ADX<20) pullback rate vs Strong trend (ADX>25)")
        print(f"    Weak: {weak_pullback:.1f}% | Strong: {strong_pullback:.1f}%")
        if weak_pullback > strong_pullback:
            print(f"    ✅ VALIDATED: Weak trends mean-revert faster ({weak_pullback:.1f}% > {strong_pullback:.1f}%)")
        else:
            print(f"    ❌ NOT VALIDATED: Strong trends had higher pullback rate")

    # Hypothesis 2: RSI > 80 should have ~68% pullback rate
    if summaries.get('rsi_80_all'):
        rsi_80_pullback = summaries['rsi_80_all']['pullback_rate']
        print(f"\nH2: RSI > 80 pullback rate (research claims 68%)")
        print(f"    Observed: {rsi_80_pullback:.1f}%")
        if 60 <= rsi_80_pullback <= 76:  # ±8% tolerance
            print(f"    ✅ VALIDATED: Close to research claim of 68%")
        else:
            print(f"    ⚠️ DIFFERS: {abs(rsi_80_pullback - 68):.1f}% difference from research claim")

    # Hypothesis 3: Strong trend + RSI > 80 should have LOWER pullback rate
    if summaries.get('rsi_80_weak') and summaries.get('rsi_80_strong'):
        weak_rsi80 = summaries['rsi_80_weak']['pullback_rate']
        strong_rsi80 = summaries['rsi_80_strong']['pullback_rate']

        print(f"\nH3: RSI > 80 pullback rate by trend strength")
        print(f"    Weak Trend: {weak_rsi80:.1f}% | Strong Trend: {strong_rsi80:.1f}%")
        if strong_rsi80 < weak_rsi80:
            print(f"    ✅ VALIDATED: Strong trends sustain RSI >80 longer")
        else:
            print(f"    ❌ NOT VALIDATED: Trend strength didn't reduce pullback rate")

    print(f"\n{'='*70}")

    return results, summaries


def main():
    """Main entry point"""
    # Test universe - diversified stocks
    test_tickers = [
        # Large Cap Tech
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
        # Large Cap Other
        'JPM', 'V', 'MA', 'UNH', 'JNJ', 'PG', 'HD',
        # Growth
        'CRM', 'NOW', 'SHOP', 'SQ', 'DDOG',
        # Traditional
        'WMT', 'KO', 'PEP', 'MCD', 'NKE', 'COST'
    ]

    print("\n" + "="*70)
    print("SWING TRADE ANALYZER - ADX/RSI THRESHOLD VALIDATION")
    print("Day 51: Testing Perplexity Research Findings")
    print("="*70)
    print(f"\nTest Universe: {len(test_tickers)} stocks")
    print(f"Tickers: {', '.join(test_tickers[:10])}...")

    results, summaries = run_adx_rsi_backtest(
        tickers=test_tickers,
        start_date='2020-01-01',
        end_date='2024-12-31'
    )

    if results:
        # Save detailed results
        all_signals = []
        for bucket_name, signals in results.items():
            for signal in signals:
                signal['bucket'] = bucket_name
                all_signals.append(signal)

        if all_signals:
            df = pd.DataFrame(all_signals)
            output_file = 'backtest_adx_rsi_results.csv'
            df.to_csv(output_file, index=False)
            print(f"\nDetailed results saved to: {output_file}")

    print("\n✅ Backtest complete!")


if __name__ == '__main__':
    main()
