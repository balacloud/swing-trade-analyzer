# Known Issues - Day 59 (February 25, 2026)

## Open Issues

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library

### Medium: EPS/Revenue Growth Using QoQ Instead of YoY
**Severity:** Medium (incorrect methodology)
**Description:** `yfinance_provider.py` calculates revenueGrowth QoQ instead of YoY
**Action:** Fix after backtest — methodology decision needed

### Info: epsGrowth Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: forwardPe Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: Negative D/E Edge Case in Scoring
**Severity:** Info (pre-existing from Day 53)

### Info: Simple Checklist Missing 5 Minervini Criteria
**Severity:** Info (enhancement, not bug)
**Description:** Simple Checklist has 4 criteria but lacks 52-week range, volume, ADX, market regime, ATR stops
**Action:** Enhance next session — backtest now validates what criteria matter

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
**Description:** API contracts doc is behind. Missing: `sma50Declining`, `market_index`, `/api/sectors/rotation`, `/api/data/freshness`, Canadian market params, version v2.22
**Action:** Update at next session that changes APIs

---

## Resolved Issues (Day 59 - This Session)

### Resolved: Bottom Line Card Shows Wrong Entry Type
**Was:** Medium
**Bug:** DVN — Bottom Line said "MOMENTUM ENTRY" while Trade Setup said "PULLBACK PREFERRED"
**Root Cause:** Bottom Line used ADX >= 30 for entry type; Trade Setup used R:R viability comparison
**Fix:** New `getEntryTypeLabel()` in BottomLineCard.jsx — calculates R:R for both entry types, prefers whichever has better R:R. Falls back to ADX-based preference only if R:R data unavailable.
**File:** `frontend/src/components/BottomLineCard.jsx`

### Resolved: Cache Staleness Concern — Needs Audit
**Was:** Medium
**Fix:** Audited all cache TTLs (all reasonable). Added `/api/data/freshness` endpoint + UI freshness meter with colored dots (green/yellow/red).
**Files:** `backend/backend.py`, `frontend/src/services/api.js`, `frontend/src/App.jsx`

### Resolved: Canadian Market Scan — 3 Bugs Fixed
**Was:** New (Day 59)
1. `set_index` + `set_markets('canada')` combo → `preset not found` error. Fix: Use `set_index` alone for tsx60.
2. `.TO` suffix triggered preferred stock filter ('O' in 'PMNOL'). Fix: Moved suffix append AFTER filter.
3. Hardcoded `['NYSE', 'NASDAQ', 'AMEX']` exchanges. Fix: `valid_exchanges` variable swaps for Canadian.
**File:** `backend/backend.py`

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY58.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 2 |
| Open - Low | 2 |
| Open - Info | 10 |
| **Total Open** | **14** |
| Resolved (Day 59 session) | 3 |
