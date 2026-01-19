# Finnhub Integration Guide
## Alternative Fundamentals Data Source

**Created:** January 19, 2026 (Day 33)
**Status:** Research/Reference - Not yet implemented
**Cost:** $0 (free tier: 60 API calls/min)

---

## WHY THIS EXISTS

Defeat Beta API is currently broken (TProtocolException) due to:
- Our library version: 0.0.6
- Latest version: 0.0.29 (requires Python 3.10+)
- We're on Python 3.9.6

**Decision (Day 33):** Keep yfinance as primary, document Finnhub as future alternative.

---

## QUICK START (30 MINUTES)

### Step 1: Register Finnhub API (2 min)
1. Go to: https://finnhub.io
2. Sign up (free account)
3. Verify email
4. Copy API key from dashboard

### Step 2: Install Library (1 min)
```bash
pip install finnhub-client
```

### Step 3: Basic Usage
```python
import finnhub

# Initialize client
finnhub_client = finnhub.Client(api_key="YOUR_API_KEY")

# Get basic financials
financials = finnhub_client.company_basic_financials('AAPL', 'all')

# Key metrics available:
# - 'epsGrowthQuarterlyYoy' -> EPS Growth
# - 'revenueGrowthQuarterlyYoy' -> Revenue Growth
# - 'roeTTM' -> ROE
# - 'totalDebt/totalEquityQuarterly' -> Debt/Equity
# - 'peNormalizedAnnual' -> P/E Ratio
```

---

## METRICS MAPPING

| Our Metric | Finnhub Field | Notes |
|------------|---------------|-------|
| EPS Growth | `epsGrowthQuarterlyYoy` | YoY quarterly |
| Revenue Growth | `revenueGrowthQuarterlyYoy` | YoY quarterly |
| ROE | `roeTTM` | Trailing 12 months |
| Debt/Equity | `totalDebt/totalEquityQuarterly` | Quarterly |
| Forward P/E | `peNormalizedAnnual` | Normalized annual |

---

## IMPLEMENTATION PLAN (WHEN READY)

### Option 1: Replace Defeat Beta
```python
# In backend.py
def get_fundamentals_finnhub(ticker_symbol):
    """Get fundamentals from Finnhub (free tier)"""
    try:
        financials = finnhub_client.company_basic_financials(ticker_symbol, 'all')
        metrics = financials.get('metric', {})

        return {
            'source': 'finnhub',
            'epsGrowth': metrics.get('epsGrowthQuarterlyYoy'),
            'revenueGrowth': metrics.get('revenueGrowthQuarterlyYoy'),
            'roe': metrics.get('roeTTM'),
            'debtToEquity': metrics.get('totalDebt/totalEquityQuarterly'),
            'forwardPe': metrics.get('peNormalizedAnnual'),
        }
    except Exception as e:
        print(f"Finnhub error: {e}")
        return None
```

### Option 2: Multi-Source Fallback Chain
```
Defeat Beta -> Finnhub -> yfinance -> unavailable
```

---

## RATE LIMITS

| Tier | Calls/Minute | Cost |
|------|--------------|------|
| Free | 60 | $0 |
| Starter | 300 | $29/mo |
| Professional | 750 | $99/mo |

For our use case (analyze ~50 stocks/day), free tier is sufficient.

---

## PROS vs YFINANCE

| Aspect | Finnhub | yfinance |
|--------|---------|----------|
| Reliability | More stable API | Occasional scraping issues |
| Data freshness | Near real-time | Slightly delayed |
| Rate limits | Clear (60/min) | Unclear/throttled |
| Documentation | Excellent | Community-driven |
| Auth required | Yes (API key) | No |

---

## FUTURE IMPLEMENTATION TRIGGER

Implement Finnhub when ANY of these occur:
1. yfinance starts failing frequently
2. We need real-time fundamental data
3. User requests higher data quality
4. We implement batch scanning with fundamentals

---

## RELATED DECISIONS

### Day 33 Decision: Python Upgrade Deferred
- **Issue:** Defeat Beta 0.0.29 requires Python 3.10+
- **Current:** Python 3.9.6
- **Decision:** Keep current setup, yfinance works fine
- **Future:** When we need to upgrade other dependencies, upgrade Python too

### Priority Order for Fundamentals:
1. ~~Defeat Beta~~ (broken, needs Python 3.10+)
2. **yfinance** (current - working)
3. **Finnhub** (future alternative)

---

*This file saved for future reference when we decide to implement alternative data sources.*
