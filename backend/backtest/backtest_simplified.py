"""
Backtest Simplified Binary System
=================================
Day 27: Testing the research-backed minimalist approach

Hypothesis: Stocks meeting ALL 4 binary criteria achieve better results
than the 75-point scoring system.

4 Binary Criteria (ALL must be YES):
1. TREND: Price > 50 SMA > 200 SMA
2. MOMENTUM: RS > 1.0 (outperforming SPY)
3. SETUP: Stop within 7% of entry
4. RISK: R:R >= 2:1

Trade Parameters:
- Entry: Close price on signal day
- Target: +10%
- Stop: -7%
- Max Hold: 60 trading days

Usage:
    python backtest_simplified.py
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


def find_support_level(prices, lookback=60):
    """
    Find nearest support level from recent swing lows
    Simple approach: lowest low in lookback period
    """
    if len(prices) < lookback:
        return None
    recent_prices = prices[-lookback:]
    return recent_prices.min()


def check_simplified_criteria(stock_df, spy_df, date_idx, target_pct=0.10, stop_pct=0.07):
    """
    Check if all 4 binary criteria are met
    Returns: (all_pass, criteria_details)
    """
    if date_idx < 252:  # Need 1 year of data
        return False, {}

    # Get data up to signal date
    stock_prices = stock_df['Close'].iloc[:date_idx+1]
    spy_prices = spy_df['Close'].iloc[:date_idx+1]
    current_price = stock_prices.iloc[-1]

    criteria = {
        'trend': False,
        'momentum': False,
        'setup': False,
        'risk': False
    }

    # 1. TREND: Price > 50 SMA > 200 SMA
    sma50 = calculate_sma(stock_prices, 50)
    sma200 = calculate_sma(stock_prices, 200)

    if sma50 and sma200:
        criteria['trend'] = (current_price > sma50) and (sma50 > sma200)

    # 2. MOMENTUM: RS > 1.0
    if len(stock_prices) >= 252 and len(spy_prices) >= 252:
        stock_return = (stock_prices.iloc[-1] / stock_prices.iloc[-252]) - 1
        spy_return = (spy_prices.iloc[-1] / spy_prices.iloc[-252]) - 1

        if spy_return != 0:
            rs_ratio = (1 + stock_return) / (1 + spy_return)
            criteria['momentum'] = rs_ratio >= 1.0

    # 3. SETUP: Can set stop within 7%
    support = find_support_level(stock_prices)
    if support:
        stop_distance = (current_price - support) / current_price
        criteria['setup'] = 0 < stop_distance <= stop_pct

    # 4. RISK: R:R >= 2:1
    if criteria['setup'] and support:
        stop_price = support
        risk = current_price - stop_price
        target_price = current_price * (1 + target_pct)
        reward = target_price - current_price

        if risk > 0:
            rr_ratio = reward / risk
            criteria['risk'] = rr_ratio >= 2.0

    all_pass = all(criteria.values())
    return all_pass, criteria


def simulate_trade(stock_df, entry_idx, target_pct=0.10, stop_pct=0.07, max_hold=60):
    """
    Simulate a single trade from entry date
    """
    entry_price = stock_df['Close'].iloc[entry_idx]
    target_price = entry_price * (1 + target_pct)
    stop_price = entry_price * (1 - stop_pct)

    for days in range(1, max_hold + 1):
        check_idx = entry_idx + days

        if check_idx >= len(stock_df):
            return 'EXPIRED', stock_df['Close'].iloc[-1], days - 1, \
                   (stock_df['Close'].iloc[-1] / entry_price - 1) * 100

        high = stock_df['High'].iloc[check_idx]
        low = stock_df['Low'].iloc[check_idx]

        # Check stop loss first
        if low <= stop_price:
            return 'LOSS', stop_price, days, -stop_pct * 100

        # Check target
        if high >= target_price:
            return 'WIN', target_price, days, target_pct * 100

    # Max hold reached
    final_price = stock_df['Close'].iloc[entry_idx + max_hold]
    return_pct = (final_price / entry_price - 1) * 100

    if return_pct > 0:
        return 'EXPIRED_PROFIT', final_price, max_hold, return_pct
    else:
        return 'EXPIRED_LOSS', final_price, max_hold, return_pct


def run_backtest(tickers, start_date='2020-01-01', end_date='2024-12-31',
                 target_pct=0.10, stop_pct=0.07, max_hold=60):
    """
    Run backtest on simplified binary system
    """
    print(f"\n{'='*60}")
    print("BACKTEST: Simplified Binary System (4 Criteria)")
    print(f"{'='*60}")
    print(f"Period: {start_date} to {end_date}")
    print(f"Entry: ALL 4 criteria must be YES")
    print(f"Target: +{target_pct*100:.0f}%")
    print(f"Stop Loss: -{stop_pct*100:.0f}%")
    print(f"Max Hold: {max_hold} days")
    print(f"{'='*60}\n")

    # Download SPY data
    print("Downloading SPY data...")
    spy_df = yf.download('SPY', start=start_date, end=end_date, progress=False)
    if spy_df.empty:
        print("ERROR: Could not download SPY data")
        return None, None

    if isinstance(spy_df.columns, pd.MultiIndex):
        spy_df.columns = spy_df.columns.get_level_values(0)

    print(f"SPY data: {len(spy_df)} days\n")

    all_trades = []

    for ticker in tickers:
        print(f"\nProcessing {ticker}...")

        try:
            buffer_start = (datetime.strptime(start_date, '%Y-%m-%d') -
                          timedelta(days=400)).strftime('%Y-%m-%d')

            stock_df = yf.download(ticker, start=buffer_start, end=end_date, progress=False)

            if stock_df.empty:
                print(f"  No data for {ticker}")
                continue

            if isinstance(stock_df.columns, pd.MultiIndex):
                stock_df.columns = stock_df.columns.get_level_values(0)

            common_dates = stock_df.index.intersection(spy_df.index)
            stock_df = stock_df.loc[common_dates]
            spy_aligned = spy_df.loc[common_dates]

            print(f"  Data: {len(stock_df)} days")

            signal_count = 0
            cooldown = 0

            for i in range(252, len(stock_df) - max_hold):
                if cooldown > 0:
                    cooldown -= 1
                    continue

                date = stock_df.index[i]

                if date < pd.Timestamp(start_date):
                    continue

                # Check simplified criteria
                all_pass, criteria = check_simplified_criteria(
                    stock_df, spy_aligned, i, target_pct, stop_pct
                )

                if all_pass:
                    # All 4 criteria met - take the trade
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
                        'trend': criteria['trend'],
                        'momentum': criteria['momentum'],
                        'setup': criteria['setup'],
                        'risk': criteria['risk']
                    }

                    all_trades.append(trade)
                    signal_count += 1
                    cooldown = days_held + 5

            print(f"  Signals: {signal_count}")

        except Exception as e:
            print(f"  Error: {str(e)}")
            continue

    if not all_trades:
        print("\nNo trades generated!")
        return None, None

    results_df = pd.DataFrame(all_trades)

    # Calculate statistics
    total_trades = len(results_df)
    wins = len(results_df[results_df['result'] == 'WIN'])
    losses = len(results_df[results_df['result'] == 'LOSS'])
    expired_profit = len(results_df[results_df['result'] == 'EXPIRED_PROFIT'])
    expired_loss = len(results_df[results_df['result'] == 'EXPIRED_LOSS'])

    win_rate = (wins + expired_profit) / total_trades * 100 if total_trades > 0 else 0

    avg_return = results_df['return_pct'].mean()
    avg_win = results_df[results_df['return_pct'] > 0]['return_pct'].mean() if wins > 0 else 0
    avg_loss = results_df[results_df['return_pct'] < 0]['return_pct'].mean() if losses > 0 else 0

    avg_days = results_df['days_held'].mean()

    gross_profits = results_df[results_df['return_pct'] > 0]['return_pct'].sum()
    gross_losses = abs(results_df[results_df['return_pct'] < 0]['return_pct'].sum())
    profit_factor = gross_profits / gross_losses if gross_losses > 0 else float('inf')

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
        'avg_days': avg_days,
        'profit_factor': profit_factor,
        'expectancy': expectancy
    }

    # Print results
    print(f"\n{'='*60}")
    print("SIMPLIFIED SYSTEM RESULTS")
    print(f"{'='*60}")
    print(f"Total Trades: {total_trades}")
    print(f"  - Wins (+{target_pct*100:.0f}%): {wins}")
    print(f"  - Losses (-{stop_pct*100:.0f}%): {losses}")
    print(f"  - Expired Profit: {expired_profit}")
    print(f"  - Expired Loss: {expired_loss}")
    print(f"\nWin Rate: {win_rate:.1f}%")
    print(f"Average Return: {avg_return:.2f}%")
    print(f"Average Win: +{avg_win:.2f}%")
    print(f"Average Loss: {avg_loss:.2f}%")
    print(f"Average Days: {avg_days:.1f}")
    print(f"\nProfit Factor: {profit_factor:.2f}")
    print(f"Expectancy: {expectancy:.2f}%")
    print(f"{'='*60}")

    return results_df, summary


def main():
    """Main entry point"""

    test_tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
        'JPM', 'V', 'MA', 'UNH', 'JNJ', 'PG', 'HD', 'DIS',
        'CRM', 'NOW', 'SHOP', 'ROKU', 'DDOG', 'ZM',
        'WMT', 'KO', 'PEP', 'MCD', 'NKE', 'COST'
    ]

    print("\n" + "="*60)
    print("SWING TRADE ANALYZER - SIMPLIFIED SYSTEM BACKTEST")
    print("Day 27: Testing Research-Backed Binary Approach")
    print("="*60)
    print(f"\nTest Universe: {len(test_tickers)} stocks")

    results_df, summary = run_backtest(
        tickers=test_tickers,
        start_date='2020-01-01',
        end_date='2024-12-31',
        target_pct=0.10,
        stop_pct=0.07,
        max_hold=60
    )

    if results_df is not None:
        results_df.to_csv('backtest_simplified_results.csv', index=False)
        print(f"\nResults saved to: backtest_simplified_results.csv")

        # Compare with original system
        print(f"\n{'='*60}")
        print("COMPARISON: Simplified vs Original 75-Point System")
        print(f"{'='*60}")
        print(f"{'Metric':<25} {'Simplified':>15} {'Original':>15}")
        print("-" * 55)
        print(f"{'Total Trades':<25} {summary['total_trades']:>15} {310:>15}")
        print(f"{'Win Rate':<25} {summary['win_rate']:>14.1f}% {49.7:>14.1f}%")
        print(f"{'Avg Return':<25} {summary['avg_return']:>14.2f}% {1.30:>14.2f}%")
        print(f"{'Profit Factor':<25} {summary['profit_factor']:>15.2f} {1.40:>15.2f}")
        print(f"{'Expectancy':<25} {summary['expectancy']:>14.2f}% {1.30:>14.2f}%")
        print(f"{'='*60}")


if __name__ == '__main__':
    main()
