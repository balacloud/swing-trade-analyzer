# Project Status — Day 130 (Nov 22)

**Version:** App v4.69, Backend v2.58, Frontend v4.65 (unchanged). Docs-only session, no app code touched.

---

## What Happened Today

### 1. Session start and a question about the engineer persona
Ran `/sta-start` (Day 129 state: 17 Medium+ open bugs, paper-trading job last ran Nov 20, within 3 days, and the program is discontinued anyway). The user asked how the engineer persona works; explained `ENGINEER.md` (five habits, the plan-review-build-prove-report cycle, checklists, the "missed" table, what the Stop hook does and does not enforce).

### 2. "Check all the days" — persona vs the whole history
The "what has been missed" table covered Days 127-129 in detail but only a short theme list for earlier days, skipping about half the Golden Rules. Checked it against the Golden Rules, the PERSONA log and the Day 64-129 update log, and added 12 themes to `ENGINEER.md`:
backtest honesty (18, 20, 45, 56); live/backtest parity and DRY (21, 35); replay reads stored entry values (27); backgrounded server stdout (23); rate-limit pool widening (25); scheduler timezone (33); a cited source that did not exist (37); one column with two meanings (38); one glyph hiding four states (44); design locked without challenge (49-51); broker id from symbol search (58); units guessed by size (61).
Found a real doc problem: `GOLDEN_RULES.md` has **no Rule 27** (numbering jumps 26 to 28); the replay rule is numbered 29 but cited as "Rule 27" in `CLAUDE_CONTEXT.md` and the ROADMAP. The header's "68 rules" is 67. Logged in the persona file, not renumbered (user chose docs-only close).
Limits stated to the user: the 112 status files were not read line by line; the `CLAUDE_CONTEXT.md` update log lacks rows for Days 71, 120-123, 126, 127.
Committed and pushed: `f9c5e72b`.

### 3. "Push all the files"
321 untracked entries (1,212 files after expanding folders). Scanned for secrets first: the only hits were placeholder text in `docs/research/context_tab_complete_spec.md` (13-character "your_key" values) and a log. Pushed 1,212 files (commit `fa38621e`). Left out on purpose: `.venv` and `node_modules` under `docs/Options_Reference_for_Build/` (about 200 MB, another project), the `.db` there, all `.log` files, `.playwright-mcp/`, `.vscode/`.

### 4. "What is next"
Answered: Alpaca's in-session bar check has to wait for a market day (today is Sunday); the refresh of `data_audit_latest.json` is the best work available now.

### Files changed
| Area | Files |
|---|---|
| Persona | `docs/claude/stable/ENGINEER.md` (12 theme rows, Rule 27 note, date) |
| Bulk push | 1,212 research / audit / backtest files (no code) |
| Close | this file, `KNOWN_ISSUES_DAY130.md`, `CLAUDE_CONTEXT.md`, `STA_STATUS_BOARD.html` |

### Review exemptions (`.claude/.review_log.tsv`)
No `trivial` rows. Plan rows (carried from Day 129): `IBKR_TRUTH_RUN_PLAN_DAY128.md`, `TRADIER_FALLBACK_RULE_PLAN_DAY129.md`, `ALPACA_PROVIDER_PLAN_DAY129.md`, each "three passes done". No code changed today, so no new row.

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report`, pulled Nov 22 (last job run Nov 20):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. Check Alpaca's in-session daily bar on a market day (Monday Nov 23 or later): today's bar, the Data Sources tab for 3 tickers, `cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`.
2. Refresh `backend/reference/data_audit_latest.json` with the after-close and Alpaca results (plan, Opus review, stamp).
3. Decide the thin-ETF cases (XDRV.TO, CARS.TO), SOXL.NE (Questrade SOXL.TO as a source?), FINN.NE (22 bad bars), BRKU volume.
4. Re-measure Twelve Data pressure now that Alpaca is first; then the unused `rsi_4h` call (ROADMAP #22) and a Tradier stall retry (#23).
5. Data Sources tab statement audit, then Scan, Sectors, Context; then the 117-ticker page audit.
6. Playbook research (ROADMAP #21) and the page-layout review (#26).
7. Carried: 🔴 High per-ticker provenance (Day 108); two engine bugs (RSI `|| 50`, missing SPY).

**Waiting on the user:** Alpaca terms of use; rotate the Twelve Data key (old lines in local `backend.log`); a go-ahead to clear the US OHLCV cache once so Alpaca data replaces old Yahoo frames.
