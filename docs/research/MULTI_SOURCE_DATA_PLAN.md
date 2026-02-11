# Multi-Source Data Intelligence Plan for STA

> **Created:** Day 51 (February 11, 2026)
> **Priority:** HIGH (eliminates yfinance single-point-of-failure)
> **Status:** RESEARCH COMPLETE - Ready for implementation
> **Reference:** `docs/research/DATA_SOURCE_INTELLIGENCE_OVERVIEW.md` (proven in Codex trading engine)
> **Prior Research:** `docs/research/DATA_STRATEGY_REVIEW_DAY34.md` (Day 34 Perplexity research)

---

## 1. Problem Statement

STA relies **100% on yfinance** for all data (OHLCV, fundamentals, VIX, SPY).

**Why this is dangerous:**
- yfinance is NOT an official API - it's a scraper wrapping Yahoo Finance's website
- Yahoo actively throttles/blocks yfinance requests (confirmed: issues #2422, #2128, #2125)
- Rate limiting has gotten worse in 2025-2026 - users hit 429 errors after ~950 tickers
- IP blocking is common with bulk requests
- Missing tickers, broken endpoints, incomplete fundamentals reported frequently
- **Day 51 evidence:** Backtest script for 25 tickers returned 0 data (all failed)

**Proven solution exists:** The user's Codex trading engine already implements multi-source fallback successfully.

---

## 2. Free Tier Provider Analysis (Researched February 2026)

### Provider Comparison Table

| Provider | Free Tier Limit | Rate Limit | OHLCV | Fundamentals | Reliability | Cost |
|----------|----------------|------------|-------|--------------|-------------|------|
| **TwelveData** | 800 credits/day | 8/min | Excellent | Too expensive (40 credits/call) | HIGH | $0 |
| **Finnhub** | Unlimited/day | 60/min (30/sec) | Good | Excellent (all in 1 call) | HIGH | $0 |
| **FMP** | 250 requests/day | N/A | Good | Good | MEDIUM | $0 |
| **yfinance** | Unlimited (unofficial) | Aggressive throttling | Decent | Inconsistent | LOW | $0 |
| **Stooq** | Low (unknown exact) | Low daily quota | Decent (EOD only) | None | LOW | $0 |
| **Alpha Vantage** | ~~25 requests/day~~ | 5/min | Good | Good | HIGH but **QUOTA TOO LOW** | $0 |
| **EODHD** | 20 requests/day | N/A | Minimal | 10 credits/call = 2/day | NOT VIABLE on free | $0 |

### Key Findings

1. **TwelveData** = Best OHLCV source (800/day, batch 5 tickers = 160 calls for all stocks)
2. **Finnhub** = Best fundamentals source (unlimited, 60/min, all metrics in 1 call)
3. **FMP** = Solid fundamentals backup (250/day)
4. **yfinance** = Demote to fallback (not primary)
5. **Alpha Vantage** = ~~Was recommended Day 34~~ NOW NEARLY USELESS (dropped from 500→100→25/day)
6. **EODHD** = NOT VIABLE on free tier (20 calls, fundamentals cost 10 each)
7. **Stooq** = Last-resort only (no real API, just pandas_datareader scraping)

### What Changed Since Day 34 Research

| Day 34 Assumption | Day 51 Reality |
|-------------------|----------------|
| Alpha Vantage = good fallback | **25/day now - nearly useless** |
| EODHD = backfill source | **20/day, fundamentals = 10 credits each - not viable free** |
| Polygon.io = emergency fallback | **5/min free - still viable but slow** |
| TwelveData = primary OHLCV | **Still valid - 800/day** |
| Finnhub = fundamentals | **Still valid - unlimited/60 per min** |

### Sources
- [TwelveData Pricing](https://twelvedata.com/pricing)
- [Alpha Vantage Limits](https://www.macroption.com/alpha-vantage-api-limits/)
- [Finnhub Rate Limits](https://finnhub.io/docs/api/rate-limit)
- [FMP Pricing](https://site.financialmodelingprep.com/pricing-plans)
- [EODHD Limits](https://eodhd.com/financial-apis/api-limits)
- [yfinance Issues](https://github.com/ranaroussi/yfinance/issues/2422)

---

## 3. Recommended Architecture for STA

### 3.1 Daily OHLCV (Price Data)

```
Priority 1: TwelveData     (800 credits/day, batch 5)
Priority 2: yfinance        (free, unreliable - use with retry + cache)
Priority 3: Stooq           (pandas_datareader, last resort)
```

**Why this order:**
- TwelveData: Official API, reliable, 800/day covers our needs easily
- yfinance: Free and unlimited in theory, but rate-limited in practice
- Stooq: No API key needed, but low quota and EOD only

**Budget per scan (single ticker):**
- TwelveData: 1 credit (stock) + 1 credit (SPY) = 2 credits
- Per day capacity: 800 / 2 = **400 individual scans** (more than enough)
- Batch mode: 5 tickers/call = up to **2,000 tickers/day**

### 3.2 Fundamentals

```
Priority 1: Finnhub         (unlimited, 60/min)
Priority 2: FMP             (250/day)
Priority 3: yfinance        (last resort)
```

**Why this order:**
- Finnhub: `/stock/metric` returns ALL fundamentals in 1 call (ROE, PE, EPS growth, margins, debt)
- FMP: 250/day is enough for fundamentals (refresh weekly = ~50 tickers/day)
- yfinance: Inconsistent but free backup

**Coverage verification (Finnhub `/stock/metric`):**

| STA Requirement | Finnhub Field | Available? |
|-----------------|---------------|-----------|
| trailingPE | `peBasicExclExtraTTM` | ✅ |
| forwardPE | `peFwd` | ✅ |
| pegRatio | `pegRatio` | ✅ |
| marketCap | `marketCapitalization` | ✅ |
| ROE | `roeTTM` | ✅ |
| ROA | `roaTTM` | ✅ |
| epsGrowth | `epsGrowthQuarterlyYoy` | ✅ |
| revenueGrowth | `revenueGrowthQuarterlyYoy` | ✅ |
| debtToEquity | `totalDebt/totalEquity` | ✅ |
| profitMargins | `netProfitMarginTTM` | ✅ |
| operatingMargins | `operatingMarginTTM` | ✅ |
| beta | `beta` | ✅ |

### 3.3 VIX / Market Data

```
Priority 1: yfinance        (single ticker ^VIX, usually works)
Priority 2: Finnhub         (/quote endpoint)
Priority 3: Cache fallback   (serve stale if all fail)
```

### 3.4 SPY Benchmark

```
Priority 1: TwelveData      (batched with stock request)
Priority 2: yfinance         (single ticker, usually works)
Priority 3: Cache fallback
```

---

## 4. Provenance & Transparency (From Codex Reference)

Adopted from the working Codex system:

### 4.1 Backend Response Fields

Every API response includes:
```json
{
  "dataSource": {
    "primary": "twelvedata",
    "benchmark": "twelvedata",
    "fallbackOrder": ["twelvedata", "yfinance", "stooq"],
    "primaryAttempts": [
      {"source": "twelvedata", "success": true, "rows": 504}
    ],
    "benchmarkAttempts": [
      {"source": "twelvedata", "success": true, "rows": 504}
    ]
  },
  "fundamentalsSources": {
    "ROE": "finnhub",
    "PE": "finnhub",
    "epsGrowth": "fmp"
  },
  "dataAge": {
    "priceData": "2026-02-11T16:00:00Z",
    "fundamentals": "2026-02-08T10:00:00Z",
    "isCached": false
  }
}
```

### 4.2 Frontend Indicator

Show data freshness to user:
- Green dot: Fresh data (fetched < 1 hour ago)
- Yellow dot: Cached data (fetched > 1 hour ago but < 24 hours)
- Red dot: Stale data (> 24 hours) with warning

### 4.3 Data Sources Tab Enhancement

Current Data Sources tab already shows provenance. Enhance with:
- Per-field source attribution
- Fallback attempt history
- Cache age indicator

---

## 5. Cache Architecture

### 5.1 Current STA Cache
- SQLite cache (Day 37) - basic key-value with TTL
- Works but no source tracking or fallback logic

### 5.2 Proposed Cache Upgrade

| Data Type | Cache Store | Fresh TTL | Stale Fallback TTL | Refresh Strategy |
|-----------|-------------|-----------|-------------------|-----------------|
| Daily OHLCV | SQLite | 4 hours | 24 hours | On-demand + nightly |
| SPY Benchmark | SQLite | 4 hours | 24 hours | On-demand |
| Fundamentals | SQLite | 7 days | 30 days | Weekly batch |
| VIX | In-memory | 1 hour | 24 hours | On-demand |
| Indicators (RSI, ADX) | Computed | Same as OHLCV | Same as OHLCV | Derived from OHLCV |

### 5.3 Cache-First Strategy

```
Request flow:
1. Check cache → If fresh, return immediately (0 API calls)
2. If stale, try Primary source → If success, update cache + return
3. If Primary fails, try Fallback 1 → If success, update cache + return
4. If Fallback 1 fails, try Fallback 2 → If success, update cache + return
5. If ALL fail, return stale cache with warning
6. If NO cache exists, return error with retry button
```

This ensures the backtest scripts AND the main app share the same data.

---

## 6. Backtest Infrastructure Fix

### Problem
Backtest scripts call yfinance directly - they don't use the backend's cache or fallback logic.

### Solution
Create a shared `DataProvider` class that both the backend AND backtest scripts import:

```python
# backend/data_providers/provider.py

class DataProvider:
    """Unified data provider with fallback + caching for all STA components."""

    def __init__(self, cache_db='data/cache.db'):
        self.cache = SQLiteCache(cache_db)
        self.providers = {
            'ohlcv': [TwelveDataProvider(), YFinanceProvider(), StooqProvider()],
            'fundamentals': [FinnhubProvider(), FMPProvider(), YFinanceProvider()],
            'vix': [YFinanceProvider(), FinnhubProvider()],
        }

    def get_ohlcv(self, ticker, period='2y'):
        """Fetch OHLCV with fallback chain + caching."""
        # 1. Check cache
        cached = self.cache.get(f'ohlcv:{ticker}', max_age_hours=4)
        if cached is not None:
            return cached, {'source': 'cache', 'age': cached.age}

        # 2. Try providers in order
        attempts = []
        for provider in self.providers['ohlcv']:
            try:
                data = provider.fetch(ticker, period)
                if data is not None and len(data) > 50:
                    self.cache.set(f'ohlcv:{ticker}', data)
                    attempts.append({'source': provider.name, 'success': True})
                    return data, {'source': provider.name, 'attempts': attempts}
            except Exception as e:
                attempts.append({'source': provider.name, 'success': False, 'error': str(e)})

        # 3. Stale cache fallback
        stale = self.cache.get(f'ohlcv:{ticker}', max_age_hours=24)
        if stale is not None:
            return stale, {'source': 'stale_cache', 'attempts': attempts, 'warning': 'All sources failed, using stale data'}

        return None, {'source': None, 'attempts': attempts, 'error': 'All sources failed'}
```

### Usage in Backtest
```python
# backend/backtest/backtest_adx_rsi_thresholds.py
from backend.data_providers.provider import DataProvider

provider = DataProvider()
data, meta = provider.get_ohlcv('AAPL', period='5y')
# Uses same cache, same fallback logic as main app
```

---

## 7. API Key Management

### Required Keys (Free Tier)

| Provider | Key Required | Registration URL | ENV Variable |
|----------|-------------|-----------------|-------------|
| TwelveData | Yes | twelvedata.com | `TWELVEDATA_API_KEY` |
| Finnhub | Yes | finnhub.io | `FINNHUB_API_KEY` |
| FMP | Yes | financialmodelingprep.com | `FMP_API_KEY` |
| yfinance | No | N/A | N/A |
| Stooq | No | N/A | N/A |

### Storage
```bash
# .env file (gitignored)
TWELVEDATA_API_KEY=your_key_here
FINNHUB_API_KEY=your_key_here
FMP_API_KEY=your_key_here
```

---

## 8. Implementation Phases

### Phase 1: DataProvider Foundation (3-4 hours)
1. Create `backend/data_providers/` directory
2. Implement base `Provider` class with standard interface
3. Implement `TwelveDataProvider` (OHLCV primary)
4. Implement `FinnhubProvider` (fundamentals primary)
5. Implement `YFinanceProvider` (fallback - wraps existing code)
6. Implement `StooqProvider` (last resort)
7. Implement `FMPProvider` (fundamentals fallback)
8. Create unified `DataProvider` with fallback chain + cache

### Phase 2: Backend Integration (2-3 hours)
1. Refactor `backend.py` to use `DataProvider` instead of direct yfinance calls
2. Add provenance fields to API responses
3. Add `dataAge` and `isCached` fields
4. Preserve existing API contract (frontend doesn't break)
5. Update cache.db schema for source tracking

### Phase 3: Frontend Transparency (1-2 hours)
1. Add data freshness indicator (green/yellow/red dot)
2. Enhance Data Sources tab with per-field attribution
3. Show fallback attempts in detail view

### Phase 4: Backtest Integration (1-2 hours)
1. Update `backtest_adx_rsi_thresholds.py` to use `DataProvider`
2. Update `backtest_technical.py` to use `DataProvider`
3. Verify backtests work with cached + live data

### Phase 5: Testing & Validation (2 hours)
1. Test each provider individually
2. Test fallback chains (simulate failures)
3. Test cache behavior (fresh, stale, expired)
4. Validate API response format unchanged
5. Run existing frontend with new backend

**Total Effort: 9-13 hours (2-3 sessions)**

---

## 9. Files to Create/Modify

### New Files
| File | Purpose |
|------|---------|
| `backend/data_providers/__init__.py` | Package init |
| `backend/data_providers/base.py` | Base provider interface |
| `backend/data_providers/twelvedata_provider.py` | TwelveData OHLCV |
| `backend/data_providers/finnhub_provider.py` | Finnhub fundamentals |
| `backend/data_providers/fmp_provider.py` | FMP fundamentals fallback |
| `backend/data_providers/yfinance_provider.py` | yfinance fallback (wraps existing) |
| `backend/data_providers/stooq_provider.py` | Stooq last resort |
| `backend/data_providers/provider.py` | Unified provider with fallback + cache |
| `.env.example` | API key template |

### Modified Files
| File | Changes |
|------|---------|
| `backend/backend.py` | Replace direct yfinance calls with DataProvider |
| `backend/backtest/backtest_*.py` | Use DataProvider instead of direct yfinance |
| `frontend/src/App.jsx` | Add data freshness indicator |
| `.gitignore` | Add `.env` |

---

## 10. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| TwelveData free tier drops | Low | High | yfinance + Stooq fallback |
| Finnhub rate limit hit | Low | Medium | FMP fallback, cache-first |
| FMP free tier drops | Low | Low | Finnhub primary, yfinance backup |
| All providers down simultaneously | Very Low | High | Stale cache serves last-known-good |
| API key accidentally committed | Medium | Medium | .env + .gitignore + .env.example |
| Field mapping differences | Medium | Medium | Normalize all to common schema |

---

## 11. Capacity Planning (Free Tiers)

### Daily Usage Budget

**Scenario: User analyzes 20 stocks/day (typical usage)**

| Provider | Operation | Credits Used | Daily Budget | % Used |
|----------|-----------|-------------|-------------|--------|
| TwelveData | 20 stocks × 1 + SPY × 1 | 21 credits | 800 | 2.6% |
| Finnhub | 20 stocks × 1 fundamental call | 20 calls | Unlimited | ~0% |
| FMP | 0 (Finnhub handles it) | 0 | 250 | 0% |

**Scenario: Backtest 50 stocks × 5 years**

| Provider | Operation | Credits Used | Daily Budget | % Used |
|----------|-----------|-------------|-------------|--------|
| TwelveData | 50 stocks × 1 (batched 5 = 10 calls) | 10 credits | 800 | 1.3% |
| Cache | Subsequent runs use cache | 0 | N/A | 0% |

**Conclusion:** Free tiers are MORE than sufficient for STA's usage patterns.

---

## 12. Comparison: Codex Engine vs STA Plan

| Aspect | Codex Engine (Reference) | STA Plan |
|--------|--------------------------|----------|
| OHLCV Fallback | TwelveData → AlphaVantage → yfinance → Stooq | TwelveData → yfinance → Stooq (skip AV - 25/day limit) |
| Fundamentals | FMP → Finnhub → EODHD → AlphaVantage | Finnhub → FMP → yfinance (skip EODHD - 20/day limit) |
| VIX | yfinance → CNBC JSON-LD | yfinance → Finnhub → cache |
| Options | Alpaca | NOT IN SCOPE |
| Provenance | Full field-level tracking | Adopt same approach |
| Cache | Memory + SQLite + TTL | Upgrade existing SQLite cache |
| Frontend | Data Sources tab | Enhance existing Data Sources tab |

**Key Differences:**
- Removed Alpha Vantage from primary chain (25/day is too low)
- Removed EODHD from primary chain (20/day, 10 credits per fundamental call)
- Swapped Finnhub and FMP order (Finnhub unlimited > FMP 250/day for fundamentals)
- No options (not in STA scope currently)

---

## 13. Success Criteria

1. **Zero single-point-of-failure:** If yfinance goes down, STA still works
2. **Backtest uses same infrastructure:** No more direct yfinance calls in backtest scripts
3. **User knows data source:** Frontend shows which provider served each data point
4. **Cache-first:** Repeated scans don't waste API credits
5. **Graceful degradation:** Stale data served with warning > complete failure
6. **Free tier sufficient:** All usage within free limits for typical patterns

---

## 14. Prerequisites Before Implementation

1. **Register for API keys:**
   - [ ] TwelveData: https://twelvedata.com/pricing (free tier)
   - [ ] Finnhub: https://finnhub.io (free tier)
   - [ ] FMP: https://financialmodelingprep.com (free tier)

2. **Verify each provider with test calls:**
   - [ ] TwelveData: `GET /time_series?symbol=AAPL&interval=1day&outputsize=5`
   - [ ] Finnhub: `GET /stock/metric?symbol=AAPL&metric=all`
   - [ ] FMP: `GET /api/v3/profile/AAPL`

3. **Create .env file with keys**

---

*This plan is based on:*
*1. Working reference implementation from Codex trading engine (DATA_SOURCE_INTELLIGENCE_OVERVIEW.md)*
*2. Day 34 Perplexity research (DATA_STRATEGY_REVIEW_DAY34.md) - UPDATED with 2026 free tier reality*
*3. Day 51 web research on current provider limits*
*4. Golden Rule #15: Never implement without validation*
