# Complete UI Cohesiveness Test Findings - Day 50
> **Date:** February 9, 2026 (Re-verification)
> **Tester:** Claude (Exhaustive Review - ALL 14 PDFs)
> **Version:** Frontend v4.3, Backend v2.16

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total PDFs Tested | 14 |
| Pass (No Issues) | 3 |
| Issues Found | 11 |
| Critical Issues | 2 |
| High Priority | 1 |
| Medium Priority | 2 |
| Low Priority | 1 |

---

## Per-Ticker Analysis

| # | Ticker | Verdict | Pass/Fail | Issues |
|---|--------|---------|-----------|--------|
| 1 | MU | BUY | FAIL | "$null-null" in recommendation (FIXED v4.3) |
| 2 | CMCSA | HOLD | FAIL | Position Size "FULL" conflicts with NOT VIABLE |
| 3 | APA | HOLD | FAIL | Position Size "FULL" conflicts with Pullback "wait" |
| 4 | NVDA | HOLD | FAIL | Entry cards hidden (should be grayed out) |
| 5 | JNJ | ERROR | FAIL | **CRITICAL: No retry button for API error** |
| 6 | COIN | AVOID | FAIL | R:R=1.0 shows NOT VIABLE; Position Size conflict |
| 7 | F | HOLD | FAIL | Position Size "FULL" conflicts with ADX 12.1; Cards hidden |
| 8 | PLTR | AVOID | FAIL | "BOTH VIABLE" badge conflicts with AVOID verdict |
| 9 | XOM | HOLD | PASS | Position Size "NONE" correct for extended stock |
| 10 | SPY | HOLD | FAIL | Position Size "FULL" conflicts with ADX 11.9; Cards hidden |
| 11 | SMCI | AVOID | FAIL | Position Size "HALF" vs Pullback "wait" inconsistent |
| 12 | T | AVOID | PASS | Both R:R < 1, both cards grayed correctly |
| 13 | AFRM | AVOID | FAIL | Position Size "HALF" vs Pullback "full" inconsistent |
| 14 | VZ | AVOID | PASS | Setup messaging acceptable for AVOID |

---

## Consolidated Issues

### Issue #1: Position Size Banner Conflict (HIGH)
**Severity:** High | **Affected:** 9/14 tickers (64%)

**Problem:** The backend's `tradeViability.position_size_advice` shows position sizing that conflicts with:
- ADX-based entry recommendations (shows "FULL" when ADX < 20 says "wait")
- Overall verdict (shows "FULL" even when verdict is AVOID)
- Individual card recommendations (banner says "HALF" but card says "full")

**Affected Tickers:** CMCSA, APA, COIN, F, SPY, SMCI, T, AFRM, VZ

**Examples:**
- F: ADX 12.1 (< 20), Banner says "FULL", Cards say "Wait for Better Setup"
- COIN: Verdict AVOID, Banner says "FULL", Both R:R < 1
- AFRM: Banner says "HALF", Pullback card says Position "full"

**Recommended Fix:**
```javascript
// Hide position_size_advice when:
// 1. Showing "Wait for Better Setup" message (ADX < 20)
// 2. Both entry strategies have R:R < 1
// 3. Verdict is AVOID
const showPositionSizeBanner =
  adx >= 20 &&
  (pullbackRR >= 1 || momentumRR >= 1) &&
  verdict !== 'AVOID';
```

---

### Issue #2: No Retry Button for API Errors (CRITICAL)
**Severity:** Critical | **Affected:** 1/14 tickers (7%)

**Problem:** When yfinance returns empty data (transient API issue), user sees "No data found for {ticker}" with no way to retry.

**Affected Tickers:** JNJ

**Evidence:** JNJ PDF shows "No data found for JNJ" - a transient error that works on retry.

**Recommended Fix:**
```jsx
{error && (
  <div className="error-display">
    <p>{error}</p>
    <button onClick={() => analyzeStock(ticker)}>
      Retry
    </button>
  </div>
)}
```

---

### Issue #3: Entry Cards Hidden Instead of Grayed Out (MEDIUM)
**Severity:** Medium | **Affected:** 4/14 tickers (29%)

**Problem:** When entry conditions not met (ADX < 20 or both R:R < 1), cards are completely hidden. User cannot see what the entries WOULD look like.

**Affected Tickers:** NVDA, F, XOM, SPY

**Current Behavior:** Shows "Wait for Better Setup" warning with no entry cards
**Expected Behavior:** Shows warning AND grayed-out cards below it

**Recommended Fix:**
```jsx
{/* Always show cards, but gray out when not viable */}
<div className={`entry-card ${!isViable ? 'grayed-out' : ''}`}>
  {!isViable && <div className="overlay">Not Recommended</div>}
  {/* Card content */}
</div>
```

---

### Issue #4: R:R = 1.0 Edge Case (LOW)
**Severity:** Low | **Affected:** 1/14 tickers (7%)

**Problem:** COIN shows R:R exactly 1.00 but displays "NOT VIABLE" with red badge.

**Affected Tickers:** COIN

**Root Cause:** Likely using `> 1.0` instead of `>= 1.0`

**Recommended Fix:**
```javascript
// Change from:
const isViable = riskReward > 1.0;
// To:
const isViable = riskReward >= 1.0;
```

---

### Issue #5: VIABLE Badge Conflicts with AVOID Verdict (MEDIUM)
**Severity:** Medium | **Affected:** 2/14 tickers (14%)

**Problem:** Shows "BOTH VIABLE" or "PULLBACK OK" badge when overall verdict is AVOID. This is confusing - the setup might be viable but the stock isn't recommended.

**Affected Tickers:** PLTR, VZ

**Examples:**
- PLTR: Verdict AVOID, but shows "BOTH VIABLE" in green
- VZ: Verdict AVOID, but shows "PULLBACK OK" with "Good setup" message

**Recommended Fix:** Add contextual warning when verdict is AVOID:
```jsx
{verdict === 'AVOID' && isAnyViable && (
  <span className="warning-note">
    (Setup viable but stock not recommended)
  </span>
)}
```

---

### Issue #6: "$null-null" Support Zone Bug (RESOLVED)
**Status:** FIXED in v4.3

**Problem:** Extended stocks with no nearby support showed "$null-null" in recommendation.

**Example:** MU at $107.5 (43.2% extended) showed "Wait for pullback to $null-null zone"

**Fix Applied:** Added conditional check for undefined support levels.

---

## Action Plan

### Immediate (P1) - Fix Today
1. **Issue #2:** Add retry button for API errors
2. **Issue #1:** Hide position size banner when conflicting

### Short-term (P2) - This Week
3. **Issue #3:** Gray out entry cards instead of hiding
4. **Issue #5:** Add warning note when AVOID + VIABLE conflict

### Low Priority (P3)
5. **Issue #4:** Fix R:R >= 1.0 edge case

---

## Test Criteria Reference

Each ticker was checked against:
1. **Verdict Logic:** T:W/D/S + F:W/D/S + S:W/N/S + R:U/N/F = Correct verdict
2. **Entry Cards:** R:R display, Position sizing, ADX badges
3. **Position Size Banner:** Consistency with cards and verdict
4. **TT Stage 2:** Only shows "In Stage 2 Uptrend" when TT >= 7/8
5. **Recommendation Card:** Matches verdict (BUY/HOLD/AVOID)
6. **No Null/Undefined Values:** All fields populated correctly

---

## Lessons Learned

1. **Exhaustive testing is non-negotiable** - Spot-checking missed the MU bug initially
2. **Position size is the #1 inconsistency source** - Backend and frontend have different logic
3. **VIABLE vs VERDICT distinction needs UX clarity** - Users confused when both shown

---

*Generated: Day 50 - Exhaustive PDF Review*
*Previous: FINDINGS_AND_ACTION_PLAN.md (spot-check version)*
