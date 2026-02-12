# Known Issues - Day 52 (February 12, 2026)

## Open Issues

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically
**Status:** Monitoring - may need FMP account verification

### Low: Defeat Beta Still Imported
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta as legacy fallback
**Impact:** None - DataProvider is tried first, defeatbeta only used if DataProvider fails
**Action:** Can be removed in a future cleanup session

---

## Resolved Issues (Day 52 - This Session)

### Resolved: yfinance Single-Point-of-Failure ✅
**Fixed in:** v4.14 (Day 52)
**Description:** STA relied 100% on yfinance, which is an unofficial Yahoo Finance scraper subject to throttling/blocking
**Impact:** Day 51 backtest of 25 tickers returned 0 data due to yfinance being down
**Fix:** Multi-source provider system with 5 providers and automatic fallback chains

### Resolved: Backtest Infrastructure Separate from App ✅
**Fixed in:** v4.14 (Day 52)
**Description:** Backtest scripts used `yf.download()` directly, not sharing app's data infrastructure
**Fix:** Created `backtest_adapter.py` that routes through DataProvider with fallback chains

### Resolved: Frontend Shows "Defeat Beta" Labels ✅
**Fixed in:** v4.14 (Day 52)
**Description:** Frontend UI showed "Defeat Beta" as data source in status bar, Data Source Map, warnings, and inline labels
**Fix:** Updated all 8+ locations in App.jsx, api.js, scoringEngine.js to show multi-source provider names

---

## Resolved Issues (Prior Sessions)

### Resolved: Position Size Banner Conflict ✅
**Fixed in:** v4.4 (Day 50)

### Resolved: Entry Cards Hidden Instead of Grayed ✅
**Fixed in:** v4.4 (Day 50)

### Resolved: VIABLE Badge + AVOID Conflict ✅
**Fixed in:** v4.4 (Day 50)

### Resolved: "$null-null" Support Zone Bug ✅
**Fixed in:** v4.3 (Day 49)

### Resolved: Entry Uses Wrong Support Level ✅
**Fixed in:** v4.3 (Day 49)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 0 |
| Open - Low | 2 |
| **Total Open** | **2** |
| Resolved (Day 52 session) | 3 |
| Resolved (Prior sessions) | 11+ |
