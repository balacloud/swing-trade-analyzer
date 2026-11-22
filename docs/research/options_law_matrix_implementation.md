# Options Law Matrix Engine — Complete Implementation Blueprint
### Swing Trade Analyzer | Options Tab v1.0
**Version**: 1.0 | **Date**: February 20, 2026  
**Purpose**: Bake all 7 immutable options laws + swing trade signal into a single emotion-free verdict engine.  
**Architecture fit**: Extends v4.17 (React + Flask). New endpoint `/api/options/<ticker>`. New React tab "Options".

---

## THE CORE IDEA

```
Swing Trade Signal          Options Law Matrix           Final Verdict
────────────────────    +   ───────────────────    =     ─────────────
BUY / HOLD / AVOID          7 Laws × 4 Strategies        DO THIS
Technical: Strong           Each law: ✅ ❌ ⚠️            or
Fundamental: Strong         Checked sequentially         DON'T DO THIS
VIX, SPY, ADX, S/R          No human emotion             with EXACT reason
Pattern, R:R                Runs in < 500ms
```

The system already removes emotions from stock trading. This module does the same for options.

---

## SECTION 1 — BACKEND: `options_engine.py`

New file: `backend/options_engine.py`

```python
"""
Options Law Matrix Engine
Evaluates 4 strategies against 7 immutable laws.
Zero emotion. Zero discretion. Binary output: ELIGIBLE / CAUTION / NOT_ELIGIBLE.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from py_vollib_vectorized import vectorized_black_scholes as vbs
from py_vollib_vectorized.greeks import vectorized_delta, vectorized_theta, vectorized_vega
from cachemanager import get_cached_iv, store_iv_snapshot

RISK_FREE_RATE = 0.05  # Update quarterly — current 3-month T-bill approx

# ─────────────────────────────────────────────────────────────────────────────
# STATUS CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
GREEN  = "green"
YELLOW = "yellow"
RED    = "red"
NA     = "na"  # pre-condition not met, strategy not applicable

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: FETCH OPTIONS CHAIN (Layer 1 data — only new fetch needed)
# ─────────────────────────────────────────────────────────────────────────────
def fetch_options_chain(ticker: str, target_dte_min=30, target_dte_max=60):
    """Fetch chain for the expiry closest to 45 DTE within 30-60 window."""
    try:
        tk = yf.Ticker(ticker)
        expiries = tk.options
        today = pd.Timestamp.today().normalize()

        chosen_expiry = None
        chosen_dte = None
        for exp in expiries:
            dte = (pd.Timestamp(exp) - today).days
            if target_dte_min <= dte <= target_dte_max:
                chosen_expiry = exp
                chosen_dte = dte
                break

        if not chosen_expiry:
            return None

        chain = tk.option_chain(chosen_expiry)
        calls = chain.calls[['strike','bid','ask','volume','openInterest','impliedVolatility']].copy()
        puts  = chain.puts [['strike','bid','ask','volume','openInterest','impliedVolatility']].copy()

        # Compute mid price and spread % for each contract
        for df in [calls, puts]:
            df['mid']      = (df['bid'] + df['ask']) / 2
            df['spread_pct'] = ((df['ask'] - df['bid']) / df['mid'].replace(0, np.nan) * 100).fillna(999)

        return {
            'expiry': chosen_expiry,
            'dte': chosen_dte,
            'calls': calls,
            'puts': puts,
            'chain_volume': int(calls['volume'].fillna(0).sum() + puts['volume'].fillna(0).sum()),
            'chain_oi':     int(calls['openInterest'].fillna(0).sum() + puts['openInterest'].fillna(0).sum()),
        }
    except Exception as e:
        return {'error': str(e)}


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: FIND ATM CONTRACT
# ─────────────────────────────────────────────────────────────────────────────
def get_atm_contract(chain_df: pd.DataFrame, spot: float):
    """Return the single row closest to ATM (nearest strike to spot price)."""
    chain_df = chain_df.copy()
    chain_df['distance'] = (chain_df['strike'] - spot).abs()
    return chain_df.loc[chain_df['distance'].idxmin()]


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: COMPUTE GREEKS (py_vollib — BSM analytical)
# ─────────────────────────────────────────────────────────────────────────────
def compute_greeks(flag: str, S: float, K: float, dte: int, iv: float) -> dict:
    """
    flag: 'c' for call, 'p' for put
    iv: implied volatility as decimal (e.g. 0.25 for 25%)
    Returns dict of delta, theta, vega or None on error.
    """
    try:
        t = max(dte / 365.0, 0.001)  # prevent zero
        r = RISK_FREE_RATE

        delta = float(vectorized_delta(flag, S, K, t, r, iv, model='black_scholes'))
        theta = float(vectorized_theta(flag, S, K, t, r, iv, model='black_scholes'))
        vega  = float(vectorized_vega (flag, S, K, t, r, iv, model='black_scholes'))

        # Theta per day as % of mid premium
        return {
            'delta': round(delta, 4),
            'theta': round(theta, 4),   # $/day per contract (divide by 100 for per-share)
            'vega':  round(vega, 4),
        }
    except Exception as e:
        return {'error': str(e)}


# ─────────────────────────────────────────────────────────────────────────────
# STEP 4: IV RANK (requires SQLite iv_history table)
# ─────────────────────────────────────────────────────────────────────────────
def compute_iv_rank(ticker: str, current_iv: float) -> dict:
    """
    Returns iv_rank (0-100), iv_percentile (0-100), and days_of_history.
    Returns None if insufficient history (< 20 trading days).
    """
    history = get_cached_iv(ticker, days=252)  # get up to 1yr from SQLite

    if not history or len(history) < 20:
        return {'iv_rank': None, 'iv_percentile': None, 'days_of_history': len(history) if history else 0}

    iv_values = [row['atm_iv'] for row in history]
    iv_52w_high = max(iv_values)
    iv_52w_low  = min(iv_values)

    iv_rank = ((current_iv - iv_52w_low) / (iv_52w_high - iv_52w_low) * 100) if iv_52w_high != iv_52w_low else 50
    iv_percentile = (sum(1 for v in iv_values if v < current_iv) / len(iv_values) * 100)

    # Store today's IV snapshot
    store_iv_snapshot(ticker, current_iv)

    return {
        'iv_rank': round(iv_rank, 1),
        'iv_percentile': round(iv_percentile, 1),
        'iv_52w_high': round(iv_52w_high, 4),
        'iv_52w_low': round(iv_52w_low, 4),
        'days_of_history': len(iv_values),
        'current_iv': round(current_iv, 4),
    }


# ─────────────────────────────────────────────────────────────────────────────
# STEP 5: THE LAW CHECKER — returns a check dict for each rule
# ─────────────────────────────────────────────────────────────────────────────
def check(name: str, value, green_fn, yellow_fn, unit="", description="", law_number=None) -> dict:
    """Evaluate a single rule. Returns structured result with status."""
    if green_fn(value):
        status = GREEN
    elif yellow_fn(value):
        status = YELLOW
    else:
        status = RED

    return {
        'name': name,
        'value': value,
        'unit': unit,
        'status': status,
        'description': description,
        'law': law_number,
    }


# ─────────────────────────────────────────────────────────────────────────────
# STEP 6: UNIVERSAL DISQUALIFIERS (run before any strategy)
# ─────────────────────────────────────────────────────────────────────────────
def run_universal_disqualifiers(stock_data: dict, chain_data: dict, iv_data: dict) -> dict:
    """
    Returns: { passed: bool, checks: [...], blocking_reason: str | None }
    If passed=False, do not run any strategy checklist.
    """
    spot        = stock_data['currentPrice']
    avg_vol     = stock_data.get('avgVolume', 0)
    vix         = stock_data.get('vix', 20)
    earnings_days = stock_data.get('daysToEarnings', 999)
    quote_type  = stock_data.get('quoteType', 'EQUITY')
    iv_pct      = iv_data.get('iv_percentile')
    chain_vol   = chain_data.get('chain_volume', 0) if chain_data else 0

    checks = [
        check("Stock price ≥ $20",       spot,
              lambda v: v >= 20, lambda v: 10 <= v < 20, unit="$",
              description="Sub-$20 stocks have poor options microstructure",
              law_number="U1"),

        check("Avg daily stock volume ≥ 500K", avg_vol/1e6,
              lambda v: v >= 1.0, lambda v: 0.5 <= v < 1.0, unit="M shares",
              description="Low underlying volume = illiquid options chain",
              law_number="U2"),

        check("Options chain volume ≥ 200", chain_vol,
              lambda v: v >= 500, lambda v: 200 <= v < 500, unit="contracts",
              description="Minimum chain activity required for viable execution",
              law_number="U3"),

        check("VIX below extreme levels", vix,
              lambda v: v < 30, lambda v: 30 <= v <= 40, unit="",
              description="VIX > 40 = panic regime, all options structurally overpriced",
              law_number="U4"),

        check("Earnings ≥ 5 days away", earnings_days,
              lambda v: v > 10, lambda v: 5 < v <= 10, unit="days",
              description="≤5 days: IV spike risk overwhelms any directional signal",
              law_number="U5"),

        check("Not leveraged ETF / ETN", 1 if quote_type == 'EQUITY' else 0,
              lambda v: v == 1, lambda v: False, unit="",
              description="Leveraged ETFs have path-dependent, non-standard options behavior",
              law_number="U6"),
    ]

    # IV Percentile only if we have history
    if iv_pct is not None:
        checks.append(check(
            "IV Percentile ≤ 95 (extreme)", iv_pct,
            lambda v: v < 85, lambda v: 85 <= v < 95, unit="%ile",
            description="IV > 95th percentile: buying options is almost always negative EV",
            law_number="U7"
        ))

    blocking = [c for c in checks if c['status'] == RED]
    passed = len(blocking) == 0

    return {
        'passed': passed,
        'checks': checks,
        'blocking_reason': blocking[0]['name'] if blocking else None
    }


# ─────────────────────────────────────────────────────────────────────────────
# STEP 7: INDIVIDUAL STRATEGY CHECKLISTS (all 4 strategies)
# ─────────────────────────────────────────────────────────────────────────────

def checklist_long_call(stock_data: dict, chain_data: dict, atm_call: dict,
                         greeks: dict, iv_data: dict, account_size: float) -> dict:
    """
    Strategy 1: Long Call (Call Buy)
    Pre-condition: Verdict = BUY, Technical = Strong
    Law focus: Law 1 (IV), Law 2 (Theta), Law 3 (Earnings), Law 4 (Liquidity), Law 5 (Sizing)
    """
    # Pre-condition gate
    if stock_data.get('verdict') != 'BUY' or stock_data.get('technical') != 'Strong':
        return {'applicable': False, 'reason': 'Requires BUY verdict + Strong Technical'}

    spot          = stock_data['currentPrice']
    adx           = stock_data.get('adx', 0)
    vix           = stock_data.get('vix', 20)
    spy_regime    = stock_data.get('spyAbove200', True)
    r1            = stock_data.get('r1', spot * 1.08)
    earnings_days = stock_data.get('daysToEarnings', 999)

    dte           = chain_data['dte']
    iv_rank       = iv_data.get('iv_rank')

    atm_mid       = atm_call.get('mid', 0)
    atm_vol       = atm_call.get('volume', 0)
    atm_oi        = atm_call.get('openInterest', 0)
    atm_spread    = atm_call.get('spread_pct', 999)
    atm_iv        = atm_call.get('impliedVolatility', 0.25)

    delta         = abs(greeks.get('delta', 0)) if greeks else 0
    theta_day     = abs(greeks.get('theta', 0)) / 100 if greeks else 0  # per share per day
    theta_pct     = (theta_day / atm_mid * 100) if atm_mid > 0 else 999

    r1_gap        = r1 - spot
    rr_vs_premium = (r1_gap / atm_mid) if atm_mid > 0 else 0
    premium_pct   = (atm_mid * 100 / account_size * 100) if account_size > 0 else 999

    checks = [
        # LAW 1 — IV Rank
        check("IV Rank ≤ 40 (Law 1: No expensive vol)", iv_rank if iv_rank is not None else -1,
              lambda v: v != -1 and v <= 40, lambda v: v != -1 and 40 < v <= 60, unit="/100",
              description="High IV = paying inflated premium. Even correct direction can lose to IV crush.",
              law_number=1),

        # LAW 2 — Theta
        check("Theta cost < 0.5%/day (Law 2: Time decay)", theta_pct,
              lambda v: v < 0.5, lambda v: 0.5 <= v < 1.0, unit="%/day",
              description="Daily theta > 1% of premium means time is destroying value faster than expected move.",
              law_number=2),

        # LAW 2 — DTE
        check("DTE 30–60 days (Law 2: Theta window)", dte,
              lambda v: 30 <= v <= 60, lambda v: 20 <= v < 30 or 60 < v <= 90, unit="days",
              description="< 20 DTE = theta acceleration kills long options. > 90 DTE = overpaying for time.",
              law_number=2),

        # LAW 3 — Earnings
        check("Earnings > 10 days away (Law 3: IV crush)", earnings_days,
              lambda v: v > 10, lambda v: 5 < v <= 10, unit="days",
              description="Earnings IV crush can cause 50-80% loss on correct directional call.",
              law_number=3),

        # LAW 4 — Liquidity
        check("Bid-ask spread ≤ 5% (Law 4: Liquidity)", atm_spread,
              lambda v: v <= 5, lambda v: 5 < v <= 8, unit="%",
              description="Wide spread = guaranteed transaction cost before trade even starts.",
              law_number=4),

        check("ATM volume ≥ 50 (Law 4: Liquidity)", atm_vol if atm_vol else 0,
              lambda v: v >= 50, lambda v: 20 <= v < 50, unit="contracts",
              description="Low volume = poor fills and wide real-world spreads.",
              law_number=4),

        check("ATM open interest ≥ 500 (Law 4: Liquidity)", atm_oi if atm_oi else 0,
              lambda v: v >= 500, lambda v: 200 <= v < 500, unit="contracts",
              description="Low OI = difficulty exiting position before expiry.",
              law_number=4),

        # LAW 5 — Position sizing
        check("Premium ≤ 2% of account (Law 5: Sizing)", premium_pct,
              lambda v: v <= 2.0, lambda v: 2.0 < v <= 3.0, unit="% of account",
              description="Options can lose 100% of premium. Size accordingly.",
              law_number=5),

        # DIRECTIONAL QUALITY (from swing trade engine)
        check("ADX ≥ 25 (trend strength)", adx,
              lambda v: v >= 25, lambda v: 20 <= v < 25, unit="",
              description="ADX < 20 = no trend to trade. Options need directional momentum.",
              law_number="ST"),

        check("Delta 0.40–0.60 (ATM zone)", delta,
              lambda v: 0.40 <= v <= 0.60, lambda v: 0.35 <= v < 0.40, unit="Δ",
              description="Delta < 0.30 = lottery ticket. Delta > 0.70 = paying for intrinsic only.",
              law_number="ST"),

        check("R1 gap ≥ 1.5× premium (R:R viable)", rr_vs_premium,
              lambda v: v >= 1.5, lambda v: 1.2 <= v < 1.5, unit="×",
              description="Stock's resistance target must justify option premium cost.",
              law_number="ST"),

        check("SPY regime: above 200 SMA", 1 if spy_regime else 0,
              lambda v: v == 1, lambda v: False, unit="",
              description="Trading long calls in bear market = fighting the primary trend.",
              law_number="ST"),
    ]

    return _finalize_strategy("Long Call", checks, {
        'expiry': chain_data['expiry'],
        'dte': dte,
        'suggested_strike': atm_call.get('strike'),
        'mid_price': round(atm_mid, 2),
        'delta': round(delta, 3),
        'theta_per_day': round(theta_day, 3),
        'exit_price': round(atm_mid * 0.5, 2),    # Law 6: 50% stop
        'max_gain_target': round(atm_mid * 2.0, 2), # 2R target
        'expected_move': round(spot * atm_iv * (dte/365)**0.5, 2),
        'iv_rank': iv_rank,
    })


def checklist_covered_call(stock_data: dict, chain_data: dict, atm_call: dict,
                            greeks: dict, iv_data: dict, owns_shares: bool) -> dict:
    """
    Strategy 2: Covered Call (Call Sell)
    Pre-condition: Verdict = HOLD or neutral BUY, AND owns_shares = True
    Law focus: Law 1 (IV — sell when high), Law 3 (Earnings), Law 4 (Liquidity), Law 7 (Regime)
    """
    if not owns_shares:
        return {'applicable': False, 'reason': 'Requires owning ≥ 100 shares (toggle in Settings)'}

    if stock_data.get('verdict') not in ['HOLD', 'BUY']:
        return {'applicable': False, 'reason': 'Requires HOLD or BUY verdict'}

    spot          = stock_data['currentPrice']
    r1            = stock_data.get('r1', spot * 1.08)
    vix           = stock_data.get('vix', 20)
    earnings_days = stock_data.get('daysToEarnings', 999)
    adx           = stock_data.get('adx', 0)

    dte           = chain_data['dte']
    iv_rank       = iv_data.get('iv_rank')

    # For covered calls, pick OTM strike above R1
    calls_df      = chain_data['calls']
    otm_calls     = calls_df[calls_df['strike'] > r1].head(3)
    if otm_calls.empty:
        otm_calls = calls_df[calls_df['strike'] > spot * 1.05].head(3)

    if otm_calls.empty:
        return {'applicable': False, 'reason': 'No suitable OTM strike found above resistance'}

    target_call   = otm_calls.iloc[0]
    strike        = target_call['strike']
    otm_pct       = ((strike / spot) - 1) * 100
    atm_spread    = target_call.get('spread_pct', target_call['spread_pct'] if 'spread_pct' in target_call else 999)
    atm_oi        = target_call.get('openInterest', 0)

    delta         = abs(greeks.get('delta', 0.5)) if greeks else 0.5

    checks = [
        # LAW 1 (inverted for sellers) — sell when IV is HIGH
        check("IV Rank ≥ 40 (Law 1: Sell rich premium)", iv_rank if iv_rank is not None else -1,
              lambda v: v != -1 and v >= 60, lambda v: v != -1 and 40 <= v < 60, unit="/100",
              description="Selling options when IV is low = collecting too little premium for the risk taken.",
              law_number=1),

        # LAW 3 — Earnings (assignment gap risk)
        check("Earnings > 10 days away (Law 3: Gap risk)", earnings_days,
              lambda v: v > 10, lambda v: 5 < v <= 10, unit="days",
              description="Earnings can gap stock above strike, forcing early assignment at suboptimal price.",
              law_number=3),

        # LAW 4 — Liquidity
        check("Bid-ask spread ≤ 5% (Law 4: Liquidity)", atm_spread,
              lambda v: v <= 5, lambda v: 5 < v <= 8, unit="%",
              description="Wide spread means poor fill on covered call and on potential roll.",
              law_number=4),

        check("Open interest ≥ 500 (Law 4: Liquidity)", atm_oi if atm_oi else 0,
              lambda v: v >= 500, lambda v: 200 <= v < 500, unit="contracts",
              description="Low OI makes rolling difficult if stock approaches strike.",
              law_number=4),

        # LAW 7 — Regime (IV regime for seller)
        check("DTE 20–45 days (Law 7: Theta sweet spot)", dte,
              lambda v: 20 <= v <= 45, lambda v: 15 <= v < 20 or 45 < v <= 60, unit="days",
              description="20-45 DTE is theta decay sweet spot for covered call sellers.",
              law_number=7),

        check("Strike OTM 5–15% (assignment buffer)", otm_pct,
              lambda v: 5 <= v <= 15, lambda v: 2 <= v < 5 or 15 < v <= 20, unit="%",
              description="< 5% OTM = high assignment risk. > 15% = too little premium to justify.",
              law_number="ST"),

        check("Strike above R1 (resistance buffer)", 1 if strike >= r1 else 0,
              lambda v: v == 1, lambda v: False, unit="",
              description="Selling call below resistance risks being assigned before stock hits your target.",
              law_number="ST"),

        check("Call delta 0.20–0.35 (assignment probability)", delta,
              lambda v: 0.20 <= v <= 0.35, lambda v: 0.35 < v <= 0.45, unit="Δ",
              description="Delta approximates probability of assignment. > 0.45 = too risky of being called away.",
              law_number="ST"),

        check("ADX ≥ 20 (has directional context)", adx,
              lambda v: v >= 20, lambda v: 15 <= v < 20, unit="",
              description="Selling calls in directionless chop without context risks missing upside.",
              law_number="ST"),
    ]

    mid = float(target_call.get('mid', target_call['mid'] if 'mid' in target_call else 0))
    return _finalize_strategy("Covered Call", checks, {
        'expiry': chain_data['expiry'],
        'dte': dte,
        'suggested_strike': float(strike),
        'premium_collected': round(mid, 2),
        'delta': round(delta, 3),
        'otm_pct': round(otm_pct, 1),
        'max_profit': round(mid * 100, 2),   # per contract
        'assignment_price': float(strike),
        'close_at': round(mid * 0.25, 2),   # close at 75% profit (take most of theta)
        'iv_rank': iv_rank,
    })


def checklist_long_put(stock_data: dict, chain_data: dict, atm_put: dict,
                        greeks: dict, iv_data: dict, account_size: float) -> dict:
    """
    Strategy 3: Long Put (Put Buy)
    Pre-condition: Verdict = AVOID, Technical = Weak
    Law focus: Law 1 (IV — don't buy expensive fear), Law 2 (Theta), Law 3 (Earnings)
    """
    if stock_data.get('verdict') != 'AVOID' or stock_data.get('technical') != 'Weak':
        return {'applicable': False, 'reason': 'Requires AVOID verdict + Weak Technical'}

    spot          = stock_data['currentPrice']
    s1            = stock_data.get('s1', spot * 0.92)
    s2            = stock_data.get('s2', spot * 0.85)
    adx           = stock_data.get('adx', 0)
    vix           = stock_data.get('vix', 20)
    earnings_days = stock_data.get('daysToEarnings', 999)

    dte           = chain_data['dte']
    iv_rank       = iv_data.get('iv_rank')

    atm_mid       = atm_put.get('mid', 0)
    atm_spread    = atm_put.get('spread_pct', 999)
    atm_oi        = atm_put.get('openInterest', 0)
    atm_vol       = atm_put.get('volume', 0)
    atm_iv        = atm_put.get('impliedVolatility', 0.25)

    delta         = abs(greeks.get('delta', 0)) if greeks else 0
    theta_day     = abs(greeks.get('theta', 0)) / 100 if greeks else 0
    theta_pct     = (theta_day / atm_mid * 100) if atm_mid > 0 else 999
    premium_pct   = (atm_mid * 100 / account_size * 100) if account_size > 0 else 999

    checks = [
        # LAW 1 — Puts are EXTRA expensive during fear (do NOT buy when VIX is already spiked)
        check("IV Rank ≤ 40 (Law 1: Puts expensive in fear)", iv_rank if iv_rank is not None else -1,
              lambda v: v != -1 and v <= 40, lambda v: v != -1 and 40 < v <= 60, unit="/100",
              description="Puts price fear premium. Buying when IV > 60 = paying maximum for protection.",
              law_number=1),

        check("VIX ≤ 25 (Law 1: Fear not yet extreme)", vix,
              lambda v: v <= 25, lambda v: 25 < v <= 35, unit="",
              description="VIX > 35 = panic pricing. Puts are structurally overpriced at these levels.",
              law_number=1),

        # LAW 2 — Theta
        check("Theta cost < 0.5%/day (Law 2: Time decay)", theta_pct,
              lambda v: v < 0.5, lambda v: 0.5 <= v < 1.0, unit="%/day",
              description="Theta destroys long put value regardless of price direction.",
              law_number=2),

        check("DTE 30–75 days (Law 2: Theta window)", dte,
              lambda v: 30 <= v <= 75, lambda v: 20 <= v < 30, unit="days",
              description="Longer DTE needed for put buyers to weather consolidation before breakdown.",
              law_number=2),

        # LAW 3 — Earnings
        check("Earnings > 10 days (Law 3: IV crush)", earnings_days,
              lambda v: v > 10, lambda v: 5 < v <= 10, unit="days",
              description="Post-earnings IV crush kills puts even when stock moves down.",
              law_number=3),

        # LAW 4 — Liquidity
        check("Bid-ask spread ≤ 5% (Law 4: Liquidity)", atm_spread,
              lambda v: v <= 5, lambda v: 5 < v <= 8, unit="%",
              description="Wide spreads are 2× as common on puts vs calls — extra vigilance needed.",
              law_number=4),

        check("ATM put volume ≥ 50 (Law 4: Liquidity)", atm_vol if atm_vol else 0,
              lambda v: v >= 50, lambda v: 20 <= v < 50, unit="contracts",
              law_number=4),

        # LAW 5 — Sizing
        check("Premium ≤ 5% of account (Law 5: Put cap)", premium_pct,
              lambda v: v <= 5.0, lambda v: 5.0 < v <= 8.0, unit="% of account",
              description="Long puts have negative EV as insurance — cap aggregate allocation.",
              law_number=5),

        # DIRECTIONAL QUALITY
        check("ADX ≥ 20 (downtrend confirmed)", adx,
              lambda v: v >= 20, lambda v: 15 <= v < 20, unit="",
              description="ADX < 15 = no trend. Don't buy directional puts in choppy market.",
              law_number="ST"),

        check("Put delta 0.35–0.55 (meaningful delta)", delta,
              lambda v: 0.35 <= v <= 0.55, lambda v: 0.25 <= v < 0.35, unit="Δ",
              description="Delta < 0.25 = deep OTM lottery. Delta > 0.60 = expensive intrinsic value.",
              law_number="ST"),
    ]

    return _finalize_strategy("Long Put", checks, {
        'expiry': chain_data['expiry'],
        'dte': dte,
        'suggested_strike': atm_put.get('strike'),
        'mid_price': round(atm_mid, 2),
        'delta': round(delta, 3),
        'theta_per_day': round(theta_day, 3),
        'exit_price': round(atm_mid * 0.5, 2),
        'target_support': round(s2, 2),
        'iv_rank': iv_rank,
    })


def checklist_cash_secured_put(stock_data: dict, chain_data: dict,
                                iv_data: dict, account_size: float,
                                willing_to_own: bool) -> dict:
    """
    Strategy 4: Cash-Secured Put (Put Sell)
    Pre-condition: Verdict = BUY/HOLD, willing_to_own = True, price extended above R1
    Law focus: Law 1 (IV — sell when high), Law 3 (Earnings), Law 5 (Sizing), Law 7 (Regime)
    """
    if not willing_to_own:
        return {'applicable': False, 'reason': 'Requires "Willing to own shares" toggle enabled'}

    if stock_data.get('verdict') not in ['BUY', 'HOLD']:
        return {'applicable': False, 'reason': 'Requires BUY or HOLD verdict (must be willing to own)'}

    if stock_data.get('fundamental') == 'Weak':
        return {'applicable': False, 'reason': 'Weak fundamentals — would not want assignment of these shares'}

    spot          = stock_data['currentPrice']
    s1            = stock_data.get('s1', spot * 0.93)
    vix           = stock_data.get('vix', 20)
    earnings_days = stock_data.get('daysToEarnings', 999)

    dte           = chain_data['dte']
    iv_rank       = iv_data.get('iv_rank')

    # Select put strike at or below S1 (5-15% OTM)
    puts_df       = chain_data['puts']
    otm_puts      = puts_df[puts_df['strike'] <= s1].sort_values('strike', ascending=False).head(3)
    if otm_puts.empty:
        otm_puts  = puts_df[puts_df['strike'] < spot * 0.93].head(3)

    if otm_puts.empty:
        return {'applicable': False, 'reason': 'No suitable put strike found below support'}

    target_put    = otm_puts.iloc[0]
    strike        = float(target_put['strike'])
    mid           = float(target_put.get('mid', 0))
    otm_pct       = ((spot - strike) / spot) * 100
    spread_pct    = float(target_put.get('spread_pct', 999))
    oi            = float(target_put.get('openInterest', 0))

    obligation    = strike * 100  # per contract
    obligation_pct = (obligation / account_size * 100) if account_size > 0 else 999

    checks = [
        # LAW 1 (inverted) — sell when IV is HIGH = rich premium
        check("IV Rank ≥ 50 (Law 1: Sell rich premium)", iv_rank if iv_rank is not None else -1,
              lambda v: v != -1 and v >= 50, lambda v: v != -1 and 35 <= v < 50, unit="/100",
              description="Selling puts when IV is low = poor premium for risk taken.",
              law_number=1),

        # LAW 3 — Earnings (gap-through-strike risk)
        check("Earnings > 10 days (Law 3: Gap risk)", earnings_days,
              lambda v: v > 10, lambda v: 5 < v <= 10, unit="days",
              description="Earnings gaps can blow through your put strike, assigning shares at a loss.",
              law_number=3),

        # LAW 4 — Liquidity
        check("Bid-ask spread ≤ 5% (Law 4: Liquidity)", spread_pct,
              lambda v: v <= 5, lambda v: 5 < v <= 8, unit="%",
              law_number=4),

        check("Open interest ≥ 500 (Law 4: Liquidity)", oi,
              lambda v: v >= 500, lambda v: 200 <= v < 500, unit="contracts",
              law_number=4),

        # LAW 5 — Capital obligation sizing
        check("Cash obligation ≤ 20% of account (Law 5)", obligation_pct,
              lambda v: v <= 20, lambda v: 20 < v <= 25, unit="% of account",
              description="Total assignment risk must not over-concentrate your capital.",
              law_number=5),

        # LAW 7 — Regime
        check("DTE 20–60 days (Law 7: Theta optimization)", dte,
              lambda v: 20 <= v <= 60, lambda v: 15 <= v < 20 or 60 < v <= 75, unit="days",
              law_number=7),

        check("VIX ≤ 30 (Law 7: Gap risk manageable)", vix,
              lambda v: v <= 30, lambda v: 25 < v <= 30, unit="",
              description="High VIX = high gap risk through strike, forced assignment at loss.",
              law_number=7),

        # DIRECTIONAL / QUALITY CHECKS
        check("Strike at/below S1 (support buffer)", 1 if strike <= s1 else 0,
              lambda v: v == 1, lambda v: False, unit="",
              description="Strike below support = assignment at a price you'd want to buy anyway.",
              law_number="ST"),

        check("Strike 5–15% OTM (buffer zone)", otm_pct,
              lambda v: 5 <= v <= 15, lambda v: 3 <= v < 5 or 15 < v <= 20, unit="%",
              description="< 3% OTM = near-certain assignment. > 15% = too little premium.",
              law_number="ST"),

        check("Fundamental quality: not Weak", 0 if stock_data.get('fundamental') == 'Weak' else 1,
              lambda v: v == 1, lambda v: False, unit="",
              description="Assignment of fundamentally weak stocks is value destruction.",
              law_number="ST"),
    ]

    return _finalize_strategy("Cash-Secured Put", checks, {
        'expiry': chain_data['expiry'],
        'dte': dte,
        'suggested_strike': strike,
        'premium_collected': round(mid, 2),
        'cash_required': round(obligation, 2),
        'obligation_pct': round(obligation_pct, 1),
        'otm_pct': round(otm_pct, 1),
        'close_at': round(mid * 0.25, 2),  # Close at 75% profit
        'break_even': round(strike - mid, 2),
        'loss_exit': round(mid * 2.0, 2),  # Law 6: 2× premium rule
        'iv_rank': iv_rank,
    })


# ─────────────────────────────────────────────────────────────────────────────
# STEP 8: FINALIZE STRATEGY — badge assignment + summary
# ─────────────────────────────────────────────────────────────────────────────
def _finalize_strategy(name: str, checks: list, contract_details: dict) -> dict:
    reds    = [c for c in checks if c['status'] == RED]
    yellows = [c for c in checks if c['status'] == YELLOW]

    if reds:
        badge   = RED
        verdict = "NOT ELIGIBLE"
        reason  = f"Failed: {reds[0]['name']}"
    elif len(yellows) >= 2:
        badge   = YELLOW
        verdict = "CAUTION"
        reason  = f"{len(yellows)} warnings — proceed with reduced size"
    else:
        badge   = GREEN
        verdict = "ELIGIBLE"
        reason  = "All critical laws pass"

    return {
        'applicable': True,
        'strategy': name,
        'badge': badge,
        'verdict': verdict,
        'reason': reason,
        'red_count': len(reds),
        'yellow_count': len(yellows),
        'checks': checks,
        'contract': contract_details,
    }


# ─────────────────────────────────────────────────────────────────────────────
# STEP 9: MASTER ORCHESTRATOR — called by Flask endpoint
# ─────────────────────────────────────────────────────────────────────────────
def run_options_law_matrix(ticker: str, stock_data: dict, account_size: float,
                            owns_shares: bool = False,
                            willing_to_own: bool = False) -> dict:
    """
    Master function. Called by /api/options/<ticker>.
    stock_data: merged dict from existing /api/stock, /api/sr, /api/market/vix, /api/fundamentals
    Returns full law matrix result for all 4 strategies.
    """
    # Fetch options chain (Layer 1 — new data)
    chain_data = fetch_options_chain(ticker)

    if not chain_data or 'error' in chain_data:
        return {'error': 'Options chain unavailable', 'details': chain_data}

    spot = stock_data['currentPrice']
    dte  = chain_data['dte']

    # Get ATM contracts
    atm_call = get_atm_contract(chain_data['calls'], spot).to_dict()
    atm_put  = get_atm_contract(chain_data['puts'], spot).to_dict()

    # Compute Greeks
    call_iv = atm_call.get('impliedVolatility', 0.25)
    put_iv  = atm_put.get('impliedVolatility', 0.25)
    call_greeks = compute_greeks('c', spot, atm_call['strike'], dte, call_iv)
    put_greeks  = compute_greeks('p', spot, atm_put['strike'], dte, put_iv)

    # IV Rank (requires SQLite history)
    iv_data = compute_iv_rank(ticker, call_iv)

    # Universal Disqualifiers
    universal = run_universal_disqualifiers(stock_data, chain_data, iv_data)

    # Individual strategy checklists
    strategies = {}
    if universal['passed']:
        strategies['long_call']        = checklist_long_call(stock_data, chain_data, atm_call, call_greeks, iv_data, account_size)
        strategies['covered_call']     = checklist_covered_call(stock_data, chain_data, atm_call, call_greeks, iv_data, owns_shares)
        strategies['long_put']         = checklist_long_put(stock_data, chain_data, atm_put, put_greeks, iv_data, account_size)
        strategies['cash_secured_put'] = checklist_cash_secured_put(stock_data, chain_data, iv_data, account_size, willing_to_own)
    else:
        for s in ['long_call','covered_call','long_put','cash_secured_put']:
            strategies[s] = {'applicable': False, 'reason': f"Universal disqualifier: {universal['blocking_reason']}"}

    # Summary strip
    summary = {k: {'badge': v.get('badge', NA), 'verdict': v.get('verdict', 'N/A'), 'applicable': v.get('applicable', False)}
               for k, v in strategies.items()}

    return {
        'ticker': ticker,
        'timestamp': datetime.utcnow().isoformat(),
        'spot': spot,
        'expiry': chain_data['expiry'],
        'dte': dte,
        'iv_data': iv_data,
        'universal': universal,
        'strategies': strategies,
        'summary': summary,
    }
```

---

## SECTION 2 — FLASK ENDPOINT: `backend.py` addition

```python
# Add to backend.py

from options_engine import run_options_law_matrix

@app.route('/api/options/<ticker>', methods=['GET'])
def get_options_analysis(ticker):
    """
    Options Law Matrix endpoint.
    Merges existing stock data with new options chain analysis.
    Query params:
      - account_size: float (default 10000)
      - owns_shares: bool (default false) — for Covered Call
      - willing_to_own: bool (default false) — for CSP
    """
    account_size  = float(request.args.get('account_size', 10000))
    owns_shares   = request.args.get('owns_shares', 'false').lower() == 'true'
    willing_to_own = request.args.get('willing_to_own', 'false').lower() == 'true'

    # Gather all existing stock data (your existing functions)
    stock_raw      = get_stock_data(ticker)       # existing
    fundamentals   = get_fundamentals(ticker)     # existing
    sr_data        = get_sr_levels(ticker)        # existing
    vix_data       = get_vix()                    # existing
    spy_data       = get_spy_regime()             # existing
    earnings_data  = get_earnings_date(ticker)    # existing (7-day warning already there)

    # Merge into single stock_data dict for options engine
    stock_data = {
        'currentPrice': stock_raw['currentPrice'],
        'avgVolume': stock_raw.get('avgVolume', 0),
        'verdict': stock_raw.get('verdict'),           # BUY / HOLD / AVOID
        'technical': stock_raw.get('technical'),       # Strong / Decent / Weak
        'fundamental': fundamentals.get('fundamental'),
        'adx': stock_raw.get('adx', 0),
        'rsi': stock_raw.get('rsi', 50),
        'vix': vix_data.get('vix', 20),
        'spyAbove200': spy_data.get('above200sma', True),
        'r1': sr_data.get('resistance', [{}])[0].get('level', stock_raw['currentPrice'] * 1.08),
        's1': sr_data.get('support', [{}])[0].get('level', stock_raw['currentPrice'] * 0.92),
        's2': sr_data.get('support', [{}])[1].get('level', stock_raw['currentPrice'] * 0.85) if len(sr_data.get('support', [])) > 1 else stock_raw['currentPrice'] * 0.85,
        'daysToEarnings': earnings_data.get('daysToEarnings', 999),
        'quoteType': stock_raw.get('quoteType', 'EQUITY'),
    }

    result = run_options_law_matrix(ticker, stock_data, account_size, owns_shares, willing_to_own)
    return jsonify(result)
```

---

## SECTION 3 — SQLITE: `cachemanager.py` additions

```python
# Add to cachemanager.py

def init_iv_table():
    """Add iv_history table to existing SQLite cache DB."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS iv_history (
                ticker TEXT NOT NULL,
                date   TEXT NOT NULL,
                atm_iv REAL NOT NULL,
                PRIMARY KEY (ticker, date)
            )
        """)
        conn.commit()

def store_iv_snapshot(ticker: str, atm_iv: float):
    today = datetime.utcnow().strftime('%Y-%m-%d')
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT OR REPLACE INTO iv_history (ticker, date, atm_iv) VALUES (?,?,?)",
            (ticker.upper(), today, atm_iv)
        )
        conn.commit()

def get_cached_iv(ticker: str, days: int = 252) -> list:
    cutoff = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%d')
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT date, atm_iv FROM iv_history WHERE ticker=? AND date>=? ORDER BY date ASC",
            (ticker.upper(), cutoff)
        ).fetchall()
    return [{'date': r[0], 'atm_iv': r[1]} for r in rows]
```

---

## SECTION 4 — REACT: `OptionsTab.jsx` UI Structure

```jsx
// frontend/src/components/OptionsTab.jsx
// Consumes /api/options/<ticker> response

// Summary Strip (top of tab)
<div className="options-summary-strip">
  {['long_call','covered_call','long_put','cash_secured_put'].map(strategy => (
    <StrategyBadge
      key={strategy}
      name={STRATEGY_LABELS[strategy]}
      badge={data.summary[strategy].badge}     // green / yellow / red / na
      verdict={data.summary[strategy].verdict} // ELIGIBLE / CAUTION / NOT ELIGIBLE / N/A
      applicable={data.summary[strategy].applicable}
    />
  ))}
</div>

// Universal Disqualifiers Banner (if not passed)
{!data.universal.passed && (
  <div className="red-banner">
    ⛔ Options Not Available — {data.universal.blocking_reason}
    <ChecklistRow checks={data.universal.checks} />
  </div>
)}

// IV Context Bar
<IVContextBar
  ivRank={data.iv_data.iv_rank}
  ivPercentile={data.iv_data.iv_percentile}
  daysOfHistory={data.iv_data.days_of_history}
  currentIV={data.iv_data.current_iv}
/>

// Strategy Cards (one per strategy)
{Object.entries(data.strategies).map(([key, strategy]) => (
  <StrategyCard
    key={key}
    strategy={strategy}
    onToggleChecklist={() => toggleExpanded(key)}
  />
))}
```

```jsx
// StrategyCard renders:
// ┌─────────────────────────────────────────────┐
// │ 🟢 Long Call       ELIGIBLE                 │
// │ Expiry: Apr 17 (45 DTE) | Strike: $125      │
// │ Delta: 0.51 | Theta: -$3.20/day             │
// │ Exit if < $1.75 (50% stop) | Max: $7.00 (2R)│
// │                              [▼ Show Checks] │
// └─────────────────────────────────────────────┘
//
// Expanded checklist:
// ✅ IV Rank: 34/100 ≤ 40          [Law 1]
// ✅ Theta: 0.38%/day < 0.5%       [Law 2]
// ✅ DTE: 45 days (30-60 range)    [Law 2]
// ✅ Earnings: 28 days away         [Law 3]
// ✅ Bid-ask spread: 3.2% ≤ 5%     [Law 4]
// ⚠️ ATM volume: 42 (target ≥ 50) [Law 4]
// ✅ Premium: 1.8% of account       [Law 5]
// ✅ ADX: 33.5 ≥ 25                [Swing]
// ✅ Delta: 0.51 (0.40-0.60)       [Swing]
// ✅ R1 gap: 2.8× premium           [Swing]
// ✅ SPY above 200 SMA              [Swing]
```

---

## SECTION 5 — CONTEXTUAL WARNINGS (React, inline)

```jsx
// Auto-generated warnings — appear above the strategy card that triggers them

const getWarnings = (strategy, ivData, stockData) => {
  const warnings = [];

  if (ivData.iv_rank > 60) warnings.push({
    level: 'danger',
    text: `IV Rank ${ivData.iv_rank}/100 — Options are expensive. IV crush may cause losses even with correct direction.`
  });

  if (stockData.daysToEarnings <= 10) warnings.push({
    level: 'danger',
    text: `Earnings in ${stockData.daysToEarnings} days. IV spike + crush creates binary risk independent of direction.`
  });

  if (strategy.contract?.spread_pct > 5) warnings.push({
    level: 'warning',
    text: `Bid-ask spread ${strategy.contract.spread_pct.toFixed(1)}% — You pay this cost before the trade begins.`
  });

  if (strategy.badge === 'green') warnings.push({
    level: 'info',
    text: `Pre-defined exit: $${strategy.contract.exit_price} (50% of premium). Set this as your stop BEFORE entry.`
  });

  return warnings;
};
```

---

## SECTION 6 — THE 7 LAWS REFERENCE (baked into tooltips)

| Law | Applied To | What It Prevents |
|---|---|---|
| **Law 1: Never Buy Expensive Vol** | Long Call, Long Put | IV crush destroying directionally correct trades |
| **Law 1 (inverted): Sell Rich Premium** | Covered Call, CSP | Collecting too little premium for the risk |
| **Law 2: Theta is a Guaranteed Tax** | Long Call, Long Put | Time decay destroying value before move materializes |
| **Law 3: Never Hold Through Earnings** | All 4 strategies | Binary event destroying options value regardless of outcome |
| **Law 4: Liquidity Non-Negotiable** | All 4 strategies | Wide spreads / poor fills eliminating edge |
| **Law 5: Options Sizing** | Long Call, Long Put, CSP | 100% premium loss / over-obligation destroying account |
| **Law 6: Never Average Down** | (Display only, not a check) | Emotional averaging into decaying asset |
| **Law 7: Strategy × Regime Matrix** | All 4 strategies | Using wrong strategy for current IV environment |

---

## SECTION 7 — BUILD ORDER

```
Day 1: Backend foundation
  □ Add iv_history table to cachemanager.py (init_iv_table)
  □ Create options_engine.py (copy from Section 1)
  □ pip install py-vollib-vectorized
  □ Add /api/options/<ticker> to backend.py
  □ Test with: curl "localhost:5001/api/options/WMT?account_size=50000"

Day 2: Verify engine output
  □ Test on WMT (liquid, BUY signal) — expect Long Call: GREEN
  □ Test on low-IV HOLD stock — expect Covered Call: YELLOW (IV too low)
  □ Test on high-VIX date simulation — expect all long options: RED
  □ Test on stock within 5 days of earnings — expect U5 disqualifier: RED

Day 3: React frontend
  □ Create OptionsTab.jsx
  □ Add "Options" tab to App.jsx navigation
  □ Build StrategyBadge component (green/yellow/red/na)
  □ Build ChecklistRow component (icon + name + value + threshold)
  □ Build IVContextBar component (shows history progress)
  □ Wire user toggles: owns_shares, willing_to_own → passed to API

Day 4: Polish + warnings
  □ Add contextual warnings (IV, earnings, spread, sizing)
  □ Add "Law N" badges to each checklist row
  □ Add pre-defined exit prices to contract details
  □ Add IV history progress bar ("X/20 days needed for IV Rank")

Day 5: Live testing
  □ Run on 5 tickers spanning all verdict types (BUY/HOLD/AVOID)
  □ Spot-check Greeks against broker platform (IBKR/Tastytrade)
  □ Verify IV Rank computation after 20+ days of data
```

---

## SECTION 8 — WMT EXAMPLE OUTPUT (expected)

```json
{
  "ticker": "WMT",
  "spot": 124.87,
  "expiry": "2026-04-17",
  "dte": 45,
  "iv_data": {
    "current_iv": 0.19,
    "iv_rank": null,
    "days_of_history": 0,
    "note": "IV history insufficient — need 20 trading days. Rank will appear after daily use."
  },
  "universal": { "passed": true },
  "summary": {
    "long_call":        { "badge": "yellow", "verdict": "CAUTION",      "note": "IV Rank unknown" },
    "covered_call":     { "badge": "na",     "verdict": "N/A",          "note": "Requires owning shares" },
    "long_put":         { "badge": "na",     "verdict": "N/A",          "note": "Requires AVOID verdict" },
    "cash_secured_put": { "badge": "yellow", "verdict": "CAUTION",      "note": "IV Rank unknown" }
  }
}
```

After 20 trading days of IV history collection, IV Rank populates and CAUTION resolves to GREEN or RED depending on actual IV regime.

---

*This document is the complete implementation guide for the Options Law Matrix Engine.*  
*It contains all code needed to build the Options tab in the Swing Trade Analyzer.*
*Cross-reference with: options_module_research.md for the theoretical foundation.*
