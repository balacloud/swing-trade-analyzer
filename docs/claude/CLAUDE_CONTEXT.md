# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 92 — end of day (July 20, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 92 |
| Version | v4.49 (Backend v2.45, Frontend v4.44, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY92_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY92.md |
| Latest API | API_CONTRACTS_DAY92.md — `/api/paper-trading/status` gained per-position `positions` detail (additive, no removals) |
| Focus | **Forward-testing accumulation is now the SOLE priority — everything else is parked until 100 trades/system are logged.** Session found and fixed a real paper-trading bug (`signal_date` stamped from the wall clock instead of the OHLCV bar it came from — could permanently strand a signal if the job ran off a trading day; 8 of momentum's 11 pending signals were affected and repaired, jumping momentum 3→10 open — new Golden Rule 28). Added per-ticker entry/exit detail to the Forward Test tab. A first-principles review of the decision engine (user-initiated, not part of the audit) found two real but low-severity gaps (volume confirmation absent from the verdict/checklist; MR's ADX docstring vs. code mismatch), logged as ROADMAP.md priority #11 and explicitly deferred. **User then raised the paper-trading confirmation bar from 50 to 100 trades per system.** |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 92 Summary (Zombie-Signal Bug Fixed + Per-Ticker UI + Confirmation Bar Raised to 100 — v4.49)
- **First-principles review of the decision engine** (user-initiated, separate from any audit): walked `determineVerdict()`, the Minervini Trend Template, and `mean_reversion.py` against canonical swing-trading principles. Core logic held up well (real 8-criteria Trend Template, RS as a hard gate, regime as a gate not a vote, equal-weighting, mechanical ATR exits). Found two real but low-severity gaps, logged as new ROADMAP.md priority #11 and explicitly deferred: (1) neither the Full Analysis verdict nor the Simple Checklist's 9 criteria check volume *confirmation* of a price move — the checklist's "Volume" criterion is a liquidity gate, not a confirmation signal, confirmed directly against a user-provided screenshot (CCO passing "Volume: PASS" on liquidity alone); (2) `mean_reversion.py`'s docstring claims an ADX/range-bound gate that the actual `detect_mr_signal()` code never checks.
- **User force-ran the paper-trading job and reported "looks like nothing happened."** Investigation found two causes: a live TwelveData rate-limit cascade (self-healed within the session, confirming Day 89's Golden Rule 25 finding still holds — verified Tradier/yfinance breakers recover on the next probe), and **a real, previously-undiscovered bug**: `live_signals.py` stamped every new signal's `signal_date` from `datetime.now()` instead of the OHLCV bar `signal_price` actually came from. A weekend/off-hours Force Run stamps a date that can never match a trading day, permanently stranding that signal in `pending_entry` with only a silent stdout print — **8 of momentum's 11 pending signals were affected.** Fixed by deriving `signal_date` from the same bar as `signal_price`; repaired the 8 stuck rows by matching stored price back to the real OHLCV date. Re-ran and confirmed 7/8 activated immediately — **momentum jumped from 3 open to 10 open in one run.** New **Golden Rule 28**.
- **Added per-position ticker/entry/exit detail to the Forward Test tab**: user asked to see "what tickers, what price entered and exit" without querying the DB directly. Extended `/api/paper-trading/status` with a `positions` field (data was already computed server-side, just discarded to a count) and added an expandable table to `AutomatedPaperTradingPanel.jsx`. Verified live in-browser via claude-in-chrome — correct rendering, zero console errors.
- **User then explicitly raised the paper-trading confirmation bar from 50 to 100 trades per system** and named forward-testing accumulation the **sole** priority — logged in `PAPER_TRADING_PREREGISTRATION.md`'s Change Log (not goalpost-moving in the Golden Rule 18 sense, since it's strictly more conservative and made with 0 momentum / 5 MR closed trades on the books). All other roadmap/backlog items explicitly parked until it clears.
- Version v4.48 → v4.49 (Backend v2.44 → v2.45, Frontend v4.43 → v4.44). API additive-only change, see `API_CONTRACTS_DAY92.md`.

### Day 91 Summary (Session 28 Audit Triage — 4 Bugs Fixed — v4.48)
- **User asked at session start whether a handoff document existed** — found `HANDOFF_sta_audit_session28.md`, untracked at the repo root, a hub-side Fable audit (Jul 17-19) never actioned or logged in the normal doc rotation. Part 1 (doc-vs-code coherence) had no urgent findings; Part 2 (tab-by-tab methodology audit — 5 Fable agents + an Opus persona pass + an external ChatGPT review) found 0 CRITICAL / 8 HIGH-equivalent findings.
- **User scoped this session to the 4 top-priority findings only.** Fixed:
  1. Scan tab's "Minervini SEPA/Stage 2 uptrend" mislabel (only checked 2 of 8 real Trend Template criteria) → renamed "Large-Cap Momentum Filter" (`backend.py`, `App.jsx`, `README.md`).
  2. Sectors tab's false "100 = market parity" claim + wrong "Data from TwelveData" label (real source: yfinance) → both corrected (`SectorRotationTab.jsx`).
  3. Context tab's CPI card (showing 3.7%/2.8% vs. the real 3.5%/2.6% BLS release) — **root-caused as a genuine bug, not caching as the audit guessed**: a fresh non-cached fetch reproduced the identical wrong number, and tracing raw FRED data found a withheld observation (`2025-10-01: "."`) silently shifted `_yoy()`'s fixed-list-index lookback onto the wrong calendar month. Fixed via calendar-date matching instead of list position (`econ_engine.py`); verified live, now shows the correct 3.5%/2.6%. New **Golden Rule 26** (verify a diagnosed root cause directly before trusting a suggested fix).
  4. Paper-trading's daily replay (`daily_job.py`) recomputed stop/target fresh from current code every day instead of reading back what the ledger already stored at entry. Fixed by wiring in the existing (unused) override params. **Verification caught a live instance of the exact risk being fixed**: KRYS's freshly-recomputed stop had already drifted from its entry-stored value due to an upstream provider data revision. New **Golden Rule 27**.
- **Verified the paper-trading fix end-to-end**: backed up the ledger, force-ran the real daily job — 11 open positions replayed correctly, none incorrectly closed. This also served as the day's paper-trading catch-up run (last scheduled run was Jul 17): Momentum 3 open/0 closed, MR 8 open/5 closed after the run.
- No API contract shape changes (only string/value corrections). Remaining lower-priority audit findings tracked as new ROADMAP.md priority #10. Version v4.47 → v4.48 (Backend v2.43 → v2.44, Frontend v4.42 → v4.43).

### Day 90 Summary (Monitoring + Force Run Investigation — No Code Changes — v4.47 unchanged)
- **Paper trading check-in** (the session's stated focus, given the freeze): `daily_job.py --report` showed Momentum 2 open/0 closed (no stats yet); MR 9 open/4 closed, 75% win rate, PF 2.19, expectancy +1.49%/trade — early, directional only.
- **User asked what happens on repeated "Force Run Now" clicks**, and why the panel shows only aggregate counts, not ticker names. Traced `daily_job.py`/`ledger.py`/`live_signals.py`/`AutomatedPaperTradingPanel.jsx` before answering, rather than guessing.
- **Findings (no bug — confirmed working as designed):** the trigger route always passes `force=True` (deliberately bypassing the same-day idempotent guard meant only for the scheduled run); `has_active_or_cooldown()` prevents any duplicate trade on repeat clicks; `job_runs.run_date` is UNIQUE with `INSERT OR REPLACE`, so a same-day re-click **overwrites** that day's summary rather than accumulating it — the "Run complete" banner only ever reflects the latest click's delta. The real (non-correctness) cost of rapid repeat-clicking is live provider load — each click re-scans ~150 candidates per side plus every open position against the same rate-limited chain Golden Rule 25 already found tips over. The panel has no ticker-level display anywhere; seeing actual tickers needs a direct SQLite query against `paper_positions`.
- Items 2-7 from Day 89's priority list (fundamentals mitigation, SimFin key rotation, N3, Value Tab Phase 2, `/ibkr-scan`, Price Structure Phase 3, Canadian page) explicitly parked in ROADMAP.md by user request, not re-litigated this session.
- No version bump, no API changes, no new Golden Rule (existing design confirmed correct, not a lesson from a mistake), no roadmap changes.

*(Day 89's summary rotated out — full detail preserved in `docs/claude/status/PROJECT_STATUS_DAY89_SHORT.md`. Day 88's is in `PROJECT_STATUS_DAY88_SHORT.md`. Day 87's is in `PROJECT_STATUS_DAY87_SHORT.md`.)*

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

**Forward-testing accumulation is the SOLE priority as of Day 92** — user explicitly parked every other item below until 100 trades/system (raised from 50) are logged. Do not propose or start any of items 2+ unless the user raises it first — this is stricter than the Day 87 feature freeze it supersedes.

1. **Let paper trading accumulate** — SOLE FOCUS. As of Day 92's close: Momentum 10 open/0 closed (jumped from 3 after fixing a real zombie-signal bug, Golden Rule 28); MR 8 open/5 closed. Confirmation bar is now **100 trades/system** (`PAPER_TRADING_PREREGISTRATION.md`). Both systems are far from the bar — no re-estimate of time-to-bar yet, the zombie-signal fix likely changes momentum's real accumulation rate but there isn't enough post-fix data to re-derive it. `/sta-start` warns automatically if the launchd job goes stale (>3 days). If a Force Run "looks like nothing happened," don't assume it's a quiet day — re-run in the foreground and read stdout before trusting the aggregate UI (this is exactly how Day 92's bug was found). Check progress via the Forward Test tab's status panel (now with per-ticker entry/exit detail, Day 92) or `venv/bin/python paper_trading/daily_job.py --report`.
2. *(parked)* **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
3. *(parked)* **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
4. *(parked)* **N3 gap-fill detection** — needs its own design session first (Day 87 finding: no spec exists yet, only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`).
5. *(parked)* **Value Tab Phase 2** — needs its own batch-prefetch infrastructure design session first (Day 87 finding: `VALUE_TAB_SPEC.md` explicitly requires a nightly watchlist-prefetch job for AlphaVantage's ~8-tickets/day budget; on-demand fetching would contradict the documented design).
6. *(parked)* **Volume confirmation missing from the decision engine** (Day 92 finding) — neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check volume *confirmation* of a price move (the checklist's "Volume" criterion is a liquidity gate, not a confirmation signal). Needs a re-backtest before shipping, since it touches frozen verdict logic. Companion item: `mean_reversion.py`'s ADX docstring doesn't match its code — likely just a doc fix.
7. *(parked)* **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
8. *(parked)* **Price Structure Phase 3** (visual chart via lightweight-charts) / Canadian Analyze page — queued.
9. *(parked)* **(Optional, low priority) Scan tab batch breakout badges** — distinguish `NOT_READY` from a failed fetch (currently both render "—"); same bug class as the Day 85 single-ticker fix, not yet requested at this location.
10. *(parked)* **(Optional, low priority) Master Framework Watchlist's Name/Market Cap columns** — still show N/A (Volume/Change % fixed Day 86, free); Name/Market Cap would need a separate fundamentals call per ticker, deferred by explicit user choice.
11. *(parked)* **Session 28 audit's remaining lower-priority findings** (Day 91) — Value tab badge attribution, Validate/Data Sources status-label honesty, Sectors CTA gating/precision polish, Forward Testing's fee-accounting/silent-failure items, plus the audit's general polish list. See ROADMAP.md priority #10 and `KNOWN_ISSUES_DAY91.md` for full detail.
12. *(parked, user's own call)* The Day 82 Fable audit's 5th recommendation bucket — consolidating the Golden Rules/doc-rotation process itself (`docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`, Section F "REMOVE/DECLUTTER" item 4) — was deliberately not applied; it's a bigger, more opinionated change than the hygiene fixes and should only happen if the user explicitly wants it.

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
| 90 | Monitoring-only session, no code changes. Paper-trading check-in (Momentum 2 open/0 closed; MR 9 open/4 closed, 75% WR, PF 2.19). Investigated "Force Run Now" repeat-click behavior at user's request — confirmed no duplicate trades possible (dedup + one-way close), same-day re-clicks overwrite the run summary rather than accumulating (job_runs UNIQUE + INSERT OR REPLACE), and the panel is aggregate-only by design (no ticker-level display). No bug found, nothing built — user parked further work and closed. Version unchanged (v4.47). |
| 91 | Found an untracked, unactioned hub-side audit (`HANDOFF_sta_audit_session28.md`) at user's request. Fixed its 4 top-priority findings: Scan tab "Minervini" mislabel, Sectors tab false "100=parity"/data-source claims, Context tab CPI (root-caused to a real `_yoy()` date-alignment bug, not caching as the audit guessed — Golden Rule 26) + PMI proxy relabel, paper-trading exit-rule integrity (replay now anchors to stored entry values — Golden Rule 27, caught a live drift instance during verification). Verified live end-to-end (force-ran the real daily job). Remaining lower-priority findings tracked as ROADMAP.md priority #10. v4.47 → v4.48 (BE v2.43 → v2.44, FE v4.42 → v4.43). |
| 92 | First-principles review of the decision engine found two real, low-severity gaps (volume confirmation missing from the verdict/checklist; MR's ADX docstring vs. code mismatch) — logged as ROADMAP.md priority #11, deferred. Investigating a "Force Run did nothing" report found and fixed a real bug: `signal_date` stamped from the wall clock instead of the OHLCV bar it came from could permanently strand a signal (Golden Rule 28) — 8 zombied momentum signals repaired, momentum went 3→10 open. Added per-position ticker/entry/exit detail to the Forward Test tab (`/api/paper-trading/status` extended, additive). **User raised the paper-trading confirmation bar from 50 to 100 trades/system and named forward-testing accumulation the sole priority** — all other roadmap items explicitly parked. v4.48 → v4.49 (BE v2.44 → v2.45, FE v4.43 → v4.44). |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
