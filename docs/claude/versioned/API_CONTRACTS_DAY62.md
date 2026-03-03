# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 62 (March 1, 2026)
> **Total API Routes:** 26 (verify with `grep -n "@app.route" backend.py`)

---

## PROJECT OVERVIEW

**Swing Trade Analyzer** - Institutional-grade stock analysis system
**Methodology:** Mark Minervini's SEPA + William O'Neil's CAN SLIM
**Target:** 10-20% profits over 1-2 months, ~50% win rate (backtested)

### Data Sources (v4.14 Multi-Source + Day 62 Context)
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
| Yield/Business Cycles | FRED API (T10Y2Y, INDPRO) | calendar compute | - | SQLite 6h |
| Econ Indicators | FRED API (FEDFUNDS, CPI, UNRATE, MANEMP) | - | - | SQLite 6h |
| News Sentiment | Alpha Vantage NEWS_SENTIMENT | - | - | SQLite 4h per ticker |
| Short Interest | yfinance (shortPercentOfFloat) | - | - | bundled with news cache |

### Provider API Keys (in `backend/.env`)
| Provider | Env Var | Rate Limit |
|----------|---------|------------|
| TwelveData | `TWELVEDATA_API_KEY` | 8/min, 800/day |
| Finnhub | `FINNHUB_API_KEY` | 60/min |
| FMP | `FMP_API_KEY` | 10/min, 250/day |
| FRED | `FRED_API_KEY` | 1000/day (free) |
| Alpha Vantage | `ALPHAVANTAGE_API_KEY` | 25/day (free) |
| yfinance | None (free) | 30/min (self-imposed) |
| Stooq | None (free) | 5/min (self-imposed) |

---

## PROJECT STRUCTURE

```
/Users/balajik/projects/swing-trade-analyzer/
├── backend/
│   ├── backend.py                  # Flask API server (v2.25)
│   ├── cycles_engine.py            # Day 62: 6 calendar/yield cycle cards (FRED + calendar)
│   ├── econ_engine.py              # Day 62: 4 economic indicator cards (FRED)
│   ├── news_engine.py              # Day 62: News sentiment (Alpha Vantage) + short interest (yfinance)
│   ├── support_resistance.py       # S&R: Agglomerative + MTF confluence
│   ├── pattern_detection.py        # VCP, Cup & Handle, Flat Base detection
│   ├── cache_manager.py            # SQLite cache (schema v2, Day 61; context TTL wrappers Day 62)
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
│   │   ├── App.jsx                 # Main React component (v4.11)
│   │   ├── components/
│   │   │   ├── DecisionMatrix.jsx  # v4.15 Decision Matrix
│   │   │   ├── BottomLineCard.jsx  # Bottom Line summary
│   │   │   ├── SectorRotationTab.jsx # Day 62: 11 sector cards + Scan for Rank 1
│   │   │   ├── ContextTab.jsx      # Day 62: 3-column pre-flight context
│   │   │   ├── RegimeBanner.jsx    # Day 62: Overall macro regime banner
│   │   │   ├── CycleCard.jsx       # Day 62: Cycle/econ card (shared by cols A+B)
│   │   │   ├── ArticleRow.jsx      # Day 62: News article row
│   │   │   └── ConflictCheck.jsx   # Day 62: ALIGNED/CONFLICT/PARTIAL banner
│   │   ├── services/api.js         # API client (v2.9)
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

## BACKEND API ENDPOINTS (26 Routes)

### Health & Diagnostics
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Backend health check + provider status |
| `/api/cache/status` | GET | Cache stats and ticker list |
| `/api/cache/clear` | POST | Clear cache (all or specific ticker) |
| `/api/provenance/<ticker>` | GET | Data source tracing (Day 38) |
| `/api/data/freshness` | GET | Cache freshness per data source (Day 59) |

### Stock & Fundamentals
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stock/<ticker>` | GET | Stock metadata + prices (NO fundamentals) |
| `/api/fundamentals/<ticker>` | GET | Fundamentals (Finnhub → FMP → yfinance) |

### Market Data
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/market/spy` | GET | SPY data for RS calculation + regime |
| `/api/market/vix` | GET | VIX for risk assessment |

### Sentiment & Earnings
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/fear-greed` | GET | CNN Fear & Greed Index |
| `/api/earnings/<ticker>` | GET | Earnings calendar + warning |

### Support & Resistance / Patterns
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + OBV |
| `/api/patterns/<ticker>` | GET | Chart patterns + Trend Template |

### TradingView Scanning
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | GET | Batch scanning with index/market filters |
| `/api/scan/strategies` | GET | Available strategies |

### Sector Rotation (Day 58)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sectors/rotation` | GET | Sector RS ranking + RRG quadrants (11 SPDR ETFs) |

### Context Tab — NEW Day 62 (4 routes)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cycles` | GET | 6 calendar/yield cycle cards. Cached 6h. No ticker needed. |
| `/api/econ` | GET | 4 economic indicator cards. Cached 6h. No ticker needed. |
| `/api/news/<ticker>` | GET | News sentiment + short interest per ticker. Cached 4h. |
| `/api/context/<ticker>` | GET | Aggregates cycles + econ + news. Computes overall_regime + options_block. |

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

## NEW ENDPOINT CONTRACTS (Day 62)

### GET `/api/cycles`
Returns 6 calendar/yield cycle cards for Column A of Context Tab.
**Cache:** 6 hours (SQLite market_cache, key `CYCLES`).
**Auth:** Requires `FRED_API_KEY` in `.env` for T10Y2Y + INDPRO cards. Calendar cards (Presidential Year, Seasonal, FOMC, Quad Witching) compute without key.

**Response:**
```json
{
  "cards": [
    {
      "name": "Yield Curve",
      "icon": "📈",
      "value": "+0.62%",
      "phase": "Normal · Steepening ↑",
      "source": "FRED T10Y2Y",
      "series_id": "T10Y2Y",
      "history": "Avg S&P +13.2%/yr in this regime",
      "regime": "FAVORABLE",
      "raw_value": 0.62
    },
    {
      "name": "Business Cycle",
      "icon": "🏭",
      "value": "+0.3% MoM",
      "phase": "Expansion",
      "source": "FRED INDPRO",
      "series_id": "INDPRO",
      "history": "Expansion: avg S&P fwd 12m +12.9%",
      "regime": "FAVORABLE",
      "raw_value": 0.3
    },
    {
      "name": "Presidential Year",
      "icon": "🏛️",
      "value": "Year 2",
      "phase": "Typically weakest year — caution",
      "source": "Calendar",
      "series_id": null,
      "history": "Avg S&P Year 2: +3.0%",
      "regime": "ADVERSE",
      "raw_value": 2
    },
    {
      "name": "Seasonal",
      "icon": "🌸",
      "value": "Mar → FAVORABLE",
      "phase": "Nov–Apr favorable window",
      "source": "Calendar",
      "series_id": null,
      "history": "Nov–Apr avg S&P: +7.1%",
      "regime": "FAVORABLE",
      "raw_value": 3
    },
    {
      "name": "FOMC Proximity",
      "icon": "🏦",
      "value": "21 days away",
      "phase": "Normal window",
      "source": "Hardcoded 2026–2027 dates",
      "series_id": null,
      "history": "Market neutral 15–40d pre-FOMC",
      "regime": "NEUTRAL",
      "raw_value": 21
    },
    {
      "name": "Quad Witching",
      "icon": "🧙",
      "value": "18 days away",
      "phase": "Outside danger window",
      "source": "3rd Friday Mar/Jun/Sep/Dec",
      "series_id": null,
      "history": "Week-of quad witching: elevated volatility",
      "regime": "FAVORABLE",
      "raw_value": 18
    }
  ],
  "options_block": {
    "has_options_block": false,
    "reason": null
  },
  "summary": {
    "favorable": 4,
    "neutral": 1,
    "adverse": 1
  },
  "timestamp": "2026-03-01T10:00:00",
  "fred_available": true,
  "from_cache": false
}
```

**`regime` Values:** `"FAVORABLE"` | `"NEUTRAL"` | `"ADVERSE"`

**`options_block` Logic:**
- `has_options_block: true` when FOMC < 5 days OR Quad Witching < 3 days
- `reason`: `"FOMC in <5d"` | `"Quad Witching in <3d"` | `null`

**Regime Thresholds:**
| Card | FAVORABLE | NEUTRAL | ADVERSE |
|------|-----------|---------|---------|
| Yield Curve (T10Y2Y) | >= 0.5% | 0–0.5% | < 0% |
| Business Cycle (INDPRO MoM%) | > 0.2% | -0.1 to 0.2% | < -0.1% |
| Presidential Year | Year 3 or 4 | Year 1 | Year 2 |
| Seasonal | Nov–Apr | May–Oct | — |
| FOMC Proximity (days) | 15–40d | 5–14d | < 5d |
| Quad Witching (days) | > 5d | 3–5d | < 3d |

---

### GET `/api/econ`
Returns 4 economic indicator cards for Column B of Context Tab.
**Cache:** 6 hours (SQLite market_cache, key `ECON_INDICATORS`).
**Auth:** Requires `FRED_API_KEY` in `.env`.

**Response:**
```json
{
  "cards": [
    {
      "name": "Fed Funds Rate",
      "icon": "💵",
      "value": "5.33%",
      "phase": "Flat/Hold (no recent cuts)",
      "source": "FRED FEDFUNDS",
      "series_id": "FEDFUNDS",
      "history": "Cutting cycles avg S&P: +15–20% fwd 12m",
      "regime": "NEUTRAL",
      "raw_value": 5.33
    },
    {
      "name": "CPI Inflation",
      "icon": "📦",
      "value": "CPI 3.1% · Core 3.5%",
      "phase": "Moderating — above target",
      "source": "FRED CPIAUCSL · CPILFESL",
      "series_id": "CPIAUCSL",
      "history": "CPI 2–3%: avg S&P fwd 12m +12.1%",
      "regime": "NEUTRAL",
      "raw_value": 3.1
    },
    {
      "name": "Manufacturing (PMI proxy)",
      "icon": "🏗️",
      "value": "+0.2% MoM",
      "phase": "Mild expansion",
      "source": "FRED MANEMP (proxy)",
      "series_id": "MANEMP",
      "history": "Manufacturing expansion: historically bullish for industrials",
      "regime": "FAVORABLE",
      "raw_value": 0.2
    },
    {
      "name": "Unemployment",
      "icon": "👷",
      "value": "4.1%",
      "phase": "Low and stable",
      "source": "FRED UNRATE",
      "series_id": "UNRATE",
      "history": "Sub-4.5%: historically bullish consumer spending",
      "regime": "FAVORABLE",
      "raw_value": 4.1
    }
  ],
  "composite": {
    "title": "Mixed Growth + Moderate CPI",
    "description": "Fed on hold, inflation moderating toward target. Historically neutral-to-positive for equities.",
    "avg_return": null,
    "source": "S&P Global factor study"
  },
  "summary": {
    "favorable": 2,
    "neutral": 2,
    "adverse": 0
  },
  "timestamp": "2026-03-01T10:00:00",
  "fred_available": true,
  "from_cache": false
}
```

**Regime Thresholds:**
| Card | FAVORABLE | NEUTRAL | ADVERSE |
|------|-----------|---------|---------|
| Fed Funds (direction) | Declining/cutting | Flat/hold | Rising/hiking |
| CPI YoY | <= 3.0% | 3.0–5.0% | > 5.0% |
| PMI proxy (MANEMP MoM%) | > 0.15% | -0.05 to 0.15% | < -0.05% |
| Unemployment (UNRATE) | < 4.5%, flat/falling | 4.5–5.5% or slowly rising | > 5.5% or rapidly rising |

---

### GET `/api/news/<ticker>`
Returns news sentiment + short interest for a specific ticker.
**Cache:** 4 hours per ticker (SQLite market_cache, key `NEWS_{TICKER}`).
**Auth:** Requires `ALPHAVANTAGE_API_KEY` in `.env` for articles. Short interest uses yfinance (no key).

**Response (key configured):**
```json
{
  "ticker": "AMD",
  "articles": [
    {
      "title": "AMD Options Activity Signals Bullish...",
      "url": "https://reuters.com/...",
      "source": "Reuters",
      "date": "2026-03-01",
      "score": 0.34,
      "emoji": "🟢",
      "sentiment_label": "Bullish"
    }
  ],
  "aggregate": {
    "label": "BULLISH",
    "avg_score": 0.153,
    "bullish": 23,
    "neutral": 21,
    "bearish": 6
  },
  "short_interest": {
    "short_pct_float": 0.081,
    "short_ratio": 2.3,
    "assessment": "Normal"
  },
  "error": null,
  "timestamp": "2026-03-01T10:00:00",
  "av_available": true,
  "from_cache": false
}
```

**Response (key not configured):**
```json
{
  "ticker": "AMD",
  "articles": [],
  "aggregate": null,
  "short_interest": {"short_pct_float": 0.081, "short_ratio": 2.3, "assessment": "Normal"},
  "error": "Alpha Vantage key not configured",
  "av_available": false
}
```

**`aggregate.label` Values:** `"BULLISH"` (avg_score > 0.1) | `"NEUTRAL"` | `"BEARISH"` (avg_score < -0.1)
**`short_interest.assessment` Values:** `"High"` (> 20% float) | `"Normal"` (5–20%) | `"Low"` (< 5%) | `"Unknown"`
**Score thresholds:** article bullish > 0.15, bearish < -0.15, neutral = in-between

---

### GET `/api/context/<ticker>`
Aggregates cycles + econ + news into a single response with overall regime classification.
**Cache:** Uses individual caches for each sub-component (cycles 6h, econ 6h, news 4h).
**Auth:** See `/api/cycles`, `/api/econ`, `/api/news/<ticker>` for key requirements.

**Response:**
```json
{
  "ticker": "AMD",
  "overall_regime": "NEUTRAL",
  "regime_counts": {
    "favorable": 6,
    "neutral": 3,
    "adverse": 1
  },
  "total_indicators": 10,
  "options_block": {
    "has_options_block": false,
    "reason": null
  },
  "cycles": { "...same as /api/cycles response..." },
  "econ": { "...same as /api/econ response..." },
  "news": { "...same as /api/news/<ticker> response..." }
}
```

**`overall_regime` Classification Logic (10 indicators total — 6 cycles + 4 econ):**
| Condition | `overall_regime` |
|-----------|-----------------|
| `adverse >= 4` | `"ADVERSE"` |
| `adverse >= 2` OR `favorable < 5` | `"NEUTRAL"` |
| Otherwise | `"FAVORABLE"` |

**IMPORTANT:** Context Tab is PRE-FLIGHT CONTEXT ONLY. `overall_regime` does NOT modify trade verdicts, categorical assessment, or decision matrix. Human is always the final decision-maker.

---

## EXISTING ENDPOINT CONTRACTS (Unchanged from Day 61)

### `/api/sectors/rotation` (Day 58)
**Response (Day 62 update — `mapping` expanded):**
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
      "monthChange": 5.3,
      "rank": 1
    }
  ],
  "mapping": {
    "Technology": "XLK",
    "Information Technology": "XLK",
    "Electronic Technology": "XLK",
    "Technology Services": "XLK",
    "Basic Materials": "XLB",
    "Materials": "XLB",
    "Non-Energy Minerals": "XLB",
    "Process Industries": "XLB",
    "Energy": "XLE",
    "Energy Minerals": "XLE"
  },
  "timestamp": "2026-03-01T12:00:00",
  "cached": true
}
```
**Day 62 change:** `mapping` now includes TradingView SIC-based sector names (49 entries total, up from ~20). This enables correct sector filter matching in Scan tab when TradingView screener returns SIC names like "Non-Energy Minerals" instead of GICS "Materials".

### All other endpoints
Unchanged from Day 61. See API_CONTRACTS_DAY61.md for full details on:
- `/api/stock/<ticker>`, `/api/fundamentals/<ticker>`
- `/api/market/spy`, `/api/market/vix`
- `/api/fear-greed`, `/api/earnings/<ticker>`
- `/api/sr/<ticker>`, `/api/patterns/<ticker>`
- `/api/scan/tradingview`, `/api/scan/strategies`
- `/api/data/freshness`, `/api/cache/*`, `/api/provenance/<ticker>`
- All validation + forward test endpoints

---

## CACHE TTL REFERENCE (Day 62)

| Cache Key | TTL | Description |
|-----------|-----|-------------|
| `OHLCV_{ticker}` | Market-aware | 4h during market, until next open otherwise |
| `FUNDAMENTALS_{ticker}` | 7 days | Schema v2 (auto-invalidates pre-Day 60) |
| `SECTOR_ROTATION` | Trading day | Expires at next market close |
| `CYCLES` | 6 hours | Calendar/yield cycles (FRED monthly data) |
| `ECON_INDICATORS` | 6 hours | Economic indicators (FRED monthly data) |
| `NEWS_{ticker}` | 4 hours | Alpha Vantage news per ticker (25 req/day limit) |

---

## FRONTEND: Data Flow (Day 62)

### Context Tab Load Pattern
```
On mount:
  GET /api/context/{ticker || 'SPY'}
    → cycles (Column A), econ (Column B), overall_regime, options_block
On ticker change:
  GET /api/news/{ticker}
    → articles, aggregate, short_interest (Column C)
```

### ConflictCheck Logic
```
ALIGNED:  cyclesRegime === 'FAVORABLE' AND newsLabel === 'BULLISH' AND !hasOptionsBlock
CONFLICT: cyclesRegime === 'ADVERSE' AND newsLabel === 'BEARISH'
PARTIAL:  all other combinations (including hasOptionsBlock alone)
```

### Sector Filter Logic (Day 62 fix)
```
// NOT: s.sector.includes("materials")          ← broken (TradingView SIC names)
// YES: getSectorContext(s.sector)?.etf === sectorFilter.etf  ← correct (ETF lookup)
```

### R:R Calculation (Day 61 — DRY, unchanged)
```
riskRewardCalc.js ──── calculateRiskReward(srData, currentPrice) ──┐
                                                                     ├─── App.jsx (viability badge)
                       hasViabilityContradiction(srData, rr) ────────┤
                                                                     ├─── App.jsx (contradiction)
                       getViabilityBadge(rr) ────────────────────────┤
                                                                     ├─── DecisionMatrix.jsx
                                                                     └─── BottomLineCard.jsx
```

### Categorical Assessment System (v4.5 — unchanged)

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

# Test existing endpoints
curl http://localhost:5001/api/health
curl http://localhost:5001/api/stock/AAPL
curl http://localhost:5001/api/fundamentals/AAPL
curl http://localhost:5001/api/sr/AAPL
curl http://localhost:5001/api/patterns/AAPL
curl http://localhost:5001/api/fear-greed
curl http://localhost:5001/api/earnings/AAPL
curl http://localhost:5001/api/sectors/rotation
curl "http://localhost:5001/api/data/freshness?ticker=AAPL"

# Test new Day 62 context endpoints
curl http://localhost:5001/api/cycles
curl http://localhost:5001/api/econ
curl http://localhost:5001/api/news/AMD
curl http://localhost:5001/api/context/AMD

# Clear context cache (if FRED key changes)
sqlite3 backend/cache.db "DELETE FROM market_cache WHERE symbol IN ('CYCLES', 'ECON_INDICATORS')"
```

---

## CHANGE LOG

| Day | Changes |
|-----|---------|
| 62 | **NEW:** `/api/cycles` (6 cycle cards, FRED + calendar, cached 6h). **NEW:** `/api/econ` (4 econ cards, FRED, cached 6h). **NEW:** `/api/news/<ticker>` (Alpha Vantage + yfinance short interest, cached 4h). **NEW:** `/api/context/<ticker>` (aggregator, overall_regime). **Updated:** `/api/sectors/rotation` mapping expanded to 49 entries (TradingView SIC names added). Route count 22→26. Backend v2.24→v2.25. Frontend v4.10→v4.11. API Service v2.8→v2.9. |
| 61 | **Earnings:** 500 on error (was 200). **F&G:** thresholds synced (60-80/35-60), `fallback:true` flag added. **Fundamentals:** NaN→null, cache schema v2. **Stock:** priceHistory NaN filtering, scalar NaN safety. **Sector Rotation** and **Data Freshness** documented. Route count 20→22. |
| 53 | **BREAKING:** `fundamentals` removed from `/api/stock/` response (SRP). Health check: removed `check_defeatbeta` param. |
| 52 | v4.14: Multi-source providers in health response, `_field_sources`, `data_provider_available` |
| 49 | Added `/api/earnings/<ticker>`, OBV in S&R response, RVOL enhanced |
| 44 | Added `/api/patterns/<ticker>`, `/api/fear-greed`, Categorical Assessment system |
| 38 | Added `/api/provenance/<ticker>` for data source transparency |

---

*This file is versioned by day. Current version: DAY62*
*Previous version: API_CONTRACTS_DAY61.md*
