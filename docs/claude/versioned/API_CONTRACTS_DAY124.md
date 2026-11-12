# API Contracts — Day 124

> Changes since `API_CONTRACTS_DAY123.md`. All additive except the `/api/market/vix`
> `regime` value, which now comes from one shared band table (same words, `low_volatility`
> boundary unchanged). No field removed.

---

## New — `GET /api/market/index/<ticker>` (Analyze Redesign Step 7)

Trend facts for one market index, for the Analyze page's Market backdrop card.

- `ticker` must be in `MARKET_INDEX_TICKERS = {'SPY', 'QQQ'}`; anything else → `400 {error}`.
- No data → `404 {error}`. Exception → `500 {error}` (logged).
- `200`: `{ ticker, trend }` where `trend` is `index_trend_facts()` (below) or `null`.
- History: `_index_history()` (provider chain → yfinance fallback), shared with `/api/market/spy`.
- Frontend: `fetchIndexTrend(ticker)` throws on non-ok with the body's error; the Analyze
  page calls it for QQQ only and isolates a failure to the QQQ row.

### `trend` object (`backend/index_trend.py` `index_trend_facts`)
Computed on **completed** daily bars only (`market_time.drop_forming_bar`, 16:30 ET cutoff).

| Field | Type | Meaning |
|---|---|---|
| `asOfDate` | `YYYY-MM-DD` | Last completed bar |
| `close` | number | That bar's close |
| `sma50`, `sma200` | number \| null | 2 dp; null with too little history |
| `aboveSma50`, `aboveSma200` | bool \| null | |
| `pctVsSma50`, `pctVsSma200` | number \| null | % above/below, 1 dp |
| `biggestDrop10d` | `{date, pct}` \| `{noDownDay: true}` \| null | Largest 1-day fall in the last 10 sessions (ties → most recent); null if no known change |
| `biggestDrop10dSince` | `YYYY-MM-DD` \| null | Last earlier day with a bigger fall, searching the whole frame |
| `searchedFrom` | `YYYY-MM-DD` | First date searched (so "largest since" is stated from data, never assumed) |
| `nanCloses` | int | NaN closes in the frame (logged); a NaN gap never creates a fake drop |

## Changed — `GET /api/market/spy` (additive)
- New `trend` field: same object as above, or `null` if the calculation fails (logged via
  `_safe_trend_facts`; the legacy fields still return).
- Legacy fields unchanged. History now from the shared `_index_history('SPY')`.
- Note: the Context tab's market phase reads SPY separately (`/api/market/phase`).

## Changed — `GET /api/market/vix`
- `regime` now comes from `backend/vix_bands.py` `vix_band()`: `<15 low_volatility`,
  `<20 normal`, `<25 elevated`, `<30 high`, else `extreme`; `null` for a missing/NaN value.
  Same boundaries as the old inline ladder, now one place.
- These are **display** bands. The engine's `assessRiskMacro` (20/30, parity-tested) and the
  phase grid's `_vix_bucket` (20/25) are deliberately separate.

## Changed — `GET /api/market/phase` (additive)
- `signals.vix.band`: the same `vix_band()` value. `signals.vix.levelBucket` is kept (it is
  the phase grid's input). The Context banner shows the band word ("normal range"), not "calm".

## Changed — `GET /api/paper-trading/status` (additive)
- `systems.mr.openBasis` and `systems.mrHub.openBasis`: the next-open re-test for that track,
  from `mean_reversion.get_mr_track_record()` (same source as the Analyze page's MR card):
  `{ trades, winPct, profitFactor, avgPnlPct, source }`, or `null` when the re-test is
  unavailable. The ledger's own figures are priced at the entry-day close (Golden Rule 60).

## Unchanged shape, now displayed — `GET /api/stock/<ticker>`
- `newestDate` (already returned, already passed through by `fetchStockData`) now labels the
  Analyze header price: "Nov 11 close", or "intraday, not a close" for a bar dated today before
  16:30 ET. The route does **not** drop the forming bar itself.
- `quoteType` drives the classification line ("Exchange-traded fund (ETF)").

## Frontend-only (no API change)
- `positionSizing.calculatePositionSize` result gains `vixUnknown` (bool).
- `getVixPositionMultiplier`: non-finite VIX → `{1.0, isDefault: true}`.
- `scoringEngine.calculateScore` result no longer has `qualityGates`.
