# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 79 — end of day (July 6, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 79 |
| Version | v4.37 (Backend v2.36, Frontend v4.36, Backtest v4.18, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY79_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY79.md |
| Latest API | API_CONTRACTS_DAY79.md |
| Focus | **Fable Remediation Phases 0–3 complete. Phase 4 (survivorship-free re-validation) is next. Paper trading unblocked — config frozen.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 79 Summary (Fable Remediation Phases 0–3 Executed + Breakout Wired — v4.37)
- **Phase 0**: RS threshold resolved (simple checklist 1.2→1.0, matching Config C). `PAPER_TRADING_PREREGISTRATION.md` created — config frozen.
- **Phase 1**: SimFin key → `.env`, `backend/venv` untracked, `BACKEND_VERSION` constant, 3 dead files deleted.
- **Phase 2**: MR transaction costs added (PF 1.26→1.23 net, edge survives). Gap-aware stop/target fills in both simulators. `metrics.py` stats overhaul (scipy t-test, actual trades/year, block bootstrap, fixed-risk DD). **JS↔Python verdict parity: 86,400-combo grid found 1 real bug (HOLD-fallback missing `Neutral` risk branch) — fixed, now 100% parity.**
- **Phase 3**: Fundamentals mismatch measured at **40.0% disagreement** (live vs backtested) — mitigation choice pending user decision. Silent RS fallback fixed on both JS and Python sides.
- **Breakout engine wired**: `/api/breakout/<ticker>` (built by a parallel session, never registered) is now live and validated on 5 tickers + 1 edge case. `BREAKOUT_ENHANCEMENT_PLAN.md` reconciled.
- **Golden Rule 19 added**: systematic grid-test parity, not hand-picked vectors.
- Paper trading unblocked (config frozen). Remediation Phase 4 (survivorship-free re-validation) is next.

### Day 78 Summary (Fable 5 Full-System Audit + Two Remediation Plans)
- **No code changes** — audit + planning session (Claude Fable 5).
- **Full-system review verdict**: engineering honesty is real, but Config C PF 1.61 is likely overstated — survivorship-biased 60-ticker universe (hand-picked 2026) + walk-forward window reused across ~20 tuning sessions (OOS no longer OOS). Honest live expectation: PF ~1.1–1.3. Also found: MR/Gate 5 backtests have zero transaction costs, stop fills ignore gap-downs, RS 1.0 vs 1.2 contradiction (default view unbacktested), SimFin key hardcoded in git, venv tracked.
- **`FABLE_REVIEW_REMEDIATION_PLAN.md` created** (design/): 6 phases, Sonnet-executable. Session 1 = RS decision + config freeze/pre-registration + hygiene → unblocks paper trading.
- **`BREAKOUT_ENHANCEMENT_PLAN.md` created** (design/): breakout inventory (already core entry model) + 4 gated phases (Config D/E backtest → scan preset → at-pivot badges → /breakout-watch skill).
- **Golden Rule 18 added**: "Reused OOS is not OOS — freeze before forward test."
- ROADMAP priority order rebuilt (remediation #1); README mirrored.

### Day 77 Summary (IBKR Screener Pipeline — Research Complete)
- **Pure research session.** No code changes.
- **IBKR 2.0 screener integration**: documented all factors from screenshots, designed 10-filter configuration derived from STA's Minervini/SEPA thesis.
- **3-LLM audit** (Perplexity + GPT + Gemini): all three raised EarnGrw% floor, tightened EMA caps, replaced Quick Ratio with 52W High Proximity.
- **Final 10 filters validated**: Market Cap ≥1B, AvgVol ≥$5M, Price/EMA(200) 1.05–1.65, Price/EMA(50) 1.00–1.20, ROE ≥15, EarnGrw% ≥20, Inst.Held 25–90, 52W High Proximity ≤-25%, MACD Histogram ≥0, Change% -2 to +8.
- **`/ibkr-scan` skill design complete** — parses IBKR screenshots via Claude vision, calls STA API, ranks top 5–10.
- 3 research docs created.

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

1. **Fable Remediation Phase 4** — `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md`: survivorship-free re-validation (the big one — rebuild backtest universe without hindsight bias, 1–2 dedicated sessions).
2. **Fable Remediation Phase 5** — paper-trading instrumentation (entry-slippage logging, regime snapshots).
3. **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM).
4. **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
5. **Paper trading** — PRIMARY FOCUS. Config is frozen and pre-registered — can start any time.
6. **Breakout Plan Phase 0** — Config D/E backtest, now unblocked (remediation Phase 2 done).
7. **Breakout Plan Phases 2–3** — scan badges + `/breakout-watch` skill, unblocked (engine wired Day 79).
8. **Build N4: Market Phase synthesis** — Research done (Day 76). Queued behind the above.
9. **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
10. **Value Tab Phase 2 / Price Structure Phase 2 / N3 / Canadian Analyze page** — queued.

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
| 77 | IBKR screener pipeline research complete. 3-LLM audit (Perplexity+GPT+Gemini). 10 validated filters. /ibkr-scan skill design done. No code changes. |
| 78 | Fable 5 full-system audit. Remediation plan + Breakout enhancement plan created (design/). Golden Rule 18 (reused OOS). Priorities rebuilt — remediation #1, then paper trading. No code changes. |
| 79 | Fable Remediation Phases 0-3 executed: RS threshold resolved, config frozen, repo hygiene, MR transaction costs, gap-aware fills, metrics.py stats overhaul, JS/Python verdict parity fixed (86,400-combo grid, 1 bug found+fixed), fundamentals mismatch measured (40.0%), RS fallback fixed both sides. Breakout engine wired + validated. Golden Rule 19 (grid-test parity). Version v4.37 (BE v2.36, FE v4.36). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
