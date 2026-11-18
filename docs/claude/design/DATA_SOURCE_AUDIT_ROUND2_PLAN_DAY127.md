# Data Source Audit, Round 2 (plan, Day 127)

Status: PLAN v2 (Opus review applied, see section 7), not built. Waiting for the user's "go".
Why now: the Statement Audit (Framework Part 7) recomputes every number from the SAME bars the page received, so it proves the maths and the words, not the data (S4 stays UNVERIFIED). If a source hands us a wrong close, the page and the audit agree and show PASS. The user asked (Day 127) to audit the sources BEFORE the 117-ticker page audit is trusted.

## 0. What already exists (so we do not redo it)
- Round 1 (Day 126, `DATA_SOURCE_TESTING_PLAN_DAY126.md`): `backtest/audit_data_sources.py` (truth-free C2, C4-C6, C8, C9) and `backtest/audit_vs_ibkr.py` (IBKR truth C1, C3, C5, C7) on **24 tickers**. Result: 22 clean on every source; SOXL.NE (Yahoo/EODHD unadjusted 3:1 split) and QPUX on Tradier (reverse split x3) fail.
- Data Sources tab v2 (Day 126): per-ticker quality panel from `data_quality.py`, side-effect-free cache readers, `reference/provider_coverage.json`, page check A11.
- Live quote (`live_quote._chain`): **already Tradier first for US**, Yahoo then Finnhub; Canada Yahoo only.
- OHLCV chain: Twelve Data (`adjust=all`, dividend-adjusted) -> Yahoo -> Tradier -> stale cache. Tradier served ~34% of logged fetches (3,897 of ~11,400; Yahoo 52%, Twelve Data 14%; whole-life `backend.log`, to be re-measured per ticker, 2.2), so it is NOT a rare fallback; it is split-adjusted but NOT dividend-adjusted and has the reverse-split bug.

## 1. What is NOT done (this plan)
1. Only 24 of the 117 universe tickers have ever been compared to a second source.
2. No inventory of what the app FETCHES versus what it COMPUTES. Anything derivable from OHLCV should be computed, so there is one source to audit.
3. Tradier appears as 37% of history fetches with a known basis difference and a known reverse-split bug, and nothing guards a one-day move over 40%.
4. The Data Sources tab's own statements (source shown, calls left, breaker state, cached rows, coverage map) have not been audited against reality, and its rare states only have planted-payload tests.
5. The Master Audit Framework only points at "the data-source audit (C3/C9)"; the real plan lives in two design docs.

## 2. Work items

### 2.1 Fetched-versus-computed inventory (read-only, no app change)
For every `/api/*` route and card, list each input as FETCHED (which provider chain) or COMPUTED (from which bars). Method: grep the provider calls in `backend.py`/`orchestrator.py` plus a per-card read. Output a table in `docs/test/DataSources_<date>/INVENTORY.md`.
Known fetched: daily OHLCV, live quote, VIX quote, fundamentals (Finnhub -> Alpha Vantage -> Yahoo field-merge), stock info and earnings date (Yahoo only), intraday 4H (Twelve Data -> Yahoo).
Known computed: SMAs, RSI, ADX, ATR, OBV, S/R zones, trade plan, RS, trend checks, breakout.
Already computed from bars (Yahoo `info` is only the short-history fallback): 52-week high/low (`backend.py:1138-1150`) and the 52-week-ago price. Candidates still FETCHED that bars could give: `avgVolume` and `avgVolume10d` (`backend.py:1214-1215`, liquidity row). Decide from the table, not assumed.
Acceptance: every number on the Analyze page is labelled FETCHED or COMPUTED, and each FETCHED one names its single owner source or its chain.

### 2.2 Tradier routing decision
First find the cause of the Tradier/Yahoo share: likely Twelve Data's 8-per-minute limit hit by parallel page loads (the nightly run uses two browsers, `nightly_audit.sh:29-34`). If so the fix is spacing the calls, not rerouting. Measure per ticker from `ohlcv_cache.source` for the 117. (the user asked "Tradier first for US")
Facts: Tradier is fast (0.2 s, 120 req/min), clean on US stocks/ETFs, volume within 0.1-2% of Yahoo; but split-adjusted only (not dividend-adjusted, so SMAs and 52-week figures shift for dividend payers, the exact mismatch Day 126 fixed), and a 1:3 reverse split is wrong.
- **Live quote:** already Tradier first for US. No change.
- **Daily history, option A (recommended): keep Twelve Data -> Yahoo -> Tradier**, and make the Tradier leg safe: (i) put QPUX and any other leveraged reverse split into `reference/known_splits.json` (the existing mechanism; it only has SOXL.NE today), and FLAG, never refuse, a one-day move over 40% that sources disagree on (real leveraged moves of that size exist, e.g. SOXL +50% on 2025-04-09); (ii) derive the basis from the cache's existing `source` field in `data_quality` and show it on the tab, no cache-schema change; (iii) measure how often Tradier serves history for the 117 and how many tickers then show a dividend-basis shift.
- **Daily history, option B: Tradier first for US.** Only if we add a dividend adjustment (needs a dividends feed; Tradier's corporate-actions endpoint is beta, untested) AND the reverse-split guard. More moving parts, and it changes the price basis of every cached US ticker. Not recommended until A's measurement shows the basis shift is material.
Decision point for the user after the measurement in 2.3. Nothing is rerouted by this plan.

### 2.3 Run the audits on the full universe (117)
0. **Prerequisite:** both audit scripts hard-code 24 tickers (`audit_data_sources.py:60-72`, `audit_vs_ibkr.py:39-44`) and `audit_vs_ibkr.py` has no `--truth` option, and any other ticker gets class `'?'` which crashes the report sort. Add `--tickers-file backend/audit_universe.txt` to both and take the class from `data_quality.classify_instrument`; keep the single keyed truth JSON `ibkr_truth_<date>.json`.
1. Truth-free: `audit_data_sources.py` on all 117 (C2, C4-C6, C8, C9). Cached on disk, so a re-run is free. Budget (Golden Rule 25): Twelve Data ~800/day free, so US tickers already cached cost nothing; EODHD 20/day only for Canada, split over days; Alpha Vantage Toronto only.
2. IBKR truth, scoped honestly: round 1 took 47 calls for 24 tickers, so 117 is ~230 calls, 8+ minutes of rate limit and 1-2 hours of conversation. So: first list which of the 117 have a contract id on the user's watchlists (Golden Rule 58; some, e.g. NVDL, AAPU, ELIL, COTG, AVGC, PNG.V, FINN.NE, CARS.TO, may not); ask the user to add the missing ones or mark them UNVERIFIED. Take truth for every leveraged, .NE, .V, CDR and split-flagged ticker plus ~20 plain ones; plain large caps where three sources agree within 0.3% rest on C9. Show exchange and currency on every row (same base symbol exists on several markets: SOXL/SOXL.NE, GEV/GEV.TO, AMD/AMD.TO, AVGO/AVGO.TO). Written to the existing `ibkr_truth_<date>.json`; then `audit_vs_ibkr.py` for C1, C3, C5, C7. Volume is checked for plausibility only (IBKR is 1.15-3x different by class; never mix sources).
3. Class matrix (US stock, US ETF, leveraged, Canadian .TO, CDR .TO, .NE) x source -> works/partial/no, written to `reference/data_audit_latest.json`.
4. Tradier measurement from 2.2: share of history fetches served, per-ticker dividend-basis gap, reverse-split exposure.

### 2.4 Data Sources tab audit (statements against reality)
For every claim the tab makes, recompute it from the source of truth:
- "Served by X" vs the orchestrator's own log for that fetch (C8).
- Rows, first/last bar, flat % vs the cache file read directly.
- "Calls left" (Twelve Data, Alpha Vantage) vs the provider counter.
- Circuit-breaker state vs a forced failure.
- Coverage map vs `provider_coverage.json` and the live chain (Stooq shown as disabled, Tradier present, EODHD "not in chain").
- Currency/exchange/class vs IBKR contract data.
Rare-state browser tests (Playwright, planted payloads): provider down, breaker open, empty cache, stale cache, fail-grade ticker (A11 already pins SOXL.NE), quota 0. Each state's text is asserted, not just "renders".
Verdicts use the Statement Audit labels; an unverifiable claim is UNVERIFIED, never PASS.

### 2.5 Framework and automation
- Add **Part 8: Data Source Audit** to `MASTER_AUDIT_FRAMEWORK.md` (checks C1-C10 summarised, the fetched-versus-computed rule, "run before trusting a page audit", and the limit "proves sources agree, not that they are right").
- Add the truth-free script to `nightly_audit.sh` weekly (not per-edit: Memory `feedback_no_slow_hooks`). No new hook, no new Golden Rule (user: "we have the majority of this already").

## 3. Order of work
0. Prerequisite from 2.3 (`--tickers-file`, classify_instrument), plus a **served-frame check** (3.1) so the audit also tests the path the app really uses.
1. 2.1 inventory (read-only) -> show the user.
2. 2.3 steps 1 and 3 (truth-free, 117) -> findings.
3. 2.3 step 2 IBKR truth for the 117 -> findings.
4. 2.2 measurement -> user decides option A or B.
5. Fixes from the findings (each its own small commit, tests first; engine/data changes get an Opus pass, wording fixes Sonnet).
6. 2.4 tab statement audit + Playwright rare states.
7. 2.5 framework Part 8 + weekly run.
8. The 117-ticker page audit already runs nightly. Until step 5 is done the nightly summary marks S4 "data UNVERIFIED" and the truth-free script runs outside the nightly window (Twelve Data quota). After step 5 its PASS means data-checked too; then the other tabs.

## 4. Acceptance
- All 117 have a verdict per check; every fail is either fixed or written into Known Issues with the reason.
- INVENTORY.md complete; a decision list of fetched items that should become computed.
- Tradier measurement table delivered; user decision recorded.
- Tab statements: 0 WRONG; UNVERIFIED listed with why.
- Existing suites (`./run_all_checks.sh --quick`, page checker) still green.

## 5. Risks
- IBKR delayed contracts ("delayed":900) can have a stale final bar: compare completed sessions only and mark the last bar.
- Provider throttling: run in batches, cache to disk, never re-fetch.
- Two sources agreeing does not make them right (both could share an upstream): say it in the report; IBKR is the tie-breaker.
- A fix that changes the history basis resets cached frames: re-check cache rules (Day 126) before any change.

## 6. Out of scope
Paid sources (named, not tested), fundamentals accuracy against filings, intraday feed accuracy, any trading rule, rerouting providers before the measurement.

## 7. Opus review, applied (Day 127; verdict GO WITH CHANGES, all accepted, claims checked against the code)
1. BLOCKER fixed: scripts hard-coded to 24 tickers; `--tickers-file` + `classify_instrument` added as step 0 (2.3).
2. 52-week high/low is already computed from bars; removed from the candidate list, `avgVolume`/`avgVolume10d` named instead (2.1).
3. Inventory grep widened to ALL `backend/*.py`, each fetch tagged "via orchestrator" or "bypass". About 17 direct yfinance/requests calls skip the orchestrator, cache and split fix: `_index_history` (:1303), sector rotation `yf.download` (:2716), MR signal/scan (:3874, :3945), cashflow (:4096), CNN fear-greed (:1510), stock-info fallback (:1135), `breakout_routes`, `market_phase_engine`, `cycles_engine`, `econ_engine`, `news_engine`, `scan_queries`; RS also fetches SPY and benchmark bars.
4. 3.1 Served-frame check: the script maps BRK-B to `BRK.B`/`BRK/B` per provider, but the app's providers do no symbol mapping and the script grades raw frames, not the frame after `_deliver` and `drop_forming_bar`. Add a check that runs `dp.get_ohlcv` and compares it with the raw frame; test BRK-B and GIB-A.TO through the real chain.
5. Guard changed: flag, never refuse; use `known_splits.json`; no cache-schema change (2.2).
6. The share is 34%, Yahoo 52% (not Twelve Data), re-measured per ticker; cause first, likely rate limit (2.2).
7. Option A confirmed: the live quote is already Tradier first; history stays on dividend-adjusted sources (Golden Rule 63, Day-126 basis work).
8. Order corrected: the page audit already runs nightly; S4 marked "data UNVERIFIED" until this is done (section 3 step 8).
9. IBKR budget made realistic (2.3 step 2).
10. Holidays/same-name pairs: avoid or use `tolerant` on 2026-11-26/27 and Canada-only holidays; C1 shows currency and exchange on every row.
11. `reference/data_audit_latest.json` exists already; written via `--update-reference`. Any cache or chain change keeps `test_price_basis` and `test_forming_bar_routes` green.
