# 🔴 KNOWN ISSUES & BUG TRACKER

> **Purpose:** Comprehensive issue tracking with status  
> **Location:** Claude Project (not daily file)  
> **Last Updated:** Day 21 (January 4, 2026)

---

## 📊 ISSUE SUMMARY

| Priority | Open | Fixed | Total |
|----------|------|-------|-------|
| Critical | 1 | 1 | 2 |
| High | 3 | 2 | 5 |
| Medium | 1 | 2 | 3 |
| Low | 4 | 0 | 4 |

---

## 🔴 CRITICAL PRIORITY

### CRIT-1: System UNPROVEN
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN |
| Affected | Entire system |
| Since | Day 1 |
| Root Cause | No backtest or forward test ever run |
| Impact | Cannot validate 60-70% win rate claim |
| Fix Plan | v2.1 - Backtesting Framework |
| Blocked By | Forward Testing UI (v1.4) needed first |

**Notes:**
- Perplexity review flagged this as CRITICAL gap
- System is "well-documented hypothesis" not proven edge
- Must complete before any live trading

---

### CRIT-2: TradingView Returns OTC Stocks ✅ FIXED
| Field | Value |
|-------|-------|
| Status | ✅ FIXED Day 21 |
| Affected | Scan Market tab |
| Since | Day 18 (originally "returns HTML"), Day 20 (OTC bug) |
| Root Cause | Multiple `.where()` calls replace filters in v3.0.0 |
| Fix | Consolidated all filters into single `.where()` call per strategy |

**What Was Wrong:**
```python
# BROKEN: Second .where() replaced the first
query = query.where(col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']))
query = query.where(col('market_cap_basic') >= 2_000_000_000, ...)  # Overwrites!
```

**Fix Applied (Day 21):**
```python
# FIXED: All filters in ONE .where() call
query = query.where(
    col('exchange').isin(['NYSE', 'NASDAQ', 'AMEX']),
    col('market_cap_basic') >= 2_000_000_000,
    ...
)
```

---

## 🟠 HIGH PRIORITY

### HIGH-1: S&R Returns 0 Support (Extended Stocks)
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN |
| Affected | 5/30 stocks (17%): AVGO, TSLA, GOOGL, AMD, F |
| Since | Day 19 |
| Root Cause | 20% proximity filter too strict for extended stocks |
| Impact | Entry/Stop = null, trade setup breaks |

**Example:**
| Ticker | Current | 20% Floor | Highest Support | Gap |
|--------|---------|-----------|-----------------|-----|
| AVGO | $346 | $276.80 | $217.54 | 21% below floor |
| TSLA | $455 | $363.86 | $288.77 | 21% below floor |
| GOOGL | $314 | $251.14 | $161.75 | 36% below floor |

**Fix Plan:** S&R Option C Enhancement (design ready)

---

### HIGH-2: S&R Returns 0 Resistance (Beaten-Down Stocks)
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN |
| Affected | 3/30 stocks (10%): NFLX, COIN, SMCI |
| Since | Day 19 |
| Root Cause | 30% proximity filter too strict for beaten-down stocks |
| Impact | Target = null, R:R cannot be calculated |

**Example:**
| Ticker | Current | 30% Ceiling | Lowest Resistance | Gap |
|--------|---------|-------------|-------------------|-----|
| NFLX | $94 | $122.27 | $124.86 | 2% above ceiling |
| COIN | $228 | $296.89 | $351.89 | 19% above ceiling |

**Fix Plan:** S&R Option C Enhancement (design ready)

---

### HIGH-3: Sentiment Is Placeholder
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN |
| Affected | All stocks |
| Since | Day 1 |
| Root Cause | Never implemented - gives default 5/10 points |
| Impact | 13% of total score is meaningless |

**Options:**
1. Remove sentiment from scoring (reduce to 65 points)
2. Implement real sentiment (news API, social sentiment)
3. Keep as-is with clear disclaimer

---

### HIGH-4: ATR = null (Pivot Method) ✅ FIXED
| Field | Value |
|-------|-------|
| Status | ✅ FIXED Day 20 |
| Affected | 8+ stocks using pivot method |
| Root Cause | ATR only calculated when projecting levels |
| Fix | ATR now always calculated in compute_sr_levels() |

---

### HIGH-5: RSI Always N/A ✅ FIXED
| Field | Value |
|-------|-------|
| Status | ✅ FIXED Day 20 |
| Affected | All stocks |
| Root Cause | calculateRSI function didn't exist |
| Fix | Added calculateRSI to technicalIndicators.js |
| Note | Needs testing to verify it works end-to-end |

---

## 🟡 MEDIUM PRIORITY

### MED-1: Fundamental Variance vs External Sources
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Affected | ~30% of stocks |
| Root Cause | Defeat Beta vs Finviz use different methodologies |
| Impact | Validation shows FAILs for D/E, Revenue Growth |

**Examples:**
- NVDA debt_equity: Defeat Beta 0.13 vs Finviz 0.09 (44% variance)
- NVDA revenue_growth: Defeat Beta 114% vs Finviz 62% (83% variance)

**Resolution:** Acceptable variance - different data sources calculate differently

---

### MED-2: SQ Returns API Error
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN |
| Affected | SQ ticker only |
| Root Cause | yfinance data unavailable |
| Impact | Cannot analyze SQ |

---

### MED-3: No Transaction Costs in Backtesting
| Field | Value |
|-------|-------|
| Status | 🔴 OPEN (Future) |
| Affected | Backtesting results |
| Root Cause | Not implemented |
| Impact | Will inflate backtest returns |
| Fix Plan | v2.1 - Add to backtesting framework |

---

## 🟢 LOW PRIORITY / BY DESIGN

### LOW-1: EPS Always Null
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Root Cause | yfinance doesn't provide EPS field |
| Impact | Validation shows WARNING |
| Resolution | Acceptable - use other fundamental metrics |

---

### LOW-2: ETF Fundamental = 0/20
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Root Cause | ETFs don't have EPS/Revenue/ROE |
| Impact | VOO, SPY show 0/20 fundamental score |
| Resolution | Expected behavior |

---

### LOW-3: ETF Sector = "Unknown"
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Root Cause | yfinance doesn't return sector for ETFs |
| Resolution | Expected behavior |

---

### LOW-4: Bull Market Dependency
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Root Cause | Minervini methodology only trades Stage 2 uptrends |
| Impact | System underperforms in bear markets |
| Resolution | By design - document clearly |

---

## 📊 30-STOCK TEST RESULTS (Day 19)

### Summary
| Metric | Value |
|--------|-------|
| Quality Score | 78.6% |
| Accuracy Rate | 80.3% |
| Coverage Rate | 98.0% |
| Stocks Tested | 30 |

### S&R Status Breakdown
| Status | Count | % | Tickers |
|--------|-------|---|---------|
| ✅ Fully Working | 18 | 60% | AAPL, NVDA, MSFT, META, JPM, XOM, PLTR, VOO, AMZN, INTC, DIS, KO, PEP, COST, WMT, HD, LLY, BA |
| ⚠️ ATR null | 4 | 13% | CRM, UNH, V + others → **FIXED** |
| ⚠️ No Resistance | 3 | 10% | NFLX, COIN, SMCI |
| ❌ No Support | 5 | 17% | AVGO, TSLA, GOOGL, AMD, F |
| ❌ API Error | 1 | 3% | SQ |

### Stocks Tested
- **Batch 1:** AAPL, NVDA, AVGO, MSFT, META, TSLA, JPM, XOM, PLTR, VOO
- **Batch 2:** GOOGL, AMZN, AMD, INTC, BA, DIS, KO, PEP, COST, WMT
- **Batch 3:** NFLX, CRM, UNH, V, HD, LLY, COIN, SMCI, F, SQ

---

## 🏗️ S&R OPTION C DESIGN (Ready to Implement)

### Problem
20% proximity filter works correctly but creates poor UX for edge cases.

### Solution: Context-Aware S&R
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

### Benefits
- No more N/A - Always shows nearest levels with context
- Educational - Explains WHY entry isn't recommended
- Works for all stock states

---

*This file lives in Claude Project - update when issues change status*
