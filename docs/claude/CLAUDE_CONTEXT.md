# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 81 — end of day (July 10, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 81 |
| Version | v4.39 (Backend v2.38, Frontend v4.37, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY81_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY81.md |
| Latest API | API_CONTRACTS_DAY79.md (no API contract changes Day 81 — /api/scan/tradingview refactored internally, response shape unchanged) |
| Focus | **Automated paper trading engine built and live (Day 81) — daily unattended job now takes every qualifying signal with zero human filtering, more rigorous than manual Forward Test logging. Both momentum (PF 1.40) and MR (PF 1.16) still need 50+ live trades before capital allocation; the engine is now accumulating them automatically.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 81 Summary (Automated Paper Trading Engine Built + Live MR Liquidity Gate Fix — v4.39)
- **User-directed, same-session build** (not a pre-planned roadmap item): asked whether the system could generate paper-trading signals and a ledger itself rather than relying on manual Forward Test logging. Answer: yes, and it's strictly more rigorous — a daily unattended job that takes every qualifying signal from the frozen config with zero human filtering removes the exact selection bias the whole remediation effort was fighting.
- **New `backend/paper_trading/` package**: `ledger.py` (SQLite, `validation_results/paper_trading_ledger.db`, stats via the same `metrics.py` the backtest uses), `live_signals.py` (momentum candidates via the exact `/api/scan/tradingview?strategy=best` query, filtered through live `categorical_engine.run_assessment()` + R:R>=1.2; MR candidates via `detect_mr_signal()`), `daily_job.py` (activate pending signals at the real next-day open → step open positions → generate new signals; idempotent).
- **`scan_queries.py`** (new): factored the Config C TradingView query out of `backend.py`'s scan route so the live Scan tab and the paper-trading engine use one implementation, not two that can drift (Golden Rule 19's lesson applied preemptively). Verified the refactored route returns identical results.
- **`trade_simulator.py`/`mr_simulator.py` gained a `live_mode` parameter**: lets the live engine replay the exact backtested exit logic (stop/target/trailing-EMA/breakeven) one day at a time instead of reimplementing it as a separate state machine. Verified byte-for-byte identical to the batch backtest on 40 synthetic trades (30 momentum + 10 MR) before wiring it in.
- **Live MR liquidity gate fixed** (closes the Day 80 known gap / old Next-Session-Priority #2): `mean_reversion.py`'s `detect_mr_signal()` now requires price>$10 + 20-day avg dollar volume>$25M (was price>$5 + 500K share-volume), matching the backtest's Day 79 re-test gate exactly.
- **macOS launchd agent installed and confirmed firing**: `com.sta.papertrading.daily.plist`, weekdays 16:30 CT (~90min after close). Idempotent (checks `job_runs` table) and self-healing for missed days on already-open positions (full historical replay) — but cannot retroactively reconstruct entry signals for days the screener wasn't queried live (TradingView has no point-in-time API). Documented as a known limitation, not treated as a bug.
- **First live run (2026-07-10)**: 0 momentum signals (2 TradingView candidates found, both correctly rejected on the fundamentals/R:R leg), 2 MR signals queued (GOOGL, ABBV) — cross-checked against `/api/mr/scan` directly, matched.
- Not done: no UI surfacing of the new ledger (separate from the manual Forward Test tab's localStorage) — deferred until trades accumulate.

### Day 80 Summary (Fable Remediation Phases 4–5 Complete + MR Liquidity Re-Test — v4.38)
- **Phase 4**: survivorship-free re-validation. Random 400-ticker sample (seed=42) from SimFin's 3,788-ticker coverage — no hand-picking. **Config C: PF 1.61→1.40 (real, not yet significant, p=0.094). MR unrestricted: PF 0.99 (clean null, 6,151 trades).**
- **Phase 5**: paper-trading instrumentation. `signalClosePrice`/`entrySlippagePct` + `regimeSnapshot` now logged on every paper trade (Forward Test tab), reusing existing categorical logic. **This completes all 5 phases of the Fable Remediation Plan.**
- **MR liquidity re-test (user-directed, one-time)**: original MR backtest had no dollar-volume gate at all. Added price>$10, 20d ADV>$25M (pre-committed, not a re-tune). **Result: PF 0.99→1.16, Sharpe -0.10→1.30 — real but still not significant (block bootstrap p=0.064).** MR now same tier as momentum: unconfirmed, needs live paper trading. Live detector (`mean_reversion.py`) not yet updated with this gate — flagged as an open item.
- **Golden Rule 20 added**: a pre-committed, principled restriction decided before seeing results is a legitimate one-time re-test, distinct from re-tuning to chase a number.
- Both trading systems now require 50+ live paper trades before capital allocation — neither is backtest-confirmed. Paper trading is the next real test.

### Day 79 Summary (Fable Remediation Phases 0–3 Executed + Breakout Wired — v4.37)
- **Phase 0**: RS threshold resolved (simple checklist 1.2→1.0, matching Config C). `PAPER_TRADING_PREREGISTRATION.md` created — config frozen.
- **Phase 1**: SimFin key → `.env`, `backend/venv` untracked, `BACKEND_VERSION` constant, 3 dead files deleted.
- **Phase 2**: MR transaction costs added (PF 1.26→1.23 net, edge survives). Gap-aware stop/target fills in both simulators. `metrics.py` stats overhaul (scipy t-test, actual trades/year, block bootstrap, fixed-risk DD). **JS↔Python verdict parity: 86,400-combo grid found 1 real bug (HOLD-fallback missing `Neutral` risk branch) — fixed, now 100% parity.**
- **Phase 3**: Fundamentals mismatch measured at **40.0% disagreement** (live vs backtested) — mitigation choice pending user decision. Silent RS fallback fixed on both JS and Python sides.
- **Breakout engine wired**: `/api/breakout/<ticker>` (built by a parallel session, never registered) is now live and validated on 5 tickers + 1 edge case. `BREAKOUT_ENHANCEMENT_PLAN.md` reconciled.
- **Golden Rule 19 added**: systematic grid-test parity, not hand-picked vectors.
- Paper trading unblocked (config frozen). Remediation Phase 4 (survivorship-free re-validation) is next.

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

1. **Let paper trading accumulate** — PRIMARY FOCUS. The automated engine (`backend/paper_trading/`) now runs unattended daily (launchd, weekdays 16:30 CT) and is the primary path to the 50-trade bar for both momentum (PF 1.40) and MR (PF 1.16). Check progress with `venv/bin/python paper_trading/daily_job.py --report`. Nothing to build here — just let it run and periodically check in.
2. **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
3. **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
4. **Breakout Plan Phase 0** — Config D/E backtest, unblocked.
5. **Breakout Plan Phases 2–3** — scan badges + `/breakout-watch` skill, unblocked (engine wired Day 79).
6. **Build N4: Market Phase synthesis** — Research done (Day 76). Queued behind the above.
7. **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
8. **Value Tab Phase 2 / Price Structure Phase 2 / N3 / Canadian Analyze page** — queued.
9. **(Optional, low priority) Surface the paper-trading ledger in the UI** — currently CLI/DB-only (`--report` flag); a Forward-Test-tab display would be a nice-to-have once trades accumulate, not a prerequisite.

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

# Paper trading ledger status (Day 81 — automated engine)
cd backend && venv/bin/python paper_trading/daily_job.py --report

# Manually trigger the daily paper-trading job (normally runs via launchd)
cd backend && venv/bin/python paper_trading/daily_job.py --force

# Check/disable the launchd scheduler
launchctl list | grep sta.papertrading
launchctl unload ~/Library/LaunchAgents/com.sta.papertrading.daily.plist
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
| 80 | Fable Remediation Phases 4-5 complete (survivorship-free re-validation + paper-trading instrumentation) — plan finished. MR liquidity re-test (user-directed, one-time): PF 0.99→1.16, still unconfirmed. Golden Rule 20 (pre-committed restriction vs re-tune). Version v4.38 (BE v2.37, FE v4.37). |
| 81 | Automated paper trading engine built (`backend/paper_trading/`): daily unattended job, no human signal filtering, launchd-scheduled. Shared TradingView query (`scan_queries.py`) and `live_mode` exit replay (`trade_simulator.py`/`mr_simulator.py`) prevent drift between backtest and live logic. Live MR liquidity gate fixed to match the backtested one. Version v4.39 (BE v2.38, Backtest v4.19). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
