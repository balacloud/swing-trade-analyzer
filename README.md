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
- **Categorical Assessment System** (v4.5) - Strong/Decent/Weak ratings across Technical, Fundamental, Sentiment, and Risk
- **BUY / HOLD / AVOID verdicts** based on categorical criteria (2+ Strong categories with favorable risk = BUY)
- **Pattern Detection** - VCP, Cup & Handle, Flat Base + Minervini Trend Template
- **Fear & Greed Index** - Real market sentiment data (replaces placeholder)
- **Trade setups** with Entry, Stop Loss, Target, and Risk/Reward ratios
- **Dual Entry Strategy** - Conservative (support) and Aggressive (current) entries
- **Relative Strength (RS)** calculations vs S&P 500
- **Batch scanning** for market opportunities (TradingView integration)
- **Data validation** against external sources (92.3% quality score)
- **Full data transparency** - see exactly where each data point comes from

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

### ✅ Implemented (v4.27)

1. **Single Stock Analysis**
   - Enter any ticker symbol
   - Get categorical assessment (Strong/Decent/Weak) across 4 dimensions
   - BUY / HOLD / AVOID verdict with detailed reasoning
   - Decision Matrix: 3-step synthesis (Should I Trade? → When Enter? → Does Math Work?)
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

6. **Market Scanning** (TradingView Screener)
   - 5 pre-built strategies: Reddit, Minervini, Momentum, Value, Best Candidates
   - **Best Candidates** aligned with backtested Config C criteria (ADX>=20, RSI 50-70, EMA momentum)
   - Market index filters: S&P 500 / NASDAQ 100 / Dow 30 / All US / TSX 60 / All Canadian
   - Stage 2 uptrend requirement (50 SMA > 200 SMA)

7. **Data Validation Engine** (Day 42)
   - Cross-references our data against StockAnalysis and Finviz
   - Quality Score = Coverage × Accuracy
   - **92.3% quality score** with methodology-aware tolerances
   - Identifies data discrepancies

8. **Multi-Source Data Intelligence** (Day 52 - v4.14)
   - **5 data providers** with automatic fallback chains
   - OHLCV: TwelveData → yfinance → Stooq
   - Fundamentals: Finnhub → FMP → yfinance (field-level merge)
   - Circuit breaker per provider (3 failures → 5min cooldown)
   - Token-bucket rate limiting per provider
   - Cache-first with stale cache fallback when all providers fail
   - Provenance tracking (which provider supplied each data field)
   - ETF detection with special handling

9. **9-Criteria Simple Checklist** (Day 27, enhanced Day 60)
    - Binary pass/fail system — ALL 9 must pass for TRADE verdict
    - **Criteria:** Trend (P>50>200 SMA), Momentum (RS>1.0), Setup (stop within 7%), Risk/Reward (R:R>=2:1), 52-Wk Range (top 25%), Volume ($10M+ daily), ADX (>=20), Market Regime (SPY>200 SMA), 200 SMA Trend (rising)
    - Based on Minervini SEPA criteria + holistic backtest validation

10. **Sector Rotation** (Day 58-62 - v4.19 → v4.24)
    - `/api/sectors/rotation` — 11 SPDR sector ETFs ranked by RS ratio vs SPY
    - RRG quadrant classification (Leading, Weakening, Lagging, Improving)
    - Color-coded sector badge on Analyze page + sector column in Scan results
    - Dedicated Sectors tab with 11 cards, rank badges, RS bars

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

14. **Decision Matrix** (Day 53 - v4.15)
    - 3-step synthesis: "Should I Trade?" → "When Enter?" → "Does Math Work?"
    - Surfaces 10 computed-but-hidden fields
    - Contradiction resolution with actionable items

15. **Holding Period Selector** (Day 53 - v4.13)
    - Quick (5-10d) / Standard (15-30d) / Position (1-3mo)
    - Signal weighting by horizon (Quick=70% Tech, Position=70% Fund)
    - Bottom Line Card with action plan summary

16. **Forward Testing / Paper Trading** (Day 47 - v4.7)
    - Add/close trades with entry, stop, target prices
    - R-multiple tracking with Van Tharp statistics (Win Rate, Expectancy, SQN)
    - Trade journal table, export to CSV, localStorage persistence

17. **Context Tab** (Day 62 - v4.24)
    - 6 calendar/yield cycle cards (Yield Curve, Business Cycle, Presidential Year, Seasonal, FOMC, Quad Witching)
    - 4 economic indicator cards (Fed Funds, CPI, PMI proxy, Unemployment) via FRED API
    - News sentiment + short interest per ticker via Alpha Vantage
    - Overall macro regime across 10 indicators + options block detection
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
│  │ - Decision  │  │ - Quick     │  │ - Quality metrics       │  │
│  │   Matrix    │  │   Analyze   │  │                         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
│                                                                  │
│  ┌─────────────────┐  ┌───────────────┐  ┌──────────────────┐   │
│  │ Data Sources Tab │  │ Forward Test  │  │   Settings Tab   │   │
│  │                  │  │               │  │                  │   │
│  │ - Provenance     │  │ - Paper trade │  │ - Account size   │   │
│  │ - Cache status   │  │ - R-multiples │  │ - Risk %         │   │
│  │ - Transparency   │  │ - Van Tharp   │  │ - Position limits│   │
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
│  │                 API ENDPOINTS (22+ routes)              │    │
│  │                                                         │    │
│  │  Core Analysis:                                         │    │
│  │  /api/stock/<ticker>        - Price data, basic info    │    │
│  │  /api/fundamentals/<ticker> - Fundamental data          │    │
│  │  /api/sr/<ticker>           - Support & Resistance      │    │
│  │  /api/patterns/<ticker>     - VCP, Cup&Handle, FlatBase │    │
│  │  /api/earnings/<ticker>     - Earnings calendar warning │    │
│  │                                                         │    │
│  │  Market Data:                                           │    │
│  │  /api/market/spy   /api/market/vix   /api/fear-greed    │    │
│  │  /api/sectors/rotation  - 11 sector RS ranking          │    │
│  │                                                         │    │
│  │  Context (FRED + Alpha Vantage):                        │    │
│  │  /api/cycles  /api/econ  /api/news/<ticker>             │    │
│  │  /api/context/<ticker>  - aggregated macro regime       │    │
│  │                                                         │    │
│  │  Scanning & Forward Test:                               │    │
│  │  /api/scan/tradingview     /api/scan/strategies         │    │
│  │  /api/forward-test/record  /signals  /performance       │    │
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
│  │ 5 data sources │  │ engine, scrapers│  │ news_engine     │   │
│  │ + orchestrator │  │ forward_tracker │  │ (FRED + AV)     │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  TwelveData  │  │   Finnhub    │  │     FMP      │           │
│  │              │  │              │  │              │           │
│  │ - OHLCV      │  │ - ROE, ROA   │  │ - EPS Growth │           │
│  │ - Intraday   │  │ - PE, Margins│  │ - Rev Growth │           │
│  │ 8/min limit  │  │ - D/E, Beta  │  │ 250/day      │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │   yfinance   │  │    Stooq     │  │  TradingView │           │
│  │  (fallback)  │  │ (last resort)│  │   Screener   │           │
│  │ - All data   │  │ - OHLCV only │  │ - Batch scans│           │
│  │ 15-30m delay │  │ No API key   │  │ - Real-time  │           │
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
        ├──► /api/stock/AAPL ──────► TwelveData → yfinance → Stooq
        ├──► /api/fundamentals/AAPL ► Finnhub → FMP → yfinance (merge)
        ├──► /api/market/spy ──────► TwelveData → yfinance (for RS)
        ├──► /api/market/vix ──────► yfinance → Finnhub (VIX)
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
│ Decision Matrix +         │
│ Dual Entry Cards +        │
│ Bottom Line Summary       │
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
| **Risk/Macro** | Favorable / Neutral / Unfavorable | VIX level, SPY regime (above 200 EMA) |

#### Technical Assessment Thresholds

| Level | Criteria |
|-------|----------|
| **Strong** | Trend Template >= 7/8 AND RSI 50-70 AND RS >= 1.0 |
| **Decent** | Trend Template >= 5/8 AND RSI 40-80 |
| **Weak** | Below thresholds, extreme RSI, or RS < 0.8 |

#### Fundamental Assessment Thresholds

| Level | Criteria |
|-------|----------|
| **Strong** | ROE > 15% AND Revenue Growth > 10% AND D/E < 1.0 |
| **Decent** | ROE 8-15% OR Revenue Growth 0-10% OR D/E 1.0-2.0 |
| **Weak** | ROE < 8% OR negative growth OR D/E > 2.0 |

### Verdict Logic

| Verdict | Conditions |
|---------|------------|
| **BUY** | 2+ Strong categories + Favorable/Neutral risk + ADX >= 20 |
| **HOLD** | Mixed signals, ADX < 20 (no trend), or Unfavorable risk |
| **AVOID** | Weak Technical (non-negotiable) OR 2+ Weak categories |

### Additional Filters

- **ADX < 20** = HOLD regardless of other signals (no trend to trade)
- **Pattern confidence >= 60%** = actionable (backtested threshold)
- **Holding period weighting**: Quick = 70% Technical, Position = 70% Fundamental
- **Bear market regime**: SPY 50 SMA declining caps risk at "Neutral"

### Backtest Validation (v4.16, Day 55)

| Config | Trades | Win Rate | Profit Factor | Sharpe | p-value |
|--------|--------|----------|---------------|--------|---------|
| A (Categorical only) | 1,108 | 51.53% | 1.41 | — | <0.000001 |
| B (A + Patterns) | 406 | 51.72% | 1.43 | — | 0.002 |
| C (Full 3-layer) | 238 | 53.78% | 1.61 | 0.85 | 0.002 |

Walk-forward validation: Out-of-sample outperforms in-sample — system is NOT overfitted.

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
- **Multi-Source Provider System** (v4.14):
  - **TwelveData** - Primary OHLCV + Intraday
  - **Finnhub** - Primary Fundamentals + Quote
  - **FMP** - Growth metrics (epsGrowth, revenueGrowth)
  - **yfinance** - Universal fallback
  - **Stooq** (pandas_datareader) - Last resort OHLCV
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
| FMP | Growth metrics | 10/min, 250/day | Fundamentals backup |
| yfinance | All types | ~30/min | Universal fallback |
| Stooq | OHLCV only | ~5/min | Last resort OHLCV |
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
| `FMP_API_KEY` | [financialmodelingprep.com](https://financialmodelingprep.com) → Get API Key | 250 calls/day |

### Optional (graceful degradation if not set)

| Variable | Where to Get It | Without It |
|----------|----------------|------------|
| `FRED_API_KEY` | [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) — instant, no credit card | Context tab shows no macro data |
| `ALPHA_VANTAGE_API_KEY` | [alphavantage.co](https://www.alphavantage.co/support/#api-key) | News column shows empty state |

> **Without FMP_API_KEY:** EPS growth and revenue growth fall back to yfinance data.

### Example `.env` file

```env
# Required
TWELVEDATA_API_KEY=your_twelvedata_key_here
FINNHUB_API_KEY=your_finnhub_key_here
FMP_API_KEY=your_fmp_key_here

# Optional
FRED_API_KEY=your_fred_key_here
ALPHA_VANTAGE_API_KEY=your_alphavantage_key_here
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
3. Select holding period: Quick (5-10d) / Standard (15-30d) / Position (1-3mo)
4. Click "Analyze" or press Enter
5. View results:
   - Verdict (BUY/HOLD/AVOID) with categorical assessment
   - Decision Matrix (3-step trade evaluation)
   - **Dual Entry Strategy cards** (Conservative vs Aggressive)
   - Trade setup (Entry/Stop/Target)
   - Pattern detection and volume analysis

### Scan for Opportunities

1. Click "Scan Market" tab
2. Select strategy:
   - **Reddit**: Mid-cap+, high relative volume
   - **Minervini**: Large-cap momentum leaders
   - **Momentum**: Sustainable 5-50% monthly gains
   - **Value**: Quality at fair price (P/E 5-25)
   - **Best Candidates**: Backtested Config C picks (ADX>=20, RSI 50-70, EMA momentum)
3. Select index (S&P 500, NASDAQ 100, Dow 30, All US)
4. Click "Scan for Opportunities"
5. Click any result to run full analysis

### Sector Rotation

1. Click **Sectors** tab to see all 11 SPDR sector ETFs ranked by Relative Strength vs SPY
2. Quadrant classification: Leading / Improving / Weakening / Lagging
3. Click "Scan for Rank #1 Sector" to filter scan results to the top sector

### Context Tab (Macro Pre-Flight)

1. Click **Context** tab
2. Columns A+B load automatically (FRED data — no ticker needed)
3. Search a ticker on Analyze tab → Column C populates with news sentiment

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

Click **Forward Test** tab to record paper trades. Track R-multiples, win rate, and expectancy using Van Tharp's SQN framework.

---

## API Reference

### GET /api/health

Returns backend health status including multi-source provider information.

```json
{
  "status": "healthy",
  "version": "2.30",
  "data_provider_available": true,
  "providers": {
    "providers": {
      "twelvedata": {"configured": true, "type": "OHLCV + Intraday"},
      "finnhub": {"configured": true, "type": "Fundamentals + Quote"},
      "fmp": {"configured": true, "type": "Fundamentals (growth)"},
      "yfinance": {"configured": true, "type": "All (fallback)"},
      "stooq": {"configured": true, "type": "OHLCV (last resort)"}
    }
  }
}
```

### GET /api/stock/\<ticker\>

Returns price data and basic info.

```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "currentPrice": 272.97,
  "fiftyTwoWeekHigh": 288.62,
  "fiftyTwoWeekLow": 169.21,
  "avgVolume": 48123456,
  "priceHistory": [...],
  "fundamentals": {...}
}
```

### GET /api/fundamentals/\<ticker\>

Returns fundamental data with multi-source fallback (Finnhub → FMP → yfinance).

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
    "epsGrowth": "fmp",
    "revenueGrowth": "fmp"
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
      "epsGrowth": {"source": "fmp", "formula": "(Current EPS - Previous EPS) / Previous EPS"}
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

Batch scan for opportunities.

```
GET /api/scan/tradingview?strategy=reddit&limit=50
```

```json
{
  "strategy": "reddit",
  "totalMatches": 847,
  "returned": 50,
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

Returns 11 SPDR sector ETFs ranked by RS ratio vs SPY with RRG quadrant classification.

```json
{
  "sectors": [
    {
      "etf": "XLK",
      "name": "Technology",
      "rsRatio": 1.05,
      "rsMomentum": 0.02,
      "quadrant": "Leading",
      "weekChange": 2.1,
      "monthChange": 5.3
    }
  ],
  "mapping": {
    "Technology": "XLK",
    "Information Technology": "XLK",
    "Financials": "XLF"
  }
}
```

**Quadrants:** Leading (RS>1 + rising), Weakening (RS>1 + falling), Lagging (RS<1 + falling), Improving (RS<1 + rising)

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

Returns news sentiment + short interest. Requires `ALPHA_VANTAGE_API_KEY`. Cached 4h.

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
    {"id": "minervini", "name": "Minervini SEPA", "description": "Large-cap momentum leaders in Stage 2 uptrend"},
    {"id": "momentum", "name": "Momentum", "description": "Sustainable gains, RSI 50-75 (not overbought)"},
    {"id": "value", "name": "Value", "description": "Quality stocks above 200 SMA at fair RSI levels"},
    {"id": "best", "name": "Best Candidates", "description": "Stage 2 + ADX≥20 + RSI 50-70 + EMA momentum"}
  ]
}
```

### POST /api/forward-test/record

Record a trading signal for forward testing / paper trading.

```json
// Request
{
  "ticker": "AAPL",
  "signal_type": "BUY",
  "score": 65,
  "price_at_signal": 250.00,
  "entry_price": 245.00,
  "stop_price": 238.00,
  "target_price": 270.00,
  "risk_reward": 3.57
}

// Response
{"success": true, "signal_id": "abc123", "message": "Recorded BUY signal for AAPL"}
```

### GET /api/forward-test/signals

Get recent forward test signals. Params: `?days=30&limit=50&ticker=AAPL`

### GET /api/forward-test/performance

Get forward test performance summary (win rate, avg P&L, signal count).

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

### Multi-Source Provider System (v4.14)

STA uses a multi-source data architecture with automatic fallback chains, eliminating single-point-of-failure dependency on any one provider.

### TwelveData (Primary - OHLCV)

- **What:** Daily OHLCV price data, intraday data (for 4H RSI)
- **Rate Limit:** 8 requests/min, 800/day (free tier)
- **API Key:** Required (`TWELVEDATA_API_KEY` in `.env`)
- **Reliability:** High, official API

### Finnhub (Primary - Fundamentals)

- **What:** PE, ROE, ROA, Debt/Equity, Profit Margin, Beta, Current Ratio
- **Rate Limit:** 60 requests/min (free tier, unlimited daily)
- **API Key:** Required (`FINNHUB_API_KEY` in `.env`)
- **Note:** Lacks epsGrowth and revenueGrowth — filled by FMP

### FMP (Backup - Growth Metrics)

- **What:** EPS Growth, Revenue Growth (fills Finnhub gaps)
- **Rate Limit:** 10/min, 250/day (free tier)
- **API Key:** Required (`FMP_API_KEY` in `.env`)

### yfinance (Universal Fallback)

- **What:** All data types (prices, fundamentals, earnings, stock info)
- **Rate Limit:** Self-imposed 30/min
- **API Key:** None (unofficial Yahoo Finance scraper)
- **Reliability:** Variable — subject to Yahoo throttling/blocking

### Stooq (Last Resort - OHLCV)

- **What:** Daily OHLCV only via pandas_datareader
- **Rate Limit:** Self-imposed 5/min
- **API Key:** None
- **Note:** Optional dependency, graceful if not installed

### Field-Level Merge Strategy

```python
# Finnhub provides most fundamental fields
# FMP fills growth gaps (epsGrowth, revenueGrowth)
# yfinance fills any remaining gaps
# Result includes _field_sources for transparency
merged = {
    "pe": "finnhub",
    "roe": "finnhub",
    "epsGrowth": "fmp",        # Finnhub lacks this
    "revenueGrowth": "fmp",    # Finnhub lacks this
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

### Tolerances (Day 42 - Methodology-Aware)

```python
TOLERANCES = {
    'price': 2%,
    'pe_ratio': 10%,
    'roe': 20%,           # Increased for methodology differences
    'revenue_growth': 50%, # Fiscal YoY vs TTM differences
    'debt_equity': 40%,    # Total debt vs long-term only
    '52w_high': 1%,
    '52w_low': 1%
}
```

**Note:** Tolerances account for legitimate methodology differences between data providers (e.g., fiscal year YoY vs TTM for revenue growth).

---

## Known Limitations

### Data Limitations

1. **Price delay** - 15-30 minute delay (acceptable for swing trading)
2. **FMP free tier** - 250 calls/day, may return 403 on some tickers
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

### Deferred Features

| Feature | Reason for Deferral |
|---------|---------------------|
| TradingView Lightweight Charts | After backtest validation |
| Canadian Analyze Page | Scan works; full analysis needs data source redesign |
| Candlestick Patterns | Low statistical accuracy |

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

---

## Project Structure

```
swing-trade-analyzer/
├── start.sh                   # Service starter script
├── stop.sh                    # Service stopper script
├── backend/
│   ├── backend.py             # Flask server (v2.30)
│   ├── cache_manager.py       # SQLite persistent cache (with source tracking)
│   ├── support_resistance.py  # S&R calculation (Agglomerative + MTF)
│   ├── pattern_detection.py   # VCP, Cup & Handle, Flat Base
│   ├── constants.py           # Shared thresholds and configuration
│   ├── cycles_engine.py       # FRED macro cycles (yield curve, FOMC, seasonal)
│   ├── econ_engine.py         # FRED economic indicators (CPI, Fed funds)
│   ├── news_engine.py         # Alpha Vantage news sentiment
│   ├── .env                   # API keys (gitignored)
│   ├── .env.example           # API key template
│   ├── providers/             # v4.14 Multi-Source Data Intelligence
│   │   ├── __init__.py        # Exports get_data_provider()
│   │   ├── orchestrator.py    # Fallback chains + field merge
│   │   ├── base.py            # Abstract interfaces
│   │   ├── exceptions.py      # Error hierarchy
│   │   ├── field_maps.py      # Field normalization
│   │   ├── rate_limiter.py    # Token-bucket per provider
│   │   ├── circuit_breaker.py # Circuit breaker pattern
│   │   ├── twelvedata_provider.py  # Primary OHLCV
│   │   ├── finnhub_provider.py     # Primary Fundamentals
│   │   ├── fmp_provider.py         # Growth metrics
│   │   ├── yfinance_provider.py    # Universal fallback
│   │   ├── stooq_provider.py       # Last resort OHLCV
│   │   └── backtest_adapter.py     # yf.download() replacement
│   ├── backtest/              # v4.16-v4.17 Holistic Backtest System
│   │   ├── backtest_holistic.py       # Main runner (60 tickers, 3 configs)
│   │   ├── backtest_technical.py      # Technical exit strategies
│   │   ├── backtest_simplified.py     # Simplified backtest runner
│   │   ├── backtest_adx_rsi_thresholds.py # ADX/RSI threshold validation
│   │   ├── categorical_engine.py      # Python port of categorical assessment
│   │   ├── trade_simulator.py         # Exit models + market regime
│   │   ├── metrics.py                 # Statistical metrics (Sharpe, Sortino, T-test)
│   │   └── simfin_loader.py           # SimFin historical fundamentals
│   ├── data/
│   │   ├── cache.db           # SQLite cache database
│   │   └── simfin/            # Cached SimFin historical datasets
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
│   │   ├── App.jsx            # Main UI (v4.14)
│   │   ├── services/
│   │   │   └── api.js         # API client + health checks (v2.9)
│   │   ├── components/
│   │   │   ├── AnalyzeTab/
│   │   │   ├── ScanTab/
│   │   │   ├── SectorRotationTab/
│   │   │   ├── ContextTab/
│   │   │   ├── DecisionMatrix.jsx        # v4.15 3-step decision synthesis
│   │   │   ├── BottomLineCard.jsx        # v4.13 Action plan summary
│   │   │   ├── CycleCard.jsx             # Context tab card (Column A+B)
│   │   │   ├── ArticleRow.jsx            # News article row
│   │   │   ├── RegimeBanner.jsx          # Overall macro regime banner
│   │   │   └── ConflictCheck.jsx         # Conflict/alignment banner
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System
│   │       ├── simplifiedScoring.js      # 9-criteria binary checklist
│   │       ├── riskRewardCalc.js         # Shared R:R utility
│   │       ├── technicalIndicators.js    # RSI, MACD, ADX calculations
│   │       ├── scoringEngine.js          # Legacy scoring + data quality
│   │       ├── forwardTesting.js         # Paper trading (v4.7)
│   │       ├── positionSizing.js         # Van Tharp calculator
│   │       └── rsCalculator.js           # RS calculations
│   └── package.json
│
├── docs/
│   ├── claude/                # Claude session documentation
│   │   ├── CLAUDE_CONTEXT.md  # Single reference point
│   │   ├── stable/            # Rarely-changing docs (GOLDEN_RULES, ROADMAP)
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
- **Financial Modeling Prep (FMP)** - Growth metrics
- **yfinance** - Universal fallback data
- **TradingView** - Screener library
- **FRED (St. Louis Fed)** - Macro economic data
- **Alpha Vantage** - News sentiment data

---

*Last Updated: March 6, 2026 (Day 65)*
