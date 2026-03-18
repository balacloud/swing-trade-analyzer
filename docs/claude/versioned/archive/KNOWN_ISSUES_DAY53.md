# Known Issues - Day 53 (February 15, 2026)

## Open Issues

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically
**Status:** Monitoring - may need FMP account verification

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library and defines DEFEATBETA_AVAILABLE constant
**Impact:** None - all 3 functions that used it are removed. Only informational references remain (health check response, startup log).
**Action:** Can be fully removed when convenient. Does not affect behavior.

### Info: epsGrowth Not Shown in Categorical Assessment
**Severity:** Info (pre-existing)
**Description:** epsGrowth is scored in scoringEngine (0-6 pts) but not displayed in categorical assessment reasons
**Impact:** Trader doesn't see epsGrowth assessment in the UI Assessment card
**Found during:** Phase 1 reconciliation

### Info: forwardPe Not Shown in Categorical Assessment
**Severity:** Info (pre-existing)
**Description:** forwardPe is scored in scoringEngine (0-2 pts) but not assessed in categoricalAssessment.js
**Impact:** Minor - 2 pts max, and P/E is a known metric traders check independently
**Found during:** Phase 1 reconciliation

### Info: Negative D/E Edge Case in Scoring
**Severity:** Info (pre-existing)
**Description:** scoringEngine.js gives 3 pts for debtToEquity < 0.5, which includes negative D/E ratios
**Impact:** Companies with negative equity (e.g., McDonald's due to buybacks) get maximum D/E score
**Found during:** Phase 1 reconciliation

---

## Resolved Issues (Day 53 - This Session)

### Resolved: Bug #7 - RS Rating Always Red ✅
**Fixed in:** Day 53
**Description:** RS Rating displayed red color regardless of actual RS value
**Root cause:** Type mismatch — string compared to number threshold
**Fix:** Proper type conversion before comparison

### Resolved: Bug #8 - Competing Viability Signals ✅
**Fixed in:** Day 53
**Description:** "Good setup" banner displayed simultaneously with "NOT VIABLE" badge
**Root cause:** Independent display logic for setup quality vs viability
**Fix:** Unified signal — viability overrides setup banner

### Resolved: Hardcoded Zeros Corrupting Scoring ✅
**Fixed in:** Day 53 (Phase 1A)
**Description:** `/api/stock/` returned `roe: 0, epsGrowth: 0, revenueGrowth: 0, debtToEquity: 0` when real data unavailable
**Impact:** D/E=0 scored as "Strong" (3 pts), revenueGrowth=0 as "Decent", roe=0 as "Weak" — all false
**Fix:** Changed to null, then removed fundamentals from `/api/stock/` entirely (Phase 2A)

### Resolved: Dual Fundamentals Endpoints (SRP Violation) ✅
**Fixed in:** Day 53 (Phase 2A)
**Description:** Both `/api/stock/` and `/api/fundamentals/` returned fundamentals data
**Impact:** When frontend merged them, zeros from `/api/stock/` could persist if merge order was wrong
**Fix:** Removed fundamentals from `/api/stock/`. Single source: `/api/fundamentals/` via DataProvider.

### Resolved: Legacy Dead Code (~255 lines) ✅
**Fixed in:** Day 53 (Phase 2C)
**Description:** `get_fundamentals_defeatbeta()` (228 lines), `get_fundamentals_yfinance()` (90 lines), `_check_defeatbeta_status()` (24 lines) — all superseded by DataProvider
**Fix:** Removed all 3 functions + cleaned health check endpoint

### Resolved: Defeat Beta Still Imported (Partial) ✅
**Fixed in:** Day 53 (Phase 2C)
**Description:** Was listed as open issue Day 52. Functions removed, but import/constant kept (informational only).
**Status:** Downgraded from "Low" to "Info" — behavioral impact eliminated

---

## Resolved Issues (Prior Sessions)

### Resolved: yfinance Single-Point-of-Failure ✅ (Day 52)
### Resolved: Position Size Banner Conflict ✅ (Day 50)
### Resolved: Entry Cards Hidden Instead of Grayed ✅ (Day 50)
### Resolved: VIABLE Badge + AVOID Conflict ✅ (Day 50)
### Resolved: "$null-null" Support Zone Bug ✅ (Day 49)
### Resolved: Entry Uses Wrong Support Level ✅ (Day 49)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 0 |
| Open - Low | 2 |
| Open - Info | 3 |
| **Total Open** | **5** |
| Resolved (Day 53 session) | 6 |
| Resolved (Prior sessions) | 14+ |
