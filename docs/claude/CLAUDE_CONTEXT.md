# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 72 (March 31, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 72 |
| Version | v4.33 (Backend v2.34, Frontend v4.33, Backtest v4.17, API Service v2.10) |
| Latest Status | PROJECT_STATUS_DAY72_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY72.md |
| Latest API | API_CONTRACTS_DAY72.md |
| Focus | **Price Structure card Phase 1 built. Master Audit Framework created. Paper trading active.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 72 Summary (Master Audit Framework + Price Structure Card Phase 1 — v4.33)
- **Master Audit Framework** created: `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md` — 5 audit types (Claim, Coherence, Behavioral, Design, External LLM). Wired into GOLDEN_RULES.md.
- **Price Structure card built**: `PriceStructureCard.jsx` + `priceStructureNarrative.js`. Teal-400 Tier 2, collapsed by default. Structured narrative (structure state, key levels with touches/confluence, watch items). Zero impact on verdict/scoring.
- **API change**: `meta.levelScores` added to `/api/sr/<ticker>` (1 line, backend.py). Touch counts now passed through from `_score_levels()`.
- **Audit findings applied**: ATR-relative proximity (2x ATR), 12-rule priority tree, RSI<30 Wilder threshold, frontend architecture (follows categoricalAssessment.js pattern).
- 5 files created, 6 files modified.

### Day 70B Summary (Simplicity Premium UI + Cap-Aware Simple Checklist — v4.32)
- **Sentiment removed from verdict**: T+F only. Risk/Macro gate intact.
- **Progressive disclosure**: 3-tier collapsible full analysis. Decision Matrix + TradingView Chart removed.
- **Simple checklist data-driven**: RS 1.0→1.2 (PF 1.78), volume cap-aware, stop cap-aware.
- 5 files modified, 0 files created.

### Day 70 Summary (Universal Principles Implementation COMPLETE — v4.31)
- All 4 tiers implemented. MR engine + VIX sizing + blended RS (info only). Zero regression on existing backtest.

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

1. **Behavioral test: Price Structure card** — Run NVDA, F, SPY, AAPL, SMCI. Verify narrative matches TradingView chart read before paper trading use.
2. **Paper trading** — System is frozen. Log real trades using Forward Testing tab.
3. **Gate 5: Combined momentum+MR system test** — Verify combined Sharpe > momentum-only.
4. **Flip default view to simple** — Last remaining simplicity premium item (30 min).
5. **Phase 2 (deferred)** — HH/HL/LH/LL market structure engine using `find_pivot_points()` — after paper trading validation.

---

## FILE STRUCTURE REFERENCE

```
/docs/claude/
├── CLAUDE_CONTEXT.md              <- THIS FILE (single reference)
├── stable/                        <- Rarely change
│   ├── GOLDEN_RULES.md           <- Core rules + lessons learned
│   ├── ROADMAP.md                <- Canonical roadmap
│   └── MASTER_AUDIT_FRAMEWORK.md <- Canonical audit protocol (5 types)
├── design/                        <- Feature design specs + audit reports
│   ├── PRICE_STRUCTURE_CARD_SPEC.md  <- v2, audited (Day 72)
│   └── PRICE_STRUCTURE_CARD_AUDIT.md <- 10 findings self-audit (Day 72)
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
| 72 | Master Audit Framework + Price Structure card Phase 1. levelScores API. v4.33. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
