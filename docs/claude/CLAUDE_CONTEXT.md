# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 70B (March 19, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 70B |
| Version | v4.32 (Backend v2.33, Frontend v4.32, Backtest v4.17, API Service v2.10) |
| Latest Status | PROJECT_STATUS_DAY70B_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY70.md |
| Latest API | API_CONTRACTS_DAY70.md |
| Focus | **Simplicity premium implemented. Cap-aware simple checklist. Feature freeze → paper trading.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 70B Summary (Simplicity Premium UI + Cap-Aware Simple Checklist — v4.32)
- **Sentiment removed from verdict**: T+F only (backtest never validated sentiment). Risk/Macro gate intact.
- **Progressive disclosure**: 3-tier collapsible full analysis. Decision Matrix + TradingView Chart removed.
- **Simple checklist data-driven**: RS 1.0→1.2 (backtest: PF 1.78), volume cap-aware ($2M/$5M/$10M), stop cap-aware (7%/9%/10%).
- **No API changes**. No backtest re-run needed (frontend checklist is independent of backtest engine).
- 5 files modified, 0 files created.

### Day 70 Summary (Universal Principles Implementation COMPLETE — v4.31)
- All 4 tiers implemented across 2 sessions (Day 69-70). MR engine + VIX sizing + blended RS (info only).
- Zero regression on existing backtest.

### Day 69 Summary (4-LLM Universal Principles Synthesis + Tier 0-1 — v4.30)
- 4-LLM synthesis complete. Tier 0 bug fixes + Tier 1 quick wins. RS 1.0 validated. Parameter stability script.

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

1. **Paper trading** — System is frozen. Start logging real trades using Forward Testing tab.
2. **Gate 5: Combined momentum+MR system test** — Verify combined Sharpe > momentum-only.
3. **Flip default view to simple** — Last remaining simplicity premium item (30 min).
4. **README fixes** — 7 items from Day 68 audit (FMP refs, versions, Fundamental Strong desc, 200 EMA→SMA).

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
| 69 | 4-LLM Universal Principles synthesis + detailed implementation plan. |
| 70 | Universal Principles Tier 2+3 complete (VIX sizing, blended RS info-only, MR engine). |
| 70B | Simplicity premium UI + cap-aware simple checklist. Sentiment informational-only. v4.32. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
