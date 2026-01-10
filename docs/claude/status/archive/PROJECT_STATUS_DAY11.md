# 🎯 SWING TRADE ANALYZER - PROJECT STATUS

> **Last Updated:** Day 11 (December 11, 2025)  
> **Status:** ✅ v1.1 Backend Complete | TradingView Screener Live  
> **Version:** 2.4 (TradingView Screener Integration)  
> **GitHub:** https://github.com/balacloud/swing-trade-analyzer

---

## 🏆 SESSION RULES (IMPORTANT FOR CLAUDE)

### Golden Rules for Every Session:
1. **START of session:** Read PROJECT_STATUS_DAY[N].md first
2. **BEFORE modifying any file:** Ask user to attach/paste the CURRENT version
3. **NEVER assume code structure** - always verify with actual file
4. **END of session:** Create updated PROJECT_STATUS_DAY[N+1].md
5. **User will say "session ending"** to trigger status file creation
6. **NEVER HALLUCINATE** - Don't claim stocks will score X without running them
7. **THINK THROUGH** - Pause and reason carefully before suggesting solutions
8. **ALWAYS VALIDATE** - Fact-check answers against external sources
9. **DO PROPER DUE DILIGENCE** - Research thoroughly before making claims
10. **REFLECT ON ANSWERS** - Self-check for correctness before responding
11. **FEEDBACK MECHANISM** - Think → Research → Verify → Answer

### Why These Rules Exist:
- Claude Projects files are READ-ONLY snapshots, not live synced
- Files must be explicitly uploaded/attached each session to be current
- Memory across sessions is limited - status file is the source of truth
- Assumptions lead to wrong fixes (e.g., field name mismatches)

---

## ✅ DAY 11 ACCOMPLISHMENTS

### Session Summary
1. **Installed TradingView Screener Library**
   - `pip install tradingview-screener` in backend venv
   - Verified with test query (top 5 stocks by market cap)

2. **Built `/api/scan/tradingview` Endpoint**
   - Initial implementation with `Column()` syntax failed
   - Fixed: Library uses `col()` function, not `Column()` class
   - Added 4 scanning strategies

3. **Refined Filters for Institutional Quality**
   - Initial results had junk tickers (OTC, penny stocks, moonshots)
   - Added exchange filter: NYSE/NASDAQ only (no OTC)
   - Increased market cap minimums ($2B-$10B depending on strategy)
   - Added RSI caps to avoid overbought chasing
   - Added momentum caps (5-50% 1M gain) to filter moonshots
   - Required Stage 2 uptrend (50 SMA > 200 SMA) for all strategies

4. **Tested All 4 Strategies Successfully**
   - Reddit: GEV, DNLI (mid-cap+ with unusual volume)
   - Minervini: PRAX (momentum leader)
   - Momentum: ALB (sustainable 31% 1M gain)
   - Value: JPM, XOM (large-cap quality at reasonable P/E)

5. **Updated Backend to v2.4**
   - Added TradingView import with graceful fallback
   - Added `/api/scan/tradingview` endpoint
   - Added `/api/scan/strategies` endpoint
   - Health check now shows `tradingview_available` status

---

## 📊 NEW API ENDPOINTS (Day 11)

### `/api/scan/tradingview`
**Method:** GET  
**Parameters:**
- `strategy`: 'reddit' (default), 'minervini', 'momentum', 'value'
- `limit`: max results (default 50, max 100)

**Response:**
```json
{
  "strategy": "reddit",
  "totalMatches": 847,
  "returned": 20,
  "timestamp": "2025-12-11T...",
  "candidates": [
    {
      "ticker": "GEV",
      "name": "GE Vernova",
      "price": 723.0,
      "volume": 11396413,
      "marketCap": 196164696259,
      "relativeVolume": 4.53,
      "sma50": 593.92,
      "sma200": 509.21,
      "rsi": 73.49,
      "pctFrom52wHigh": -1.09,
      "sector": "Producer Manufacturing",
      "industry": "Electrical Products"
    }
  ]
}
```

### `/api/scan/strategies`
**Method:** GET  
**Returns:** List of available strategies with descriptions

---

## 📋 SCANNING STRATEGIES (Refined)

| Strategy | Market Cap | Price | Key Filters | Sort By |
|----------|------------|-------|-------------|---------|
| **reddit** | >$2B | >$10 | Stage 2, RSI 40-75, RelVol>1x | Relative Volume |
| **minervini** | >$5B | >$15 | Stage 2, RSI 50-75 | 1-Month Perf |
| **momentum** | >$5B | >$15 | Stage 2, RSI 50-70, 1M gain 5-50% | 1-Month Perf |
| **value** | >$10B | >$15 | Stage 2, P/E 5-25, RSI 45-70 | Market Cap |

**All strategies include:**
- NYSE/NASDAQ only (no OTC)
- Stage 2 uptrend required (50 SMA > 200 SMA)
- Minimum avg volume 500K+
- Primary listing only

---

## 🔧 Technical Details

### Backend (Flask - Port 5001)
- **Version:** 2.4
- **New Dependencies:** `tradingview-screener==3.0.0`
- **Data Sources:** 
  - yfinance (prices, basic info) - 15-30 MIN DELAY
  - Defeat Beta (fundamentals via `.data` attribute) - WEEKLY UPDATES
  - TradingView Screener (batch scanning) - REAL-TIME

### API Endpoints (Complete)
| Endpoint | Description | Status |
|----------|-------------|--------|
| `/api/health` | Backend health check | ✅ |
| `/api/stock/<ticker>` | Stock data + prices | ✅ |
| `/api/fundamentals/<ticker>` | Rich fundamentals | ✅ |
| `/api/market/spy` | SPY data for RS | ✅ |
| `/api/market/vix` | VIX for risk | ✅ |
| `/api/scan/tradingview` | **NEW** Batch scanning | ✅ |
| `/api/scan/strategies` | **NEW** List strategies | ✅ |

---

## 🔍 COMPLETE PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── .git/
├── .gitignore
├── README.md                    # GitHub readme
├── debug_bundle.txt
├── Files_Archives/
│
├── backend/
│   ├── venv/
│   │   └── lib/python3.9/site-packages/
│   │       └── tradingview_screener/  # NEW - installed Day 11
│   ├── backend.py              # ✅ Main Flask server (v2.4)
│   ├── backend_day4.py         # Archive
│   ├── backend_v2.0_broken.py  # Archive
│   ├── diagnose_defeatbeta.py  # Diagnostic tools
│   ├── diagnose_defeatbeta_v2.py
│   ├── diagnose_defeatbeta_v3.py
│   └── requirements.txt        # NEEDS UPDATE: add tradingview-screener
│
└── frontend/
    ├── node_modules/
    ├── public/
    ├── src/
    │   ├── services/
    │   │   ├── api.js          # API calls to backend
    │   │   └── api_day4.js     # Archive
    │   ├── utils/
    │   │   ├── rsCalculator.js     # ✅ RS calculation
    │   │   ├── scoringEngine.js    # ✅ 75-point scoring logic
    │   │   ├── scoringEngine_day4.js
    │   │   └── technicalIndicators.js
    │   ├── App.jsx             # ✅ Main UI component
    │   ├── App_day4.jsx        # Archive
    │   ├── index.js
    │   └── index.css
    ├── package.json
    └── package-lock.json
```

---

## 📋 ROADMAP (Updated)

### v1.0 - COMPLETE ✅
- Single stock manual entry
- 75-point scoring system
- Real-time prices (yfinance)
- Fundamentals (Defeat Beta)
- Quality gates
- 80% validation pass rate

### v1.1 - BACKEND COMPLETE ✅ | FRONTEND PENDING 🔄
**TradingView Screener Integration**
- ✅ Install `tradingview-screener` library
- ✅ Create `/api/scan/tradingview` endpoint
- ✅ 4 strategies with institutional-quality filters
- 🔄 **NEXT:** Frontend button "Scan for Opportunities"
- 🔄 **NEXT:** Display scan results in UI

**Also in v1.1:**
- EPS Growth stock split adjustment (AVGO 10:1 split issue)
- UI: Show both data sources indicator (low priority)

### v1.2 - PLANNED 📅
**Support & Resistance Engine**
- Multi-method approach: Pivot, KMeans, Volume Profile
- Fail-safe logic (always returns levels)
- Enables Entry/Stop/Target output

### v2.0 - FUTURE 🔮
- Pattern detection (VCP, cup-and-handle, flat base)
- Multi-timeframe analysis
- Real sentiment analysis
- Backtesting component

---

## ⚠️ Known Issues & Future Enhancements

### Resolved (Day 11)
- ~~TradingView Column syntax error~~ - Fixed: use `col()` not `Column()`
- ~~OTC junk tickers in results~~ - Fixed: exchange filter added
- ~~Moonshot/overbought stocks~~ - Fixed: RSI caps and momentum caps

### Pending
1. **EPS Growth stock split** - AVGO shows -62% due to 10:1 split (v1.1)
2. **Frontend scan button** - Need to add UI for batch scanning (v1.1)
3. **requirements.txt update** - Add `tradingview-screener==3.0.0`

---

## 🚀 Quick Commands

```bash
# Start backend
cd /Users/balajik/projects/swing-trade-analyzer/backend
source venv/bin/activate
python backend.py

# Start frontend
cd /Users/balajik/projects/swing-trade-analyzer/frontend
npm start

# Test TradingView endpoints
curl http://localhost:5001/api/scan/tradingview
curl "http://localhost:5001/api/scan/tradingview?strategy=minervini&limit=20"
curl "http://localhost:5001/api/scan/tradingview?strategy=momentum&limit=20"
curl "http://localhost:5001/api/scan/tradingview?strategy=value&limit=20"
curl http://localhost:5001/api/scan/strategies

# Git commands for Day 11
cd /Users/balajik/projects/swing-trade-analyzer
git add .
git commit -m "Day 11: TradingView screener integration - 4 strategies with institutional filters"
git push origin main
```

---

## 🔄 How to Resume (Day 12)

### Start Message
> "Resume swing trade analyzer - read PROJECT_STATUS_DAY11.md. Ready to build frontend scan button and results display."

### Day 12 Tasks
1. Add "Scan for Opportunities" button to frontend
2. Create scan results display component
3. Allow user to select strategy from dropdown
4. Click on candidate to analyze with full scoring
5. Update requirements.txt with tradingview-screener

---

## 💡 Key Learnings (Day 11)

1. **TradingView Screener uses `col()` not `Column()`** - Library syntax is `col('field') > value`
2. **Exchange filtering is critical** - Without it, OTC junk floods results
3. **RSI caps prevent chasing** - RSI < 75 filters overbought stocks
4. **Momentum caps filter moonshots** - 1M gain 5-50% removes parabolic moves
5. **Stage 2 is non-negotiable** - 50 SMA > 200 SMA ensures proper uptrend
6. **Market cap matters** - $2B+ for tradeable mid-caps, $5B+ for institutional

### Sample Quality Results (Day 11)
| Strategy | Sample Tickers | Quality |
|----------|----------------|---------|
| Reddit | GEV, DNLI | ✅ Mid-cap+ with volume |
| Minervini | PRAX | ✅ Momentum leader |
| Momentum | ALB | ✅ Sustainable gains |
| Value | JPM, XOM | ✅ Large-cap quality |

---

## 📚 Reference Resources

### APIs & Libraries
- **TradingView Screener:** https://shner-elmo.github.io/TradingView-Screener/
- **Defeat Beta:** https://github.com/defeat-beta/defeatbeta-api
- **yfinance:** https://github.com/ranaroussi/yfinance
- **GitHub Repo:** https://github.com/balacloud/swing-trade-analyzer

### TradingView Screener Syntax
```python
from tradingview_screener import Query, col

(Query()
 .select('name', 'close', 'volume')
 .where(
     col('market_cap_basic') > 1_000_000_000,
     col('close') > col('SMA50'),
     col('exchange').isin(['NASDAQ', 'NYSE'])
 )
 .order_by('volume', ascending=False)
 .limit(50)
 .get_scanner_data())
```

---

## 📄 Files Created This Session

| File | Purpose |
|------|---------|
| backend.py (v2.4) | Updated with TradingView screener endpoints |
| PROJECT_STATUS_DAY11.md | Session tracker (this file) |

---

*Last updated: December 11, 2025 - End of Day 11 session*
*Status: v1.1 Backend Complete | Frontend Scan UI Pending*
