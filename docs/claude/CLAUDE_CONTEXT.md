# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 96 — end of day (July 24, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 96 |
| Version | v4.52 (Backend v2.45, Frontend v4.47, Backtest v4.19, API Service v2.11) |
| Latest Status | PROJECT_STATUS_DAY96_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY96.md |
| Latest API | API_CONTRACTS_DAY96.md — `/api/paper-trading/status` gains `momentumPathB` (additive) |
| Focus | **Forward-testing accumulation remains the SOLE priority for Path A/MR — unchanged from Day 92.** One large session: fixed the paper-trading launchd timezone bug (Golden Rule 33); built `PERSONA.md`, a 30-year-veteran trading-judgment lens wired into `/sta-start`/`/sta-end` (Golden Rule 34); fixed a systemic circuit-breaker bug across all 6 data providers where ticker-specific data gaps were miscounted as provider-health failures (Golden Rule 36); and discovered the live momentum R:R gate never matched the actual backtested Config C entry logic — a real S&R-based check, not the flat/ATR proxy substituted since Day 81 (Golden Rule 35). Fixed by building **Path B**, a parallel forward-test experiment using the real gate, its own ledger `variant` tag, its own 100-trade bar, zero effect on Path A's count — now visible as its own card in the Forward Test tab UI. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 96 Summary (Persona + Provider Reliability Overhaul + Path B Forward-Test Experiment — v4.52)
- **Paper-trading launchd timezone bug fixed first** (carried in from Day 95's opening): machine's real timezone is Eastern, not Central as the plist assumed — job was firing at 4:30pm ET instead of 4:30pm CT, cutting the intended ~90-min post-close buffer to ~30 min. Fixed, schedule shifted to 17:30 ET. New **Golden Rule 33**.
- **Built `docs/claude/stable/PERSONA.md`** — a 30-year, all-cycle veteran trader's decision-making lens (first-principles discipline, market "don'ts," behavioral-finance pitfalls each grounded in a real project moment), wired into `/sta-start` (loaded every session) and `/sta-end` (Feedback Log updated at close). New **Golden Rule 34**.
- **Deep-dived the TradingView screener pipeline** end to end (how Config C candidates flow into momentum/MR signals) and measured that momentum's live R:R gate rejected 81% of otherwise-qualifying candidates, 45% hitting an exact 0.80 ceiling — a structural artifact of `compute_entry_levels()`'s flat+8%/ATR-clamped-stop formula.
- **Systemic data-provider circuit-breaker bug found and fixed across all 6 providers.** Every provider counted a ticker-specific `DataNotFoundError`/`InsufficientDataError` (e.g. BRK.A having no data on Tradier) the same as a genuine connectivity failure — a couple of unlucky ticker misses could trip a perfectly healthy provider's breaker and block everyone else in that scan for 5 minutes. Verified live: Tradier re-tested 10/10 clean immediately after. New **Golden Rule 36**. Also centralized fragile `.env` loading into `providers/__init__.py`.
- **The big one: found that momentum's live R:R gate never matched the actual backtested Config C entry logic.** An initial fix attempt (widen the stop clamp) was tested via a quick backtest sanity check and proved directionally backwards — caught cheaply before weeks of live testing were wasted. Tracing *why* the trade set didn't change at all led to the real discovery: `backtest_holistic.py`'s real entry gate computes R:R from actual support/resistance levels, completely different from the flat/ATR proxy `live_signals.py` has used as its entry decision since Day 81 — same bug class as Golden Rule 19 (JS/Python parity), just live-vs-backtest. New **Golden Rule 35**.
- **Fixed by building Path B**: a parallel forward-test experiment using the real S&R-based gate (`check_sr_gate()`), same daily momentum candidates as Path A, tracked under its own ledger `variant` tag with its own 100-trade bar — Path A's frozen count is completely untouched. Surfaced live in the Forward Test tab as a visually-distinct "Momentum (Path B)" card, verified in-browser with zero console errors. The wrong first attempt was reverted cleanly and logged honestly in `PERSONA.md`'s Feedback Log, not defended.
- **Paper trading status:** Path A momentum 22 open/2 closed, Path B momentum 0 open/0 closed (new), MR 3 open/25 closed.
- Version v4.51 → v4.52 (Backend v2.44 → v2.45, Frontend v4.46 → v4.47). API additive-only change, see `API_CONTRACTS_DAY96.md`.

### Day 94 Summary (Sector Rotation Error-Handling Fix + Full README Audit — v4.51)
- **Sector Rotation Monitor silent-failure bug, found and fixed after a user question about yfinance failure handling.** `fetchSectorRotation()` swallowed every error to `null`, leaving the Sectors tab permanently stuck on its loading spinner with zero indication anything had broken. Fixed: `api.js` now throws, `App.jsx` gained `sectorRotationError` state + a shared `loadSectorRotation()`, `SectorRotationTab.jsx` gained a red error banner + Retry (matching the already-proven `ContextTab.jsx` convention). **A 2nd review pass (explicitly requested) caught a real regression**: `fetchSectorRotation()` is also called inside the Analyze Stock page's `Promise.all` — making it throw would have taken the whole page down on a sector-data hiccup, not just the badge; isolated with its own `.catch`. **A 3rd pass (same reason) caught a second real bug**: the Analyze page's own `sectorRotation` write path never cleared `sectorRotationError`, so a stale error banner could mask genuinely fresh data arriving via that other path. **New Golden Rule 32**: every fix now gets 3 review passes (does it work / what else calls the changed thing / what other state does it touch) — codified using this exact fix as the worked example.
- **First-ever full README.md Coherence Audit**, user-requested ("time to do our audits for documentation," flagged the README as stale). Ran 5 parallel research passes (Master Audit Framework, Layer 1) across the full 1486-line file against the live codebase — found ~50 real issues: 3 fully fictional API endpoints (`/api/forward-test/*` — never existed in code), the entire automated paper-trading engine and breakout engine nearly invisible (undocumented endpoints, missing from every diagram), a self-contradicting footer ("Day 65") sitting three lines below a Roadmap section that documents through Day 93, Stooq presented as an active data source despite being dead since Day 82 while Tradier (real since Day 83) was absent everywhere, and a Project Structure tree with phantom component directories that never existed. Fixed all CRITICAL/HIGH/MEDIUM findings plus most LOW ones directly, verified clean with a final sweep.
- **New `DEVELOPER_ONBOARDING.md`** — the user's friend is setting up a local fork to independently test/validate the tool (not to trade on it directly). Self-contained setup guide with the corrected env-var table, a disclaimer section up front, a pointer to `MASTER_AUDIT_FRAMEWORK.md` for independent validation, and the genuinely-applicable parts of `GOLDEN_RULES.md` translated for a human contributor rather than dumped verbatim.
- **Paper trading, monitoring only.** Momentum 14 open/1 closed, MR 3 open/23 closed — both unchanged from Day 93. Job confirmed healthy (`launchctl` active, exit code 0); traced a genuinely missed 2026-07-14 run (confirmed via ledger, not recoverable — TradingView has no point-in-time query), not actioned.
- Version v4.50 → v4.51 (Backend v2.44 unchanged — no backend.py edits this session; Frontend v4.45 → v4.46). No API contract changes.

### Day 93 Summary (Sectors/Context Tab Audit + Cross-Tab Connection — v4.50)
- **Sector Rotation Monitor — 3 real bugs then a full redesign.** Cap Size Rotation banner was mid-cap-blind (both the header signal and the momentum note computed text from QQQ/IWM only, ignoring MDY — produced "fading across all cap sizes" while MDY showed the opposite); fixed to genuinely consider all 3 tiers, catching a grammar bug via exhaustive testing of the fix itself. Bar/number color contradicted the quadrant label on the same tiles (user-caught from a live screenshot: MDY's bar was red while its label said "Improving"); fixed so both track the same quadrant color. Then, user-requested full redesign ("how would a quant trader design this for a beginner"): CTA was recommending the sector with the highest RS Ratio *magnitude* regardless of favorability (surfaced a "Weakening" sector as top pick) — new `pickBestSector()` fixes this properly; added a plain-English takeaway; grouped all 11 cards by quadrant; **removed the per-card "#N" rank badge entirely** after the user pointed out any ordinal reads as "the winner" regardless of qualifying text.
- **Context tab audit.** `econ_engine.py`'s composite narrative box had a real Day 91 regression — a stale PMI card-name lookup silently disabled 3 of 5 narrative branches (`KNOWN_ISSUES_DAY91.md` had even flagged "re-check the composite reflects it," never done); fixed via a shared `PMI_CARD_NAME` constant, dead `unemp` variable removed. Seasonal Regime card's May–Oct text contradicted its own NEUTRAL badge ("Sell in May"/"reduced exposure justified" next to yellow); softened per user's choice without touching the `overall_regime` aggregate.
- **New cross-tab connection.** Sectors tab now states in one sentence whether the macro backdrop supports the rotation shown (`macro_alignment` field, reusing the same FRED-cached engines, zero new API calls) — directly answering a question the user had to manually cross-reference two tabs to answer earlier in the session. Caught a second real bug: `api.js`'s `fetchSectorRotation()` silently whitelisted fields and dropped the new ones — invisible from code review, found only by checking the browser (new **Golden Rule 30**). Extended the same reconciliation to the Context tab's own Market Phase vs. Macro Regime banners, which had been stacked with zero explanation of whether they agreed.
- **Self-audit against GOLDEN_RULES.md** on this session's own work found: a Golden Rule 21 (DRY) violation between two components' duplicated style maps, fixed via new shared `frontend/src/utils/alignmentStyles.js`; a cached-response gotcha where several fixes appeared not to work live purely because `data/cache.db` was still serving pre-fix responses (new **Golden Rule 31**); an unverified extraction (`compute_overall_regime()`) closed by re-diffing live output; and a documentation self-contradiction (a fixed finding still listed as open in `KNOWN_ISSUES_DAY92.md`/`ROADMAP.md`), corrected.
- **Paper trading, monitoring only.** Momentum 14 open/1 closed; MR 3 open/23 closed (95.65% WR, PF 20.5 — confirmed via direct ledger inspection to be a real but heavily clustered result tied to one semiconductor-sector news event, not a demonstrated edge). Both far from the 100-trade bar; no rule/threshold changes.
- Version v4.49 → v4.50 (Backend v2.43→2.44 — also corrected a real code/docs version-drift found in the process; Frontend v4.44→v4.45). API additive-only change, see `API_CONTRACTS_DAY93.md`.

*(Day 92's summary rotated out — full detail preserved in `docs/claude/status/PROJECT_STATUS_DAY92_SHORT.md`. Day 91's is in `PROJECT_STATUS_DAY91_SHORT.md`. Day 90's is in `PROJECT_STATUS_DAY90_SHORT.md`.)*

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

**Forward-testing accumulation is the SOLE priority as of Day 92, unchanged Day 93-96** — user explicitly parked every other item below until 100 trades/system (raised from 50) are logged. Do not propose or start any of items 2+ unless the user raises it first — this is stricter than the Day 87 feature freeze it supersedes. (The Day 93 Sectors/Context tab work, Day 94's Sector Rotation fix + README audit, Day 95's launchd schedule/timezone fix, and Day 96's provider-reliability overhaul + PERSONA.md were explicitly scoped as independent of this freeze — pure display/UI/docs/ops/infra, no frozen-threshold contact — not new exceptions to the pattern. Path B is a genuinely new experiment, not a freeze exception, since it never touches Path A's count.)

1. **Let paper trading accumulate** — SOLE FOCUS. As of Day 96: **Path A** Momentum 22 open/2 closed (50% WR, PF 1.691 — still a tiny sample); **Path B** Momentum 0 open/0 closed (brand new — real S&R-based gate, see Golden Rule 35/`PAPER_TRADING_PREREGISTRATION.md` §8b); **MR** 3 open/25 closed (92% WR, PF 10.82 — still likely overfitting on a small sample per the system's own sanity check). Confirmation bar is **100 trades/system** for all three (`PAPER_TRADING_PREREGISTRATION.md`). Momentum Path A's pace is very slow — realistically weeks-to-months from the bar; Path B is untested territory, watch its first real signal when one comes. The job's `launchd` schedule was corrected Day 95 (now 17:30 ET) — sanity-check the next weekday's run fires as expected, once. `/sta-start` warns automatically if the launchd job goes stale (>3 days). If a Force Run "looks like nothing happened," don't assume it's a quiet day — re-run in the foreground and read stdout before trusting the aggregate UI. Check progress via the Forward Test tab's status panel (now with a separate Path B card) or `venv/bin/python paper_trading/daily_job.py --report`.
2. *(parked)* **Decide fundamentals mitigation** — Task 3.2 measured 40.0% live↔backtest disagreement; user decision pending (align live-to-SimFin or backtest-to-TTM). Now also affects the automated engine's momentum leg.
3. *(parked)* **Confirm SimFin key rotation** — user to verify the old leaked key was rotated at simfin.com; a possible new key was shared in conversation but not yet applied.
4. *(parked)* **N3 gap-fill detection** — needs its own design session first (Day 87 finding: no spec exists yet, only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`).
5. *(parked)* **Value Tab Phase 2** — needs its own batch-prefetch infrastructure design session first (Day 87 finding: `VALUE_TAB_SPEC.md` explicitly requires a nightly watchlist-prefetch job for AlphaVantage's ~8-tickets/day budget; on-demand fetching would contradict the documented design).
6. *(parked)* **Volume confirmation missing from the decision engine** (Day 92 finding) — neither the Full Analysis verdict tree nor the Simple Checklist's 9 criteria check volume *confirmation* of a price move (the checklist's "Volume" criterion is a liquidity gate, not a confirmation signal). Needs a re-backtest before shipping, since it touches frozen verdict logic. Companion item: `mean_reversion.py`'s ADX docstring doesn't match its code — likely just a doc fix.
7. *(parked)* **Build `/ibkr-scan` skill** — Research done (Day 77). Verify 52W High Proximity in IBKR first.
8. *(parked)* **Price Structure Phase 3** (visual chart via lightweight-charts) / Canadian Analyze page — queued.
9. *(parked)* **(Optional, low priority) Scan tab batch breakout badges** — distinguish `NOT_READY` from a failed fetch (currently both render "—"); same bug class as the Day 85 single-ticker fix, not yet requested at this location.
10. *(parked)* **(Optional, low priority) Master Framework Watchlist's Name/Market Cap columns** — still show N/A (Volume/Change % fixed Day 86, free); Name/Market Cap would need a separate fundamentals call per ticker, deferred by explicit user choice.
11. *(parked)* **Session 28 audit's remaining lower-priority findings** (Day 91) — Value tab badge attribution, Validate/Data Sources status-label honesty, Sectors `.toFixed(3)` false precision (the CTA-gating sub-item was fixed Day 93 via the Sectors tab redesign), Forward Testing's fee-accounting/silent-failure items, plus the audit's general polish list. See ROADMAP.md priority #10 and `KNOWN_ISSUES_DAY91.md` for full detail.
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

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
