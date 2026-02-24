# Known Issues - Day 58 (February 22, 2026)

## Open Issues

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library

### Medium: Cache Staleness Concern — Needs Audit
**Severity:** Medium (potential data quality issue)
**Description:** Multiple caching layers (SQLite stock cache, market cache, sector rotation cache) may serve stale data without user awareness. No UI indicator shows data freshness.
**Action:** Day 59 — Audit all cache TTLs, add UI freshness meter to show data age per source

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

### Info: API_CONTRACTS_DAY53.md Outdated
**Severity:** Info (documentation)
**Description:** API contracts doc is behind. Missing: `sma50Declining` in SPY endpoint, `market_index` param in scan, `/api/sectors/rotation` endpoint, version v2.21
**Action:** Update at next session that changes APIs

---

## Resolved Issues (Day 58 - This Session)

### Resolved: Sector Badge Not Showing on Analyze Page
**Fix:** Added `fetchSectorRotation()` to `fetchFullAnalysisData()` as 9th parallel call. Previously depended on startup fetch which had race condition.
**Commit:** `dcebdb9a`

### Resolved: Scan Results Empty With No Explanation
**Fix:** Added "No stocks matched criteria" message when candidates array is empty. Added "Backend Error" label with troubleshooting hint for exceptions.
**Commit:** `dcebdb9a`

### Resolved: Sector Rotation Fetched Fresh on Every App Load
**Fix:** Added SQLite `market_cache` with key `SECTOR_ROTATION`, expires at next market close (4 PM ET + 30 min buffer).
**Commit:** `dcebdb9a`

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY57.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 2 |
| Open - Low | 2 |
| Open - Info | 8 |
| **Total Open** | **12** |
| Resolved (Day 58 session) | 3 |
