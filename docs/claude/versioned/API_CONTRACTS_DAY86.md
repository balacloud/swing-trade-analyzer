# API Contracts — Day 86 (July 15, 2026)

> Supersedes `API_CONTRACTS_DAY79.md` for the one endpoint below. All other
> endpoints documented there are unchanged.

---

## Day 86 Changed Endpoint — `GET /api/sr/<ticker>`

### Purpose
Unchanged — computes support/resistance levels, trade setup suggestion, and
technical meta (ADX, RSI, OBV, RVOL, MTF confluence) from OHLCV price
history.

### What changed
Two new top-level response fields, both computed from the OHLCV frame the
route already fetches — **no new provider/API call added**:

| Field | Type | Description |
|---|---|---|
| `volume` | `int \| null` | Today's raw share volume (last bar's `volume`, from the same 2-year OHLCV history already used for S/R). `null` if the OHLCV frame is empty (shouldn't happen — the route 404s before this point if it is). |
| `change` | `float \| null` | Day change %, `(close[-1] - close[-2]) / close[-2] * 100`, rounded to 2 decimals. `null` if fewer than 2 bars are available or the prior close is 0. |

### Why
`/api/sr/<ticker>` is the endpoint the curated-ticker-list Scan presets
(Nirmal's Watchlist, Master Framework Watchlist) call per ticker — those
presets bypass TradingView's market-wide query entirely, so their summary
table never had Volume/Change data (both come from the TradingView response
for the other 5 scan strategies). This was a real, user-reported gap in the
Master Framework Watchlist's first live test. Fixed by exposing data the
route already had, rather than adding a new fetch.

### Backward compatibility
Additive only — existing consumers that don't read `volume`/`change` are
unaffected. `frontend/src/services/api.js`'s `fetchSupportResistance()`
field whitelist was updated to pass both through (previously would have
silently dropped them even after the backend started returning them).

### Verified (Day 86)
Live spot-check against the running backend:

| Ticker | volume | change |
|---|---|---|
| GEV | 526,156 | -1.0% |
| CCO.TO | 800,496 | -0.92% |
| PLTR | 25,984,282 | +0.03% |
| TECK-B.TO | 1,098,720 | -3.72% |
| NVDA | 118,979,465 | +0.33% |

### Known limitation (unchanged, not addressed by this fix)
`/api/sr/<ticker>` still never returns company `name`, `sector`, or
`marketCap` — those require a separate fundamentals/quote call this route
was never built to make. Deferred by explicit user choice (see
`docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md`).

---

## Unchanged Endpoints (Day 79 reference)

See `API_CONTRACTS_DAY79.md` for the full contract of `/api/breakout/<ticker>`
and all other endpoints — nothing else changed this session.
