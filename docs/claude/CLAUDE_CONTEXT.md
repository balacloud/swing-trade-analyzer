# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 76 — end of day (May 18, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 76 |
| Version | v4.36 (Backend v2.35, Frontend v4.35, Backtest v4.18, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY76_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY76.md |
| Latest API | API_CONTRACTS_DAY75.md |
| Focus | **N4 Market Phase synthesis — research done, build next. Paper trading unblocked.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 76 Summary (Session Protocol Fix + N4 Research + Skills Built — v4.36)
- **Session start protocol failure diagnosed**: CLAUDE_CONTEXT.md must be read first (not just GOLDEN_RULES.md). GOLDEN_RULES Rule 17 added. Memory updated.
- **N4 Market Phase synthesis — research done**: 5-phase framework designed (Bull Rally / Late Bull / Distribution / Correction / Recovery). `^SPXA200R` dead on yfinance — RSP/SPY ratio confirmed as breadth proxy. DataProvider OHLCV chain confirmed for price signals. Existing context engines feed macro signals. Not yet built.
- **Two project skills built**: `/sta-start` (`.claude/commands/sta-start.md`) + `/sta-end` (`.claude/commands/sta-end.md`). Automate full session open/close protocols.
- 2 skill files created, 3 docs updated, 2 memory files updated.

### Day 75 Summary (Value Tab + Gate 5 + Behavioral Test + N1/N2/Flip — v4.35)
- **Value Investing Tab built** (Phase 1): `/api/value/<ticker>` + `ValueTab.jsx`. Amber theme, isolated lens. Metrics: ROIC, ROE, Graham Number, P/E, PEG/PEGY, FCF yield. Cap-size adjusted thresholds.
- **Bug fix**: AAPL dividend yield 36.22% → 0.35% (switched to `trailingAnnualDividendYield` in yfinance).
- **Gate 5 PASSED**: Combined momentum+MR backtest, 60 tickers, 5 years. 1.9% overlap, 0.274 P&L correlation. All gates cleared.
- **Price Structure behavioral test PASSED 5/5**: NVDA, SPY, SMCI, AAPL, F. Two bugs fixed: ATH breakout now requires TT≥5; RSI overbought Priority 6 watch item added.
- **N1/N2/Flip**: Two-price entry labels, Nirmal watchlist preset, default view flipped to simple.
- 4 files created, 4 files modified.

### Day 74 Summary (Context Session — Scanner Explanation)
- **No code changes.** Pure context session.
- **TradingView scanner brief prepared**: Key file `backend/backend.py` lines 1747–1990. Library `tradingview-screener`, 5 strategies, 17 fields, 7 critical gotchas.
- 0 files created, 0 files modified.

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

1. **Paper trading** — PRIMARY FOCUS. All gates cleared, all prereqs done.
2. **Build N4: Market Phase synthesis** — Research done (Day 76). New file `market_phase_engine.py` + `/api/market/phase` endpoint. DataProvider for price signals, existing context engines for macro. Display in Context tab.
3. **Value Tab Phase 2** — AV earnings history, interest coverage, EV/EBIT, ROE 5yr median.
4. **Price Structure Phase 2** — HH/HL/LH/LL engine using `find_pivot_points()`.
5. **Gap-fill detection (N3)** — Deferred post paper-trading.
6. **Canadian Analyze page** — Medium bug, high complexity. Data source redesign for `.TO` tickers.

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
| 75 | Value Tab Phase 1 + Gate 5 PASSED + Behavioral test 5/5 (2 bugs fixed) + N1/N2/flip. All gates cleared. v4.35. |
| 76 | Session protocol fix (CLAUDE_CONTEXT.md first — Rule 17). N4 research done (RSP/SPY breadth proxy, 5-phase framework). /sta-start + /sta-end skills built. v4.36. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
