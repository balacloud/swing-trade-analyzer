# Universal Principles Evolution — Detailed Implementation Plan

**Date:** 2026-03-18 (Day 69)
**Author:** Claude Opus 4.6 (acting as systems architect)
**Source of Truth:** Code → then this plan → then synthesis doc
**Prerequisite:** `docs/research/UNIVERSAL_PRINCIPLES_SYNTHESIS.md` (4-LLM consensus)
**Current Version:** v4.30 (Backend v2.32, Frontend v4.30, Backtest v4.17, API Service v2.9)

---

## PHILOSOPHY

> "Change one file. Test it. Validate it doesn't break anything else. Then move to the next."

Every change in this plan follows 5 rules:
1. **One logical change per commit** — never bundle unrelated changes
2. **Test before AND after** — run existing tests, then verify the specific change
3. **Blast radius documented** — every change lists what files it touches and what it could break
4. **Rollback plan** — git revert is always the escape hatch
5. **Frontend and backend MUST stay in sync** — `categoricalAssessment.js` is the frontend source of truth, `categorical_engine.py` is the backtest port. If one changes, the other MUST change in the same commit

---

## DEPENDENCY MAP (Read First)

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                          │
│                                                              │
│  App.jsx ──────────── calls ──────────→ api.js              │
│    │                                      │                  │
│    ├── categoricalAssessment.js           │ fetches from     │
│    │     ├── assessTechnical()            │ backend          │
│    │     ├── assessFundamental()          │                  │
│    │     ├── assessSentiment()            ▼                  │
│    │     └── determineVerdict()     ┌──────────┐            │
│    │                                │ Backend  │            │
│    ├── positionSizing.js           │ Flask    │            │
│    │     └── calculatePositionSize()│ :5001   │            │
│    │                                └────┬─────┘            │
│    └── riskRewardCalc.js                │                   │
│          └── calculateRiskReward()      │                   │
│               (uses ATR × 2 for stop)   │                   │
│                                          │                   │
└──────────────────────────────────────────┼───────────────────┘
                                           │
┌──────────────────────────────────────────┼───────────────────┐
│                    BACKEND (Flask)        │                   │
│                                          │                   │
│  backend.py ──── /api/stock/<t> ─────────┘                   │
│    ├── calculate_rsi(closes, period=14)                      │
│    ├── calculate_adx(high, low, close)  → returns ATR too    │
│    └── routes: 25 endpoints                                  │
│                                                              │
│  backtest/                                                   │
│    ├── categorical_engine.py  ← MUST MIRROR frontend JS     │
│    ├── trade_simulator.py     ← ATR, stops, exit strategies  │
│    ├── backtest_holistic.py   ← orchestrator (60 tickers)    │
│    ├── metrics.py             ← Sharpe, PF, win rate         │
│    └── simfin_loader.py       ← historical fundamentals      │
│                                                              │
│  pattern_detection.py  ← VCP, C&H, Flat Base, Trend Template│
│  support_resistance.py ← S&R with ATR-based stops           │
│  cache_manager.py      ← SQLite persistent cache            │
│                                                              │
│  cycles_engine.py  ← Context Tab (FRED)                     │
│  econ_engine.py    ← Context Tab (FRED)                     │
│  news_engine.py    ← Context Tab (Alpha Vantage)            │
└──────────────────────────────────────────────────────────────┘
```

**Critical sync pairs:**
- `categoricalAssessment.js` ↔ `categorical_engine.py` (MUST match)
- `riskRewardCalc.js` ↔ `trade_simulator.py` (stop logic must be consistent)
- `api.js` ↔ `backend.py` routes (API contract)

---

## PRE-WORK: 7 MUST-FIX BUGS (From First Audit)

These are correctness bugs, not architecture changes. Fix BEFORE any evolution.

### Bug 0A: Remove "3.2x" Hallucinated MTF Claim
- **File:** Search all `.md` files for "3.2x" or "MTF" claims
- **Change:** Remove or correct the hallucinated claim
- **Blast radius:** Documentation only, zero code impact
- **Test:** Grep for "3.2x" returns 0 matches

### Bug 0B: VCP Volume Dry-Up Check
- **File:** `backend/pattern_detection.py` — `detect_vcp()` function
- **Change:** Add volume contraction check (volume should decrease across each contraction)
- **Blast radius:** Pattern detection results may change → affects Scan tab + Analyze tab
- **Test:** Run `backtest_holistic.py --configs C` → compare before/after metrics
- **Acceptance:** Pattern count may decrease (fewer false VCPs), but PF should stay ≥1.5

### Bug 0C: Trend Template 25%→30% Above 52-Week Low
- **File:** `backend/pattern_detection.py` — `check_trend_template()`
- **Change:** Change the "price at least 25% above 52-week low" to 30%
- **Blast radius:** TT scores may decrease for borderline stocks → fewer "Strong" technical assessments
- **Test:** Run backtest → verify WR and PF don't collapse. If they do, revert.

### Bug 0D: RS Threshold — Backtest 1.0 vs 1.1 vs 1.2
- **Files:** `categorical_engine.py` line 51, `categoricalAssessment.js` (matching line)
- **Change:** Test RS ≥ 1.0 vs ≥ 1.1 vs ≥ 1.2 for Strong Technical threshold
- **Blast radius:** Directly affects BUY signal frequency. Higher threshold = fewer BUYs
- **Test:** Run `backtest_adx_rsi_thresholds.py` (modify for RS sweep)
- **Decision:** Pick the threshold that maximizes PF without dropping trade count below 150

### Bug 0E: RRG Normalization Baseline
- **File:** Backend sector rotation calculation
- **Change:** Verify RS-Ratio and RS-Momentum use correct 100 baseline (not 0)
- **Blast radius:** Sector rotation quadrant assignments
- **Test:** Compare current output vs manual calculation for XLK

### Bug 0F: RRG Momentum Center (0 vs 100)
- **File:** Same as 0E
- **Change:** Ensure momentum values center around 100, not 0
- **Test:** All sectors should cluster around 100 when market is flat

### Bug 0G: F&G Neutral Zone Narrowing
- **Files:** `categoricalAssessment.js` (line with F&G thresholds), `categorical_engine.py`
- **Change:** Current neutral is 35-60 (Day 45). Consider narrowing to 40-55
- **Blast radius:** More stocks get non-Neutral sentiment → affects verdicts
- **Test:** Backtest with narrow vs current → pick better PF
- **Note:** Both JS and Python files MUST be updated together

---

## TIER 1: QUICK WINS (Day 69-70)

### Change 1A: ATR Stops Primary, 7% as Maximum Cap

**Rationale:** VERIFIED 3/4 LLMs. We already compute ATR stops. Just change the priority.

**Files affected (3):**

| File | Change | Lines |
|------|--------|-------|
| `backend/backtest/trade_simulator.py` | Reorder stop logic: ATR first, 7% cap | ~lines 100-180 |
| `frontend/src/utils/riskRewardCalc.js` | Already uses ATR × 2 — add 7% max cap comment | ~line 26 |
| `frontend/src/utils/categoricalAssessment.js` | Update stop description text if displayed | minimal |

**Detailed changes:**

**trade_simulator.py** (the critical file):
```
CURRENT (Standard holding period):
  stop = swing_low - 2×ATR
  clamped to 3-10% range
  fallback: -7% to -8% if ATR unavailable

NEW:
  primary_stop = swing_low - 2×ATR    (unchanged)
  max_stop_cap = entry × 0.93         (7% max — unchanged numerically)
  stop = max(primary_stop, max_stop_cap)  (ATR stop unless it exceeds 7%)
  clamped to 3-10% range              (unchanged)
```

This is actually ALREADY how it works in Standard/Position mode. The "Quick" mode uses a fixed 5% stop. The change is:
- Quick mode: Change from fixed 5% to min(5%, 2×ATR) — use ATR if it gives a tighter stop
- Documentation: Clarify that ATR is primary, percentage is cap

**Blast radius:**
- Backtest results will change slightly for Quick mode trades
- Frontend R:R display unchanged (already ATR-based)
- Position sizing calculator unchanged (uses R = entry - stop)

**Test protocol:**
1. Run `backtest_holistic.py --configs C --walk-forward` BEFORE change → save metrics
2. Make change
3. Run same command AFTER → compare
4. Acceptance: PF stays ≥1.5, WR stays ≥50%, Max DD doesn't increase >3%

**Rollback:** `git revert <commit>` — single file change, clean revert

---

### Change 1B: Equal-Weight Principle (Documentation + Validation)

**Rationale:** MISLEADING 4/4 LLMs on weight optimization. Formalize what we already do.

**Files affected (2):**

| File | Change | Lines |
|------|--------|-------|
| `frontend/src/utils/categoricalAssessment.js` | Add comment block documenting equal-weight principle | Top of file |
| `backend/backtest/categorical_engine.py` | Mirror comment | Top of file |

**Actual change:** Comments only. Our system already treats 4 categories equally (each is Strong/Decent/Weak, verdict uses count of Strong). No code logic change.

**The real enforcement:** Add a GOLDEN_RULES.md entry:
```
Rule 16: EQUAL WEIGHT — Never optimize category weights.
DeMiguel et al. (2009): equal weights beat optimized out-of-sample.
238 trades is insufficient to optimize 4+ weights. If future evolution
moves to continuous scoring, start with equal weights.
```

**Blast radius:** Zero. Comments + documentation only.
**Test:** N/A
**Rollback:** N/A

---

### Change 1C: Parameter Stability Test Script

**Rationale:** MISLEADING 4/4 that walk-forward alone prevents overfitting.

**Files affected (1 new):**

| File | Change |
|------|--------|
| `backend/backtest/parameter_stability.py` (NEW) | New validation script |

**What it does:**
```python
# For each key parameter, run backtest at ±1 and ±2 from current value
# If PF drops below 1.0 at ANY nearby value, flag as FRAGILE

PARAMETERS_TO_TEST = {
    'adx_threshold': [18, 19, 20, 21, 22],        # Current: 20
    'rs_threshold': [0.9, 0.95, 1.0, 1.05, 1.1],  # Current: 1.0
    'rsi_low': [45, 48, 50, 52, 55],               # Current: 50
    'rsi_high': [65, 68, 70, 72, 75],              # Current: 70
    'pattern_confidence': [50, 55, 60, 65, 70],    # Current: 60
    'stop_atr_multiple': [1.5, 1.75, 2.0, 2.25, 2.5],  # Current: 2.0
}

# Output: stability_report.json
# { parameter: { values: [...], PFs: [...], WRs: [...], stable: bool } }
```

**Architecture:**
- Reuses `backtest_holistic.py` configs and `categorical_engine.py` assessment
- Override single parameter per run
- Quick mode: 5 tickers, 1 year (for speed)
- Full mode: 60 tickers, 5 years (for confidence)

**Blast radius:** Zero — new file, reads existing code, writes report
**Test:** Run it. If it works, the output IS the test
**Rollback:** Delete the file

---

## TIER 2: HIGH IMPACT (Day 71-72)

### Change 2A: VIX-Based Position Sizing Multiplier

**Rationale:** PLAUSIBLE 3/4. Moreira & Muir (2017). Most impactful single change.

**Files affected (4):**

| File | Change | Blast Radius |
|------|--------|--------------|
| `frontend/src/utils/positionSizing.js` | Add `vixMultiplier` parameter | Position sizing output changes |
| `frontend/src/utils/categoricalAssessment.js` | Add VIX regime to risk assessment display | Display only |
| `frontend/src/App.jsx` | Pass VIX value to position sizing | Wiring change |
| `backend/backtest/trade_simulator.py` | Add VIX multiplier to backtest simulation | Backtest results change |

**Design:**
```javascript
// positionSizing.js — NEW parameter
export function calculatePositionSize(accountSize, riskPercent, entryPrice, stopPrice, options = {}) {
  // ... existing code ...

  // NEW: VIX-based position scaling
  const vixMultiplier = options.vixMultiplier || 1.0;
  // VIX < 20: 1.0 (full size)
  // VIX 20-30: 0.75
  // VIX > 30: 0.50
  shares = Math.floor(shares * vixMultiplier);

  // ... rest unchanged ...
}
```

```python
# trade_simulator.py — ADD to simulate_trade()
def get_vix_multiplier(vix_value):
    """Position sizing multiplier based on VIX regime."""
    if vix_value is None:
        return 1.0
    if vix_value < 20:
        return 1.0
    elif vix_value <= 30:
        return 0.75
    else:
        return 0.50
```

**Frontend wiring (App.jsx):**
```javascript
// In the position sizing section, compute multiplier from existing VIX data
const vixMultiplier = vixData?.current < 20 ? 1.0
                    : vixData?.current <= 30 ? 0.75
                    : 0.50;
// Pass to calculatePositionSize via options.vixMultiplier
```

**Blast radius:**
- Position size calculations change when VIX ≥ 20
- Backtest results change (position sizing affects $ PnL, not WR or PF)
- R:R calculations unchanged (those are per-share, not position-level)
- Categorical assessment unchanged
- Frontend display: position size number changes, everything else same

**Test protocol:**
1. Run backtest BEFORE → save metrics (PF, WR, max DD, Sharpe)
2. Make change (trade_simulator.py only first)
3. Run backtest AFTER → expect: similar PF/WR, LOWER max DD, potentially higher Sharpe
4. Then update frontend files
5. Manual test: analyze AMD → verify position size reflects VIX multiplier

**Dependency chain:**
```
trade_simulator.py (backtest) → validates the math works
    ↓ (after validation)
positionSizing.js (frontend) → user-facing display
    ↓
App.jsx → wiring VIX data to position sizing
    ↓
categoricalAssessment.js → display text only (optional)
```

**Rollback:** Revert the 4 files. VIX multiplier defaults to 1.0 everywhere.

---

### Change 2B: Blend 3 Momentum Lookbacks

**Rationale:** MISLEADING 3/4 that 12-1 is best. Blending is more robust than single lookback.

**Files affected (4):**

| File | Change | Blast Radius |
|------|--------|--------------|
| `backend/backend.py` | Add 21d ROC + 63d RS calculation alongside existing 52w RS | New data in API response |
| `backend/backtest/backtest_holistic.py` | Calculate blended RS for backtest | Backtest results change |
| `frontend/src/utils/categoricalAssessment.js` | Use blended RS in technical assessment | Verdict logic changes |
| `backend/backtest/categorical_engine.py` | Mirror frontend change | MUST match JS |

**Design — Backend (`backend.py`):**
```python
# In the /api/stock/<ticker> response, ADD alongside existing rs_52w:
def calculate_momentum_blend(df, spy_df):
    """
    Blend 3 momentum lookbacks (equal weight):
    - 21-day ROC (short-term persistence)
    - 63-day RS vs SPY (3-month intermediate drift)
    - 126-day RS vs SPY (6-month momentum)

    Returns composite RS score (1.0 = market perform)
    """
    close = df['Close']
    spy_close = spy_df['Close']

    # 21-day ROC: (price_now / price_21d_ago) - 1
    roc_21 = (close.iloc[-1] / close.iloc[-22]) - 1 if len(close) > 22 else 0

    # 63-day RS vs SPY: (stock_63d_return / spy_63d_return)
    stock_63d = (close.iloc[-1] / close.iloc[-64]) - 1 if len(close) > 64 else 0
    spy_63d = (spy_close.iloc[-1] / spy_close.iloc[-64]) - 1 if len(spy_close) > 64 else 0
    rs_63 = (1 + stock_63d) / (1 + spy_63d) if (1 + spy_63d) != 0 else 1.0

    # 126-day RS vs SPY (what we currently use as approximate 52-week RS)
    stock_126d = (close.iloc[-1] / close.iloc[-127]) - 1 if len(close) > 127 else 0
    spy_126d = (spy_close.iloc[-1] / spy_close.iloc[-127]) - 1 if len(spy_close) > 127 else 0
    rs_126 = (1 + stock_126d) / (1 + spy_126d) if (1 + spy_126d) != 0 else 1.0

    # Normalize 21d ROC to RS-like scale (1.0 = neutral)
    # ROC of +10% → RS of 1.10, ROC of -5% → RS of 0.95
    rs_21 = 1.0 + roc_21

    # Equal-weight blend
    blended = (rs_21 + rs_63 + rs_126) / 3.0

    return {
        'rs_blended': round(blended, 3),
        'rs_21d': round(rs_21, 3),
        'rs_63d': round(rs_63, 3),
        'rs_126d': round(rs_126, 3),
        'rs_52w': existing_rs_52w  # KEEP existing for backward compat
    }
```

**Critical decision:** Keep `rs_52w` in API response for backward compatibility. Add `rs_blended` alongside it. Frontend uses `rs_blended` for assessment, displays both.

**Frontend (`categoricalAssessment.js`):**
```javascript
// CURRENT:
if (pass_count >= 7 && rsi >= 50 && rsi <= 70 && rs_52w >= 1.0)  → Strong

// NEW:
const rs = stockData.rs_blended || stockData.rs_52w || 1.0;  // fallback chain
if (pass_count >= 7 && rsi >= 50 && rsi <= 70 && rs >= 1.0)  → Strong
```

**Backend (`categorical_engine.py`):**
```python
# CURRENT:
if pass_count >= 7 and 50 <= rsi_val <= 70 and rs_52w >= 1.0:

# NEW: accept rs_blended parameter, fallback to rs_52w
def assess_technical(trend_template_score, rsi, rs_52w=1.0, rs_blended=None, adx=None, total_criteria=8):
    rs = rs_blended if rs_blended is not None else rs_52w
    # ... rest uses `rs` instead of `rs_52w`
```

**Blast radius:**
- API response gains new fields (`rs_blended`, `rs_21d`, `rs_63d`, `rs_126d`) — additive, no breaks
- Technical assessment may change verdict for stocks where blended RS differs from 52w RS
- Backtest results will change (different RS values → different Strong/Decent/Weak assessments)
- Scan tab results may change
- Position sizing: unaffected
- R:R calculation: unaffected
- Pattern detection: unaffected
- Context tab: unaffected

**Test protocol:**
1. Run backtest BEFORE → save full metrics
2. Add `calculate_momentum_blend()` to backend.py → test with `curl localhost:5001/api/stock/AMD`
3. Verify `rs_blended` appears in response alongside `rs_52w`
4. Update `categorical_engine.py` to accept `rs_blended`
5. Update `backtest_holistic.py` to compute and pass `rs_blended`
6. Run backtest AFTER → compare
7. Acceptance: PF ≥ 1.5, WR ≥ 50%. If blended RS degrades metrics, REVERT and keep 52w only
8. If backtest passes → update `categoricalAssessment.js` to use `rs_blended`
9. Manual test: analyze AAPL, NVDA, TSLA → verify blended RS appears and assessment is reasonable

**Dependency chain:**
```
backend.py (add calculation) → test API response
    ↓
categorical_engine.py (accept new param) → test backtest
    ↓
backtest_holistic.py (compute & pass) → run full backtest validation
    ↓ (ONLY if backtest passes)
categoricalAssessment.js (use rs_blended) → test frontend
    ↓
api.js → NO CHANGE (already fetches stock data, new fields come free)
```

**Rollback:** Revert all 4 files. `rs_52w` still exists as fallback everywhere.

---

## TIER 3: MEAN-REVERSION ARM (Day 73-75)

### Change 3A: RSI(2) Scanner — Backend

**Rationale:** VERIFIED 2/4 that MR+momentum diversifies. RSI(2)<10 is the evidence-based entry.

**Files affected (2 new, 2 modified):**

| File | Action | Purpose |
|------|--------|---------|
| `backend/mean_reversion.py` (NEW) | Create | RSI(2) calculator + MR signal detection |
| `backend/backtest/mr_simulator.py` (NEW) | Create | MR-specific trade simulation (different exits) |
| `backend/backend.py` | Modify | Add `/api/mr/scan` + `/api/mr/signal/<ticker>` endpoints |
| `frontend/src/services/api.js` | Modify | Add `fetchMRSignals()` + `fetchMRScan()` |

**NEW: `backend/mean_reversion.py` (~150 lines):**
```python
"""
Mean-Reversion Engine — Connors RSI(2) Approach

Entry: RSI(2) < 10 AND Price > 200 SMA
Exit: RSI(2) > 70 OR time-based (max 10 days)
Stop: 3-5% below entry (tighter than momentum stops)

Only active when: ADX < 20 (range-bound) or as secondary signal alongside momentum

Source: Larry Connors "Short Term Trading Strategies That Work" (2009)
Validated by: 4-LLM audit (PLAUSIBLE 3/4, MISLEADING on RSI(14) vs RSI(2))
"""

import pandas as pd
import numpy as np

def calculate_rsi_short(closes, period=2):
    """RSI with very short period (Connors approach)."""
    delta = closes.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def detect_mr_signal(df, spy_df=None):
    """
    Detect mean-reversion entry signal.

    Conditions:
    1. RSI(2) < 10 (oversold on short timeframe)
    2. Price > 200 SMA (long-term uptrend intact — don't catch falling knives)
    3. Price > $5 (liquidity filter)
    4. Volume > 500K avg (tradeable)

    Returns:
        dict with {signal: bool, rsi2: float, sma200: float, entry_price, stop, target}
    """
    if len(df) < 200:
        return {'signal': False, 'reason': 'Insufficient data for 200 SMA'}

    close = df['Close']
    rsi2 = calculate_rsi_short(close, period=2).iloc[-1]
    sma200 = close.rolling(200).mean().iloc[-1]
    current_price = close.iloc[-1]
    avg_volume = df['Volume'].rolling(20).mean().iloc[-1]

    conditions = {
        'rsi2_oversold': rsi2 < 10,
        'above_200sma': current_price > sma200,
        'price_filter': current_price > 5,
        'volume_filter': avg_volume > 500000,
    }

    signal = all(conditions.values())

    # MR-specific risk params (tighter than momentum)
    atr = calculate_atr(df)  # reuse existing ATR function
    stop = max(current_price * 0.95, current_price - (atr * 1.5))  # 5% max or 1.5×ATR
    target = sma200 * 1.02  # target: slightly above 200 SMA (the "mean")

    return {
        'signal': signal,
        'strategy': 'mean_reversion',
        'rsi2': round(rsi2, 2),
        'sma200': round(sma200, 2),
        'current_price': round(current_price, 2),
        'conditions': conditions,
        'stop': round(stop, 2),
        'target': round(target, 2),
        'max_hold_days': 10,
        'exit_rule': 'RSI(2) > 70 OR 10 days max',
    }
```

**NEW: `backend/backtest/mr_simulator.py` (~200 lines):**
```python
"""
Mean-Reversion Trade Simulator

Different from momentum simulator:
- Tighter stops (3-5% vs 7-10%)
- Time-based exit (max 10 days)
- RSI(2) > 70 exit (indicator-based, not price target)
- No trailing stops (holding period too short)
- Smaller position sizes (50% of momentum standard)
"""

def simulate_mr_trade(stock_df, entry_idx, atr, stop_pct=0.05, max_days=10):
    """
    Simulate a mean-reversion trade.

    Exit conditions (first triggered wins):
    1. RSI(2) > 70 (mean recovered)
    2. Price hits stop (entry × (1 - stop_pct))
    3. Max holding days reached (time exit)

    Returns: dict with entry, exit, pnl, exit_reason, hold_days
    """
```

**Backend endpoints (`backend.py`):**
```python
@app.route('/api/mr/signal/<ticker>')
def get_mr_signal(ticker):
    """Check if ticker has active MR signal."""

@app.route('/api/mr/scan')
def scan_mr_signals():
    """Scan universe for MR signals. Returns list of tickers with RSI(2)<10 + above 200SMA."""
```

**Blast radius:**
- NEW files — zero impact on existing code
- `backend.py` gets 2 new endpoints — additive, no existing routes affected
- `api.js` gets 2 new functions — additive
- Existing momentum system: COMPLETELY UNTOUCHED
- Categorical assessment: UNTOUCHED (MR signals are a separate path)
- Backtest: MR has its own simulator, doesn't modify existing backtest

**Test protocol:**
1. Create `mean_reversion.py` → unit test with known RSI(2) values
2. Create `mr_simulator.py` → unit test with synthetic trade data
3. Add endpoints to `backend.py` → test with curl
4. Run `backtest_holistic.py` → verify ZERO change (confirms isolation)
5. Create separate MR backtest script → validate MR strategy independently
6. Acceptance: MR strategy WR ≥ 55%, avg hold < 7 days, max DD per trade < 5%

**Rollback:** Delete new files, remove 2 endpoints from backend.py.

---

### Change 3B: MR Frontend Display (Day 74-75)

**Files affected (3):**

| File | Change | Blast Radius |
|------|--------|--------------|
| `frontend/src/App.jsx` | Add MR signal indicator to Analyze tab | Display only |
| `frontend/src/services/api.js` | Add `fetchMRSignal(ticker)` | Additive |
| `frontend/src/components/` (new component) | MR Signal Card | Display only |

**Design principle:** MR signals appear as a SEPARATE card below the momentum analysis, not mixed into it. The user sees:
```
┌─ Momentum Analysis (existing) ─────────────────┐
│ Technical: Strong | Fundamental: Decent         │
│ Verdict: BUY (momentum breakout)                │
└─────────────────────────────────────────────────┘

┌─ Mean-Reversion Signal (NEW) ──────────────────┐
│ RSI(2): 7.3 (OVERSOLD)  |  Above 200 SMA: YES │
│ Signal: ACTIVE                                  │
│ Stop: $142.30 (3.2%)  |  Target: $151.80       │
│ Max Hold: 10 days  |  Exit: RSI(2) > 70        │
│ ⚠️ Different strategy — tighter stops, shorter hold │
└─────────────────────────────────────────────────┘
```

**Blast radius:** Display-only addition to Analyze tab. No existing components modified.

---

## API CONTRACT CHANGES

### New Endpoints (Tier 3 only)

| Method | Path | Purpose | Cache |
|--------|------|---------|-------|
| GET | `/api/mr/signal/<ticker>` | MR signal for single ticker | 1h |
| GET | `/api/mr/scan` | Scan universe for MR signals | 1h |

### Modified Responses (Tier 2)

| Endpoint | Change | Backward Compatible |
|----------|--------|---------------------|
| GET `/api/stock/<ticker>` | Add `rs_blended`, `rs_21d`, `rs_63d`, `rs_126d` fields | YES — new fields only, existing fields unchanged |

### No Changes

All other 25 endpoints remain unchanged. Categorical assessment endpoints, S&R, patterns, context tab, validation — all untouched.

---

## FILE-LEVEL CHANGE MATRIX

### Summary: 7 files modified, 3 files created, all existing tests must pass

| # | File | Tier | Action | Lines Changed | Risk |
|---|------|------|--------|---------------|------|
| 1 | `backend/backtest/trade_simulator.py` | 1A, 2A | Modify | ~20 lines | LOW — stop logic + VIX multiplier |
| 2 | `frontend/src/utils/categoricalAssessment.js` | 1B, 2B | Modify | ~10 lines | MEDIUM — verdict logic |
| 3 | `backend/backtest/categorical_engine.py` | 1B, 2B | Modify | ~10 lines | MEDIUM — MUST match JS |
| 4 | `docs/claude/stable/GOLDEN_RULES.md` | 1B | Modify | ~5 lines | ZERO |
| 5 | `backend/backtest/parameter_stability.py` | 1C | NEW | ~200 lines | ZERO — standalone script |
| 6 | `frontend/src/utils/positionSizing.js` | 2A | Modify | ~10 lines | LOW — additive param |
| 7 | `frontend/src/App.jsx` | 2A, 3B | Modify | ~15 lines | LOW — wiring only |
| 8 | `backend/backend.py` | 2B, 3A | Modify | ~50 lines | LOW — new calc + new endpoints |
| 9 | `backend/backtest/backtest_holistic.py` | 2B | Modify | ~20 lines | MEDIUM — affects backtest |
| 10 | `backend/mean_reversion.py` | 3A | NEW | ~150 lines | ZERO — standalone |
| 11 | `backend/backtest/mr_simulator.py` | 3A | NEW | ~200 lines | ZERO — standalone |
| 12 | `frontend/src/services/api.js` | 3A | Modify | ~15 lines | LOW — additive functions |

---

## TESTING STRATEGY

### Gate 1: Existing Tests Pass (After EVERY change)
```bash
# Run existing backtest — metrics must not regress
python backend/backtest/backtest_holistic.py --configs C --walk-forward

# Acceptance criteria (from Day 55-56):
# WR ≥ 50%, PF ≥ 1.5, Sharpe ≥ 0.7, p < 0.01, Max DD < 20%
```

### Gate 2: Parameter Stability (After Tier 1C)
```bash
python backend/backtest/parameter_stability.py --mode quick
# All parameters must show PF > 1.0 at ±2 from current value
```

### Gate 3: Blended RS Validation (After Tier 2B)
```bash
# Compare 52w RS vs blended RS on full backtest
python backend/backtest/backtest_holistic.py --configs C --rs-mode blended
python backend/backtest/backtest_holistic.py --configs C --rs-mode 52w
# Blended must equal or beat 52w on PF and Sharpe
```

### Gate 4: MR Strategy Standalone (After Tier 3A)
```bash
python backend/backtest/mr_backtest.py --universe sp500 --period 5y
# Acceptance: WR ≥ 55%, avg hold < 7 days, Sharpe > 0.5
```

### Gate 5: Combined System (After All Tiers)
```bash
# Run both momentum + MR together
# Verify combined Sharpe > momentum-only Sharpe
# Verify max DD combined < max DD momentum-only
```

---

## DOCUMENTATION UPDATES (Session Close)

After each tier completion, update:

| Doc | What |
|-----|------|
| `CLAUDE_CONTEXT.md` | Version bump, day summary, next priorities |
| `PROJECT_STATUS_DAY[N]_SHORT.md` | New status file |
| `KNOWN_ISSUES_DAY[N].md` | Updated issues |
| `API_CONTRACTS_DAY[N].md` | Only if new endpoints added (Tier 3) |
| `ROADMAP.md` | Mark Universal Principles evolution progress |
| `GOLDEN_RULES.md` | Add new rules if lessons learned |

---

## COMMIT STRATEGY

```
Tier 0 (Pre-work bugs): 1 commit per bug fix (7 commits)
Tier 1A: "Make ATR stops primary, 7% as maximum cap"
Tier 1B: "Document equal-weight factor principle"
Tier 1C: "Add parameter stability analysis script"
Tier 2A: "Add VIX-based position sizing multiplier"
Tier 2B: "Blend 3 momentum lookbacks (21d/63d/126d RS)"
Tier 3A: "Add mean-reversion engine (RSI(2) scanner)"
Tier 3B: "Add mean-reversion frontend display"
```

Each commit: ONE logical change. If a commit touches both frontend JS and backend Python (like the categorical sync), that's fine — they're ONE logical change.

---

## RISK ASSESSMENT

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Blended RS degrades backtest | Medium | HIGH | Keep `rs_52w` as fallback, revert if PF drops |
| VIX sizing reduces capital utilization | Low | MEDIUM | Only affects high-VIX periods (designed behavior) |
| MR signals conflict with momentum signals | Low | LOW | Separate display paths, user decides |
| Parameter stability reveals fragility | Medium | HIGH | Better to know now. Fix fragile params before going live |
| Frontend/backend sync breaks | Low | HIGH | Always commit JS + Python together for assessment changes |

---

## SUCCESS CRITERIA (The Final Gate)

After all tiers complete:

| Metric | Before (Current) | Target | Red Flag |
|--------|-------------------|--------|----------|
| Win Rate | 53.78% | ≥ 52% | < 48% |
| Profit Factor | 1.61 | ≥ 1.55 | < 1.3 |
| Sharpe Ratio | 0.85 | ≥ 0.80 | < 0.6 |
| p-value | 0.002 | < 0.01 | > 0.05 |
| Max Drawdown | (current) | ≤ current | > current + 5% |
| Parameter Stability | (new) | All PF > 1.0 at ±2 | Any PF < 0.5 |
| MR Standalone WR | (new) | ≥ 55% | < 45% |
| Combined Sharpe | (new) | > Momentum-only | < Momentum-only |

**If ANY red flag is hit: STOP. Investigate. Do not proceed to next tier.**

---

## VERSION BUMP (At Completion of All Tiers)

```
Backend:  v2.32 → v2.35 (v2.33 = bugs, v2.34 = tier 2, v2.35 = tier 3)
Frontend: v4.30 → v4.33 (same pattern)
Backtest: v4.17 → v4.20 (v4.18 = stability, v4.19 = blended RS, v4.20 = MR)
API Service: v2.9 → v2.10 (new MR endpoints)
Overall:  v4.30 → v4.35
```
