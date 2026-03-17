# KNOWN ISSUES - Day 39

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 39 (January 28, 2026)

---

## RESOLVED (Day 39)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No local RSI calculation | Added calculate_rsi() to backend.py | Independence from TradingView |
| Fixed % stop losses | Implemented structural stops | swing_low - (ATR * 2) |
| No trend strength indicator | Added ADX calculation | With strength classification |
| No 4H momentum confirmation | Added calculate_rsi_4h() | Uses yfinance 1H resampled |

### Day 39 Implementation Details:
- **Structural Stops**: Replaced fixed 7% with swing_low - (2 * ATR)
- **Local RSI**: Wilder's smoothing, no TradingView dependency
- **ADX**: Wilder's method with trend_strength (choppy/weak/strong/very_strong)
- **4H RSI**: yfinance 1H data resampled to 4H (177 bars available)

---

## RESOLVED (Day 38)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No data provenance visibility | Added Data Sources tab | Full transparency UI |
| Cache status not per-ticker | Added get_ticker_cache_info() | Shows age, expiry per ticker |

---

## RESOLVED (Day 37)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Cache lost on restart | SQLite persistent cache | cache_manager.py |
| Redundant yfinance calls | OHLCV + Fundamentals cached | 5.5x speedup |
| No cache statistics | Added hit rate tracking | /api/cache/status |
| Legacy files cluttering root | Moved to docs/obsolete/ | PROJECT_INSTRUCTIONS.md, dot-claude |

---

## PENDING VALIDATION (Day 39)

### Gate G1: Structural Stops Backtest
- **Status:** PENDING - Need to run backtest comparison
- **Test:** `python backtest_technical.py --compare-stops`
- **Success Criteria:** Structural stops reduce avg loss vs 7% fixed

### Gate G2: ADX Value
- **Status:** PENDING - Not yet tested
- **Criteria:** Win rate improves when using ADX gating

### Gate G4: 4H RSI Value
- **Status:** PENDING - Need backtest with 4H entry timing
- **Criteria:** Entry timing improves with 4H RSI confirmation

---

## DEFERRED ITEMS (Day 39)

### 1. Phase 4: Enhanced Entry Options UI (Day 40 Priority)
- **Goal:** Show dual strategies in Trade Setup card
- **Location:** `frontend/src/App.jsx` lines 805-872
- **Content:**
  - Strategy A: Wait for Pullback (conservative)
  - Strategy B: Enter at Support (momentum confirmation)
  - Show ADX trend strength badge
  - Show 4H RSI entry signal
- **Status:** Ready for implementation

### 2. TradingView Phase 2 (Lightweight Charts)
- **Goal:** Show our S&R levels on a professional chart
- **Solution:** TradingView's free Lightweight Charts library
- **Status:** Deferred to Day 41+
- **Effort:** Medium (4-6 hours)

### 3. Forward Testing UI / Trade Journal
- **Goal:** Track actual trades with R-multiple logging
- **Status:** Planned after Enhanced Entry Options
- **Effort:** High

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance over time
- **Status:** Planned for v3.8 (Forward Testing UI)
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### 2. Enhanced Entry Options Not Yet in UI
- **Goal:** Show dual entry strategies with confirmation signals
- **Current:** Single pullback-based entry only
- **Solution:** Phase 4 implementation (Day 40)
- **Effort:** 3-4 hours

#### 3. Sentiment Score Placeholder (10 points)
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 13% of score is placeholder data
- **Decision:** Defer until after Forward Testing UI

#### 4. Market Breadth Placeholder (1 point)
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Status:** Will implement as part of scoring refactor

### Priority: LOW

#### 5. ETFs Have No Fundamentals
- **Affected:** SPY, QQQ, IWM
- **Cause:** ETFs don't have ROE/EPS metrics
- **Status:** Expected behavior - handled with special ETF detection

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| SQLite Cache | WORKING | 5.5x speedup on hits |
| OHLCV Caching | WORKING | Market-aware TTL |
| Fundamentals Caching | WORKING | 7-day TTL |
| Data Sources Tab | WORKING | Full provenance visibility |
| Local RSI | NEW | v2.12 calculate_rsi() |
| Local ADX | NEW | v2.12 calculate_adx() |
| 4H RSI | NEW | v2.12 calculate_rsi_4h() |
| Structural Stops | NEW | Pending backtest validation |
| S&R levels | VALIDATED | 100% detection, 7/9 Pine Script match |
| Fibonacci extensions | VALIDATED | 66.7% ATH usage |
| pegRatio calculation | VALIDATED | Local fallback working |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `backend/backend.py` | v2.12 with RSI/ADX/4H RSI functions |
| `backend/support_resistance.py` | Structural stop implementation |
| `backend/backtest/backtest_technical.py` | Stop comparison functions |
| `backend/cache_manager.py` | SQLite cache + provenance functions |
| `frontend/src/App.jsx` | Enhanced entry options (Phase 4 target) |

---

## API FUNCTIONS (Day 39 Additions)

| Function | Location | Description |
|----------|----------|-------------|
| `calculate_rsi(closes, period)` | backend.py | Local RSI calculation |
| `calculate_adx(high, low, close, period)` | backend.py | ADX with trend strength |
| `calculate_rsi_4h(ticker, period)` | backend.py | 4H RSI from yfinance |

---

*Previous: KNOWN_ISSUES_DAY38.md*
*Next: KNOWN_ISSUES_DAY40.md*
