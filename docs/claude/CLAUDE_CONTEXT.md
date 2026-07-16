# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 89 — end of day (July 16, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 89 |
| Version | v4.47 (Backend v2.43, Frontend v4.42 unchanged, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY89_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY89.md |
| Latest API | No API contract changes this session (see API_CONTRACTS_DAY88.md for the latest) — internal signal-generation logic only |
| Focus | **Complete feature freeze in effect, with a second scoped exception (same rationale as Day 88).** User asked how the automated engine works and how to get to ~10 signals/day faster. Widened the MR arm's live universe from a static 54-ticker list to a dynamic ~150-ticker TradingView scan — legitimate because it's candidate-pool breadth, not a threshold re-tune (Golden Rule 18 still holds). A live test at limit=300 found a real bug: it tripped TwelveData's rate limiter, cascading to yfinance/Tradier, silently failing the same tail-end tickers every run (deterministic market-cap sort) — new Golden Rule 25. Recalibrated to limit=150, re-verified: 8 signals in one clean run vs. 0-2/day historically. Also directly verified (not assumed) that both Tradier and TwelveData are genuinely functional, per user's skepticism from seeing circuit-breaker-open log lines. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 89 Summary (MR Universe Widened for Faster Sample Accumulation — Rate-Limit Bug Found + Fixed — v4.47)
- **Continuation of the same session.** User asked how the automated paper-trading engine works and how to get to at least 10 signals/day so the 50-trade confirmation bar arrives faster.
- **Explained the mechanics and the one legitimate lever**: momentum already scans market-wide; MR only checked a static 54-ticker list. Widening the *candidate pool* (more tickers checked against the same frozen rule) is legitimate; loosening the frozen RSI(2)/R:R thresholds to manufacture more signals would not be — that's exactly what Golden Rule 18 forbids, since it would mean paper-trading a different, unvalidated strategy.
- **Built `scan_queries.build_mr_universe_query()`** — dynamic TradingView liquid-universe scan replacing the static list for the automated engine only (the manual `/api/mr/scan` UI endpoint is untouched). Momentum's raw-candidate limit also raised 50→150.
- **First live test (limit=300) found a real bug, not just a slow run**: tripped TwelveData's rate limiter, opening its circuit breaker, cascading to yfinance and Tradier — ~35% of ~231 tickers failed on every provider. Because the query sorts by market cap descending, this would have silently and *permanently* excluded the same tail-end tickers every single day, not a random subset. **New Golden Rule 25.**
- **Recalibrated to limit=150** (the number that completed cleanly) and re-verified: 8 real MR signals in one clean run, zero rate-limit failures — versus the historical 0-2/day baseline.
- **Directly verified Tradier and TwelveData are genuinely functional**, per the user's skepticism from seeing "Circuit breaker OPEN" in logs — tested both providers directly (bypassing the app's breaker wrapper), got real current quotes/OHLCV from each, and watched both breakers self-heal live (OPEN → HALF_OPEN → CLOSED) once real calls succeeded after cooldown. They were legitimately tripped by the earlier stress test, not broken.
- Scoped as the same kind of freeze exception as Day 88 — directly aids the paper-trading gate's sample-accumulation rate, not general product work. Version v4.46 → v4.47 (Backend v2.42 → v2.43, Frontend unchanged — no frontend files touched this session).

### Day 88 Summary (Paper Trading Ledger Surfaced in UI — Scoped Freeze Exception — v4.46)
- **Continuation of Day 87's session.** After the complete feature freeze was declared, user asked two follow-ups about the automated paper-trading engine: where to see the ledger visually (is it in the Forward Test tab?), and whether a manual "missed run" trigger button could be added.
- **Confirmed the ledger had zero UI surface**: the Forward Test tab is a separate, older, manual localStorage trade journal (`forwardTesting.js`) — no connection to the automated engine's SQLite ledger (`backend/paper_trading/`, built Day 81), which was CLI/`--report`-only until now.
- **Scoped as the one legitimate freeze exception, not a resumption of general feature work** — user's own words: "we built this only because it's aiding our fwd testing... everything else is on freeze."
- **Built and verified live**: two new endpoints (`GET /api/paper-trading/status` read-only, `POST /api/paper-trading/trigger` wraps the exact same `run_daily_job(force=True)` the launchd scheduler already calls — no new trading logic) and a new `AutomatedPaperTradingPanel.jsx` component in the Forward Test tab (visually distinct from the manual journal, shows both systems' stats + a staleness warning + the trigger button). Verified end-to-end by actually triggering a run: `lastRunDate` advanced, momentum open positions 1→2, MR open positions 2→4 — confirming the trigger and status endpoints read/write the same ledger, not just independently-plausible code.
- Version v4.45 → v4.46 (Backend v2.41 → v2.42). New API_CONTRACTS_DAY88.md. No new Golden Rule — straightforward build, no surprises.

### Day 87 Summary (Backlog Cleanup — Breakout Plan Complete + N4 + Price Structure Phase 2 — Complete Freeze Declared — v4.45)
- **User asked what 3 bundled backlog items (Breakout Plan Phase 1, N4 Market Phase, "Value Tab Phase 2/Price Structure Phase 2/N3") actually were, why they mattered, and whether they mattered from first principles** given the project's feature freeze. Answered directly: none of them touch the paper-trading gate (the only thing that actually matters right now), all are informational/entry-signal decoration — the 10%-of-results bucket per Van Tharp, not the 90%-of-results position-sizing/risk bucket. User heard the argument, decided to close out the ones that were genuinely quick, then declare a full freeze.
- **Caught 2 scope mischaracterizations before building, not after** (Golden Rule 24, new this session): N3 (gap-fill detection) turned out to have no design doc at all — deferred, needs its own design session. Value Tab Phase 2's actual spec (`VALUE_TAB_SPEC.md`) explicitly requires nightly batch-prefetch infrastructure and says "build only after feature freeze lift" — building it on-demand (the natural approach) would have contradicted its own documented design and blown through AlphaVantage's ~8-tickets/day free-tier budget. A diagnostic check to verify AV field names before writing code burned the day's remaining AV quota (2 of 3 test calls rate-limited by AlphaVantage's own servers) — confirmed `INCOME_STATEMENT` fields but not `BALANCE_SHEET`/`CASH_FLOW`. Both deferrals were confirmed with the user before proceeding.
- **Shipped 3 items, each exhaustively verified, not spot-checked:**
  1. **Breakout Enhancement Plan Phase 1** ("Near Breakout" scan preset) — completes the entire plan. New `strategy=breakout` option: Stage-2 stocks within 8% of 52W high, mkt cap≥$2B, price>$10, RSI 50-70, ADX≥20, ADV≥$5M. The 8%-from-high and dollar-volume filters are post-filters (TradingView `col()` can't do the needed arithmetic) applied after fetching a wider net so the post-filter isn't starved. All 50 returned candidates checked against every filter — zero violations.
  2. **N4 Market Phase Synthesis** — new `market_phase_engine.py` + `/api/market/phase`. Classifies market conditions into 5 phases via a transparent 3×3 grid (SPY trend × VIX level), breadth/sector as supporting evidence not gates. Grid logic exhaustively unit-tested (all 9 cells + refinement rule + boundaries). Displayed in a new Context tab banner.
  3. **Price Structure Card Phase 2** — new `market_structure_engine.py`, HH/HL/LH/LL classification wired into `/api/sr/<ticker>`'s `meta.marketStructure`. Deliberately did NOT reuse the spec's assumed `find_pivot_points()` (doesn't exist) or `support_resistance.py`'s `_detect_zigzag_pivots()` (sorts+dedupes by price, destroying the chronological order needed) — wrote a separate detector instead of touching the frozen core S&R engine. **Exhaustive synthetic testing caught a real bug**: Transition detection wasn't filtering unlabeled bootstrap pivots, so a genuine reversal wasn't classified correctly — fixed before shipping.
- Version v4.44 → v4.45 (Backend v2.40 → v2.41). New API_CONTRACTS_DAY87.md, Golden Rule 24 added. **Complete feature freeze now formally in effect** — bug fixes and paper-trading monitoring only.

*(Day 86's summary rotated out — full detail preserved in `docs/claude/status/PROJECT_STATUS_DAY86_SHORT.md`. Day 85's is in `PROJECT_STATUS_DAY85_SHORT.md`.)*

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

**Complete feature freeze in effect as of Day 87** — bug fixes and paper-trading monitoring only, until 50+ live trades confirm the momentum/MR edges. Days 88-89 added two narrowly-scoped, explicitly-agreed exceptions (paper-trading ledger UI + manual trigger; MR universe widened for faster sample accumulation — see below); the items still "queued" (N3, Value Tab Phase 2) are backlog, not freeze exceptions — they need their own design sessions before any code, per Golden Rule 24.

1. **Let paper trading accumulate** — PRIMARY FOCUS, the only thing actually gating capital allocation. MR's sample rate should now be meaningfully faster after Day 89's universe widening (8 signals in one test run vs. 0-2/day historically) — momentum's rate is largely unchanged (bottleneck is qualifying candidates, not scan limit). Prior estimate (**~7 months for MR, ~2.2 years for momentum**, Day 82, highly uncertain) should be re-derived once a few weeks of the new MR rate are observed. `/sta-start` warns automatically if the launchd job goes stale (>3 days). Check progress via the Forward Test tab's status panel (Day 88) or `venv/bin/python paper_trading/daily_job.py --report`. Nothing to build here.
2. **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
3. **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
4. **N3 gap-fill detection** — needs its own design session first (Day 87 finding: no spec exists yet, only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`).
5. **Value Tab Phase 2** — needs its own batch-prefetch infrastructure design session first (Day 87 finding: `VALUE_TAB_SPEC.md` explicitly requires a nightly watchlist-prefetch job for AlphaVantage's ~8-tickets/day budget; on-demand fetching would contradict the documented design).
6. **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
7. **Price Structure Phase 3** (visual chart via lightweight-charts) / Canadian Analyze page — queued.
8. **(Optional, low priority) Scan tab batch breakout badges** — distinguish `NOT_READY` from a failed fetch (currently both render "—"); same bug class as the Day 85 single-ticker fix, not yet requested at this location.
9. **(Optional, low priority) Master Framework Watchlist's Name/Market Cap columns** — still show N/A (Volume/Change % fixed Day 86, free); Name/Market Cap would need a separate fundamentals call per ticker, deferred by explicit user choice.
11. **(Deferred, user's own call)** The Day 82 Fable audit's 5th recommendation bucket — consolidating the Golden Rules/doc-rotation process itself (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`, Section F "REMOVE/DECLUTTER" item 4) — was deliberately not applied; it's a bigger, more opinionated change than the hygiene fixes and should only happen if the user explicitly wants it.

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
| 85 | Root-caused a "breakout card shows nothing" report to `start.sh` leaving both dev servers' stdout tied to the launching terminal — closing it broke every `print()`-logging request path (Golden Rule 23). Fixed a second bug underneath: NOT_READY breakout status was hidden instead of shown muted (per the engine's own spec). Wrote a portable TradingView screener reference doc. Scoped and built a new "Master Framework Watchlist" Scan tab preset (76 tickers from the user's Notion investment frameworks), exhaustively verified against the live backend (caught 3 ticker-format bugs + 1 unsupported ticker), user-tested live. No version bump. |
| 86 | User's first live test of the Master Framework Watchlist found Name/Sector/Change/Volume/Market Cap all showing N/A. Fixed Volume/Change for free (`/api/sr/<ticker>` already fetched the OHLCV needed, wasn't returning it) — fixes both curated watchlists at once; Name/Market Cap deferred by explicit user choice (would need a per-ticker fundamentals call). New API_CONTRACTS_DAY86.md. Version v4.43 → v4.44 (BE v2.39 → v2.40, FE v4.39 → v4.40). |
| 87 | Backlog cleanup session: Breakout Enhancement Plan Phase 1 shipped (completes the whole plan), N4 Market Phase Synthesis built, Price Structure Card Phase 2 built (HH/HL/LH/LL structure). N3 and Value Tab Phase 2 scoped and explicitly deferred — both needed their own design/infra work, not quick adds (Golden Rule 24). Exhaustive testing caught a real Transition-detection bug in the new market structure classifier before shipping. **Complete feature freeze declared.** Version v4.44 → v4.45 (BE v2.40 → v2.41, FE v4.40 → v4.41). |
| 88 | Paper trading ledger surfaced in UI (Forward Test tab panel + `/api/paper-trading/status`/`trigger`) — agreed as the one scoped exception to Day 87's freeze since it directly aids the paper-trading gate itself. Verified live end-to-end (triggered a real run, confirmed ledger state updated). Version v4.45 → v4.46 (BE v2.41 → v2.42, FE v4.41 → v4.42). |
| 89 | MR arm's live universe widened from a static 54-ticker list to a dynamic ~150-ticker TradingView scan (8 signals/run vs. 0-2/day historically) — same scoped-exception rationale as Day 88. Live testing at limit=300 found a real rate-limit cascade bug (TwelveData → yfinance → Tradier, same tail-end tickers silently excluded every run due to deterministic sort) — new Golden Rule 25, recalibrated to limit=150. Also directly verified Tradier/TwelveData are genuinely functional per user's skepticism. Version v4.46 → v4.47 (BE v2.42 → v2.43, FE unchanged). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
