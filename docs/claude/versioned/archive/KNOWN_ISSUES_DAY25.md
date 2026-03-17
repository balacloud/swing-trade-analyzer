# KNOWN ISSUES & BUG TRACKER

> **Purpose:** Comprehensive issue tracking with status
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 25 (January 10, 2026)

---

## ISSUE SUMMARY

| Priority | Open | Fixed | Mitigated | Total |
|----------|------|-------|-----------|-------|
| Critical | 1 | 1 | 0 | 2 |
| High | 2 | 3 | 2 | 7 |
| Medium | 2 | 2 | 0 | 4 |
| Low | 4 | 0 | 0 | 4 |

---

## CRITICAL PRIORITY

### CRIT-1: System UNPROVEN
| Field | Value |
|-------|-------|
| Status | OPEN |
| Affected | Entire system |
| Since | Day 1 |
| Root Cause | No backtest or forward test ever run |
| Impact | Cannot validate 60-70% win rate claim |
| Fix Plan | Forward Testing UI (NEXT PRIORITY) |

**Day 23 Review:** "Stop adding features. Start proving the system works."

---

### CRIT-2: TradingView Returns OTC Stocks - FIXED
| Field | Value |
|-------|-------|
| Status | FIXED Day 21 |
| Root Cause | Multiple .where() calls replace filters in v3.0.0 |
| Fix | Consolidated all filters into single .where() call |

---

## HIGH PRIORITY

### HIGH-1: S&R Returns 0 Support - MITIGATED
| Field | Value |
|-------|-------|
| Status | MITIGATED Day 22 (Option D) |
| Affected | 17% of stocks (AVGO, TSLA, GOOGL, AMD, F) |
| Mitigation | Option D shows "NOT VIABLE - wait for pullback" |

---

### HIGH-2: S&R Returns 0 Resistance - MITIGATED
| Field | Value |
|-------|-------|
| Status | MITIGATED Day 22 (Option D) |
| Affected | 10% of stocks (NFLX, COIN, SMCI) |

---

### HIGH-3: Sentiment Is Placeholder
| Field | Value |
|-------|-------|
| Status | OPEN - DECISION NEEDED |
| Since | Day 1 |
| Impact | 13% of total score is fake (5/10 default) |
| Root Cause | Never implemented |

**Options:**
1. **Remove** - Reduce to 65-point system (honest)
2. **Fear & Greed Index** - `https://api.alternative.me/fng/` (free, market-wide)
3. **Earnings proximity** - Flag upcoming earnings as risk

---

### HIGH-4: ATR = null (Pivot Method) - FIXED
| Status | FIXED Day 20 |

---

### HIGH-5: RSI Always N/A - FIXED
| Status | FIXED Day 22 |

---

### HIGH-6: Risk/Macro Expand Crash
| Field | Value |
|-------|-------|
| Status | OPEN Day 23 |
| Affected | Score Breakdown -> Risk/Macro expand |
| Error | "Objects are not valid as a React child" |
| Root Cause | Rendering object `{score, max, aboveSma200}` directly |
| Fix | Update App.jsx rendering logic |
| Priority | Quick fix |

---

### HIGH-7: UX Confusion - Mixed Signals
| Field | Value |
|-------|-------|
| Status | OPEN Day 23 |
| Affected | Beginner users |
| Problem | AVOID (red) + VIABLE (green) confuses users |
| Root Cause | Two different questions being answered without explanation |
| Fix | Add unified "Bottom Line" summary section |

---

### HIGH-8: Backend Fundamentals Cache Stale - FIXED
| Field | Value |
|-------|-------|
| Status | FIXED Day 25 |
| Root Cause | Defeat Beta data cached indefinitely, no refresh |
| Impact | 93% of stocks returned null ROE/EPS until backend restart |
| Fix | Added TTL-based cache (1 hour) with /api/cache/clear endpoint |

**Day 25 Test Results:**
- Before restart: 28/30 stocks had null fundamentals
- After restart: 2/30 stocks had null fundamentals (ETFs only)

---

## MEDIUM PRIORITY

### MED-1: Fundamental Variance vs External Sources
| Status | BY DESIGN |
| Root Cause | Defeat Beta vs Finviz use different methodologies |

---

### MED-2: SQ Returns API Error
| Status | OPEN |
| Affected | SQ ticker only |
| Root Cause | yfinance data unavailable |

---

### MED-3: No Transaction Costs in Backtesting
| Status | OPEN (Future v2.1) |

---

### MED-4: ATR N/A in Analyze Stock UI
| Status | Day 22 |
| Note | Backend S&R ATR works, frontend calculation issue |

---

## LOW PRIORITY / BY DESIGN

| Issue | Status | Notes |
|-------|--------|-------|
| LOW-1: EPS Always Null | BY DESIGN | yfinance doesn't provide |
| LOW-2: ETF Fundamental = 0/20 | HANDLED Day 25 | ETFs now show special message |
| LOW-3: ETF Sector = "Unknown" | BY DESIGN | yfinance limitation |
| LOW-4: Bull Market Dependency | BY DESIGN | Minervini = Stage 2 only |

---

## VALIDATION TEST RESULTS

### Day 25: 30-Stock Comprehensive Test
| Metric | Before Restart | After Restart |
|--------|----------------|---------------|
| API Quality Score | 100% | 100% |
| Null ROE | 93% (28/30) | 7% (2/30) |
| Trade Viable YES | 60% (18/30) | 60% (18/30) |
| Zero Support Levels | 20% (6/30) | 20% (6/30) |

### Day 19: 30-Stock Validation
| Metric | Value |
|--------|-------|
| Quality Score | 78.6% |
| Accuracy Rate | 80.3% |
| Coverage Rate | 98.0% |

---

## DAY 25 FIX PRIORITIES

| # | Issue | Effort | Impact | Status |
|---|-------|--------|--------|--------|
| 1 | Backend cache stale | Medium | High | FIXED |
| 2 | ETF ticker handling | Low | Medium | FIXED |
| 3 | Extreme value context | Low | Medium | FIXED |
| 4 | Risk/Macro expand crash | Low | Medium | Open |
| 5 | Sentiment decision | Medium | High | Open |
| 6 | UX "Bottom Line" | Medium | High | Open |
| 7 | Forward Testing UI | High | CRITICAL | Open |

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| Day 25 | Fixed backend cache, added ETF handling, extreme value context |
| Day 24 | Reorganized docs, versioned format |
| Day 23 | Added HIGH-6 (Risk crash), HIGH-7 (UX confusion) |
| Day 22 | Mitigated HIGH-1, HIGH-2 with Option D |
| Day 21 | Fixed CRIT-2 (TradingView OTC) |

---

*This file is versioned by day. Current version: DAY25*
