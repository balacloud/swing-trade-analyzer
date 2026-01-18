# Scoring System Research Analysis

> **Purpose:** Analysis of Perplexity research findings and recommendation plan
> **Date:** January 17, 2026 (Day 30)
> **Status:** Analysis Complete - Awaiting Decision

---

## Executive Summary

| Question | Research Answer | Confidence |
|----------|-----------------|------------|
| Is 50% win rate acceptable? | **YES** - Common for systematic swing trading | Very High |
| Keep or remove 75-point? | **KEEP and REFACTOR** | High |
| Keep or remove 4-criteria? | **KEEP as hard filter** | High |
| Build real sentiment? | **OPTIONAL** - Only weekly aggregated | Medium |
| Focus on entries or sizing? | **SIZING** - 90% of results | Very High |

---

## Key Research Findings

### Finding 1: Your System is NOT Broken

The research confirms:
- **50% win rate is normal** for rules-based swing systems
- Many successful traders run 35-50% win rates with 2:1 R:R
- Your **profit factor 1.40 is acceptable** for retail swing accounts
- The "problem" is signal quality ≈ random, but **that's fixable**

**Implication:** Don't throw away the system. Refactor it.

### Finding 2: Two-System Architecture

The research recommends keeping both systems with different roles:

```
┌─────────────────────────────────────────────────────────────┐
│                    PROPOSED ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  STEP 1: 4-Rule Binary Filter (GATEKEEPER)                  │
│  ─────────────────────────────────────────                  │
│  Must pass ALL 4:                                            │
│  ├── Price > 50 SMA > 200 SMA (structural uptrend)          │
│  ├── RS > 1.0 vs S&P 500 (momentum)                         │
│  ├── Stop ≤ 7% (setup quality)                              │
│  └── R:R ≥ 2:1 (risk/reward)                                │
│                                                              │
│  If ANY fail → SKIP (don't even score)                      │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  STEP 2: 75-Point Scorer (RANKER + SIZING)                  │
│  ─────────────────────────────────────────                  │
│  For stocks that PASS the filter:                           │
│  ├── Rank candidates by score                               │
│  ├── Adjust position size based on score                    │
│  └── Prioritize higher scores when capital limited          │
│                                                              │
│  Example sizing:                                             │
│  ├── Score 60-75: Full position (1R)                        │
│  ├── Score 50-59: 75% position (0.75R)                      │
│  └── Score 40-49: 50% position (0.5R)                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Implication:** Current implementation where both systems run independently should change. Binary filter first, then score.

### Finding 3: Highest ROI Improvements

The research ranks improvements by impact:

| Priority | Improvement | Current State | Research Recommendation |
|----------|-------------|---------------|------------------------|
| **1** | Market Regime/Breadth | Placeholder (1pt) | Make it a HARD FILTER, not just points |
| **2** | RS/Momentum weight | 10 of 40 pts | Increase to 25-30 pts total |
| **3** | Quality fundamentals | 20 pts | Keep but focus on growth + quality |
| **4** | Sentiment | Placeholder (5/10) | Only if weekly aggregated, else remove |
| **5** | Position sizing rules | Manual | Systematize and tie to scores |

### Finding 4: What Actually Predicts 1-2 Month Returns

Research consensus on predictive factors:

| Factor | Evidence Strength | Currently Used? |
|--------|------------------|-----------------|
| **Medium-term momentum (3-12 mo)** | Very Strong | ✅ Yes (RS) |
| **Trend structure (MA alignment)** | Very Strong | ✅ Yes (50>200 SMA) |
| **Market regime/breadth** | Strong | ❌ Placeholder |
| **Quality fundamentals (ROE, growth)** | Moderate | ✅ Yes |
| **Weekly news sentiment** | Modest | ❌ Placeholder |
| **Daily sentiment** | Weak | N/A |
| **Forward P/E** | Very Weak for short-term | ⚠️ Included but low value |

### Finding 5: Position Sizing Dominance

The research confirms Van Tharp's findings:

```
Position sizing = ~90% of performance variance
Entry signals = ~10% of performance variance

Your backtest confirms this:
- Entry rules ≈ random (50% win rate)
- But R:R and sizing create positive expectancy (PF 1.40)
```

**Implication:**
- Don't obsess over squeezing win rate from 50% to 55%
- Focus on:
  1. Portfolio-level risk caps (max 6-8% total open risk)
  2. Per-trade sizing based on score quality
  3. Better R:R identification (not just fixed 10%/7%)

### Finding 6: Don't Use ML (Yet)

Research caution:
- 310 trades over 5 years
- Only 28 stocks in universe
- **Not enough independent data** for ML without overfitting

**Implication:** Stick with rules-based system. ML can wait until data grows significantly.

---

## Recommended Score Rebalancing

### Current Weights (75 points)

| Category | Current Points | Issues |
|----------|----------------|--------|
| Technical | 40 | RS could be higher |
| Fundamental | 20 | Forward P/E low value |
| Sentiment | 10 | **100% Placeholder** |
| Risk/Macro | 5 | **Mostly Placeholder** |

### Proposed Weights (75 points)

| Category | New Points | Change | Rationale |
|----------|------------|--------|-----------|
| **Trend + Momentum** | 30 | +5 | Highest predictive power |
| **Quality Fundamentals** | 20 | 0 | Keep, but drop Forward P/E |
| **Setup Quality** | 10 | NEW | ATR-based stop, pattern quality |
| **Regime/Breadth** | 10 | +5 | Make it real (% above 50 SMA) |
| **Sentiment** | 5 | -5 | Only if weekly, else 0 |

### Alternative: Remove Sentiment Entirely

If building real sentiment is too complex:

| Category | Points | Notes |
|----------|--------|-------|
| Trend + Momentum | 35 | RS, MA distance, volume |
| Quality Fundamentals | 20 | EPS, Revenue, ROE (drop PE) |
| Setup Quality | 10 | Stop distance, pattern |
| Regime/Breadth | 10 | Real breadth calculation |
| **Total** | **75** | No placeholder components |

---

## Implementation Options

### Option A: Minimal Changes (Low Effort, Moderate Impact)

**Effort:** 2-4 hours
**Impact:** Modest improvement

Changes:
1. Make breadth filter real (% stocks above 50 SMA)
2. Remove Forward P/E from fundamentals (low value)
3. Use binary system as hard filter BEFORE scoring
4. Document that sentiment is placeholder (don't pretend it works)

### Option B: Moderate Refactor (Medium Effort, High Impact)

**Effort:** 8-12 hours
**Impact:** Significant improvement

Changes:
1. All of Option A, plus:
2. Rebalance weights toward momentum/RS
3. Add setup quality score (ATR-based stop, pattern flags)
4. Tie position sizing to score (60+ = full, 50-59 = 75%, etc.)
5. Add regime filter as hard gate (no longs in bear regime)

### Option C: Full Refactor (High Effort, Maximum Impact)

**Effort:** 20-30 hours
**Impact:** System overhaul

Changes:
1. All of Option B, plus:
2. Build weekly sentiment aggregation (VADER + NewsAPI)
3. Add sector-relative RS scoring
4. Implement Van Tharp position sizing framework
5. Add portfolio-level risk caps (max 6-8% total open risk)

---

## Decision Matrix

Fill this in after review:

| Component | Keep | Remove | Refactor | Priority |
|-----------|------|--------|----------|----------|
| 4-Rule Binary Filter | | | | |
| 75-Point Scorer | | | | |
| Technical (40 pts) | | | | |
| Fundamental (20 pts) | | | | |
| Sentiment (10 pts placeholder) | | | | |
| Risk/Macro (5 pts partial) | | | | |
| Market Breadth | | | | |
| Position Sizing Rules | | | | |

---

## My Recommendation

Based on the research, I recommend **Option B: Moderate Refactor** with this priority order:

### Phase 1: Quick Wins (2-4 hours)
1. Use binary filter as GATEKEEPER (not parallel system)
2. Make breadth filter real (yfinance calculation)
3. Remove Forward P/E from fundamentals

### Phase 2: Score Rebalancing (4-6 hours)
1. Increase momentum/RS weight to 30 pts
2. Add setup quality score (10 pts)
3. Formalize regime as hard filter

### Phase 3: Sizing Integration (4-6 hours)
1. Tie position size to score quality
2. Add portfolio-level risk caps
3. Document the new system

### Phase 4: Optional Sentiment (8-10 hours, DEFER)
Only if Phases 1-3 show improvement:
1. Weekly news sentiment via VADER
2. Cap at 5-10 points weight

---

## Questions for User Decision

Before proceeding, need your input on:

1. **Which option?** A (minimal), B (moderate), or C (full)?

2. **Sentiment priority?**
   - Build it now (adds complexity)
   - Remove entirely and reallocate points
   - Keep placeholder but document it's fake

3. **Position sizing integration?**
   - Manual (current) - you decide size
   - Score-based (new) - system suggests size based on score
   - Both (show both options)

4. **Implementation timeline?**
   - This session (partial)
   - Next session (Day 31)
   - Backlog (after S&R improvements)

---

## Comparison: S&R vs Scoring Improvements

You have two improvement tracks. Which first?

| Track | Effort | Expected Impact | Dependencies |
|-------|--------|-----------------|--------------|
| **S&R (DBSCAN)** | 18 hrs (4 weeks) | 80%→95% detection | Independent |
| **Scoring Refactor** | 8-12 hrs | Better signal quality | Independent |

**Recommendation:** They are independent. Can run in parallel or sequence based on your preference.

---

*Analysis complete: January 17, 2026*
*Awaiting user decision on approach*
