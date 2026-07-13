# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 83 — end of day (July 12, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 83 |
| Version | v4.42 (Backend v2.37, Frontend v4.38, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY83_SHORT.md (consolidates Day 82, which had no dedicated status file, plus Day 83's own work) |
| Latest Issues | KNOWN_ISSUES_DAY83.md |
| Latest API | API_CONTRACTS_DAY79.md (no API contract changes Day 83 — `fetchBreakout()` reuses the existing `/api/breakout/<ticker>` endpoint) |
| Focus | **Analyze page / Scan tab / Tradier code-quality fix plan is documented but NOT yet executed (`docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`) — next session should either triage which groups to fix or wait for direction. Data-source reliability fixed this session (5 bugs + a real cross-process rate-limiter/circuit-breaker state gap, now Golden Rule 22). Paper trading itself: still 0 closed trades — unchanged, expected to take months, see the Day 82 estimate below.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 83 Summary (Data-Source Reliability Fixes + BottomLineCard Removed + Analyze/Scan/Tradier Fix Plan Documented — v4.42)
- **Data-source review (5 bugs fixed)**: cache period mismatch, an uncached MR signal route, AlphaVantage rate-limiter token waste (`_check_availability()` was consuming a token via `check_rate_limit()` on every non-HTTP check), uncached VIX quotes, and dead Stooq code removed.
- **Cross-process state architecture gap fixed**: the rate-limiter and circuit-breaker (`rate_limiter.py`, `circuit_breaker.py`) were in-memory, per-process state — the Flask backend and the separate `daily_job.py` paper-trading process were silently NOT sharing rate-limit budgets or circuit-breaker trip state with each other. Rebuilt on a shared SQLite store (`backend/data/provider_state.db`). **New Golden Rule 22** codifies this.
- **UI cleanup (user-flagged via screenshot)**: deleted `BottomLineCard.jsx` (480 lines) — verdict was rendered 3x on one page, its bullets reworded facts the Categorical Assessment card already showed; confirmed via code read it was a safe, self-contained leaf component before deleting. Added the previously-orphaned single-ticker breakout endpoint (`/api/breakout/<ticker>`, live since Day 78) to the Analyze Stock page — badge in Simple view, dedicated card in Full Analysis view (the slot Bottom Line vacated). Verified in a real browser session.
- **Deep Fable audit, 3 parallel dispatches** (Analyze page Full Analysis cards, Scan Market tab, a newly-added Tradier API key): synthesized into `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` — 6 real bugs (incl. a Scan-tab/paper-trading-engine candidate-set divergence from an `order_by()` override, and a negative-stop-price bug in Trade Setup Card, both confirmed true by direct code read), 6 DRY violations, a dead-code inventory, a fully-specified Tradier provider build (OHLCV/quote fallback, confirmed production token — NOT dividend-adjusted, no options/fundamentals scope creep), and 6 polish items. One raw audit claim was checked and corrected (MR Signal Card does NOT show null-edge signals — only its display labels are stale). **Documented only, per explicit user request — nothing in the fix plan has been executed or triaged yet.**
- Paper trading status unchanged: still 0 closed trades, 2 pending MR signals — this session found no reason to intervene.

### Day 82 Summary (Breakout Plan Finished + Fable Process/Hygiene Audit — v4.41)
- **Breakout Enhancement Plan Phase 0**: Config D (confirmed-breakout-only) backtested — **0 trades**, both IS and OOS periods. Genuine, root-caused finding (not a bug): `pattern_detection.py`'s confidence score measures pre-breakout base quality, which structurally can't coexist with `broken_out` status. Config E (anticipatory-only) captured 83–90% of Config C's real trades. Verified Config C's own numbers unchanged (git stash diff) before/after adding D/E. Full writeup: `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY81.md`.
- **Breakout Enhancement Plan Phases 2–3**: `/api/breakout/batch` endpoint (inside `breakout_routes.py`, no `backend.py` changes needed), a new "Breakout" badge column on the Scan tab (verified in a real headless-Chromium session — installed Playwright locally since no project run-skill existed), and `.claude/commands/breakout-watch.md` (reuses the batch endpoint, verified against the live backend). **Only Phase 1 (scan preset) remains of the entire plan**, gated on user approval.
- **User-requested "core Fable audit"**: dispatched a Fable-model agent (read-only) to assess goal fidelity, progress honesty, process bloat, and codebase hygiene. Full report: `docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`. User approved 4 of the recommendation buckets to act on immediately (declined the 5th — consolidating the Golden Rules/doc-rotation process itself — as a bigger future decision):
  - **Git risk items fixed**: `frontend/node_modules` (40,801 files, ~101MB) was tracked in git — untracked + gitignored. `backend/providers/alphavantage_provider.py` (the live production growth-metrics provider) was untracked — now tracked. Checked the audit's claim that `fmp_provider.py` is dead code and found it **wrong** — verified it's a deliberate placeholder, still imported; left it alone.
  - **Stale docs reconciled**: `KNOWN_ISSUES_DAY81.md`, `MEMORY.md` and its linked files, and `PAPER_TRADING_PREREGISTRATION.md` all still described breakout Phases 0/2–3 as not-started and/or the pre-Day-81 MR liquidity gate — all corrected. Also caught `BACKEND_VERSION` in code (`'2.35'`) had drifted from what docs claimed (`v2.38`) — the exact class of drift a Day 78 fix was meant to prevent, recurring; corrected to `2.36` (ground truth = code, bumped for today's real changes).
  - **Safety nets added**: dead-man switch in `/sta-start` (warns if the paper-trading launchd job hasn't run in >3 days), automatic ledger backup after every `daily_job.py` run (`ledger.backup_db()`, SQLite's safe backup API, 30-copy rolling retention), and a computed time-to-50-trades estimate — **MR ~7 months, momentum ~2.2 years at backtest-implied rates (both highly uncertain, re-estimate after 4-6 weeks of real data)**.
  - **Dead code deleted**: `backend/validation/forward_tracker.py` + 3 orphaned `/api/forward-test/*` routes (confirmed zero frontend callers), 5 old `App_dayN.jsx`/`api_dayN.js` snapshot files, 12 one-shot root test/debug scripts, a redundant backup zip, and ~21 stale scratch artifacts (test/scan/validation result dumps, `backend.log`, empty `cache.db`) — all verified individually before deletion, not deleted on the audit's word alone.
- Paper trading status unchanged by any of the above: still 0 closed trades, 2 pending MR signals (GOOGL, ABBV) — this session found no reason to intervene, which is itself the correct outcome (nothing should touch the frozen config).

### Day 81 Summary (Automated Paper Trading Engine Built + Live MR Liquidity Gate Fix — v4.39)
- **User-directed, same-session build** (not a pre-planned roadmap item): asked whether the system could generate paper-trading signals and a ledger itself rather than relying on manual Forward Test logging. Answer: yes, and it's strictly more rigorous — a daily unattended job that takes every qualifying signal from the frozen config with zero human filtering removes the exact selection bias the whole remediation effort was fighting.
- **New `backend/paper_trading/` package**: `ledger.py` (SQLite, `validation_results/paper_trading_ledger.db`, stats via the same `metrics.py` the backtest uses), `live_signals.py` (momentum candidates via the exact `/api/scan/tradingview?strategy=best` query, filtered through live `categorical_engine.run_assessment()` + R:R>=1.2; MR candidates via `detect_mr_signal()`), `daily_job.py` (activate pending signals at the real next-day open → step open positions → generate new signals; idempotent).
- **`scan_queries.py`** (new): factored the Config C TradingView query out of `backend.py`'s scan route so the live Scan tab and the paper-trading engine use one implementation, not two that can drift (Golden Rule 19's lesson applied preemptively). Verified the refactored route returns identical results.
- **`trade_simulator.py`/`mr_simulator.py` gained a `live_mode` parameter**: lets the live engine replay the exact backtested exit logic (stop/target/trailing-EMA/breakeven) one day at a time instead of reimplementing it as a separate state machine. Verified byte-for-byte identical to the batch backtest on 40 synthetic trades (30 momentum + 10 MR) before wiring it in.
- **Live MR liquidity gate fixed** (closes the Day 80 known gap / old Next-Session-Priority #2): `mean_reversion.py`'s `detect_mr_signal()` now requires price>$10 + 20-day avg dollar volume>$25M (was price>$5 + 500K share-volume), matching the backtest's Day 79 re-test gate exactly.
- **macOS launchd agent installed and confirmed firing**: `com.sta.papertrading.daily.plist`, weekdays 16:30 CT (~90min after close). Idempotent (checks `job_runs` table) and self-healing for missed days on already-open positions (full historical replay) — but cannot retroactively reconstruct entry signals for days the screener wasn't queried live (TradingView has no point-in-time API). Documented as a known limitation, not treated as a bug.
- **First live run (2026-07-10)**: 0 momentum signals (2 TradingView candidates found, both correctly rejected on the fundamentals/R:R leg), 2 MR signals queued (GOOGL, ABBV) — cross-checked against `/api/mr/scan` directly, matched.
- Not done: no UI surfacing of the new ledger (separate from the manual Forward Test tab's localStorage) — deferred until trades accumulate.

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

1. **Triage the UI Code Quality Fix Plan** — `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` (written Day 83, covers Analyze page cards + Scan Market tab + a Tradier provider build spec). Nothing in it has been executed yet — decide which of Groups A-E to fix now vs. later, or call out the 2-3 most urgent items. Group A (6 real bugs, incl. a Scan-tab/paper-trading-engine candidate-set divergence and a negative-stop-price bug) is the natural starting point if picking one group.
2. **Let paper trading accumulate** — expect it to take a while: **~7 months for MR, ~2.2 years for momentum at backtest-implied rates (Day 82 estimate, highly uncertain — re-estimate after 4-6 weeks of real data)**. `/sta-start` warns automatically if the launchd job goes stale (>3 days). Check progress with `venv/bin/python paper_trading/daily_job.py --report`. Nothing to build here.
3. **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
4. **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
5. **Breakout Plan Phase 1** (near-breakout scan preset) — the only remaining phase of the whole plan; needs explicit user go-ahead (small feature, mid-freeze).
6. **Build N4: Market Phase synthesis** — Research done (Day 76). Queued behind the above.
7. **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
8. **Value Tab Phase 2 / Price Structure Phase 2 / N3 / Canadian Analyze page** — queued.
9. **(Optional, low priority) Surface the paper-trading ledger in the UI** — currently CLI/DB-only (`--report` flag); a Forward-Test-tab display would be a nice-to-have once trades accumulate, not a prerequisite.
10. **(Deferred, user's own call)** The Day 82 Fable audit's 5th recommendation bucket — consolidating the Golden Rules/doc-rotation process itself (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`, Section F "REMOVE/DECLUTTER" item 4) — was deliberately not applied; it's a bigger, more opinionated change than the hygiene fixes and should only happen if the user explicitly wants it.

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
└── status/                        <- Daily status
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                   <- Older than 15 days
```
*(Day 82: removed `backup_pre_cleanup_day68/` — a tracked backup zip redundant with git history itself; deleted in the Fable hygiene pass.)*

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

# Dead-man check (Day 82) — last date the paper-trading job actually ran
sqlite3 backend/validation_results/paper_trading_ledger.db "SELECT MAX(run_date) FROM job_runs;"
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
| 82 | Breakout Plan Phase 0 (Config D=0 trades, root-caused) + Phases 2-3 (batch endpoint, badges, skill) — plan essentially complete. User-requested Fable process/hygiene audit: fixed 2 real git risk items (untracked provider, tracked node_modules), deleted ~20 dead files, reconciled stale docs (CLAUDE_CONTEXT, KNOWN_ISSUES_DAY81, MEMORY.md, PAPER_TRADING_PREREGISTRATION.md, BACKEND_VERSION drift), added dead-man switch + ledger backup + time-to-50-trades estimate. Version v4.41 (BE v2.36 — corrected down from a drifted v2.38 claim). |
| 83 | Data-source review: 5 bugs fixed + a real cross-process rate-limiter/circuit-breaker state gap fixed (shared SQLite store), Golden Rule 22 added. Removed redundant BottomLineCard (user-flagged), added breakout status to the Analyze Stock page. Deep 3-way Fable audit (Analyze page cards, Scan tab, Tradier API eval) synthesized into an executable fix plan (`UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`) — documented only, not yet triaged/executed. Version v4.42 (BE v2.37, FE v4.38). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
