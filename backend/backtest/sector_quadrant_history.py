"""
Sector Quadrant History — Gate 0 prerequisite #1 (SRPS design doc v1.2, Section 3)

Gate 0 (SRPS: Sector Rotation Pullback System) needs to count how many
historical trading days would have produced a qualifying signal. That
requires knowing which sector(s) were in the "Improving" RRG quadrant on
each past day — but `/api/sectors/rotation` (backend.py's get_sector_rotation())
only ever computes TODAY's quadrant (yf.download(period='6mo'), reads
.iloc[-1], cached per trading day). There was no historical replay path.

This script builds that replay path WITHOUT duplicating the quadrant
formula: it imports compute_rs_ratio_and_quadrant() and SECTOR_ETF_MAP
directly from backend.py (Golden Rule 21 — one formula, not two that can
drift apart, same discipline as the Day 101 sub-industry work).

Methodology (must match production exactly, since this replay's whole
purpose is telling you what the LIVE system would have shown you on a past
day): for each trading day t in the target window, take the trailing 6mo
of aligned SPY/ETF closes ENDING AT t (the same trailing-window length
get_sector_rotation() uses by default) and call compute_rs_ratio_and_quadrant()
on that slice. This is O(days) independent recomputations, not a single
vectorized rolling formula — slower, but it's a direct, undeniable replay
of the exact same function production calls, not a re-derivation that could
subtly diverge.

FROZEN PARAMETERS (read from production, recorded here per the SRPS doc's
own "PARAMETER FREEZE" requirement, Section 6):
    RS ratio lookback window   = 6 months trailing (~126 trading days)
                                  (get_sector_rotation()'s period='6mo' default)
    RS momentum smoothing      = 10 trading days
                                  (compute_rs_ratio_and_quadrant()'s
                                  momentum_lookback=10 default)
These are NOT re-tuned here. If SRPS's backtest disappoints later, the
correct response is to reject the design, not adjust these two numbers
after seeing the result (Golden Rule 18/20).

Usage:
    python backend/backtest/sector_quadrant_history.py                    # trailing 12 months
    python backend/backtest/sector_quadrant_history.py --months 12
    python backend/backtest/sector_quadrant_history.py --start 2020-01-01 --end 2025-12-31
"""

import os
import sys
import argparse
import warnings
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from backend import compute_rs_ratio_and_quadrant, SECTOR_ETF_MAP  # noqa: E402

TRAILING_WINDOW_TRADING_DAYS = 126  # ~6mo, matches get_sector_rotation()'s period='6mo' default
MOMENTUM_LOOKBACK = 10  # matches compute_rs_ratio_and_quadrant()'s default


def download_history(start_date, end_date):
    """Download SPY + all 11 sector ETF daily closes, with enough lookback
    buffer before start_date to compute a full trailing window on day 1."""
    etf_tickers = list(SECTOR_ETF_MAP.keys())
    all_tickers = ['SPY'] + etf_tickers

    buffer_start = (pd.Timestamp(start_date) - timedelta(days=270)).strftime('%Y-%m-%d')
    print(f"Downloading {len(all_tickers)} tickers, {buffer_start} -> {end_date} "
          f"(buffer before {start_date} to fill the first trailing window)...")

    data = yf.download(all_tickers, start=buffer_start, end=end_date, progress=False, group_by='ticker')
    if data is None or data.empty:
        raise RuntimeError("yfinance returned no data — check tickers/dates/network")

    closes = {}
    for t in all_tickers:
        try:
            s = data[t]['Close'].dropna()
            if len(s) > 0:
                closes[t] = s
        except (KeyError, TypeError):
            print(f"  WARNING: no data for {t}, skipping")
    return closes


def replay_quadrants(closes, start_date, end_date):
    """For each trading day in [start_date, end_date], recompute each
    sector's quadrant using ONLY data available up to and including that
    day (a trailing TRAILING_WINDOW_TRADING_DAYS-bar window), calling the
    production function directly. Returns a long-format DataFrame."""
    spy_close = closes['SPY']
    trading_days = spy_close.loc[start_date:end_date].index
    etf_tickers = [t for t in SECTOR_ETF_MAP if t in closes]

    rows = []
    for day in trading_days:
        for etf in etf_tickers:
            etf_close = closes[etf]
            common_idx = spy_close.index.intersection(etf_close.index)
            common_idx = common_idx[common_idx <= day]
            if len(common_idx) < TRAILING_WINDOW_TRADING_DAYS:
                continue  # not enough history yet for a full trailing window
            window_idx = common_idx[-TRAILING_WINDOW_TRADING_DAYS:]

            spy_aligned = spy_close.loc[window_idx]
            etf_aligned = etf_close.loc[window_idx]

            rs_ratio, rs_momentum, quadrant = compute_rs_ratio_and_quadrant(
                etf_aligned, spy_aligned, momentum_lookback=MOMENTUM_LOOKBACK
            )
            rows.append({
                'date': day.strftime('%Y-%m-%d'),
                'etf': etf,
                'sector': SECTOR_ETF_MAP[etf]['name'],
                'rsRatio': rs_ratio,
                'rsMomentum': rs_momentum,
                'quadrant': quadrant,
            })

    return pd.DataFrame(rows)


def summarize(df):
    print("\n" + "=" * 70)
    print("QUADRANT-DAY DISTRIBUTION BY SECTOR (share of trading days)")
    print("=" * 70)
    pivot = df.pivot_table(index='sector', columns='quadrant', aggfunc='size', fill_value=0)
    for q in ['Leading', 'Weakening', 'Lagging', 'Improving']:
        if q not in pivot.columns:
            pivot[q] = 0
    pivot = pivot[['Leading', 'Weakening', 'Lagging', 'Improving']]
    pivot_pct = (pivot.div(pivot.sum(axis=1), axis=0) * 100).round(1)
    print(pivot_pct.to_string())

    print("\n" + "=" * 70)
    print("HOW OFTEN IS AT LEAST N SECTORS 'IMPROVING' ON THE SAME DAY")
    print("(this is the real ceiling on SRPS's daily candidate pool)")
    print("=" * 70)
    improving_per_day = df[df['quadrant'] == 'Improving'].groupby('date').size()
    total_days = df['date'].nunique()
    for n in [1, 2, 3, 4]:
        days_with_n = (improving_per_day >= n).sum()
        pct = round(100 * days_with_n / total_days, 1) if total_days else 0
        print(f"  >= {n} sector(s) Improving: {days_with_n}/{total_days} days ({pct}%)")
    zero_days = total_days - (improving_per_day >= 1).sum()
    print(f"  0 sectors Improving:        {zero_days}/{total_days} days "
          f"({round(100*zero_days/total_days, 1) if total_days else 0}%) "
          f"-> SRPS generates ZERO signals on these days")


def main():
    parser = argparse.ArgumentParser(description="Gate 0 prerequisite: historical sector quadrant replay")
    parser.add_argument('--months', type=int, default=12, help="Trailing N months from today (default 12, matches Gate 0)")
    parser.add_argument('--start', type=str, default=None, help="Explicit start date YYYY-MM-DD (overrides --months)")
    parser.add_argument('--end', type=str, default=None, help="Explicit end date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    end_date = args.end or datetime.now().strftime('%Y-%m-%d')
    if args.start:
        start_date = args.start
    else:
        start_date = (pd.Timestamp(end_date) - pd.DateOffset(months=args.months)).strftime('%Y-%m-%d')

    print(f"Replaying sector quadrants: {start_date} -> {end_date}")
    print(f"Frozen params: trailing window = {TRAILING_WINDOW_TRADING_DAYS} trading days "
          f"(~6mo, matches production), momentum_lookback = {MOMENTUM_LOOKBACK} days\n")

    closes = download_history(start_date, end_date)
    df = replay_quadrants(closes, start_date, end_date)

    if df.empty:
        print("No rows produced — check date range / data availability.")
        return

    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'validation_results')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'sector_quadrant_history_{start_date}_to_{end_date}.csv')
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows ({df['date'].nunique()} trading days x {df['etf'].nunique()} sectors) to {out_path}")

    summarize(df)


if __name__ == '__main__':
    main()
