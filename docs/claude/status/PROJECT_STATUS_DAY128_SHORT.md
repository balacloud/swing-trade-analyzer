# Project Status — Day 128 (Nov 19)

**Version:** App v4.68, Backend v2.57, Frontend v4.64 unchanged (from v4.67 / v2.56 / v4.64)

---

## What Happened Today

The user's worry carried on from Day 127: "if the data is wrong the whole compute is wrong." Today was Data Source Audit Round 2, started: audit the data itself, not just the maths on it. The user also asked, twice, for plain English, and corrected me once for answering a bigger question than the one asked ("all I asked was, was the math perfect?").

### 1. Fetched-versus-computed inventory (Analyze page)
Draft in `docs/test/DataSources_20261119/INVENTORY.md`, from reading the code. Findings: the same price bars are fetched separately by `/api/stock`, `/api/sr`, `/api/patterns`, `/api/breakout`, the live quote and SPY/QQQ, so two cards can come from different providers; the Mean-Reversion card reads Yahoo directly, around the provider chain; the Liquidity row uses Yahoo's average volume although the app computes one from bars; `rsi_4h` spends an intraday call on every `/api/sr` and no card uses it. Other tabs and about 17 bypass calls are not inventoried yet.

### 2. Truth-free audit on all 117 tickers (run mid-session, 10:17 ET)
Report: `docs/test/DataSources_20261119/REPORT.md`. Clean for all 47 US stocks, 13 Canadian stocks and 8 CDRs. Real problems: FINN.NE (22 malformed bars), XDRV.TO (83% flat zero-volume bars), SOXL.NE (100% flat, known), QPUX and DRAL looked like a 3-4% Yahoo vs Twelve Data disagreement but it is only on Nov 19, the unfinished day (the run was mid-session); on every completed day both match IBKR exactly (checked afterwards against the Nov 14 IBKR truth), so they are NOT data problems. Not settled by this run: freshness (ran mid-session, every ticker warned), Tradier (breaker opened, 1 of 79 US tickers tested), Canada (one source only).
Measured, not assumed: the app's cache shows Yahoo served 61 of 97 US tickers; the app log shows Twelve Data's breaker opened 82 times ("Rate limit exceeded"). So the app really falls back to Yahoo a lot. **My first explanation (the audit itself used up the limit) was wrong and was retracted.**

### 3. Tradier error handling (plan, Opus review, built, three passes)
Tradier's docs and live probes: over the limit returns HTTP 400 (not 429); an unknown ticker on `/markets/history` also returns 400; `/markets/quotes` answers 200 with `unmatched_symbols`; an empty symbol hangs until the timeout. Old code counted every 400 as "Tradier is broken". Now: "symbol not found" is "no data" (no breaker failure); a quota 400 (body "quota" or `X-Ratelimit-Available` 0) is a rate limit; any other 400 raises a loud `ProviderError`; an empty symbol never sends a request. 61 tests against a throwaway state file (they can never open the live breaker); the tests fail on the old code. Plan: `docs/claude/design/TRADIER_ERROR_HANDLING_PLAN_DAY127.md`.

### 4. Empty price row (found by the page checker, plan, Opus review, built, three passes)
15 cached Yahoo tickers (AAPL, MSFT, META, NVDA, AVGO, LLY, V, WMT, PG, HD, ABBV, KEYS, MRVL, VRT, ALAB) had a Nov 18 newest bar with open/high/low/close all empty but a normal volume, cached 20:58-21:16 ET and kept until today's close. `/api/sr` sent invalid JSON (`"currentPrice": NaN`). My audit missed it because it downloads fresh data and never read the app's own saved copy.
Fix (Opus changed my design): the CACHE stays raw (audit and Data Sources tab must see the hole); the empty rows are dropped when a frame is SERVED (`market_time.drop_empty_close`, called in `orchestrator._deliver` and `split_adjust.fix_frame`, which cover every route and every direct-Yahoo fallback); a frame whose newest close is empty is cached for 30 minutes only; `data_quality.check_history` reads "last bar" as the last bar WITH a price and FAILs an empty newest bar (Data Sources tab and audit C4); `/api/stock` answers 404 instead of a fake price of 0; page checker gets A14 (price answers are valid JSON with a real price; the runner used to only warn). 44 tests; with the fix switched off 17 fail, including the original "invalid JSON NaN". The 15 entries were refreshed one at a time (price history only): all show the real Nov 18 bar; NVDA, KEYS, AAPL and CAT match Tradier to the cent. Plan: `docs/claude/design/EMPTY_PRICE_ROW_PLAN_DAY127.md`.

### 5. Review process
Opus reviewed both plans (GO WITH CHANGES each) and its changes were applied; it also caught five wrong claims in my first plan (see Known Issues). `/three-pass` run and stamped twice. `./run_all_checks.sh --quick` ALL OK; page checker 48/48 on AAPL, SOXL.NE, NVDA, RIVN.

### Files changed (main)
| Area | Files |
|---|---|
| Tradier | `backend/providers/tradier_provider.py`, `backend/test_tradier_errors.py` (new) |
| Empty price row | `backend/market_time.py`, `providers/orchestrator.py`, `split_adjust.py`, `cache_manager.py`, `data_quality.py`, `backend.py` (`/api/stock`), `backtest/audit_data_sources.py`, `backend/test_empty_price_row.py` (new) |
| Page checker | `frontend/scripts/lib/analyzeChecks.js` (A14), `frontend/scripts/test_analyze_checks.mjs` |
| Checks | `run_all_checks.sh` (two new tests) |
| Docs | `docs/claude/design/TRADIER_ERROR_HANDLING_PLAN_DAY127.md`, `EMPTY_PRICE_ROW_PLAN_DAY127.md`, `docs/test/DataSources_20261119/` (INVENTORY.md, REPORT.md) |

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-19 (unchanged from Day 127):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Data Source Audit Round 2: about 40% done
Done: step 0, Analyze-page inventory (draft), truth-free audit (mid-session), Tradier 400 fix, empty-price-row fix and its audit checks. Not done: after-close re-run, IBKR truth (list tickers without a watchlist contract id first), fixes for FINN.NE / XDRV.TO / SOXL.NE (QPUX and DRAL cleared), Twelve Data running out, Data Sources tab statement audit + rare states, other tabs, 117-ticker page audit, framework Part 8.

## Next Session Priorities
1. Re-run the truth-free audit after the 4pm close (freshness, Tradier); measure which provider serves each of the 117.
2. List which of the 117 tickers have a watchlist contract id; then the IBKR truth run. Decide QPUX / DRAL and fix FINN.NE / XDRV.TO / SOXL.NE.
3. Twelve Data pressure: remove the unused 4-hour RSI call (needs a small plan); decide Tradier retry on a stall.
4. Data Sources tab statement audit + Playwright rare states; then Scan, Sectors, Context; then the 117-ticker page audit.
5. Playbook research prompt (ROADMAP #21) and the page-layout review (user to name the 2-3 least intuitive screens; screen-by-screen like the Analyze redesign).
6. Carried: 🔴 High per-ticker provenance (Day 108); the two engine bugs (RSI `|| 50`, missing SPY); page-level horizontal scroll at 390px.
