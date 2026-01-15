# KNOWN ISSUES - Day 28

> **Purpose:** Track all known bugs and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 28 (January 14, 2026)

---

## RESOLVED (Day 27)

| Issue | Resolution | Notes |
|-------|------------|-------|
| Scoring accuracy unknown | Backtest completed - 49.7% win rate | System is essentially random |
| No simplified alternative | Created 4-criteria binary system | `simplifiedScoring.js` |
| No historical validation | Created backtest scripts | `backtest_technical.py`, `backtest_simplified.py` |

---

## CRITICAL FINDINGS (Day 27)

### System Validation Results

| Metric | 75-Point System | Simplified System | Random |
|--------|-----------------|-------------------|--------|
| Win Rate | 49.7% | 51.7% | 50% |
| Profit Factor | 1.40 | 1.43 | 1.0 |
| Trades (5 years) | 310 | 29 | - |

**Conclusion:** Neither system significantly beats random. Profitability comes from R:R math (10% target, 7% stop), not signal quality.

### Key Discovery: Wrong Optimization Target
- **Entry signals:** ~10% of trading results
- **Position sizing:** ~90% of trading results
- **We optimized:** Entry signals for 27 days
- **We ignored:** Position sizing, R-multiples, expectancy

---

## OPEN ISSUES

### Priority: HIGH (Architectural Gap)

#### 1. No Position Sizing Calculator
- **Impact:** User cannot determine proper position size
- **Status:** Building Day 28 (Phase 1)
- **Solution:** Settings tab + Position calculator based on Van Tharp principles

#### 2. No Trade Journal / R-Multiple Tracking
- **Impact:** Cannot measure actual system performance
- **Status:** Deferred to Phase 2
- **Solution:** Trade journal with R-multiple logging and expectancy calculation

### Priority: MEDIUM (Existing Placeholders)

#### 3. Sentiment Score Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Always returns 5/10 for all stocks
- **Impact:** 10 points potentially misallocated (13% of score is fake)
- **Decision:** Keep in legacy system; simplified system ignores this

#### 4. Market Breadth Placeholder
- **File:** `scoringEngine.js`
- **Issue:** Market breadth score is hardcoded
- **Decision:** Keep in legacy system; simplified system ignores this

### Priority: LOW

#### 5. HOLD Verdict Needs Nuance
- **Issue:** HOLD (40-59) covers wide range
- **Status:** Low priority - focus on position sizing first

---

## BACKTEST INSIGHTS

### Counter-Intuitive Finding
Higher technical scores performed WORSE:
- Scores 30-34: 51.7% win rate
- Scores 35-39: 43.1% win rate

**Hypothesis:** Over-optimization leads to fewer opportunities and worse timing.

### What Actually Matters (Van Tharp Research)
1. **Position sizing** - How much to risk per trade
2. **R-multiples** - Measuring results relative to risk
3. **Expectancy** - (Win% × Avg Win R) + (Loss% × Avg Loss R)
4. **SQN** - System Quality Number for comparing systems

---

## VALIDATION STATUS

| Component | Status | Notes |
|-----------|--------|-------|
| Technical scoring | ✅ Validated | Does not predict outcomes |
| Simplified criteria | ✅ Validated | Similar to original, fewer trades |
| S&R levels | ⚠️ Not validated | Compare to TradingView |
| Fundamental data | ⚠️ Variance noted | Defeat Beta vs actual differs |
| Position sizing | ❌ Not built | Day 28 priority |

---

## FILES TO WATCH

| File | Reason |
|------|--------|
| `scoringEngine.js` | Legacy 75-point system (keep for reference) |
| `simplifiedScoring.js` | New 4-criteria binary system |
| `positionSizing.js` | To be created Day 28 |
| `Settings.jsx` | To be created Day 28 |
| `PositionCalculator.jsx` | To be created Day 28 |

---

## TEST RESULTS (Day 27)

### Backtest: 75-Point Technical System
```
Period: 2020-01-01 to 2024-12-31
Stocks: 28 (large/mid cap)
Total Trades: 310
Win Rate: 49.7%
Avg Return: 1.30%
Profit Factor: 1.40
Expectancy: 1.30%
```

### Backtest: Simplified Binary System
```
Period: 2020-01-01 to 2024-12-31
Stocks: 27
Total Trades: 29
Win Rate: 51.7%
Avg Return: 1.73%
Profit Factor: 1.43
Expectancy: 1.52%
```

---

*Previous: KNOWN_ISSUES_DAY27.md*
*Next: KNOWN_ISSUES_DAY29.md*
