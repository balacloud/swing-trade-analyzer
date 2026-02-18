# Known Issues - Day 55 (February 18, 2026)

## Open Issues

### Low: Scan Market Missing 5th Filter in Fallback
**Severity:** Low (cosmetic when backend not running)
**Description:** App.jsx hardcoded fallback (lines 2356-2361) has 4 scan filters. The 5th "Best Candidates" filter only loads dynamically from `/api/scan/strategies`. When backend fails to load, dropdown shows 4 instead of 5.
**Fix:** Add `<option value="best">Best Candidates - Most likely BUY</option>` to fallback list
**Found during:** Day 55 session

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

### Info: Simple Checklist Missing 5 Minervini Criteria
**Severity:** Info (enhancement, not bug)
**Description:** Simple Checklist has 4 criteria but lacks 52-week range, volume, ADX, market regime, ATR stops
**Action:** Enhance AFTER backtest validates what criteria matter

### Medium: EPS/Revenue Growth Using QoQ Instead of YoY
**Severity:** Medium (incorrect methodology)
**Description:** `yfinance_provider.py` calculates revenueGrowth QoQ instead of YoY
**Action:** Fix after backtest — methodology decision needed

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)

### Info: Backtest Max Drawdown Still High (52.6%)
**Severity:** Info (backtest-only, not production)
**Description:** Config C backtest shows 52.6% max drawdown. This is per-trade sequential drawdown across 246 trades without position sizing. Real drawdown with Minervini-style 1% risk per trade would be significantly lower.
**Context:** Drawdown in backtest = cumulative sequential return, not portfolio-level. No position sizing applied.
**Action:** User handling position sizing separately

---

## Resolved Issues (Day 55 - This Session)

### Resolved: Config C Producing 0 Trades ✅
**Fixed in:** Day 55
**Root Cause:** `compute_sr_levels()` expects lowercase columns (close, high, low) but yfinance returns capitalized (Close, High, Low). Every call silently failed via bare `except`.
**Additional fixes:** Support/resistance indexing (max/min for nearest), accepted CAUTION viability, ATR-based R:R fallback
**Impact:** Config C went from 0 → 238 trades

### Resolved: Standard Target Unreachable (10%) ✅
**Fixed in:** Day 55
**Root Cause:** Data showed zero Config C trades reaching 10% MFE. Target was unreachable.
**Fix:** Lowered to 8%, added 10-day EMA trailing stop + breakeven stop
**Impact:** max_hold exits dropped 130 → 92, trailing_ema_exit captures 27 trades

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY54.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 3 |
| Open - Info | 5 |
| **Total Open** | **9** |
| Resolved (Day 55 session) | 2 |
