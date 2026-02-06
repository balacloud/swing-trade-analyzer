# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 46 (February 6, 2026)
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v4.0 (Backend v2.15)

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

### v4.6: Perplexity Research Recommendations (Day 45-46)
- **Priority:** HIGH
- **Status:** IN PROGRESS (2/4 recommendations done + UI testing complete)
- **Source:** `docs/research/Perplexity_STA_Analysis_result_Feb5_2026`
- **Recommendations to Implement:**

| # | Recommendation | Priority | Effort | Status |
|---|----------------|----------|--------|--------|
| 1 | **F&G Threshold Fix** - Expand neutral zone from 45-55 to 35-60 | HIGH | Low | ✅ DONE (Day 45) |
| 2 | **Entry Preference Logic** - ADX-based (>25 momentum, 20-25 pullback) | MEDIUM | Medium | PENDING |
| 3 | **Pattern Actionability** - Only show patterns ≥80% formed | MEDIUM | Medium | PENDING |
| 4 | **Structure > Sentiment Hierarchy** - Risk/Macro overrides F&G assessment | HIGH | Low | ✅ DONE (Day 45) |

**Day 46 Testing & Bug Fix:**
- UI Test Report: `docs/test/UI_TEST_REPORT_DAY46.md` (10-ticker comprehensive test)
- Issue #0 Fixed: Recommendation Card now uses `entryPreference` for alert prices
- 2nd Iteration Validation: 5/5 tickers pass post-fix

**Key Findings from Research:**
- F&G at 44.7 vs 45.0 creates cliff behavior (0.3 point = different assessment)
- Elder's Triple Screen: Structure determines IF, Sentiment determines HOW
- ADX > 25 = trend confirmed, favor momentum; ADX 20-25 = favor pullback
- Patterns < 80% have high false positive rate - don't show "75% forming"

### v4.7: Comprehensive Testing Framework (Day 45)
- **Priority:** HIGH (prerequisite for forward testing)
- **Status:** ACTIVE (baseline tests complete, validation ongoing)
- **Test Plan:** `docs/test/TEST_PLAN_COMPREHENSIVE.md`
- **Test Script:** `backend/test_categorical_comprehensive.py`
- **Categories:**
  - A: API Contract Tests (structure validation)
  - B: Categorical Logic Tests (threshold behavior)
  - C: Edge Case Tests (ETFs, extremes, missing data)
  - D: Cross-Validation (vs external sources)
  - E: Integration Tests (frontend-backend match)
  - F: Forward Testing Framework

**Test Tickers:**
- Tier 1: AAPL, NVDA, JPM, MSFT, COST (baseline)
- Tier 2: SPY, QQQ (ETFs)
- Tier 3: Technical extremes (RSI < 30, > 80)
- Tier 4: TSLA, AMC (fundamental extremes)
- Tier 5: Small caps (PLTR, SOFI)

---

## DEFERRED (v2+ / Low Priority)

| Feature | Reason for Deferral |
|---------|---------------------|
| Sector Rotation RRG | Complex, marginal v1 value |
| Candlestick Patterns | Low statistical accuracy per research |
| Full TradingView Integration | After Lightweight Charts validated |

---

## RESEARCH COMPLETED

| Document | Topic | Day |
|----------|-------|-----|
| PERPLEXITY_RESEARCH_SYNTHESIS.md | Trading system validation | Day 41 |
| OPTIONS_TAB_FEASIBILITY_ANALYSIS.md | Options data requirements | Day 42 |
| SECTOR_ROTATION_IDENTIFICATION_GUIDE.md | Sector rotation methods | Day 42 |
| Perplexity_STA_Analysis_result_Feb5_2026 | UX/Trading system design (4 questions) | Day 45 |
| TEST_PLAN_COMPREHENSIVE.md | Quant-style testing methodology | Day 45 |

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

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
