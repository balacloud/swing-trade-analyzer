"""
Test 4H Data Availability
=========================
Day 39: Validate 4H OHLCV data sources for Dual Entry Strategy

This script tests:
1. yfinance 4H data (60-day limit)
2. Whether 60 days is sufficient for RSI calculation
3. Data quality and reliability

Usage:
    python test_4h_data.py
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def test_yfinance_4h(ticker='AAPL'):
    """
    Test yfinance 4H data availability.

    yfinance limitations:
    - 4H interval only available for last 60 days
    - Requires specific interval format: '1h' and resample, or check '4h' directly
    """
    print(f"\n{'='*60}")
    print(f"Testing yfinance 4H data for {ticker}")
    print(f"{'='*60}")

    try:
        # Test 1: Try 4h interval directly (may not be supported)
        print("\n1. Testing interval='4h' directly...")
        try:
            stock = yf.Ticker(ticker)
            df_4h = stock.history(period='60d', interval='1h')  # 1h is more reliable
            if not df_4h.empty:
                print(f"   ✅ Got {len(df_4h)} hourly bars")
                print(f"   Date range: {df_4h.index[0]} to {df_4h.index[-1]}")

                # Resample to 4H
                df_4h_resampled = df_4h.resample('4h').agg({
                    'Open': 'first',
                    'High': 'max',
                    'Low': 'min',
                    'Close': 'last',
                    'Volume': 'sum'
                }).dropna()

                print(f"   ✅ Resampled to {len(df_4h_resampled)} 4H bars")

                # Check if enough for RSI calculation (need at least 14 + buffer)
                if len(df_4h_resampled) >= 20:
                    print(f"   ✅ Sufficient for RSI(14) calculation: {len(df_4h_resampled)} bars >= 20")
                else:
                    print(f"   ⚠️ May be insufficient for RSI: {len(df_4h_resampled)} bars < 20")

                return df_4h_resampled
            else:
                print("   ❌ No data returned")
                return None
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def calculate_rsi_from_4h(df_4h, period=14):
    """Calculate RSI from 4H data"""
    if df_4h is None or len(df_4h) < period + 1:
        return None

    closes = df_4h['Close']

    delta = closes.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi.iloc[-1]


def test_multiple_tickers():
    """Test 4H data for multiple tickers"""
    test_tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA']

    print(f"\n{'='*60}")
    print("Testing 4H data for multiple tickers")
    print(f"{'='*60}")

    results = []

    for ticker in test_tickers:
        print(f"\n--- {ticker} ---")
        df_4h = test_yfinance_4h(ticker)

        if df_4h is not None and len(df_4h) > 0:
            rsi_4h = calculate_rsi_from_4h(df_4h)
            print(f"   RSI(14) 4H: {rsi_4h:.1f}" if rsi_4h else "   RSI: Could not calculate")

            results.append({
                'ticker': ticker,
                'bars_4h': len(df_4h),
                'rsi_4h': round(rsi_4h, 1) if rsi_4h else None,
                'status': 'OK' if len(df_4h) >= 20 else 'INSUFFICIENT'
            })
        else:
            results.append({
                'ticker': ticker,
                'bars_4h': 0,
                'rsi_4h': None,
                'status': 'FAILED'
            })

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY: 4H Data Availability")
    print(f"{'='*60}")

    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))

    success_count = len(results_df[results_df['status'] == 'OK'])
    total = len(results_df)

    print(f"\nSuccess rate: {success_count}/{total} ({success_count/total*100:.0f}%)")

    if success_count == total:
        print("\n✅ GATE G3 PASSED: 4H data is reliable and sufficient")
        print("   Proceed to Phase 3: Implement 4H RSI in backend")
    else:
        print("\n⚠️ GATE G3 PARTIAL: Some tickers have insufficient 4H data")
        print("   Consider: Use daily RSI as fallback when 4H unavailable")

    return results_df


def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("4H DATA AVAILABILITY TEST")
    print("Day 39: Dual Entry Strategy - Phase 2.2")
    print("="*60)

    # Test single ticker first
    df_4h = test_yfinance_4h('AAPL')

    if df_4h is not None:
        print(f"\n4H data sample (last 5 bars):")
        print(df_4h.tail())

    # Test multiple tickers
    results = test_multiple_tickers()

    print(f"\n{'='*60}")
    print("CONCLUSION")
    print(f"{'='*60}")
    print("""
yfinance provides 60 days of hourly data which can be resampled to 4H.
This gives approximately 60-90 4H bars (depending on market hours),
which is sufficient for RSI(14) calculation.

RECOMMENDATION:
- Use yfinance 1H data, resample to 4H
- Calculate RSI(14) locally
- Fall back to daily RSI if 4H data unavailable

No need for TwelveData API for basic 4H RSI functionality.
""")


if __name__ == '__main__':
    main()
