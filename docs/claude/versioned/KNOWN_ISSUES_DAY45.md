# KNOWN ISSUES - Day 45

> **Purpose:** Track all known bugs, gaps, and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 45 (February 4, 2026) - v4.5 Categorical Assessment Complete

---

## RESOLVED (Day 44)

| Issue | Resolution | Date |
|-------|------------|------|
| 75-point scoring meaningless | Replaced with Categorical Assessment (v4.5) | Day 44 |
| Sentiment was placeholder 5/10 | Integrated real Fear & Greed Index | Day 44 |
| No Pattern Detection | Added VCP, Cup-Handle, Flat Base detection | Day 44 |
| Position Size: NONE confusing | Added Actionable Recommendation Card | Day 44 |
| criteria_met vs criteria_passed mismatch | Fixed in categoricalAssessment.js | Day 44 |
| Entire verdict card colored | Changed to neutral bg, only verdict text colored | Day 44 |

---

## OPEN ISSUES

### Issue 1: Frontend/Backend Data Validation Needed
- **Severity:** MEDIUM
- **Description:** Need systematic validation that frontend displays match backend API responses
- **Symptoms:**
  - Trend Template was showing 0/8 despite API returning 8/8
  - Could be other hidden mismatches
- **Action:** Run validation test on 20 tickers, compare frontend vs API
- **Status:** PENDING - Next session priority

### Issue 2: RSI Calculation Location
- **Severity:** LOW
- **Description:** RSI calculated in frontend scoringEngine.js from price history, not returned from backend API
- **Impact:** Works correctly, but adds complexity
- **Consider:** Backend could pre-calculate RSI for consistency
- **Status:** DEFERRED - Working as-is

### Issue 3: SPY 200 EMA Shows $0.00 in Test Script
- **Severity:** LOW
- **Description:** Test script shows "SPY Regime: Bull (Price: $686.22, 200 EMA: $0.00)"
- **Impact:** Visual only - regime detection still working via price comparison
- **Root Cause:** Stock API doesn't return ema200 indicator
- **Status:** DEFERRED - Not blocking

### Issue 4: Fear & Greed 25-45 Zone is "Weak"
- **Severity:** INFO
- **Description:** F&G values 25-45 marked as "Weak" because pullback setups fail in fear
- **Current Value:** 39.5 (Fear)
- **Impact:** Most stocks showing Sentiment=Weak currently
- **Note:** This is working as intended per research
- **Status:** MONITORING

---

## VALIDATION GATES STATUS

| Gate | Criteria | Status |
|------|----------|--------|
| G1: Structural Stops | Avg loss < 7% baseline | PASSED (-6.51%) |
| G2: ADX Value | Win rate improves with gating | PENDING |
| G3: 4H Data | Reliable, sufficient history | PASSED (118 bars) |
| G4: 4H RSI Value | Entry timing improves | PENDING |
| G5: Regime Filter | Reduces bear market losses | IMPLEMENTED |
| G6: Volume Filter | Reduces failed breakouts | IMPLEMENTED |
| G7: Categorical Assessment | Honest representation | IMPLEMENTED (Day 44) |
| G8: Fear & Greed Integration | Real sentiment data | IMPLEMENTED (Day 44) |

---

## DATA QUALITY VALIDATION PLAN (Next Session)

### Phase 1: Frontend Validation (Manual)
| Test | Method | Pass Criteria |
|------|--------|---------------|
| Trend Template Display | Compare UI vs `curl /api/patterns/TICKER` | Values match |
| RSI Display | Compare UI vs calculated from price history | Within 1.0 difference |
| Fear & Greed Display | Compare UI vs `curl /api/fear-greed` | Exact match |
| Viability Logic | Compare UI vs `curl /api/sr/TICKER` | Logic matches |

### Phase 2: Automated Validation
| Test | Script | Expected |
|------|--------|----------|
| 30-stock categorical test | `test_categorical_30stocks.py` | Distribution reasonable |
| Validation engine | Run on 20 tickers | Quality score > 85% |
| API response times | Measure latency | < 5 seconds per ticker |

### Phase 3: Edge Cases
| Scenario | Test Ticker | Expected Behavior |
|----------|-------------|-------------------|
| ETF (no fundamentals) | SPY, QQQ | Fundamental = "N/A" |
| Missing data | NEWIPO | Graceful fallback |
| Extreme overbought | Any RSI > 80 | Technical = "Weak" |
| Extreme oversold | Any RSI < 30 | Technical = "Weak" |

---

## SYSTEM HEALTH CHECK

### Backend v2.15
| Endpoint | Status | Notes |
|----------|--------|-------|
| /api/stock/:ticker | OK | Core data |
| /api/sr/:ticker | OK | S&R levels |
| /api/patterns/:ticker | OK | Pattern detection |
| /api/fear-greed | OK | CNN API with proper headers |
| /api/fundamentals/:ticker | OK | Defeat Beta primary |

### Frontend v4.1
| Component | Status | Notes |
|-----------|--------|-------|
| Categorical Assessment | OK | v4.5 complete |
| Recommendation Card | OK | Actionable guidance |
| Verdict Card | OK | Neutral design |
| Pattern Detection UI | OK | 8/8 trend template display |
| Fear & Greed Gauge | OK | Progress bar + value |

---

## DEFERRED ITEMS (v2+)

| Feature | Reason for Deferral |
|---------|---------------------|
| Sector Rotation (RRG) | Complex, marginal v1 value |
| Forward Testing UI | HIGH priority - next after validation |
| TradingView Lightweight Charts | After forward testing |
| Options Tab | Complex data sourcing |

---

## FILES MODIFIED (Day 44)

| File | Changes |
|------|---------|
| `backend/backend.py` | v2.15 - Fear & Greed endpoint |
| `backend/pattern_detection.py` | VCP, Cup-Handle, Flat Base |
| `frontend/src/utils/categoricalAssessment.js` | NEW - v4.5 categorical logic |
| `frontend/src/services/api.js` | v2.6 - fetchFearGreed(), fetchPatterns() |
| `frontend/src/App.jsx` | v4.1 - Recommendation card, neutral verdict |
| `backend/test_categorical_30stocks.py` | NEW - 30-stock validation test |
| `docs/claude/stable/ROADMAP.md` | Updated v4.2-v4.5 as complete |

---

*Previous: KNOWN_ISSUES_DAY41.md*
*Next: KNOWN_ISSUES_DAY46.md*
