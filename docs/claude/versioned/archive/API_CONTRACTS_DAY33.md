# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 33 (January 19, 2026)
> **Total API Routes:** 17 (verify with `grep -n "@app.route" backend.py`)

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

---

## PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # Flask API server (v2.8)
│   ├── support_resistance.py       # S&R: Agglomerative + MTF confluence
│   ├── comprehensive_test.py       # 30-stock test script (Day 25)
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── engine.py               # Validation engine
│   │   ├── scrapers.py             # External data scrapers
│   │   ├── comparators.py
│   │   ├── forward_tracker.py
│   │   └── report_generator.py
│   ├── validation_results/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main React component (v3.4 - Day 33)
│   │   ├── services/api.js         # API client + health checks
│   │   └── utils/
│   │       ├── scoringEngine.js    # 75-point scoring + data quality
│   │       ├── rsCalculator.js     # Relative Strength
│   │       └── technicalIndicators.js  # SMA, EMA, ATR, RSI
│   └── package.json
│
├── docs/
│   ├── claude/                     # Claude session documentation
│   │   ├── CLAUDE_CONTEXT.md       # Single reference point
│   │   ├── stable/                 # Non-versioned docs
│   │   ├── versioned/              # Day-versioned docs
│   │   │   └── archive/            # Older than 15 days
│   │   └── status/                 # Daily status files
│   └── research/                   # Research documents
│       ├── SR_IMPROVEMENT_RESEARCH.md
│       ├── TRADINGVIEW_INTEGRATION.md
│       └── FINNHUB_INTEGRATION_GUIDE.md
│
└── README.md
```

---

## BACKEND API ENDPOINTS

### Health & Diagnostics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check (Day 33: +Defeat Beta status) |
| `/api/stock/<ticker>` | GET | Stock data + prices |
| `/api/fundamentals/<ticker>` | GET | Fundamentals with failsafe (Defeat Beta → yfinance) |

**Health Check Response (Day 33):**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-19T10:00:00",
  "version": "2.8",
  "defeatbeta_available": true,
  "tradingview_available": true,
  "sr_engine_available": true,
  "cache_size": 15,
  "cache_ttl_seconds": 3600,
  "defeatbeta_status": {
    "working": false,
    "error": "API connection error (TProtocolException)",
    "last_checked": "2026-01-19T10:00:00"
  }
}
```

**Query Params:** `?check_defeatbeta=true` (triggers live API check)

### Fundamentals (Day 31-33: With Failsafe)
**Response Structure:**
```json
{
  "source": "yfinance",
  "dataSource": "yfinance_fallback",
  "dataQuality": "partial",
  "fallbackUsed": true,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 12.5,
  "revenueGrowth": 6.43,
  "debtToEquity": 1.34,
  "profitMargin": 24.3,
  "isETF": false
}
```

**Data Quality Values:**
| Value | Meaning |
|-------|---------|
| `full` | Defeat Beta working, all fields available |
| `partial` | yfinance fallback, core fields available |
| `unavailable` | No data source working |

### Cache Management (Day 25)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cache/status` | GET | Check cache status and stats |
| `/api/cache/clear` | POST | Clear all cache or specific ticker |

**Cache Status Response:**
```json
{
  "cacheSize": 15,
  "ttlSeconds": 3600,
  "tickers": ["AAPL", "MSFT", "NVDA"],
  "oldestEntry": "2026-01-19T10:15:00",
  "newestEntry": "2026-01-19T11:00:00"
}
```

**Cache Clear - Query Params:** `?ticker=AAPL` (optional - clears all if not specified)

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation |
| `/api/market/vix` | GET | VIX for risk assessment |

### Support & Resistance (Day 31-33: Agglomerative + MTF)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + MTF confluence |

**S&R Response Structure (Day 33 - with MTF):**
```json
{
  "ticker": "AAPL",
  "currentPrice": 263.73,
  "method": "agglomerative",
  "support": [251.31, 232.16, 211.95],
  "resistance": [273.06],
  "allSupport": [211.95, 232.16, 251.31],
  "allResistance": [273.06],
  "suggestedEntry": 251.31,
  "suggestedStop": 243.77,
  "suggestedTarget": 273.06,
  "riskReward": 2.88,
  "dataPoints": 260,
  "timestamp": "2026-01-19T10:00:55.316712",
  "meta": {
    "methodUsed": "agglomerative",
    "supportCount": 3,
    "resistanceCount": 1,
    "atr": 3.89,
    "resistanceProjected": false,
    "supportProjected": false,
    "proximityFilter": {
      "supportFloor": 211.66,
      "resistanceCeiling": 343.94,
      "supportPct": 0.2,
      "resistancePct": 0.3
    },
    "tradeViability": {
      "viable": "YES",
      "support_distance_pct": 5.3,
      "resistance_distance_pct": 2.9,
      "risk_reward_context": 0.55,
      "advice": "Good setup - tight stop placement possible",
      "stop_suggestion": 246.28,
      "position_size_advice": "FULL - low risk entry"
    },
    "mtf": {
      "enabled": true,
      "confluence_pct": 27.3,
      "confluent_levels": 3,
      "total_levels": 11,
      "weekly_support": [250.50, 232.00],
      "weekly_resistance": [275.00, 290.00],
      "confluence_map": {
        "251.31": {"confluent": true, "weekly_match": 250.50, "strength": 1.0}
      }
    }
  }
}
```

**S&R Methods (Priority Order):**
1. `pivot` - ZigZag pivot detection (5% threshold)
2. `agglomerative` - Adaptive clustering (fallback if pivot insufficient)
3. `volume_profile` - Volume-weighted levels (final fallback)

### Trade Viability Values
| Viable | Support Distance | Position Size | Meaning |
|--------|------------------|---------------|---------|
| YES | ≤10% | FULL | Ideal Minervini setup |
| CAUTION | 10-20% | HALF | Wide stop, reduce size |
| NO | >20% | NONE | Extended, wait for pullback |
| UNKNOWN | N/A | REDUCED | No support found |

### TradingView Scanning
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | GET | Batch scanning (FIXED Day 21) |
| `/api/scan/strategies` | GET | Available strategies |

**Query Params:** `?strategy=reddit|minervini|momentum|value|best&limit=50`

### Validation
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/validation/run` | POST | Run validation for tickers |
| `/api/validation/results` | GET | Get latest validation results |
| `/api/validation/history` | GET | Get list of all validation runs |

### Forward Testing
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/forward-test/record` | POST | Record a trading signal |
| `/api/forward-test/signals` | GET | Get recent signals |
| `/api/forward-test/performance` | GET | Get performance summary |

---

## FRONTEND: scoringEngine.calculateScore()

### Input
```javascript
calculateScore(stockData, spyData, vixData)
```

### Output (v3.4 - Day 33)
```javascript
{
  // Basic info
  ticker: string,
  name: string,
  sector: string,
  industry: string,

  // Price data
  currentPrice: number,
  fiftyTwoWeekHigh: number,
  fiftyTwoWeekLow: number,
  pctFromHigh: number,

  // Scores
  totalScore: number,         // 0-75
  maxScore: 75,
  scores: {
    technical: number,        // 0-40
    fundamental: number,      // 0-20
    sentiment: number,        // 0-10 (placeholder)
    risk: number              // 0-5
  },

  // Verdict
  verdict: {
    verdict: string,          // "BUY" | "HOLD" | "AVOID"
    reason: string,
    color: string             // "green" | "yellow" | "red"
  },

  // RS Data
  rsData: {
    rsRatio: number,
    rs52Week: number,
    rs13Week: number,
    rsRating: number,
    rsTrend: string,
    stock52wReturn: number,
    spy52wReturn: number,
    interpretation: string,
    passesQualityGate: boolean
  },

  // Technical indicators
  indicators: {
    sma50: number,
    sma200: number,
    ema8: number,
    ema21: number,
    atr: number,
    rsi: number,
    avgVolume50: number
  },

  // Detailed breakdown
  breakdown: {
    technical: { score, details },
    fundamental: {
      score,
      details,
      isETF: boolean,
      etfNote: string,
      extremeValueContext: object,
      dataQuality: string,      // Day 31: "full" | "partial" | "unavailable"
      fallbackUsed: boolean     // Day 31: true if yfinance fallback
    },
    sentiment: { score, details },
    risk: { score, details }
  },

  timestamp: string
}
```

---

## SCORING METHODOLOGY (75 Points)

### Technical Analysis: 40 points
| Metric | Points | Criteria |
|--------|--------|----------|
| Trend Structure | 15 | Price > 50 SMA > 200 SMA |
| Short-term Trend | 10 | Price > 8 EMA > 21 EMA |
| Relative Strength | 10 | RS ≥1.5 = 10pts, ≥1.2 = 7pts, ≥1.0 = 4pts |
| Volume | 5 | ≥1.5x 50-day avg = 5pts |

### Fundamental Analysis: 20 points
| Metric | Points | Criteria |
|--------|--------|----------|
| EPS Growth | 6 | ≥25% = 6pts |
| Revenue Growth | 5 | ≥20% = 5pts |
| ROE | 4 | ≥15% = 4pts |
| Debt/Equity | 3 | <0.5 = 3pts |
| Forward P/E | 2 | <20 = 2pts |

### Sentiment: 10 points (PLACEHOLDER)
Currently gives default 5 points to all stocks - needs real implementation.

### Risk/Macro: 5 points
| Metric | Points | Criteria |
|--------|--------|----------|
| VIX Level | 2 | <15 = 2pts |
| S&P Regime | 2 | SPY > 200 SMA = 2pts |
| Market Breadth | 1 | Placeholder |

### Verdict Logic
```
BUY:   Score ≥60 + No critical fails + RS ≥1.0
HOLD:  Score 40-59 OR 1 critical fail
AVOID: Score <40 OR 2+ critical fails OR RS <0.8
```

---

## FEATURE FLAGS (Day 33)

| Flag | Location | Default | Purpose |
|------|----------|---------|---------|
| `use_agglomerative` | SRConfig | `True` | Enable/disable agglomerative clustering |
| `use_mtf` | SRConfig | `True` | Enable/disable multi-timeframe confluence |

To rollback S&R changes:
```python
cfg = SRConfig(use_agglomerative=False, use_mtf=False)
```

---

## QUICK COMMANDS

```bash
# Start backend
cd /Users/balajik/projects/swing-trade-analyzer/backend
source venv/bin/activate
python backend.py

# Start frontend
cd /Users/balajik/projects/swing-trade-analyzer/frontend
npm start

# Test endpoints
curl http://localhost:5001/api/health
curl "http://localhost:5001/api/health?check_defeatbeta=true"
curl http://localhost:5001/api/stock/AAPL
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/fundamentals/AAPL

# Cache management
curl http://localhost:5001/api/cache/status
curl -X POST http://localhost:5001/api/cache/clear
curl -X POST "http://localhost:5001/api/cache/clear?ticker=AAPL"

# Run 30-stock comprehensive test
python comprehensive_test.py
```

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| Day 33 | Health endpoint with Defeat Beta live check, MTF data in S&R response, data quality fields in fundamentals |
| Day 32 | MTF confluence implementation (backend only) |
| Day 31 | Agglomerative clustering, yfinance failsafe, data quality indicators |
| Day 29 | Session refresh endpoint, position controls (max position, manual override) |
| Day 28 | Position sizing calculator |
| Day 27 | Simplified binary scoring |
| Day 26 | Added "best" scanner strategy, scanner ticker filters |
| Day 25 | Added cache endpoints, ETF detection, extreme value context |

---

*This file is versioned by day. Current version: DAY33*
*Previous version: API_CONTRACTS_DAY26.md*
