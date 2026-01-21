# Data Strategy Review - Day 34

> **Date:** January 21, 2026
> **Source:** Perplexity Deep Research Report
> **Status:** PLANNING (No implementation yet)

---

## Executive Summary from Research

**Recommended Stack:**
- **TwelveData** (OHLCV primary) - 800 credits/day free
- **Finnhub** (Fundamentals) - Unlimited free tier (60/min)
- **Polygon.io** (Backup) - 5/min emergency fallback
- **EODHD** - One-time historical backfill

**Cost:** $0/month
**Runtime:** 19 minutes total daily

---

## Key Finding: yfinance is BROKEN in 2025-2026

From research:
> "yfinance is BROKEN in 2025-2026:
> - Yahoo Finance detects yfinance library and throttles it
> - Even new users hit rate limits on first request
> - No reliable workaround (User-Agent rotation is temporary)"

**This explains our current rate limit issues!** We need to migrate away from yfinance as primary.

---

## API Credit Analysis

### TwelveData (800 credits/day free)

| Endpoint | Cost | Recommendation |
|----------|------|----------------|
| `/time_series` (OHLCV) | 1 credit | ✅ USE - Primary for OHLCV |
| `/statistics` | 40 credits | ❌ TOO EXPENSIVE |
| `/income_statement` | 40 credits | ❌ TOO EXPENSIVE |

**Batching:** Can batch 5 tickers per call
- 563 stocks ÷ 5 = 113 calls
- 113 credits/day = **14% of quota**

### Finnhub (Unlimited, 60/min free)

| Endpoint | Cost | Recommendation |
|----------|------|----------------|
| `/stock/metric` | 1 request | ✅ All fundamentals in one call |
| `/stock/financial` | 1 request | ✅ Income + Balance sheet |

**Weekly refresh:** 563 stocks × 1 call = 563 calls (~10 min at 60/min)

### Polygon.io (5/min free)

- Emergency fallback only
- Slower but 99%+ uptime
- Use when TwelveData fails

---

## Data Coverage Verification

### What We Need vs What's Available

| Our Requirement | TwelveData | Finnhub | Covered? |
|-----------------|------------|---------|----------|
| OHLCV 2yr | ✅ 10+ years | ✅ | ✅ |
| Weekly OHLCV (MTF) | ✅ | ✅ | ✅ |
| trailingPE | ❌ (40 credits) | ✅ Free | ✅ |
| forwardPE | ❌ (40 credits) | ✅ Free | ✅ |
| pegRatio | ❌ | ✅ Free | ✅ |
| marketCap | ❌ | ✅ Free | ✅ |
| ROE | ❌ | ✅ Free | ✅ |
| ROA | ❌ | ✅ Free | ✅ |
| epsGrowth | ❌ | ✅ Free | ✅ |
| revenueGrowth | ❌ | ✅ Free | ✅ |
| debtToEquity | ❌ | ✅ Free | ✅ |
| profitMargins | ❌ | ✅ Free | ✅ |
| operatingMargins | ❌ | ✅ Free | ✅ |
| beta | ❌ | ✅ Free | ✅ |
| dividendYield | ❌ | ✅ Free | ✅ |
| SPY OHLCV | ✅ | ✅ | ✅ |
| VIX | ✅ | ✅ | ✅ |

**Result:** All our data requirements are covered by the free tier combo.

---

## Storage Strategy

### Recommended by Research

| Data Type | Format | Size | Update Frequency |
|-----------|--------|------|------------------|
| OHLCV | Parquet | ~250 MB | Daily (nightly) |
| Fundamentals | SQLite | ~50 MB | Weekly |
| Technicals cache | Computed | ~100 MB | On-demand |

**Total:** ~400 MB

### Why Parquet for OHLCV?
- Columnar storage (10-100x faster reads)
- 2-5x compression vs CSV
- Native pandas support
- Perfect for technical calculations

### Why SQLite for Fundamentals?
- Schema-friendly
- Easy queries by ticker
- Single file database
- Built-in Python support

---

## Proposed Daily Workflow

```
11:00 PM (After market close):
├─ Run nightly_download.py
├─ Fetch OHLCV for 563 stocks (TwelveData, 113 batched calls)
├─ Save to Parquet
├─ Calculate SMA, RSI, ATR locally
├─ Runtime: 14 minutes
└─ API quota: 113/800 (14%)

6:30 AM (Pre-market):
├─ Run screener.py
├─ Load OHLCV from Parquet (all 563 in <1 sec)
├─ Apply scoring engine
├─ Filter to candidates (≥50 points)
├─ Calculate S&R levels
├─ Runtime: 5 minutes
└─ API calls: 0 (all from cache)

Thursday 10:00 AM (Weekly):
├─ Run weekly_fundamentals.py
├─ Fetch fundamentals (Finnhub, 563 calls)
├─ Save to SQLite
├─ Runtime: 10 minutes
└─ API cost: $0
```

---

## Questions/Concerns to Verify

### 1. TSX 60 Support
- Does TwelveData support TSX tickers (e.g., RY.TO, TD.TO)?
- Does Finnhub have fundamentals for Canadian stocks?
- **Action:** Test with 5 TSX tickers before full implementation

### 2. Finnhub Metric Coverage
- Does `/stock/metric` return ALL 13 fundamentals we need?
- Research shows "all metrics" but need to verify exact fields
- **Action:** Make test API call to verify response structure

### 3. Parquet File Strategy
- One file per ticker (563 files) vs one big file?
- Research suggests per-ticker files
- **Action:** Benchmark both approaches with 50 stocks

### 4. Weekly OHLCV for MTF
- Currently we fetch weekly OHLCV separately
- Can TwelveData return weekly bars?
- Or do we aggregate daily → weekly locally?
- **Action:** Check TwelveData interval options

### 5. Fallback Trigger Logic
- When exactly to fallback to Polygon?
- HTTP 429 (rate limit)?
- Connection timeout?
- Empty response?
- **Action:** Define clear fallback triggers

### 6. Existing yfinance Code
- How much code needs refactoring?
- Can we abstract data source behind interface?
- **Action:** Audit all yfinance usage in codebase

---

## Impact on Existing Modules

### Files That Need Changes

| File | Current | After Migration | Effort |
|------|---------|-----------------|--------|
| `backend/backend.py` | yfinance calls | DataProvider interface | High |
| `backend/support_resistance.py` | yfinance OHLCV | Load from Parquet | Medium |
| `frontend/src/utils/rsCalculator.js` | Expects API response | No change (API same) | None |
| `frontend/src/utils/scoringEngine.js` | Expects API response | No change (API same) | None |

### New Files Needed

| File | Purpose |
|------|---------|
| `backend/data_providers/twelvedata.py` | TwelveData API wrapper |
| `backend/data_providers/finnhub.py` | Finnhub API wrapper |
| `backend/data_providers/polygon.py` | Polygon fallback wrapper |
| `backend/data_storage/parquet_store.py` | Parquet read/write |
| `backend/data_storage/sqlite_store.py` | SQLite read/write |
| `backend/jobs/nightly_download.py` | Cron job for OHLCV |
| `backend/jobs/weekly_fundamentals.py` | Cron job for fundamentals |

---

## Implementation Phases (From Research)

### Phase 1: Foundation (Week 1)
- [ ] Register for free tier APIs (TwelveData, Finnhub, Polygon, EODHD)
- [ ] Store API keys in environment variables
- [ ] Create directory structure: `./data/{ohlcv,fundamentals}`
- [ ] Install dependencies: pandas, requests, pyarrow, sqlite3

### Phase 2: Data Infrastructure (Week 2)
- [ ] Create ParquetStore class
- [ ] Create SQLiteStore class
- [ ] Download 2-year OHLCV for all 563 stocks (one-time backfill)
- [ ] Create fundamentals SQLite schema
- [ ] Test with 20 stocks first

### Phase 3: Batch Downloader (Week 3)
- [ ] Implement TwelveData wrapper with batching
- [ ] Implement Finnhub wrapper
- [ ] Implement Polygon fallback wrapper
- [ ] Test with 50 stocks
- [ ] Add rate limit enforcement

### Phase 4: Integration (Week 4)
- [ ] Refactor backend.py to use new DataProvider
- [ ] Update S&R module to load from Parquet
- [ ] Verify API responses match current format
- [ ] Test full screener flow

### Phase 5: Automation (Week 5)
- [ ] Create nightly cron job (11pm download)
- [ ] Create weekly cron job (Thursday fundamentals)
- [ ] Set up logging
- [ ] Add alerting for failures

### Phase 6: Testing & Production (Week 6)
- [ ] Full 563-stock test run
- [ ] Monitor API usage for 1 week
- [ ] Verify no rate limit hits
- [ ] Document for maintenance

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| TwelveData free tier discontinued | Low | High | Polygon backup ready |
| Finnhub fundamentals missing fields | Medium | Medium | Verify before migration |
| TSX stocks not supported | Medium | Medium | Test TSX tickers early |
| Parquet performance issues | Low | Low | SQLite fallback option |
| Cron job failures | Medium | Medium | Alerting + manual trigger option |

---

## Decision Points

Before implementation, need user decisions on:

1. **Phased vs Big Bang Migration?**
   - Option A: Run both systems in parallel, validate, then switch
   - Option B: Direct replacement (riskier but faster)

2. **TSX 60 Priority?**
   - If TSX not supported, do we drop it or find alternative?
   - Or focus on S&P 500 only initially?

3. **Cron Job Hosting?**
   - Local machine (always-on)?
   - Cloud function (AWS Lambda, etc.)?
   - Manual trigger for now?

4. **Backfill Strategy?**
   - Use EODHD for one-time historical backfill?
   - Or incremental TwelveData download over several days?

---

## Next Steps (No Implementation Yet)

1. **Validate API Access**
   - Register for all 4 free tier APIs
   - Test single ticker on each API
   - Verify data format matches our needs

2. **Audit Current Codebase**
   - List all yfinance calls
   - Identify abstraction points
   - Estimate refactoring effort

3. **Prototype Storage**
   - Test Parquet with 10 stocks
   - Test SQLite schema with fundamentals
   - Benchmark read performance

4. **User Decisions**
   - Phased vs big bang?
   - TSX priority?
   - Cron hosting?

---

*This is a PLANNING document. No implementation until questions are resolved and user approves approach.*
