# Known Issues - Day 49 (February 9, 2026)

## Open Issues

### Issue #1: Old Position Size Banner Conflict (HIGH)
**Severity:** High | **Component:** Frontend UI
**Description:** The backend's `tradeViability.position_size_advice` shows "FULL - low risk entry" even when ADX < 20. This conflicts with our new entry cards that say "wait" based on ADX.
**Example:** F (Ford) - ADX 12.1 < 20, old banner says "FULL", but entry cards show "Wait for Better Setup"
**Fix:** Hide position_size_advice line when showing "Wait for Better Setup" message
**File:** `frontend/src/App.jsx`

### Issue #2: Transient Data Fetch Errors (HIGH)
**Severity:** High | **Component:** Frontend UX
**Description:** When yfinance returns empty data (transient API issue), user sees "No data found for {ticker}" with no way to retry.
**Example:** JNJ failed during UI test but works now (transient issue)
**Root Cause:** Backend returns 404 when `hist.empty`, frontend has no retry mechanism
**Fix:** Add "Retry" button in error display
**File:** `frontend/src/App.jsx` (error display section)

### Issue #3: Entry Cards Should Gray Out, Not Hide (MEDIUM)
**Severity:** Medium | **Component:** Frontend UI
**Description:** When both entry strategies have bad R:R or no trend, we should still show the cards (grayed out) instead of hiding them. User needs to see what the entries would look like.
**Current Behavior:** Shows "Wait for Better Setup" warning and hides cards
**Expected:** Show warning AND grayed-out cards below it
**File:** `frontend/src/App.jsx` (Entry Strategy section)

### Issue #4: R:R = 1.0 Edge Case (LOW)
**Severity:** Low | **Component:** Frontend Logic
**Description:** COIN shows R:R exactly 1.00 but displays "NOT VIABLE"
**Expected:** R:R >= 1.0 should be considered viable
**Fix:** Verify pullbackRRValue >= 1.0 check (not > 1.0)
**File:** `frontend/src/App.jsx`

---

## Resolved Issues (Day 49)

### Resolved: Entry Uses Wrong Support Level ✅
**Fixed in:** v4.3
**Description:** Pullback Entry was using `support[0]` (any level) instead of nearest support
**Fix:** Changed to `Math.max(...srData.support)` to get nearest (highest) support

### Resolved: Position "full" with "wait" Reason ✅
**Fixed in:** v4.3
**Description:** Position showed "full" even when reason said "wait for better entry"
**Fix:** Position now dynamic based on ADX: full (>=25), reduced (20-25), wait (<20)

### Resolved: Generic VIABLE Badge ✅
**Fixed in:** v4.3
**Description:** Badge just said "VIABLE" without specifying which strategy
**Fix:** Now shows "PULLBACK OK", "MOMENTUM OK", "BOTH VIABLE", or "NOT VIABLE"

### Resolved: R:R < 1.0 Not Filtered ✅
**Fixed in:** v4.2
**Description:** Entry cards displayed even with terrible R:R
**Fix:** Cards grayed out with "⛔ R:R < 1" badge when R:R < 1.0

### Resolved: ADX-Based Entry Logic ✅
**Fixed in:** v4.2
**Description:** Momentum was "SUGGESTED" even when ADX < 25 (no trend)
**Fix:** Corrected logic: ADX >=25 = PREFERRED, 20-25 = VIABLE, <20 = CAUTION

### Resolved: MU "$null-null" Support Zone Bug ✅
**Fixed in:** v4.3
**Description:** Extended stocks with no nearby support levels showed "$null-null" in recommendation
**Example:** MU at $107.5 (43.2% extended) showed "Wait for pullback to $null-null zone before entry"
**Fix:** Added conditional check - shows alternative text when support levels unavailable

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - High | 2 |
| Open - Medium | 1 |
| Open - Low | 1 |
| Resolved Today | 6 |
