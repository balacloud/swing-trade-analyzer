# Perplexity Research Prompts - Day 42

> **Purpose:** Research prompts for sector rotation, candle patterns, and options tools
> **Date:** February 2, 2026
> **Usage:** Copy each prompt into Perplexity for deep research

---

## PROMPT 1: Programmatic Sector Rotation Detection

```
I'm building a swing trading system and need to programmatically detect sector rotation. Please research and provide:

1. **Quantitative Methods for Detecting Sector Rotation:**
   - What mathematical formulas or algorithms can detect sector rotation?
   - How do quant funds and algorithmic traders detect sector rotation programmatically?
   - What is the RRG (Relative Rotation Graph) algorithm and how can I implement it?

2. **Data Requirements:**
   - What data do I need? (sector ETF prices, breadth data, etc.)
   - What timeframes are optimal for detection (daily, weekly)?
   - What is the minimum lookback period required?

3. **Specific Indicators to Calculate:**
   - Relative Strength (RS) vs benchmark - exact formula
   - Momentum (MoM) calculation - exact formula
   - How to combine RS and MoM into quadrant classification
   - What thresholds define "Leading", "Weakening", "Lagging", "Improving"?

4. **Python Implementation:**
   - Are there any Python libraries that calculate sector rotation?
   - How do I calculate RRG coordinates programmatically?
   - Sample code or pseudocode for detection algorithm

5. **Validation:**
   - How accurate is programmatic sector rotation detection?
   - What is the typical lag time before rotation is detected?
   - How do professionals validate their rotation signals?

Focus on quantitative, implementable methods rather than discretionary analysis. I'm using Python with yfinance for data.
```

---

## PROMPT 2: Candle Close & Trend Reversal for Swing Trading

```
I'm building a swing trading system and need to understand the importance of candlestick patterns for entry timing. Please research:

1. **Which Candlestick Patterns Are Statistically Validated:**
   - Which patterns have been backtested and proven statistically significant?
   - What are the actual win rates of common reversal patterns (hammer, engulfing, doji)?
   - Cite any academic studies or large-scale backtests on candlestick effectiveness

2. **Trend Reversal Confirmation:**
   - How do professional swing traders confirm trend reversals?
   - What combination of candle + indicator works best? (candle + RSI, candle + volume, etc.)
   - How many days/candles of confirmation are needed to reduce false signals?

3. **Entry Timing:**
   - Should swing traders enter on the reversal candle or wait for confirmation?
   - What is the optimal entry: close of signal candle, open of next candle, or breakout of high?
   - How does entry timing affect win rate and risk/reward?

4. **Volume Confirmation:**
   - How important is volume in confirming candlestick patterns?
   - What volume ratio (vs average) validates a reversal pattern?
   - Does the research support volume confirmation or is it overrated?

5. **Implementation Recommendation:**
   - For a systematic swing trading system (not discretionary), which patterns should I code?
   - What is the minimum pattern set that covers most valuable signals?
   - Should candlestick patterns be primary signals or confirmation for other indicators?

Please cite specific studies, backtests, or professional sources. I want data-driven answers, not traditional candlestick lore.
```

---

## PROMPT 3: Simple Options Recommendation Engines on GitHub

```
I'm looking for open-source options trading tools on GitHub that I can learn from or integrate. My requirements are SIMPLE - I'm NOT building a complex options trading system. I just want basic call/put recommendations based on directional bias.

Please research and provide:

1. **GitHub Repositories:**
   - What are the most starred/popular options analysis repos on GitHub?
   - Are there any simple options screeners or recommendation engines?
   - Any repos that calculate basic options metrics (no complex Greeks if possible)?

2. **Simple Options Tools:**
   - Repos that provide directional options signals (call buy, put buy)
   - Tools that select strikes based on technical analysis
   - Any projects that integrate stock signals with options recommendations?

3. **Data Sources:**
   - What free APIs do these repos use for options data?
   - Does yfinance provide enough for simple options analysis?
   - Any repos that work with yfinance options data?

4. **Specific Features I Need:**
   - Strike selection (ATM, 1 strike OTM)
   - Expiration selection (nearest monthly, 30-45 DTE)
   - Basic IV display (already available from yfinance)
   - Volume/Open Interest filtering for liquidity

5. **What to Avoid:**
   - I don't need Greeks calculation libraries
   - I don't need options pricing models (Black-Scholes)
   - I don't need complex spread strategies
   - I don't need backtesting for options

Please provide direct GitHub links, repo names, and a brief description of what each does. Focus on SIMPLE, beginner-friendly tools rather than institutional-grade systems.
```

---

## PROMPT 4: Sector Rotation Implementation Details

```
Follow-up research on implementing sector rotation detection:

1. **Sector ETF List:**
   - What are the 11 GICS sector ETFs (XLK, XLF, etc.)?
   - What benchmark should I use (SPY or equal-weight)?

2. **RRG Calculation Formula:**
   - Step-by-step: How to calculate JdK RS-Ratio?
   - Step-by-step: How to calculate JdK RS-Momentum?
   - What smoothing parameters are standard?

3. **Quadrant Thresholds:**
   - What RS value separates Leading from Improving?
   - What Momentum value separates Leading from Weakening?
   - Is 100 the dividing line or something else?

4. **Rotation Speed:**
   - How many weeks does typical rotation take?
   - How to calculate "tail length" in RRG?
   - What tail length indicates strong vs weak rotation?

5. **Implementation Priority:**
   - For a simple first version, what's the minimum viable detection?
   - Can I just use 1-month and 3-month performance rankings instead of full RRG?
   - What's the simplest quantitative rotation signal that works?

I'm using Python with pandas. Please provide formulas I can implement directly.
```

---

## HOW TO USE THESE PROMPTS

1. Copy one prompt at a time into Perplexity
2. Read the response carefully
3. Save the response to a markdown file in `/docs/research/`
4. Synthesize findings into implementation plan

---

## EXPECTED OUTPUTS

| Prompt | Expected Deliverable |
|--------|---------------------|
| 1 | Python algorithm for sector rotation detection |
| 2 | List of validated candlestick patterns + confirmation rules |
| 3 | List of GitHub repos to evaluate |
| 4 | Formulas for RRG calculation |

---

*Created: February 2, 2026*
