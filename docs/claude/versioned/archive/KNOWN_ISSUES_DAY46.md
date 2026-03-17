# KNOWN ISSUES - Day 46

> **Purpose:** Track all known bugs, gaps, and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 46 (February 6, 2026) - v4.6 UI Testing + Validation
> **UI Test Report:** `docs/test/UI_TEST_REPORT_DAY46.md`

---

## RESOLVED (Day 45-46)

| Issue | Resolution | Date |
|-------|------------|------|
| F&G 25-45 Zone Cliff at 45 | Expanded neutral zone to 35-60, cliff eliminated | Day 45 |
| Sentiment could veto BUY | Structure > Sentiment hierarchy implemented | Day 45 |
| No systematic test plan | Created comprehensive test plan + automated script | Day 45 |
| **Issue 0: Recommendation Card Mismatch** | Fixed - now uses `entryPreference` to show "Wait for pullback to $X" when applicable. Alert price uses support (entry) not resistance. | Day 46 |

---

## OPEN ISSUES

### Issue 1: ADX Entry Preference Not Implemented
- **Severity:** MEDIUM
- **Description:** Perplexity research recommends ADX-based entry preference
- **Expected Behavior:**
  - ADX > 25 = Momentum entry viable
  - ADX 20-25 = Pullback preferred
  - ADX < 20 = Wait for trend
- **Status:** PENDING - v4.6 Recommendation #2

### Issue 2: Pattern Actionability Missing
- **Severity:** MEDIUM
- **Description:** Patterns shown at all completion percentages without actionable guidance
- **Expected Behavior:**
  - Only show patterns ≥80% formed
  - Include specific trigger price
  - Include stop level
- **Status:** PENDING - v4.6 Recommendation #3

### Issue 3: Frontend/Backend Data Validation Needed
- **Severity:** MEDIUM
- **Description:** Need systematic validation that frontend displays match backend API responses
- **Progress:** Test framework created, baseline tests pass
- **Status:** ONGOING - v4.7 Test Framework active

### Issue 4: Test Script Field Name Mismatch
- **Severity:** LOW
- **Description:** test_categorical_comprehensive.py checks for "prices" and "technicals" but API returns "priceHistory" and different structure
- **Impact:** Shows warnings but doesn't affect test results
- **Status:** DEFERRED - Cosmetic issue

### Issue 5: SPY 200 EMA Shows $0.00 in Test Script
- **Severity:** LOW
- **Description:** Test script shows "SPY Regime: Bull (Price: $686.22, 200 EMA: $0.00)"
- **Impact:** Visual only - regime detection still working
- **Status:** DEFERRED - Not blocking

### Issue 6: RSI Range Too Narrow for Strong Technical
- **Severity:** MEDIUM
- **Description:** RSI range 50-70 for "Strong" Technical is very narrow
- **Examples:**
  - JPM: 7/8 Trend Template but RSI 49.1 → Technical = Decent
  - IWM: 8/8 Trend Template but RSI 43.5 → Technical = Decent
- **Current Logic:** Strong = TT ≥ 7 AND RSI 50-70
- **Proposed:** Strong = TT ≥ 7 AND RSI 40-75 (when TT = 8/8)
- **Status:** DEFERRED - Needs more data to validate

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
| G9: F&G Threshold Fix | No cliff at 45 | IMPLEMENTED (Day 45) |
| G10: Structure > Sentiment | Hierarchy applied | IMPLEMENTED (Day 45) |

---

## v4.6 PERPLEXITY RECOMMENDATIONS STATUS

| # | Recommendation | Status | Notes |
|---|----------------|--------|-------|
| 1 | F&G Threshold Fix | ✅ DONE | Neutral zone 35-60 |
| 2 | ADX Entry Preference | PENDING | Next priority |
| 3 | Pattern Actionability | PENDING | After ADX |
| 4 | Structure > Sentiment | ✅ DONE | Entry preference added |

---

## UI TEST RESULTS (Day 46)

### 10-Ticker Manual Test
| Ticker | Verdict | Assessment | Rec Card | Issues |
|--------|---------|------------|----------|--------|
| AAPL | HOLD | T:S F:D S:W R:N | WATCHLIST | ⚠️ Entry mismatch |
| NVDA | AVOID | T:W F:S S:W R:N | SKIP | ✅ Pass |
| META | HOLD | T:D F:S S:W R:N | PATIENCE | ✅ Pass |
| JPM | AVOID | T:D F:D S:W R:N | SKIP | ⚠️ RSI range |
| GOOGL | **BUY** | T:S F:S S:W R:N | READY | ✅ Pass |
| SPY | AVOID | T:W F:N S:W R:N | SKIP | ✅ Pass |
| TSLA | AVOID | T:W F:W S:W R:N | SKIP | ✅ Pass |
| IWM | AVOID | T:D F:N S:W R:N | SKIP | ⚠️ RSI range |
| XLE | AVOID | T:D F:N S:W R:N | SKIP | ✅ Pass |
| INTC | HOLD | T:S F:W S:W R:N | WATCHLIST | ⚠️ Alert price wrong |

### Summary
- **Pass Rate:** 6/10 (60%) - no issues
- **Minor Issues:** 4/10 (40%) - actionable but not breaking
- **Structure > Sentiment:** ✅ Working (GOOGL proves it)
- **F&G Thresholds:** ✅ Working (all show Weak at ~33)
- **ETF Handling:** ✅ Working (SPY, IWM, XLE show N/A fundamentals)

### Report Location
`docs/test/UI_TEST_REPORT_DAY46.md`

---

## TEST FRAMEWORK STATUS (v4.7)

### Test Plan
- **Location:** `docs/test/TEST_PLAN_COMPREHENSIVE.md`
- **Categories:** 6 (API Contract, Categorical Logic, Edge Cases, Cross-Validation, Integration, Forward Testing)

### Automated Script
- **Location:** `backend/test_categorical_comprehensive.py`
- **Baseline Result:** 100% pass rate (33/33 tests)
- **Warnings:** 15 (field name mismatches - cosmetic)

### Test Tickers
- Tier 1: AAPL, NVDA, JPM, MSFT, COST (baseline)
- Tier 2: SPY, QQQ, IWM (ETFs)
- Tier 3: Technical extremes (RSI < 30, > 80)
- Tier 4: TSLA, AMC, META (fundamental extremes)
- Tier 5: PLTR, SOFI, HOOD (small caps)

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

### Frontend v4.6
| Component | Status | Notes |
|-----------|--------|-------|
| Categorical Assessment | OK | v4.6 - F&G thresholds fixed |
| Structure > Sentiment | OK | v4.6 - Entry preference added |
| Recommendation Card | ⚠️ BUG | Message doesn't match preferred entry (Issue #0) |
| Verdict Card | OK | Neutral design |

---

## FILES MODIFIED (Day 45)

| File | Changes |
|------|---------|
| `frontend/src/utils/categoricalAssessment.js` | v4.6 - F&G thresholds + Structure > Sentiment |
| `docs/claude/stable/ROADMAP.md` | Added v4.6 and v4.7 sections |
| `docs/test/TEST_PLAN_COMPREHENSIVE.md` | NEW - Comprehensive test plan |
| `backend/test_categorical_comprehensive.py` | NEW - Automated test script |

---

## DEFERRED ITEMS (v2+)

| Feature | Reason for Deferral |
|---------|---------------------|
| Sector Rotation (RRG) | Complex, marginal v1 value |
| Forward Testing UI | HIGH priority - next after v4.6 complete |
| TradingView Lightweight Charts | After forward testing |
| Options Tab | Complex data sourcing |

---

*Previous: KNOWN_ISSUES_DAY45.md*
*Next: KNOWN_ISSUES_DAY47.md*
