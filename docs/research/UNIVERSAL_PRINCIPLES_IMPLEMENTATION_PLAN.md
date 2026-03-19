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
- `scoringEngine.js` → `categoricalAssessment.js` (RS data flows through `rsData` object)
- `scoringEngine.js` RS quality gates ↔ `categoricalAssessment.js` RS thresholds (MUST agree)
- `riskRewardCalc.js` ↔ `trade_simulator.py` (stop logic must be consistent)
- `api.js` ↔ `backend.py` routes (API contract)

---

## PRE-WORK: 6 MUST-FIX BUGS (From First Audit — was 7, Bug 0C removed as already correct)

These are correctness bugs, not architecture changes. Fix BEFORE any evolution.

### Bug 0A: Remove "3.2x" Hallucinated MTF Claim
- **File:** `backend/support_resistance.py` — lines 23 and 1235 (docstring comments)
- **CORRECTION (self-review round 3):** The source is in a Python file's docstrings, NOT .md files. The .md files (audit docs, known issues, implementation plan) only REFERENCE the bug as a finding — those references should remain.
- **Change:** Remove or correct the "3.2x stronger predictive power" claim in both docstring locations
- **Blast radius:** Docstrings only, zero functional code impact
- **Test:** `grep -r "3\.2x" backend/ --include="*.py" --exclude-dir=venv` returns 0 matches (exclude .md audit docs from test scope)

### Bug 0B: VCP Volume Dry-Up Check
- **File:** `backend/pattern_detection.py` — `detect_vcp()` function (lines 298-439)
- **Change:** Add per-contraction volume dry-up check (volume should decrease across each contraction, not just overall)
- **IMPORTANT (self-review round 3):** Add as a **confidence booster** (+10 pts), NOT a gate. Current VCP uses 3 gates (contractions ≥ 2, strictly decreasing depths, tight_base < 10%) + confidence boosters (volatility +15, volume +5). Per-contraction volume check should follow the booster pattern. Current overall volume decline is +5; per-contraction check replaces it with +10 when validated.
- **Blast radius:** VCP confidence scores change → some borderline VCPs may drop below 60% actionability threshold → affects Scan tab + Analyze tab. Main verdict (BUY/HOLD/AVOID) is NOT affected (patterns are separate from categorical verdict).
- **Test:** Run `backtest_holistic.py --configs C` → compare before/after metrics
- **Acceptance:** PF should stay ≥1.5. Trade count may decrease slightly (expected: fewer false VCPs).

### ~~Bug 0C: Trend Template 25%→30% Above 52-Week Low~~ — **ALREADY CORRECT (No Change Needed)**
- **File:** `backend/pattern_detection.py` — `check_trend_template()` line 271
- **Current code:** `'above_30pct_52w_low': current_price >= low_52w * 1.30` — already uses 30%
- **Status:** ~~Bug~~ → **VERIFIED CORRECT** (self-review Day 69, round 2)
- **Action:** NONE. Remove from Tier 0 checklist.

### Bug 0D: RS Threshold — Backtest 1.0 vs 1.1 vs 1.2
- **Files (3 — not 2!):**
  1. `categorical_engine.py` line 51 — backtest assessment
  2. `categoricalAssessment.js` line 263 — frontend assessment (reads `technicalData?.rsData?.rs52Week`)
  3. `scoringEngine.js` lines 412, 466, 477 — quality gates + auto-AVOID at RS<0.8, BUY requires RS≥1.0
- **CRITICAL NOTE:** RS flows through `scoringEngine.js` → `calculateRelativeStrength()` → `rsData.rs52Week` → `categoricalAssessment.js`. The scoring engine ALSO enforces RS thresholds independently via quality gates. ALL THREE files must be updated together.
- **Change:** Test RS ≥ 1.0 vs ≥ 1.1 vs ≥ 1.2 for Strong Technical threshold
- **Blast radius:** Directly affects BUY signal frequency. Higher threshold = fewer BUYs
- **Test approach (self-review round 3):** `backtest_adx_rsi_thresholds.py` exists but is hardcoded for ADX/RSI with no CLI args. **Simpler approach:** Edit RS threshold in `categorical_engine.py` line 51 manually, run `backtest_holistic.py --configs C` three times (once per threshold value), compare results. This avoids modifying an unrelated test script.
- **Decision:** Pick the threshold that maximizes PF without dropping trade count below 150

### Bug 0E-F: RRG Normalization — Convention Issue, Not Math Error
- **File:** `backend/backend.py` lines 2364-2402 (sector rotation), 2432-2436 (size rotation)
- **Current state (verified Day 69, round 2):**
  - RS-Ratio: normalized to 100 via static midpoint → `(rs_line / rs_line.iloc[midpoint]) * 100`
  - RS-Momentum: 0-centered delta → `rs_normalized[-1] - rs_normalized[-10]`
  - Quadrants: `(RS ≥ 100, Momentum ≥ 0)` — Leading, Weakening, Lagging, Improving
- **Standard RRG convention:** Both axes centered at 100, using EMA-based normalization (not static midpoint)
- **Audit verdict:** "Functionally equivalent but mislabeled" — this is a linear reparameterization, NOT a logic error
- **Recommended fix:** TWO options:
  1. **(Easy, low risk):** Add code comment documenting this as a deliberate swing-trading variant, not standard RRG. Update any docs that claim "standard RRG."
  2. **(Harder, medium risk):** Rewrite to use EMA-based normalization + 100-centered momentum. Would change all sector quadrant assignments.
- **Blast radius:** Option 1 = zero. Option 2 = all sector rotation displays change
- **Test:** Option 1: N/A. Option 2: Compare before/after quadrant assignments for all 11 sectors
- **Recommendation:** Option 1 (documentation fix). The current implementation works correctly for swing trading purposes.

### Bug 0G: F&G Neutral Zone Narrowing
- **File:** `categoricalAssessment.js` ONLY (lines 495-518) — **NOT categorical_engine.py**
- **CRITICAL NOTE (self-review Day 69, round 2):** `categorical_engine.py` has NO `assess_sentiment()` function. Line 376: *"Sentiment is always 'Neutral' for backtesting"*. F&G thresholds are **frontend-only**.
- **Change:** Current neutral is 35-60. Consider narrowing to 40-55
- **Blast radius:** Frontend verdicts only — backtest results UNAFFECTED (backtest hardcodes sentiment=Neutral)
- **Test:** Cannot backtest this change (backtest ignores F&G). Manual review: analyze 5 stocks with current F&G value and verify Neutral/Strong/Weak assignment is reasonable
- **Note:** This is a frontend-only change. No backend sync required.

---

## TIER 1: QUICK WINS (Day 69-70)

### Change 1A: ATR Stops Primary, 7% as Maximum Cap

**Rationale:** VERIFIED 3/4 LLMs. We already compute ATR stops. Just change the priority.

**Files affected (2):**

| File | Change | Lines |
|------|--------|-------|
| `backend/backtest/trade_simulator.py` | Quick mode: use tighter of 5% or 2×ATR | ~lines 189-194 |
| `frontend/src/utils/riskRewardCalc.js` | Already uses ATR × 2 — add 7% max cap comment | ~line 26 |

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
- Quick mode: Use tighter of (5% fixed, 2×ATR) — `max(stop_prices)` not `min`
- ATR is already computed at lines 180-186 (before holding period check), so no signature changes needed
- Documentation: Clarify that ATR is primary, percentage is cap

**CRITICAL (self-review round 4): Use `max()` not `min()` for stop prices.**
"Tighter stop" = closer to entry = higher price. `max(fixed_stop, atr_stop)` picks the higher (tighter) stop.
```python
# CORRECT implementation:
fixed_stop = entry_price * 0.95
if atr is not None and atr > 0:
    atr_stop = entry_price - (atr * 2)
    stop_price = max(fixed_stop, atr_stop)  # max = tighter = less risk
else:
    stop_price = fixed_stop
```

**Blast radius:**
- Backtest results will change slightly for Quick mode trades
- Frontend R:R display unchanged (already ATR-based)
- Position sizing calculator unchanged (uses R = entry - stop)

**NOTE (self-review Day 69, round 2): Known ATR multiplier mismatch (not in scope):**
- `riskRewardCalc.js` uses **1.5×ATR** for momentum stops, **2×ATR** for pullback stops
- `trade_simulator.py` uses **2×ATR** for ALL entry types (no pullback/momentum distinction)
- This mismatch means frontend R:R display may show different stop than what backtest would use for momentum entries
- **Decision:** Document but don't fix in this evolution. Aligning would require backtest architecture changes.

**Test protocol:**
1. Run `backtest_holistic.py --configs C` BEFORE change → save metrics
2. Make change to trade_simulator.py (Quick mode block, lines 189-194)
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
  // ... existing validation ...

  const riskPerShare = entryPrice - stopPrice;
  const maxRiskAmount = accountSize * (riskPercent / 100);
  let shares = Math.floor(maxRiskAmount / riskPerShare);

  // NEW: VIX-based position scaling — applied to maxPositionPercent BEFORE cap check
  // (self-review round 4: apply BEFORE cap, not after, so cap still works correctly)
  const vixMultiplier = options.vixMultiplier || 1.0;
  // VIX < 20: 1.0 (full size), VIX 20-30: 0.75, VIX > 30: 0.50
  const effectiveMaxPositionPercent = (options.maxPositionPercent || 100) * vixMultiplier;
  const maxPositionValue = accountSize * (effectiveMaxPositionPercent / 100);
  const maxSharesByPosition = Math.floor(maxPositionValue / entryPrice);

  // ... existing cap logic uses maxSharesByPosition ...
  // ... rest unchanged ...
}
```
**Why apply to maxPositionPercent (not shares directly):**
- If applied AFTER the cap: VIX reduction fights against position limits
- If applied BEFORE: VIX scales the maximum allowed position, cap still applies cleanly
- Default `vixMultiplier = 1.0` preserves existing behavior exactly
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

**Files affected (5):**

| File | Change | Blast Radius |
|------|--------|--------------|
| `frontend/src/utils/rsCalculator.js` | Add blended RS calculation (21d/63d/126d) | RS data changes |
| `frontend/src/utils/scoringEngine.js` | Pass rsBlended through rsData object | Quality gates may change |
| `frontend/src/utils/categoricalAssessment.js` | Use blended RS in technical assessment | Verdict logic changes |
| `backend/backtest/backtest_holistic.py` | Calculate blended RS for backtest | Backtest results change |
| `backend/backtest/categorical_engine.py` | Mirror frontend change | MUST match JS |

**ARCHITECTURE NOTE (self-review Day 69, round 2):**
RS is computed ENTIRELY CLIENT-SIDE in `rsCalculator.js`, NOT in `backend.py`. The backend only returns raw prices (`price52wAgo`, `price13wAgo`, `priceHistory`). The original plan incorrectly targeted `backend.py` for blended RS. The correct approach:

**Option A (preferred): Compute in rsCalculator.js from existing priceHistory**
The frontend already receives full price history. Compute blended lookbacks from it:
```javascript
// rsCalculator.js — ADD to calculateRelativeStrength()
function calculateBlendedRS(stockPrices, spyPrices) {
    // 21-day ROC (short-term persistence)
    const roc21 = stockPrices.length > 22
        ? (stockPrices[stockPrices.length - 1] / stockPrices[stockPrices.length - 22]) - 1 : 0;

    // 63-day RS vs SPY
    const stock63d = stockPrices.length > 64
        ? (stockPrices[stockPrices.length - 1] / stockPrices[stockPrices.length - 64]) - 1 : 0;
    const spy63d = spyPrices.length > 64
        ? (spyPrices[spyPrices.length - 1] / spyPrices[spyPrices.length - 64]) - 1 : 0;
    const rs63 = (1 + spy63d) !== 0 ? (1 + stock63d) / (1 + spy63d) : 1.0;

    // 126-day RS vs SPY
    const stock126d = stockPrices.length > 127
        ? (stockPrices[stockPrices.length - 1] / stockPrices[stockPrices.length - 127]) - 1 : 0;
    const spy126d = spyPrices.length > 127
        ? (spyPrices[spyPrices.length - 1] / spyPrices[spyPrices.length - 127]) - 1 : 0;
    const rs126 = (1 + spy126d) !== 0 ? (1 + stock126d) / (1 + spy126d) : 1.0;

    // Normalize 21d ROC to RS-like scale (1.0 = neutral)
    const rs21 = 1.0 + roc21;

    // Equal-weight blend
    return {
        rsBlended: Math.round(((rs21 + rs63 + rs126) / 3.0) * 1000) / 1000,
        rs21d: Math.round(rs21 * 1000) / 1000,
        rs63d: Math.round(rs63 * 1000) / 1000,
        rs126d: Math.round(rs126 * 1000) / 1000,
    };
}
```

**Option B: Backend adds blended RS to API response** — adds server-side computation, NOT needed since priceHistory is already available client-side. Avoid this to keep backend changes minimal.

**Critical decision:** Keep `rs52Week` everywhere for backward compatibility. Add `rsBlended` alongside it. Frontend assessment uses `rsBlended` when available, falls back to `rs52Week`.

**Frontend (`categoricalAssessment.js`):**

**CRITICAL DATA FLOW (verified by code audit):**
```
scoringEngine.js → calculateRelativeStrength(stockData, spyData)
    → returns rsData { rs52Week, rs13Week, rsRating, ... }
    → attaches to technicalResult.rsData
categoricalAssessment.js line 256:
    const rs52Week = technicalData?.rsData?.rs52Week || 1.0;
```

RS blended must flow through the SAME path:
```javascript
// scoringEngine.js — MODIFY calculateRelativeStrength() or its caller
// Add rsBlended to the rsData object:
rsData: {
    rs52Week: rsData.rs52Week,       // KEEP (backward compat)
    rsBlended: rsData.rsBlended,     // NEW (from backend or computed here)
    rs13Week: rsData.rs13Week,
    ...
}

// categoricalAssessment.js line 256 — CHANGE:
// CURRENT:
const rs52Week = technicalData?.rsData?.rs52Week || 1.0;

// NEW:
const rsValue = technicalData?.rsData?.rsBlended || technicalData?.rsData?.rs52Week || 1.0;
```

**Also update `scoringEngine.js` quality gates + verdict (3 places):**
```javascript
// Line 412: Quality gate RS check
if (rsData?.rsBlended && rsData.rsBlended < 0.8) { ... }  // or keep rs52Week here for safety

// Line 466: Auto-AVOID
if (rsData?.rs52Week && rsData.rs52Week < 0.8) { ... }  // keep 52w for hard floor

// Line 477: BUY requires RS≥1.0
if (rsData?.rsBlended && rsData.rsBlended >= 1.0) { ... }  // use blended for BUY gate
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

**Test protocol (corrected — self-review round 5):**
1. Run backtest BEFORE → save full metrics
2. Add `calculate_rs_blended()` to `backtest_holistic.py` (not backend.py — RS is client-side for live, backtest computes its own)
3. Update `categorical_engine.py` to accept `rs_blended` parameter with fallback to `rs_52w`
4. Run backtest AFTER → compare
5. Acceptance: PF ≥ 1.5, WR ≥ 50%. If blended RS degrades metrics, REVERT and keep 52w only
6. If backtest passes → update `rsCalculator.js` to compute blended RS from priceHistory
7. Update `scoringEngine.js` to pass `rsBlended` through rsData object
8. Update `categoricalAssessment.js` to use `rsBlended` with `rs52Week` fallback
9. Manual test: analyze AAPL, NVDA, TSLA → verify blended RS appears and assessment is reasonable

**Dependency chain (CORRECTED — Day 69 self-review round 2):**
```
BACKTEST VALIDATION FIRST (isolated from frontend):
categorical_engine.py (accept rs_blended param) → unit test
    ↓
backtest_holistic.py (compute blended RS from price data & pass) → full backtest
    ↓ (ONLY if backtest PF ≥ 1.5 and WR ≥ 50%)

FRONTEND (only after backtest validates):
rsCalculator.js (add calculateBlendedRS) → unit test with known prices
    ↓
scoringEngine.js (pass rsBlended through rsData) → verify rsData object
    ↓
categoricalAssessment.js (use rsBlended with rs52Week fallback) → test assessment
    ↓
backend.py / api.js → NO CHANGE (priceHistory already available)
```

**Rollback:** Revert all 5 files. `rs52Week` still exists as fallback everywhere.

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
    """RSI with very short period (Connors approach).

    IMPORTANT (self-review round 4): Uses Wilder's EMA (ewm), NOT SMA (rolling).
    Both backend.py:247 and backtest_holistic.py:105 use ewm(alpha=1/period).
    For RSI(2): alpha = 1/2 = 0.5. Using SMA would give different values.
    """
    delta = closes.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = (-delta).where(delta < 0, 0.0)
    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()  # Wilder's, NOT rolling
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()  # Wilder's, NOT rolling
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

### Summary: 14 files modified, 3 files created, all existing tests must pass

| # | File | Tier | Action | Lines Changed | Risk |
|---|------|------|--------|---------------|------|
| 1 | `backend/support_resistance.py` | 0A | Modify | ~2 lines (docstrings) | ZERO — remove hallucinated claim |
| 2 | `backend/pattern_detection.py` | 0B | Modify | ~15 lines | LOW — VCP confidence booster |
| 3 | `backend/backtest/trade_simulator.py` | 1A, 2A | Modify | ~20 lines | LOW — stop logic + VIX multiplier |
| 4 | `frontend/src/utils/riskRewardCalc.js` | 1A | Modify | ~2 lines (comment) | ZERO — document ATR-primary, 7% cap |
| 5 | `frontend/src/utils/categoricalAssessment.js` | 0D, 0G, 1B, 2B | Modify | ~15 lines | MEDIUM — verdict logic + F&G thresholds |
| 6 | `backend/backtest/categorical_engine.py` | 0D, 1B, 2B | Modify | ~10 lines | MEDIUM — MUST match JS |
| 7 | `frontend/src/utils/scoringEngine.js` | 0D, 2B | Modify | ~15 lines | MEDIUM — RS quality gates + rsData flow |
| 8 | `frontend/src/utils/rsCalculator.js` | 2B | Modify | ~40 lines | MEDIUM — blended RS computation |
| 9 | `docs/claude/stable/GOLDEN_RULES.md` | 1B | Modify | ~5 lines | ZERO |
| 10 | `backend/backtest/parameter_stability.py` | 1C | NEW | ~200 lines | ZERO — standalone script |
| 11 | `frontend/src/utils/positionSizing.js` | 2A | Modify | ~10 lines | LOW — additive param |
| 12 | `frontend/src/App.jsx` | 2A, 3B | Modify | ~15 lines | LOW — wiring only |
| 13 | `backend/backend.py` | 0E-F, 3A | Modify | ~30 lines | LOW — RRG comment + new MR endpoints |
| 14 | `backend/backtest/backtest_holistic.py` | 2B | Modify | ~30 lines | MEDIUM — blended RS + affects backtest |
| 15 | `backend/mean_reversion.py` | 3A | NEW | ~150 lines | ZERO — standalone |
| 16 | `backend/backtest/mr_simulator.py` | 3A | NEW | ~200 lines | ZERO — standalone |
| 17 | `frontend/src/services/api.js` | 3A | Modify | ~15 lines | LOW — additive functions |

**SELF-REVIEW LOG (5 rounds, Day 69):**

**Round 1:** `scoringEngine.js` was MISSING. RS flows through it to `categoricalAssessment.js`. Added.

**Round 2:** `rsCalculator.js` MISSING (RS is client-side, not backend). Bug 0C already correct (removed). Bug 0G frontend-only. Bug 0E-F is convention issue. ATR 1.5x/2x mismatch documented.

**Round 3:** Bug 0A targets `support_resistance.py` (Python), not .md files. Bug 0B should be confidence booster, not gate. Bug 0D test simplified to manual threshold + 3 runs.

**Round 4:** `min()` → `max()` for stop prices (CRITICAL — was backwards). RSI(2) must use `ewm()` not `rolling()`. VIX multiplier placement: apply to maxPositionPercent BEFORE cap. Removed phantom categoricalAssessment.js line item from 1A.

**Round 5:** Fixed document inconsistencies — file count (9→14 modified), commit count (7→6), Change 1A header (3→2), Tier 2B test protocol (backend.py→rsCalculator.js), added missing files to matrix (support_resistance.py, pattern_detection.py, riskRewardCalc.js).

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
Tier 0 (Pre-work bugs): 1 commit per bug fix (6 commits — Bug 0C removed as already correct)
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
