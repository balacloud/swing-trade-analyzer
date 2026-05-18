# Session Start — Swing Trade Analyzer

Execute the full STA session start protocol. Do every step in order. Do not skip any.

## Step 1: Read CLAUDE_CONTEXT.md first

Read `docs/claude/CLAUDE_CONTEXT.md`.

Extract from it:
- Current Day N (from CURRENT STATE table)
- Current version string (Backend vX, Frontend vY)
- The Day N summary (1-line description of last session)
- Next Session Priorities list

## Step 2: Read the 4 required files

Read all four — do not skip any:

1. `docs/claude/stable/GOLDEN_RULES.md`
2. `docs/claude/stable/ROADMAP.md`
3. `docs/claude/status/PROJECT_STATUS_DAY[N]_SHORT.md` — use the Day N you found in Step 1
4. `docs/claude/versioned/KNOWN_ISSUES_DAY[N].md` — use the Day N you found in Step 1

## Step 3: Count open bugs

From KNOWN_ISSUES, count issues at severity Medium or higher (ignore Info-level).

## Step 4: Output session summary to user

Report in this exact format:

```
Day [N] | v[X] | Backend v[Y] | Frontend v[Z]
Last session: [1-line summary from CLAUDE_CONTEXT.md]
Open bugs: [count] Medium+ ([list them by name, comma separated, or "none"])
Next priorities:
  1. [priority 1]
  2. [priority 2]
  3. [priority 3]
  (continue as needed)
```

Then ask: "What would you like to focus on?"

## Rules

- MEMORY.md is auto-loaded — do not re-read it manually
- README.md is external-facing — not part of session start
- If PROJECT_STATUS or KNOWN_ISSUES file for Day N is missing, say so explicitly — do not guess or fabricate content
- Do not begin any work until the user responds to "What would you like to focus on?"
