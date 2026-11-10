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

## Step 1: Create PROJECT_STATUS_DAY[N+1]_SHORT.md

Create `docs/claude/status/PROJECT_STATUS_DAY[N+1]_SHORT.md`.

Include:
- Version header
- "What Happened Today" section — one subsection per meaningful change, with a table of files changed
- "All Gates Status" table (carry forward from Day N status, update any that changed)
- "Next Session Priorities" numbered list

## Step 2: Create KNOWN_ISSUES_DAY[N+1].md

Create `docs/claude/versioned/KNOWN_ISSUES_DAY[N+1].md`.

Include:
- "Changes from Day N" section (what was resolved, what was added)
- All open issues carried forward from Day N, updated as needed
- Any new issues discovered this session

## Step 3: Create API_CONTRACTS (conditional)

Only if APIs changed this session:
Create `docs/claude/versioned/API_CONTRACTS_DAY[N+1].md` with updated endpoint documentation.

## Step 4: Update GOLDEN_RULES.md (conditional)

Only if new lessons were learned:
- Update `docs/claude/stable/GOLDEN_RULES.md`
- Update "Last Updated" date in the header to today's date

## Step 5: Update ROADMAP.md and README.md (conditional)

Only if roadmap changed (items completed, new items, priority shifts):
- Update `docs/claude/stable/ROADMAP.md` — update "Last Updated" date in header
- Update `README.md` in the project root to mirror ROADMAP changes (external-facing)
- Both files must be updated together — never one without the other

## Step 5b: Update PERSONA.md's Feedback Log (conditional)

Only if the persona lens caught, confirmed, or reframed something this session (per the Step 0 question):
- Append a new dated entry (most recent first) to `docs/claude/stable/PERSONA.md`'s "Feedback Log" section — what the persona lens caught/confirmed, tied to the specific decision it applied to
- Update the "Last Updated" date in the header
- If nothing to log, skip this step entirely — do not force an entry just to have one

## Step 6: Update CLAUDE_CONTEXT.md

Always. Update all of the following:

- **CURRENT STATE table**: Day → N+1, Version → new version, Latest Status/Issues/API file names → Day N+1, Focus → one line summary of next priority
- **RECENT DAY SUMMARIES**: Add Day N+1 summary at top. Keep last 3 days only — move the oldest out (it goes to archive, not deleted)
- **NEXT SESSION PRIORITIES**: Update to reflect what's actually next
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

## Step 7: Update memory files (conditional)

Only if this session produced new information worth persisting across future conversations:
- New user feedback or corrected behavior → write/update a `feedback_*.md` file in memory
- New project facts (decisions, dates, milestones) → write/update a `project_*.md` file in memory
- Update `MEMORY.md` index if any memory file was added or changed

## Step 8: Archive old files

Check these two directories for files older than 15 days from today:
- `docs/claude/status/` — move old PROJECT_STATUS files to `docs/claude/status/archive/`
- `docs/claude/versioned/` — move old KNOWN_ISSUES and API_CONTRACTS files to `docs/claude/versioned/archive/`

Do not delete — move only.

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
- README.md only changes if ROADMAP.md changes — they are always updated as a pair
- MEMORY.md (auto-memory) is separate from project docs — update it independently in Step 7
- PERSONA.md's Feedback Log is append-only — never edit or remove a prior dated entry, only add new ones
