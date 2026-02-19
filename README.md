# 🎯 Swing Trade Analyzer

An institutional-grade stock analysis system for swing traders, built on proven methodologies from **Mark Minervini's SEPA** (Specific Entry Point Analysis) and **William O'Neil's CAN SLIM** approach.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Scoring Methodology](#scoring-methodology)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Data Sources](#data-sources)
- [Validation System](#validation-system)
- [Known Limitations](#known-limitations)
- [Roadmap](#roadmap)

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
| Hold Period | 1-2 months |
| Target Returns | 10-20% per trade (2-3R) |
| Position Risk | 2-5% of account per trade |
| Risk/Reward | Minimum 2:1 required |

> **Day 27 Critical Insight:** Backtesting revealed score-to-return correlation = 0.011 (essentially ZERO). Entry signals account for only ~10% of trading results, while position sizing accounts for ~90%.
>
> **Day 44 Response (v4.5):** Replaced 75-point numerical scoring with categorical assessments (Strong/Decent/Weak). The system works as a FILTER, not a RANKER. Categorical assessments honestly represent this reality and eliminate false precision.

---

## Features

### ✅ Implemented (v4.17)

1. **Single Stock Analysis**
   - Enter any ticker symbol
   - Get categorical assessment (Strong/Decent/Weak) across 4 dimensions
   - BUY / HOLD / AVOID verdict with detailed reasoning
   - Decision Matrix: 3-step synthesis (Should I Trade? → When Enter? → Does Math Work?)
   - Holding period selector: Quick (5-10d) / Standard (15-30d) / Position (1-3mo)

3. **Position Sizing Calculator** (Day 28-29)
   - Van Tharp R-multiple principles
   - Configurable account size and risk % (2-5%)
   - Auto-calculates shares, R targets (1.5R, 2R, 3R)
   - Auto-fill from stock analysis
   - Manual override for custom entry/stop prices
   - Max position limit to prevent over-allocation

4. **Advanced S&R Detection** (Day 31-34)
   - **Agglomerative Clustering** - Adaptive cluster count (replaced KMeans)
   - **ZigZag Pivot Detection** - 5% minimum price change threshold
   - **Touch-based Scoring** - Levels ranked by historical touches
   - **Multi-Timeframe Confluence** - Daily + Weekly S&R alignment
   - **Fibonacci Extensions** - For stocks at all-time highs
   - 100% detection rate (was 80% with KMeans)
   - Confluence badge shows % of levels confirmed by weekly data

5. **Dual Entry Strategy** (Day 39-40) ⭐ NEW
   - **Conservative Entry** - Wait for pullback to support
   - **Aggressive Entry** - Enter at current price
   - Side-by-side comparison cards for ALL stocks
   - Shows R:R ratio, ADX trend strength, 4H RSI confirmation
   - Structural stop loss (below support) for both strategies

6. **Trade Setup Generation**
   - Support & Resistance detection (Pivot → Agglomerative → Volume Profile)
   - Suggested Entry, Stop Loss, Target
   - Risk/Reward ratio calculation
   - Pullback re-entry zones for extended stocks
   - **MTF Confluence indicators** (★ marks confluent levels)

7. **Market Scanning** (TradingView Screener)
   - 5 pre-built strategies: Reddit, Minervini, Momentum, Value, Best Candidates
   - **Best Candidates** aligned with backtested Config C criteria (ADX>=20, RSI 50-70, EMA momentum)
   - Filters for institutional-quality stocks
   - Stage 2 uptrend requirement (50 SMA > 200 SMA)

8. **Data Validation Engine** (Day 42 - Enhanced)
   - Cross-references our data against StockAnalysis and Finviz
   - Quality Score = Coverage × Accuracy
   - **92.3% quality score** with methodology-aware tolerances
   - Identifies data discrepancies

9. **Multi-Source Data Intelligence** (Day 52 - v4.14)
   - **5 data providers** with automatic fallback chains
   - OHLCV: TwelveData → yfinance → Stooq
   - Fundamentals: Finnhub → FMP → yfinance (field-level merge)
   - Circuit breaker per provider (3 failures → 5min cooldown)
   - Token-bucket rate limiting per provider
   - Cache-first with stale cache fallback when all providers fail
   - Provenance tracking (which provider supplied each data field)
   - ETF detection with special handling

10. **SQLite Persistent Cache** (Day 37) ⭐ NEW
    - 5.5x performance improvement
    - OHLCV cache with market-aware TTL (expires after market close)
    - Fundamentals cache with 7-day TTL
    - Survives backend restarts
    - Cache status endpoint for monitoring

11. **Data Sources Tab** (Day 38)
    - Full transparency on data provenance
    - Shows which provider supplied each data field
    - Cache hit/miss status
    - Calculation formulas displayed

12. **Service Management Scripts** (Day 37) ⭐ NEW
    - `./start.sh` - Start backend and/or frontend
    - `./stop.sh` - Stop services cleanly

13. **Session Management** (Day 29)
    - Session refresh button (clears backend cache + frontend state)
    - Ensures fresh data without browser refresh

14. **Settings & Configuration**
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
│  ┌─────────────────────────┐  ┌─────────────────────────────┐   │
│  │    Data Sources Tab     │  │      Settings Tab           │   │
│  │                         │  │                             │   │
│  │ - Data provenance       │  │ - Account size              │   │
│  │ - Cache status          │  │ - Risk percentage           │   │
│  │ - Source transparency   │  │ - Position limits           │   │
│  └─────────────────────────┘  └─────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│                      SERVICES & UTILS                           │
│  ┌──────────────┐  ┌───────────────┐  ┌───────────────────┐     │
│  │   api.js     │  │ categorical   │  │  rsCalculator.js  │     │
│  │              │  │ Assessment.js │  │                   │     │
│  │ API calls    │  │ Verdict logic │  │ RS vs S&P 500     │     │
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
│  │                    API ENDPOINTS                        │    │
│  │                                                         │    │
│  │  /api/stock/<ticker>      - Price data, basic info      │    │
│  │  /api/fundamentals/<ticker> - Rich fundamental data     │    │
│  │  /api/market/spy          - S&P 500 data for RS         │    │
│  │  /api/market/vix          - VIX for risk assessment     │    │
│  │  /api/sr/<ticker>         - Support & Resistance        │    │
│  │  /api/scan/tradingview    - Batch market scanning       │    │
│  │  /api/validation/run      - Data validation             │    │
│  │  /api/provenance/<ticker> - Data source transparency    │    │
│  │  /api/cache/status        - Cache monitoring            │    │
│  │  /api/cache/clear         - Cache management            │    │
│  │  /api/health              - Backend health check        │    │
│  └─────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────┤
│                        MODULES                                  │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │ support_       │  │   validation/   │  │  cache_manager  │   │
│  │ resistance.py  │  │   engine.py     │  │      .py        │   │
│  │                │  │   scrapers.py   │  │                 │   │
│  │ Agglomerative  │  │   comparators   │  │ SQLite cache    │   │
│  │ + MTF S&R      │  │                 │  │ (5.5x speedup)  │   │
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
│                              │                                   │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SQLite Cache                          │    │
│  │         backend/data/cache.db (persistent)              │    │
│  │  - OHLCV: 24h TTL (market-aware) + source tracking      │    │
│  │  - Fundamentals: 7 day TTL                              │    │
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
        └──► /api/sr/AAPL ─────────► S&R Engine (Entry/Stop/Target)
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

### Data Sources

| Source | Data Type | Rate Limit | Role |
|--------|-----------|------------|------|
| TwelveData | OHLCV, Intraday | 8/min, 800/day | Primary OHLCV |
| Finnhub | Fundamentals, Quote | 60/min | Primary Fundamentals |
| FMP | Growth metrics | 10/min, 250/day | Fundamentals backup |
| yfinance | All types | ~30/min | Universal fallback |
| Stooq | OHLCV only | ~5/min | Last resort OHLCV |
| TradingView Screener | Batch scanning | Real-time | Market scanning |
| StockAnalysis | Validation | Real-time | Data quality check |
| Finviz | Validation | Real-time | Data quality check |

---

## Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- Chrome browser (for Selenium validation)

### Quick Start (Recommended)

```bash
# Clone repository
git clone https://github.com/balacloud/swing-trade-analyzer.git
cd swing-trade-analyzer

# Start both services
./start.sh

# Or start individually
./start.sh backend   # Backend only (http://localhost:5001)
./start.sh frontend  # Frontend only (http://localhost:3000)
```

### Manual Setup

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys (copy template and add your keys)
cp .env.example .env
# Edit .env with your API keys (TwelveData, Finnhub, FMP)

# Start backend
python backend.py
# Backend runs on http://localhost:5001
```

#### Frontend Setup

```bash
cd frontend
npm install
npm start
# Frontend runs on http://localhost:3000
```

### Stopping Services

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
3. Click "Scan for Opportunities"
4. Click any result to run full analysis

### Validate Data Accuracy

1. Click "Validate Data" tab
2. Enter tickers (comma-separated)
3. Click "Run Validation"
4. Review Quality Score, Coverage, Accuracy

### View Data Sources (Day 38)

1. Click "Data Sources" tab
2. Enter a ticker to see:
   - Where each data point comes from
   - Cache hit/miss status
   - Calculation formulas used

---

## API Reference

### GET /api/health

Returns backend health status including multi-source provider information.

```json
{
  "status": "healthy",
  "version": "2.19",
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

### GET /api/stock/<ticker>

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

### GET /api/fundamentals/<ticker>

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

### GET /api/sr/<ticker>

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

### GET /api/provenance/<ticker> (Day 38)

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

### GET /api/cache/status (Day 37)

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

### POST /api/cache/clear (Day 37)

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
- **Note:** Lacks epsGrowth and revenueGrowth - filled by FMP

### FMP (Backup - Growth Metrics)

- **What:** EPS Growth, Revenue Growth (fills Finnhub gaps)
- **Rate Limit:** 10/min, 250/day (free tier)
- **API Key:** Required (`FMP_API_KEY` in `.env`)

### yfinance (Universal Fallback)

- **What:** All data types (prices, fundamentals, earnings, stock info)
- **Rate Limit:** Self-imposed 30/min
- **API Key:** None (unofficial Yahoo Finance scraper)
- **Reliability:** Variable - subject to Yahoo throttling/blocking

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

### S&R Engine (v3.9 - Complete)

1. **100% detection rate** - Agglomerative clustering finds levels for all stocks
2. **Multi-timeframe confluence** - ~27% of levels confirmed by weekly data
3. **Touch-based scoring** - Levels ranked by historical significance
4. **Fibonacci extensions** - Available for ATH stocks

### Validation Methodology Differences

1. **Debt/Equity** - Different providers use total debt vs long-term only (30-50% variance)
2. **Revenue Growth** - Fiscal YoY vs TTM differences between sources (60-85% variance)
3. **These are not bugs** - Different valid calculation methods

### Deferred Features (v2+)

| Feature | Reason for Deferral |
|---------|---------------------|
| Options Tab | Needs Greeks calculation (complex) |
| Sector Rotation RRG | Complex, marginal v1 value |
| Candlestick Patterns | Low statistical accuracy |
| Full Lightweight Charts | After backtest validation |

---

## Roadmap

### Completed ✅

- v1.0: Single stock analysis, 75-point scoring
- v1.1: TradingView screener integration
- v1.2: S&R Engine with trade setups
- v1.3: Validation Engine with UI
- v2.0: Score breakdown with explanations
- v2.5: Trade viability display
- v2.9: Simplified Binary Scoring (4-criteria system)
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

### S&R Improvement Progress (Complete)

| Week | Task | Status |
|------|------|--------|
| 1 | Agglomerative Clustering | ✅ Complete (Day 31) |
| 2 | Multi-Timeframe Confluence | ✅ Complete (Day 32-33) |
| 3 | Fibonacci Extensions | ✅ Complete (Day 34) |
| 4 | Validation vs TradingView | ✅ Complete (Day 34) |

### Research Completed (Day 41-42)

- Perplexity research synthesis complete
- TIER 1 backtest improvements implemented
- Options tab feasibility analysis documented
- Sector rotation research documented

### Completed (Day 44-56)

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

### Planned 📅

- **S&P 500 Index Filter** - Restrict scans to S&P 500 constituents
- **TradingView Lightweight Charts** - Interactive charts with RSI/MACD overlays
- **Sector Rotation Tab** - Sector RS ranking vs SPY
- **Options Tab** - If data sources become available

### Philosophy (Day 27 + Day 44 Update)

Original roadmap focused on improving **win rate** through better signals.
After backtesting, we learned:
- Entry signals = ~10% of results
- Position sizing = ~90% of results
- **Score-to-return correlation = 0.011** (essentially ZERO)

**Day 44 Response:** Replaced 75-point numerical scoring with categorical assessments (Strong/Decent/Weak). The system works as a FILTER, not a RANKER - categorical assessments honestly represent this reality.

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
│   ├── backend.py             # Flask server (v2.19)
│   ├── cache_manager.py       # SQLite persistent cache (with source tracking)
│   ├── support_resistance.py  # S&R calculation (Agglomerative + MTF)
│   ├── pattern_detection.py   # VCP, Cup & Handle, Flat Base
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
│   │   └── comparators.py     # Tolerance checking
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main UI (v4.5)
│   │   ├── services/
│   │   │   └── api.js         # API client + health checks
│   │   ├── components/
│   │   │   ├── DecisionMatrix.jsx        # v4.15 3-step decision synthesis
│   │   │   └── BottomLineCard.jsx        # v4.13 Action plan summary
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System
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

---

*Last Updated: February 19, 2026 (Day 56)*
*Version: v4.17 (Backend v2.19, Frontend v4.5, Backtest v4.17)*
