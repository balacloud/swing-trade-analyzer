# KNOWN ISSUES - Day 27

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 27 (January 13, 2026)

---

## RESOLVED (Day 26)

| Issue | Resolution | Commit |
|-------|------------|--------|
| ATR showing N/A | Fixed - wrong args to calculateATR (now passes highs/lows/closes) | 42221f46 |
| R:R showing ":1" when null | Added null check, shows "N/A" | ae59b536 |
| Scan prices $0.00 | Changed stock.close to stock.price | 886b4456 |
| Scan missing change % | Added change field to backend response | 886b4456 |
| Pullback guidance not showing | Added allSupport to api.js return | 886b4456 |
| Scanner noise (preferred, SPACs) | Added ticker filters | 886b4456 |

---

## OPEN ISSUES

### Priority: MEDIUM

#### 1. Sentiment Score Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 10 points potentially misallocated
- **Suggested Fix:** Implement actual sentiment analysis or remove from scoring

#### 2. Market Breadth Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Impact:** Risk score may be inaccurate
- **Suggested Fix:** Add NYSE advance/decline data

### Priority: LOW

#### 3. HOLD Verdict Needs Nuance
- **Issue:** HOLD (40-59) covers wide range
- **Suggestion:** Split into "HOLD - Strong" (55-59) vs "HOLD - Weak" (40-54)

#### 4. No Position Sizing Calculator
- **Issue:** User must manually calculate position size
- **Suggestion:** Add calculator based on account size and risk tolerance

---

## VALIDATION CONCERNS (For Day 27)

### Unvalidated Components
1. **Scoring accuracy** - Not compared to external sources
2. **S&R level accuracy** - Not validated against TradingView
3. **Fundamental data accuracy** - Defeat Beta vs actual
4. **Historical backtest** - No proof system works

### Potential Biases
1. Minervini criteria may be too strict for current market
2. RSI 50-75 range may miss some opportunities
3. Large-cap bias in "best" scanner

---

## TEST RESULTS (Day 26)

### Comprehensive 30-Stock Test
- API Success Rate: 100%
- ATR null rate: 0% (fixed)
- Fundamental null rate: 7% (ETFs only - expected)
- Zero support rate: 20% (by design - extended stocks)

### Scanner Test
- All 4 strategies working
- Ticker filters removing noise (preferred, SPACs, warrants)
- "Best" strategy returning 54 high-conviction candidates

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `scoringEngine.js` | Core scoring logic, placeholder scores |
| `backend.py` | API contracts, scanner filters |
| `support_resistance.py` | S&R calculation accuracy |
| `api.js` | Data transformation, field mapping |

---

*Previous: KNOWN_ISSUES_DAY26.md (if exists)*
*Next: KNOWN_ISSUES_DAY28.md*
