# KNOWN ISSUES - Day 34

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 34 (January 20, 2026)

---

## RESOLVED (Day 34)

| Issue | Resolution | Notes |
|-------|------------|-------|
| MTF Confluence Too Low (28.2%) | Tuned threshold to 1.5% | Now 51.8% (PASS) |
| Fibonacci Extensions Missing | Implemented for ATH stocks | 66.7% usage (correct) |
| No TradingView Comparison Tool | Created `tradingview_comparison.py` | Manual spot-check enabled |
| No Validation Framework | Created `validation_week4.py` | 30-stock systematic test |

### Day 34 Implementation Details:
- **MTF Threshold:** Increased from 0.5% to 1.5% - weekly bars are smoother
- **Fibonacci Logic:** Only activates when no historical resistance exists
- **Validation:** 100% detection, 51.8% MTF confluence, 93.3% trade viability

---

## RESOLVED (Day 33)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Fundamentals Transparency (Full) | Implemented header banner + health endpoint | Shows data source status prominently |
| MTF Confluence Frontend Display | Added to Trade Setup card | Badge + starred confluent levels + weekly levels dropdown |

---

## RESOLVED (Day 32)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No multi-timeframe confluence | Implemented MTF with weekly data | 51.8% avg confluence (tuned Day 34) |
| Duplicated MTF code | Extracted `_enrich_with_mtf()` helper | 4 return paths unified |

---

## RESOLVED (Day 31)

| Issue | Resolution | Notes |
|-------|------------|-------|
| S&R Detection Rate Only 80% | Implemented Agglomerative clustering | Now 100% (30/30 stocks) |
| Strong uptrends no actionable support | Added actionable support check (20%) | Falls through to agglomerative |
| Defeat Beta silent failures | Added yfinance failsafe | Auto-fallback when key fields null |
| No indication of data unavailable | Added dataQuality + warning banner | User sees yellow/red warning |

---

## DEFERRED ITEMS (Day 34)

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
- **Status:** Planned for v3.6 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### 2. TradingView Widget Integration
- **Goal:** Add professional indicators (RSI, MACD) as supplementary view
- **Research:** See `/docs/research/TRADINGVIEW_INTEGRATION.md`
- **Phase 1 (Free):** Collapsible TradingView chart below our S&R chart
- **Phase 2 (Future/Paid):** Full integration with S&R overlay
- **Limitation:** Free widget cannot show our custom S&R levels
- **Effort:** Phase 1 = 3-4 hours
- **Status:** Research complete, ready to implement

#### 3. Confluent Levels Not Visually Distinct
- **File:** `App.jsx`
- **Issue:** MTF-confluent levels only show star, not different styling
- **Desired:** Thicker lines, different color for strong confluence levels
- **Status:** Planned for Day 35

#### 4. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is fake data
- **Research Finding:** Weekly sentiment has modest predictive power
- **Decision:** Defer until after Forward Testing UI
- **Options:**
  - Build weekly sentiment (8-10 hrs)
  - Remove entirely and reallocate points
  - Keep placeholder with documentation

#### 5. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Research Finding:** Real breadth filter is HIGH ROI
- **Status:** Will implement as part of scoring refactor

#### 6. Forward P/E Low Value
- **File:** `scoringEngine.js`
- **Issue:** Forward P/E has weak predictive power for 1-2 month returns
- **Research Finding:** Valuation matters over years, not weeks
- **Recommendation:** Remove from fundamentals scoring

### Priority: LOW

#### 7. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection
- **Day 25 Fix:** Added ETF detection and special handling

---

## IMPLEMENTATION COMPLETE

### S&R Research Project (Weeks 1-4) - DONE

| Week | Task | Status | Notes |
|------|------|--------|-------|
| 1 | DBSCAN/Agglomerative | COMPLETE | Day 31 - 100% detection |
| 2 | Multi-timeframe confluence | COMPLETE | Day 32-34 - 51.8% confluence |
| 3 | Fibonacci extensions | COMPLETE | Day 34 - ATH stocks |
| 4 | Validation | COMPLETE | Day 34 - All criteria passed |

### Next Project: TradingView Widget + Forward Testing UI

| Phase | Task | Status | Notes |
|-------|------|--------|-------|
| 1 | Free widget (RSI, MACD) | Ready | Collapsible UI |
| 2 | Settings integration | Pending | User preferences |
| 3 | Trade journal | Planned | R-multiple tracking |

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | Verified | 50% win rate is acceptable |
| S&R levels | VALIDATED | 100% detection, 51.8% MTF confluence |
| Fibonacci extensions | VALIDATED | 66.7% ATH usage (correct) |
| Backend cache | Working | Clear/status endpoints functional |
| Position sizing | Working | Max position + manual override |
| Session refresh | Working | Clears both backend and frontend |
| Fundamentals failsafe | Working | yfinance fallback working |
| Fundamentals transparency | Working | Header + banner shows data source |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (now frozen) |
| `backend/backend.py` | Health endpoint + fundamentals failsafe |
| `frontend/src/utils/scoringEngine.js` | Data quality detection |
| `frontend/src/App.jsx` | MTF display + data source banner |
| `frontend/src/services/api.js` | Health check with Defeat Beta status |

## RESEARCH DOCUMENTS

| Document | Purpose |
|----------|---------|
| `/docs/research/VALIDATION_WEEK4_RESULTS.md` | Week 4 validation results (NEW) |
| `/docs/research/DAY32_RESEARCH.md` | Fundamentals + TradingView analysis |
| `/docs/research/TRADINGVIEW_INTEGRATION.md` | Full TradingView roadmap |
| `/docs/research/SR_IMPROVEMENT_RESEARCH.md` | S&R improvement plan (COMPLETE) |
| `/docs/research/FINNHUB_INTEGRATION_GUIDE.md` | Alternative fundamentals source |

---

## FEATURE FLAGS (Day 34 - Frozen)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable agglomerative clustering |
| `use_mtf` | SRConfig | `True` | Enable multi-timeframe confluence |
| `use_fibonacci` | SRConfig | `True` | Enable Fibonacci for ATH stocks |

To rollback:
```python
cfg = SRConfig(use_agglomerative=False, use_mtf=False, use_fibonacci=False)
```

---

*Previous: KNOWN_ISSUES_DAY33.md*
*Next: KNOWN_ISSUES_DAY35.md*
