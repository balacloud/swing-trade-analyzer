# TradingView Integration Research & Roadmap

> **Purpose:** Long-term reference for TradingView integration
> **Date:** January 18, 2026 (Day 32)
> **Status:** Research Complete - Phased Implementation Planned

---

## Executive Summary

TradingView offers powerful charting widgets that can complement our analysis. The free widget provides professional indicators (RSI, MACD, 80+) but cannot display custom S&R levels. The paid Charting Library enables full programmatic control.

**Strategy:** Start with free widget as supplementary view, upgrade to paid library when budget allows.

---

## Free Widget Capabilities

### What's Included (FREE)
| Feature | Details |
|---------|---------|
| Real-time chart | Candlestick, line, area, Heikin Ashi, etc. |
| 80+ indicators | RSI, MACD, Bollinger, Stochastic, etc. |
| Drawing tools | For users to draw on chart manually |
| Symbol switching | User can change ticker |
| Multiple timeframes | 1m to Monthly |
| Comparison mode | Overlay multiple symbols |
| Volume display | Built-in volume bars |
| Themes | Light/Dark mode |

### What's NOT Included (FREE)
| Feature | Limitation |
|---------|------------|
| Custom S&R lines | Cannot programmatically draw lines |
| Custom indicators | No Pine Script execution |
| Remove branding | TradingView logo always shown |
| API callbacks | Limited event handling |
| Data export | Cannot extract data |

---

## Paid Charting Library

### Licensing
- Contact TradingView for pricing (typically $$$$/month)
- Requires commercial agreement
- Unlocks full API access

### What's Unlocked (PAID)
| Feature | Details |
|---------|---------|
| `createShape()` API | Draw horizontal lines at our S&R levels |
| `createStudy()` API | Add custom indicator overlays |
| Remove branding | White-label solution |
| Full event system | onTick, onSymbolChange, etc. |
| Save/Load charts | User preferences persist |
| Custom data feed | Use our backend as data source |

---

## Implementation Phases

### Phase 1: Free Widget (Day 33-34)
**Effort:** 3-4 hours

**Goal:** Add TradingView as supplementary chart below our S&R chart

**Features:**
- Collapsible TradingView section
- Pre-configured with RSI (14) + MACD
- Symbol syncs with our ticker input
- Dark theme to match our UI

**UI Location:**
```
┌─────────────────────────────────────┐
│  Stock Analysis: AAPL               │
├─────────────────────────────────────┤
│  [Our Chart with S&R Levels]        │  <- Primary (our value-add)
│  Support: 220, 215, 210             │
│  Resistance: 235, 240, 250          │
├─────────────────────────────────────┤
│  ▼ TradingView Indicators           │  <- Collapsible
│  ┌─────────────────────────────────┐│
│  │ [TradingView Widget]            ││
│  │ RSI, MACD, Volume               ││
│  └─────────────────────────────────┘│
│  ⚠️ S&R levels shown above only     │
└─────────────────────────────────────┘
```

**Code Structure:**
```jsx
// components/TradingViewWidget.jsx
import { useEffect, useRef } from 'react';

const TradingViewWidget = ({ symbol, collapsed, onToggle }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (collapsed) return;

    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.async = true;
    script.innerHTML = JSON.stringify({
      symbol: symbol,
      width: '100%',
      height: 400,
      interval: 'D',
      timezone: 'America/New_York',
      theme: 'dark',
      style: '1',
      locale: 'en',
      hide_top_toolbar: false,
      hide_legend: false,
      studies: [
        'RSI@tv-basicstudies',
        'MACD@tv-basicstudies'
      ],
      backgroundColor: 'rgba(17, 24, 39, 1)',
      gridColor: 'rgba(55, 65, 81, 0.5)'
    });

    containerRef.current?.appendChild(script);

    return () => {
      containerRef.current?.innerHTML = '';
    };
  }, [symbol, collapsed]);

  return (
    <div className="mt-4">
      <button
        onClick={onToggle}
        className="flex items-center gap-2 text-gray-400 hover:text-white"
      >
        {collapsed ? '▶' : '▼'} TradingView Indicators
      </button>
      {!collapsed && (
        <div className="mt-2 border border-gray-700 rounded-lg overflow-hidden">
          <div ref={containerRef} />
          <div className="bg-yellow-900/30 text-yellow-300 text-xs p-2 text-center">
            Note: Our S&R levels are shown in the chart above. This widget shows additional indicators.
          </div>
        </div>
      )}
    </div>
  );
};
```

### Phase 2: Settings Integration (Day 35+)
**Effort:** 1-2 hours

**Features:**
- Add to Settings tab: "Show TradingView Chart"
- Remember preference in localStorage
- Choose which indicators to display

### Phase 3: Paid Library (Future)
**Effort:** 8-16 hours (after licensing)

**Features:**
- Replace free widget with Charting Library
- Draw our S&R levels on TradingView chart
- Highlight confluent levels (thicker/different color)
- Single unified chart experience
- Custom indicator showing our composite score

---

## UI Design Considerations

### Current Layout Challenges
1. Adding second chart increases vertical scroll
2. Two charts showing same data may confuse users
3. Mobile experience would be degraded

### Proposed Solutions

**Option A: Tab-Based (Recommended for Phase 1)**
```
┌─────────────────────────────────────┐
│  [Our S&R Chart] | [TradingView]    │  <- Tab switcher
├─────────────────────────────────────┤
│  Currently showing: Our S&R Chart   │
│  [Chart Content]                    │
└─────────────────────────────────────┘
```

**Option B: Side-by-Side (Desktop Only)**
```
┌──────────────────┬──────────────────┐
│ [Our S&R Chart]  │ [TradingView]    │
│                  │                  │
└──────────────────┴──────────────────┘
```

**Option C: Collapsible (Current Plan)**
```
┌─────────────────────────────────────┐
│  [Our S&R Chart - Always Visible]   │
├─────────────────────────────────────┤
│  ▼ TradingView Indicators           │  <- Collapsed by default
└─────────────────────────────────────┘
```

### Future Full Integration (Paid Library)
```
┌─────────────────────────────────────┐
│  [Single TradingView Chart]         │
│  - Our S&R levels drawn via API     │
│  - Confluent levels highlighted     │
│  - RSI/MACD in subcharts            │
│  - Unified experience               │
└─────────────────────────────────────┘
```

---

## Indicator Selection Rationale

### Recommended Indicators for Phase 1

| Indicator | Why | Complements Our System |
|-----------|-----|------------------------|
| **RSI (14)** | Overbought/oversold detection | Our momentum score uses RSI but doesn't visualize it |
| **MACD** | Trend confirmation | Our trend score; visual crossover signals |

### Optional Additions (User Configurable)

| Indicator | Use Case |
|-----------|----------|
| 50 SMA | Already in our scoring; visual confirmation |
| 200 SMA | Long-term trend line |
| Volume Profile | High-volume price nodes (complements our volume_profile S&R) |
| Bollinger Bands | Volatility visualization |

### NOT Recommended
- Too many overlays create noise
- Avoid duplicating what our chart shows
- Keep it simple: 2-3 indicators max

---

## Sources

- [TradingView Advanced Chart Widget](https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/)
- [TradingView Widget Constructor](https://www.tradingview.com/charting-library-docs/latest/core_concepts/Widget-Constructor/)
- [TradingView Charting Library (Paid)](https://www.tradingview.com/charting-library-docs/)
- [All TradingView Widgets](https://www.tradingview.com/widget/)

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| Day 32 | Start with free widget | Validate value before paying |
| Day 32 | Use collapsible UI | Minimize disruption to existing flow |
| Day 32 | RSI + MACD default | Most complementary to our scoring |
| Future | Evaluate paid library | When S&R overlay becomes critical |

---

*Last Updated: Day 32 (January 18, 2026)*
