# Plan (Day 135, build 3): data notes under the header price (thin-ETF note + leveraged "follows its underlying" line)

## Context
The user chose "header note only" for XDRV.TO, CARS.TO and FINN.NE (no prices changed) and wants the leveraged line. Today the Data Sources tab already marks these tickers FAIL/WARN, and the audit knows each leveraged fund's underlying (C11), but the Analyze page says nothing about either. Sizing (honest): this is a medium build, about one session: one backend field, one audit write, one pass-through, one util, one header render, one page check, tests. No prices change.

## Facts read from the code (Day 135)
- `data_quality.quality_level(check_history(...))['checks']['integrity']` already holds the tab's wording and level: `"82% of bars flat with zero volume; 0 malformed bars; zero volume on 3 of the last 5 days"` (WARN/FAIL by `level_integrity`). Reuse it verbatim: one label, one number (Golden Rule 63).
- XDRV.TO: integrity FAIL (82% flat zero-volume); CARS.TO: WARN (12%); FINN.NE: FAIL (28 bars whose high/low do not contain the close; closes match IBKR). All three have Yahoo as the only source.
- C11 facts (reference ticker, declared multiple, correlation, beta, days) are computed by the audit (`audit_data_sources.tracking_check`) but only a text note is stored in the run JSON; `data_audit_latest.json` stores only WARN/FAIL lines, so the page cannot read C11 today.
- `/api/stock` (`backend.py`, `priceFreshness` added Day 135) is rebuilt field by field in `frontend/src/services/api.js` (Golden Rule 30). The header already shows the saved-prices line (`utils/priceFreshness.js`, `App.jsx` `data-testid="price-freshness"`).

## Approach
1. **Audit stores the tracking facts.** `tracking_check` returns the facts dict as well; `grade()` passes it out under a private key that `main()` pops (same pattern as `per_source`); `data_quality.update_audit_reference(..., tracking=...)` writes `tickers[SYM]['tracking'] = {reference, multiple, corr, beta, n, date}` (no level key, so `read_audit_summary` ignores it). New `data_quality.read_tracking(symbol)` (never raises, None when absent). Only funds in `leveraged_underlyings.json` with a reference get it.
2. **Backend `/api/stock` adds `dataNotes`:** `{integrity: {level, note} | None, tracking: {...} | None}`. `integrity` comes from a new helper `data_quality.integrity_note(df, ticker)` that wraps `check_history` + `quality_level` and returns the integrity check only when WARN/FAIL (so the page and the tab can never word it differently). Never raises; `None` on any failure with a log line.
3. **Frontend:** `api.js` passes `dataNotes` through (null when absent). New pure `utils/dataNotes.js` -> `describeDataNotes(dataNotes) -> [{id, level, text}]`. Texts, plain facts only, no verdict words:
   - integrity: `Price data: <tab note verbatim>.`
   - tracking, multiple known: `Follows NVDA x2: correlation 1.00 over 503 days (audit Nov 24).`
   - tracking, multiple unknown: `Compared with GDX: correlation 0.98 over 490 days (audit Nov 24).`
   - SOXL.NE case (reference is another fund, multiple 1): `Follows SOXL x1 ...` (same template).
   `App.jsx` renders the lines under the saved-prices line, muted gray for tracking, amber for integrity. Nothing renders when there are no notes (no hidden states, no empty `<p>`).
4. **Page check A17** (`analyzeChecks.js`, reader in `ui-verify-checklist.js`): expectation derived from raw `api.stock.dataNotes` (not from the util): integrity line present iff level WARN/FAIL and it contains the API's note; tracking line present iff tracking present and contains reference, correlation and days; no lines otherwise.
5. **Docs:** API contract (`dataNotes`), ROADMAP #20 note, KNOWN_ISSUES (thin ETFs: note shown, data unchanged; the real fix is #30), `leveraged_underlyings.json` unchanged.

## Not in scope (decided with the user)
No price repair for FINN.NE, no volume change for XDRV.TO, no new source (ROADMAP #30). The tab's audit line for NVDL ("C5 ... needs IBKR") is not rewritten here.

## Edge cases to cover
Empty or one-row frame; frame with no `volume` column; NaN rows; `dataNotes` missing from an older backend; `tracking` with `multiple: null`; reference not in the audit run (no tracking stored); audit file missing or invalid JSON; a stored tracking entry older than the funds map (fund removed from the map: line still shows with its audit date, fine); very long note text on a phone (wraps at 390px); the line never appears for plain stocks with clean data (AAPL).

## Verification
- Tests: `test_data_notes.py` (integrity_note on planted frames: clean, 82% flat, 28 malformed, NaN, empty; read_tracking: present, absent, bad file; update_audit_reference writes `tracking` and leaves `read_audit_summary` unchanged), `test_data_notes.mjs` (texts, null/empty, no verdict words), api passthrough test extended, `test_analyze_checks.mjs` A17 cases. Mutation-check each fix.
- Real data: `/api/stock/XDRV.TO`, `CARS.TO`, `FINN.NE`, `NVDL`, `SOXL.NE`, `GDXU.TO`, `AAPL`; page checker on those plus VFV.TO; screenshots at 390px and desktop for XDRV.TO and NVDL. Measure the added time of `integrity_note` per `/api/stock` call (must stay small next to the existing call).
- `./run_all_checks.sh --quick`, audit offline replay to write the tracking facts, then re-read the reference file.

## Process
Copy to `docs/claude/design/DATA_NOTES_PLAN_DAY135.md`, Opus review (new API field, new key in the audit reference file read by the tab, shared wording with the tab: Golden Rules 30, 57, 59, 63), apply, build, `/three-pass`, stamp with `--plan`.

## Opus review (Day 135), applied: verdict GO WITH CHANGES
Premise corrected: the plan computed the integrity note on the frame `/api/stock` serves (after `_deliver`: empty-close rows dropped, split-adjusted). The tab reads the RAW cache (`backend.py:977-980`, `read_ohlcv_entry`) and counts the empty-close rows (`nan_closes`, `newest_close_missing`), so the page could show nothing while the tab warns, and the two could quote different percentages (Golden Rule 63).
1. **One helper, one path:** `data_quality.cached_quality(ticker)` = `read_ohlcv_entry` + `check_history(ticker=)` + `quality_level(source=, blocked=)`, returning exactly the block `/api/provenance` builds today. `/api/provenance` is changed to call it (replacing its inline code); `/api/stock` calls the same helper. `state != 'ok'` gives no note (never an invented integrity FAIL).
2. **Say which bars the % covers:** the note carries "(of N saved bars since DATE)" from the same facts (the page analyses 260 bars; the % covers the whole saved history).
3. **Audit write:** the private tracking key is popped in `main()` next to `per_source`/`used`, on both the no-chain early return and the normal path, and also stored in the run row (a replay matches). `update_audit_reference(tracking=None)` means "leave stored entries alone" (the `audit_vs_ibkr.py` call keeps them); an explicit dict deletes the stored entry for any symbol missing from it (reference missing, error, fund dropped from the map). `read_tracking` also returns None when the map's reference no longer matches the stored one.
4. **Hook comment:** `three_pass_check.sh:24` says no logic reads `data_audit_latest.json`; reworded to "read only to display notes (Data Sources tab, Analyze header), no trading or verdict logic". The exemption stays (a deliberate decision; tests rerun).
5. **Frontend:** A17 follows A16 (`CHECK_IDS`, `NAMES`, `fns`, header comment 14 -> 15, reader field in `ui-verify-checklist.js`); no hard-coded count exists. New testids `data-note-integrity`, `data-note-tracking`. `api.js` passes `dataNotes`.
6. **Wording (facts, not claims):** "Follows" is a claim, so: stock basis `Compared with NVDA (x2 stated): correlation 1.000, beta 1.98 over 503 trading days (audit, Nov 24).`; measured basis `Compared with BOTZ, the closest match by price (x2 stated): ...`; unknown multiple `Compared with GDX (multiple not known): ...`; a same-leverage twin (SOXL.NE, new `"twin": true` in the map) `Compared with SOXL, a fund with the same leverage (x1): ...`. Correlation and beta shown with 3 and 2 decimals exactly as stored (no `toFixed(2)` rounding of 0.995 to "1.00"). "trading days", and the date is the audit's date, labelled "audit".
7. **Noise check before shipping:** count how many of the 117 tickers would get an integrity line (a plain stock with 1 malformed bar would show an amber line); if it is noisy, decide with the user before shipping.
8. Performance measured by the reviewer: `check_history` + `quality_level` about 2.5 ms on 520 bars; `read_tracking` under 1 ms; `/api/stock` is called once per Analyze click. Fine.
