# Project Status — Day 135 (Nov 25-26)

**Version:** App v4.73, Backend v2.61, Frontend v4.69. Backend API changes (documented in `API_CONTRACTS_DAY135.md`); frontend header lines.

---

## What Happened Today

### 1. Data audit refreshed (117 tickers) and the stop hook fixed
Ran the truth-free audit after the Nov 24 close. A pre-market run counts today as an expected session (116 false "1 session behind" warnings), so the final copy is an offline replay of the saved bars with `--now 2026-11-24T17:00` (no provider calls; a second live re-run lost EODHD data for 9 Canadian tickers because the free quota was spent). The stop hook counted the generated `data_audit_latest.json` as code and refused a data-only stamp; the user chose to exclude it (only that file: `known_splits.json` still counts).

### 2. `.env` now wins over a stale launch environment (ROADMAP #29, done)
`backend/env_loader.py` replaces all 6 `load_dotenv` calls. A non-empty `.env` value wins; the log and `/api/health` (`env_overridden`) name the replaced KEY NAMES only; `STA_ENV_OVERRIDE=0` keeps the old behaviour. Opus review caught the 6th/7th call sites, a test that would have been overridden, and the reloader child process hiding the result from `/api/health`. Plan `ENV_OVERRIDE_PLAN_DAY135.md`.

### 3. Saved prices are now said on the Analyze header (VFV.TO, v4.72)
VFV.TO served saved prices on Nov 24 at 6:02 pm (Yahoo rate limit; Canada has one source). New `priceFreshness` on `/api/stock`, `utils/priceFreshness.js`, page check A16. Rule: warn only when the orchestrator marked the frame as a saved copy (the marker rides on `df.attrs`) or the Data Sources tab's own tolerant rule says WARN/FAIL (3+ sessions behind); no new threshold. Plan `STALE_PRICE_AND_LEVERAGED_PLAN_DAY135.md`.

### 4. Leveraged funds
Measured on saved bars: single-stock 2x funds track their stock almost exactly; SOXL follows SOXX (corr 0.999), not SMH; SOXL.NE follows SOXL (corr 0.999 after the split table). New audit check **C11** (facts only, level NA) with `reference/leveraged_underlyings.json`; the audit no longer grades Tradier for Tradier-blocked funds (NVDL/QPUX stopped failing C5); DRAL/AVGC "RS1" smoke-audit row fixed (the audit was wrong, the page right). **QPUX +48% on 2026-05-21 verified real with IBKR** (all four sources match IBKR). NVDL +61.7% = 2 x NVDA +31.5%.

### 5. Header data notes (v4.73)
`dataNotes` on `/api/stock`: a thin-data line (the Data Sources tab's own integrity wording from ONE shared builder `data_quality.cached_quality`; 7 of 117 tickers today, all thin Canadian funds) and, for 19 mapped leveraged funds, the audit's measured comparison with the underlying. Page check A17. No prices changed. Opus review caught that the page and the tab would have used different copies of the data.

### 6. NVDL audit line
The tab's audit line for NVDL now reads "...needs IBKR; NVDA x2 that day: +63.0%)" (`data_quality.annotate_jumps`, exact-date match, level unchanged). Plan `NVDL_JUMP_NOTE_PLAN_DAY135.md`.

### Decision (user, Day 135)
Thin-ETF close differences (XDRV.TO, CARS.TO, FINN.NE) are **not pursued**; the header shows the integrity wording only. The real fix is the second Canada source (ROADMAP #30).

### Files changed
| Area | Files |
|---|---|
| Backend | `env_loader.py` (new), `backend.py`, `data_quality.py`, `providers/orchestrator.py`, `providers/__init__.py`, `providers/backtest_adapter.py`, `backtest/audit_data_sources.py`, `backtest/simfin_loader.py`, `backtest/backtest_adx_rsi_thresholds.py`, `audit_cards.py`, `reference/leveraged_underlyings.json` (new), `reference/data_audit_latest.json` |
| Frontend | `src/utils/priceFreshness.js`, `src/utils/dataNotes.js` (new), `src/services/api.js`, `src/App.jsx`, `scripts/lib/analyzeChecks.js` (A16, A17), `scripts/ui-verify-checklist.js` |
| Tests | `test_env_loader.py`, `test_price_freshness.py`, `test_leveraged_tracking.py` (62), `test_data_notes.py` (27), `test_audit_cards.py`, `test_price_freshness.mjs`, `test_data_notes.mjs`, `test_api_stock_passthrough.mjs`, `test_analyze_checks.mjs` (A16/A17) |
| Process | `.claude/hooks/three_pass_check.sh` (+ test), `run_all_checks.sh` |
| Docs | four plan files (`ENV_OVERRIDE`, `STALE_PRICE_AND_LEVERAGED`, `DATA_NOTES`, `NVDL_JUMP_NOTE`), this status, `KNOWN_ISSUES_DAY135.md`, `API_CONTRACTS_DAY135.md`, ROADMAP, README, CLAUDE_CONTEXT, history logs |

### Review exemptions (`.claude/.review_log.tsv`)
No `trivial` exemption was used on Day 135; every code change had a plan, an Opus review, three passes and a stamp (four stamps). Older trivial rows still in the log: 2026-11-23 "version: footer v4.64 to v4.70 and BACKEND_VERSION 2.57 to 2.58" (8 files), 2026-11-25 "version: footer v4.70 to v4.71" (10 files).

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report` (last job run Nov 25), unchanged:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | n/a |
| Path B | 232 | 42.24% | 0.87 | n/a (retired Day 112) |

## Next Session Priorities
1. Data Sources tab statement audit (+ Playwright rare states: provider down, breaker open, empty or stale cache, quota 0), **merged with per-ticker provenance (item 4 below, ROADMAP #16): user decided Day 135 to do them together, since the rare states need the same per-provider attempt record.**
2. Scan, Sectors, Context data audit and the ~17 direct provider calls that bypass the chain; the 117-ticker page audit.
3. Second Canada source plan (ROADMAP #30: EODHD is 20 calls/day) and spacing Yahoo calls in the Sectors batch.
4. Per-ticker provenance, "never checked" vs "just failed" (High, Day 108): merged into item 1.
5. Alpaca in-session bar check on a market day (the Nov 25 session is complete now).
6. Twelve Data re-measure and `rsi_4h` (#22); Tradier stall retry (#23); framework Part 8.
7. Playbook research (#21), page-layout review (#26).

**Waiting on the user:** rotate the old FRED key committed in `docs/claude/versioned/archive/KNOWN_ISSUES_DAY62.md` (line 88); Alpaca terms of use; Twelve Data key rotation.
