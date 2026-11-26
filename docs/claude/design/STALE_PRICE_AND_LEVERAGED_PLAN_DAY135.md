# Plan (Day 135): stale-price warning + leveraged-fund "tracks its underlying" check

## Context
1. **VFV.TO (Nov 24, 6:02 pm):** Yahoo answered "Rate limit exceeded". For Canada, Yahoo is the ONLY price source (Alpaca, Twelve Data, Tradier say "not a US symbol"), so the app silently served the old saved bars (`orchestrator.py:212-216`, `_last_source = 'stale_cache'`). Only the Data Sources tab says so (`dataSourcesView.js:65`); the Analyze page shows nothing.
2. **Leveraged funds:** the audit grades them with checks built for plain stocks (short history, big jumps "needs IBKR"). Measured today on saved bars (Day 135): a leveraged fund is a clean second test of its own data, because its daily move should be about `multiple x underlying`.

## Measured facts (saved bars, 503 days, Alpaca; read-only)
| Fund vs reference | corr | beta | median / p95 / max daily gap |
|---|---|---|---|
| NVDL vs NVDA (2x) | 1.000 | 1.98 | 0.09% / 0.38% / 1.6% |
| AAPU, MSFU, TSLL, AMZU, GGLL, METU, NFXL vs their stock (2x) | 0.999-1.000 | 1.98-2.00 | median 0.06-0.11%, max 0.5-2.2% |
| BRKU vs BRK-B (2x) | 0.995 | 1.95 | 0.13% / 0.47% / 1.0% |
| **SOXL vs SOXX (3x)** | 0.999 | 2.96 | 0.14% / 0.77% / 2.7% |
| SOXL vs SMH (3x) | 0.984 | 3.20 | 0.99% / 3.4% / 7.1% (worse proxy) |
| **SOXL.NE (BetaPro 3x, CAD) vs SOXL** | 0.988 | 1.02 | p95 0.9%, **max 16.2% on 2026-07-02** |
| SOXL.NE vs SOXX / SMH | 0.989 / 0.976 | 3.04 / 3.38 | |
| URAA vs URA, UBOT vs BOTZ | 0.991, 0.998 | 1.90, 1.98 | UBOT max 13% (Apr 9 2025) |
| GDXU.TO vs GDX (declared 3x) | 0.964 | **1.88** | median 2.1%, max 15% (declared multiple looks wrong or FX/timing noise) |
| QPUX vs QTUM (2x) | **0.70** | 3.7 | no usable proxy; the +48% on 2026-05-21 is NOT explained by QTUM |
NVDL's +62% on Nov 23 = 2 x NVDA's +31.5%: real, consistent. Inference only: SOXL tracks the ICE/PHLX semiconductor index; SOXX is the closest proxy we have (SMH is not).

## Part A: stale-price warning (all tickers, wording mentions Canada)
- **Backend** `/api/stock/<ticker>` (`backend.py:~1206`): add `priceFreshness = {newestDate, expectedDate, sessionsBehind, servedFromStaleCache}`. `expectedDate` from `data_quality.expected_last_session` (weekday based, no holiday calendar); `servedFromStaleCache` from `get_data_provider()._last_source[f'{ticker}_ohlcv'] == 'stale_cache'`, read straight after the fetch (same-ticker parallel routes can overwrite it, so the date test is the backstop).
- **Rule (no tuned numbers):** warn only when `servedFromStaleCache` OR `sessionsBehind >= 2`. One session behind is not warned (a holiday looks the same without a calendar; a stale serve is already caught by the flag).
- **Frontend:** pure `frontend/src/utils/priceFreshness.js` (returns null or `{text}`), used by a small banner near the price header in `App.jsx`, same pattern as Day 134 `utils/planStatus.js`. Plain-facts text, e.g. "Showing saved prices up to Nov 24. The price source did not answer. Yahoo is the only source for Canadian tickers." No verdict words, no changed numbers.
- **Not in scope (own ROADMAP item):** a second Canada source (EODHD is 20 calls/day) and a Yahoo spacing fix for the Sectors batch.

## Part B: leveraged funds
1. **Reference map** `backend/reference/leveraged_underlyings.json`: fund -> `{reference, declared_multiple, measured_beta, corr, n, measured_on}`. Entries from the table above. Single-stock funds -> the stock. SOXL -> SOXX. SOXL.NE -> SOXL (and SOXX as second). GDXU.TO, UBOT, URAA: record measured beta, flag "declared multiple not confirmed". QPUX: **no reference** (listed as such, never guessed).
2. **New audit check C10 "tracks its underlying"** (`backtest/audit_data_sources.py` + shared `data_quality.py`, so the tab and audit say the same): per day `|fund return - beta x reference return|` against the pair's own median gap. WARN only, never FAIL; lists the worst 3 dates. Tolerance = max(5 x the pair's own median gap, 1%) (a heuristic, labelled "not tested"). Pure function with tests (empty, one row, misaligned dates, NaN, zero-move day).
3. **Stop a never-served source turning a ticker red:** C5 and C8 ignore a source the app is forbidden to serve for that ticker (`providers/fallback_policy.tradier_blocked`). Clears QPUX and NVDL's FAIL (both come from Tradier-only errors; QPUX's reverse split is already adjusted by the three served sources).
4. **IBKR spot checks (measurement, no code):** QPUX 2026-05-21 (+48%) and 2026-03-20..23 (split), SOXL.NE 2026-07-02 (16% gap vs SOXL). Contract ids come from the saved truth file (Golden Rule 58): QPUX 866508540, SOXL.NE 805995437. NVDL needs none (C10 clears it).
5. **DRAL "RS1" smoke-audit row:** DRAL has 105-107 bars; find which side is wrong (page shows a number, audit expects N/A), fix it, add a test. Same check for AVGC (104 bars).
- **Not in scope:** a better SOXL.NE data source (Yahoo is close-only, no volume); BRKU Twelve Data zero volume (Alpaca serves it); dividend-basis warnings on URAA/AAPU/MSFU/NFXL/ELIL.

## Trader note (PERSONA lens, common practice, not tested here)
The thesis lives in the underlying; the leveraged fund is the instrument you are filled in, so stops and size are read on the fund's own price (a 3x fund's stop in % is about 3x wider; size by stop distance). The reference only tells us whether the fund's DATA is sane.

## Verification
- Tests: `test_price_freshness.mjs`, a backend test for the `priceFreshness` fields (stale flag, 0/1/2 sessions behind, empty frame), `test_leveraged_tracking.py` for C10 and for the blocked-source grading; mutation-check each fix.
- Real data: force a stale serve (set the Yahoo breaker open for a `.TO` ticker, or stub the provider) and see the banner; load VFV.TO normally and see none. Run C10 on all 21 leveraged funds and compare with the table above. Page checker `ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN VFV.TO` plus phone width (390px) screenshot.
- `./run_all_checks.sh --quick`, audit re-run (offline replay, no provider calls), IBKR spot checks reported with dates and numbers.

## Process
Copy to `docs/claude/design/STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md`, Opus review (it changes an API response, a grading rule used by the tab AND the audit, and adds a reference file: Golden Rules 55, 59), apply, build Part A then Part B, `/three-pass`, stamp with `--plan`.

## Opus review (Day 135), applied: verdict GO WITH CHANGES
Premises checked against the code; the plan above is amended as follows (this section wins where it differs).

**Part A**
1. **Pass the field through `frontend/src/services/api.js:35-57`** (it rebuilds the stock object field by field, Golden Rule 30; `formingBarDropped` is already lost there). Test that `priceFreshness` arrives.
2. **Stale flag set where the data is served, not read from a shared dict.** `_deliver` / the per-ticker locked fetch (`orchestrator.py:167`) puts the source in `df.attrs['source']`; the route reads it. `servedFromStaleCache = (not _legacy_path) and source == 'stale_cache'` (the legacy path means the stale fallback also failed). The cached-OHLCV branch is fresh-only (`cache_manager.py:269`) so it never serves stale.
3. **No `sessionsBehind >= 2` rule.** `expected_last_session` returns today even while the session is open and `drop_forming_bar` removes today's bar, so mid-session the gap is always 1, and after a holiday (US-only or Canada-only) it is 2: a false warning on every ticker. Reuse the existing rule, `data_quality.level_freshness(..., tolerant=True)` (3+ behind = WARN), and the stale flag. No third threshold (Rules 59/63).
4. **A stale copy can be fully current, or hold a partial bar.** Text states the date fact only ("saved prices up to Nov 25"); it never says "old". A stale entry cached before 16:30 ET on its own last bar's date is flagged as possibly partial (`cached_at` from `read_ohlcv_entry` meta).
5. **One place for the date:** put the text beside the existing `priceAsOf.js` label (`App.jsx:~1007`), not in a second banner; check the wording when a live quote is showing.
6. **Edge tests:** empty `priceHistory` (no banner, no crash), one row, tz-aware index, 16:15 ET, Saturday, stale copy that is current. Log one line per stale serve with the ticker (route side).

**Part B**
1. **Tradier-blocked handling lives in ONE place:** `chain_sources()` (`audit_data_sources.py:227`) drops Tradier when `tradier_blocked(sym)` (same rule as `orchestrator.py:187-189`); Tradier stays in `extras` as comparison only. Cleans C2/C4/C5/C6/C8. C5 for NVDL/QPUX then drops to WARN (shared +62% / +48%), not PASS. Keep the C8 `used == 'tradier'` FAIL path.
2. **Copies that change together:** `grade()` and `chain_sources()`; the check tuples in `write_report` (`:419`, `:425`); `data_quality.read_audit_summary` (`:304`); `dataSourcesView.js:21` labels and `:94-96` pass count over `Object.keys(checks)` (Rule 57).
3. **C10 is audit-only** (the tab reads one cached frame, the reference may not be cached). **No tuned tolerance, no fitted beta:** use the DECLARED multiple; report facts only: correlation, the worst 3 dates with the gap, and on every C5 jump date the reference's move x multiple beside it (settles NVDL +62% = 2 x NVDA +31.5%). C10 never downgrades C5; it annotates the C5 note. Join dates first, then compute returns. Declared multiple vs measured beta mismatch is shown as a fact (GDXU.TO 1.88 vs 3).
4. **`leveraged_underlyings.json` holds the mapping and the declared multiple only** (no frozen measured numbers; the audit measures at run time).
5. **DRAL "RS1": the audit is wrong, the page is right.** The card now shows N/A plus a reason line (`App.jsx:1163-1166`, `rs-na-reason`); `audit_cards.py:431` needs the three N/A fields adjacent, so it reports "a number" without finding one. Fix the pattern to allow the reason line; report "a number" only when digits are captured; drop the stale note "card does not say why"; claim the "105 loaded" number so U1 stops listing it. AVGC has the same cause. Test with a planted card text (with and without the reason line, and with a real number).

## Build notes (Day 135)
- **C10 became C11.** "C10" is already reserved in the Day 126 docs for fundamentals and classification, so the new "tracks its underlying" check is **C11** (audit only, level `NA`, facts in the note).
- **C11 compares the copy the app uses:** the fund's frame goes through the app's split table first (`split_adjust.adjust_for_splits`), otherwise SOXL.NE's covered 3:1 split (and the US holiday gap on 2026-05-25) shows as a fake -60% gap. Found by running it on real data, then fixed and tested.
- **The IBKR spot check for SOXL.NE is no longer needed:** after the split fix SOXL.NE vs SOXL is corr 0.999, beta 1.01, biggest gap 2.7%. My first "16% on 2026-07-02" came from a date misalignment in my own scratch comparison.
- **QPUX +48% on 2026-05-21 is real (IBKR, conId 866508540):** closes 26.83 (May 20) and 39.60 (May 21); all four sources match IBKR on 2026-03-20, 03-23, 05-20, 05-21 (within 0.01). IBKR lists the reverse split on 2026-03-23 and its history is split-adjusted through it.
- **Backend v2.60, frontend v4.72** (new `priceFreshness` field; footer).
