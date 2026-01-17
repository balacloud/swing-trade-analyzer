# KNOWN ISSUES - Day 29

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 29 (January 16, 2026)

---

## RESOLVED (Day 29)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Risk/Macro React error | Fixed in App.jsx | `spyRegime` object now renders properties correctly |
| No cache refresh control | Added Session Refresh button | Clears backend + frontend state |
| No position size limits | Added Max Position % setting | Default 25%, configurable 10-50% |
| No manual share override | Added manual shares checkbox | Can override calculated shares |

---

## RESOLVED (Day 28)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No Position Sizing Calculator | Built in Settings tab | Van Tharp R-multiple principles |
| No auto-fill from analysis | Added "Calculate Position Size" button | Carries entry/stop to calculator |

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.3 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

#### 2. S&R Returns No Setup for Strong Uptrends
- **Affected Stocks:** GOOGL, GS, XOM, CAT, BA, GE (Day 29 testing)
- **Cause:** No calculated support levels below current price
- **Impact:** Cannot generate trade setup for these stocks
- **Status:** By design - no support = no valid stop = no trade
- **Workaround:** Wait for pullback to establish support

### Priority: MEDIUM

#### 3. Sentiment Score Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 10 points potentially misallocated (13% of score is fake)
- **Decision:** Keep in legacy system; simplified system ignores this

#### 4. Market Breadth Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Decision:** Keep in legacy system; simplified system ignores this

### Priority: LOW

#### 5. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - not a bug
- **Workaround:** Use technical analysis only for ETFs

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | ✅ Verified Day 29 | AVGO 0/10 short-term confirmed correct |
| S&R levels | ✅ Working | 80% of stocks get trade setup |
| Backend cache | ✅ Working | Clear/status endpoints functional |
| Position sizing | ✅ Working | Max position + manual override working |
| Session refresh | ✅ Working | Clears both backend and frontend |

---

## DAY 29 TEST RESULTS

### Comprehensive Backend Test (30 stocks)

| API | Success Rate | Notes |
|-----|-------------|-------|
| Stock API | 100% (30/30) | All working |
| Fundamentals | 90% (27/30) | 3 ETFs expected missing |
| S&R | 80% (24/30) | 6 stocks in strong uptrends |

### Stocks Without S&R Setup
- GOOGL, GS, XOM, CAT, BA, GE
- Reason: 0 support levels (trading above all pivots)
- This is correct behavior

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `App.jsx` | v3.2 - Session refresh + position controls |
| `positionSizing.js` | Max position + manual shares logic |
| `api.js` | Cache management endpoints |

---

## NEXT PRIORITIES

1. **Forward Testing UI** - Track real trades, build SQN
2. **Pattern Detection** - VCP, cup-and-handle for better R:R
3. **Sentiment Filter** - Earnings/news risk filter

---

*Previous: KNOWN_ISSUES_DAY28.md*
*Next: KNOWN_ISSUES_DAY30.md*
