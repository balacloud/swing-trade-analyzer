# Project Status — Day 134 (Nov 24-25)

**Version:** App v4.71, Backend v2.58, Frontend v4.67. Frontend card change. No API change.

---

## What Happened Today

### 1. Alpaca was not actually serving the app (found and fixed)
The user asked for the Alpaca in-session check. It showed Alpaca returning HTTP 401, the breaker open, and the chain quietly falling through to Twelve Data. Cause: stale keys in the long-lived parent process environment (`load_dotenv` does not override existing variables). Fix: full `./stop.sh` and `./start.sh`. After that, 97 of 138 cached frames are Alpaca.

### 2. Trade Setup says so when the live price has already broken the plan (SOXL.NE, v4.71)
Screenshots showed Entry checks at $8.54 while Trade Setup said Buy $10.73 and "wait for a dip to support". Cause: two cards use two "now" prices (a Day 126 design choice: the plan uses the last completed close, Entry checks uses the live quote). It fails when price falls through the whole plan.
- New rule, no tuned numbers: a usable live price strictly below the nearest support zone's low voids the plan (`below_support`); with no zone, strictly below the plan stop (`below_stop`). Only `live` and `recent` quote states void; pre-market and after-hours show one muted fact line. The plan numbers do not move with live ticks.
- When void: red banner with plain facts, muted numbers, an amber "last trade" tick on the bar, "Sizing is off" instead of "Size this plan", and a Key Levels note ("Measured at the last close ($X), not the live price.").
- Plan with Opus review (GO WITH CHANGES, applied): `docs/claude/design/PLAN_VOID_BELOW_SUPPORT_PLAN_DAY133.md`. Three passes done and stamped. Pass 2 found and fixed two real bugs (a Key Levels note beside "no pullback plan"; the page check demanding a tick in the no-ATR state).
- Checked on real data: SOXL.NE ($8.54 vs zone $9.22-$10.73) and NVDA ($153 vs $163.89) both void live; closed-market view identical to before. Audit 124 PASS / 0 WRONG; page checker 52/52 (new A15); suite ALL OK; tests 54 + 216 + 48 (mutation-checked).

### 3. US OHLCV cache cleared (user's go-ahead)
Measured first: 97 Alpaca, 39 Yahoo, 2 Twelve Data frames. Only RIVN and RSP were old US frames; cleared those two only (`/api/cache/clear?ticker=X&type=ohlcv`), both refetched as Alpaca. The other Yahoo frames are Canada tickers and `^VIX` (Yahoo by design).

### Files changed
| Area | Files |
|---|---|
| Frontend | new `src/utils/planStatus.js`; `src/components/PullbackPlan.jsx`, `KeyLevels.jsx`; `src/App.jsx` (wiring, footer v4.71) |
| Audit / tests | `backend/audit_cards.py`, `backend/test_audit_cards.py`, `frontend/scripts/lib/analyzeChecks.js`, `test_analyze_checks.mjs`, new `test_plan_status.mjs`, `ui-verify-checklist.js` |
| Docs | plan file, this status, `KNOWN_ISSUES_DAY134.md`, ROADMAP, README, CLAUDE_CONTEXT, history logs |

### Review exemptions (`.claude/.review_log.tsv`)
One `trivial` row this close: "version: footer v4.70 to v4.71" (no logic). Carried older row: Day 131 version-string alignment. The void-plan change itself used a full plan and review.

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report` (last job run Nov 24), unchanged:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | n/a |
| Path B | 232 | 42.24% | 0.87 | n/a (retired Day 112) |

## Next Session Priorities
1. Refresh `backend/reference/data_audit_latest.json` with the after-close and Alpaca results (plan, Opus review, stamp). Run the 117-ticker audit in the background and read only the summary.
2. Alpaca startup warning for a stale `.env` or launch environment (new Medium; plan, Opus review, stamp).
3. Decide the thin tickers in one question: XDRV.TO, CARS.TO, SOXL.NE, FINN.NE, BRKU volume.
4. Data Sources tab statement audit (+ Playwright rare states), then Scan, Sectors, Context; the 117-ticker page audit.
5. DRAL RS1 smoke-audit row.
6. Twelve Data re-measure, `rsi_4h` (#22); Tradier stall retry (#23).
7. Playbook research (#21), page-layout review (#26). Carried: High per-ticker provenance (Day 108).

**Waiting on the user:** Alpaca terms of use; Twelve Data key rotation.
