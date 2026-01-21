# Architecture Planning - Data Provider Strategy

> **Date:** January 21, 2026
> **Day:** 34
> **Status:** VALIDATION COMPLETE - Revised Recommendations
> **Approach:** Think like a systems architect + quant developer

---

## VALIDATION RESULTS (January 21, 2026)

### Summary: Perplexity Claims vs Reality

| Claim | Perplexity Said | We Verified | Verdict |
|-------|-----------------|-------------|---------|
| yfinance broken | "BROKEN in 2025-2026" | **100% success (50/50)** | FALSE |
| TSX support | Unknown | **WORKING (5/5 tickers)** | SUPPORTED |
| Defeat Beta | "Needs upgrade" | TProtocolException, needs Python 3.10+ | TRUE |

### Key Finding: yfinance is WORKING

```
Batch Download Test: 50/50 success (100%) in 2.16s
Individual Downloads: 20/20 success (100%)
TSX Support: All 5 Canadian banks working
Fundamentals: 85-92% field coverage
```

**The rate limit errors were from TwelveData, NOT yfinance.**

### Defeat Beta Status: BLOCKED

- Current: v0.0.6 (BROKEN - TProtocolException)
- Latest: v0.0.29 (requires numpy>=2.2.5)
- numpy 2.2.5 requires Python 3.10+
- Current Python: 3.9.6

**Upgrade NOT POSSIBLE without Python version change.**

See: [VALIDATION_RESULTS_DAY34.md](./VALIDATION_RESULTS_DAY34.md) for full details.

---

## REVISED PLAN (Post-Validation)

### What Changed

1. **yfinance stays as PRIMARY** - No replacement needed
2. **Defeat Beta deferred** - Python upgrade is high effort, uncertain payoff
3. **Alternative APIs become OPTIONAL backup** - Not urgent

### New Priority Order

| Priority | Task | Effort | Value |
|----------|------|--------|-------|
| 1 | Add caching to yfinance | Low | High (reduce calls) |
| 2 | Calculate missing fields locally | Low | Medium (pegRatio, etc.) |
| 3 | Add Finnhub as backup | Medium | Low (for edge cases) |
| 4 | Python 3.10 upgrade | High | Uncertain (for Defeat Beta) |

---

## Critical Analysis: Challenging Perplexity Assumptions

### Assumption 1: "yfinance is BROKEN in 2025-2026"

**What Perplexity claimed:**
- Yahoo actively throttles yfinance
- Even new users hit rate limits on first request
- No reliable workaround

**VERIFIED - CLAIM IS FALSE:**
- [x] Run diagnostic: 50 stock batch with yfinance - **100% success**
- [x] Test individual downloads with delays - **100% success**
- [x] Document actual error messages - **No rate limit errors**
- [x] TSX ticker support - **WORKING**

**Conclusion:** yfinance works perfectly in our environment. The original rate limit error was from TwelveData API, not yfinance.

---

### Assumption 2: "TwelveData is the best OHLCV source"

**What Perplexity claimed:**
- 800 credits/day free tier
- 1 credit per OHLCV call
- Can batch 5 tickers per call

**REVISED ASSESSMENT:**
Since yfinance works 100%, TwelveData is only needed as a backup.

**Status:** DEFERRED - Not urgent
- [ ] Sign up for TwelveData free tier (when/if needed)
- [ ] Test TSX support (when/if needed)

---

### Assumption 3: "Finnhub has all our fundamentals"

**What Perplexity claimed:**
- `/stock/metric` returns all metrics
- Unlimited free tier (60/min)

**REVISED ASSESSMENT:**
yfinance already provides 85-92% of our required fields. Finnhub is optional.

**yfinance Coverage (verified):**
```
Available (11-12/13):
✓ trailingPE, forwardPE, marketCap, returnOnEquity,
✓ returnOnAssets, earningsGrowth, revenueGrowth,
✓ profitMargins, operatingMargins, beta, dividendYield

Sometimes Missing:
- pegRatio (can calculate: PE / earningsGrowth)
- debtToEquity (missing for some banks)
```

**Status:** OPTIONAL BACKUP
- [ ] Sign up for Finnhub (when/if yfinance gaps become problematic)

---

### Defeat Beta: VERIFIED BLOCKED

**Current State (Verified):**
- Defeat Beta v0.0.6 installed
- Error: `TProtocolException: Invalid data` when fetching any ticker
- Latest: v0.0.29 requires numpy>=2.2.5
- numpy 2.2.5 requires Python 3.10+
- Current Python: 3.9.6

**Upgrade Blocking Issues:**
```
defeatbeta-api 0.0.29 dependencies:
- numpy>=2.2.5 ──► BLOCKED (requires Python 3.10+)
- duckdb>=1.4.1 ──► OK (already satisfied)
- pandas>=2.3.3 ──► OK (already satisfied)
```

**Revised Trade-off Analysis:**

| Option | Effort | Risk | Value |
|--------|--------|------|-------|
| Keep yfinance (working) | 0 hours | LOW | HIGH |
| Upgrade Python + Defeat Beta | 4-6 hours | HIGH | UNCERTAIN |
| Add Finnhub backup | 2-3 hours | LOW | MEDIUM |

**Decision:** DEFER Defeat Beta upgrade
- yfinance works 100%
- Python upgrade is high-risk (may break other dependencies)
- Defeat Beta value is uncertain (may have same data as yfinance)

---

## Architectural Design: Data Provider Abstraction

### Principle: Don't Replace - Abstract

Instead of "replacing yfinance with TwelveData", design an abstraction layer that:
1. Uses yfinance as PRIMARY (it's already working, mostly)
2. Falls back to alternatives when yfinance fails
3. Allows swapping providers without code changes
4. Caches aggressively to minimize API calls

### Proposed Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DataProviderManager                       │
│  - Orchestrates calls across multiple providers              │
│  - Handles fallback logic                                    │
│  - Manages rate limiting                                     │
│  - Caches results                                            │
└─────────────────────────────────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  YFinanceProvider│  │TwelveDataProvider│ │ FinnhubProvider │
│  (Primary OHLCV) │  │ (Fallback OHLCV)│  │ (Fundamentals)  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   CacheLayer    │
                    │ (Parquet/SQLite)│
                    └─────────────────┘
```

### Interface Design

```python
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import pandas as pd

class OHLCVProvider(ABC):
    """Abstract base class for OHLCV data providers"""

    @abstractmethod
    def get_ohlcv(self, ticker: str, period: str = "2y") -> Optional[pd.DataFrame]:
        """Fetch OHLCV data for a single ticker"""
        pass

    @abstractmethod
    def get_ohlcv_batch(self, tickers: list, period: str = "2y") -> Dict[str, pd.DataFrame]:
        """Fetch OHLCV data for multiple tickers"""
        pass

    @abstractmethod
    def supports_ticker(self, ticker: str) -> bool:
        """Check if provider supports this ticker (e.g., TSX)"""
        pass

    @property
    @abstractmethod
    def rate_limit(self) -> int:
        """Requests per minute allowed"""
        pass


class FundamentalsProvider(ABC):
    """Abstract base class for fundamental data providers"""

    @abstractmethod
    def get_fundamentals(self, ticker: str) -> Optional[Dict[str, Any]]:
        """Fetch fundamental data for a single ticker"""
        pass

    @abstractmethod
    def get_fundamentals_batch(self, tickers: list) -> Dict[str, Dict[str, Any]]:
        """Fetch fundamental data for multiple tickers"""
        pass

    @property
    @abstractmethod
    def supported_fields(self) -> list:
        """List of fundamental fields this provider returns"""
        pass
```

### Fallback Strategy Design

```python
class DataProviderManager:
    """
    Orchestrates data fetching with intelligent fallback.

    Strategy:
    1. Check cache first (< 24 hours old for OHLCV, < 7 days for fundamentals)
    2. Try primary provider
    3. If primary fails, try fallback providers in order
    4. If all fail, return cached data (even if stale) with warning
    5. If no cache and all fail, raise error
    """

    def __init__(self):
        self.ohlcv_providers = [
            YFinanceProvider(),      # Primary - free, no signup
            TwelveDataProvider(),    # Fallback 1 - 800/day free
            PolygonProvider(),       # Fallback 2 - 5/min free
        ]

        self.fundamentals_providers = [
            FinnhubProvider(),       # Primary - unlimited free
            YFinanceProvider(),      # Fallback - from stock.info
            DefeatBetaProvider(),    # Fallback 2 - if fixed
        ]

        self.cache = CacheLayer()

    def get_ohlcv(self, ticker: str, max_age_hours: int = 24) -> pd.DataFrame:
        """
        Get OHLCV with intelligent caching and fallback.
        """
        # Step 1: Check cache
        cached = self.cache.get_ohlcv(ticker)
        if cached is not None and cached.age_hours < max_age_hours:
            return cached.data

        # Step 2: Try providers in order
        last_error = None
        for provider in self.ohlcv_providers:
            if not provider.supports_ticker(ticker):
                continue

            try:
                data = provider.get_ohlcv(ticker)
                if data is not None and not data.empty:
                    self.cache.save_ohlcv(ticker, data)
                    return data
            except Exception as e:
                last_error = e
                logger.warning(f"{provider.__class__.__name__} failed for {ticker}: {e}")
                continue

        # Step 3: Return stale cache if available
        if cached is not None:
            logger.warning(f"All providers failed for {ticker}, using stale cache ({cached.age_hours}h old)")
            return cached.data

        # Step 4: All failed, no cache
        raise DataUnavailableError(f"Could not fetch OHLCV for {ticker}: {last_error}")
```

---

## TSX 60 Support: Research Required

### Current Knowledge
- yfinance supports TSX tickers with `.TO` suffix (e.g., `RY.TO`)
- TwelveData support for TSX: UNKNOWN
- Finnhub support for TSX fundamentals: UNKNOWN

### Action Items
- [ ] Test yfinance with 5 TSX tickers: RY.TO, TD.TO, BNS.TO, BMO.TO, ENB.TO
- [ ] Test TwelveData with same tickers (if available)
- [ ] Test Finnhub fundamentals with same tickers
- [ ] Document which providers support Canadian stocks

### Contingency Plans

| Scenario | Plan |
|----------|------|
| TwelveData doesn't support TSX | Use yfinance for TSX, TwelveData for US |
| Finnhub doesn't have TSX fundamentals | Use yfinance fundamentals for TSX |
| None support TSX | Consider dropping TSX or finding Canadian-specific API |

---

## Cron Hosting Analysis

### Option 1: Local Machine (Current)
**Pros:**
- No additional cost
- Simple setup
- No cloud dependency

**Cons:**
- Machine must be on at scheduled time
- No redundancy
- Manual recovery if machine sleeps/reboots

**Best For:** Development, testing, small-scale personal use

### Option 2: Cloud VM (AWS EC2 / DigitalOcean)
**Pros:**
- Always on
- Reliable scheduling
- Can be very cheap (~$5/month for t2.micro)

**Cons:**
- Monthly cost
- Setup overhead
- Another system to maintain

**Best For:** Production with 24/7 reliability requirement

### Option 3: Serverless (AWS Lambda / GCP Cloud Functions)
**Pros:**
- Pay only for execution time
- Auto-scaling
- No server maintenance

**Cons:**
- Cold start latency
- 15-minute execution limit (Lambda)
- More complex deployment
- Dependencies must be packaged

**Best For:** Event-driven, short-duration tasks

### Option 4: GitHub Actions (Free tier)
**Pros:**
- Free for public repos (2000 min/month for private)
- Easy YAML-based scheduling
- Built-in secrets management
- No infrastructure to manage

**Cons:**
- Not designed for data processing
- Limited compute resources
- Not ideal for large datasets

**Best For:** Small scheduled tasks, CI/CD integration

### Recommendation for Our Use Case

**Phase 1 (Now):** Local machine with manual trigger option
- Develop and test the system
- Run manually or via cron on dev machine
- No infrastructure cost

**Phase 2 (Later):** GitHub Actions or cheap cloud VM
- Once system is stable
- ~$5-10/month for reliability
- Or free with GitHub Actions if within limits

**Action Items:**
- [ ] Design system to work with manual trigger first
- [ ] Add command-line interface for easy manual runs
- [ ] Defer cron automation until system is validated

---

## Phased Implementation Plan

### Phase 0: Validation (Before any code changes)

**Goal:** Verify assumptions from Perplexity research

| Task | Duration | Output |
|------|----------|--------|
| Test yfinance reliability | 2 hours | Success rate data |
| Test TwelveData API | 2 hours | TSX support confirmed |
| Test Finnhub fundamentals | 2 hours | Field mapping document |
| Test Defeat Beta upgrade | 2 hours | Upgrade feasibility |
| Analyze current failure patterns | 1 hour | Root cause document |

**Exit Criteria:** We know EXACTLY which providers work for our use case

### Phase 1: Abstraction Layer (No new APIs yet)

**Goal:** Create provider abstraction using ONLY yfinance

| Task | Duration | Output |
|------|----------|--------|
| Create OHLCVProvider interface | 2 hours | Abstract base class |
| Create FundamentalsProvider interface | 2 hours | Abstract base class |
| Implement YFinanceOHLCVProvider | 4 hours | Concrete implementation |
| Implement YFinanceFundamentalsProvider | 4 hours | Concrete implementation |
| Create CacheLayer (Parquet/SQLite) | 4 hours | Storage abstraction |
| Create DataProviderManager | 4 hours | Orchestration layer |
| Refactor backend.py to use new abstraction | 8 hours | Integrated system |

**Exit Criteria:** System works exactly as before, but with abstraction layer

### Phase 2: Add Fallback Providers

**Goal:** Add alternative providers behind the abstraction

| Task | Duration | Output |
|------|----------|--------|
| Implement TwelveDataOHLCVProvider | 4 hours | Working provider |
| Implement FinnhubFundamentalsProvider | 4 hours | Working provider |
| Implement fallback logic in Manager | 4 hours | Auto-failover |
| Test fallback scenarios | 4 hours | Reliability confirmed |

**Exit Criteria:** System gracefully falls back when yfinance fails

### Phase 3: Fix Defeat Beta (Optional)

**Goal:** Upgrade Python and restore Defeat Beta

| Task | Duration | Output |
|------|----------|--------|
| Create Python 3.10 venv | 1 hour | New environment |
| Test all dependencies on 3.10 | 2 hours | Compatibility confirmed |
| Upgrade Defeat Beta to v0.0.29 | 1 hour | Working library |
| Implement DefeatBetaFundamentalsProvider | 4 hours | Provider class |
| Compare data quality vs Finnhub | 2 hours | Quality assessment |

**Exit Criteria:** Defeat Beta working as additional fundamentals source

### Phase 4: Nightly Batch System

**Goal:** Automated nightly data refresh

| Task | Duration | Output |
|------|----------|--------|
| Create batch download script | 4 hours | nightly_download.py |
| Add progress logging and alerting | 2 hours | Monitoring |
| Test full 563-stock run | 4 hours | Performance baseline |
| Add manual trigger option | 2 hours | CLI interface |
| Document operations procedures | 2 hours | Runbook |

**Exit Criteria:** Can refresh all data nightly with <15 min runtime

---

## Decision Matrix: UPDATED After Validation

| Decision | Options | Recommendation | Rationale |
|----------|---------|----------------|-----------|
| Primary OHLCV | yfinance vs TwelveData | **yfinance (KEEP)** | 100% success rate verified |
| Primary Fundamentals | yfinance vs Finnhub | **yfinance (KEEP)** | 85-92% coverage, sufficient |
| TSX Strategy | Include vs Exclude | **INCLUDE (WORKING)** | TSX fully supported |
| Cron Hosting | Local vs Cloud | **Local first** | Simple, no cost |
| Defeat Beta | Fix vs Defer | **DEFER** | Python upgrade too risky |
| Migration | Big Bang vs Incremental | **None needed** | Current system works |

---

## Next Steps (Updated After Validation)

### Immediate (This Session)
- [x] Run yfinance validation tests - **DONE (100% success)**
- [x] Test TSX support - **DONE (WORKING)**
- [x] Check Defeat Beta upgrade - **DONE (BLOCKED)**
- [x] Document findings - **DONE (VALIDATION_RESULTS_DAY34.md)**

### Short-Term (Optional Improvements)
1. **Add caching layer** to yfinance calls
   - TTL-based cache (24h for OHLCV, 7d for fundamentals)
   - Reduces redundant API calls
   - Effort: Low

2. **Calculate missing fields locally**
   - pegRatio = PE / earningsGrowth
   - Effort: Trivial

### Medium-Term (If Issues Arise)
3. **Add Finnhub as backup** (only if yfinance starts failing)
4. **Python 3.10 upgrade** (only if Defeat Beta is truly needed)

---

## Open Questions (Updated)

Most questions are now answered by validation:

| Question | Status | Answer |
|----------|--------|--------|
| yfinance reliability? | ANSWERED | 100% working |
| TSX support? | ANSWERED | Fully supported |
| Defeat Beta upgrade? | ANSWERED | Blocked on Python 3.9 |
| Need alternative APIs? | ANSWERED | Not urgent |

### Remaining Questions

1. **Cron Timing:** What time should nightly download run? (After market close = 4pm ET?)

2. **Failure Tolerance:** If a stock's data is unavailable:
   - Skip silently? Show with warning? Block screener?

3. **Cache Duration Preferences:**
   - OHLCV: 24 hours (recommended)
   - Fundamentals: 7 days (recommended)

---

## Summary

**Validation completed January 21, 2026.**

The Perplexity research suggested a major architectural overhaul. Our empirical testing shows this is **NOT NECESSARY**:

- yfinance works 100%
- TSX stocks are supported
- Fundamentals coverage is adequate
- Defeat Beta upgrade is blocked

**Recommendation:** Keep current architecture with minor improvements (caching, missing field calculations). Defer major changes until there's an actual problem to solve.

---

*This document has been updated with validation results. See VALIDATION_RESULTS_DAY34.md for detailed test data.*
