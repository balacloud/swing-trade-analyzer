# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 133 — 2026-11-24

---

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 133 |
| Version | v4.70 (Backend v2.58, Frontend v4.66) |
| Latest Status | PROJECT_STATUS_DAY133_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY133.md |
| Latest API | API_CONTRACTS_DAY129.md |
| Focus | **Next: Alpaca in-session daily-bar check on a market day (after 09:30 ET), then the DRAL RS1 smoke-audit row, then refresh `data_audit_latest.json` (ROADMAP #20). Day 133: docs layered into L1/L2/L3 (see below).** Open for the user: Alpaca terms, Twelve Data key rotation, go-ahead to clear the US OHLCV cache once. The old long Focus text is in `history/CLAUDE_CONTEXT_LOG.md`. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in history/CLAUDE_CONTEXT_LOG.md)

### Day 133 Summary (docs only, v4.70 unchanged)
- **Layered the project docs** into L1 (read every session, about 77 KB, was 391 KB), L2 (`stable/rules/<cluster>.md`, full Golden Rule text) and L3 (`docs/claude/history/`). Plan with Opus review: `design/LAYERED_CONTEXT_PLAN_DAY133.md`. Nothing deleted; checked line by line. Commit `73358520`.
- Cold-start probe passed 5 of 5; two weak spots found and fixed. `/sta-start` and `/sta-end` updated; `/sta-end` Step 6c runs `.claude/check_context_layers.py`.
- STA priorities unchanged: Alpaca in-session bar (market day), DRAL RS1 row, refresh `data_audit_latest.json`.

### Day 132 Summary (no STA code change — v4.70 unchanged)
- Most of the session went on a non-STA task (kept out of the repo on purpose).
- Corrected my own overclaim (a "match" that used an estimated input); added a row to `ENGINEER.md`.
- STA priorities unchanged: Alpaca in-session bar (needs market hours), DRAL RS1 row, refresh `data_audit_latest.json`. Waiting on the user: Alpaca terms, Twelve Data key rotation, US cache clear.

### Day 131 Summary (engine bugs fixed — v4.70, Golden Rule 69)
- **Missing RSI** no longer counts as 50 (cannot be Strong; may be Decent with 5+ trend checks; a real 0 is kept). **Missing SPY** still gives Unfavorable (no BUY, user's choice) but says "SPY trend unavailable" instead of "below its 200-day". JS and Python changed together; parity grid 172,800 rows, 0 mismatches; original rows unchanged; mutation-checked; two false Technical Read texts fixed. Plan + Opus review: `ENGINE_MISSING_INPUTS_PLAN_DAY131.md`.
- **My own wrong claim corrected:** "the MR route reads Yahoo directly" (stale Known Issues line, Days 128-130) was false; it uses the provider chain first. No code change. Golden Rule 69.
- Version strings in code (footer v4.64, backend 2.57) brought up to the docs. Found, not fixed: smoke audit DRAL RS1 row (predates today).

## HOW THE DOCS ARE LAYERED (Day 133)

- **L1, read at every `/sta-start`:** this file, `stable/GOLDEN_RULES.md` (index + always-read rules), `stable/PERSONA.md`, `stable/ENGINEER.md`, `stable/ROADMAP.md` (open priorities only), the latest `status/PROJECT_STATUS_DAY[N]_SHORT.md`, `versioned/KNOWN_ISSUES_DAY[N].md` (open Medium+ only).
- **L2, read when the task touches the area:** `stable/rules/<cluster>.md` (full Golden Rule text). Open the cluster when an index line in `GOLDEN_RULES.md` matches your task.
- **L3, read on request:** `docs/claude/history/` (ROADMAP history, PERSONA log, ENGINEER log, CLAUDE_CONTEXT log, Low and resolved known issues).

| If the task is about... | Read first |
|---|---|
| A Golden Rule number or its full text | `stable/rules/<cluster>.md` (cluster named in the index) |
| A closed ROADMAP priority, an old day's version note, a COMPLETE section | `history/ROADMAP_HISTORY.md` |
| Why the persona said something on a past day | `history/PERSONA_LOG.md` |
| An old miss or the engineer log | `history/ENGINEER_LOG.md` |
| A Low or resolved known issue | `history/KNOWN_ISSUES_LOW_AND_RESOLVED.md` |
| Old session summaries, old priority lists, the update log | `history/CLAUDE_CONTEXT_LOG.md` |
| Data providers, caches, audits | `rules/data-providers.md`, `rules/cache-time-audit.md`, `design/` audit plans |
| Verdict engine or backtests | `rules/engine-parity.md`, `rules/backtest-honesty.md` |

---

## SESSION START PROTOCOL

Single source: `.claude/commands/sta-start.md`. Read the L1 files above, report Day, version, open Medium+ bugs, the paper-trading dead-man check and the priorities, then ask what to focus on. The old text is in `history/CLAUDE_CONTEXT_LOG.md`.

### Rules During Session:
- STOP before coding — understand problem first
- READ files before modifying them
- RUN diagnostics before writing fixes
- TEST incrementally — one change at a time
- Every code change: plan (plan mode) -> `docs/claude/design/*_PLAN_*.md` with an Opus review verdict -> build -> `/three-pass` -> stamp with `--plan <file>`; only trivial changes may use `--trivial "kind: reason"` (hook-enforced, Golden Rules 55 and 64)
- If fix fails, STOP and diagnose — don't chain guesses
- NEVER ask user to manually update files — Claude does it
- NEVER provide git commands — Claude commits AND pushes

---

## SESSION CLOSE PROTOCOL

Single source: `.claude/commands/sta-end.md`. Claude runs every step and never asks the user to do one. The old step list is in `history/CLAUDE_CONTEXT_LOG.md`.

---

## SESSION RESUME PROTOCOL (After Context Limit)

```
1. READ the summary provided
2. READ PROJECT_STATUS for context
3. READ KNOWN_ISSUES for active bugs
4. Resume the task in progress
5. Do NOT ask user to re-explain
```

---

## NEXT SESSION PRIORITIES (one-line references; detail lives in the file named)

No freeze, no live gates. STA is an on-demand analysis tool (paper trading discontinued Day 113). Pick by what the user wants. Source of truth: the latest `PROJECT_STATUS_DAY[N]_SHORT.md` "Next Session Priorities" and `ROADMAP.md` "OPEN PRIORITIES".

1. Alpaca in-session daily bar check on a market day, then the Data Sources tab for 3 tickers (ROADMAP #20, #27).
2. DRAL RS1 smoke-audit row (KNOWN_ISSUES, Low-Medium).
3. Refresh `backend/reference/data_audit_latest.json` (ROADMAP #20).
4. Thin ETFs (XDRV.TO, CARS.TO), SOXL.NE, FINN.NE, BRKU volume (ROADMAP #20).
5. Twelve Data re-measure, `rsi_4h` (ROADMAP #22), Tradier stall retry (#23).
6. Data Sources tab statement audit, then Scan, Sectors, Context; 117-ticker page audit (ROADMAP #20).
7. Playbook research (ROADMAP #21), page-layout review (#26).
8. Carried: per-ticker provenance (High, Day 108, ROADMAP #16).

## FILE STRUCTURE REFERENCE

```
/docs/claude/
├── CLAUDE_CONTEXT.md              <- THIS FILE (single reference)
├── stable/                        <- Rarely change
│   ├── GOLDEN_RULES.md           <- Index + always-read rules (Day 133)
│   ├── rules/                    <- L2: full text of Golden Rules by cluster
│   ├── PERSONA.md                <- Trading-judgment lens (30yr veteran persona) + Feedback Log
│   ├── ENGINEER.md               <- Engineer's lens (surgical developer persona) + the table of what has been missed + Feedback Log
│   ├── ROADMAP.md                <- Canonical roadmap
│   └── MASTER_AUDIT_FRAMEWORK.md <- Canonical audit protocol (5 types)
├── history/                       <- L3: append-only history (read on request)
├── design/                        <- Feature design specs + audit reports
│   ├── PRICE_STRUCTURE_CARD_SPEC.md  <- v2, audited (Day 72)
│   └── PRICE_STRUCTURE_CARD_AUDIT.md <- 10 findings self-audit (Day 72)
├── versioned/                     <- Day-versioned (active last 15 days)
│   ├── API_CONTRACTS_DAY[N].md   <- API reference
│   ├── KNOWN_ISSUES_DAY[N].md    <- Bug tracker
│   ├── COHERENCE_AUDIT_DAY[N].md <- Audit reports
│   └── archive/                   <- Older than 15 days
└── status/                        <- Daily status
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                   <- Older than 15 days
```
*(Day 82: removed `backup_pre_cleanup_day68/` — a tracked backup zip redundant with git history itself; deleted in the Fable hygiene pass.)*

---

## QUICK COMMANDS

```bash
# Start/Stop services — run from project root
./start.sh               # Start both backend and frontend
./stop.sh                # Stop both services

# Find latest day number
ls docs/claude/status/ | grep PROJECT_STATUS | tail -1

# Cache status
curl http://localhost:5001/api/cache/status

# Paper trading ledger status (Day 81 — automated engine)
cd backend && venv/bin/python paper_trading/daily_job.py --report

# Manually trigger the daily paper-trading job (normally runs via launchd)
cd backend && venv/bin/python paper_trading/daily_job.py --force

# Check/disable the launchd scheduler
launchctl list | grep sta.papertrading
launchctl unload ~/Library/LaunchAgents/com.sta.papertrading.daily.plist

# Dead-man check (Day 82) — last date the paper-trading job actually ran
sqlite3 backend/validation_results/paper_trading_ledger.db "SELECT MAX(run_date) FROM job_runs;"
```

---
