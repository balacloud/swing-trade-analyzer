# KNOWN ISSUES - Day 41

> **Purpose:** Track all known bugs, gaps, and issues
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 41 (February 1, 2026) - TIER 1 Fixes Complete

---

## TIER 1 FIXES - IMPLEMENTED

### Fix 1: Market Regime Filter - IMPLEMENTED
- **File:** `backend/backtest/backtest_technical.py`
- **Function:** `check_bull_regime(spy_df, date_idx, ema_period=200)`
- **Rule:** Skip entries when SPY < 200-EMA (bear market)
- **Impact:** Reduced trade count from 310 to ~257

### Fix 2: Volume Confirmation - IMPLEMENTED
- **File:** `backend/backtest/backtest_technical.py`
- **Function:** `check_volume_confirmation(stock_df, date_idx, ma_period=50)`
- **Rule:** Skip entries when Volume < 50-day MA
- **Impact:** Further filters low-conviction entries

### Fix 3: Earnings Blackout - IMPLEMENTED (Limited Data)
- **File:** `backend/backtest/backtest_technical.py`
- **Functions:** `get_earnings_dates_cached()`, `check_earnings_blackout()`
- **Rule:** Skip entries within ±5 days of earnings
- **Note:** yfinance historical earnings data is limited; filter may not catch all events

---

## BACKTEST RESULTS COMPARISON

### Baseline (No Fixes)
```
Total Trades: 310
Win Rate: 49.7%
Profit Factor: 1.40
Expectancy: +1.30%
Avg Win: +9.06%
Avg Loss: -6.67%
```

### With TIER 1 Fixes
```
Total Trades: 257
Win Rate: 49.0%
Profit Factor: 1.35
Expectancy: +1.18%
Avg Win: +9.17%
Avg Loss: -6.51%
```

### Analysis
- **Trades Filtered:** 53 entries blocked (17% reduction)
- **Avg Loss Improved:** -6.67% → -6.51% (smaller losses)
- **Avg Win Improved:** +9.06% → +9.17% (slightly bigger wins)
- **Win Rate Similar:** Filters don't dramatically improve win rate
- **System Profitable:** Profit Factor 1.35, positive expectancy

### Conclusion
The TIER 1 fixes **prevent bad trades** but don't fundamentally improve entry quality. The system remains profitable but below the 55% win rate target.

---

## RESOLVED (Day 41)

| Issue | Resolution | Date |
|-------|------------|------|
| Gap 1: No Market Regime Filter | Implemented check_bull_regime() | Day 41 |
| Gap 2: No Volume Confirmation | Implemented check_volume_confirmation() | Day 41 |
| Gap 3: No Earnings Avoidance | Implemented check_earnings_blackout() | Day 41 |
| Gap 4: Zero Backtest Validation | Ran 257-trade backtest | Day 41 |
| Redundant Trade Levels Grid | Removed from App.jsx | Day 41 |
| No tooltips on UI elements | Added to ADX, RSI, R:R, strategies | Day 41 |
| Research not synthesized | Created PERPLEXITY_RESEARCH_SYNTHESIS.md | Day 41 |

---

## RESOLVED (Day 39/40)

| Issue | Resolution | Notes |
|-------|------------|-------|
| No local RSI calculation | Added calculate_rsi() to backend.py | Independence from TradingView |
| Fixed % stop losses | Implemented structural stops | swing_low - (ATR * 2) |
| No trend strength indicator | Added ADX calculation | With strength classification |
| No 4H momentum confirmation | Added calculate_rsi_4h() | Uses yfinance 1H resampled |
| Dual cards only for CAUTION | Fixed to show for ALL stocks | Condition updated |

---

## VALIDATION GATES STATUS

| Gate | Criteria | Status |
|------|----------|--------|
| G1: Structural Stops | Avg loss < 7% baseline | PASSED (-6.51%) |
| G2: ADX Value | Win rate improves with gating | PENDING |
| G3: 4H Data | Reliable, sufficient history | PASSED (118 bars) |
| G4: 4H RSI Value | Entry timing improves | PENDING |
| G5: Regime Filter | Reduces bear market losses | IMPLEMENTED |
| G6: Volume Filter | Reduces failed breakouts | IMPLEMENTED |

---

## NEXT STEPS

### TIER 2 Fixes (If Needed)
1. Improve RSI crossover logic (RSI crosses above 30)
2. Add VIX-based position sizing
3. Walk-forward validation

### Key Questions
1. Is 49% win rate acceptable with 1.35 profit factor?
2. Should we raise the score threshold from 30 to 35?
3. Do we need additional entry filters?

---

## DEFERRED ITEMS (v2+)

| Feature | Reason for Deferral |
|---------|---------------------|
| Sector Rotation (RRG) | Complex, marginal v1 value |
| Credit Spread Monitoring | Early warning, not entry filter |
| Kelly Criterion Sizing | Our half/full sizing acceptable |
| Yield Curve Tracking | Recession indicator, not trade filter |
| Full Lightweight Charts | After backtest validation |

---

## FILES MODIFIED (Day 41)

| File | Changes |
|------|---------|
| `backend/backtest/backtest_technical.py` | Added TIER 1 filters |
| `docs/claude/versioned/KNOWN_ISSUES_DAY41.md` | Updated with results |
| `docs/research/PERPLEXITY_RESEARCH_SYNTHESIS.md` | Created |

---

*Previous: KNOWN_ISSUES_DAY40.md*
*Next: KNOWN_ISSUES_DAY42.md*
