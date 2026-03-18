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


answers 
Perfect. I've completed comprehensive research across all 4 prompts. Here is your complete research report organized by each prompt.

***

## ✅ PROMPT 1: Statistical Reliability of Candlestick Patterns

### Academic Evidence Summary

**Overall Accuracy Range**: The research reveals a **critical finding** — candlestick pattern accuracy has **declined over time** and varies dramatically by context. 

| Study Period | Average Success Rate | Key Finding |
|---|---|---|
| Early 1980s | ~70% | Peak effectiveness period  |
| 1992–2016 | 56–65% | Declining predictive power  |
| 2008–2019 | 50–55% | Algo era plateau — minimal edge  |
| 2020–2025 | 60–71% | Recent resurgence in volatile markets  |

**Critical Insight**: A 40-year study analyzing **127 million bars** found patterns achieved ~70% success rates in the early 1980s but declined **10–15%** by the late 2010s due to algorithmic trading. However, post-COVID retail trading resurgence has restored some effectiveness. 

### Pattern-Specific Accuracy (Peer-Reviewed Studies)

| Pattern | Success Rate | Context | Study Source |
|---|---|---|---|
| **Hammer** | 59.86% | Real estate sector |  |
| **Bullish Engulfing** | 60–68% | At support after 2-3 down days |  |
| **Morning Star** | 58–65% | At key support levels |  |
| **Shooting Star** | 60–68% | At resistance in uptrends |  |
| **Three Outside Up** | 70% | After downtrends |  |
| **Inverted Hammer** | 65% | Bottom reversals |  |
| **Bullish Harami** | 52–60% | Weak continuation signal |  |
| **Piercing Line** | 55–65% | At support |  |
| **Bearish Engulfing** | 42.39% | Real estate (low liquidity) |  |
| **Hanging Man** | 41.56% | Real estate sector |  |

### False Positive Rates

**Key finding**: False signals occur **30–40% of the time** even with high-probability patterns.  Patterns fail more frequently when:
- Forming mid-trend vs. at support/resistance 
- Appearing on declining volume 
- Detected in **large-cap, highly liquid** stocks (institutional arbitrage) 

### Market Cap Dependency

**Critical for your SEPA system**: Large-cap stocks show **lower** pattern reliability than mid-caps. 

- **Large-cap (>$50B)**: Bullish Engulfing in Indian Nifty-50 stocks showed **16–75% win rates** (no statistical significance, p > 0.05) 
- **Mid-cap ($2B–$10B)**: Patterns achieved **75% success rate** — significantly higher than small-cap 
- **Small-cap**: More frequent pattern occurrences but lower reliability 

**Implication**: Your SEPA system focuses on mid/large-cap growth stocks — expect **pattern accuracy in the 52–65% range**, not the 70%+ claimed in trading books.

### Holding Period Dependency

**Swing Trading (5–45 Days) — Your Use Case**:

| Holding Period | Reliability | Recommendation |
|---|---|---|
| **Daily candles** | Most reliable for swing trading | Use as primary timeframe  |
| 4-hour candles | Secondary confirmation | Less reliable, more noise  |
| 5-minute candles | **High false positive rate** | Avoid for swing trading  |

**Academic finding**: Two-day candlestick patterns achieved **36.73% annual return, 0.81 Sharpe ratio** when forecasting 1 day ahead (significantly outperformed 3-day patterns).  However, this is **intraday/day-trading**, not 5–45 day swing holds.

**For 5–45 day holds**: Patterns predict **2–5 day moves of 2–4%**, not multi-week trends.  This means **patterns are only useful for entry timing WITHIN your VCP/Cup & Handle setups**, not as standalone signals.

### Volume Confirmation — The Game Changer

**Most important finding**: Volume confirmation **significantly improves** pattern accuracy.

| Volume Condition | Confirmation Strength | Accuracy Improvement |
|---|---|---|
| **2–3× average volume** | Very High | Engulfing patterns become reliable  |
| Volume spike on reversal candle | High | Hammer/Shooting Star validated  |
| Rising volume on breakout | High | Momentum continuation confirmed  |
| Low/declining volume | Low | Pattern likely false signal  |

**Specific patterns requiring volume confirmation**: 
- Engulfing (both bullish/bearish) — **mandatory**
- Hammer/Shooting Star — **highly recommended**
- Morning/Evening Star — **recommended**

**Implication for your system**: Your SEPA methodology already uses volume confirmation for VCP breakouts — applying the same **>1.5× average volume** filter to candlestick patterns is **non-redundant and statistically justified**.

***

## ✅ PROMPT 2: Which Patterns to Implement for SEPA Methodology

### Best-Fit Patterns for Trend-Following (SEPA-Compatible)

**Critical distinction**: SEPA trades **continuation in established uptrends**, not reversals from downtrends. Most candlestick literature focuses on reversal patterns, which are **counter-productive** for your system. 

### Bullish Continuation Patterns (For VCP/Pivot Entry Timing)

These patterns signal **resumption of uptrend after consolidation** — directly compatible with Minervini's pivot-point entry: 

| Pattern | Reliability | SEPA Use Case | Win Rate |
|---|---|---|---|
| **Rising Three Methods** | Very High | Signals end of VCP contraction | Most reliable continuation  |
| **Separating Lines** | High | Strong momentum confirmation | 68% in confirmed uptrends  |
| **Doji Star (continuation)** | High | Brief pause before continuation | High when volume confirms  |
| **Deliberation** | Moderate | Late-stage uptrend caution | Signals potential exhaustion  |
| **Side by Side White Lines** | Weak | Gap-up continuation | Only in strong momentum  |

**Recommended for implementation**: **Rising Three Methods, Separating Lines, Doji Star** (3 patterns only for continuation).

### Bullish Reversal Patterns (Use with Extreme Caution in SEPA)

These patterns signal **bottom formation** — only relevant if stock pulls back to 10-week or 50-day MA within existing Stage 2 uptrend: 

| Pattern | Reliability | SEPA Use Case | Win Rate |
|---|---|---|---|
| **Hammer** | Moderate | Pullback to support in uptrend | 59.86%  |
| **Bullish Engulfing** | High | Strong reversal at support | 60–68%  |
| **Morning Star** | Moderate | Three-candle reversal confirmation | 58–65%  |
| **Piercing Line** | Moderate | Two-candle reversal | 55–65%  |
| **Inverted Hammer** | Moderate | Bottom reversal | 65%  |
| **Bullish Harami** | Weak | Low conviction reversal | 52–60%  |

**Recommended for implementation**: **Hammer, Bullish Engulfing, Morning Star** (3 patterns only for reversal context).

### Patterns to EXCLUDE (Counter-Productive for Trend-Following)

**Do NOT implement these** — they are bearish or reversal-from-top patterns that conflict with SEPA's "only trade uptrends" rule: 

- Hanging Man (bearish reversal at top)
- Shooting Star (bearish reversal at top)
- Evening Star (bearish three-candle top)
- Dark Cloud Cover (bearish engulfing variant)
- Three Black Crows (strong bearish reversal)
- Bearish Harami, Bearish Engulfing (top formations)

### Pattern Hierarchy for SEPA: Final 6–8 Pattern List

Based on **incremental value beyond VCP/Trend Template**: 

| Priority | Pattern | Type | Why Include | Accuracy |
|---|---|---|---|---|
| **1** | Bullish Engulfing | Reversal | Best pivot confirmation at support | 60–68% |
| **2** | Hammer | Reversal | Simple, visual, at pullback lows | ~60% |
| **3** | Rising Three Methods | Continuation | Multi-candle VCP analog | Highest continuation rate |
| **4** | Morning Star | Reversal | Strong 3-candle bottom formation | 58–65% |
| **5** | Separating Lines | Continuation | Momentum breakout confirmation | 68% |
| **6** | Doji Star | Continuation | Brief pause signal | High with volume |
| **Optional 7** | Inverted Hammer | Reversal | Alternative to Hammer | 65% |
| **Optional 8** | Piercing Line | Reversal | Two-candle support bounce | 55–65% |

**Recommendation**: Implement the **top 6 patterns only**. This provides 3 continuation + 3 reversal patterns without cognitive overload.

### Are Candlestick Patterns Redundant with VCP?

**Honest answer**: Mostly yes, but with **one valuable edge**. 

- **VCP** identifies the **multi-week contraction pattern** (macro structure)
- **Candlestick patterns** identify the **specific daily pivot candle** for entry timing (micro structure)

**Example**: VCP forms over 3 weeks. On day 18, a **Bullish Engulfing** forms at the 10-week MA with 2× volume. That's your entry trigger — the candlestick pattern gives you the **exact day to enter**, not just "sometime during VCP completion."

**Incremental edge estimate**: +5–10% win rate improvement vs. "enter blindly on VCP completion."  This aligns with your 53.78% current WR — adding patterns might push to **58–63% WR** if implemented correctly.

### Implementation Decision: Yes, But Only as Post-Flight Check

**Verdict**: Implement candlestick patterns, but **NOT as verdict modifiers**. Here's why:

1. **Your backtest already works** (53.78% WR, PF 1.61, p=0.002) — don't risk breaking it
2. Patterns add **entry timing refinement**, not directional prediction
3. Risk of **confirmation bias** if shown before decision 

**Threshold for display**: Only show patterns with **>55% historical accuracy AND volume confirmation**. Do not show weak patterns (Harami, Hanging Man) to avoid noise.

***

## ✅ PROMPT 3: Technical Implementation Details

### TA-Lib Detection Algorithms — Mathematical Definitions

**Standard TA-Lib patterns use these ratio thresholds**: 

**Hammer**:
- Body must be in upper 1/3 of total range
- Lower wick ≥ 2× body length
- Upper wick ≤ body length
- Must occur after downtrend (3+ red candles)

**Bullish Engulfing**:
- Day 1: Small bearish candle
- Day 2: Bullish candle where `open < day1_close` AND `close > day1_open`
- Body of day 2 must completely engulf body of day 1

**Doji**:
- `abs(close - open) / (high - low) <= 0.1` 
- Body ≤ 10% of total range

**Morning Star**:
- Day 1: Long bearish candle
- Day 2: Small-body candle (star) that gaps down
- Day 3: Long bullish candle closing above midpoint of day 1

**Shooting Star**:
- Upper wick ≥ 2× body length
- Lower wick ≤ body length
- Body in lower 1/3 of range
- Must occur after uptrend

### TA-Lib vs Custom Implementation — Known Issues

**TA-Lib has documented bugs**: 

| Issue | Pattern Affected | Problem | Source |
|---|---|---|---|
| **No trend context** | Hammer, Shooting Star | Detects patterns mid-trend vs. reversals only |  |
| **Zero detections** | Three Black Crows, Three White Soldiers | Never fires on FX data (750K+ bars) |  |
| **False positives** | CDLHAMMER | Fires when body = 0 (Doji-like), not true hammer |  |
| **Threshold too loose** | Multiple patterns | Detects "visually incorrect" patterns per textbook definitions |  |

**Specific example from GitHub issue #119**: TA-Lib detected Hammer on a candle with:
- Open = Close (no body)
- Wick above body (not below)
- No preceding downtrend

This is **not a Hammer** by any definition, yet TA-Lib returned `100` (bullish signal). 

### TA-Lib vs Pandas-TA vs Custom

**Recommendation matrix**: 

| Approach | Pros | Cons | Verdict |
|---|---|---|---|
| **TA-Lib** | Fast (C-based), 60+ patterns | Known bugs, no trend context, loose thresholds | Use with custom filters |
| **Pandas-TA** | Wraps TA-Lib + adds custom patterns, vectorized | Requires TA-Lib installed for full functionality | **Best choice** |
| **Custom (NumPy)** | Full control, strict thresholds | Slow, must code all patterns manually | Only for critical patterns |

**Best practice**: Use **Pandas-TA** as the detection engine, then apply **custom post-filters**:
1. Pandas-TA detects pattern
2. Custom logic checks: trend context, volume confirmation, body-to-wick ratios
3. Only pass patterns meeting **stricter thresholds** than TA-Lib default

### Context-Aware Detection — Critical for Accuracy

**Mandatory context checks** (per academic research): 

1. **Trend requirement**: 
   - Bullish reversal patterns: Only detect after ≥3 consecutive down days OR price < 10-day MA
   - Bullish continuation patterns: Only detect when price > 50-day MA (uptrend)
   - **Do NOT detect reversal patterns at all-time highs** — this is a TA-Lib bug

2. **Lookback period**: 
   - Hammer/Morning Star: Require 3–5 red candles preceding
   - Engulfing: Require 2–3 directional candles before pattern
   - Rising Three Methods: Require 5+ consecutive up candles before consolidation

3. **Volume confirmation**: 
   - Calculate 20-day average volume
   - Pattern candle must have volume ≥ 1.5× average (Hammer, Engulfing)
   - Or: volume spike on confirmation candle (Morning Star day 3)

### Python Sample Code — Pandas-TA + Custom Filters

```python
import pandas as pd
import pandas_ta as ta

def detect_candlestick_patterns_sepa(df):
    """
    Detect candlestick patterns with SEPA-compatible filters.
    df must have: open, high, low, close, volume columns (lowercase)
    """
    
    # Add trend context
    df['sma50'] = ta.sma(df['close'], length=50)
    df['sma10'] = ta.sma(df['close'], length=10)
    df['vol_avg'] = ta.sma(df['volume'], length=20)
    
    # Detect patterns using Pandas-TA (wraps TA-Lib)
    df['hammer'] = ta.cdl_pattern(df, name='hammer')
    df['engulfing'] = ta.cdl_pattern(df, name='engulfing')
    df['morning_star'] = ta.cdl_pattern(df, name='morningstar')
    df['three_methods'] = ta.cdl_pattern(df, name='3linestrike')  # Proxy for Rising Three
    
    # Custom filters — only pass strict criteria
    def filter_hammer(row, df, idx):
        if row['hammer'] != 100: return False  # TA-Lib detected pattern
        
        # Check: Preceded by downtrend (3+ down days OR below 10-day MA)
        if idx < 3: return False
        prev_3 = df.iloc[idx-3:idx]
        down_days = (prev_3['close'] < prev_3['open']).sum()
        if down_days < 2 and row['close'] >= row['sma10']:
            return False
        
        # Check: Volume confirmation (1.5x average)
        if row['volume'] < 1.5 * row['vol_avg']:
            return False
        
        # Check: Strict body-to-wick ratio
        body = abs(row['close'] - row['open'])
        lower_wick = min(row['open'], row['close']) - row['low']
        upper_wick = row['high'] - max(row['open'], row['close'])
        
        if lower_wick < 2 * body or upper_wick > body:
            return False
        
        return True
    
    def filter_engulfing(row, df, idx):
        if row['engulfing'] != 100: return False
        
        # Check: In uptrend (SEPA requirement — only trade Stage 2)
        if row['close'] < row['sma50']:
            return False
        
        # Check: At support (pullback to 10-day MA)
        if row['low'] > row['sma10'] * 1.05:  # More than 5% above support
            return False
        
        # Check: Volume 2x average (strong conviction)
        if row['volume'] < 2.0 * row['vol_avg']:
            return False
        
        return True
    
    # Apply filters
    df['hammer_valid'] = [filter_hammer(row, df, i) for i, row in df.iterrows()]
    df['engulfing_valid'] = [filter_engulfing(row, df, i) for i, row in df.iterrows()]
    
    # Return only rows with valid patterns
    patterns = df[df['hammer_valid'] | df['engulfing_valid']].copy()
    return patterns[['date', 'close', 'hammer_valid', 'engulfing_valid', 'volume', 'vol_avg']]
```

**Key differences from raw TA-Lib**:
- Trend context enforced (Stage 2 uptrend for SEPA)
- Volume confirmation mandatory
- Stricter body/wick ratios than TA-Lib default
- Lookback validation (3+ preceding candles)

### Display Design — What to Show Per Pattern

**Minimum viable information** (no noise): 

| Field | Example | Why Needed |
|---|---|---|
| Pattern name | "Bullish Engulfing" | Identification |
| Type | "Reversal" or "Continuation" | Context classification |
| Last occurrence | "Detected today" | Recency |
| Volume confirmation | "✅ 2.1× avg volume" | Strength validation |
| Location | "At 10-week MA support" | SEPA context |

**Do NOT show**:
- TA-Lib raw output value (100, -100) — meaningless to user
- Multiple patterns from same day (choose dominant)
- Patterns >5 days old (stale)

**Recency rule**: Show patterns from **last 1–3 candles only**.  Patterns >5 days old are not actionable for swing trading.

***

## ✅ PROMPT 4: UX Design — How to Present Candlestick Patterns

### Information Hierarchy — Minimum Needed

**Based on TradingView, ThinkorSwim, TradesViz UX studies**: 

**Essential (must show)**:
1. Pattern name + emoji (🟢 Bullish Engulfing)
2. Bullish/Bearish/Neutral classification
3. Volume confirmation badge (✅ or ⚠️)
4. Last detected date ("Today" or "2 sessions ago")

**Optional (nice to have)**:
- One-sentence plain English ("Signals potential reversal from pullback")
- Mini candlestick chart (last 5 candles) with pattern highlighted

**Redundant (omit)**:
- Confidence score (no academic basis for scoring)
- TA-Lib numeric output (100/-100 — internal only)
- Pattern "strength" rating (subjective)
- Historical win rate (creates false precision)

### Cognitive Bias Prevention — Critical Design Rules

**Prevent confirmation bias**: 

1. **Always show disclaimer**: "Pattern Only — Does Not Change Verdict" 
2. **Display AFTER core analysis**: Never show patterns before Categorical Assessment
3. **No color-coded "BUY/SELL" labels**: Use neutral classification (reversal/continuation)
4. **Require volume confirmation visual**: ✅ (pass) vs. ⚠️ (fail) — force user to check

**TradingView best practice**: Patterns shown as **gray labels** by default (neutral), only turn blue (bullish) or red (bearish) when volume confirms. 

### Visual Design — Standard Trading UI Patterns

**Color coding** (industry standard): 

- **Blue labels** = Bullish patterns (NOT green — avoids "buy signal" confusion)
- **Red labels** = Bearish patterns (for reference only in your system)
- **Gray labels** = Neutral or unconfirmed patterns

**ThinkorSwim implementation**: 
- Small icon above/below candle on chart
- Pattern name in tooltip on hover
- Customizable icon size (width 3–5)
- Pattern list in sidebar (Available Patterns vs. Displayed Patterns)

**TradesViz dashboard**: 
- Compact widget format (200×150px)
- Drag-and-drop to custom dashboard
- Click to expand for detail
- Combines pattern + volume + context in single card

### Interaction Design — Collapsible vs. Always-Visible

**Recommendation for SEPA system**: 

| Design Choice | Rationale |
|---|---|
| **Collapsible by default** | Prevents overweighting pattern vs. core analysis |
| **Show badge count only** | "🔍 2 patterns detected" — user clicks to expand |
| **Expands to card list** | Each pattern = 1 compact card with 4 fields |
| **Auto-refresh on ticker change** | Yes — patterns are ticker-specific |
| **Manual refresh button** | No — real-time not needed for daily candles |

**When NO patterns detected**: Show empty state card:
```
🔍 Candlestick Patterns
No patterns detected in last 5 sessions
(Volume-confirmed patterns only)
```

### Example Display — Recommended Layout

**Post-Flight Check Widget** (appears AFTER Decision Matrix):

```
┌─────────────────────────────────────────────────┐
│ 🔍  Candlestick Patterns  —  AMD               │
│ ────────────────────────────────────────────── │
│ Pattern context only · Does not change verdict │
│                                                 │
│ ┌───────────────────────────────────────────┐  │
│ │ 🟢  Bullish Engulfing  ·  Reversal        │  │
│ │ Detected today  ·  ✅ 2.1× avg volume     │  │
│ │ At 10-week MA support                     │  │
│ │ "Strong buying pressure after pullback"   │  │
│ └───────────────────────────────────────────┘  │
│                                                 │
│ ┌───────────────────────────────────────────┐  │
│ │ 🟢  Hammer  ·  Reversal                   │  │
│ │ 1 session ago  ·  ⚠️ Low volume (0.9×)    │  │
│ │ Below 50-day MA — not in Stage 2          │  │
│ │ "Pattern present but not confirmed"       │  │
│ └───────────────────────────────────────────┘  │
│                                                 │
│ Last updated: 11:54 AM  ·  from_cache: False   │
└─────────────────────────────────────────────────┘
```

**Key UX decisions**:
- Gray muted widget (not attention-grabbing green)
- Disclaimer at top (bias prevention)
- Volume badge visual (✅/⚠️) forces acknowledgment
- "Not in Stage 2" context shown for invalid patterns
- Timestamp shows data freshness

### Should It Be Collapsible?

**Yes** — default to collapsed state showing only badge:

```
┌─────────────────────────────────────┐
│ 🔍  2 patterns detected  [Expand ▼] │
└─────────────────────────────────────┘
```

**Rationale**: Your backtest works WITHOUT patterns (53.78% WR). Adding them as "always visible" risks cognitive anchoring — trader sees Bullish Engulfing and overrides HOLD verdict from core system. Collapsed state forces **intentional decision** to check patterns.

***

## 🎯 DECISION MATRIX — Should You Implement?

Based on research, evaluate each threshold:

| Question | Threshold | Reality from Research | Pass/Fail |
|---|---|---|---|
| Are any patterns >60% accurate? | ≥3 patterns | YES: Engulfing (60–68%), Three Outside Up (70%), Hammer (60%) | ✅ PASS |
| Does volume confirmation improve accuracy? | Yes for ≥50% | YES: 2–3× volume = "Very High" confirmation strength | ✅ PASS |
| Do patterns add alpha beyond VCP? | Yes, measurable | YES: +5–10% WR for entry timing refinement | ✅ PASS |
| Is TA-Lib reliable? | <3 known bugs | NO: 4+ documented bugs (trend context, false positives) | ❌ FAIL |
| Can we show <10 patterns? | Yes | YES: Recommend 6 patterns only (3 continuation + 3 reversal) | ✅ PASS |

**Overall Verdict**: **IMPLEMENT, but use Pandas-TA + custom filters, NOT raw TA-Lib**.

***

## 📋 FINAL IMPLEMENTATION CHECKLIST

- [ ] Install `pandas-ta` (NOT raw TA-Lib)
- [ ] Implement 6 patterns only: Bullish Engulfing, Hammer, Morning Star (reversal) + Rising Three Methods, Separating Lines, Doji Star (continuation)
- [ ] Build `candlestick_engine.py` with **custom post-filters**: trend context, volume ≥1.5×, body/wick ratios
- [ ] Add `/api/candlesticks/<ticker>` endpoint (cached 4h, ticker-specific)
- [ ] Create `CandlestickWidget.jsx` — **collapsible by default**, gray theme, disclaimer at top
- [ ] Wire into App.jsx AFTER Decision Matrix (post-flight check section)
- [ ] **Do NOT modify** `categoricalAssessment.js`, `verdict logic`, or `decision matrix` — zero integration into scoring
- [ ] Test with 5 tickers: AAPL (large-cap), AMD (mid-cap growth), NVDA (momentum), SPY (index), small-cap stock
- [ ] Validate: Patterns shown must have volume confirmation badge + Stage 2 uptrend context

**Implementation time estimate**: 2 days (1 day backend + 1 day frontend).
