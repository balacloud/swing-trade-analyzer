# Breakout Engine Specification — STA Human-in-the-Loop

> **Purpose:** Single source of truth for breakout state definitions used by STA backend, TradingView Pine companion, frontend badges, Claude/GPT chart review, and forward testing.
>
> **Status:** v1 design spec — implementation must be validated against real tickers before treating it as production logic.
>
> **Scope:** Swing-trading breakout review only. This is not an auto-trading system and not execution advice.

---

## 1. Design Philosophy

The breakout engine is a **filter and review assistant**, not a prediction engine.

A veteran breakout trader does not only ask:

> Did price break resistance?

They ask:

> Did price break a meaningful level with institutional-style participation, controlled risk, limited overhead supply, and a clean invalidation point?

The engine therefore prioritizes avoiding bad breakouts over generating more signals.

---

## 2. System Responsibility Split

| Layer | Responsibility | Source of Truth |
|---|---|---|
| TradingView Screener | Candidate discovery | TradingView scanner fields |
| IBKR Scanner | Live activity/liquidity confirmation | IBKR market data |
| STA Backend Breakout Engine | Breakout state classification | `backend/breakout_detection.py` |
| TradingView Pine Companion | Visual mirror / human charting aid | Must mirror this spec |
| Claude/GPT Skill | Contextual chart review | Uses screenshots + this state language |
| Human Trader | Final decision and risk judgment | Human-in-the-loop |
| STA Forward Test | Reality validation | Journal + R-multiple outcomes |

**Architectural rule:** backend breakout engine is the producer. Frontend and prompts adapt to its API. Pine should remain a visual companion, not a competing source of truth.

---

## 3. Required Data Inputs

Minimum OHLCV requirements:

| Input | Required | Purpose |
|---|---:|---|
| Open | Yes | Candle body and rejection analysis |
| High | Yes | Resistance and candle range |
| Low | Yes | Support, retest, invalidation |
| Close | Yes | Breakout confirmation and trend checks |
| Volume | Yes | RVOL, volume expansion/dry-up |
| Benchmark OHLCV, usually SPY | Preferred | Relative strength check |

Minimum bars:

| Use | Bars |
|---|---:|
| Fast breakout classification | 80+ |
| Preferred swing review | 200+ |
| Full STA context | 2 years when available |

---

## 4. Core Calculations

| Calculation | Default | Purpose |
|---|---:|---|
| EMA20 | 20 bars | Short-term trend / retest support |
| SMA50 | 50 bars | Intermediate trend and extension |
| SMA200 | 200 bars | Stage 2 / institutional trend filter |
| Volume average | 20 bars | RVOL confirmation |
| Volume dry-up | 5-bar avg < 20-bar avg | Supply contraction clue |
| ATR | 14 bars | Volatility and candle range context |
| ATR average | 50 bars | Contraction detection |
| Resistance lookback | 60 bars | Fast pivot/level proxy |
| Support lookback | 60 bars | Fast invalidation proxy |

---

## 5. Default Thresholds

| Parameter | Default | Rationale |
|---|---:|---|
| Breakout buffer | 0.30% above resistance | Avoid penny-perfect false triggers |
| Near resistance zone | Within 2.00% of resistance | Watch zone before breakout |
| Retest zone | ±1.00% of breakout level | Practical retest tolerance |
| RVOL confirmation | ≥ 1.50x 20-bar volume | Participation confirmation |
| ATR contraction | ATR < 0.85 × ATR average | Volatility compression |
| Max extension from SMA50 | ≤ 12.00% | Avoid late chase entries |
| Recent breakout window | 30 bars | Retest/fail monitoring window |

These thresholds are **starting defaults**, not proven universal laws. They require forward testing and behavioral audits.

---

## 6. Trend Gate

`trendOk = true` only when:

| Condition | Meaning |
|---|---|
| Close > SMA50 | Price above intermediate trend |
| SMA50 > SMA200 | Stage 2 style alignment |
| SMA200 > SMA200 20 bars ago | Long-term trend rising |

If SMA200 history is unavailable, the system should return `null` or `false`, never fabricate trend strength.

---

## 7. Relative Strength Gate

`rsStrong = true` when:

| Condition | Meaning |
|---|---|
| Stock/benchmark ratio > 20-bar average of ratio | Stock is outperforming benchmark recently |

Preferred benchmark: SPY for U.S. stocks. Future Canadian logic may require a Canadian benchmark such as XIU/XIC or TSX index proxy.

If benchmark data is unavailable, return `rsStrong=false` and include evidence that benchmark data was unavailable. Do not fake RS.

---

## 8. Volume and Volatility Gates

| Gate | Condition | Interpretation |
|---|---|---|
| `volumeExpansion` | RVOL ≥ 1.50 | Participation confirms move |
| `volumeDryUp` | 5-bar volume avg < 20-bar volume avg | Supply may be drying up |
| `atrContracting` | ATR < 0.85 × ATR average | Volatility compression before expansion |

Professional interpretation:
- Dry-up before breakout is constructive.
- Expansion on breakout is constructive.
- High-volume red candle near resistance is negative.

---

## 9. Candle Quality Gates

A breakout candle is high quality only when all are true:

| Gate | Condition | Meaning |
|---|---|---|
| `strongClose` | Close location ≥ 0.75 | Close in top 25% of candle range |
| `strongBody` | Body ≥ 50% of candle range | Conviction candle |
| `lowUpperWick` | Upper wick ≤ 35% of range | Limited rejection |
| `wideRange` | Candle range ≥ 1.20 × ATR | Meaningful expansion |

`candleQualityOk = strongClose AND strongBody AND lowUpperWick AND wideRange`

This gate intentionally makes `BREAKOUT_CONFIRMED` harder to achieve.

---

## 10. Warning Gates

| Warning | Condition | Meaning |
|---|---|---|
| `rejectionCandle` | Close location ≤ 0.50 and upper wick ≥ 45% | Sellers rejected the move |
| `highVolumeRed` | Red candle with RVOL ≥ 1.50 | Distribution / supply clue |
| `supplyWarning` | Near resistance and (`rejectionCandle` OR `highVolumeRed`) | Avoid trusting breakout |
| `extensionRisk` | Price > 12% above SMA50 | Chase risk |
| `failedBreakout` | Close < breakout level - retest tolerance | Breakout failed |

Warnings have priority over bullish states.

---

## 11. State Definitions and Priority Order

The engine returns exactly one status.

Priority order:

1. `FAILED_BREAKOUT`
2. `SUPPLY_WARNING`
3. `EXTENDED_CHASE_RISK`
4. `RETEST_ENTRY`
5. `BREAKOUT_CONFIRMED`
6. `BREAKOUT_WATCH`
7. `BUILDING_BASE`
8. `NOT_READY`

### 11.1 FAILED_BREAKOUT

Return when:

| Required | Condition |
|---|---|
| Recent breakout exists | Close exceeded prior resistance within recent breakout window |
| Failure condition | Current close < breakout level × (1 - retest tolerance) |

Human action:
> Avoid or reassess; breakout level failed.

### 11.2 SUPPLY_WARNING

Return when:

| Required | Condition |
|---|---|
| Near resistance | Price is within near-resistance zone |
| Supply evidence | Rejection candle OR high-volume red candle |

Human action:
> Wait; sellers/rejection visible near resistance.

### 11.3 EXTENDED_CHASE_RISK

Return when:

| Required | Condition |
|---|---|
| Extension risk | Price is more than max extension above SMA50 |

Human action:
> Avoid chasing; wait for pullback or base reset.

### 11.4 RETEST_ENTRY

Return when:

| Required | Condition |
|---|---|
| Recent breakout exists | Breakout within recent window |
| Retest zone touched | Low <= retest zone high |
| Level held | Close >= retest zone low and close > breakout level |
| Short trend intact | Close > EMA20 |

Human action:
> Review for possible retest entry with defined stop.

### 11.5 BREAKOUT_CONFIRMED

Return when all are true:

| Required | Condition |
|---|---|
| Price breakout | Close > resistance + breakout buffer |
| Trend | `trendOk` |
| Volume | `volumeExpansion` |
| Relative strength | `rsStrong` |
| Candle | `candleQualityOk` |
| Extension | `notExtended` |
| Supply | No `supplyWarning` |

Human action:
> Valid candidate; verify chart context and risk/reward before trade.

### 11.6 BREAKOUT_WATCH

Return when:

| Required | Condition |
|---|---|
| Near resistance | Within watch zone |
| Trend | `trendOk` |
| Compression | `atrContracting` OR `volumeDryUp` |
| Relative strength | `rsStrong` |
| Not confirmed | Not `BREAKOUT_CONFIRMED` |
| Supply | No `supplyWarning` |

Human action:
> Watch closely; wait for decisive close/volume confirmation.

### 11.7 BUILDING_BASE

Return when:

| Required | Condition |
|---|---|
| Price above SMA50 | Intermediate trend intact |
| Price below resistance | Not broken out yet |
| Compression | `atrContracting` OR `volumeDryUp` |

Human action:
> Monitor; base/compression may be forming.

### 11.8 NOT_READY

Return when none of the above states applies.

Human action:
> Ignore for now or keep on watchlist.

---

## 12. API Contract Draft

Endpoint:

```text
GET /api/breakout/<ticker>
```

Expected response shape:

```json
{
  "ticker": "IBM",
  "status": "BREAKOUT_WATCH",
  "humanAction": "Watch closely; wait for decisive close/volume confirmation.",
  "currentPrice": 248.25,
  "breakoutLevel": 245.50,
  "supportLevel": 238.00,
  "invalidation": 238.00,
  "retestZoneLow": 243.05,
  "retestZoneHigh": 247.95,
  "rvol": 1.62,
  "atrPct": 2.10,
  "extensionFromSma50Pct": 6.40,
  "checks": {
    "trendOk": true,
    "rsStrong": true,
    "volumeExpansion": false,
    "candleQualityOk": false
  },
  "warnings": {
    "supplyWarning": false,
    "extensionRisk": false,
    "failedBreakout": false
  },
  "evidence": {
    "method": "STA breakout v1 — price/volume/candle/RS filter",
    "resistanceLookbackBars": 60,
    "supportLookbackBars": 60,
    "closeLocation": 0.82,
    "bodyPct": 0.58,
    "upperWickPct": 0.12
  },
  "timestamp": "2026-06-01T...Z"
}
```

Missing values must be returned as `null`, not fake zeros.

---

## 13. Frontend Display Rules

| Status | Badge | Human Meaning |
|---|---|---|
| `BREAKOUT_CONFIRMED` | Green | Valid candidate, still needs risk review |
| `RETEST_ENTRY` | Blue | Potential safer secondary entry |
| `BREAKOUT_WATCH` | Amber | Watch, not trade-ready |
| `BUILDING_BASE` | Gray | Developing setup |
| `SUPPLY_WARNING` | Red | Sellers/rejection present |
| `FAILED_BREAKOUT` | Red | Avoid/reassess |
| `EXTENDED_CHASE_RISK` | Orange | Too extended |
| `NOT_READY` | Muted | Ignore/watchlist only |

Do not display a green badge as a buy recommendation.

---

## 14. Pine Companion Rules

The Pine script should visually mirror these same states.

Allowed difference:
- Pine may use simpler level detection due to charting constraints.

Not allowed:
- Pine must not redefine state meanings differently from this spec.
- Pine must not display a confirmed breakout if backend criteria would classify it as supply warning or extended chase risk.

---

## 15. Claude/GPT Review Rules

Claude/GPT prompt should treat the engine status as **evidence**, not truth.

Claude/GPT must independently review:

1. Price structure
2. Candle quality
3. Volume quality
4. Overhead supply
5. Extension risk
6. Risk/reward
7. Market context

The prompt may downgrade a backend `BREAKOUT_CONFIRMED` if visible chart context shows overhead supply or weak market context.

---

## 16. Validation Plan

Minimum behavioral test before frontend integration:

| Ticker Type | Example | Expected Purpose |
|---|---|---|
| Mega-cap trend | MSFT / AAPL | Normal trend state |
| Breakout-style candidate | IBM / NVDA | Watch/confirmed logic |
| Extended winner | PLTR / high momentum name | Extension risk |
| Failed breakout | Select manually | Failed breakout detection |
| Weak downtrend | Any below 50/200 | NOT_READY |

Validation steps:

1. Run `/api/breakout/<ticker>`.
2. Open TradingView daily chart with Pine companion.
3. Compare backend state vs Pine state.
4. Use Claude/GPT screenshot prompt for chart review.
5. Record discrepancies.
6. Fix only after diagnosing root cause.

---

## 17. Known Limitations v1

| Limitation | Reason |
|---|---|
| Resistance uses simple rolling high | Fast backend classification; richer S&R engine remains separate |
| No true multi-touch resistance scoring yet | Planned future enhancement |
| No overhead supply zone engine yet | Requires gap/red-candle zone detection |
| No accumulation/distribution day count yet | Institutional layer planned later |
| Canadian benchmark unresolved | Existing known issue: Canadian Analyze page needs redesign |
| Not backtested yet | Must be forward-tested before edge claims |

---

## 18. Future Enhancements

Priority order:

1. Multi-touch resistance scoring
2. Weekly timeframe confirmation
3. Overhead supply zone detection
4. Accumulation/distribution day count
5. IBKR live activity confirmation
6. Frontend scan badge
7. Forward-test breakout-specific fields
8. Behavioral audit across 20+ tickers

---

## 19. Audit Verdict

> **Claim:** This breakout engine can improve STA by adding entry-timing discipline.

**Reasoning:** The design combines trend, relative strength, volatility contraction, volume participation, candle quality, supply warnings, and extension risk. This is logically consistent with professional breakout review. However, no performance edge is proven until behavioral tests and forward testing validate the states.

**Verdict:** [PLAUSIBLE — REASON: Architecturally sound and consistent with practitioner principles, but not yet performance-validated.]

---

*Spec owner: STA backend breakout engine. Any future Pine/frontend/prompt changes should reference this file.*
