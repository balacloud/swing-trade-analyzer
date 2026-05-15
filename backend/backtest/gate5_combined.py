"""
Gate 5: Combined Momentum + Mean-Reversion Backtest

Question: When momentum and MR signals coexist on the same ticker, do they
improve or cannibalize returns? Are the two systems truly complementary or do
they fight for the same capital?

Approach:
  - Run MR strategy (backtest_mr_strategy) on the 60-ticker universe
  - Run simplified technical momentum proxy (no SimFin) on same universe
    Entry: Trend Template >= 5 AND RSI(14) > 50 AND ADX > 20 AND RS52W > 1.0
    Exit: ATR-based 7% stop OR 10% target OR 20 days max
  - Measure overlap: same ticker + date windows that conflict
  - Compute combined portfolio metrics assuming equal allocation splits
  - Verdict: PASS (complementary) or FAIL (capital conflict / correlation)

Usage:
  python gate5_combined.py --quick-test    # 10 tickers, 2 years
  python gate5_combined.py                 # Full 60 tickers, 5 years

Gate PASS criteria (consensus from Day 70 audit framework):
  - Overlap rate < 30% (same ticker, overlapping holding periods)
  - Combined Sharpe >= max(individual Sharpe) × 0.9 (no cannibalization)
  - Combined PF >= 1.2 (system still profitable)
  - Correlation of daily P&L streams < 0.4 (genuinely independent)
"""

import os
import sys
import argparse
import warnings
from datetime import datetime, timedelta

import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yfinance as yf

from backtest.mr_simulator import backtest_mr_strategy


# ─── Universe ────────────────────────────────────────────────────────────────

BACKTEST_TICKERS = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA',
    'JPM', 'V', 'MA', 'GS', 'BAC',
    'UNH', 'JNJ', 'LLY', 'ABBV',
    'PG', 'HD', 'WMT', 'KO', 'PEP', 'MCD',
    'CAT', 'HON', 'UPS', 'DE',
    'XOM', 'CVX', 'COP',
    'CRM', 'NOW', 'SHOP', 'SQ', 'DDOG', 'PANW', 'CRWD', 'SNOW',
    'COST', 'NKE', 'LULU', 'CMG', 'ABNB', 'UBER',
    'ROKU', 'COIN', 'AFRM', 'PLTR',
    'AMD', 'AVGO', 'MU', 'MRVL', 'ON',
    'T', 'VZ', 'NEE', 'AMT',
    'BRK-B', 'DIS', 'F', 'GM',
]

QUICK_TEST_TICKERS = ['AAPL', 'NVDA', 'JPM', 'XOM', 'PLTR', 'AMD', 'TSLA', 'MSFT', 'META', 'CRM']

WARMUP_BARS = 260   # need 252 days for RS + trend template
MOM_MAX_DAYS = 20   # momentum exit: max 20 days
MOM_STOP_PCT = 0.07
MOM_TARGET_PCT = 0.10
MOM_COOLDOWN = 10


# ─── Indicator Helpers ────────────────────────────────────────────────────────

def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    deltas = prices.diff()
    gains = deltas.where(deltas > 0, 0)
    losses_s = -deltas.where(deltas < 0, 0)
    avg_gain = gains.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = losses_s.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def calculate_adx(high, low, close, period=14):
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
    return dx.ewm(alpha=1 / period, min_periods=period).mean()


def calculate_rs_52w(stock_close, spy_close):
    if len(stock_close) < 252 or len(spy_close) < 252:
        return None
    stock_ret = stock_close / stock_close.shift(252) - 1
    spy_ret = spy_close / spy_close.shift(252) - 1
    return (1 + stock_ret) / (1 + spy_ret)


def check_trend_template_simple(df_slice):
    """
    Simplified Trend Template: count criteria met (0-6).
    No pattern detection or S/R — just moving averages and price position.
    """
    if len(df_slice) < 200:
        return 0
    close = df_slice['Close']
    sma50 = close.rolling(50).mean()
    sma150 = close.rolling(150).mean()
    sma200 = close.rolling(200).mean()
    sma200_20ago = sma200.shift(20)

    c = float(close.iloc[-1])
    s50 = float(sma50.iloc[-1])
    s150 = float(sma150.iloc[-1])
    s200 = float(sma200.iloc[-1])
    s200_20 = float(sma200_20ago.iloc[-1]) if not pd.isna(sma200_20ago.iloc[-1]) else s200

    low_52w = float(close.rolling(252).min().iloc[-1])
    high_52w = float(close.rolling(252).max().iloc[-1])

    score = 0
    if c > s150 and c > s200:
        score += 1
    if s150 > s200:
        score += 1
    if s200 > s200_20:
        score += 1
    if s50 > s150 and s50 > s200:
        score += 1
    if c > s50:
        score += 1
    if high_52w > 0 and c >= low_52w * 1.25:
        score += 1

    return score


# ─── Data Download ────────────────────────────────────────────────────────────

def download_data(ticker, start_date, end_date, buffer_days=400):
    buffer_start = (datetime.strptime(start_date, '%Y-%m-%d')
                    - timedelta(days=buffer_days)).strftime('%Y-%m-%d')
    try:
        df = yf.download(ticker, start=buffer_start, end=end_date, progress=False, auto_adjust=True)
        if df.empty:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df
    except Exception as e:
        print(f"    ERROR downloading {ticker}: {e}")
        return None


# ─── Momentum Proxy ───────────────────────────────────────────────────────────

def backtest_momentum_proxy(stock_df, spy_df, ticker='UNKNOWN'):
    """
    Simplified technical momentum — no SimFin fundamentals.

    Entry: TT >= 5 AND RSI(14) > 50 AND ADX > 20 AND RS52W > 1.0
    Exit: 7% stop OR 10% target OR 20 days max
    Cooldown: 10 bars after any exit.
    """
    if len(stock_df) < WARMUP_BARS:
        return {'ticker': ticker, 'trades': [], 'error': 'Insufficient data'}

    close = stock_df['Close']
    high = stock_df['High']
    low = stock_df['Low']

    rsi_series = calculate_rsi(close, period=14)
    adx_series = calculate_adx(high, low, close, period=14)
    rs_series = calculate_rs_52w(close, spy_df['Close'].reindex(close.index, method='ffill'))

    if rsi_series is None or adx_series is None:
        return {'ticker': ticker, 'trades': [], 'error': 'Indicator calculation failed'}

    trades = []
    last_exit_idx = -1

    for i in range(WARMUP_BARS, len(stock_df)):
        if i < last_exit_idx + MOM_COOLDOWN:
            continue

        rsi_val = float(rsi_series.iloc[i]) if not pd.isna(rsi_series.iloc[i]) else None
        adx_val = float(adx_series.iloc[i]) if not pd.isna(adx_series.iloc[i]) else None
        rs_val = float(rs_series.iloc[i]) if rs_series is not None and not pd.isna(rs_series.iloc[i]) else 1.0

        if rsi_val is None or adx_val is None:
            continue

        # Trend template on slice
        df_slice = stock_df.iloc[:i + 1]
        tt_score = check_trend_template_simple(df_slice)

        # Entry check
        if not (tt_score >= 5 and rsi_val > 50 and adx_val > 20 and rs_val > 1.0):
            continue

        entry_price = float(close.iloc[i])
        stop_price = entry_price * (1 - MOM_STOP_PCT)
        target_price = entry_price * (1 + MOM_TARGET_PCT)

        exit_price = None
        exit_reason = None
        exit_idx = None

        for day in range(1, MOM_MAX_DAYS + 1):
            bar_idx = i + day
            if bar_idx >= len(stock_df):
                exit_idx = len(stock_df) - 1
                exit_price = float(close.iloc[exit_idx])
                exit_reason = 'data_end'
                break

            bar_low = float(low.iloc[bar_idx])
            bar_high = float(high.iloc[bar_idx])
            bar_close = float(close.iloc[bar_idx])

            if bar_low <= stop_price:
                exit_price = stop_price
                exit_idx = bar_idx
                exit_reason = 'stop_hit'
                break

            if bar_high >= target_price:
                exit_price = target_price
                exit_idx = bar_idx
                exit_reason = 'target_hit'
                break

            if day == MOM_MAX_DAYS:
                exit_price = bar_close
                exit_idx = bar_idx
                exit_reason = 'time_exit'
                break

        if exit_price is None:
            continue

        pnl_pct = ((exit_price - entry_price) / entry_price) * 100

        entry_date = str(stock_df.index[i].date()) if hasattr(stock_df.index[i], 'date') else str(stock_df.index[i])
        exit_date = str(stock_df.index[exit_idx].date()) if hasattr(stock_df.index[exit_idx], 'date') else str(stock_df.index[exit_idx])

        trades.append({
            'ticker': ticker,
            'entry_idx': i,
            'exit_idx': exit_idx,
            'entry_date': entry_date,
            'exit_date': exit_date,
            'entry_price': round(entry_price, 2),
            'exit_price': round(exit_price, 2),
            'pnl_pct': round(pnl_pct, 2),
            'hold_days': exit_idx - i,
            'exit_reason': exit_reason,
            'win': pnl_pct > 0,
            'tt_score': tt_score,
            'rsi': round(rsi_val, 1),
            'adx': round(adx_val, 1),
            'rs': round(rs_val, 3),
        })
        last_exit_idx = exit_idx

    return {'ticker': ticker, 'trades': trades}


# ─── Overlap Analysis ─────────────────────────────────────────────────────────

def analyze_overlap(mr_trades, mom_trades):
    """
    Detect overlapping holding windows: same ticker, date ranges that conflict.

    Overlap = MR entry date falls within momentum holding window, OR
              momentum entry falls within MR holding window.

    Returns overlap count, total pairs compared, and detailed conflict list.
    """
    conflicts = []

    # Group by ticker
    mr_by_ticker = {}
    for t in mr_trades:
        mr_by_ticker.setdefault(t['ticker'], []).append(t)

    mom_by_ticker = {}
    for t in mom_trades:
        mom_by_ticker.setdefault(t['ticker'], []).append(t)

    tickers_in_both = set(mr_by_ticker.keys()) & set(mom_by_ticker.keys())
    total_pairs = 0

    for ticker in tickers_in_both:
        for mr_t in mr_by_ticker[ticker]:
            mr_start = mr_t['entry_date']
            mr_end = mr_t['exit_date']
            for mom_t in mom_by_ticker[ticker]:
                total_pairs += 1
                mom_start = mom_t['entry_date']
                mom_end = mom_t['exit_date']
                # Check date overlap
                if mr_start <= mom_end and mom_start <= mr_end:
                    conflicts.append({
                        'ticker': ticker,
                        'mr_entry': mr_start,
                        'mr_exit': mr_end,
                        'mom_entry': mom_start,
                        'mom_exit': mom_end,
                    })

    return conflicts, total_pairs


# ─── Daily P&L Streams ────────────────────────────────────────────────────────

def build_daily_pnl_series(all_trades, all_dates):
    """
    Build a daily P&L series from a list of trades.
    Each trade contributes pnl_pct to its exit date (mark-to-exit).
    Dates are the union of all trading dates across the universe.
    """
    pnl_by_date = {}
    for t in all_trades:
        date = t['exit_date']
        pnl_by_date[date] = pnl_by_date.get(date, 0) + t['pnl_pct']

    series = pd.Series(pnl_by_date, name='pnl')
    series.index = pd.to_datetime(series.index)
    series = series.reindex(all_dates, fill_value=0.0)
    return series


# ─── Summary Stats ────────────────────────────────────────────────────────────

def compute_summary(trades, label):
    if not trades:
        return {
            'label': label,
            'total_trades': 0,
            'win_rate': 0,
            'avg_pnl': 0,
            'profit_factor': 0,
            'sharpe': 0,
        }
    wins = [t for t in trades if t['win']]
    pnls = [t['pnl_pct'] for t in trades]
    gross_profit = sum(t['pnl_pct'] for t in wins) if wins else 0
    gross_loss = abs(sum(t['pnl_pct'] for t in trades if not t['win']))
    pf = gross_profit / gross_loss if gross_loss > 0 else float('inf') if gross_profit > 0 else 0

    pnl_arr = np.array(pnls)
    sharpe = (np.mean(pnl_arr) / np.std(pnl_arr) * np.sqrt(252)) if np.std(pnl_arr) > 0 else 0

    return {
        'label': label,
        'total_trades': len(trades),
        'win_rate': round(len(wins) / len(trades) * 100, 1),
        'avg_pnl': round(np.mean(pnls), 2),
        'profit_factor': round(pf, 2),
        'sharpe': round(sharpe, 2),
    }


# ─── Main ─────────────────────────────────────────────────────────────────────

def run_gate5(tickers, start_date, end_date):
    print(f"\n{'='*60}")
    print(f"Gate 5: Combined Momentum + MR Backtest")
    print(f"Universe: {len(tickers)} tickers | {start_date} → {end_date}")
    print(f"{'='*60}\n")

    # Download SPY once
    print("Downloading SPY...")
    spy_df = download_data('SPY', start_date, end_date)
    if spy_df is None:
        print("FATAL: Could not download SPY data")
        return

    all_mr_trades = []
    all_mom_trades = []
    failed = []

    for i, ticker in enumerate(tickers):
        print(f"  [{i+1}/{len(tickers)}] {ticker}...", end='', flush=True)
        stock_df = download_data(ticker, start_date, end_date)
        if stock_df is None or len(stock_df) < WARMUP_BARS:
            print(" SKIP (insufficient data)")
            failed.append(ticker)
            continue

        # MR strategy
        mr_result = backtest_mr_strategy(stock_df, ticker=ticker)
        mr_trades = mr_result.get('trades', [])

        # Momentum proxy
        mom_result = backtest_momentum_proxy(stock_df, spy_df, ticker=ticker)
        mom_trades = mom_result.get('trades', [])

        all_mr_trades.extend(mr_trades)
        all_mom_trades.extend(mom_trades)

        print(f" MR={len(mr_trades)} trades, MOM={len(mom_trades)} trades")

    print(f"\n{'─'*60}")
    print(f"INDIVIDUAL SYSTEM RESULTS")
    print(f"{'─'*60}")

    mr_summary = compute_summary(all_mr_trades, 'MR')
    mom_summary = compute_summary(all_mom_trades, 'Momentum Proxy')

    for s in [mr_summary, mom_summary]:
        print(f"\n{s['label']}:")
        print(f"  Total trades:  {s['total_trades']}")
        print(f"  Win rate:      {s['win_rate']}%")
        print(f"  Avg P&L:       {s['avg_pnl']}%")
        print(f"  Profit Factor: {s['profit_factor']}")
        print(f"  Sharpe (ann):  {s['sharpe']}")

    # ── Overlap Analysis ──────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"OVERLAP ANALYSIS")
    print(f"{'─'*60}")

    conflicts, total_pairs = analyze_overlap(all_mr_trades, all_mom_trades)
    overlap_rate = (len(conflicts) / total_pairs * 100) if total_pairs > 0 else 0

    print(f"  Total cross-ticker pairs:    {total_pairs}")
    print(f"  Conflicting pairs (overlap): {len(conflicts)}")
    print(f"  Overlap rate:                {overlap_rate:.1f}%")

    if conflicts:
        print(f"\n  Sample conflicts (first 5):")
        for c in conflicts[:5]:
            print(f"    {c['ticker']}: MR {c['mr_entry']}→{c['mr_exit']} vs MOM {c['mom_entry']}→{c['mom_exit']}")

    # ── P&L Correlation ───────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"P&L CORRELATION")
    print(f"{'─'*60}")

    all_dates = pd.date_range(start=start_date, end=end_date, freq='B')
    mr_pnl = build_daily_pnl_series(all_mr_trades, all_dates)
    mom_pnl = build_daily_pnl_series(all_mom_trades, all_dates)

    corr = mr_pnl.corr(mom_pnl)
    print(f"  Daily P&L correlation (MR vs MOM): {corr:.3f}")

    # ── Combined Portfolio ────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"COMBINED PORTFOLIO (equal weight: 50% MR, 50% MOM)")
    print(f"{'─'*60}")

    combined_pnl = (mr_pnl * 0.5) + (mom_pnl * 0.5)
    combined_trades = all_mr_trades + all_mom_trades
    combined_summary = compute_summary(combined_trades, 'Combined')

    # Combined Sharpe on daily P&L
    combined_arr = combined_pnl.values
    combined_sharpe = (np.mean(combined_arr) / np.std(combined_arr) * np.sqrt(252)) if np.std(combined_arr) > 0 else 0

    print(f"  Total trades:        {combined_summary['total_trades']}")
    print(f"  Combined Sharpe:     {combined_sharpe:.2f}")
    print(f"  Combined P&L corr:   {corr:.3f}")
    print(f"  MR Sharpe:           {mr_summary['sharpe']}")
    print(f"  MOM Sharpe:          {mom_summary['sharpe']}")
    best_individual_sharpe = max(mr_summary['sharpe'], mom_summary['sharpe'])
    sharpe_ratio = (combined_sharpe / best_individual_sharpe) if best_individual_sharpe > 0 else 0
    print(f"  Combined/Best ratio: {sharpe_ratio:.2f}x  (≥0.9 = no cannibalization)")

    # ── Verdict ───────────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"GATE 5 VERDICT")
    print(f"{'='*60}")

    criteria = {
        'Overlap rate < 30%': overlap_rate < 30,
        'Combined Sharpe >= best × 0.9': sharpe_ratio >= 0.9,
        'Combined PF >= 1.2': combined_summary['profit_factor'] >= 1.2,
        'P&L correlation < 0.4': corr < 0.4,
    }

    passed = sum(criteria.values())
    total = len(criteria)

    for name, result in criteria.items():
        status = 'PASS' if result else 'FAIL'
        print(f"  [{status}] {name}")

    print(f"\n  Score: {passed}/{total}")

    if passed >= 3:
        verdict = 'PASS'
        print(f"\n  GATE 5: PASS — Systems are complementary.")
        print(f"  Recommendation: Run both. Allocate 50% capital to each stream.")
        if overlap_rate >= 20:
            print(f"  WARNING: Overlap {overlap_rate:.1f}% is elevated — consider per-ticker capital cap.")
    else:
        verdict = 'FAIL'
        print(f"\n  GATE 5: FAIL — Systems conflict or cannibalize.")
        print(f"  Recommendation: Run separately with hard capital segregation.")
        if corr >= 0.4:
            print(f"  Root cause: High P&L correlation ({corr:.3f}) — systems react to same market moves.")
        if overlap_rate >= 30:
            print(f"  Root cause: High overlap ({overlap_rate:.1f}%) — same tickers, same windows.")

    print(f"\n  Failed tickers ({len(failed)}): {failed if failed else 'none'}")
    print(f"{'='*60}\n")

    return {
        'verdict': verdict,
        'overlap_rate': round(overlap_rate, 1),
        'pnl_correlation': round(corr, 3),
        'combined_sharpe': round(combined_sharpe, 2),
        'mr_summary': mr_summary,
        'mom_summary': mom_summary,
        'combined_summary': combined_summary,
        'criteria': criteria,
        'conflicts_sample': conflicts[:10],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gate 5: Combined Momentum + MR Backtest')
    parser.add_argument('--quick-test', action='store_true',
                        help='Run on 10 tickers, 2 years (fast validation)')
    args = parser.parse_args()

    end_date = datetime.now().strftime('%Y-%m-%d')

    if args.quick_test:
        tickers = QUICK_TEST_TICKERS
        start_date = (datetime.now() - timedelta(days=365 * 2)).strftime('%Y-%m-%d')
        print("QUICK TEST MODE: 10 tickers, 2 years")
    else:
        tickers = BACKTEST_TICKERS
        start_date = (datetime.now() - timedelta(days=365 * 5)).strftime('%Y-%m-%d')

    run_gate5(tickers, start_date, end_date)
