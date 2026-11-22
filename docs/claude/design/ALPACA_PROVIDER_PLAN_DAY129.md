# Alpaca as the first US price source (plan, Day 129), v2, Opus review applied (GO WITH CHANGES)

## Context
Twelve Data (primary US source) allows 8 calls a minute, so it runs out under load. Tradier, the last fallback, is not dividend-adjusted and has split errors on leveraged funds (NVDL, QPUX).
Alpaca's free plan (key in `backend/.env`) was tested read-only on 2026-11-21: 200 calls a minute, daily bars since 2016, 515 bars in one 0.3 s call. Against our saved Twelve Data and Yahoo data, whole-history close differences were within 0.04% for AAPL, JNJ, NEE, NVDL and QPUX (`adjustment=all`; no split error on NVDL or QPUX). Volume with `feed=sip` was x0.85 to x1.01 of Twelve Data. US only.
**Correction found by the review and verified by us in `backend/backend.log`:** the earlier "Twelve Data breaker opened about 82 times" understated and mixed two causes. The log has 315 `404 Client Error` lines: Twelve Data answers 404 for symbols it does not have (Canadian `.TO`/`.NE`, `^VIX`, `BRK-B`), `twelvedata_provider.py` has no 404 branch, so `raise_for_status()` raises and the generic `except` counts a breaker FAILURE (Golden Rule 36: a ticker-specific answer is not a health signal). Those false failures open the breaker for real US tickers too. Also verified: the log has 324 lines containing `apikey=`: **the Twelve Data API key is written to `backend.log`** (the file is gitignored, 11 MB, local only).

## Decision
Chain for US tickers: **Alpaca -> Twelve Data -> Yahoo -> Tradier**. Alpaca first (review: with the cache holding one source per frame, a fixed first source keeps each ticker's volume basis stable; Alpaca second would pick the source by how many of the 8 calls a minute are left). Canada unchanged (Yahoo). Tradier's leveraged-fund block unchanged; Alpaca serves leveraged funds.

## Changes
1. **New `backend/providers/coverage.py`**: one `is_us_symbol(ticker)` helper (Canadian suffixes `.TO .V .NE .NEO .CN`, `^` index symbols and empty are not US); reuse the suffix tuple of `live_quote.CANADIAN_SUFFIXES` (`live_quote.py:33`) and `audit_data_sources.is_ca` so there is one copy.
2. **New `backend/providers/alpaca_provider.py`** (template `tradier_provider.py`):
   - `name='alpaca'`; keys `ALPACA_API_KEY` / `ALPACA_SECRET_KEY`; `GET https://data.alpaca.markets/v2/stocks/bars`, `timeframe=1Day`, `adjustment=all`, **`feed=sip` hard-coded** (the `.env` has `ALPACA_DATA_FEED=iex`: never read it; fix its comment in `.env.example`; IEX volume is a different basis), `limit=10000`, `next_page_token` pagination, **never send `end`** (the default end is 15 minutes ago; an `end` inside the last 15 minutes returns 403 "subscription does not permit querying recent SIP data").
   - `start` from a per-period day table with a margin (like `PERIOD_TO_DAYS`: 2y ~ 740 days), then cut to Twelve Data's bar counts (`2y` 504, `1y` 252 ...), so the cache row-count gate passes.
   - Index: bar time converted to America/New_York, then **normalized to midnight, tz-naive** (a 04:00 left in place breaks every `.intersection` with other frames, Golden Rule 40).
   - Not covered (`DataNotFoundError`, no HTTP, no limiter token, no breaker): `not is_us_symbol`. Symbol map `BRK-B` -> `BRK.B` (verify with one call).
   - Error mapping (Golden Rules 36/65, each probed once with a real call before finalizing: good, unknown, malformed symbol): 401 and a plain 403 = `AuthenticationError` + breaker failure (loud log); **403 whose body mentions subscription/permit = loud `ProviderError`, no breaker failure** (our request-window bug, not a bad key); **400 and 422 = loud `ProviderError`, no breaker failure** (422 is undocumented); 200 with no bars for the symbol = `DataNotFoundError`; 429 = `RateLimitError` + breaker failure (log `X-RateLimit-*` headers if present); 5xx/timeout = `ProviderUnavailableError` + breaker failure; under 10 bars = `InsufficientDataError`. Error text never contains the request URL or headers.
   - Bars with zero volume are not emitted by Alpaca, so thin funds can miss whole sessions (no flat zero-volume bars): note it; the real-data check counts missing sessions.
3. **`providers/rate_limiter.py`**: `PROVIDER_LIMITS['alpaca'] = {'rate_per_minute': 150, 'daily_limit': 0}`.
4. **`providers/orchestrator.py`**: `self.alpaca`; `_ohlcv_chain = [alpaca, twelvedata, yfinance, tradier]`; startup print, docstrings, and `get_provider_status`: Alpaca `role: 'primary'` (OHLCV, US), Twelve Data becomes "fallback (OHLCV), primary (intraday)". Intraday and quote chains unchanged.
5. **Twelve Data fix (found by the review, same rollout)** in `twelvedata_provider.py`: (a) `is_us_symbol` check BEFORE `_check_availability` (no limiter token, no call for Canada or `^`); (b) HTTP 404 -> `DataNotFoundError`, no breaker failure; (c) map `-` to `.` (BRK-B -> BRK.B); (d) never put the request URL (it carries the key) in an error message or log line. Docstrings that say "primary" are updated.
6. **Cache rule for ALL sources (`cache_manager.set_cached_ohlcv`)**: if the newest bar's date is today in New York and the time is before 16:30 ET, `expires_at = min(expires_at, today 16:30 ET)` (use the `market_time` close constants). Reason: a fetch at 16:05 (Alpaca's data ends 15 minutes back, so it can miss the closing auction) would otherwise be cached until tomorrow 16:30 and served as a complete day after 16:30.
7. **Audit and tab**: `audit_data_sources.py` (fetch plan line ~192 adds Alpaca for US with a light sleep; `chain_sources`; docstring), `audit_vs_ibkr.py` (hard-coded source lists lines ~165, 186, 190), `frontend/src/utils/dataSourcesView.js` (`DISPLAY` gets `alpaca: 'Alpaca'`), `backend/reference/provider_coverage.json` (Alpaca: US works, Canada no; measured date in the note because the file has one shared `tested` date). `indicator_golden.py` is left alone (adding Alpaca there would move the golden snapshot).
8. **Rollout**: after deploy every cached US frame from Twelve Data or Yahoo shows an audit C8 WARN ("fell through") until it expires; clear the US OHLCV cache once at rollout (user's data, not code) or accept the temporary WARNs.
9. `run_all_checks.sh`: add `test_alpaca_provider`.

## Known unknowns / open items
- **In-session bar:** check on the next market day what Alpaca returns for today during the session; change 6 is the safety net, the check confirms it.
- **Terms of use (open, for the user):** no Alpaca-specific data terms found; the exchange agreements Alpaca points to limit non-professional use to personal, non-business use. Inside this local single-user app that looks consistent; do NOT publish Alpaca-sourced prices in shared Artifacts (Beginner Playbook, Status Board).
- **Extended-hours volume** may keep changing after 16:30 (forum posts, not docs): noted, not blocking.
- **Rotate the Twelve Data key?** It sits in a local gitignored log; that is the user's call. Change 5(d) stops new leaks; old lines stay in the log file.
- **Golden Rule 54 caller graph:** `backtest_adapter.download_ohlcv`, `mr_open_entry_retest.py`, `compare_sr_engines.py`, `backtest_adx_rsi_thresholds.py` read history through the orchestrator for 2y or less; a re-run reads Alpaca data (closes within 0.04%, volume x0.85-1.01), so a re-run can differ slightly from documented numbers (for example MR PF 1.50). Note in the docs.

## Tests (new `backend/test_alpaca_provider.py`, mocked `requests`, throwaway breaker/limiter state like `test_tradier_errors.py`)
- parse: lowercase columns, midnight tz-naive index, sorted, pagination joined, 04:00Z and 05:00Z stamps both give the right New York date, bars cut to 504; request carries `adjustment=all`, `feed=sip`, no `end`; `ALPACA_DATA_FEED=iex` in the environment is ignored.
- `BRK-B` mapped; Canadian symbol, `^VIX`, empty: no HTTP, no limiter token, no breaker failure.
- every error code above maps to the right exception and breaker effect; error text has no URL or key.
- chain with fake providers: Alpaca first; failure falls to Twelve Data; Canadian ticker never reaches Alpaca; leveraged block and 60 s failure memo still hold.
- Twelve Data: Canadian/`^VIX` make no call and take no token; HTTP 404 -> `DataNotFoundError`, no breaker failure; `BRK-B` sent as `BRK.B`; an error message never contains `apikey`.
- cache expiry: a frame with today's bar fetched at 16:05 and at 16:20 ET both expire at 16:30; a frame without today's bar, or fetched after 16:30, is unchanged.
- existing suites: `test_tradier_fallback_rule`, `test_tradier_errors`, `test_empty_price_row`, `test_price_basis`, `./run_all_checks.sh --quick`.

## Verify with real data
1. One real call each for a good, an unknown and a malformed symbol (Golden Rule 65), and `BRK.B`.
2. All US tickers of `backend/audit_universe.txt` once (about 1 minute at 200/min): at least 95% within 0.5% close difference over the last 20 sessions against Twelve Data and Yahoo, and also open/high/low, volume ratio and count of sessions missing against the others; every miss explained or listed.
3. After-close audit with Alpaca as a source; report under `docs/test/`.
4. Next market day in session: today's bar and the tab for 3 tickers; page checker `cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`.

## Rollback
Remove `self.alpaca` from `_ohlcv_chain` (one line). Missing or revoked keys already fall through to Twelve Data.

## Opus review, applied (verdict GO WITH CHANGES)
Checked by the reviewer against code and docs: Alpaca first is right; `end` must never be sent (403 on the last 15 minutes); 403 must be split by body; 422 is undocumented so it is not "not found"; daily timestamps are New York trading days (normalize); BRK.B works per an Alpaca forum answer (verify); Twelve Data's missing 404 branch and key-in-log leak (both verified by us in `backend.log`); the 16:00-16:30 cache hole; `audit_vs_ibkr.py` source lists and the Twelve Data `role` label were missing from the plan. All eleven changes applied above.
