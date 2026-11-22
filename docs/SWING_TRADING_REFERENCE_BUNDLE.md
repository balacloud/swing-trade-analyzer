# Swing Trading System - Reference Bundle

> **Purpose:** Complete reference for bootstrapping a swing trading system
> **Use with:** Antigravity, Codex, GPT, or any AI coding assistant
> **Source:** Proven codebase built over 33 days of development

---

## STARTER PROMPT FOR AI

```
Build a swing trading screener with these components:

1. **Technical Indicators Module**
   - SMA (50, 200 day) - trend detection
   - EMA (8, 21 day) - short-term momentum
   - ATR (14 day) - volatility/stop loss
   - RSI (14 day) - overbought/oversold

2. **Relative Strength Calculator**
   - Compare stock 52-week return vs SPY
   - RS > 1.0 = outperforming market
   - This is THE #1 predictor for swing trading

3. **4-Criteria Binary Checklist (All must pass = TRADE)**
   - TREND: Price > 50 SMA > 200 SMA (Stage 2 uptrend)
   - MOMENTUM: RS > 1.0 (outperforming SPY)
   - SETUP: Stop within 7% of entry (tight risk)
   - RISK/REWARD: R:R ratio >= 2:1

4. **Support & Resistance Engine**
   - ZigZag pivot detection (5% threshold)
   - Agglomerative clustering for price levels
   - Touch-based scoring (more touches = stronger)
   - Fibonacci extensions for ATH stocks

5. **Data Source:** yfinance (free, 15-min delay, fine for swing trading)

**Stack:** Python Flask backend + React frontend (or your preference)

Use the reference code below - don't reinvent the wheel.
```

---

## CRITICAL INSIGHT (From Day 27 Backtesting)

```
Entry signals = ~10% of trading results
Position sizing = ~90% of trading results

Don't over-optimize the screener. Focus on position sizing.
```

---

## FILE 1: Technical Indicators (JavaScript)

```javascript
/**
 * Technical Indicators Calculator
 * Core functions: SMA, EMA, ATR, RSI
 */

// Simple Moving Average
export function calculateSMA(prices, period) {
  if (!prices || prices.length < period) return null;
  const slice = prices.slice(-period);
  return slice.reduce((sum, price) => sum + price, 0) / period;
}

// Exponential Moving Average
export function calculateEMA(prices, period) {
  if (!prices || prices.length < period) return null;

  const k = 2 / (period + 1);
  let ema = prices[0];

  for (let i = 1; i < prices.length; i++) {
    ema = prices[i] * k + ema * (1 - k);
  }

  return ema;
}

// Average True Range (for stop loss calculation)
export function calculateATR(highs, lows, closes, period = 14) {
  if (!highs || !lows || !closes || closes.length < period + 1) return null;

  const trueRanges = [];

  for (let i = 1; i < closes.length; i++) {
    const tr = Math.max(
      highs[i] - lows[i],
      Math.abs(highs[i] - closes[i - 1]),
      Math.abs(lows[i] - closes[i - 1])
    );
    trueRanges.push(tr);
  }

  const recentTR = trueRanges.slice(-period);
  return recentTR.reduce((sum, tr) => sum + tr, 0) / period;
}

// Relative Strength Index (Wilder's smoothing method)
export function calculateRSI(prices, period = 14) {
  if (!prices || prices.length < period + 1) return null;

  const changes = [];
  for (let i = 1; i < prices.length; i++) {
    changes.push(prices[i] - prices[i - 1]);
  }

  const gains = changes.map(c => c > 0 ? c : 0);
  const losses = changes.map(c => c < 0 ? Math.abs(c) : 0);

  let avgGain = gains.slice(0, period).reduce((sum, g) => sum + g, 0) / period;
  let avgLoss = losses.slice(0, period).reduce((sum, l) => sum + l, 0) / period;

  // Wilder's smoothing
  for (let i = period; i < changes.length; i++) {
    avgGain = (avgGain * (period - 1) + gains[i]) / period;
    avgLoss = (avgLoss * (period - 1) + losses[i]) / period;
  }

  if (avgLoss === 0) return 100;

  const rs = avgGain / avgLoss;
  const rsi = 100 - (100 / (1 + rs));

  return parseFloat(rsi.toFixed(2));
}

// Trend Analysis (Stage 2 detection)
export function analyzeTrend(prices) {
  const currentPrice = prices[prices.length - 1];
  const sma50 = calculateSMA(prices, 50);
  const sma200 = calculateSMA(prices, 200);
  const ema8 = calculateEMA(prices, 8);
  const ema21 = calculateEMA(prices, 21);

  return {
    currentPrice,
    sma50,
    sma200,
    ema8,
    ema21,
    isStage2: currentPrice > sma50 && sma50 > sma200,
    isShortTermBullish: currentPrice > ema8 && ema8 > ema21
  };
}
```

---

## FILE 2: Relative Strength Calculator (JavaScript)

```javascript
/**
 * Relative Strength (RS) Calculator
 * RS = (Stock % Change) / (SPY % Change)
 * RS > 1.0 = Outperforming the market
 */

export function calculateRelativeStrength(stockData, spyData) {
  const stockCurrent = stockData.currentPrice;
  const stock52wAgo = stockData.price52wAgo;
  const stock13wAgo = stockData.price13wAgo;

  const spyCurrent = spyData.currentPrice;
  const spy52wAgo = spyData.price52wAgo;
  const spy13wAgo = spyData.price13wAgo;

  if (!stockCurrent || !stock52wAgo || !spyCurrent || !spy52wAgo) {
    return { error: 'Insufficient data for RS calculation' };
  }

  // 52-week RS
  const stockReturn52w = stockCurrent / stock52wAgo;
  const spyReturn52w = spyCurrent / spy52wAgo;
  const rs52Week = stockReturn52w / spyReturn52w;

  // 13-week RS (short-term momentum)
  let rs13Week = null;
  if (stock13wAgo && spy13wAgo) {
    const stockReturn13w = stockCurrent / stock13wAgo;
    const spyReturn13w = spyCurrent / spy13wAgo;
    rs13Week = stockReturn13w / spyReturn13w;
  }

  // Trend detection
  let rsTrend = 'stable';
  if (rs13Week !== null) {
    if (rs13Week > rs52Week * 1.05) rsTrend = 'improving';
    else if (rs13Week < rs52Week * 0.95) rsTrend = 'declining';
  }

  // RS Rating (0-100 scale)
  const rsRating = Math.min(99, Math.max(1, Math.round((rs52Week - 0.5) * 80 + 10)));

  return {
    rs52Week: parseFloat(rs52Week.toFixed(3)),
    rs13Week: rs13Week ? parseFloat(rs13Week.toFixed(3)) : null,
    rsRating,
    rsTrend,
    passesQualityGate: rs52Week >= 1.0,
    interpretation: interpretRS(rs52Week)
  };
}

function interpretRS(rs) {
  if (rs >= 1.3) return 'Exceptional strength - Top tier performer';
  if (rs >= 1.2) return 'Strong outperformance vs market';
  if (rs >= 1.1) return 'Good relative strength';
  if (rs >= 1.0) return 'Performing in-line with market';
  if (rs >= 0.9) return 'Slight underperformance';
  return 'Significant laggard - Avoid';
}
```

---

## FILE 3: 4-Criteria Binary Checklist (JavaScript)

```javascript
/**
 * Simplified Binary Scoring System
 * 4 Criteria - ALL must pass = TRADE
 * Based on: AQR Momentum Research + Turtle Trading
 */

import { calculateSMA } from './technicalIndicators';

export function calculateSimplifiedAnalysis(stockData, spyData, srData) {
  const results = {
    criteria: {
      trend: { pass: false, label: 'Trend', reason: '' },
      momentum: { pass: false, label: 'Momentum', reason: '' },
      setup: { pass: false, label: 'Setup', reason: '' },
      risk: { pass: false, label: 'Risk/Reward', reason: '' }
    },
    verdict: 'PASS',
    passCount: 0
  };

  const prices = stockData.priceHistory.map(d => d.close);
  const currentPrice = prices[prices.length - 1];

  // CRITERION 1: TREND (Price > 50 SMA > 200 SMA)
  const sma50 = calculateSMA(prices, 50);
  const sma200 = calculateSMA(prices, 200);

  if (currentPrice > sma50 && sma50 > sma200) {
    results.criteria.trend.pass = true;
    results.criteria.trend.reason = `Stage 2 uptrend confirmed`;
  } else {
    results.criteria.trend.reason = `Not in Stage 2 uptrend`;
  }

  // CRITERION 2: MOMENTUM (RS > 1.0)
  if (stockData.priceHistory.length >= 252 && spyData?.priceHistory?.length >= 252) {
    const stockPrices = stockData.priceHistory.map(d => d.close);
    const spyPrices = spyData.priceHistory.map(d => d.close);

    const stockReturn = (stockPrices[stockPrices.length - 1] / stockPrices[stockPrices.length - 252]) - 1;
    const spyReturn = (spyPrices[spyPrices.length - 1] / spyPrices[spyPrices.length - 252]) - 1;
    const rsRatio = (1 + stockReturn) / (1 + spyReturn);

    if (rsRatio >= 1.0) {
      results.criteria.momentum.pass = true;
      results.criteria.momentum.reason = `RS ${rsRatio.toFixed(2)} - outperforming SPY`;
    } else {
      results.criteria.momentum.reason = `RS ${rsRatio.toFixed(2)} - underperforming SPY`;
    }
  }

  // CRITERION 3: SETUP (Stop within 7%)
  if (srData?.suggestedEntry && srData?.suggestedStop) {
    const stopPct = ((srData.suggestedEntry - srData.suggestedStop) / srData.suggestedEntry) * 100;

    if (stopPct <= 7 && stopPct > 0) {
      results.criteria.setup.pass = true;
      results.criteria.setup.reason = `Stop ${stopPct.toFixed(1)}% below entry - tight risk`;
    } else {
      results.criteria.setup.reason = `Stop ${stopPct.toFixed(1)}% - too wide (max 7%)`;
    }
  }

  // CRITERION 4: RISK/REWARD (>= 2:1)
  if (srData?.riskReward >= 2.0) {
    results.criteria.risk.pass = true;
    results.criteria.risk.reason = `R:R ${srData.riskReward.toFixed(2)}:1 - favorable`;
  } else {
    results.criteria.risk.reason = `R:R ${srData?.riskReward?.toFixed(2) || 'N/A'}:1 - want >= 2:1`;
  }

  // FINAL VERDICT
  results.passCount = Object.values(results.criteria).filter(c => c.pass).length;
  results.verdict = results.passCount === 4 ? 'TRADE' : 'PASS';

  return results;
}
```

---

## FILE 4: Support & Resistance Engine (Python)

```python
"""
Support & Resistance Engine
Methods: ZigZag Pivot Detection + Agglomerative Clustering
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


@dataclass
class SRConfig:
    """Configuration for S&R engine."""
    min_bars: int = 150
    zigzag_percent_delta: float = 0.05  # 5% min change for pivot
    merge_percent: float = 0.02  # 2% merge threshold
    touch_threshold: float = 0.005  # 0.5% = "touch"
    min_touches_for_level: int = 2
    atr_period: int = 14
    fib_extensions: Tuple[float, ...] = (1.272, 1.618, 2.0)


@dataclass
class SRLevels:
    """Container for S&R levels."""
    method: str
    support: List[float] = field(default_factory=list)
    resistance: List[float] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)


def calculate_atr(df: pd.DataFrame, period: int = 14) -> float:
    """Calculate Average True Range."""
    high = df["high"].values
    low = df["low"].values
    close = df["close"].values

    tr = np.zeros(len(df))
    tr[0] = high[0] - low[0]
    tr[1:] = np.maximum(
        high[1:] - low[1:],
        np.maximum(
            np.abs(high[1:] - close[:-1]),
            np.abs(low[1:] - close[:-1])
        )
    )

    return float(np.mean(tr[-period:]))


def detect_zigzag_pivots(
    df: pd.DataFrame,
    percent_delta: float = 0.05,
    min_bars: int = 5
) -> Tuple[List[float], List[float]]:
    """
    Detect significant pivot highs and lows using ZigZag algorithm.
    Filters noise by requiring minimum percent_delta change.
    """
    pivot_highs = []
    pivot_lows = []

    highs = df["high"].values
    lows = df["low"].values

    if len(highs) < min_bars * 2:
        return [], []

    # Initialize
    initial_high = np.max(highs[:min_bars])
    initial_low = np.min(lows[:min_bars])

    if initial_high / initial_low - 1 > percent_delta:
        last_pivot_type = 'high'
        last_pivot_price = initial_high
        pivot_highs.append(float(initial_high))
    else:
        last_pivot_type = 'low'
        last_pivot_price = initial_low
        pivot_lows.append(float(initial_low))

    last_pivot_idx = 0

    # Scan through data
    for i in range(min_bars, len(df)):
        current_high = highs[i]
        current_low = lows[i]

        if last_pivot_type == 'high':
            pct_change = (last_pivot_price - current_low) / last_pivot_price
            if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                pivot_lows.append(float(current_low))
                last_pivot_type = 'low'
                last_pivot_price = current_low
                last_pivot_idx = i
            elif current_high > last_pivot_price:
                if pivot_highs:
                    pivot_highs[-1] = float(current_high)
                last_pivot_price = current_high
                last_pivot_idx = i
        else:
            pct_change = (current_high - last_pivot_price) / last_pivot_price
            if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                pivot_highs.append(float(current_high))
                last_pivot_type = 'high'
                last_pivot_price = current_high
                last_pivot_idx = i
            elif current_low < last_pivot_price:
                if pivot_lows:
                    pivot_lows[-1] = float(current_low)
                last_pivot_price = current_low
                last_pivot_idx = i

    return sorted(list(set(pivot_highs))), sorted(list(set(pivot_lows)))


def cluster_with_agglom(
    pivot_prices: np.ndarray,
    merge_percent: float = 0.02,
    current_price: float = None
) -> List[float]:
    """
    Cluster pivot prices using AgglomerativeClustering.
    No fixed cluster count - uses distance threshold.
    """
    if len(pivot_prices) < 2:
        return list(pivot_prices)

    if current_price is None:
        current_price = float(np.mean(pivot_prices))

    merge_distance = current_price * merge_percent
    prices_2d = pivot_prices.reshape(-1, 1)

    clustering = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=merge_distance,
        linkage='average'
    )

    labels = clustering.fit_predict(prices_2d)

    centers = []
    for label in set(labels):
        cluster_prices = pivot_prices[labels == label]
        centers.append(float(np.median(cluster_prices)))

    return sorted(centers)


def score_levels(
    levels: List[float],
    df: pd.DataFrame,
    touch_threshold: float = 0.005
) -> List[Tuple[float, int]]:
    """Score levels by number of price touches."""
    scores = []

    for level in levels:
        upper = level * (1 + touch_threshold)
        lower = level * (1 - touch_threshold)

        high_touch = (df['high'] >= lower) & (df['high'] <= upper)
        low_touch = (df['low'] >= lower) & (df['low'] <= upper)

        touches = int((high_touch | low_touch).sum())
        scores.append((level, touches))

    return sorted(scores, key=lambda x: x[1], reverse=True)


def project_fibonacci_resistance(
    ath_price: float,
    swing_low: float,
    extensions: Tuple[float, ...] = (1.272, 1.618, 2.0)
) -> List[float]:
    """
    Project resistance using Fibonacci extensions.
    For stocks at all-time highs with no historical resistance.
    """
    if swing_low >= ath_price:
        return []

    price_range = ath_price - swing_low
    projected = []

    for ext in extensions:
        extension_amount = (ext - 1.0) * price_range
        level = round(ath_price + extension_amount, 2)
        projected.append(level)

    return projected


def compute_sr_levels(df: pd.DataFrame, cfg: SRConfig = None) -> SRLevels:
    """
    Main function: Compute Support & Resistance levels.

    Algorithm:
    1. Detect ZigZag pivots (significant swings only)
    2. Cluster pivots using AgglomerativeClustering
    3. Score levels by touch count
    4. Split into support/resistance around current price
    5. Project Fibonacci extensions for ATH stocks
    """
    cfg = cfg or SRConfig()
    current_price = float(df["close"].iloc[-1])
    atr = calculate_atr(df, cfg.atr_period)

    # Step 1: Detect ZigZag pivots
    pivot_highs, pivot_lows = detect_zigzag_pivots(
        df,
        percent_delta=cfg.zigzag_percent_delta,
        min_bars=5
    )

    all_pivots = pivot_highs + pivot_lows

    if len(all_pivots) < 2:
        # Fallback: project levels using ATR
        support = [round(current_price - m * atr, 2) for m in [1.0, 1.5, 2.0]]
        resistance = [round(current_price + m * atr, 2) for m in [1.0, 1.5, 2.0]]
        return SRLevels(method="atr_projection", support=support, resistance=resistance)

    # Step 2: Cluster pivots
    pivot_array = np.array(all_pivots)
    clustered_levels = cluster_with_agglom(
        pivot_array,
        merge_percent=cfg.merge_percent,
        current_price=current_price
    )

    # Step 3: Score levels by touches
    scored_levels = score_levels(clustered_levels, df, cfg.touch_threshold)

    valid_levels = [level for level, score in scored_levels
                   if score >= cfg.min_touches_for_level]

    if len(valid_levels) < 2:
        valid_levels = clustered_levels

    # Step 4: Split into support/resistance
    support = sorted([l for l in valid_levels if l <= current_price])
    resistance = sorted([l for l in valid_levels if l > current_price])

    # Step 5: Handle ATH (no resistance) - use Fibonacci
    if not resistance:
        swing_low = float(df['low'].tail(60).min())
        fifty_two_week_high = float(df['high'].max())

        if swing_low < current_price * 0.9:
            ath_reference = max(current_price, fifty_two_week_high)
            resistance = project_fibonacci_resistance(
                ath_reference, swing_low, cfg.fib_extensions
            )

    # Handle ATL (no support) - project using ATR
    if not support:
        support = [round(current_price - m * atr, 2) for m in [1.0, 1.5, 2.0]]
        support = [s for s in support if s > 0]

    meta = {
        "atr": round(atr, 2),
        "pivot_count": len(all_pivots),
        "level_scores": {str(round(l, 2)): s for l, s in scored_levels[:5]}
    }

    return SRLevels(
        method="agglomerative",
        support=support,
        resistance=resistance,
        meta=meta
    )
```

---

## QUICK SETUP

### Backend (Python)
```bash
pip install flask yfinance pandas numpy scikit-learn
```

### Frontend (React)
```bash
npx create-react-app swing-trader
cd swing-trader
npm install
```

### Data Source (yfinance)
```python
import yfinance as yf

def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return {
        "ticker": ticker,
        "currentPrice": df['Close'].iloc[-1],
        "price52wAgo": df['Close'].iloc[0] if len(df) >= 252 else None,
        "priceHistory": df.to_dict('records')
    }
```

---

## SWING TRADING CRITERIA SUMMARY

| Criterion | Rule | Why |
|-----------|------|-----|
| **Trend** | Price > 50 SMA > 200 SMA | Stage 2 uptrend (Minervini) |
| **Momentum** | RS > 1.0 vs SPY | Outperforming market |
| **Setup** | Stop within 7% | Tight risk management |
| **Risk/Reward** | R:R >= 2:1 | Favorable risk/reward |

**ALL 4 must pass = TRADE**
**Any fail = PASS (no trade)**

---

## REFERENCES

- Mark Minervini - SEPA methodology, VCP patterns
- William O'Neil - CAN SLIM strategy
- AQR - Momentum Factor Research
- Turtle Trading - Trend following principles

---

---

## DOCUMENTATION STRUCTURE (For AI Context Management)

> **Purpose:** Maintain context across sessions so AI doesn't lose track of progress
> **Proven:** Used over 33 days of development with Claude

### File Structure to Create

```
your-project/
├── docs/
│   ├── ai/                          # AI session documentation
│   │   ├── AI_CONTEXT.md            # Single reference point (read this first)
│   │   ├── stable/                  # Rarely change
│   │   │   └── GOLDEN_RULES.md      # Core rules learned from mistakes
│   │   ├── versioned/               # Day-versioned
│   │   │   ├── API_CONTRACTS_DAY[N].md
│   │   │   └── KNOWN_ISSUES_DAY[N].md
│   │   └── status/                  # Daily status
│   │       └── PROJECT_STATUS_DAY[N].md
│   └── research/                    # Research documents
└── README.md
```

### AI_CONTEXT.md Template

```markdown
# AI CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session
> **Last Updated:** Day [N] ([Date])

---

## CURRENT STATE

| Field | Value |
|-------|-------|
| Current Day | [N] |
| Version | v[X.Y] |
| Latest Status | PROJECT_STATUS_DAY[N].md |
| Latest Issues | KNOWN_ISSUES_DAY[N].md |
| Focus | [Current priority] |

---

## SESSION START CHECKLIST

1. Read GOLDEN_RULES.md - internalize the rules
2. Read PROJECT_STATUS - understand current state
3. Read KNOWN_ISSUES - know active bugs
4. Confirm to user: version, last accomplishments, priorities
5. Ask: "What would you like to focus on today?"

---

## SESSION CLOSE CHECKLIST

1. Create PROJECT_STATUS_DAY[N+1].md with:
   - What was accomplished today
   - What's pending
   - Next session priorities
2. Update KNOWN_ISSUES if bugs found/fixed
3. Update GOLDEN_RULES if new lessons learned
4. Update this file's CURRENT STATE table
5. Provide git commit command

---

## CORE RULES (Quick Reference)

1. BEFORE modifying any file: Read it first
2. NEVER assume code structure - verify with actual file
3. NEVER HALLUCINATE - Don't claim results without running
4. TEST incrementally - one change at a time
5. If fix fails, STOP and diagnose - don't chain guesses
```

### GOLDEN_RULES.md Template

```markdown
# GOLDEN RULES

> Rules learned from mistakes. NEVER violate these.

---

## Rule 1: Read Before Modify
NEVER modify a file without reading it first.
**Why:** Assumptions about code structure cause bugs.

## Rule 2: Verify Don't Assume
NEVER assume code structure - verify with actual file.
**Why:** Code evolves. What was true Day 1 may not be true Day 10.

## Rule 3: No Hallucination
NEVER claim results without actually running the code.
**Why:** False confidence leads to cascading bugs.

## Rule 4: Incremental Testing
TEST one change at a time.
**Why:** Multiple changes make debugging impossible.

## Rule 5: Stop on Failure
If a fix fails, STOP and diagnose - don't chain guesses.
**Why:** Guessing chains create 10x more bugs.

## Rule 6: Debug Properly
1. Understand the symptom
2. Form hypothesis about cause
3. Write diagnostic query to TEST hypothesis
4. Run diagnostic, analyze results
5. Only THEN write the fix
6. If fix fails, go back to step 2

---

## Project-Specific Rules

[Add rules specific to your project as you learn them]
```

### PROJECT_STATUS Template

```markdown
# PROJECT STATUS - Day [N] ([Date])

## Version: v[X.Y]

## Today's Focus: [Brief description]

---

## Accomplishments

### 1. [Feature/Fix Name]
- What was done
- Key implementation details
- Test results

### 2. [Feature/Fix Name]
- ...

---

## Files Modified

| File | Changes |
|------|---------|
| `path/to/file.py` | Brief description |

---

## Active State

| Item | Value |
|------|-------|
| Frontend Version | v[X.Y] |
| Backend Version | [X.Y] |
| Key Metric | [Value] |

---

## Next Session Priorities

### Priority 1: [Task Name]
- Brief description
- Why it matters

### Priority 2: [Task Name]
- ...

---

*Previous: PROJECT_STATUS_DAY[N-1].md*
*Next: PROJECT_STATUS_DAY[N+1].md*
```

### KNOWN_ISSUES Template

```markdown
# KNOWN ISSUES - Day [N]

---

## RESOLVED (Day [N])

| Issue | Resolution | Notes |
|-------|------------|-------|
| [Issue description] | [How it was fixed] | [Any notes] |

---

## OPEN ISSUES

### Priority: HIGH

#### 1. [Issue Title]
- **File:** `path/to/file.py`
- **Symptom:** What's happening
- **Root Cause:** Why (if known)
- **Solution:** Proposed fix

### Priority: MEDIUM

#### 1. [Issue Title]
- ...

### Priority: LOW

#### 1. [Issue Title]
- ...

---

## DEFERRED ITEMS

### 1. [Item Name]
- **Why Deferred:** Reason
- **When to Revisit:** Trigger condition
- **Effort:** Estimated time
```

---

## PROMPT FOR CODEX: Documentation Setup

```
Set up a documentation structure for maintaining AI context across sessions:

1. Create these files:
   - docs/ai/AI_CONTEXT.md (single reference point)
   - docs/ai/stable/GOLDEN_RULES.md (core rules)
   - docs/ai/status/PROJECT_STATUS_DAY1.md (daily status)
   - docs/ai/versioned/KNOWN_ISSUES_DAY1.md (bug tracker)

2. Use the templates provided in the reference bundle.

3. At START of each session:
   - Read AI_CONTEXT.md first
   - Read the latest PROJECT_STATUS
   - Confirm current state with user

4. At END of each session:
   - Create new PROJECT_STATUS_DAY[N+1].md
   - Update KNOWN_ISSUES if needed
   - Update AI_CONTEXT.md current state table

5. When you make a mistake, add it to GOLDEN_RULES.md so you don't repeat it.

This system ensures context is never lost between sessions.
```

---

## KEY INSIGHT: Why This Structure Works

| Problem | Solution |
|---------|----------|
| AI forgets context between sessions | Status files capture state |
| AI repeats same mistakes | GOLDEN_RULES prevents repetition |
| User has to re-explain everything | AI_CONTEXT provides quick catchup |
| Bugs get forgotten | KNOWN_ISSUES tracks all bugs |
| No clear priorities | Status files list next priorities |

**The 5-minute rule:** At session start, AI should be productive within 5 minutes of reading the docs.

---

*Generated from Swing Trade Analyzer v3.4 (Day 33)*
*Source: github.com/balacloud/swing-trade-analyzer*
