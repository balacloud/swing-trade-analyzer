# CLAUDE CONTEXT - Single Reference Point

> **Purpose:** ONE file to reference in every session - handles all scenarios
> **Location:** Git `/docs/claude/` (root of claude docs)
> **Usage:** Add this file to Claude context. That's it.
> **Last Updated:** Day 105 — end of day (August 11, 2026)

---

## CURRENT STATE (Update this section each day)

| Field | Value |
|-------|-------|
| Current Day | 105 |
| Version | v4.57 (Backend v2.46, Frontend v4.52) — new sub-industry pullback screener endpoint + real Sectors-tab staleness fix |
| Latest Status | PROJECT_STATUS_DAY105_SHORT.md |
| Latest Issues | KNOWN_ISSUES_DAY105.md |
| Latest API | API_CONTRACTS_DAY105.md — new `GET /api/sectors/sub-industry-pullback-screen` |
| Focus | **Forward-testing accumulation remains the SOLE priority for the 4 live automated tracks — none of them were touched Day 105 either.** Session did real, freeze-independent app-code work: fixed a user-reported Sectors-tab staleness bug ("Refresh Session" cleared the backend cache but never told already-loaded frontend components to refetch — new Golden Rule 43), built a user-requested Sub-Sector Pullback Screener (SRPS's Day 103 discretionary screener extended from 11 broad sectors to the 21 Sub-Industry Watch clusters, sharing rule logic via newly-extracted helpers), and cross-checked 3 live screener candidates (CGNX, GEV, RIVN) against STA's own Full Analysis engine — all 3 came back "No Trade," surfacing a real structural gap in SRPS's own R:R math (fixed 2.5x-risk target, never checked against real resistance). MR (broad) forward-test now 83/100 closed, closest to its bar by a wide margin. |

---

## RECENT DAY SUMMARIES (Last 3 days only — older in status/archive/)

### Day 105 Summary (Sub-Sector Pullback Screener + Sectors-tab staleness fix, new Golden Rule 43, SRPS R:R gap found — v4.56 → v4.57)
- **Fixed a real, user-reported Sectors-tab staleness bug**: "Refresh Session" correctly cleared the backend's `market_cache` (Sector Rotation, Sub-Industry Watch, SRPS Pullback Screener) via `POST /api/cache/clear`, but the tab's own already-fetched frontend state (main sector cards, both lazy-loaded sub-sections) had no code path telling it to refetch — clicking Refresh Session repeatedly showed identical numbers with zero error or stale-data indicator. Fixed by threading a bump-able `sectorRefreshTrigger` prop into every component holding independently-fetched sector state, plus a new scoped in-tab "🔄 Refresh" button (new `clearMarketCache()` via `POST /api/cache/clear?type=market`, much narrower blast radius than the full Refresh Session). **New Golden Rule 43** — clearing a backend cache is not the same as invalidating frontend state that already fetched from it.
- **Built the Sub-Sector Pullback Screener** (user-requested, citing positive discretionary experience with the Day 103 sector-level version): the same SRPS Rules 1/3/4/6 applied to the 21 Sub-Industry Watch clusters instead of the 11 broad GICS sectors. New `GET /api/sectors/sub-industry-pullback-screen`; extracted `_srps_true_rs()`/`_srps_evaluate_candidate()` as shared helpers (Golden Rule 21) rather than forking the sector-level screener's logic a second time — verified behavior-preserving via live curl comparison. Two judgment calls confirmed with the user before building (both recommended options taken): included overlapping clusters that duplicate broad-sector coverage anyway, and screened proxy-only clusters (Gold Miners, Biotech — no underlying stock list) directly on their ETF rather than silently skipping them.
- **Three-pass review (Golden Rule 41) caught two real issues before shipping**: a pre-existing gap in the *sector-level* screener (its `sectorsCappedFrom` field has been computed since Day 102 but the frontend never displayed it — fixed alongside the new endpoint's equivalent field), and a real fan-out risk in the new endpoint itself (Semis alone has 16 curated candidate tickers, above the sector version's own established per-sector safety cap — added a matching `LIVE_CANDIDATE_LIMIT`).
- **Cross-checked 3 live screener candidates (CGNX, GEV, RIVN) against STA's own Full Analysis engine, at the user's request** — all 3 came back **"No Trade — avoid"** (4/9 or fewer Simple Checklist criteria, ADX <20 "no trend," Failed Breakout flags on 2 of 3). Found a real, generalizable structural gap, not specific to these 3 tickers: SRPS's target price is fixed at `entry + 2.5×risk` and never checks real chart resistance — STA's own Risk/Reward check (against actual support/resistance) came back at 0.48:1 and 0.27:1 for GEV/RIVN, nowhere near the screener's own implied 2.5:1. Logged as a Known Issue and in PERSONA.md's Feedback Log, not fixed — informational screen, not a live gate, and exactly the "apply your own judgment" its disclaimer already asks for.
- **Ran `/watchlist-report` on a new leveraged-ETF watchlist** ("AI_Leveraged," 8 tickers) at the user's request — flagged before running that 2×/3× daily-reset products carry decay risk the skill's existing readiness framework doesn't price in, and made sure the published report (a new, separate Artifact) carried that caveat prominently. Corrected a real misreading of `QPUX` mid-research (its actual holdings are quantum-computing names, not a "quant" trading strategy, despite the abbreviated ticker name). No `backend/`/`frontend/` files touched by this item — skill file + scratchpad Artifact only, same convention as Day 104.
- Version v4.56 → v4.57 (Backend v2.45→v2.46, Frontend v4.51→v4.52). Additive API change, see `API_CONTRACTS_DAY105.md`. No changes to the automated paper-trading engine or any frozen threshold — MR (broad) now 83/100 closed (live-pulled), closest to its bar by a wide margin.

### Day 104 Summary (Built `/watchlist-report` skill, re-sourced from real IBKR data, new Golden Rule 42 — v4.56 unchanged)
- **Built `.claude/commands/watchlist-report.md`** — a new Claude Code skill (not an STA app feature) that turns a pasted IBKR/TWS thematic ETF watchlist into a durable Claude Artifact report: catalyst/regime research per theme cluster (WebSearch), 10-day earnings-risk flags, and a small set of risk-framing technical indicators. Deliberately scoped separate from STA's own Sectors tab (thematic ETFs don't map onto STA's 11 broad GICS sectors) — confirmed with the user before building.
- **Made it actionable, precedent-researched first**: before building, researched how sibling projects (Trading Intelligence Hub's Options Sieve gate, Sector Advisory Panel's "alerting never deciding" rule) and STA's own `breakout_detection.py` handle "actionable without being a signal," proposed the approach back to the user via `AskUserQuestion`, got explicit confirmation, then built: readiness bucketing (🟢 Ready/🟡 Extended/🔴 Below trend/⚪ Unclassified, a state description not a verdict, per PERSONA.md Core Principle 2) plus RSI(14)/relative volume/ATR-stop%/trend-vs-200EMA.
- **2 real design bugs found live-testing** (not from a symptom report): RSI(14) alone missed a genuinely stretched long-term trend (SMH/SOXX read neutral RSI while +21-23% above their 200-EMA) — fixed by making "Extended" an OR of RSI≥65 or Px/EMA200≥+15%; relative volume's partial-bar problem (today's still-forming volume compared against a complete-session average reads structurally low) — same failure family as Golden Rule 39 in a new shape, fixed by removing it from bucket-gating logic. Plus 1 rendering bug (missing `<meta charset="utf-8">` caused a near-blank Artifact render), found by actually loading and looking at the published page.
- **Re-sourced from real IBKR account data at the user's explicit instruction** (`get_watchlists`→`get_watchlist`→`get_price_history` per real `contract_id`, RSI/ATR still computed via STA's own reused functions). **Found a new, project-general bug**: a 24-call parallel batch of `get_price_history` did not reliably preserve call order — two tickers' full OHLCV series came back transposed. Caught only by cross-verifying each result's last-close/volume against the pasted watchlist's real numbers before trusting anything positionally; resolved by re-fetching the ambiguous subset in smaller, well-separated batches. **New Golden Rule 42** — generalizes to any parallel tool-call batch keyed by which call produced each result, not just IBKR.
- Also self-caught 2 transcription errors while manually compiling the verified data (COPP/DRAM duplicated, DRIV/BOTZ swapped) via a programmatic last-close verification script before they reached the report.
- **Open item**: the republished Artifact rendered blank on the platform (no console error) — isolated to a platform-side issue, not a file bug, by confirming a clean local-server render of the identical file. Reported honestly as unresolved rather than claimed done. Not an STA issue — tracked in the skill file and status docs only.
- No `backend/` or `frontend/` files touched. No version bump (v4.56 unchanged). No API changes.

### Day 103 Summary (SRPS investigated + failed its own backtest, pivoted to a screener — v4.56)
- **SRPS (Sector Rotation Pullback System)** — a fully-specified user-brought design for a 5th forward-test track, run through its own pre-registered Gate 0 (signal frequency — passed, ~143 signal-days/year) and Gate 1 (full survivorship-free backtest, 400 tickers, 2020-2025, a new day-by-day portfolio simulator with a real max-6-concurrent-position cap — the first backtest in this project built that way). **Gate 1 failed**: 34.1% win rate (needed >45%), PF 1.177 (needed >1.2). Internally consistent with the design's own corrected expectancy math, not a broken/surprising number. Per the design's own rule, not built as a live automated track — sub-industry expansion (its own Phase 2) explicitly not pursued either, since the failure was about the entry/exit rules, not the universe.
- **Three real bugs found and fixed during the Gate 1 build**: a Rule 3/Rule 5 whipsaw (entries could trigger their own exit within 1 day — fixed with a 5-bar trail delay matching this project's own pre-existing EMA-trail convention); a universe-construction bias that silently dropped real historical bankruptcies before a survivorship-free test could count them (fixed by reordering — download price history first, tag sector only for survivors); a near-zero stop-distance bug that produced a 331,408 R-multiple artifact (fixed with a new minimum-stop floor, `srps_constants.py`).
- **Pivoted to a discretionary screener** — same rule logic, new `GET /api/sectors/pullback-screen` + a new "🎯 Sector Pullback Screener" section on the Sectors tab. Informational only, permanent disclaimer that the backtest failed, no ledger/automated entry-exit. A three-pass review of this endpoint (see below) found and fixed 2 further real bugs before shipping.
- **New Golden Rule 41** — escalating three-pass code review (each pass strictly more critical than the last), adopted from the Trading Intelligence Hub's own standing rule at the user's request, explicitly superseding Rule 32's older fixed-lens version. First real run (on the screener) caught a timezone-normalization fix that was silently discarded before reaching the data it needed to fix, and an unbounded per-sector data-fetch loop — capped after confirming live that 8-9 sectors being simultaneously Improving happens ~4x/year, not hypothetically.
- **Forward Test tab bug fix (user-reported "not all is displayed")**: the closed-trades table (and its "Show tickers (N)" button count) silently under-reported MR/HUB-65 — 71/28 real closed trades, only 20 ever shown, no indication. The aggregate stats were always correct; only the per-ticker table was wrong. Fixed with a visible truncation note, matching the Scan tab's own existing 20-row-cap precedent.
- **Forward Test data investigation (user-reported "I think it's off")**: confirmed the display was correct (an early diagnostic script of Claude's own had missed a key, corrected before concluding). Path A's real win-rate drop traced to a correlated 4-trade batch — 2 REITs, plus the general-partner/limited-partner units of the same pipeline company entering as if independent — a live materialization of the already-known correlation-gap Known Issue (Day 100), not a new bug. Exit mechanics verified clean.
- **Sector Rotation data-sourcing review (investigation only, not fixed)**: confirmed the original 11-sector endpoint still has no provider fallback (its two newer siblings both do) and its frontend fetch function is still a whitelist reconstruction — the exact pattern that already caused one real bug (Day 92). Logged as new Known Issues, offered as a future fix.
- **Version-drift correction**: `backend.py`'s `BACKEND_VERSION` constant was stuck at `'2.44'` (4 versions behind docs) and the frontend footer hardcoded `"v4.30"` (20 versions behind docs) — both pre-existing, corrected at the source this close.
- Version v4.55 → v4.56 (Backend v2.44→v2.45, Frontend v4.30→v4.51, both corrected-and-bumped). Additive API change, see `API_CONTRACTS_DAY103.md`. No changes to the automated paper-trading engine or any frozen threshold.

*(Day 102's summary rotated out — full detail preserved in `docs/claude/status/PROJECT_STATUS_DAY102_SHORT.md` (Questrade Flow experiment scoping, real-money ETF automation separate from STA). Day 101's is in `PROJECT_STATUS_DAY101_SHORT.md` (Sub-Industry Watch, new Golden Rule 40). Day 100's is in `PROJECT_STATUS_DAY100_SHORT.md`. Day 99's is in `PROJECT_STATUS_DAY99_SHORT.md`. Day 98's is in `PROJECT_STATUS_DAY98_SHORT.md`. Day 97's is in `PROJECT_STATUS_DAY97_SHORT.md`. Day 96's is in `PROJECT_STATUS_DAY96_SHORT.md`. Day 94's is in `PROJECT_STATUS_DAY94_SHORT.md`.)*

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

**Forward-testing accumulation is the SOLE priority as of Day 92, unchanged Day 93-105** — user explicitly parked every other item below until 100 trades/system (raised from 50) are logged, now across FOUR tracks. Do not propose or start any of items 2+ unless the user raises it first — this is stricter than the Day 87 feature freeze it supersedes. (The Day 93 Sectors/Context tab work, Day 94's Sector Rotation fix + README audit, Day 95's launchd schedule/timezone fix, Day 96's provider-reliability overhaul + PERSONA.md, Day 98's HUB-65 track, Day 99's partial-bar ledger contamination fix, Day 100's monitoring/documentation session, Day 101's Sub-Industry Watch feature, Day 103's SRPS investigation + Sector Pullback Screener, Day 104's `/watchlist-report` skill build, and Day 105's Sub-Sector Pullback Screener + Sectors-tab staleness fix were explicitly scoped as independent of this freeze — pure display/UI/docs/ops/infra, a genuinely new separately-tracked experiment (that in SRPS's case failed its own backtest and was never built live), a data-integrity fix to existing infrastructure, a user-requested extension of an already-informational screener, or (Day 104) a standalone Claude Code skill that touches no STA app code at all — not new exceptions to the pattern. Path B and HUB-65 are both genuinely new experiments, not freeze exceptions, since neither touches an existing track's count. Day 97's IBKR research/plan is explicitly parked by the user's own choice — do not start Phase 1 unless raised again. Day 99's "Quick" momentum holding-period idea was scoped/planned but the user stopped before approval — nothing built, needs re-planning from scratch if raised again. Day 100's scheduled breakout-alert watcher idea (ROADMAP priority #15) is explicitly idea-only — needs its own design session before any build, not started.)

1. **Let paper trading accumulate** — SOLE FOCUS, now across 4 tracks, on a *corrected* ledger (Day 99 partial-bar fix — see Golden Rule 39). **Track numbers move fast between sessions — always pull live via `daily_job.py --report`, never quote a status doc.** As of last live check (2026-08-11, job last ran 2026-08-10): **Path A** Momentum 35 open/24 closed (41.67% WR, PF 0.9697); **Path B** Momentum 85 open/26 closed (61.54% WR, PF 1.9825); **MR** (broad) 8 open/**83 closed (79.52% WR, PF 4.5809** — closest to its bar by a wide margin, "win rate >70%, likely overfitting" warning still showing, same expected-cooling read as prior sessions applies); **MR (HUB-65)** 2 open/29 closed (51.72% WR, PF 1.4306). All four tracks gained new closed trades since Day 103/104's check (Path A +8, Path B +11, MR broad +12, HUB-65 +1). Confirmation bar is **100 trades/system** for all four (`PAPER_TRADING_PREREGISTRATION.md`). MR (broad) is closest to the bar at 83/100 — plausibly clears it within the next few sessions. The job's `launchd` schedule was corrected Day 95 (now 17:30 ET). `/sta-start` warns automatically if the launchd job goes stale (>3 days). If a Force Run "looks like nothing happened," don't assume it's a quiet day — re-run in the foreground and read stdout before trusting the aggregate UI. Check progress via the Forward Test tab's status panel or `venv/bin/python paper_trading/daily_job.py --report`.
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
13. *(parked, offered not requested, Day 103)* **Bring `/api/sectors/rotation` up to the same standard as its two newer siblings** — swap its direct `yf.download()` call for the multi-provider orchestrator (matching `/api/sectors/sub-industry` and `/api/sectors/pullback-screen`), and convert `fetchSectorRotation()` in `api.js` from a whitelist reconstruction to a pass-through (matching the same two siblings, and the exact fix that already prevented a repeat of the Day 92 `macro_alignment` bug elsewhere). A contained, freeze-independent fix — offered to the user Day 103, not started.
14. *(not an STA item, Day 104)* **`/watchlist-report`'s published Artifact was rendering blank** at Day 104's close (platform-side, file verified correct via local server) — if the skill is used again, check `https://claude.ai/code/artifact/03423c12-9a9c-4334-8e32-6b2b822f418e` and republish if still blank. Not tracked as an STA bug since it's outside the app entirely. Not rechecked Day 105 (a different watchlist's Artifact was published instead).
15. *(parked, offered not requested, Day 105)* **SRPS screener's R:R is structurally disconnected from real support/resistance** (both `/api/sectors/pullback-screen` and `/api/sectors/sub-industry-pullback-screen`) — the target price is fixed at `entry + 2.5×risk`, never checked against actual chart resistance. Cross-checking 3 live candidates against STA's own Full Analysis Risk/Reward check found real R:R of 0.48:1 and 0.27:1, nowhere near the screener's own implied 2.5:1 — true of every candidate the screener will ever produce. A real fix (computing target against actual resistance, matching the Full Analysis engine's own method) would be a genuine rule change to SRPS's already-fixed, backtested-and-failed rule set. Not urgent — the screener is explicitly informational and its disclaimer already asks for exactly this kind of judgment. See `KNOWN_ISSUES_DAY105.md`.

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

---

*This file replaces the need for SESSION_START.md + SESSION_PROMPT_TEMPLATE.md*
*User only needs to reference this ONE file in Claude context*
*For core rules and lessons learned → see GOLDEN_RULES.md*
