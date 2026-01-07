# 🔴 KNOWN ISSUES & BUG TRACKER

> **Purpose:** Comprehensive issue tracking with status  
> **Location:** Claude Project (not daily file)  
> **Last Updated:** Day 23 (January 6, 2026)

---

## 📊 ISSUE SUMMARY

| Priority | Open | Fixed | Mitigated | Total |
|----------|------|-------|-----------|-------|
| Critical | 1 | 1 | 0 | 2 |
| High | 3 | 2 | 2 | 7 |
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

**Notes:**
- Day 23 holistic review reinforced this is THE critical gap
- "Stop adding features. Start proving the system works."

---

### CRIT-2: TradingView Returns OTC Stocks ✅ FIXED
| Field | Value |
|-------|-------|
| Status | ✅ FIXED Day 21 |
| Root Cause | Multiple .where() calls replace filters in v3.0.0 |
| Fix | Consolidated all filters into single .where() call |

---

## 🟠 HIGH PRIORITY

### HIGH-1: S&R Returns 0 Support 🟢 MITIGATED
| Status | 🟢 MITIGATED Day 22 (Option D) |
| Affected | 17% of stocks |
| Mitigation | Option D shows "NOT VIABLE - wait for pullback" |

### HIGH-2: S&R Returns 0 Resistance 🟢 MITIGATED
| Status | 🟢 MITIGATED Day 22 (Option D) |
| Affected | 10% of stocks |

### HIGH-3: Sentiment Is Placeholder 🔴
| Status | 🔴 OPEN |
| Impact | 13% of total score is fake (5/10 default) |
| Options | Remove (65-pt) OR implement Fear & Greed Index |

### HIGH-4: ATR = null (Pivot Method) ✅ FIXED Day 20

### HIGH-5: RSI Always N/A ✅ FIXED Day 22

### HIGH-6: Risk/Macro Expand Crash 🆕
| Status | 🔴 NEW Day 23 |
| Error | "Objects are not valid as a React child" |
| Root Cause | Rendering object {score, max, aboveSma200} directly |
| Fix | Update rendering logic in App.jsx |

### HIGH-7: UX Confusion - Mixed Signals 🆕
| Status | 🔴 NEW Day 23 |
| Problem | AVOID (red) + VIABLE (green) confuses beginners |
| Fix | Add unified "Bottom Line" summary section |

---

## 🟡 MEDIUM PRIORITY

### MED-1: Fundamental Variance ⚪ BY DESIGN
### MED-2: SQ Returns API Error 🔴 OPEN
### MED-3: No Transaction Costs 🔴 OPEN (Future)
### MED-4: ATR N/A in UI 🟡 Day 22

---

## 🟢 LOW PRIORITY / BY DESIGN

- LOW-1: EPS Always Null ⚪
- LOW-2: ETF Fundamental = 0/20 ⚪
- LOW-3: ETF Sector = "Unknown" ⚪
- LOW-4: Bull Market Dependency ⚪

---

## 📊 DAY 23 HOLISTIC REVIEW KEY INSIGHT

> **"Stop adding features. Start proving the system works."**

---

*This file lives in Claude Project - update when issues change status*
