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
- **75-point scoring system** across technical, fundamental, sentiment, and risk factors
- **BUY / HOLD / AVOID verdicts** based on quantitative analysis
- **Trade setups** with Entry, Stop Loss, Target, and Risk/Reward ratios
- **Relative Strength (RS)** calculations vs S&P 500
- **Batch scanning** for market opportunities (TradingView integration)
- **Data validation** against external sources for accuracy verification

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

> **Day 27 Critical Insight:** Backtesting revealed our 75-point scoring system achieves ~50% win rate (essentially random). This taught us that **entry signals account for only ~10% of trading results**, while **position sizing accounts for ~90%**. The system now focuses on proper position sizing using Van Tharp principles rather than chasing higher win rates.

---

## Features

### ✅ Implemented (v3.4)

1. **Single Stock Analysis**
   - Enter any ticker symbol
   - Get comprehensive 75-point score
   - View detailed breakdown by category with explanations

2. **Simplified Binary Scoring** (Day 27)
   - Research-backed 4-criteria system
   - Trend, Momentum, Setup, Risk/Reward checks
   - ALL 4 must pass = TRADE, any fail = PASS
   - Based on AQR Momentum Research + Turtle Trading

3. **Position Sizing Calculator** (Day 28)
   - Van Tharp R-multiple principles
   - Configurable account size and risk % (2-5%)
   - Auto-calculates shares, R targets (1.5R, 2R, 3R)
   - Auto-fill from stock analysis
   - **Day 29:** Manual override for custom entry/stop prices
   - **Day 29:** Max position limit to prevent over-allocation

4. **Advanced S&R Detection** (Day 31-32)
   - **Agglomerative Clustering** - Adaptive cluster count (replaced KMeans)
   - **ZigZag Pivot Detection** - 5% minimum price change threshold
   - **Touch-based Scoring** - Levels ranked by historical touches
   - **Multi-Timeframe Confluence** - Daily + Weekly S&R alignment
   - 100% detection rate (was 80% with KMeans)
   - Confluence badge shows % of levels confirmed by weekly data

5. **Trade Setup Generation**
   - Support & Resistance detection (Pivot → Agglomerative → Volume Profile)
   - Suggested Entry, Stop Loss, Target
   - Risk/Reward ratio calculation
   - Pullback re-entry zones for extended stocks
   - **MTF Confluence indicators** (★ marks confluent levels)

6. **Market Scanning** (TradingView Screener)
   - 5 pre-built strategies: Reddit, Minervini, Momentum, Value, Best Candidates
   - Filters for institutional-quality stocks
   - Stage 2 uptrend requirement (50 SMA > 200 SMA)

7. **Data Validation Engine**
   - Cross-references our data against StockAnalysis and Finviz
   - Quality Score = Coverage × Accuracy
   - Identifies data discrepancies

8. **Fundamentals with Failsafe** (Day 31-33)
   - Primary: Defeat Beta API
   - Fallback: yfinance (automatic when primary fails)
   - **Data source transparency** - Banner shows when using fallback
   - **Health endpoint** - `/api/health?check_defeatbeta=true` for diagnostics
   - ETF detection with special handling

9. **Session Management** (Day 29)
   - Session refresh button (clears backend cache + frontend state)
   - Ensures fresh data without browser refresh

10. **Settings & Configuration**
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
│  │ - Scores    │  │ - Results   │  │ - Pass/Fail/Warning     │  │
│  │ - Trade     │  │ - Quick     │  │ - Quality metrics       │  │
│  │   Setup     │  │   Analyze   │  │                         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│                      SERVICES & UTILS                           │
│  ┌──────────────┐  ┌───────────────┐  ┌───────────────────┐     │
│  │   api.js     │  │scoringEngine  │  │  rsCalculator.js  │     │
│  │              │  │    .js        │  │                   │     │
│  │ API calls    │  │ 75-pt scoring │  │ RS vs S&P 500     │     │
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
│  │  /api/health              - Backend health check        │    │
│  └─────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────┤
│                        MODULES                                  │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │ support_       │  │   validation/   │  │  TradingView    │   │
│  │ resistance.py  │  │   engine.py     │  │  Screener       │   │
│  │                │  │   scrapers.py   │  │                 │   │
│  │ Agglomerative  │  │   comparators   │  │ Batch scanning  │   │
│  │ + MTF S&R      │  │                 │  │                 │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐   │
│  │    yfinance    │  │   Defeat Beta   │  │   TradingView   │   │
│  │                │  │                 │  │    Screener     │   │
│  │ - Prices       │  │ - ROE, ROIC     │  │                 │   │
│  │ - Volume       │  │ - EPS Growth    │  │ - Batch scans   │   │
│  │ - 52w High/Low │  │ - Revenue Growth│  │ - Real-time     │   │
│  │ - Basic info   │  │ - Debt/Equity   │  │   filters       │   │
│  │                │  │ - Profit Margin │  │                 │   │
│  │ 15-30 min delay│  │ Weekly updates  │  │ Real-time       │   │
│  └────────────────┘  └─────────────────┘  └─────────────────┘   │
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
        ├──► /api/stock/AAPL ──────► yfinance (prices, volume)
        ├──► /api/fundamentals/AAPL ► Defeat Beta (ROE, EPS, etc.)
        ├──► /api/market/spy ──────► yfinance (S&P 500 for RS)
        ├──► /api/market/vix ──────► yfinance (VIX for risk)
        └──► /api/sr/AAPL ─────────► S&R Engine (Entry/Stop/Target)
        │
        ▼
┌───────────────────┐
│ calculateScore()  │ (scoringEngine.js)
│                   │
│ - Technical: 40   │
│ - Fundamental: 20 │
│ - Sentiment: 10   │
│ - Risk: 5         │
│ ─────────────────│
│ Total: 75 points  │
└───────────────────┘
        │
        ▼
┌───────────────────┐
│ Verdict:          │
│ BUY / HOLD / AVOID│
└───────────────────┘
```

---

## Scoring Methodology

### 75-Point Scoring System

#### Technical Analysis (40 points)

| Metric | Points | Criteria |
|--------|--------|----------|
| **Trend Structure** | 15 | Price > 50 SMA > 200 SMA (Stage 2 uptrend) |
| **Short-term Trend** | 10 | Price > 8 EMA > 21 EMA |
| **Relative Strength** | 10 | RS ≥1.5 = 10pts, ≥1.2 = 7pts, ≥1.0 = 4pts |
| **Volume** | 5 | ≥1.5x 50-day avg = 5pts, ≥1.0x = 2pts |

#### Fundamental Analysis (20 points)

| Metric | Points | Criteria |
|--------|--------|----------|
| **EPS Growth** | 6 | ≥25% = 6pts, ≥15% = 4pts, ≥10% = 2pts |
| **Revenue Growth** | 5 | ≥20% = 5pts, ≥10% = 3pts, ≥5% = 1pt |
| **ROE** | 4 | ≥15% = 4pts, ≥10% = 2pts |
| **Debt/Equity** | 3 | <0.5 = 3pts, <1.0 = 2pts, <1.5 = 1pt |
| **Forward P/E** | 2 | <20 = 2pts, <25 = 1pt |

#### Sentiment (10 points)

| Metric | Points | Criteria |
|--------|--------|----------|
| **News Sentiment** | 10 | Placeholder (real sentiment in v2.0) |

#### Risk/Macro (5 points)

| Metric | Points | Criteria |
|--------|--------|----------|
| **VIX Level** | 2 | <15 = 2pts, <20 = 1pt |
| **S&P Regime** | 2 | SPY > 200 SMA = 2pts |
| **Market Breadth** | 1 | Placeholder |

### Verdict Logic

| Verdict | Conditions |
|---------|------------|
| **BUY** | Score ≥60 + No critical fails + RS ≥1.0 |
| **HOLD** | Score 40-59 OR 1 critical fail |
| **AVOID** | Score <40 OR 2+ critical fails OR RS <0.8 |

### Quality Gates (Auto-AVOID Triggers)

- Stock below 200 SMA (downtrend)
- RS < 0.8 (significant underperformance)
- Average daily dollar volume < $10M (illiquid)

---

## Tech Stack

### Frontend
- **React 18** - UI framework
- **Tailwind CSS** - Styling
- **Fetch API** - HTTP requests

### Backend
- **Python 3.9+** - Runtime
- **Flask** - Web framework
- **yfinance** - Price data
- **defeatbeta** - Fundamental data
- **tradingview-screener** - Batch scanning
- **scikit-learn** - Agglomerative clustering for S&R
- **beautifulsoup4 + selenium** - Web scraping for validation

### Data Sources

| Source | Data Type | Update Frequency |
|--------|-----------|------------------|
| yfinance | Prices, Volume, 52w High/Low | 15-30 min delay |
| Defeat Beta | ROE, EPS Growth, Revenue Growth, D/E | Weekly |
| TradingView Screener | Batch scanning, real-time filters | Real-time |
| StockAnalysis | Validation (prices, P/E, EPS) | Real-time |
| Finviz | Validation (ROE, D/E, Revenue Growth) | Real-time |

---

## Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- Chrome browser (for Selenium validation)

### Backend Setup

```bash
# Clone repository
git clone https://github.com/balacloud/swing-trade-analyzer.git
cd swing-trade-analyzer

# Create virtual environment
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask yfinance defeatbeta tradingview-screener scikit-learn
pip install beautifulsoup4 selenium webdriver-manager
pip install --break-system-packages <package>  # If needed on some systems

# Start backend
python backend.py
# Backend runs on http://localhost:5001
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
# Frontend runs on http://localhost:3000
```

---

## Usage

### Analyze a Stock

1. Open http://localhost:3000
2. Enter ticker symbol (e.g., "AAPL")
3. Click "Analyze" or press Enter
4. View results:
   - Verdict (BUY/HOLD/AVOID)
   - 75-point score breakdown
   - Trade setup (Entry/Stop/Target)
   - Relative Strength metrics

### Scan for Opportunities

1. Click "Scan Market" tab
2. Select strategy:
   - **Reddit**: Mid-cap+, high relative volume
   - **Minervini**: Large-cap momentum leaders
   - **Momentum**: Sustainable 5-50% monthly gains
   - **Value**: Quality at fair price (P/E 5-25)
3. Click "Scan for Opportunities"
4. Click any result to run full analysis

### Validate Data Accuracy

1. Click "Validate Data" tab
2. Enter tickers (comma-separated)
3. Click "Run Validation"
4. Review Quality Score, Coverage, Accuracy

---

## API Reference

### GET /api/health

Returns backend health status. Add `?check_defeatbeta=true` for live API diagnostics.

```json
{
  "status": "healthy",
  "version": "2.8",
  "defeatbeta_available": true,
  "defeatbeta_status": {
    "working": false,
    "error": "API connection error (TProtocolException)",
    "last_checked": "2026-01-19T10:00:00"
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

Returns fundamental data with automatic failsafe (Defeat Beta → yfinance).

```json
{
  "source": "yfinance",
  "dataSource": "yfinance_fallback",
  "dataQuality": "partial",
  "fallbackUsed": true,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 12.5,
  "revenueGrowth": 6.43,
  "debtToEquity": 1.34,
  "profitMargin": 24.3
}
```

**Data Quality Values:** `"full"` (Defeat Beta working), `"partial"` (yfinance fallback), `"unavailable"`

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
    "quality_score": 80.3,
    "coverage_rate": 97.4,
    "accuracy_rate": 82.5,
    "passed": 94,
    "failed": 11,
    "warnings": 9
  },
  "ticker_results": [...]
}
```

---

## Data Sources

### yfinance (Primary - Prices)

- **What:** Real-time prices, volume, 52-week high/low, basic info
- **Delay:** 15-30 minutes
- **Reliability:** High for price data
- **Limitations:** Fundamentals often incomplete or zero

### Defeat Beta (Primary - Fundamentals)

- **What:** ROE, ROIC, EPS Growth, Revenue Growth, Debt/Equity, Margins
- **Update Frequency:** Weekly
- **Reliability:** Good for fundamental metrics
- **Access:** `.data` attribute for raw data

### TradingView Screener (Scanning)

- **What:** Batch market scanning with filters
- **Update Frequency:** Real-time
- **Filters Available:** Market cap, RSI, SMA relationships, volume, sector

### Blended Approach

We merge data from multiple sources:
```python
# yfinance provides P/E, forwardP/E
# Defeat Beta provides ROE, EPS Growth, Revenue Growth
merged_fundamentals = {**yfinance_data, **defeatbeta_data}
```

This ensures we get the best data available from each source.

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

### Tolerances

```python
TOLERANCES = {
    'price': 2%,
    'pe_ratio': 10%,
    'roe': 15%,
    'revenue_growth': 25%,
    'debt_equity': 15%,
    '52w_high': 1%,
    '52w_low': 1%
}
```

---

## Known Limitations

### Data Limitations

1. **EPS not available** - yfinance doesn't provide EPS in fundamentals
2. **Defeat Beta weekly lag** - Fundamentals may be 1-7 days old
3. **Price delay** - 15-30 minute delay (acceptable for swing trading)

### S&R Engine (v3.4 - Improved)

1. **100% detection rate** - Agglomerative clustering finds levels for all stocks
2. **Multi-timeframe confluence** - ~27% of levels confirmed by weekly data
3. **Touch-based scoring** - Levels ranked by historical significance

**Remaining Limitations:**
1. **ATH stocks** - Fibonacci extensions planned for stocks at all-time highs (Week 3)
2. **Validation pending** - TradingView comparison not yet done (Week 4)

### Validation Limitations

1. **Different calculation periods** - Defeat Beta (TTM) vs Finviz (Q/Q)
2. **Scraping dependency** - External sites may change structure

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
- v3.4: Multi-timeframe confluence, fundamentals transparency, data source indicators

### S&R Improvement Progress (Day 30-33)

| Week | Task | Status |
|------|------|--------|
| 1 | Agglomerative Clustering | ✅ Complete (Day 31) |
| 2 | Multi-Timeframe Confluence | ✅ Complete (Day 32-33) |
| 3 | Fibonacci Extensions | 📅 Planned (ATH stocks) |
| 4 | Validation vs TradingView | 📅 Planned |

### Planned 📅

- v3.5: **Forward Testing UI** - Track actual trades, record R-multiples, build SQN over time
- v3.6: **TradingView Widget** - Supplementary RSI/MACD view (free tier)
- v3.7: **Fibonacci Extensions** - Resistance projection for ATH stocks
- v3.8: **Pattern Detection** - VCP, cup-and-handle, flat base (better entry timing)

### Philosophy Change (Day 27)

Original roadmap focused on improving **win rate** through better signals.
After backtesting, we learned:
- Entry signals = ~10% of results
- Position sizing = ~90% of results

New roadmap focuses on:
- **Better R:R** through pattern-based entry timing
- **Risk reduction** through sentiment filtering
- **System measurement** through forward testing and SQN tracking

---

## Project Structure

```
swing-trade-analyzer/
├── backend/
│   ├── backend.py              # Flask server (v2.8)
│   ├── support_resistance.py   # S&R calculation (Agglomerative + MTF)
│   ├── validation/
│   │   ├── engine.py           # Validation orchestrator
│   │   ├── scrapers.py         # StockAnalysis + Finviz
│   │   └── comparators.py      # Tolerance checking
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main UI (v3.4)
│   │   ├── services/
│   │   │   └── api.js          # API client + health checks
│   │   └── utils/
│   │       ├── scoringEngine.js      # 75-point scoring + data quality
│   │       ├── simplifiedScoring.js  # 4-criteria binary (Day 27)
│   │       ├── positionSizing.js     # Van Tharp calculator (Day 28)
│   │       └── rsCalculator.js       # RS calculations
│   └── package.json
│
├── docs/
│   ├── claude/                 # Claude session documentation
│   │   ├── CLAUDE_CONTEXT.md   # Single reference point
│   │   ├── stable/             # Rarely-changing docs (GOLDEN_RULES)
│   │   ├── versioned/          # Day-versioned docs (API_CONTRACTS, KNOWN_ISSUES)
│   │   └── status/             # Daily status files
│   └── research/               # Research documents
│       ├── SR_IMPROVEMENT_RESEARCH.md
│       ├── TRADINGVIEW_INTEGRATION.md
│       └── FINNHUB_INTEGRATION_GUIDE.md
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
- **yfinance** - Free market data
- **Defeat Beta** - Fundamental data API
- **TradingView** - Screener library

---

*Last Updated: January 19, 2026 (Day 33)*
*Version: 3.4*
