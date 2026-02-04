# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 44 (February 4, 2026)
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

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
