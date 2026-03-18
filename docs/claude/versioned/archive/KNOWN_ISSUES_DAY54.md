# Known Issues - Day 54 (February 16, 2026)

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
**Found during:** Phase 1 reconciliation (Day 53)

### Info: forwardPe Not Shown in Categorical Assessment
**Severity:** Info (pre-existing)
**Description:** forwardPe is scored in scoringEngine (0-2 pts) but not assessed in categoricalAssessment.js
**Impact:** Minor - 2 pts max, and P/E is a known metric traders check independently
**Found during:** Phase 1 reconciliation (Day 53)

### Info: Negative D/E Edge Case in Scoring
**Severity:** Info (pre-existing)
**Description:** scoringEngine.js gives 3 pts for debtToEquity < 0.5, which includes negative D/E ratios
**Impact:** Companies with negative equity (e.g., McDonald's due to buybacks) get maximum D/E score
**Found during:** Phase 1 reconciliation (Day 53)

### Info: Simple Checklist Missing 5 Minervini Criteria
**Severity:** Info (enhancement, not bug)
**Description:** Simple Checklist has 4 criteria (TREND, MOMENTUM, SETUP, R:R) but lacks:
  1. 52-week range filters (within 25% of high, 25%+ above low)
  2. Volume confirmation (RVOL ≥ 1.5)
  3. ADX/RSI momentum check (ADX ≥ 20)
  4. Market regime filter (SPY above 200 SMA)
  5. ATR-based stops (instead of hardcoded 3%)
**Impact:** Checklist passes stocks that Minervini would reject (50% SEPA alignment)
**Action:** Enhance AFTER backtest validates what criteria actually matter
**Found during:** Day 54 pre-backtest audit

### Medium: EPS/Revenue Growth Using QoQ Instead of YoY
**Severity:** Medium (incorrect methodology)
**Description:** `yfinance_provider.py` calculates revenueGrowth by comparing adjacent quarters (Q4 vs Q3 = QoQ). epsGrowth is missing entirely — Finnhub doesn't have it, FMP free tier 403s, yfinance `info['earningsGrowth']` often returns None.
**Impact:** QoQ growth is distorted by seasonality (e.g., retail Q4 always > Q3). Industry standard for swing trading (Finviz, Minervini/SEPA, IBD) is YoY quarterly (Q4 2025 vs Q4 2024).
**Fix required:** Change both revenue and EPS growth to YoY (needs ≥5 quarters of data). Don't just add epsGrowth with the same QoQ bug.
**Action:** Fix AFTER backtest planning — methodology decision needed first
**Found during:** Day 54 validation fix review

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)
**Description:** Fear & Greed Index is a lagging, macro-level narrative tool. CNN API is unreliable (frequent failures). Already redundant with VIX in `assessRiskMacro()`.
**Evidence:** Research shows declining predictive power, lagging structure, and inferior to pure price-volume indicators for swing trading.
**Recommendation:** Don't include as backtest variable. Consider removing from categorical assessment in favor of VIX-only macro risk.
**Found during:** Day 54 pre-backtest discussion

---

## Resolved Issues (Day 54 - This Session)

### Resolved: Sentiment Score Hardcoded 5/10 ✅
**Fixed in:** Day 54
**Description:** `calculateSentimentScore()` in scoringEngine.js returned hardcoded 5/10
**Impact:** Legacy 75-point score inflated by 5 phantom points for every stock
**Fix:** Returns 0/10 with note — real sentiment handled by categorical assessment

### Resolved: Market Breadth Hardcoded to 1 Point ✅
**Fixed in:** Day 54
**Description:** `scores.breadth = 1` in scoringEngine.js — no data source, always 1/1
**Impact:** Legacy risk score inflated by 1 point for every stock
**Fix:** Returns 0/1 — honest about missing data

### Resolved: Fear & Greed Silent Fallback to 50 ✅
**Fixed in:** Day 54
**Description:** Both backend and frontend returned `value: 50, rating: "Neutral"` when CNN API failed
**Impact:** Categorical assessment made decisions on phantom sentiment data
**Fix:** Backend marks with `fallback: true`, frontend returns `null`. `assessSentiment()` catches both and returns gray "Unavailable"

### Resolved: VIX Silent Fallback to 20 ✅
**Fixed in:** Day 54
**Description:** `fetchVIXData()` returned `{current: 20, regime: "normal"}` on error
**Impact:** Risk assessment used phantom data — always showed "normal volatility"
**Fix:** Returns `{current: null, fallback: true}`. `assessRiskMacro()` handles null VIX with SPY-only assessment

---

## Resolved Issues (Prior Sessions)

### Resolved: Bug #7 - RS Rating Always Red ✅ (Day 53)
### Resolved: Bug #8 - Competing Viability Signals ✅ (Day 53)
### Resolved: Hardcoded Zeros Corrupting Scoring ✅ (Day 53)
### Resolved: Dual Fundamentals Endpoints (SRP Violation) ✅ (Day 53)
### Resolved: Legacy Dead Code (~255 lines) ✅ (Day 53)
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
| Open - Info | 4 |
| **Total Open** | **6** |
| Resolved (Day 54 session) | 4 |
| Resolved (Prior sessions) | 17+ |
