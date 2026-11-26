# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 135 — 2026-11-26

---

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 135 |
| Version | v4.73 (Backend v2.61, Frontend v4.69) |
| Latest Status | PROJECT_STATUS_DAY135_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY135.md |
| Latest API | API_CONTRACTS_DAY135.md |
| Focus | **Next: Data Sources tab statement audit + rare states (provider down, breaker open, empty/stale cache), then Scan/Sectors/Context data audit and the direct provider calls, then the second Canada source plan (ROADMAP #30).** Day 135: `.env` wins over a stale launch environment, saved-prices line, leveraged-fund audit (C11) and header data notes (v4.73). Thin-ETF close differences are NOT pursued (user). Open for the user: rotate the old FRED key in git history, Alpaca terms, Twelve Data key. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in history/CLAUDE_CONTEXT_LOG.md)

### Day 135 Summary (v4.73, Backend v2.61)
- **Data audit refreshed** (117 tickers, after the Nov 24 close, offline replay with `--now`); the stop hook now ignores the generated `data_audit_latest.json`. **`.env` now wins** over a stale launch environment (`backend/env_loader.py`, `/api/health` `env_overridden`).
- **Analyze header** says when prices are a saved copy (VFV.TO: Yahoo rate limit, Canada has one source; `priceFreshness`, A16) and carries two fact lines (`dataNotes`, A17): the Data Sources tab's own thin-data wording (7 of 117 tickers, one shared builder) and, for 19 leveraged funds, the audit's measured comparison with the underlying. No prices changed.
- **Leveraged funds:** audit check C11 (facts only), `reference/leveraged_underlyings.json`, Tradier-blocked grading fixed (NVDL/QPUX no longer FAIL), DRAL/AVGC RS1 audit row fixed (the audit was wrong), QPUX +48% verified with IBKR, NVDL tab line now shows "NVDA x2 that day: +63.0%".
- User decision: thin-ETF close differences (XDRV.TO, CARS.TO, FINN.NE) are not pursued. Data-source work about 85% done (estimate). Plans: `ENV_OVERRIDE`, `STALE_PRICE_AND_LEVERAGED`, `DATA_NOTES`, `NVDL_JUMP_NOTE` (all `_PLAN_DAY135.md`).

### Day 134 Summary (v4.71, Trade Setup void-plan banner)
- **Alpaca was not serving the app** (401, stale env in the parent process); a full restart fixed it. 97 of 138 cached frames are Alpaca now; only RIVN and RSP needed their US cache frames cleared.
- **Trade Setup void rule:** live price strictly below the support zone's low (or the plan stop when there is no zone) gives a plain-facts banner, muted numbers, a last-trade tick and "Sizing is off"; the plan numbers stay at the last close. Plan + Opus review `PLAN_VOID_BELOW_SUPPORT_PLAN_DAY133.md`; three passes, audit 124 PASS / 0 WRONG, page checker 52/52 (A15).
- Priorities: refresh `data_audit_latest.json`, Alpaca startup warning (#29), thin tickers, Data Sources tab statement audit.

### Day 133 Summary (docs only, v4.70 unchanged)
- **Layered the project docs** into L1 (read every session, about 77 KB, was 391 KB), L2 (`stable/rules/<cluster>.md`, full Golden Rule text) and L3 (`docs/claude/history/`). Plan with Opus review: `design/LAYERED_CONTEXT_PLAN_DAY133.md`. Nothing deleted; checked line by line. Commit `73358520`.
- Cold-start probe passed 5 of 5; two weak spots found and fixed. `/sta-start` and `/sta-end` updated; `/sta-end` Step 6c runs `.claude/check_context_layers.py`.
- STA priorities unchanged: Alpaca in-session bar (market day), DRAL RS1 row, refresh `data_audit_latest.json`.


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

1. Data Sources tab statement audit + Playwright rare states (ROADMAP #20), **merged with per-ticker provenance (#16, "never checked" vs "just failed"; user decision Day 135)**.
2. Scan, Sectors, Context data audit; ~17 direct provider calls; 117-ticker page audit (#20).
3. Second Canada source plan + Sectors batch Yahoo spacing (ROADMAP #30).
4. (Per-ticker provenance, ROADMAP #16, is now part of item 1.)
5. Alpaca in-session bar check on a market day (#27); Twelve Data re-measure, `rsi_4h` (#22), Tradier stall retry (#23).
6. Playbook research (#21), page-layout review (#26).
7. Waiting on the user: rotate the old FRED key in git history, Alpaca terms, Twelve Data key.

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
