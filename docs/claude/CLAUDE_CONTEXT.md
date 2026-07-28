# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 100 — end of day (July 28, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 100 |
| Version | v4.54 (unchanged — no app code touched Day 100) |
| Latest Status | PROJECT_STATUS_DAY100_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY100.md |
| Latest API | API_CONTRACTS_DAY98.md — unchanged since Day 98 |
| Focus | **Forward-testing accumulation remains the SOLE priority.** Day 100 was monitoring, verification, and documentation — no app code changed. Verified the Day 99 ledger fix under real live use (a mid-session Force Run correctly deferred to the prior day's close). Found and verified in code a real structural gap: neither automated track (momentum or MR) has any sector-correlation awareness in its entry gate — traced against a live example (a same-day semis-sector selloff), and connected to the project's own Day 78 block-bootstrap docstring, which already partially named this exact risk to the significance math but never reached the entry gate or trade count. Not actionable mid-freeze (would be a re-tune of a frozen gate); logged as Known Issue + new ROADMAP priority #15 (a scheduled/proactive breakout-alert watcher, idea only, not started). Also built and published a living reference doc, `docs/claude/design/HOW_STOCK_PICKING_WORKS.html`, explaining the Simple Checklist and Full Analysis verdict logic — explicitly meant to keep accumulating as real questions come up. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 100 Summary (Monitoring, Regime-Gap Finding, Living Doc — v4.54 unchanged)
- **Verified the Day 99 partial-bar fix under real live use**: user ran a real Force Run mid-session (10:31 EDT, market open); the one trade it closed (MR's NVO) correctly resolved against the prior day's real close, not the still-forming intraday bar.
- **Found and verified a real structural gap, prompted by a live example**: a same-day semis/AI-supply-chain sector selloff (MU, AMD, MRVL, etc.) raised the question of whether the automated engines account for sector-wide regime shifts. Checked `detect_mr_signal()` directly — exactly 4 conditions (RSI(2), price vs. its own 200-day SMA, price floor, dollar volume), zero regime/sector awareness. Momentum's verdict engine has broad VIX/SPY regime awareness but nothing sector-specific either. Live-checked a 10-ticker cluster: 6 were already pending signals from the same shock, 4 more would fire once the bar closed.
- **Traced this to the project's own Day 78 block-bootstrap docstring**, which already names "correlated tickers entering around the same time" as a known risk to the significance math — that mitigation never reached the entry gate or the raw trade count toward the 100-trade bar. Same underlying mechanism as the Day 93 clustering finding, mirror direction (selloff vs. rally).
- **Confirmed this is a deliberate design split, not an oversight**: verified with the user that the Sectors/Context tabs are still actively used for manual, discretionary decisions — the automated engine's "zero human filtering" is the intended design, not a gap to close mid-freeze.
- **Built and published `docs/claude/design/HOW_STOCK_PICKING_WORKS.html`** — a living, plain-language flowchart of the Simple Checklist (9 binary criteria) and Full Analysis (4-category, 7-rule cascade) paths, verified against current code, published as a persistent Claude Artifact. Grew across the session: a worked example (Regime = Uptrend), a "Test Scenarios" Q&A log (2 entries: the "buy the dip in a bad regime" question, and the scanner/breakout-alert question), and a full "Scanners" section covering all 6 TradingView scan presets + 3 curated watchlists with verified filter criteria.
- **New ROADMAP priority #15**: a scheduled/proactive breakout-alert watcher — `/breakout-watch` and the Scan tab's badge column already work on-demand against any personal list, but nothing runs on a schedule or alerts unprompted. User asked to mark it for later, explicitly not to build now.
- No app code changed, no version bump, no new Golden Rule.

### Day 99 Summary (Partial-Bar Ledger Contamination Fix — v4.54)
- **User asked what an Opus 5 review would be best spent on.** Chose the paper-trading ledger/exit-replay path — the highest-stakes, silently-accumulating code in the project, and one every prior review pass had come from the same session's own Claude, never a genuinely fresh look.
- **Found a real HIGH-severity bug**: the data provider returns a partially-formed bar for the current session while the market is open; neither `simulate_trade()` nor `simulate_mr_trade()` checked bar completeness before reading it. A mid-session `--force`/Force-Run-Now click could write an intraday price into the ledger as a closing price — permanent, since `close_position()` is one-way. The scheduled 17:30 ET job was always safe. Exhaustive re-replay (not sampled) found 19 of 25 closed MR trades affected, including one (MS) that should still have been open — a phantom closed trade.
- **Diagnosed and planned before any code changed**: `docs/claude/design/PARTIAL_BAR_LEDGER_CONTAMINATION_FIX_PLAN.md`, then implemented via Plan Mode across 4 phases: (1) incomplete-bar guard in `live_signals.py` (`_prepare_ohlcv`, explicit `zoneinfo` market timezone), verified via a 6-trade regression proof; (2) `repair_partial_bar_exits.py` (new) — backup, dry-run shown to the user, `--apply`, JSON audit trail — applied 20 corrections (GEV flipped win→loss, MS and a brand-new live-caught contamination (NVO) both reopened); (3) Force Run UI caption fixed (stale "16:30 CT" → "17:30 ET") plus a new mid-session warning; (4) momentum's live stats now net transaction costs like MR already did, two dead `.get()` fallbacks fixed.
- **A live-fire confirmation, unplanned**: mid-Phase-1, `backend.log` shows a real Force Run click during market hours (before the fix had been picked up by Flask's reloader) that closed NVO on a partial bar — an independent, real-time reproduction of the exact bug, correctly caught and corrected by the repair script.
- **Post-repair: all 27 remaining closed trades re-replay exactly (0.00pp) against complete history** — verified exhaustively. MR (broad) moved from a contaminated ~92%WR/~PF10.8 to a correct **84.0% WR, PF 8.06, 25 trades** — still flagged by the system's own sanity check as likely overfitting on a small, clustered sample (Day 93 finding unchanged).
- **Brainstormed FWD-testing speed-up ideas** (no re-tuning, per Golden Rule 18): the strongest was reusing `PAPER_TRADING_PREREGISTRATION.md` §7's already-frozen "Quick" holding period (5-day hold, never exercised by the live engine) as a third momentum track. Planned in Plan Mode (own 100-trade bar, `variant='A_frozen'` unchanged + `holding_period` as a genuinely independent axis) — **user stopped before approval; nothing built.**
- New **Golden Rule 39**: a live engine replaying historical bars must verify the last bar is actually closed.
- Version v4.53 → v4.54 (Backend v2.46 → v2.47, Frontend v4.48 → v4.49). No API contract shape change.

### Day 98 Summary (HUB-65 Curated-Universe Mean-Reversion Backtest + Forward-Test — v4.53)
- **User brought an external AI tool's "buy the 5% dip, sell on recovery" idea**, sourced from a sibling project's own curated 65-ticker watchlist ("HUB-65" — semis, uranium/nuclear, fintech, China-EV, thematic ETFs). Recognized this as exactly the project's own already-built, already-validated Connors RSI(2) Mean-Reversion engine, applied to a new universe — not a new strategy.
- **Planned twice** — once directly, then explicitly re-planned via a Plan agent with `model: "opus"` at the user's request to "see if new things surface," which found real corrections (the headline selection-bias caveat, a `variant`-naming precision fix, the real rate-limit risk location) folded into the final approved plan.
- **`HUB_UNIVERSE`** (64 tickers, VIX excluded) added to `mean_reversion.py`, mirrored byte-for-byte in `App.jsx`'s `HUB_WATCHLIST`.
- **Backtest** (`backend/backtest/backtest_hub_mr.py`, new — imports, doesn't duplicate, `backtest_survivorship_free.py`'s helpers): 1,940 trades, WR 57.78%, PF 1.2574, Sharpe 1.5278, block-bootstrap p=0.0311. **Explicitly documented everywhere as selection-biased and NOT comparable to the survivorship-free baseline (PF 1.16)** — a 2026 watchlist picked because the names already look strong.
- **Forward-test**: `get_mr_signals()` gained a `variant` param (backward-compatible); `daily_job.py` runs a second, shuffled HUB-65 pass tagged `variant='mr_hub65'`. New **Golden Rule 38**: the ledger's `variant` column now means two different things per `system` (momentum = gate experiment, mr = universe) — documented explicitly so a future read doesn't assume one meaning everywhere.
- **Reporting**: `/api/paper-trading/status` gained an additive `mrHub` block; Forward Test tab gained a teal-badged "Mean-Reversion (HUB-65)" card (deliberately distinct color from Path B's amber, since this is a different universe, not a different gate); Scan tab gained a new "HUB-65 Watchlist" preset.
- **Verified end-to-end**: throwaway-DB isolation/cooldown test, a real `daily_job.py --force` run (queued a genuine AFRM HUB-65 signal + 2 real first-ever Path B signals, JOYY/EBC), live `curl`, live in-browser checks on both the Forward Test and Scan tabs (63/64 HUB tickers live-scanned, DRAM correctly excluded as delisted), zero console errors. 3-pass review (Golden Rule 32) confirmed no other caller of `get_mr_signals()` breaks and the broad `mr` block stays correctly pinned to `variant='A_frozen'`.
- **Paper trading status:** Path A momentum 22 open/2 closed; Path B 0 open/0 closed, 2 pending (first real signals); broad MR 3 open/25 closed; **HUB-65 MR 0 open/0 closed, 1 pending (AFRM)** — new 4th track.
- Version v4.52 → v4.53 (Backend v2.45 → v2.46, Frontend v4.47 → v4.48, Backtest v4.19 → v4.20). Additive API change, see `API_CONTRACTS_DAY98.md`.

*(Day 97's summary rotated out — full detail preserved in `docs/claude/status/PROJECT_STATUS_DAY97_SHORT.md`. Day 96's is in `PROJECT_STATUS_DAY96_SHORT.md`. Day 94's is in `PROJECT_STATUS_DAY94_SHORT.md`.)*

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
   □ PERSONA.md (trading-judgment lens — Golden Rule 34)
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
STEP 4b: IF the persona lens caught/confirmed something → UPDATE stable/PERSONA.md's Feedback Log (+ "Last Updated" date)
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

**Forward-testing accumulation is the SOLE priority as of Day 92, unchanged Day 93-100** — user explicitly parked every other item below until 100 trades/system (raised from 50) are logged, now across FOUR tracks. Do not propose or start any of items 2+ unless the user raises it first — this is stricter than the Day 87 feature freeze it supersedes. (The Day 93 Sectors/Context tab work, Day 94's Sector Rotation fix + README audit, Day 95's launchd schedule/timezone fix, Day 96's provider-reliability overhaul + PERSONA.md, Day 98's HUB-65 track, Day 99's partial-bar ledger contamination fix, and Day 100's monitoring/documentation session were explicitly scoped as independent of this freeze — pure display/UI/docs/ops/infra, a genuinely new separately-tracked experiment, or a data-integrity fix to existing infrastructure, no frozen-threshold contact — not new exceptions to the pattern. Path B and HUB-65 are both genuinely new experiments, not freeze exceptions, since neither touches an existing track's count. Day 97's IBKR research/plan is explicitly parked by the user's own choice — do not start Phase 1 unless raised again. Day 99's "Quick" momentum holding-period idea was scoped/planned but the user stopped before approval — nothing built, needs re-planning from scratch if raised again. Day 100's scheduled breakout-alert watcher idea (ROADMAP priority #15) is explicitly idea-only — needs its own design session before any build, not started.)

1. **Let paper trading accumulate** — SOLE FOCUS, now across 4 tracks, on a *corrected* ledger (Day 99 partial-bar fix — see Golden Rule 39). As of Day 100: **Path A** Momentum 28 open/2 closed (50% WR, PF 1.691 — still a tiny sample); **Path B** Momentum 6 open/0 closed; **MR** (broad) 2 open/**26 closed (84.62% WR, PF 8.26** — still likely overfitting on a small clustered sample per the system's own sanity check, Day 93 finding unchanged, and now known to have zero sector-correlation awareness, Day 100 finding, KNOWN_ISSUES_DAY100.md); **MR (HUB-65)** 2 open/0 closed. Confirmation bar is **100 trades/system** for all four (`PAPER_TRADING_PREREGISTRATION.md`). Momentum Path A's pace is genuinely slow (pipeline-bound, not signal-starved — most of its 28 open positions are still early in their 15-day hold); Path B and HUB-65 are both still too young to say anything about pace. The job's `launchd` schedule was corrected Day 95 (now 17:30 ET). `/sta-start` warns automatically if the launchd job goes stale (>3 days). If a Force Run "looks like nothing happened," don't assume it's a quiet day — re-run in the foreground and read stdout before trusting the aggregate UI. Check progress via the Forward Test tab's status panel or `venv/bin/python paper_trading/daily_job.py --report`.
2. *(parked, explicitly by user's own request)* **IBKR real paper-trading execution** — full 4-phase plan at `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md` (ROADMAP Priority #13). Do not start Phase 1 unless the user explicitly raises it — they want to do additional research/review first (specifically: confirming the CIRO Rule 3200 paper-account question directly with IBKR support, per the plan's own "Open items" section).
3. *(parked)* **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
4. *(parked)* **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
5. *(parked)* **N3 gap-fill detection** — needs its own design session first (Day 87 finding: no spec exists yet, only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`).
6. *(parked)* **Value Tab Phase 2** — needs its own batch-prefetch infrastructure design session first (Day 87 finding: `VALUE_TAB_SPEC.md` explicitly requires a nightly watchlist-prefetch job for AlphaVantage's ~8-tickets/day budget; on-demand fetching would contradict the documented design).
7. *(parked)* **Volume confirmation missing from the decision engine** (Day 92 finding) — neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check volume *confirmation* of a price move (the checklist's "Volume" criterion is a liquidity gate, not a confirmation signal). Needs a re-backtest before shipping, since it touches frozen verdict logic. Companion item: `mean_reversion.py`'s ADX docstring doesn't match its code — likely just a doc fix.
8. *(parked)* **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
9. *(parked)* **Price Structure Phase 3** (visual chart via lightweight-charts) / Canadian Analyze page — queued.
10. *(parked)* **(Optional, low priority) Scan tab batch breakout badges** — distinguish `NOT_READY` from a failed fetch (currently both render "—"); same bug class as the Day 85 single-ticker fix, not yet requested at this location.
11. *(parked)* **(Optional, low priority) Master Framework Watchlist's Name/Market Cap columns** — still show N/A (Volume/Change % fixed Day 86, free); Name/Market Cap would need a separate fundamentals call per ticker, deferred by explicit user choice.
12. *(parked)* **Session 28 audit's remaining lower-priority findings** (Day 91) — Value tab badge attribution, Validate/Data Sources status-label honesty, Sectors `.toFixed(3)` false precision (the CTA-gating sub-item was fixed Day 93 via the Sectors tab redesign), Forward Testing's fee-accounting/silent-failure items, plus the audit's general polish list. See ROADMAP.md priority #10 and `KNOWN_ISSUES_DAY91.md` for full detail.
12. *(parked, user's own call)* The Day 82 Fable audit's 5th recommendation bucket — consolidating the Golden Rules/doc-rotation process itself (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`, Section F "REMOVE/DECLUTTER" item 4) — was deliberately not applied; it's a bigger, more opinionated change than the hygiene fixes and should only happen if the user explicitly wants it.

---

## FILE STRUCTURE REFERENCE

```
/docs/claude/
├── CLAUDE_CONTEXT.md              <- THIS FILE (single reference)
├── stable/                        <- Rarely change
│   ├── GOLDEN_RULES.md           <- Core rules + lessons learned
│   ├── PERSONA.md                <- Trading-judgment lens (30yr veteran persona) + Feedback Log
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
| 90 | Monitoring-only session, no code changes. Paper-trading check-in (Momentum 2 open/0 closed; MR 9 open/4 closed, 75% WR, PF 2.19). Investigated "Force Run Now" repeat-click behavior at user's request — confirmed no duplicate trades possible (dedup + one-way close), same-day re-clicks overwrite the run summary rather than accumulating (job_runs UNIQUE + INSERT OR REPLACE), and the panel is aggregate-only by design (no ticker-level display). No bug found, nothing built — user parked further work and closed. Version unchanged (v4.47). |
| 91 | Found an untracked, unactioned hub-side audit (`HANDOFF_sta_audit_session28.md`) at user's request. Fixed its 4 top-priority findings: Scan tab "Minervini" mislabel, Sectors tab false "100=parity"/data-source claims, Context tab CPI (root-caused to a real `_yoy()` date-alignment bug, not caching as the audit guessed — Golden Rule 26) + PMI proxy relabel, paper-trading exit-rule integrity (replay now anchors to stored entry values — Golden Rule 27, caught a live drift instance during verification). Verified live end-to-end (force-ran the real daily job). Remaining lower-priority findings tracked as ROADMAP.md priority #10. v4.47 → v4.48 (BE v2.43 → v2.44, FE v4.42 → v4.43). |
| 92 | First-principles review of the decision engine found two real, low-severity gaps (volume confirmation missing from the verdict/checklist; MR's ADX docstring vs. code mismatch) — logged as ROADMAP.md priority #11, deferred. Investigating a "Force Run did nothing" report found and fixed a real bug: `signal_date` stamped from the wall clock instead of the OHLCV bar it came from could permanently strand a signal (Golden Rule 28) — 8 zombied momentum signals repaired, momentum went 3→10 open. Added per-position ticker/entry/exit detail to the Forward Test tab (`/api/paper-trading/status` extended, additive). **User raised the paper-trading confirmation bar from 50 to 100 trades/system and named forward-testing accumulation the sole priority** — all other roadmap items explicitly parked. v4.48 → v4.49 (BE v2.44 → v2.45, FE v4.43 → v4.44). |
| 93 | Sectors/Context tab audit, explicitly independent of the freeze (pure display/UI logic). 3 real bugs + a full beginner-focused redesign on the Sectors tab; 2 real bugs on the Context tab (a Day 91 regression in the econ composite, a Seasonal Regime text/badge contradiction); new Sectors↔Context `macro_alignment` connection + Market-Phase↔Macro-Regime reconciliation. Self-audit against GOLDEN_RULES.md found a real DRY violation, fixed (Golden Rules 30-31 added). Corrected a real Backend version-drift (code said 2.43, docs claimed 2.45). v4.49 → v4.50 (BE v2.43 → v2.44, FE v4.44 → v4.45). |
| 94 | Fixed a real Sector Rotation silent-failure bug (visible error banner + Retry); a mandated 2nd/3rd review pass caught a cascading-failure regression and a stale-error-masking-fresh-data bug before shipping (new Golden Rule 32: 3 review passes per fix, always). Ran the project's first full README.md Coherence Audit (5 parallel passes) — fixed ~50 real issues (3 fictional API endpoints, ~10 undocumented real ones incl. the entire paper-trading/breakout engines, a self-contradicting version/date header, Stooq-vs-Tradier corrected throughout). New `DEVELOPER_ONBOARDING.md` for an external collaborator. v4.50 → v4.51 (BE v2.44 unchanged, FE v4.45 → v4.46). |
| 95 | Fixed a real paper-trading `launchd` schedule bug: the plist's own comment assumed the machine ran on Central Time, but `/etc/localtime` showed it's actually Eastern (America/Toronto) — the job had been firing at 4:30pm ET instead of the intended 4:30pm CT, cutting its 90-min post-close data-settling buffer to 30 min. Shifted schedule to 17:30 ET, corrected the comment, reloaded via launchctl. New Golden Rule 33. No version bump (config/ops-only, no app code touched). |
| 96 | Built `PERSONA.md` (Golden Rule 34). Fixed a systemic circuit-breaker bug across all 6 data providers — ticker-specific data gaps were miscounted as provider-health failures (Golden Rule 36) — plus centralized fragile `.env` loading. Discovered the live momentum R:R gate never matched the actual backtested Config C entry logic (Golden Rule 35); fixed by building **Path B**, a parallel forward-test experiment on the real S&R-based gate, own ledger variant, own 100-trade bar, zero effect on Path A — surfaced live in the Forward Test tab. v4.51 → v4.52 (BE v2.44 → v2.45, FE v4.46 → v4.47). Additive API change, see `API_CONTRACTS_DAY96.md`. |
| 97 | Research/planning-only session: investigated real IBKR paper-trading execution. A cited regulatory research file didn't exist, so researched CIRO Dealer Member Rule 3200 directly against CIRO's own guidance rather than a secondhand summary (Golden Rule 37) — governs real orders to a real marketplace, doesn't appear to restrict a pure paper account. Produced a full 4-phase implementation plan via Plan mode + a Plan-agent review; user explicitly parked implementation pending further research. Persisted as `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md`, tagged ROADMAP Priority #13. No code changed, no version bump. |
| 98 | Recognized the user's "buy the 5% dip" idea (sourced from a sibling project's curated 65-ticker watchlist, "HUB-65") as the project's own existing, unchanged MR engine applied to a new universe. Re-planned via an Opus Plan agent per the user's explicit request, which surfaced real corrections. Built: `HUB_UNIVERSE` (64 tickers), a new backtest script (1,940 trades, PF 1.2574, Sharpe 1.5278 — explicitly caveated as selection-biased, not comparable to the survivorship-free PF 1.16 baseline), a real forward-test track (`variant='mr_hub65'`, new Golden Rule 38 on the ledger's now dual-meaning `variant` column), a new `mrHub` API block, a teal-badged Forward Test tab card, and a visible Scan tab HUB-65 watchlist. Verified end-to-end (isolation test, real daily-job run, live browser checks, zero console errors). v4.52 → v4.53 (BE v2.45 → v2.46, FE v4.47 → v4.48, Backtest v4.19 → v4.20). Additive API change, see `API_CONTRACTS_DAY98.md`. |
| 99 | A targeted Opus 5 review of the paper-trading ledger/exit-replay path (chosen because nothing looked broken, not in response to a symptom) found a real HIGH-severity bug: mid-session manual runs could write an intraday, not-yet-final price into the ledger as a closing price, permanently (`close_position()` is one-way). Exhaustive re-replay found 19 of 25 closed MR trades affected. Fixed in 4 Plan-Mode-approved phases: incomplete-bar guard (explicit `zoneinfo` market timezone), a dry-run-then-`--apply` repair script (20 corrections, one — MS — reopened, one caught live mid-implementation via a real Force Run click — NVO), Force Run UI warning, two minor cleanups (gross/net stats, dead fallbacks). All 27 remaining closed trades now re-replay exactly; MR corrected from a contaminated ~92%WR/~PF10.8 to 84.0%WR/PF8.06. New Golden Rule 39. A "Quick" 5-day-hold momentum track was scoped/planned as a legitimate speed-up (reusing an already-frozen, unused holding period) but the user stopped before approval — not built. v4.53 → v4.54 (BE v2.46 → v2.47, FE v4.48 → v4.49). No API contract shape change. |
| 100 | Monitoring/documentation session, no app code changed. Verified the Day 99 fix under real live use (a mid-session Force Run correctly deferred to the prior day's close). Found and code-verified a real structural gap prompted by a live semis-sector selloff: neither automated track has any sector-correlation awareness in its entry gate — traced to the project's own Day 78 block-bootstrap docstring, which already partially named this exact risk to the significance math but never reached the entry gate or trade count. Confirmed the Sectors/Context tabs are still the deliberate, actively-used home for that judgment (manual workflow), not a gap in the automated engine. Logged as a Known Issue, not fixed (would be a re-tune of a frozen gate mid-freeze). Built and published a new living reference doc, `docs/claude/design/HOW_STOCK_PICKING_WORKS.html` (Simple Checklist + Full Analysis verdict logic, a growing Test Scenarios Q&A log, a Scanners section), meant to keep accumulating across future sessions. New ROADMAP priority #15 (scheduled breakout-alert watcher) — idea only, not started. v4.54 unchanged, no version bump. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
