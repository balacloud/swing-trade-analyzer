# Known Issues - Day 51 (February 11, 2026)

## Open Issues

*No open issues. All prior issues resolved in Day 49-50.*

---

## Pending Validation

### Pending: ADX/RSI Threshold Backtest
**Status:** BLOCKED (yfinance API down)
**Script:** `backend/backtest/backtest_adx_rsi_thresholds.py`
**Purpose:** Validate Perplexity research findings:
1. ADX < 20 + RSI > 70 = mean reversion expected
2. ADX > 25 + RSI > 70 = momentum continuation
3. RSI > 80 = 68% pullback rate within 14 days
4. RSI > 80 + strong trend = lower pullback rate
**Action:** Run when yfinance API recovers

---

## Design Changes (Day 51)

### Changed: v4.13 Holding Period Selector Plan
**Previous Approach:** Adjust RSI thresholds by holding period (40-65 / 35-70 / 30-75)
**Research Finding:** INVALIDATED - thresholds vary by ADX REGIME, not holding period
**New Approach:** Signal WEIGHTING by horizon:
- Quick swing (5-10d): 70% Technical, 30% Fundamental
- Standard (15-30d): 50% Technical, 50% Fundamental
- Position (1-3mo): 30% Technical, 70% Fundamental

**ADX-based RSI interpretation PRESERVED (already in v4.6.2):**
- ADX < 20: RSI > 70 = pullback likely
- ADX > 25: RSI > 70 = momentum confirmation

---

## Resolved Issues (Day 49-50)

| Issue | Fixed | Day |
|-------|-------|-----|
| Position Size Banner Conflict | v4.4 | Day 50 |
| No Retry Button for API Errors | v4.4 | Day 50 |
| Entry Cards Hidden Instead of Grayed | v4.4 | Day 50 |
| R:R = 1.0 Edge Case | v4.4 | Day 50 |
| VIABLE Badge + AVOID Conflict | v4.4 | Day 50 |
| "$null-null" Support Zone Bug | v4.3 | Day 49 |
| Entry Uses Wrong Support Level | v4.3 | Day 49 |
| Position "full" with "wait" Reason | v4.3 | Day 49 |
| Generic VIABLE Badge | v4.3 | Day 49 |
| R:R < 1.0 Not Filtered | v4.2 | Day 49 |
| ADX-Based Entry Logic | v4.2 | Day 49 |

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 0 |
| Open - Low | 0 |
| **Total Open** | **0** |
| Pending Validation | 1 (backtest) |
| Resolved (Day 49-51) | 11 |

---

## Lessons Learned (Day 51)

1. **Never implement without validation** (Golden Rule #15)
   - Original RSI thresholds by holding period were INVENTED
   - Sounded logical but research showed they were WRONG
   - Shorter periods need MORE extreme thresholds (15/85), not tighter (40-65)

2. **ADX regime > holding period for RSI interpretation**
   - ADX determines if RSI extremes mean reversal or continuation
   - Holding period determines which SIGNALS to weight more

3. **Kavout format is marketing, not research**
   - Assumed "if they use it, it's validated" - WRONG
   - Always require evidence before implementing
