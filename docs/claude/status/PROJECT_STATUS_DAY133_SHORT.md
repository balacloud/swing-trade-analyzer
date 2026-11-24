# Project Status — Day 133 (Nov 24)

**Version:** App v4.70, Backend v2.58, Frontend v4.66. No STA code change. No API change. Docs only.

---

## What Happened Today

### 1. Layered context (L1 / L2 / L3) for the project docs
Question: is our own context a burden? Yes: `/sta-start` read about 391 KB (about 98k tokens). Plan written, Opus-reviewed (GO WITH CHANGES, 19 amendments applied), built and committed (`73358520`). Plan: `docs/claude/design/LAYERED_CONTEXT_PLAN_DAY133.md`.
- **L1 (read every session, about 77 KB, about 20k tokens):** `CLAUDE_CONTEXT.md`, `GOLDEN_RULES.md` (rules 1-15 and the always-read rules in full, one index line for each other rule), `PERSONA.md` core, `ENGINEER.md`, slim `ROADMAP.md` (open priorities), the latest status, `KNOWN_ISSUES_DAY133.md` (open Medium+ only).
- **L2 (read when the task matches):** `stable/rules/<cluster>.md`, 7 cluster files with the full rule text, word for word.
- **L3 (on request):** `docs/claude/history/` (ROADMAP history, PERSONA log, ENGINEER log, CLAUDE_CONTEXT log, Low and resolved known issues).
- `/sta-start` and `/sta-end` updated; `.claude/check_context_layers.py` (run by `/sta-end` Step 6c, not a hook).
- Nothing deleted. Checks: all 68 rules in exactly one place, byte-identical; no line lost in ROADMAP, CLAUDE_CONTEXT, PERSONA, ENGINEER, KNOWN_ISSUES; hook tests 31/31.
- Cold-start probe (an agent that read only L1): 5 of 5 answered, 0-1 extra file opens. It found two weak spots, both fixed: the ROADMAP pointer now names the heading "Closed priority rows"; the `GOLDEN_RULES.md` header count says 68 rules.

### Files changed (STA repo)
| Area | Files |
|---|---|
| Docs (moved/split) | `GOLDEN_RULES.md`, new `stable/rules/*` (7), `ROADMAP.md`, `CLAUDE_CONTEXT.md`, `PERSONA.md`, `ENGINEER.md`, new `history/*` (5), `KNOWN_ISSUES_DAY133.md` |
| Commands | `.claude/commands/sta-start.md`, `sta-end.md`, new `.claude/check_context_layers.py` |
| Other | `DEVELOPER_ONBOARDING.md` (2 lines), plan file, `MEMORY_MD_BEFORE_LAYERING_DAY133.md`, status board source |
| Memory (outside repo) | `MEMORY.md` trimmed (20 KB to 13 KB), new `project_history_compacted.md`, 2 notes updated |

### Review exemptions (`.claude/.review_log.tsv`)
None this session (no code change). Carried: one `trivial` row from Day 131, "version: footer v4.64 to v4.70 and BACKEND_VERSION 2.57 to 2.58 to match docs".

### Found, not fixed (logged in `history/KNOWN_ISSUES_LOW_AND_RESOLVED.md`)
README roadmap section is stale; `watchlist-report.md:53` cites a PERSONA phrase that no longer exists.

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report` (last job run Nov 23), unchanged:

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
8. Carried: High per-ticker provenance (Day 108).
9. First real use of the layered docs: note whether any index line sent a session to the wrong file, and fix that line.

**Waiting on the user:** Alpaca terms of use; rotate the Twelve Data key; go-ahead to clear the US OHLCV cache once.
