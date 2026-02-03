# KNOWN ISSUES - Day 43

> **Purpose:** Track all known bugs, gaps, and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 43 (February 3, 2026) - Documentation Architecture Updated

---

## RESOLVED (Day 43)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Roadmap items getting lost | Created ROADMAP.md in stable/ | Now read at session start |
| Missing data source labels | Added to Technical, Sentiment, Risk/Macro | UI transparency |
| Defeat Beta error handling | Enhanced with specific error tracking | v2.13 |
| README out of date | Updated v3.4→v3.9 | 9 days of changes documented |

---

## DEFEAT BETA STATUS - WORKING

**Current Status (Day 42 verified):**
```
✅ Defeat Beta API: WORKING
✅ Version: 0.0.6
✅ Data Update: 2026-01-31
✅ .data attribute: EXISTS
✅ /api/fundamentals/AAPL: Returns dataQuality: "rich"
```

**Test Command (if issues recur):**
```bash
cd backend && source venv/bin/activate && python3 -c "
from defeatbeta_api.data.ticker import Ticker as DBTicker
ticker = DBTicker('AAPL')
inc = ticker.annual_income_statement()
print(f'Has .data: {hasattr(inc, \"data\")}')
print(f'Columns: {list(inc.data.columns[:3])}')
"
```

---

## VALIDATION MODULE - WORKING

- **Quality Score:** 92.3%
- **Accuracy Rate:** 100%
- **Tolerances:** Updated for methodology differences (Day 42)

---

## PENDING VALIDATION GATES

| Gate | Description | Status | Test Command |
|------|-------------|--------|--------------|
| G1 | Structural Stops Backtest | PENDING | `python backtest_technical.py --compare-stops` |
| G2 | ADX Value Validation | PENDING | Win rate comparison with ADX gating |
| G4 | 4H RSI Entry Timing | PENDING | Entry timing backtest |

---

## SCORING PLACEHOLDERS - TRACKED IN ROADMAP

| Component | Current State | Points | Roadmap |
|-----------|---------------|--------|---------|
| **Sentiment** | Hardcoded 5/10 | 10 pts (13%) | v4.4 |
| **Market Breadth** | Hardcoded 1/1 | 1 pt (1%) | v4.5 |

**UI shows explicit "placeholder" labels** (Day 42)

---

## OPEN ISSUES

### Priority: HIGH

#### 1. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance
- **Roadmap:** v4.0 Forward Testing UI
- **Solution:** Trade journal with R-multiple logging, SQN calculation

### Priority: MEDIUM

#### 2. Pattern Detection Not Implemented
- **Impact:** Missing VCP, cup-and-handle, flat base detection
- **Roadmap:** v4.2 Pattern Detection
- **Status:** Next session priority

#### 3. No Interactive Charts
- **Impact:** Users can't visualize S&R levels on charts
- **Roadmap:** v4.1 TradingView Lightweight Charts
- **Solution:** Free open-source charting library

---

## DEFERRED ITEMS

| Feature | Roadmap | Reason |
|---------|---------|--------|
| Options Tab | v4.3 | Needs Greeks calculation |
| Sector Rotation RRG | - | Complex, marginal v1 value |
| Candlestick Patterns | - | Low statistical accuracy |
| Sentiment Integration | v4.4 | After Forward Testing UI |
| Scoring Logic Review | v4.5 | After more backtest data |

---

## DOCUMENTATION ARCHITECTURE (Day 43)

**New File:** `docs/claude/stable/ROADMAP.md`
- Canonical source for all roadmap items
- Read at session start (added to CLAUDE_CONTEXT.md)
- Prevents losing track of planned features

**Startup Checklist Now Includes:**
1. GOLDEN_RULES.md
2. **ROADMAP.md** ← NEW
3. PROJECT_STATUS
4. KNOWN_ISSUES

---

## FILES MODIFIED (Day 43)

| File | Changes |
|------|---------|
| `README.md` | Comprehensive update v3.4→v3.9 |
| `frontend/src/App.jsx` | Data source labels (v3.9) |
| `backend/backend.py` | Defeat Beta error handling (v2.13) |
| `docs/claude/stable/ROADMAP.md` | NEW - Canonical roadmap |
| `docs/claude/CLAUDE_CONTEXT.md` | Added ROADMAP.md to checklist |

---

*Previous: KNOWN_ISSUES_DAY42.md*
*Next: KNOWN_ISSUES_DAY44.md*
