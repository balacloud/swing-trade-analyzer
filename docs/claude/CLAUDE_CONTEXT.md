# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 68 (March 17, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 68 |
| Version | v4.30 (Backend v2.32, Frontend v4.30, Backtest v4.17, API Service v2.9) |
| Latest Status | PROJECT_STATUS_DAY68_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY68.md |
| Latest API | API_CONTRACTS_DAY62.md (updated Day 68) |
| Focus | **Paper trading. Feature freeze. Data sources transparency complete.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 68 Summary (System Audit + Doc Cleanup — v4.30, no code changes)
- **System audit Layer 1:** 15 README claims audited — 9 VERIFIED, 5 MISLEADING, 1 PLAUSIBLE. Key: stale FMP refs, wrong versions, Fundamental Strong mismatch, 200 EMA→SMA.
- **Audit protocol established:** 2-layer approach (consistency + correctness). Added to GOLDEN_RULES.md.
- **External LLM prompts:** 5 module-specific prompts (45 questions) for Perplexity/GPT/Gemini validation.
- **Doc framework cleanup:** 62% reduction in brain files (934→354 lines). 59 old files archived. 3 legacy files deleted. Archiving step added to close protocol.
- **Backup:** `docs/claude/backup_pre_cleanup_day68/docs_claude_full_backup.zip`

### Day 67 Summary (Data Sources Transparency Audit & 7 Bug Fixes → v4.30)
- Full multi-provider chain audit: Finnhub → AlphaVantage → yfinance confirmed. FMP permanently dead.
- 8 FMP text references updated. 7 UI/provenance bugs fixed. JUST FETCHED badge added.

### Day 66 Summary (Cap Size Rotation strip → v4.28)
- QQQ/MDY/IWM RS vs SPY in Sectors tab. Sector card audit fixes. start.sh/stop.sh auto kill-port.

---

## SCENARIO DETECTION

| User Says | Scenario | Action |
|-----------|----------|--------|
| "Resume session" / "Continue" / "Start Day X" | SESSION_START | Read files, confirm context |
| "Session ending" / "Close session" / "Wrap up" | SESSION_CLOSE | Create status files, commit + push |
| Context was summarized / "Pick up where we left" | SESSION_RESUME | Read summary + status files |
| Nothing specific | SESSION_START | Default to startup checklist |

---

## SESSION START PROTOCOL

```
1. READ FILES (in this exact order):
   □ GOLDEN_RULES.md
   □ ROADMAP.md
   □ PROJECT_STATUS_DAY[N]_SHORT.md
   □ KNOWN_ISSUES_DAY[N].md

2. CONFIRM TO USER:
   "Day [N] | v[X] | Backend v[Y]"
   "Last session: [1-line summary]"
   "Open bugs: [Medium+ count]"

3. ASK: "What would you like to focus on?"
```

### Rules During Session:
- STOP before coding — understand problem first
- READ files before modifying them
- RUN diagnostics before writing fixes
- TEST incrementally — one change at a time
- If fix fails, STOP and diagnose — don't chain guesses
- NEVER ask user to manually update files — Claude does it
- NEVER provide git commands — Claude commits AND pushes

---

## SESSION CLOSE PROTOCOL

**CRITICAL: Follow EVERY step. Do NOT skip any. Do NOT ask user to do any step.**

```
STEP 1: CREATE status/PROJECT_STATUS_DAY[N+1]_SHORT.md
STEP 2: CREATE versioned/KNOWN_ISSUES_DAY[N+1].md
STEP 3: IF APIs changed → CREATE versioned/API_CONTRACTS_DAY[N+1].md
STEP 4: IF lessons learned → UPDATE stable/GOLDEN_RULES.md (+ "Last Updated" date)
STEP 5: IF roadmap changed → UPDATE stable/ROADMAP.md (+ "Last Updated" date)
STEP 6: UPDATE THIS FILE (CLAUDE_CONTEXT.md):
        □ CURRENT STATE table (Day, Version, Status, Issues, Focus)
        □ Day [N+1] Summary (rotate: keep last 3, move oldest to archive)
        □ Next Session Priorities
        □ "Last Updated" header
STEP 7: ARCHIVE if needed — move files older than 15 days to archive/ folders
STEP 8: GIT COMMIT + PUSH (Claude does this — NEVER ask user)
```

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

## NEXT SESSION PRIORITIES

1. **Paper trading** — Feature freeze. Use system on 5-10 real tickers.
2. **Log first Forward Test trade** if BUY signal found.
3. **README fixes** — 7 items from Day 68 audit (FMP refs, versions, Fundamental Strong desc, 200 EMA→SMA).
4. **External LLM audit synthesis** — When user returns with Perplexity/GPT/Gemini answers.

---

## FILE STRUCTURE REFERENCE

```
/docs/claude/
├── CLAUDE_CONTEXT.md              <- THIS FILE (single reference)
├── stable/                        <- Rarely change
│   ├── GOLDEN_RULES.md           <- Core rules + lessons learned
│   └── ROADMAP.md                <- Canonical roadmap
├── versioned/                     <- Day-versioned (active last 15 days)
│   ├── API_CONTRACTS_DAY[N].md   <- API reference
│   ├── KNOWN_ISSUES_DAY[N].md    <- Bug tracker
│   ├── COHERENCE_AUDIT_DAY[N].md <- Audit reports
│   └── archive/                   <- Older than 15 days
├── status/                        <- Daily status
│   ├── PROJECT_STATUS_DAY[N]_SHORT.md
│   └── archive/                   <- Older than 15 days
└── backup_pre_cleanup_day68/      <- Full backup before cleanup
```

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
```

---

## UPDATE LOG (Last 5 entries — full log in git history)

| Day | Changes to this file |
|-----|---------------------|
| 64 | Deep audit: 18 bugs fixed, v4.27. |
| 65 | README rewrite, no code changes. |
| 66 | Cap size rotation strip, sector card fixes, v4.28. |
| 67 | Data sources transparency, 7 bug fixes, v4.30. |
| 68 | System audit (Layer 1+2), doc framework cleanup, archiving protocol added. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
