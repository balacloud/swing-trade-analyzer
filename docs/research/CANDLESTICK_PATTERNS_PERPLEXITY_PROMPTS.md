# Candlestick Pattern Implementation — Perplexity Deep Research Prompts

> **Purpose:** Research prompts to run in Perplexity AI before implementing candlestick patterns
> **Context:** Swing Trade Analyzer — Mark Minervini SEPA methodology, 5-45 day holding periods
> **Decision:** Candlestick patterns will be a STANDALONE POST-FLIGHT CHECK only. NOT integrated into full analysis, decision matrix, or simple checklist. Human makes final decision.
> **Created:** Day 62 (March 1, 2026)

---

## Background Context (Share with Perplexity)

This system uses:
- **Core strategy:** Mark Minervini SEPA + William O'Neil CAN SLIM
- **Holding periods:** Quick (5-10d), Standard (15-30d), Position (1-3mo)
- **Entry style:** VCP (Volatility Contraction Pattern), Cup & Handle, Flat Base breakouts
- **Current signals:** ADX > 25 (momentum), RSI, Relative Strength vs SPY, Volume confirmation
- **Backtest results:** Config C (full 3-layer system) = 53.78% WR, PF 1.61, 238 trades, statistically significant (p=0.002)
- **Philosophy:** Entry signals = ~10% of results. Position sizing = ~90% of results.
- **Key constraint:** Candlestick patterns must NOT modify existing verdicts or scoring — they are post-flight context only.

---

## Prompt 1: Statistical Reliability of Candlestick Patterns (Run This First)

```
I'm building a swing trading tool using Mark Minervini's SEPA methodology with 5-45 day holding periods. I want to add candlestick patterns as a POST-FLIGHT CHECK — informational context shown AFTER my core technical + fundamental analysis produces a trade signal.

I need rigorous statistical data, not trading book claims. Please research:

1. STATISTICAL ACCURACY of candlestick patterns in academic literature:
   - What is the measured prediction accuracy (not claimed accuracy) of the top 10 most-used candlestick patterns?
   - Which patterns have been validated by peer-reviewed studies vs only in trading books?
   - What are the false positive rates for: Hammer, Engulfing, Doji, Morning Star, Evening Star, Shooting Star, Harami, Piercing Line, Dark Cloud Cover?
   - How does pattern accuracy vary by market cap (large cap vs small cap vs mid cap)?
   - How does accuracy change in trending markets vs ranging markets?

2. HOLDING PERIOD DEPENDENCY:
   - Are certain patterns only predictive over specific timeframes (1-3 days vs 5-10 days)?
   - Do candlestick reversal patterns actually predict reversals or just short-term volatility?
   - For 5-45 day swing trading specifically: which patterns have demonstrated statistically significant edges?

3. VOLUME CONFIRMATION:
   - Does requiring volume confirmation (e.g., >1.5x average) significantly improve pattern accuracy?
   - Which patterns specifically REQUIRE volume confirmation to be meaningful?

Please cite specific studies, journals, or quantitative research. Distinguish between backtested data and real-time forward-tested data. Flag any patterns where "the evidence is weak or inconclusive" explicitly.
```

---

## Prompt 2: Which Patterns to Implement for SEPA Methodology

```
Context: I use Mark Minervini's SEPA system for swing trading. Stocks must pass 8-point Trend Template (above 150/200 EMA, price > 30 weeks ago, etc.), VCP/Cup & Handle patterns, and volume confirmation. My holding period is 5-45 days.

Given this context, research the following:

1. BEST-FIT PATTERNS FOR TREND-FOLLOWING:
   - Which candlestick patterns work BEST as entry timing signals in ALREADY ESTABLISHED UPTRENDS (not reversals)?
   - Minervini focuses on "pivot point" entry — which candlestick patterns best signal a pivot from a tight consolidation?
   - Which reversal patterns are COUNTER-PRODUCTIVE when trading trend-following?

2. CONTINUATION PATTERNS vs REVERSAL PATTERNS:
   - List the top 5-8 candlestick CONTINUATION patterns (bullish continuation) with their win rates from studies
   - List the top 5-8 candlestick REVERSAL (both bullish reversal from pullback) patterns with their win rates
   - Which patterns have the highest false positive rate and should be EXCLUDED?

3. PATTERN HIERARCHY FOR SEPA:
   - If I had to pick ONLY 6-8 patterns to show a trader using SEPA, which ones provide the most incremental information beyond "stock is in uptrend + forming VCP"?
   - Are candlestick patterns essentially redundant with VCP/Cup & Handle confirmation, or do they add genuine alpha?

4. IMPLEMENTATION DECISION:
   - Given that my backtest shows 53.78% win rate with PF 1.61 WITHOUT candlestick patterns, what is the estimated incremental edge from adding them?
   - Is there a threshold of pattern accuracy below which it's better to NOT show the signal to avoid cognitive bias / overtrading?

Provide specific pattern names, win rates, and your recommendation on whether to implement each one.
```

---

## Prompt 3: Technical Implementation Details

```
I'm implementing a candlestick pattern detection module in Python for a Flask backend that already uses pandas + numpy for technical analysis. The candlestick data I have is daily OHLCV (open, high, low, close, volume) for US equities.

Research the following for implementation:

1. DETECTION ALGORITHMS:
   - What are the canonical mathematical definitions for the following patterns?
     * Hammer (and Hanging Man)
     * Bullish/Bearish Engulfing
     * Doji (standard, long-legged, gravestone, dragonfly)
     * Morning Star / Evening Star
     * Shooting Star
     * Bullish/Bearish Harami
     * Three White Soldiers / Three Black Crows
   - What are the standard ratio thresholds used by professional quantitative systems?
     (e.g., "body must be at least X% of total range", "shadow must be Y times body size")
   - Does TA-Lib (the Python library) implement these correctly, or does it have known issues?

2. USING TA-LIB vs CUSTOM IMPLEMENTATION:
   - Is TA-Lib reliable for candlestick pattern detection in production?
   - What are the known bugs or threshold issues with TA-Lib's candlestick functions?
   - Is there a better Python alternative (pandas-ta, vectorbt, etc.)?
   - Should I use lookback periods (e.g., require uptrend context before detecting Hammer)?

3. CONTEXT-AWARE DETECTION:
   - Should I detect patterns ONLY when the stock is in an uptrend (Trend Template passes)?
   - What lookback period should precede pattern detection for it to be meaningful?
     (e.g., "Hammer only meaningful after 3-5 red candles preceding it")
   - How do I differentiate a "real" Hammer from a random short-body candle?

4. DISPLAY DESIGN:
   - What information should be shown per detected pattern?
     (pattern name, type, last occurrence, signal strength, volume confirmation?)
   - Should multiple patterns from the same timeframe be shown, or only the most recent?
   - Should I show patterns from the last 1 candle, 3 candles, or 5 candles?

5. SAMPLE CODE:
   - Provide a Python function to detect Hammer, Bullish Engulfing, Morning Star, and Doji using pandas DataFrame with OHLCV columns
   - Show the ratio-based detection logic clearly (not just calling TA-Lib blindly)

Please be specific about thresholds and provide actual Python code examples.
```

---

## Prompt 4: UX Design — How to Present Candlestick Patterns

```
I'm designing a "Post-Flight Check" widget for candlestick patterns in a React frontend for a swing trading tool. The widget appears AFTER the main analysis (categorical assessment, trade setup, decision matrix) and is INFORMATIONAL ONLY — it does not change any buy/sell recommendations.

The user profile: experienced retail swing trader who understands candlestick patterns. They use Mark Minervini's SEPA methodology. They do NOT want noise — they want signal.

Research and recommend the following:

1. INFORMATION HIERARCHY:
   - What is the minimum information a trader needs from a candlestick pattern?
     (pattern name, bullish/bearish/neutral classification, volume confirmation, recency?)
   - What information is redundant or distracting and should be OMITTED?
   - Should I show ALL detected patterns from the last N candles, or only the MOST SIGNIFICANT one?

2. COGNITIVE BIAS PREVENTION:
   - How do I design the widget so traders DON'T overweight the candlestick signal vs the core analysis?
   - Should candlestick patterns be shown with a confidence score, or just present/absent?
   - What disclaimers or context labels help prevent overtrading based on patterns?

3. VISUAL DESIGN:
   - What color coding is standard for candlestick signals in trading UIs?
   - Should I show a mini candlestick chart (last 5-10 candles) or just text description?
   - What level of detail is appropriate for a "post-flight check" widget vs an in-depth analysis tool?

4. INTERACTION DESIGN:
   - Should the widget be always visible or collapsible/hidden by default?
   - Should it refresh when the ticker changes, or require manual refresh?
   - What should the widget show when NO patterns are detected in the last 5 candles?

5. EXAMPLE DISPLAY:
   Recommend a specific UI layout for showing:
   - Pattern name + type (bullish reversal / bearish reversal / continuation / neutral)
   - Last occurrence (e.g., "Detected today" or "3 sessions ago")
   - Volume confirmation (yes/no)
   - One-sentence plain-English interpretation
   - A label like "Pattern Only — Does Not Change Verdict"

   Suggest whether this should be a card, a banner, a collapsible section, or a simple badge list.

Please reference any established trading platform UX (ThinkorSwim, TradingView, Interactive Brokers) as examples.
```

---

## How to Use These Prompts

1. **Run Prompt 1 first** — establishes the statistical foundation. If patterns have < 55% accuracy in studies, reconsider whether to implement at all.

2. **Run Prompt 2 second** — determines WHICH patterns to implement. Use the list to create a curated set (target: 6-10 patterns maximum).

3. **Run Prompt 3 third** — get implementation details. Specifically: TA-Lib vs custom, detection thresholds, Python code.

4. **Run Prompt 4 fourth** — only after deciding to implement. Guides the React component design.

---

## Decision Criteria

Before implementing, use Perplexity results to answer:

| Question | Threshold | Action if fails |
|----------|-----------|-----------------|
| Are any patterns > 60% accurate in studies? | At least 3 patterns | Don't implement |
| Does volume confirmation improve accuracy significantly? | Yes for at least half | Require volume |
| Do patterns add alpha beyond VCP/Trend Template? | Yes, measurable | Implement as post-flight |
| Is TA-Lib reliable enough? | < 3 known bugs on target patterns | Use TA-Lib |
| Can we show < 10 patterns without noise? | Yes | Curate the list |

---

## Implementation Checklist (After Research)

- [ ] Read Perplexity results from all 4 prompts
- [ ] Decide final pattern list (target: 6-10 max)
- [ ] Decide detection library (TA-Lib vs custom vs pandas-ta)
- [ ] Implement `pattern_detection.py` additions (or new `candlestick_engine.py`)
- [ ] Add `/api/candlesticks/<ticker>` endpoint (NOT `/api/patterns` — keep separate)
- [ ] Create `CandlestickWidget.jsx` React component
- [ ] Wire into App.jsx as OPTIONAL post-flight section (collapsible, after Decision Matrix)
- [ ] Verify: ZERO changes to categoricalAssessment.js, verdict logic, decision matrix
- [ ] Build + test with 5 tickers (AAPL, AMD, NVDA, SPY, a small cap)
