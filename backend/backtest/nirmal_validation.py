"""
Nirmal Trade Call Validation — Does STA's categorical assessment agree with Nirmal?

Parses Nirmal's stock calls from the raw WhatsApp chat export, then runs each
call through STA's categorical_engine to determine what verdict STA would have
given on the day Nirmal posted it.

This validates (or challenges) our categorical assessment as a systematized
version of Nirmal's practitioner intuition.

Usage:
    cd backend
    python backtest/nirmal_validation.py

Output:
    - Summary stats: % BUY / HOLD / AVOID when Nirmal said BUY
    - Breakdown by year, sector
    - Full CSV: nirmal_validation_results.csv
    - Saves to docs/research/NIRMAL_STA_VALIDATION_RESULTS.md
"""

import os
import sys
import re
import json
import warnings
from datetime import datetime, timedelta
from collections import defaultdict

import pandas as pd
import numpy as np
import yfinance as yf

warnings.filterwarnings('ignore')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backtest.categorical_engine import run_assessment
from backtest.trade_simulator import is_spy_above_200sma, is_spy_50sma_declining

# ─── Configuration ────────────────────────────────────────────────────────────

CHAT_FILE = os.path.join(
    os.path.dirname(__file__), '../../docs/research/Nirmals_Trading_April2026.md'
)

OUTPUT_CSV = os.path.join(
    os.path.dirname(__file__), '../../docs/research/nirmal_validation_results.csv'
)

OUTPUT_MD = os.path.join(
    os.path.dirname(__file__), '../../docs/research/NIRMAL_STA_VALIDATION_RESULTS.md'
)

WARMUP_DAYS = 400  # Buffer for RSI/RS/ADX warmup (252 trading days needed)

# ─── Regex: Parse Nirmal's stock calls ────────────────────────────────────────
# Format: "Buying TICKER Entry1$ and Entry2$ Target T$ SL SL$"
# Also: "Buy TICKER @Price" and "Accumulate buy TICKER Price$"
# Excludes options (contains "call option" or "put")

CALL_PATTERN = re.compile(
    r'^\[(\d{4}-\d{2}-\d{2}),\s[\d:,\s APM]+\]\s+Nirmal Stocks India Cognizant:\s+'
    r'(?:Buying|Buy|Accumulate\s+buy?)\s+([A-Z]{1,5})\s+\(?[^)]*\)?\s*'
    r'(\d+\.?\d*)\$?\s*(?:and\s+(\d+\.?\d*)\$?)?\s*'
    r'(?:Target[s]?\s+(\d+\.?\d*)\$?)?\s*(?:and\s+(\d+\.?\d*)\$?)?\s*'
    r'(?:SL\s+(\d+\.?\d*)\$?)?',
    re.IGNORECASE | re.MULTILINE
)

# Simpler targeted pattern (more reliable)
STOCK_CALL_PATTERN = re.compile(
    r'^\[(\d{4}-\d{2}-\d{2}),.*?\]\s+Nirmal Stocks India Cognizant:\s+'
    r'(?:Buying|Buy(?!\s+USTEC|US30|BTCUSD|IWM\s+\d+\$\s+call|SPY\s+\d+\$\s+call|QQQ\s+\d+\$\s+call|TQQQ\s+\d+\$\s+call))\s+'
    r'([A-Z]{1,5})\b',
    re.MULTILINE
)

# Full call parser
FULL_CALL_PATTERN = re.compile(
    r'^\[(\d{4}-\d{2}-\d{2}),.*?\]\s+Nirmal Stocks India Cognizant:\s+'
    r'Buying\s+([A-Z\-]{1,6})\s+(?:\([^)]*\)\s+)?'
    r'(\d+\.?\d*)\$?\s+(?:and\s+(\d+\.?\d*)\$?\s+)?'
    r'(?:Target[s]?\s+(\d+\.?\d*)\$?(?:\s+and\s+(\d+\.?\d*))?)?'
    r'(?:\s+SL\s+(\d+\.?\d*))?',
    re.MULTILINE | re.IGNORECASE
)


def parse_calls_from_chat(filepath):
    """
    Parse stock calls from Nirmal's WhatsApp chat export.
    Returns list of dicts: {date, ticker, entry1, entry2, target1, target2, sl, raw_line}
    Excludes: options calls, crypto (BTC/ETH), forex (US30/USTEC), ETF index calls when
    accompanied by options in same message.
    """
    calls = []
    seen = set()  # deduplicate same ticker+date

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: Chat file not found: {filepath}")
        return []

    lines = content.split('\n')

    # Known exclusions - not tradeable stocks / crypto / forex
    EXCLUDE_TICKERS = {
        'BTCUSD', 'ETHUSD', 'US30', 'USTEC', 'US100', 'XAUUSD',
        'BTC', 'ETH', 'DOGE', 'XRP',
    }

    # Options indicator phrases
    OPTIONS_PHRASES = ['call option', 'put option', 'call buy', 'expiry', 'strike']

    for i, line in enumerate(lines):
        # Only process Nirmal's messages
        if 'Nirmal Stocks India Cognizant' not in line:
            continue

        # Skip options calls
        line_lower = line.lower()
        if any(phrase in line_lower for phrase in OPTIONS_PHRASES):
            continue

        # Skip deleted/edited markers
        if 'This message was deleted' in line or 'image omitted' in line:
            continue

        # Extract date
        date_match = re.match(r'^\[(\d{4}-\d{2}-\d{2}),', line)
        if not date_match:
            continue
        call_date = date_match.group(1)

        # Try full call pattern
        m = FULL_CALL_PATTERN.match(line)
        if m:
            date_str = m.group(1)
            ticker = m.group(2).upper().strip()
            entry1 = float(m.group(3)) if m.group(3) else None
            entry2 = float(m.group(4)) if m.group(4) else None
            target1 = float(m.group(5)) if m.group(5) else None
            target2 = float(m.group(6)) if m.group(6) else None
            sl = float(m.group(7)) if m.group(7) else None

            # Exclusions
            if ticker in EXCLUDE_TICKERS:
                continue
            if entry1 is None or entry1 <= 0:
                continue
            # Skip if entry looks like an options strike ($1-5 range calls for cheap stocks)
            # Cheap options: premium < $10, very low entry price with no SL
            if entry1 < 1.0:
                continue
            # Skip BTC-range prices
            if entry1 > 5000:
                continue

            key = (date_str, ticker)
            if key in seen:
                continue
            seen.add(key)

            calls.append({
                'date': date_str,
                'ticker': ticker,
                'entry1': entry1,
                'entry2': entry2,
                'target1': target1,
                'target2': target2,
                'sl': sl,
                'raw_line': line[:120],
            })

    print(f"Parsed {len(calls)} stock calls from chat")
    return calls


# ─── Indicator helpers ────────────────────────────────────────────────────────

def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    deltas = prices.diff()
    gains = deltas.where(deltas > 0, 0)
    losses_s = -deltas.where(deltas < 0, 0)
    avg_gain = gains.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = losses_s.ewm(alpha=1 / period, min_periods=period).mean()
    rs_ratio = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs_ratio))
    return rsi


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
    adx = dx.ewm(alpha=1 / period, min_periods=period).mean()
    return adx


def calculate_rs_52w(stock_close, spy_close):
    if len(stock_close) < 252 or len(spy_close) < 252:
        return None
    stock_ret = stock_close / stock_close.shift(252) - 1
    spy_ret = spy_close / spy_close.shift(252) - 1
    return (1 + stock_ret) / (1 + spy_ret)


def check_trend_template_manual(df):
    """
    Minervini Trend Template — 8 criteria (manual implementation).
    Returns count of criteria passed (0-8).
    """
    if len(df) < 252:
        return 0

    close = df['Close']
    high = df['High']
    low = df['Low']

    c = close.iloc[-1]
    try:
        sma50 = close.rolling(50).mean().iloc[-1]
        sma150 = close.rolling(150).mean().iloc[-1]
        sma200 = close.rolling(200).mean().iloc[-1]
        sma200_30ago = close.rolling(200).mean().iloc[-30] if len(close) >= 230 else sma200
        high52 = high.rolling(252).max().iloc[-1]
        low52 = low.rolling(252).min().iloc[-1]
    except Exception:
        return 0

    score = 0
    # 1. Price > 150 SMA
    if c > sma150:
        score += 1
    # 2. Price > 200 SMA
    if c > sma200:
        score += 1
    # 3. 150 SMA > 200 SMA
    if sma150 > sma200:
        score += 1
    # 4. 200 SMA trending up (vs 30 days ago)
    if sma200 > sma200_30ago:
        score += 1
    # 5. 50 SMA > 150 SMA
    if sma50 > sma150:
        score += 1
    # 6. Price > 50 SMA
    if c > sma50:
        score += 1
    # 7. Price >= 25% above 52-week low
    if c >= low52 * 1.25:
        score += 1
    # 8. Price within 25% of 52-week high
    if c >= high52 * 0.75:
        score += 1

    return score


def get_fundamentals(ticker):
    """Fetch fundamentals from yfinance (best-effort)."""
    try:
        info = yf.Ticker(ticker).info
        roe = info.get('returnOnEquity')
        if roe is not None:
            roe = roe * 100  # convert from decimal
        rev_growth = info.get('revenueGrowth')
        if rev_growth is not None:
            rev_growth = rev_growth * 100
        de = info.get('debtToEquity')
        if de is not None:
            de = de / 100  # yfinance returns as percentage

        return {
            'roe': roe,
            'revenue_growth': rev_growth,
            'debt_equity': de,
        }
    except Exception:
        return {'roe': None, 'revenue_growth': None, 'debt_equity': None}


# ─── Main Validation Logic ─────────────────────────────────────────────────────

def validate_call(call, spy_cache, vix_cache, fund_cache):
    """
    For a single Nirmal call, compute STA categorical assessment.
    Returns dict with verdict + details, or None on error.
    """
    ticker = call['ticker']
    call_date = call['date']

    # Fetch stock data with warmup buffer
    try:
        start_dt = (datetime.strptime(call_date, '%Y-%m-%d') - timedelta(days=WARMUP_DAYS)).strftime('%Y-%m-%d')
        end_dt = (datetime.strptime(call_date, '%Y-%m-%d') + timedelta(days=3)).strftime('%Y-%m-%d')

        df = yf.download(ticker, start=start_dt, end=end_dt, progress=False, auto_adjust=True)
        if df.empty or len(df) < 50:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
    except Exception as e:
        print(f"  SKIP {ticker} {call_date}: {e}")
        return None

    # Find the index for the call date (or closest trading day)
    df.index = pd.to_datetime(df.index)
    target_date = pd.Timestamp(call_date)
    # Find nearest available date on or after the call date
    avail_dates = df.index[df.index >= target_date]
    if len(avail_dates) == 0:
        avail_dates = df.index[df.index <= target_date]
        if len(avail_dates) == 0:
            return None
    actual_date = avail_dates[0]
    date_idx = df.index.get_loc(actual_date)

    if date_idx < 50:
        return None

    # Compute indicators
    rsi_series = calculate_rsi(df['Close'], 14)
    adx_series = calculate_adx(df['High'], df['Low'], df['Close'], 14)

    rsi_val = float(rsi_series.iloc[date_idx]) if rsi_series is not None and date_idx < len(rsi_series) else None
    adx_val = float(adx_series.iloc[date_idx]) if adx_series is not None and date_idx < len(adx_series) else None

    if rsi_val is None or pd.isna(rsi_val):
        return None

    # Trend Template
    df_slice = df.iloc[:date_idx + 1]
    tt_score = check_trend_template_manual(df_slice)

    # RS 52-week vs SPY
    rs_val = 1.0
    if ticker in spy_cache:
        spy_df = spy_cache[ticker]
        # Align SPY to stock dates
        aligned_spy = spy_df.reindex(df.index, method='ffill')
        rs_series = calculate_rs_52w(df['Close'], aligned_spy['Close'])
        if rs_series is not None and date_idx < len(rs_series):
            v = rs_series.iloc[date_idx]
            if v is not None and not pd.isna(v):
                rs_val = float(v)

    # SPY regime
    spy_above = True
    spy_declining = False
    if 'SPY_GLOBAL' in spy_cache:
        spy_data = spy_cache['SPY_GLOBAL']
        # Find matching date in SPY
        spy_avail = spy_data.index[spy_data.index >= target_date]
        if len(spy_avail) > 0:
            spy_date_idx = spy_data.index.get_loc(spy_avail[0])
            spy_above = is_spy_above_200sma(spy_data, spy_date_idx)
            spy_declining = is_spy_50sma_declining(spy_data, spy_date_idx)

    # VIX
    vix_val = None
    if 'VIX' in vix_cache:
        vix_data = vix_cache['VIX']
        vix_avail = vix_data.index[vix_data.index >= target_date]
        if len(vix_avail) > 0:
            vix_val = float(vix_data['Close'].iloc[vix_data.index.get_loc(vix_avail[0])])

    # Fundamentals (cached per ticker)
    if ticker not in fund_cache:
        fund_cache[ticker] = get_fundamentals(ticker)
    funds = fund_cache[ticker]

    # Run STA assessment
    result = run_assessment(
        trend_template_score=tt_score,
        rsi=rsi_val,
        rs_52w=rs_val,
        adx=adx_val if adx_val and not pd.isna(adx_val) else None,
        vix=vix_val,
        spy_above_200sma=spy_above,
        spy_50sma_declining=spy_declining,
        roe=funds.get('roe'),
        revenue_growth=funds.get('revenue_growth'),
        debt_equity=funds.get('debt_equity'),
        holding_period='standard',
    )

    verdict = result['verdict']['verdict']
    technical = result['technical']['assessment']
    fundamental = result['fundamental']['assessment']
    risk_macro = result['risk_macro']['assessment']

    return {
        'date': call_date,
        'ticker': ticker,
        'entry1': call['entry1'],
        'entry2': call.get('entry2'),
        'target1': call.get('target1'),
        'sl': call.get('sl'),
        'tt_score': tt_score,
        'rsi': round(rsi_val, 1) if rsi_val else None,
        'rs_52w': round(rs_val, 3),
        'adx': round(adx_val, 1) if adx_val and not pd.isna(adx_val) else None,
        'vix': round(vix_val, 1) if vix_val else None,
        'spy_above_200sma': spy_above,
        'technical': technical,
        'fundamental': fundamental,
        'risk_macro': risk_macro,
        'sta_verdict': verdict,
        'verdict_reason': result['verdict']['reason'],
        'year': call_date[:4],
    }


def run_validation():
    print("=" * 60)
    print("NIRMAL CALL VALIDATION — STA CATEGORICAL ASSESSMENT")
    print("=" * 60)

    # 1. Parse calls
    calls = parse_calls_from_chat(CHAT_FILE)
    if not calls:
        print("No calls parsed. Check chat file path.")
        return

    print(f"\nTotal calls to validate: {len(calls)}")
    print(f"Date range: {calls[0]['date']} → {calls[-1]['date']}")
    print(f"Unique tickers: {len(set(c['ticker'] for c in calls))}")

    # 2. Pre-load shared data (SPY + VIX) for full date range
    print("\nPre-loading SPY and VIX data...")
    earliest = min(c['date'] for c in calls)
    latest = max(c['date'] for c in calls)
    buf_start = (datetime.strptime(earliest, '%Y-%m-%d') - timedelta(days=WARMUP_DAYS)).strftime('%Y-%m-%d')
    buf_end = (datetime.strptime(latest, '%Y-%m-%d') + timedelta(days=5)).strftime('%Y-%m-%d')

    spy_cache = {}
    vix_cache = {}

    try:
        spy_global = yf.download('SPY', start=buf_start, end=buf_end, progress=False, auto_adjust=True)
        if isinstance(spy_global.columns, pd.MultiIndex):
            spy_global.columns = spy_global.columns.get_level_values(0)
        spy_global.index = pd.to_datetime(spy_global.index)
        spy_cache['SPY_GLOBAL'] = spy_global

        # Also use SPY for RS calculations per ticker
        spy_cache['_SPY_RS'] = spy_global
        print(f"  SPY loaded: {len(spy_global)} bars")
    except Exception as e:
        print(f"  WARNING: SPY load failed: {e}")

    try:
        vix_data = yf.download('^VIX', start=buf_start, end=buf_end, progress=False, auto_adjust=True)
        if isinstance(vix_data.columns, pd.MultiIndex):
            vix_data.columns = vix_data.columns.get_level_values(0)
        vix_data.index = pd.to_datetime(vix_data.index)
        vix_cache['VIX'] = vix_data
        print(f"  VIX loaded: {len(vix_data)} bars")
    except Exception as e:
        print(f"  WARNING: VIX load failed: {e}")

    # For RS: use SPY global
    for call in calls:
        spy_cache[call['ticker']] = spy_cache.get('_SPY_RS', pd.DataFrame())

    # 3. Validate each call
    print(f"\nValidating {len(calls)} calls (this takes ~2-3 min)...\n")
    results = []
    fund_cache = {}
    errors = 0

    for i, call in enumerate(calls, 1):
        ticker = call['ticker']
        date = call['date']
        if i % 20 == 0 or i == 1:
            print(f"  [{i}/{len(calls)}] {ticker} {date}...")

        r = validate_call(call, spy_cache, vix_cache, fund_cache)
        if r:
            results.append(r)
        else:
            errors += 1

    print(f"\nCompleted: {len(results)} validated, {errors} skipped/errored")

    if not results:
        print("No results. Check data sources.")
        return

    # 4. Compute statistics
    df_results = pd.DataFrame(results)

    total = len(df_results)
    buy_count = (df_results['sta_verdict'] == 'BUY').sum()
    hold_count = (df_results['sta_verdict'] == 'HOLD').sum()
    avoid_count = (df_results['sta_verdict'] == 'AVOID').sum()

    buy_pct = buy_count / total * 100
    hold_pct = hold_count / total * 100
    avoid_pct = avoid_count / total * 100

    # Agreement rate: BUY or HOLD (not an outright contradiction)
    agree_pct = (buy_count + hold_count) / total * 100

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Total calls validated: {total}")
    print(f"BUY  (STA agrees):   {buy_count:3d}  ({buy_pct:.1f}%)")
    print(f"HOLD (STA cautious): {hold_count:3d}  ({hold_pct:.1f}%)")
    print(f"AVOID (STA disagrees): {avoid_count:3d}  ({avoid_pct:.1f}%)")
    print(f"\nAgreement rate (BUY+HOLD): {agree_pct:.1f}%")
    print(f"Contradiction rate (AVOID when Nirmal said BUY): {avoid_pct:.1f}%")

    # By year
    print("\n--- By Year ---")
    for year in sorted(df_results['year'].unique()):
        yr = df_results[df_results['year'] == year]
        yr_buy = (yr['sta_verdict'] == 'BUY').sum()
        yr_total = len(yr)
        print(f"  {year}: {yr_total} calls → {yr_buy} BUY ({yr_buy/yr_total*100:.1f}%), "
              f"{(yr['sta_verdict']=='HOLD').sum()} HOLD, "
              f"{(yr['sta_verdict']=='AVOID').sum()} AVOID")

    # Where STA disagreed — what caused it?
    avoids = df_results[df_results['sta_verdict'] == 'AVOID']
    if len(avoids) > 0:
        print(f"\n--- Top Avoid Reasons (sample) ---")
        for _, row in avoids.head(10).iterrows():
            print(f"  {row['date']} {row['ticker']}: TT={row['tt_score']}/8, RSI={row['rsi']}, "
                  f"RS={row['rs_52w']}, Tech={row['technical']}, "
                  f"Fund={row['fundamental']}, Risk={row['risk_macro']}")
            print(f"    Reason: {row['verdict_reason']}")

    # Technical breakdown for BUY calls
    print("\n--- Technical Assessment Distribution ---")
    for assessment in ['Strong', 'Decent', 'Weak']:
        n = (df_results['technical'] == assessment).sum()
        print(f"  Technical {assessment}: {n} ({n/total*100:.1f}%)")

    print("\n--- Risk/Macro Distribution ---")
    for assessment in ['Favorable', 'Neutral', 'Unfavorable']:
        n = (df_results['risk_macro'] == assessment).sum()
        print(f"  Risk/Macro {assessment}: {n} ({n/total*100:.1f}%)")

    # 5. Save CSV
    df_results.to_csv(OUTPUT_CSV, index=False)
    print(f"\nFull results saved: {OUTPUT_CSV}")

    # 6. Save markdown report
    _write_md_report(df_results, total, buy_count, hold_count, avoid_count,
                     buy_pct, hold_pct, avoid_pct, agree_pct)

    print(f"Markdown report saved: {OUTPUT_MD}")
    return df_results


def _write_md_report(df, total, buy_count, hold_count, avoid_count,
                     buy_pct, hold_pct, avoid_pct, agree_pct):
    """Write a clean markdown results report."""
    avoids = df[df['sta_verdict'] == 'AVOID'].head(20)
    buys = df[df['sta_verdict'] == 'BUY'].head(20)

    lines = [
        "# Nirmal vs STA — Categorical Assessment Validation",
        "",
        f"**Run Date:** {datetime.now().strftime('%Y-%m-%d')}  ",
        f"**Chat Data:** June 2023 – May 2026  ",
        f"**Total Calls Validated:** {total}  ",
        "",
        "---",
        "",
        "## Headline Result",
        "",
        f"| STA Verdict | Count | % |",
        f"|-------------|-------|---|",
        f"| ✅ BUY (full agreement) | {buy_count} | {buy_pct:.1f}% |",
        f"| 🟡 HOLD (partial agreement) | {hold_count} | {hold_pct:.1f}% |",
        f"| ❌ AVOID (contradiction) | {avoid_count} | {avoid_pct:.1f}% |",
        f"| **Agreement rate (BUY+HOLD)** | **{buy_count+hold_count}** | **{agree_pct:.1f}%** |",
        "",
        "> **Interpretation:**",
        f"> - {buy_pct:.0f}% of Nirmal's calls, STA would have independently flagged as BUY",
        f"> - {hold_pct:.0f}% STA was cautious but not contradicting (HOLD = 'wait for better entry')",
        f"> - {avoid_pct:.0f}% are genuine contradictions — cases worth studying",
        "",
        "---",
        "",
        "## By Year",
        "",
        "| Year | Calls | BUY % | HOLD % | AVOID % |",
        "|------|-------|-------|--------|---------|",
    ]

    for year in sorted(df['year'].unique()):
        yr = df[df['year'] == year]
        n = len(yr)
        b = (yr['sta_verdict'] == 'BUY').sum()
        h = (yr['sta_verdict'] == 'HOLD').sum()
        a = (yr['sta_verdict'] == 'AVOID').sum()
        lines.append(f"| {year} | {n} | {b/n*100:.1f}% | {h/n*100:.1f}% | {a/n*100:.1f}% |")

    lines += [
        "",
        "---",
        "",
        "## Where STA Disagreed (AVOID cases — sample)",
        "",
        "These are the most interesting rows — Nirmal said BUY but STA said AVOID.",
        "Understanding WHY reveals gaps in our logic or valid disagreements.",
        "",
        "| Date | Ticker | TT | RSI | RS | Technical | Fundamental | Risk/Macro | Reason |",
        "|------|--------|----|-----|----|-----------|-------------|------------|--------|",
    ]

    for _, row in avoids.iterrows():
        lines.append(
            f"| {row['date']} | {row['ticker']} | {row['tt_score']}/8 | "
            f"{row['rsi']} | {row['rs_52w']} | {row['technical']} | "
            f"{row['fundamental']} | {row['risk_macro']} | {row['verdict_reason']} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Where STA Agreed (BUY cases — sample)",
        "",
        "| Date | Ticker | TT | RSI | RS | Technical | Fundamental | Risk/Macro |",
        "|------|--------|----|-----|----|-----------|-------------|------------|",
    ]

    for _, row in buys.iterrows():
        lines.append(
            f"| {row['date']} | {row['ticker']} | {row['tt_score']}/8 | "
            f"{row['rsi']} | {row['rs_52w']} | {row['technical']} | "
            f"{row['fundamental']} | {row['risk_macro']} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Technical Assessment Breakdown",
        "",
        "| Technical | Count | % |",
        "|-----------|-------|---|",
    ]
    for assessment in ['Strong', 'Decent', 'Weak']:
        n = (df['technical'] == assessment).sum()
        lines.append(f"| {assessment} | {n} | {n/total*100:.1f}% |")

    lines += [
        "",
        "## Risk/Macro Breakdown",
        "",
        "| Risk/Macro | Count | % |",
        "|------------|-------|---|",
    ]
    for assessment in ['Favorable', 'Neutral', 'Unfavorable']:
        n = (df['risk_macro'] == assessment).sum()
        lines.append(f"| {assessment} | {n} | {n/total*100:.1f}% |")

    lines += [
        "",
        "---",
        "",
        "## What This Means for STA",
        "",
        "- **If BUY% > 60%:** STA is a reliable systematization of Nirmal's intuition.",
        "  Our categorical assessment captures what he does informally.",
        "- **If AVOID% > 30%:** Significant gaps exist — Nirmal sees setups STA misses.",
        "  Likely candidates: gap-fill entries, mean-reversion plays, news catalysts.",
        "- **HOLD cases:** Often correct caution (wrong market environment for entry).",
        "  These may be timing differences, not fundamental disagreements.",
        "",
        "*Full data: `nirmal_validation_results.csv`*",
    ]

    with open(OUTPUT_MD, 'w') as f:
        f.write('\n'.join(lines))


if __name__ == '__main__':
    run_validation()
