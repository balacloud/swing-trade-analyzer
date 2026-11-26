# API Contracts — Day 135

> Changes since `API_CONTRACTS_DAY129.md`. Backend v2.58 → v2.61. Plans: `ENV_OVERRIDE_PLAN_DAY135.md`, `STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md`.

## Changed — `GET /api/health`
- New field **`env_overridden`**: sorted list of environment variable NAMES (never values) where `backend/.env` replaced a different launch-environment value. Normally `[]`. Existing fields unchanged; consumers read only `status` and `providers`.

## Changed — `GET /api/stock/<ticker>` (backend v2.60)
- New field **`priceFreshness`**: `{newestDate, expectedDate, sessionsBehind, behindLevel ('PASS'|'WARN'|'FAIL'), servedFromStaleCache (bool), maybePartial (bool)}`. Built by `data_quality.price_freshness` from the frame the page uses (forming bar already dropped). `behindLevel` is the Data Sources tab's tolerant rule (3+ sessions behind WARN, 6+ FAIL); no new threshold. `servedFromStaleCache` is true only when the orchestrator served an expired saved copy because every source failed (the marker rides on the frame: `df.attrs['served_from']`, `df.attrs['cached_at']`). `maybePartial`: the saved copy was written before 16:30 ET on its own last bar's day. Existing fields unchanged. Frontend: `services/api.js` passes it through (`priceFreshness`), `utils/priceFreshness.js` writes the line, page check A16.
## Changed — `GET /api/stock/<ticker>` again (backend v2.61)
- New field **`dataNotes`**: `{integrity: {level, note, bars, since} | null, tracking: {reference, multiple, basis, twin, corr, beta, n, date} | null}`. `integrity` is the Data Sources tab's own integrity check (same builder, `data_quality.cached_quality`, raw cached frame) and appears only when WARN/FAIL; `bars`/`since` say which saved bars the percentage covers. `tracking` is the audit's stored C11 facts for a mapped leveraged fund (`data_quality.read_tracking`, hidden if the fund left `leveraged_underlyings.json` or its reference changed). Frontend: `api.js` passes it through, `utils/dataNotes.js` writes the lines (`data-note-integrity`, `data-note-tracking`), page check A17.
- `/api/provenance/<ticker>` `quality` block is now built by the same `data_quality.cached_quality` (identical keys).
- Audit (no API change): `data_audit_latest.json` ticker sections may carry a `tracking` object (no `level`), written by `audit_data_sources.py --update-reference`; `update_audit_reference(tracking=None)` leaves stored entries alone, a dict replaces and deletes. `leveraged_underlyings.json` gained `"twin": true` (SOXL.NE).
- Audit only (no API change): new check **C11** "tracks its underlying" (facts, level `NA`), `backend/reference/leveraged_underlyings.json`; the audit no longer grades Tradier for Tradier-blocked leveraged funds.
- Audit wording (no API change): the C5 big-move note in `data_audit_latest.json` (shown as the Data Sources tab's audit line) may now end `needs IBKR; NVDA x2 that day: +63.0%)` (`data_quality.annotate_jumps`, exact date, level unchanged).
