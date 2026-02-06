# UI Test Report - Day 46

> **Date:** February 6, 2026
> **Version:** v4.6 (Backend v2.15)
> **Tester:** Claude Code (automated analysis)
> **Test Method:** Manual UI capture (10 PDF screenshots) + systematic analysis

---

## Executive Summary

**Overall Assessment: MOSTLY COHESIVE with 2 actionable issues**

| Category | Status |
|----------|--------|
| Categorical Assessment Display | ✅ PASS |
| Structure > Sentiment Hierarchy | ✅ PASS |
| F&G Threshold Fix (v4.6) | ✅ PASS |
| ETF Handling | ✅ PASS |
| Trade Setup / Entry Strategy | ⚠️ ISSUE |
| Recommendation Card Messaging | 🔴 CRITICAL ISSUE |
| Pattern Detection Display | ⚠️ PENDING (v4.6 #3) |

---

## Test Tickers

| # | Ticker | Type | Sector | Purpose |
|---|--------|------|--------|---------|
| 1 | AAPL | Stock | Technology | Baseline - quality stock |
| 2 | NVDA | Stock | Semiconductors | Weak technical (RSI oversold) |
| 3 | META | Stock | Communication | Below 200 SMA test |
| 4 | JPM | Stock | Financials | Sector diversity |
| 5 | GOOGL | Stock | Communication | Strong setup test |
| 6 | SPY | ETF | Index | ETF fundamental handling |
| 7 | TSLA | Stock | Consumer | Weak fundamentals test |
| 8 | IWM | ETF | Small Cap | ETF + 8/8 trend template |
| 9 | XLE | ETF | Energy | Sector ETF + overbought RSI |
| 10 | INTC | Stock | Semiconductors | Strong tech, weak fundamentals |

---

## Detailed Results

### Test 1: AAPL - Apple Inc.
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | HOLD | Correct |
| Technical | Strong (8/8, RSI 67.1) | ✅ |
| Fundamental | Decent | ✅ |
| Sentiment | Weak (F&G 33.7) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | WATCHLIST - MONITOR | ⚠️ See Issue #1 |
| Entry Strategy | Pullback PREFERRED @ $226.24 | ✅ |

**Issue**: Recommendation says "near support" but pullback entry is 18% below current price.

---

### Test 2: NVDA - NVIDIA Corporation
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Correct |
| Technical | Weak (6/8, RSI 34.3) | ✅ |
| Fundamental | Strong | ✅ |
| Sentiment | Weak (F&G 33.7) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |

**Assessment**: PASS - Weak technicals correctly override strong fundamentals.

---

### Test 3: META - Meta Platforms
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | HOLD | Correct |
| Technical | Decent (5/8, RSI 51.5) | ✅ |
| Fundamental | Strong | ✅ |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | NOT NOW - PATIENCE | ✅ |
| Alert Price | $573.36 | ✅ Matches pullback entry |
| Quality Warning | Below 200 SMA | ✅ |

**Assessment**: PASS - Excellent cohesion. Alert price matches preferred entry.

---

### Test 4: JPM - JP Morgan Chase
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Questionable |
| Technical | Decent (7/8, RSI 49.1) | ⚠️ See Issue #2 |
| Fundamental | Decent | ✅ |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |

**Issue**: 7/8 Trend Template but RSI 49.1 triggers "Decent" instead of "Strong". RSI threshold may be too narrow.

---

### Test 5: GOOGL - Alphabet Inc. ⭐
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | **BUY** | ✅ Correct |
| Technical | Strong (8/8, RSI 53.2) | ✅ |
| Fundamental | Strong | ✅ |
| Sentiment | Weak (F&G 33.5) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | READY TO TRADE | ✅ |
| Why This Verdict | "structure bullish despite fearful sentiment" | ✅ |
| Support Distance | 0.8% away | ✅ Truly "near support" |

**Assessment**: EXCELLENT - This is the model case. Structure > Sentiment working correctly.

---

### Test 6: SPY - S&P 500 ETF
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Correct |
| Technical | Weak (7/8, RSI 39.0) | ✅ |
| Fundamental | N/A | ✅ ETF handled |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |
| Backup Data Notice | Displayed | ✅ |

**Assessment**: PASS - ETF correctly shows N/A for fundamentals.

---

### Test 7: TSLA - Tesla Inc.
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Correct |
| Technical | Weak (6/8, RSI 34.3) | ✅ |
| Fundamental | Weak (ROE 4.6%, Rev -2.9%) | ✅ |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |

**Assessment**: PASS - All weak categories correctly trigger AVOID.

---

### Test 8: IWM - Russell 2000 ETF
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Correct |
| Technical | Decent (8/8, RSI 43.5) | ⚠️ See Issue #2 |
| Fundamental | N/A | ✅ ETF handled |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |

**Issue**: 8/8 Trend Template but RSI 43.5 triggers "Decent" instead of "Strong".

---

### Test 9: XLE - Energy Select Sector ETF
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | AVOID | Correct |
| Technical | Decent (8/8, RSI 71.2) | ✅ |
| Fundamental | N/A | ✅ ETF handled |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | SKIP THIS ONE | ✅ |
| Trade Setup | CAUTION (wide stop) | ✅ |
| VCP Status | at_pivot | Noted |

**Assessment**: PASS - RSI 71.2 (overbought) correctly prevents Strong technical.

---

### Test 10: INTC - Intel Corporation
| Field | Value | Assessment |
|-------|-------|------------|
| Verdict | HOLD | Correct |
| Technical | Strong (8/8, RSI 55.6) | ✅ |
| Fundamental | Weak (ROE -0.2%) | ✅ |
| Sentiment | Weak (F&G 33.8) | ✅ |
| Risk/Macro | Neutral | ✅ |
| Recommendation | WATCHLIST - MONITOR | ⚠️ See Issue #1 |
| Alert Price | $54.60 | ⚠️ This is resistance, not entry |
| Entry Strategy | Pullback PREFERRED @ $39.65 | ✅ |

**Issue**: Alert price ($54.60) is 52-week high resistance, but preferred entry is $39.65 (18% lower).

---

## Issues Summary

### 🔴 ISSUE #1: CRITICAL - Recommendation Card / Entry Mismatch

**Affected Tickers**: AAPL, INTC (and likely others with Pullback PREFERRED)

**Problem**:
- Recommendation card says "consider entry at current price" or "near support"
- But Entry Strategy shows Pullback PREFERRED at 15-20% below current price
- Alert prices sometimes show resistance instead of entry level

**User Impact**: Misleading guidance - user might enter at current price when system recommends waiting for pullback.

**Fix Required**:
```javascript
// In recommendation card logic
if (preferredEntry === 'Pullback' && pullbackEntryPrice < currentPrice * 0.9) {
  message = `Wait for pullback to ~$${pullbackEntryPrice.toFixed(2)}`;
  alertPrice = pullbackEntryPrice;
} else if (preferredEntry === 'Momentum') {
  message = 'Consider entry at current price';
  alertPrice = currentPrice;
}
```

---

### ⚠️ ISSUE #2: MEDIUM - RSI Range Too Narrow for Strong Technical

**Affected Tickers**: JPM (RSI 49.1), IWM (RSI 43.5)

**Problem**:
- RSI range 50-70 for "Strong" Technical is very narrow
- Stocks with perfect 8/8 Trend Template get "Decent" because RSI is 49.1

**Current Logic**: Strong = TT ≥ 7 AND RSI 50-70
**Proposed**: Strong = TT ≥ 7 AND RSI 40-75 (when TT = 8/8)

**Status**: DEFERRED - needs more data to validate

---

### ⚠️ ISSUE #3: LOW - Pattern Percentages < 80%

**Problem**: VCP 40%, Flat Base 65% shown but not actionable
**Per Perplexity Research**: Patterns < 80% have high false positive rate
**Status**: PENDING - v4.6 Recommendation #3

---

## Verdict Distribution

| Verdict | Count | % | Expected in Fear Market |
|---------|-------|---|-------------------------|
| BUY | 1 | 10% | ✅ Appropriately selective |
| HOLD | 3 | 30% | ✅ Quality stocks to watch |
| AVOID | 6 | 60% | ✅ Filtering working |

**Conclusion**: System correctly acts as FILTER in fearful market (F&G ~33).

---

## Recommendations

### Immediate (Day 46-47)
1. ~~**Fix Issue #1**: Align recommendation card message with preferred entry strategy~~ ✅ **FIXED**
2. ~~**Update alert prices**: Should match preferred entry, not resistance~~ ✅ **FIXED**

**Fix Applied (Day 46):** Updated `generateActionableRecommendation()` in [App.jsx](frontend/src/App.jsx#L398-L506):
- Uses `entryPreference` from categorical assessment
- When pullback preferred + entry >10% below → "Wait for pullback to $X"
- Alert price now uses support (entry level), not resistance

### Future (v4.7+)
3. **Evaluate Issue #2**: Consider wider RSI range for Strong when TT = 8/8
4. **Implement v4.6 #3**: Only show patterns ≥ 80% formed

---

## Test Environment

- **Frontend**: v4.6 (localhost:3000)
- **Backend**: v2.15 (localhost:5001)
- **Fear & Greed Index**: 33.5-33.8 (Weak/Fear)
- **Market Regime**: SPY above 200 EMA (Bull)
- **VIX**: ~20-22 (Neutral)

---

*Report generated: February 6, 2026*
*Updated: February 6, 2026 - Issue #1 Fixed*
