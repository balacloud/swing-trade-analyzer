# API Contracts — Day 128

> Changes since `API_CONTRACTS_DAY127.md`. Backend v2.56 → v2.57. Plans: `docs/claude/design/EMPTY_PRICE_ROW_PLAN_DAY127.md`,
> `TRADIER_ERROR_HANDLING_PLAN_DAY127.md`.

## Changed — price frames served to every route (`/api/stock`, `/api/sr`, `/api/patterns`, `/api/breakout`, `/api/market/spy`, `/api/market/index/<t>`, `/api/mr/*`, `/api/quote`)
- Rows whose **close price is empty (NaN)** are removed when a frame is served (`market_time.drop_empty_close`, applied in `orchestrator._deliver` and `split_adjust.fix_frame`). The cache itself stays raw.
  Effect: when Yahoo sends an empty newest bar, every price, date, change and volume on the page is that of the last bar that HAS a price (the date shown says which). `/api/sr` never sends `NaN` for `currentPrice` / `change` from this cause.

## Changed — `GET /api/stock/<ticker>`
- Answers **404** `{"error": "No usable price data for <ticker>"}` when no bar has a close price. It used to fall back to a `currentPrice` of **0**. (In practice the earlier "no completed trading day yet" 404 answers first.)

## Changed — `GET /api/provenance/<ticker>` (Data Sources tab quality block)
- `quality` facts gain **`newest_close_missing`** (bool). `last_date` is now the last bar WITH a close price (it used to be the last row, even an empty one), so `sessions_behind` counts an empty newest bar as behind.
- `quality.checks.integrity.level` is **FAIL** when `newest_close_missing` is true; its `note` says "the NEWEST bar has no price (the app skips it when serving)". A frame with no price in any row gives `state: 'error'`, reason "no row has a close price".
- `data_quality.level_integrity(...)` takes an optional 5th argument `newest_close_missing` (default False; old 4-argument calls unchanged).

## Changed — cache expiry (internal)
- `cache_manager.set_cached_ohlcv`: a frame whose newest close is empty is cached for at most `EMPTY_NEWEST_BAR_TTL_MIN` = 30 minutes (other frames: unchanged, next close + 30 min; Tradier: 45 min).

## Changed — Tradier provider error contract (internal)
- HTTP 400 with "symbol not found" -> `DataNotFoundError` (no breaker failure); 400 with "quota" or `X-Ratelimit-Available: 0` -> `RateLimitError` (+ breaker failure); any other 400 -> `ProviderError` (no breaker failure, printed loudly);
  empty or `^`-only symbol -> `DataNotFoundError` with no request. 429/401/403/5xx and timeouts unchanged. Effect on `/api/quote`: a Tradier "not found" counts toward "no live price for this ticker".

## Changed — page checker (not an API)
- `frontend/scripts/lib/analyzeChecks.js`: new check **A14** (price answers are valid JSON with a real price); 11 -> 12 checks per ticker.

Nothing else changed shape.
