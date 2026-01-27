# KNOWN ISSUES - Day 38

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 38 (January 27, 2026)

---

## RESOLVED (Day 38)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No data provenance visibility | Added Data Sources tab | Full transparency UI |
| Cache status not per-ticker | Added get_ticker_cache_info() | Shows age, expiry per ticker |

### Day 38 Implementation Details:
- **Data Sources Tab**: New tab showing OHLCV/Fundamentals sources
- **Local Calculations Table**: Shows formulas for SMA, EMA, RSI, ATR, etc.
- **Provenance Endpoint**: `/api/provenance/<ticker>` returns cache metadata

---

## RESOLVED (Day 37)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Cache lost on restart | SQLite persistent cache | cache_manager.py |
| Redundant yfinance calls | OHLCV + Fundamentals cached | 5.5x speedup |
| No cache statistics | Added hit rate tracking | /api/cache/status |
| Legacy files cluttering root | Moved to docs/obsolete/ | PROJECT_INSTRUCTIONS.md, dot-claude |

---

## DEFERRED ITEMS (Day 38)

### 1. TradingView Phase 2 (Lightweight Charts)
- **Goal:** Show our S&R levels on a professional chart
- **Solution:** TradingView's free Lightweight Charts library
- **Status:** Planned for next session
- **Effort:** Medium (4-6 hours)
- **No subscription required** - fully open source

### 2. Forward Testing UI / Trade Journal
- **Goal:** Track actual trades with R-multiple logging
- **Status:** Planned after Lightweight Charts
- **Effort:** High

### 3. Update Validation Module
- **Goal:** Reflect new local calculations in validation
- **Status:** Low priority
- **Effort:** Low (1-2 hours)

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.8 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### 2. TradingView Phase 2 (Lightweight Charts)
- **Goal:** Show our S&R levels visually on chart
- **Current:** Phase 1 iframe only shows RSI/MACD (no custom overlay)
- **Solution:** Lightweight Charts (free, open source)
- **Effort:** 4-6 hours

#### 3. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is placeholder data
- **Decision:** Defer until after Forward Testing UI

#### 4. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Status:** Will implement as part of scoring refactor

### Priority: LOW

#### 5. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| SQLite Cache | WORKING | 5.5x speedup on hits |
| OHLCV Caching | WORKING | Market-aware TTL |
| Fundamentals Caching | WORKING | 7-day TTL |
| Data Sources Tab | NEW | Full provenance visibility |
| Technical calculations | VERIFIED | Industry-standard formulas |
| S&R levels | VALIDATED | 100% detection, 7/9 Pine Script match |
| Fibonacci extensions | VALIDATED | 66.7% ATH usage |
| pegRatio calculation | VALIDATED | Local fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/cache_manager.py` | SQLite cache + provenance functions |
| `backend/backend.py` | v2.10 with /api/provenance endpoint |
| `frontend/src/App.jsx` | Data Sources tab (v3.7) |
| `backend/support_resistance.py` | S&R implementation (frozen) |

---

## API ENDPOINTS (Data Sources Related)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/provenance/<ticker>` | GET | Data provenance for ticker (NEW) |
| `/api/cache/status` | GET | Cache stats, hit rates, entries |
| `/api/cache/clear` | POST | Clear cache (all or specific) |

---

*Previous: KNOWN_ISSUES_DAY37.md*
*Next: KNOWN_ISSUES_DAY39.md*
