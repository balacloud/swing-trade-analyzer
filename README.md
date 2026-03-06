# Swing Trade Analyzer (STA)

A personal swing trading analysis system built on **Mark Minervini's SEPA** methodology and **William O'Neil's CAN SLIM** approach. Analyzes individual stocks, scans the market for opportunities, detects chart patterns, and generates structured trade setups with risk/reward calculations.

> **Disclaimer:** This tool is for educational and research purposes only. It is not financial advice. All trading decisions are your own responsibility.

---

## Table of Contents

- [What It Does](#what-it-does)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables (API Keys)](#environment-variables-api-keys)
- [Running the App](#running-the-app)
- [How to Use](#how-to-use)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)

---

## What It Does

| Feature | Description |
|---------|-------------|
| **Stock Analysis** | Categorical assessment (Strong/Decent/Weak) across Technical, Fundamental, Sentiment, and Risk dimensions. Verdict: BUY / HOLD / AVOID |
| **Trade Setup** | Entry price, stop loss, target, R:R ratio. Dual entry strategy (conservative pullback vs aggressive momentum) |
| **Pattern Detection** | VCP, Cup & Handle, Flat Base, Minervini 8-point Trend Template |
| **Market Scanner** | 5 pre-built strategies using TradingView screener (Minervini, Momentum, Value, Reddit, Best Candidates) |
| **Sector Rotation** | 11 SPDR ETFs ranked by Relative Strength vs SPY with RRG quadrant classification |
| **Support & Resistance** | Agglomerative clustering + ZigZag pivot detection + multi-timeframe confluence |
| **Context Tab** | Macro regime: yield curve, Fed funds, CPI, FOMC proximity, seasonal cycle — via FRED API |
| **Forward Testing** | Paper trade journal with R-multiple tracking (Van Tharp SQN statistics) |
| **Data Validation** | Cross-references data against StockAnalysis and Finviz for quality scoring |

---

## Tech Stack

**Backend:** Python 3.9+, Flask, SQLite, scikit-learn, pandas, numpy

**Frontend:** React 18, Tailwind CSS

**Data providers:** TwelveData, Finnhub, FMP, yfinance, Stooq (fallback chain)

**Optional:** FRED API (macro context), Alpha Vantage (news sentiment)

---

## Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- npm
- Chrome browser (required only for the Data Validation feature — uses Selenium)
- Git

---

## Installation

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

Create `backend/.env` based on `backend/.env.example`. Here is every variable and where to get it:

### Required

| Variable | Where to Get It | Free Tier |
|----------|----------------|-----------|
| `TWELVEDATA_API_KEY` | [twelvedata.com](https://twelvedata.com) → Sign up → API Keys | 800 credits/day, 8/min |
| `FINNHUB_API_KEY` | [finnhub.io](https://finnhub.io) → Sign up → Dashboard | 60 calls/min |
| `FMP_API_KEY` | [financialmodelingprep.com](https://financialmodelingprep.com) → Get API Key | 250 calls/day |

### Optional (graceful degradation if not set)

| Variable | Where to Get It | Used For |
|----------|----------------|---------|
| `FRED_API_KEY` | [fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html) — instant, no credit card | Context Tab: yield curve, CPI, Fed funds |
| `ALPHA_VANTAGE_API_KEY` | [alphavantage.co](https://www.alphavantage.co/support/#api-key) | Context Tab: news sentiment |

> **Without FRED_API_KEY:** The Context tab will not load macro indicator data. All other features work normally.
>
> **Without ALPHA_VANTAGE_API_KEY:** News sentiment in the Context tab shows an empty state. All other features work normally.
>
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
```

Backend starts on `http://localhost:5001`
Frontend starts on `http://localhost:3000`

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
./stop.sh
```

### Verify it's working

Open `http://localhost:3000` in your browser. Type a ticker (e.g., `AAPL`) and click Analyze. You should see a verdict card with categorical assessment within a few seconds.

If the backend connection indicator shows red, check that `backend.py` is running and the `.env` file is correctly set up.

---

## How to Use

### Analyze a Stock

1. Go to the **Analyze Stock** tab
2. Enter a ticker symbol (e.g., `NVDA`, `AAPL`, `MSFT`)
3. Select holding period: Quick (5-10 days) / Standard (15-30 days) / Position (1-3 months)
4. Click **Analyze**

The result shows:
- **Verdict** (BUY / HOLD / AVOID) with reasoning
- **Categorical breakdown** — Technical, Fundamental, Sentiment, Risk/Macro
- **Decision Matrix** — 3-step synthesis: Should I Trade? → When to Enter? → Does Math Work?
- **Dual Entry Strategy** — Conservative (pullback to support) vs Aggressive (current price)
- **Pattern detection** — VCP, Cup & Handle, Flat Base with confidence score
- **Trade setup** — Entry, Stop Loss, Target, Risk/Reward ratio

### Scan the Market

1. Click **Scan Market** tab
2. Pick a strategy:
   - **Best Candidates** — aligned with backtested criteria (ADX≥20, RSI 50-70, EMA momentum)
   - **Minervini** — large-cap momentum leaders
   - **Momentum** — sustainable trend stocks
   - **Value** — quality at fair price (P/E 5-25)
   - **Reddit** — mid-cap, high relative volume
3. Select index (S&P 500, NASDAQ 100, Dow 30, All US)
4. Click **Scan for Opportunities**
5. Click any result row to run full analysis on that stock

### Sector Rotation

Click **Sectors** tab to see all 11 SPDR sector ETFs ranked by Relative Strength vs SPY with quadrant classification (Leading / Improving / Weakening / Lagging).

### Forward Test (Paper Trading)

Click **Forward Test** tab to record paper trades. Track R-multiples, win rate, and expectancy using Van Tharp's SQN framework.

---

## Architecture

```
frontend (React, port 3000)
        │
        │ HTTP REST
        ▼
backend (Flask, port 5001)
        │
        ├── cache_manager.py     SQLite persistent cache (backend/data/cache.db)
        ├── providers/           Multi-source data provider with fallback chain
        │     ├── twelvedata     Primary OHLCV
        │     ├── finnhub        Primary fundamentals
        │     ├── fmp            Growth metrics
        │     ├── yfinance       Universal fallback
        │     └── stooq          Last resort OHLCV
        ├── support_resistance.py  Agglomerative clustering + ZigZag + MTF
        ├── pattern_detection.py   VCP, Cup & Handle, Flat Base, Trend Template
        ├── cycles_engine.py       FRED macro data (yield curve, business cycle)
        ├── econ_engine.py         FRED econ indicators (CPI, Fed funds, unemployment)
        ├── news_engine.py         Alpha Vantage news sentiment
        └── validation/            Selenium scrapers for data quality checks
```

### Data Provider Fallback Chain

```
OHLCV:        TwelveData → yfinance → Stooq
Fundamentals: Finnhub → FMP → yfinance (field-level merge)
Market data:  TwelveData → yfinance
VIX:          yfinance → Finnhub
Fear & Greed: CNN Money (scraped)
Macro:        FRED API
```

All provider failures are logged. The SQLite cache serves stale data as a last resort so the UI never crashes on an API outage.

### Verdict Logic

```
Technical:   Strong = Trend Template ≥7/8 + RSI 50-70 + RS ≥1.0
             Decent = Trend Template ≥5/8 + RSI 40-80
             Weak   = below thresholds

Fundamental: Strong = ROE >15% + Revenue Growth >10% + D/E <1.0
             Decent = partial criteria met
             Weak   = below thresholds

Sentiment:   Strong = Fear & Greed 60-80 (Greed)
             Neutral = 35-60
             Weak   = <35 (Extreme Fear) or >80 (Extreme Greed)

Risk/Macro:  Favorable = VIX <20 + SPY above 200 SMA
             Neutral   = VIX 20-30 or SPY mixed
             Unfavorable = VIX >30 or SPY below 200 SMA

BUY  = 2+ Strong categories + Favorable or Neutral risk + ADX ≥20
HOLD = mixed signals, ADX <20, or Unfavorable risk
AVOID = Weak Technical (non-negotiable) OR 2+ Weak categories
```

---

## API Reference

All endpoints are served from `http://localhost:5001`.

### Core Analysis

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stock/<ticker>` | GET | Price data, RS, ADX, trend template, volume |
| `/api/fundamentals/<ticker>` | GET | ROE, revenue growth, D/E ratio, EPS growth |
| `/api/sr/<ticker>` | GET | Support & resistance levels, entry/stop/target |
| `/api/patterns/<ticker>` | GET | VCP, Cup & Handle, Flat Base detection |
| `/api/earnings/<ticker>` | GET | Days to next earnings event |

### Market Data

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY price, 200 SMA status, 5-day return |
| `/api/market/vix` | GET | VIX level and regime |
| `/api/fear-greed` | GET | CNN Fear & Greed Index |
| `/api/sectors/rotation` | GET | 11 sector ETFs ranked by RS vs SPY |

### Context (requires FRED_API_KEY)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cycles` | GET | Yield curve, business cycle, presidential year, seasonal, FOMC, quad witching |
| `/api/econ` | GET | Fed funds, CPI, PMI proxy, unemployment |
| `/api/news/<ticker>` | GET | News sentiment (requires ALPHA_VANTAGE_API_KEY) |
| `/api/context/<ticker>` | GET | Aggregated macro regime + options block detection |

### Scanning & Utilities

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | POST | Run a TradingView screener strategy |
| `/api/scan/strategies` | GET | List available scan strategies |
| `/api/cache/status` | GET | Cache hit/miss stats and age |
| `/api/cache/clear` | POST | Clear all cached data |
| `/api/health` | GET | Backend health check |
| `/api/data/freshness` | GET | Data age per source |

### Forward Test

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/forward-test/record` | POST | Record a paper trade |
| `/api/forward-test/signals` | GET | List all paper trades |
| `/api/forward-test/performance` | GET | Win rate, expectancy, SQN |

---

## Data Sources

| Source | What It Provides | Rate Limits | API Key Required |
|--------|-----------------|-------------|-----------------|
| TwelveData | OHLCV, intraday | 8/min, 800/day | Yes |
| Finnhub | Fundamentals, quote | 60/min | Yes |
| FMP | EPS growth, revenue growth | 10/min, 250/day | Yes |
| yfinance | Everything (fallback) | ~30/min (unofficial) | No |
| Stooq | OHLCV (last resort) | ~5/min | No |
| TradingView Screener | Batch market scan | Real-time | No |
| FRED | Macro economic data | 1000/day | Yes (free) |
| Alpha Vantage | News sentiment | 25/day (free tier) | Yes (free) |
| CNN Money | Fear & Greed Index | Scraped | No |

---

## Project Structure

```
swing-trade-analyzer/
├── start.sh                    Start both services
├── stop.sh                     Stop both services
│
├── backend/
│   ├── backend.py              Main Flask app (all API routes)
│   ├── requirements.txt        Python dependencies
│   ├── .env.example            Environment variable template
│   ├── .env                    Your API keys (never committed to git)
│   │
│   ├── support_resistance.py   S&R engine (agglomerative + ZigZag + MTF)
│   ├── pattern_detection.py    Chart pattern detection (VCP, C&H, Flat Base)
│   ├── cache_manager.py        SQLite persistent cache
│   ├── constants.py            Shared thresholds and configuration
│   ├── field_maps.py           Data field normalization across providers
│   │
│   ├── cycles_engine.py        FRED macro cycles (yield curve, FOMC, seasonal)
│   ├── econ_engine.py          FRED economic indicators (CPI, Fed funds)
│   ├── news_engine.py          Alpha Vantage news sentiment
│   │
│   ├── providers/
│   │   ├── orchestrator.py     Provider cascade + circuit breaker + rate limiting
│   │   ├── twelvedata_provider.py
│   │   ├── finnhub_provider.py
│   │   ├── fmp_provider.py
│   │   ├── yfinance_provider.py
│   │   └── stooq_provider.py
│   │
│   ├── validation/
│   │   ├── engine.py           Validation orchestrator
│   │   ├── scrapers.py         StockAnalysis + Finviz scrapers
│   │   └── forward_tracker.py  Paper trade tracker
│   │
│   └── data/
│       └── cache.db            SQLite cache (auto-created, not committed)
│
└── frontend/
    ├── package.json
    └── src/
        ├── App.jsx                 Main app, tab routing, state management
        ├── services/
        │   └── api.js              All API calls to backend
        ├── utils/
        │   ├── categoricalAssessment.js   Verdict logic
        │   ├── simplifiedScoring.js       9-criteria checklist
        │   └── riskRewardCalc.js          R:R and position sizing
        └── components/
            ├── AnalyzeTab/         Stock analysis UI
            ├── ScanTab/            Market scanner UI
            ├── SectorRotationTab/  Sector rotation UI
            ├── ContextTab/         Macro context UI
            └── ...
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

### Scan returns no results
- TradingView screener filters are strict by design; try "All US" market instead of "S&P 500"
- The scan requires no API key — it uses the `tradingview-screener` Python package

### Context tab shows no data
- Add `FRED_API_KEY` to `backend/.env` — get one free at [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html)

---

## Disclaimer

This software is provided for **educational and research purposes only**. It does not constitute financial advice. Past performance of any strategy shown is not indicative of future results. Always do your own research before making any investment decisions. The authors accept no responsibility for financial losses incurred using this software.
