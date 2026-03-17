# KNOWN ISSUES - Day 36

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 36 (January 25, 2026)

---

## RESOLVED (Day 36)

| Issue | Resolution | Notes |
|-------|------------|-------|
| pegRatio Missing from yfinance | Added local calculation fallback | PE / (earningsGrowth * 100) |
| Pine Script Validation Incomplete | Completed 9/9 screenshots | 7/9 GOOD match rate |
| pine_scripts folder location | Moved to docs/pine_scripts/ | Better organization |

### Day 36 Implementation Details:
- **pegRatio Formula:** `PE / (earningsGrowth * 100)` - yfinance returns growth as decimal
- **Negative Growth Guard:** Changed from `!= 0` to `> 0` (negative PEG not meaningful)
- **Validation:** AAPL=0.36, MSFT=2.61, NVDA=0.70, SOFI=0.44

---

## RESOLVED (Day 35)

| Issue | Resolution | Notes |
|-------|------------|-------|
| yfinance reliability concerns | Validated 100% success rate | Perplexity claims were FALSE |
| TSX support unknown | Verified WORKING (5/5 tickers) | All Canadian banks supported |
| Defeat Beta broken | Documented as BLOCKED | Needs Python 3.10+ |

---

## DEFERRED ITEMS (Day 36)

### 1. Python Upgrade + Defeat Beta Fix
- **Issue:** Defeat Beta API broken (TProtocolException)
- **Root Cause:** Library v0.0.6 incompatible with current API; v0.0.29 requires Python 3.10+
- **Current Python:** 3.9.6
- **Decision:** Keep yfinance as primary (works fine)
- **Effort:** 1-2 hours (recreate venv, test dependencies)

### 2. yfinance Caching Layer
- **Issue:** Redundant API calls during batch operations
- **Solution:** TTL-based cache (24h OHLCV, 7d fundamentals)
- **Status:** Planned for next session
- **Effort:** 2-3 hours

### 3. Finnhub as Alternative Data Source
- **Research:** See `/docs/research/FINNHUB_INTEGRATION_GUIDE.md`
- **Trigger:** Implement if yfinance starts failing
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
- **Limitation:** Free widget cannot show our custom S&R levels
- **Effort:** Phase 1 = 3-4 hours
- **Status:** Research complete, ready to implement

#### 3. Confluent Levels Not Visually Distinct
- **File:** `App.jsx`
- **Issue:** MTF-confluent levels only show star, not different styling
- **Desired:** Thicker lines, different color for strong confluence levels

#### 4. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is placeholder data
- **Decision:** Defer until after Forward Testing UI

#### 5. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Status:** Will implement as part of scoring refactor

### Priority: LOW

#### 6. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | Verified | 50% win rate acceptable |
| S&R levels | VALIDATED | 100% detection, 51.8% MTF confluence |
| Pine Script v2 | VALIDATED | 7/9 GOOD match rate |
| Fibonacci extensions | VALIDATED | 66.7% ATH usage |
| pegRatio calculation | VALIDATED | Local fallback working |
| Backend cache | Working | Clear/status endpoints functional |
| Position sizing | Working | Max position + manual override |
| Session refresh | Working | Clears both backend and frontend |
| Fundamentals failsafe | Working | yfinance fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (frozen) |
| `backend/backend.py` | pegRatio calculation + health endpoint |
| `frontend/src/utils/scoringEngine.js` | Data quality detection |
| `frontend/src/App.jsx` | MTF display + data source banner |
| `docs/pine_scripts/` | Pine Script v2 for TradingView |

## RESEARCH DOCUMENTS

| Document | Purpose |
|----------|---------|
| `/docs/research/VALIDATION_RESULTS_DAY34.md` | yfinance validation results |
| `/docs/research/PINE_SCRIPT_VALIDATION_IN_PROGRESS.md` | Pine Script comparison |
| `/docs/research/TRADINGVIEW_INTEGRATION.md` | TradingView widget roadmap |
| `/docs/research/FINNHUB_INTEGRATION_GUIDE.md` | Alternative fundamentals source |

---

## FEATURE FLAGS (Day 36 - Frozen)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable agglomerative clustering |
| `use_mtf` | SRConfig | `True` | Enable multi-timeframe confluence |
| `use_fibonacci` | SRConfig | `True` | Enable Fibonacci for ATH stocks |

---

*Previous: KNOWN_ISSUES_DAY34.md*
*Next: KNOWN_ISSUES_DAY37.md*
