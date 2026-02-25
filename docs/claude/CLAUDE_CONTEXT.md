# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 59 (February 25, 2026)

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
| Current Day | 59 |
| Version | v4.21 (Backend v2.22, Frontend v4.8, Backtest v4.17) |
| Latest Status | PROJECT_STATUS_DAY59_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY59.md |
| Latest API | API_CONTRACTS_DAY53.md (outdated — update when APIs change next) |
| Focus | **v4.20+v4.21 Complete** — Cache Freshness Meter + Canadian Market + DVN Fix + AI Fluency Analysis |

### Day 59 Summary (Current)
- **v4.20 Cache Freshness Meter + v4.21 Canadian Market + Bug Fixes**
  - Cache Audit complete: all TTLs reasonable. New `/api/data/freshness` endpoint + UI freshness dots (green/yellow/red)
  - DVN Bottom Line bug fix: `getEntryTypeLabel()` uses R:R viability (not just ADX) — matches Trade Setup card
  - Canadian Market: TSX 60 scan + All Canadian scan working. 3 bugs fixed (.TO suffix filter, exchange validation, set_index combo)
  - Session protocol flowcharts added to CLAUDE_CONTEXT.md
  - AI Fluency Critical Analysis: `docs/research/AI_FLUENCY_CRITICAL_ANALYSIS.md` — mapped Anthropic research to project, no code changes needed

### Day 58 Summary
- **v4.19 Pattern Descriptions + Sector Rotation Phase 1**
  - Pattern trader descriptions added to all 3 pattern cards
  - Sector Rotation Phase 1: `/api/sectors/rotation` endpoint, RS ratio + RRG quadrant, badge + scan column
  - SQLite cache for sector data, sector badge reliability fix, scan transparency

### Day 57 Summary
- **v4.17 Production Coherence + Bear Regime + 5th Filter Redesign**
  - 5th "Best Candidates" filter redesigned to match Config C criteria
  - Frontend-backend coherence audit: 39/42 parameters match
  - Bear market regime: SPY 50 SMA declining caps risk at "Neutral"

### Implementation Status (v4.9-v4.21)
| Priority | Feature | Effort | Status |
|----------|---------|--------|--------|
| P1 | v4.9-v4.15: All features | — | ✅ **COMPLETE** |
| P0 | v4.16: Holistic 3-Layer Backtest | 6-8 hrs | ✅ **COMPLETE** |
| P0 | v4.17: Coherence + Bear Regime | 2 hrs | ✅ **COMPLETE** (Day 56) |
| P1 | v4.18: Index Filters (S&P/NASDAQ/Dow) | 1 hr | ✅ **COMPLETE** (Day 57) |
| P1 | v4.19: Sector Rotation Phase 1 | 1.5 hrs | ✅ **COMPLETE** (Day 58) |
| P1 | v4.20: Cache Audit + Freshness Meter | 1 hr | ✅ **COMPLETE** (Day 59) |
| P1 | v4.21: Canadian Market Support | 2 hrs | ✅ **COMPLETE** (Day 59) |
| P1 | DVN Bottom Line Entry Type Fix | 0.5 hr | ✅ **COMPLETE** (Day 59) |
| P3 | v4.12: Charts (Own Tab) | 4-6 hrs | QUEUED |

### Backtest Results Summary (Day 57)
| Period | Trades | Win Rate | PF | Sharpe | Walk-Forward |
|--------|--------|----------|----|--------|--------------|
| Quick (1-5d) | 318 | 55.35% | 1.72 | 0.85 | PASS (all metrics improved OOS) |
| Standard (5-15d) | 244 | 53.69% | 1.62 | 0.85 | PASS (Day 55) |
| Position (15-45d) | 362 | 38.67% | 1.51 | 0.61 | PASS (regime-sensitive, not overfitted) |

### Next Session Priorities (Day 60)
1. **Sector Rotation Phase 2** — dedicated tab with 11 sector cards ranked, quadrant colors, **"Scan for Rank 1"** filter (user requested)
2. **Simple Checklist enhancements** — backtest validates criteria, add 52-week range, volume, ADX, market regime, ATR stops
3. **EPS/Revenue Growth methodology fix** — QoQ → YoY (Medium severity)
4. **TradingView Lightweight Charts** — Interactive charts with S&R levels, RSI/MACD overlays

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

## SESSION START PROTOCOL (Flowchart)

```
┌─────────────────────────────────────────┐
│  1. READ FILES (in this exact order)     │
│     □ GOLDEN_RULES.md                    │
│     □ ROADMAP.md                         │
│     □ PROJECT_STATUS_DAY[N]_SHORT.md     │
│     □ KNOWN_ISSUES_DAY[N].md             │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│  2. CONFIRM TO USER (always say this)    │
│     "Day [N] | v[X] | Backend v[Y]"     │
│     "Last session: [1-line summary]"     │
│     "Open bugs: [Medium+ count]"         │
│     "Today's priorities: [from ROADMAP]" │
└──────────────┬──────────────────────────┘
               ▼
┌─────────────────────────────────────────┐
│  3. ASK USER                             │
│     "What would you like to focus on?"   │
│     (unless user already specified)      │
└─────────────────────────────────────────┘
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

## SESSION CLOSE PROTOCOL (Flowchart)

**CRITICAL: Follow EVERY step. Do NOT skip any. Do NOT ask user to do any step.**

```
┌──────────────────────────────────────────┐
│  STEP 1: CREATE PROJECT_STATUS           │
│  File: status/PROJECT_STATUS_DAY[N+1]    │
│  _SHORT.md                               │
│  Contents:                               │
│    □ What was accomplished today          │
│    □ Files modified + files created       │
│    □ Git commits (hash + description)     │
│    □ Version summary (FE/BE/BT)          │
│    □ Next session priorities              │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 2: CREATE KNOWN_ISSUES             │
│  File: versioned/KNOWN_ISSUES_DAY[N+1]   │
│  .md                                     │
│  Contents:                               │
│    □ Copy open issues from previous      │
│    □ Move resolved issues to Resolved    │
│    □ Add ANY new issues found today      │
│    □ Update issue statistics table        │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 3: CHECK — Did APIs change?        │
│  ├─ YES → Update API_CONTRACTS_DAY[N+1]  │
│  └─ NO  → Skip (note: currently DAY53)   │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 4: CHECK — New lessons learned?    │
│  ├─ YES → Add to GOLDEN_RULES.md         │
│  │        Update "Last Updated" date     │
│  └─ NO  → Skip                           │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 5: CHECK — Roadmap items changed?  │
│  ├─ YES → Update ROADMAP.md              │
│  │        Update "Last Updated" date     │
│  │        Update UPDATE LOG table        │
│  └─ NO  → Skip                           │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 6: UPDATE THIS FILE                │
│  (CLAUDE_CONTEXT.md — MANDATORY)         │
│    □ CURRENT STATE table:                │
│      - Current Day → [N+1]               │
│      - Version → [new version]           │
│      - Latest Status → DAY[N+1]          │
│      - Latest Issues → DAY[N+1]          │
│      - Focus → [today's work]            │
│    □ Day [N+1] Summary section           │
│    □ Implementation Status table         │
│    □ Next Session Priorities             │
│    □ Files to Read paths (update day #)  │
│    □ UPDATE LOG entry                    │
│    □ "Last Updated" header               │
└──────────────┬───────────────────────────┘
               ▼
┌──────────────────────────────────────────┐
│  STEP 7: GIT COMMIT + PUSH              │
│  (Claude does this — NEVER ask user)     │
│    □ git add [specific files]            │
│    □ git commit -m "Day [N+1]: ..."      │
│    □ git push                            │
│    □ Verify push succeeded               │
└──────────────────────────────────────────┘
```

### Common Mistakes to Avoid at Close:
- Forgetting to update "Last Updated" dates on stable docs
- Forgetting to push after commit
- Asking user to run git commands
- Asking user to manually update any file
- Missing KNOWN_ISSUES for bugs observed during session
- Not updating CLAUDE_CONTEXT.md file paths (still pointing to old day)

---

## SESSION RESUME PROTOCOL (After Context Limit)

```
┌─────────────────────────────────────────┐
│  1. READ the summary provided            │
│  2. READ PROJECT_STATUS for context      │
│  3. READ KNOWN_ISSUES for active bugs    │
│  4. Resume the task in progress           │
│  5. Do NOT ask user to re-explain        │
└─────────────────────────────────────────┘
```

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

All commands run from the **project root**: `/Users/balajik/projects/swing-trade-analyzer/`

```bash
# Start/Stop services (Day 37+) — run from project root
./start.sh               # Start both backend and frontend
./start.sh backend       # Start only backend
./start.sh frontend      # Start only frontend
./stop.sh                # Stop both services
./stop.sh backend        # Stop only backend

# Find latest day number — run from project root
ls -la docs/claude/status/ | grep PROJECT_STATUS | tail -1

# Git status — run from project root
git status

# Cache status (Day 37+) — run from anywhere
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
| 48 | Updated for Day 48: Multi-AI research analysis complete, v4.9-v4.12 roadmap added, verified features vs deferred based on research |
| 49 | Updated for Day 49: v4.9 OBV+RVOL, v4.10 Earnings, API_CONTRACTS_DAY49.md created (was 16 days outdated!) |
| 50 | Exhaustive UI re-test: 21% true pass rate (not 92.8%), 5 open issues identified, Position Size banner is main culprit (64% affected) |
| 52 | v4.14 Multi-Source Data Intelligence complete: 5 providers (TwelveData, Finnhub, FMP, yfinance, Stooq), 13 new files, backend v2.17, frontend labels updated |
| 53 | v4.15 Decision Matrix, v4.13 Holding Period, Bugs #7/#8, Architectural cleanup (SRP: removed fundamentals from /api/stock/, ~255 lines dead code removed, backend v2.18). Focus shifted to v4.16 backtest. |
| 54 | Pre-backtest audit: 3 CRITICAL hardcoded fallbacks fixed (sentiment 5→0, breadth 1→0, F&G 50→null, VIX 20→null). Decision Matrix coherence verified (ALL CLEAR). Simple Checklist gaps documented. Next: PLAN backtest. |
| 55 | v4.16 Holistic Backtest COMPLETE: 60 tickers, 3 configs, all statistically significant. Config C fixed (0→238 trades). Walk-forward validated (OOS>IS). Exit optimization: trailing 10 EMA + breakeven stop, DD 65.9%→52.6%. No unintended changes to production code. |
| 56 | v4.17: 5th filter redesigned (Config C criteria), coherence audit (39/42 match, pattern threshold synced 80→60), bear regime filter (SPY 50 SMA declining), S&P 500 index filter researched (native TradingView support). |
| 57 | v4.18: S&P 500/NASDAQ 100/Dow 30 index filter complete, bear regime coherence gap fixed (sma50Declining in backend+frontend), Options tab deferred (v4.19), TSX 60 deferred (v4.20), coherence audit document created. Backtest: bear regime validated (WR 71.4%), Quick+Position walk-forward passed, yfinance 0.2.28→1.2.0. Sector rotation rethought (Phase 1: embed in views). |
| 58 | v4.19: Pattern trader descriptions, Sector Rotation Phase 1 complete (endpoint + badge + scan column + SQLite cache), sector badge reliability fix, scan transparency (empty vs error). Day 59 priorities: Phase 2 dedicated tab with "Scan for Rank 1", Cache Audit + UI Freshness Meter. |
| 59 | v4.20 Cache Freshness Meter (endpoint + UI dots), v4.21 Canadian Market (TSX 60 + All Canadian scan, 3 bugs fixed), DVN Bottom Line entry type fix (R:R-based getEntryTypeLabel), session protocol flowcharts, AI Fluency Critical Analysis document. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
