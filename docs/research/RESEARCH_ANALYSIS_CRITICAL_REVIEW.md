# Critical Analysis: Multi-Source Research Review

> **Date:** February 7, 2026 (Day 48)
> **Sources Analyzed:** Grok, ChatGPT, Perplexity
> **Purpose:** Extract verified, actionable insights - reject unverifiable claims
> **Approach:** No confirmation bias - question everything

---

## Source Credibility Assessment

| Source | Strengths | Weaknesses |
|--------|-----------|------------|
| **Grok** | Specific numbers, detailed breakdowns | Numbers often unverifiable, may be hallucinated |
| **ChatGPT** | Honest about limitations ("Not verified", "compute your own") | Conservative, fewer actionable specifics |
| **Perplexity** | Cites sources with links | Some links may be outdated or broken |

**Winner for honesty:** ChatGPT - explicitly states when data isn't verifiable

---

## Claim Verification Matrix

### Volume Indicators

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| OBV is reliable for swing trading | ✅ | ✅ | ✅ | **YES** | Consensus across all sources, well-documented indicator |
| CMF/A-D for money flow | ✅ | ✅ | ✅ | **YES** | Standard technical analysis |
| RVOL for breakout confirmation | ✅ | ✅ | ✅ | **YES** | We already use 1.5x volume threshold |
| "75-80% accuracy combining indicators" | - | - | ✅ | **NO** | Unverifiable claim, no methodology cited |

**Verdict:** OBV, CMF, RVOL are verified useful. Accuracy percentages are suspect.

### Open Interest Data Sources

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| yfinance has options OI | - | - | ✅ | **NEEDS TESTING** | Must verify with actual API call |
| Yahoo Finance endpoints work | ✅ | ✅ | - | **PARTIAL** | Known to break, rate-limited |
| OCC has free data | ✅ | ✅ | - | **YES** | Official but requires parsing |
| Polygon.io free tier | ✅ | - | ✅ | **YES** | 15-min delayed, limited calls |

**Verdict:** No reliable FREE source for real-time OI. yfinance claim needs verification before implementation.

### Time Cycles

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| Multiple timeframe analysis works | ✅ | ✅ | ✅ | **YES** | Standard practice, we already do this |
| Seasonality has small edge | - | ✅ | - | **PROBABLY** | ChatGPT most honest - "use as context, not signal" |
| "60% win rate with daily charts" | - | - | ✅ | **NO** | Specific percentage unverifiable |
| Earnings proximity matters | - | ✅ | - | **YES** | Common sense, avoids gap risk |

**Verdict:** Stick with MTF. Seasonality is low priority. Earnings calendar = HIGH VALUE.

### Optimal Weighting

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| Price 40-50%, Volume 20-30% | ✅ | - | ✅ | **NO** | No universal optimal weight exists |
| Walk-forward testing needed | - | ✅ | - | **YES** | This is the correct approach |
| No universal answer | - | ✅ | - | **YES** | Most honest assessment |

**Verdict:** ChatGPT is right - there's NO universal optimal weight. Anyone giving specific percentages is guessing. Use walk-forward testing if we implement weighting.

### Trend Reversal False Positive Rates

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| H&S false positive 27-46% | ✅ | - | - | **NO** | Grok gives specific range, ChatGPT says "not available" |
| Double Top 25-35% FPR | ✅ | - | ✅ | **NO** | Same issue - varies by definition |
| Academic research "scarce and inconclusive" | - | ✅ | ✅ | **YES** | NY Fed paper confirms this |
| Hybrid approach best | ✅ | ✅ | ✅ | **YES** | Consensus |

**Verdict:** Specific FPR numbers are UNVERIFIABLE. We must compute our own if implementing. Hybrid approach is verified best practice.

### Sector Rotation

| Claim | Grok | ChatGPT | Perplexity | Verified? | Notes |
|-------|------|---------|------------|-----------|-------|
| RS ratio (Sector/SPY) is effective | ✅ | ✅ | ✅ | **YES** | Simple, proven method |
| RRG is complex, simpler works | ✅ | ✅ | ✅ | **YES** | Consensus |
| 2-8 week lead time | - | - | ✅ | **UNVERIFIABLE** | Varies by market regime |
| SPDR ETFs best proxies | ✅ | ✅ | ✅ | **YES** | XLK, XLF, etc. are standard |
| Filter stocks by sector first | ✅ | ✅ | ✅ | **YES** | Top-down approach validated |

**Verdict:** Sector RS ranking is verified useful and simple to implement.

---

## Red Flags Identified

### 1. Specific Accuracy Percentages
- "75-80% accuracy" (Perplexity)
- "60% win rate with daily charts" (Perplexity)
- "65-75% success with confirmation" (Grok)

**Problem:** No methodology, no sample size, no time period. These are likely approximations or marketing claims.

### 2. False Positive Rate Claims
- Grok gives specific ranges (27-46%, 25-35%)
- ChatGPT explicitly says "Not available as a single universal number"

**Problem:** FPR depends entirely on:
- Pattern definition (what counts as valid H&S?)
- Timeframe
- Market regime
- Entry/exit rules

**Correct approach:** Compute YOUR OWN FPR with YOUR detection algorithm.

### 3. Optimal Weights
- Grok: "40-50% price, 20-30% volume"
- ChatGPT: "Not universally verifiable"

**Problem:** Weights that work in one regime fail in another. Anyone claiming optimal weights is oversimplifying.

---

## What's Actually Useful for STA

### Tier 1: High Value, Verified, Low Complexity

| Feature | Value | Complexity | Data Available? | Recommendation |
|---------|-------|------------|-----------------|----------------|
| **OBV Indicator** | Confirms accumulation/distribution | Low | yfinance ✅ | **IMPLEMENT** |
| **RVOL Display** | Already have 1.5x, add visual | Low | yfinance ✅ | **IMPLEMENT** |
| **Sector RS Ranking** | Filter by sector strength | Medium | yfinance ✅ | **IMPLEMENT** |
| **Earnings Calendar** | Avoid gap risk | Low | yfinance ✅ | **IMPLEMENT** |

### Tier 2: Medium Value, Needs Validation

| Feature | Value | Complexity | Data Available? | Recommendation |
|---------|-------|------------|-----------------|----------------|
| **RSI/MACD Divergence** | Reversal signals | Medium | yfinance ✅ | RESEARCH MORE |
| **Volume Divergence** | OBV vs price divergence | Medium | yfinance ✅ | RESEARCH MORE |
| **Time-in-base** | Already partial in patterns | Low | Calculated ✅ | ENHANCE |

### Tier 3: Low Value or Blocked

| Feature | Value | Complexity | Data Available? | Recommendation |
|---------|-------|------------|-----------------|----------------|
| **Options OI** | Would be high value | High | **UNCERTAIN** | VERIFY DATA FIRST |
| **Seasonal Patterns** | "Small edge" per ChatGPT | High | Calculated | DEFER |
| **H&S Detection** | High FPR, subjective | High | Calculated | DEFER |
| **Full RRG Charts** | Overkill | High | Calculated | DEFER - RS ranking is enough |

---

## Key Insights Worth Keeping

### From ChatGPT (Most Honest):
1. "Not universally verifiable" - acknowledge uncertainty
2. "Compute your own false-positive rate" - don't trust generic numbers
3. "Walk-forward testing for weights" - empirical > theoretical
4. "Time analysis: event time, setup maturity, seasonality" - good framework

### From Perplexity (Best Links):
1. NY Fed paper confirms pattern research is "scarce and inconclusive"
2. StockCharts RRG articles for reference if needed
3. Investopedia for indicator definitions

### From Grok (Best Structure):
1. "Gated confirmation model" for reversals - Gate A (structure), Gate B (2 of 3 signals), Gate C (trigger)
2. MVP indicator list per dimension

---

## Contradictions Between Sources

| Topic | Grok Says | ChatGPT Says | Truth |
|-------|-----------|--------------|-------|
| H&S false positive | 27-46% | "Not available" | ChatGPT is right - varies too much |
| Optimal weights | 40% price, 25% volume | "No universal answer" | ChatGPT is right |
| Time cycle lead | Specific predictions | "Use as context" | ChatGPT is more cautious |

**Pattern:** Grok gives specific numbers that sound authoritative but may be hallucinated. ChatGPT acknowledges uncertainty.

---

## Data Source Verification Needed

Before implementing Open Interest features, must verify:

```python
# TEST: Does yfinance actually return options OI?
import yfinance as yf
ticker = yf.Ticker("AAPL")
options = ticker.option_chain()  # Does this return OI?
# Check: options.calls['openInterest'], options.puts['openInterest']
```

**Action:** Run this test before adding OI to roadmap.

---

## Final Recommendations

### IMPLEMENT (Verified Value)

1. **OBV Indicator** - Add to technical analysis, all sources agree it's useful
2. **Sector RS Tab** - Simple: (Sector ETF / SPY) ratio with trend
3. **Earnings Calendar Warning** - Flag stocks with earnings within 7 days
4. **Enhanced Volume Display** - Show RVOL ratio on existing analysis

### RESEARCH FURTHER (Potential Value)

1. **Divergence Detection** - RSI/MACD divergence, but compute own FPR first
2. **Options OI** - ONLY if yfinance data verified

### DEFER (Unverified or Low Value)

1. **Seasonal Patterns** - "Small edge", high complexity
2. **Head & Shoulders Detection** - Academic research inconclusive
3. **Full RRG Implementation** - RS ranking is sufficient
4. **Specific Optimal Weights** - No universal answer exists

---

## Honest Assessment

**What we learned:**
- Volume indicators (OBV, RVOL) are verified useful
- Sector RS ranking is proven and simple
- Reversal detection is messier than sources suggest
- Options OI data availability is uncertain

**What we can't trust:**
- Specific accuracy percentages
- Specific false positive rates
- Optimal weighting claims
- "Lead time" predictions

**Key principle:** Implement what's VERIFIED, defer what's UNCERTAIN.

---

*Analysis complete. Recommendations extracted with skepticism.*
