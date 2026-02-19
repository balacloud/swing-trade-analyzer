"""
v4.16 Holistic 3-Layer Backtest Runner

Tests whether the categorical assessment system (built Days 28-54) adds
genuine edge over the Day 27 baseline (49.7% win rate = random).

Three entry configurations (layered testing):
  Config A: Categorical verdict = BUY (assessment only)
  Config B: Config A + pattern >= 60% confidence (at_pivot/broken_out)
  Config C: Config B + trade viable + R:R >= 1.2

Running all 3 shows which layer contributes edge.

Usage:
  python backtest_holistic.py --quick-test          # 5 tickers, 1 year
  python backtest_holistic.py                       # Full 60 tickers, 5 years
  python backtest_holistic.py --walk-forward        # With walk-forward validation
  python backtest_holistic.py --configs A B --periods standard
"""

import os
import sys
import json
import time
import argparse
import warnings
from datetime import datetime, timedelta
from collections import defaultdict

import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import yfinance as yf

from backtest.categorical_engine import run_assessment
from backtest.trade_simulator import (
    simulate_trade, classify_market_regime, is_spy_above_200sma,
    is_spy_50sma_declining, calculate_atr_at, calculate_atr_series
)
from backtest.metrics import compute_metrics, apply_transaction_costs
from backtest.simfin_loader import get_fundamentals_at_date

# These are in the parent backend/ directory
from pattern_detection import check_trend_template, detect_patterns
from support_resistance import compute_sr_levels


# ─── Ticker Universe ─────────────────────────────────────────────────────────

BACKTEST_TICKERS = [
    # Large Cap Tech (7)
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
    # Finance (5)
    'JPM', 'V', 'MA', 'GS', 'BAC',
    # Healthcare (4)
    'UNH', 'JNJ', 'LLY', 'ABBV',
    # Consumer (6)
    'PG', 'HD', 'WMT', 'KO', 'PEP', 'MCD',
    # Industrial (4)
    'CAT', 'HON', 'UPS', 'DE',
    # Energy (3)
    'XOM', 'CVX', 'COP',
    # Growth Tech (8)
    'CRM', 'NOW', 'SHOP', 'SQ', 'DDOG', 'PANW', 'CRWD', 'SNOW',
    # Growth Other (6)
    'COST', 'NKE', 'LULU', 'CMG', 'ABNB', 'UBER',
    # Volatile (4)
    'ROKU', 'COIN', 'AFRM', 'PLTR',
    # Semiconductors (5)
    'AMD', 'AVGO', 'MU', 'MRVL', 'ON',
    # Telecom/Utilities (4)
    'T', 'VZ', 'NEE', 'AMT',
    # Value (4)
    'BRK-B', 'DIS', 'F', 'GM',
]

QUICK_TEST_TICKERS = ['AAPL', 'NVDA', 'JPM', 'XOM', 'PLTR']

# Pattern actionability threshold (lowered from 80 to 60 per Perplexity research)
PATTERN_CONFIDENCE_THRESHOLD = 60

# Cooldown between entries for same ticker (trading days)
# Dynamic: 5 days after target hit (winning exit), 10 days after stop hit (losing exit)
ENTRY_COOLDOWN_AFTER_WIN = 5
ENTRY_COOLDOWN_AFTER_LOSS = 10

# Warmup period (need 252 days for trend template + RS calculation)
WARMUP_BARS = 260


# ─── Indicator Calculations ──────────────────────────────────────────────────

def calculate_rsi(prices, period=14):
    """RSI using Wilder's smoothing."""
    if len(prices) < period + 1:
        return None
    deltas = prices.diff()
    gains = deltas.where(deltas > 0, 0)
    losses_s = -deltas.where(deltas < 0, 0)
    avg_gain = gains.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = losses_s.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_adx(high, low, close, period=14):
    """ADX calculation — returns Series."""
    if len(close) < period * 2:
        return None
    tr1 = high - low
    tr2 = (high - close.shift(1)).abs()
    tr3 = (low - close.shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    plus_dm = high.diff()
    minus_dm = -low.diff()
    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0)

    atr = tr.ewm(alpha=1 / period, min_periods=period).mean()
    plus_di = 100 * (plus_dm.ewm(alpha=1 / period, min_periods=period).mean() / atr)
    minus_di = 100 * (minus_dm.ewm(alpha=1 / period, min_periods=period).mean() / atr)

    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di)
    adx = dx.ewm(alpha=1 / period, min_periods=period).mean()
    return adx


def calculate_rs_52w(stock_close, spy_close):
    """52-week relative strength vs SPY at each bar."""
    if len(stock_close) < 252 or len(spy_close) < 252:
        return None
    stock_ret = stock_close / stock_close.shift(252) - 1
    spy_ret = spy_close / spy_close.shift(252) - 1
    rs = (1 + stock_ret) / (1 + spy_ret)
    return rs


# ─── Data Loading ────────────────────────────────────────────────────────────

def download_data(ticker, start_date, end_date, buffer_days=400):
    """Download OHLCV data with buffer for warmup indicators."""
    buffer_start = (datetime.strptime(start_date, '%Y-%m-%d')
                    - timedelta(days=buffer_days)).strftime('%Y-%m-%d')
    try:
        df = yf.download(ticker, start=buffer_start, end=end_date, progress=False)
        if df.empty:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df
    except Exception as e:
        print(f"    ERROR downloading {ticker}: {e}")
        return None


def get_vix_at_date(vix_df, date_idx):
    """Get VIX value at a specific index."""
    if vix_df is None or date_idx >= len(vix_df):
        return None
    return vix_df['Close'].iloc[date_idx]


# ─── Signal Detection ────────────────────────────────────────────────────────

def check_entry_signals(stock_df, spy_df, vix_df, date_idx,
                        rsi_series, adx_series, rs_series,
                        holding_period, ticker, fundamentals_cache):
    """
    Check all entry signals at a specific date for all configs.

    Returns dict with:
      config_a: bool (categorical BUY)
      config_b: bool (A + pattern >= 80%)
      config_c: bool (B + viable + R:R >= 1.5)
      assessment: full assessment result
      patterns: pattern detection result
      sr_levels: support/resistance levels
      trade_meta: extra info for trade record
    """
    result = {
        'config_a': False,
        'config_b': False,
        'config_c': False,
        'assessment': None,
        'patterns': None,
        'sr_levels': None,
        'trade_meta': {},
    }

    # Slice dataframe up to current date (no future data)
    df_slice = stock_df.iloc[:date_idx + 1].copy()

    if len(df_slice) < WARMUP_BARS:
        return result

    # Get indicators at current bar
    rsi_val = rsi_series.iloc[date_idx] if rsi_series is not None and date_idx < len(rsi_series) else None
    adx_val = adx_series.iloc[date_idx] if adx_series is not None and date_idx < len(adx_series) else None
    rs_val = rs_series.iloc[date_idx] if rs_series is not None and date_idx < len(rs_series) else None

    if rsi_val is None or pd.isna(rsi_val):
        return result
    if adx_val is None or pd.isna(adx_val):
        return result

    rs_val = rs_val if (rs_val is not None and not pd.isna(rs_val)) else 1.0

    # VIX and SPY regime
    vix_val = get_vix_at_date(vix_df, date_idx) if vix_df is not None else None
    spy_above = is_spy_above_200sma(spy_df, date_idx) if spy_df is not None else True
    spy_declining = is_spy_50sma_declining(spy_df, date_idx) if spy_df is not None else False

    # Trend template (using the slice up to current date)
    trend = check_trend_template(df_slice)
    if trend is None:
        return result

    tt_score = trend.get('criteria_met', 0)

    # Get fundamentals (point-in-time from SimFin)
    trade_date = str(stock_df.index[date_idx].date())
    fund = fundamentals_cache.get(ticker, {}).get(trade_date)

    # If not cached, try to load
    if fund is None:
        try:
            fund = get_fundamentals_at_date(ticker, trade_date)
            if ticker not in fundamentals_cache:
                fundamentals_cache[ticker] = {}
            fundamentals_cache[ticker][trade_date] = fund
        except Exception:
            fund = None

    roe = fund['roe'] if fund else None
    rev_growth = fund['revenue_growth_yoy'] if fund else None
    de_ratio = fund['debt_equity'] if fund else None
    eps_growth = fund['eps_growth_yoy'] if fund else None

    # Run categorical assessment
    assessment = run_assessment(
        trend_template_score=tt_score,
        rsi=rsi_val,
        rs_52w=rs_val,
        adx=adx_val,
        vix=vix_val,
        spy_above_200sma=spy_above,
        spy_50sma_declining=spy_declining,
        roe=roe,
        revenue_growth=rev_growth,
        debt_equity=de_ratio,
        eps_growth=eps_growth,
        holding_period=holding_period,
    )

    result['assessment'] = assessment

    verdict = assessment['verdict']['verdict']

    # Store metadata
    result['trade_meta'] = {
        'tt_score': tt_score,
        'rsi': round(rsi_val, 1),
        'adx': round(adx_val, 1),
        'rs_52w': round(rs_val, 3),
        'vix': round(vix_val, 1) if vix_val else None,
        'spy_above_200sma': spy_above,
        'roe': roe,
        'revenue_growth': rev_growth,
        'debt_equity': de_ratio,
        'eps_growth': eps_growth,
        'fundamental_available': fund is not None,
        'tech_assessment': assessment['technical']['assessment'],
        'fund_assessment': assessment['fundamental']['assessment'],
        'risk_assessment': assessment['risk_macro']['assessment'],
    }

    # CONFIG A: Categorical verdict = BUY + ADX >= 20
    if verdict == 'BUY' and adx_val >= 20:
        result['config_a'] = True

    # CONFIG B: A + actionable pattern
    if result['config_a']:
        patterns = detect_patterns(df_slice)
        result['patterns'] = patterns

        has_actionable_pattern = False
        if patterns and patterns.get('patterns'):
            for pname in ['vcp', 'cup_handle', 'flat_base']:
                p = patterns['patterns'].get(pname, {})
                if (p.get('detected') and
                        p.get('confidence', 0) >= PATTERN_CONFIDENCE_THRESHOLD and
                        p.get('status') in ('at_pivot', 'broken_out', 'complete', 'forming')):
                    has_actionable_pattern = True
                    result['trade_meta']['pattern'] = pname
                    result['trade_meta']['pattern_confidence'] = p.get('confidence')
                    result['trade_meta']['pattern_status'] = p.get('status')
                    break

        if has_actionable_pattern:
            result['config_b'] = True

    # CONFIG C: B + trade viable + R:R >= 1.2
    if result['config_b']:
        try:
            # compute_sr_levels expects lowercase columns
            df_lower = df_slice.rename(columns={
                'Open': 'open', 'High': 'high', 'Low': 'low',
                'Close': 'close', 'Volume': 'volume',
            })
            sr_levels = compute_sr_levels(df_lower)
            result['sr_levels'] = sr_levels

            viability = sr_levels.meta.get('trade_viability', {}) if sr_levels and sr_levels.meta else {}
            # Accept YES, True, or CAUTION (projected support is still tradeable)
            is_viable = viability.get('viable') in ('YES', True, 'CAUTION')

            # Calculate R:R from S&R levels
            # support sorted ascending → max() = nearest to price
            # resistance sorted ascending → min() = nearest to price
            current_price = df_slice['Close'].iloc[-1]
            nearest_support = max(sr_levels.support) if sr_levels and sr_levels.support else None
            nearest_resistance = min(sr_levels.resistance) if sr_levels and sr_levels.resistance else None

            rr_ratio = 0
            if (nearest_support and nearest_resistance
                    and nearest_support < current_price < nearest_resistance):
                risk = current_price - nearest_support
                reward = nearest_resistance - current_price
                if risk > 0:
                    rr_ratio = reward / risk

            # Fallback: if no S&R found, use ATR-based R:R estimate
            if rr_ratio == 0 and is_viable:
                lookback_start = max(0, date_idx - 50)
                atr_val = calculate_atr_at(
                    stock_df['High'].iloc[lookback_start:date_idx + 1],
                    stock_df['Low'].iloc[lookback_start:date_idx + 1],
                    stock_df['Close'].iloc[lookback_start:date_idx + 1],
                )
                if atr_val and atr_val > 0:
                    rr_ratio = 1.5  # Conservative default when S&R unavailable

            result['trade_meta']['viable'] = is_viable
            result['trade_meta']['rr_ratio'] = round(rr_ratio, 2)
            result['trade_meta']['nearest_support'] = nearest_support
            result['trade_meta']['nearest_resistance'] = nearest_resistance

            if is_viable and rr_ratio >= 1.2:
                result['config_c'] = True

        except Exception:
            pass  # S&R computation can fail for some data shapes

    return result


# ─── Main Backtest Loop ──────────────────────────────────────────────────────

def run_holistic_backtest(tickers, start='2020-01-01', end='2025-12-31',
                          holding_periods=None, configs=None,
                          scan_interval=1, verbose=True):
    """
    Main backtest runner.

    Args:
        tickers: list of ticker symbols
        start: backtest start date
        end: backtest end date
        holding_periods: list of 'quick', 'standard', 'position'
        configs: list of 'A', 'B', 'C'
        scan_interval: check signals every N trading days (reduces computation)
        verbose: print progress

    Returns:
        dict with trades, metrics, and report data
    """
    if holding_periods is None:
        holding_periods = ['standard']
    if configs is None:
        configs = ['A', 'B', 'C']

    start_time = time.time()

    if verbose:
        print(f"\n{'=' * 70}")
        print(f"  v4.16 HOLISTIC 3-LAYER BACKTEST")
        print(f"{'=' * 70}")
        print(f"  Period:    {start} to {end}")
        print(f"  Tickers:   {len(tickers)}")
        print(f"  Configs:   {', '.join(configs)}")
        print(f"  Periods:   {', '.join(holding_periods)}")
        print(f"  Scan Every: {scan_interval} trading days")
        print(f"{'=' * 70}\n")

    # 1. Download SPY + VIX data
    if verbose:
        print("Downloading SPY and VIX data...")

    spy_df = download_data('SPY', start, end)
    vix_df = download_data('^VIX', start, end)

    if spy_df is None or spy_df.empty:
        print("ERROR: Could not download SPY data. Aborting.")
        return None

    # 2. Pre-compute SPY indicators
    spy_rsi = calculate_rsi(spy_df['Close'])
    spy_sma200 = spy_df['Close'].rolling(200).mean()

    # Track all trades per config × holding period
    all_trades = defaultdict(list)  # key: (config, holding_period)
    fundamentals_cache = {}  # Avoid re-fetching
    tickers_processed = 0
    tickers_with_trades = 0

    # 3. Process each ticker
    for ticker_num, ticker in enumerate(tickers, 1):
        if verbose:
            print(f"\n[{ticker_num}/{len(tickers)}] Processing {ticker}...")

        stock_df = download_data(ticker, start, end)
        if stock_df is None or stock_df.empty:
            if verbose:
                print(f"  Skipped: no data")
            continue

        # Align to SPY dates
        common_dates = stock_df.index.intersection(spy_df.index)
        if len(common_dates) < WARMUP_BARS:
            if verbose:
                print(f"  Skipped: only {len(common_dates)} common dates (need {WARMUP_BARS})")
            continue

        stock_df = stock_df.loc[common_dates]
        spy_aligned = spy_df.loc[common_dates]
        vix_aligned = vix_df.loc[common_dates] if vix_df is not None else None

        tickers_processed += 1

        # Pre-compute indicators for this ticker
        rsi_series = calculate_rsi(stock_df['Close'])
        adx_series = calculate_adx(stock_df['High'], stock_df['Low'], stock_df['Close'])
        rs_series = calculate_rs_52w(stock_df['Close'], spy_aligned['Close'])

        # Find the actual start index (after warmup, within start date)
        start_ts = pd.Timestamp(start)
        start_idx = WARMUP_BARS
        for i in range(WARMUP_BARS, len(stock_df)):
            if stock_df.index[i] >= start_ts:
                start_idx = i
                break

        ticker_trade_count = 0

        # Track cooldown per config × holding period
        cooldowns = defaultdict(int)  # key: (config, period) → remaining cooldown

        # Scan through trading days
        for i in range(start_idx, len(stock_df), scan_interval):
            for hp in holding_periods:
                # Check each config
                for config in configs:
                    cd_key = (config, hp)
                    if cooldowns[cd_key] > 0:
                        cooldowns[cd_key] -= scan_interval
                        continue

                    # Check entry signals
                    signals = check_entry_signals(
                        stock_df, spy_aligned, vix_aligned, i,
                        rsi_series, adx_series, rs_series,
                        hp, ticker, fundamentals_cache
                    )

                    # Determine if this config fires
                    config_key = f"config_{config.lower()}"
                    if not signals.get(config_key, False):
                        continue

                    # Determine max hold days for sufficient forward data
                    max_hold_map = {'quick': 5, 'standard': 15, 'position': 45}
                    max_hold = max_hold_map.get(hp, 15)

                    if i + max_hold >= len(stock_df):
                        continue  # Not enough forward data

                    # TRADE ENTRY
                    trade_result = simulate_trade(stock_df, i, hp)

                    # Apply transaction costs
                    costs = apply_transaction_costs(
                        trade_result['entry_price'],
                        trade_result['exit_price']
                    )
                    trade_result['return_pct_net'] = costs['net_return_pct']
                    trade_result['transaction_cost'] = costs['total_cost']

                    # Classify market regime at entry
                    vix_val = get_vix_at_date(vix_aligned, i) if vix_aligned is not None else None
                    trade_result['regime'] = classify_market_regime(spy_aligned, vix_val, i)

                    # Add metadata
                    trade_result['ticker'] = ticker
                    trade_result['config'] = config
                    trade_result['holding_period'] = hp
                    trade_result.update(signals.get('trade_meta', {}))

                    all_trades[(config, hp)].append(trade_result)
                    ticker_trade_count += 1

                    # Dynamic cooldown: shorter after wins, longer after losses
                    if trade_result.get('exit_reason') in ('target_hit',):
                        cooldowns[cd_key] = ENTRY_COOLDOWN_AFTER_WIN
                    else:
                        cooldowns[cd_key] = ENTRY_COOLDOWN_AFTER_LOSS

        if ticker_trade_count > 0:
            tickers_with_trades += 1
            if verbose:
                print(f"  {ticker_trade_count} trades generated")

    # 4. Compute metrics for each config × holding period
    elapsed = time.time() - start_time

    if verbose:
        print(f"\n{'=' * 70}")
        print(f"  COMPUTING METRICS")
        print(f"{'=' * 70}")

    results = {
        'meta': {
            'start_date': start,
            'end_date': end,
            'tickers': tickers,
            'tickers_processed': tickers_processed,
            'tickers_with_trades': tickers_with_trades,
            'configs': configs,
            'holding_periods': holding_periods,
            'scan_interval': scan_interval,
            'elapsed_seconds': round(elapsed, 1),
            'timestamp': datetime.now().isoformat(),
        },
        'results': {},
        'all_trades': {},
    }

    for config in configs:
        for hp in holding_periods:
            key = f"{config}_{hp}"
            trades = all_trades.get((config, hp), [])
            metrics = compute_metrics(trades)

            results['results'][key] = metrics
            results['all_trades'][key] = trades

            if verbose:
                print(f"\n  Config {config} / {hp}:")
                print(f"    Trades: {metrics['total_trades']} "
                      f"({metrics['wins']}W / {metrics['losses']}L / {metrics['breakevens']}BE)")
                print(f"    Win Rate: {metrics['win_rate']}%")
                print(f"    Avg Return: {metrics['avg_return_pct']}%")
                print(f"    Profit Factor: {metrics['profit_factor']}")
                print(f"    Avg R-Multiple: {metrics['avg_r_multiple']}")
                if metrics.get('sharpe_ratio') is not None:
                    print(f"    Sharpe: {metrics['sharpe_ratio']}")
                print(f"    Max Drawdown: {metrics['max_drawdown_pct']}%")
                if metrics.get('t_statistic') is not None:
                    sig = "YES" if metrics.get('t_significant') else "NO"
                    print(f"    T-test: t={metrics['t_statistic']}, p={metrics['t_pvalue']} "
                          f"(significant: {sig})")
                if metrics['warnings']:
                    for w in metrics['warnings']:
                        print(f"    WARNING: {w}")

    if verbose:
        print(f"\n  Total elapsed: {elapsed:.1f}s")

    return results


# ─── Walk-Forward Validation ─────────────────────────────────────────────────

def run_walk_forward(tickers, configs=None, holding_periods=None, verbose=True):
    """
    Walk-forward validation:
      In-sample:  2020-01-01 to 2023-06-30 (60%)
      Out-sample: 2023-07-01 to 2025-12-31 (40%)

    System is robust if OOS metrics within 20% of IS.
    """
    if configs is None:
        configs = ['A', 'B', 'C']
    if holding_periods is None:
        holding_periods = ['standard']

    if verbose:
        print("\n" + "=" * 70)
        print("  WALK-FORWARD VALIDATION")
        print("=" * 70)
        print("  In-sample:  2020-01-01 to 2023-06-30 (60%)")
        print("  Out-sample: 2023-07-01 to 2025-12-31 (40%)")
        print("=" * 70)

    is_results = run_holistic_backtest(
        tickers, start='2020-01-01', end='2023-06-30',
        holding_periods=holding_periods, configs=configs, verbose=verbose
    )

    oos_results = run_holistic_backtest(
        tickers, start='2023-07-01', end='2025-12-31',
        holding_periods=holding_periods, configs=configs, verbose=verbose
    )

    if verbose and is_results and oos_results:
        print(f"\n{'=' * 70}")
        print(f"  WALK-FORWARD COMPARISON")
        print(f"{'=' * 70}")

        for config in configs:
            for hp in holding_periods:
                key = f"{config}_{hp}"
                is_m = is_results['results'].get(key, {})
                oos_m = oos_results['results'].get(key, {})

                print(f"\n  Config {config} / {hp}:")
                _compare_metric('Win Rate', is_m.get('win_rate', 0), oos_m.get('win_rate', 0), '%')
                _compare_metric('Avg Return', is_m.get('avg_return_pct', 0), oos_m.get('avg_return_pct', 0), '%')
                _compare_metric('Profit Factor', is_m.get('profit_factor', 0), oos_m.get('profit_factor', 0), '')
                _compare_metric('Avg R', is_m.get('avg_r_multiple', 0), oos_m.get('avg_r_multiple', 0), '')

    return {'in_sample': is_results, 'out_of_sample': oos_results}


def _compare_metric(name, is_val, oos_val, unit):
    """Print IS vs OOS comparison with degradation %."""
    if is_val and is_val != 0:
        degradation = ((oos_val - is_val) / abs(is_val)) * 100
        status = 'OK' if abs(degradation) <= 20 else 'DEGRADED'
        print(f"    {name:15s} IS={is_val:8.2f}{unit}  OOS={oos_val:8.2f}{unit}  "
              f"Δ={degradation:+.1f}% [{status}]")
    else:
        print(f"    {name:15s} IS={is_val}{unit}  OOS={oos_val}{unit}")


# ─── Report Generation ───────────────────────────────────────────────────────

def save_results(results, output_dir=None):
    """Save results to JSON and generate summary."""
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'backtest_results_holistic')

    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save full results (trades + metrics)
    json_path = os.path.join(output_dir, f'backtest_{timestamp}.json')

    # Convert trades for JSON serialization
    save_data = {
        'meta': results['meta'],
        'results': results['results'],
        'trade_count': {k: len(v) for k, v in results['all_trades'].items()},
    }

    with open(json_path, 'w') as f:
        json.dump(save_data, f, indent=2, default=str)

    # Save trades as CSV
    for key, trades in results['all_trades'].items():
        if trades:
            csv_path = os.path.join(output_dir, f'trades_{key}_{timestamp}.csv')
            df = pd.DataFrame(trades)
            df.to_csv(csv_path, index=False)

    # Generate HTML report
    html_path = os.path.join(output_dir, f'report_{timestamp}.html')
    _generate_html_report(results, html_path)

    print(f"\n  Results saved to: {output_dir}/")
    print(f"    JSON:  backtest_{timestamp}.json")
    print(f"    HTML:  report_{timestamp}.html")

    return json_path, html_path


def _generate_html_report(results, html_path):
    """Generate HTML report."""
    meta = results['meta']

    html = f"""<!DOCTYPE html>
<html><head><title>v4.16 Holistic Backtest Report</title>
<style>
body {{ font-family: -apple-system, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
h1 {{ color: #1a1a2e; border-bottom: 3px solid #16213e; padding-bottom: 10px; }}
h2 {{ color: #16213e; margin-top: 30px; }}
.card {{ background: white; border-radius: 8px; padding: 20px; margin: 15px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
table {{ border-collapse: collapse; width: 100%; margin: 10px 0; }}
th, td {{ padding: 8px 12px; text-align: right; border-bottom: 1px solid #eee; }}
th {{ background: #16213e; color: white; text-align: right; }}
th:first-child, td:first-child {{ text-align: left; }}
.green {{ color: #27ae60; font-weight: bold; }}
.red {{ color: #e74c3c; font-weight: bold; }}
.yellow {{ color: #f39c12; font-weight: bold; }}
.warning {{ background: #fff3cd; border: 1px solid #ffc107; padding: 10px; border-radius: 4px; margin: 5px 0; }}
.meta {{ color: #666; font-size: 0.9em; }}
</style></head>
<body>
<h1>v4.16 Holistic 3-Layer Backtest Report</h1>
<div class="meta">
Generated: {meta['timestamp']}<br>
Period: {meta['start_date']} to {meta['end_date']}<br>
Tickers: {meta['tickers_processed']} processed ({meta['tickers_with_trades']} with trades)<br>
Elapsed: {meta['elapsed_seconds']}s
</div>

<h2>Config Comparison</h2>
<div class="card">
<p><b>Config A:</b> Categorical BUY + ADX &ge; 20 (assessment only)</p>
<p><b>Config B:</b> A + Pattern &ge; 60% confidence (adds pattern layer)</p>
<p><b>Config C:</b> B + Trade Viable + R:R &ge; 1.2 (full 3-layer system)</p>
<table>
<tr><th>Config / Period</th><th>Trades</th><th>Win Rate</th><th>Avg Return</th>
<th>Profit Factor</th><th>Avg R</th><th>Sharpe</th><th>Max DD</th><th>T-stat</th><th>p-value</th></tr>
"""

    for key, metrics in results['results'].items():
        wr = metrics['win_rate']
        wr_class = 'green' if wr >= 55 else 'red' if wr < 45 else 'yellow'
        pf = metrics['profit_factor']
        pf_class = 'green' if isinstance(pf, (int, float)) and pf > 1.5 else 'red' if isinstance(pf, (int, float)) and pf < 1.0 else 'yellow'

        html += f"""<tr>
<td>{key}</td>
<td>{metrics['total_trades']}</td>
<td class="{wr_class}">{wr}%</td>
<td>{metrics['avg_return_pct']}%</td>
<td class="{pf_class}">{pf}</td>
<td>{metrics['avg_r_multiple']}</td>
<td>{metrics.get('sharpe_ratio', 'N/A')}</td>
<td>{metrics['max_drawdown_pct']}%</td>
<td>{metrics.get('t_statistic', 'N/A')}</td>
<td>{metrics.get('t_pvalue', 'N/A')}</td>
</tr>"""

    html += """</table></div>"""

    # Warnings section
    all_warnings = []
    for key, metrics in results['results'].items():
        for w in metrics.get('warnings', []):
            all_warnings.append(f"[{key}] {w}")

    if all_warnings:
        html += "<h2>Sanity Warnings</h2><div class='card'>"
        for w in all_warnings:
            html += f"<div class='warning'>{w}</div>"
        html += "</div>"

    # Regime breakdown
    html += "<h2>Regime Breakdown</h2><div class='card'>"
    for key, metrics in results['results'].items():
        regime = metrics.get('regime_breakdown', {})
        if regime:
            html += f"<h3>{key}</h3><table>"
            html += "<tr><th>Regime</th><th>Trades</th><th>Win Rate</th><th>Avg Return</th></tr>"
            for r, rm in regime.items():
                html += f"<tr><td>{r}</td><td>{rm['trades']}</td>"
                html += f"<td>{rm['win_rate']}%</td><td>{rm['avg_return']}%</td></tr>"
            html += "</table>"
    html += "</div>"

    # Known limitations
    html += """
<h2>Known Limitations</h2>
<div class="card">
<ul>
<li><b>Survivorship bias:</b> Only tests tickers that exist today. Delisted stocks not included.</li>
<li><b>SimFin coverage:</b> Free tier has 5 years of data delayed 12 months. Some recent dates may lack fundamentals.</li>
<li><b>Scan interval:</b> Default is daily scanning. Configurable via --scan-interval.</li>
<li><b>No portfolio-level sizing:</b> Each trade evaluated independently (no position sizing optimization).</li>
<li><b>All entries/exits at daily close:</b> No intraday execution modeling.</li>
</ul>
</div>

</body></html>"""

    with open(html_path, 'w') as f:
        f.write(html)


# ─── CLI Entry Point ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='v4.16 Holistic 3-Layer Backtest')
    parser.add_argument('--quick-test', action='store_true', help='5 tickers, 1 year')
    parser.add_argument('--walk-forward', action='store_true', help='Walk-forward validation')
    parser.add_argument('--configs', nargs='+', default=['A', 'B', 'C'],
                        help='Configs to test (A B C)')
    parser.add_argument('--periods', nargs='+', default=['standard'],
                        help='Holding periods (quick standard position)')
    parser.add_argument('--tickers', nargs='+', default=None,
                        help='Override ticker list')
    parser.add_argument('--start', default='2020-01-01', help='Start date')
    parser.add_argument('--end', default='2025-12-31', help='End date')
    parser.add_argument('--scan-interval', type=int, default=1,
                        help='Check signals every N trading days (1=daily)')
    parser.add_argument('--no-save', action='store_true', help='Skip saving results')

    args = parser.parse_args()

    if args.quick_test:
        tickers = QUICK_TEST_TICKERS
        start = '2023-01-01'
        end = '2024-12-31'
        print("QUICK TEST MODE: 5 tickers, 2023-2024")
    else:
        tickers = args.tickers or BACKTEST_TICKERS
        start = args.start
        end = args.end

    if args.walk_forward:
        results = run_walk_forward(
            tickers, configs=args.configs,
            holding_periods=args.periods
        )
        if results and not args.no_save:
            if results.get('out_of_sample'):
                save_results(results['out_of_sample'])
    else:
        results = run_holistic_backtest(
            tickers, start=start, end=end,
            holding_periods=args.periods,
            configs=args.configs,
            scan_interval=args.scan_interval,
        )
        if results and not args.no_save:
            save_results(results)


if __name__ == '__main__':
    main()
