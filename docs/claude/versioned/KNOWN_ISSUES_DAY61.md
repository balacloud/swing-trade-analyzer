# Known Issues - Day 61 (February 27, 2026)

## Open Issues

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library

### Info: epsGrowth Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: forwardPe Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: Negative D/E Edge Case in Scoring
**Severity:** Info (pre-existing from Day 53)

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)

### Info: Backtest Max Drawdown Still High
**Severity:** Info (backtest-only, not production)
**Description:** Config C max drawdown by period: Quick 39.4%, Standard 52.5%, Position 66.5%
**Context:** Per-trade sequential drawdown across all trades without portfolio-level position sizing
**Action:** User handling position sizing separately

### Info: Position Period Regime-Sensitive
**Severity:** Info (backtest finding)
**Description:** Position holding period (15-45d) has low WR (38.67%) but high avg winners (8.05%). Walk-forward showed IS profit factor of only 1.14 vs OOS 1.53 — highly dependent on market regime.

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated
**Severity:** Info (assumption logged, advisory only)
**Description:** ADX >= 25 vs 20-25 for entry preference was never independently backtested.
**Action:** Not urgent — entry preference is advisory (doesn't change verdict).

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: yfinance Reliability for .TO Tickers
**Severity:** Info (monitoring needed)
**Description:** SHOP.TO returned price but null SMA/RSI on first fetch.

### Info: ROE Heuristic Fails for ROE >= 100%
**Severity:** Info (edge case, found Day 61 audit)
**Description:** ROE heuristic `lambda v: v * 100 if v and abs(v) < 1 else v` fails for ROE >= 100% (value 1.2 treated as 1.2% instead of 120%). Affects financial sector stocks with high leverage.
**Impact:** Stocks like GS, MS with ROE > 100% may be underscored.
**Action:** Low priority — rare edge case, mostly financial sector.

### Info: _growth_to_pct Cliff at 500% Growth
**Severity:** Info (edge case, found Day 61 audit)
**Description:** `_growth_to_pct` threshold at `abs(v) < 5` creates cliff at exactly 500% growth (value 5.0 stays as 5.0 instead of becoming 500.0).
**Impact:** Extremely rare — only affects stocks with exactly 500% growth.

### Info: Dual Entry Cards R:R Still Inline
**Severity:** Info (accepted, Day 61)
**Description:** Dual Entry Strategy Cards in App.jsx (~lines 1334-1484) still use inline R:R calculation instead of shared `riskRewardCalc.js` utility. Left intentionally because display values are tightly coupled to card UI.
**Action:** Acceptable — formulas identical to utility, no maintenance risk.

### Info: 11 Unused Backend Fields in S&R Response
**Severity:** Info (found Day 61 audit)
**Description:** Backend sends OBV, RVOL, rsi_4h, etc. in `/api/sr/` that frontend doesn't display.
**Action:** Low priority — no harm, possible future use.

### Info: Fundamentals Scorer Generates Verdict When All Data is Null
**Severity:** Info (found Day 61 audit Layer 4)
**Description:** When fundamentals fetch returns 404, `assessFundamental()` still generates "Weak" verdict (no criteria met = all fail). User sees assessment as if fundamentals were analyzed.
**Action:** Consider returning "Unknown" instead of "Weak" when all inputs are null.

---

## Resolved Issues (Day 61 - This Session)

### Resolved: Stale Cache Serves Growth Values in Wrong Format
**Was:** CRITICAL (affects paper trading decisions)
**Root Cause:** `_growth_to_pct` transform added Day 60, but fundamentals cache had 7-day TTL. Cached entries retained old decimal format (0.183 instead of 18.3).
**Fix:** Cleared 56 stale cache entries + added cache schema versioning (v2) to invalidate old entries automatically.
**Files:** `backend/cache_manager.py`

### Resolved: NaN Passes Through Transform Functions into JSON
**Was:** CRITICAL (NaN not valid JSON per RFC 7159)
**Root Cause:** Transform functions checked for `None` but not `float('nan')`. Ford (F) had `epsGrowth: NaN`.
**Fix:** Added `_is_nan()` helper and NaN checks to all transforms in field_maps.py + `_sanitize()` in categoricalAssessment.js + priceHistory NaN filtering in backend.py.
**Files:** `backend/providers/field_maps.py`, `frontend/src/utils/categoricalAssessment.js`, `backend/backend.py`

### Resolved: F&G Assessment Threshold Drift (Backend vs Frontend)
**Was:** MEDIUM (backend assessment field was dead code)
**Root Cause:** Backend used Day 44 thresholds (Strong: 55-75), frontend used Day 56 thresholds (Strong: 60-80).
**Fix:** Updated backend thresholds to match frontend (60-80, 35-60, <35/>80).
**File:** `backend/backend.py`

### Resolved: Earnings Endpoint Returns 200 on Error
**Was:** MEDIUM (indistinguishable from "no upcoming earnings")
**Fix:** Changed to return HTTP 500 on exception. api.js catch returns `hasUpcoming: null` (not `false`).
**Files:** `backend/backend.py`, `frontend/src/services/api.js`

### Resolved: F&G Fallback Flag Stripped by api.js
**Was:** LOW (lost fallback information)
**Fix:** Added `fallback: data.fallback || false` to fetchFearGreed return object.
**File:** `frontend/src/services/api.js`

### Resolved: R:R Calculation Duplicated in 4 Locations
**Was:** MEDIUM (maintenance risk)
**Fix:** Extracted to shared `riskRewardCalc.js` with `calculateRiskReward()`, `hasViabilityContradiction()`, `getViabilityBadge()`. Used by App.jsx (2 locations), DecisionMatrix.jsx, BottomLineCard.jsx.
**Files:** `frontend/src/utils/riskRewardCalc.js` (new), + 3 consumer files

### Resolved: DecisionMatrix momentumStop ESLint Error
**Was:** ERROR (frontend won't compile)
**Root Cause:** `momentumStop` not included in destructuring after R:R refactor to shared utility.
**Fix:** Added `momentumStop` to destructured properties from `calculateRiskReward()`.
**File:** `frontend/src/components/DecisionMatrix.jsx`

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY60.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 2 |
| Open - Info | 12 |
| **Total Open** | **15** |
| Resolved (Day 61 session) | 7 |
