# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 52 (February 12, 2026)
> **Total API Routes:** 20 (verify with `grep -n "@app.route" backend.py`)

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
| Fundamentals | Finnhub | FMP | yfinance | SQLite (7-day TTL) |
| VIX Quote | yfinance | Finnhub | stale cache | - |
| Stock Info (name/sector) | yfinance | - | - | - |
| Earnings | yfinance | - | - | - |
| Batch Scanning | TradingView Screener | - | - | - |
| Sentiment | CNN Fear & Greed | - | Default 50 | - |

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
│   ├── backend.py                  # Flask API server (v2.17)
│   ├── support_resistance.py       # S&R: Agglomerative + MTF confluence
│   ├── pattern_detection.py        # VCP, Cup & Handle, Flat Base detection
│   ├── cache_manager.py            # SQLite cache (source column added Day 52)
│   ├── .env                        # API keys (gitignored)
│   ├── .env.example                # Template with registration URLs
│   ├── providers/                  # v4.14 Multi-Source Data Intelligence
│   │   ├── __init__.py             # Exports get_data_provider()
│   │   ├── orchestrator.py         # THE CORE: fallback chains, field merge
│   │   ├── base.py                 # Abstract interfaces + result dataclasses
│   │   ├── exceptions.py           # ProviderError hierarchy
│   │   ├── field_maps.py           # Field normalization per provider
│   │   ├── rate_limiter.py         # Token-bucket per provider
│   │   ├── circuit_breaker.py      # CLOSED→OPEN→HALF_OPEN pattern
│   │   ├── twelvedata_provider.py  # Primary OHLCV + Intraday
│   │   ├── finnhub_provider.py     # Primary Fundamentals + Quote
│   │   ├── fmp_provider.py         # Growth metrics (epsGrowth, revenueGrowth)
│   │   ├── yfinance_provider.py    # Universal fallback (all 6 interfaces)
│   │   ├── stooq_provider.py       # Last-resort OHLCV
│   │   └── backtest_adapter.py     # Drop-in yf.download() replacement
│   ├── backtest/
│   │   └── backtest_adx_rsi_thresholds.py  # Uses backtest_adapter
│   ├── validation/
│   │   └── engine.py, scrapers.py, etc.
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main React component (v4.4)
│   │   ├── services/api.js         # API client (v2.8)
│   │   └── utils/
│   │       ├── categoricalAssessment.js  # v4.5 Categorical System
│   │       ├── scoringEngine.js    # Legacy scoring + multi-source quality
│   │       ├── forwardTesting.js   # Paper trading (v4.7)
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

## BACKEND API ENDPOINTS (20 Routes)

### Health & Diagnostics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check + provider status |
| `/api/cache/status` | GET | Cache stats and ticker list |
| `/api/cache/clear` | POST | Clear cache (all or specific ticker) |
| `/api/provenance/<ticker>` | GET | Data source tracing (Day 38) |

**Health Check Response (v2.17):**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-12T06:00:00",
  "version": "2.17",
  "data_provider_available": true,
  "providers": {
    "providers": {
      "twelvedata": {"configured": true, "type": "OHLCV + Intraday"},
      "finnhub": {"configured": true, "type": "Fundamentals + Quote"},
      "fmp": {"configured": true, "type": "Fundamentals (growth)"},
      "yfinance": {"configured": true, "type": "All (fallback)"},
      "stooq": {"configured": true, "type": "OHLCV (last resort)"}
    },
    "circuit_breakers": {},
    "rate_limiters": {},
    "last_sources": {"AAPL_ohlcv": "twelvedata", "AAPL_fundamentals": "finnhub"}
  },
  "defeatbeta_available": true,
  "tradingview_available": true,
  "sr_engine_available": true,
  "validation_available": true,
  "cache": {
    "ohlcv_count": 32,
    "fundamentals_count": 10,
    "cache_size_kb": 4548.0
  }
}
```

### Stock & Fundamentals
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stock/<ticker>` | GET | Stock data + prices |
| `/api/fundamentals/<ticker>` | GET | Fundamentals (Finnhub → FMP → yfinance) |

**Fundamentals Response (v4.14):**
```json
{
  "source": "finnhub",
  "dataSource": "finnhub",
  "dataQuality": "full",
  "fallbackUsed": false,
  "ticker": "AAPL",
  "roe": 151.91,
  "epsGrowth": 12.5,
  "revenueGrowth": 6.43,
  "debtToEquity": 1.34,
  "profitMargin": 24.3,
  "_field_sources": {
    "pe": "finnhub",
    "roe": "finnhub",
    "roa": "finnhub",
    "epsGrowth": "fmp",
    "revenueGrowth": "fmp",
    "debtToEquity": "finnhub",
    "profitMargin": "finnhub",
    "pegRatio": "yfinance"
  },
  "isETF": false
}
```

**Data Quality Values:** `"full"` (multi-source merge working), `"partial"` (yfinance fallback only), `"unavailable"`

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation |
| `/api/market/vix` | GET | VIX for risk assessment |

### Fear & Greed Index (Day 44 - v4.5)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fear-greed` | GET | CNN Fear & Greed Index for sentiment |

### Earnings Calendar (Day 49 - v4.10)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/earnings/<ticker>` | GET | Earnings calendar + warning |

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
| `/api/scan/tradingview` | GET | Batch scanning |
| `/api/scan/strategies` | GET | Available strategies |

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

### Verdict Logic (Day 45)
```
BUY:   2+ Strong categories + Favorable/Neutral Risk
HOLD:  1 Strong category OR Unfavorable Risk override
AVOID: Technical Weak OR (Fundamental Weak + Sentiment Weak)
```

### Entry Preference (ADX-based, Day 47)
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
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/patterns/AAPL
curl http://localhost:5001/api/fear-greed
curl http://localhost:5001/api/earnings/AAPL

# Check provider status
curl -s http://localhost:5001/api/health | python3 -m json.tool
```

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| 52 | v4.14: Multi-source providers in health response, fundamentals now show `_field_sources`, `data_provider_available` field added |
| 49 | Added `/api/earnings/<ticker>`, OBV in S&R response, RVOL enhanced |
| 44 | Added `/api/patterns/<ticker>`, `/api/fear-greed`, Categorical Assessment system |
| 38 | Added `/api/provenance/<ticker>` for data source transparency |
| 33 | MTF confluence in S&R, Defeat Beta health check |
| 31 | Agglomerative clustering, yfinance failsafe |

---

*This file is versioned by day. Current version: DAY52*
*Previous version: API_CONTRACTS_DAY49.md*
