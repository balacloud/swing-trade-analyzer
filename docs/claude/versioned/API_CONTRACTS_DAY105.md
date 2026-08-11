# API Contracts — Day 105 (August 11, 2026)

> Adds one new endpoint. Every endpoint documented in prior `API_CONTRACTS_DAY*.md`
> files is unchanged.

---

## New — `GET /api/sectors/sub-industry-pullback-screen`

### What it is
The SRPS pullback screener (Day 103's `/api/sectors/pullback-screen`), applied to
the 21 Sub-Industry Watch theme clusters (Day 100+) instead of the 11 broad GICS
sectors. Same Rules 1/3/4/6, shared via `_srps_true_rs()`/`_srps_evaluate_candidate()`
(new module-level helpers in `backend.py`, extracted from the sector-level endpoint —
Golden Rule 21, not a second implementation). **Not a forward-test track.** Unlike
its sector-level sibling, this sub-industry universe has **not been separately
backtested at all** — it applies the already-failed mechanical rule set to a finer,
entirely untested universe. The response's own `disclaimer` field says this
explicitly.

### Why
User-requested extension, after citing positive discretionary experience with the
sector-level screener. Confirmed with the user before building (via `AskUserQuestion`)
how to handle two things the sub-industry universe forces that the sector-level
version didn't: overlapping clusters that duplicate broad-sector coverage (included
anyway), and proxy-only clusters with no underlying stock list (screened on the proxy
ETF itself rather than skipped).

### Request

```
GET /api/sectors/sub-industry-pullback-screen
```

No query parameters. Fixed 1-year OHLCV lookback, fixed rule thresholds
(`backend/srps_constants.py`, shared with the sector-level screener).

### Response shape

```json
{
  "regimeOk": true,
  "regimeMessage": "SPY above 200-SMA — Rule 1 regime gate open",
  "spyClose": 773.03,
  "spySma200": 703.48,
  "improvingClusterCount": 8,
  "clustersCappedFrom": 9,
  "clusters": [
    {
      "cluster": "AI Infra/Power",
      "proxy": "GRID",
      "quadrant": "Improving",
      "error": null,
      "candidates": [
        {
          "ticker": "GEV",
          "rsRatio": 0.909,
          "price": 990.85,
          "stopPrice": 934.98,
          "targetPrice": 1130.54,
          "riskPct": 5.64,
          "volumeVsAvg20d": 0.57,
          "daysUntilEarnings": null,
          "earningsWarning": null
        }
      ]
    }
  ],
  "disclaimer": "Informational screen only — this applies the same SRPS mechanical rule set that already FAILED its own pre-registered backtest at the broad-sector level (34.1% win rate, PF 1.177, both below the required minimum) to a finer sub-industry universe that has NOT been separately backtested at all. This is not a buy signal and not an automated forward-test track. Apply your own judgment (regime, news, catalysts) before acting on anything shown here.",
  "timestamp": "2026-08-11T10:15:22.104883"
}
```

### Field notes

- Same shape as `/api/sectors/pullback-screen`, with `sectors`/`etf`/`sector` renamed
  to `clusters`/`proxy`/`cluster` and `sectorsCappedFrom` renamed to
  `clustersCappedFrom` — otherwise identical field semantics (see
  `API_CONTRACTS_DAY103.md` for the shared candidate-object fields).
- `clusters` — only clusters currently in the `Improving` quadrant (per
  `/api/sectors/sub-industry`'s own classification), capped to the top 8 by RS ratio
  (`MAX_CLUSTERS_PER_REQUEST`). `clustersCappedFrom` is the true pre-cap count when
  truncation happened, `null` otherwise.
- Candidate sourcing differs from the sector-level version: no TradingView scanner
  field exists to query a thematic cluster the way `build_sector_query()` queries a
  real GICS sector, so this reuses each cluster's own hand-curated `tickers` list from
  `sub_industry_clusters.py` (previously documented there as informational-only — this
  is the first thing that actually queries them), capped at 8 tickers per cluster
  (`LIVE_CANDIDATE_LIMIT`, same Golden Rule 25/40 fan-out reasoning as the cluster cap,
  applied one level deeper — Semis alone has 16 curated tickers). Clusters with an
  empty curated list (Gold Miners/GDX, Biotech/XBI — the proxy ETF IS the theme) use
  `[proxy]` as the sole candidate rather than being silently skipped.
- Cached per trading day, same convention as the sector-level screener (SQLite
  `market_cache`, key `SRPS_SUB_INDUSTRY_PULLBACK_SCREEN`).

### Errors

Same error shape as `/api/sectors/pullback-screen`: `503` (data provider
unavailable), `500` (SPY fetch failed / insufficient history), per-cluster failures
isolated to that cluster's own `error` field rather than failing the whole request.

---

## Also changed (no contract shape change)

`GET /api/sectors/pullback-screen`'s response is unchanged in shape, but its
implementation now calls the same shared `_srps_true_rs()`/`_srps_evaluate_candidate()`
helpers as the new endpoint above — verified behavior-preserving (identical output
before/after the refactor) via live curl comparison, not just code review.
