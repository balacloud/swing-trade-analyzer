# 🎯 PROJECT STATUS - Day 21

> **Date:** January 3, 2026  
> **Version:** v1.3.2 (ATR/RSI fixed, TradingView OTC bug open)  
> **Stable Docs:** GOLDEN_RULES.md, API_CONTRACTS.md, KNOWN_ISSUES.md (in Claude Project)

---

## 📋 TODAY'S FOCUS

### Priority 1: Fix TradingView OTC Filter Bug
**Status:** 🟡 In Progress  
**File:** `backend/backend.py` (lines ~813-935)

**The Bug:**
- Scanner returns OTC stocks (SCGLF, SBGOF, TRAUF) instead of NYSE/NASDAQ
- Exchange filter `col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX'])` not working

**Diagnostic Finding (Day 20):**
```python
# Library returns correct values in isolation:
# NYSE: 409, NASDAQ: 337, AMEX: 216, OTC: 1
# Filter works standalone - bug is in query chain construction
```

**Fix Approach:**
1. Run diagnostic query with filter in isolation
2. Compare working vs broken query structure
3. Identify where filter gets lost
4. Fix incrementally

### Priority 2: Test RSI Function
**Status:** 🔵 Added Day 20, needs verification  
**File:** `frontend/src/utils/technicalIndicators.js`

---

## ✅ RECENT ACCOMPLISHMENTS

### Day 20
- ✅ Fixed ATR null for pivot method (`support_resistance.py`)
- ✅ Added calculateRSI function (`technicalIndicators.js`)
- ✅ Created TradingView scan endpoint (but OTC bug)
- ❌ TradingView filter not working (carried to Day 21)

### Day 19
- ✅ Tested 30 stocks (78.6% quality, 80.3% accuracy)
- ✅ Perplexity architecture review (validated methodology)
- ✅ Designed S&R Option C enhancement

### Day 18
- ✅ Fixed Analyze Stock UI (all N/A resolved)
- ✅ scoringEngine v2.1 clean API

---

## 🔴 ACTIVE BUGS (Working On)

| Bug | Status | Priority |
|-----|--------|----------|
| TradingView returns OTC | 🟡 In Progress | HIGH |
| S&R 0 support (17% stocks) | 🔴 Open | HIGH |
| S&R 0 resistance (10% stocks) | 🔴 Open | HIGH |

*Full issue list in KNOWN_ISSUES.md*

---

## 📅 NEXT STEPS (After TradingView Fixed)

1. **S&R Option C Enhancement** - Design ready, implement context-aware filter
2. **Forward Testing UI (v1.4)** - CRITICAL for system validation
3. **Test RSI end-to-end** - Verify it displays in UI

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

# Debug TradingView (run this FIRST)
python3 << 'EOF'
from tradingview_screener import Query, col

# Test 1: Without filter
print("=== WITHOUT FILTER ===")
count, df = Query().set_markets('america').select('name', 'exchange').limit(10).get_scanner_data()
print(df[['name', 'exchange']].to_string())

# Test 2: With filter
print("\n=== WITH FILTER ===")
count2, df2 = Query().set_markets('america').select('name', 'exchange').where(col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX'])).limit(10).get_scanner_data()
print(df2[['name', 'exchange']].to_string())
EOF

# Test current endpoint (shows OTC bug)
curl -s "http://localhost:5001/api/scan/tradingview?strategy=reddit&limit=5" | python3 -m json.tool
```

---

## 📁 FILES TO MODIFY TODAY

| File | Reason |
|------|--------|
| `backend/backend.py` | Fix TradingView filter |

*Request current file before modifying!*

---

## 💡 SESSION REMINDER

```
CLAUDE SESSION REMINDER:
1. STOP before coding - understand the problem first
2. ASK for current file before modifying anything
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose - don't guess again
```

---

---

## 📚 STABLE DOCS UPDATE RULES

### When to Update Each Doc:

| Doc | Update When | Who Updates |
|-----|-------------|-------------|
| **KNOWN_ISSUES.md** | Bug fixed, new bug found, status change | Claude creates updated version at session end |
| **API_CONTRACTS.md** | API endpoint added/changed, data structure changed | Claude creates updated version when code changes |
| **GOLDEN_RULES.md** | New lesson learned, new rule needed | Claude creates updated version (rare) |

### Session End Checklist:
1. ✅ Create next day's PROJECT_STATUS_SHORT
2. ✅ Ask: "Did any bugs get fixed or found?" → Update KNOWN_ISSUES.md
3. ✅ Ask: "Did any APIs change?" → Update API_CONTRACTS.md
4. ✅ Ask: "Did we learn a new rule?" → Update GOLDEN_RULES.md
5. ✅ Provide git commit command

### How Updates Work:
- Claude creates the updated file in `/mnt/user-data/outputs/`
- User downloads and replaces the file in Claude Project
- User confirms update is done

---

*Stable reference docs in Claude Project: GOLDEN_RULES.md, API_CONTRACTS.md, KNOWN_ISSUES.md*
