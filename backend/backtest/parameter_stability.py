"""
Parameter Stability Analysis Script — Tier 1C (Day 69)

Tests whether key parameters are robust or fragile by running backtest at
±1 and ±2 from current value. If PF drops below 1.0 at any nearby value,
the parameter is flagged as FRAGILE.

Usage:
    python -m backtest.parameter_stability --mode quick
    python -m backtest.parameter_stability --mode full
"""

import argparse
import json
import sys
import os
import copy
import time
from datetime import datetime

# Ensure backend is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import pandas as pd
import yfinance as yf

from backtest.categorical_engine import (
    assess_technical, assess_fundamental, assess_risk_macro, determine_verdict, run_assessment
)
from backtest.trade_simulator import (
    simulate_trade, classify_market_regime, is_spy_above_200sma,
    is_spy_50sma_declining, calculate_atr_at
)


# ─── Parameter Definitions ─────────────────────────────────────────────────

PARAMETERS_TO_TEST = {
    'rs_threshold': {
        'current': 1.0,
        'values': [0.9, 0.95, 1.0, 1.05, 1.1],
        'description': 'RS 52-week threshold for Strong technical (categorical_engine line 51)',
        'patch_target': 'assess_technical',
    },
    'rsi_low': {
        'current': 50,
        'values': [45, 48, 50, 52, 55],
        'description': 'RSI lower bound for Strong technical',
        'patch_target': 'assess_technical',
    },
    'rsi_high': {
        'current': 70,
        'values': [65, 68, 70, 72, 75],
        'description': 'RSI upper bound for Strong technical',
        'patch_target': 'assess_technical',
    },
    'pattern_confidence': {
        'current': 60,
        'values': [50, 55, 60, 65, 70],
        'description': 'Minimum pattern confidence for actionable signal',
        'patch_target': 'signal_generation',
    },
    'stop_atr_multiple': {
        'current': 2.0,
        'values': [1.5, 1.75, 2.0, 2.25, 2.5],
        'description': 'ATR multiplier for stop-loss calculation',
        'patch_target': 'trade_simulator',
    },
}

# ─── Quick Test Config ──────────────────────────────────────────────────────

QUICK_TICKERS = ['AAPL', 'MSFT', 'NVDA', 'JPM', 'AMZN']
FULL_TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA', 'AMD', 'CRM', 'AVGO',
    'JPM', 'BAC', 'GS', 'MS', 'WFC', 'V', 'MA',
    'UNH', 'JNJ', 'PFE', 'ABBV', 'MRK', 'LLY',
    'HD', 'NKE', 'SBUX', 'MCD', 'TGT', 'COST',
    'XOM', 'CVX', 'COP', 'SLB',
    'CAT', 'HON', 'UPS', 'BA',
    'PG', 'KO', 'PEP', 'WMT',
    'PLTR', 'NET', 'SNOW', 'COIN', 'SQ',
    'T', 'VZ', 'CMCSA', 'DIS',
    'NEE', 'AMT', 'BRK-B', 'F', 'GM',
    'MRVL', 'ON', 'MU', 'INTC', 'QCOM',
]


def download_data(tickers, start, end):
    """Download OHLCV data for all tickers + SPY."""
    all_tickers = list(set(tickers + ['SPY']))
    print(f"Downloading data for {len(all_tickers)} tickers...")
    data = {}
    for t in all_tickers:
        try:
            df = yf.download(t, start=start, end=end, progress=False, auto_adjust=True)
            if df is not None and len(df) > 50:
                # Flatten MultiIndex columns from yfinance
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
                data[t] = df
        except Exception as e:
            print(f"  Warning: Failed to download {t}: {e}")
    print(f"  Downloaded {len(data)} tickers successfully")
    return data


def run_single_backtest(data, tickers, holding_period='standard',
                        rs_threshold=1.0, rsi_low=50, rsi_high=70,
                        pattern_confidence=60, stop_atr_multiple=2.0):
    """
    Run a simplified backtest with overridable parameters.
    Returns basic metrics: trades, wins, losses, PF, WR, avg_return.
    """
    from backtest.backtest_holistic import calculate_rs_52w
    from backtest.simfin_loader import get_fundamentals_at_date

    # Import trend template from pattern_detection
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from pattern_detection import check_trend_template

    spy_df = data.get('SPY')
    if spy_df is None:
        return None

    trades = []

    for ticker in tickers:
        if ticker == 'SPY' or ticker not in data:
            continue

        stock_df = data[ticker]
        if len(stock_df) < 260:
            continue

        try:
            # Align SPY with stock dates
            common_idx = stock_df.index.intersection(spy_df.index)
            if len(common_idx) < 260:
                continue
            spy_aligned = spy_df.loc[common_idx]
            stock_aligned = stock_df.loc[common_idx]

            # Pre-compute RS
            rs_series = calculate_rs_52w(stock_aligned['Close'], spy_aligned['Close'])

            # RSI (Wilder's EMA)
            rsi_period = 14
            delta = stock_aligned['Close'].diff()
            gain = delta.where(delta > 0, 0.0)
            loss = (-delta).where(delta < 0, 0.0)
            avg_gain = gain.ewm(alpha=1/rsi_period, min_periods=rsi_period).mean()
            avg_loss = loss.ewm(alpha=1/rsi_period, min_periods=rsi_period).mean()
            rs = avg_gain / avg_loss.replace(0, np.inf)
            rsi_series = 100 - (100 / (1 + rs))

            # Get fundamentals once (use mid-period date)
            mid_date = stock_aligned.index[len(stock_aligned) // 2].strftime('%Y-%m-%d')
            try:
                fund = get_fundamentals_at_date(ticker, mid_date)
            except Exception:
                fund = None

            # Scan every N days
            scan_interval = 5  # check every week for speed
            for i in range(260, len(stock_aligned) - 20, scan_interval):
                # Trend template on slice up to current date
                df_slice = stock_aligned.iloc[:i+1]
                tt_result = check_trend_template(df_slice)
                tt_score = tt_result['criteria_met'] if tt_result else 0
                rsi_val = rsi_series.iloc[i] if i < len(rsi_series) else 50
                rs_val = rs_series.iloc[i] if i < len(rs_series) else 1.0

                vix_val = 20  # Default VIX for stability test
                spy_above = is_spy_above_200sma(spy_aligned, i)
                spy_declining = is_spy_50sma_declining(spy_aligned, i)

                # Custom assess_technical with overridden thresholds
                pass_count = tt_score or 0
                rsi_v = rsi_val if rsi_val is not None else 50

                if pass_count >= 7 and rsi_low <= rsi_v <= rsi_high and rs_val >= rs_threshold:
                    tech_assessment = 'Strong'
                elif pass_count >= 5 and 40 <= rsi_v <= 80:
                    tech_assessment = 'Decent'
                else:
                    tech_assessment = 'Weak'

                # Standard fundamental and risk/macro assessment
                fund_assessment = assess_fundamental(
                    roe=fund.get('roe') if fund else None,
                    revenue_growth=fund.get('revenue_growth_yoy') if fund else None,
                    debt_equity=fund.get('debt_equity') if fund else None,
                    eps_growth=fund.get('eps_growth_yoy') if fund else None,
                )['assessment']

                risk_assessment = assess_risk_macro(
                    vix=vix_val,
                    spy_above_200sma=spy_above,
                    spy_50sma_declining=spy_declining,
                )['assessment']

                # Verdict using standard logic
                verdict_result = determine_verdict(
                    tech_assessment, fund_assessment, risk_assessment,
                    holding_period=holding_period, sentiment='Neutral'
                )

                if verdict_result['verdict'] != 'BUY':
                    continue

                # Simulate trade with custom stop ATR multiple
                entry_price = stock_aligned['Close'].iloc[i]

                # Custom stop with overridden ATR multiple
                lookback_start = max(0, i - 50)
                atr = calculate_atr_at(
                    stock_aligned['High'].iloc[lookback_start:i + 1],
                    stock_aligned['Low'].iloc[lookback_start:i + 1],
                    stock_aligned['Close'].iloc[lookback_start:i + 1],
                )

                if holding_period == 'quick':
                    max_hold = 5
                    target = entry_price * 1.07
                    fixed_stop = entry_price * 0.95
                    if atr is not None and atr > 0:
                        atr_stop = entry_price - (atr * stop_atr_multiple)
                        stop = max(fixed_stop, atr_stop)
                    else:
                        stop = fixed_stop
                else:  # standard
                    max_hold = 15
                    target = entry_price * 1.08
                    if atr is not None and atr > 0:
                        stop = entry_price - (atr * stop_atr_multiple)
                        stop = max(stop, entry_price * 0.90)
                        stop = min(stop, entry_price * 0.97)
                    else:
                        stop = entry_price * 0.93

                # Simulate forward
                exit_idx = min(i + max_hold, len(stock_aligned) - 1)
                for j in range(i + 1, exit_idx + 1):
                    day_low = stock_aligned['Low'].iloc[j]
                    day_high = stock_aligned['High'].iloc[j]
                    day_close = stock_aligned['Close'].iloc[j]

                    if day_low <= stop:
                        ret = (stop - entry_price) / entry_price * 100
                        trades.append(ret)
                        break
                    elif day_high >= target:
                        ret = (target - entry_price) / entry_price * 100
                        trades.append(ret)
                        break
                else:
                    # Held to max, exit at close
                    exit_price = stock_aligned['Close'].iloc[exit_idx]
                    ret = (exit_price - entry_price) / entry_price * 100
                    trades.append(ret)

        except Exception as e:
            print(f"  Warning: Error processing {ticker}: {e}")
            continue

    if not trades:
        return {
            'trades': 0, 'wins': 0, 'losses': 0,
            'win_rate': 0, 'profit_factor': 0, 'avg_return': 0,
        }

    wins = [t for t in trades if t > 0.5]
    losses = [t for t in trades if t < -0.5]
    breakevens = [t for t in trades if -0.5 <= t <= 0.5]

    gross_profit = sum(wins) if wins else 0
    gross_loss = abs(sum(losses)) if losses else 0.001

    return {
        'trades': len(trades),
        'wins': len(wins),
        'losses': len(losses),
        'breakevens': len(breakevens),
        'win_rate': round(len(wins) / len(trades) * 100, 2) if trades else 0,
        'profit_factor': round(gross_profit / gross_loss, 4) if gross_loss > 0 else 0,
        'avg_return': round(sum(trades) / len(trades), 4) if trades else 0,
    }


def run_stability_analysis(mode='quick'):
    """Run parameter stability analysis across all parameters."""
    if mode == 'quick':
        tickers = QUICK_TICKERS
        start = '2023-01-01'
        end = '2024-12-31'
    else:
        tickers = FULL_TICKERS
        start = '2020-01-01'
        end = '2025-12-31'

    print(f"\n{'='*70}")
    print(f"  PARAMETER STABILITY ANALYSIS — {mode.upper()} MODE")
    print(f"  Tickers: {len(tickers)} | Period: {start} to {end}")
    print(f"{'='*70}\n")

    data = download_data(tickers, start, end)
    if 'SPY' not in data:
        print("ERROR: Could not download SPY data. Aborting.")
        return None

    results = {}
    total_start = time.time()

    for param_name, param_config in PARAMETERS_TO_TEST.items():
        print(f"\n--- Testing: {param_name} ---")
        print(f"    {param_config['description']}")
        print(f"    Values: {param_config['values']} (current: {param_config['current']})")

        param_results = {
            'description': param_config['description'],
            'current': param_config['current'],
            'values': [],
            'metrics': [],
            'stable': True,
            'fragile_at': [],
        }

        for val in param_config['values']:
            # Build kwargs with this parameter overridden
            kwargs = {
                'rs_threshold': PARAMETERS_TO_TEST['rs_threshold']['current'],
                'rsi_low': PARAMETERS_TO_TEST['rsi_low']['current'],
                'rsi_high': PARAMETERS_TO_TEST['rsi_high']['current'],
                'pattern_confidence': PARAMETERS_TO_TEST['pattern_confidence']['current'],
                'stop_atr_multiple': PARAMETERS_TO_TEST['stop_atr_multiple']['current'],
            }
            kwargs[param_name] = val

            t0 = time.time()
            metrics = run_single_backtest(
                data, tickers, holding_period='standard', **kwargs
            )
            elapsed = time.time() - t0

            is_current = (val == param_config['current'])
            marker = " ← CURRENT" if is_current else ""

            pf = metrics['profit_factor']
            wr = metrics['win_rate']
            trades = metrics['trades']

            print(f"    {param_name}={val}: "
                  f"PF={pf:.2f}, WR={wr:.1f}%, "
                  f"Trades={trades}, "
                  f"AvgRet={metrics['avg_return']:.2f}% "
                  f"({elapsed:.1f}s){marker}")

            param_results['values'].append(val)
            param_results['metrics'].append(metrics)

            if pf < 1.0 and trades >= 3:
                param_results['stable'] = False
                param_results['fragile_at'].append(val)

        results[param_name] = param_results

    total_elapsed = time.time() - total_start

    # ─── Summary ────────────────────────────────────────────────────────────

    print(f"\n{'='*70}")
    print(f"  STABILITY SUMMARY")
    print(f"{'='*70}\n")

    stable_count = 0
    fragile_count = 0

    for param_name, r in results.items():
        status = "STABLE" if r['stable'] else "FRAGILE"
        icon = "✅" if r['stable'] else "⚠️"

        if r['stable']:
            stable_count += 1
        else:
            fragile_count += 1

        pfs = [m['profit_factor'] for m in r['metrics']]
        print(f"  {icon} {param_name}: {status}")
        print(f"     PF range: {min(pfs):.2f} – {max(pfs):.2f}")
        if not r['stable']:
            print(f"     FRAGILE at: {r['fragile_at']}")

    print(f"\n  Total: {stable_count} stable, {fragile_count} fragile")
    print(f"  Elapsed: {total_elapsed:.1f}s")

    # Save report
    report = {
        'mode': mode,
        'tickers': tickers,
        'period': f"{start} to {end}",
        'timestamp': datetime.now().isoformat(),
        'parameters': {},
        'summary': {
            'stable': stable_count,
            'fragile': fragile_count,
            'total': len(results),
        }
    }

    for param_name, r in results.items():
        report['parameters'][param_name] = {
            'description': r['description'],
            'current': r['current'],
            'values': r['values'],
            'profit_factors': [m['profit_factor'] for m in r['metrics']],
            'win_rates': [m['win_rate'] for m in r['metrics']],
            'trade_counts': [m['trades'] for m in r['metrics']],
            'avg_returns': [m['avg_return'] for m in r['metrics']],
            'stable': r['stable'],
            'fragile_at': r['fragile_at'],
        }

    report_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'validation_results',
        f'stability_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    )

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n  Report saved: {report_path}")

    return report


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Parameter Stability Analysis (Tier 1C)')
    parser.add_argument('--mode', choices=['quick', 'full'], default='quick',
                        help='quick=5 tickers/2yr, full=60 tickers/5yr')
    args = parser.parse_args()
    run_stability_analysis(args.mode)


if __name__ == '__main__':
    main()
