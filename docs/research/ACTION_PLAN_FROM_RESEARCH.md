# Action Plan: Research-Backed Feature Implementation

> **Date:** February 7, 2026 (Day 48)
> **Source:** Critical review of Grok/ChatGPT/Perplexity research
> **Principle:** Only implement what's VERIFIED - defer what's UNCERTAIN

---

## Implementation Roadmap

### Phase 1: Quick Wins (1-2 hours each)

These are verified useful, low complexity, data available via yfinance.

#### 1.1 OBV (On-Balance Volume) Indicator
**Consensus:** All three sources agree OBV is the most reliable volume indicator.

| Aspect | Details |
|--------|---------|
| What | Cumulative volume measure: +volume on up days, -volume on down days |
| Why | Shows accumulation/distribution before price moves |
| Where | Add to technical indicators display |
| Data | yfinance OHLCV ✅ |
| Effort | Low - standard formula |

**Implementation:**
```python
# Already calculated in some libraries, or:
obv = (np.sign(close.diff()) * volume).cumsum()
# Display: OBV trend (rising/falling/flat) vs price trend
```

**Value Signal:** OBV rising while price flat = accumulation (bullish)

---

#### 1.2 Earnings Calendar Warning
**Consensus:** ChatGPT highlights this as "event risk dominates technicals."

| Aspect | Details |
|--------|---------|
| What | Flag stocks with earnings within X days |
| Why | Avoid surprise gaps that invalidate technicals |
| Where | Add warning badge on analysis card |
| Data | yfinance `.calendar` or `.earnings_dates` |
| Effort | Low |

**Implementation:**
```python
ticker = yf.Ticker("AAPL")
earnings = ticker.calendar  # Check 'Earnings Date'
# If within 7 days: Show "⚠️ Earnings in X days"
```

**Decision:** User can choose to trade or wait based on warning.

---

#### 1.3 Enhanced Volume Display (RVOL)
**What we have:** 1.5x volume threshold for breakout confirmation.
**What to add:** Show actual RVOL ratio on UI.

| Aspect | Details |
|--------|---------|
| What | Display "Volume: 2.3x avg" instead of just "confirmed/not" |
| Why | Gives trader context on strength |
| Where | Pattern breakout section |
| Data | Already calculated ✅ |
| Effort | Very Low - UI change only |

---

### Phase 2: Sector Rotation Tab (4-6 hours)

**Consensus:** All sources agree RS ratio is the simplest effective method.

#### 2.1 Sector RS Calculation

| Aspect | Details |
|--------|---------|
| What | RS = Sector ETF Price / SPY Price |
| Timeframe | Daily, with 20-day and 50-day MA |
| Ranking | Sort sectors by RS momentum |
| Data | yfinance for all sector ETFs ✅ |

**Sector ETFs (verified standard):**
- XLK (Tech), XLF (Financials), XLV (Healthcare)
- XLE (Energy), XLI (Industrials), XLP (Staples)
- XLY (Discretionary), XLU (Utilities), XLRE (Real Estate)
- XLC (Communication), XLB (Materials)

#### 2.2 Simple 3-Criteria System (from ChatGPT)

Instead of complex RRG quadrants:

| Criteria | Meaning |
|----------|---------|
| RS > 0 (or > 1.0) | Sector outperforming SPY |
| RS > 20-day MA | Momentum is positive |
| Sector near 52-week high | Sustained strength |

**Display:** Rank table showing:
- Sector name
- Current RS ratio
- RS trend (up/down arrow)
- Momentum score (0-3 based on criteria)

#### 2.3 Integration with Stock Analysis

**Filter Logic:**
- If stock's sector is in Bottom 3: Show warning "Sector is lagging"
- If stock's sector is in Top 3: Show "Sector is leading"

This aligns with research consensus: "50% of stock move ties to sector."

---

### Phase 3: Research Required (Before Implementation)

#### 3.1 Verify yfinance Options Data

**BLOCKER:** Before any OI features, must verify data availability.

```python
# Run this test:
import yfinance as yf
ticker = yf.Ticker("AAPL")
try:
    options = ticker.option_chain()
    print("Calls OI:", options.calls['openInterest'].head())
    print("Puts OI:", options.puts['openInterest'].head())
except Exception as e:
    print("Options data NOT available:", e)
```

**If successful:** Add to Phase 4 roadmap
**If fails:** Document blocker, explore alternatives (Polygon.io, OCC)

---

#### 3.2 Divergence Detection Backtest

Before implementing RSI/MACD divergence detection:

1. Define exact detection algorithm
2. Backtest on 100+ stocks over 2 years
3. Calculate OUR OWN false positive rate
4. Only implement if FPR < 40%

**Why:** ChatGPT correctly states generic FPR numbers are unverifiable.

---

### Phase 4: Deferred (Low Priority or Blocked)

| Feature | Reason for Deferral |
|---------|---------------------|
| **Options Open Interest** | Data availability uncertain - verify first |
| **Seasonal Patterns** | ChatGPT: "small edge", regime-dependent |
| **H&S Pattern Detection** | Academic research "scarce and inconclusive" |
| **Full RRG Charts** | Overkill - simple RS ranking is sufficient |
| **Optimal Weighting System** | No universal answer exists - would need walk-forward testing |

---

## Verification Checklist

Before implementing each feature:

- [ ] Is the claim verified by multiple sources?
- [ ] Is the data available via yfinance (free)?
- [ ] Does it add actionable information (not just complexity)?
- [ ] Can we compute our own accuracy/FPR if needed?
- [ ] Does it integrate with existing categorical system?

---

## Estimated Timeline

| Phase | Features | Effort | Priority |
|-------|----------|--------|----------|
| 1.1 | OBV Indicator | 2 hours | HIGH |
| 1.2 | Earnings Warning | 1 hour | HIGH |
| 1.3 | RVOL Display | 30 min | HIGH |
| 2 | Sector Rotation Tab | 4-6 hours | MEDIUM |
| 3.1 | Options Data Verification | 30 min | RESEARCH |
| 3.2 | Divergence Backtest | 2-3 hours | RESEARCH |

---

## What We're NOT Doing (and Why)

1. **Not chasing accuracy percentages** - They're unverifiable
2. **Not implementing complex weighting** - No universal optimal exists
3. **Not building H&S detection** - Research is inconclusive
4. **Not building full RRG** - RS ranking achieves same goal simpler
5. **Not trusting specific FPR numbers** - We'll compute our own

---

## Success Metrics

For each implemented feature, track:

1. **Does it change any BUY/HOLD/AVOID verdicts?** (If never changes anything, remove it)
2. **Do users find it actionable?** (Feedback)
3. **Does it correlate with forward test results?** (R-multiples)

---

*Action plan based on verified research only. Speculation excluded.*
