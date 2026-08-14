# API Contracts — Day 101 (July 29, 2026)

> Adds one new endpoint. Every endpoint documented in prior `API_CONTRACTS_DAY*.md`
> files is unchanged — including `GET /api/sectors/rotation`, whose internal RS-ratio
> calculation was refactored (extracted into a shared helper) but whose response shape
> and values are unchanged (verified via `test_sector_rotation.py` before/after).

---

## New — `GET /api/sectors/sub-industry`

### What it is
Sub-industry theme-cluster RS-ratio/momentum/quadrant — one level below the 11 broad
GICS sectors `/api/sectors/rotation` already covers (Semis, Memory/Storage,
Nuclear/Uranium, Gold Miners, Biotech, and 16 more, 21 total). Fills a real gap: the
broad-sector endpoint is too coarse to show a genuinely sector-specific move (e.g. a
semis-only selloff shows up there only as a soft "XLK: Weakening").

### Why
User request, built natively into STA after seeing the Trading Intelligence Hub's own
separate standalone version of this. Uses STA's own existing RS-ratio formula (shared
`compute_rs_ratio_and_quadrant()` helper, extracted from `get_sector_rotation()` this
session) rather than a second, differently-normalized implementation — the Hub's
version indexes to the start of the window; STA's indexes to the midpoint, so building
this natively (not just depending on the Hub's tool) avoids the "different
normalization epoch" caveat the Hub's report has to carry for overlapping tickers.

### Request

```
GET /api/sectors/sub-industry?period=6mo
```

`period` optional, defaults to `6mo` (matches the broad-sector endpoint's own default).

### Response shape

```json
{
  "clusters": [
    {
      "cluster": "Semis",
      "proxy": "SMH",
      "tickers": ["NVDA", "AMD", "MU", "MRVL", "AVGO", "..."],
      "rsRatio": 99.49,
      "rsMomentum": -8.46,
      "quadrant": "Lagging",
      "shortHistory": false,
      "usableDays": 126,
      "error": null
    },
    {
      "cluster": "Memory/Storage",
      "proxy": "DRAM",
      "tickers": ["WDC"],
      "rsRatio": 70.00,
      "rsMomentum": -7.77,
      "quadrant": "Lagging",
      "shortHistory": true,
      "usableDays": 81,
      "error": null
    }
  ],
  "clusterCount": 21,
  "noProxyClusters": [
    { "cluster": "Past survivors", "tickers": ["POET"] }
  ],
  "timestamp": "2026-07-29T14:32:10.123456",
  "period": "6mo"
}
```

- `shortHistory: true` whenever the aligned series is shorter than the full ~6mo
  target window (115 trading days) — flags a thinner-than-usual read (e.g. DRAM,
  launched Apr 2026) without ever rejecting it outright.
- A cluster whose proxy fetch fails (any provider, any reason) returns
  `rsRatio`/`rsMomentum`/`quadrant`/`shortHistory`/`usableDays` all `null` and a
  human-readable `error` string — never a partial row.
- `noProxyClusters` lists clusters with no defensible thematic ETF (currently just
  "Past survivors"/POET) — informational only, never scored.

### Backend internals
Uses STA's existing multi-provider orchestrator (`get_data_provider().get_ohlcv()`,
TwelveData → yfinance → Tradier) per ticker — 21 proxies + SPY, SPY fetched once and
shared across all clusters — rather than a single yfinance batch download like the
broad-sector endpoint, since several proxies (e.g. DRAM) aren't reliably on the
earlier provider tiers and need Tradier's fallback coverage. Cached per trading day
via the existing `cache_manager.get_cached_market('SUB_INDUSTRY_ROTATION')` /
`set_cached_market(...)` pattern.

**Known failure mode fixed before shipping (Golden Rule 40):** calling 22 tickers
per-request can trip TwelveData's rate limiter partway through; the yfinance fallback
for the remaining tickers returns a tz-aware index while an already-cached SPY series
(from an earlier TwelveData fetch) is tz-naive. Both series are now normalized to
tz-naive at the alignment boundary before `.index.intersection()` runs.

New file `backend/sub_industry_clusters.py` holds `SUB_INDUSTRY_CLUSTERS` (21 entries)
and `NO_PROXY_CLUSTERS` (1 entry) — transcribed from the Trading Intelligence Hub's own
hand-curated, Tradier-verified `ticker_themes.py`.

### Frontend
New `fetchSubIndustryRotation()` in `frontend/src/services/api.js` — returns the
parsed JSON directly (no whitelisted field reconstruction, unlike
`fetchSectorRotation()` — sidesteps the Golden Rule 30 trap deliberately). New
collapsible "🔬 Sub-Industry Watch" section in `SectorRotationTab.jsx`, Tier-2 style,
collapsed by default, lazy-loaded only on first expand (own component-local loading
state — nothing else in the app consumes this data, unlike `sectorRotation.mapping`,
which the Analyze page's sector badge reads).

---

## Unchanged — `GET /api/sectors/rotation`

Response shape, field names, and values are identical to `API_CONTRACTS_DAY*` prior
documentation. Internal refactor only: the RS-ratio/momentum/quadrant calculation
(previously inline) is now `compute_rs_ratio_and_quadrant()`, a shared helper called by
both this endpoint and the new one above. Verified behavior-preserving via
`test_sector_rotation.py` (9/9 checks, run before and after the refactor) and a live
browser check of the Analyze Stock page's sector badge (`sectorRotation.mapping`
lookup, consumed outside the Sectors tab).
