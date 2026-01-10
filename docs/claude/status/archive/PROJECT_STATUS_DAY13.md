# 🎯 SWING TRADE ANALYZER - PROJECT STATUS

> **Last Updated:** Day 13 (December 15, 2025)  
> **Status:** ✅ v1.2 S&R Backend Deployed | ⚠️ Tuning Needed  
> **Version:** 2.5 (Backend) / 2.1 (Frontend)  
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

## ✅ DAY 13 ACCOMPLISHMENTS

### Session Summary
1. **Reviewed S&R Engine Design**
   - Examined existing `support_resistance.py` from ChatGPT
   - Confirmed architecture is solid: Pivot → KMeans → Volume Profile failover
   - Minor fix: pandas deprecation (`ffill()` instead of `fillna(method="ffill")`)

2. **Integrated S&R Engine into Backend**
   - Added `support_resistance.py` to backend folder
   - Updated `backend.py` to v2.5 with new endpoint
   - Added graceful import fallback for S&R engine
   - Health check now shows `sr_engine_available`

3. **Created `/api/sr/<ticker>` Endpoint**
   - Returns support and resistance levels
   - Calculates suggested Entry, Stop, Target
   - Computes Risk/Reward ratio
   - Shows which method was used (pivot/kmeans/volume_profile)

4. **Tested S&R Endpoint**
   - AAPL test successful (endpoint working)
   - ⚠️ Issue discovered: returned 0 resistance levels
   - Used KMeans instead of Pivot method
   - Root cause: AAPL near all-time high, all historical levels are below current price

---

## ⚠️ S&R ENGINE ISSUE (Day 13)

### Test Result for AAPL
```json
{
  "ticker": "AAPL",
  "currentPrice": 278.28,
  "method": "kmeans",
  "support": [197.72, 211.89, 231.63, 249.16, 273.19],
  "resistance": [],
  "suggestedEntry": 273.19,
  "suggestedStop": 264.99,
  "suggestedTarget": null,
  "riskReward": null
}
```

### Analysis
1. **Why KMeans instead of Pivot?**
   - Likely pivot levels were too tightly packed (spacing check failed)
   - Or high volatility regime was detected

2. **Why 0 Resistance Levels?**
   - AAPL is near all-time high (~$278)
   - All historical price clusters are BELOW current price
   - Split logic: `resistance = [c for c in centers if c >= last]`
   - When price is at ATH, no historical levels qualify as resistance

3. **Fix Needed (Day 14)**
   - Add ATH edge case handling
   - When no resistance found, project levels above current price
   - Options:
     - Use 52-week high as resistance
     - Project based on ATR (e.g., current + 1.5*ATR)
     - Use round number psychology levels ($280, $285, $290)

---

## 📊 API ENDPOINTS (Complete)

| Endpoint | Description | Status |
|----------|-------------|--------|
| `/api/health` | Health check (shows all 4 data sources) | ✅ |
| `/api/stock/<ticker>` | Stock data + prices | ✅ |
| `/api/fundamentals/<ticker>` | Rich fundamentals (Defeat Beta) | ✅ |
| `/api/market/spy` | SPY data for RS calculation | ✅ |
| `/api/market/vix` | VIX for risk assessment | ✅ |
| `/api/scan/tradingview` | Batch scanning (4 strategies) | ✅ |
| `/api/scan/strategies` | List available strategies | ✅ |
| `/api/sr/<ticker>` | **NEW** Support & Resistance levels | ⚠️ Needs tuning |

---

## 🔧 Technical Details

### Backend (Flask - Port 5001)
- **Version:** 2.5
- **New Files:** `support_resistance.py`
- **New Dependency:** `scikit-learn` (for KMeans)
- **Data Sources:** 
  - yfinance (prices) - 15-30 MIN DELAY
  - defeatbeta-api (fundamentals) - WEEKLY UPDATES
  - tradingview-screener (batch scanning) - REAL-TIME
  - support_resistance (S&R levels) - LOCAL CALCULATION

### Frontend (React - Port 3000)
- **Version:** 2.1
- **No changes Day 13** - S&R frontend integration pending

---

## 📁 COMPLETE PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── .git/
├── .gitignore
├── README.md
├── debug_bundle.txt
├── Files_Archives/
│
├── backend/
│   ├── venv/
│   ├── backend.py                  # ✅ v2.5 - S&R endpoint added
│   ├── backend_v2.4_day12.py       # Backup
│   ├── support_resistance.py       # ✅ NEW - S&R engine
│   ├── backend_day4.py             # Archive
│   ├── backend_v2.0_broken.py      # Archive
│   ├── diagnose_defeatbeta.py
│   ├── diagnose_defeatbeta_v2.py
│   ├── diagnose_defeatbeta_v3.py
│   └── requirements.txt            # NEEDS UPDATE: add scikit-learn
│
└── frontend/
    ├── node_modules/
    ├── public/
    ├── src/
    │   ├── services/
    │   │   ├── api.js              # v2.1
    │   │   └── api_day4.js         # Archive
    │   ├── utils/
    │   │   ├── rsCalculator.js
    │   │   ├── scoringEngine.js
    │   │   └── technicalIndicators.js
    │   ├── App.jsx                 # v2.1
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

### v1.1 - COMPLETE ✅
- TradingView screener backend (Day 11)
- 4 strategies with institutional filters
- Frontend scan tab (Day 12)
- Click-to-analyze flow

### v1.2 - IN PROGRESS 🔄
**Support & Resistance Engine**
- ✅ Backend endpoint `/api/sr/<ticker>` deployed
- ✅ Multi-method approach (Pivot, KMeans, Volume Profile)
- ⚠️ **BUG:** Returns 0 resistance for stocks at ATH
- 🔄 Fix ATH edge case
- 🔄 Frontend integration to display Entry/Stop/Target
- 🔄 EPS Growth stock split adjustment

### v2.0 - FUTURE 🔮
- Pattern detection (VCP, cup-and-handle, flat base)
- Multi-timeframe analysis
- Real sentiment analysis
- Backtesting component

---

## ⚠️ Known Issues & Pending Work

### Critical (Day 14 Priority)
1. **S&R resistance edge case** - Stocks at ATH return empty resistance array
   - Need fallback: project resistance above current price
   - Options: 52w high, ATR-based, round numbers

### Pending (v1.2)
2. **Frontend S&R integration** - Display Entry/Stop/Target in UI
3. **EPS Growth stock split** - AVGO shows -62% due to 10:1 split

### Low Priority
4. **UI data source indicator** - Show yfinance delay, Defeat Beta weekly

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

# Test S&R endpoint
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/sr/NVDA
curl http://localhost:5001/api/sr/JPM

# Check health (should show sr_engine_available: true)
curl http://localhost:5001/api/health

# Git commands for Day 13
cd /Users/balajik/projects/swing-trade-analyzer
git add .
git commit -m "Day 13: S&R Engine backend integration - v2.5"
git push origin main
```

---

## 🔄 How to Resume (Day 14)

### Start Message
> "Resume swing trade analyzer - read PROJECT_STATUS_DAY13.md. Priority: fix S&R resistance edge case for stocks at ATH."

### Day 14 Tasks (Priority Order)
1. **Fix S&R ATH edge case** - Add fallback when resistance is empty
2. **Test with multiple stocks** - Verify pivot vs kmeans selection
3. **Frontend S&R integration** - Display Entry/Stop/Target
4. Update requirements.txt with scikit-learn

---

## 💡 Key Learnings (Day 13)

1. **S&R engine architecture is sound** - Pivot → KMeans → Volume Profile failover works
2. **ATH edge case not handled** - When stock is at all-time high, no historical resistance exists
3. **KMeans fallback triggered** - Likely due to tight pivot spacing at high prices
4. **Need resistance projection** - For ATH stocks, must project future levels (ATR, round numbers)
5. **scikit-learn required** - Must add to requirements.txt

### S&R Method Selection Logic
| Condition | Method Used |
|-----------|-------------|
| Normal volatility, good spacing | Pivot |
| High volatility OR tight pivot spacing | KMeans |
| KMeans fails | Volume Profile |
| Ultimate fallback | Last close as magnet |

---

## 📄 Files Created/Modified This Session

| File | Action | Purpose |
|------|--------|---------|
| support_resistance.py | Created | S&R engine with 3 methods |
| backend.py | Modified | v2.5 with /api/sr endpoint |
| backend_v2.4_day12.py | Created | Backup of previous version |
| PROJECT_STATUS_DAY13.md | Created | Session tracker (this file) |

---

## 📚 S&R Engine Reference

### API Response Structure
```json
{
  "ticker": "AAPL",
  "currentPrice": 278.28,
  "method": "pivot|kmeans|volume_profile",
  "support": [level1, level2, ...],
  "resistance": [level1, level2, ...],
  "suggestedEntry": 273.19,
  "suggestedStop": 264.99,
  "suggestedTarget": null,
  "riskReward": 1.5,
  "dataPoints": 260,
  "timestamp": "2025-12-15T..."
}
```

### Configuration Defaults (SRConfig)
```python
min_bars: 150
pivot_left: 5
pivot_right: 5
pivot_max_levels: 5
pivot_min_spacing_frac: 0.0025  # 0.25% of price
kmeans_clusters: 5
volatility_threshold: 0.08  # 8%
volume_bins: 40
```

---

*Last updated: December 15, 2025 - End of Day 13 session*
*Status: v1.2 S&R Backend Deployed | ATH Edge Case Bug Identified*
