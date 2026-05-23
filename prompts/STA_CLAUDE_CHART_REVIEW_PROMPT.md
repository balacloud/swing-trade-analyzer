# STA Claude/GPT Chart Review Prompt

Use this prompt after taking a TradingView screenshot with the STA Pine Breakout Companion visible.

## Required screenshot contents

Before using this prompt, make sure the screenshot includes:

- Daily candlestick chart
- Volume bars
- STA Pine checklist table
- Support/resistance lines
- EMA20, SMA50, SMA200
- At least 6 months of price history
- Enough left-side chart history to see overhead supply
- Optional but preferred: second screenshot of weekly chart

---

## Prompt

```text
You are acting as a senior swing-trading chart reviewer using the STA Breakout Human-in-the-Loop workflow.

Do not act as an auto-trading bot. Do not give blind buy/sell advice. Your job is to review chart quality, identify risks, and help a human decide whether the setup deserves attention.

Analyze the attached TradingView screenshot.

Important context:
- The chart may include the STA Pine Breakout Companion.
- Treat Pine labels as helpful evidence, not truth.
- Verify the setup independently from price, volume, candles, support/resistance, and trend.
- Be skeptical of weak breakouts, late entries, overhead supply, and high-volume rejection candles.

Review the chart using these sections:

1. Breakout status
Classify as exactly one:
- NOT READY
- BUILDING BASE
- BREAKOUT WATCH
- BREAKOUT CONFIRMED
- RETEST ENTRY
- EXTENDED / CHASE RISK
- SUPPLY WARNING
- FAILED BREAKOUT

2. Price structure
Evaluate:
- Is the stock forming higher highs and higher lows?
- Is the stock above EMA20 / SMA50 / SMA200?
- Is the 50 SMA above the 200 SMA?
- Is the 200 SMA rising or flat/declining?

3. Support and resistance quality
Evaluate:
- Is the resistance level obvious?
- How many touches/rejections are visible?
- Is support nearby enough to create a logical stop?
- Is this a clean level or a messy zone?

4. Candle quality
Evaluate:
- Did the breakout candle close near the high?
- Is the candle body strong?
- Is there a large upper wick/rejection?
- Was the candle range meaningfully larger than recent candles?

5. Volume quality
Evaluate:
- Is volume expanding on the breakout?
- Was there volume dry-up before the move?
- Are there high-volume red candles near resistance?
- Does volume suggest accumulation or distribution?

6. Volatility and base quality
Evaluate:
- Is there visible volatility contraction?
- Is the base tight or sloppy?
- Are pullbacks controlled or deep?
- Does this resemble a VCP / flat base / cup-with-handle style setup?

7. Relative strength and leadership
Evaluate:
- Does the stock appear to outperform the market?
- Is it acting like a leader or laggard?
- Does the sector context appear supportive if visible?

8. Overhead supply risk
Evaluate:
- Are there prior breakdown levels above current price?
- Are there large red candles, gaps, or trapped-buyer zones overhead?
- Is the next resistance too close to justify the risk?

9. Entry and risk quality
Evaluate:
- Is current price actionable or too extended?
- Would a retest entry be safer?
- Where is the logical invalidation level?
- Is there room for at least 2R before major resistance?

10. Final decision support
Return this table:

| Area | Observation | Evidence from chart | Risk | Verdict |
|---|---|---|---|---|
| Trend |  |  |  | PASS / WAIT / FAIL |
| Resistance |  |  |  | PASS / WAIT / FAIL |
| Candle |  |  |  | PASS / WAIT / FAIL |
| Volume |  |  |  | PASS / WAIT / FAIL |
| Volatility/Base |  |  |  | PASS / WAIT / FAIL |
| Overhead Supply |  |  |  | PASS / WAIT / FAIL |
| Risk/Reward |  |  |  | PASS / WAIT / FAIL |

End with:

Final classification:
Human action:
- Ignore
- Watch
- Wait for retest
- Valid setup but needs risk plan
- Avoid

Ideal entry zone:
Invalidation level:
Main risk:
What would improve the setup:
What would invalidate the setup:
Confidence level: Low / Medium / High

Use calibrated language. If the screenshot does not show enough information, say what is missing instead of guessing.
```

---

## Review philosophy

Pine detects structure.
Claude/GPT interprets context.
The human makes the final risk decision.
STA forward testing validates whether the workflow has an edge.
