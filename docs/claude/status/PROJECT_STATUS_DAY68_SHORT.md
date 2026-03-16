# Project Status — Day 68 (March 16, 2026)

## Session Summary
Day 67 (March 15-16) — Data Sources transparency audit & fixes. No new features.
Full provider chain audit, 3 UI correctness bugs fixed, provenance section overhauled.

---

## What Was Accomplished

### 1. Full Multi-Provider Data Intelligence Audit
- Traced complete chain: Finnhub → AlphaVantage → yfinance (confirmed working)
- Confirmed FMP is permanently dead (v3 deprecated Aug 2025) — AlphaVantage replaces it
- Confirmed MDA "Fundamentals Unavailable" is legitimate: Finnhub has 0 fields, AV has no quarterly data, yfinance has only forwardPe+marketCap. All 4 scoring-critical fields (roe, epsGrowth, revenueGrowth, debtToEquity) genuinely unavailable.
- Verified AAPL chain: Finnhub (10 fields) + AlphaVantage (revenueGrowth) + yfinance (epsGrowth, pegRatio) — field-level merge working perfectly

### 2. FMP Text References — 8 Locations Updated
All user-facing and inline references to "Finnhub, FMP, yfinance" updated to "Finnhub, AlphaVantage, yfinance":
- `App.jsx` error banner (line 1132)
- `scoringEngine.js` error string + rich source detection + comment
- `api.js` function comment
- `backend.py` x2 (endpoint comment + legacy removal comment)
- `orchestrator.py` docstring (FMP → AlphaVantage in strategy)

### 3. Data Sources Screen — 3 UI Correctness Fixes
**Fix A: "Analyze a stock first" never going away**
- Root cause: `analysisResult?.stock?.ticker` path doesn't exist. `analysisResult` from `calculateScore()` returns `{ ticker, name, ... }` at top level — no nested `stock` object.
- Fixed: `analysisResult?.stock?.ticker` → `analysisResult?.ticker` in BOTH the `useEffect` AND the tab click handler.

**Fix B: TwelveData not showing ACTIVE in Market Data row**
- Added `providerActiveKey` per-provider override. TwelveData: `providerActiveKey: 'ohlcv'`, yfinance: `providerActiveKey: 'quote'`. Each resolves independently.
- Both now show ACTIVE simultaneously (TwelveData for SPY OHLCV, yfinance for VIX).

**Fix C: "circuit open — skipped" on ACTIVE providers**
- Added `!isActive` guard: `{health === 'open' && !isActive && (...)}`. A provider can't logically be both ACTIVE and skipped.

### 4. Provenance Section — 4 Bugs Fixed
**Bug A: OHLCV source hardcoded 'yfinance'**
- Backend provenance endpoint always said `'source': 'yfinance'` regardless of actual provider.
- Fixed: `ohlcv_cache.get('source', 'unknown')` — reads real source from cache metadata.

**Bug B: Negative age_hours (-0.9h)**
- Root cause: `expires_at` stored as timezone-aware ISO string; `cached_at` as naive. `.replace(tzinfo=ET)` reinterprets naive local time as ET → wrong offset.
- Fixed: `_naive()` helper strips tzinfo from both `expires_at` and `cached_at`; `datetime.now()` (naive local) used for comparison. All 3 datetimes consistently naive.

**Bug C: "0" rendering as bare text in Fundamentals card**
- React `{age_days && <div>...</div>}` when `age_days=0` → `{0}` → renders "0".
- Fixed: `age_days != null && age_days > 0` guard. Same pattern applied to all 4 conditional renders in provenance section.

**Bug D: Fundamentals source hardcoded 'yfinance' (secondary)**
- Same as Bug A but for fundamentals. Fixed in same edit.

### 5. JUST FETCHED vs CACHED Status Label
Added 3-state `_cache_status()` function in backend.py:
- `just_fetched` — in cache, < 5 min old (live API call was just made this session)
- `cached` — in cache, ≥ 5 min old (served from existing cache, no API call)
- `live` — not in cache (would trigger a fresh API call)

Frontend badge:
- `JUST FETCHED` = cyan — "TwelveData was just called live for this ticker"
- `CACHED` = green — "data was already here before you analyzed"
- `LIVE` = gray — not cached yet

---

## Files Modified

| File | Change |
|------|--------|
| `frontend/src/App.jsx` | v4.30: provenance path fix, providerActiveKey, circuit-open guard, FMP text, null guards, JUST FETCHED badge |
| `frontend/src/utils/scoringEngine.js` | FMP→AlphaVantage text + `alphavantage` source detection |
| `frontend/src/services/api.js` | Comment fix |
| `backend/backend.py` | Comments + `_cache_status()` + OHLCV source fix |
| `backend/providers/orchestrator.py` | Docstring fix |
| `backend/cache_manager.py` | `_naive()` helper for timezone-safe comparison |

---

## Version Summary

| Component | Previous | Now |
|-----------|----------|-----|
| Frontend | v4.16 | v4.30 |
| Backend | v2.31 | v2.32 |
| Backtest | v4.17 | v4.17 (unchanged) |
| API Service | v2.9 | v2.9 (unchanged) |
| **Overall** | **v4.28** | **v4.30** |

---

## Next Session Priorities (Day 68)

1. **Paper trading** — Feature freeze in effect. Analyze 5-10 real tickers using the now-clean data pipeline.
2. **Log Forward Test trades** — If BUY signal found, log in Forward Test tab.
3. **Field bugs only** — No new features until meaningful paper trades are logged.
