# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 51 (February 11, 2026)
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v4.10 (Backend v2.16, Frontend v4.3)

---

## COMPLETED (v1.0 - v3.9)

### Core Features
| Version | Feature | Day |
|---------|---------|-----|
| v1.0 | Single stock analysis, 75-point scoring | Day 1-5 |
| v1.1 | TradingView screener integration | Day 11 |
| v1.2 | S&R Engine with trade setups | Day 13 |
| v1.3 | Validation Engine with UI | Day 14 |
| v2.0 | Score breakdown with explanations | Day 23 |
| v2.5 | Trade viability display (Option D) | Day 22 |
| v2.9 | Simplified Binary Scoring (4-criteria) | Day 27 |
| v3.0 | Settings tab + Position Sizing Calculator | Day 28 |
| v3.1 | Auto-fill integration | Day 28 |
| v3.2 | Session refresh, position controls | Day 29 |
| v3.3 | Agglomerative S&R clustering | Day 31 |
| v3.4 | MTF confluence, fundamentals transparency | Day 33 |
| v3.5 | SQLite persistent cache (5.5x speedup) | Day 37 |
| v3.6 | start.sh/stop.sh service scripts | Day 37 |
| v3.7 | Data Sources tab (transparency UI) | Day 38 |
| v3.8 | Dual Entry Strategy UI | Day 39-40 |
| v3.9 | Data source labels, Defeat Beta error handling | Day 42 |
| v4.0 | Pattern Detection (VCP, Cup-Handle, Flat Base) + Categorical Assessment | Day 44 |

### S&R Improvements (Complete)
| Week | Task | Status |
|------|------|--------|
| 1 | Agglomerative Clustering | ✅ Day 31 |
| 2 | Multi-Timeframe Confluence | ✅ Day 32-33 |
| 3 | Fibonacci Extensions | ✅ Day 34 |
| 4 | Validation vs TradingView | ✅ Day 34 |

### Bug Fixes (Historical)
| Issue | Fixed | Day |
|-------|-------|-----|
| Risk/Macro Expand Crash | ✅ | Day 29 |
| TradingView OTC Stocks | ✅ | Day 21 |
| ATR = null | ✅ | Day 20 |
| RSI Always N/A | ✅ | Day 22 |
| Backend Cache Stale | ✅ | Day 25 + Day 37 |
| UX Confusion (Mixed Signals) | ✅ | Day 23 ("Why This Score?") |
| VIX Stale Data | ✅ | Day 42 |
| Validation Low Scores | ✅ | Day 42 (tolerances) |
| Recommendation Card Alert Price | ✅ | Day 46 (Issue #0 - used resistance instead of support) |

---

## IN PROGRESS / PENDING VALIDATION

### Backtest Gates (Day 40-41)
| Gate | Description | Status |
|------|-------------|--------|
| G1 | Structural Stops Backtest | PENDING |
| G2 | ADX Value Validation | PENDING |
| G4 | 4H RSI Entry Timing | PENDING |

**Test Command:** `python backtest_technical.py --compare-stops`

---

## PLANNED

### v4.0: Forward Testing UI
- **Priority:** HIGH (tracked since Day 25 as CRITICAL)
- **Description:** Track actual trades, record R-multiples, build SQN over time
- **Why:** Cannot validate system without tracking real performance
- **Effort:** High

### v4.1: TradingView Lightweight Charts
- **Priority:** MEDIUM
- **Description:** Interactive charts with S&R levels, RSI/MACD overlays
- **Technology:** TradingView Lightweight Charts (free, open source)
- **Effort:** Medium (4-6 hours)

### v4.2: Pattern Detection ✅ COMPLETED (Day 44)
- **Status:** Implemented in v4.0
- **Features:**
  - VCP (Volatility Contraction Pattern) detection
  - Cup & Handle pattern detection
  - Flat Base pattern detection
  - Minervini's 8-point Trend Template
- **Files:** `backend/pattern_detection.py`, `/api/patterns/<ticker>` endpoint

### v4.3: Options Tab
- **Priority:** LOW
- **Description:** Options data display if data sources available
- **Blocker:** Needs Greeks calculation, complex data sourcing
- **Research:** `docs/research/OPTIONS_TAB_FEASIBILITY_ANALYSIS.md`

### v4.4: Sentiment Integration ✅ COMPLETED (Day 44)
- **Status:** Implemented via Fear & Greed Index
- **Solution Used:** CNN Fear & Greed Index (free API, no key required)
- **Endpoint:** `/api/fear-greed` returns value (0-100), rating, assessment
- **Integration:** Part of v4.5 Categorical Assessment System

### v4.5: Categorical Assessment System ✅ COMPLETED (Day 44)
- **Status:** Replaced 75-point numerical scoring
- **Key Finding:** Score-to-return correlation = 0.011 (essentially ZERO)
- **New Approach:** Categorical assessments (Strong/Decent/Weak)
  - Technical: Based on Trend Template + RSI + RS
  - Fundamental: Based on ROE, Revenue Growth, Debt/Equity
  - Sentiment: Based on Fear & Greed Index (55-75 = Strong)
  - Risk/Macro: Based on VIX (<20) + SPY regime (>200 EMA)
- **Verdict Logic:** Need 2+ Strong categories with Favorable/Neutral risk for BUY
- **Files:** `frontend/src/utils/categoricalAssessment.js`

### v4.6: Perplexity Research Recommendations (Day 45-47)
- **Priority:** HIGH
- **Status:** ✅ COMPLETE (4/4 recommendations done)
- **Source:** `docs/research/Perplexity_STA_Analysis_result_Feb5_2026`
- **Recommendations Implemented:**

| # | Recommendation | Priority | Effort | Status |
|---|----------------|----------|--------|--------|
| 1 | **F&G Threshold Fix** - Expand neutral zone from 45-55 to 35-60 | HIGH | Low | ✅ DONE (Day 45) |
| 2 | **Entry Preference Logic** - ADX-based (>25 momentum, 20-25 pullback) | MEDIUM | Medium | ✅ DONE (Day 47) |
| 3 | **Pattern Actionability** - Only show patterns ≥80% formed | MEDIUM | Medium | ✅ DONE (Day 47) |
| 4 | **Structure > Sentiment Hierarchy** - Risk/Macro overrides F&G assessment | HIGH | Low | ✅ DONE (Day 45) |

**Day 47 Implementation (v4.6.2 + v4.7.1):**
- ADX-based entry preference: >25 = Momentum viable, 20-25 = Pullback preferred, <20 = Wait for trend
- Pattern actionability: Only patterns ≥80% confidence shown as "Actionable" with trigger/stop/target prices
- **Breakout Volume Confirmation (v4.7.1):** Volume ≥1.5x avg = confirmed, shows quality badge (High/Medium/Low)
- Files modified: `categoricalAssessment.js`, `App.jsx`, `pattern_detection.py`

**Key Findings Applied:**
- F&G at 44.7 vs 45.0 creates cliff behavior (0.3 point = different assessment) → Fixed
- Elder's Triple Screen: Structure determines IF, Sentiment determines HOW → Implemented
- ADX > 25 = trend confirmed, favor momentum; ADX 20-25 = favor pullback → Implemented
- Patterns < 80% have high false positive rate - don't show "75% forming" → Implemented

### v4.7: Forward Testing UI ✅ COMPLETE (Day 47)
- **Priority:** HIGH (tracked since Day 25 as CRITICAL)
- **Status:** ✅ IMPLEMENTED
- **Description:** Paper trading simulation with R-multiple tracking
- **Features:**
  - Add/close trades with entry, stop, target prices
  - Automatic R-multiple calculation on close
  - Van Tharp statistics: Win Rate, Avg Win R, Avg Loss R, Expectancy, SQN
  - Trade journal table with status tracking
  - Export to CSV functionality
  - LocalStorage persistence
- **Files:** `frontend/src/utils/forwardTesting.js`, Forward Test tab in `App.jsx`

### v4.8: Comprehensive Testing Framework (Day 45)
- **Priority:** MEDIUM (testing ongoing)
- **Status:** ACTIVE (baseline tests complete, validation ongoing)
- **Test Plan:** `docs/test/TEST_PLAN_COMPREHENSIVE.md`
- **Test Script:** `backend/test_categorical_comprehensive.py`
- **Categories:**
  - A: API Contract Tests (structure validation)
  - B: Categorical Logic Tests (threshold behavior)
  - C: Edge Case Tests (ETFs, extremes, missing data)
  - D: Cross-Validation (vs external sources)
  - E: Integration Tests (frontend-backend match)

**Test Tickers:**
- Tier 1: AAPL, NVDA, JPM, MSFT, COST (baseline)
- Tier 2: SPY, QQQ (ETFs)
- Tier 3: Technical extremes (RSI < 30, > 80)
- Tier 4: TSLA, AMC (fundamental extremes)
- Tier 5: Small caps (PLTR, SOFI)

---

## PLANNED (Research-Verified Features)

> **Source:** Day 48 Multi-AI Research Analysis (Grok/ChatGPT/Perplexity)
> **Principle:** Only implement what's VERIFIED by multiple sources

### v4.9: Enhanced Volume Analysis ✅ COMPLETE (Day 49)
- **Priority:** HIGH (verified useful by all 3 sources)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - OBV (On-Balance Volume) indicator with trend detection (Rising/Falling/Flat)
  - OBV vs Price divergence detection (Bullish/Bearish/None)
  - Enhanced RVOL display (shows "2.3x avg" not just "confirmed")
  - Tooltips explaining each indicator
- **Files Modified:** `backend/backend.py` (v2.16), `frontend/src/App.jsx`
- **Backend:** `calculate_obv()` function added, returns in `/api/sr/<ticker>` meta

### v4.10: Earnings Calendar Warning ✅ COMPLETE (Day 49)
- **Priority:** HIGH (verified - "event risk dominates technicals")
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - Flag stocks with earnings within 7 days (configurable)
  - Warning badge on analysis card (red pulse for ≤3 days, yellow for 4-7 days)
  - Recommendation text based on timing (CAUTION, AWARE)
  - Tooltip with earnings date and specific advice
- **Backend:** `/api/earnings/<ticker>` endpoint with multiple yfinance fallback methods
- **Files Modified:** `backend/backend.py`, `frontend/src/services/api.js`, `frontend/src/App.jsx`

### v4.11: Sector Rotation Tab (Day 49+)
- **Priority:** MEDIUM (verified - simple RS ranking is effective)
- **Status:** PLANNED
- **Features:**
  - Sector RS Calculation (Sector ETF / SPY)
  - 11 SPDR Sector ETFs tracked
  - Simple 3-criteria ranking (RS > 0, RS > MA, near 52wk high)
  - Integration: Show sector context for analyzed stocks
- **Research:** `docs/research/RESEARCH_ANALYSIS_CRITICAL_REVIEW.md`
- **Effort:** 4-6 hours

### v4.12: TradingView Lightweight Charts
- **Priority:** MEDIUM
- **Status:** PLANNED (after volume/earnings features)
- **Description:** Interactive charts with S&R levels, RSI/MACD overlays
- **Technology:** TradingView Lightweight Charts (free, open source)
- **Effort:** 4-6 hours

### v4.13: Holding Period Selector + Bottom Line Summary (Day 50-51)
- **Priority:** HIGH (addresses core UX confusion)
- **Status:** PLANNED (REVISED after Day 51 research validation)
- **Problem:** Conflicting signals confuse users (JNJ: AVOID + PULLBACK OK + Stage 2 Uptrend)
- **Day 51 Research Findings:**
  - ❌ INVALIDATED: RSI thresholds by holding period (40-65/35-70/30-75 were invented, not research-backed)
  - ✅ VALIDATED: ADX-based regime determines RSI interpretation (already in v4.6.2)
  - ✅ VALIDATED: Signal weighting by horizon (arXiv 2512.00280 - 40 bps monthly alpha)
  - ✅ VALIDATED: Consolidated summary cards (UX research supports)
- **Revised Solution:**
  - 3-way holding period toggle: 5-10 days | 15-30 days | 1-3 months
  - Signal WEIGHTING by horizon (Quick=70% tech, Position=70% fund), NOT threshold adjustment
  - ADX-based RSI interpretation PRESERVED (weak trend=mean reversion, strong trend=momentum)
  - Unified "Bottom Line" card replacing confusing multiple signals
  - Clear action plan with entry/stop/target/alert prices
- **Plan:** `docs/research/HOLDING_PERIOD_SELECTOR_PLAN.md` (REVISED Day 51)
- **Effort:** 4-6 hours

### v4.14: Multi-Source Data Intelligence (Day 51+)
- **Priority:** HIGH (eliminates single-source dependency)
- **Status:** RESEARCH COMPLETE - Plan created
- **Problem:** STA relies 100% on yfinance (unofficial scraper, rate-limited, IP blocked)
- **Day 51 Research Findings (free tier reality):**
  - TwelveData: 800 credits/day, 8/min - BEST for OHLCV
  - Finnhub: Unlimited, 60/min - BEST for fundamentals
  - FMP: 250/day - Good fundamentals backup
  - Alpha Vantage: ~~25/day~~ - NOW NEARLY USELESS (was 500/day)
  - EODHD: 20/day, 10 credits/fundamental - NOT VIABLE free
  - yfinance: Free but unreliable - DEMOTE to fallback
- **Fallback Architecture:**
  - OHLCV: TwelveData → yfinance → Stooq
  - Fundamentals: Finnhub → FMP → yfinance
  - VIX: yfinance → Finnhub → cache fallback
- **Also Includes:**
  - Unified `DataProvider` class for backend + backtest scripts
  - Provenance tracking (which source served each data point)
  - Cache-first strategy with stale fallback
  - Frontend data freshness indicator (green/yellow/red dot)
- **Plan:** `docs/research/MULTI_SOURCE_DATA_PLAN.md`
- **Reference:** `docs/research/DATA_SOURCE_INTELLIGENCE_OVERVIEW.md` (proven in Codex engine)
- **Effort:** 9-13 hours (2-3 sessions)

---

## RESEARCH REQUIRED (Before Implementation)

### Options Open Interest
- **Status:** BLOCKED - Data availability uncertain
- **Action:** Verify yfinance options data works before planning
- **Test:** Run `ticker.option_chain()` and check `openInterest` field
- **If fails:** Explore Polygon.io or OCC as alternatives

### RSI/MACD Divergence Detection
- **Status:** RESEARCH NEEDED
- **Problem:** Generic false positive rates are unverifiable
- **Action:** If implementing, must compute OUR OWN FPR via backtest
- **Threshold:** Only implement if FPR < 40%

---

## DEFERRED (v2+ / Low Priority)

| Feature | Reason for Deferral |
|---------|---------------------|
| Full RRG Charts | Overkill - simple RS ranking achieves same goal (Day 48 research) |
| Candlestick Patterns | Low statistical accuracy per research |
| Full TradingView Integration | After Lightweight Charts validated |
| H&S Pattern Detection | Academic research "scarce and inconclusive" (NY Fed) |
| Seasonal Patterns | "Small edge", regime-dependent (ChatGPT) |
| Optimal Weighting System | No universal answer exists - varies by regime |
| Options Open Interest | Data source uncertain - verify first |

---

## RESEARCH COMPLETED

| Document | Topic | Day |
|----------|-------|-----|
| PERPLEXITY_RESEARCH_SYNTHESIS.md | Trading system validation | Day 41 |
| OPTIONS_TAB_FEASIBILITY_ANALYSIS.md | Options data requirements | Day 42 |
| SECTOR_ROTATION_IDENTIFICATION_GUIDE.md | Sector rotation methods | Day 42 |
| Perplexity_STA_Analysis_result_Feb5_2026 | UX/Trading system design (4 questions) | Day 45 |
| TEST_PLAN_COMPREHENSIVE.md | Quant-style testing methodology | Day 45 |
| Research_answers_For_Thinking_Journal.md | Multi-AI research (Grok/ChatGPT/Perplexity) | Day 48 |
| RESEARCH_ANALYSIS_CRITICAL_REVIEW.md | Critical analysis of research - verified vs unverified | Day 48 |
| ACTION_PLAN_FROM_RESEARCH.md | Implementation priorities from research | Day 48 |

---

## KEY INSIGHTS (Day 27 Philosophy + Day 44 Update)

From backtesting:
- **Entry signals = ~10% of results**
- **Position sizing = ~90% of results**
- Score-to-return correlation = 0.011 (essentially ZERO)
- 75-point scoring achieves ~50% win rate (essentially random)

**Day 44 Response (v4.5 Categorical Assessment):**
- Replaced 75-point numerical scoring with categorical assessments
- System works as a FILTER, not a RANKER
- Categories (Strong/Decent/Weak) honestly represent this reality
- Real Fear & Greed Index replaces placeholder sentiment

**Current Focus:**
- Better R:R through dual entry strategy
- Risk reduction through proper stops
- System measurement through forward testing
- Categorical filtering over numerical ranking

---

## UPDATE LOG

| Day | Changes |
|-----|---------|
| 42 | Created ROADMAP.md, added v4.4/v4.5 for placeholders |
| 44 | v4.2 Pattern Detection complete, v4.4 Sentiment (Fear & Greed) complete, v4.5 Categorical Assessment complete |
| 45 | v4.6 Perplexity Research Recommendations added, v4.7 Comprehensive Testing Framework added |
| 46 | v4.6 UI Testing complete, Issue #0 fixed (Recommendation Card alert prices), validated with 5-ticker 2nd iteration |
| 47 | v4.6.2 ADX Entry Preference + Pattern Actionability ≥80% complete, v4.7 Forward Testing UI complete |
| 48 | Multi-AI research analysis, added v4.9-v4.12 (OBV, Earnings, Sector Rotation, Charts), updated DEFERRED with research findings |
| 49 | v4.9 OBV+RVOL complete, v4.10 Earnings Warning complete, UI Cohesiveness test (92.8% pass), 5 issues fixed (support level, position sizing, VIABLE badge, R:R filter, null support zone) |
| 50 | Exhaustive UI re-test (21% true pass vs 92.8% spot-check), ALL 5 UI issues FIXED (v4.4), v4.13 Holding Period Selector plan created, n8n research notes added |
| 51 | v4.13 plan REVISED after research validation - RSI thresholds INVALIDATED, signal weighting VALIDATED, Golden Rule #15. v4.14 Multi-Source Data plan created - researched free tier limits, TwelveData+Finnhub primary, yfinance demoted to fallback |

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
