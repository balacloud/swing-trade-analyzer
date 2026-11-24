# Session End — Swing Trade Analyzer

Execute the full STA session close protocol. Do every step in order. Do not skip any step. Do not ask the user to do anything — Claude does all of it.

## Step 0: Gather session facts

Read `docs/claude/CLAUDE_CONTEXT.md` to get current Day N and version. The new status files will be Day N+1.

Ask the user one consolidated question before proceeding:
- What is the version bump, if any? (e.g. "v4.36, Backend v2.36, Frontend v4.36" — or "no version change")
- Did any APIs change (new endpoints, changed response fields)?
- Any new lessons learned for GOLDEN_RULES?
- Any roadmap changes (items completed, new items added, priorities shifted)?
- Did the PERSONA.md trading-judgment lens catch, confirm, or reframe anything this session (a threshold call, a "too good to be true" result, a behavioral-finance pitfall)? Or nothing to log?

Wait for the user's answers, then proceed through all steps.

## Step 0b: List the review exemptions used this session

Run `cat .claude/.review_log.tsv 2>/dev/null | tail -20`. Rows with kind `trivial` are changes that skipped the plan and Opus review (Golden Rule 55). Show each one (date, reason, number of code files) in the status file under "Review exemptions" so the user can spot misuse. Rows with kind `plan` need no listing beyond the plan name. If the file is empty or missing, write "none".

## Step 1: Create PROJECT_STATUS_DAY[N+1]_SHORT.md

Create `docs/claude/status/PROJECT_STATUS_DAY[N+1]_SHORT.md`.

Include:
- Version header
- "What Happened Today" section — one subsection per meaningful change, with a table of files changed
- "All Gates Status" table (carry forward from Day N status, update any that changed)
- "Next Session Priorities" numbered list

## Step 2: Create KNOWN_ISSUES_DAY[N+1].md

Create `docs/claude/versioned/KNOWN_ISSUES_DAY[N+1].md` (if it already exists, the Day 133 layering created it: edit it, do not recreate it).

This file holds **open issues at Medium or above only** (plus any Low-Medium item that is a next-session priority). It is layer L1 and is read in full every session.
- Open Medium+ issues carried forward from Day N, updated as needed, each heading word for word
- Any new Medium+ issue found this session
- Do NOT write a "Changes from Day N" history here. Put this session's resolved items, new Low/Info items and per-day change notes into `docs/claude/history/KNOWN_ISSUES_LOW_AND_RESOLVED.md` as a new `## Day N+1` section (append only).
- Triage each heading, not each section: open items can hide under "Changes from" or "New open issues" headings. "Low-Medium" does not count as Medium+.
- Count check before moving on: every heading of the old file is in exactly one of the two files (open file or history file).

## Step 3: Create API_CONTRACTS (conditional)

Only if APIs changed this session:
Create `docs/claude/versioned/API_CONTRACTS_DAY[N+1].md` with updated endpoint documentation.

## Step 4: Update GOLDEN_RULES.md (conditional)

Only if new lessons were learned:
- Add the full rule text to the right cluster file in `docs/claude/stable/rules/<cluster>.md` (clusters: process, claims-verification, backtest-honesty, engine-parity, data-providers, cache-time-audit, display-consumers). Add its number to that file's `rules:` frontmatter list.
- Add one index line to `docs/claude/stable/GOLDEN_RULES.md` (number, short title, "read when:" trigger words; not a restatement). Only a rule that applies to every session goes in full in `GOLDEN_RULES.md`.
- Update "Last Updated" date in the header of every `stable/` file touched (Rule 14)

## Step 5: Update ROADMAP.md and README.md (conditional)

Only if roadmap changed (items completed, new items, priority shifts):
- Update `docs/claude/stable/ROADMAP.md` — update "Last Updated" date in header, and the "Current Version" line on every version bump. ROADMAP holds **open priorities only**: move any priority closed this session, with its row text word for word, to `docs/claude/history/ROADMAP_HISTORY.md` under a new `## Day N+1` section. Do not edit code comments that cite closed priorities (the numbers resolve in history).
- Update `README.md` in the project root so it mirrors the open priorities (external-facing)
- Both files must be updated together — never one without the other

## Step 5b: Update PERSONA.md's Feedback Log (conditional)

Only if the persona lens caught, confirmed, or reframed something this session (per the Step 0 question):
- Append a new dated entry (most recent first) to the top of the list in `docs/claude/history/PERSONA_LOG.md` — what the persona lens caught/confirmed, tied to the specific decision it applied to
- Update the "Last Updated" date in the header of `docs/claude/stable/PERSONA.md` only if its core text changed
- If nothing to log, skip this step entirely — do not force an entry just to have one

## Step 6: Update CLAUDE_CONTEXT.md

Always. Update all of the following:

- **CURRENT STATE table**: Day → N+1, Version → new version, Latest Status/Issues/API file names → Day N+1, Focus → one line summary of next priority
- **RECENT DAY SUMMARIES**: Add Day N+1 summary at top. Keep last 3 days only — append the oldest, word for word, to `docs/claude/history/CLAUDE_CONTEXT_LOG.md` under a `## Day N` heading (not deleted)
- **NEXT SESSION PRIORITIES**: One-line references only (detail lives in the status file and ROADMAP). Update to reflect what's actually next
- **ENGINEER.md**: new "what has been missed" rows and the Feedback Log entry go in `docs/claude/history/ENGINEER_LOG.md`; edit `stable/ENGINEER.md` only for its themes table or checklists
- **"Last Updated" header**: Update to today's date

## Step 6b: Update and republish the STA Status Board

Always. Source: `docs/claude/design/STA_STATUS_BOARD.html`. Published at
`https://claude.ai/artifact/Bk4WTv5EYKfXxBbhNtfXPz`. Always pass this `url` when republishing from
a new session, or the publish creates a duplicate page.

1. Run `cd backend && venv/bin/python paper_trading/daily_job.py --report` and update the
   "Forward-test final results" table from it. Never copy numbers from a status doc.
2. Update the header's "last updated" line, the four status tiles, Next priorities, Open bugs
   (Medium+ from the new KNOWN_ISSUES file), and add the new day at the top of Recent sessions
   (keep about 4 rows).
3. Artifact map (`ITEMS` array in the script): run Artifact `action: "list"`. Add a row for every
   new STA-related artifact. Change the status of any artifact whose subject changed this session
   (current → snapshot/stale), and of any that was republished (→ current). Leave out non-STA pages
   (CanStack, personal finance, Trading Intelligence Hub, Options IQ).
   Then list every Snapshot row whose "Updated" date is more than 30 days old in the session-close
   summary as "needs recheck", so old snapshots don't sit unreviewed indefinitely.
   If an Analyze Page Redesign build step shipped this session, update the Decision Map
   (`8ih9hWm6N8Sq6vy7VjHq6A`, source `docs/claude/design/artifacts_src/decision_map/index.html`) and
   the Mockup (`WacHXh9VioxQgzwsPGdX1X`, source `docs/claude/design/mockups/analyze_page_redesign_mockup.html`)
   to match, republish both to their existing URLs, and keep the repo source copies identical to what
   was published.
4. Republish with the Artifact tool (`file_path` above plus `url`).

## Step 6c: Layer completeness check (fast, not a hook)

Run `python3 .claude/check_context_layers.py`. It confirms every Golden Rule number in the index is in exactly one `rules/*.md` file (and the reverse), the `history/` files exist, and the L1 core files are under 85 KB. Fix every PROBLEM line before continuing. Also confirm by eye that the Step 2 KNOWN_ISSUES heading count check passed.

## Step 7: Update memory files (conditional)

Only if this session produced new information worth persisting across future conversations:
- New user feedback or corrected behavior → write/update a `feedback_*.md` file in memory
- New project facts (decisions, dates, milestones) → write/update a `project_*.md` file in memory
- Update `MEMORY.md` index if any memory file was added or changed. Keep `MEMORY.md` an index only (one line per memory); old day history goes in `project_history_compacted.md`.

## Step 8: Archive old files

Check these two directories for files older than 15 days from today:
- `docs/claude/status/` — move old PROJECT_STATUS files to `docs/claude/status/archive/`
- `docs/claude/versioned/` — move old KNOWN_ISSUES and API_CONTRACTS files to `docs/claude/versioned/archive/`

Do not delete — move only. Never archive `docs/claude/history/` or `docs/claude/stable/rules/` (they are layers L3 and L2, not old copies).

## Step 9: Git commit and push

Stage all changed and new files (be specific — list files by name, do not use `git add -A`).

Commit with a message in this format:
```
Day [N+1]: [one-line description of what was built/fixed] (v[X.Y])
```

Then push to origin main.

Confirm to the user: "Session closed. Day [N+1] status files created and pushed."

## Rules

- Never ask the user to run git commands or update files manually
- Never skip archiving — stale files accumulate silently
- Never commit without pushing — the session is not closed until it's pushed
- README.md only changes if ROADMAP.md changes — they are always updated as a pair (README mirrors the open priorities)
- MEMORY.md (auto-memory) is separate from project docs — update it independently in Step 7
- `history/PERSONA_LOG.md` (the Feedback Log) and the other `history/` files are append-only — never edit or remove a prior dated entry, only add new ones
