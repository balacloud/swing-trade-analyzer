# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 42 (February 2, 2026)
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v3.9 (Backend v2.13)

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

### v4.2: Pattern Detection
- **Priority:** MEDIUM
- **Description:** VCP, cup-and-handle, flat base patterns
- **Why:** Better entry timing for swing trades
- **Effort:** Medium

### v4.3: Options Tab
- **Priority:** LOW
- **Description:** Options data display if data sources available
- **Blocker:** Needs Greeks calculation, complex data sourcing
- **Research:** `docs/research/OPTIONS_TAB_FEASIBILITY_ANALYSIS.md`

### v4.4: Sentiment Integration
- **Priority:** MEDIUM (tracked since Day 1)
- **Description:** Replace placeholder 5/10 sentiment with real data
- **Current State:** Hardcoded 5/10 (13% of score is fake)
- **Solution Options:**
  1. Finnhub free tier (news sentiment)
  2. Fear & Greed Index API
  3. Earnings proximity flag
- **UI:** Now shows "placeholder" label (Day 42)

### v4.5: Scoring Logic Review + Market Breadth
- **Priority:** MEDIUM (tracked since Day 1)
- **Description:**
  1. Replace Market Breadth placeholder (1/1 pts)
  2. Re-evaluate 75-point weights based on backtest data
- **Current State:** Market Breadth hardcoded (1% of score)
- **Research Finding:** Real breadth filter is HIGH ROI (Day 34)

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

## KEY INSIGHTS (Day 27 Philosophy)

From backtesting:
- **Entry signals = ~10% of results**
- **Position sizing = ~90% of results**
- 75-point scoring achieves ~50% win rate (essentially random)

**Current Focus:**
- Better R:R through dual entry strategy
- Risk reduction through proper stops
- System measurement through forward testing

---

## UPDATE LOG

| Day | Changes |
|-----|---------|
| 42 | Created ROADMAP.md, added v4.4/v4.5 for placeholders |

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
