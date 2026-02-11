# Holding Period Selector - Implementation Plan

> **Created:** Day 50 (February 10, 2026)
> **Last Updated:** Day 51 (February 11, 2026)
> **Priority:** P1 - Addresses core UX confusion
> **Effort:** 4-6 hours
> **Status:** REVISED AFTER RESEARCH VALIDATION

---

## CRITICAL: Day 51 Research Findings

### What Was INVALIDATED

The original RSI thresholds by holding period were **invented without research backing**:

| Period | Original Thresholds | Research Finding |
|--------|---------------------|------------------|
| Quick (5-10d) | RSI 40-65 | WRONG - shorter periods need MORE EXTREME thresholds (15/85), not tighter |
| Standard (15-30d) | RSI 35-70 | Partially correct but regime-dependent |
| Position (1-3mo) | RSI 30-75 | WRONG - thresholds don't relax with time |

**Root Cause:** RSI interpretation varies by **ADX REGIME**, not holding period:
- ADX < 20 (weak trend): RSI > 70 = mean reversion expected
- ADX > 25 (strong trend): RSI > 70 = momentum confirmation (BUY signal)

### What Was VALIDATED

1. **ADX-based regime messaging** (already in v4.6.2) - correct approach
2. **Signal weighting by horizon** - academic research supports:
   - Short-horizon trades → Technical signals dominate
   - Long-horizon trades → Fundamental signals dominate
3. **Bottom Line summary card** - UX research supports consolidated views
4. **Separating analysis by horizon** - earns ~40 bps monthly alpha (arXiv 2512.00280)

### What Was NOT Research-Backed

- Kavout's dual-horizon format: "No peer-reviewed studies, backtesting results, or independent validation"
- Specific RSI thresholds per holding period: No practitioner consensus found

---

## Problem Statement

Users see conflicting signals that create confusion:
- JNJ Example: "AVOID" verdict + "PULLBACK OK" badge + "Stage 2 Uptrend (ideal)" + "SKIP THIS ONE"
- The system is trying to say "Quality stock, bad entry timing" but doesn't communicate this clearly

---

## REVISED Solution

### 1. Holding Period Selector (3 Options) - SIGNAL WEIGHTING, NOT THRESHOLDS

| Period | Label | Primary Signal Weight | Secondary Signal Weight |
|--------|-------|----------------------|------------------------|
| 5-10 days | Quick Swing | Technical (70%) | Fundamental (30%) |
| 15-30 days | Standard Swing | Technical (50%) | Fundamental (50%) |
| 1-3 months | Position Trade | Technical (30%) | Fundamental (70%) |

**Research Basis:** arXiv 2512.00280 found short-horizon investors use "support, volume, break, target, stop" (technical) while long-horizon use "EPS, financials" (fundamental).

### 2. ADX-Based Regime Messaging (KEEP EXISTING)

Our current v4.6.2 ADX logic is correct:
```javascript
// VALIDATED - Keep this approach
if (adx < 20) {
  // Weak trend - RSI extremes matter (mean reversion likely)
  if (rsi > 70) return 'AVOID - Wait for pullback';
} else if (adx > 25) {
  // Strong trend - RSI extremes = momentum confirmation
  if (rsi > 70) return 'MOMENTUM - Trend strong, pullbacks are buying opportunities';
}
```

### 3. Unified "Bottom Line" Summary Card (KEEP - UX VALIDATED)

Replace the current recommendation card with a consolidated summary:

```
┌─────────────────────────────────────────────────────────────────┐
│ 📋 BOTTOM LINE (for 15-30 day swing)                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ⏳ WATCHLIST - WAIT FOR PULLBACK                               │
│                                                                 │
│ WHAT'S GOOD:                                                    │
│ • Stage 2 Uptrend (8/8 TT) - ideal for swing trades            │
│ • Strong fundamentals (ROE 25%, low debt)                       │
│ • RS 1.37 - outperforming market                               │
│                                                                 │
│ WHAT'S RISKY:                                                   │
│ • RSI 82.1 + ADX 18 - overbought in WEAK trend = pullback likely│
│ • Only 1% from 52-week high - limited upside at current price  │
│                                                                 │
│ ACTION PLAN:                                                    │
│ 1. Set alert at $215.19 (nearest support, 9.8% below)          │
│ 2. Entry at support offers 3.20 R:R                            │
│ 3. Stop: $207.15 | Target: $240.94                             │
│                                                                 │
│ WHY NOT NOW:                                                    │
│ Current price ($238.64) offers only 0.08 R:R to resistance     │
└─────────────────────────────────────────────────────────────────┘
```

**UX Research Basis:**
- "Traders struggle with overloaded dashboards" (Medium UX Guide)
- "Simplified alert systems help them respond faster" (HRT)

### 4. UI Changes

#### A. Holding Period Toggle (for signal weighting)
```jsx
<div className="flex gap-2 mb-4">
  <button
    className={holdingPeriod === 'quick' ? 'active' : ''}
    onClick={() => setHoldingPeriod('quick')}
    title="Emphasizes Technical signals (RS, TT, RSI)"
  >
    5-10 days
  </button>
  <button
    className={holdingPeriod === 'standard' ? 'active' : ''}
    onClick={() => setHoldingPeriod('standard')}
    title="Balanced Technical + Fundamental"
  >
    15-30 days
  </button>
  <button
    className={holdingPeriod === 'position' ? 'active' : ''}
    onClick={() => setHoldingPeriod('position')}
    title="Emphasizes Fundamental signals (ROE, growth)"
  >
    1-3 months
  </button>
</div>
```

#### B. Signal Weighting Logic
```javascript
// REVISED: Weight signals by horizon, don't change thresholds
const getSignalWeight = (holdingPeriod) => {
  switch (holdingPeriod) {
    case 'quick':    // 5-10 days - Technical dominates
      return { technical: 0.7, fundamental: 0.3 };
    case 'standard': // 15-30 days - Balanced
      return { technical: 0.5, fundamental: 0.5 };
    case 'position': // 1-3 months - Fundamental dominates
      return { technical: 0.3, fundamental: 0.7 };
  }
};

// Verdict influenced by weighted categories
const getWeightedVerdict = (techScore, fundScore, holdingPeriod) => {
  const weights = getSignalWeight(holdingPeriod);
  const weightedScore = (techScore * weights.technical) + (fundScore * weights.fundamental);

  // ADX regime still determines RSI interpretation (unchanged)
  // This weighting affects category importance in final verdict
  return weightedScore;
};
```

---

## Implementation Phases (REVISED)

### Phase 1: Bottom Line Card (2 hours)
1. Design the consolidated summary component
2. Generate "What's Good" / "What's Risky" from existing data
3. Include ADX regime context in RSI messaging
4. Replace current fragmented recommendation cards

### Phase 2: Signal Weighting (2 hours)
1. Add `holdingPeriod` state to App.jsx
2. Implement `getSignalWeight()` function
3. Apply weights to verdict calculation
4. Update category display based on weighting

### Phase 3: UI Integration (2 hours)
1. Add holding period toggle to UI
2. Show which signals are emphasized for selected period
3. Test with various stocks (JNJ, NVDA, F, COIN)

---

## Test Cases (REVISED)

| Ticker | ADX | RSI | TT | Quick (Tech Heavy) | Standard (Balanced) | Position (Fund Heavy) |
|--------|-----|-----|----|--------------------|---------------------|----------------------|
| JNJ | 18 | 82.1 | 8/8 | AVOID (weak trend + overbought) | WATCHLIST | CONSIDER (strong fundamentals) |
| NVDA | 32 | 55.4 | 8/8 | BUY | BUY | BUY |
| F | 28 | 45.2 | 8/8 | BUY | BUY | WATCHLIST (weak fundamentals) |
| AFRM | 15 | 30.0 | 3/8 | AVOID | AVOID | AVOID |

**Key Difference:** ADX determines RSI interpretation, holding period determines signal emphasis.

---

## Research Sources

### Validated
1. **arXiv 2512.00280** - "Retail Investor Horizon and Earnings Announcements"
   - Short-horizon = technical signals, overreaction
   - Long-horizon = fundamental signals, underreaction
   - Strategy earns ~40 bps monthly alpha

2. **Perplexity Research (Day 51)** - ADX/RSI threshold validation
   - ADX regime determines RSI interpretation
   - RSI > 80 = 68% pullback within 14 days (all regimes)
   - RSI > 70 in strong trend (ADX > 25) = momentum confirmation

3. **UX Research** - Multi-timeframe interfaces
   - Simplified dashboards improve decision-making
   - Consolidated views reduce cognitive load

### NOT Validated
1. **Kavout dual-horizon format** - Marketing, no research backing
2. **RSI thresholds by holding period** - No practitioner consensus
3. **Original plan's RSI 40-65/35-70/30-75** - Invented, contradicts research

---

## Files to Modify

| File | Changes |
|------|---------|
| `frontend/src/App.jsx` | Add holdingPeriod state, toggle UI, signal weighting |
| `frontend/src/utils/categoricalAssessment.js` | Add signal weighting logic |
| `frontend/src/components/BottomLineCard.jsx` | NEW - consolidated summary |

---

## Success Criteria

1. **JNJ Test:** Shows "WATCHLIST - Wait for Pullback" with clear ADX context
2. **No conflicting signals:** Bottom Line card reconciles all indicators
3. **Clear action:** User knows exactly what to do (wait, set alert, enter)
4. **Signal emphasis changes:** Quick swing emphasizes technicals, Position emphasizes fundamentals
5. **ADX context preserved:** RSI interpretation tied to regime, not holding period

---

## Backtest Pending

The ADX/RSI threshold backtest (`backend/backtest/backtest_adx_rsi_thresholds.py`) could not run due to yfinance API outage. Run when API recovers to validate:
1. ADX < 20 + RSI > 70 = mean reversion rate
2. ADX > 25 + RSI > 70 = momentum continuation rate
3. RSI > 80 = 68% pullback claim from research

---

*This plan addresses the core UX confusion identified in Day 50 testing (JNJ case study)*
*REVISED Day 51 after research validation - removed invented thresholds, added signal weighting*
