# 📊 API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts  
> **Location:** Claude Project + Git `/docs/claude/versioned/`  
> **Version:** Day 24 (January 6, 2026)  
> **Total API Routes:** 14 (verify with `grep -n "@app.route" backend.py`)

---

## 🎯 PROJECT OVERVIEW

**Swing Trade Analyzer** - Institutional-grade stock analysis system  
**Methodology:** Mark Minervini's SEPA + William O'Neil's CAN SLIM  
**Target:** 10-20% profits over 1-2 months, 60-70% win rate (UNPROVEN)

### Data Sources
| Data Type | Source | Update Frequency |
|-----------|--------|------------------|
| Prices & Technicals | yfinance | 15-30 min delay |
| Fundamentals | Defeat Beta | Weekly |
| Batch Scanning | TradingView Screener | Real-time |

---

## 📂 PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # Flask API server
│   ├── support_resistance.py       # S&R calculation + Option D viability
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
│   │   ├── App.jsx                 # Main React component (v2.6 - Day 23)
│   │   ├── services/api.js         # API client
│   │   └── utils/
│   │       ├── scoringEngine.js    # 75-point scoring (v2.2 - RSI working)
│   │       ├── rsCalculator.js     # Relative Strength
│   │       └── technicalIndicators.js  # SMA, EMA, ATR, RSI
│   └── package.json
│
├── docs/
│   └── claude/                     # Claude session documentation (Day 24)
│       ├── stable/                 # Non-versioned docs (SESSION_START, GOLDEN_RULES)
│       ├── versioned/              # Day-versioned docs (API_CONTRACTS, KNOWN_ISSUES)
│       │   └── archive/            # Older than 15 days
│       └── status/                 # Daily status files (PROJECT_STATUS)
│           └── archive/            # Older than 15 days
│
├── test_script.sh                  # Batch test scripts
└── README.md
```

---

## 📌 BACKEND API ENDPOINTS

### Health & Basic
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check |
| `/api/stock/<ticker>` | GET | Stock data + prices |
| `/api/fundamentals/<ticker>` | GET | Rich fundamentals from Defeat Beta |

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation |
| `/api/market/vix` | GET | VIX for risk assessment |

### Support & Resistance
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + viability |

**S&R Response Structure (Day 22 - with Option D):**
```json
{
  "ticker": "AAPL",
  "currentPrice": 263.73,
  "method": "pivot|kmeans|volume_profile",
  "support": [251.31, 232.16, 211.95],
  "resistance": [273.06],
  "allSupport": [211.95, 232.16, 251.31],
  "allResistance": [273.06],
  "suggestedEntry": 251.31,
  "suggestedStop": 243.77,
  "suggestedTarget": 273.06,
  "riskReward": 2.88,
  "dataPoints": 260,
  "timestamp": "2026-01-06T10:00:55.316712",
  "meta": {
    "methodUsed": "kmeans",
    "supportCount": 3,
    "resistanceCount": 1,
    "allSupportCount": 4,
    "allResistanceCount": 1,
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
      "viable": "YES|CAUTION|NO|UNKNOWN",
      "support_distance_pct": 5.3,
      "resistance_distance_pct": 2.9,
      "risk_reward_context": 0.55,
      "advice": "Good setup - tight stop placement possible",
      "stop_suggestion": 246.28,
      "position_size_advice": "FULL - low risk entry"
    }
  }
}
```

### Trade Viability Values (Option D - Day 22)
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

**Query Params:** `?strategy=reddit|minervini|momentum|value&limit=50`

**Strategies Response:**
```json
{
  "strategies": [
    {"id": "reddit", "name": "Reddit Style", "description": "Mid-cap+, high relative volume, momentum stocks"},
    {"id": "minervini", "name": "Minervini SEPA", "description": "Large-cap momentum leaders in Stage 2 uptrend"},
    {"id": "momentum", "name": "Momentum", "description": "Sustainable gains, RSI 50-75 (not overbought)"},
    {"id": "value", "name": "Value", "description": "Quality stocks above 200 SMA at fair RSI levels"}
  ]
}
```

### Validation
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/validation/run` | POST | Run validation for tickers |
| `/api/validation/results` | GET | Get latest validation results |
| `/api/validation/history` | GET | Get list of all validation runs |

**Run Validation - Request:**
```json
POST /api/validation/run
{"tickers": ["AAPL", "NVDA"]}
```

**Get Results - Query Params:** `?run_id=<optional>`

**Get History - Query Params:** `?limit=10`

### Forward Testing
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/forward-test/record` | POST | Record a trading signal |
| `/api/forward-test/signals` | GET | Get recent signals |
| `/api/forward-test/performance` | GET | Get performance summary |

**Record Signal - Request:**
```json
POST /api/forward-test/record
{
  "ticker": "AAPL",
  "signal_type": "BUY",
  "score": 65,
  "price_at_signal": 250.00,
  "entry_price": 245.00,
  "stop_price": 238.00,
  "target_price": 270.00,
  "risk_reward": 3.57,
  "verdict_reason": "Strong score with good RS"
}
```

**Get Signals - Query Params:** `?days=30&limit=50&ticker=<optional>`

**Get Performance - Response:**
```json
{
  "total_signals": 50,
  "win_rate": 0.65,
  "avg_pnl": 12.5,
  "best_trade": {...},
  "worst_trade": {...}
}
```

---

## 📊 FRONTEND: scoringEngine.calculateScore()

### Input
```javascript
calculateScore(stockData, spyData, vixData)
```

### Output (v2.2 - Day 22)
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
  pctFromHigh: number,        // Negative percentage (e.g., -11.5)
  
  // Scores (FLAT - for UI consumption)
  totalScore: number,         // 0-75
  maxScore: 75,
  scores: {
    technical: number,        // 0-40
    fundamental: number,      // 0-20
    sentiment: number,        // 0-10 (⚠️ placeholder)
    risk: number              // 0-5
  },
  
  // Verdict
  verdict: {
    verdict: string,          // "BUY" | "HOLD" | "AVOID"
    reason: string,
    color: string             // "green" | "yellow" | "red"
  },
  qualityGates: {
    passed: boolean,
    gates: [],
    criticalFails: number
  },
  
  // RS Data (normalized field names for UI)
  rsData: {
    rsRatio: number,          // Same as rs52Week (e.g., 1.17)
    rs52Week: number,
    rs13Week: number,
    rsRating: number,         // 0-99 percentile
    rsTrend: string,          // 'improving' | 'declining' | 'stable'
    stock52wReturn: number,   // Percentage (e.g., 37.1)
    spy52wReturn: number,     // Percentage (e.g., 16.9)
    interpretation: string,
    passesQualityGate: boolean
  },
  
  // Technical indicators (Day 22: RSI now working)
  indicators: {
    sma50: number,
    sma200: number,
    ema8: number,
    ema21: number,
    atr: number,              // ⚠️ May be null in frontend
    rsi: number,              // ✅ Now working (Day 22)
    avgVolume50: number
  },
  
  // Detailed breakdown (for UI expandable cards - Day 23)
  breakdown: {
    technical: { score, details },
    fundamental: { score, details },
    sentiment: { score, details },
    risk: { score, details }
  },
  
  timestamp: string
}
```

### Breakdown Details Structure (Day 23 - for expandable UI)

**Technical Breakdown:**
```javascript
breakdown.technical.details = {
  trendStructure: { score: 0-15, max: 15 },
  shortTermTrend: { score: 0-10, max: 10 },
  volume: { score: 0-5, max: 5 },
  relativeStrength: { score: 0-10, max: 10 }
}
```

**Fundamental Breakdown:**
```javascript
breakdown.fundamental.details = {
  epsGrowth: { score: 0-6, max: 6, value: number|null },
  revenueGrowth: { score: 0-5, max: 5, value: number|null },
  roe: { score: 0-4, max: 4, value: number|null },
  debtToEquity: { score: 0-3, max: 3, value: number|null },
  forwardPe: { score: 0-2, max: 2, value: number|null }
}
breakdown.fundamental.dataSource = 'defeatbeta' | 'yfinance'
breakdown.fundamental.dataQuality = 'rich' | 'basic'
```

---

## 📊 SCORING METHODOLOGY (75 Points)

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

### Sentiment: 10 points (⚠️ PLACEHOLDER)
Currently gives default 5 points to all stocks - needs real implementation.

**Options under consideration (Day 23 review):**
1. Remove sentiment (reduce to 65-point system)
2. Implement Fear & Greed Index (`https://api.alternative.me/fng/`)
3. Add earnings proximity check

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

## 📊 FRONTEND: rsCalculator

### Input
```javascript
calculateRelativeStrength(stockPrices, spyPrices)
```

### Output
```javascript
{
  rs52Week: number,           // Stock return / SPY return (e.g., 1.17)
  rs13Week: number,
  rsRating: number,           // 0-99 percentile ranking
  rsTrend: string,            // 'improving' | 'declining' | 'stable'
  stock52wReturn: number,     // Raw percentage
  spy52wReturn: number,       // Raw percentage
  interpretation: string,     // Human readable
  passesQualityGate: boolean  // RS >= 1.0
}
```

---

## 🚀 QUICK COMMANDS

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
curl http://localhost:5001/api/stock/AAPL
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/fundamentals/AAPL

# Test trade viability (Day 22)
curl -s http://localhost:5001/api/sr/AAPL | python3 -m json.tool | grep -A 10 "tradeViability"

# Test validation
curl -X POST http://localhost:5001/api/validation/run \
  -H "Content-Type: application/json" \
  -d '{"tickers": ["AAPL","NVDA"]}'
```

---

## 📋 CHANGE LOG

| Day | Changes |
|-----|---------|
| Day 24 | Reorganized docs to /docs/claude/, versioned format, added breakdown details structure |
| Day 23 | Added expandable Score Breakdown UI, breakdown.details documented |
| Day 22 | Added tradeViability to S&R response, RSI working in frontend |
| Day 21 | Fixed TradingView scanning (OTC bug) |
| Day 20 | Added ATR to S&R response |

---

*This file is versioned by day. Current version: DAY24*
*Previous version: API_CONTRACTS.md (Day 22)*
