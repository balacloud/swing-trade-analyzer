"""
Mean-Reversion Trade Simulator

Different from momentum simulator (trade_simulator.py):
- Tighter stops (3-5% vs 7-10%)
- Time-based exit (max 10 days)
- RSI(2) > 70 exit (indicator-based, not price target)
- No trailing stops (holding period too short)
- Smaller position sizes (50% of momentum standard)

Tier 3A (Day 69): NEW file — zero impact on existing backtest code.
"""

import pandas as pd
import numpy as np
import sys
import os

# Add parent directory for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mean_reversion import calculate_rsi_short
from backtest.metrics import apply_transaction_costs  # Day 78: Fable Remediation Task 2.1


def simulate_mr_trade(stock_df, entry_idx, stop_pct=0.05, max_days=10, live_mode=False):
    """
    Simulate a mean-reversion trade.

    Exit conditions (first triggered wins):
    1. RSI(2) > 70 (mean recovered)
    2. Price hits stop (entry x (1 - stop_pct))
    3. Max holding days reached (time exit)

    Parameters
    ----------
    stock_df : pd.DataFrame
        Full OHLCV DataFrame with 'Close', 'High', 'Low', 'Volume' columns
    entry_idx : int
        Integer index of entry bar in stock_df
    stop_pct : float
        Stop loss percentage below entry (default 5%)
    max_days : int
        Maximum holding period in trading days (default 10)
    live_mode : bool
        If True, running out of price history (today's bar is the latest
        available) means the position is still open — returns a
        'status': 'open' snapshot instead of forcing a data_end exit. Lets
        the live paper-trading engine replay this same function fresh every
        day instead of maintaining a separate state machine.

    Returns
    -------
    dict
        Trade result with entry, exit, pnl, exit_reason, hold_days
    """
    if entry_idx >= len(stock_df) - 1:
        if live_mode:
            entry_date = stock_df.index[entry_idx]
            return {
                'status': 'open',
                'entry_price': round(float(stock_df['Close'].iloc[entry_idx]), 2),
                'stop_price': round(float(stock_df['Close'].iloc[entry_idx]) * (1 - stop_pct), 2),
                'entry_date': str(entry_date.date()) if hasattr(entry_date, 'date') else str(entry_date),
                'last_bar_date': str(entry_date.date()) if hasattr(entry_date, 'date') else str(entry_date),
                'days_held': 0,
            }
        return None

    entry_price = float(stock_df['Close'].iloc[entry_idx])
    stop_price = entry_price * (1 - stop_pct)

    # Calculate RSI(2) series for the full dataframe
    rsi2_series = calculate_rsi_short(stock_df['Close'], period=2)

    exit_price = None
    exit_reason = None
    exit_idx = None

    # Walk forward from entry+1
    for day in range(1, max_days + 1):
        bar_idx = entry_idx + day
        if bar_idx >= len(stock_df):
            if live_mode:
                entry_date = stock_df.index[entry_idx]
                last_bar_date = stock_df.index[-1]
                return {
                    'status': 'open',
                    'entry_price': round(entry_price, 2),
                    'stop_price': round(stop_price, 2),
                    'entry_date': str(entry_date.date()) if hasattr(entry_date, 'date') else str(entry_date),
                    'last_bar_date': str(last_bar_date.date()) if hasattr(last_bar_date, 'date') else str(last_bar_date),
                    'days_held': day - 1,
                }
            # Ran out of data — exit at last available bar
            exit_idx = len(stock_df) - 1
            exit_price = float(stock_df['Close'].iloc[exit_idx])
            exit_reason = 'data_end'
            break

        bar_low = float(stock_df['Low'].iloc[bar_idx])
        bar_close = float(stock_df['Close'].iloc[bar_idx])
        bar_open = float(stock_df['Open'].iloc[bar_idx])
        bar_rsi2 = float(rsi2_series.iloc[bar_idx])

        # Check stop first (intraday).
        # Day 78 (Fable Remediation Task 2.2): gap-aware fill. MR entries buy
        # 2-period-oversold stocks — precisely the population most prone to
        # gap-downs, so this optimism mattered most here. A gap-down that
        # opens through the stop fills at the open, not the stop price.
        if bar_open <= stop_price:
            exit_price = bar_open
            exit_idx = bar_idx
            exit_reason = 'stop_hit_gap'
            break
        if bar_low <= stop_price:
            exit_price = stop_price
            exit_idx = bar_idx
            exit_reason = 'stop_hit'
            break

        # Check RSI(2) exit (end of day)
        if bar_rsi2 > 70:
            exit_price = bar_close
            exit_idx = bar_idx
            exit_reason = 'rsi2_exit'
            break

        # Check time exit on last allowed day
        if day == max_days:
            exit_price = bar_close
            exit_idx = bar_idx
            exit_reason = 'time_exit'
            break

    if exit_price is None:
        return None

    pnl_pct = ((exit_price - entry_price) / entry_price) * 100
    hold_days = exit_idx - entry_idx

    # Day 78 (Fable Remediation Task 2.1): apply transaction costs.
    # This backtest previously reported PF 1.26 gross-of-cost — no slippage/
    # commission was modeled anywhere in the MR path. Net figures are now primary.
    costs = apply_transaction_costs(entry_price, exit_price)
    pnl_pct_net = costs['net_return_pct']

    return {
        'status': 'closed',
        'entry_price': round(entry_price, 2),
        'exit_price': round(exit_price, 2),
        'stop_price': round(stop_price, 2),
        'pnl_pct': round(pnl_pct, 2),                  # gross (legacy/reference only)
        'pnl_pct_net': round(pnl_pct_net, 4),          # net of transaction costs — primary
        'transaction_cost': costs['total_cost'],
        'pnl_r': round(pnl_pct / (stop_pct * 100), 2) if stop_pct > 0 else 0,          # gross R (legacy/reference)
        'pnl_r_net': round(pnl_pct_net / (stop_pct * 100), 4) if stop_pct > 0 else 0,  # net R-multiple — primary
        'hold_days': hold_days,
        'exit_reason': exit_reason,
        'entry_idx': entry_idx,
        'exit_idx': exit_idx,
        'win': pnl_pct_net > 0,  # Day 78: win classification is now net-of-costs (was gross)
    }


def backtest_mr_strategy(stock_df, ticker='UNKNOWN', stop_pct=0.05, max_days=10, cooldown=5):
    """
    Backtest mean-reversion strategy on a single stock.

    Entry: RSI(2) < 10 AND Price > 200 SMA AND Price > $5
    Exit: RSI(2) > 70 OR stop OR time

    Parameters
    ----------
    stock_df : pd.DataFrame
        Full OHLCV DataFrame
    ticker : str
        Ticker symbol (for labeling)
    stop_pct : float
        Stop loss percentage
    max_days : int
        Max holding period
    cooldown : int
        Minimum bars between entries to prevent overlapping trades

    Returns
    -------
    dict
        Backtest results with trades list and summary statistics
    """
    if len(stock_df) < 200:
        return {'ticker': ticker, 'trades': [], 'error': 'Insufficient data'}

    close = stock_df['Close']
    volume = stock_df['Volume']
    rsi2_series = calculate_rsi_short(close, period=2)
    sma200 = close.rolling(200).mean()
    # Day 79 (post-Phase-4 liquidity re-test): 20-day average DOLLAR volume.
    # The original entry condition had only a $5 price floor — no liquidity
    # gate at all — unlike the momentum system's $5M ADV gate. The Day 79
    # survivorship-free null result (PF 0.99, 6,151 trades) therefore
    # included thinly-traded/shell-adjacent names Connors' RSI(2) approach
    # was never validated on. This is a ONE-TIME, pre-committed liquidity
    # restriction (not a performance-chasing re-tune): price > $10 and 20d
    # avg dollar volume > $25M — a defensible "real desk could execute this"
    # bar. Do not iterate this threshold to chase a better backtest number.
    avg_dollar_vol_20 = (close * volume).rolling(20).mean()

    trades = []
    last_exit_idx = -1

    for i in range(200, len(stock_df)):
        # Cooldown check
        if i < last_exit_idx + cooldown:
            continue

        rsi2_val = float(rsi2_series.iloc[i])
        sma200_val = float(sma200.iloc[i])
        price = float(close.iloc[i])
        adv20 = float(avg_dollar_vol_20.iloc[i]) if not pd.isna(avg_dollar_vol_20.iloc[i]) else 0

        # Entry conditions (liquidity gate added Day 79 post-Phase-4 re-test)
        if rsi2_val < 10 and price > sma200_val and price > 10 and adv20 > 25_000_000:
            result = simulate_mr_trade(stock_df, i, stop_pct=stop_pct, max_days=max_days)
            if result:
                result['ticker'] = ticker
                result['entry_date'] = str(stock_df.index[i].date()) if hasattr(stock_df.index[i], 'date') else str(stock_df.index[i])
                result['exit_date'] = str(stock_df.index[result['exit_idx']].date()) if hasattr(stock_df.index[result['exit_idx']], 'date') else str(stock_df.index[result['exit_idx']])
                trades.append(result)
                last_exit_idx = result['exit_idx']

    # Summary statistics
    if not trades:
        return {
            'ticker': ticker,
            'trades': [],
            'summary': {
                'total_trades': 0,
                'win_rate': 0,
                'avg_pnl': 0,
                'avg_hold_days': 0,
            }
        }

    # Day 78 (Fable Remediation Task 2.1): net-of-cost figures are now primary.
    # 'win' is net-based (see simulate_mr_trade). Gross figures kept alongside
    # for an honest before/after delta — do not delete these when reporting.
    wins = [t for t in trades if t['win']]
    pnls_net = [t.get('pnl_pct_net', t['pnl_pct']) for t in trades]
    pnls_gross = [t['pnl_pct'] for t in trades]
    hold_days = [t['hold_days'] for t in trades]
    exit_reasons = {}
    for t in trades:
        reason = t['exit_reason']
        exit_reasons[reason] = exit_reasons.get(reason, 0) + 1

    avg_win = np.mean([t.get('pnl_pct_net', t['pnl_pct']) for t in wins]) if wins else 0
    avg_loss = np.mean([t.get('pnl_pct_net', t['pnl_pct']) for t in trades if not t['win']]) if len(trades) > len(wins) else 0

    # Profit Factor (net of costs — primary)
    gross_profit = sum(t.get('pnl_pct_net', t['pnl_pct']) for t in wins) if wins else 0
    gross_loss = abs(sum(t.get('pnl_pct_net', t['pnl_pct']) for t in trades if not t['win'])) if len(trades) > len(wins) else 0
    profit_factor = gross_profit / gross_loss if gross_loss > 0 else float('inf') if gross_profit > 0 else 0

    # Gross-of-cost comparison figures (pre-remediation methodology)
    wins_gross = [t for t in trades if t['pnl_pct'] > 0]
    gp_gross = sum(t['pnl_pct'] for t in wins_gross) if wins_gross else 0
    gl_gross = abs(sum(t['pnl_pct'] for t in trades if t['pnl_pct'] <= 0))
    profit_factor_gross = gp_gross / gl_gross if gl_gross > 0 else float('inf') if gp_gross > 0 else 0

    return {
        'ticker': ticker,
        'trades': trades,
        'summary': {
            'total_trades': len(trades),
            'wins': len(wins),
            'losses': len(trades) - len(wins),
            'win_rate': round(len(wins) / len(trades) * 100, 1),
            'win_rate_gross': round(len(wins_gross) / len(trades) * 100, 1),
            'avg_pnl': round(np.mean(pnls_net), 2),
            'avg_pnl_gross': round(np.mean(pnls_gross), 2),
            'avg_win': round(avg_win, 2),
            'avg_loss': round(avg_loss, 2),
            'avg_hold_days': round(np.mean(hold_days), 1),
            'profit_factor': round(profit_factor, 2) if profit_factor != float('inf') else 'inf',
            'profit_factor_gross': round(profit_factor_gross, 2) if profit_factor_gross != float('inf') else 'inf',
            'exit_reasons': exit_reasons,
            'total_pnl': round(sum(pnls_net), 2),
            'total_pnl_gross': round(sum(pnls_gross), 2),
        }
    }
