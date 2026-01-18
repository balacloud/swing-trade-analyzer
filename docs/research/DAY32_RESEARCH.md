# Day 32 Research: Fundamentals Data Source + TradingView Widget

> **Purpose:** Research findings before implementation
> **Date:** January 18, 2026
> **Status:** Research Complete - Awaiting User Decision

---

## Issue 1: Fundamentals Always Using yfinance

### Current State

**Observation:** The user noticed fundamentals always appear to use yfinance fallback instead of Defeat Beta.

### Root Cause Analysis

**Tested:** Ran diagnostic on AAPL, MSFT, NVDA

```
Defeat Beta Available: True  <-- Library is installed
ERROR DuckDBClient - Query failed: TProtocolException: Invalid data
```

**Findings:**
1. Defeat Beta library IS installed and initialized
2. But the API calls are FAILING with "TProtocolException: Invalid data"
3. This is a **third-party API issue**, not our code
4. Our fallback logic is working CORRECTLY - it detects empty data and switches to yfinance

### Frontend Display Analysis

**Current Implementation (Day 31):**
- `dataQuality: 'rich'` = Defeat Beta working
- `dataQuality: 'yfinance_fallback'` or `fallbackUsed: true` = Fallback triggered
- `dataQuality: 'unavailable'` = Both sources failed

**Frontend shows:**
- Yellow banner when fallback
- Red banner when unavailable
- Footer shows: `Data: {source} - Quality: {quality}`

**Issue:** The banner says "Primary data source (Defeat Beta) unavailable" but doesn't make it clear this is an ongoing issue, not a temporary glitch.

### Recommendation

**Improvement A: Enhanced Visibility**
1. Add data source indicator to the analysis header (not just footer)
2. Show specific error type (API down vs. temporary)
3. Add "Check Defeat Beta status" link or diagnostic info

**Improvement B: Proactive Diagnosis**
1. Add backend health check endpoint `/api/health/defeatbeta`
2. Check on startup and periodically
3. Show "known issue" banner if Defeat Beta is down

**Effort Estimate:** ~1 hour

---

## Issue 2: TradingView Advanced Chart Widget

### Research Summary

**Widget Type:** Free embeddable iframe-based chart

**Official Sources:**
- [Advanced Chart Widget](https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/)
- [Widget Constructor Docs](https://www.tradingview.com/charting-library-docs/latest/core_concepts/Widget-Constructor/)
- [All TradingView Widgets](https://www.tradingview.com/widget/)

### Capabilities

| Feature | Free Widget | Charting Library (Paid) |
|---------|-------------|-------------------------|
| Embed chart | Yes | Yes |
| 80+ built-in indicators | Yes | Yes |
| Pre-configure RSI/MACD/etc | Yes | Yes |
| Drawing tools for users | Yes | Yes |
| **Custom S&R lines via API** | **NO** | **YES** |
| Custom indicator code | No | Yes (Pine Script) |
| Remove TradingView branding | No | Yes |
| Real-time data | Yes | Yes |
| Symbol switching | Yes | Yes |

### Critical Finding

**Cannot overlay our computed S&R levels on the free widget.**

The free widget is an iframe - we cannot programmatically add horizontal lines for our support/resistance levels. The Charting Library (paid/licensed) has APIs for this, but the free widget does not.

### What We CAN Do

**Option A: Complementary View (Recommended)**
- Add TradingView widget as a SECOND chart below our existing chart
- Our chart shows S&R levels (current behavior)
- TradingView shows professional indicators (RSI, MACD, Volume Profile)
- User gets best of both worlds

**Option B: Replace Our Chart**
- Use TradingView widget as primary chart
- Show our S&R levels in a separate panel (text/table)
- Lose visual overlay of S&R on price
- NOT RECOMMENDED

**Option C: Paid Integration**
- License TradingView Charting Library ($$$)
- Full programmatic control
- Can draw our S&R levels on their chart
- NOT RECOMMENDED for MVP

### Best Indicators to Add

Based on our scoring system and research:

| Indicator | Why | Complements |
|-----------|-----|-------------|
| RSI (14) | Overbought/oversold | Our momentum score |
| MACD | Trend confirmation | Our trend score |
| Volume | Volume verification | Our volume score |
| 50 SMA | Trend filter | Our price > 50 SMA check |
| 200 SMA | Long-term trend | Already in our system |

**NOTE:** Adding too many indicators creates noise. 2-3 max recommended.

### Implementation Approach (Option A)

```jsx
// Embed in App.jsx below our existing chart
<div className="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js">
  {
    "symbol": `NASDAQ:${ticker}`,
    "width": "100%",
    "height": 400,
    "interval": "D",
    "timezone": "America/New_York",
    "theme": "dark",
    "style": "1",
    "locale": "en",
    "studies": [
      "RSI@tv-basicstudies",
      "MACD@tv-basicstudies"
    ],
    "hide_top_toolbar": false,
    "hide_legend": false
  }
  </script>
</div>
```

**Effort Estimate:** ~2-3 hours

---

## Critical Analysis

### Fundamentals (Issue 1)

**Pro:** Our fallback is working correctly. yfinance provides adequate data.
**Con:** User has no visibility into WHY Defeat Beta keeps failing.
**Risk:** Low - system works, just missing transparency.
**Priority:** Medium - improves trust/transparency.

### TradingView Widget (Issue 2)

**Pro:** Professional chart with industry-standard indicators. Free.
**Con:** Cannot show our S&R levels on it. Adds iframe complexity.
**Risk:**
- Medium - could confuse users with two charts
- Low - doesn't break anything

**Priority:** Low-Medium - nice-to-have, not essential.

**Trade-off Question:**
> Does adding a second chart (TradingView) actually help users make better decisions, or does it add complexity without value?

Our S&R levels are the unique value proposition. A TradingView chart shows the same indicators anyone can see for free on tradingview.com. The question is whether embedding it saves users a context switch.

---

## Recommended Plan

### Phase 1: Fundamentals Transparency (1 hour)

1. **Update App.jsx header** to show data source icon:
   - Green checkmark if Defeat Beta working
   - Yellow warning if using yfinance fallback
   - Red X if data unavailable

2. **Add tooltip** explaining the issue:
   - "Primary data source (Defeat Beta API) is currently experiencing issues. Using backup data from yfinance."

3. **Backend diagnostic endpoint** `/api/health`:
   - Returns status of all external dependencies
   - Defeat Beta, yfinance, TradingView screener

### Phase 2: TradingView Widget (Optional - 2-3 hours)

**Decision Point:** Does user want this? It adds complexity.

If YES:
1. Add collapsible TradingView chart section below our chart
2. Pre-configure with RSI + MACD
3. Make it toggleable (Settings > Show TradingView Chart)
4. Clear label: "TradingView Chart (Indicators Only - S&R shown above)"

If NO:
1. Skip this entirely
2. Focus on core features (Fibonacci, validation)

---

## User Decision Required

**Question 1: Fundamentals**
> Do you want full Phase 1 (header icon + tooltip + health endpoint) or minimal (just better messaging)?

**Question 2: TradingView**
> Given that we CANNOT show our S&R levels on the TradingView chart, do you still want to add it as a supplementary view for RSI/MACD indicators? Or would you prefer we focus on other priorities?

---

## Sources

- [TradingView Advanced Chart Widget](https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/)
- [TradingView Widget Constructor](https://www.tradingview.com/charting-library-docs/latest/core_concepts/Widget-Constructor/)
- [TradingView Free Widgets](https://www.tradingview.com/widget/)
- Defeat Beta API error logs (tested January 18, 2026)
