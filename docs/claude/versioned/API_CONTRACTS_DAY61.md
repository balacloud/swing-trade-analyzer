# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 61 (February 27, 2026)
> **Total API Routes:** 22 (verify with `grep -n "@app.route" backend.py`)

---

## PROJECT OVERVIEW

**Swing Trade Analyzer** - Institutional-grade stock analysis system
**Methodology:** Mark Minervini's SEPA + William O'Neil's CAN SLIM
**Target:** 10-20% profits over 1-2 months, ~50% win rate (backtested)

### Data Sources (v4.14 Multi-Source)
| Data Type | Primary | Fallback 1 | Fallback 2 | Cache |
|-----------|---------|------------|------------|-------|
| OHLCV (Daily) | TwelveData | yfinance | Stooq | SQLite (market-aware TTL) |
| Intraday (4H RSI) | TwelveData | yfinance | - | Not cached |
| Fundamentals | Finnhub | FMP | yfinance | SQLite (7-day TTL, schema v2) |
| VIX Quote | yfinance | Finnhub | stale cache | - |
| Stock Info (name/sector) | yfinance | - | - | - |
| Earnings | yfinance | - | - | - |
| Batch Scanning | TradingView Screener | - | - | - |
| Sentiment | CNN Fear & Greed | - | fallback w/ flag | - |
| Sector Rotation | yfinance (11 SPDR ETFs) | - | - | SQLite (trading day) |

### Provider API Keys (in `backend/.env`)
| Provider | Env Var | Rate Limit |
|----------|---------|------------|
| TwelveData | `TWELVEDATA_API_KEY` | 8/min, 800/day |
| Finnhub | `FINNHUB_API_KEY` | 60/min |
| FMP | `FMP_API_KEY` | 10/min, 250/day |
| yfinance | None (free) | 30/min (self-imposed) |
| Stooq | None (free) | 5/min (self-imposed) |

---

## PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # Flask API server (v2.24)
│   ├── support_resistance.py       # S&R: Agglomerative + MTF confluence
│   ├── pattern_detection.py        # VCP, Cup & Handle, Flat Base detection
│   ├── cache_manager.py            # SQLite cache (schema v2, Day 61)
│   ├── .env                        # API keys (gitignored)
│   ├── .env.example                # Template with registration URLs
│   ├── providers/                  # v4.14 Multi-Source Data Intelligence
│   │   ├── __init__.py             # Exports get_data_provider()
│   │   ├── orchestrator.py         # THE CORE: fallback chains, field merge
│   │   ├── base.py                 # Abstract interfaces + result dataclasses
│   │   ├── exceptions.py           # ProviderError hierarchy
│   │   ├── field_maps.py           # Field normalization + NaN safety (Day 61)
│   │   ├── rate_limiter.py         # Token-bucket per provider
│   │   ├── circuit_breaker.py      # CLOSED→OPEN→HALF_OPEN pattern
│   │   ├── twelvedata_provider.py  # Primary OHLCV + Intraday
│   │   ├── finnhub_provider.py     # Primary Fundamentals + Quote
│   │   ├── fmp_provider.py         # Growth metrics (epsGrowth, revenueGrowth)
│   │   ├── yfinance_provider.py    # Universal fallback (all 6 interfaces)
│   │   ├── stooq_provider.py       # Last-resort OHLCV
│   │   └── backtest_adapter.py     # Drop-in yf.download() replacement
│   ├── backtest/                   # v4.16-v4.17 Holistic Backtest
│   │   ├── backtest_holistic.py    # Main runner (5 configs, walk-forward)
│   │   ├── categorical_engine.py   # Python port of categorical assessment
│   │   ├── trade_simulator.py      # Exit strategies per holding period
│   │   ├── metrics.py              # Statistical metrics (Sharpe, PF, etc.)
│   │   └── simfin_loader.py        # Historical fundamentals (SimFin API)
│   ├── validation/
│   │   └── engine.py, scrapers.py, etc.
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main React component (v4.10)
│   │   ├── components/
│   │   │   ├── DecisionMatrix.jsx  # v4.15 Decision Matrix
│   │   │   └── BottomLineCard.jsx  # Bottom Line summary
│   │   ├── services/api.js         # API client (v2.8)
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System + NaN defense
│   │       ├── riskRewardCalc.js    # Shared R:R utility (Day 61)
│   │       ├── simplifiedScoring.js # 9-criteria binary checklist
│   │       ├── scoringEngine.js     # Legacy scoring + multi-source quality
│   │       ├── forwardTesting.js    # Paper trading (v4.7)
│   │       └── technicalIndicators.js
│   └── package.json
│
├── docs/
│   ├── claude/                     # Claude session documentation
│   └── research/                   # Research documents
│
└── README.md
```

---

## BACKEND API ENDPOINTS (22 Routes)

### Health & Diagnostics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check + provider status |
| `/api/cache/status` | GET | Cache stats and ticker list |
| `/api/cache/clear` | POST | Clear cache (all or specific ticker) |
| `/api/provenance/<ticker>` | GET | Data source tracing (Day 38) |
| `/api/data/freshness` | GET | Cache freshness per data source (Day 59) |

**Data Freshness Response (Day 59):**
```json
{
  "sources": [
    {
      "name": "Price Data",
      "key": "ohlcv",
      "status": "fresh",
      "ageMinutes": 45.2,
      "cachedAt": "2026-02-27T10:00:00",
      "expiresAt": "2026-02-27T14:00:00",
      "source": "twelvedata"
    },
    {
      "name": "Fundamentals",
      "key": "fundamentals",
      "status": "aging",
      "ageMinutes": 4320.0,
      "source": "finnhub"
    }
  ]
}
```
**Query Params:** `?ticker=AAPL` (optional — for ticker-specific OHLCV/fundamentals)
**Status Values:** `fresh` (green) | `aging` (yellow) | `stale` (red) | `live` (blue) | `unknown` (gray)

### Stock & Fundamentals
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stock/<ticker>` | GET | Stock metadata + prices (NO fundamentals) |
| `/api/fundamentals/<ticker>` | GET | Fundamentals (Finnhub → FMP → yfinance) — **SINGLE source of truth** |

**Stock Response (v2.24 — Day 61: NaN-safe):**
```json
{
  "ticker": "AAPL",
  "name": "Apple Inc",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "currentPrice": 185.50,
  "price52wAgo": 165.25,
  "price13wAgo": 180.10,
  "fiftyTwoWeekHigh": 199.62,
  "fiftyTwoWeekLow": 156.01,
  "avgVolume": 48000000,
  "avgVolume10d": 52000000,
  "priceHistory": [{"date": "2024-02-15", "open": 185.20, "high": 186.10, "low": 184.80, "close": 185.50, "volume": 48000000}],
  "dataPoints": 260,
  "oldestDate": "2024-02-15",
  "newestDate": "2026-02-27"
}
```
**Day 61 changes:** priceHistory NaN filtering (close-NaN rows skipped, OHLV fallback to close, volume fallback to 0). Scalar prices (currentPrice, price52wAgo, price13wAgo) NaN-safe with fallback to last non-NaN close.

**Fundamentals Response (v2.24 — Day 61: NaN→null, schema v2):**
```json
{
  "source": "finnhub",
  "dataSource": "finnhub",
  "dataQuality": "multi_source",
  "fallbackUsed": false,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 18.3,
  "revenueGrowth": 15.7,
  "debtToEquity": 1.34,
  "profitMargin": 24.3,
  "_field_sources": {
    "pe": "finnhub",
    "roe": "finnhub",
    "epsGrowth": "fmp",
    "revenueGrowth": "fmp",
    "debtToEquity": "finnhub",
    "profitMargin": "finnhub"
  },
  "isETF": false
}
```
**Day 60 changes:** Growth values now in percentage format (18.3, not 0.183) via `_growth_to_pct()` transform.
**Day 61 changes:** NaN values converted to null (not propagated as NaN). Cache schema versioning (v2) auto-invalidates pre-Day 60 cached entries.

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation + regime |
| `/api/market/vix` | GET | VIX for risk assessment |

**SPY Response (v2.24 — Day 57+):**
```json
{
  "ticker": "SPY",
  "currentPrice": 498.50,
  "price52wAgo": 445.25,
  "price13wAgo": 480.10,
  "sma200": 470.30,
  "aboveSma200": true,
  "sma50Declining": false,
  "priceHistory": [...],
  "dataPoints": 260
}
```
**Day 57 addition:** `sma50Declining` (bool) — early bear market indicator. True when SPY 50 SMA has declined > 1% over 20 trading days. Used by frontend to cap Risk/Macro at "Neutral".

### Fear & Greed Index (Day 44 - v4.5)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fear-greed` | GET | CNN Fear & Greed Index for sentiment |

**Response (Day 61 — thresholds synced):**
```json
{
  "value": 44.7,
  "rating": "Fear",
  "assessment": "Neutral",
  "timestamp": "2026-02-27T12:00:00",
  "previousClose": 42.3,
  "source": "CNN Fear & Greed Index"
}
```
**Day 61 changes:** Assessment thresholds synced with frontend: Strong 60-80, Neutral 35-60, Weak <35 or >80.

**Fallback Response (API error):**
```json
{
  "value": 50,
  "rating": "Neutral",
  "assessment": "Neutral",
  "source": "default (API error fallback)",
  "fallback": true,
  "error": "Connection timeout"
}
```
**Day 61 addition:** `fallback: true` flag preserved through api.js so frontend can display gray "unavailable" badge.

### Earnings Calendar (Day 49 - v4.10)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/earnings/<ticker>` | GET | Earnings calendar + warning |

**Success Response:**
```json
{
  "ticker": "AAPL",
  "has_upcoming": true,
  "earnings_date": "2026-03-05",
  "days_until": 6,
  "warning": "📅 Earnings in 6 days",
  "recommendation": "AWARE - Consider exiting before earnings if position is taken.",
  "source": "calendar"
}
```

**No Earnings Found (HTTP 200):**
```json
{
  "ticker": "AAPL",
  "has_upcoming": false,
  "earnings_date": null,
  "days_until": null,
  "warning": null,
  "recommendation": "No earnings date found",
  "source": null
}
```

**Error Response (HTTP 500 — Day 61 change):**
```json
{
  "ticker": "AAPL",
  "error": "Failed to fetch earnings: ...",
  "has_upcoming": null,
  "earnings_date": null,
  "days_until": null,
  "warning": null,
  "recommendation": null,
  "source": null
}
```
**Day 61 CHANGE:** Previously returned HTTP 200 with `has_upcoming: false` on error (indistinguishable from "no earnings"). Now returns HTTP 500 with `has_upcoming: null`. Frontend api.js catch block returns `hasUpcoming: null` (not `false`).

### Support & Resistance (Day 31-49)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + OBV |

### Pattern Detection (Day 44 - v4.2)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/patterns/<ticker>` | GET | Chart patterns + Trend Template |

### TradingView Scanning
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | GET | Batch scanning with index/market filters |
| `/api/scan/strategies` | GET | Available strategies |

**Scan Query Params (Day 57+):**
- `strategy` — scan strategy name (e.g., `minervini_momentum`)
- `market_index` — index filter: `sp500` / `nasdaq100` / `dow30` / `tsx60` / `all_canadian` / `all` (default)

**Day 57 addition:** `market_index` param uses TradingView `set_index()` for native S&P 500, NASDAQ 100, Dow 30 filtering.
**Day 59 addition:** `tsx60` and `all_canadian` market index options for Canadian market scanning.

### Sector Rotation (Day 58)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sectors/rotation` | GET | Sector RS ranking + RRG quadrants |

**Response:**
```json
{
  "sectors": [
    {
      "etf": "XLK",
      "name": "Technology",
      "rsRatio": 103.45,
      "rsMomentum": 1.23,
      "quadrant": "Leading",
      "weekChange": 2.1,
      "monthChange": 5.3
    }
  ],
  "mapping": {
    "Technology": "XLK",
    "Healthcare": "XLV",
    "Financials": "XLF"
  },
  "timestamp": "2026-02-27T12:00:00",
  "cached": true
}
```
**Quadrant Values:** `Leading` (RS>100, momentum>0) | `Weakening` (RS>100, momentum<0) | `Lagging` (RS<100, momentum<0) | `Improving` (RS<100, momentum>0)
**Cache:** Per trading day (SQLite market_cache, expires at next market close)

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

## FRONTEND: Data Flow (Day 61 — NaN-safe)

### Fundamentals Data Flow
```
/api/fundamentals/<ticker>  ─── fetchFundamentals() ──┐
                                                       ├─── stockData.fundamentals = { ...fundamentals, enriched: true }
/api/stock/<ticker>         ─── fetchStockData() ─────┘    (NO merge — fundamentals from single source)
```

**Happy path:** `stockData.fundamentals = { ...fundamentals, enriched: true, enrichedSource: 'finnhub' }`
**Failure path:** `stockData.fundamentals = { dataQuality: 'unavailable', enriched: false }`

### NaN Defense (Day 61 — 3-Layer)
```
Backend transforms (field_maps.py) ─── NaN → None ──┐
                                                      ├─── JSON always valid (no NaN)
Cache (cache_manager.py) ─── Schema v2 invalidation ─┤
                                                      ├─── Frontend _sanitize() catches any leaks
Frontend (categoricalAssessment.js) ─── NaN → null ──┘
```

### R:R Calculation (Day 61 — DRY)
```
riskRewardCalc.js ──── calculateRiskReward(srData, currentPrice) ──┐
                                                                     ├─── App.jsx (viability badge)
                       hasViabilityContradiction(srData, rr) ────────┤
                                                                     ├─── App.jsx (contradiction)
                       getViabilityBadge(rr) ────────────────────────┤
                                                                     ├─── DecisionMatrix.jsx
                                                                     └─── BottomLineCard.jsx
```

### Categorical Assessment System (v4.5)

**Verdict Logic (Day 45):**
```
BUY:   2+ Strong categories + Favorable/Neutral Risk
HOLD:  1 Strong category OR Unfavorable Risk override
AVOID: Technical Weak OR (Fundamental Weak + Sentiment Weak)
```

**F&G Thresholds (Day 61 — synced backend + frontend):**
| Range | Assessment |
|-------|------------|
| 60-80 | Strong (greed but not extreme) |
| 35-60 | Neutral (balanced) |
| <35 or >80 | Weak (fear or extreme greed) |

**Entry Preference (ADX-based, Day 47):**
| ADX Value | Entry Preference |
|-----------|------------------|
| >= 25 | "Momentum entry viable" - Strong trend |
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
curl http://localhost:5001/api/fundamentals/AAPL
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/patterns/AAPL
curl http://localhost:5001/api/fear-greed
curl http://localhost:5001/api/earnings/AAPL
curl http://localhost:5001/api/sectors/rotation
curl "http://localhost:5001/api/data/freshness?ticker=AAPL"

# Check provider status
curl -s http://localhost:5001/api/health | python3 -m json.tool
```

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| 61 | **Earnings:** 500 on error (was 200). **F&G:** thresholds synced (60-80/35-60), `fallback:true` flag added. **Fundamentals:** NaN→null, cache schema v2. **Stock:** priceHistory NaN filtering, scalar NaN safety. **Sector Rotation** and **Data Freshness** documented (were missing since Day 58-59). **Scan:** `market_index` param documented (missing since Day 57). **SPY:** `sma50Declining` documented (missing since Day 57). Route count 20→22. |
| 53 | **BREAKING:** `fundamentals` removed from `/api/stock/` response (SRP). Health check: removed `check_defeatbeta` param. Dead functions removed. |
| 52 | v4.14: Multi-source providers in health response, `_field_sources`, `data_provider_available` |
| 49 | Added `/api/earnings/<ticker>`, OBV in S&R response, RVOL enhanced |
| 44 | Added `/api/patterns/<ticker>`, `/api/fear-greed`, Categorical Assessment system |
| 38 | Added `/api/provenance/<ticker>` for data source transparency |
| 33 | MTF confluence in S&R, Defeat Beta health check |
| 31 | Agglomerative clustering, yfinance failsafe |

---

*This file is versioned by day. Current version: DAY61*
*Previous version: API_CONTRACTS_DAY53.md*
