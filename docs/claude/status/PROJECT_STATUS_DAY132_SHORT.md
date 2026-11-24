# Project Status — Day 132 (Nov 23-24)

**Version:** App v4.70, Backend v2.58, Frontend v4.66. No STA code change. No API change.

---

## What Happened Today

### 1. Session start, then a non-STA task
Ran `/sta-start` (Day 131 state). Most of the session went on a personal task outside STA at the user's request; it is not part of this project and its details are deliberately kept out of the repo. One process lesson from it went into `ENGINEER.md`.

### 2. STA state check
No STA code or docs changed except this close. Plan for the Alpaca in-session check confirmed: it needs market hours (opens 09:30 ET Tue Nov 24); the DRAL RS1 row and the `data_audit_latest.json` refresh follow it.

### Files changed (STA repo)
| Area | Files |
|---|---|
| Docs | this file, `KNOWN_ISSUES_DAY132.md`, `CLAUDE_CONTEXT.md`, `ENGINEER.md` (one miss row + log entry), status board source |

### Review exemptions (`.claude/.review_log.tsv`)
None this session (no code change). Carried from Day 131: one `trivial` row, "version: footer v4.64 to v4.70 and BACKEND_VERSION 2.57 to 2.58 to match docs".

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report`, pulled Nov 24 (last job run Nov 23), unchanged from Day 131:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. Alpaca in-session daily bar on a market day (after 09:30 ET): today's bar, the Data Sources tab for 3 tickers, `cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`. Read the audit and Alpaca plans first.
2. Fix or explain the DRAL RS1 smoke-audit row.
3. Refresh `backend/reference/data_audit_latest.json` (plan, Opus review, stamp), after 1 and 2.
4. Thin-ETF cases (XDRV.TO, CARS.TO), SOXL.NE, FINN.NE, BRKU volume.
5. Twelve Data pressure re-measure, `rsi_4h` (#22), Tradier stall retry (#23).
6. Data Sources tab statement audit, then Scan, Sectors, Context; the 117-ticker page audit.
7. Playbook research (#21), page-layout review (#26).
8. Carried: 🔴 High per-ticker provenance (Day 108).

**Waiting on the user:** Alpaca terms of use; rotate the Twelve Data key; go-ahead to clear the US OHLCV cache once.
