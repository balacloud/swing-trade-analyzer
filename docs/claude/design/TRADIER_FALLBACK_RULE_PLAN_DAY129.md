# Tradier fallback rule + tab explanation (plan, Day 129), v2, Opus review applied (GO WITH CHANGES)

## Context (corrected by the Opus review; numbers checked against `data_audit_20261119_pm.json`)
The after-close audit (`docs/test/DataSources_20261119_pm/REPORT.md`) graded Tradier for the first time:
- NVDL: a +191% one-day step (2026-06-25) only in Tradier = split error. QPUX: -69% on 2026-03-20, Tradier only.
- 21 tickers have malformed bars in Tradier's data; 5 of them (JNJ, NEE, SO, DUK, PLD) FAIL the integrity check (the other 3 integrity FAILs are Yahoo-served Canadian tickers). Tradier is split-adjusted but NOT dividend-adjusted (tradier_provider.py docstring). That the bad bars fall on dividend dates is INFERRED (the two examples looked at), not measured.
- The tab ALREADY warns on some of these (NEE, DUK integrity FAIL; NVDL, QPUX jumps WARN) and already says "Data from Tradier". What it lacks is the REASON (backup source, not dividend-adjusted, split errors). Audit C8's "the tab shows no warning" text is wrong: C8 never reads the tab's quality result (`tab_claim` returns only `ohlcv`).
- Twelve Data and Yahoo agree within 1% over the last 20 completed sessions (C9 window).
- Tradier IS called for .TO/.NE tickers too (no Canadian handling in tradier_provider.py); only the audit script skips it for Canada.

## Decision (agreed with the user)
1. Plain US stocks and ETFs: Twelve Data -> Yahoo -> Tradier (Tradier last resort).
2. Leveraged funds never use Tradier. If Twelve Data and Yahoo both fail, serve the saved copy (marked stale); if there is none, a clear error. Cost, stated plainly: the cache keeps ONE row per ticker, so a leveraged fund whose current row came from Tradier (12 of 19 US ones at the PM run) has no price until Twelve Data or Yahoo succeeds. A visible error is better than a 3x-wrong price (NVDL's +191% step falls inside the 260 bars Analyze uses).
3. The Data Sources tab explains when the saved prices came from Tradier.

## Changes
1. New `backend/providers/fallback_policy.py`: a Python constant `NO_TRADIER` (dict ticker -> reason), no JSON file (nothing to fail to read; the review showed a JSON "safety net" depends on the same file). Contents: AAPU, AMZU, AVGC, BRKU, COPZ, COTG, ELIL, GGLL, METU, MSFU, NFXL, NVDL, SOXL, TSLL, URAA, QPUX, DRAL, SPCL, UBOT, SOXL.NE, GDXU.TO, plus plain GDXU (a user may type it without the suffix). Helper `tradier_blocked(ticker)`.
2. `orchestrator._get_ohlcv_locked`: skip Tradier for a blocked ticker (one log line). `_get_stale_ohlcv`: refuse a stale copy whose meta source is `tradier` for a blocked ticker (a non-Tradier stale copy of any age is still served). No change to `get_cached_ohlcv` (the review: existing Tradier entries expire in 45 min, `TRADIER_OHLCV_TTL_MIN`, and no new ones are written, so a read-time "miss" rule is not needed).
3. Failure memo: for a blocked ticker, after the whole chain fails, raise the same error immediately for 60 seconds (in memory, per ticker). Reason: without a Tradier fill, the ~5 Analyze routes waiting on the per-ticker lock would each re-run Twelve Data and Yahoo and burn the 8 calls a minute.
4. `data_quality.quality_level(facts, tolerant=True, source=None, blocked=False)`: add a `source` check ONLY when `source == 'tradier'` (no PASS row for other sources, so "all checks passed" counts stay as they are): WARN, note worded as a fact with small impact: "Served by Tradier, the backup source. Prices are not adjusted for dividends, so older prices can sit a little above the other sources; a few bars may be malformed." With `blocked=True`: FAIL "Tradier has split errors on this fund; the app should not serve it." `/api/provenance` passes `_meta['source']` and `tradier_blocked(ticker)`. The frontend lists every WARN/FAIL check already; add the label "Data source" to `CHECK_LABEL` in `dataSourcesView.js`.
5. `audit_data_sources.py` C8: read `/api/provenance` `quality.checks` (today only `ohlcv`), grade the tab on what it really shows (a Tradier-served ticker with no `source` check = FAIL), and drop the wrong "the tab shows no warning" wording.

## Out of scope
Live quote (display-only, Tradier first); NaN-to-null API issue (#24); Twelve Data pressure (#22); Tradier stall retry (#23).

## Tests (new `backend/test_tradier_fallback_rule.py`, isolated cache DB, fake providers like `test_empty_price_row.py` / `test_price_basis.py`)
- Blocked ticker, Twelve Data and Yahoo fail: Tradier fake gets 0 calls; stale non-Tradier copy served; stale Tradier copy refused; no copy = clear error.
- Plain ticker, both fail: Tradier IS called.
- Failure memo: second request within 60 s makes no provider calls; after 60 s (patched clock) it retries.
- `quality_level`: Tradier WARN; Tradier + blocked FAIL; other sources and `None` add no check; old callers (`test_data_quality.py:46` all-PASS) unchanged.
- Drift test: every leveraged ticker in the audit's hand-labelled list and every "Leveraged ETF" from `classify_instrument` over `instrument_class_cache.json` is in `NO_TRADIER`.
- C8 test: Tradier-served ticker whose tab payload lacks the `source` check fails; with it, passes.
- Also run the 61 Tradier-error tests, the 44 empty-row tests, `frontend/scripts/test_data_sources_view.mjs`, `./run_all_checks.sh --quick`.

## Verify with real data
Throwaway cache DB (never the live one): force JNJ and NVDL rows to source `tradier`, call `/api/provenance/JNJ` and `/NVDL`, confirm WARN / FAIL text; then the page checker `cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`.

## Opus review, applied (verdict GO WITH CHANGES)
Checked by the reviewer against code and audit data: a curated list is right (the name classifier finds only 15 of the leveraged funds; QPUX, DRAL, SPCL, UBOT are hand-labelled); GDXU.TO was missing; no price-history caller depends on Tradier serving these funds (live_quote handles errors); a JSON-based safety net was circular; the cached-Tradier-miss rule was unnecessary; the repeated-call risk was real; Context numbers corrected as above; C8 needed a change. All seven changes applied above.
