# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 74 (May 14, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 74 |
| Version | v4.33 (Backend v2.34, Frontend v4.33, Backtest v4.17, API Service v2.10) |
| Latest Status | PROJECT_STATUS_DAY74_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY74.md |
| Latest API | API_CONTRACTS_DAY72.md |
| Focus | **Context session. Next: Gate 5 + Price Structure behavioral test + paper trading.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 74 Summary (Context Session — Scanner Explanation)
- **No code changes.** Pure context session.
- **TradingView scanner brief prepared**: User needed to explain STA's scanner to another LLM/project. Key file: `backend/backend.py` lines 1747–1990. Brief covers library (`tradingview-screener`), 5 strategies, 17 fields, 7 critical gotchas (col() arithmetic, single .where(), Perf.Y, set_index resets market, ticker prefix stripping, .TO suffix ordering, Canadian split).
- 0 files created, 0 files modified.

### Day 73 Summary (Nirmal Recovery + Regime Clarity + Priority Reorder + Value Investing Research)
- **Nirmal validation recovered** (uncommitted from prev session): 378 calls, BUY 15.3%. Style difference, not system failure. STA = universal quant framework (NOT Minervini). Corrected in all docs.
- **Regime awareness clarified:** VIX level alone is lagging. Full regime = VIX direction + sector rotation + breadth. April 2026 tariff crash proved STA was blind until VIX>30. N4 Market Phase synthesis = highest leverage feature.
- **Priority reordered (quant/trader lens):** Gate 5 → behavioral test → paper trading → N4 research → N4 build → N1/N2/flip → N3 → Canadian.
- **Value Investing Tab:** Buffett/Damodaran/Graham/Lynch/Greenblatt style. Separate tab, zero swing impact. Graham Number + DCF Lite + PEG + quality checklist. Research prompts created (`VALUE_INVESTING_RESEARCH_PROMPT.md` — 4 prompts for 4 LLMs).
- 6 files created, 4 modified. Roadmap fully updated.

### Day 72 Summary (Master Audit Framework + Price Structure Card Phase 1 — v4.33)
- **Master Audit Framework** created: `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md` — 5 audit types (Claim, Coherence, Behavioral, Design, External LLM). Wired into GOLDEN_RULES.md.
- **Price Structure card built**: `PriceStructureCard.jsx` + `priceStructureNarrative.js`. Teal-400 Tier 2, collapsed by default. Structured narrative (structure state, key levels with touches/confluence, watch items). Zero impact on verdict/scoring.
- **API change**: `meta.levelScores` added to `/api/sr/<ticker>` (1 line, backend.py). Touch counts now passed through from `_score_levels()`.
- 5 files created, 6 files modified.

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

1. **Gate 5: Combined momentum+MR backtest** — Quant discipline. Can't paper trade both arms without knowing if they improve or cannibalize. Fast (1 session).
2. **Behavioral test: Price Structure card** — Prerequisite before trusting it in paper trades. Run NVDA, F, SPY, AAPL, SMCI.
3. **Paper trading** — PRIMARY FOCUS. But Gates 1+2 must clear first.
4. **Research + validate N4: Market Phase synthesis** — Highest leverage feature. VIX direction + sector rotation + breadth → 5-phase label. Needs validation before building (Golden Rule #15).
5. **Build N4: Market Phase synthesis** — After research validates it. Changes quality of every output.
6. **N1: Two-price entry labels** — Trade Setup card: Primary Entry + Averaging Entry (~2 hours, approved).
7. **N2: Nirmal watchlist preset** — Scan tab dropdown. 30 min, approved.
8. **Flip default view to simple** — 30 min, approved.
9. **Gap-fill detection (N3)** — Deferred post paper-trading.
10. **Canadian Analyze page** — Medium bug, high complexity. Data source redesign for `.TO` tickers.

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
| 73 | Research session. Positional vs swing trading concepts. No code changes. |
| 74 | Context session. TradingView scanner brief for external LLM. No code changes. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
