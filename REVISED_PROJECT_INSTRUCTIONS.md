# 📋 SWING TRADE ANALYZER - PROJECT INSTRUCTIONS FOR CLAUDE

> **Project Status:** ✅ v1.0 COMPLETE | Ready for v1.1  
> **Last Updated:** December 10, 2025 (Day 10)  
> **GitHub:** https://github.com/balacloud/swing-trade-analyzer

---

## 🏆 SESSION RULES FOR CLAUDE (READ FIRST!)

### Golden Rules for Every Session:
1. **START of session:** Read PROJECT_STATUS_DAY[N].md first
2. **BEFORE modifying any file:** Ask user to attach/paste the CURRENT version
3. **NEVER assume code structure** - always verify with actual file
4. **END of session:** User will say "session ending" - create PROJECT_STATUS_DAY[N+1].md
5. **Files in Claude Projects are READ-ONLY snapshots** - not live-synced with local files
6. **NEVER HALLUCINATE** - Don't claim stocks will score X without running them
7. **THINK THROUGH** - Pause and reason carefully before suggesting solutions
8. **ALWAYS VALIDATE** - Fact-check answers against external sources
9. **DO PROPER DUE DILIGENCE** - Research thoroughly before making claims
10. **REFLECT ON ANSWERS** - Self-check for correctness before responding
11. **FEEDBACK MECHANISM** - Think → Research → Verify → Answer

### Why These Rules Exist:
- Claude Projects files are uploaded snapshots, not live synced
- Files must be explicitly uploaded/attached each session to be current
- Memory across sessions is limited - PROJECT_STATUS file is the source of truth
- Assumptions about code structure lead to wrong fixes
- Always ask for fresh screenshots before validation

### Current Status Reference:
- **Always check the latest PROJECT_STATUS_DAY[N].md** in project files
- This contains: current bugs, what's fixed, what's next, file locations

---

## 🎯 PROJECT OVERVIEW

### What We Built (v1.0 Complete)
An **institutional-grade swing trade recommendation engine** that analyzes individual stocks and provides data-driven verdicts based on proven methodologies from Mark Minervini (SEPA) and William O'Neil (CAN SLIM).

**Target Users:** Active swing traders seeking data-driven trade recommendations  
**Hold Period:** 1-2 months per trade  
**Target Returns:** 10-20% per trade with 60-70% win rate (aspirational - needs backtesting)

### Current Capabilities (v1.0)
1. User enters a stock ticker manually (e.g., AAPL, NVDA)
2. System fetches real market data (yfinance + Defeat Beta)
3. System calculates 75-point score across 4 categories
4. System generates BUY/HOLD/AVOID verdict
5. Quality gates flag critical issues (below 200 SMA, etc.)

### Validation Status (Day 10)
- **80% pass rate** against external sources (CNBC, StockAnalysis, GuruFocus)
- **Revenue Growth:** EXACT match on all tested stocks
- **ROE variance:** Acceptable (Defeat Beta weekly updates by design)
- **Technical scoring:** Correctly penalizes weak setups

### Methodology Alignment (Validated via Perplexity Analysis)
- **Minervini SEPA Coverage:** ~70-75%
- **O'Neil CAN SLIM Coverage:** ~70-75%
- **Approach:** Lean/focused (NOT indicator soup) - validated as correct

---

## 🔧 TECHNICAL ARCHITECTURE

### Tech Stack
- **Frontend:** React + Tailwind CSS (localhost:3000)
- **Backend:** Python Flask (localhost:5001)
- **Version Control:** GitHub

### Data Sources (IMPORTANT)
| Data Type | Source | Update Frequency | Used For |
|-----------|--------|------------------|----------|
| **Prices & Technicals** | yfinance | 15-30 min delay | Price, SMAs, EMAs, Volume, RS |
| **Fundamentals** | Defeat Beta | Weekly | EPS, Revenue, ROE, D/E, P/E |

**Note:** Both delays are acceptable for swing trading (1-2 month holds). This is NOT a day trading or scalping system.

### API Endpoints
| Endpoint | Description | Status |
|----------|-------------|--------|
| `/api/health` | Backend health check | ✅ |
| `/api/stock/<ticker>` | Stock data + prices | ✅ |
| `/api/fundamentals/<ticker>` | Rich fundamentals | ✅ |
| `/api/market/spy` | SPY data for RS | ✅ |
| `/api/market/vix` | VIX for risk | ✅ |

### File Locations
```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py          # Flask API server
│   ├── requirements.txt    # Python dependencies
│   └── venv/               # Virtual environment
└── frontend/
    ├── src/
    │   ├── App.jsx         # Main React component
    │   ├── components/     # UI components
    │   └── utils/          # RS calculator, scoring engine
    └── package.json
```

---

## 📊 SCORING METHODOLOGY (75 Points Total)

### Technical Analysis: 40 points
| Metric | Points | Criteria |
|--------|--------|----------|
| Trend Structure | 15 | Price > 50 SMA > 200 SMA (Stage 2 uptrend) |
| Short-term Trend | 10 | Price > 8 EMA > 21 EMA |
| Relative Strength | 10 | RS vs S&P 500: ≥1.5 = 10pts, ≥1.2 = 7pts, ≥1.0 = 4pts |
| Volume | 5 | ≥1.5x 50-day avg = 5pts, ≥1.0x = 2pts |

### Fundamental Analysis: 20 points
| Metric | Points | Criteria |
|--------|--------|----------|
| EPS Growth | 6 | ≥25% = 6pts, ≥15% = 4pts, ≥10% = 2pts |
| Revenue Growth | 5 | ≥20% = 5pts, ≥10% = 3pts, ≥5% = 1pt |
| ROE | 4 | ≥15% = 4pts, ≥10% = 2pts |
| Debt/Equity | 3 | <0.5 = 3pts, <1.0 = 2pts, <1.5 = 1pt |
| Forward P/E | 2 | <20 = 2pts, <25 = 1pt |

### Sentiment: 10 points
| Metric | Points | Criteria |
|--------|--------|----------|
| News Sentiment | 10 | Placeholder (real sentiment in v2.0) |

### Risk/Macro: 5 points
| Metric | Points | Criteria |
|--------|--------|----------|
| VIX Level | 2 | <15 = 2pts, <20 = 1pt |
| S&P Regime | 2 | SPY > 200 SMA = 2pts |
| Market Breadth | 1 | Placeholder |

---

## 🎯 VERDICT LOGIC

**BUY:** Score ≥60/75 + No critical fails + RS ≥1.0  
**HOLD:** Score 40-59 OR 1 critical fail  
**AVOID:** Score <40 OR 2+ critical fails OR RS <0.8

### Quality Gate Conditions (Critical Fails)
- Stock below 200 SMA (downtrend)
- RS < 0.8 (significant underperformance)
- Average daily dollar volume < $10M (illiquid)

---

## 📋 ROADMAP

### v1.0 - COMPLETE ✅
- Single stock manual entry
- 75-point scoring system
- Real-time prices (yfinance)
- Fundamentals (Defeat Beta)
- Quality gates
- 80% validation pass rate

### v1.1 - NEXT PRIORITY 🔄
**TradingView Screener Integration**
- Install `tradingview-screener` library
- Create `/api/scan/tradingview` endpoint
- Batch scanning for S&P 500 opportunities
- Frontend button: "Scan for Opportunities"

**Also in v1.1:**
- EPS Growth stock split adjustment (AVGO 10:1 split issue)
- UI: Show both data sources indicator (low priority)

### v1.2 - PLANNED 📅
**Support & Resistance Engine**
- Multi-method approach: Pivot, KMeans, Volume Profile
- Fail-safe logic (always returns levels)
- **Enables precise output:**
  - Entry Price (near support + confirmation)
  - Stop Loss (below key support)
  - Target (next resistance)
  - Risk/Reward Ratio

### v2.0 - FUTURE 🔮
- Pattern detection (VCP, cup-and-handle, flat base)
- Multi-timeframe analysis
- Real sentiment analysis
- **Backtesting component** (validate 60-70% win rate target)

---

## ⚠️ KNOWN LIMITATIONS & DESIGN DECISIONS

### By Design (Not Bugs)
1. **Defeat Beta ROE lag** - Weekly updates vs real-time (blended approach intentional)
2. **yfinance price delay** - 15-30 min delay acceptable for swing trading
3. **Minor D/E variances** - Different calculation methods across sources

### Known Issues to Fix
1. **EPS Growth stock split** - AVGO shows -62% due to 10:1 split in July 2024 (v1.1)

### What System Does NOT Do (Yet)
- ❌ Precise entry/stop/target prices (coming in v1.2 with S/R Engine)
- ❌ Pattern recognition (VCP, cup-handle) (v2.0)
- ❌ Backtesting (v2.0)
- ❌ Institutional ownership tracking (future)

---

## 🚀 QUICK COMMANDS

```bash
# Start backend
cd /Users/balajik/projects/swing-trade-analyzer/backend
source venv/bin/activate
python backend.py

# Start frontend
cd /Users/balajik/projects/swing-trade-analyzer/frontend
npm start

# Install TradingView screener (v1.1)
pip install tradingview-screener

# Git
git add .
git commit -m "Description"
git push origin main
```

---

## 📚 REFERENCE RESOURCES

### Validation Sources
- **StockAnalysis:** https://stockanalysis.com
- **GuruFocus:** https://www.gurufocus.com
- **FinanceCharts:** https://www.financecharts.com
- **Yahoo Finance:** https://finance.yahoo.com
- **CNBC:** https://www.cnbc.com/quotes

### APIs & Libraries
- **TradingView Screener:** https://shner-elmo.github.io/TradingView-Screener/
- **Defeat Beta:** https://github.com/defeat-beta/defeatbeta-api
- **yfinance:** https://github.com/ranaroussi/yfinance

### Trading Methodologies
- Mark Minervini: SEPA methodology, VCP patterns
- William O'Neil: CAN SLIM strategy

---

## 🔄 HOW TO RESUME WORK

### Start Message Template
> "Resume swing trade analyzer - read PROJECT_STATUS_DAY[N].md first. [Describe what you want to work on today]."

### Always Provide
1. The latest PROJECT_STATUS_DAY[N].md file
2. Any code files that need modification (attach fresh copies)
3. Screenshots if validating app behavior

---

## 💡 KEY LEARNINGS (Day 10)

1. **Revenue Growth is rock-solid** - Defeat Beta matches external sources exactly
2. **ROE variance is acceptable** - weekly update lag is by design
3. **Technical scoring works correctly** - penalizes stocks below key SMAs
4. **Quality gates are effective** - catching issues like META below 200 SMA
5. **Volume thresholds already correct** - ≥1.5x = 5 points
6. **Lean approach validated** - focused system beats indicator soup
7. **NVDA AVOID proves system wisdom** - good fundamentals + bad technicals = bad trade

---

*This file is the PROJECT INSTRUCTIONS for Claude Projects.*  
*For current session status, always refer to PROJECT_STATUS_DAY[N].md*
