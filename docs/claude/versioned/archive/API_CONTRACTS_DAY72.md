# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Claude Project + Git `/docs/claude/versioned/`
> **Version:** Day 72 (March 31, 2026)
> **Total API Routes:** 28 (no new routes added Day 72)
>
> **Day 72 Changes:** `GET /api/sr/<ticker>` response extended — `meta.levelScores` added (touch count dict). No new endpoints. Frontend v4.33, Backend v2.34, API Service v2.10.

---

## Day 72 API Change — `/api/sr/<ticker>`

### What Changed
`meta.levelScores` is now included in the S/R response `meta` object.

Previously: `level_scores` was computed in `support_resistance.py:_score_levels()` but never passed through to the API response.

Now: 1-line addition in `backend.py` (inside `get_support_resistance()`) exposes it.

### New Field: `meta.levelScores`

```json
{
  "meta": {
    "levelScores": {
      "689.28": 7,
      "637.06": 4,
      "601.50": 3
    }
  }
}
```

**Type:** `dict[str, int]`
**Keys:** Stringified rounded prices (2 decimal places, e.g. `"689.28"`)
**Values:** Integer touch count — how many times price has tested/approached this level
**Source:** `support_resistance.py:_score_levels()` — agglomerative clustering score
**Consumer:** `frontend/src/utils/priceStructureNarrative.js:getTouches()` — fuzzy match within 0.5 price units

### Lookup Pattern (Frontend)
```js
// getTouches() uses fuzzy match because rounding can drift:
for (const k of Object.keys(levelScores)) {
  if (Math.abs(parseFloat(k) - level) < 0.5) {
    return levelScores[k];  // integer touch count
  }
}
```

### Full `/api/sr/<ticker>` Response Shape (Day 72)

```json
{
  "ticker": "NVDA",
  "currentPrice": 873.45,
  "resistance": [900.0, 940.0],
  "support": [850.0, 820.0],
  "weeklyResistance": [...],
  "weeklySupport": [...],
  "resistanceProjected": false,
  "supportProjected": false,
  "obv": {...},
  "meta": {
    "atr": 24.5,
    "rvol": 1.2,
    "rsi_daily": 58.3,
    "adx": { "adx": 32.1, "trend_strength": "Strong" },
    "tradeViability": {
      "viable": "YES",
      "support_distance_pct": 5.3,
      "...": "..."
    },
    "levelScores": {
      "900.00": 5,
      "940.00": 3,
      "850.00": 7,
      "820.00": 4
    },
    "mtf": {
      "confluence_map": {
        "850.00": { "confluent": true, "timeframes": ["daily", "weekly"] }
      }
    }
  }
}
```

---

## All Endpoints (No Change from Day 70)

### Core Analysis
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/analyze/<ticker>` | GET | Full analysis (fundamentals + technical) |
| `/api/sr/<ticker>` | GET | S&R levels + trade setup + OBV (**levelScores added Day 72**) |
| `/api/patterns/<ticker>` | GET | Chart patterns + Trend Template |
| `/api/fear-greed` | GET | CNN Fear & Greed Index |
| `/api/earnings/<ticker>` | GET | Earnings calendar + warning |

### TradingView Scanning
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/tradingview` | GET | Batch scanning with index/market filters |
| `/api/scan/strategies` | GET | Available strategies |

### Sector Rotation (Day 58)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/sectors/rotation` | GET | Sector RS ranking + RRG quadrants (11 SPDR ETFs) |

### Context Tab (Day 62)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cycles` | GET | 6 calendar/yield cycle cards. Cached 6h. |
| `/api/econ` | GET | 4 economic indicator cards. Cached 6h. |
| `/api/news/<ticker>` | GET | News sentiment + short interest per ticker. Cached 4h. |
| `/api/context/<ticker>` | GET | Aggregates cycles + econ + news. overall_regime + options_block. |

### Mean-Reversion (Day 70)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/mr/signal/<ticker>` | GET | RSI(2) oversold signal. Returns rsi2, sma200, conditions, stop/target. |
| `/api/mr/scan` | GET | Scan universe for MR signals. Optional `?tickers=AAPL,AMD,...`. |

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

## Data Sources (unchanged from Day 70)

| Data Type | Primary | Fallback 1 | Fallback 2 | Cache |
|-----------|---------|------------|------------|-------|
| OHLCV (Daily) | TwelveData | yfinance | Stooq | SQLite (market-aware TTL) |
| Intraday (4H RSI) | TwelveData | yfinance | - | Not cached |
| Fundamentals | Finnhub | AlphaVantage | yfinance | SQLite (7-day TTL) |
| VIX Quote | yfinance | Finnhub | stale cache | - |
| Sentiment | CNN Fear & Greed | - | fallback w/ flag | - |
| Sector Rotation | yfinance (11 SPDR ETFs) | - | - | SQLite (trading day) |
| Yield/Business Cycles | FRED API | calendar compute | - | SQLite 6h |
| Econ Indicators | FRED API | - | - | SQLite 6h |
| News Sentiment | Alpha Vantage NEWS_SENTIMENT | - | - | SQLite 4h per ticker |

> Full API contracts (all endpoints with response shapes) are in `API_CONTRACTS_DAY70.md`.
> Day 72 only adds `meta.levelScores` to `/api/sr/<ticker>`. All other contracts unchanged.
