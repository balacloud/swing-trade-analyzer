# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 57 (February 22, 2026)
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v4.18 (Backend v2.20, Frontend v4.6, Backtest v4.17)

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

### Backtest Status (Day 55-56)
| Gate | Description | Status |
|------|-------------|--------|
| G1 | Holistic 3-Layer Backtest (60 tickers) | ✅ COMPLETE (Day 55) |
| G2 | Walk-Forward Validation (IS vs OOS) | ✅ COMPLETE (Day 55) |
| G3 | Exit Strategy Optimization | ✅ COMPLETE (Day 55) |
| G4 | Bear Market Regime Filter | ✅ VALIDATED (Day 57) — bear WR 55.6%→71.4% |
| G5 | Frontend-Backend Threshold Sync | ✅ COMPLETE (Day 56) |
| G6 | Quick & Position Period Backtest | ✅ COMPLETE (Day 57) — walk-forward validated |
| G7 | Full System Coherence Audit | ✅ COMPLETE (Day 57) — 71 params, 96% coherence |

**Test Command:** `python backend/backtest/backtest_holistic.py --configs C --walk-forward`

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

### v4.11: Sector Rotation (Day 49+, Rethought Day 57)
- **Priority:** MEDIUM (verified - simple RS ranking is effective)
- **Status:** PLANNED (Phase 1 approach — embed in existing views first)
- **Research:** `docs/research/Sector_Rotation_analysis.md` (450+ lines, comprehensive)
- **Phase 1 (1-2 hrs):** Sector context in existing views — NO new tab
  - Backend: `/api/sectors/rotation` — fetch 11 SPDR ETFs, calculate RS vs SPY, cache daily
  - Analyze page: Show "Technology (XLK) — LEADING" below stock header
  - Scan results: Add sector strength badge
  - Decision Matrix: Add sector as informational factor (no verdict change)
  - Purely informational — does NOT change any trade signals or verdicts
- **Phase 2 (later, only if Phase 1 insufficient):** Dedicated sector tab
  - 11 sector cards ranked by RS with quadrant colors (Leading/Improving/Weakening/Lagging)
  - "Show stocks in this sector" → pre-filter Scan tab
- **Key insight:** 70% of stock price movement comes from sector leadership (Faber study)
- **Effort:** Phase 1: 1-2 hours | Phase 2: 2-3 hours additional

### v4.12: TradingView Lightweight Charts
- **Priority:** MEDIUM
- **Status:** PLANNED (after volume/earnings features)
- **Description:** Interactive charts with S&R levels, RSI/MACD overlays
- **Technology:** TradingView Lightweight Charts (free, open source)
- **Effort:** 4-6 hours

### v4.13: Holding Period Selector + Bottom Line Summary ✅ COMPLETE (Day 53)
- **Priority:** HIGH (addresses core UX confusion)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - 3-way holding period toggle: Quick (5-10d) | Standard (15-30d) | Position (1-3mo)
  - Signal WEIGHTING by horizon (Quick=T:70%/F:30%, Standard=50/50, Position=T:30%/F:70%)
  - Verdict changes when Tech and Fundamental disagree (weighting tips the balance)
  - Bottom Line Card with action plan, what's good/risky, weight badges
  - Research-validated: arXiv 2512.00280 (40 bps monthly alpha from signal weighting)
- **Files Modified:** `categoricalAssessment.js`, `BottomLineCard.jsx`, `App.jsx`

### v4.15: Decision Matrix Tab ✅ COMPLETE (Day 53)
- **Priority:** HIGH (synthesis layer for 3 independent analysis systems)
- **Status:** ✅ IMPLEMENTED
- **Problem Solved:** 3 layers (Assessment, Patterns, Trade Setup) each produce correct output independently but nobody SYNTHESIZES them. Trader had to mentally cross-reference 4+ UI cards.
- **Features:**
  - 3-step workflow: "Should I Trade This?" → "When Should I Enter?" → "Does The Math Work?"
  - Surfaces 10 computed-but-hidden fields (RS interpretation, ADX analysis, signal weights, entry preference, fundamental metrics, sentiment subLabel)
  - Contradiction resolution: explains WHY backend says "Good setup" but R:R fails
  - Contextual action items based on verdict + viability + patterns
  - 3rd view toggle between Full Analysis and Simple Checklist
- **Files:** `frontend/src/components/DecisionMatrix.jsx` (new), `App.jsx` (3 edits)

### v4.16: Holistic 3-Layer System Backtest ✅ COMPLETE (Day 55)
- **Priority:** HIGH (cannot validate system without historical outcome testing)
- **Status:** ✅ IMPLEMENTED
- **Results (60 tickers, 2020-2025):**
  - Config A (Categorical only): 1108 trades, 51.53% WR, PF 1.41, p<0.000001
  - Config B (A + Patterns): 406 trades, 51.72% WR, PF 1.43, p=0.002
  - Config C (Full 3-layer): 238 trades, 53.78% WR, PF 1.61, Sharpe 0.85, p=0.002
  - **All 3 configs statistically significant — NOT random**
- **Walk-Forward:** OOS outperforms IS — system is NOT overfitted
- **Exit Optimization:** 10-day EMA trailing stop + breakeven stop, max drawdown 65.9% → 52.6%
- **Files:** `backend/backtest/` (5 new files: simfin_loader, categorical_engine, metrics, trade_simulator, backtest_holistic)

### v4.17: Production Coherence + Bear Regime ✅ COMPLETE (Day 56)
- **Priority:** HIGH (sync production with backtested thresholds)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - Frontend-backend coherence audit: 39/42 parameters matched
  - Pattern confidence threshold synced: 80% → 60% in production
  - Bear market regime: SPY 50 SMA declining caps risk at "Neutral"
  - 5th scan filter redesigned to match Config C criteria
- **Files Modified:** `categoricalAssessment.js`, `backend.py`, `App.jsx`, backtest files

### v4.14: Multi-Source Data Intelligence ✅ COMPLETE (Day 52)
- **Priority:** HIGH (eliminates single-source dependency)
- **Status:** ✅ IMPLEMENTED
- **Problem Solved:** STA relied 100% on yfinance (unofficial scraper, rate-limited, IP blocked)
- **Providers Implemented:**
  - TwelveData: 800 credits/day, 8/min - Primary OHLCV
  - Finnhub: Unlimited, 60/min - Primary fundamentals
  - FMP: 250/day - Fundamentals backup (epsGrowth, revenueGrowth)
  - yfinance: Free - Universal fallback
  - Stooq: Free via pandas_datareader - Last resort OHLCV
- **Fallback Architecture:**
  - OHLCV: TwelveData → yfinance → Stooq
  - Fundamentals: Finnhub → FMP → yfinance (field-level merge)
  - VIX: yfinance → Finnhub → stale cache
- **Infrastructure:**
  - `backend/providers/` package (13 files)
  - `DataProvider` orchestrator with singleton pattern
  - Circuit breaker per provider (3 failures → 5min cooldown)
  - Token-bucket rate limiting per provider
  - Cache-first strategy with stale cache fallback
  - Provenance tracking (`_field_sources` dict)
  - `backtest_adapter.py` for backtest scripts
- **Backend Integration:** All 9 yfinance call sites replaced with DataProvider + legacy fallback
- **Frontend:** All data source labels updated from "Defeat Beta" / "yfinance" to multi-source names
- **Files:** `backend/providers/` (13 files), `backend/backend.py` (v2.17), `backend/cache_manager.py`

---

### v4.18: S&P 500 / NASDAQ 100 / Dow 30 Index Filter ✅ COMPLETE (Day 56)
- **Priority:** MEDIUM (user-requested quality filter)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - User-selectable dropdown: All US Stocks / S&P 500 / NASDAQ 100 / Dow 30
  - TradingView native `Query().set_index()` — no maintenance needed
  - Correct index identifiers (verified via live testing):
    - S&P 500: `SYML:SP;SPX` (503 stocks)
    - NASDAQ 100: `SYML:NASDAQ;NDX` (101 stocks)
    - Dow 30: `SYML:DJ;DJI` (30 stocks)
  - Works with all 5 scan strategies
- **Files Modified:** `backend.py` (INDEX_MAP + market_index param), `api.js` (marketIndex param), `App.jsx` (dropdown)

---

## RESEARCH REQUIRED (Before Implementation)

### RSI/MACD Divergence Detection

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

### v4.19: Basic Options Tab (LOWEST PRIORITY)
- **Priority:** LOW — build only when daily forward testing is running and system is in maintenance mode
- **Status:** RESEARCH COMPLETE (Perplexity deep research, Day 56)
- **Research doc:** `docs/research/OPTIONS_TAB_PERPLEXITY_PROMPT.md` (includes full results)
- **Scope:** 4 signals: Call Buy, Covered Call, Put Buy, Cash-Secured Put eligibility
- **Data:** yfinance chains + `py_vollib_vectorized` for local Greeks/IV computation
- **Key decisions:**
  - Binary "Eligible / Not Eligible" per strategy with bullet rationale
  - IV Rank/Percentile computed locally from stored IV history
  - Greeks via Black-Scholes (no vendor dependency)
  - No multi-leg strategies, no naked selling, no real-time dashboards
- **Prerequisite:** System must be in daily forward testing phase first

### v4.20: Canadian Market Support (TSX) (LOW PRIORITY)
- **Priority:** LOW — build when US market flow is stable
- **Status:** RESEARCH COMPLETE (Day 56, live-tested)
- **Verified:**
  - TradingView `set_markets('canada')` → 8,408 stocks (TSX + NEO exchanges)
  - TSX 60 index: `set_index('SYML:TSX;TX60')` → 60 stocks
  - All technical columns (RSI, ADX, EMA50, SMA200, RVOL) available and identical to US
- **Changes needed:**
  - **Scan tab (easy):** Add `tsx60` to INDEX_MAP, add `canada` to set_markets, frontend dropdown options
  - **Analysis tab (medium):** Ticker mapping `TSX:RY` → `RY.TO` for yfinance/TwelveData
  - **Benchmark decision:** RS vs SPY (keep) or RS vs XIU.TO (Canadian benchmark) — or auto-detect
  - **Currency:** CAD label on prices (no conversion needed)
  - **VIX/Regime:** US VIX still valid for global sentiment; Canadian VIXC optional
- **What doesn't change:** All technical analysis, S/R clustering, pattern detection, decision matrix — math is math
- **Market hours:** TSX = same as NYSE (9:30-4:00 ET) — no timezone issues

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
| OPTIONS_TAB_PERPLEXITY_PROMPT.md | Options Tab: data sources, checklists, Greeks, decision matrix | Day 56 |

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
| 52 | v4.14 Multi-Source Data Intelligence COMPLETE: 5 providers, 13 new files, backend v2.17, field-level merge, circuit breakers, rate limiting, frontend labels updated, Defeat Beta now redundant |
| 53 | v4.15 Decision Matrix COMPLETE, v4.13 Holding Period COMPLETE, Bugs #7/#8 fixed, Architectural audit: removed fundamentals from /api/stock/ (SRP), removed ~255 lines dead code, 5-field end-to-end reconciliation. Backend v2.18. |
| 54 | Pre-backtest audit (3 investigations): API data integrity (3 CRITICAL + 4 HIGH found), Decision Matrix coherence (ALL CLEAR), Simple Checklist review (50% SEPA alignment). Fixed 4 hardcoded fallbacks: sentiment 5→0, breadth 1→0, F&G 50→null, VIX 20→null. Golden Rule: silent fallbacks are invisible lies. |
| 55 | v4.16 Holistic 3-Layer Backtest COMPLETE: 60 tickers, 3 configs, all statistically significant. Config C: 53.78% WR, PF 1.61, Sharpe 0.85. Walk-forward validated. Exit optimization: trailing 10 EMA + breakeven stop, DD reduced -13.3%. |
| 56 | v4.17: 5th filter redesigned (Config C), coherence audit (39/42 match, pattern threshold 80→60), bear regime filter added. v4.18 S&P/NASDAQ/Dow index filter IMPLEMENTED. Options Tab research complete (v4.19, deferred). |
| 57 | Bear regime backtest VALIDATED (bear WR 71.4%). Quick+Position periods backtested and walk-forward validated. Full coherence audit (71 params, 96%). sma50Declining wired backend→frontend. yfinance 0.2.28→1.2.0. Sector rotation plan RETHOUGHT (Phase 1: embed in views, not new tab). |

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
