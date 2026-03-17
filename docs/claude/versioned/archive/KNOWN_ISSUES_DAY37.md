# KNOWN ISSUES - Day 37

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 37 (January 26, 2026)

---

## RESOLVED (Day 37)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Cache lost on restart | SQLite persistent cache | cache_manager.py |
| Redundant yfinance calls | OHLCV + Fundamentals cached | 5.5x speedup |
| No cache statistics | Added hit rate tracking | /api/cache/status |
| Legacy files cluttering root | Moved to docs/obsolete/ | PROJECT_INSTRUCTIONS.md, dot-claude |

### Day 37 Implementation Details:
- **SQLite Cache**: `backend/data/cache.db` - persists across restarts
- **Market-aware TTL**: OHLCV expires at next 4pm ET market close
- **Fundamentals TTL**: 7 days (quarterly data rarely changes)
- **Cache Stats**: Hit rate tracking, size monitoring

---

## RESOLVED (Day 36)

| Issue | Resolution | Notes |
|-------|------------|-------|
| pegRatio Missing from yfinance | Added local calculation fallback | PE / (earningsGrowth * 100) |
| Pine Script Validation Incomplete | Completed 9/9 screenshots | 7/9 GOOD match rate |

---

## DEFERRED ITEMS (Day 37)

### 1. TradingView Phase 2 (Lightweight Charts)
- **Goal:** Show our S&R levels on a professional chart
- **Solution:** TradingView's free Lightweight Charts library
- **Status:** Planned for next session
- **Effort:** Medium (4-6 hours)
- **No subscription required** - fully open source

### 2. Python Upgrade + Defeat Beta Fix
- **Issue:** Defeat Beta API broken (TProtocolException)
- **Root Cause:** Library v0.0.6 incompatible; v0.0.29 requires Python 3.10+
- **Decision:** Keep yfinance as primary (works fine)
- **Effort:** 1-2 hours if needed

### 3. Cache Warming Script
- **Goal:** Pre-populate cache for watchlist tickers
- **Benefit:** First request for common tickers already cached
- **Effort:** Low (1-2 hours)

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.7 (Forward Testing UI)
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
| Technical calculations | VERIFIED | Industry-standard formulas |
| S&R levels | VALIDATED | 100% detection, 7/9 Pine Script match |
| Fibonacci extensions | VALIDATED | 66.7% ATH usage |
| pegRatio calculation | VALIDATED | Local fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/cache_manager.py` | SQLite cache (NEW Day 37) |
| `backend/data/cache.db` | Cache database |
| `backend/backend.py` | v2.9 with cache integration |
| `backend/support_resistance.py` | S&R implementation (frozen) |
| `frontend/src/App.jsx` | TradingView widget |

## CACHE CONFIGURATION

| Data Type | TTL | Storage |
|-----------|-----|---------|
| OHLCV | Next market close + 30min | SQLite |
| Fundamentals | 7 days | SQLite |
| SPY/VIX | Next market close + 30min | SQLite |

---

## API ENDPOINTS (Cache-Related)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cache/status` | GET | Cache stats, hit rates, entries |
| `/api/cache/clear` | POST | Clear cache (all or specific) |
| `/api/health` | GET | Now includes cache stats |

---

*Previous: KNOWN_ISSUES_DAY36.md*
*Next: KNOWN_ISSUES_DAY38.md*
