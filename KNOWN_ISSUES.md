# 🔴 KNOWN ISSUES & BUG TRACKER

> **Purpose:** Comprehensive issue tracking with status  
> **Location:** Claude Project (not daily file)  
> **Last Updated:** Day 22 (January 6, 2026)

---

## 📊 ISSUE SUMMARY

| Priority | Open | Fixed | Mitigated | Total |
|----------|------|-------|-----------|-------|
| Critical | 1 | 1 | 0 | 2 |
| High | 1 | 2 | 2 | 5 |
| Medium | 2 | 2 | 0 | 4 |
| Low | 4 | 0 | 0 | 4 |

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
| Fix Plan | v1.4 - Forward Testing UI (NEXT PRIORITY) |
| Blocked By | Nothing - ready to build |

**Notes:**
- Perplexity review flagged this as CRITICAL gap
- System is "well-documented hypothesis" not proven edge
- Must complete before any live trading
- Day 22: Perplexity analysis reinforced this - 22 days ≠ 10 years experience

---

### CRIT-2: TradingView Returns OTC Stocks ✅ FIXED
| Field | Value |
|-------|-------|
| Status | ✅ FIXED Day 21 |
| Affected | Scan Market tab |
| Since | Day 18 (originally "returns HTML"), Day 20 (OTC bug) |
| Root Cause | Multiple `.where()` calls replace filters in v3.0.0 |
| Fix | Consolidated all filters into single `.where()` call per strategy |

---

## 🟠 HIGH PRIORITY

### HIGH-1: S&R Returns 0 Support (Extended Stocks) 🟢 MITIGATED
| Field | Value |
|-------|-------|
| Status | 🟢 MITIGATED Day 22 (Option D) |
| Affected | 5/30 stocks (17%): AVGO, TSLA, GOOGL, AMD, F |
| Since | Day 19 |
| Root Cause | 20% proximity filter too strict for extended stocks |
| Mitigation | Option D now shows "NOT VIABLE - wait for pullback" instead of N/A confusion |
| Full Fix | Not needed - Option D handles this correctly |

**Option D Behavior:**
- Stock >20% from support → Viability = "NO"
- Advice: "Extended X% from support - wait for pullback before entering"
- Entry/Stop show N/A (correct - don't trade extended stocks)

---

### HIGH-2: S&R Returns 0 Resistance (Beaten-Down Stocks) 🟢 MITIGATED
| Field | Value |
|-------|-------|
| Status | 🟢 MITIGATED Day 22 (Option D) |
| Affected | 3/30 stocks (10%): NFLX, COIN, SMCI |
| Since | Day 19 |
| Root Cause | 30% proximity filter too strict for beaten-down stocks |
| Mitigation | Option D still shows viability based on support distance |

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
| Status | ✅ FIXED Day 22 |
| Affected | All stocks |
| Root Cause | calculateRSI existed but wasn't imported/called in scoringEngine |
| Fix | Added import and call: `rsi: calculateRSI(prices, 14)` |
| Verified | RSI now shows values (e.g., AAPL: 36.8, NFLX: 28.7) |

---

## 🟡 MEDIUM PRIORITY

### MED-1: Fundamental Variance vs External Sources
| Field | Value |
|-------|-------|
| Status | ⚪ BY DESIGN |
| Affected | ~30% of stocks |
| Root Cause | Defeat Beta vs Finviz use different methodologies |
| Impact | Validation shows FAILs for D/E, Revenue Growth |

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

### MED-4: ATR N/A in Analyze Stock UI 🆕
| Field | Value |
|-------|-------|
| Status | 🟡 NEW Day 22 |
| Affected | Analyze Stock tab → Technical Indicators section |
| Root Cause | Unknown - frontend calculateATR may have issue |
| Note | Backend S&R ATR works fine (fixed Day 20) |
| Impact | Low - ATR shows in Trade Setup via S&R |

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

## 📊 30-STOCK TEST RESULTS

### Day 19 Validation Summary
| Metric | Value |
|--------|-------|
| Quality Score | 78.6% |
| Accuracy Rate | 80.3% |
| Coverage Rate | 98.0% |
| Stocks Tested | 30 |

### Day 22 Option D Viability Test
| Viability | Count | % | Stocks |
|-----------|-------|---|--------|
| YES | 21 | 70% | AAPL, NVDA, MSFT, META, JPM, PLTR, VOO, AMZN, INTC, DIS, KO, PEP, COST, WMT, NFLX, CRM, V, HD, LLY, COIN, SMCI |
| CAUTION | 2 | 7% | XOM, UNH |
| NO | 6 | 20% | AVGO, TSLA, GOOGL, AMD, BA, F |
| ERROR | 1 | 3% | SQ |

---

## 🗂 OPTION D IMPLEMENTATION (Day 22)

### What It Does
Simple Minervini-aligned trade viability assessment:
- **YES** (≤10% from support): Good setup, tight stop, FULL position
- **CAUTION** (10-20% from support): Wide stop, HALF position
- **NO** (>20% from support): Extended, do NOT enter

### Files Changed
| File | Change |
|------|--------|
| `support_resistance.py` | Added `assess_trade_viability()` function |
| `backend.py` | Added `tradeViability` to meta (line 776) |
| `App.jsx` | Added viability badge + advice banner |

### API Response
```json
"tradeViability": {
  "viable": "YES" | "CAUTION" | "NO",
  "support_distance_pct": 5.3,
  "advice": "Good setup - tight stop placement possible",
  "position_size_advice": "FULL - low risk entry",
  "stop_suggestion": 246.28
}
```

---

*This file lives in Claude Project - update when issues change status*
