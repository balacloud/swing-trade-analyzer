# Session Start — Swing Trade Analyzer

Execute the full STA session start protocol. Do every step in order. Do not skip any.

## Step 1: Read CLAUDE_CONTEXT.md first

Read `docs/claude/CLAUDE_CONTEXT.md`.

Extract from it:
- Current Day N (from CURRENT STATE table)
- Current version string (Backend vX, Frontend vY)
- The Day N summary (1-line description of last session)
- Next Session Priorities list

## Step 2: Read the layer-1 files (layered docs, Day 133)

Read all six — do not skip any. These are layer L1, small on purpose. The full text of Golden Rules is layer L2 and history is layer L3: **do not read them now; open them when the task needs them** (see the rule below).

1. `docs/claude/stable/GOLDEN_RULES.md` — rules 1-15 and the always-read rules in full, plus one index line per other rule
2. `docs/claude/stable/PERSONA.md` — the trading-judgment persona (30-year veteran trader lens). Load it as an active decision-making filter for this session, not just background reading — apply it to any threshold decision, backtest/live result interpretation, or "can we speed this up" request.
3. `docs/claude/stable/ENGINEER.md` — the surgeon's lens (engineer persona, Day 129). Load it as an active filter for every plan and code change: evidence before claim, read what the check reads, find every copy, break it before the user does, and re-read its "what has been missed" table before planning.
4. `docs/claude/stable/ROADMAP.md` — open priorities only
5. `docs/claude/status/PROJECT_STATUS_DAY[N]_SHORT.md` — use the Day N you found in Step 1
6. `docs/claude/versioned/KNOWN_ISSUES_DAY[N].md` — use the Day N you found in Step 1 (open Medium+ only)

**Layer rule (L2/L3):** when the task matches an index line in `GOLDEN_RULES.md`, open that cluster file `docs/claude/stable/rules/<cluster>.md` and read the full rule BEFORE acting. Closed priorities, old day notes, the persona and engineer logs, and Low or resolved known issues are in `docs/claude/history/` (read on request). `CLAUDE_CONTEXT.md` has a "when the task is about X, read Y" map.

## Step 3: Count open bugs

From KNOWN_ISSUES, count issues at severity Medium or higher (ignore Info-level).

## Step 4: Check the paper-trading job hasn't gone silent (Day 82 dead-man check)

The automated paper-trading engine (`backend/paper_trading/`) can silently lose
entry signals for any day it doesn't run — TradingView's screener has no
point-in-time API, so a missed day's signals aren't recoverable later (see
`docs/claude/CLAUDE_CONTEXT.md`'s Day 81 summary). Nothing else currently
watches for this, so check it here, every session:

```bash
sqlite3 backend/validation_results/paper_trading_ledger.db "SELECT MAX(run_date) FROM job_runs;" 2>/dev/null
```

- If the file or table doesn't exist yet, note that the job has never run — not an error, just say so.
- If the last `run_date` is more than 3 calendar days before today, flag it prominently in the session summary (Step 5) as a warning — the launchd job (`launchctl list | grep sta.papertrading`) has likely gone silent (laptop asleep at 16:30 CT, or the agent unloaded). Suggest `cd backend && venv/bin/python paper_trading/daily_job.py --force` to catch up, and that catch-up only recovers open-position state, not the missed day's entry signals (documented limitation, not a bug).
- If within 3 days, no need to mention it — a normal weekend gap isn't worth flagging every session.

## Step 5: Output session summary to user

Report in this exact format:

```
Day [N] | v[X] | Backend v[Y] | Frontend v[Z]
Last session: [1-line summary from CLAUDE_CONTEXT.md]
Open bugs: [count] Medium+ ([list them by name, comma separated, or "none"])
Paper trading job: [last run date, or "⚠️ stale since [date] — see above" if flagged in Step 4]
Next priorities:
  1. [priority 1]
  2. [priority 2]
  3. [priority 3]
  (continue as needed)
```

Then ask: "What would you like to focus on?"

## Rules

- MEMORY.md is auto-loaded — do not re-read it manually
- Do not read `docs/claude/stable/rules/*` or `docs/claude/history/*` at session start; they are layers L2 and L3
- README.md is external-facing — not part of session start
- If PROJECT_STATUS or KNOWN_ISSUES file for Day N is missing, say so explicitly — do not guess or fabricate content
- Do not begin any work until the user responds to "What would you like to focus on?"
- Every code change follows the flow (Golden Rules 55, 64): plan in plan mode (EnterPlanMode; the user approves at ExitPlanMode) -> write it to `docs/claude/design/<NAME>_PLAN_<DAY>.md` and get an Opus review, apply its changes and tell the user what changed -> build -> `/three-pass` -> `three_pass_check.sh --stamp ... --plan <file>` (trivial changes only: `--trivial "kind: reason"`). A hook refuses the stamp without a plan.
