# STA Breakout Human-in-the-Loop Workflow

This document defines the workflow for using TradingView screeners, the STA Pine companion script, Claude/GPT chart review, and STA forward testing.

## Goal

Use automation to narrow candidates and standardize chart review, while keeping final trading decisions human-controlled.

This is not an auto-trading system.

## Workflow

```text
TradingView Screener
        ↓
STA Pine Breakout Companion
        ↓
Screenshot with checklist visible
        ↓
Claude/GPT chart review prompt
        ↓
Human decision
        ↓
STA forward test / journal
```

## Step 1 — TradingView Screener

Use TradingView to reduce the stock universe before opening charts.

Suggested starter filters:

| Filter | Purpose |
|---|---|
| Price above 50 SMA | Avoid weak downtrends |
| 50 SMA above 200 SMA | Stage 2 / trend alignment |
| Relative volume elevated or volume above average | Participation |
| Market cap minimum | Avoid illiquid junk |
| Average dollar volume minimum | Tradability |
| 1M / 3M performance positive | Momentum |
| Sector strength positive | Institutional tailwind |

The screener finds candidates. It does not make decisions.

## Step 2 — Apply STA Pine Companion

Open each candidate chart in TradingView and apply:

`pine/sta_breakout_companion.pine`

Use the default daily timeframe first.

Review the status:

| Status | Meaning |
|---|---|
| NOT READY | No clean setup yet |
| BUILDING BASE | Compression or consolidation forming |
| BREAKOUT WATCH | Near resistance with trend/RS/compression |
| BREAKOUT CONFIRMED | Price cleared resistance with trend, volume, and candle quality |
| SUPPLY WARNING | Rejection or high-volume selling near resistance |
| RETEST ENTRY | Old resistance appears to hold as support |
| FAILED BREAKOUT | Price closed back below breakout level |

## Step 3 — Screenshot Rules

For Claude/GPT review, the screenshot should include:

- Daily candles
- Volume bars
- STA Pine checklist table
- Support/resistance lines
- SMA50 and SMA200
- At least 6 months of price history
- If possible, include weekly chart screenshot separately

Avoid cropped screenshots that hide left-side overhead supply.

## Step 4 — Claude/GPT Chart Review Prompt

Use this prompt with each screenshot:

```text
Analyze this TradingView chart using the STA breakout workflow.

Do not predict blindly. Act as a senior chart reviewer.

Review:
1. Breakout status: NOT READY / BUILDING BASE / WATCH / CONFIRMED / RETEST / FAILED
2. Price structure and support/resistance quality
3. Volume quality and RVOL confirmation
4. Candle quality: close location, body strength, upper wick rejection
5. Volatility contraction or expansion
6. Relative strength clues
7. Overhead supply risk
8. Extension risk from moving averages
9. False breakout risk
10. Best human action: ignore / watch / wait for retest / valid setup / avoid

Return a table with:
- Observation
- Evidence from chart
- Interpretation
- Risk
- Verdict

End with:
Final classification:
Action:
Invalidation level:
What would change my mind:
```

## Step 5 — Human Decision

The human decision should consider:

| Question | Pass condition |
|---|---|
| Is the market regime supportive? | SPY above key moving averages / risk-on context |
| Is the stock a leader? | Relative strength positive |
| Is the breakout level meaningful? | Multiple touches or clear pivot |
| Is volume confirming? | RVOL expansion on breakout |
| Is candle quality strong? | Close near high, limited upper wick |
| Is risk/reward acceptable? | Stop distance allows at least 2R target |
| Is the stock too extended? | Not too far above SMA50 |
| Is there overhead supply? | No obvious nearby resistance shelf/gap |

## Step 6 — STA Forward Testing

Every accepted setup should be logged in STA forward testing.

Minimum journal fields:

| Field | Example |
|---|---|
| Ticker | IBM |
| Setup type | Breakout / Retest |
| Pine status | WATCH / CONFIRMED / RETEST |
| Entry | 245.50 |
| Stop | 238.00 |
| Target | 260.50 |
| R:R | 2.0+ |
| Screenshot reviewed | Yes |
| Claude/GPT classification | Confirmed but watch overhead supply |
| Outcome | Win/Loss/Break-even |
| R multiple | +2R / -1R |

## Operating Rule

A Pine alert is not a buy signal.

A Claude/GPT review is not a buy signal.

A trade is only valid when:

1. Screener finds candidate
2. Pine marks a valid state
3. Human verifies chart quality
4. Risk/reward is acceptable
5. Setup is logged for forward testing

## Future v3 Enhancements

- Multi-touch resistance scoring
- Weekly timeframe confirmation
- Overhead supply zone detection
- Inside-bar / tight-close sequence recognition
- Screenshot annotation standard
- STA backend breakout endpoint
- Breakout tab in Scan results
