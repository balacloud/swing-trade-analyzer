# API Contracts — Day 87 (July 16, 2026)

> Supersedes `API_CONTRACTS_DAY86.md` for the endpoints below. All other
> endpoints documented there (and in `API_CONTRACTS_DAY79.md`) are unchanged.

---

## New — `GET /api/market/phase`

### Purpose
N4 Market Phase Synthesis (Day 76 research, Day 87 build). Classifies
current market-wide conditions into one of 5 phases from SPY trend
structure + VIX level, with breadth (RSP/SPY ratio) and sector leadership
(Growth vs Defensive ETFs) shown as supporting context. **Purely
informational — zero impact on verdict, scoring, or Trade Setup.**
Ticker-independent (a whole-market read, not per-stock). Cached per trading
day (same mechanism as `/api/sectors/rotation`).

### Response shape

```json
{
  "phase": "Late Bull",
  "description": "SPY still above its 200-day average but momentum slowing, or VIX creeping up — uptrend intact but maturing.",
  "signals": {
    "spy": {
      "close": 754.51,
      "sma200": 695.85,
      "aboveSma200": true,
      "pctChange20d": -0.04,
      "pctOffRecentLow20d": 3.5,
      "trendBucket": "FLAT"
    },
    "vix": {
      "current": 16.08,
      "pctChange10d": -3.07,
      "levelBucket": "CALM"
    },
    "breadth": {
      "rspSpyRatio": 0.2823,
      "pctChange20d": 0.08,
      "label": "Flat"
    },
    "sectors": {
      "growthReturn20d": -1.57,
      "defensiveReturn20d": 2.74,
      "differential": -4.31,
      "label": "Mixed"
    }
  },
  "asOf": "2026-07-15",
  "timestamp": "2026-07-16T09:48:36.720307",
  "cached": false
}
```

`phase` is one of: `Bull Rally`, `Late Bull`, `Distribution`, `Correction`,
`Recovery`. Classification is a transparent 3×3 grid (SPY trend bucket ×
VIX level bucket) — breadth/sector fields are supporting evidence, not
additional gates, to avoid stacking tuned thresholds on an
informational-only feature.

Returns `503` if the DataProvider isn't available; `500` with
`{"error": ...}` on insufficient SPY history (<200 bars) or missing
VIX/RSP data.

### Data sources
SPY, `^VIX`, RSP via the existing DataProvider OHLCV chain (no new data
sources). Sector ETFs (XLK/XLY/XLC growth, XLU/XLP/XLV defensive) via a
yfinance batch download, same pattern as `/api/sectors/rotation`.

### Verified (Day 87)
Grid classification exhaustively unit-tested (all 9 SPY×VIX combinations +
the DOWN+CALM refinement rule + boundary values at 2%/20/25). Live endpoint
tested and caching (`cached: true` on second call) confirmed.

---

## Changed — `GET /api/scan/tradingview`

### What changed
New `strategy=breakout` option (Breakout Enhancement Plan Phase 1 — "Near
Breakout" scan preset). Finds Stage-2 stocks approaching/crossing new
52-week-high territory, market-wide.

**Query filters** (`col().where()`): exchange in valid list, market cap
≥$2B, close >$10, close > SMA50 > SMA200, RSI 50-70, ADX ≥20.

**Post-filters** (applied in `scan_queries.parse_candidates()`, since these
require arithmetic `col()` doesn't support): within 8% of 52-week high,
average dollar volume (10d avg volume × price) ≥$5M. To avoid the post-filter
starving the result set, the query fetches a wider net (300 candidates,
sorted by relative volume) before filtering, then truncates to the
requested `limit`.

Candidates for **all** strategies now include a new `avgDollarVolume` field
(10-day average volume × price) — additive, no consumer needs to read it.

### Verified (Day 87)
All 50 returned `breakout` candidates checked exhaustively (not
spot-checked) against every filter (price, market cap, RSI, ADX,
pctFromHigh, avgDollarVolume) — zero violations.

---

## Changed — `GET /api/scan/strategies`

New entry added to the `strategies` array:

```json
{
  "id": "breakout",
  "name": "Near Breakout",
  "description": "Stage 2 stocks within 8% of 52-week high — candidates approaching a pivot"
}
```

---

## Changed — `GET /api/sr/<ticker>`

### What changed
New `meta.marketStructure` field (Price Structure Card Phase 2):

```json
"marketStructure": {
  "structure": "Downtrend",
  "trendAgeBars": 29,
  "volumeBehavior": "Flat",
  "recentPivots": [
    {"type": "high", "price": 331.37, "label": "HH"},
    {"type": "low", "price": 273.75, "label": "HL"}
  ]
}
```

- `structure`: one of `Uptrend`, `Downtrend`, `Range`, `Transition`,
  `Insufficient Data`, `Unknown` (error fallback).
- `trendAgeBars`: bars since the current consistent HH/HL (or LH/LL) run
  began. `null` if no labeled pivots exist yet.
- `volumeBehavior`: `Rising`, `Falling`, `Flat`, `Unknown`, or `Insufficient
  data` — volume trend in the run-up to the most recent pivot.
- `recentPivots`: last 8 classified pivots (chronological), each tagged
  HH/LH (highs) or HL/LL (lows) vs. the previous pivot of the same type.
  First high and first low have `label: null` (no prior to compare).

Computed by a new, separate `backend/market_structure_engine.py` —
deliberately does **not** reuse or modify `support_resistance.py`'s
existing `_detect_zigzag_pivots()`, which sorts+dedupes pivots by price
(destroying the chronological order this classification needs). Never
raises; returns a safe default (`structure: "Unknown"`) on any internal
failure so this additive field can't 500 the whole endpoint.

### Verified (Day 87)
Classification logic exhaustively unit-tested with synthetic pivot
sequences (clean uptrend, clean downtrend, up→down transition, down→up
transition, choppy/range, insufficient data) — caught and fixed one real
bug (Transition detection wasn't filtering unlabeled bootstrap pivots
before the "was this an established trend" check). Live-tested on 5 real
tickers (AAPL, NVDA, JPM, COST, TSLA) — no errors.

---

## Unchanged Endpoints

See `API_CONTRACTS_DAY86.md` (which itself points to `API_CONTRACTS_DAY79.md`)
for `/api/breakout/<ticker>` and all other endpoints not listed above.
