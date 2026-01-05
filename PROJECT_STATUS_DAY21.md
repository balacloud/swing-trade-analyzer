# 🎯 SWING TRADE ANALYZER - PROJECT STATUS

> **Last Updated:** Day 21 (January 3, 2026)  
> **Status:** 🔧 v1.3.2 - ATR/RSI Fixed, TradingView OTC Bug In Progress  
> **Version:** 2.9 (Backend) / 2.4 (Frontend)  
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
9. **GENERATE FILES ONE AT A TIME** - Wait for user confirmation before next file
10. **FOLLOW CODE ARCHITECTURE RULES** - See section below
11. **DEBUG APIS PROPERLY** - Run diagnostic queries FIRST before writing fixes (Added Day 20)

### 🔄 SESSION STARTUP CHECKLIST (For Claude)
When user starts a new session:
1. ✅ Read this PROJECT_STATUS file (user will attach it)
2. ✅ Memory is persistent - no need to reload unless user asks
3. ✅ Verify context by summarizing current state to user
4. ✅ Ask: "What would you like to focus on today?"
5. ❌ Do NOT ask user to re-explain the project
6. ❌ Do NOT ask for files unless you need to modify them
7. ❌ Do NOT jump to fixing - understand the problem first

### 📋 SESSION CLOSE CHECKLIST (For Claude)
When user says "session ending" or "close session":
1. ✅ Create PROJECT_STATUS_DAY[N+1].md - CARRY FORWARD ALL CONTEXT
2. ✅ Update Claude Memory if significant changes
3. ✅ Provide git commit command
4. ✅ Note any deferred tasks for next session
5. ✅ Ensure file versions are updated
6. ✅ Preserve API contracts, project structure, architecture rules

### ⚠️ CLAUDE SESSION REMINDER (Paste at start of each session)
```
CLAUDE SESSION REMINDER:
1. STOP before coding - understand the problem first
2. ASK for current file before modifying anything
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose - don't guess again
6. At end, create PROJECT_STATUS with ALL context preserved
```

---

## 🏗️ CODE ARCHITECTURE RULES (Day 18+)

### Best Practices for Code Generation:
1. **Verify data contracts BEFORE writing code** - Check actual return structures before writing consuming code
2. **Document API contracts** - Each module's input/output should be documented in comments
3. **Producer defines API** - Data producer (e.g., scoringEngine) defines the structure; consumer (e.g., App.jsx) adapts to it
4. **Don't double-calculate** - If scoringEngine calculates RS, don't recalculate in App.jsx and overwrite
5. **Test incrementally** - Verify each change works before proceeding to next
6. **Clean separation of concerns** - UI should not need to know internal implementation details
7. **Flat API structures preferred** - `scores.technical` is better than `breakdown.technical.score`

### Why These Rules Exist:
- Day 18 bug was caused by UI assuming field names that didn't exist in scoringEngine
- App.jsx was overwriting scoringEngine's properly-mapped rsData with raw rsCalculator output
- Resulted in N/A values throughout the Analyze Stock tab
- Root cause: Lack of verified data contracts between modules

### Debugging Rules (Added Day 20):
- **ALWAYS run diagnostic queries FIRST** before writing fixes
- **Never assume library behavior** - verify actual return values
- **If fix fails, STOP** - diagnose root cause, don't chain guesses

---

## 📊 CURRENT SYSTEM STATUS

### What's WORKING ✅
| Component | Status | Confidence | Last Verified |
|-----------|--------|------------|---------------|
| Single stock analysis (Analyze Stock tab) | ✅ Working | HIGH | Day 18 |
| 75-point scoring system | ✅ Working | HIGH | Day 18 |
| Relative Strength calculation | ✅ Working | HIGH | Day 18 |
| S&R detection (basic) | ✅ Working | MEDIUM | Day 19 |
| Validation engine | ✅ Working | HIGH | Day 19 |
| Backend API | ✅ Working | HIGH | Day 20 |
| ATR calculation (all methods) | ✅ Fixed | HIGH | Day 20 |
| RSI calculation | ✅ Added | NEEDS TEST | Day 20 |

### What's BROKEN ❌
| Component | Status | Since | Root Cause |
|-----------|--------|-------|------------|
| TradingView Scanner | ❌ Returns OTC stocks | Day 18 | Exchange filter not applied in query chain |
| S&R for extended stocks | ⚠️ 17% return 0 support | Day 19 | Proximity filter too strict |
| S&R for beaten-down stocks | ⚠️ 10% return 0 resistance | Day 19 | Proximity filter too strict |

### What's UNPROVEN ⚠️ (CRITICAL)
| Component | Status | Impact |
|-----------|--------|--------|
| System win rate | NO DATA - never backtested | Cannot validate 60-70% claim |
| Forward testing | NO DATA - UI not built | Cannot track real performance |
| Sentiment scoring | FAKE - placeholder 5/10 points | 13% of score is meaningless |

---

## 📈 CUMULATIVE PROGRESS

### Day 18: Analyze Stock UI Fixed
- Fixed scoringEngine API structure (flat scores object)
- Fixed rsData field name mapping
- Removed duplicate RS calculation in App.jsx
- All N/A values resolved in Analyze Stock tab

### Day 19: Comprehensive Testing & Architecture Review
- Tested 30 stocks across 3 batches
- 78.6% quality score, 80.3% accuracy, 98.0% coverage
- Perplexity critical analysis validated methodology
- Designed S&R Option C enhancement
- Documented all known issues with root causes

### Day 20: Quick Fixes (Partial)
- ✅ Fixed ATR null for pivot method
- ✅ Added calculateRSI function
- ✅ Created TradingView scan endpoint
- ❌ TradingView still returns OTC stocks (filter bug)

### Day 20 Key Diagnostic Finding:
```python
# TradingView library DOES return proper exchange values:
# NYSE: 409, NASDAQ: 337, AMEX: 216, CBOE: 37, OTC: 1
# The filter col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']) SHOULD work
# Bug is in how query chain applies the filter
```

---

## 📊 30-STOCK TEST RESULTS (Day 19)

### Validation Summary
| Metric | Batch 1 | Batch 2 | Batch 3 | Overall |
|--------|---------|---------|---------|---------|
| Quality Score | 80.3% | 78.7% | 76.9% | **78.6%** |
| Accuracy Rate | 82.5% | 80.7% | 77.6% | **80.3%** |
| Coverage Rate | 97.4% | 97.5% | 99.1% | **98.0%** |

### S&R Engine Results
| Status | Count | % | Tickers |
|--------|-------|---|---------|
| ✅ Fully Working | 18 | 60% | AAPL, NVDA, MSFT, META, JPM, XOM, PLTR, VOO, AMZN, INTC, DIS, KO, PEP, COST, WMT, HD, LLY, BA |
| ⚠️ ATR null (pivot) | 4 | 13% | CRM, UNH, V + others → **FIXED Day 20** |
| ⚠️ No Resistance | 3 | 10% | NFLX, COIN, SMCI |
| ❌ No Support | 5 | 17% | AVGO, TSLA, GOOGL, AMD, F |
| ❌ API Error | 1 | 3% | SQ |

### Stocks Tested
- **Batch 1:** AAPL, NVDA, AVGO, MSFT, META, TSLA, JPM, XOM, PLTR, VOO
- **Batch 2:** GOOGL, AMZN, AMD, INTC, BA, DIS, KO, PEP, COST, WMT
- **Batch 3:** NFLX, CRM, UNH, V, HD, LLY, COIN, SMCI, F, SQ

---

## 🔴 ALL KNOWN ISSUES

### Critical Priority
| # | Issue | Affected | Root Cause | Status |
|---|-------|----------|------------|--------|
| 1 | **System UNPROVEN** | Entire system | No backtest or forward test | 🔴 Open (v2.1) |
| 2 | **TradingView returns OTC** | Scan Market tab | Exchange filter not applied in query | 🟡 In Progress |

### High Priority
| # | Issue | Affected | Root Cause | Status |
|---|-------|----------|------------|--------|
| 3 | **S&R returns 0 support** | 5/30 stocks (17%) | Proximity filter too strict for extended stocks | 🔴 Open |
| 4 | **S&R returns 0 resistance** | 3/30 stocks (10%) | Proximity filter too strict for beaten-down | 🔴 Open |
| 5 | **Sentiment is placeholder** | All stocks | 10 points (13%) are fake | 🔴 Open |

### Medium Priority
| # | Issue | Affected | Root Cause | Status |
|---|-------|----------|------------|--------|
| 6 | ATR = null (pivot method) | 8+ stocks | ATR not calculated when pivot used | ✅ Fixed Day 20 |
| 7 | RSI always N/A | All stocks | Missing calculateRSI function | ✅ Fixed Day 20 |
| 8 | Fundamental variance | ~30% of stocks | Defeat Beta vs Finviz methodology | N/A (expected) |

### Low Priority / By Design
| # | Issue | Notes |
|---|-------|-------|
| 9 | EPS always null | yfinance limitation - acceptable |
| 10 | ETF Fundamental = 0 | Expected - ETFs have no fundamentals |
| 11 | Bull market dependency | By design (Minervini only trades Stage 2) |
| 12 | SQ returns API error | yfinance data unavailable for this ticker |

---

## 🏗️ S&R OPTION C DESIGN (Ready to Implement)

### Current Problem
The 20% proximity filter works correctly but creates poor UX:
- Extended stocks (AVGO, TSLA, GOOGL, AMD): All support >20% below → 0 support
- Beaten-down stocks (NFLX, COIN, SMCI): All resistance >30% above → 0 resistance

### Proposed Solution: Context-Aware S&R

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
1. **Always return nearest S&R** (no filter initially)
2. **Add `stockState` classification** - Color-coded badge
3. **Add `tradeAdvice`** - Human-readable guidance
4. **Add `entryViable` flag** - True/False/WAIT

### Benefits
- No more N/A - Always shows nearest levels with context
- Educational - Explains WHY entry isn't recommended
- Works for extended, beaten-down, and normal stocks

---

## 📋 ROADMAP

### v1.0 - COMPLETE ✅
- Single stock analysis, 75-point scoring

### v1.1 - COMPLETE ✅
- TradingView screener, 4 strategies

### v1.2 - COMPLETE ✅
- S&R Engine with proximity filter

### v1.2.2 - COMPLETE ✅ (Day 16)
- Validation Engine backend

### v1.3.0 - COMPLETE ✅ (Day 17)
- Validation UI tab
- Fundamentals merge fix (P/E now working)

### v1.3.1 - COMPLETE ✅ (Day 18)
- Fixed Analyze Stock UI (all N/A values resolved)
- scoringEngine v2.1 clean API

### v1.3.2 - IN PROGRESS 🔧 (Day 20-21)
- ✅ Fixed ATR null for pivot method
- ✅ Added calculateRSI function
- 🔧 TradingView OTC filter bug (in progress)

### v1.4 - NEXT 📅
- **Forward Testing UI** (CRITICAL)
- S&R Option C Enhancement
- Signal recording and tracking

### v2.0 - FUTURE 🔮
- Pattern detection (VCP, cup-and-handle)

### v2.1 - FUTURE 🔮 (CRITICAL PATH)
- **Backtesting Framework**
- Transaction cost model
- System validation

---

## 📁 PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # v2.9 (Day 20: TradingView endpoint)
│   ├── support_resistance.py       # Day 20: ATR always calculated
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── engine.py               # v3.1 - Fundamentals merge + tolerances
│   │   ├── scrapers.py             # v2 - StockAnalysis + Finviz
│   │   ├── comparators.py
│   │   ├── forward_tracker.py
│   │   └── report_generator.py
│   ├── validation_results/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # v2.4 - Fixed rsData overwrite
│   │   ├── services/api.js         # v2.3 - Validation endpoints
│   │   └── utils/
│   │       ├── scoringEngine.js    # v2.1 - Clean API structure
│   │       ├── rsCalculator.js     # Unchanged
│   │       └── technicalIndicators.js  # Day 20: Added calculateRSI
│   └── package.json
│
├── test_script.sh                  # Batch 1 test (Day 19)
├── test_script_batch2.sh           # Batch 2 test (Day 19)
├── test_script_batch3.sh           # Batch 3 test (Day 19)
└── README.md                       # Comprehensive docs (Day 19)
```

---

## 📊 API CONTRACT: scoringEngine.calculateScore()

```javascript
// INPUT
calculateScore(stockData, spyData, vixData)

// OUTPUT (v2.1)
{
  // Basic info
  ticker: string,
  name: string,
  sector: string,
  industry: string,
  
  // Price data
  currentPrice: number,
  fiftyTwoWeekHigh: number,
  fiftyTwoWeekLow: number,
  pctFromHigh: number,
  
  // Scores (FLAT - for UI)
  totalScore: number,
  maxScore: 75,
  scores: {
    technical: number,    // 0-40
    fundamental: number,  // 0-20
    sentiment: number,    // 0-10
    risk: number          // 0-5
  },
  
  // Verdict
  verdict: { verdict: string, reason: string, color: string },
  qualityGates: { passed: boolean, gates: [], criticalFails: number },
  
  // RS Data (normalized for UI)
  rsData: {
    rsRatio: number,        // Same as rs52Week
    rs52Week: number,
    rs13Week: number,
    rsRating: number,       // 0-99
    rsTrend: string,        // 'improving' | 'declining' | 'stable'
    stock52wReturn: number, // Percentage (e.g., 37.1)
    spy52wReturn: number,   // Percentage (e.g., 16.9)
    interpretation: string,
    passesQualityGate: boolean
  },
  
  // Technical indicators
  indicators: { sma50, sma200, ema8, ema21, atr, rsi, avgVolume50 },
  
  // Detailed breakdown (for debugging)
  breakdown: { technical, fundamental, sentiment, risk },
  
  timestamp: string
}
```

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

# Test TradingView (currently returning OTC - needs fix)
curl -s "http://localhost:5001/api/scan/tradingview?strategy=reddit&limit=5" | python3 -m json.tool

# Debug TradingView library directly
python3 << 'EOF'
from tradingview_screener import Query, col
count, df = Query().set_markets('america').select('name', 'exchange', 'close').where(col('exchange').isin(['NYSE', 'NASDAQ'])).limit(10).get_scanner_data()
print(df[['name', 'exchange']].to_string())
EOF

# Test S&R ATR (should work now - fixed Day 20)
curl http://localhost:5001/api/sr/GOOGL | python3 -m json.tool | grep atr

# Run validation
curl -X POST http://localhost:5001/api/validation/run \
  -H "Content-Type: application/json" \
  -d '{"tickers": ["AAPL","NVDA"]}'

# Test scripts (created Day 19)
./test_script.sh          # Batch 1: 10 stocks
./test_script_batch2.sh   # Batch 2: 10 stocks  
./test_script_batch3.sh   # Batch 3: 10 stocks
```

---

## 🔄 HOW TO RESUME (Day 22+)

### Start Message
> "Resume swing trade analyzer - read PROJECT_STATUS_DAY21.md"

### Paste This Reminder
```
CLAUDE SESSION REMINDER:
1. STOP before coding - understand the problem first
2. ASK for current file before modifying anything
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose - don't guess again
6. At end, create PROJECT_STATUS with ALL context preserved
```

---

## 📋 DAY 21 PRIORITIES

### Immediate
| # | Task | Complexity | Impact |
|---|------|------------|--------|
| 1 | **Fix TradingView OTC filter** | Medium | High |
| 2 | **Test RSI function** | Low | Low |

### After TradingView Fixed
| # | Task | Complexity | Impact |
|---|------|------------|--------|
| 3 | S&R Option C Enhancement | Medium | High |
| 4 | Forward Testing UI (v1.4) | Medium | CRITICAL |

### TradingView Debug Approach
1. Run diagnostic query in isolation (verify filter works)
2. Compare working query vs endpoint query structure
3. Identify where filter is lost in query chain
4. Fix and test incrementally

---

## 💡 KEY LEARNINGS (Cumulative)

### Day 18
1. Verify data contracts BEFORE writing UI code
2. Don't double-calculate - producer defines API
3. Check for overwrites in consuming code
4. Clean API > nested structures

### Day 19
1. Test extensively before fixing - 30 stocks revealed patterns
2. External review is valuable - Perplexity caught gaps
3. Document before fixing - understand root cause first
4. S&R filter works correctly - but UX needs improvement

### Day 20
1. **Debug before coding** - Run diagnostic queries first
2. **Don't chain failed attempts** - Stop, think, verify
3. **Library behavior ≠ assumptions** - Always verify actual values
4. **PROJECT_STATUS must carry forward ALL context**

---

## 📝 FILES MODIFIED HISTORY

### Day 20
| File | Change | Status |
|------|--------|--------|
| `backend/backend.py` | Added TradingView scan endpoint | ⚠️ OTC bug |
| `backend/support_resistance.py` | ATR always calculated for pivot | ✅ Fixed |
| `frontend/src/utils/technicalIndicators.js` | Added calculateRSI function | ✅ Added |

### Day 19
| File | Purpose |
|------|---------|
| `README.md` | Comprehensive project documentation |
| `test_script.sh` | Batch 1 test script |
| `test_script_batch2.sh` | Batch 2 test script |
| `test_script_batch3.sh` | Batch 3 test script |

### Day 18
| File | Version | Changes |
|------|---------|---------|
| `frontend/src/utils/scoringEngine.js` | v2.1 | Clean API structure |
| `frontend/src/App.jsx` | v2.4 | Removed duplicate RS calc |

---

## 📝 MISSING FILE COMMENTS (To Add)

**backend.py:**
```python
# Day 20: Added TradingView scan endpoint (exchange filter bug - to fix)
```

**support_resistance.py:**
```python
# Day 20: Fixed ATR always calculated for pivot method (was only added when projecting)
```

**technicalIndicators.js:**
```javascript
// Day 20: Added calculateRSI function using Wilder's smoothing method
```

---

*Last updated: January 3, 2026 - Start of Day 21 session*
*Status: v1.3.2 In Progress | ATR/RSI Fixed | TradingView OTC Bug Open*
*Next: Fix TradingView filter, then S&R Option C, then Forward Testing UI*
