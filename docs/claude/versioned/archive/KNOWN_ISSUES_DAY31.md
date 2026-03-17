# KNOWN ISSUES - Day 31

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 31 (January 18, 2026)

---

## RESOLVED (Day 31)

| Issue | Resolution | Notes |
|-------|------------|-------|
| S&R Detection Rate Only 80% | Implemented Agglomerative clustering | Now 100% (20/20 stocks) |
| Strong uptrends no actionable support | Added actionable support check (20%) | Falls through to agglomerative |
| Defeat Beta silent failures | Added yfinance failsafe | Auto-fallback when key fields null |
| No indication of data unavailable | Added dataQuality + warning banner | User sees yellow/red warning |

---

## RESOLVED (Day 30)

*Day 30 was research only - no code changes*

---

## RESOLVED (Day 29)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Risk/Macro React error | Fixed in App.jsx | `spyRegime` object now renders properties correctly |
| No cache refresh control | Added Session Refresh button | Clears backend + frontend state |
| No position size limits | Added Max Position % setting | Default 25%, configurable 10-50% |
| No manual share override | Added manual shares checkbox | Can override calculated shares |

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.4 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

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

### Priority: LOW

#### 5. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection
- **Day 25 Fix:** Added ETF detection and special handling

---

## IMPLEMENTATION PROGRESS

### S&R Improvements (4 weeks)
| Week | Task | Status | Notes |
|------|------|--------|-------|
| 1 | DBSCAN/Agglomerative | COMPLETE | Day 31 - 100% detection |
| 2 | Multi-timeframe confluence | Pending | Next priority |
| 3 | Fibonacci extensions | Pending | ATH stocks |
| 4 | Validation | Pending | TradingView comparison |

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
| Backend cache | Working | Clear/status endpoints functional |
| Position sizing | Working | Max position + manual override |
| Session refresh | Working | Clears both backend and frontend |
| Fundamentals failsafe | NEW | yfinance fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (MTF next) |
| `backend/backend.py` | Fundamentals failsafe added |
| `frontend/src/utils/scoringEngine.js` | Data quality detection |
| `frontend/src/App.jsx` | Warning banner UI |

---

## NEW FEATURE FLAGS (Day 31)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable/disable agglomerative clustering |

To rollback to KMeans:
```python
cfg = SRConfig(use_agglomerative=False)
```

---

*Previous: KNOWN_ISSUES_DAY30.md*
*Next: KNOWN_ISSUES_DAY32.md*
