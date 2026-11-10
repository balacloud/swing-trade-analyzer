# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 122 — 2026-11-10

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 122 |
| Version | v4.62 (Backend v2.51, Frontend v4.59) — unchanged; Day 121 added 4 display-only frontend helpers that nothing imports yet |
| Latest Status | PROJECT_STATUS_DAY122_SHORT.md (consolidated Days 121–122) |
| Latest Issues | KNOWN_ISSUES_DAY122.md |
| Latest API | API_CONTRACTS_DAY118.md (unchanged Days 119-122) |
| Focus | **Analyze Page Redesign in progress, one signed-off step at a time.** Steps 1–2 (Phase 0 copy fixes + baseline, Phase 1 helpers) done Day 121. Day 122 signed off the Technical Read card design (mockup v0.8): 4 key checks + full-score line, engine keeps all 8 checks (Golden Rule 59). Next: Step 3 (Phase 2, Trade Setup card) — **only on the user's go-ahead**. |
---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Days 121–122 Summary (Analyze Page Redesign Steps 1–2 built, Technical Read card designed — no version bump, new Golden Rule 59)
- **Day 121 (Nov 5–6), Phase 0 + Phase 1:** decision doc §6/§9 copy corrected (two blocks that
  described bugs fixed Day 112/118); baseline: parity 86,400/86,400, both UI scripts time out
  (pre-existing). 4 display-only helpers added, not imported: `deriveTechnicalRead`,
  `screenFundamentalRedFlags`, `describeRegimeRead`, `getVixPositionMultiplier`. User approved.
- **Day 122 (Nov 6–10), Technical Read card signed off (mockup v0.8):** 4 key trend checks
  (200-day above + rising, above 50-day, within 25% of 52-week high — cutoff kept after canon +
  Reddit check) plus a full-score line; "taking a breather" / "momentum n/a" wording; timing
  ("Is now a good moment to get in?", vs the 21-day EMA) and volume ("Are buyers behind the
  move?") as Info-only answers; "support" reserved for the Trade Setup card.
- **Checks 5–8 stay in the engine.** Claude first suggested a frontend-only removal; the user's
  architect question reversed it (the 7-of-8 rule lives in 4 places). New **Golden Rule 59**,
  PERSONA "Architect's Lens", and a PostToolUse **verdict parity hook**
  (`.claude/hooks/verdict_parity.sh`).
- **Volume data check:** TwelveData = yfinance to the share; IBKR is 46–65% of that (filtered
  trades), closes identical. STA's volume is the full count; never mix IBKR volume in.

### Day 120 Summary (Leveraged ETF Board + Beginner Trading Starter Playbook, standalone Artifacts — no version bump, new Golden Rule 58)
- **Leveraged ETF Board** (`LEVERAGED_ETF_BOARD.html`, https://claude.ai/artifact/HdErxTqUhq8KYs6McSU5V7):
  live IBKR page (read-only `mcp`, `get_price_history` only) running the user's adopted Reddit
  and canon rules on the 8 funds in their IBKR watchlist "AI_Leveraged". The JS formulas were
  checked bit-identical to STA's Python. v1 picked the US SOXL/GDXU by symbol search, but the user
  holds the Canadian BetaPro funds, which gave **Golden Rule 58** (take conids from the user's
  watchlist). The user set the scope: a count-only display (they own the rule count); Claude
  watches splits and explains stops and sizing, and doesn't nag about fundamentals, holding
  period or backtests. Logged in PERSONA.
- **Beginner Trading Starter Playbook** (`STARTER_PLAYBOOK.html`, https://claude.ai/artifact/CfnNDEEs8jS112MuTU4HPp):
  an 8-tab, light-theme page for the user's beginner friend, shared anyone-with-the-link. Tabs:
  trader type, US–Canada macro table plus market-reaction guide, Reddit rules, 100-year canon,
  top-10 coding rules, General, live data and gamification, and building it with Claude Code
  (FastAPI, React, Lightweight Charts). Data provenance is disclosed on the page. The tab bar now
  wraps, because the 8th tab had been hidden off-screen.
- **Final MR number corrected:** the live ledger shows 241 closed, 70.54% win rate, **PF 2.00**.
  The "PF ~2.5" in older docs is stale. STA Status Board republished.
- No STA application code touched. Version unchanged (v4.62).

### Day 119 Summary (Analyze Page Redesign implementation plan re-verified and corrected — no version bump)
- User pushed back on the shape of the post-Day-118 backlog (mostly Medium/Low, informational,
  no live gates) — agreed continuing to clear it item-by-item has diminishing returns. Recommended
  the Analyze Page Redesign (Priority #17) as the one bounded, real piece of work left — fully
  designed already, would change what's felt every time the app opens, unlike isolated point-fixes.
- **Opus-planned re-verification of the Day 109 decision doc's own §7 (implementation plan) and §8
  (freeze-safety audit)** against six sessions of intervening code changes (Golden Rule 55 —
  touches shipped live displays, multiple downstream consumers, changes methodology). Verdict: the
  17 locked decisions and §7's phase structure hold; §8's freeze-safety audit is obsolete in its
  justification (the freeze it protected is gone, Day 113) but its "don't touch the backend"
  conclusions survive, now on parity/backtest-comparability grounds (re-ran Golden Rule 54's
  caller-graph check fresh — `compute_sr_levels()`/`categorical_engine.py` still have live callers:
  the backtest harness, the 86,400-combo parity grid, several diagnostic scripts).
- **9 corrections found**, most importantly: two blocks of the plan's prescribed on-card copy (§6)
  described bugs that no longer exist — the pivot S&R extreme-vs-nearest selection (fixed Day 112,
  Golden Rule 53) and Pattern Detection's flat-multiple target (replaced Day 112/118). Shipping
  either as originally written would have put a fabricated open bug and formula in front of the
  user. Also: a helper misnamed `describeRegimeGate()` renamed to `describeRegimeRead()` (Regime
  is Info, not a gate, since Day 110); the negative-EPS red-flag question answered and declined
  (`epsGrowth` is a YoY rate, misleading as a flag); both UI verification scripts confirmed
  silently non-functional since Day 75 (block on text that only renders in the non-default view).
- New plan: `docs/claude/design/ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md` — supersedes
  only §7/§8's *execution* plan, not the 17 locked decisions. Go/no-go: **GO**. First phase: Phase
  0 (copy correction + parity-test baseline) then Phase 1 (additive utilities, zero visible
  change). **No application code touched.** `ROADMAP.md`/`README.md` updated to match (Priority
  #17 no longer gated behind anything, since the freeze it was scoped around is gone).

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

**No freeze, no live gates.** The paper-trading program (and the Day-92 freeze that protected
it) is discontinued as of Day 113 — STA is a pure analysis/recommendation tool now, the user
places and manages every trade themselves. Every item below is available to work whenever —
pick deliberately based on what the user actually wants next, not backlog order.

**The one bounded, real piece of work — has a corrected, ready-to-execute plan (Day 119):**
0. **Analyze Page Redesign (Priority #17)** — `docs/claude/design/ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`,
   progress on the Status Board's "Redesign progress" section. Steps 1–2 done Day 121; Technical
   Read card design signed off Day 122 (decisions doc §10, mockup v0.8). **Next: Step 3 (Phase 2,
   Trade Setup card) — wait for the user's go-ahead; the user signs off on each piece.** Every
   step keeps the parity test passing, touches no backend code, adds no Simple Checklist
   criterion (Golden Rule 57). Any rule/threshold change: run the Architect's Lens first
   (Golden Rule 59).

**High severity, no plan written yet:**
1. **Per-ticker provenance can't distinguish "never checked" from "just failed."** Day 108
   finding, the oldest unaddressed item from that audit. Needs its own new failure-tracking
   mechanism and its own session — plan with Opus first per Golden Rule 55(c) (more than one
   downstream consumer likely).

**Medium severity, no plan written for any of these:**
2. VIX position-sizing never wired into the paper-trading engine (Day 108) — check first
   whether this is now moot, since that engine is discontinued; don't spend planning effort
   before confirming something still reads this path.
3. `ContextTab.jsx` bypasses the shared `api.js` fetch layer (Day 108) — needs `api.js`'s dead
   Context functions fixed to throw-not-swallow first.
4. Value tab's "Buffett" ROE attribution wording — decision already made (drop investor-name
   labels, group under 3 functional headings), just not implemented (Day 111).
5. Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp
   ceiling (Day 108) — needs a product decision.
6. Backtest-Live Fundamentals data-source mismatch, ~40% disagreement measured (Day 78/79) —
   mitigation choice still a pending user decision (align live-to-SimFin or backtest-to-TTM).
7. Two batch endpoints (Sectors Rotation, Market Phase breadth) bypass circuit-breaker
   protection, no Tradier fallback (Day 111) — `/api/mr/scan`'s sibling bypass was fixed Day 111.

**Zero-risk cleanup batch, any order, no planning needed:**
8. 5 dead `App.jsx` functions (confirmed via build warnings): `cacheResult`,
   `getViabilityStyle`, `generateActionableRecommendation`, `generateScoreExplanation`,
   `getSubScoreInfo`.
9. Data Sources tab's field-source doc still says "Defeat Beta API" (stale, Day 111).
10. Value Tab investor-name relabeling — same fix as item 4, could ship together.

**Bigger open questions, no urgency:**
11. ~~Does the Analyze Page Redesign become a real implementation project, or stay a documented
    reference?~~ **Answered Day 119: it has a corrected, ready-to-execute plan** (see priority 0
    above) — the remaining question is purely "when," not "if/how." Includes one still-live bug
    that Phase 2 of the plan fixes: the Momentum entry panel's position-size label has been
    hardcoded to "half" since Day 39.
12. Decide how the Analyze-page R:R should be *framed* now that `_pivot_sr` returns real
    nearest levels (it will honestly show sub-1.2:1 where real resistance is close, not a
    fabricated 3:1) — copy/framing, not logic, since R:R is already informational.

**Still genuinely parked, needs a design session before any build:**
13. `/ibkr-scan` skill (research done Day 77, verify 52W High Proximity in IBKR first).
14. Price Structure Phase 3 (visual chart) / N3 gap-fill detection — no spec exists yet for
    either.
15. Value Tab Phase 2 — needs its own batch-prefetch infra design (AlphaVantage budget
    constraint), per `VALUE_TAB_SPEC.md`.
16. SRPS screener's R:R stays structurally disconnected from real resistance (fixed
    `entry + 2.5x risk`) — not urgent, it's explicitly informational with its own disclaimer.
17. Simple Checklist's "PASS" badge reads as good news even at low pass counts (e.g. 2/9) —
    a copy fix is already specified in the redesign's §7.5, not applied standalone.
18. `mean_reversion.py`'s ADX docstring doesn't match its code (Day 92) — likely just a doc fix.
19. `/api/sectors/rotation` still uses a direct `yf.download()` instead of the multi-provider
    orchestrator its two newer siblings use (Day 108) — the `fetchSectorRotation()` half of
    this was fixed Day 108 (Golden Rule 47); the backend half remains.

**Full detail on every open item:** `docs/claude/versioned/KNOWN_ISSUES_DAY119.md`.

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
| 101 | Built "Sub-Industry Watch" (21 sub-industry theme-cluster proxy ETFs, Sectors tab) natively after the user showed the Trading Intelligence Hub's own separate version — reused STA's own RS-ratio formula (newly-extracted shared helper) and existing Tradier credentials instead of depending on the Hub's copy. Found and fixed a real bug mid-build: a per-request provider rate-limit fallback could silently mix tz-naive/tz-aware series across tickers, zeroing out date alignment (new Golden Rule 40). Adopted a hub-side test-coverage handoff for the existing `/api/sectors/rotation` endpoint, independently re-verified before adoption. Freeze-independent (Sectors-tab display work, same category as Day 93). v4.54 → v4.55 (Backend v2.47 → v2.48, Frontend v4.49 → v4.50). |
| 103 | Investigated SRPS, a user-brought 5th-forward-test-track proposal, through its own two pre-registered gates: Gate 0 (signal frequency) passed; Gate 1 (a new day-by-day portfolio backtest, 400-ticker survivorship-free universe, 2020-2025, real max-6-concurrent-position cap) failed its own bar (34.1% WR vs required 45%, PF 1.177 vs required 1.2) — not built as a live track. Found+fixed 3 real bugs during the build (Rule 3/5 whipsaw, a universe-construction survivorship leak, a near-zero-stop-distance R-multiple artifact). Pivoted the same rules into a discretionary Sectors-tab screener instead (shipped). Adopted the Trading Intelligence Hub's escalating three-pass review as Golden Rule 41 (supersedes Rule 32). Fixed a real, user-reported Forward Test tab display bug (closed trades silently capped at 20 for MR/HUB-65). Investigated (not fixed) a real Sector Rotation data-sourcing gap. Corrected a real backend/frontend version-drift found in source code, not just docs. Freeze-independent throughout — the 4 live tracks untouched. v4.55 → v4.56 (Backend v2.44→v2.45, Frontend v4.30→v4.51, both corrected-and-bumped). Additive API change, see `API_CONTRACTS_DAY103.md`. |
| 104 | Built `.claude/commands/watchlist-report.md`, a new Claude Code skill (not STA app code) turning a pasted IBKR/TWS thematic ETF watchlist into a durable Artifact catalyst report. Made it actionable via precedent-researched readiness bucketing + 4 risk-framing indicators (user-confirmed before building); found+fixed 2 real design bugs (RSI-alone extension flag, partial-bar relative volume) and a charset rendering bug while live-testing. Re-sourced data from real IBKR account data at the user's instruction; found a new, project-general bug — parallel `get_price_history` results don't reliably preserve call order — caught via cross-verification, not trusted positionally; new Golden Rule 42. No `backend/`/`frontend/` files touched, no version bump, no API changes. Open item: the published Artifact was rendering blank on the platform at session close (file verified correct locally; not an STA issue). |
| 107 | Deep-validated Path B forward-test data (real, net-of-fees math confirmed; a large-gap-entry pattern flagged, not fixed). Re-ran `/watchlist-report`, found+fixed a real cross-provider stock-split data mismatch (yfinance stale on 2 leveraged ETFs vs. IBKR correct — new Golden Rule 46). Built the "STA vs. 100 Years of Trading Principles" Artifact via full Plan Mode: 3-pass-verified code audit (Pass 3 caught a real, previously-unknown UI bug — a 3rd stale Fear & Greed threshold copy in `App.jsx`) cross-checked against 3 independently-researched LLM sources (Perplexity, ChatGPT, Gemini — ChatGPT caught and corrected a real imprecision in Perplexity's framing of the Moreira & Muir paper). Result: 7/9 categories match, 1 partial (momentum), 1 gap (volume). Ran a backtest-only research spike (user's explicit choice among 3 options) testing both directly via 2 new, purely-additive research configs in `backtest_holistic.py` — neither shows a credible edge (volume confirmation's tested design was too strict; dual momentum tested clean but near-inert). Found SimFin's ticker universe has drifted since Day 79, breaking exact seed-based backtest reproducibility — new Golden Rule 45. No live app code touched, no version bump. |
| 108 | Full 10-group system audit (all 9 tabs + core verdict engine + FWD-testing engine + providers package), scoped via Plan Mode after the user caught 2 real gaps in an initial too-narrow scoping pass. 27 items checked: 15 real bugs fixed (most severe: MTF Confluence's fabricated-dates bug, CRITICAL; Golden Rule 30's `fetchSectorRotation()` fix finally applied at its root — new Golden Rule 47; `/api/health`'s hardcoded-always-healthy status; a wasted-Alpha-Vantage-credit Context-tab bug), 8 parked (most notable: VIX position sizing never wired into the live engine, verified zero impact on current stats — new Golden Rule 48), 4 clean. Resolved the long-uncertain Canadian Analyze page question (confirmed fully working). v4.58→v4.59 (BE v2.46→v2.47, FE v4.53→v4.54). One additive API change. Zero findings touched any of the 4 live tracks' frozen logic. |
| 109 | Analyze Page Redesign — design phase complete, zero application code touched. 17 decisions locked via an item-by-item Q&A process (new Golden Rule 49): Technical structure and Market Regime stay mechanical (Regime gains a new, more-visible gate), Fundamentals becomes a red-flag screen, Risk:Reward and position sizing become fully informational, default view changes Simple→Full. User explicitly demanded independent persona pushback rather than execution of their own framing, producing 2 surviving disagreements (new PERSONA.md Feedback Log entry). A dedicated Opus validation pass caught 4 real corrections (new Golden Rule 50) and resolved 4 more open items, including a real bug found live since Day 39 — a hardcoded fake "half" position-size label (new Golden Rule 51). Full record: `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`. New ROADMAP Priority #17. v4.59 unchanged. |
| 110 | Built + published an interactive mockup of the Day 109 redesign. Live clustering check across all 4 forward-test tracks found real single-day entry concentration in every one, most notably MR HUB-65 (48.5% of its sample, one semiconductor-heavy day that *underperformed* rather than inflated the number). MR broad reached 99/100 closed. User directly challenged and got Claude to reverse the Day 109 "Regime stays a hard gate" decision after genuine re-examination (new PERSONA.md Feedback Log entry). New Golden Rule 52 after a real near-miss (a reply claimed a doc edit was done before the tool call had happened — caught before close). Zero application code touched, v4.59 unchanged. |
| 111 | Longest session in the project's history. Full technical audit of 5 Analyze-page cards graded against real methodology (S&R 2/10, MTF Confluence 3/10, Pattern Detection's price target 1.5/10 — new Golden Rule 53) + a complete data-provenance map (5 findings, 2 fixed). Two real features shipped and verified live: MR Scanner wired to the Scan tab (existed since Day 81, never connected), Volume Confirmation + Direction on the Trade Setup card (two-phase Opus-planned build, new `meta.candle` API field). MR (broad) crossed 100 trades and genuinely confirmed (PF 3.0021, holds at 2.24 ex-cluster) — the first track to ever clear the bar for real; Momentum Path B also crossed 100 but fails the identical stress-test (PF 1.2293 headline, PF 0.72 ex-cluster, 66.7% of the sample in one 4-day window) — not treated as confirmed. New Golden Rule 54 after discovering, before writing any code, that the planned S&R fix would reset Path B's live count — that decision is the top open item for next session. v4.59→v4.60 (BE v2.47→v2.48, FE v4.54→v4.55). Additive API change (`meta.candle`). |
| 112 | **Momentum Path B RETIRED** (150 closed, no live edge, ex-cluster PF 0.72) — stops generating signals, open positions wind down, row kept as history. **S&R `_pivot_sr` nearest-level fix (Golden Rule 53)** — the pivot method kept the most *extreme* levels, not the *nearest*; fixed behind `SRConfig.pivot_nearest_selection`; + BUG-A (★ confluence-badge key-format mismatch, ~10% of levels) + BUG-B (Price Structure showed deepest supports not nearest) + touch scoring restored on the pivot path. Verified live on META (R1 $612.43 / 0.3% above vs pre-fix ~$745). **Config C backtest re-baselined PF 0.97 → 0.53** on corrected levels — the old number was partly a bug artifact (R:R inflated by a far reward target); pre-registered "trades rise" prediction was wrong, logged (Golden Rule 56). PF 1.40 formally retired. Fix ships anyway — Config C is not a live track. Closes the "corrected-S&R momentum forward-test variant" question: NO. **Pattern targets** — Cup & Handle / Flat Base now measured-move (cup depth / base height), null when geometry missing; VCP flagged flat +15% pending Phase 4. New Golden Rule 55 (scoped Opus-plan-then-Sonnet-implement). New `--momentum-only` backtest flag; additive `meta.pivotSelection` API field. 4 stale artifacts repaired + 1 new (Forward-Test Track Board). Version constants were drifted (BE v2.47/FE v4.54) — corrected to v2.49/v4.56. v4.60→v4.61. |
| 113-118 | Consolidated close (no formal `/sta-end` had run since Day 112). **Day 113:** paper-trading program DISCONTINUED entirely at the user's explicit direction — pure analysis/recommendation tool from here on, no IBKR execution, MR (broad) stands as the final confirmed result. **Day 116:** OBV `trend` sign bug fixed + a real, previously-unlogged partial-bar RVOL bug found and fixed same session (new `barComplete`/`prevBar` API fields) + a new same-day effort-vs-result volume read. **Day 117:** Antonacci's absolute-momentum leg surfaced as an informational read on both Analyze-page views, sourced from the real Day 107 backtest constant — new Golden Rule 57 after the Opus plan caught a near-miss that would have silently added a 10th criterion to the 9-criterion checklist. **Day 118:** completed the S&R fix chain — MTF Confluence's dead `strength` field is now a real graduated score with synthetic-level exclusion; VCP's flat +15% target replaced with real nearest-resistance/measured-contraction-depth. Every read this stretch verified as gating nothing. v4.61→v4.62 (BE v2.49→v2.51, FE v4.56→v4.59). |
| 119 | Planning-only, no version bump. User challenged the shape of the post-Day-118 backlog (diminishing-returns audit items, no live gates left); agreed and re-scoped the Analyze Page Redesign (Priority #17) as the one bounded piece of real work remaining. Opus-planned re-verification of the Day 109 decision doc's own §7/§8 execution plan against six sessions of intervening code (Golden Rule 55): 17 decisions and phase structure hold; freeze-safety audit's conclusions survive but for new reasons (parity/backtest-comparability, not forward-test — the freeze itself ended Day 113); 9 corrections found, most importantly two blocks of prescribed on-card copy that described bugs already fixed (Day 112/118) and would have shipped as fabrications. New plan: `ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`, go/no-go GO, not yet built. Zero application code touched. |

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
