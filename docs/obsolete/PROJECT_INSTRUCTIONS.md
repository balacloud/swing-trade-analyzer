# 📋 SWING TRADE ANALYZER - PROJECT INSTRUCTIONS FOR CLAUDE

> **Project Status:** ✅ v1.3.1 COMPLETE | Ready for v1.4  
> **Last Updated:** December 31, 2025 (Day 19)  
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
- Always ask for fresh code before making changes

---

## 🎯 PROJECT OVERVIEW

### What We Built (v1.3.1 Complete)
An **institutional-grade swing trade recommendation engine** that analyzes individual stocks and provides data-driven verdicts based on proven methodologies from Mark Minervini (SEPA) and William O'Neil (CAN SLIM).

**Target Users:** Active swing traders seeking data-driven trade recommendations  
**Hold Period:** 1-2 months per trade  
**Target Returns:** 10-20% per trade with 60-70% win rate (aspirational - needs backtesting)

### Current Capabilities (v1.3.1)
1. ✅ Single stock analysis with 75-point scoring
2. ✅ Relative Strength calculation vs S&P 500
3. ✅ Support & Resistance detection (Pivot + KMeans methods)
4. ✅ Trade setups (Entry/Stop/Target/R:R)
5. ✅ TradingView batch scanning (4 strategies)
6. ✅ Data validation against external sources
7. ✅ Quality gates (200 SMA, RS, liquidity)

### ⚠️ CRITICAL: System is UNPROVEN
- No backtest results
- No forward testing data
- 60-70% win rate is aspirational, not validated
- **DO NOT TRADE LIVE until backtesting (v2.1) complete**

---

## 📊 VALIDATION STATUS (Day 19)

### 30-Stock Test Results
| Metric | Value |
|--------|-------|
| Quality Score | 78.6% |
| Accuracy Rate | 80.3% |
| Coverage Rate | 98.0% |
| Stocks Tested | 30 |

### Known Issues
| Issue | Severity | Status |
|-------|----------|--------|
| S&R returns 0 support (17% of stocks) | HIGH | Option C designed |
| S&R returns 0 resistance (10% of stocks) | HIGH | Option C designed |
| TradingView Scan 404 | HIGH | To fix |
| ATR null for pivot method | MEDIUM | To fix |
| System UNPROVEN | CRITICAL | v2.1 planned |
| Sentiment placeholder (10pts fake) | MEDIUM | To address |

---

## 🔧 TECHNICAL ARCHITECTURE

### Tech Stack
- **Frontend:** React + Tailwind CSS (localhost:3000)
- **Backend:** Python Flask (localhost:5001)
- **Version Control:** GitHub

### Data Sources
| Data Type | Source | Update Frequency |
|-----------|--------|------------------|
| Prices & Technicals | yfinance | 15-30 min delay |
| Fundamentals | Defeat Beta | Weekly |
| Batch Scanning | TradingView Screener | Real-time |

### API Endpoints
| Endpoint | Description | Status |
|----------|-------------|--------|
| `/api/health` | Backend health check | ✅ |
| `/api/stock/<ticker>` | Stock data + prices | ✅ |
| `/api/fundamentals/<ticker>` | Rich fundamentals | ✅ |
| `/api/market/spy` | SPY data for RS | ✅ |
| `/api/market/vix` | VIX for risk | ✅ |
| `/api/sr/<ticker>` | Support & Resistance | ✅ (needs enhancement) |
| `/api/scan/tradingview` | Batch scanning | ❌ 404 error |
| `/api/validation/run` | Data validation | ✅ |

### File Locations
```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py              # Flask API server (v2.8)
│   ├── support_resistance.py   # S&R calculation
│   ├── validation/             # Validation engine
│   ├── requirements.txt
│   └── venv/
└── frontend/
    ├── src/
    │   ├── App.jsx             # Main React component (v2.4)
    │   ├── services/api.js     # API client (v2.3)
    │   └── utils/
    │       ├── scoringEngine.js    # 75-point scoring (v2.1)
    │       ├── rsCalculator.js     # RS calculations
    │       └── technicalIndicators.js
    └── package.json
```

---

## 📊 SCORING METHODOLOGY (75 Points Total)

### Technical Analysis: 40 points
| Metric | Points | Criteria |
|--------|--------|----------|
| Trend Structure | 15 | Price > 50 SMA > 200 SMA |
| Short-term Trend | 10 | Price > 8 EMA > 21 EMA |
| Relative Strength | 10 | RS ≥1.5 = 10pts, ≥1.2 = 7pts, ≥1.0 = 4pts |
| Volume | 5 | ≥1.5x 50-day avg = 5pts |

### Fundamental Analysis: 20 points
| Metric | Points | Criteria |
|--------|--------|----------|
| EPS Growth | 6 | ≥25% = 6pts |
| Revenue Growth | 5 | ≥20% = 5pts |
| ROE | 4 | ≥15% = 4pts |
| Debt/Equity | 3 | <0.5 = 3pts |
| Forward P/E | 2 | <20 = 2pts |

### Sentiment: 10 points (⚠️ PLACEHOLDER)
Currently gives default 5 points to all stocks - needs real implementation or removal.

### Risk/Macro: 5 points
| Metric | Points | Criteria |
|--------|--------|----------|
| VIX Level | 2 | <15 = 2pts |
| S&P Regime | 2 | SPY > 200 SMA = 2pts |
| Market Breadth | 1 | Placeholder |

### Verdict Logic
**BUY:** Score ≥60 + No critical fails + RS ≥1.0  
**HOLD:** Score 40-59 OR 1 critical fail  
**AVOID:** Score <40 OR 2+ critical fails OR RS <0.8

---

## 📋 ROADMAP

### ✅ Completed
- v1.0: Single stock analysis, 75-point scoring
- v1.1: TradingView screener integration
- v1.2: S&R Engine with trade setups
- v1.3: Validation Engine with UI

### 🔄 v1.4 - NEXT (Priority Order)
1. **Forward Testing UI** (CRITICAL) - Track signals in real-time
2. **S&R Option C Enhancement** - Context-aware filtering
3. **Fix TradingView Scan 404** - Quick fix
4. **Fix ATR null for pivot** - Quick fix
5. **Fix RSI N/A** - Quick fix

### 📅 v2.0-2.1 - PLANNED
- Backtesting Framework (CRITICAL)
- Transaction cost model
- Pattern detection (VCP, cup-and-handle)
- Real sentiment analysis

---

## 🏗️ S&R OPTION C DESIGN (Ready to Implement)

### Problem
- 17% of stocks return 0 support (extended stocks)
- 10% of stocks return 0 resistance (beaten-down stocks)
- Current 20% proximity filter is too strict

### Solution: Stock State Classification
```python
STOCK_STATES = {
    "TIGHT_BASE": support_dist <= 8%,      # Ideal entry
    "NORMAL_PULLBACK": support_dist <= 15%, # Good setup
    "EXTENDED": support_dist <= 25%,        # Wait for pullback
    "VERY_EXTENDED": support_dist <= 40%,   # High risk
    "PARABOLIC": support_dist > 40%,        # No valid entry
    "BEATEN_DOWN": resistance_dist > 30%    # Potential value, high risk
}
```

### Key Changes
1. Always return nearest S&R (no filter initially)
2. Add `stockState` classification
3. Add `tradeAdvice` human-readable guidance
4. Add `entryViable` flag (True/False/WAIT)

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

# Test endpoints
curl http://localhost:5001/api/health
curl http://localhost:5001/api/stock/AAPL
curl http://localhost:5001/api/sr/AAPL
curl -X POST http://localhost:5001/api/validation/run \
  -H "Content-Type: application/json" \
  -d '{"tickers": ["AAPL","NVDA"]}'
```

---

## 🔄 HOW TO RESUME WORK

### Start Message Template
> "Resume swing trade analyzer - read PROJECT_STATUS_DAY19.md"

### Always Provide
1. The latest PROJECT_STATUS_DAY[N].md file
2. Any code files that need modification (attach fresh copies)
3. Screenshots if validating app behavior

---

## 📚 REFERENCE RESOURCES

### Validation Sources
- StockAnalysis: https://stockanalysis.com
- Finviz: https://www.finviz.com
- GuruFocus: https://www.gurufocus.com

### APIs & Libraries
- TradingView Screener: https://shner-elmo.github.io/TradingView-Screener/
- Defeat Beta: https://github.com/defeat-beta/defeatbeta-api
- yfinance: https://github.com/ranaroussi/yfinance

### Trading Methodologies
- Mark Minervini: SEPA methodology, VCP patterns
- William O'Neil: CAN SLIM strategy

---

## 💡 KEY LEARNINGS

### Day 19 Learnings
1. **Test extensively before fixing** - 30 stocks revealed patterns
2. **External review is valuable** - Perplexity caught gaps we missed
3. **S&R filter works but UX is poor** - Option C solves this
4. **System is UNPROVEN** - Backtesting is critical path
5. **Document before fixing** - Understanding root cause prevents wrong fixes

### Architecture Rules (Day 18+)
1. Verify data contracts BEFORE writing code
2. Document API contracts
3. Producer defines API; consumer adapts
4. Don't double-calculate
5. Test incrementally
6. Clean separation of concerns
7. Flat API structures preferred

---

*This file is the PROJECT INSTRUCTIONS for Claude Projects.*  
*For current session status, always refer to PROJECT_STATUS_DAY[N].md*
