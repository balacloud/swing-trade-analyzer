# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 84 — end of day (July 13, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 84 |
| Version | v4.43 (Backend v2.39, Frontend v4.39, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY84_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY84.md |
| Latest API | API_CONTRACTS_DAY79.md (no API contract changes Day 84) |
| Focus | **The entire UI Code Quality Fix Plan (`docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`) is now fully executed — all 5 groups (A-E), every fix browser/API-verified. Nothing left to triage from it. Paper trading remains the primary open item: still accumulating, expected to take months (see estimate below) — that has not changed and this session found nothing that would.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 84 Summary (UI Code Quality Fix Plan — ALL Groups A-E Executed — v4.43)
- **Picked up the Day 82 fix plan and executed it end to end**, in the plan's own suggested order (A → C → B → D → E), verifying every single fix live against the running app rather than trusting code review alone.
- **Group A (6 real bugs, commit `c48d16d8`)**: Scan tab/paper-trading candidate-set divergence fixed (an `order_by()` override bug — verified byte-identical output after the fix); Trade Setup Card's negative-stop-price bug fixed (verified with a synthetic edge case); Price Structure Card's dead "pattern forming" watch item fixed (verified live on JPM); 3 conflicting liquidity thresholds unified (verified on small-cap ASIC); Nirmal watchlist's silent-failure bug fixed (verified both directions — backend down/up); MR Signal Card's stale labels fixed (verified on ABBV).
- **Groups B-E (commit `b77e06ff`)**: Pattern Detection Card and Categorical Assessment's copy-pasted tiles both extracted into shared components (`PatternMiniCard.jsx`, `AssessmentTile.jsx`) — the latter deliberately preserved each category's intentional color differences rather than flattening them. The legacy 0.011-correlation `determineVerdict()` function deleted entirely after tracing that its fallback path was permanently unreachable. RS Card's fake "percentile" relabeled. A dormant Canadian-ticker bug fixed in the paper-trading engine's `live_signals.py`. ~7 dead functions/exports and ~37 debug `console.log` lines removed. New `backend/providers/tradier_provider.py` built as a 3rd-tier OHLCV/quote fallback — verified with forced-failover tests (TwelveData + yfinance monkey-patched to fail, no real credentials touched, confirmed real data returned from Tradier for both OHLCV and a VIX quote). Breakout Status card gained a loading skeleton and now surfaces previously-dropped `warnings`/`breakoutLevel` fields; 2 stale-response-race bugs fixed via `useRef`-tracked request IDs.
- **Backend v2.36 → v2.39 across the arc.** `ROADMAP.md` gained a "COMPLETE" section for the whole plan (also caught and fixed a version-drift gap on ROADMAP's own version line, stale since Day 81). README.md's Roadmap section, also stale since Day 80, brought current.
- Paper trading status unchanged: this session touched zero trading logic, config, or thresholds — purely UI/reliability code quality work.

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

1. **Let paper trading accumulate** — PRIMARY FOCUS, the UI Code Quality Fix Plan is now fully done so this is the only thing actually gating capital allocation. Expect it to take a while: **~7 months for MR, ~2.2 years for momentum at backtest-implied rates (Day 82 estimate, highly uncertain — re-estimate after 4-6 weeks of real data)**. `/sta-start` warns automatically if the launchd job goes stale (>3 days). Check progress with `venv/bin/python paper_trading/daily_job.py --report`. Nothing to build here.
2. **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
3. **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
4. **Breakout Plan Phase 1** (near-breakout scan preset) — the only remaining phase of the whole plan; needs explicit user go-ahead (small feature, mid-freeze).
5. **Build N4: Market Phase synthesis** — Research done (Day 76). Queued behind the above.
6. **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
7. **Value Tab Phase 2 / Price Structure Phase 2 / N3 / Canadian Analyze page** — queued.
8. **(Optional, low priority) Surface the paper-trading ledger in the UI** — currently CLI/DB-only (`--report` flag); a Forward-Test-tab display would be a nice-to-have once trades accumulate, not a prerequisite.
9. **(Deferred, user's own call)** The Day 82 Fable audit's 5th recommendation bucket — consolidating the Golden Rules/doc-rotation process itself (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`, Section F "REMOVE/DECLUTTER" item 4) — was deliberately not applied; it's a bigger, more opinionated change than the hygiene fixes and should only happen if the user explicitly wants it.

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
| 84 | Executed the entire UI Code Quality Fix Plan (all Groups A-E) from the prior day's doc: 6 real bugs, 6 DRY-violation cleanups (incl. deleting the legacy 0.011-correlation verdict function), ~7 dead-code items + ~37 debug logs removed, a new Tradier provider built (3rd-tier OHLCV/quote fallback, verified with forced-failover tests), and 4 UI polish items. Every fix browser/API-verified, not just code-reviewed. ROADMAP.md and README.md version-drift caught and fixed. Version v4.43 (BE v2.39, FE v4.39). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
