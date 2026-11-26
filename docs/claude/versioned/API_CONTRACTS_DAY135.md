# API Contracts — Day 135

> Changes since `API_CONTRACTS_DAY129.md`. Backend v2.58 → v2.60. Plans: `ENV_OVERRIDE_PLAN_DAY135.md`, `STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md`.

## Changed — `GET /api/health`
- New field **`env_overridden`**: sorted list of environment variable NAMES (never values) where `backend/.env` replaced a different launch-environment value. Normally `[]`. Existing fields unchanged; consumers read only `status` and `providers`.

## Changed — `GET /api/stock/<ticker>` (backend v2.60)
- New field **`priceFreshness`**: `{newestDate, expectedDate, sessionsBehind, behindLevel ('PASS'|'WARN'|'FAIL'), servedFromStaleCache (bool), maybePartial (bool)}`. Built by `data_quality.price_freshness` from the frame the page uses (forming bar already dropped). `behindLevel` is the Data Sources tab's tolerant rule (3+ sessions behind WARN, 6+ FAIL); no new threshold. `servedFromStaleCache` is true only when the orchestrator served an expired saved copy because every source failed (the marker rides on the frame: `df.attrs['served_from']`, `df.attrs['cached_at']`). `maybePartial`: the saved copy was written before 16:30 ET on its own last bar's day. Existing fields unchanged. Frontend: `services/api.js` passes it through (`priceFreshness`), `utils/priceFreshness.js` writes the line, page check A16.
- Audit only (no API change): new check **C11** "tracks its underlying" (facts, level `NA`), `backend/reference/leveraged_underlyings.json`; the audit no longer grades Tradier for Tradier-blocked leveraged funds.
