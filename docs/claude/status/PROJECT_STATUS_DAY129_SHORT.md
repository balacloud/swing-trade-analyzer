# Project Status — Day 129 (Nov 20-22)

**Version:** App v4.69, Backend v2.58, Frontend v4.65 (from v4.68 / v2.57 / v4.64)

---

## What Happened Today

Data Source Audit Round 2 continued ("if that data is wrong the whole compute is wrong"). Three builds, all with a plan, an Opus review, three passes and a stamp. The user asked for plain English throughout and said "i dont want to go in to rabit holes".

### 1. After-close audit re-run (fresh)
The first "after-close" re-run reused the morning cache (Twelve Data volume 800, "session still open" for all 117), so I deleted its outputs and re-ran under `--date 20261119_pm`. Result folder: `docs/test/DataSources_20261119_pm/REPORT.md` (committed in ad05b5ea). Freshness now reads correctly. Tradier was graded for the first time.

### 2. Tradier leveraged-fund rule (plan, Opus review, built, three passes) — commit ad05b5ea
Tradier is the last fallback and is never served for leveraged funds (`providers/fallback_policy.py`, `NO_TRADIER`, 22 symbols). Tradier is not dividend-adjusted and had split errors on QPUX and NVDL. A 60-second failure memo (`_chain_failures`) stops repeated Twelve Data and Yahoo calls for blocked tickers; stale Tradier copies of blocked tickers are refused. The Data Sources tab now adds a `source` check when Tradier served the data (WARN, or FAIL when blocked). Audit check C8 now reads the tab's own checks (`/api/provenance` `quality.checks`) instead of guessing. 32 tests. The v1 plan overclaimed five things (counts, "the tab shows no warning"); the Opus review caught them and v2 fixed them.

### 3. Alpaca as the first US price source (plan, Opus review, built, three passes) — commit 4bdb3546
US chain is now **Alpaca -> Twelve Data -> Yahoo -> Tradier**; Canada stays Yahoo only. Alpaca free plan: 200 calls a minute, daily bars, `feed=sip` hard-coded (`ALPACA_DATA_FEED=iex` in `.env` is ignored), `adjustment=all`, never an `end` parameter (an `end` in the last 15 minutes returns 403). Index converted to New York time and normalized to midnight. Error mapping follows Golden Rules 36/65 (400 "invalid symbol" is no-data; other 400s, 422 and "subscription" 403s are loud and stay out of the breaker). 66 tests.
Real-data acceptance on 79 US tickers vs the saved after-close data: vs Yahoo 100% of closes within 0.5% (96% within 0.1%, volume ratio median 1.00); vs Twelve Data 96% within 0.5% (volume ratio median 0.97). The misses are cases where Alpaca and Yahoo agree and Twelve Data is the odd one (DRAL 2.2%, CVX 0.83%, SPCL 0.62%).
Fixes found by the review, same rollout:
- **Twelve Data 404:** Twelve Data answers HTTP 404 for symbols it lacks (`.TO`, `.NE`, `^VIX`, `BRK-B`). The code had no 404 branch, so it counted a false breaker failure (315 "404 Client Error" lines in `backend.log`). Now `DataNotFoundError`, no failure; Canadian and `^` symbols never reach Twelve Data (no call, no limiter token); `-` is sent as `.`.
- **Key in the log:** the HTTPError text carried the request URL, so the Twelve Data key was written to `backend/backend.log` 324 times (local, gitignored). Error text no longer carries a URL or key. Old lines remain; whether to rotate the key is the user's call.
- **Cache hole 16:00-16:30:** a frame whose newest bar is today (New York) and was fetched before 16:30 now expires at 16:30 (`cache_manager.set_cached_ohlcv` with `market_time.is_forming_bar`), for every source. A mutation check (cap disabled) gave 3 failures.

### 4. Engineer persona — commit d7009e77
New `docs/claude/stable/ENGINEER.md`: the surgeon's lens (evidence before claim, read what the check reads, find every copy, break it before the user does, small and reversible), checklists (data, keys and secrets, exceptions, testing, performance, concurrency, interfaces, process), a "what has been missed" table of about 17 misses from Days 127-129, and a "before you say done" gate. It is the 3rd required read in `/sta-start`, `/three-pass` points at it, and `CLAUDE_CONTEXT.md` lists it.

### 5. Other
- Questrade connector checked (Canada): raw prices (not dividend-adjusted), split-adjusted history, trade-only candles, lists SOXL.TO. IBKR and Questrade connectors are Claude-only (the Flask app cannot use them); only useful for audits.
- A "Data Trail" visual (where each price came from) was mocked up as a private Artifact and **parked** at the user's direction ("as long as our data source tab accommodates this i am fine").
- Process misses logged in ENGINEER.md: the after-close run that reused a cache, a misread "completed" notification, the v1 plan overclaims.

### Files changed (main)
| Area | Files |
|---|---|
| Tradier rule | `backend/providers/fallback_policy.py` (new), `providers/orchestrator.py`, `data_quality.py`, `backend.py` (`/api/provenance`), `backend/test_tradier_fallback_rule.py` (new), `frontend/src/utils/dataSourcesView.js` |
| Alpaca | `backend/providers/alpaca_provider.py` (new), `providers/coverage.py` (new), `providers/orchestrator.py`, `providers/rate_limiter.py`, `providers/twelvedata_provider.py`, `cache_manager.py`, `live_quote.py`, `backend/test_alpaca_provider.py` (new), `reference/provider_coverage.json`, `.env.example` |
| Audit | `backtest/audit_data_sources.py` (Alpaca source, C8 reads the tab), `backtest/audit_vs_ibkr.py` |
| Checks | `run_all_checks.sh` (three new tests) |
| Persona | `docs/claude/stable/ENGINEER.md` (new), `.claude/commands/sta-start.md`, `.claude/commands/three-pass.md`, `docs/claude/CLAUDE_CONTEXT.md` |
| Docs | `docs/claude/design/TRADIER_FALLBACK_RULE_PLAN_DAY129.md`, `ALPACA_PROVIDER_PLAN_DAY129.md`, `docs/test/DataSources_20261119_pm/REPORT.md` |

### Verification
`./run_all_checks.sh --quick` ALL OK; page checker 48/48 (AAPL, SOXL.NE, NVDA, RIVN); `test_tradier_fallback_rule` 32, `test_alpaca_provider` 66.

### Review exemptions (`.claude/.review_log.tsv`)
None. Three plan rows this period: `IBKR_TRUTH_RUN_PLAN_DAY128.md` (Nov 19), `TRADIER_FALLBACK_RULE_PLAN_DAY129.md` (Nov 21), `ALPACA_PROVIDER_PLAN_DAY129.md` (Nov 22), each "three passes done". No `trivial` rows.

## All Gates Status
No live forward-test gates (program discontinued Day 113). Unchanged from Day 128 (`daily_job.py --report`):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Data Source Audit Round 2: about 60% done
Done: step 0, inventory (draft), truth-free audit (mid-session and after close), Tradier 400 fix, empty-price-row fix, IBKR truth (63 of 117), Tradier leveraged-fund rule, Alpaca first US source, Twelve Data 404/key-leak fixes, forming-bar cache cap. Not done: refresh `backend/reference/data_audit_latest.json` with the after-close and Alpaca results, Alpaca in-session bar check, Data Sources tab statement audit + rare states, other tabs, 117-ticker page audit, framework Part 8.

## Open for the user
- **Alpaca terms of use:** no Alpaca-specific data terms found; the exchange agreements limit non-professional use to personal, non-business use. Local single-user use looks consistent. Do not put Alpaca-sourced prices in shared Artifacts (Beginner Playbook, Status Board).
- **Rotate the Twelve Data key?** Your call (it sits in the local gitignored `backend/backend.log`).
- **Rollout:** AAPL still showed Yahoo from the old cache. Either clear the US OHLCV cache once (needs your go-ahead) or accept temporary C8 "fell through" WARNs until frames expire.

## Next Session Priorities
1. Check Alpaca's in-session daily bar on a market day (today bar, tab, 3 tickers; page checker).
2. Refresh `backend/reference/data_audit_latest.json` (the Data Sources tab's file) with the after-close and Alpaca results (needs plan + stamp).
3. Decide the thin-ETF cases (XDRV.TO, CARS.TO: no-trade-day conventions, not Yahoo errors), SOXL.NE (Questrade SOXL.TO as a source?), FINN.NE (22 bad bars), BRKU volume.
4. Twelve Data pressure should now be much lower (Alpaca first); re-measure from the cache, then decide the unused `rsi_4h` call (ROADMAP #22) and a Tradier stall retry (#23).
5. Data Sources tab statement audit, then Scan, Sectors, Context; then the 117-ticker page audit.
6. Playbook research (ROADMAP #21) and the page-layout review (#26).
7. Carried: 🔴 High per-ticker provenance (Day 108); two engine bugs (RSI `|| 50`, missing SPY).
