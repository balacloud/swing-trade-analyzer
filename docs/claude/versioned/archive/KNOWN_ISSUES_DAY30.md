# KNOWN ISSUES - Day 30

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 30 (January 17, 2026)

---

## RESOLVED (Day 30)

*No code changes today - research session*

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

#### 1. S&R Detection Rate Only 80%
- **Impact:** 20% of stocks (strong uptrends) get no usable entry
- **Root Cause:** KMeans uses fixed 5 clusters, not adaptive
- **Status:** Research complete, implementation plan ready
- **Solution:** Replace KMeans with DBSCAN/Agglomerative
- **Expected Result:** 80% → 87-95% detection rate
- **Files to change:** `backend/support_resistance.py`

#### 2. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.3 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### 3. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is fake data
- **Research Finding:** Weekly sentiment has modest predictive power
- **Decision:** Defer until after S&R improvements
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

#### 6. S&R Returns No Setup for Strong Uptrends
- **Affected Stocks:** GOOGL, GS, XOM, CAT, BA, GE (Day 29 testing)
- **Cause:** No calculated support levels below current price
- **Status:** By design, but Fibonacci extensions can help
- **Solution:** Part of S&R improvement (Week 3)

#### 7. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - not a bug

---

## RESEARCH FINDINGS (Day 30)

### S&R Research Validated

| Improvement | Evidence | Priority |
|-------------|----------|----------|
| DBSCAN over KMeans | 23% better precision (QuantInsti) | Week 1 |
| Multi-timeframe confluence | 3.2x stronger signal | Week 2 |
| Fibonacci for ATH | 72% accuracy | Week 3 |

### Scoring Research Validated

| Finding | Evidence | Implication |
|---------|----------|-------------|
| 50% win rate is normal | Practitioner consensus | System not broken |
| Position sizing = 90% | Van Tharp confirmed | Focus on sizing, not entries |
| Breadth filter = high ROI | Strong predictive power | Make it real |

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | ✅ Verified | 50% win rate is acceptable |
| S&R levels | ⚠️ 80% success | DBSCAN will improve |
| Backend cache | ✅ Working | Clear/status endpoints functional |
| Position sizing | ✅ Working | Max position + manual override |
| Session refresh | ✅ Working | Clears both backend and frontend |

---

## IMPLEMENTATION ROADMAP

### Phase 1: S&R Improvements (Next Priority)
- Week 1: DBSCAN replacement (2 hrs)
- Week 2: Multi-timeframe confluence (6 hrs)
- Week 3: Fibonacci extensions (3 hrs)
- Week 4: Validation (4 hrs)

### Phase 2: Scoring Refactor (After S&R)
- Real breadth filter
- Weight rebalancing
- Position sizing integration
- Sentiment decision

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/support_resistance.py` | S&R implementation (next changes) |
| `frontend/src/utils/scoringEngine.js` | Scoring refactor (later) |
| `frontend/src/utils/simplifiedScoring.js` | Binary system (keep parallel) |

---

*Previous: KNOWN_ISSUES_DAY29.md*
*Next: KNOWN_ISSUES_DAY31.md*
