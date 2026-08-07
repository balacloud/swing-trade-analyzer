"""
SRPS Gate 0 — Historical Stock-Level Signal Count (design doc v1.2, Section 3)

The two Gate 0 prerequisites are already built and verified:
  1. sector_quadrant_history.py — historical per-day sector quadrant replay
  2. scan_queries.build_sector_query()/rank_candidates_by_rs() — sector
     membership + true 3-month RS ranking, all 11 sectors resolved
     (including the XLRE industry-field fix and the XLC hand-curated
     override — TradingView's sector taxonomy can't cleanly isolate
     either sector by field alone).

Neither prerequisite alone answers Gate 0's actual question: "how many
distinct trading days over the last 12 months would SRPS have produced at
least one qualifying signal?" This script is the replay that answers it,
by combining both prerequisites with Rules 3-4 evaluated day-by-day
against real historical OHLCV for every S&P 500 constituent.

METHODOLOGY:
  1. Universe: today's live S&P 500 membership, sector-tagged via the same
     scan_queries logic already verified for all 11 sectors (including the
     XLRE/XLC special cases). Gate 0 only needs the trailing 12 months
     (per the design doc's own Gate 0 procedure), and S&P 500 membership
     rarely changes within a 12-month window — a materially different
     situation from Section 6's full 2020-2025 backtest, which WOULD need
     a genuinely point-in-time, survivorship-free universe
     (backtest_survivorship_free.py's approach) and is explicitly a later,
     separate step gated behind Gate 0 passing.
  2. For each trading day in the window:
       a. Rule 1 (SPY > 200-SMA) — if false, zero signals, skip the day.
       b. For each sector in 'Improving' that day (from the quadrant
          replay CSV): rank that sector's full membership by 3-month RS
          vs SPY AS OF THAT DAY (not today), take the top 3 (Section 3
          Step 2's actual selection rule).
       c. For each of those top-3: check Rule 3 (pullback zone around the
          21-EMA, close > 200-SMA, RS >= 0.9, volume < 20d avg) and Rule 4
          (stop — tighter of 1xATR(20) or the 10-bar swing low — within
          8% of entry).
       d. Any that pass all of the above = one qualifying signal that day.

  Rule 6 (earnings > 21 days away) is DELIBERATELY NOT APPLIED — see the
  "WHAT THIS DOESN'T DO" section below. The count this script produces is
  therefore an UPPER BOUND, not the true post-earnings-filter count.

Usage:
    python backend/backtest/srps_gate0_signal_count.py                # trailing 12 months
    python backend/backtest/srps_gate0_signal_count.py --months 12
"""

import os
import sys
import json
import argparse
import warnings
from datetime import datetime

import pandas as pd
import numpy as np
import yfinance as yf

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

import scan_queries  # noqa: E402
from backend import SECTOR_ETF_MAP  # noqa: E402
from backtest_holistic import download_data  # noqa: E402
from trade_simulator import calculate_atr_series  # noqa: E402
from srps_constants import (  # noqa: E402
    RS_LOOKBACK_DAYS, RS_FLOOR, EMA_PULLBACK_LOW, EMA_PULLBACK_HIGH,
    STOP_MAX_PCT, STOP_MIN_PCT, SWING_LOW_LOOKBACK,
)
# STOP_MIN_PCT: Rule 4 only states a MAXIMUM stop distance (8%) in the
# design doc — found via Gate 1's real run that nothing stopped a
# near-ZERO stop distance either (a stock sitting exactly at its own
# 10-bar low, or ATR essentially 0). One trade (NWE, 2023-04-27) had a
# stop distance rounding to near-zero, producing a 331,408 R-multiple from
# an ordinary 1.6% price move — meaningless, and it silently dominated the
# whole backtest's average R/expectancy/drawdown figures. See
# srps_constants.py for the fix rationale (same family as Golden Rule 20's
# liquidity-floor precedent — a data-integrity/execution-realism floor,
# not a re-tune of Rule 3/4's own economic thresholds).


def get_sector_universe():
    """
    Real S&P 500 membership per broad sector, using the exact same
    resolution logic already verified live for all 11 sectors (including
    the XLRE industry-field fix and XLC hand-curated override).
    require_above_sma200=False — this is a MEMBERSHIP list, not a
    today-filtered candidate list; Rule 3's trend condition gets applied
    per historical day below, not once at fetch time.

    Returns {etf: [tickers]}.
    """
    universe = {}
    for etf, info in SECTOR_ETF_MAP.items():
        if etf == 'XLRE':
            query, is_canadian = scan_queries.build_sector_query(
                scan_queries.REAL_ESTATE_TV_INDUSTRY_VALUES, limit=100,
                field='industry', require_above_sma200=False)
        elif etf == 'XLC':
            query, is_canadian = scan_queries.build_sector_query(
                tickers=scan_queries.XLC_OVERRIDE_TICKERS, limit=100,
                require_above_sma200=False)
        else:
            query, is_canadian = scan_queries.build_sector_query(
                info['gics'], limit=100, require_above_sma200=False)
        count, results = query.get_scanner_data()
        candidates = scan_queries.parse_candidates(results, is_canadian, strategy='sector')
        universe[etf] = [c['ticker'] for c in candidates]
        print(f"  {etf} ({info['name']}): {len(universe[etf])} constituents")
    return universe


def download_universe(universe, start_date, end_date):
    """Sequential per-ticker download via the project's own download_data()
    helper (backtest_holistic.py) — same reliable, already-proven pattern
    Day 79's 400-ticker survivorship-free run used, not a from-scratch
    batch downloader. Returns {ticker: OHLCV DataFrame}."""
    all_tickers = sorted(set(t for tickers in universe.values() for t in tickers) | {'SPY'})
    data = {}
    skipped = []
    print(f"\nDownloading {len(all_tickers)} tickers ({start_date} -> {end_date}, with buffer)...")
    for i, ticker in enumerate(all_tickers, 1):
        df = download_data(ticker, start_date, end_date, buffer_days=400)
        if df is None or len(df) < 200:
            skipped.append(ticker)
            continue
        data[ticker] = df
        if i % 50 == 0 or i == len(all_tickers):
            print(f"  [{i}/{len(all_tickers)}] downloaded, {len(skipped)} skipped so far")
    print(f"Done: {len(data)} usable, {len(skipped)} skipped (insufficient/no data): {skipped[:20]}"
          f"{'...' if len(skipped) > 20 else ''}")
    return data


def compute_indicators(df):
    """21-EMA, 200-SMA, 20d avg volume, ATR(20), 10-bar rolling swing low
    (prior bar, excludes the current bar) — everything Rules 3-4 need,
    computed once per ticker as full Series, not recomputed per day."""
    close = df['Close']
    ind = pd.DataFrame(index=df.index)
    ind['close'] = close
    ind['ema21'] = close.ewm(span=21, adjust=False).mean()
    ind['sma200'] = close.rolling(200).mean()
    ind['avgvol20'] = df['Volume'].rolling(20).mean()
    ind['volume'] = df['Volume']
    ind['atr20'] = calculate_atr_series(df['High'], df['Low'], df['Close'], period=20)
    ind['swing_low_10'] = df['Low'].rolling(SWING_LOW_LOOKBACK).min().shift(1)
    return ind


def compute_rs_series(close, spy_close, lookback=RS_LOOKBACK_DAYS):
    """RS = (1 + stock's lookback-day return) / (1 + SPY's lookback-day
    return), as a full Series — same shape as backtest_holistic.py's
    calculate_rs_52w(), at a 3-month lookback instead of 52-week, matching
    SRPS Rule 3's actual spec."""
    stock_ret = close / close.shift(lookback) - 1
    spy_ret = spy_close / spy_close.shift(lookback) - 1
    return (1 + stock_ret) / (1 + spy_ret)


def main():
    parser = argparse.ArgumentParser(description="SRPS Gate 0: historical stock-level signal count")
    parser.add_argument('--months', type=int, default=12)
    parser.add_argument('--quadrant-csv', type=str, default=None,
                         help="Path to sector_quadrant_history_*.csv (default: auto-find latest matching --months)")
    args = parser.parse_args()

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (pd.Timestamp(end_date) - pd.DateOffset(months=args.months)).strftime('%Y-%m-%d')

    val_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'validation_results')
    quadrant_csv = args.quadrant_csv
    if quadrant_csv is None:
        candidates = [f for f in os.listdir(val_dir) if f.startswith('sector_quadrant_history_')]
        if not candidates:
            print("ERROR: no sector_quadrant_history_*.csv found — run sector_quadrant_history.py first.")
            sys.exit(1)
        quadrant_csv = os.path.join(val_dir, sorted(candidates)[-1])
    print(f"Using quadrant history: {quadrant_csv}")
    quadrant_df = pd.read_csv(quadrant_csv)
    quadrant_df['date'] = pd.to_datetime(quadrant_df['date'])

    etf_by_name = {info['name']: etf for etf, info in SECTOR_ETF_MAP.items()}
    quadrant_df['etf'] = quadrant_df['sector'].map(etf_by_name)

    print("\nResolving sector membership (Gate 0 prerequisite #2)...")
    universe = get_sector_universe()

    ohlcv = download_universe(universe, start_date, end_date)
    if 'SPY' not in ohlcv:
        print("ERROR: SPY download failed, cannot proceed.")
        sys.exit(1)

    print("\nComputing indicators (EMA21, SMA200, ATR20, 20d avg volume, swing low, 3mo RS)...")
    spy_ind = compute_indicators(ohlcv['SPY'])
    indicators = {}
    rs_series = {}
    for ticker, df in ohlcv.items():
        if ticker == 'SPY':
            continue
        indicators[ticker] = compute_indicators(df)
        rs_series[ticker] = compute_rs_series(df['Close'], ohlcv['SPY']['Close'])

    trading_days = quadrant_df['date'].sort_values().unique()
    trading_days = [d for d in trading_days if pd.Timestamp(start_date) <= d <= pd.Timestamp(end_date)]

    signal_days = set()
    all_signals = []  # (date, ticker, sector)
    zero_regime_days = 0

    for day in trading_days:
        if day not in spy_ind.index:
            continue
        spy_close_today = spy_ind.loc[day, 'close']
        spy_sma200_today = spy_ind.loc[day, 'sma200']
        if pd.isna(spy_sma200_today) or spy_close_today <= spy_sma200_today:
            zero_regime_days += 1
            continue  # Rule 1 fails — zero signals this day, market-wide

        improving_today = quadrant_df[(quadrant_df['date'] == day) & (quadrant_df['quadrant'] == 'Improving')]
        for _, row in improving_today.iterrows():
            etf = row['etf']
            sector_tickers = [t for t in universe.get(etf, []) if t in indicators and day in indicators[t].index]
            if not sector_tickers:
                continue

            # Rank sector's full membership by RS AS OF THIS DAY (Section 3 Step 2)
            rs_today = []
            for t in sector_tickers:
                rs_val = rs_series[t].get(day)
                if rs_val is not None and not pd.isna(rs_val):
                    rs_today.append((t, rs_val))
            rs_today.sort(key=lambda x: x[1], reverse=True)
            top3 = rs_today[:3]

            for ticker, rs_val in top3:
                ind = indicators[ticker].loc[day]
                if pd.isna(ind['ema21']) or pd.isna(ind['sma200']) or pd.isna(ind['avgvol20']):
                    continue

                # Rule 3
                in_pullback_zone = (EMA_PULLBACK_LOW * ind['ema21'] <= ind['close'] <= EMA_PULLBACK_HIGH * ind['ema21'])
                above_sma200 = ind['close'] > ind['sma200']
                rs_ok = rs_val >= RS_FLOOR
                volume_below_avg = ind['volume'] < ind['avgvol20']
                if not (in_pullback_zone and above_sma200 and rs_ok and volume_below_avg):
                    continue

                # Rule 4: tighter of 1xATR20 or 10-bar swing low
                if pd.isna(ind['atr20']) or pd.isna(ind['swing_low_10']):
                    continue
                stop_atr = ind['close'] - ind['atr20']
                stop_swing = ind['swing_low_10']
                stop_price = max(stop_atr, stop_swing)  # tighter = higher/closer stop
                stop_pct = (ind['close'] - stop_price) / ind['close']
                if stop_pct > STOP_MAX_PCT or stop_pct < STOP_MIN_PCT:
                    continue

                signal_days.add(day)
                all_signals.append({'date': str(day.date()), 'ticker': ticker, 'sector': row['sector'], 'rsRatio': round(rs_val, 3)})

    total_days = len(trading_days)
    n_signal_days = len(signal_days)

    print("\n" + "=" * 70)
    print("GATE 0 RESULT — SIGNAL FREQUENCY (Rules 1-4, Rule 6 earnings NOT applied — see below)")
    print("=" * 70)
    print(f"Window: {start_date} -> {end_date} ({total_days} trading days)")
    print(f"Days with SPY < 200-SMA (Rule 1 fails, market-wide zero): {zero_regime_days} ({round(100*zero_regime_days/total_days,1)}%)")
    print(f"Days with >=1 qualifying signal: {n_signal_days} ({round(100*n_signal_days/total_days,1) if total_days else 0}%)")
    print(f"Total signal INSTANCES (ticker-days, can be >1/day): {len(all_signals)}")
    annualized = round(n_signal_days * (365 / max(total_days, 1)), 1)
    print(f"Annualized signal-day rate: ~{annualized}/year")

    print("\nGate 0 threshold check (design doc Section 3):")
    if annualized >= 60:
        verdict = "VIABLE (>= 60/year) — proceed to backtest (Section 6)"
    elif annualized >= 40:
        verdict = "MARGINAL (40-59/year) — proceed only with a loosened variant active"
    else:
        verdict = "DO NOT BUILD (< 40/year) — loosen Rule 3's bands or the RS floor and re-run"
    print(f"  {verdict}")

    if all_signals:
        sig_df = pd.DataFrame(all_signals)
        print("\nSignal-days by sector:")
        print(sig_df.groupby('sector')['date'].nunique().sort_values(ascending=False).to_string())

    out_path = os.path.join(val_dir, f'srps_gate0_signals_{start_date}_to_{end_date}.json')
    with open(out_path, 'w') as f:
        json.dump({
            'window': {'start': start_date, 'end': end_date, 'trading_days': total_days},
            'zero_regime_days': zero_regime_days,
            'signal_days': n_signal_days,
            'signal_instances': len(all_signals),
            'annualized_rate': annualized,
            'verdict': verdict,
            'rule6_earnings_applied': False,
            'signals': all_signals,
        }, f, indent=2)
    print(f"\nWrote full detail to {out_path}")

    print("\n" + "=" * 70)
    print("WHAT THIS DOESN'T DO (read before trusting the count above)")
    print("=" * 70)
    print("""
- Rule 6 (earnings > 21 days away) is NOT applied. STA's /api/earnings/<ticker>
  is a live/upcoming calendar, not a historical one — there is no cheap
  source in this codebase for "was ticker X within 21 days of an earnings
  date on historical date Y" across ~500 tickers x 12 months. The count
  above is therefore an UPPER BOUND. Directionally this can only ever
  REDUCE the true count (earnings exclusion never adds signals), and each
  company reports ~4x/year with an ~42-day exclusion window per report
  (21 days either side is not what Rule 6 says — Rule 6 excludes 21 days
  BEFORE earnings only, i.e. ~21/365 = ~5.8% of any single ticker's
  calendar days) — a rough, order-of-magnitude expectation is a small
  single-digit-percent reduction in the final count, not a multiple-x
  correction. Do not treat the number above as final without either
  sourcing historical earnings dates or accepting this as a known,
  quantified-direction approximation.
- Universe is TODAY's S&P 500 membership applied across the trailing 12
  months, not a point-in-time reconstruction. Reasonable for a 12-month
  Gate 0 check (index turnover is slow); NOT reasonable to reuse for
  Section 6's full 2020-2025 backtest without switching to
  backtest_survivorship_free.py's point-in-time approach.
- Rule 2's sector-quadrant gate is baked in throughout (this counts the
  gated `srps` track only). The design doc's `srps-nogate` variant would
  need this same day-by-day loop with the Improving-quadrant filter on
  Section 3 Step 1 removed — not built here, since Gate 0's frequency
  concern is specifically about the gated, more-selective variant.
""")


if __name__ == '__main__':
    main()
