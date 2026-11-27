# API Contracts — Day 136

> Changes since `API_CONTRACTS_DAY135.md`. Backend v2.61 → v2.62. Plan: `DATA_SOURCES_PROVENANCE_PLAN_DAY136.md`.

## Changed — `GET /api/provenance/<ticker>` (backend v2.62)
- New block **`ohlcv.attempt`** and **`fundamentals.attempt`**: `{state: 'never'|'ok'|'failed', last_ok_ts, last_ok_provider, last_ok_detail, last_fail_ts, detail, served_stale (bool), period, error}`. Timestamps are epoch seconds. `state` is `failed` when the last failure is newer than the last success; `never` means this app has no record (a cache hit records nothing); `never` with `error` set means the record could not be read (state DB unreadable). `detail` holds provider names and exception CLASS names only (for example `alpaca:RateLimitError; yfinance:ProviderError`), at most 200 characters, never exception text (URLs can hold keys). Fundamentals `last_ok_detail` starts with `partial:` when some provider failed but data was obtained.
- Frozen keys (`ohlcv.source`, `rows`, `status`, and the rest) are unchanged. Old frontends ignore the new block.
- Storage: table `fetch_attempts(ticker, data_type, period, last_ok_ts, last_ok_provider, last_ok_detail, last_fail_ts, last_fail_detail, served_stale)`, one row per (ticker, data_type), in the shared `backend/data/provider_state.db`. Writes are best effort (0.5 s timeout); a failed write is logged and never breaks a fetch. Written by `providers/orchestrator.py` (OHLCV and fundamentals) and by the legacy direct-yfinance path in `/api/stock`.

## Changed — `GET /api/health`
- Provider rows: no change to the payload. The Data Sources tab now reads the existing `configured` flag to show "no key" instead of "ok" for a provider without an API key.

## Frontend / audit (no API change)
- `utils/dataSourcesView.js`: `describeAttempt`, `etTime`; `describeIdentity` returns `attempt` instead of `session`. `DataSourcesTab.jsx` shows `data-testid="ds-attempt"`. Page check A18.
- New: `backend/audit_data_sources_tab.py` (read-only statement audit of the tab), `frontend/scripts/test_data_sources_rare_states.js`, `dump_data_sources_tab.js`, `lib/readDataSourcesTab.js`.
