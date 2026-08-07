"""
SRPS Gate 1 — Survivorship-Free Backtest (design doc v1.2, Section 6)

Gate 0 passed (~143 signal-days/year, well above the 60/year bar) — this
is the next gate the design doc requires before any live forward-test
track gets built: a real backtest of the FULL rule set (Rules 1-5, minus
Rule 6 earnings — same documented gap as Gate 0) against the
survivorship-free 2020-2025 universe, not today's S&P 500.

PARAMETER FREEZE (per Section 6's own instruction — read from production,
recorded, never re-tuned after seeing a result):
    RS ratio lookback window   = 6 months trailing (~126 trading days)
    RS momentum smoothing      = 10 trading days
Both inherited unchanged from sector_quadrant_history.py, which already
froze them against backend.py's own get_sector_rotation()/
compute_rs_ratio_and_quadrant() defaults.

WHAT'S REUSED (Golden Rule 21 — one implementation, not a second that can
drift):
    - build_unbiased_universe() from backtest_survivorship_free.py — SAME
      seed=42, sample_size=400 as Day 79's own momentum/MR re-validation,
      for direct comparability and to avoid a new, unprincipled universe
      choice.
    - download_data() from backtest_holistic.py — same per-ticker yfinance
      wrapper already proven at this exact scale (Day 79: 400 tickers,
      ~35% delisted/no-data dropout, expected and honest, not a bug).
    - compute_indicators()/compute_rs_series() and the Rules 1-4 constants
      from srps_gate0_signal_count.py — same entry logic already
      smoke-tested and verified there, imported rather than re-derived a
      second time.
    - calculate_atr_series() from trade_simulator.py.
    - compute_metrics() from metrics.py — the project's own single PF/win
      rate/expectancy/Sharpe/drawdown/significance implementation, used by
      every other backtest in this repo.
    - scan_queries' REAL_ESTATE_TV_INDUSTRY_VALUES / XLC_OVERRIDE_TICKERS
      constants, reused here for a DIFFERENT purpose than their original
      TradingView-query role: XLC_OVERRIDE_TICKERS also fixes the fact
      that SimFin's own sector taxonomy (used for THIS script's
      historical/delisted-ticker sector tagging, since TradingView can't
      classify a delisted ticker) likewise has no distinct Communication
      Services category — see SIMFIN_SECTOR_TO_ETF below.

WHAT'S GENUINELY NEW HERE (the design doc's own Section 5 item 3 — "exit
replay logic... ~80 lines"): Rule 5's stop/target/21-EMA-trail exit state
machine, and the day-by-day portfolio event loop enforcing Rule 4's max-6-
concurrent-positions cap. Neither existed anywhere in this codebase before
this script — momentum/MR's existing simulators run each ticker fully
independently with no cross-ticker concurrency limit, which SRPS's design
explicitly requires (Rule 4).

MODELING DECISIONS WHERE THE DESIGN DOC WAS AMBIGUOUS (stated explicitly,
not silently assumed):
    - Entries fill at the NEXT trading day's open after a qualifying
      signal close (standard swing-backtest convention; the doc doesn't
      say same-day-close fills, which wouldn't be executable in reality).
    - Stop/target are computed from the signal day's close-based
      indicators, then re-based onto the actual next-day entry fill price
      (preserves the same intended $ risk distance rather than silently
      changing it because the fill price moved overnight).
    - Rule 5's three exits are all evaluated off the day's CLOSE (matching
      the design doc's own framing: "applied in priority order each day
      after the close"). Stop and Trailing fill at the FOLLOWING day's
      open (matches the doc's literal "exit next open" wording, including
      the doc's own gap-risk clause: whatever that open actually is,
      including gapped further beyond the stop, is the fill). Target
      fills immediately at that day's own close (the doc's "exit at
      market" for Target, distinguished from the other two's "next open"
      wording). Priority when multiple trigger the same day: Stop >
      Target > Trailing (worst-case-first).
    - Slippage: 0.1% per side, applied multiplicatively to both entry and
      exit fills, per Section 6's own frozen parameter table (NOT this
      project's existing $0.005/share SLIPPAGE_PER_SHARE convention in
      metrics.py — the design doc pre-registered a different, explicit
      number for SRPS specifically, so that takes precedence here).

STILL NOT APPLIED (same as Gate 0, for the same reason): Rule 6 (earnings
exclusion) — no historical earnings-date source exists cheaply in this
codebase across ~400 tickers x 6 years. Results below are an upper bound.

Usage:
    python backend/backtest/srps_gate1_backtest.py                       # full 400-ticker, 2020-2025
    python backend/backtest/srps_gate1_backtest.py --sample-size 30      # smoke test
"""

import os
import sys
import json
import argparse
import warnings
from datetime import datetime

import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from backtest_survivorship_free import build_unbiased_universe  # noqa: E402
from backtest_holistic import download_data  # noqa: E402
from trade_simulator import calculate_atr_series  # noqa: E402
from metrics import compute_metrics  # noqa: E402
from srps_gate0_signal_count import (  # noqa: E402
    compute_indicators, compute_rs_series,
)
from srps_constants import (  # noqa: E402
    RS_LOOKBACK_DAYS, RS_FLOOR, EMA_PULLBACK_LOW, EMA_PULLBACK_HIGH,
    STOP_MAX_PCT, STOP_MIN_PCT, SWING_LOW_LOOKBACK, TARGET_R_MULTIPLE,
)
from sector_quadrant_history import download_history as download_sector_etf_history, replay_quadrants  # noqa: E402
import scan_queries  # noqa: E402
from backend import SECTOR_ETF_MAP  # noqa: E402

SLIPPAGE_PCT = 0.001  # 0.1% per side — Section 6's frozen parameter, NOT metrics.py's convention
MAX_CONCURRENT_POSITIONS = 6  # Rule 4

# SimFin's own sector taxonomy has NO distinct Communication Services
# category (12 values total: Basic Materials, Business Services, Consumer
# Cyclical, Consumer Defensive, Energy, Financial Services, Healthcare,
# Industrials, Other, Real Estate, Technology, Utilities — live-checked
# 2026-08-07 against simfin.load_industries()). This is the SAME kind of
# taxonomy gap already found and fixed for TradingView's screener (XLRE,
# XLC) — just recurring in a different data source. 'Business Services'
# is mapped to XLI (Industrials) as the closest GICS analogue (commercial/
# professional services); 'Other' is dropped (unclassifiable). XLC is
# handled entirely via the override below, not this table.
SIMFIN_SECTOR_TO_ETF = {
    'Technology': 'XLK',
    'Financial Services': 'XLF',
    'Healthcare': 'XLV',
    'Industrials': 'XLI',
    'Business Services': 'XLI',
    'Consumer Cyclical': 'XLY',
    'Consumer Defensive': 'XLP',
    'Energy': 'XLE',
    'Basic Materials': 'XLB',
    'Utilities': 'XLU',
    'Real Estate': 'XLRE',
}


def get_simfin_sector_map():
    """ticker -> SimFin Sector string, for every SimFin-covered US company
    (includes many delisted names — this dataset is historical, not a live
    listing, unlike TradingView's screener which only covers current
    listings)."""
    import simfin as sf
    api_key = os.environ.get('SIMFIN_API_KEY')
    sf.set_api_key(api_key)
    sf.set_data_dir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'simfin'))
    companies = sf.load_companies(market='us')
    industries = sf.load_industries()
    merged = companies.join(industries, on='IndustryId')
    return merged['Sector'].to_dict()


def tag_universe_with_sectors(tickers):
    """tickers -> {etf: [tickers]}, using SimFin's sector classification +
    the XLC hand-curated override (reused from scan_queries.py — see
    module docstring). Drops tickers with no resolvable sector (SimFin
    coverage gap or 'Other') — same honest-dropout spirit as Day 79's
    ~35% no-data rate, not silently forced into a sector they don't belong
    in."""
    sector_map = get_simfin_sector_map()
    xlc_set = set(scan_queries.XLC_OVERRIDE_TICKERS)

    universe = {etf: [] for etf in SECTOR_ETF_MAP}
    unmapped = []
    for t in tickers:
        if t in xlc_set:
            universe['XLC'].append(t)
            continue
        simfin_sector = sector_map.get(t)
        etf = SIMFIN_SECTOR_TO_ETF.get(simfin_sector)
        if etf:
            universe[etf].append(t)
        else:
            unmapped.append(t)
    print(f"Sector tagging: {sum(len(v) for v in universe.values())}/{len(tickers)} tagged, "
          f"{len(unmapped)} unmapped (no SimFin sector or 'Other'/unclassifiable): {unmapped[:15]}"
          f"{'...' if len(unmapped) > 15 else ''}")
    for etf, ts in universe.items():
        print(f"  {etf} ({SECTOR_ETF_MAP[etf]['name']}): {len(ts)} tickers")
    return universe


def build_quadrant_lookup(start_date, end_date):
    """Reuses sector_quadrant_history.py's own replay functions directly
    (not a re-derivation) for the full backtest window."""
    closes = download_sector_etf_history(start_date, end_date)
    df = replay_quadrants(closes, start_date, end_date)
    etf_by_name = {info['name']: etf for etf, info in SECTOR_ETF_MAP.items()}
    df['etf'] = df['sector'].map(etf_by_name)
    # date -> etf -> quadrant, for O(1) daily lookup instead of filtering a
    # long DataFrame inside the hot per-day loop below. replay_quadrants()
    # stores 'date' as a string (day.strftime('%Y-%m-%d')) — MUST convert
    # to Timestamp here, since run_backtest()'s trading_days loop below
    # uses pd.Timestamp keys (from an OHLCV DatetimeIndex); a string/
    # Timestamp key mismatch would make every lookup silently return {},
    # zeroing out Rule 2's gate for the entire backtest with no error.
    lookup = {}
    for row in df.itertuples():
        lookup.setdefault(pd.Timestamp(row.date), {})[row.etf] = row.quadrant
    return lookup, closes['SPY']


def run_backtest(universe, ohlcv, indicators, rs_series, quadrant_lookup, spy_close, start_date, end_date):
    # spy_close (from the quadrant-history download) is Close-only; use the
    # full OHLCV already fetched into ohlcv['SPY']/indicators['SPY'] instead,
    # which has real SMA200 computed from actual daily bars.
    spy_ind = indicators['SPY']

    trading_days = sorted(d for d in spy_ind.index if pd.Timestamp(start_date) <= d <= pd.Timestamp(end_date))

    open_positions = {}   # ticker -> dict
    pending_exits = {}    # ticker -> exit_reason, executes at NEXT day's open
    pending_entries = []  # list of (ticker, sector, stop_price_signal, entry_close_signal), executes at NEXT day's open
    closed_trades = []

    for day in trading_days:
        # ---- 1. Execute pending exits at TODAY's open (decided yesterday) ----
        for ticker, reason in list(pending_exits.items()):
            pos = open_positions.pop(ticker, None)
            if pos is None or ticker not in ohlcv or day not in ohlcv[ticker].index:
                continue
            exit_price_raw = ohlcv[ticker].loc[day, 'Open']
            exit_price_net = exit_price_raw * (1 - SLIPPAGE_PCT)
            _record_trade(closed_trades, pos, day, exit_price_net, reason)
        pending_exits = {}

        # ---- 2. Execute pending entries at TODAY's open (signaled yesterday) ----
        for ticker, sector, stop_price_signal, entry_close_signal in pending_entries:
            if ticker in open_positions or day not in ohlcv[ticker].index:
                continue
            if len(open_positions) >= MAX_CONCURRENT_POSITIONS:
                continue  # room ran out overnight (other entries filled first)
            entry_price_raw = ohlcv[ticker].loc[day, 'Open']
            entry_price_net = entry_price_raw * (1 + SLIPPAGE_PCT)
            risk_per_share_signal = entry_close_signal - stop_price_signal
            if risk_per_share_signal <= 0:
                continue
            stop_price = entry_price_net - risk_per_share_signal  # re-based to actual fill, same $ risk distance
            target_price = entry_price_net + TARGET_R_MULTIPLE * risk_per_share_signal
            open_positions[ticker] = {
                'ticker': ticker, 'sector': sector, 'entry_date': str(day.date()),
                'entry_price_net': entry_price_net, 'stop_price': stop_price,
                'target_price': target_price, 'risk_per_share': risk_per_share_signal,
                'bars_held': 0,
            }
        pending_entries = []

        # ---- 3. Evaluate exits off TODAY's close (fills scheduled for tomorrow, except target) ----
        # TRAIL_ACTIVATION_DELAY_BARS: fix applied after the first smoke test
        # found 81/104 exits were 'ema_trail' at a 3.3-day average hold — a
        # real rule-interaction bug, not a coding bug. Rule 3 admits entries
        # up to 3% BELOW the 21-EMA, and Rule 5's trail fires on any close
        # below the 21-EMA — so a large share of entries were already at or
        # past their own trail trigger on day 1, guaranteeing near-immediate
        # whipsaw exits (confirmed live: WTTR entered/exited within 1 day,
        # 3 separate times, each a real loss). Fixed per explicit user
        # choice: a 5-BAR trail activation delay, matching this project's
        # own existing, already-proven EMA-trailing-stop convention
        # (trade_simulator.py's Standard/Position configs both gate their
        # EMA trail on `day >= 5`). Stop and Target stay active from bar 1
        # — only the trailing-EMA exit waits.
        TRAIL_ACTIVATION_DELAY_BARS = 5
        for ticker, pos in list(open_positions.items()):
            if ticker not in ohlcv or day not in ohlcv[ticker].index:
                continue
            pos['bars_held'] += 1
            close_today = ohlcv[ticker].loc[day, 'Close']
            if close_today < pos['stop_price']:
                pending_exits[ticker] = 'stop_hit'
            elif close_today >= pos['target_price']:
                # Target fills immediately at today's close (doc: "exit at market", vs the other two's "next open")
                exit_price_net = close_today * (1 - SLIPPAGE_PCT)
                del open_positions[ticker]
                _record_trade(closed_trades, pos, day, exit_price_net, 'target_hit')
            elif pos['bars_held'] >= TRAIL_ACTIVATION_DELAY_BARS:
                ema21_today = indicators[ticker].loc[day, 'ema21'] if day in indicators[ticker].index else None
                if ema21_today is not None and close_today < ema21_today:
                    pending_exits[ticker] = 'ema_trail'

        # ---- 4. Evaluate entries off TODAY's close (Rules 1-4, fills scheduled for tomorrow) ----
        if day not in spy_ind.index:
            continue
        spy_close_today = spy_ind.loc[day, 'close']
        spy_sma200_today = spy_ind.loc[day, 'sma200']
        if pd.isna(spy_sma200_today) or spy_close_today <= spy_sma200_today:
            continue  # Rule 1 fails, market-wide zero new entries today

        day_quadrants = quadrant_lookup.get(day, {})
        room = MAX_CONCURRENT_POSITIONS - len(open_positions) - len(pending_entries)
        if room <= 0:
            continue

        for etf, quadrant in day_quadrants.items():
            if quadrant != 'Improving' or room <= 0:
                continue
            sector_tickers = [t for t in universe.get(etf, [])
                               if t in indicators and day in indicators[t].index
                               and t not in open_positions
                               and t not in [p[0] for p in pending_entries]]
            if not sector_tickers:
                continue
            rs_today = [(t, rs_series[t].get(day)) for t in sector_tickers]
            rs_today = [(t, v) for t, v in rs_today if v is not None and not pd.isna(v)]
            rs_today.sort(key=lambda x: x[1], reverse=True)

            for ticker, rs_val in rs_today[:3]:
                if room <= 0:
                    break
                ind = indicators[ticker].loc[day]
                if pd.isna(ind['ema21']) or pd.isna(ind['sma200']) or pd.isna(ind['avgvol20']):
                    continue
                in_pullback_zone = (EMA_PULLBACK_LOW * ind['ema21'] <= ind['close'] <= EMA_PULLBACK_HIGH * ind['ema21'])
                above_sma200 = ind['close'] > ind['sma200']
                rs_ok = rs_val >= RS_FLOOR
                volume_below_avg = ind['volume'] < ind['avgvol20']
                if not (in_pullback_zone and above_sma200 and rs_ok and volume_below_avg):
                    continue
                if pd.isna(ind['atr20']) or pd.isna(ind['swing_low_10']):
                    continue
                stop_price_signal = max(ind['close'] - ind['atr20'], ind['swing_low_10'])
                stop_pct = (ind['close'] - stop_price_signal) / ind['close']
                if stop_pct > STOP_MAX_PCT or stop_pct < STOP_MIN_PCT:
                    continue
                pending_entries.append((ticker, etf, stop_price_signal, ind['close']))
                room -= 1

    return closed_trades, open_positions


def _record_trade(closed_trades, pos, exit_date, exit_price_net, reason):
    entry_price = pos['entry_price_net']
    risk_per_share = pos['risk_per_share']
    return_pct_net = (exit_price_net / entry_price - 1) * 100
    return_r = (exit_price_net - entry_price) / risk_per_share if risk_per_share else 0
    if return_pct_net > 0.5:
        result = 'win'
    elif return_pct_net < -0.5:
        result = 'loss'
    else:
        result = 'breakeven'
    days_held = (exit_date - pd.Timestamp(pos['entry_date'])).days
    closed_trades.append({
        'ticker': pos['ticker'], 'sector': pos['sector'],
        'entry_date': pos['entry_date'], 'exit_date': str(exit_date.date()),
        'return_pct': round(return_pct_net, 4), 'return_pct_net': round(return_pct_net, 4),
        'return_r': round(return_r, 4), 'days_held': days_held,
        'result': result, 'exit_reason': reason, 'regime': 'unknown',
    })


def main():
    parser = argparse.ArgumentParser(description="SRPS Gate 1: survivorship-free 2020-2025 backtest")
    parser.add_argument('--sample-size', type=int, default=400)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--start', default='2020-01-01')
    parser.add_argument('--end', default='2025-12-31')
    args = parser.parse_args()

    print(f"Building unbiased universe (sample_size={args.sample_size}, seed={args.seed}, "
          f"SAME as Day 79's survivorship-free re-validation)...")
    sample, total_available = build_unbiased_universe(args.sample_size, args.seed)
    print(f"Sampled {len(sample)} of {total_available} SimFin-covered US tickers.")

    # Download OHLCV for the FULL random sample FIRST, before any sector
    # tagging. Found via the persona/golden-rules review: tagging sector
    # BEFORE checking OHLCV availability silently conflated two different
    # populations — "no SimFin sector metadata" (313/6589 SimFin tickers,
    # live-checked 2026-08-07: a real mix of genuine bankruptcies with
    # usable price history up to delisting — ITT Educational Services,
    # BurgerFi, Alta Mesa Holdings, tagged '_delisted' or with no
    # IndustryId at all — alongside unrelated recent IPOs like Figma that
    # just haven't been classified yet) vs. "no usable price history"
    # (Day 79's already-accepted ~35% dropout). Filtering on sector first
    # would have silently dropped real historical LOSSES that a
    # survivorship-free backtest exists specifically to capture — the same
    # bias Day 79 already paid the cost to eliminate, sneaking back in
    # through the sector-tagging step. Fix: download first, tag sector
    # only for tickers that actually survive the OHLCV step — shrinks the
    # "genuinely unclassifiable" residual to whatever's left after the
    # real, already-understood delisting filter, instead of stacking a
    # second, unexamined filter in front of it.
    print(f"\nDownloading {len(sample)+1} tickers ({args.start} -> {args.end}, with buffer) "
          f"BEFORE sector tagging, so a missing SimFin sector never masks as a missing price...")
    ohlcv = {}
    skipped = []
    for i, ticker in enumerate(sample + ['SPY'], 1):
        df = download_data(ticker, args.start, args.end, buffer_days=400)
        if df is None or len(df) < 200:
            skipped.append(ticker)
            continue
        ohlcv[ticker] = df
        if i % 50 == 0 or i == len(sample) + 1:
            print(f"  [{i}/{len(sample)+1}] downloaded, {len(skipped)} skipped so far")
    print(f"Done: {len(ohlcv)} usable, {len(skipped)} skipped "
          f"({round(100*len(skipped)/(len(sample)+1),1)}% — Day 79 found ~35% for this same universe methodology)")

    if 'SPY' not in ohlcv:
        print("ERROR: SPY download failed.")
        sys.exit(1)

    price_survivors = [t for t in sample if t in ohlcv]
    universe = tag_universe_with_sectors(price_survivors)

    print("\nComputing indicators + 3mo RS series for all tickers...")
    indicators = {}
    rs_series = {}
    for ticker, df in ohlcv.items():
        indicators[ticker] = compute_indicators(df)
        if ticker != 'SPY':
            rs_series[ticker] = compute_rs_series(df['Close'], ohlcv['SPY']['Close'])

    print("\nReplaying historical sector quadrants for the full backtest window (this reuses "
          "sector_quadrant_history.py, not a second implementation)...")
    quadrant_lookup, spy_close_for_quadrant = build_quadrant_lookup(args.start, args.end)

    print("\nRunning the day-by-day portfolio backtest (Rules 1-5, max 6 concurrent, Rule 6 NOT applied)...")
    closed_trades, still_open = run_backtest(
        universe, ohlcv, indicators, rs_series, quadrant_lookup, spy_close_for_quadrant, args.start, args.end)

    print(f"\n{len(closed_trades)} closed trades, {len(still_open)} still open at end of backtest window.")

    metrics = compute_metrics(closed_trades)

    print("\n" + "=" * 70)
    print("GATE 1 RESULT")
    print("=" * 70)
    print(f"Total trades:     {metrics['total_trades']}")
    print(f"Win rate:         {metrics['win_rate']}%")
    print(f"Profit factor:    {metrics['profit_factor']}")
    print(f"Avg R-multiple:   {metrics['avg_r_multiple']}")
    print(f"Sharpe:           {metrics['sharpe_ratio']}")
    print(f"Max DD (fixed 2% risk): {metrics['max_drawdown_fixed_risk_pct']}")
    print(f"Block-bootstrap p-value: {metrics['t_pvalue_block_bootstrap']}")
    print(f"Exit reasons:     {metrics['exit_reasons']}")
    print(f"Avg days held:    {metrics['avg_days_held']}")
    if metrics['warnings']:
        print(f"WARNINGS: {metrics['warnings']}")

    print("\nGate 1 threshold check (design doc Section 6):")
    checks = {
        'Profit Factor > 1.2': metrics['profit_factor'] not in ('inf',) and metrics['profit_factor'] > 1.2,
        'Win rate > 45%': metrics['win_rate'] > 45,
        'Expectancy > +0.15R': metrics['avg_r_multiple'] > 0.15,
        'Trade count > 150': metrics['total_trades'] > 150,
    }
    for label, passed in checks.items():
        print(f"  [{'PASS' if passed else 'FAIL'}] {label} (actual: "
              f"{metrics['profit_factor'] if 'Profit' in label else metrics['win_rate'] if 'Win' in label else metrics['avg_r_multiple'] if 'Expectancy' in label else metrics['total_trades']})")
    all_pass = all(checks.values())
    print(f"\n  OVERALL: {'PASS — proceed to live forward-testing' if all_pass else 'FAIL — do not proceed to live forward-testing as designed'}")

    val_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'validation_results')
    out_path = os.path.join(val_dir, f'srps_gate1_backtest_{args.start}_to_{args.end}_n{args.sample_size}.json')
    with open(out_path, 'w') as f:
        json.dump({
            'params': {'sample_size': args.sample_size, 'seed': args.seed, 'start': args.start, 'end': args.end,
                       'slippage_pct': SLIPPAGE_PCT, 'target_r': TARGET_R_MULTIPLE, 'max_concurrent': MAX_CONCURRENT_POSITIONS,
                       'rs_lookback_days': RS_LOOKBACK_DAYS, 'rs_floor': RS_FLOOR},
            'universe_summary': {etf: len(ts) for etf, ts in universe.items()},
            'tickers_downloaded': len(ohlcv), 'tickers_skipped': len(skipped),
            'metrics': metrics, 'gate1_checks': checks, 'gate1_pass': all_pass,
            'rule6_earnings_applied': False,
            'trades': closed_trades,
        }, f, indent=2, default=str)
    print(f"\nWrote full detail to {out_path}")


if __name__ == '__main__':
    main()
