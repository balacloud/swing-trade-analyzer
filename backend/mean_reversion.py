"""
Mean-Reversion Engine — Connors RSI(2) Approach

Entry: RSI(2) < 10 AND Price > 200 SMA AND price > $10 AND 20d $ volume > $25M
Exit: RSI(2) > 70 OR 10 trading days; stop 5% below the fill; no target
(MR_RULES below is the single definition, Day 123.)

Source: Larry Connors "Short Term Trading Strategies That Work" (2009)
Validated by: 4-LLM audit (PLAUSIBLE 3/4, MISLEADING on RSI(14) vs RSI(2))

Tier 3A (Day 69): NEW file — zero impact on existing code.
"""

import glob
import json
import os
import sqlite3

import pandas as pd
import numpy as np

# Day 81: shared with backend.py's /api/mr/scan default watchlist and the
# automated paper-trading engine (paper_trading/live_signals.py) — one list,
# not two that can drift.
DEFAULT_MR_UNIVERSE = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'META', 'TSLA',
    'AMD', 'NFLX', 'CRM', 'ADBE', 'INTC', 'QCOM', 'AVGO', 'TXN',
    'JPM', 'BAC', 'GS', 'MS', 'V', 'MA', 'PYPL',
    'UNH', 'JNJ', 'PFE', 'ABBV', 'MRK', 'LLY', 'BMY',
    'XOM', 'CVX', 'COP', 'SLB',
    'HD', 'LOW', 'TGT', 'WMT', 'COST',
    'DIS', 'CMCSA', 'T', 'VZ',
    'CAT', 'DE', 'BA', 'RTX', 'LMT', 'GE',
    'COIN', 'SQ', 'SHOP', 'PLTR', 'SOFI', 'AFRM',
]

# Day 97: HUB watchlist snapshot (sibling options-research project's curated
# "HUB_EXTENDED"/"HUB_CORE" watchlist), captured 2026-07-22. Same MR entry/exit
# rule as DEFAULT_MR_UNIVERSE above — this is a different UNIVERSE, not a
# different strategy (see paper_trading/live_signals.py's variant='mr_hub65').
#
# VIX EXCLUDED: ^VIX is not a tradeable equity — it has no "price > 200 SMA
# uptrend" semantics and fails the $10/$25M-ADV liquidity gates by
# construction. The 6 sector/thematic ETFs (SMH, URA, XLF, XBI, GDX, SOXX)
# ARE kept — they're tradeable and have valid SMA/dollar-volume behavior.
#
# NOTE: this is a hand-picked, thematically-concentrated 2026 watchlist —
# explicitly NOT survivorship-free like DEFAULT_MR_UNIVERSE's own backtest
# baseline. See backend/backtest/backtest_hub_mr.py's docstring for why this
# means its backtest numbers are not comparable to the survivorship-free
# 400-ticker result (PF 1.16, Sharpe 1.30). Several names here are recent
# IPOs (OKLO, LUNR, ASTS, RKLB, RIVN, POET, ALAB, DRAM) that will contribute
# little/nothing pre-listing given the 200-bar SMA warmup + liquidity gate —
# effective N is below the full list length.
#
# Keep this in sync with frontend/src/App.jsx's HUB_WATCHLIST (same 64
# tickers, JS side, used for the visible Scan tab watchlist) if this list is
# ever edited — same two-lists-that-can-drift risk as DEFAULT_MR_UNIVERSE's
# own cross-reference comment above.
HUB_UNIVERSE = [
    'CEG', 'ETN', 'ANET', 'ALAB', 'MOD', 'GLW', 'APH', 'FN', 'DELL', 'HPE', 'HPQ',
    'TMUS', 'KEYS', 'NOC', 'CGNX', 'ISRG', 'XYL', 'SMCI', 'ARM', 'ON', 'QCOM',
    'TSM', 'AMAT', 'LRCX', 'KLAC', 'ASML', 'LSCC', 'CCJ', 'OKLO', 'BWXT', 'FCX',
    'MP', 'TECK', 'WDC', 'SNOW', 'NET', 'SHOP', 'DDOG', 'PATH', 'GIB', 'HOOD',
    'SOFI', 'AFRM', 'UPST', 'NIO', 'LI', 'XPEV', 'JD', 'GS', 'LUNR', 'RKLB',
    'RIVN', 'ASTS', 'OXY', 'TRP', 'NFLX', 'POET', 'SMH', 'URA', 'XLF', 'XBI',
    'GDX', 'SOXX', 'DRAM',
]

# HUB_UNIVERSE's theme tags, for the backtest script's per-theme breakdown
# (a single sector-wide event can otherwise silently multi-count as
# independent wins/losses — see backtest_hub_mr.py).
HUB_THEME_MAP = {
    'CEG': 'Energy/Utility', 'ETN': 'Industrial', 'ANET': 'Networking/AI', 'ALAB': 'Semis',
    'MOD': 'Industrial', 'GLW': 'Industrial', 'APH': 'Industrial', 'FN': 'Networking/AI',
    'DELL': 'Hardware', 'HPE': 'Hardware', 'HPQ': 'Hardware', 'TMUS': 'Telecom',
    'KEYS': 'Industrial', 'NOC': 'Defense', 'CGNX': 'Industrial', 'ISRG': 'Healthcare',
    'XYL': 'Industrial', 'SMCI': 'Hardware', 'ARM': 'Semis', 'ON': 'Semis', 'QCOM': 'Semis',
    'TSM': 'Semis', 'AMAT': 'Semis', 'LRCX': 'Semis', 'KLAC': 'Semis', 'ASML': 'Semis',
    'LSCC': 'Semis', 'CCJ': 'Uranium/Nuclear', 'OKLO': 'Uranium/Nuclear', 'BWXT': 'Uranium/Nuclear',
    'FCX': 'Commodities', 'MP': 'Commodities', 'TECK': 'Commodities', 'WDC': 'Hardware',
    'SNOW': 'Cloud/SaaS', 'NET': 'Cloud/SaaS', 'SHOP': 'Cloud/SaaS', 'DDOG': 'Cloud/SaaS',
    'PATH': 'Cloud/SaaS', 'GIB': 'IT Services', 'HOOD': 'Fintech', 'SOFI': 'Fintech',
    'AFRM': 'Fintech', 'UPST': 'Fintech', 'NIO': 'China/EV', 'LI': 'China/EV',
    'XPEV': 'China/EV', 'JD': 'China/EV', 'GS': 'Financials', 'LUNR': 'Space',
    'RKLB': 'Space', 'RIVN': 'EV', 'ASTS': 'Space', 'OXY': 'Energy', 'TRP': 'Energy',
    'NFLX': 'Media', 'POET': 'Semis', 'SMH': 'ETF', 'URA': 'ETF', 'XLF': 'ETF',
    'XBI': 'ETF', 'GDX': 'ETF', 'SOXX': 'ETF', 'DRAM': 'ETF',
}


def calculate_rsi_short(closes, period=2):
    """RSI with very short period (Connors approach).

    IMPORTANT (self-review round 4): Uses Wilder's EMA (ewm), NOT SMA (rolling).
    Both backend.py:247 and backtest_holistic.py:105 use ewm(alpha=1/period).
    For RSI(2): alpha = 1/2 = 0.5. Using SMA would give different values.
    """
    if len(closes) < period + 1:
        return pd.Series(dtype=float)

    delta = closes.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def calculate_adx(high, low, close, period=14):
    """Calculate Average Directional Index for range-bound detection."""
    if len(close) < period * 2:
        return None

    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where((plus_dm > minus_dm) & (plus_dm > 0), 0.0)
    minus_dm = minus_dm.where((minus_dm > plus_dm) & (minus_dm > 0), 0.0)

    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.ewm(alpha=1/period, min_periods=period).mean()
    plus_di = 100 * (plus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)
    minus_di = 100 * (minus_dm.ewm(alpha=1/period, min_periods=period).mean() / atr)

    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(alpha=1/period, min_periods=period).mean()
    return adx


# Day 123: the MR rules, defined once. detect_mr_signal() uses them and the
# Analyze page card reads them from the API (no literals in the frontend).
# backtest/mr_simulator.py defaults and paper_trading/daily_job.py constants
# are frozen code with the same values; backtest/test_mr_rules.py asserts parity.
MR_RULES = {
    'rsi2_entry': 10,              # buy signal: RSI(2) below this
    'price_min': 10,               # close above $10
    'dollar_volume_min': 25_000_000,  # 20-day average dollar volume above this
    'stop_pct': 0.05,              # stop 5% below the fill
    'rsi2_exit': 70,               # sell on the first close with RSI(2) above this
    'max_hold_days': 10,           # or sell after this many trading days
    'cooldown_days': 5,            # forward test: 5 calendar days (ledger.py); backtest: 5 bars
}

# 2020-2025 survivorship-free backtest (ROADMAP.md "MR" rows, Day 79-81):
# 400 random liquid US stocks, liquidity gate applied, entry at the signal
# day's close. PF 1.16, Sharpe 1.30, block-bootstrap p = 0.064 (not
# statistically confirmed).
MR_BACKTEST = {
    'profitFactor': 1.16,
    'period': '2020-2025',
    'universe': '400 random liquid US stocks (survivorship-free)',
    'entry': 'signal day close',
    'note': 'not statistically confirmed (p = 0.064)',
}


def _finite(x):
    """float(x) when finite, else None (NaN/inf/None never become a rule result)."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if np.isfinite(v) else None


def detect_mr_signal(df):
    """
    Detect the mean-reversion entry signal on the LAST bar of `df`.

    Callers must pass completed bars only (see market_time.drop_forming_bar);
    the tested system decided on a finished day's close.

    Conditions (MR_RULES), each True / False / None (None = input missing):
    1. RSI(2) < 10 (sharp 2-day drop)
    2. Close > 200-day SMA (long-term uptrend intact)
    3. Close > $10
    4. 20-day avg dollar volume > $25M

    Day 81: liquidity gate matches mr_simulator's validated config.
    Day 123: the ATR-based stop / entry+2ATR target (never the tested rule)
    and the `current_price * 0.02` ATR fallback are removed. The tested exit
    plan is MR_RULES (stop 5% below the fill, RSI(2) > 70 or 10 days, no
    target). Missing inputs are reported in `missing`, never read as a fail.

    Returns
    -------
    dict  signal, conditions, values, missing, rules
    """
    if df is None or len(df) < 200:
        return {'signal': False, 'reason': 'Insufficient data (need 200+ bars)',
                'bars': 0 if df is None else len(df)}

    close = df['Close']
    rsi2_series = calculate_rsi_short(close, period=2)

    rsi2 = _finite(rsi2_series.iloc[-1]) if not rsi2_series.empty else None
    sma200 = _finite(close.rolling(200).mean().iloc[-1])
    current_price = _finite(close.iloc[-1])
    avg_volume = _finite(df['Volume'].rolling(20).mean().iloc[-1])
    avg_dollar_volume = _finite((close * df['Volume']).rolling(20).mean().iloc[-1])

    # ADX for context only (not part of the tested rule, not shown on the card)
    adx_series = calculate_adx(df['High'], df['Low'], close)
    adx_value = _finite(adx_series.iloc[-1]) if adx_series is not None else None

    def check(value, test):
        return None if value is None else bool(test(value))

    conditions = {
        'rsi2_oversold': check(rsi2, lambda v: v < MR_RULES['rsi2_entry']),
        'above_200sma': None if current_price is None or sma200 is None else current_price > sma200,
        'price_filter': check(current_price, lambda v: v > MR_RULES['price_min']),
        'volume_filter': check(avg_dollar_volume, lambda v: v > MR_RULES['dollar_volume_min']),
    }
    missing = [k for k, v in conditions.items() if v is None]
    signal = not missing and all(conditions.values())

    pct_above = round((current_price / sma200 - 1) * 100, 2) if current_price and sma200 else None

    return {
        'signal': signal,
        'strategy': 'mean_reversion',
        'rsi2': round(rsi2, 2) if rsi2 is not None else None,
        'sma200': round(sma200, 2) if sma200 is not None else None,
        'current_price': round(current_price, 2) if current_price is not None else None,
        'pct_above_sma200': pct_above,
        'adx': round(adx_value, 2) if adx_value is not None else None,
        'range_bound': adx_value is not None and adx_value < 20,
        'avg_volume': int(avg_volume) if avg_volume is not None else None,
        'avg_dollar_volume': int(avg_dollar_volume) if avg_dollar_volume is not None else None,
        'conditions': conditions,
        'missing': missing,
        'rules': MR_RULES,
        'max_hold_days': MR_RULES['max_hold_days'],
        'exit_rule': f"RSI(2) > {MR_RULES['rsi2_exit']} OR {MR_RULES['max_hold_days']} days max",
    }


def scan_universe_for_mr(tickers, fetch_data_fn):
    """
    Scan a list of tickers for MR signals.

    Parameters
    ----------
    tickers : list of str
        Ticker symbols to scan
    fetch_data_fn : callable
        Function that takes (ticker, period) and returns a DataFrame with OHLCV data.
        Should return None on failure.

    Returns
    -------
    list of dict
        List of signal dicts for tickers with active MR signals
    """
    signals = []
    for ticker in tickers:
        try:
            df = fetch_data_fn(ticker, '1y')
            if df is None or df.empty:
                continue
            result = detect_mr_signal(df)
            if result.get('signal'):
                result['ticker'] = ticker
                result['asOf'] = str(df.index[-1])[:10]  # Day 123: the completed close it was checked on
                signals.append(result)
        except Exception as e:
            print(f"MR scan error for {ticker}: {e}")
            continue

    # Sort by RSI(2) ascending (most oversold first)
    signals.sort(key=lambda x: x.get('rsi2', 100))
    return signals


# ---------------------------------------------------------------------------
# Day 123: forward-test track record for the Analyze page MR card.
# The paper-trading program is discontinued, so the ledger is final. The
# ledger's stored PF priced each trade at the entry day's CLOSE (see
# backtest/mr_open_entry_retest.py), so the card's numbers come from that
# re-test's open-basis result, which matches the card's "buy at the next
# open" plan. Cached for the process lifetime.
# ---------------------------------------------------------------------------
_BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
_LEDGER = os.path.join(_BACKEND_DIR, 'validation_results', 'paper_trading_ledger.db')
_RETEST_GLOB = os.path.join(_BACKEND_DIR, 'validation_results', 'mr_open_entry_retest_*.json')
_TRACK_RECORD_CACHE = {}

_VARIANT_LABELS = {'A_frozen': 'broad screened universe', 'mr_hub65': 'HUB-65 watchlist'}


def get_mr_track_record():
    """Forward-test results at the next-day open, per universe, or None.

    Returns {'variants': [{variant, label, trades, wins, winPct,
    profitFactor, avgPnlPct, firstEntry, lastExit}], 'basis', 'source',
    'backtest': MR_BACKTEST}. None (with a printed warning) when the re-test
    file or the ledger is missing — the card then says so.
    """
    if 'value' in _TRACK_RECORD_CACHE:
        return _TRACK_RECORD_CACHE['value']

    value = None
    try:
        files = sorted(glob.glob(_RETEST_GLOB))
        if not files:
            print("⚠️ MR track record: no mr_open_entry_retest_*.json found")
        elif not os.path.exists(_LEDGER):
            print(f"⚠️ MR track record: ledger missing at {_LEDGER}")
        else:
            with open(files[-1]) as f:
                retest = json.load(f)
            con = sqlite3.connect(_LEDGER)
            try:
                dates = {row[0]: (row[1], row[2]) for row in con.execute(
                    "SELECT variant, MIN(entry_date), MAX(exit_date) FROM paper_positions "
                    "WHERE system='mr' AND status='closed' GROUP BY variant")}
            finally:
                con.close()
            variants = []
            for variant, label in _VARIANT_LABELS.items():
                vr = retest.get('variants', {}).get(variant, {})
                # every trade, both bases on the same data (falls back to the
                # reproduced-only subset for an older re-test file)
                ob = vr.get('all_trades_open_basis') or vr.get('open_basis')
                if not ob or not ob.get('trades'):
                    print(f"⚠️ MR track record: no open-basis result for {variant}")
                    continue
                first, last = dates.get(variant, (None, None))
                variants.append({
                    'variant': variant, 'label': label,
                    'trades': ob['trades'], 'wins': ob['wins'], 'winPct': ob['win_pct'],
                    'profitFactor': ob['profit_factor'], 'avgPnlPct': ob['avg_pnl_pct'],
                    'firstEntry': first, 'lastExit': last,
                })
            if variants:
                value = {
                    'variants': variants,
                    'basis': f"bought at the next open, {round(MR_RULES['stop_pct'] * 100)}% stop from the fill, net of costs",
                    'source': os.path.basename(files[-1]),
                    'backtest': MR_BACKTEST,
                }
    except Exception as e:  # never let a stats read take down the signal route
        print(f"⚠️ MR track record unavailable: {e}")
        value = None

    if value is not None:  # don't pin a failure; retry on the next request
        _TRACK_RECORD_CACHE['value'] = value
    return value
