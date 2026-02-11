# Data Source Intelligence Overview - Swing Trade Engine

## 1) Scope
This document explains the intelligent multi-source data handling implemented in the Swing Trade Engine, including backend source selection, fallback logic, cache behavior, provenance reporting, UI transparency, and validation flows.

Covered API surfaces:
- `GET /api/analyze`
- `GET /api/options/<symbol>`
- `GET /api/options/expiries/<symbol>`

## 2) Data Source Matrix

| Domain | Primary | Fallback Order | Key Fields | Freshness/Caching |
|---|---|---|---|---|
| Daily OHLCV | TwelveData | Alpha Vantage -> yfinance -> Stooq | `open, high, low, close, adj_close, volume` | Source-driven; stale checks via `DERIVED_STALE_DAYS` |
| 4H OHLCV | TwelveData | Alpha Vantage -> yfinance (60m -> 4H resample) | 4H OHLCV, RSI(14), MACD | Best effort; attempts tracked in response |
| Fundamentals | Multi-vendor aggregate | FMP/Finnhub/EODHD/Alpha Vantage per field | ROE, ROA, EPS growth, margins, beta, etc | In-memory TTL (`FUNDAMENTALS_CACHE_TTL`, default 21600s) |
| VIX | yfinance | CNBC JSON-LD fallback | VIX quote + metadata | In-memory cache (1h fresh, 24h stale fallback) |
| Options Chain | Alpaca | Memory cache -> SQLite cache -> hard-TTL cache (throttled mode) | strike, bid/ask, IV, OI, greeks (if present) | `OPTIONS_CACHE_TTL_SEC`, `OPTIONS_HARD_TTL_SEC`, `OPTIONS_MIN_REFRESH_SEC`, throttle window |

## 3) Source Selection Rules

### 3.1 Daily/Benchmark price routing
- Analyzer retrieves stock + SPY with unified fetch wrappers.
- Fallback order is explicitly returned as:
  - `dataSource.fallbackOrder = ["twelvedata", "alphavantage", "yfinance", "stooq"]`
- Every attempt is captured:
  - `dataSource.primaryAttempts`
  - `dataSource.benchmarkAttempts`

### 3.2 4H routing
- 4H retrieval uses dedicated intraday fetch path and returns:
  - `dataSource4h.source`
  - `dataSource4h.meta`
  - `dataSource4h.attempts`
- If unavailable, analyzer still responds with degraded-state warning (`dataQuality.warnings`).

### 3.3 Options routing and cache policy
- Base source: Alpaca option chain snapshot.
- Cache tiers in order:
  1. In-memory cache (fresh <= `OPTIONS_CACHE_TTL_SEC`)
  2. SQLite cache (fresh <= `OPTIONS_CACHE_TTL_SEC`, source `cache_db`)
  3. SQLite hard fallback when throttled (<= `OPTIONS_HARD_TTL_SEC`, source `cache_throttled`)
- Throttle protections:
  - Per-symbol min refresh interval (`OPTIONS_MIN_REFRESH_SEC`)
  - Global request cap (`OPTIONS_MAX_REQUESTS_PER_MIN`)
- If requested expiry is empty, endpoint tries next 8 Fridays and annotates:
  - `meta.requestedExpiry`
  - `meta.fallbackExpiry`

### 3.4 Expiry availability endpoint
- `GET /api/options/expiries/<symbol>`
- Returns next 8 Friday expiries with `available: true/false`.
- `refresh=true` performs live checks; default reads cache (`HARD_TTL_SEC`).

## 4) Provenance and Transparency Model

### 4.1 Backend provenance fields
- `dataSource.primary`, `dataSource.benchmark`, `dataSource.fallbackOrder`
- `dataSource.primaryMeta`, `dataSource.benchmarkMeta`
- `dataSource.primaryAttempts`, `dataSource.benchmarkAttempts`
- `dataSource4h.source/meta/attempts`
- `fundamentalsSources`, `fundamentalsAttempts`
- `fieldProvenance` for local formulas

### 4.2 UI Data Sources page behavior
The frontend shows visually:
- Which provider served each dataset
- Full fallback order
- Per-attempt success/failure information
- 4H source and row metadata
- Fundamentals source attribution by field

This makes source provenance auditable without reading backend logs.

## 5) Options Intelligence Layer (Rule-based)

Options recommendation is deterministic and explainable:
- Bias score from trend + RSI + ADX (`BULLISH/BEARISH/NEUTRAL`, strength levels)
- Contract candidate scoring by risk tier (`safe/balanced/aggressive`) using:
  - strike distance to spot
  - spread penalty
  - OI contribution
  - IV sanity penalties
  - delta target alignment (if available)
  - liquidity score
- Outputs include:
  - `signals.recommended.call/put`
  - `signals.score`, `signals.distancePct`, `signals.spreadPct`
  - `signals.impliedMovePct`
  - `signals.confidenceScore`
  - `signals.dataQuality.warnings/stats`

## 6) Validation Performed

### Automated checks and scripts
- Regression test:
  - `backend/tests/test_analyze_response.py`
- Diagnostics:
  - `backend/scripts/diagnose_4h_reliability.py`
  - `backend/scripts/diagnose_adx_sensitivity.py`
  - `backend/scripts/diagnose_sr_modes.py`
  - `backend/scripts/diagnose_alpaca_options.py`
- Integrated API validation:
  - `backend/scripts/validate_options_dashboard.py`

### Visual validation
- Frontend Data Sources tab displays provider + fallback + attempts.
- Frontend Options tab displays source, cache/live feed state, expiry availability, fallback expiry message, and quality warnings.

## 7) Failure Modes and Guardrails

### Common failure modes
- Missing keys (provider-specific hard failures)
- Partial payloads (missing IV/greeks/bid-ask)
- Intraday data gaps for 4H
- Empty options expiries
- Throttle lock when options are over-polled

### Guardrails implemented
- Cascade fallback across daily providers
- Cache fallback for options under throttle
- Expiry fallback to nearest available Friday
- Confidence and warning flags in options payload
- Degraded-mode analyzer responses with `dataQuality.warnings`

## 8) Current Limitations
- Options source is Alpaca-only for live chains (no secondary live provider integrated)
- Recommendations are rule-based heuristics, not backtested options models
- Greeks may be absent depending on chain payload
- Fundamentals cache is in-memory only (resets on restart)
- One integration test currently assumes running backend (`localhost:5010`)

## 9) Operational Runbook

### Start services
- Backend:
  - `cd backend && .venv/bin/python -m app.main`
- Frontend:
  - `cd frontend && npm run dev`

### Validate source behavior quickly
- Analyze endpoint:
  - `curl "http://localhost:5010/api/analyze?ticker=AAPL"`
- Options endpoint:
  - `curl "http://localhost:5010/api/options/AAPL?limit=40"`
- Expiry availability:
  - `curl "http://localhost:5010/api/options/expiries/AAPL"`

### Run validation scripts
- `backend/.venv/bin/python backend/scripts/validate_options_dashboard.py AAPL`
- `cd backend && .venv/bin/python -m pytest -q`

### Cache maintenance
- Prune old options snapshots:
  - `backend/.venv/bin/python backend/scripts/prune_options_cache.py 7`

## 10) Machine-Readable Appendix

```json
{
  "system": "swing-trade-engine",
  "api_endpoints": [
    {
      "path": "/api/analyze",
      "domains": ["daily_ohlcv", "spy_benchmark", "4h_intraday", "fundamentals", "vix"],
      "provenance_fields": [
        "dataSource.primary",
        "dataSource.benchmark",
        "dataSource.fallbackOrder",
        "dataSource.primaryAttempts",
        "dataSource.benchmarkAttempts",
        "dataSource4h.source",
        "dataSource4h.meta",
        "dataSource4h.attempts",
        "fundamentalsSources",
        "fundamentalsAttempts",
        "fieldProvenance"
      ]
    },
    {
      "path": "/api/options/<symbol>",
      "domains": ["options_chain", "options_signals"],
      "query_params": ["expiry", "refresh", "limit", "type", "min_oi", "strike_window", "spot", "sort", "risk_tier"],
      "provenance_fields": ["meta.source", "meta.requestedExpiry", "meta.fallbackExpiry", "signals.dataQuality", "signals.confidenceScore"]
    },
    {
      "path": "/api/options/expiries/<symbol>",
      "domains": ["expiry_availability"],
      "query_params": ["refresh"],
      "response_shape": {"symbol": "string", "expiries": [{"date": "YYYY-MM-DD", "available": "bool"}]}
    }
  ],
  "fallback_policies": {
    "daily_ohlcv": ["twelvedata", "alphavantage", "yfinance", "stooq"],
    "intraday_4h": ["twelvedata", "alphavantage", "yfinance_resample_60m_to_4h"],
    "options_chain": ["alpaca_live", "memory_cache", "sqlite_cache", "sqlite_hard_ttl_when_throttled"],
    "vix": ["yfinance", "cnbc_json_ld"],
    "fundamentals": ["fmp", "finnhub", "eodhd", "alphavantage"]
  },
  "cache_policies": {
    "options": {
      "memory_ttl_sec": "OPTIONS_CACHE_TTL_SEC",
      "hard_ttl_sec": "OPTIONS_HARD_TTL_SEC",
      "min_refresh_sec": "OPTIONS_MIN_REFRESH_SEC",
      "max_requests_per_min": "OPTIONS_MAX_REQUESTS_PER_MIN",
      "persistent_store": "sqlite backend/data/options.db"
    },
    "fundamentals": {
      "ttl_sec": "FUNDAMENTALS_CACHE_TTL",
      "store": "in_memory"
    },
    "vix": {
      "fresh_ttl_sec": 3600,
      "stale_fallback_ttl_sec": 86400,
      "store": "in_memory"
    }
  },
  "validation_artifacts": [
    "backend/tests/test_analyze_response.py",
    "backend/scripts/validate_options_dashboard.py",
    "backend/scripts/diagnose_4h_reliability.py",
    "backend/scripts/diagnose_adx_sensitivity.py",
    "backend/scripts/diagnose_sr_modes.py",
    "backend/scripts/diagnose_alpaca_options.py"
  ]
}
```
