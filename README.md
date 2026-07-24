# 🎯 Swing Trade Analyzer

An institutional-grade stock analysis system for swing traders, built on proven methodologies from **Mark Minervini's SEPA** (Specific Entry Point Analysis) and **William O'Neil's CAN SLIM** approach.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Assessment Methodology](#assessment-methodology)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Environment Variables (API Keys)](#environment-variables-api-keys)
- [Running the App](#running-the-app)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Data Sources](#data-sources)
- [Validation System](#validation-system)
- [Known Limitations](#known-limitations)
- [Roadmap](#roadmap)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

### What is This?

A **data-driven swing trade recommendation engine** that analyzes stocks and provides:
- **Categorical Assessment System** (v4.5+) - Strong/Decent/Weak ratings across Technical, Fundamental, Sentiment (info-only), and Risk
- **BUY / HOLD / AVOID verdicts** based on Technical + Fundamental categories (2 Strong = BUY, Risk/Macro = gate)
- **Pattern Detection** - VCP, Cup & Handle, Flat Base + Minervini Trend Template
- **Fear & Greed Index** - Real market sentiment data (replaces placeholder)
- **Trade setups** with Entry, Stop Loss, Target, and Risk/Reward ratios
- **Dual Entry Strategy** - Conservative (support) and Aggressive (current) entries
- **Relative Strength (RS)** calculations vs S&P 500
- **Batch scanning** for market opportunities (TradingView integration)
- **Data validation** against external sources (typical quality score ~90%+, methodology-aware tolerances)
- **Full data transparency** - see exactly where each data point comes from
- **Automated paper-trading engine** - unattended daily job takes every qualifying signal (momentum + mean-reversion) with zero human filtering, the real forward-test of the system

### Target Users

- Active swing traders seeking data-driven trade recommendations
- Traders following Minervini SEPA or O'Neil CAN SLIM methodologies
- Anyone looking for systematic stock analysis with quantified edge

### Trading Parameters

| Parameter | Value |
|-----------|-------|
| Hold Period | Quick (5-10d) / Standard (15-30d) / Position (1-3mo) |
| Target Returns | 10-20% per trade (2-3R) |
| Position Risk | 2-5% of account per trade |
| Risk/Reward | Minimum 2:1 required |

> **Day 27 Critical Insight:** Backtesting revealed score-to-return correlation = 0.011 (essentially ZERO). Entry signals account for only ~10% of trading results, while position sizing accounts for ~90%.
>
> **Day 44 Response (v4.5):** Replaced 75-point numerical scoring with categorical assessments (Strong/Decent/Weak). The system works as a FILTER, not a RANKER. Categorical assessments honestly represent this reality and eliminate false precision.

---

## Features

> **Status note:** a complete feature freeze has been in effect since Day 87 — the list below reflects everything shipped, but active work is currently limited to bug fixes and the automated paper-trading engine (100 confirmed trades/system required before any capital allocation). See [Roadmap](#roadmap) for current priorities.

### ✅ Implemented (v4.52)

1. **Single Stock Analysis**
   - Enter any ticker symbol
   - Get categorical assessment (Strong/Decent/Weak) across 4 dimensions
   - BUY / HOLD / AVOID verdict with detailed reasoning
   - 3-tier progressive disclosure (always visible / collapsed / hidden)
   - Holding period selector: Quick (5-10d) / Standard (15-30d) / Position (1-3mo)

2. **Position Sizing Calculator** (Day 28-29)
   - Van Tharp R-multiple principles
   - Configurable account size and risk % (2-5%)
   - Auto-calculates shares, R targets (1.5R, 2R, 3R)
   - Auto-fill from stock analysis
   - Manual override for custom entry/stop prices
   - Max position limit to prevent over-allocation

3. **Advanced S&R Detection** (Day 31-34)
   - **Agglomerative Clustering** - Adaptive cluster count (replaced KMeans)
   - **ZigZag Pivot Detection** - 5% minimum price change threshold
   - **Touch-based Scoring** - Levels ranked by historical touches
   - **Multi-Timeframe Confluence** - Daily + Weekly S&R alignment
   - **Fibonacci Extensions** - For stocks at all-time highs
   - 100% detection rate (was 80% with KMeans)
   - Confluence badge shows % of levels confirmed by weekly data

4. **Dual Entry Strategy** (Day 39-40)
   - **Conservative Entry** - Wait for pullback to support
   - **Aggressive Entry** - Enter at current price
   - Side-by-side comparison cards for ALL stocks
   - Shows R:R ratio, ADX trend strength, 4H RSI confirmation
   - Structural stop loss (below support) for both strategies

5. **Trade Setup Generation**
   - Support & Resistance detection (Pivot → Agglomerative → Volume Profile)
   - Suggested Entry, Stop Loss, Target
   - Risk/Reward ratio calculation
   - Pullback re-entry zones for extended stocks
   - **MTF Confluence indicators** (★ marks confluent levels)

6. **Market Scanning** (TradingView Screener + IBKR Pipeline research)
   - 6 pre-built strategies: Reddit, Minervini (Large-Cap Momentum Filter), Momentum, Value, Best Candidates, **Near Breakout**
   - Plus 2 curated personal watchlists: Nirmal's Watchlist (20 tickers) and the Master Framework Watchlist (76 tickers, sourced from Notion research)
   - **Best Candidates** aligned with backtested Config C criteria (ADX>=20, RSI 50-70, EMA10>EMA21, positive 52-week performance, RVOL>=1)
   - Market index filters: S&P 500 / NASDAQ 100 / Dow 30 / All US / TSX 60 / All Canadian
   - Stage 2 uptrend requirement (50 SMA > 200 SMA)
   - **IBKR two-stage pipeline** (research complete, build pending): 10-factor real-time screener → `/ibkr-scan` Claude skill → top 5–10 STA candidates. 3-LLM validated filters (Minervini/SEPA-derived).

7. **Data Validation Engine** (Day 42)
   - Cross-references our data against StockAnalysis and Finviz
   - Quality Score = Coverage × Accuracy
   - Methodology-aware tolerances (see [Validation System](#validation-system))
   - Identifies data discrepancies

8. **Multi-Source Data Intelligence** (Day 52 - v4.14, extended through Day 83)
   - **7 data providers** with automatic fallback chains (2 dormant/inactive, kept for status reporting — see [Data Sources](#data-sources))
   - OHLCV: TwelveData → yfinance → **Tradier** → stale cache
   - Fundamentals: Finnhub → AlphaVantage → yfinance (field-level merge)
   - Circuit breaker per provider (3 failures → 5min cooldown), now shared across the Flask backend and the paper-trading job via SQLite so both processes see the same provider health (Day 83)
   - Token-bucket rate limiting per provider
   - Cache-first with stale cache fallback when all providers fail
   - Provenance tracking (which provider supplied each data field)
   - ETF detection with special handling

9. **Breakout Detection Engine** (Day 79-87)
   - Standalone 8-state classifier: `NOT_READY`, `BUILDING_BASE`, `BREAKOUT_WATCH`, `BREAKOUT_CONFIRMED`, `RETEST_ENTRY`, `SUPPLY_WARNING`, `FAILED_BREAKOUT`, `EXTENDED_CHASE_RISK`
   - Per-ticker (`/api/breakout/<ticker>`) and batch (`/api/breakout/batch`, up to 20 tickers) endpoints
   - Breakout badge column on Scan tab results, breakout status on the Analyze page
   - `/breakout-watch` Claude skill for an EOD sweep across a watchlist

10. **Automated Paper Trading Engine** (Day 81+)
    - Unattended daily job (launchd, weekdays ~16:30 CT) — takes every qualifying signal for both momentum and mean-reversion with zero human filtering, removing selection bias from the forward test
    - Shared exit-replay logic with the backtest engine (`live_mode` parameter) so live and backtested results can't silently drift apart
    - Status panel + manual "Force Run Now" trigger in the Forward Test tab, with per-position ticker/entry/exit detail
    - Currently the project's sole active development focus: 100 confirmed trades/system required (raised from 50, Day 92) before any capital allocation

11. **Market Phase Synthesis** (Day 87)
    - Market-wide read (not per-stock) classifying current conditions into one of 5 phases: Bull Rally, Late Bull, Distribution, Correction, Recovery
    - 3×3 grid: SPY trend bucket × VIX level bucket, with breadth (RSP/SPY ratio) and sector leadership (Growth vs Defensive ETFs) as supporting context
    - Purely informational — zero impact on verdict/scoring

12. **Value Investing Tab** (Day 75)
    - Standalone value lens (Buffett/Graham/Lynch/Damodaran) — ROIC, ROE, Graham Number, P/E, PEG/PEGY, FCF yield
    - Zero impact on the swing verdict or categorical assessment

9. **9-Criteria Simple Checklist** (Day 27, enhanced Day 60)
    - Binary pass/fail system — ALL 9 must pass for TRADE verdict
    - **Criteria:** Trend (P>50>200 SMA), Momentum (RS>1.0), Setup (stop within 7%), Risk/Reward (R:R>=2:1), 52-Wk Range (top 25%), Volume ($10M+ daily), ADX (>=20), Market Regime (SPY>200 SMA), 200 SMA Trend (rising)
    - Based on Minervini SEPA criteria + holistic backtest validation

10. **Sector Rotation** (Day 58-62 - v4.19 → v4.24, redesigned Day 93 - v4.50)
    - `/api/sectors/rotation` — 11 SPDR sector ETFs ranked by RS ratio vs SPY, plus a Cap Size Rotation strip (QQQ/MDY/IWM)
    - RRG quadrant classification (Leading, Weakening, Lagging, Improving)
    - Color-coded sector badge on Analyze page + sector column in Scan results
    - Dedicated Sectors tab, cards grouped by quadrant with a plain-English takeaway (redesigned Day 93 — no per-card rank badge, since any ordinal reads as "the winner" regardless of qualifying text)
    - `macro_alignment` — states in one sentence whether the macro backdrop (Context tab's FRED-derived regime) supports the rotation currently shown (Day 93)

11. **Pattern Detection** (Day 44 - v4.2, refined Day 64)
    - VCP (Volatility Contraction Pattern), Cup & Handle, Flat Base
    - Minervini's 8-point Trend Template
    - Pattern confidence scoring with actionability threshold (>= 60%)
    - Breakout quality assessment (High/Medium/Low)

12. **Earnings Calendar Warning** (Day 49 - v4.10)
    - Flags stocks with earnings within 7 days
    - Red pulse badge for ≤ 3 days, yellow for 4-7 days
    - Recommendation text (CAUTION / AWARE)

13. **Enhanced Volume Analysis** (Day 49 - v4.9)
    - OBV (On-Balance Volume) with trend detection (Rising/Falling/Flat)
    - OBV vs Price divergence detection (Bullish/Bearish/None)
    - Enhanced RVOL display ("2.3x avg")

14. **~~Decision Matrix~~ (Removed Day 70 — Simplicity Premium)**
    - Replaced by 3-tier progressive disclosure in full analysis view

15. **Holding Period Selector** (Day 53 - v4.13)
    - Quick (5-10d) / Standard (15-30d) / Position (1-3mo)
    - Signal weighting by horizon (Quick=70% Tech, Position=70% Fund)
    - Bottom Line Card with action plan summary

16. **Forward Testing / Paper Trading — manual journal** (Day 47 - v4.7)
    - Add/close trades manually with entry, stop, target prices
    - R-multiple tracking with Van Tharp statistics (Win Rate, Expectancy, SQN)
    - Trade journal table, export to CSV, localStorage persistence
    - Distinct from the **automated paper-trading engine** (item 10 above) — this is the original manual-entry journal, still present and separate from the unattended Day-81 engine

17. **Context Tab** (Day 62 - v4.24)
    - 6 calendar/yield cycle cards (Yield Curve, Business Cycle, Presidential Year, Seasonal, FOMC, Quad Witching)
    - 4 economic indicator cards (Fed Funds, CPI, PMI proxy, Unemployment) via FRED API
    - News sentiment + short interest per ticker via Alpha Vantage
    - Overall macro regime across 10 indicators + options block detection
    - Market Phase banner (item 11 above) and a Market-Phase↔Macro-Regime reconciliation, plus the same Sectors↔Context `macro_alignment` link (Day 93)
    - PRE-FLIGHT CONTEXT ONLY — does not modify verdicts

18. **Cache Freshness Meter** (Day 59 - v4.20)
    - `/api/data/freshness` endpoint — returns cache age per data source
    - UI freshness dots (green=fresh, yellow=aging, red=stale) on Analyze page

19. **Canadian Market Scanning** (Day 59 - v4.21)
    - TSX 60 and All Canadian market scan support
    - Ticker mapping: `TSX:RY` → `RY.TO` for data providers

20. **SQLite Persistent Cache** (Day 37)
    - 5.5x performance improvement
    - OHLCV cache with market-aware TTL (expires after market close)
    - Fundamentals cache with 7-day TTL
    - Survives backend restarts
    - Cache status endpoint for monitoring

21. **Data Sources Tab** (Day 38)
    - Full transparency on data provenance
    - Shows which provider supplied each data field
    - Cache hit/miss status
    - Calculation formulas displayed

22. **Service Management Scripts** (Day 37)
    - `./start.sh` - Start backend and/or frontend
    - `./stop.sh` - Stop services cleanly

23. **Settings & Configuration**
    - Persistent account settings (localStorage)
    - Risk percentage slider (2-5%)
    - Position sizing preferences

---

## Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                         │
│                        localhost:3000                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Analyze Tab │  │  Scan Tab   │  │    Validation Tab       │  │
│  │             │  │             │  │                         │  │
│  │ - Ticker    │  │ - Strategy  │  │ - Multi-ticker input    │  │
│  │ - Assessment│  │ - Results   │  │ - Pass/Fail/Warning     │  │
│  │ - Trade     │  │ - Quick     │  │ - Quality metrics       │  │
│  │   Setup     │  │   Analyze   │  │                         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Sectors Tab │  │ Context Tab │  │       Value Tab         │  │
│  │             │  │             │  │                         │  │
│  │ - 11 sector │  │ - Cycles +  │  │ - ROIC/ROE, Graham #    │  │
│  │   RS cards  │  │   econ +    │  │ - PE/PEG, FCF yield     │  │
│  │ - Cap size  │  │   news      │  │ - Buffett/Graham/Lynch  │  │
│  │   rotation  │  │ - Macro     │  │                         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
│                                                                  │
│  ┌─────────────────┐  ┌───────────────┐  ┌──────────────────┐   │
│  │ Data Sources Tab │  │ Forward Test  │  │   Settings Tab   │   │
│  │                  │  │               │  │                  │   │
│  │ - Provenance     │  │ - Automated   │  │ - Account size   │   │
│  │ - Cache status   │  │   paper-trade │  │ - Risk %         │   │
│  │ - Transparency   │  │   ledger      │  │ - Position limits│   │
│  │                  │  │ - Manual R-   │  │                  │   │
│  │                  │  │   multiple    │  │                  │   │
│  │                  │  │   journal     │  │                  │   │
│  └─────────────────┘  └───────────────┘  └──────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│                      SERVICES & UTILS                           │
│  ┌──────────────┐  ┌───────────────┐  ┌───────────────────┐     │
│  │   api.js     │  │ categorical   │  │ simplified        │     │
│  │              │  │ Assessment.js │  │ Scoring.js        │     │
│  │ 10 parallel  │  │ Verdict logic │  │ 9-criteria        │     │
│  │ API calls    │  │ (4 categories)│  │ binary checklist  │     │
│  └──────────────┘  └───────────────┘  └───────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP/REST
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       BACKEND (Flask)                           │
│                       localhost:5001                            │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 API ENDPOINTS (30+ routes)               │    │
│  │                                                         │    │
│  │  Core Analysis:                                         │    │
│  │  /api/stock/<ticker>        - Price data, basic info    │    │
│  │  /api/fundamentals/<ticker> - Fundamental data          │    │
│  │  /api/sr/<ticker>           - Support & Resistance      │    │
│  │  /api/patterns/<ticker>     - VCP, Cup&Handle, FlatBase │    │
│  │  /api/earnings/<ticker>     - Earnings calendar warning │    │
│  │  /api/breakout/<ticker>     /api/breakout/batch         │    │
│  │  /api/value/<ticker>        - Value investing analysis  │    │
│  │                                                         │    │
│  │  Market Data:                                           │    │
│  │  /api/market/spy   /api/market/vix   /api/fear-greed    │    │
│  │  /api/market/phase - 5-phase market classification      │    │
│  │  /api/sectors/rotation  - 11 sector RS ranking          │    │
│  │  /api/mr/signal/<ticker>    /api/mr/scan                │    │
│  │                                                         │    │
│  │  Context (FRED + Alpha Vantage):                        │    │
│  │  /api/cycles  /api/econ  /api/news/<ticker>             │    │
│  │  /api/context/<ticker>  - aggregated macro regime        │    │
│  │                                                         │    │
│  │  Scanning & Paper Trading:                               │    │
│  │  /api/scan/tradingview     /api/scan/strategies          │    │
│  │  /api/paper-trading/status  /api/paper-trading/trigger   │    │
│  │                                                         │    │
│  │  Validation & Infrastructure:                           │    │
│  │  /api/validation/run  /results  /history                │    │
│  │  /api/provenance/<ticker>  /api/data/freshness          │    │
│  │  /api/cache/status  /api/cache/clear  /api/health       │    │
│  └─────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────┤
│                        MODULES                                  │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │ support_       │  │ pattern_        │  │  cache_manager  │   │
│  │ resistance.py  │  │ detection.py    │  │      .py        │   │
│  │                │  │                 │  │                 │   │
│  │ Agglomerative  │  │ VCP, Cup&Handle │  │ SQLite cache    │   │
│  │ + MTF S&R      │  │ Trend Template  │  │ (5.5x speedup)  │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │  providers/    │  │   validation/   │  │ cycles_engine/  │   │
│  │                │  │                 │  │ econ_engine/    │   │
│  │ 7 data sources │  │ engine, scrapers│  │ news_engine     │   │
│  │ + orchestrator │  │ forward_tracker │  │ (FRED + AV)     │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │ paper_trading/ │  │ mean_reversion  │  │ market_phase_   │   │
│  │                │  │ .py             │  │ engine.py       │   │
│  │ ledger,        │  │                 │  │ market_         │   │
│  │ live_signals,  │  │ RSI(2) MR       │  │ structure_      │   │
│  │ daily_job      │  │ engine          │  │ engine.py       │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
│  ┌────────────────┐                                              │
│  │ breakout_      │                                              │
│  │ routes.py /    │                                              │
│  │ _detection.py  │                                              │
│  │ scan_queries.py│                                              │
│  └────────────────┘                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  TwelveData  │  │   Finnhub    │  │ AlphaVantage │           │
│  │              │  │              │  │              │           │
│  │ - OHLCV      │  │ - ROE, ROA   │  │ - EPS Growth │           │
│  │ - Intraday   │  │ - PE, Margins│  │ - Rev Growth │           │
│  │ 8/min limit  │  │ - D/E, Beta  │  │ 250/day      │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │   yfinance   │  │   Tradier    │  │  TradingView │           │
│  │  (fallback)  │  │ (last resort)│  │   Screener   │           │
│  │ - All data   │  │ - OHLCV+Quote│  │ - Batch scans│           │
│  │ 15-30m delay │  │ 120/min      │  │ - Real-time  │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│  ┌──────────────┐  ┌──────────────┐                             │
│  │     FRED     │  │ Alpha Vantage│                             │
│  │              │  │              │                             │
│  │ - Yield curve│  │ - News       │                             │
│  │ - CPI, Funds │  │   sentiment  │                             │
│  │ 1000/day     │  │ 25/day free  │                             │
│  └──────────────┘  └──────────────┘                             │
│                              │                                   │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SQLite Cache                          │    │
│  │         backend/data/cache.db (persistent)              │    │
│  │  - OHLCV: 24h TTL (market-aware) + source tracking      │    │
│  │  - Fundamentals: 7 day TTL                              │    │
│  │  - Context (FRED/news): 4-6h TTL                        │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User enters ticker
        │
        ▼
┌───────────────────┐
│ fetchFullAnalysis │ (api.js)
│ Data()            │
└───────────────────┘
        │
        ├──► Check SQLite cache first
        │         │
        │         ├──► Cache HIT: Return cached data (5.5x faster)
        │         │
        │         └──► Cache MISS: Fetch from sources ──┐
        │                                                │
        ├──► /api/stock/AAPL ──────► TwelveData → yfinance → Tradier → stale cache
        ├──► /api/fundamentals/AAPL ► Finnhub → AlphaVantage → yfinance (merge)
        ├──► /api/market/spy ──────► Same OHLCV chain (for RS)
        ├──► /api/market/vix ──────► Cache(1h) → yfinance → Finnhub → Tradier → stale cache
        ├──► /api/sr/AAPL ─────────► S&R Engine (Entry/Stop/Target)
        ├──► /api/patterns/AAPL ───► VCP, Cup&Handle, Flat Base detection
        ├──► /api/fear-greed ──────► CNN Fear & Greed Index
        ├──► /api/earnings/AAPL ───► Earnings calendar (event risk)
        ├──► /api/sectors/rotation ► 11 sector RS ranking vs SPY
        └──► /api/data/freshness ──► Cache age per data source
        │
        ▼
┌───────────────────────────┐
│ Categorical Assessment    │ (categoricalAssessment.js)
│                           │
│ Technical:  Strong/Decent/Weak  (Trend Template + RSI + RS)
│ Fundamental: Strong/Decent/Weak (ROE, Revenue Growth, D/E)
│ Sentiment:  Strong/Neutral/Weak (Fear & Greed Index)
│ Risk/Macro: Favorable/Neutral/Unfavorable (VIX + SPY)
└───────────────────────────┘
        │
        ▼
┌───────────────────────────┐
│ Verdict:                  │
│ BUY / HOLD / AVOID        │
│ (2+ Strong + Favorable    │
│  Risk = BUY)              │
└───────────────────────────┘
        │
        ▼
┌───────────────────────────┐
│ 3-Tier Progressive         │
│ Disclosure + Dual Entry    │
│ Strategy Cards             │
└───────────────────────────┘
```

---

## Assessment Methodology

### Categorical Assessment System (v4.5+)

Replaced the original 75-point numerical scoring (which had 0.011 score-to-return correlation) with categorical assessments. The system works as a **FILTER**, not a RANKER.

#### Four Assessment Dimensions

| Dimension | Levels | Key Metrics |
|-----------|--------|-------------|
| **Technical** | Strong / Decent / Weak | Trend Template (8-point), RSI, RS vs SPY, ADX |
| **Fundamental** | Strong / Decent / Weak | ROE, Revenue Growth, Debt/Equity |
| **Sentiment** | Strong / Neutral / Weak | CNN Fear & Greed Index |
| **Risk/Macro** | Favorable / Neutral / Unfavorable | VIX level, SPY regime (above 200 SMA) |

#### Technical Assessment Thresholds

| Level | Criteria |
|-------|----------|
| **Strong** | Trend Template >= 7/8 AND RSI 50-70 AND RS >= 1.0 |
| **Decent** | Trend Template >= 5/8 AND RSI 40-80 |
| **Weak** | Below thresholds, extreme RSI, or RS < 0.8 |

#### Fundamental Assessment Thresholds

| Level | Criteria |
|-------|----------|
| **Strong** | 2+ strong metrics (ROE > 15%, RevGrowth > 10%, D/E < 1.0) AND 0 weak |
| **Decent** | Mixed — some strong, some moderate (ROE 8-15%, RevGrowth 0-10%, D/E 1-2) |
| **Weak** | 2+ weak metrics (ROE < 8%, negative growth, D/E > 2.0) |

### Verdict Logic

Only Technical and Fundamental feed the strong/weak count that drives the verdict — Sentiment is display-only, Risk/Macro is a gate, not a vote.

| Verdict | Conditions |
|---------|------------|
| **BUY** | 2 Strong categories (Technical + Fundamental) + Favorable/Neutral risk, with an ADX<20 downgrade to HOLD (see Additional Filters) |
| **HOLD** | Mixed signals, or Unfavorable risk gate |
| **AVOID** | Weak Technical (non-negotiable). Weak Fundamental is holding-period-conditional — for a Position hold it's an AVOID; for a Quick hold with Strong Technical it can still pass through |

> **Note:** Sentiment (Fear & Greed) is displayed as informational only — it does not affect the verdict. Backtest validated T+F as verdict drivers and Risk/Macro as a gate. Sentiment was never validated (hardcoded Neutral in backtest).

### Additional Filters

- **ADX < 20** downgrades a would-be BUY (2 strong categories) to HOLD — it does not override every other path (e.g. it never overrides a Weak-Technical AVOID)
- **Pattern confidence >= 60%** = actionable (backtested threshold)
- **Holding period weighting**: Quick = 70% Technical, Position = 70% Fundamental
- **Bear market regime**: SPY 50 SMA declining caps risk at "Neutral"

### Backtest Validation

**Historical (v4.16, Day 55, hand-picked 60-ticker universe — kept for history, superseded below):**

| Config | Trades | Win Rate | Profit Factor | Sharpe | p-value |
|--------|--------|----------|---------------|--------|---------|
| A (Categorical only) | 1,108 | 51.53% | 1.41 | — | <0.000001 |
| B (A + Patterns) | 406 | 51.72% | 1.43 | — | 0.002 |
| C (Full 3-layer) | 238 | 53.78% | 1.61 | 0.85 | 0.002 |

**Canonical (Day 79, survivorship-free — 400 tickers randomly sampled from a 3,788-ticker universe, no hand-picking):**

| System | Trades | Win Rate | Profit Factor | Sharpe | Significant? |
|--------|--------|----------|----------------|--------|--------------|
| Momentum (Config C) | 114 | 49.12% | 1.40 | 0.52 | No — block bootstrap p=0.094 |
| Mean-Reversion (liquidity-restricted) | 3,210 | 57.35% | 1.16 | 1.30 | No — p=0.064 (close, not confirmed) |

Both edges survive directionally (PF > 1) but are not yet statistically distinguishable from chance. Since Day 81, an automated paper-trading engine has been running unattended daily to get the real confirmation: **100 live trades/system required before any capital allocation.** See [Roadmap](#roadmap) for current status.

---

## Tech Stack

### Frontend
- **React 18** - UI framework
- **Tailwind CSS** - Styling
- **Fetch API** - HTTP requests

### Backend
- **Python 3.9+** - Runtime
- **Flask** - Web framework
- **SQLite** - Persistent cache (Day 37)
- **Multi-Source Provider System** (v4.14, extended Day 83):
  - **TwelveData** - Primary OHLCV + Intraday
  - **Finnhub** - Primary Fundamentals + Quote
  - **AlphaVantage** - Growth metrics (epsGrowth, revenueGrowth) + News Sentiment
  - **yfinance** - Universal fallback
  - **Tradier** - 3rd-tier OHLCV + Quote fallback, 120 req/min (Day 83)
  - **Stooq** (pandas_datareader) — present in code but inactive since Day 82 (bot-blocked); kept only for status reporting
  - **FMP** — present in code but inactive since Aug 2025 (dormant, kept for a future paid-plan upgrade)
- **tradingview-screener** - Batch scanning
- **scikit-learn** - Agglomerative clustering for S&R
- **beautifulsoup4 + selenium** - Web scraping for validation
- **FRED API** - Macro economic data (yield curve, CPI, Fed funds)
- **Alpha Vantage** - News sentiment

### Data Sources

| Source | Data Type | Rate Limit | Role |
|--------|-----------|------------|------|
| TwelveData | OHLCV, Intraday | 8/min, 800/day | Primary OHLCV |
| Finnhub | Fundamentals, Quote | 60/min | Primary Fundamentals |
| AlphaVantage | Growth metrics, News | 25/day (free) | Fundamentals backup + News |
| yfinance | All types | ~30/min | Universal fallback |
| Tradier | OHLCV, Quote | 120/min | Last resort OHLCV/Quote |
| ~~Stooq~~ | OHLCV only | ~5/min | Inactive since Day 82 (bot-blocked); code retained |
| TradingView Screener | Batch scanning | Real-time | Market scanning |
| FRED | Macro data | 1000/day | Context Tab |
| Alpha Vantage | News sentiment | 25/day (free) | Context Tab |
| StockAnalysis | Validation | Real-time | Data quality check |
| Finviz | Validation | Real-time | Data quality check |

---

## Installation

### Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- npm
- Chrome browser (required only for the Data Validation feature — uses Selenium)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/balacloud/swing-trade-analyzer.git
cd swing-trade-analyzer
```

### 2. Backend setup

```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API keys

The backend requires API keys to fetch market data. **API keys are never committed to git.** You must create the `.env` file manually:

```bash
# From the backend/ directory
cp .env.example .env
```

Then open `backend/.env` and fill in your keys. See the [Environment Variables](#environment-variables-api-keys) section below for how to get each key.

### 4. Frontend setup

```bash
cd ../frontend
npm install
```

---

## Environment Variables (API Keys)

Create `backend/.env` based on `backend/.env.example`. Here is every variable, where to get it, and what degrades without it:

### Required

| Variable | Where to Get It | Free Tier |
|----------|----------------|-----------|
| `TWELVEDATA_API_KEY` | [twelvedata.com](https://twelvedata.com) → Sign up → API Keys | 800 credits/day, 8/min |
| `FINNHUB_API_KEY` | [finnhub.io](https://finnhub.io) → Sign up → Dashboard | 60 calls/min |
| `ALPHAVANTAGE_API_KEY` | [alphavantage.co](https://www.alphavantage.co/support/#api-key) | 25 calls/day (free) |

### Optional (graceful degradation if not set)

| Variable | Where to Get It | Without It |
|----------|----------------|------------|
| `FRED_API_KEY` | [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) — instant, no credit card | Context tab shows no macro data |
| `TRADIER_ACCESS_TOKEN` | [tradier.com](https://tradier.com) → developer account | Loses the 3rd-tier OHLCV/Quote fallback (confirmed production-tier, 120 req/min) — chain degrades to yfinance as the last active tier |
| `SIMFIN_API_KEY` | [simfin.com](https://simfin.com) | Only needed for backtest scripts (`backend/backtest/`), not the live app |
| `FMP_API_KEY` | [financialmodelingprep.com](https://financialmodelingprep.com) | Currently dormant regardless — kept in code pending a future paid-plan decision |

> **Without ALPHAVANTAGE_API_KEY:** EPS growth, revenue growth, and news sentiment fall back to yfinance data.

### Example `.env` file

```env
# Required
TWELVEDATA_API_KEY=your_twelvedata_key_here
FINNHUB_API_KEY=your_finnhub_key_here
ALPHAVANTAGE_API_KEY=your_alphavantage_key_here

# Optional
FRED_API_KEY=your_fred_key_here
TRADIER_ACCESS_TOKEN=your_tradier_token_here
SIMFIN_API_KEY=your_simfin_key_here
FMP_API_KEY=your_fmp_key_here
```

---

## Running the App

### Quick start (both services)

```bash
# From project root
./start.sh

# Or start individually
./start.sh backend   # Backend only (http://localhost:5001)
./start.sh frontend  # Frontend only (http://localhost:3000)
```

### Manual start

```bash
# Terminal 1 — Backend
cd backend
source venv/bin/activate
python backend.py

# Terminal 2 — Frontend
cd frontend
npm start
```

### Stop services

```bash
./stop.sh           # Stop both
./stop.sh backend   # Stop backend only
./stop.sh frontend  # Stop frontend only
```

---

## Usage

### Analyze a Stock

1. Open http://localhost:3000
2. Enter ticker symbol (e.g., "AAPL")
3. Click "Analyze" or press Enter
4. View results:
   - Verdict (BUY/HOLD/AVOID) with categorical assessment
   - **Dual Entry Strategy cards** (Conservative vs Aggressive)
   - Trade setup (Entry/Stop/Target)
   - Pattern detection and volume analysis
5. Optionally adjust the **holding period** (Quick 5-10d / Standard 15-30d / Position 1-3mo) — this appears after results load, collapsed by default, and re-weights the signal (Quick=70% Technical, Position=70% Fundamental)

### Scan for Opportunities

1. Click "Scan Market" tab
2. Select strategy:
   - **Reddit**: Mid-cap+, high relative volume
   - **Minervini** (Large-Cap Momentum Filter): Large-cap ($10B+) stocks above rising SMA50/SMA200 with positive momentum
   - **Momentum**: Sustainable 5-50% monthly gains
   - **Value**: Quality at fair price (P/E 5-25)
   - **Best Candidates**: Backtested Config C picks (ADX>=20, RSI 50-70, EMA10>EMA21, positive 52W performance, RVOL>=1)
   - **Near Breakout**: Stage-2 stocks within 8% of their 52-week high
   - Or one of 2 curated personal watchlists (Nirmal's Watchlist, Master Framework Watchlist)
3. Select index (S&P 500, NASDAQ 100, Dow 30, All US, TSX 60, All Canadian)
4. Click "Scan for Opportunities"
5. Click any result to run full analysis

### Sector Rotation

1. Click **Sectors** tab to see all 11 SPDR sector ETFs, grouped by RRG quadrant (Leading / Improving / Weakening / Lagging), plus a Cap Size Rotation strip
2. Read the plain-English takeaway and the macro-alignment note (whether the current macro backdrop supports the rotation shown)
3. Click "Scan for [Sector]" on the recommended card to filter scan results to that sector

### Context Tab (Macro Pre-Flight)

1. Click **Context** tab
2. Cycle/yield-curve and economic-indicator cards load automatically (FRED data — no ticker needed), along with the Market Phase banner
3. Search a ticker on Analyze tab → the news/sentiment column populates for that ticker

### Validate Data Accuracy

1. Click "Validate Data" tab
2. Enter tickers (comma-separated)
3. Click "Run Validation"
4. Review Quality Score, Coverage, Accuracy

### View Data Sources

1. Click "Data Sources" tab
2. Enter a ticker to see:
   - Where each data point comes from
   - Cache hit/miss status
   - Calculation formulas used

### Forward Test (Paper Trading)

Click **Forward Test** tab to see the automated paper-trading engine's status (open/closed positions and per-ticker entry/exit detail for both the momentum and mean-reversion systems, with a manual "Force Run Now" trigger), or record trades manually in the separate R-multiple journal (Van Tharp SQN framework).

### Settings

Click **Settings** tab to configure account size, risk percentage (2-5%), and position sizing preferences for the Position Sizing Calculator (Van Tharp R-multiple framework).

---

## API Reference

### GET /api/health

Returns backend health status including multi-source provider information.

```json
{
  "status": "healthy",
  "timestamp": "2026-07-22T16:24:13Z",
  "version": "2.44",
  "defeatbeta_available": true,
  "tradingview_available": true,
  "sr_engine_available": true,
  "validation_available": true,
  "sqlite_cache_available": true,
  "data_provider_available": true,
  "cache": {"ohlcv_count": 45, "fundamentals_count": 32, "market_count": 5, "cache_size_kb": 1024},
  "providers": {
    "providers": {
      "twelvedata": {"configured": true, "type": "OHLCV + Intraday"},
      "finnhub": {"configured": true, "type": "Fundamentals + Quote"},
      "alphavantage": {"configured": true, "type": "Fundamentals (growth) + News"},
      "yfinance": {"configured": true, "type": "All (fallback)"},
      "tradier": {"configured": true, "type": "OHLCV + Quote (last resort)"}
    }
  }
}
```

### GET /api/stock/\<ticker\>

Returns price data and basic info. **Does not include fundamentals** — call `/api/fundamentals/<ticker>` separately (a hardcoded-zeros fundamentals bug used to corrupt categorical scoring here, so this endpoint deliberately never returns that field).

```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "currentPrice": 272.97,
  "fiftyTwoWeekHigh": 288.62,
  "fiftyTwoWeekLow": 169.21,
  "avgVolume": 48123456,
  "priceHistory": [...]
}
```

### GET /api/fundamentals/\<ticker\>

Returns fundamental data with multi-source fallback (Finnhub → AlphaVantage → yfinance).

```json
{
  "source": "finnhub",
  "dataSource": "finnhub",
  "dataQuality": "full",
  "fallbackUsed": false,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 12.5,
  "revenueGrowth": 6.43,
  "debtToEquity": 1.34,
  "profitMargin": 24.3,
  "_field_sources": {
    "pe": "finnhub",
    "roe": "finnhub",
    "epsGrowth": "alphavantage",
    "revenueGrowth": "alphavantage"
  }
}
```

**Data Quality Values:** `"full"` (multi-source working), `"partial"` (yfinance fallback only), `"unavailable"`

### GET /api/sr/\<ticker\>

Returns Support & Resistance levels with trade setup and MTF confluence.

```json
{
  "ticker": "AAPL",
  "currentPrice": 272.97,
  "volume": 48123456,
  "change": 1.24,
  "method": "agglomerative",
  "support": [251.19, 245.67, 238.90],
  "resistance": [273.29, 280.45, 288.62],
  "suggestedEntry": 251.19,
  "suggestedStop": 243.65,
  "suggestedTarget": 273.29,
  "riskReward": 2.93,
  "meta": {
    "mtf": {
      "enabled": true,
      "confluence_pct": 27.3,
      "confluent_levels": 3,
      "total_levels": 11,
      "weekly_support": [250.50, 232.00],
      "weekly_resistance": [275.00, 290.00],
      "confluence_map": {
        "251.19": {"confluent": true, "weekly_match": 250.50}
      }
    },
    "marketStructure": {
      "structure": "Uptrend",
      "trendAgeBars": 34,
      "volumeBehavior": "rising",
      "recentPivots": [{"type": "HH", "price": 273.29}, {"type": "HL", "price": 251.19}]
    }
  }
}
```

### GET /api/provenance/\<ticker\>

Returns detailed data source provenance for transparency.

```json
{
  "ticker": "AAPL",
  "price_data": {
    "source": "yfinance",
    "cached": true,
    "cache_age_seconds": 3600,
    "fields": {
      "currentPrice": {"source": "yfinance", "cached": true},
      "fiftyTwoWeekHigh": {"source": "yfinance", "cached": true}
    }
  },
  "fundamentals": {
    "source": "finnhub",
    "cached": true,
    "cache_age_seconds": 86400,
    "fields": {
      "roe": {"source": "finnhub", "formula": "Net Income / Shareholders Equity"},
      "epsGrowth": {"source": "alphavantage", "formula": "(Current EPS - Previous EPS) / Previous EPS"}
    }
  }
}
```

### GET /api/cache/status

Returns detailed cache statistics.

```json
{
  "status": "healthy",
  "storage": "sqlite",
  "database_size_kb": 1024,
  "ohlcv": {
    "count": 45,
    "hit_rate_24h": 0.87,
    "entries": [{"ticker": "AAPL", "cached_at": "...", "expires_at": "..."}]
  },
  "fundamentals": {
    "count": 32,
    "hit_rate_24h": 0.92,
    "entries": [...]
  }
}
```

### POST /api/cache/clear

Clear cache with optional filters.

```
POST /api/cache/clear              # Clear all
POST /api/cache/clear?ticker=AAPL  # Clear specific ticker
POST /api/cache/clear?type=ohlcv   # Clear specific cache type
```

### GET /api/scan/tradingview

Batch scan for opportunities. `strategy` accepts `reddit`, `minervini`, `momentum`, `value`, `best`, or `breakout`. `market_index` accepts `sp500`, `nasdaq100`, `dow30`, `tsx60`, or `canada` (default: all US).

```
GET /api/scan/tradingview?strategy=reddit&limit=50&market_index=sp500
```

```json
{
  "strategy": "reddit",
  "marketIndex": "sp500",
  "totalMatches": 847,
  "returned": 50,
  "timestamp": "2026-07-22T16:24:13Z",
  "candidates": [
    {
      "ticker": "GEV",
      "name": "GE Vernova",
      "price": 723.0,
      "marketCap": 196164696259,
      "rsi": 73.49,
      "relativeVolume": 4.53
    }
  ]
}
```

### GET /api/patterns/\<ticker\>

Detect chart patterns (VCP, Cup & Handle, Flat Base) and Minervini Trend Template.

```json
{
  "ticker": "AAPL",
  "patterns": {
    "vcp": {"detected": false, "confidence": 0},
    "cup_handle": {"detected": true, "confidence": 72.5},
    "flat_base": {"detected": false, "confidence": 0}
  },
  "summary": {
    "patterns_detected": ["cup_handle"],
    "best_pattern": "cup_handle",
    "confidence": 72.5,
    "actionable": true
  },
  "trend_template": {
    "criteria_met": 7,
    "total_criteria": 8,
    "details": [...]
  }
}
```

### GET /api/fear-greed

Returns CNN Fear & Greed Index for sentiment assessment.

```json
{
  "value": 62.5,
  "rating": "Greed",
  "assessment": "Strong",
  "timestamp": "2026-02-25T16:00:00Z",
  "previousClose": 58.2,
  "source": "CNN Fear & Greed Index"
}
```

**Assessment mapping:** Strong (60-80), Neutral (35-60), Weak (<35 or >80)

### GET /api/earnings/\<ticker\>

Flags upcoming earnings to avoid gap risk.

```json
{
  "ticker": "AAPL",
  "has_upcoming": true,
  "earnings_date": "2026-04-30",
  "days_until": 5,
  "warning": "📅 Earnings in 5 days",
  "recommendation": "AWARE - Consider exiting before earnings if position is taken.",
  "source": "calendar"
}
```

### GET /api/sectors/rotation

Returns 11 SPDR sector ETFs ranked by RS ratio vs SPY with RRG quadrant classification, cap-size rotation (QQQ/MDY/IWM), and a macro-alignment read. Cached per trading day. **Note:** `frontend/src/services/api.js`'s `fetchSectorRotation()` reconstructs this object field-by-field rather than passing it through raw — if you add a new backend field here, it must also be added there or the frontend silently won't receive it (a real bug found Day 92).

```json
{
  "sectors": [
    {
      "etf": "XLK",
      "name": "Technology",
      "price": 268.41,
      "rsRatio": 1.05,
      "rsMomentum": 0.02,
      "quadrant": "Leading",
      "weekChange": 2.1,
      "monthChange": 5.3
    }
  ],
  "sectorCount": 11,
  "mapping": {
    "Technology": "XLK",
    "Information Technology": "XLK",
    "Financials": "XLF"
  },
  "size_rotation": [
    {"etf": "QQQ", "label": "Large Cap Growth", "rsRatio": 101.9, "quadrant": "Weakening"}
  ],
  "size_signal": "Mixed",
  "size_signal_detail": "mid/small caps gaining, large cap fading",
  "macro_alignment": "Macro backdrop is NEUTRAL — neither confirming nor contradicting the current sector picture.",
  "macro_alignment_status": "neutral",
  "timestamp": "2026-07-22T16:24:13Z",
  "period": "3mo"
}
```

**Quadrants:** Leading (RS>1 + rising), Weakening (RS>1 + falling), Lagging (RS<1 + falling), Improving (RS<1 + rising)
**`macro_alignment_status`:** `aligned` | `cross_current` | `neutral`

### GET /api/cycles

Returns 6 calendar/yield cycle cards. Requires `FRED_API_KEY`. Cached 6h.

```json
{
  "cards": [
    {
      "name": "Yield Curve",
      "value": "+0.62%",
      "phase": "Normal · Steepening",
      "regime": "FAVORABLE",
      "source": "FRED T10Y2Y"
    }
  ],
  "options_block": {"has_options_block": false, "reason": null},
  "summary": {"favorable": 4, "neutral": 1, "adverse": 1}
}
```

### GET /api/econ

Returns 4 economic indicator cards (Fed Funds, CPI, PMI proxy, Unemployment). Cached 6h.

### GET /api/news/\<ticker\>

Returns news sentiment + short interest. Requires `ALPHAVANTAGE_API_KEY`. Cached 4h.

### GET /api/context/\<ticker\>

Aggregates cycles + econ + news. Computes `overall_regime` across 10 indicators and `options_block`.

```json
{
  "ticker": "AMD",
  "overall_regime": "FAVORABLE",
  "regime_counts": {"favorable": 7, "neutral": 2, "adverse": 1},
  "total_indicators": 10,
  "options_block": {"has_options_block": false, "reason": null},
  "cycles": {...},
  "econ": {...},
  "news": {...}
}
```

### GET /api/data/freshness

Returns cache age and freshness status per data source for the UI freshness meter.

```
GET /api/data/freshness?ticker=AAPL
```

```json
{
  "sources": [
    {
      "name": "Price Data",
      "key": "ohlcv",
      "status": "fresh",
      "ageMinutes": 45.2,
      "source": "twelvedata"
    },
    {
      "name": "Fundamentals",
      "key": "fundamentals",
      "status": "aging",
      "ageMinutes": 4320.0,
      "source": "finnhub"
    }
  ]
}
```

**Status values:** `fresh` (green), `aging` (yellow), `stale` (red), `live` (blue), `unknown` (gray)

### GET /api/scan/strategies

Returns available scan strategy definitions.

```json
{
  "strategies": [
    {"id": "reddit", "name": "Reddit Style", "description": "Mid-cap+, high relative volume, momentum stocks"},
    {"id": "minervini", "name": "Large-Cap Momentum Filter", "description": "Large-cap ($10B+) stocks above rising SMA50/SMA200 with positive 1W/1M momentum"},
    {"id": "momentum", "name": "Momentum", "description": "Sustainable gains, RSI 50-75 (not overbought)"},
    {"id": "value", "name": "Value", "description": "Quality stocks above 200 SMA at fair RSI levels"},
    {"id": "best", "name": "Best Candidates", "description": "Stage 2 + ADX≥20 + RSI 50-70 + EMA10>EMA21 + positive 52W performance + RVOL≥1"},
    {"id": "breakout", "name": "Near Breakout", "description": "Stage-2 stocks within 8% of 52-week high, RSI 50-70, ADX≥20"}
  ]
}
```

### GET /api/paper-trading/status

Read-only status of the automated paper-trading ledger — open/pending/closed positions and stats for both systems (momentum, mr), plus per-position ticker/entry/exit detail.

```json
{
  "lastRunDate": "2026-07-22",
  "systems": {
    "momentum": {
      "openPositions": 14,
      "closedTrades": 1,
      "stats": {"total_trades": 1, "win_rate": 0.0, "profit_factor": 0.0, "expectancy": -4.731, "avg_r_multiple": -1.0},
      "positions": {"open": [...], "pending": [...], "closed": [...]}
    },
    "mr": {
      "openPositions": 3,
      "closedTrades": 23,
      "stats": {"total_trades": 23, "win_rate": 95.65, "profit_factor": 20.54, "expectancy": 4.271, "avg_r_multiple": 0.854},
      "positions": {"open": [...], "pending": [...], "closed": [...]}
    }
  }
}
```

### POST /api/paper-trading/trigger

Manually force-runs the daily paper-trading job (catch-up after a missed scheduled run). Synchronous — can take 10-30+ seconds (live OHLCV fetches + TradingView scan).

```json
// Response
{"summary": {"momentum_signals": 0, "mr_signals": 2, "positions_stepped": 17, "date": "2026-07-22"}}
```

### GET /api/breakout/\<ticker\>

Returns one of 8 breakout states: `NOT_READY`, `BUILDING_BASE`, `BREAKOUT_WATCH`, `BREAKOUT_CONFIRMED`, `RETEST_ENTRY`, `SUPPLY_WARNING`, `FAILED_BREAKOUT`, `EXTENDED_CHASE_RISK`.

```json
{
  "ticker": "AAPL",
  "status": "BREAKOUT_WATCH",
  "dataPoints": 260,
  "source": "twelvedata",
  "benchmark": {"ticker": "SPY", "source": "twelvedata", "available": true},
  "apiTimestamp": "2026-07-22T16:24:13Z"
}
```

### POST /api/breakout/batch

Batch breakout status for up to 20 tickers in one call (Scan tab badge column). Returns partial results — a bad ticker doesn't fail the whole batch.

```json
// Request
{"tickers": ["AAPL", "NVDA", "MSFT"]}
```

### GET /api/mr/signal/\<ticker\>

Checks for an active mean-reversion signal (RSI(2) < 10, above 200 SMA, liquidity gate).

```json
{"ticker": "AAPL", "signal": true, "rsi2": 8.3, "range_bound": true}
```

### GET /api/mr/scan

Scans a universe (default: `mean_reversion.DEFAULT_MR_UNIVERSE`, or pass `?tickers=AAPL,MSFT,...`) for active MR signals.

```json
{"signals": [{"ticker": "AAPL", "rsi2": 8.3}], "scanned": 54, "found": 1}
```

### GET /api/value/\<ticker\>

Value-investing analysis (Buffett/Graham/Lynch/Damodaran framing) — quality (ROIC, ROE, FCF yield) + valuation (Graham Number, P/E, PEG/PEGY). Zero impact on the swing verdict.

```json
{
  "ticker": "AAPL",
  "cap_size": "large",
  "sector": "Technology",
  "quality": {
    "roic": {"value": 42.1, "wacc_approx": 9.0, "spread": 33.1, "verdict": "strong"},
    "roe": {"value": 151.9, "threshold": 15.0, "leverage_flag": true, "verdict": "strong"},
    "fcf_yield": {"value": 3.2, "verdict": "decent"},
    "verdict": "strong"
  },
  "valuation": {"...": "Graham Number, P/E, PEG/PEGY — same shape pattern as quality"}
}
```

### GET /api/market/phase

N4 Market Phase Synthesis — classifies current market-wide conditions into one of 5 phases from SPY trend + VIX level, with breadth and sector-leadership as supporting context. Ticker-independent, cached per trading day, purely informational.

```json
{
  "phase": "Late Bull",
  "description": "SPY still above its 200-day average but momentum slowing, or VIX creeping up — uptrend intact but maturing.",
  "signals": {
    "spy": {"close": 754.51, "sma200": 695.85, "aboveSma200": true, "pctChange20d": -0.04, "trendBucket": "FLAT"},
    "vix": {"current": 16.08, "pctChange10d": -3.07, "levelBucket": "CALM"},
    "breadth": {"rspSpyRatio": 0.2823, "pctChange20d": 0.08, "label": "Flat"},
    "sectors": {"growthReturn20d": -1.57, "defensiveReturn20d": 2.74, "label": "Mixed"}
  }
}
```

### GET /api/market/spy

SPY OHLCV via the standard multi-source chain (used for RS calculations).

### GET /api/market/vix

Current VIX level via the quote chain (cache 1h → yfinance → Finnhub → Tradier → stale cache).

### GET /api/validation/results

Get latest (or specific) validation results. Params: `?run_id=20260225_103000`

### GET /api/validation/history

Get list of all validation runs. Params: `?limit=10`

### POST /api/validation/run

Cross-validate data against external sources.

```json
// Request
{ "tickers": ["AAPL", "NVDA", "MSFT"] }

// Response
{
  "summary": {
    "quality_score": 92.3,
    "coverage_rate": 97.4,
    "accuracy_rate": 100.0,
    "passed": 94,
    "failed": 0,
    "warnings": 9
  },
  "ticker_results": [...]
}
```

---

## Data Sources

### Multi-Source Provider System (v4.14, extended Day 83)

STA uses a multi-source data architecture with automatic fallback chains, eliminating single-point-of-failure dependency on any one provider. The real OHLCV chain is TwelveData → yfinance → Tradier → stale cache; fundamentals is Finnhub → AlphaVantage → yfinance.

### TwelveData (Primary - OHLCV)

- **What:** Daily OHLCV price data, intraday data (for 4H RSI)
- **Rate Limit:** 8 requests/min, 800/day (free tier)
- **API Key:** Required (`TWELVEDATA_API_KEY` in `.env`)
- **Reliability:** High, official API

### Finnhub (Primary - Fundamentals)

- **What:** PE, ROE, ROA, Debt/Equity, Profit Margin, Beta, Current Ratio
- **Rate Limit:** 60 requests/min (free tier, unlimited daily)
- **API Key:** Required (`FINNHUB_API_KEY` in `.env`)
- **Note:** Lacks epsGrowth and revenueGrowth — filled by AlphaVantage

### AlphaVantage (Backup - Growth Metrics + News)

- **What:** EPS Growth, Revenue Growth (fills Finnhub gaps) + News Sentiment for Context Tab
- **Rate Limit:** 25/day (free tier)
- **API Key:** Required (`ALPHAVANTAGE_API_KEY` in `.env`)

### yfinance (Universal Fallback)

- **What:** All data types (prices, fundamentals, earnings, stock info)
- **Rate Limit:** Self-imposed 30/min
- **API Key:** None (unofficial Yahoo Finance scraper)
- **Reliability:** Variable — subject to Yahoo throttling/blocking

### Tradier (Last Resort - OHLCV + Quote)

- **What:** Daily OHLCV and quote data (VIX, etc.) — 3rd-tier fallback, added Day 83
- **Rate Limit:** 120 requests/min (confirmed production-tier)
- **API Key:** Required for this tier (`TRADIER_ACCESS_TOKEN` in `.env`) — chain simply stops one tier earlier without it
- **Reliability:** High, official brokerage API

### ~~Stooq~~ (Inactive since Day 82)

- **What:** Daily OHLCV only via pandas_datareader — kept in code for status reporting only, **not in the active fallback chain** (bot-blocked)
- **API Key:** None

### Field-Level Merge Strategy

```python
# Finnhub provides most fundamental fields
# AlphaVantage fills growth gaps (epsGrowth, revenueGrowth)
# yfinance fills any remaining gaps
# Result includes _field_sources for transparency
merged = {
    "pe": "finnhub",
    "roe": "finnhub",
    "epsGrowth": "alphavantage",    # Finnhub lacks this
    "revenueGrowth": "alphavantage", # Finnhub lacks this
    "pegRatio": "yfinance"     # Only yfinance has this
}
```

### TradingView Screener (Scanning)

- **What:** Batch market scanning with filters
- **Update Frequency:** Real-time
- **Filters Available:** Market cap, RSI, SMA relationships, volume, sector

---

## Validation System

### Purpose

Ensure our data matches external sources to maintain accuracy.

### Sources Compared

| Our Data | Compared Against |
|----------|------------------|
| Price, P/E, EPS, 52w High/Low | StockAnalysis.com |
| ROE, Debt/Equity, Revenue Growth | Finviz.com |
| S&R Logic | Internal consistency checks |

### Metrics

| Metric | Formula |
|--------|---------|
| **Coverage** | Checks with external data / Total checks |
| **Accuracy** | Passed checks / Validated checks |
| **Quality Score** | Coverage × Accuracy |

### Tolerances (Day 42, revised Day 54 - Methodology-Aware)

```python
TOLERANCES = {
    'price': 2%,
    'pe_ratio': 10%,
    'roe': 20%,            # Increased for methodology differences
    'revenue_growth': 25%, # Fiscal YoY vs TTM differences (was 85%, unit bug fixed Day 54)
    'eps_growth': 25%,
    'debt_equity': 50%,    # Total debt vs long-term only
    '52w_high': 1%,
    '52w_low': 1%
}
```

**Note:** Tolerances account for legitimate methodology differences between data providers (e.g., fiscal year YoY vs TTM for revenue growth).

---

## Known Limitations

### Data Limitations

1. **Price delay** - 15-30 minute delay (acceptable for swing trading)
2. **AlphaVantage free tier** - 25 calls/day (4h cache mitigates this)
3. **TwelveData free tier** - 800 credits/day, 8/min (sufficient for ~100 tickers/day)
4. **Field-level gaps** - Some fundamental fields may come from fallback providers
5. **Alpha Vantage free tier** - 25 calls/day; news sentiment cache (4h TTL) is mandatory

### S&R Engine

1. **100% detection rate** - Agglomerative clustering finds levels for all stocks
2. **Multi-timeframe confluence** - ~27% of levels confirmed by weekly data
3. **Touch-based scoring** - Levels ranked by historical significance
4. **Fibonacci extensions** - Available for ATH stocks

### Validation Methodology Differences

1. **Debt/Equity** - Different providers use total debt vs long-term only (30-50% variance)
2. **Revenue Growth** - Fiscal YoY vs TTM differences between sources (60-85% variance)
3. **These are not bugs** - Different valid calculation methods

### Known Open Issues (current, see `docs/claude/versioned/KNOWN_ISSUES_DAY93.md`)

1. **Backtest↔Live Fundamentals Mismatch** (Medium) - 40% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) fundamentals labels. Mitigation choice still pending.
2. **Volume confirmation missing from the decision engine** (Low) - Neither the Full Analysis verdict nor the Simple Checklist check whether a price move is confirmed by rising volume vs. thin volume. Deferred pending a re-backtest, since it touches frozen verdict logic.

### Deferred Features

| Feature | Reason for Deferral |
|---------|---------------------|
| TradingView Lightweight Charts (Price Structure Phase 3) | Queued behind the paper-trading confirmation freeze |
| Canadian Analyze Page | Scan works; full analysis needs data source redesign |
| Candlestick Patterns | 4 viable patterns identified by research (Day 63) — deferred for implementation effort (needs pure-NumPy port, TA-Lib not installed), not accuracy concerns |

---

## Roadmap

### Completed ✅

- v1.0: Single stock analysis, 75-point scoring
- v1.1: TradingView screener integration
- v1.2: S&R Engine with trade setups
- v1.3: Validation Engine with UI
- v2.0: Score breakdown with explanations
- v2.5: Trade viability display
- v2.9: Simplified Binary Scoring (4→9 criteria, Day 60)
- v3.0: Settings tab + Position Sizing Calculator
- v3.1: Auto-fill integration (Analysis → Position Calculator)
- v3.2: Session refresh, position controls (max position, manual override)
- v3.3: Agglomerative S&R clustering (100% detection rate)
- v3.4: Multi-timeframe confluence, fundamentals transparency
- v3.5: SQLite persistent cache (5.5x speedup)
- v3.6: start.sh/stop.sh service management scripts
- v3.7: Data Sources tab (full transparency UI)
- v3.8: Dual Entry Strategy UI (Conservative vs Aggressive)
- v3.9: Validation tolerances fixed (92.3% quality), VIX real-time fix
- **v4.2: Pattern Detection** ✅ VCP, cup-and-handle, flat base detection + Minervini Trend Template
- **v4.4: Sentiment Integration** ✅ CNN Fear & Greed Index (real data, free API)
- **v4.5: Categorical Assessment** ✅ Replaced 75-point scoring with Strong/Decent/Weak categories
- **v4.7: Forward Testing UI** ✅ Paper trading with R-multiple tracking and Van Tharp statistics
- **v4.9: Enhanced Volume** ✅ OBV indicator + divergence detection + enhanced RVOL
- **v4.10: Earnings Warning** ✅ Flags stocks with earnings within 7 days
- **v4.13: Holding Period Selector** ✅ Quick/Standard/Position with signal weighting
- **v4.14: Multi-Source Data** ✅ 5 providers with automatic fallback chains
- **v4.15: Decision Matrix** ✅ 3-step synthesis: Should I Trade? → When Enter? → Does Math Work?
- **v4.16: Holistic 3-Layer Backtest** ✅ 60 tickers, statistically significant edge (p=0.002)
- **v4.17: Production Coherence** ✅ Bear regime filter, threshold sync, 5th filter redesign
- **v4.18: Index Filters** ✅ S&P 500 / NASDAQ 100 / Dow 30 scan filters (Day 56)
- **v4.19: Sector Rotation Phase 1** ✅ RS ranking, RRG quadrant, badge + scan column (Day 58)
- **v4.20: Cache Freshness Meter** ✅ Freshness endpoint + UI dots (Day 59)
- **v4.21: Canadian Market (Scan)** ✅ TSX 60 + All Canadian scan (Day 59)
- **v4.22: 9-Criteria Checklist + Growth Fix** ✅ Simple Checklist 4→9 criteria, EPS/Revenue YoY fix (Day 60)
- **v4.24: Sector Rotation Phase 2 + Context Tab** ✅ Dedicated Sectors tab, FRED macro, news sentiment (Day 62)
- **v4.27: Deep Audit + 18 Bug Fixes** ✅ VCP, ATR, W-FRI, stops, patterns, labels, constants (Day 64)
- **v4.30: Universal Principles Tier 0-1** ✅ 4-LLM audit, bug fixes, ATR-primary stops, parameter stability (Day 69)
- **v4.31: Universal Principles Tier 2-3** ✅ VIX position sizing, blended RS (info), MR engine (Day 70)
- **v4.32: Simplicity Premium** ✅ Sentiment info-only, progressive disclosure, cap-aware checklist (Day 70B)
- **v4.37: Fable Remediation + Breakout Wiring** ✅ MR transaction costs + gap-aware fills, backtest statistics overhaul, JS↔Python verdict parity fix (86,400-combo grid), fundamentals mismatch measured, breakout classification engine wired (`/api/breakout/<ticker>`) (Day 78-79)
- **v4.38: Survivorship-Free Re-Validation + Paper-Trading Instrumentation** ✅ Fable Remediation Plan complete (all 5 phases): unbiased-universe backtest (Config C PF 1.61→1.40), one-time MR liquidity re-test (PF 0.99→1.16), entry-slippage + regime-snapshot logging in Forward Test tab (Day 79-80)
- **v4.39: Automated Paper Trading Engine** ✅ Unattended daily job takes every qualifying signal with zero human filtering (removes selection bias); shared TradingView query + `live_mode` exit replay prevent backtest/live drift (Day 81)
- **v4.41: Breakout Enhancement Plan + Fable Hygiene Audit** ✅ Breakout badge column + `/api/breakout/batch` + `/breakout-watch` skill; process/hygiene audit fixed 2 git risk items and deleted ~20 dead files (Day 82)
- **v4.42: Data-Source Reliability + BottomLineCard Removal** ✅ 5 data-source bugs fixed, cross-process rate-limiter/circuit-breaker state shared via SQLite; redundant Bottom Line Card removed, breakout status added to Analyze page (Day 83)
- **v4.43: UI Code Quality Fix Plan** ✅ 3 Fable audits (Analyze page cards, Scan tab, Tradier eval) synthesized and fully executed — 6 real bugs, 6 DRY-violation cleanups, dead-code removal, a new Tradier data provider (3rd-tier OHLCV/quote fallback), and UI polish, all browser-verified (Day 82-83)
- **v4.44: Master Framework Watchlist** ✅ 76-ticker Scan tab preset sourced from the user's Notion investment research (AI Supply Chain, CanGem, STRATUM, QUBIT frameworks); `/api/sr/<ticker>` gained free `volume`/`change` fields after live testing found a summary-table gap (Day 85-86)
- **v4.45: Breakout Enhancement Plan Complete + N4 Market Phase + Price Structure Phase 2** ✅ "Near Breakout" scan preset (Stage-2 stocks within 8% of 52W high) completes the whole Breakout plan; market-wide phase classifier (Bull Rally/Late Bull/Distribution/Correction/Recovery) added to the Context tab; HH/HL/LH/LL structure classification added to the Price Structure Card (Day 87)
- **v4.46: Paper Trading Ledger Surfaced in UI** ✅ New status panel + manual "Force Run Now" trigger in the Forward Test tab for the automated paper-trading engine (previously CLI-only) — a scoped exception to the freeze since it directly aids the paper-trading gate itself (Day 88)
- **v4.47: MR Universe Widened** ✅ Mean-reversion's live signal universe widened from a static 54-ticker list to a dynamic ~150-ticker TradingView scan for faster sample accumulation (8 signals in one test run vs. 0-2/day historically) (Day 89)
- **v4.48: Session 28 Audit Triage** ✅ Fixed 4 top-priority findings from a hub-side audit — Scan tab mislabel, Sectors tab false claims, Context tab CPI date-alignment bug, paper-trading exit-rule integrity (replay now anchors to stored entry values) (Day 91)
- **v4.49: Paper-Trading Bug Fix + Per-Ticker UI** ✅ Fixed a real bug where a signal's date could be stamped from the wall clock instead of the trading day it came from, permanently stranding it (momentum jumped from 3 to 10 open positions on repair); `/api/paper-trading/status` now surfaces per-ticker entry/exit detail in the Forward Test tab. Confirmation bar raised from 50 to 100 trades/system (Day 92)
- **v4.50: Sectors/Context Tab Audit + Cross-Tab Connection** ✅ Independent of the paper-trading freeze (pure display/UI logic): fixed a mid-cap-blind rotation banner, a bar-color/label contradiction, and redesigned the Sectors tab's CTA/card layout for beginner interpretability; fixed a real Day-91 regression in the Context tab's economic composite box and a Seasonal Regime text/badge contradiction; built a new `macro_alignment` connection so the Sectors tab states whether the macro backdrop supports the rotation it's showing, plus a Market-Phase↔Macro-Regime reconciliation on the Context tab itself (Day 93)
- **v4.51: Sector Rotation Error-Handling + README Audit** ✅ Fixed a silent-failure bug on the Sectors tab (visible error banner + Retry instead of an endless spinner); ran the project's first full README Coherence Audit, fixing ~50 findings including fictional API endpoints and undocumented real ones (Day 94)
- **v4.52: Provider Reliability Overhaul + Path B Forward-Test Experiment** ✅ Fixed a systemic bug where every data provider's circuit breaker miscounted a ticker having no data as the provider itself being unhealthy (all 6 providers). Discovered the live momentum engine's R:R check had never matched the real backtested entry logic (a live/backtest divergence since Day 81) — fixed by launching **Path B**, a parallel forward-test experiment using the actual validated support/resistance-based R:R gate, visible in its own Forward Test tab card, tracked completely independently of the original ("Path A") system's count (Day 95-96)

### Philosophy (Day 27 + Day 44 Update)

Original roadmap focused on improving **win rate** through better signals.
After backtesting, we learned:
- Entry signals = ~10% of results
- Position sizing = ~90% of results
- **Score-to-return correlation = 0.011** (essentially ZERO)

**Day 44 Response:** Replaced 75-point numerical scoring with categorical assessments (Strong/Decent/Weak). The system works as a FILTER, not a RANKER — categorical assessments honestly represent this reality.

Current focus:
- **Better R:R** through dual entry strategy
- **Categorical filtering** over numerical ranking
- **System measurement** through forward testing and SQN tracking

### Current Priorities (Day 92-96 — forward-testing accumulation is the sole priority)

A full-system audit (Day 78) found the backtested edge was likely overstated — survivorship bias in the test universe and a reused walk-forward window. The resulting remediation plan is **fully complete (all 5 phases)**, and an automated paper-trading engine (Day 81) now runs daily, unattended, taking every qualifying signal with zero human filtering — this is the real test for both systems now, and it's been running since Day 81.

**Where the two trading systems stand:** momentum (Config C) re-validated at PF 1.40 (was 1.61 on the hand-picked universe) — real but not yet statistically significant. Mean-reversion's one-time, pre-committed liquidity restriction recovered PF 1.16 from an initial clean null (PF 0.99) — also real but not yet significant. **Both systems require live paper-trading confirmation (100+ trades each, raised from 50 on Day 92) before any capital allocation.** As of Day 92: momentum 0 closed / 10 open, MR 5 closed / 8 open — both far from the bar.

**Day 87: the Breakout Enhancement Plan, N4 Market Phase Synthesis, and Price Structure Card Phase 2 all shipped**, clearing the last of the backlog that could reasonably be closed out — see v4.45 above. Two remaining backlog items (Value Tab Phase 2, N3 gap-fill detection) were scoped and explicitly deferred rather than built: both need their own design/infrastructure work first, not just implementation (see Known Issues). **A complete feature freeze is now in effect** — bug fixes and paper-trading monitoring only, until live trades confirm the momentum/MR edges.

**Day 88-89: two scoped exceptions to the freeze** — the paper-trading ledger surfaced in the Forward Test tab with a manual "Force Run Now" trigger (Day 88), and the MR arm's live signal universe widened from a static 54-ticker list to a dynamic ~150-ticker TradingView scan for faster sample accumulation (Day 89). Both agreed narrowly because they directly aid observing/operating the paper-trading gate itself.

**Day 91: a hub-side audit's top-4 findings fixed** — a scan-tab mislabel, false claims on the Sectors tab, a real date-alignment bug in the Context tab's CPI card, and a paper-trading exit-rule integrity fix (daily replay now anchors to stored entry values instead of recomputing fresh).

**Day 92: found and fixed a real paper-trading bug, then the user raised the bar.** A signal's `signal_date` could be stamped from the wall clock instead of the trading day it actually came from — a weekend/off-hours run permanently stranded 8 of momentum's 11 pending signals with no visible error. Fixed and repaired; momentum jumped from 3 to 10 open positions in one run. Per-ticker entry/exit detail was also added to the Forward Test tab's panel. **The user then explicitly raised the confirmation bar from 50 to 100 trades per system and named forward-testing accumulation the sole priority** — everything below is parked until it clears.

**Day 95-96: a data-reliability overhaul, and a real discovery about the momentum engine itself.** Every one of the 6 data providers' circuit breakers was miscounting a ticker simply having no data as evidence the whole provider was unhealthy — a couple of unlucky misses could take a perfectly healthy provider out of rotation for everyone else mid-scan; fixed across all 6. Separately, investigating why so few momentum candidates were qualifying led to a genuine finding: the live engine's R:R check had never been the same logic actually validated in the historical backtest (that real gate uses support/resistance levels, not the flat-target/ATR-clamp proxy the live engine substituted since Day 81). Rather than changing the frozen system (which would reset its count), a **parallel "Path B" experiment** now runs the real, historically-validated gate side-by-side — same daily candidates, its own independent 100-trade bar, visible as its own card in the Forward Test tab. Path A's original count and logic are completely untouched.

1. **Let paper trading accumulate — SOLE FOCUS.** Nothing else gets worked on unless explicitly raised. Check progress in the Forward Test tab's status panel (now with per-ticker detail, plus a separate Path B card), or via `daily_job.py --report`.
2. *(parked)* **Fundamentals mitigation decision** — a measured 40% disagreement between live and backtested fundamentals data sources is still pending a choice (align live-to-SimFin or backtest-to-TTM).
3. *(parked)* **Confirm SimFin key rotation** — small housekeeping item.
4. *(parked)* **N3 gap-fill detection** — needs its own design session first (no spec exists yet).
5. *(parked)* **Value Tab Phase 2** — needs its own batch-prefetch infrastructure design session first (AlphaVantage free-tier budget constraints).
6. *(parked)* **Volume confirmation missing from the decision engine** — neither the Full Analysis verdict nor the Simple Checklist check whether a price move is backed by rising volume; found Day 92, needs a re-backtest before shipping.
7. *(parked)* `/ibkr-scan` skill, Price Structure Phase 3 (visual chart), Canadian Analyze page — queued behind the above.

**Day 85-86:** Built a "🏛️ Master Framework Watchlist" Scan tab preset — 76 tickers sourced from the user's own curated Notion investment research (AI Supply Chain, CanGem, STRATUM, QUBIT frameworks), scanned with STA's existing technical engine, same pattern as the pre-existing Nirmal watchlist. First live test found the summary table's Volume/Change columns showing N/A; fixed for free by exposing data `/api/sr/<ticker>` already computed (v4.44).

---

## Project Structure

```
swing-trade-analyzer/
├── start.sh                   # Service starter script
├── stop.sh                    # Service stopper script
├── DEVELOPER_ONBOARDING.md    # New-contributor setup guide
├── backend/
│   ├── backend.py             # Flask server (BACKEND_VERSION = source of truth for version)
│   ├── cache_manager.py       # SQLite persistent cache (with source tracking)
│   ├── support_resistance.py  # S&R calculation (Agglomerative + MTF)
│   ├── pattern_detection.py   # VCP, Cup & Handle, Flat Base
│   ├── market_structure_engine.py # HH/HL/LH/LL structure classification (Day 87)
│   ├── market_phase_engine.py # N4 market-wide phase classifier (Day 87)
│   ├── mean_reversion.py      # RSI(2) mean-reversion engine (Day 69-70)
│   ├── scan_queries.py        # Shared TradingView query builder (live Scan tab + paper-trading engine)
│   ├── breakout_routes.py     # Breakout API routes
│   ├── breakout_detection.py  # 8-state breakout classifier
│   ├── constants.py           # Shared thresholds and configuration
│   ├── cycles_engine.py       # FRED macro cycles (yield curve, FOMC, seasonal)
│   ├── econ_engine.py         # FRED economic indicators (CPI, Fed funds)
│   ├── news_engine.py         # Alpha Vantage news sentiment
│   ├── .env                   # API keys (gitignored)
│   ├── .env.example           # API key template
│   ├── paper_trading/         # Automated paper-trading engine (Day 81+)
│   │   ├── ledger.py          # SQLite ledger (positions, job_runs)
│   │   ├── live_signals.py    # Live momentum + MR signal generation
│   │   └── daily_job.py       # Daily orchestrator (launchd-scheduled)
│   ├── providers/             # v4.14 Multi-Source Data Intelligence, extended Day 83
│   │   ├── __init__.py        # Exports get_data_provider()
│   │   ├── orchestrator.py    # Fallback chains + field merge
│   │   ├── base.py            # Abstract interfaces
│   │   ├── exceptions.py      # Error hierarchy
│   │   ├── field_maps.py      # Field normalization
│   │   ├── rate_limiter.py    # Token-bucket per provider
│   │   ├── circuit_breaker.py # Circuit breaker pattern (shared cross-process via SQLite, Day 83)
│   │   ├── twelvedata_provider.py  # Primary OHLCV
│   │   ├── finnhub_provider.py     # Primary Fundamentals
│   │   ├── alphavantage_provider.py # Growth metrics + News
│   │   ├── yfinance_provider.py    # Universal fallback
│   │   ├── tradier_provider.py     # 3rd-tier OHLCV/Quote fallback (Day 83)
│   │   ├── stooq_provider.py       # Inactive since Day 82 (bot-blocked), kept for status reporting
│   │   └── backtest_adapter.py     # yf.download() replacement
│   ├── backtest/              # v4.16-v4.17 Holistic Backtest System
│   │   ├── backtest_holistic.py       # Main runner (60 tickers, 3 configs)
│   │   ├── backtest_survivorship_free.py # Canonical unbiased-universe backtest (Day 79)
│   │   ├── backtest_technical.py      # Technical exit strategies
│   │   ├── backtest_simplified.py     # Simplified backtest runner
│   │   ├── backtest_adx_rsi_thresholds.py # ADX/RSI threshold validation
│   │   ├── categorical_engine.py      # Python port of categorical assessment
│   │   ├── trade_simulator.py         # Exit models + market regime (shared with live paper-trading via live_mode)
│   │   ├── mr_simulator.py            # MR exit models (shared with live paper-trading)
│   │   ├── metrics.py                 # Statistical metrics (Sharpe, Sortino, T-test)
│   │   └── simfin_loader.py           # SimFin historical fundamentals
│   ├── data/
│   │   ├── cache.db           # SQLite cache database
│   │   ├── provider_state.db  # Cross-process rate-limiter/circuit-breaker state (Day 83)
│   │   └── simfin/            # Cached SimFin historical datasets
│   ├── validation_results/
│   │   └── paper_trading_ledger.db # Paper-trading positions + job run history
│   ├── validation/
│   │   ├── engine.py          # Validation orchestrator
│   │   ├── scrapers.py        # StockAnalysis + Finviz
│   │   ├── comparators.py     # Tolerance checking
│   │   ├── forward_tracker.py # Forward test signal recording
│   │   └── report_generator.py # Validation HTML reports
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main UI — Analyze/Scan/Validate tabs live inline here, not in separate directories
│   │   ├── services/
│   │   │   └── api.js         # API client + health checks
│   │   ├── components/
│   │   │   ├── SectorRotationTab.jsx      # Sectors tab (redesigned Day 93)
│   │   │   ├── ContextTab.jsx             # Context tab
│   │   │   ├── ValueTab.jsx               # Value Investing tab (Day 75)
│   │   │   ├── MarketPhaseBanner.jsx      # N4 Market Phase banner (Day 87)
│   │   │   ├── PriceStructureCard.jsx     # Price Structure card (Day 72, 87)
│   │   │   ├── AutomatedPaperTradingPanel.jsx # Paper-trading status panel (Day 88)
│   │   │   ├── MRSignalCard.jsx           # Mean-reversion signal (Day 70)
│   │   │   ├── PatternMiniCard.jsx        # Shared pattern-detection tile
│   │   │   ├── AssessmentTile.jsx         # Shared categorical-assessment tile
│   │   │   ├── CycleCard.jsx              # Context tab card (cycles/econ)
│   │   │   ├── ArticleRow.jsx             # News article row
│   │   │   ├── RegimeBanner.jsx           # Overall macro regime banner
│   │   │   └── ConflictCheck.jsx          # Conflict/alignment banner
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System
│   │       ├── simplifiedScoring.js      # 9-criteria binary checklist
│   │       ├── priceStructureNarrative.js # Price Structure narrative generation (Day 72)
│   │       ├── alignmentStyles.js        # Shared status→color/icon map (Day 93)
│   │       ├── liquidityThresholds.js    # Unified liquidity threshold constants
│   │       ├── riskRewardCalc.js         # Shared R:R utility
│   │       ├── technicalIndicators.js    # RSI, MACD, ADX calculations
│   │       ├── scoringEngine.js          # Legacy scoring + data quality
│   │       ├── forwardTesting.js         # Manual R-multiple journal (Day 47)
│   │       ├── positionSizing.js         # Van Tharp calculator
│   │       └── rsCalculator.js           # RS calculations
│   └── package.json
│
├── docs/
│   ├── claude/                # Project development-process documentation
│   │   ├── CLAUDE_CONTEXT.md  # Single reference point
│   │   ├── stable/            # Rarely-changing docs (GOLDEN_RULES, ROADMAP, MASTER_AUDIT_FRAMEWORK)
│   │   ├── versioned/         # Day-versioned docs (API_CONTRACTS, KNOWN_ISSUES)
│   │   └── status/            # Daily status files
│   └── research/              # Research documents
│
└── README.md
```

---

## Troubleshooting

### Backend won't start
- Check that you created `backend/.env` (not just `.env.example`)
- Check that your virtual environment is activated: `source venv/bin/activate`
- Run `pip install -r requirements.txt` again if packages are missing

### "Backend Disconnected" in the UI
- Make sure `python backend.py` is running in a terminal
- Check it's on port 5001: `curl http://localhost:5001/api/health`

### Data shows "N/A" or all nulls
- Your API keys may be invalid or rate-limited
- Check `backend/backend.log` for error messages
- Try `curl http://localhost:5001/api/stock/AAPL` to see raw response
- TwelveData free tier: 800 credits/day — each OHLCV fetch uses 1 credit

### Stale prices after earnings / catalyst
- Click **Refresh Session** button (top right) — clears the SQLite cache and resets all frontend state
- Then re-analyze the ticker to fetch fresh live data

### Scan returns no results
- TradingView screener filters are strict by design; try "All US" market instead of "S&P 500"
- The scan requires no API key — it uses the `tradingview-screener` Python package

### Context tab shows no data
- Add `FRED_API_KEY` to `backend/.env` — get one free at fred.stlouisfed.org (instant, no credit card)

---

## Contributing

This is a personal project for learning and trading research. Feel free to fork and adapt for your own use.

---

## Disclaimer

**This software is for educational and research purposes only.**

- Not financial advice
- Past performance doesn't guarantee future results
- Always do your own due diligence
- Use at your own risk

---

## License

MIT License - See LICENSE file for details.

---

## Acknowledgments

- **Mark Minervini** - SEPA methodology, VCP patterns
- **William O'Neil** - CAN SLIM strategy
- **TwelveData** - Primary OHLCV data
- **Finnhub** - Primary fundamentals data
- **Alpha Vantage** - Growth metrics + News Sentiment
- **yfinance** - Universal fallback data
- **Tradier** - Last-resort OHLCV/Quote fallback
- **TradingView** - Screener library
- **FRED (St. Louis Fed)** - Macro economic data

---

*Last Updated: July 22, 2026 (Day 93)*
