# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 49 (February 9, 2026)
> **Total API Routes:** 20 (verify with `grep -n "@app.route" backend.py`)

---

## PROJECT OVERVIEW

**Swing Trade Analyzer** - Institutional-grade stock analysis system
**Methodology:** Mark Minervini's SEPA + William O'Neil's CAN SLIM
**Target:** 10-20% profits over 1-2 months, ~50% win rate (backtested)

### Data Sources
| Data Type | Source | Update Frequency | Fallback |
|-----------|--------|------------------|----------|
| Prices & Technicals | yfinance | 15-30 min delay | - |
| Fundamentals | Defeat Beta | Weekly (cached 1hr) | yfinance |
| Batch Scanning | TradingView Screener | Real-time | - |
| Sentiment | CNN Fear & Greed | Daily | Default 50 |
| Earnings | yfinance calendar | Daily | Multiple fallbacks |

---

## PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # Flask API server (v2.16)
│   ├── support_resistance.py       # S&R: Agglomerative + MTF confluence
│   ├── pattern_detection.py        # VCP, Cup & Handle, Flat Base detection
│   ├── test_indicator_coherence.py # 30-stock coherence test (Day 49)
│   ├── validation/
│   │   └── engine.py, scrapers.py, etc.
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main React component (v4.3)
│   │   ├── services/api.js         # API client (v2.7)
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System
│   │       ├── scoringEngine.js    # Legacy scoring (deprecated)
│   │       ├── forwardTesting.js   # Paper trading (v4.7)
│   │       └── technicalIndicators.js
│   └── package.json
│
├── docs/
│   ├── claude/                     # Claude session documentation
│   │   ├── CLAUDE_CONTEXT.md       # Single reference point
│   │   ├── stable/                 # Non-versioned docs
│   │   ├── versioned/              # Day-versioned docs
│   │   └── status/                 # Daily status files
│   └── research/                   # Research documents
│
└── README.md
```

---

## BACKEND API ENDPOINTS (20 Routes)

### Health & Diagnostics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check + service status |
| `/api/cache/status` | GET | Cache stats and ticker list |
| `/api/cache/clear` | POST | Clear cache (all or specific ticker) |
| `/api/provenance/<ticker>` | GET | Data source tracing (Day 38) |

**Health Check Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-09T10:00:00",
  "version": "2.16",
  "defeatbeta_available": true,
  "tradingview_available": true,
  "sr_engine_available": true,
  "pattern_detection_available": true,
  "cache_size": 15,
  "cache_ttl_seconds": 3600
}
```

### Stock & Fundamentals
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stock/<ticker>` | GET | Stock data + prices |
| `/api/fundamentals/<ticker>` | GET | Fundamentals (Defeat Beta → yfinance fallback) |

**Fundamentals Response:**
```json
{
  "source": "defeatbeta",
  "dataSource": "defeatbeta_api",
  "dataQuality": "full",
  "fallbackUsed": false,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 12.5,
  "revenueGrowth": 6.43,
  "debtToEquity": 1.34,
  "profitMargin": 24.3,
  "isETF": false
}
```

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation |
| `/api/market/vix` | GET | VIX for risk assessment |

### Fear & Greed Index (Day 44 - v4.5)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fear-greed` | GET | CNN Fear & Greed Index for sentiment |

**Fear & Greed Response:**
```json
{
  "value": 52.5,
  "rating": "Neutral",
  "assessment": "Neutral",
  "timestamp": "2026-02-09T10:00:00Z",
  "previousClose": 51.2,
  "source": "CNN Fear & Greed Index"
}
```

**Assessment Logic:**
| Value Range | Assessment | Meaning |
|-------------|------------|---------|
| 55-75 | Strong | Greed but not extreme - good for momentum |
| 35-60 | Neutral | Balanced sentiment (expanded Day 45) |
| 0-35 or 75-100 | Weak | Extreme fear/greed - increased risk |

### Earnings Calendar (Day 49 - v4.10)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/earnings/<ticker>` | GET | Earnings calendar + warning |

**Query Params:** `?days=7` (warning window, default 7)

**Earnings Response:**
```json
{
  "ticker": "AAPL",
  "has_upcoming": true,
  "earnings_date": "2026-02-12",
  "days_until": 3,
  "warning": "⚠️ Earnings in 3 days",
  "recommendation": "CAUTION - Consider reduced position size",
  "source": "earnings_dates"
}
```

**Warning Logic:**
| Days Until | Warning | Action |
|------------|---------|--------|
| 0 | EARNINGS TODAY | HIGH RISK - Gap risk maximum |
| 1-3 | Earnings in X days | CAUTION - Reduce position |
| 4-7 | Earnings in X days | AWARE - Monitor closely |
| >7 | None | Normal trading |

### Support & Resistance (Day 31-49)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + OBV |

**S&R Response (v2.16 - with OBV):**
```json
{
  "ticker": "AAPL",
  "currentPrice": 263.73,
  "method": "agglomerative",
  "support": [251.31, 232.16, 211.95],
  "resistance": [273.06],
  "suggestedEntry": 251.31,
  "suggestedStop": 243.77,
  "suggestedTarget": 273.06,
  "riskReward": 2.88,
  "meta": {
    "methodUsed": "agglomerative",
    "atr": 3.89,
    "tradeViability": {
      "viable": "YES",
      "support_distance_pct": 5.3,
      "position_size_advice": "FULL - low risk entry"
    },
    "mtf": {
      "enabled": true,
      "confluence_pct": 27.3
    },
    "technicals": {
      "rsi14": 55.2,
      "adx14": 28.5,
      "rvol": 1.45
    },
    "obv": {
      "current": 1234567890,
      "sma20": 1200000000,
      "trend": "rising",
      "divergence": "none"
    }
  }
}
```

**OBV Fields (Day 49):**
| Field | Values | Meaning |
|-------|--------|---------|
| trend | rising/falling/flat | OBV direction vs 20 SMA |
| divergence | bullish/bearish/none | Price vs OBV divergence |

### Pattern Detection (Day 44 - v4.2)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/patterns/<ticker>` | GET | Chart patterns + Trend Template |

**Pattern Response:**
```json
{
  "ticker": "AAPL",
  "patterns": {
    "vcp": {
      "detected": true,
      "confidence": 85,
      "status": "at_pivot",
      "contractions_count": 3,
      "base_tightness_pct": 12.5,
      "pivot_price": 265.00,
      "breakout": {
        "quality": "High",
        "volume_confirmed": true,
        "volume_ratio": 1.8,
        "tradeable": true
      }
    },
    "cup_handle": {
      "detected": false,
      "confidence": 0
    },
    "flat_base": {
      "detected": false,
      "confidence": 0
    }
  },
  "trend_template": {
    "criteria_met": 7,
    "total_criteria": 8,
    "criteria": {
      "price_above_150sma": true,
      "price_above_200sma": true,
      "sma150_above_200sma": true,
      "sma200_rising": true,
      "near_52w_high": true,
      "above_52w_low": true,
      "rs_above_70": false,
      "above_all_short_ma": true
    },
    "interpretation": "Near Stage 2 Uptrend (7/8 criteria)"
  },
  "summary": {
    "patterns_detected": ["VCP"],
    "best_pattern": "VCP",
    "best_confidence": 85,
    "actionable": true
  }
}
```

**Actionability Threshold:** ≥80% confidence (Day 47)

### TradingView Scanning
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | GET | Batch scanning |
| `/api/scan/strategies` | GET | Available strategies |

**Query Params:** `?strategy=reddit|minervini|momentum|value|best&limit=50`

### Validation & Forward Testing
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/validation/run` | POST | Run validation for tickers |
| `/api/validation/results` | GET | Latest validation results |
| `/api/validation/history` | GET | List of validation runs |
| `/api/forward-test/record` | POST | Record a trading signal |
| `/api/forward-test/signals` | GET | Get recent signals |
| `/api/forward-test/performance` | GET | Performance summary |

---

## FRONTEND: Categorical Assessment System (v4.5)

### Replaced 75-Point Scoring (Day 44)
**Reason:** Score-to-return correlation = 0.011 (essentially ZERO)

### Input
```javascript
runCategoricalAssessment(stockData, spyData, vixData, fundamentals, fearGreedData)
```

### Output
```javascript
{
  // Basic info
  ticker: string,
  name: string,

  // Categorical Assessments
  assessments: {
    technical: 'Strong' | 'Decent' | 'Weak',
    fundamental: 'Strong' | 'Decent' | 'Weak',
    sentiment: 'Strong' | 'Neutral' | 'Weak',
    riskMacro: 'Favorable' | 'Neutral' | 'Unfavorable'
  },

  // Verdict
  verdict: {
    verdict: 'BUY' | 'HOLD' | 'AVOID',
    reason: string,
    color: 'green' | 'yellow' | 'red',
    entryPreference: string  // "Momentum viable" | "Pullback preferred" | "Wait for trend"
  },

  // Details
  technicalDetails: {...},
  fundamentalDetails: {...},
  sentimentDetails: {...},
  riskDetails: {...},

  timestamp: string
}
```

### Assessment Criteria

**Technical Assessment:**
| Category | Criteria |
|----------|----------|
| Strong | Trend Template 7-8/8, RSI 50-70, RS ≥ 1.2 |
| Decent | Trend Template 5-6/8, RSI 40-80, RS ≥ 1.0 |
| Weak | Trend Template < 5/8, RSI extreme, RS < 1.0 |

**Fundamental Assessment:**
| Category | Criteria |
|----------|----------|
| Strong | ROE > 15%, Revenue Growth > 10%, Debt/Equity < 1.0 |
| Decent | ROE 8-15%, Revenue Growth 0-10%, Debt/Equity 1.0-2.0 |
| Weak | ROE < 8%, Negative growth, High debt |

**Sentiment Assessment (Fear & Greed):**
| Category | F&G Value |
|----------|-----------|
| Strong | 55-75 (Greed, not extreme) |
| Neutral | 35-60 (Balanced) |
| Weak | <35 (Fear) or >75 (Extreme greed) |

**Risk/Macro Assessment:**
| Category | Criteria |
|----------|----------|
| Favorable | VIX < 20, SPY > 200 EMA |
| Neutral | VIX 20-30, or SPY near 200 EMA |
| Unfavorable | VIX > 30 OR SPY < 200 EMA |

### Verdict Logic (Day 45)
```
BUY:   2+ Strong categories + Favorable/Neutral Risk
HOLD:  1 Strong category OR Unfavorable Risk override
AVOID: Technical Weak OR (Fundamental Weak + Sentiment Weak)
```

### Entry Preference (ADX-based, Day 47)
| ADX Value | Entry Preference |
|-----------|------------------|
| ≥ 25 | "Momentum entry viable" - Strong trend |
| 20-25 | "Pullback preferred" - Moderate trend |
| < 20 | "Wait for trend" - No trend/choppy |

---

## QUICK COMMANDS

```bash
# Start/Stop services
./start.sh               # Start both backend and frontend
./stop.sh                # Stop both services

# Test endpoints
curl http://localhost:5001/api/health
curl http://localhost:5001/api/stock/AAPL
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/patterns/AAPL
curl http://localhost:5001/api/fear-greed
curl http://localhost:5001/api/earnings/AAPL

# Run coherence test (Day 49)
python test_indicator_coherence.py
```

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| 49 | Added `/api/earnings/<ticker>`, OBV in S&R response, RVOL enhanced |
| 44 | Added `/api/patterns/<ticker>`, `/api/fear-greed`, Categorical Assessment system |
| 38 | Added `/api/provenance/<ticker>` for data source transparency |
| 33 | MTF confluence in S&R, Defeat Beta health check |
| 31 | Agglomerative clustering, yfinance failsafe |

---

*This file is versioned by day. Current version: DAY49*
*Previous version: API_CONTRACTS_DAY33.md*
