# Perplexity Research Prompts for System Validation

> **Purpose:** Comprehensive prompts to validate our dual entry strategy system
> **Created:** Day 40 (January 31, 2026)
> **Usage:** Copy and paste these prompts into Perplexity for deep research

---

## Prompt 1: Dual Entry Strategy Validation

```
I'm building a swing trading entry strategy system and want to validate my approach against professional/institutional practices. Please analyze and critique the following methodology:

## MY DUAL ENTRY STRATEGY SYSTEM:

### Strategy A: Pullback Entry (for trending markets)
- **Trigger**: ADX ≥ 25 (strong trend detected)
- **Entry**: At nearest support level (calculated via pivot points)
- **Stop Loss**: Support level - (2 × ATR)
- **Target**: Nearest resistance or Fibonacci extension (1.618)
- **Position Size**: Full position
- **Logic**: Strong trends tend to bounce off support; waiting for pullback improves R:R

### Strategy B: Momentum Entry (for ranging/weak trend markets)
- **Trigger**: ADX < 25 (weak trend or ranging)
- **Entry**: At current price (breakout/momentum play)
- **Stop Loss**: Nearest support - (1.5 × ATR)
- **Target**: Same as Strategy A
- **Position Size**: Half position (higher risk)
- **Confirmation**: Requires 4H RSI < 40 (oversold) or rising from lows
- **Logic**: Ranging markets need momentum confirmation; smaller position for higher risk

### Technical Indicators Used:
1. **ADX (14-period)**: Trend strength classification
   - <20 = choppy/no trend
   - 20-25 = weak trend
   - 25-40 = strong trend
   - >40 = very strong trend

2. **4H RSI (14-period)**: Multi-timeframe momentum confirmation
   - Used on 4-hour chart when daily chart triggers
   - <40 = oversold (good entry zone)
   - >60 = overbought (avoid new entries)

3. **ATR (14-period)**: Volatility-based stop placement
   - Structural stop = swing_low - (ATR × multiplier)
   - Adapts to each stock's volatility

4. **Support/Resistance**: Pivot point method with agglomerative clustering
   - 1-year of daily data
   - Cluster nearby levels within 2% price tolerance

## QUESTIONS FOR VALIDATION:

1. **ADX Threshold**: Is 25 the right cutoff for trend strength? Some sources suggest 20 or 30. What does academic research or institutional practice show?

2. **ATR Multiplier**: I use 2×ATR for pullback stops and 1.5×ATR for momentum. Are these reasonable? What do professional traders use?

3. **4H RSI for Confirmation**: Is using a higher timeframe RSI for entry confirmation a valid technique? Should I use RSI crossover signals instead of static levels?

4. **Position Sizing**: Half position for momentum (higher risk) vs full for pullback (lower risk). Is this the right approach? Should I use Kelly Criterion or fixed fractional instead?

5. **Missing Elements**: What critical components am I missing for a complete swing trading system? Consider:
   - Market regime filters (bull/bear/neutral)
   - Sector rotation considerations
   - Volume confirmation
   - Earnings/event avoidance
   - Correlation with market indices

6. **Backtesting Requirements**: What statistical tests should I run to validate this system?
   - Minimum number of trades needed?
   - Walk-forward vs in-sample/out-of-sample?
   - What metrics beyond win rate? (Expectancy, Sharpe, Max Drawdown, SQN)

7. **Known Pitfalls**: What are common mistakes in dual-strategy systems like this? How do I avoid:
   - Curve fitting
   - Overly complex rules
   - Whipsaw in ranging markets
   - Failed breakouts in momentum strategy

Please provide specific, actionable recommendations with references to academic papers, books (like Van Tharp, Mark Minervini, Alexander Elder), or institutional practices where possible.
```

---

## Prompt 2: Market Regime Detection

```
How should a swing trading system adapt to different market regimes?

## Context:
I have a dual-entry system (pullback vs momentum) for individual stocks. I need to add market regime detection and adjustment rules.

## Questions:

1. **What's the most reliable market regime detection method?**
   - Simple: SPY vs 200 SMA
   - Composite: SPY + VIX + Breadth (A/D line)
   - Momentum: Rate of change or moving average crossovers
   - Academic: Markov regime switching models

2. **How should position sizing change by regime?**
   - Bull market max exposure?
   - Bear market max exposure?
   - Should I go to cash entirely in bear markets?

3. **Should I filter out ALL long entries in bear markets, or just reduce size?**

4. **What additional indicators help detect regime changes early?**
   - Yield curve?
   - Credit spreads?
   - Sector rotation patterns?
   - Put/call ratios?

5. **How do professional swing traders handle earnings season and high-volatility events?**

6. **What's the best way to define bull/neutral/bear thresholds?**
   - SPY % above/below 200 SMA?
   - VIX levels?
   - Breadth indicators?

Please provide specific rules I can implement programmatically, with code-friendly thresholds and conditions.
```

---

## Prompt 3: ATR-Based Stop Loss Validation

```
I'm researching ATR-based stop loss strategies for swing trading. Please help me validate and optimize my approach.

## Current Implementation:
- **Pullback Stop**: Nearest support level - (2 × ATR)
- **Momentum Stop**: Nearest support level - (1.5 × ATR)
- **ATR Period**: 14 days (standard)

## Questions:

1. **ATR Multiplier Research**: What does academic research say about optimal ATR multipliers for stop losses?
   - Is 2× ATR too tight or too loose?
   - Does the optimal multiplier vary by:
     - Market cap (large cap vs small cap)?
     - Volatility regime (high VIX vs low VIX)?
     - Holding period (swing vs position trading)?

2. **Structural vs Fixed Stops**: I calculate stops as swing_low - (ATR × multiplier). Compare this to:
   - Fixed percentage stops (e.g., 7% from entry)
   - Chandelier exits
   - Parabolic SAR
   - Which performs better in backtests?

3. **Stop Placement Below Support**: Is placing stops below support levels (rather than at arbitrary ATR distances) academically supported?

4. **ATR Period Selection**: Why 14 periods? Would 10 or 21 periods be better for swing trading?

5. **Adaptive ATR**: Should the multiplier adapt to market conditions?
   - Higher multiplier in high VIX environments?
   - Lower multiplier in low VIX environments?

6. **Trailing Stops**: At what point should I switch from initial stop to trailing stop? Common approaches:
   - After price moves 1R in my favor
   - After specific time (e.g., 3 days)
   - Never (use fixed target only)

Please provide specific research citations and quantitative findings where available.
```

---

## Prompt 4: System Evaluation Metrics

```
What metrics and tests should I use to evaluate a swing trading system before live trading?

## My System:
- Dual entry strategy (pullback vs momentum)
- ATR-based stops
- ADX for trend detection
- 4H RSI for confirmation

## Questions:

1. **Minimum Trade Count**: How many trades do I need in a backtest for statistical significance?
   - Some say 30, some say 100, some say 1000
   - What does academic research recommend?

2. **Key Metrics Beyond Win Rate**: Please explain the importance of:
   - Expectancy (how to calculate and interpret)
   - System Quality Number (SQN) - Van Tharp's metric
   - Profit Factor
   - Sharpe Ratio for trading systems
   - Maximum Drawdown
   - Recovery Factor
   - Average R-Multiple

3. **Walk-Forward Analysis**:
   - What's the proper procedure?
   - How much data for optimization vs out-of-sample?
   - How many walk-forward periods are needed?

4. **Monte Carlo Simulation**:
   - How does it work for trading systems?
   - What should I look for in results?
   - How many simulations (1000? 10000?)?

5. **Curve Fitting Detection**:
   - How do I know if my system is overfit?
   - Warning signs to watch for?
   - How to make systems more robust?

6. **Paper Trading Duration**:
   - How long before going live?
   - What metrics should match backtest results?

7. **Benchmark Comparison**:
   - Should I compare to buy-and-hold SPY?
   - What's a "good" alpha for a swing trading system?

Please provide specific thresholds and guidelines I can use to evaluate my system.
```

---

## Prompt 5: Multi-Timeframe RSI Analysis

```
I'm using multi-timeframe RSI for entry confirmation in my swing trading system. Please validate this approach.

## Current Implementation:
- Daily chart: Identifies potential trade setups
- 4H chart RSI: Confirms entry timing
- Entry signal: 4H RSI < 40 (oversold) or rising from lows

## Questions:

1. **Is Multi-Timeframe Analysis Valid?**: What does academic research say about using multiple timeframes?
   - Does it improve results vs single timeframe?
   - What's the optimal timeframe ratio (daily + 4H = 6:1)?

2. **RSI Thresholds**:
   - Is 40 the right oversold level, or should it be 30?
   - Does this vary by market conditions?
   - Should I use RSI divergence instead of static levels?

3. **RSI Period on 4H Chart**:
   - Standard 14 periods = 56 hours = ~2.5 trading days
   - Is this appropriate for swing trading?
   - Would 21 or 10 periods be better?

4. **Alternative Confirmation Methods**:
   - Stochastic RSI
   - MACD on lower timeframe
   - Volume confirmation
   - Price action patterns
   - Which works best with daily chart setups?

5. **Entry Timing Research**:
   - How much does entry timing affect overall results?
   - Some say entries are only 10% of results - is this accurate?
   - Should I focus more on exits instead?

6. **Avoiding False Signals**:
   - What filters can prevent whipsaw in ranging markets?
   - How do professionals handle RSI false positives?

Please include any relevant research on multi-timeframe analysis effectiveness.
```

---

## Prompt 6: Position Sizing for Dual Strategy

```
I need to validate my position sizing approach for a dual-strategy swing trading system.

## Current Approach:
- **Pullback entries**: Full position (lower risk)
- **Momentum entries**: Half position (higher risk)
- **Risk per trade**: 1% of portfolio (fixed fractional)

## Questions:

1. **Is Variable Position Sizing Valid?**
   - Should position size vary by strategy/risk level?
   - Or should risk per trade be constant regardless of setup quality?

2. **Optimal Risk Per Trade**:
   - Is 1% too conservative?
   - What do professional swing traders use?
   - Van Tharp suggests up to 2% - when is this appropriate?

3. **Kelly Criterion**:
   - Should I use Kelly for optimal position sizing?
   - Half-Kelly or quarter-Kelly for safety?
   - How to calculate Kelly for a swing trading system?

4. **Portfolio Heat**:
   - Maximum total exposure at any time?
   - How many concurrent positions?
   - Correlation considerations?

5. **Scaling In/Out**:
   - Should I scale into positions?
   - Pyramid up as trade moves in my favor?
   - Or enter full position at once?

6. **Position Sizing by Market Regime**:
   - Reduce size in bear markets?
   - Increase in strong bull markets?
   - Go to 100% cash sometimes?

Please provide specific formulas and guidelines I can implement programmatically.
```

---

## How to Use These Prompts

1. **Start with Prompt 1** - Overall system validation
2. **Use Prompt 2** - If you want to add market regime detection
3. **Use Prompt 3** - To validate stop loss methodology
4. **Use Prompt 4** - Before running backtests
5. **Use Prompt 5** - To validate RSI approach
6. **Use Prompt 6** - To finalize position sizing

## Key Validation Criteria

| Metric | Target | Notes |
|--------|--------|-------|
| Win Rate | >40% | Combined with good R:R |
| Average R-Multiple | >1.5 | Expectancy driver |
| Profit Factor | >1.5 | Gross profit / gross loss |
| Max Drawdown | <20% | Risk management check |
| SQN | >2.0 | System quality indicator |
| Sharpe Ratio | >1.0 | Risk-adjusted returns |

---

*Save this document and use prompts as needed during system development*
