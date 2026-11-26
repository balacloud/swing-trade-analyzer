# Known Issues — Day 135

> **Open issues only (L1).** Layered Day 133: this file lists Medium-and-above open items plus the two Low-Medium items that are next-session priorities (DRAL RS1, stale `data_audit_latest.json`). Everything else (Low, Info, fixed, per-day change notes) is in `docs/claude/history/KNOWN_ISSUES_LOW_AND_RESOLVED.md`. Supersedes `KNOWN_ISSUES_DAY134.md`. v4.73 (Backend v2.61, Frontend v4.69).

## Open Issues

### Medium: Data Source Audit Round 2, about 60% done (Day 129; ROADMAP #20)
**Update (Day 135): about 85% done.** The reference file `data_audit_latest.json` was refreshed after the Nov 24 close (117 tickers; the Day 134 "stale" item is resolved). Added this day: Alpaca startup/env fix, saved-prices line on the Analyze header, leveraged-fund audit (C11, Tradier-blocked grading, underlying map), header data notes. **Thin-ETF close differences (XDRV.TO, CARS.TO, FINN.NE) are NOT being pursued (user decision, Day 135):** the page shows the Data Sources integrity wording only, prices unchanged. Still open: Data Sources tab statement audit + rare states, Scan/Sectors/Context and the ~17 direct provider calls, second Canada source (ROADMAP #30), per-ticker provenance, Alpaca in-session bar, framework Part 8. Older Day 128-129 detail below.
The Statement Audit proves the maths on the bars the page received, not the data. Round 2 (`docs/claude/design/DATA_SOURCE_AUDIT_ROUND2_PLAN_DAY127.md`).
**Done:** step 0 (audit scripts take `--tickers-file`), Analyze-page inventory (draft), truth-free audit on all 117 (mid-session), Tradier 400 fix, empty-price-row fix + audit checks.
**Not done:** (1) re-run the audit AFTER the 4pm close (freshness read "warn" for every ticker because the run was at 10:17 ET; Tradier's breaker opened so only 1 of 79 US tickers was tested); (2) IBKR truth for the 117
(every ticker has a watchlist contract id; 24 already have truth from Round 1; QPUX and DRAL were CLEARED: the 3-4% Yahoo vs Twelve Data gap was only on Nov 19, the unfinished day; on every completed day the two providers agree within 1% for all 79 tickers that have both, and both match IBKR on the 5 days Round 1 covered, Nov 9-13); (3) fix FINN.NE (22 malformed bars), XDRV.TO (83% flat zero-volume bars), SOXL.NE (100% flat,
close-only; known); (4) Canada has one source for most tickers, so "unchecked" there is not "clean"; (5) Data Sources tab statement audit + Playwright rare states; (6) inventory of the other tabs and about 17 direct
provider calls that bypass the orchestrator; (7) the 117-ticker page audit, then Scan / Sectors / Context; (8) framework Part 8.
**Update (Day 128, later): the IBKR truth run is DONE** (`docs/claude/design/IBKR_TRUTH_RUN_PLAN_DAY128.md`, report `docs/test/DataSources_20261119/REPORT_vs_IBKR.md`). 63 of 117 tickers compared with IBKR (24 from Round 1 plus 39 new: all Canadian/CDR and the other US leveraged funds; the 54 plain US stocks/ETFs were skipped on purpose because Twelve Data and Yahoo agree on every completed day). Truth covers closes to Nov 18. Result: closes match IBKR within 0.3% for nearly every ticker (C3: 96 pass, 4 warn, 2 fail; C5 month-end levels: 92 pass, 10 warn, 0 fail; C7 volume: 94 pass, 6 warn, 2 fail). **Real findings:** (a) XDRV.TO and CARS.TO: Yahoo closes differ from IBKR by up to 2.2% and 2.6% on settled days (thin ETFs; which "close" is right depends on last trade vs auction, not decided); (b) SOXL.NE: Yahoo volume is zero and its Nov 13 close is 4.2% off (known close-only data); (c) BRKU: Twelve Data volume is zero (a gap). **Expected, not errors:** 10 C5 warnings on leveraged US funds (URAA, AAPU, MSFU, NFXL, ELIL) where the Nov 2025 month-end differs 7-12% from IBKR while Twelve Data and Yahoo agree with each other: likely dividend adjustment (IBKR history is split-adjusted only; these funds pay large distributions), not tested further. WARN 0.6% on MTRX.TO and SGRD.TO (thin ETFs). Limits: IBKR data for the Canadian tickers is 15 minutes delayed, splits were not fetched (monthly levels catch unadjusted splits), two sources agreeing is not proof. **Caveat found in the review:** QPUX's IBKR verdict flipped FAIL to PASS only because Tradier's breaker was open during the run (Tradier was not graded); its Tradier split error (x3, Nov 14) is NOT fixed and the older truth-free FAIL still shows on the tab. Token cost: roughly 100,000 by my count (estimate was 74,000; US funds returned 14-32 monthly bars, not 13).
The nightly summary should keep saying "data UNVERIFIED" until the after-close re-run and the fixes for (a)-(c) are done.

### Medium (likely much reduced by Alpaca, Day 129, NOT re-measured): Twelve Data keeps hitting its limit, so the app fell back to Yahoo for most US tickers (Day 128, measured)
The app cache shows Yahoo served 61 of 97 US tickers and Twelve Data 36; the app log shows the Twelve Data breaker opened 82 times ("Rate limit exceeded", 8 calls a minute). Intraday (4-hour RSI) calls draw on the same
allowance (log: "Intraday twelvedata failed ... Rate limit exceeded"), and `rsi_4h` has no card using it, so removing that call is the cheapest likely relief (inference, not yet tested). Yahoo history is dividend-adjusted like
Twelve Data but starts about 4 days later (501 vs 504 bars) and is where the empty-newest-bar problem came from. Needs a small plan (Opus first, Golden Rule 55). Not changed.

### Medium: Tradier stalls on random single calls (Day 128, measured, not fixed)
Tradier answers most calls in 0.4-1.0 s, but about 1 call in 6-8 hangs until our timeout: 6 of the first 7 US calls in the audit (CAT, BRK-B, JPM, JNJ, GEV, NFLX), then NVDA once (15 s) and LLY once (40 s) while the calls
around them took about 1 s. Not ticker-specific (NVDA stalled once and then answered in 0.7 s). Three stalls in a short time open our breaker for 5 minutes, which is why Tradier looks "down". Tradier's docs say nothing about
timeouts. Option: one retry on a timeout (a design choice, needs a plan). Also no per-call timing is logged, so the stall rate is unmeasured over time.

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Medium: the MR ledger holds a fake MNST −50.8% loss (split artifact) (Day 123)
*Unverified since Day 123: not re-read or re-run since it was written; check before repeating it (Golden Rule 69).*
Found by `mr_open_entry_retest.py`. On today's data both re-test bases replay it correctly, so
the corrected PF 1.50 is unaffected. The stored ledger row and `daily_job.py --report`'s PF 2.00
still include it. **Fix:** not needed for any live use (program discontinued); document only.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
*Unverified since Day 108: not re-read or re-run since it was written; check before repeating it (Golden Rule 69).*
**Fix:** Not actioned. Likely moot now — the paper-trading engine it would wire into is
discontinued (Day 113). Worth a 2-minute check before ever planning a fix: confirm nothing else
reads this sizing path before spending effort on it.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty — decision made, not implemented (carried from Day 111)
**Fix (decided, not implemented):** drop the investor-name labels, group the six metrics under
three functional headings (Efficiency & Quality, Valuation, Cash Generation). Frontend-only.

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (carried from Day 108)
**Fix:** Not actioned — needs a product decision.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Fix:** Mitigation choice still a pending user decision.

### Medium: Two batch endpoints (Sectors Rotation, Market Phase breadth) bypass circuit-breaker protection, no Tradier fallback (carried from Day 111)
**Fix:** Not actioned. `/api/mr/scan`'s bypass was fixed Day 111; these two remain.

### Medium: Alpaca's in-session daily bar is only partly checked (Day 129, updated Day 134)
Day 133 (market open): the running app was NOT using Alpaca (HTTP 401, breaker open, stale keys in the long-lived parent process); a full `./stop.sh` and `./start.sh` fixed it. After the restart 97 of 138 cached frames are Alpaca, and the page checker passed 52/52 on live prices. Still open: look at today's bar itself (missing, partial, complete) and the Data Sources tab for 3 tickers; the 16:30 ET forming-bar cap and `drop_forming_bar` stay the safety net.

### Medium (user decision): Alpaca terms of use and the Twelve Data key (Day 129)
No Alpaca-specific data terms were found; exchange agreements limit non-professional use to personal, non-business use. Local single-user use looks consistent; **do not publish Alpaca-sourced prices in shared Artifacts** (Beginner Playbook, Status Board). The Twelve Data key sits in old lines of `backend/backend.log`; rotation is the user's call.

### Medium (new Day 135, user decision): an old FRED key value is committed in git history
`docs/claude/versioned/archive/KNOWN_ISSUES_DAY62.md` line 88 holds what looks like a real `FRED_API_KEY` (not compared with the current `.env` key). Rotating it is the user's call.

### Medium (new Day 135): Canada has one price source, so Yahoo trouble means saved prices
VFV.TO served the saved copy on Nov 24 at 6:02 pm (Yahoo "Rate limit exceeded" during the Sectors batch). The Analyze header now says so (v4.72). Open: a second Canada source and spacing Yahoo calls in the Sectors batch (ROADMAP #30). Not measured: how often a Canadian ticker the user opens hits a rate limit (the log has over 10,000 Yahoo rate-limit messages over its whole life).

