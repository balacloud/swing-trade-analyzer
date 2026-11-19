# IBKR truth run (plan, Day 128), v2, Opus review applied (GO WITH CHANGES). Section 3 (group C), 4 (identity check) and 5 (budget) are superseded by section 9.

Part of Data Source Audit Round 2 (ROADMAP #20, step "IBKR truth"). The user declined the Python / IB Gateway route ("too complicated") and asked for a token-efficient way with the existing IBKR connector.

## 1. Goal
Get IBKR's own prices for the tickers where a second opinion matters, so `audit_vs_ibkr.py` can grade C1/C3/C5/C7 for them. IBKR is the tie-breaker when two providers could share the same fault.

## 2. Facts already measured (Day 128)
- 24 of the 117 tickers already have IBKR truth from Round 1 (`backend/validation_results/ibkr_truth_20261114.json`, includes QPUX, DRAL, SOXL.NE, SPCL, UBOT, GDXU.TO, the .TO CDRs). 93 remain.
- QPUX and DRAL are cleared: Yahoo and Twelve Data match IBKR exactly on all completed days; the 3-4% gap was only Nov 19, the unfinished day (my audit ran mid-session).
- Every ticker has a contract id on the user's watchlists (ids saved in the scratchpad, `ibkr_conids.json`, not in the repo). Symbols with two ids: GEV, AVGO, AMD, SOXL, ORBX. Round 1 used 805995437 for SOXL.NE (Canadian), so US SOXL is 73340487. GEV's Canadian id is 780710890.
- The connector's `get_price_history` takes `step_count`: 6 daily bars cost about 450 tokens of output (measured on AAPL). It does NOT echo the contract id.
- `audit_vs_ibkr.py` needs per ticker: `conid`, `ibkr_description`, `dates` + `close` + `volume` (last 5 sessions), `monthly` (three month-end closes), `splits` (corporate actions). So most tickers need TWO calls (daily, monthly with `include_corporate_actions`).

## 3. Scope: 49 tickers (not 93, not 117)
Why: for US stocks and US ETFs two independent providers (Twelve Data and Yahoo) already cross-check each other and agree; IBKR adds little. The gaps are tickers with ONE source and the leveraged funds.
- **A. Single-source Canada / CDR (24):** CNQ.TO, FINN.NE, WDC.TO, CCO.TO, ASML.TO, ANET.TO, GIB-A.TO, GEV.TO, HURA.TO, XGD.TO, MTRX.TO, ORBX.TO, RBOT.TO, XDRV.TO, CARS.TO, COPP.TO, XETM.TO, SGRD.TO, MDA.TO, NTR.TO, ASTL.TO, BDT.TO, PNG.V, CGY.TO. Daily + monthly + splits.
- **B. US leveraged (15):** SOXL, URAA, COPZ, NVDL, AAPU, MSFU, METU, GGLL, NFXL, AMZU, TSLL, BRKU, ELIL, COTG, AVGC. Daily + monthly + splits (splits and reverse splits are common on these).
- **C. Spot-check of plain US names (10):** AAPL, NVDA, LLY, KEYS, MRVL, HD (six of the 15 tickers whose cache was repaired today), ORCL, CVX, QTUM, COPX (audit C9 warnings). Daily only (`monthly` empty, `splits` empty; C5 not graded for these).
- Not fetched: the other 34 US stocks and ETFs (C9 passes with two agreeing sources), and the 24 done in Round 1.

## 4. Method
1. **Measure first.** One monthly call (`ONE_MONTH`, `step_count` 12, `include_corporate_actions` true) on one group-A id; recompute the budget from the real size. Stop and re-plan if a monthly result is over about 1,000 tokens.
2. **Dry run of the script (free).** Run `audit_vs_ibkr.py` on a tiny truth file with one real entry and one entry with empty `monthly`/`splits`, to be sure it does not crash on group C.
3. **Batches of 8 parallel calls** (4 tickers x 2 calls). Parallel results can come back in any order (Golden Rule 42) and the connector does not echo the contract id, so every ticker is identity-checked before it is recorded:
   - the last COMPLETED daily close must equal the app's own close for that date within 0.5% (read from `data_audit_cache_20261119.json`); a US/Canadian pair of the same symbol also differs in price level, so this picks the right id for GEV, AVGO, AMD, SOXL, ORBX;
   - the last monthly bar's close must be within 1% of the daily call's last close (same ticker, two calls).
   A ticker that fails is re-fetched ALONE once; if it still fails it is left out and listed as "identity unconfirmed", never recorded.
4. **Drop today's bar.** The last daily bar is the unfinished day (Nov 19). Keep only the 5 completed sessions (this is exactly how QPUX/DRAL fooled the mid-session audit).
5. **Record** one compact Python merge per batch into `backend/validation_results/ibkr_truth_20261119.json` (same keys as Round 1: conid, ibkr_description, dates, close, volume, monthly, splits). Only numbers are typed; nothing else is copied from tool output.
6. **Run** `venv/bin/python backtest/audit_vs_ibkr.py --date 20261119`; read the summary, not the whole report.
7. **Close-out:** findings into Known Issues / ROADMAP #20; ticker-level fixes are separate plans (Opus first, Golden Rule 55). The three-pass hook applies if any code file changes.

## 5. Token budget (estimate; step 1 replaces the guesses with a measurement)
| Item | Calls | Per ticker | Total |
|---|---|---|---|
| A + B: daily (about 570 incl. call) + monthly (about 740 incl. call) + record (about 150) | 78 | about 1,460 | about 57,000 |
| C: daily only (about 570 + about 80 record) | 10 | about 650 | about 6,500 |
| Batch overhead (8 identity-check runs, summaries) | | | about 8,000 |
| **Total** | **88** | | **about 70,000 (range 60,000 to 80,000)** |
My earlier "35,000" ignored the monthly/splits call; this is the corrected number. Compare: all 117 tickers with a month of bars was about 400,000+.
Levers if it must be cheaper: drop group C (-6,500); fetch group A first and stop (about 36,000 incl. overhead); split over two sessions.

## 6. Acceptance
- Truth file with every in-scope ticker or an explicit "identity unconfirmed" / "no data" line for each one left out.
- `REPORT_vs_IBKR.md` generated; every FAIL or WARN either explained or logged; FINN.NE, XDRV.TO and SOXL.NE verdicts confirmed against IBKR.
- Actual tokens used reported against the 70,000 estimate.
- `./run_all_checks.sh --quick` still ALL OK (no app code is changed by this run).

## 7. Out of scope
The Python / IB Gateway route (declined), fixes for findings, volume accuracy (plausibility only), the after-close re-run of the truth-free audit (separate step), US stocks beyond the spot-check.

## 8. Questions for the reviewer
1. Is the scope (49) right, or is it either wasteful (drop C?) or missing a class where IBKR matters (e.g. the 8 CDRs done, US ETFs)?
2. Is there a cheaper call design (fewer bars, `period` instead of `step_count`, one call instead of two, a different bar size) that still gives the script what it needs? Verify what `audit_vs_ibkr.py` really reads.
3. Does the script crash or mis-grade on an empty `monthly`/`splits` (group C), and on a last bar that is today's partial bar?
4. Is the identity check sound (0.5% to the app's close; 1% daily-vs-monthly), and are there cases it would pass a wrong contract?
5. Token math: any item wrong or missing? What would you cut first?

## 9. Opus review, applied (verdict GO WITH CHANGES; claims checked by us where free)
**Checked by us (free, from the saved audit data):** with Nov 19 excluded, 0 of 79 tickers that have both Twelve Data and Yahoo differ by more than 1% on any completed day; the only differences are QPUX and DRAL on the unfinished Nov 19 (the audit's C9 includes the forming bar, a small flaw, logged). So the C9 warnings that justified group C are probably the same artifact.
**Corrections to this plan:** (1) `audit_vs_ibkr.py` grades C3, C5 and C7 only; C1 appears only in its docstring. (2) "QPUX and DRAL match IBKR on all completed days" overreached: Round 1 truth covers only Nov 9-13 (the providers agree with each other on every other completed day). (3) 12 monthly bars do not reach 2025-11 (the Round 1 month-ends were 2025-11, 2026-05, 2026-10): use 13+. (4) Splits are display-only in the script; grading uses `dates`, `close`, `volume`, `monthly`.
**Changes accepted:**
1. **Identity by structure, not price.** The price check I proposed was circular (it gates on agreement with the very source being audited; for a Yahoo-only ticker a Yahoo error on the last day would make true IBKR data look "unconfirmed" and hide the finding, and a 3x fund moving more than 1% today fails the daily-vs-monthly test falsely). Instead give every call in a batch a DISTINCT `step_count` (daily 6, 7, 8, 9; monthly 13, 14, 15, 16) and match result to call by bar count (Golden Rule 42). Price is only a LOOSE sanity check (within 20%, and US vs Canadian price level) used to choose between two contract ids for the same symbol (GEV, AVGO, AMD, SOXL, ORBX); it never gates.
2. **Group C is DROPPED.** An empty `monthly` makes C5 read PASS ("month-end levels match IBKR") and that false PASS would be written to `data_audit_latest.json`, which the Data Sources tab shows (backend.py:~1037); fixing it needs a code change. The six repaired tickers were already cross-checked against Tradier (NVDA, KEYS, AAPL, CAT matched to the cent), and the 79 two-source tickers agree on every completed day.
3. **Monthly call uses 13 bars** (`include_corporate_actions` true); drop today's bar BY DATE (keep dates up to 2026-11-18), not by position (after the close, or on an illiquid ticker, a position-based drop would delete a completed day).
4. **Merge the 24 Round 1 entries** into `ibkr_truth_20261119.json` at no token cost. Their dates (Nov 9-13) are in the new frames, and it avoids a regression: `audit_splits.py:23` reads only the NEWEST `data_audit_vs_ibkr_*.json`, which would otherwise drop Round 1's IBKR splits (SOXX, QPUX, SOXL.NE, GDXU.TO, AMD.TO, MU.TO).
5. **C9 recheck with Nov 19 excluded:** done above (0 tickers).
**Scope now: 39 tickers fetched (A 24 + B 15), 24 reused from Round 1.**
**Revised token budget:** 39 tickers x (daily about 570 + monthly with 13 bars about 800 + record about 150) = about 59,000, plus about 6,000 overhead and re-fetches = **about 65,000 (range 55,000 to 75,000)**. Measure one monthly call first (Golden Rule 25) and re-plan if it is over about 1,000 tokens. Lever: skipping the monthly call for plain Canadian stocks without splits saves about 8,000 but gives up C5 on single-source tickers (the unadjusted-split check), so it is not recommended.
**Acceptance additions:** Round 1's 24 entries present in the new file; every fetched ticker's calls matched by bar count; any ticker left out is listed with the reason; the report states which tickers' truth is Round 1 (Nov 9-13) and which is new (to Nov 18).
