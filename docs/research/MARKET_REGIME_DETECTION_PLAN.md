# Market Regime Detection - Feature Plan

> **Purpose:** Design document for adding market regime detection to adapt system for bull/neutral/bear markets
> **Created:** Day 40 (January 31, 2026)
> **Status:** PLANNING - Needs validation via Perplexity research first

---

## Problem Statement

Our current system treats all market conditions the same. A pullback entry in a bull market is very different from a pullback entry in a bear market. We need:

1. **Detection**: Know what regime we're in
2. **Adaptation**: Adjust strategy based on regime
3. **Protection**: Reduce exposure in risky regimes

---

## Proposed Detection Methods

### Method 1: Simple (SPY + SMA)
```python
def get_market_regime_simple(spy_price, spy_sma200):
    """Simple regime detection using SPY vs 200 SMA"""
    pct_from_sma = ((spy_price - spy_sma200) / spy_sma200) * 100

    if pct_from_sma > 5:
        return 'BULL'
    elif pct_from_sma < -5:
        return 'BEAR'
    else:
        return 'NEUTRAL'
```

**Pros**: Simple, fast, well-understood
**Cons**: Laggy, many false signals near SMA

### Method 2: Composite (SPY + VIX + Breadth)
```python
def get_market_regime_composite(spy_price, spy_sma200, vix, breadth_pct):
    """
    Composite score combining multiple factors

    Parameters:
    - spy_price: Current SPY price
    - spy_sma200: SPY 200-day SMA
    - vix: Current VIX level
    - breadth_pct: % of stocks above their 50-day SMA
    """
    score = 0

    # SPY vs SMA200 (weight: 40%)
    spy_pct = ((spy_price - spy_sma200) / spy_sma200) * 100
    if spy_pct > 5:
        score += 40
    elif spy_pct > 0:
        score += 20
    elif spy_pct > -5:
        score += 0
    else:
        score -= 40

    # VIX level (weight: 30%)
    if vix < 15:
        score += 30  # Very calm = bullish
    elif vix < 20:
        score += 15  # Normal
    elif vix < 25:
        score -= 15  # Elevated
    else:
        score -= 30  # High fear = bearish

    # Breadth (weight: 30%)
    if breadth_pct > 70:
        score += 30  # Most stocks participating
    elif breadth_pct > 50:
        score += 15
    elif breadth_pct > 30:
        score -= 15
    else:
        score -= 30  # Most stocks weak

    # Classify regime
    if score >= 40:
        return 'BULL', score
    elif score <= -40:
        return 'BEAR', score
    else:
        return 'NEUTRAL', score
```

**Pros**: More robust, multiple confirmation
**Cons**: More complex, needs breadth data source

### Method 3: Trend + Momentum (SMA Cross + ROC)
```python
def get_market_regime_trend(spy_sma50, spy_sma200, spy_roc_20):
    """
    Trend-based regime using SMA relationship and momentum

    Parameters:
    - spy_sma50: SPY 50-day SMA
    - spy_sma200: SPY 200-day SMA
    - spy_roc_20: 20-day rate of change
    """
    # Golden/Death cross
    sma_bullish = spy_sma50 > spy_sma200

    # Momentum confirmation
    momentum_bullish = spy_roc_20 > 0

    if sma_bullish and momentum_bullish:
        return 'BULL'
    elif not sma_bullish and not momentum_bullish:
        return 'BEAR'
    else:
        return 'NEUTRAL'
```

**Pros**: Trend-following logic, fewer whipsaws
**Cons**: Very laggy, misses regime changes

---

## Strategy Adjustments by Regime

| Regime | Position Size | Strategy Preference | Max Exposure | Long/Short |
|--------|---------------|---------------------|--------------|------------|
| **BULL** | Full | Pullback preferred | 100% | Long only |
| **NEUTRAL** | Half | Both strategies OK | 50% | Long only |
| **BEAR** | Quarter | Momentum only | 25% | Long + Short candidates |

### Detailed Rules

#### BULL Regime
- Allow full positions
- Prefer pullback entries (strong trends bounce)
- Target R:R of 2:1 minimum
- Use wider stops (2.5 × ATR)
- Scan for growth stocks

#### NEUTRAL Regime
- Reduce position sizes by 50%
- Use both strategies equally
- Tighter stops (2 × ATR)
- Focus on stocks with relative strength
- Higher quality setups only (R:R > 3:1)

#### BEAR Regime
- Minimum position sizes (25%)
- Only momentum entries with confirmation
- Tightest stops (1.5 × ATR)
- Consider short candidates
- Cash is a valid position
- Only trade strongest stocks (RS > 95)

---

## UI Design

### New Component: Market Regime Banner

```
┌────────────────────────────────────────────────────────┐
│  📈 MARKET REGIME: BULL                                │
│  SPY: $485.23 (+3.2% above 200 SMA)                   │
│  VIX: 14.5 (Low)  |  Breadth: 72% (Strong)            │
│  Position Size: FULL  |  Strategy: Pullback Preferred  │
└────────────────────────────────────────────────────────┘
```

### Tooltip Content
- **BULL**: "Market is in uptrend. Full positions allowed. Pullback entries preferred."
- **NEUTRAL**: "Market is ranging. Reduce position sizes by 50%. Be selective."
- **BEAR**: "Market is in downtrend. Minimum positions. Consider cash. Only strongest setups."

---

## Backend Implementation Plan

### New Endpoint: `/api/market/regime`

```python
@app.route('/api/market/regime', methods=['GET'])
def get_market_regime():
    """
    Returns current market regime assessment
    """
    # Fetch SPY data
    spy_data = fetch_spy_data()
    spy_price = spy_data['currentPrice']
    spy_sma200 = spy_data['sma200']
    spy_sma50 = calculate_sma(spy_data['prices'], 50)

    # Fetch VIX
    vix_data = fetch_vix_data()
    vix = vix_data['current']

    # Calculate breadth (% stocks above 50 SMA) - may need external source
    breadth = calculate_market_breadth()

    # Determine regime
    regime, score = get_market_regime_composite(
        spy_price, spy_sma200, vix, breadth
    )

    return jsonify({
        'regime': regime,
        'score': score,
        'spy': {
            'price': spy_price,
            'sma200': spy_sma200,
            'sma50': spy_sma50,
            'pct_from_sma200': ((spy_price - spy_sma200) / spy_sma200) * 100
        },
        'vix': {
            'current': vix,
            'classification': 'low' if vix < 20 else 'high'
        },
        'breadth': {
            'pct_above_50sma': breadth,
            'classification': 'strong' if breadth > 60 else 'weak'
        },
        'recommendations': {
            'position_size': 'full' if regime == 'BULL' else 'half' if regime == 'NEUTRAL' else 'quarter',
            'max_exposure_pct': 100 if regime == 'BULL' else 50 if regime == 'NEUTRAL' else 25,
            'strategy_preference': 'pullback' if regime == 'BULL' else 'both' if regime == 'NEUTRAL' else 'momentum'
        },
        'timestamp': datetime.now().isoformat()
    })
```

### Data Sources Needed

| Data | Current Source | Notes |
|------|----------------|-------|
| SPY Price | yfinance | Already have |
| SPY SMA200 | yfinance | Already calculating |
| SPY SMA50 | yfinance | Easy to add |
| VIX | yfinance | Already have |
| Market Breadth | TBD | Need to find source |

#### Breadth Data Options:
1. **Finviz**: Scrape % above 50 SMA
2. **TradingView Screener**: Query count of stocks above SMA
3. **Calculate locally**: Expensive (scan all stocks)
4. **Skip breadth**: Use simpler 2-factor model (SPY + VIX)

---

## Implementation Phases

### Phase 1: Simple Detection (Day 41-42)
- Implement SPY + VIX regime detection (no breadth)
- Add `/api/market/regime` endpoint
- Add regime banner to UI
- Adjust position size recommendations

### Phase 2: Strategy Integration (Day 43-44)
- Modify dual entry strategy to respect regime
- Show regime-adjusted R:R targets
- Add regime to trade setup reasoning

### Phase 3: Breadth Integration (Day 45+)
- Find breadth data source
- Add breadth to composite score
- Backtest regime detection accuracy

---

## Validation Checklist (Use Perplexity)

Before implementing, validate via Perplexity Prompt 2:
- [ ] Best regime detection method for swing trading
- [ ] Optimal thresholds for SPY % from SMA
- [ ] VIX level classifications (what's truly high/low?)
- [ ] How professionals adjust position sizing by regime
- [ ] Whether to include breadth or keep it simple

---

## Open Questions

1. **Should regime affect whether we trade at all?**
   - In BEAR regime, should we show "No trades recommended"?
   - Or just reduce size and be more selective?

2. **How often to recalculate regime?**
   - Once per day (market open)?
   - Real-time?

3. **Regime change handling**
   - What to do with open positions when regime changes?
   - Alert user? Auto-adjust stops?

4. **Backtesting regime**
   - How to validate regime detection historically?
   - What accuracy should we target?

---

*Next step: Use Perplexity Prompt 2 to validate approach before implementation*
