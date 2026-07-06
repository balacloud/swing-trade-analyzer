# API CONTRACTS & DATA STRUCTURES

> **Purpose:** Stable reference for all API contracts
> **Location:** Git `/docs/claude/versioned/`
> **Version:** Day 79 (July 6, 2026)
> **Total API Routes:** 30 (1 new route wired Day 79: `/api/breakout/<ticker>`)
>
> **Day 79 Changes:** `GET /api/breakout/<ticker>` — built by a parallel session (Day 78) but never registered in `backend.py`; wired and behaviorally validated this session. Isolated read-only classification endpoint, no impact on existing routes, verdict logic, or scoring. Frontend v4.36, Backend v2.36, API Service v2.11.

---

## Day 79 New (Wired) Endpoint — `GET /api/breakout/<ticker>`

### Purpose
Standalone breakout state classifier — human-in-the-loop filter, not an auto-trading signal. Complements (does not replace) `pattern_detection.py`'s VCP/Cup&Handle/Flat Base lifecycle with a richer, independent classification: trend + relative strength + volume + candle quality + supply/rejection + extension-risk gates. **Completely isolated from swing verdict, categorical assessment, and Config C.**

### Implementation
- Engine: `backend/breakout_detection.py` — `detect_breakout()`
- Route registration: `backend/breakout_routes.py` — `register_breakout_routes()`, called from `backend.py` following the standard optional-import pattern (see `DATA_PROVIDER_AVAILABLE`, `VALIDATION_AVAILABLE` for the precedent)
- Spec (source of truth for state definitions): `docs/claude/design/BREAKOUT_ENGINE_SPEC.md`

### Data Flow
`DataProvider` first (cache-first, TwelveData→yfinance chain) → yfinance fallback → SPY benchmark fetched the same way → `detect_breakout(ohlcv, ticker, benchmark_ohlcv)` → flat JSON. No fabricated fallback values — missing fields are `null`.

### Response Shape (verified live, IBM example)

```json
{
  "ticker": "IBM",
  "status": "FAILED_BREAKOUT",
  "humanAction": "Avoid or reassess; breakout level failed.",
  "currentPrice": 289.52,
  "breakoutLevel": 332.46,
  "supportLevel": 212.34,
  "invalidation": 212.34,
  "retestZoneLow": 324.7,
  "retestZoneHigh": 331.26,
  "rvol": 0.7,
  "atrPct": 3.96,
  "extensionFromSma50Pct": 13.39,
  "checks": {
    "trendOk": false,
    "priceAboveEma20": true,
    "nearResistance": false,
    "rsStrong": true,
    "atrContracting": false,
    "volumeDryUp": true,
    "volumeExpansion": false,
    "strongClose": true,
    "strongBody": true,
    "lowUpperWick": true,
    "wideRange": false,
    "candleQualityOk": false,
    "notExtended": false,
    "breakoutConfirmed": false,
    "breakoutWatch": false,
    "buildingBase": true,
    "retestEntry": false
  },
  "warnings": {
    "supplyWarning": false,
    "rejectionCandle": false,
    "highVolumeRed": false,
    "extensionRisk": true,
    "failedBreakout": true
  },
  "evidence": {
    "ticker": "IBM",
    "method": "STA breakout v1 — price/volume/candle/RS filter",
    "resistanceLookbackBars": 60,
    "supportLookbackBars": 60,
    "recentBreakoutLevel": 327.98,
    "recentBreakoutBarsAgo": 21,
    "closeLocation": 0.84,
    "bodyPct": 0.74,
    "upperWickPct": 0.16,
    "atr": 11.46,
    "sma50": 255.34,
    "sma200": 274.28
  },
  "source": "DataProvider",
  "benchmark": { "ticker": "SPY", "source": "DataProvider", "available": true },
  "dataPoints": 260,
  "apiTimestamp": "2026-07-06T12:49:25.090953+00:00"
}
```

### 8 Possible `status` Values (priority order — see spec §11)
`FAILED_BREAKOUT` > `SUPPLY_WARNING` > `EXTENDED_CHASE_RISK` > `RETEST_ENTRY` > `BREAKOUT_CONFIRMED` > `BREAKOUT_WATCH` > `BUILDING_BASE` > `NOT_READY`

### Frontend Display Rule (spec §13 — not yet built, no frontend consumer exists yet)
| Status | Badge color | Meaning |
|--------|------------|---------|
| `BREAKOUT_CONFIRMED` | Green | Valid candidate, still needs risk review — **never a blind buy signal** |
| `RETEST_ENTRY` | Blue | Potential safer secondary entry |
| `BREAKOUT_WATCH` | Amber | Watch, not trade-ready |
| `BUILDING_BASE` | Gray | Developing setup |
| `SUPPLY_WARNING` / `FAILED_BREAKOUT` | Red | Avoid/reassess |
| `EXTENDED_CHASE_RISK` | Orange | Too extended |
| `NOT_READY` | Muted | Ignore/watchlist only |

### Error Handling
- No data / ticker not found → `404 {"error": "No data found for <ticker>"}`
- Insufficient bars (<80) → `400 {"error": "Insufficient data...", "message": "Need at least 80 bars, got N"}`
- Unexpected exception → `500 {"error": str(e)}` with server-side traceback

### Validated (Day 79)
IBM, MSFT, NVDA, PLTR, INTC (weak-name check — correctly never returns `BREAKOUT_CONFIRMED`), and one invalid ticker (clean 404, no crash). No fabricated values observed; `null` correctly used for unavailable fields (e.g., `retestZoneLow/High` when no recent breakout exists).

### Known Limitations (v1, per spec §17)
- Resistance uses simple rolling high (fast classification) — the richer `/api/sr/<ticker>` engine remains separate and authoritative for touch-count-scored levels
- No multi-touch resistance scoring, no overhead supply zone engine, no accumulation/distribution day count yet
- Canadian benchmark unresolved (same known limitation as the rest of STA)
- **Not backtested yet** — architecturally sound (per spec's own audit verdict: PLAUSIBLE) but no performance edge is proven until forward/behavioral testing accumulates

---

## Unchanged Endpoints (Day 75 reference)

See `API_CONTRACTS_DAY75.md` (and archived `API_CONTRACTS_DAY72.md`) for full documentation of all 29 pre-existing endpoints. Key endpoints unchanged:

| Endpoint | Purpose |
|----------|---------|
| `GET /api/stock/<ticker>` | OHLCV + price history for analysis |
| `GET /api/fundamentals/<ticker>` | Multi-source fundamentals (Finnhub→AlphaVantage→yfinance) |
| `GET /api/sr/<ticker>` | Support/resistance levels + `meta.levelScores` (Day 72) |
| `GET /api/patterns/<ticker>` | VCP/Cup&Handle/Flat Base pattern detection |
| `GET /api/value/<ticker>` | Value investing lens (Day 75) |
| `GET /api/context/<ticker>` | Market context (cycles, econ, news, regime) |
| `GET /api/mr/signal/<ticker>` | Mean-reversion signal |
| `GET /api/mr/scan` | MR scan across watchlist |
| `GET /api/scan/tradingview` | TradingView screener scan (5 strategies) |
| `GET /api/fear-greed` | Fear & Greed index |
| `GET /api/health` | Health check — now reports `BACKEND_VERSION` constant (Day 78 fix, was hardcoded '2.23') |
| `GET /api/cache/status` | Cache status |

**Note:** `metrics.py`'s new statistical fields (Task 2.3 — `trades_per_year_actual`, `max_drawdown_fixed_risk_pct`, `t_pvalue_block_bootstrap`, etc.) are backtest-internal, not exposed via any public API route — not documented here as a contract change.
