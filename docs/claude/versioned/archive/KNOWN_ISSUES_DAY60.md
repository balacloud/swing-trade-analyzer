# Known Issues - Day 60 (February 25, 2026)

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
**Note:** Quick period has most reasonable drawdown; Position is regime-sensitive (mostly bear-period losses)
**Action:** User handling position sizing separately

### Info: Position Period Regime-Sensitive
**Severity:** Info (backtest finding)
**Description:** Position holding period (15-45d) has low WR (38.67%) but high avg winners (8.05%). Walk-forward showed IS profit factor of only 1.14 vs OOS 1.53 — highly dependent on market regime.
**Action:** Consider adding UI warning when selecting Position period outside bull regime

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated
**Severity:** Info (assumption logged, advisory only)
**Description:** The distinction between "momentum viable" (ADX >= 25) and "pullback preferred" (ADX 20-25) was never independently backtested. Backtest validated ADX >= 20 as trend filter, but the 25 threshold for entry preference is arbitrary.
**Source:** AI Fluency Critical Analysis (Day 59)
**Action:** Not urgent — entry preference is advisory (doesn't change BUY/HOLD/AVOID verdict). Validate if entry logic is ever refined.

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. The full **Analyze** page does NOT work for Canadian tickers yet. Requires:
- Data source redesign: TwelveData/Finnhub/FMP may not cover TSX tickers — need to verify coverage and add yfinance-first fallback for `.TO` tickers
- Fundamentals: Canadian companies may not be in FMP/Finnhub free tier — need research
- S&R engine, pattern detection, categorical assessment: likely work as-is (math is math) but untested
- Sector rotation: Canadian sectors map to same SPDR ETFs? Or need TSX sector ETFs?
- Fear & Greed: US-only indicator — may need Canadian equivalent or just use US as proxy
**Action:** Separate task for future session — design data flow for Canadian Analyze page

### Info: yfinance Reliability for .TO Tickers
**Severity:** Info (monitoring needed)
**Description:** SHOP.TO returned price but null SMA/RSI on first fetch. Unclear if transient or systematic.
**Observed:** Day 59 during Canadian market testing
**Action:** Monitor — may need retry logic or cache warm-up for Canadian tickers

### Info: API_CONTRACTS_DAY53.md Outdated
**Severity:** Info (documentation)
**Description:** API contracts doc is behind. Missing: `sma50Declining`, `market_index`, `/api/sectors/rotation`, `/api/data/freshness`, Canadian market params, version v2.23
**Action:** Update at next session that changes APIs

---

## Resolved Issues (Day 60 - This Session)

### Resolved: EPS/Revenue Growth Using QoQ Instead of YoY
**Was:** Medium (incorrect methodology)
**Root Cause:** yfinance_provider.py compared `iloc[0]` vs `iloc[1]` (sequential quarters = QoQ). Also, FMP/yfinance returned growth as decimals (0.15) but categorical assessment expected percentages (15.0).
**Fix:**
1. Changed to `iloc[0]` vs `iloc[4]` (same quarter, year-over-year) for seasonality-adjusted growth
2. Added `_growth_to_pct()` transform in field_maps.py to normalize decimal→percentage
3. Added EPS growth calculation with Diluted EPS → Basic EPS → Net Income fallback
**Files:** `backend/providers/yfinance_provider.py`, `backend/providers/field_maps.py`

### Resolved: Simple Checklist Missing 5 Minervini Criteria
**Was:** Info (enhancement)
**Fix:** Enhanced from 4 to 9 criteria: added 52-Wk Range, Volume, ADX, Market Regime, 200 SMA Trend. All data already available — no API changes needed.
**Files:** `frontend/src/utils/simplifiedScoring.js`, `frontend/src/App.jsx`

### Resolved: adxValue.toFixed Crash on TXN
**Was:** New (Day 60)
**Bug:** `adxValue.toFixed is not a function` when analyzing TXN ticker
**Root Cause:** `srData.meta.adx` returned as non-number type (string) from API. Passed `!== null` check but `.toFixed()` not available on strings.
**Fix:** Coerce to `Number()` with `isNaN()` validation before calling `.toFixed()`. Same pattern applied to `riskReward`.
**File:** `frontend/src/utils/simplifiedScoring.js`

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY59.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 2 |
| Open - Info | 9 |
| **Total Open** | **12** |
| Resolved (Day 60 session) | 3 |
