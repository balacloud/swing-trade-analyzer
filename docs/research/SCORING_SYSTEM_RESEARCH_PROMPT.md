# Scoring System Deep Research Prompt

> **Purpose:** Research prompt for Perplexity to validate direction on 75-point scoring system
> **Context:** Day 27 backtest showed ~50% win rate (essentially random)
> **Question:** Should we keep it, remove it, or improve it?

---

## Current State Summary

### System 1: 75-Point Scoring Engine

| Category | Points | Status | Issue |
|----------|--------|--------|-------|
| Technical | 40 | Working | Based on Minervini SEPA |
| Fundamental | 20 | Working | Uses Defeat Beta data |
| Sentiment | 10 | **Placeholder** | Always returns 5/10 |
| Risk/Macro | 5 | Partial | Breadth is placeholder |

**Backtest Results (Day 27):**
- Period: 2020-2024 (5 years)
- Stocks: 28 large/mid cap
- **Win Rate: 49.7%** (essentially random)
- Profit Factor: 1.40 (profitable due to R:R, not signal quality)

### System 2: Simplified Binary (4 Criteria)

| Criterion | Logic | Source |
|-----------|-------|--------|
| Trend | Price > 50 SMA > 200 SMA | Stage 2 concept |
| Momentum | RS > 1.0 | Relative strength |
| Setup | Stop within 7% | Position sizing |
| Risk/Reward | R:R >= 2:1 | Risk management |

**Backtest Results:**
- Win Rate: 51.7% (slightly better, still near random)
- Profit Factor: 1.43
- Trades: Only 29 (very selective)

### Key Day 27 Discovery

```
Entry signals = ~10% of trading results
Position sizing = ~90% of trading results

Implication: We spent 27 days optimizing the 10%, ignored the 90%
```

---

## Research Questions for Perplexity

### Main Prompt (Copy-Paste Ready)

```
I have a stock screening/scoring system for swing trading that I need to validate.
My backtesting shows the system achieves ~50% win rate (essentially random), but is
still profitable due to favorable risk/reward (10% target, 7% stop).

CURRENT SYSTEM (75 points):
- Technical (40 pts): Trend structure, short-term momentum, volume, relative strength
- Fundamental (20 pts): EPS growth, revenue growth, ROE, debt/equity, forward P/E
- Sentiment (10 pts): PLACEHOLDER - always returns 5/10
- Risk/Macro (5 pts): VIX level, S&P regime, market breadth (partial placeholder)

BACKTEST RESULTS (2020-2024, 28 stocks):
- Win Rate: 49.7% (essentially random)
- Profit Factor: 1.40 (profitable from R:R, not signal quality)
- Total Trades: 310

I also have a simplified 4-criteria binary system:
- Trend: Price > 50 SMA > 200 SMA
- Momentum: RS > 1.0 (outperforming S&P 500)
- Setup: Stop within 7% of entry
- R:R: Risk/reward >= 2:1

This scored 51.7% win rate (29 trades, very selective).

RESEARCH QUESTIONS:

1. **KEEP, IMPROVE, OR REMOVE?**
   - Should I keep both systems, merge them, or remove one entirely?
   - Is a ~50% win rate with good R:R actually acceptable for swing trading?
   - What win rate do successful systematic swing traders typically achieve?

2. **IF IMPROVE - WHERE TO FOCUS?**
   - My sentiment score is a placeholder (10 points = 13% of total). Should I:
     a) Build real sentiment analysis (earnings, news)?
     b) Remove sentiment entirely and rebalance weights?
     c) Replace with something more quantifiable (like options flow)?
   - Market breadth is also placeholder. Worth implementing?

3. **WHAT ACTUALLY PREDICTS SWING TRADE SUCCESS?**
   - Academic research: What factors predict 1-2 month stock returns?
   - Does fundamental analysis add value for short-term trades?
   - Is relative strength (RS) the most important factor?
   - What about price patterns (VCP, cup-and-handle, flags)?

4. **ALTERNATIVE APPROACHES:**
   - Factor investing for short-term: Momentum, quality, volatility?
   - Machine learning for scoring: Worth exploring or overkill?
   - Regime detection: Bull/bear market adjustments?
   - Sector rotation: Score relative to sector, not absolute?

5. **POSITION SIZING VS ENTRY SIGNALS:**
   - Van Tharp research says position sizing = 90% of results
   - My backtest confirms entry signals = ~10% of results
   - Should I stop optimizing entry signals and focus purely on:
     a) Better risk/reward identification?
     b) Better position sizing rules?
     c) Portfolio-level risk management?

6. **PRACTICAL IMPLEMENTATION:**
   - Best Python libraries for sentiment analysis (free tier)?
   - Best APIs for earnings calendar data?
   - Best approach for market breadth (% stocks above 50 SMA)?
   - Any open-source scoring systems I can learn from?

CONTEXT:
- Trading style: Swing trading, 1-2 month holds
- Data source: yfinance (free), Defeat Beta (fundamentals)
- Tech stack: Python backend, React frontend
- Account size: Retail ($10K-$100K)
- Time commitment: Part-time (not monitoring intraday)

Please provide:
1. Clear recommendation: Keep, improve, or remove the scoring system
2. If improve: Which components have the highest ROI for development time
3. Academic or practitioner evidence for each recommendation
4. Specific tools/APIs/libraries for implementation
5. What win rate is realistic for systematic swing trading
```

---

## Alternative Shorter Prompt

```
Research whether multi-factor stock scoring systems (like 75-point with
technical + fundamental + sentiment) actually predict 1-2 month returns.

My backtest shows ~50% win rate (essentially random) despite using:
- Trend structure (Price > 50 SMA > 200 SMA)
- Relative Strength (vs S&P 500)
- Fundamental metrics (ROE, EPS growth)
- VIX and market regime

Questions:
1. Is ~50% win rate acceptable if R:R is favorable (2:1+)?
2. What factors actually predict short-term (1-2 month) returns?
3. Should I focus on entry signals or position sizing?
4. Is sentiment analysis worth building, or is it noise for swing trading?
5. What do successful systematic swing traders actually use?

Include: Academic research, practitioner insights, GitHub implementations.
```

---

## What to Look For in Results

### Signals to KEEP the System

| Finding | Implication |
|---------|-------------|
| ~50% win rate is normal for systematic trading | System is fine, focus on R:R |
| Momentum factor (RS) has academic backing | Keep RS as primary signal |
| Fundamentals don't predict short-term returns | Remove fundamentals, save API calls |

### Signals to IMPROVE the System

| Finding | Implication |
|---------|-------------|
| Sentiment adds X% edge | Build real sentiment analysis |
| Market breadth is predictive | Implement breadth calculation |
| Price patterns add edge | Add VCP/flag detection |

### Signals to REMOVE/SIMPLIFY

| Finding | Implication |
|---------|-------------|
| All complexity is noise | Simplify to binary (4 criteria) only |
| Position sizing is everything | Remove scoring, focus on risk management |
| Factor-based approaches are better | Replace with factor exposure analysis |

---

## Key Hypothesis to Validate

### Hypothesis 1: Entry Signals Don't Matter Much
```
Van Tharp: Position sizing = 90% of results
My backtest: 75-point system = 50% win rate (random)

If true → Stop optimizing scoring, focus on:
- Better stop placement
- Better target selection
- Portfolio risk limits
```

### Hypothesis 2: Relative Strength is King
```
AQR momentum research: 12-month RS predicts future returns
My simplified system: RS > 1.0 is one of 4 criteria

If true → Make RS the primary signal, everything else is noise
```

### Hypothesis 3: Sentiment is Unquantifiable
```
My placeholder always returns 5/10
Building real sentiment requires NLP, API costs, complexity

If true → Remove sentiment, accept we can't predict news impact
```

---

## Decision Matrix

After research, fill in this matrix:

| Component | Keep | Improve | Remove | Rationale |
|-----------|------|---------|--------|-----------|
| Technical (40pt) | | | | |
| Fundamental (20pt) | | | | |
| Sentiment (10pt) | | | | |
| Risk/Macro (5pt) | | | | |
| Simplified Binary | | | | |
| Position Sizing Focus | | | | |

---

## Expected Outcome

This research should answer:

1. **Directional Decision:** Keep both systems, merge, or remove one
2. **Priority Order:** If improving, which component first
3. **Resource Allocation:** Should next sprint be scoring or S&R improvement
4. **Realistic Expectations:** What win rate to target (55%? 60%? or accept 50%+R:R)

---

*Prompt created: January 17, 2026*
*Use with Perplexity Deep Research mode*
