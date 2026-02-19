# Known Issues - Day 56 (February 19, 2026)

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
**Description:** Config C backtest shows 52.6% max drawdown. Per-trade sequential drawdown across 246 trades without position sizing.
**Context:** Bear regime filter (Day 56) not yet validated — may reduce this
**Action:** User handling position sizing separately

---

## Resolved Issues (Day 56 - This Session)

### Resolved: Scan Market Missing 5th Filter in Fallback ✅
**Fixed in:** Day 56
**Description:** App.jsx hardcoded fallback had 4 scan filters. Added 5th "Best Candidates" option.
**Additional:** Redesigned filter to match backtested Config C criteria (ADX>=20, RSI 50-70, EMA momentum)

### Resolved: Pattern Confidence Mismatch (80% vs 60%) ✅
**Fixed in:** Day 56
**Description:** `categoricalAssessment.js` used 80% threshold but backtest validated 60% (Config C: PF 1.61, p=0.002)
**Fix:** Lowered `PATTERN_ACTIONABILITY_THRESHOLD` from 80 to 60

### Resolved: Bear Regime Not Gating Entries ✅
**Fixed in:** Day 56
**Description:** Backtest detected "early bear" (SPY 50 SMA declining) but didn't use it to gate entries
**Fix:** Added `spy_50sma_declining` parameter — caps risk assessment at "Neutral" during early bear
**Impact:** Pending re-run to validate

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY55.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 2 |
| Open - Info | 5 |
| **Total Open** | **8** |
| Resolved (Day 56 session) | 3 |
