# Data Sources tab: per-ticker provenance + statement audit + rare states (Day 136)

## Context
Last leg of the Data Sources tab (ROADMAP #20 merged with #16, user decision Day 135). Two gaps:
1. `/api/provenance/<ticker>` is built only from cache rows (`backend.py:939-1027`). A failed fetch leaves it identical to "never fetched". The orchestrator (`providers/orchestrator.py:186-227`) only `print`s failures; the only "just failed" signal is `df.attrs['served_from']` on one frame (not persisted, not on provenance).
2. Nobody has checked the tab's sentences against code, and no test renders the tab in rare states (provider down, breaker open, empty/stale cache, quota 0).

Outcome: the tab says one of "never fetched / last fetch OK / last fetch failed (when, which provider, class of error)", every sentence on the tab is graded PASS/WRONG/MISLEADING/UNVERIFIED, and rare states are rendered and checked.

## Part A. Attempt record (backend)
- New table `fetch_attempts(ticker, data_type, last_ok_ts, last_ok_provider, last_fail_ts, last_fail_detail, served_stale)`, one row per (ticker, data_type) via upsert (no growth). Lives in the shared `backend/data/provider_state.db` (same file as breaker/limiter, so launchd/CLI/server all write to it). Survives restarts and cache clears.
- New small module `backend/providers/attempt_log.py` (`record_ok`, `record_fail`, `read`). All writes best-effort: on any DB error, log loudly with ticker and continue; a logging failure must never break a fetch.
- Hook into the orchestrator at the exact points found: OHLCV success (line ~201), per-provider `ProviderError` (205-208), stale-cache exit (211-221), all-failed exit (223-227); same for fundamentals (~260-352). Quote/stock-info/earnings are NOT shown on the tab, so out of scope.
- Error detail stores provider name + exception class + HTTP status only, never `str(e)` (URLs may hold keys; Golden Rule 67, ENGINEER keys checklist).
- Cache hits record nothing (a cache hit is not a check). That is the point: "last_ok_ts" means a real provider answered.
- `/api/provenance` adds `ohlcv.attempt` and `fundamentals.attempt` = `{state: never|ok|failed, last_ok_ts, last_fail_ts, provider, detail, served_stale}`. FROZEN keys (`ohlcv.source/rows/status`) untouched; new keys only (Rule 57: check who enumerates keys; grep consumers first).
- Chain table: `get_provider_status` (`orchestrator.py:523-568`) "ok" for a never-called provider or a missing key is the same conflation at provider level. Add `configured` to the row and show "no key" / "not used yet" instead of a green "ok" (Rule 44: no single glyph for several reasons).

## Part B. Frontend
- `utils/dataSourcesView.js`: new pure `describeAttempt(provenance)`; `DataSourcesTab.jsx` shows one plain-facts line under Identity ("Last provider check: OK 2:14 pm from Alpaca" / "failed 2:14 pm (all providers), showing saved prices" / "never fetched by this app"). Facts only, no verdict words (Facts-not-Verdicts).
- Fix statement mismatches the audit finds (known candidates: static "cached until next close + 30 min" line vs Tradier 45-min and empty-newest-bar 30-min TTLs, `cache_manager.py:154-155`; "just fetched" is a guess from cache age <5 min).
- Update `test_data_sources_view.mjs` for the new states.

## Part C. Statement audit (extend the existing Statement Audit)
- Add the Data Sources tab to `backend/audit_statements.py` / `frontend/scripts/dump_page_statements.js` (their scope notes list it as NOT YET COVERED). Each of the ~25 strings in the explorer's table gets a verdict against code/data: cache label vs cache row, "Data from" vs `ohlcv_cache.source`, calls-left vs limiter counter, breaker dot vs forced breaker state, coverage chips vs `provider_coverage.json`, currency/exchange/class vs the reference lists. Acceptance (Round 2 plan 2.4): 0 WRONG; UNVERIFIED listed with why.

## Part D. Rare-state harness
- Extend the existing Puppeteer page checker (`ui-verify-checklist.js`, `lib/analyzeChecks.js` A11); no new dependency (repo has no Playwright). Request interception with planted payloads for `/api/health`, `/api/provenance`, `/api/cache/status`, `/api/data-sources/coverage`: provider down, breaker open, empty cache, stale/expired cache, fail-grade ticker, quota 0, attempt=failed, attempt=never, endpoint error (Retry button).
- Plus one REAL forced state with a throwaway state DB: trip a breaker, force a fetch failure on a fake ticker, check the tab. Never touch the live breaker file (ENGINEER testing checklist).
- New check A18 in `analyzeChecks.js` + `test_analyze_checks.mjs`.

## Tests
- `backend/test_attempt_log.py`: ok, fail, fail-then-ok, stale served, DB locked/missing (must not raise), no key text in detail, concurrency (two threads), orchestrator integration with fake providers + throwaway DB. Mutation check: disable the hook, expect failures.
- Node: view tests for each attempt state; checks test for A18.
- Edge: empty ticker, lowercase, `.TO`/`.NE`, ticker never seen.

## Process (Golden Rules 55, 64)
After approval: write this as `docs/claude/design/DATA_SOURCES_PROVENANCE_PLAN_DAY136.md`, get the Opus review (ask the user first per memory), apply its changes and tell the user; build in phases A -> B -> C -> D, one verifiable step at a time; `/three-pass`; `three_pass_check.sh --stamp ... --plan <file>`. Version bump (Backend v2.62, Frontend v4.70, app v4.74), update ROADMAP #16/#20, KNOWN_ISSUES (retire the High provenance item), API_CONTRACTS, status docs.

## Verification
1. `backend` unit tests + `run_all_checks.sh` green; mutation check fails as expected.
2. Real run: analyze one US ticker, one `.TO` ticker, force a failure (throwaway DB), read `/api/provenance` and the tab; compare with `backend.log`.
3. Page checker incl. A11/A18 passes; the rare-state screenshots reviewed by reading the DOM text, not just screenshots.
4. Statement audit report saved under `docs/test/`, 0 WRONG.

## Out of scope
Scan/Sectors/Context audits and the ~17 direct provider calls (priority 2), second Canada source (#30), Tradier retry (#23), quote/intraday attempt logging.

## Opus review
Verdict: GO WITH CHANGES

Reviewed Day 136 against the code. The direction is right. These changes are required before building:

1. **Wrong premise: `configured` is already there.** `get_provider_status` already returns `configured` for every provider (`orchestrator.py:544-597`). The gap is in the frontend only: `describeChains` row drops it (`dataSourcesView.js:137-149`), and `ChainRow` shows a green dot from `health` alone (`DataSourcesTab.jsx:119`). So it is a view change, not a backend change. "Not used yet" cannot come from this plan's table, which is keyed per (ticker, data_type). A breaker row with no failures also means "not used yet". Either add a per-provider `last_ok_ts`/`last_fail_ts` (a `provider` key row in the same table), or show only "no key" and leave "not used yet" out.
2. **Tests would write to the live DB (this blocks the build).** Three existing tests run the real `get_ohlcv` with fake providers on real symbols: `test_price_basis.py:69-79` (LOCKT), `test_tradier_fallback_rule.py:48-67` (**NVDL**, a user ticker, all failing) and `test_price_freshness.py:76-80` (**VFV.TO**, failing). With the hook in place, `run_all_checks.sh` would mark NVDL and VFV.TO "last fetch failed" in the live `provider_state.db`. Fix: `attempt_log` gets its own module `DB_PATH` plus `_initialized`, using the same pattern as `test_alpaca_provider.py:41`. Every test that touches the orchestrator must redirect it, or the hook must be a no-op unless enabled. Add a check that fails if any test writes the real path.
3. **The write must not slow a fetch.** The breaker and limiter use `sqlite3.connect(..., timeout=10)` with the default rollback journal and no WAL (`circuit_breaker.py:50-52`, `rate_limiter.py:41-43`). The hook runs inside the per-ticker lock (`orchestrator.py:164-166`). A busy DB (nightly launchd audit, `daily_job`, the Flask reloader child from `backend.py:4252 debug=True`) could hold an Analyze load for up to 10 s. `attempt_log` should use `timeout≈0.5` and catch `sqlite3.Error` plus everything else. It should log once per ticker and never raise. Do NOT switch the shared file to WAL in this plan: that changes breaker and limiter behavior.
4. **No HTTP status exists.** `ProviderError` carries only `provider`, `ticker` and a message (`exceptions.py:9-14`). yfinance puts the raw `str(e)` into the message (`yfinance_provider.py:94-96`). Store `provider` + `type(e).__name__` only. Never parse the status out of the message. Cap the all-failed detail (for example `alpaca:RateLimitError; yfinance:ProviderUnavailableError`).
5. **Missing exit paths in OHLCV:**
   - (a) Non-`ProviderError` exceptions escape the loop with no record. Examples: `set_cached_ohlcv` raising at `:199`, or a `None` df at `:195`. Use try/except around the loop body or an outer `finally`.
   - (b) The memo raise at `:180-183` makes no call. Record nothing there, and say so in the plan.
   - (c) The legacy direct-yfinance path writes a fresh cache with default source `'yfinance'` (`backend.py:1083-1098`, `cache_manager.py:300`). The attempt would then say "failed" while the cache is fresh. Record ok from that path, or name it in the tab line.
   - (d) A successful fetch later must clear `served_stale`.
6. **Fundamentals has no single failure loop.** The plan says "same for fundamentals". It actually has three separate try blocks, and success can be partial (`orchestrator.py:279-325`). All-empty returns `None` or stale without raising (`:328-335`). Define what counts: ok = merged has data (provider = `primary_source`), failed = all None. Per-provider errors go in the detail even on ok. Note that `/api/fundamentals` retries once (`backend.py:1263-1269`), so the second call overwrites the first.
7. **Same fact, three lines (Golden Rule 59 / less text).** `describeIdentity` already shows `session` from the in-process `_last_source` (`dataSourcesView.js:63-67`, `backend.py:976-981`). The new attempt line would repeat it, and could disagree with it, since attempts are cross-process. "Data from" (cache source) is the third line. Replace the `session` line with the attempt line rather than adding one. The header freshness dots (`App.jsx:1044-1062`, `/api/data/freshness` `backend.py:809`) are another copy of the same fact. List them as out of scope by name.
8. **The audit reads `prov['ohlcv']` whole** (`audit_data_sources.py:419-421`). Today it writes only source/rows/status (`:381`), but the new nested `attempt` would be copied into the saved claims JSON. Check that this is harmless. Checks A11 and A16/A17 read `ohlcv.source` only (`analyzeChecks.js:263`), so they are fine.
9. **Phase order.** B fixes "the mismatches the audit finds" before C runs the audit. Use this order: A, then C (grade a baseline), then B, then D, then C again (0 WRONG).
10. **Rare-state harness.** `ui-verify-checklist.js` has no request interception today (`:220`, `:328`). Put it behind a separate flag and page, so the real-data checks A1-A17 never see planted payloads. Every intercepted request must be continued, or the page hangs. For the "REAL forced state", a second server needs env-configurable `DB_PATH`s and a port, because 5001 is hard-coded (`backend.py:4252`) and the cache path is fixed (`cache_manager.py:24`). Use the Flask `test_client` with both DB paths redirected instead.
11. **A18 wiring.** Add A18 to `CHECK_IDS` and the labels (`analyzeChecks.js:23-39`). Update the count comment (15 -> 16) and `test_analyze_checks.mjs`.
12. **Time display.** Store epoch UTC. Show the time in ET with the date when it is not today. Store `period` in the row, because a 1y MR-scan success is not a 2y fetch.
13. **Stamp.** `three_pass_check.sh:50` accepts this verdict line. `backend/data/` is ignored by the gate (`:23`), so a test DB placed there is safe.

## Changes applied after the Opus review (Day 136)
1. `configured` already exists in `get_provider_status`; the gap is frontend only (`describeChains` drops it, `ChainRow` colours from `health`). Show "no key" for an unconfigured provider. Drop the "not used yet" idea (the table is per ticker, not per provider).
2. `attempt_log` gets its own patchable `DB_PATH` and `_initialized`. Every orchestrator test (`test_price_basis`, `test_tradier_fallback_rule`, `test_price_freshness`) redirects it to a temp DB. A guard test fails if any test writes the real path.
3. Writes use a ~0.5 s SQLite timeout, catch everything, never raise. No WAL change to the shared file.
4. Detail = provider name + exception class name, length-capped. No HTTP status, never `str(e)`.
5. Also cover: non-`ProviderError` exits (cache write failing, None df), the repeat-memo raise records nothing (stated), the legacy direct-yfinance path in `backend.py` (~1083-1098) is documented as not recorded, a later success clears `served_stale`.
6. Fundamentals: define ok / failed / partial from the three try blocks and the all-empty return; note the double call in `/api/fundamentals`.
7. Replace the existing `session` line with the attempt line (one fact, one place; Rule 59). Header freshness dots are out of scope.
8. `audit_data_sources.py` copies `prov['ohlcv']` whole; check the nested `attempt` is harmless.
9. Phase order: A, then C (baseline grades), then B, then D, then C again (0 WRONG).
10. Rare-state harness: separate flag and page, interception never touches A1-A17, every intercepted request is continued. Real forced state uses the Flask `test_client` with both DB paths redirected (not the live server).
11. A18 added to `CHECK_IDS` and labels in `analyzeChecks.js`; count comment and `test_analyze_checks.mjs` updated.
12. Store epoch UTC plus `period`; show time in ET with the date when not today.
