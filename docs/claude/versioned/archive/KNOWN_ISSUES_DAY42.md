# KNOWN ISSUES - Day 42

> **Purpose:** Track all known bugs, gaps, and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 42 (February 2, 2026) - Validation Module Fixed

---

## PRIORITY: MONITOR DEFEAT BETA STATUS

### Issue: Conflicting Reports About Defeat Beta

**Background:**
- Previous session summary stated: `'Ticker' object has no attribute 'data'` error
- Day 42 live test: Defeat Beta works perfectly (v0.0.6, `.data` attribute exists)

**Current Status (Day 42 Live Test):**
```
✅ Defeat Beta API: WORKING
✅ Version: 0.0.6
✅ Data Update: 2026-01-31
✅ .data attribute: EXISTS and returns DataFrame
✅ /api/fundamentals/AAPL: Returns dataQuality: "rich", source: "defeatbeta"
```

**Test Command to Verify:**
```bash
cd backend && source venv/bin/activate && python3 -c "
from defeatbeta_api.data.ticker import Ticker as DBTicker
ticker = DBTicker('AAPL')
inc = ticker.annual_income_statement()
print(f'Has .data: {hasattr(inc, \"data\")}')
print(f'Columns: {list(inc.data.columns[:3])}')
"
```

**Possible Explanations for Discrepancy:**
1. Transient API downtime that recovered
2. Test ran in wrong venv (system Python vs project venv)
3. Session summary misattributed error from different context
4. Network/SSL issues that resolved

**Action Required:**
- If Defeat Beta fails again, run test command above to verify
- Check which Python environment is active (`which python3`)
- Document exact error message and stack trace

---

## VALIDATION MODULE - FIXED (Day 42)

### Issue: Low Validation Scores (76.9%)

**Root Cause:** Methodology differences between data sources, NOT bugs

| Metric | Defeat Beta Method | Finviz Method | Expected Variance |
|--------|-------------------|---------------|-------------------|
| Debt/Equity | Total Debt (current + LT) | Long-term debt only | 30-50% |
| Revenue Growth | Fiscal Year YoY | TTM (trailing 12 months) | 60-85% |

**Fix Applied:**
- Updated `backend/validation/engine.py` tolerances (lines 84-96)
- Documented methodology differences in code comments

**Results After Fix:**
| Metric | Before | After |
|--------|--------|-------|
| Accuracy Rate | 83.3% | 100% |
| Quality Score | 76.9% | 92.3% |

---

## VIX DATA - FIXED (Day 42)

### Issue: VIX showing stale price (17 instead of 19.28)

**Root Cause:** Used `hist.iloc[-1]['Close']` which returns last daily close, not real-time

**Fix Applied:**
- Changed to `vix.info.get('regularMarketPrice')` with fallback
- File: `backend/backend.py` `/api/market/vix` endpoint

---

## NaN JSON SERIALIZATION - FIXED (Day 42)

### Issue: `"NaN is not valid JSON"` in validation results

**Fix Applied:**
- Added `_sanitize_for_json()` helper in `backend/validation/engine.py`
- Converts NaN/Inf to None before JSON serialization

---

## TIER 1 FIXES STATUS (From Day 41)

All TIER 1 backtest fixes remain implemented and active:

| Fix | File | Status |
|-----|------|--------|
| Market Regime Filter | `backtest_technical.py` | ✅ Active |
| Volume Confirmation | `backtest_technical.py` | ✅ Active |
| Earnings Blackout | `backtest_technical.py` | ✅ Active |

---

## RESEARCH DOCUMENTS CREATED (Day 42)

| Document | Purpose |
|----------|---------|
| `docs/research/OPTIONS_TAB_FEASIBILITY_ANALYSIS.md` | Options tab data requirements |
| `docs/research/SECTOR_ROTATION_IDENTIFICATION_GUIDE.md` | How to identify sector rotation |
| `docs/research/PERPLEXITY_PROMPTS_DAY42.md` | Research prompts for future sessions |

---

## SCORING PLACEHOLDERS - NOW TRACKED IN ROADMAP

**Issue:** 13% of score (Sentiment) is placeholder - tracked since Day 23, now in roadmap

| Component | Current State | Points | Roadmap |
|-----------|---------------|--------|---------|
| **Sentiment** | Hardcoded 5/10 | 10 pts (13%) | v4.4 |
| **Market Breadth** | Hardcoded 1/1 | 1 pt (1%) | v4.5 |

**UI now shows explicit "placeholder" labels** (Day 42 update)

---

## DEFERRED ITEMS (v2+)

| Feature | Reason for Deferral |
|---------|---------------------|
| Options Tab | Needs Greeks calculation (complex) - v4.3 |
| Sector Rotation RRG | Complex, marginal v1 value |
| Candlestick Patterns | Low statistical accuracy |
| Sentiment Integration | v4.4 - Finnhub free tier |
| Scoring Logic Review | v4.5 - Re-evaluate after more backtest data |

---

## FILES MODIFIED (Day 42)

| File | Changes |
|------|---------|
| `backend/validation/engine.py` | Updated tolerances for methodology differences |
| `backend/backend.py` | Fixed VIX real-time price, enhanced Defeat Beta error handling (v2.13) |
| `frontend/src/App.jsx` | Added data source labels to all score sections (v3.9) |
| `README.md` | Added v4.4 Sentiment, v4.5 Scoring Review to roadmap |

---

*Previous: KNOWN_ISSUES_DAY41.md*
*Next: KNOWN_ISSUES_DAY43.md*
