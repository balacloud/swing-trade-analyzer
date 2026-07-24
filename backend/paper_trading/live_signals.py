"""
Live Signal Generation — Automated Daily Paper Trading Engine (Day 81)

Two systems, both reusing the exact frozen logic from
docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md rather than
reimplementing it:

  Momentum: cheap TradingView pre-filter (scan_queries.build_best_query --
            the SAME query /api/scan/tradingview?strategy=best uses) narrows
            the whole market down to up to `limit` candidates (150 as of
            Day 88, was 50), then a full live categorical assessment
            (categorical_engine.run_assessment, the JS-parity-verified
            verdict engine) + R:R check on survivors only decides which
            ones actually queue as signals.

  Mean-reversion: mean_reversion.detect_mr_signal() (Day 81 liquidity gate)
            over a dynamic TradingView-scanned universe (Day 88 —
            scan_queries.build_mr_universe_query(), ~200-300 liquid
            tickers, falls back to the static mean_reversion.DEFAULT_MR_UNIVERSE
            if the screener is unavailable). Replaced the previous static
            54-ticker list to increase daily sample throughput toward the
            50-trade confirmation bar — a breadth change only, the entry
            gate itself (RSI(2)<10, price>$10, 20d ADV>$25M) is unchanged
            and still frozen per PAPER_TRADING_PREREGISTRATION.md.
            backend.py's manual /api/mr/scan endpoint still uses the static
            list (different consumer, not part of this change).

No human filters these — every qualifying signal is queued, which is the
whole point (selection-bias-free OOS test, see ledger.py's module docstring).
"""
import sys
import os
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

import pandas as pd

import scan_queries
import mean_reversion
import pattern_detection
from providers import get_data_provider
from support_resistance import compute_sr_levels

from backtest.categorical_engine import run_assessment
from backtest.backtest_holistic import calculate_rs_52w
from backtest.trade_simulator import compute_entry_levels, calculate_atr_at
from paper_trading import ledger

MOMENTUM_COOLDOWN_DAYS = 5   # matches backtest_holistic.py's re-entry cooldown
MR_COOLDOWN_DAYS = 5         # matches mr_simulator.py's backtest_mr_strategy() cooldown
MIN_RR = 1.2                 # Config C definition (PAPER_TRADING_PREREGISTRATION.md section 6)
DEFAULT_HOLDING_PERIOD = 'standard'  # matches Config C's canonical backtest


def _to_capitalized_ohlcv(df):
    """
    DataProvider returns lowercase columns; pattern_detection/trade_simulator/
    mr_simulator all expect capitalized (Close/High/Low/Volume) — same
    normalization backend.py already applies for SPY in get_spy_data().
    """
    df = df.copy()
    df.columns = [c.capitalize() for c in df.columns]
    return df


def get_market_regime():
    """
    VIX + SPY regime, computed the same way backend.py's /api/market/vix and
    /api/market/spy routes do — but as a direct Python call, since the daily
    job must run standalone (no dependency on Flask being up).

    Returns (regime_dict, spy_df).
    """
    dp = get_data_provider()

    vix = None
    try:
        quote = dp.get_quote('^VIX')
        vix = quote.price if quote else None
    except Exception as e:
        print(f"live_signals: VIX fetch failed: {e}")

    spy_df = _to_capitalized_ohlcv(dp.get_ohlcv('SPY', period='2y'))
    close = spy_df['Close']
    sma200 = float(close.tail(200).mean())
    current = float(close.iloc[-1])
    above_200sma = current > sma200

    sma50_declining = False
    if len(close) >= 70:
        sma50_now = float(close.iloc[-50:].mean())
        sma50_20d_ago = float(close.iloc[-70:-20].mean())
        if sma50_20d_ago > 0:
            sma50_declining = (sma50_now - sma50_20d_ago) / sma50_20d_ago * 100 < -1.0

    regime = {
        'vix': vix,
        'spy_above_200sma': above_200sma,
        'spy_50sma_declining': sma50_declining,
    }
    return regime, spy_df


# Day 95: Path B forward-test experiment.
#
# Traced (Day 95) that backtest_holistic.py's actual Config C ENTRY GATE
# never uses compute_entry_levels()'s flat+8%/ATR-clamped-stop formula at
# all — that formula is EXIT MANAGEMENT only (how a position is stopped/
# targeted once taken). The real backtested entry gate (check_entry_signals())
# computes R:R from actual chart structure: risk = price - nearest_support,
# reward = nearest_resistance - price, gated on is_viable and rr_ratio>=1.2
# (falling back to a flat 1.5 R:R estimate only when no S&R levels exist).
# live_signals.py (this file) has used the EXIT formula as if it were the
# entry gate since Day 81 — a live/backtest divergence in the same bug class
# as Golden Rule 19 (JS/Python verdict parity), just never caught until now
# because nobody had reason to compare the two "R:R checks" against each
# other before.
#
# Path B replicates the REAL, already-validated S&R-based entry gate exactly
# (see check_sr_gate() below) instead of inventing something new. Path A is
# untouched — same flat/ATR proxy gate it's always used, still accumulating
# toward its own 100-trade bar. Both variants, once a signal qualifies,
# share the EXACT SAME exit-management formula (compute_entry_levels(),
# unchanged) — they only differ in what decided the trade was worth taking.
# Tracked under its own `variant` ledger tag so it never touches Path A's
# count. See KNOWN_ISSUES_DAY95.md / ROADMAP Priority #12 and
# docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md's Path B section.

SR_FALLBACK_RR = 1.5  # matches backtest_holistic.py's "no S&R found" fallback exactly


def check_sr_gate(stock_df, entry_idx):
    """
    Replicates backtest_holistic.py's check_entry_signals() Config C R:R gate
    exactly: real support/resistance levels for risk/reward, is_viable +
    rr_ratio>=1.2 as the pass condition, flat 1.5 ATR-based fallback when no
    S&R levels exist. Returns (passes: bool, rr_ratio: float, viable, nearest_support, nearest_resistance).
    """
    df_slice = stock_df.iloc[:entry_idx + 1]
    current_price = float(df_slice['Close'].iloc[-1])

    df_lower = df_slice.rename(columns={
        'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume',
    })
    sr_levels = compute_sr_levels(df_lower)

    viability = sr_levels.meta.get('trade_viability', {}) if sr_levels and sr_levels.meta else {}
    is_viable = viability.get('viable') in ('YES', True, 'CAUTION')

    nearest_support = max(sr_levels.support) if sr_levels and sr_levels.support else None
    nearest_resistance = min(sr_levels.resistance) if sr_levels and sr_levels.resistance else None

    rr_ratio = 0
    if (nearest_support and nearest_resistance
            and nearest_support < current_price < nearest_resistance):
        risk = current_price - nearest_support
        reward = nearest_resistance - current_price
        if risk > 0:
            rr_ratio = reward / risk

    if rr_ratio == 0 and is_viable:
        lookback_start = max(0, entry_idx - 50)
        atr_val = calculate_atr_at(
            stock_df['High'].iloc[lookback_start:entry_idx + 1],
            stock_df['Low'].iloc[lookback_start:entry_idx + 1],
            stock_df['Close'].iloc[lookback_start:entry_idx + 1],
        )
        if atr_val and atr_val > 0:
            rr_ratio = SR_FALLBACK_RR

    passes = is_viable and rr_ratio >= MIN_RR
    return passes, round(rr_ratio, 2), is_viable, nearest_support, nearest_resistance


def get_momentum_signals(as_of_date=None, limit=200, market_index='all'):
    """
    Returns a list of dicts (ticker, signal_date, signal_price, holding_period,
    verdict_reason, regime_snapshot, variant) for every Config C-qualifying
    momentum BUY not already active/in cooldown for its own variant. Caller
    queues each via ledger.queue_pending_signal(variant=...).

    Day 95: now yields signals for BOTH Path A (frozen, flat/ATR R:R proxy —
    unchanged since Day 81) and Path B (real S&R-based R:R gate, see
    check_sr_gate() above) — same shared Trend Template/RS/fundamentals/
    verdict computation per candidate, each variant independently checked
    against its own gate and its own cooldown state. A candidate can qualify
    for one variant, both, or neither.

    Day 88: default limit raised 50->150 (more raw ADX-ranked candidates get
    the full per-ticker categorical assessment) — a breadth change to
    increase sample-accumulation rate, not a threshold change. Config C's
    BUY/R:R criteria are unchanged.

    Day 95: raised 150->200 — measured that Config C's base TradingView
    filter only matches ~160 stocks market-wide on a given day, so 150
    already captured ~94% of the real universe; 200 gives headroom for
    that count to grow without needing another bump. Breadth-only change,
    same rationale as Day 88 (Golden Rule 18/20's distinction) — the real
    bottleneck (measured Day 95) is the R:R gate, not candidate volume; see
    ROADMAP.md Priority #12.
    """
    if not scan_queries.TRADINGVIEW_AVAILABLE:
        print("live_signals: TradingView screener unavailable, skipping momentum scan")
        return []

    if as_of_date is None:
        as_of_date = datetime.now().strftime('%Y-%m-%d')

    # Day 83 fix (Task B6): build_best_query() already derives is_canadian from
    # market_index — this was discarding it and hardcoding False, which would
    # have broken .TO suffix handling if this function were ever pointed at a
    # Canadian market_index (dormant today since the engine defaults to 'all').
    query, is_canadian = scan_queries.build_best_query(limit=limit, market_index=market_index)
    count, results = query.get_scanner_data()
    candidates = scan_queries.parse_candidates(results, is_canadian=is_canadian, strategy='best')

    regime, spy_df = get_market_regime()
    spy_close = spy_df['Close']

    dp = get_data_provider()
    signals = []

    for c in candidates:
        ticker = c['ticker']
        # Cooldown checked per-variant below, not here — a candidate might
        # qualify for Path B while Path A is on cooldown (or vice versa).
        if (ledger.has_active_or_cooldown(ticker, 'momentum', cooldown_days=MOMENTUM_COOLDOWN_DAYS,
                                           as_of_date=as_of_date, variant='A_frozen')
                and ledger.has_active_or_cooldown(ticker, 'momentum', cooldown_days=MOMENTUM_COOLDOWN_DAYS,
                                                   as_of_date=as_of_date, variant='B_revised_rr')):
            continue

        time.sleep(0.4)  # light pacing — avoid tripping provider rate limits on batch scans
        try:
            stock_df = _to_capitalized_ohlcv(dp.get_ohlcv(ticker, period='2y'))
            if len(stock_df) < 252:
                continue

            trend = pattern_detection.check_trend_template(stock_df)
            if trend is None:
                continue
            tt_score = trend['criteria_met']

            aligned_spy_close = spy_close.reindex(stock_df.index).ffill()
            rs_series = calculate_rs_52w(stock_df['Close'], aligned_spy_close)
            rs_52w = None
            if rs_series is not None and not pd.isna(rs_series.iloc[-1]):
                rs_52w = float(rs_series.iloc[-1])

            fundamentals = dp.get_fundamentals(ticker) or {}

            assessment = run_assessment(
                trend_template_score=tt_score,
                rsi=c.get('rsi'),
                rs_52w=rs_52w,
                adx=c.get('adx'),
                vix=regime['vix'],
                spy_above_200sma=regime['spy_above_200sma'],
                spy_50sma_declining=regime['spy_50sma_declining'],
                roe=fundamentals.get('roe'),
                revenue_growth=fundamentals.get('revenueGrowth'),
                debt_equity=fundamentals.get('debtToEquity'),
                eps_growth=fundamentals.get('epsGrowth'),
                holding_period=DEFAULT_HOLDING_PERIOD,
            )

            if assessment['verdict']['verdict'] != 'BUY':
                continue

            entry_idx = len(stock_df) - 1
            signal_price = float(stock_df['Close'].iloc[entry_idx])
            # Day 92: stamp signal_date from the ticker's own last OHLCV bar,
            # not the wall-clock date. as_of_date is `datetime.now()`'s
            # calendar day — if the job is force-run on a non-trading day
            # (or after-hours before that day's bar has posted), signal_date
            # would be a date that never appears in any OHLCV index, and
            # activate_pending_signals()'s _find_index_for_date() would fail
            # on it forever (permanently stuck pending_entry, only a stdout
            # print, no error surfaced anywhere). The last row of stock_df is
            # exactly the bar signal_price was read from two lines above, so
            # deriving signal_date from the same row guarantees a match.
            actual_signal_date = str(stock_df.index[entry_idx].date())
            rs_txt = f"RS {rs_52w:.2f}" if rs_52w is not None else "RS n/a"

            # Day 95: Path A (flat/ATR R:R proxy, unchanged since Day 81) and
            # Path B (real S&R-based gate, matching what the backtest
            # actually validated) each decide independently whether this
            # candidate is a qualifying entry. Exit management (stop/target
            # once entered) is identical for both — computed once, below.
            stop_price, target_price, _max_hold = compute_entry_levels(
                stock_df, entry_idx, DEFAULT_HOLDING_PERIOD, signal_price
            )
            risk_a = signal_price - stop_price
            reward_a = target_price - signal_price
            rr_a = (reward_a / risk_a) if risk_a > 0 else None
            path_a_passes = rr_a is not None and rr_a >= MIN_RR

            sr_passes, sr_rr, sr_viable, sr_support, sr_resistance = check_sr_gate(stock_df, entry_idx)

            gates = []
            if path_a_passes:
                gates.append(('A_frozen', f"BUY, TT {tt_score}/8, {rs_txt}, R:R(proxy) {rr_a:.2f}"))
            if sr_passes:
                gates.append(('B_revised_rr',
                               f"BUY, TT {tt_score}/8, {rs_txt}, R:R(S&R) {sr_rr:.2f} "
                               f"(support ${sr_support:.2f}, resistance ${sr_resistance:.2f})"))

            for variant, reason in gates:
                if ledger.has_active_or_cooldown(ticker, 'momentum', cooldown_days=MOMENTUM_COOLDOWN_DAYS,
                                                  as_of_date=as_of_date, variant=variant):
                    continue
                signals.append({
                    'ticker': ticker,
                    'signal_date': actual_signal_date,
                    'signal_price': round(signal_price, 2),
                    'holding_period': DEFAULT_HOLDING_PERIOD,
                    'verdict_reason': reason,
                    'regime_snapshot': regime,
                    'variant': variant,
                })
        except Exception as e:
            print(f"live_signals: momentum check failed for {ticker}: {e}")
            continue

    return signals


def _get_dynamic_mr_universe(limit=250):
    """
    Day 88: broad TradingView liquid-universe scan, replacing the
    hardcoded 54-name DEFAULT_MR_UNIVERSE for the automated daily job only
    (backend.py's manual /api/mr/scan endpoint still uses the static list —
    different consumer, not touched here). Breadth-only change: the actual
    MR entry gate is unchanged, still enforced per-ticker downstream in
    mean_reversion.detect_mr_signal(). Falls back to DEFAULT_MR_UNIVERSE if
    the TradingView query fails, so a screener outage can't silently stop
    the job from generating any MR signals at all.

    Day 95: raised 150->250 after a live rate-limit test (Day 89's own
    methodology) on the untested tail (candidates 151-250 today): 33 new
    real candidates, 0 OHLCV fetch failures. Still well under the 300 that
    tripped TwelveData's rate limiter Day 89. Breadth-only, same Golden
    Rule 18/20 rationale as the momentum limit bump this same session.
    """
    if not scan_queries.TRADINGVIEW_AVAILABLE:
        print("live_signals: TradingView unavailable, falling back to DEFAULT_MR_UNIVERSE")
        return mean_reversion.DEFAULT_MR_UNIVERSE
    try:
        query, is_canadian = scan_queries.build_mr_universe_query(limit=limit)
        count, results = query.get_scanner_data()
        candidates = scan_queries.parse_candidates(results, is_canadian, strategy='mr_universe')
        tickers = [c['ticker'] for c in candidates]
        if not tickers:
            print("live_signals: MR universe scan returned 0 tickers, falling back to DEFAULT_MR_UNIVERSE")
            return mean_reversion.DEFAULT_MR_UNIVERSE
        return tickers
    except Exception as e:
        print(f"live_signals: MR universe scan failed ({e}), falling back to DEFAULT_MR_UNIVERSE")
        return mean_reversion.DEFAULT_MR_UNIVERSE


def get_mr_signals(as_of_date=None, tickers=None):
    """
    Returns a list of dicts for every MR-qualifying ticker (detect_mr_signal,
    with the Day 81 liquidity gate) not already active/in cooldown.
    """
    if as_of_date is None:
        as_of_date = datetime.now().strftime('%Y-%m-%d')

    universe = tickers or _get_dynamic_mr_universe()
    dp = get_data_provider()
    regime, _ = get_market_regime()
    signals = []

    for ticker in universe:
        if ledger.has_active_or_cooldown(ticker, 'mr', cooldown_days=MR_COOLDOWN_DAYS,
                                          as_of_date=as_of_date):
            continue
        time.sleep(0.4)  # light pacing — avoid tripping provider rate limits on batch scans
        try:
            stock_df = _to_capitalized_ohlcv(dp.get_ohlcv(ticker, period='1y'))
            if len(stock_df) < 200:
                continue
            result = mean_reversion.detect_mr_signal(stock_df)
            if not result.get('signal'):
                continue

            signal_price = result['current_price']
            # Day 92: same fix as get_momentum_signals() — derive signal_date
            # from the actual last bar signal_price came from, not as_of_date.
            actual_signal_date = str(stock_df.index[-1].date())
            signals.append({
                'ticker': ticker,
                'signal_date': actual_signal_date,
                'signal_price': signal_price,
                'holding_period': None,
                'verdict_reason': (
                    f"MR: RSI(2)={result['rsi2']}, "
                    f"ADV20=${result['avg_dollar_volume']:,}"
                ),
                'regime_snapshot': regime,
            })
        except Exception as e:
            print(f"live_signals: MR check failed for {ticker}: {e}")
            continue

    return signals


if __name__ == '__main__':
    print("Momentum signals:")
    for s in get_momentum_signals():
        print(f"  {s['ticker']}: {s['verdict_reason']}")

    print("\nMR signals:")
    for s in get_mr_signals():
        print(f"  {s['ticker']}: {s['verdict_reason']}")
