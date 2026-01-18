# KNOWN ISSUES - Day 32

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 32 (January 18, 2026)

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

## OPEN ISSUES

### Priority: HIGH

#### 1. Fundamentals Transparency (Full)
- **Issue:** User has no visibility when Defeat Beta API is failing
- **Root Cause:** Defeat Beta returning "TProtocolException: Invalid data"
- **Current State:** Fallback to yfinance works, but user doesn't know WHY
- **Solution (Full):**
  - Header icon showing data source status (green/yellow/red)
  - Tooltip explaining the issue
  - Backend `/api/health` endpoint for diagnostics
- **Effort:** 1-2 hours
- **Status:** Ready to implement

#### 2. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.5 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### NEW: TradingView Widget Integration
- **Goal:** Add professional indicators (RSI, MACD) as supplementary view
- **Research:** See `/docs/research/TRADINGVIEW_INTEGRATION.md`
- **Phase 1 (Free):** Collapsible TradingView chart below our S&R chart
- **Phase 2 (Future/Paid):** Full integration with S&R overlay
- **Limitation:** Free widget cannot show our custom S&R levels
- **Effort:** Phase 1 = 3-4 hours
- **Status:** Research complete, ready to implement

#### 2. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is fake data
- **Research Finding:** Weekly sentiment has modest predictive power
- **Decision:** Defer until after S&R improvements complete
- **Options:**
  - Build weekly sentiment (8-10 hrs)
  - Remove entirely and reallocate points
  - Keep placeholder with documentation

#### 3. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Research Finding:** Real breadth filter is HIGH ROI
- **Status:** Will implement as part of scoring refactor

#### 4. Forward P/E Low Value
- **File:** `scoringEngine.js`
- **Issue:** Forward P/E has weak predictive power for 1-2 month returns
- **Research Finding:** Valuation matters over years, not weeks
- **Recommendation:** Remove from fundamentals scoring

#### 5. MTF Confluence Not Displayed in Frontend
- **File:** `App.jsx`
- **Issue:** Weekly S&R levels and confluence data not shown in UI
- **Status:** Pending - Priority for Day 33
- **Solution:** Add weekly levels to chart, highlight confluent levels

### Priority: LOW

#### 6. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection
- **Day 25 Fix:** Added ETF detection and special handling

---

## IMPLEMENTATION PROGRESS

### Immediate Priorities (Day 33+)
| Priority | Task | Effort | Status |
|----------|------|--------|--------|
| 1 | Fundamentals Transparency (Full) | 1-2 hrs | Ready |
| 3 | MTF Confluence Frontend Display | 2 hrs | Ready |
| 3 | Fibonacci Extensions (Week 3) | 3 hrs | Research done |
| 4 | TradingView Widget (Free) | 3-4 hrs | Ready |

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
| MTF Confluence | NEW | 27.1% average confluence |
| Backend cache | Working | Clear/status endpoints functional |
| Position sizing | Working | Max position + manual override |
| Session refresh | Working | Clears both backend and frontend |
| Fundamentals failsafe | Working | yfinance fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (Fibonacci next) |
| `backend/backend.py` | Fundamentals failsafe + health endpoint |
| `frontend/src/utils/scoringEngine.js` | Data quality detection |
| `frontend/src/App.jsx` | MTF display + TradingView widget |
| `frontend/src/components/TradingViewWidget.jsx` | NEW: TradingView integration |

## RESEARCH DOCUMENTS

| Document | Purpose |
|----------|---------|
| `/docs/research/DAY32_RESEARCH.md` | Fundamentals + TradingView analysis |
| `/docs/research/TRADINGVIEW_INTEGRATION.md` | Full TradingView roadmap |
| `/docs/research/SR_IMPROVEMENT_RESEARCH.md` | S&R improvement plan |

---

## FEATURE FLAGS (Day 32)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable/disable agglomerative clustering |
| `use_mtf` | SRConfig | `True` | Enable/disable multi-timeframe confluence |

To rollback:
```python
cfg = SRConfig(use_agglomerative=False, use_mtf=False)
```

---

*Previous: KNOWN_ISSUES_DAY31.md*
*Next: KNOWN_ISSUES_DAY33.md*
