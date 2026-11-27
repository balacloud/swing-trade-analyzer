# Project Status — Day 136 (Nov 27)

**Version:** App v4.74, Backend v2.62, Frontend v4.70. Backend API addition (documented in `API_CONTRACTS_DAY136.md`); Data Sources tab line.

---

## What Happened Today

### 1. The tab can now tell "never checked" from "just failed" (ROADMAP #16 + #20, merged by the user Day 135)
New attempt log: `backend/providers/attempt_log.py`, table `fetch_attempts` in the shared `provider_state.db`, one row per (ticker, prices|fundamentals). The orchestrator records the last real provider answer or failure (a cache hit records nothing); the legacy direct-Yahoo path in `/api/stock` records too. `/api/provenance` gained `ohlcv.attempt` and `fundamentals.attempt`; the tab line reads "no provider check recorded by this app yet", "answered by X at T", or "failed at T (alpaca:RateLimitError), saved data was shown instead; last success T by X". Stored detail is provider and exception class names only (never error text: URLs can hold keys). A write failure is logged and never breaks a fetch. Plan + Opus review ("GO WITH CHANGES"): `DATA_SOURCES_PROVENANCE_PLAN_DAY136.md`.

### 2. Tab wording fixed after the statement audit
"Just fetched" (a guess from cache age) removed; a provider with no API key shows "no key" instead of a green "ok"; the cache-lifetime sentence now names the exceptions (unfinished bar or short source expires sooner).

### 3. Statement audit and rare-state test
`backend/audit_data_sources_tab.py` grades every sentence (DS-0 to DS-23) against the cache, breaker/limiter/attempt databases, coverage file and chains: 96 PASS, 0 WRONG, 0 MISLEADING, 27 UNVERIFIED with reasons (baseline before fixes: 1 MISLEADING). `test_data_sources_rare_states.js` plants payloads in the real page: provider down, breaker open, quota 0, no key, empty and expired cache, failed and unreadable attempt, old backend, FAIL quality, 500 on each endpoint, Retry. 25 checks pass; mutation-checked. New page check A18. Report: `docs/test/DataSourcesTab_final/REPORT_DATASOURCES_TAB.md`.

### 4. Found and fixed along the way
Three older backend tests could have marked NVDL and VFV.TO "last fetch failed" in the live state file (now redirected, guard test added). A legacy-path gap and an unknown-state display were found by passes 1 and 2. The Market Backdrop audit tolerance (0.011) gave 8 false WRONGs; now 0.0501. The long report path overflowed at phone width; wrapped. Headless 'new' hangs here: the new scripts default to 'shell'.

### Tests at close
Backend: test_attempt_log 31, test_provenance_route 11, test_price_basis 21, test_alpaca_provider 66, test_tradier_fallback_rule 32, test_price_freshness 22, 0 failed. Frontend: test_data_sources_view 71, test_analyze_checks 251, 0 failed. Page checker 64/64 on AAPL SOXL.NE NVDA RIVN. Rare states 25/25. Smoke audit 0 WRONG.

### Files changed
| Area | Files |
|---|---|
| Backend | `providers/attempt_log.py` (new), `providers/orchestrator.py`, `backend.py` (v2.62, `/api/provenance`, legacy path), `audit_data_sources_tab.py` (new), `audit_cards2.py` |
| Frontend | `src/utils/dataSourcesView.js`, `src/components/DataSourcesTab.jsx`, `src/App.jsx` (v4.74), `scripts/lib/readDataSourcesTab.js` (new), `scripts/dump_data_sources_tab.js` (new), `scripts/test_data_sources_rare_states.js` (new), `scripts/lib/analyzeChecks.js` (A18), `scripts/ui-verify-checklist.js` |
| Tests | `test_attempt_log.py`, `test_provenance_route.py` (new); redirect added to `test_price_basis.py`, `test_tradier_fallback_rule.py`, `test_price_freshness.py`, `test_alpaca_provider.py`; `test_analyze_checks.mjs`, `test_data_sources_view.mjs`; `run_all_checks.sh` |
| Docs | plan file, this status, `KNOWN_ISSUES_DAY136.md`, `API_CONTRACTS_DAY136.md`, ROADMAP, README, CLAUDE_CONTEXT |

### Review exemptions (`.claude/.review_log.tsv`)
No `trivial` exemption was used on Day 136; one stamp with a plan (21 files). Older trivial rows still in the log: 2026-11-23 "version: footer v4.64 to v4.70 and BACKEND_VERSION 2.57 to 2.58" (8 files), 2026-11-25 "version: footer v4.70 to v4.71" (10 files).

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report` (last job run Nov 26), unchanged:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | n/a |
| Path B | 232 | 42.24% | 0.87 | n/a (retired Day 112) |

## Next Session Priorities
1. Scan, Sectors, Context data audit and the ~17 direct provider calls that bypass the chain; the 117-ticker page audit.
2. Second Canada source plan (ROADMAP #30: EODHD is 20 calls/day) and spacing Yahoo calls in the Sectors batch.
3. Alpaca in-session bar check on a market day.
4. Twelve Data re-measure and `rsi_4h` (#22); Tradier stall retry (#23); framework Part 8.
5. Playbook research (#21), page-layout review (#26; includes the 390 px tab-strip overflow).

**Waiting on the user:** rotate the old FRED key committed in `docs/claude/versioned/archive/KNOWN_ISSUES_DAY62.md` (line 88); Alpaca terms of use; Twelve Data key rotation.
