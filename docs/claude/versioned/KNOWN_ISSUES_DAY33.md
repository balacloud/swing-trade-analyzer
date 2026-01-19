# KNOWN ISSUES - Day 33

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 33 (January 19, 2026)

---

## RESOLVED (Day 33)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Fundamentals Transparency (Full) | Implemented header banner + health endpoint | Shows data source status prominently |
| MTF Confluence Frontend Display | Added to Trade Setup card | Badge + starred confluent levels + weekly levels dropdown |

### Day 33 Implementation Details:
- **Header Status Bar:** Shows "Defeat Beta ⚠️" with tooltip when API is failing
- **Analysis Banner:** Yellow banner appears below verdict card when using fallback data
- **Health Endpoint:** `/api/health?check_defeatbeta=true` returns live API status
- **Data Quality Fields:** `dataQuality`, `fallbackUsed`, `dataSource` in fundamentals response

---

## RESOLVED (Day 32)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No multi-timeframe confluence | Implemented MTF with weekly data | 27.1% avg confluence |
| Duplicated MTF code | Extracted `_enrich_with_mtf()` helper | 4 return paths unified |

---

## RESOLVED (Day 31)

| Issue | Resolution | Notes |
|-------|------------|-------|
| S&R Detection Rate Only 80% | Implemented Agglomerative clustering | Now 100% (20/20 stocks) |
| Strong uptrends no actionable support | Added actionable support check (20%) | Falls through to agglomerative |
| Defeat Beta silent failures | Added yfinance failsafe | Auto-fallback when key fields null |
| No indication of data unavailable | Added dataQuality + warning banner | User sees yellow/red warning |

---

## DEFERRED ITEMS (Day 33)

### 1. Python Upgrade + Defeat Beta Fix
- **Issue:** Defeat Beta API broken (TProtocolException)
- **Root Cause:** Library v0.0.6 incompatible with current API; v0.0.29 requires Python 3.10+
- **Current Python:** 3.9.6
- **Decision:** Keep yfinance as primary (works fine for our 5 parameters)
- **Future Action:** When upgrading other dependencies, upgrade Python to 3.10+ and defeatbeta-api
- **Effort:** 1-2 hours (recreate venv, test dependencies)

### 2. Finnhub as Alternative Data Source
- **Research:** See `/docs/research/FINNHUB_INTEGRATION_GUIDE.md`
- **Cost:** Free (60 API calls/min)
- **Advantage:** More stable API than yfinance, better documentation
- **Trigger:** Implement if yfinance starts failing or we need higher quality data
- **Effort:** 2-3 hours

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.5 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### ~~1. MTF Confluence Not Displayed in Frontend~~ (RESOLVED Day 33)
- ~~**File:** `App.jsx`~~
- ~~**Issue:** Weekly S&R levels and confluence data not shown in UI~~
- **Status:** RESOLVED - Implemented in Day 33
- **Implementation:** Badge with confluence %, starred confluent levels, collapsible weekly levels

#### 2. TradingView Widget Integration
- **Goal:** Add professional indicators (RSI, MACD) as supplementary view
- **Research:** See `/docs/research/TRADINGVIEW_INTEGRATION.md`
- **Phase 1 (Free):** Collapsible TradingView chart below our S&R chart
- **Phase 2 (Future/Paid):** Full integration with S&R overlay
- **Limitation:** Free widget cannot show our custom S&R levels
- **Effort:** Phase 1 = 3-4 hours
- **Status:** Research complete, ready to implement

#### 3. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is fake data
- **Research Finding:** Weekly sentiment has modest predictive power
- **Decision:** Defer until after S&R improvements complete
- **Options:**
  - Build weekly sentiment (8-10 hrs)
  - Remove entirely and reallocate points
  - Keep placeholder with documentation

#### 4. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Research Finding:** Real breadth filter is HIGH ROI
- **Status:** Will implement as part of scoring refactor

#### 5. Forward P/E Low Value
- **File:** `scoringEngine.js`
- **Issue:** Forward P/E has weak predictive power for 1-2 month returns
- **Research Finding:** Valuation matters over years, not weeks
- **Recommendation:** Remove from fundamentals scoring

### Priority: LOW

#### 6. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection
- **Day 25 Fix:** Added ETF detection and special handling

---

## IMPLEMENTATION PROGRESS

### Immediate Priorities (Day 34+)
| Priority | Task | Effort | Status |
|----------|------|--------|--------|
| 1 | MTF Confluence Frontend Display | 2 hrs | Ready |
| 2 | Fibonacci Extensions (Week 3) | 3 hrs | Research done |
| 3 | TradingView Widget (Free) | 3-4 hrs | Ready |

### S&R Improvements (4 weeks)
| Week | Task | Status | Notes |
|------|------|--------|-------|
| 1 | DBSCAN/Agglomerative | COMPLETE | Day 31 - 100% detection |
| 2 | Multi-timeframe confluence | COMPLETE | Day 32 - 27.1% avg confluence |
| 3 | Fibonacci extensions | Pending | ATH stocks |
| 4 | Validation | Pending | TradingView comparison |

### TradingView Integration Roadmap
| Phase | Task | Status | Notes |
|-------|------|--------|-------|
| 1 | Free widget (RSI, MACD) | Ready | Collapsible UI |
| 2 | Settings integration | Pending | User preferences |
| 3 | Paid library (future) | Planned | S&R overlay capability |

See: `/docs/research/TRADINGVIEW_INTEGRATION.md`

### Scoring Refactor (After S&R)
| Task | Status |
|------|--------|
| Real breadth filter | Pending |
| Weight rebalancing | Pending |
| Position sizing integration | Pending |
| Sentiment decision | Deferred |

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | Verified | 50% win rate is acceptable |
| S&R levels | IMPROVED | 100% detection (was 80%) |
| MTF Confluence | Working | 27.1% average confluence |
| Backend cache | Working | Clear/status endpoints functional |
| Position sizing | Working | Max position + manual override |
| Session refresh | Working | Clears both backend and frontend |
| Fundamentals failsafe | Working | yfinance fallback working |
| Fundamentals transparency | NEW | Header + banner shows data source |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (Fibonacci next) |
| `backend/backend.py` | Health endpoint + fundamentals failsafe |
| `frontend/src/utils/scoringEngine.js` | Data quality detection |
| `frontend/src/App.jsx` | MTF display + data source banner |
| `frontend/src/services/api.js` | Health check with Defeat Beta status |

## RESEARCH DOCUMENTS

| Document | Purpose |
|----------|---------|
| `/docs/research/DAY32_RESEARCH.md` | Fundamentals + TradingView analysis |
| `/docs/research/TRADINGVIEW_INTEGRATION.md` | Full TradingView roadmap |
| `/docs/research/SR_IMPROVEMENT_RESEARCH.md` | S&R improvement plan |
| `/docs/research/FINNHUB_INTEGRATION_GUIDE.md` | Alternative fundamentals source (Day 33) |

---

## FEATURE FLAGS (Day 33)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable/disable agglomerative clustering |
| `use_mtf` | SRConfig | `True` | Enable/disable multi-timeframe confluence |

To rollback:
```python
cfg = SRConfig(use_agglomerative=False, use_mtf=False)
```

---

*Previous: KNOWN_ISSUES_DAY32.md*
*Next: KNOWN_ISSUES_DAY34.md*
