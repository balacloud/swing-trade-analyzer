# Known Issues - Day 50 (February 9, 2026)

## Open Issues

*All 5 issues from Day 50 testing resolved in this session.*

---

## Resolved Issues (Day 50 - This Session)

### Resolved: Issue #1 - Position Size Banner Conflict ✅
**Fixed in:** v4.4 (Day 50)
**Description:** Position size banner conflicted with ADX recommendations and AVOID verdict
**Affected:** 9/14 tickers (64%)
**Fix:** Hide position_size_advice when verdict is AVOID or ADX < 20

### Resolved: Issue #2 - No Retry Button for API Errors ✅
**Fixed in:** v4.4 (Day 50)
**Description:** No way to retry when yfinance returns empty data
**Fix:** Added "Retry" button in error display section

### Resolved: Issue #3 - Entry Cards Hidden Instead of Grayed ✅
**Fixed in:** v4.4 (Day 50)
**Description:** Cards hidden when conditions not met, user couldn't see potential entries
**Affected:** 4/14 tickers
**Fix:** Now shows "Wait for Better Setup" warning AND grayed-out cards below

### Resolved: Issue #4 - R:R = 1.0 Edge Case ✅
**Fixed in:** v4.4 (Day 50)
**Description:** R:R exactly 1.00 showed "NOT VIABLE"
**Verification:** Reviewed code - already uses `>= 1.0` correctly. Issue was misread.

### Resolved: Issue #5 - VIABLE Badge + AVOID Conflict ✅
**Fixed in:** v4.4 (Day 50)
**Description:** Showed "VIABLE" badge when overall verdict was AVOID
**Fix:** Added warning tooltip: "⚠️ Stock not recommended"

---

## Resolved Issues (Day 49-50)

### Resolved: "$null-null" Support Zone Bug ✅
**Fixed in:** v4.3 (Day 49)
**Description:** Extended stocks with no nearby support showed "$null-null" in recommendation
**Example:** MU at $107.5 (43.2% extended) showed "Wait for pullback to $null-null zone"
**Fix:** Added conditional check for undefined support levels

### Resolved: Entry Uses Wrong Support Level ✅
**Fixed in:** v4.3 (Day 49)
**Description:** Pullback Entry was using `support[0]` (any level) instead of nearest support
**Fix:** Changed to `Math.max(...srData.support)` to get nearest (highest) support

### Resolved: Position "full" with "wait" Reason ✅
**Fixed in:** v4.3 (Day 49)
**Description:** Position showed "full" even when reason said "wait for better entry"
**Fix:** Position now dynamic based on ADX: full (>=25), reduced (20-25), wait (<20)

### Resolved: Generic VIABLE Badge ✅
**Fixed in:** v4.3 (Day 49)
**Description:** Badge just said "VIABLE" without specifying which strategy
**Fix:** Now shows "PULLBACK OK", "MOMENTUM OK", "BOTH VIABLE", or "NOT VIABLE"

### Resolved: R:R < 1.0 Not Filtered ✅
**Fixed in:** v4.2 (Day 49)
**Description:** Entry cards displayed even with terrible R:R
**Fix:** Cards grayed out with "⛔ R:R < 1" badge when R:R < 1.0

### Resolved: ADX-Based Entry Logic ✅
**Fixed in:** v4.2 (Day 49)
**Description:** Momentum was "SUGGESTED" even when ADX < 25 (no trend)
**Fix:** Corrected logic: ADX >=25 = PREFERRED, 20-25 = VIABLE, <20 = CAUTION

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 0 |
| Open - Low | 0 |
| **Total Open** | **0** |
| Resolved (Day 50 session) | 5 |
| Resolved (Day 49-50 prior) | 6 |
| **Total Resolved** | **11** |

---

## Test Results Summary
| Test | Pass Rate | Notes |
|------|-----------|-------|
| UI Cohesiveness (spot-check) | 13/14 (92.8%) | Day 49 - missed issues |
| UI Cohesiveness (exhaustive) | 3/14 (21%) | Day 50 - proper verification |

**Lesson:** Exhaustive verification reveals true state. Position Size banner is the #1 issue.
