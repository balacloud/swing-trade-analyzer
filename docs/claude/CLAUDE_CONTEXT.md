# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 47 (February 6, 2026)

---

## HOW TO USE THIS FILE

**For User:** Just add this ONE file to your Claude context/project. Done.

**For Claude:** When you see this file:
1. Detect the scenario (new session, resume, or close)
2. Read the appropriate files listed below
3. Follow the corresponding checklist

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 47 |
| Version | v4.6.1 (Backend v2.15) |
| Latest Status | PROJECT_STATUS_DAY47_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY46.md |
| Latest API | API_CONTRACTS_DAY33.md |
| Focus | **v4.6 Perplexity Research Implementation** + ADX Entry Preference |

### Day 46 Summary
- **Fixed:** Issue #0 (CRITICAL) - Recommendation Card / Entry Mismatch
  - Alert prices now show support (entry) not resistance
  - Uses `entryPreference` from categorical assessment
- **Created:** UI Test Report (docs/test/UI_TEST_REPORT_DAY46.md) - 10 tickers
- **Validated:** 2nd iteration 5-ticker test - 100% pass rate
- **Noted:** Market F&G improved from ~33 (Weak) to ~40 (Neutral)

### Next Session: ADX Entry + Pattern Actionability
- ADX Entry Preference Logic (v4.6 Recommendation #2)
- Pattern Actionability ≥80% (v4.6 Recommendation #3)
- Forward Testing UI (v4.0 Roadmap priority)

---

## SCENARIO DETECTION

**Claude:** Determine which scenario applies:

| User Says | Scenario | Action |
|-----------|----------|--------|
| "Resume session" / "Continue" / "Start Day X" | SESSION_START | Read files, confirm context |
| "Session ending" / "Close session" / "Wrap up" | SESSION_CLOSE | Create status files, provide git command |
| Context was summarized / "Pick up where we left" | SESSION_RESUME | Read summary + status files |
| Nothing specific | SESSION_START | Default to startup checklist |

---

## SCENARIO 1: SESSION_START

### Files to Read (in order):
```
docs/claude/stable/GOLDEN_RULES.md          <- Core rules (CRITICAL)
docs/claude/stable/ROADMAP.md               <- What's planned (v4.0-v4.7) - DON'T LOSE TRACK
docs/claude/status/PROJECT_STATUS_DAY47_SHORT.md   <- Current state
docs/claude/versioned/KNOWN_ISSUES_DAY46.md        <- Active bugs
docs/research/PERPLEXITY_RESEARCH_SYNTHESIS.md     <- Research validation findings
docs/claude/versioned/API_CONTRACTS_DAY33.md       <- API reference (if needed)
```

### Startup Checklist:
1. Read GOLDEN_RULES.md - internalize the rules
2. Read ROADMAP.md - know what's planned (prevents losing track of items)
3. Read PROJECT_STATUS - understand current state
4. Read KNOWN_ISSUES - know active bugs
5. Confirm to user:
   - Current version and day
   - What was accomplished last session
   - Active priorities from ROADMAP
6. Ask: "What would you like to focus on today?"

### Rules to Follow:
- STOP before coding - understand problem first
- ASK for file content before modifying
- RUN diagnostic queries before writing fixes
- TEST incrementally - one change at a time
- If fix fails, STOP and diagnose - don't chain guesses

---

## SCENARIO 2: SESSION_CLOSE

### Files to Create/Update:
```
docs/claude/status/PROJECT_STATUS_DAY[N+1]_SHORT.md
docs/claude/versioned/KNOWN_ISSUES_DAY[N+1].md
docs/claude/versioned/API_CONTRACTS_DAY[N+1].md  (only if APIs changed)
docs/claude/stable/GOLDEN_RULES.md              (only if new rules learned)
docs/claude/stable/ROADMAP.md                   (only if roadmap items changed)
```

### Close Checklist:
1. Create PROJECT_STATUS_DAY[N+1]_SHORT.md with:
   - What was accomplished today
   - What's pending
   - Next session priorities
2. Create KNOWN_ISSUES_DAY[N+1].md with:
   - Resolved issues (move from Open to Resolved)
   - New issues discovered
3. Update API_CONTRACTS if any APIs added/changed
4. Update GOLDEN_RULES if new lessons learned
5. Update ROADMAP.md if roadmap items completed/added
6. Provide git commit command
7. Update the CURRENT STATE table in this file
8. Tell user which files to update in Claude Project

---

## SCENARIO 3: SESSION_RESUME (After Context Limit)

### Recognition:
- Conversation shows "summarized from previous context"
- User says "pick up where we left off" or "continue"

### Action:
1. Read the summary provided
2. Read PROJECT_STATUS for current context
3. Read KNOWN_ISSUES for active bugs
4. Resume the task that was in progress
5. Do NOT ask user to re-explain - you have the summary

---

## CORE RULES (Embedded - Always Apply)

### The 12 Golden Rules:
1. START of session: Read PROJECT_STATUS first
2. BEFORE modifying any file: Read it first
3. NEVER assume code structure - verify with actual file
4. END of session: Create updated PROJECT_STATUS
5. User will say "session ending" to trigger close
6. NEVER HALLUCINATE - Don't claim results without running
7. THINK THROUGH - Pause and reason before solutions
8. ALWAYS VALIDATE - Fact-check against external sources
9. GENERATE FILES ONE AT A TIME - Wait for confirmation
10. FOLLOW CODE ARCHITECTURE RULES
11. DEBUG APIS PROPERLY - Run diagnostic queries FIRST
12. LOCAL FILES FIRST, THEN GIT - Update files locally, then commit

### Debugging Workflow:
1. Understand the symptom
2. Form hypothesis about cause
3. Write diagnostic query to TEST hypothesis
4. Run diagnostic, analyze results
5. Only THEN write the fix
6. Test fix incrementally
7. If fix fails, go back to step 2 (don't guess again)

### Day 27 Critical Insights:
- Entry signals = ~10% of trading results
- Position sizing = ~90% of trading results
- Backtest before believing any system
- R-Multiples matter more than win rate
- Expectancy = (Win% x Avg Win R) + (Loss% x Avg Loss R)

---

## FILE STRUCTURE REFERENCE

```
/docs/claude/
├── CLAUDE_CONTEXT.md              <- THIS FILE (single reference)
├── stable/                        <- Rarely change
│   ├── GOLDEN_RULES.md           <- Core rules
│   ├── ROADMAP.md                <- Canonical roadmap (v4.0-v4.5)
│   ├── SESSION_START.md          <- Legacy (now in CLAUDE_CONTEXT)
│   ├── SESSION_PROMPT_TEMPLATE.md <- Legacy (now in CLAUDE_CONTEXT)
│   └── CLAUDE_CODE_GUIDE.md      <- Tool usage guide
├── versioned/                     <- Day-versioned
│   ├── API_CONTRACTS_DAY[N].md   <- API reference
│   ├── KNOWN_ISSUES_DAY[N].md    <- Bug tracker
│   └── archive/                   <- Older than 15 days
└── status/                        <- Daily status
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                   <- Older than 15 days
```

---

## QUICK COMMANDS

```bash
# Start/Stop services (Day 37+)
./start.sh               # Start both backend and frontend
./start.sh backend       # Start only backend
./stop.sh                # Stop both services
./stop.sh backend        # Stop only backend

# Find latest day number
ls -la docs/claude/status/ | grep PROJECT_STATUS | tail -1

# Git status
git status

# Cache status (Day 37+)
curl http://localhost:5001/api/cache/status
```

---

## UPDATE LOG

| Day | Changes to this file |
|-----|---------------------|
| 28 | Created CLAUDE_CONTEXT.md as single reference point |
| 29 | Updated for Day 29: Session Refresh + Position Controls |
| 30 | Updated for Day 30: S&R Research + DBSCAN Plan |
| 31 | Updated for Day 31: Agglomerative S&R + Fundamentals Failsafe |
| 32 | Updated for Day 32: MTF Confluence + Fundamentals/TradingView Research |
| 33 | Updated for Day 33: MTF Frontend + Fundamentals Transparency + README v3.4 |
| 34 | Updated for Day 34: Week 4 Validation Complete + Fibonacci + S&R Research DONE |
| 35 | Updated for Day 35: Data Provider Validation - yfinance 100% working, Defeat Beta blocked |
| 36 | Updated for Day 36: pegRatio local calculation, Pine Script validation complete (9/9) |
| 37 | Updated for Day 37: SQLite persistent cache (5.5x speedup), start.sh/stop.sh scripts, architecture cleanup |
| 38 | Updated for Day 38: Data Sources tab (transparency UI), /api/provenance endpoint |
| 39 | Updated for Day 39: Dual Entry Strategy Phases 1-3: structural stops, local RSI/ADX, 4H RSI |
| 40 | Updated for Day 40: Dual Entry Strategy UI complete, side-by-side cards for ALL stocks |
| 41 | Updated for Day 41: Perplexity research synthesis complete, TIER 1 gaps identified, baseline backtest priority |
| 42 | Updated for Day 42: Defeat Beta confirmed working, validation tolerances fixed (92.3% quality), VIX fixed, README v3.9, ROADMAP.md created |
| 43 | Updated for Day 43: Data source labels, Defeat Beta error handling (v2.13), ROADMAP.md added to startup checklist |
| 44 | Updated for Day 44: v4.2-v4.5 complete (Pattern Detection, Sentiment, Categorical Assessment), Actionable Recommendation Card, 30-stock validation |
| 45 | Updated for Day 45: v4.6 Perplexity Research (F&G thresholds, Structure > Sentiment), Comprehensive Test Plan, 100% baseline pass rate |
| 46 | Updated for Day 46: Issue #0 fixed (Recommendation Card Mismatch), UI Test Report created, 2nd iteration validation 100% pass |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
