# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 111
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v4.60 (Backend v2.48, Frontend v4.55, Backtest v4.20→v4.21, API Service v2.11)
*Day 111: v4.59→v4.60 (Backend v2.47→v2.48, Frontend v4.54→v4.55) — the longest session in the project's history. Full technical audit of 5 Analyze-page cards graded against real methodology (Price Structure/Breakout Status 9/10, Pattern Detection recognition 8/10 but its price target 1.5/10, MTF Confluence 3/10, S&R 2/10 — new Golden Rule 53), plus a complete data-provenance map of every tab (4 separate data systems, not one pipeline; 5 findings, 2 fixed). Two real features shipped and verified live: the MR Scanner (`fetchMRScan()`/`/api/mr/scan` had existed since Day 81, fully built, never wired to a button — now is, plus its orchestrator-bypass bug fixed) and Volume Confirmation + Direction (a two-phase build on the Trade Setup card — magnitude first, then a directional lean combining price change/close-location/OBV trend, both Opus-planned before implementation, both catching real premise errors in the process; new `meta.candle` API field). Two forward-test tracks crossed their 100-trade bar with sharply different outcomes under the same stress-test: MR (broad) genuinely confirmed (138 closed, PF 3.0021, held at PF 2.24 excluding its largest cluster); Momentum Path B clears the numeric bar (117 closed, PF 1.2293) but 66.7% of its sample entered in one 4-day window and excluding it flips the track to PF 0.72, net losing — not treated as confirmed. New Golden Rule 54 after discovering, before any code was written, that the planned S&R fix would reset Path B's live count (support_resistance.py's compute_sr_levels() is imported directly by the live paper-trading entry gate, not just the Analyze page) — that decision is still pending. New `AUDIT_COVERAGE_LEDGER.md` and `SESSION_ARTIFACTS_INDEX_DAY111.md` (7 Artifacts published this session, cataloged with an honest current-state note on each). Full detail: `docs/claude/status/PROJECT_STATUS_DAY111_SHORT.md`, `docs/claude/versioned/KNOWN_ISSUES_DAY111.md`.*
*Day 110: no version bump — mockup/forward-test check-in session, zero application code touched. Built and published an interactive mockup of the Day 109 Analyze Page Redesign (`docs/claude/design/mockups/analyze_page_redesign_mockup.html`), closing the "no visual mockup built yet" open item from §9 of the decision doc. Pulled live forward-test numbers for all 4 tracks and ran the same entry-date clustering check that first caught a bad pattern in broad MR on Day 93 — found real single-day concentration in all four: Path A (27% on one day, bank-heavy), Path B (23% on one day, energy-heavy), MR broad (40% across 3 consecutive days, the same Day-93 pattern persisting), and most notably MR HUB-65 (48.5% — 16 of 33 closed trades — on one semiconductor-heavy day, a cohort that actually *underperformed* the rest of the sample rather than inflating it). Confirmed via a fresh code check (Explore agent, file:line cited) that the Day 100 "no sector/portfolio-correlation awareness in either entry gate" finding is still exactly true — no code changed. Force-ran the paper-trading daily job (safe, same-day re-run, no duplicate trades — confirmed the Day 90 dedup guarantee still holds); MR broad is at 99/100 closed, one trade from its bar. Separately, the user directly challenged the Day 109 decision to keep Market Regime a hard gate on the Analyze page; re-examined honestly and reversed it — Regime becomes informational (Info), kept expanded by default rather than collapsed since it's portfolio-wide, but no longer enforced or using imperative language. `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` item 4 updated with the reversal; the published mockup itself was **not** updated to match this session and still shows the pre-reversal copy (flagged as a known inconsistency, §9). New Golden Rule 52 — a reply claimed a decision-doc edit had already been made when the tool call hadn't actually happened; caught and fixed before this session's close, not after. See Priority #17 below.*
*Day 109: no version bump — design-only session, zero application code touched. Redesigned the Analyze page's decision architecture end-to-end via an item-by-item Q&A process with the user (new Golden Rule 49), each decision researched, discussed through the PERSONA lens, and locked before moving to the next — 13 items decided this way, then stress-tested by a dedicated Opus validation pass that found 4 real corrections a lighter pass had missed (new Golden Rule 50) and resolved 4 more open items (new Golden Rule 51). Net result, recorded in full at `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`: Technical structure and Market Regime stay mechanical (the latter gets a new, more-visible always-on gate, not less); Fundamentals becomes an evidence-based binary red-flag screen instead of a scored verdict input; Risk:Reward and position sizing become fully informational (fixing a real, previously-undiscovered bug along the way — the Momentum entry panel's "half" position-size label was hardcoded with zero computation behind it, live since Day 39); the Analyze page's default view changes from the mechanical Simple Checklist to the redesigned Full Analysis view. A full phased implementation plan and freeze-safety audit are written but **not executed** — `backend/support_resistance.py`, `backend/backtest/categorical_engine.py`, and all 4 live forward-test tracks are explicitly confirmed untouched and stay that way until a future session is asked to build this. See Priority #17 below.*
*Day 108: a full 10-group system audit (scoped and executed same session via Plan Mode + parallel background sub-agents, using `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`), covering all 9 tabs + the core verdict engine + the FWD-testing engine + the data-provider package. 27 items checked, 15 real bugs fixed, 8 real findings parked (need a decision or bigger scope), 4 came back clean. Most severe fix: the Analyze page's MTF Confluence weekly S&R levels were silently computed from fabricated calendar dates, not real trading weeks (CRITICAL). Also fixed: Golden Rule 30's `fetchSectorRotation()` whitelist bug (never actually migrated to the fix it was named after — new Golden Rule 47), `/api/health`'s hardcoded-always-healthy status, a wasted-Alpha-Vantage-credit bug on the Context tab, an ETF-inaccurate data-source banner, a negative-FCF-Yield badge bug, two React falsy-zero risks, several mislabeled/silently-hidden UI states. Resolved the long-uncertain "Canadian Analyze page" question — confirmed fully working end-to-end (CMG.TO + RY.TO, broader coverage than the Day-106 spot-check). Most notable parked finding: VIX-based position sizing was never wired into any of the 4 live automated tracks — verified this doesn't affect any current live-track statistic (all are position-size-invariant %/R-multiple figures), so parked without urgency rather than escalated (new Golden Rule 48). Zero findings required touching any of the 4 live tracks' frozen entry/exit logic — see `docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md` for full detail, `API_CONTRACTS_DAY108.md` for the one additive API change.*
*Day 107: no live app version bump — Backend/Frontend untouched. Backtest tooling only: added two new, purely-additive research configs (F/G) to `backtest_holistic.py`'s `check_entry_signals()` plus a new standalone script `research_spike_volume_momentum.py`, to test the two gaps found by the same day's "STA vs. 100 Years of Trading Principles" Artifact (`https://claude.ai/code/artifact/cc9d82c6-b961-4aec-aa37-e384ca512083`) — volume confirmation and dual/absolute momentum. Diff-verified as purely additive (zero lines touching Config C's own logic). Result on the same 400-ticker/seed=42 survivorship-free universe: neither shows a credible edge — Config F (1.5x volume confirm) cut trades 75→5, too strict to evaluate; Config G (absolute momentum vs. 5% risk-free) excluded only 1 of 75 trades, technically clean but near-inert in practice. Both stay parked on Priority #11 below, now with real backtest evidence. Side-finding while sanity-checking a surprising Config C baseline: SimFin's ticker coverage has drifted (3,788→3,745 since Day 79), so the same seed no longer reproduces the canonical PF 1.40 exactly — new Golden Rule 45. Also found (Day 107, via the same audit's 3-pass review) a real, unfixed UI bug: `App.jsx`'s Fear & Greed gauge uses a third, stale copy of the sentiment threshold bands — see `KNOWN_ISSUES_DAY107.md`.*
*Day 106 (v4.58): Fixed the Scan tab's breakout-badge dash ambiguity — a bare "—" used to mean three different things ("beyond the 20-row cap," "requested but no result came back," "checked and genuinely NOT_READY"); each now gets its own honest label (new Golden Rule 44), closing ACTIVE PRIORITY ORDER item #9. Built a new "STA Verdict" column on the Scan tab — an on-demand BUY/HOLD/AVOID button, shown only for rows the breakout engine already flagged Retest Entry / Building Base, reusing the existing `determineVerdict()` pipeline rather than a new decision path. Corrected an oversimplified self-description of the app (a prior assistant turn called it "a Minervini system" that "doesn't play the reversal game" — untrue, given the live Connors RSI(2) mean-reversion track and several other independent engines); updated the app's header tagline, the Analyze tab's empty-state caption, and README.md's opening paragraph to reflect the real multi-engine picture. No backend/API changes — frontend + docs only, freeze-independent (the 4 live forward-test tracks untouched).*
*Day 105 (v4.57): fixed a real Sectors-tab staleness bug (user-reported) — "Refresh Session" cleared the backend cache correctly but never told already-loaded frontend components (main sector state, Sub-Industry Watch, SRPS Pullback Screener) to refetch; new Golden Rule 43. Added a scoped in-tab "🔄 Refresh" button alongside the fix. Built the **Sub-Sector Pullback Screener** at the user's explicit request — the SRPS discretionary screener extended from the 11 broad GICS sectors to the 21 Sub-Industry Watch clusters, new `GET /api/sectors/sub-industry-pullback-screen`, sharing its Rules 1/3/4/6 logic with the sector-level screener via two newly-extracted helpers (`_srps_true_rs()`/`_srps_evaluate_candidate()` — Golden Rule 21). Cross-checked 3 live candidates from these screeners (CGNX, GEV, RIVN) against STA's own Full Analysis engine — all 3 came back "No Trade," and found a real structural gap in SRPS's own R:R math (target is fixed at entry+2.5×risk, never checked against real resistance) — logged as a Known Issue, not fixed (informational screen, not a live gate). See `API_CONTRACTS_DAY105.md`, `KNOWN_ISSUES_DAY105.md`. Freeze-independent throughout — the 4 live forward-test tracks untouched.*
*Day 103 close: another version-drift catch — this time in the actual SOURCE CODE, not just docs. `backend.py`'s own `BACKEND_VERSION` constant was stuck at `'2.44'` (unchanged since Day 92) while this file and CLAUDE_CONTEXT.md had moved on to claiming v2.48; the frontend footer hardcoded `"v4.30"` while docs claimed v4.50 (a 20-version gap). Both corrected at the source this close, same recurring pattern as the Day 84/96/101 doc-only drifts below — a session's version bump routinely updates the docs but not always the literal constant/string that displays it.*
*Day 103 (v4.56): investigated SRPS (Sector Rotation Pullback System), a fully-specified user-brought design for a 5th potential forward-test track — buy strong stocks in recovering sectors pulling back to their 21-EMA. Ran both of the design's own pre-registered gates before any live build: Gate 0 (signal frequency, ~143 signal-days/year) passed comfortably; Gate 1 (full survivorship-free backtest, 400 tickers, 2020-2025, a new day-by-day portfolio simulator with a real max-6-concurrent-position cap — the first backtest in this project with that shape) **failed** its own bar (34.1% win rate vs. required >45%, PF 1.177 vs. required >1.2). Per the design's own rule, not built as a live track. Found and fixed 3 real bugs during the build (a Rule 3/Rule 5 whipsaw interaction, a universe-construction bias that silently dropped real historical bankruptcies, a near-zero-stop-distance bug that produced a 331,408 R-multiple artifact) — see its own COMPLETE section below. Pivoted the same rule logic into a discretionary screener instead: new `GET /api/sectors/pullback-screen` endpoint + new Sectors-tab section, informational only, carries a permanent disclaimer that the backtest failed. Also: adopted the Trading Intelligence Hub's escalating three-pass code review as new Golden Rule 41 (supersedes Rule 32's fixed-lens version); fixed a real Forward Test tab display bug (closed-trades list silently truncated to 20 for MR/HUB-65 with no indication); investigated (not fixed) a real gap in Sector Rotation's original endpoint — no provider fallback, and its frontend fetch function is a whitelist reconstruction, not a pass-through, the same pattern that already caused a bug once. See `API_CONTRACTS_DAY103.md`, `KNOWN_ISSUES_DAY103.md`. Freeze-independent throughout — the 4 live forward-test tracks were not touched.*
*Day 101 (v4.55): built "Sub-Industry Watch" — 21 sub-industry theme-cluster proxy ETFs on the Sectors tab, one level below the 11 broad GICS sectors, built natively into STA after seeing the Trading Intelligence Hub's own separate version. New `GET /api/sectors/sub-industry` endpoint reuses STA's own RS-ratio formula via a newly-extracted shared helper (`compute_rs_ratio_and_quadrant()`) rather than a second implementation. Found and fixed a real bug mid-build: a per-request rate-limit fallback could silently mix tz-naive and tz-aware series, zeroing out the date-alignment step (new Golden Rule 40). Also adopted a hub-side test-coverage handoff for the existing `/api/sectors/rotation` endpoint (`test_sector_rotation.py`), independently re-verified before adoption. See its own COMPLETE section below, `API_CONTRACTS_DAY101.md`, `KNOWN_ISSUES_DAY101.md`. Freeze-independent (Sectors-tab display work, same category as Day 93).*
*Day 99 (v4.54): partial-bar ledger contamination fix (Golden Rule 39) — not reflected in this line until now, see the Day 101 catch-up note above.*
*Day 98 (v4.53): built a new, fully parallel Mean-Reversion track on a curated 65-ticker watchlist ("HUB-65", sourced from a sibling project's own screener research) — both a one-shot backtest of the existing, completely unchanged MR engine against this universe (`backend/backtest/backtest_hub_mr.py`, new) and a real forward-test track (`variant='mr_hub65'`, reusing the `variant` column's Day 95 plumbing for a second, orthogonal meaning — see new Golden Rule 38). Backtest: 1,940 trades, WR 57.78%, PF 1.2574, Sharpe 1.5278, block-bootstrap p=0.0311 — explicitly documented as selection-biased and NOT comparable to the survivorship-free baseline (PF 1.16), since HUB-65 is a 2026 watchlist picked because the names already look strong. Forward-test wired into `daily_job.py`'s Step 3 (randomized iteration order per Golden Rule 25), reported via a new `mrHub` block in `/api/paper-trading/status` (see `API_CONTRACTS_DAY98.md`) and a distinctly-badged (teal, "Curated-65 Universe") card in the Forward Test tab UI — deliberately different color/wording from Path B's amber "Experimental" badge, since this is a different *universe*, not a different *gate*. Also shipped a new "HUB-65 Watchlist" preset on the Scan tab (same `fetchWatchlistCandidates()` pattern as the existing Nirmal/Master Framework watchlists). Verified live end-to-end: isolation/cooldown-independence test (throwaway DB), a real `daily_job.py --force` run that queued a genuine AFRM signal, live `curl` of the API, and live in-browser checks of both the Forward Test card and the Scan tab watchlist (63/64 tickers live-scanned, DRAM correctly excluded as delisted, zero console errors). Own independent 100-trade bar — tagged Priority #14 below, tracked the same way Path B is, not a freeze exception since it never touches the broad MR track's count.*
*Day 97: no version bump — research/planning-only session. Investigated real IBKR paper-trading execution (user asked to connect to IBKR and actually place paper orders instead of the internal simulator). Verified the cited CIRO Rule 3200 regulatory restriction directly against CIRO's own published guidance rather than a secondhand summary (new Golden Rule 37) — governs real orders to a real marketplace, doesn't appear to restrict a pure paper account. Produced a full 4-phase implementation plan via Plan mode + a Plan-agent review, locked several design decisions with the user, then the user explicitly parked implementation pending their own further research — persisted as `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md`, tagged as Priority #13 below. No code changed.*
*Day 96 close: catching up a version-drift gap — this line was still Day 93's v4.50 while CLAUDE_CONTEXT.md had already moved through v4.51 (Day 94) and was closing at v4.52 (Day 95→96). Not part of the Day 94/95 closes' update checklists at the time; now caught up, same pattern as the Day 84 gap noted below.*
*Day 96 (v4.52): a single large session — paper-trading launchd timezone fix (Golden Rule 33); new `PERSONA.md` trading-judgment lens wired into `/sta-start`/`/sta-end` (Golden Rule 34); a systemic circuit-breaker fix across all 6 data providers, where ticker-specific data gaps were miscounted as provider-health failures (Golden Rule 36); and the big one — discovered the live momentum R:R gate never matched the actual backtested Config C entry logic (real S&R-based, not the flat/ATR proxy `live_signals.py` substituted since Day 81 — Golden Rule 35), fixed by building **Path B**, a parallel forward-test experiment using the real gate, tracked under its own ledger variant with its own 100-trade bar, zero impact on Path A's count. Surfaced live in the Forward Test tab UI. See `KNOWN_ISSUES_DAY96.md`, `PAPER_TRADING_PREREGISTRATION.md` §8b, `API_CONTRACTS_DAY96.md`.*
*Day 95 (mid-session, superseded by the Day 96 close above): sole focus remained forward-testing accumulation; this session's early work (screener deep dive, R:R measurement) was scoped as freeze-independent, same pattern as Days 93-94.*
*Day 84 close: fixed a version-drift gap — this line was still Day 81's v4.39 while CLAUDE_CONTEXT.md had already moved to v4.42 (Day 83). ROADMAP.md's version line wasn't part of the Day 83 close's update checklist; now caught up.*
*Day 85: no version bump — session was a backend/frontend reliability fix (Golden Rule 23), a breakout NOT_READY badge display fix, and a new TradingView screener reference doc, not a versioned feature.*
*Day 86: v4.44 — Master Framework Watchlist's user-tested gap (Name/Volume/Change/Market Cap showing N/A) led to a real `/api/sr/<ticker>` API change (new `volume`/`change` fields, see `API_CONTRACTS_DAY86.md`), warranting a backend version bump.*
*Day 87: v4.45 — Breakout Enhancement Plan Phase 1 (completing the whole plan), N4 Market Phase Synthesis, and Price Structure Card Phase 2 all shipped in one session (backlog cleanup before declaring a complete feature freeze). Value Tab Phase 2 and N3 gap-fill detection were scoped and explicitly deferred — see Golden Rule 24.*
*Day 88: v4.46 — Paper trading ledger surfaced in the UI (`/api/paper-trading/status` + `/trigger`, new Forward Test tab panel), agreed as the one scoped exception to the Day 87 freeze since it directly aids the paper-trading gate itself, not general product work.*
*Day 89: v4.47 — MR arm's automated live universe widened from a static 54-ticker list to a dynamic ~150-ticker TradingView scan (8 signals in one test run vs. 0-2/day historically), calibrated down from an initial 300 after a live test tripped TwelveData's rate limiter (new Golden Rule 25). Same scoped-exception rationale as Day 88 — faster sample accumulation for the paper-trading gate, not new features.*
*Day 91: v4.48 — Triaged the hub-side Session 28 audit (`HANDOFF_sta_audit_session28.md`, found untracked at repo root) and fixed its 4 top-priority findings: Scan tab's "Minervini SEPA" mislabel renamed, Sectors tab's false "100=market parity"/wrong-data-source claims corrected, Context tab's CPI card root-caused to a real date-alignment bug in `_yoy()` (not caching as the audit guessed — new Golden Rule 26) and fixed, PMI proxy card relabeled, and paper-trading's daily replay fixed to anchor stop/target to values already stored at entry instead of recomputing fresh (new Golden Rule 27). All bug fixes to existing systems — no new features, no API contract shape changes. Freeze remains in effect.*
*Day 92: v4.49 — A first-principles review of the decision engine found two real gaps (volume-confirmation missing from the verdict/checklist; MR's ADX docstring vs. code mismatch), logged as Priority #11 below and explicitly deferred. Separately, investigating a "Force Run did nothing" report found and fixed a real bug: `signal_date` was stamped from the wall clock instead of the OHLCV bar `signal_price` came from, which could permanently strand a signal in `pending_entry` if the job ran off a trading day (new Golden Rule 28) — 8 already-affected momentum signals were repaired, jumping momentum from 3 to 10 open positions. `/api/paper-trading/status` extended with per-position ticker/entry/exit detail (additive, see `API_CONTRACTS_DAY92.md`). **User explicitly raised the paper-trading confirmation bar from 50 to 100 trades/system and named forward-testing accumulation the sole priority** — see `PAPER_TRADING_PREREGISTRATION.md`'s Change Log and Priority #1 below.*

---

## COMPLETED (v1.0 - v3.9)

### Core Features
| Version | Feature | Day |
|---------|---------|-----|
| v1.0 | Single stock analysis, 75-point scoring | Day 1-5 |
| v1.1 | TradingView screener integration | Day 11 |
| v1.2 | S&R Engine with trade setups | Day 13 |
| v1.3 | Validation Engine with UI | Day 14 |
| v2.0 | Score breakdown with explanations | Day 23 |
| v2.5 | Trade viability display (Option D) | Day 22 |
| v2.9 | Simplified Binary Scoring (4→9 criteria, Day 60) | Day 27, 60 |
| v3.0 | Settings tab + Position Sizing Calculator | Day 28 |
| v3.1 | Auto-fill integration | Day 28 |
| v3.2 | Session refresh, position controls | Day 29 |
| v3.3 | Agglomerative S&R clustering | Day 31 |
| v3.4 | MTF confluence, fundamentals transparency | Day 33 |
| v3.5 | SQLite persistent cache (5.5x speedup) | Day 37 |
| v3.6 | start.sh/stop.sh service scripts | Day 37 |
| v3.7 | Data Sources tab (transparency UI) | Day 38 |
| v3.8 | Dual Entry Strategy UI | Day 39-40 |
| v3.9 | Data source labels, Defeat Beta error handling | Day 42 |
| v4.0 | Pattern Detection (VCP, Cup-Handle, Flat Base) + Categorical Assessment | Day 44 |

### S&R Improvements (Complete)
| Week | Task | Status |
|------|------|--------|
| 1 | Agglomerative Clustering | ✅ Day 31 |
| 2 | Multi-Timeframe Confluence | ✅ Day 32-33 |
| 3 | Fibonacci Extensions | ✅ Day 34 |
| 4 | Validation vs TradingView | ✅ Day 34 |

### Bug Fixes (Historical)
| Issue | Fixed | Day |
|-------|-------|-----|
| Risk/Macro Expand Crash | ✅ | Day 29 |
| TradingView OTC Stocks | ✅ | Day 21 |
| ATR = null | ✅ | Day 20 |
| RSI Always N/A | ✅ | Day 22 |
| Backend Cache Stale | ✅ | Day 25 + Day 37 |
| UX Confusion (Mixed Signals) | ✅ | Day 23 ("Why This Score?") |
| VIX Stale Data | ✅ | Day 42 |
| Validation Low Scores | ✅ | Day 42 (tolerances) |
| Recommendation Card Alert Price | ✅ | Day 46 (Issue #0 - used resistance instead of support) |

---

## IN PROGRESS / PENDING VALIDATION

### Backtest Status (Day 55-56)
| Gate | Description | Status |
|------|-------------|--------|
| G1 | Holistic 3-Layer Backtest (60 tickers) | ✅ COMPLETE (Day 55) |
| G2 | Walk-Forward Validation (IS vs OOS) | ✅ COMPLETE (Day 55) |
| G3 | Exit Strategy Optimization | ✅ COMPLETE (Day 55) |
| G4 | Bear Market Regime Filter | ✅ VALIDATED (Day 57) — bear WR 55.6%→71.4% |
| G5 | Frontend-Backend Threshold Sync | ✅ COMPLETE (Day 56) |
| G6 | Quick & Position Period Backtest | ✅ COMPLETE (Day 57) — walk-forward validated |
| G7 | Full System Coherence Audit | ✅ COMPLETE (Day 57) — 71 params, 96% coherence |
| G8 | 4-Layer Deep Coherence Audit | ✅ COMPLETE (Day 61) — 87 fields, 89% coherence, 9 bugs fixed |
| G9 | Comprehensive Module Audit (Day 64) | ✅ COMPLETE (Day 64) — 4 rounds, 18 bugs fixed, pattern/ATR/stop/categorical |

**Test Command:** `python backend/backtest/backtest_holistic.py --configs C --walk-forward`

---

## COMPLETE — Universal Principles Evolution (Day 69-70)

**Source:** 4-LLM audit synthesis (`docs/research/UNIVERSAL_PRINCIPLES_SYNTHESIS.md`)
**Plan:** `docs/research/UNIVERSAL_PRINCIPLES_IMPLEMENTATION_PLAN.md`
**Principle:** ~85% code survives. Surgical changes only. One file, test, validate.

| Tier | Change | Files | Status |
|------|--------|-------|--------|
| 0A | Remove "3.2x" hallucinated MTF claim | support_resistance.py | ✅ Day 69 |
| 0B | VCP volume dry-up check | pattern_detection.py | ✅ Day 69 |
| 0C | TT 25%→30% above 52w low | Already correct (no change) | ✅ Day 69 |
| 0D | RS threshold backtest (1.0 vs 1.1 vs 1.2) | Validated 1.0 optimal | ✅ Day 69 |
| 0E-F | RRG normalization + momentum center | backend.py (docs only) | ✅ Day 69 |
| 0G | F&G neutral zone narrowing (35-60→40-55) | categoricalAssessment.js | ✅ Day 69 |
| 1A | ATR stops primary, 5% as cap | trade_simulator.py, riskRewardCalc.js | ✅ Day 69 |
| 1B | Equal-weight principle (docs + code) | GOLDEN_RULES.md, categorical_engine.py, categoricalAssessment.js | ✅ Day 69 |
| 1C | Parameter stability test script | parameter_stability.py (NEW) | ✅ Day 69 |
| 2A | VIX-based position sizing | positionSizing.js, trade_simulator.py, App.jsx | ✅ Day 70 |
| 2B | Blend 3 momentum lookbacks (informational) | rsCalculator.js, scoringEngine.js, categorical_engine.py, backtest_holistic.py | ✅ Day 70 |
| 3A | Mean-reversion engine RSI(2) | mean_reversion.py (NEW), mr_simulator.py (NEW), backend.py, api.js | ✅ Day 70 |
| 3B | MR frontend display | MRSignalCard.jsx (NEW), App.jsx | ✅ Day 70 |

**Key findings during implementation:**
- Blended RS (2B) **degrades** backtest metrics (PF 1.90→1.51, Sharpe 1.17→0.68). Kept as informational only. rs52Week remains verdict driver.
- Parameter stability (1C): rsi_low fragile at 55 (PF 0.83), stop_atr_multiple fragile at 1.5x (PF 0.98). Validates current parameter choices.
- RS threshold (0D): 1.0 optimal (5 trades, 80% WR, PF 2.18). 1.2 breaks (3 trades, 33% WR, PF 0.50). **[Day 78: this is the threshold now shared by both full view and simple checklist — see resolution below.]**

---

## COMPLETE — Price Structure Card Phase 1 (Day 72 — v4.33)

**Purpose:** Replace subjective TradingView chart-reading with structured narrative (S/R levels + touch counts + watch items). Zero impact on verdict/scoring.

| Component | File | Status |
|-----------|------|--------|
| Backend: expose levelScores | `backend.py` (+1 line in `/api/sr/<ticker>`) | ✅ Day 72 |
| Narrative utility | `frontend/src/utils/priceStructureNarrative.js` (165 lines) | ✅ Day 72 |
| Card component | `frontend/src/components/PriceStructureCard.jsx` (110 lines) | ✅ Day 72 |
| Design spec + self-audit | `docs/claude/design/PRICE_STRUCTURE_CARD_SPEC.md` (v2) | ✅ Day 72 |

**Key design decisions:** ATR-relative proximity (2x ATR), 12-rule priority tree, Wilder RSI thresholds, frontend generation (follows `categoricalAssessment.js` pattern). Tier 2, teal-400, collapsed by default.

**Phase 2 (deferred):** HH/HL/LH/LL market structure engine using existing `find_pivot_points()`.
**Phase 3 (deferred):** Visual chart via lightweight-charts.

---

## COMPLETE — Gate 5: Combined Momentum + MR Backtest (Day 75) — ⚠️ HINDSIGHT-UNIVERSE, see Day 79 below

**Script:** `backend/backtest/gate5_combined.py`
**Run:** 60 tickers (hand-picked), 5 years (2021–2026)

| System | Trades | Win Rate | Profit Factor |
|--------|--------|----------|---------------|
| MR | 1,968 | 63.4% | 1.27 |
| Momentum proxy | 968 | 52.2% | 1.34 |

**Overlap:** 1.9% (negligible — systems fire on opposite conditions)
**P&L correlation:** 0.274 (genuinely independent)
**Verdict at the time: PASS.** Run both with 50/50 capital split.

**⚠️ Day 79 update: this verdict does NOT hold on an unbiased universe.** MR's PF collapses to 0.99 (net losing) when re-tested on a random 400-ticker sample instead of the hand-picked 60. **Update (session 4): a one-time liquidity restriction (price>$10, 20d ADV>$25M) recovered PF 1.16** — see below. Still not statistically confirmed by the robust test; requires live paper-trading before any capital allocation.

---

## COMPLETE — Survivorship-Free Re-Validation (Day 79 — Fable Remediation Phase 4)

**Script:** `backend/backtest/backtest_survivorship_free.py`
**Doc:** `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY79.md` (full analysis)
**Run:** 400 tickers, randomly sampled (seed=42) from SimFin's full 3,788-ticker US coverage — no hand-picking. Same 2020–2025 period. 140/400 (35%) had no usable data (mostly delisted) — honest residual survivorship, not zero, as expected.

**These are now the canonical headline numbers** (the Day 55/75 figures above are hindsight-universe and kept for history only):

| System | Trades | Win Rate | Profit Factor | Sharpe | Significant? |
|--------|--------|----------|----------------|--------|--------------|
| **Config C (momentum)** | 114 | 49.12% | **1.40** (was 1.61) | 0.52 (was 0.85) | No — block bootstrap p=0.094 |
| **MR, unrestricted universe** | 6,151 | 53.03% | 0.99 (was 1.23 net) | −0.10 | No — p=0.518, net losing |
| **MR, liquidity-restricted (session 4)** | 3,210 | 57.35% | **1.16** | **1.30** | No — block bootstrap p=0.064 (close, not confirmed) |

**MR verdict updated (session 4):** the original MR entry had no dollar-volume liquidity gate at all (only price>$5) — a legitimate, principled, ONE-TIME re-test (price>$10, 20d ADV>$25M — pre-committed before seeing the result, not a performance-chasing re-tune) recovered a positive, Sharpe-1.3 result. Still not confirmed by the robust significance test, and fixed-risk drawdown is high (78%). **Current status: same tier as momentum — real but modest, requires live paper-trading confirmation (100+ trades, raised from 50 Day 92) before capital allocation.** No further MR backtest iteration; see `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY79.md` addendum for full detail.

**Verdict:**
- **Momentum (Config C):** edge survives directionally (PF > 1, positive Sharpe) but is NOT yet statistically distinguishable from chance at only 114 trades. Consistent with the Fable review's estimate of "honest live PF ~1.1–1.3" — proceed to paper trading per the pre-registered plan; that live test is the real confirmation, not this backtest.
- **MR:** unrestricted result was a clean null (PF 0.99, 6,151 trades). A one-time, pre-committed liquidity restriction (session 4 — see table above) recovered PF 1.16, Sharpe 1.30 — real but modest, same tier as momentum. **Not yet statistically confirmed** (block bootstrap p=0.064) and fixed-risk drawdown is high (78%). Treat identically to momentum: paper trade first, no capital allocation until 50+ live trades clear the pre-registered bar.
- **Per Golden Rule 18/19 and this plan's own instruction: no further re-tuning of either system's thresholds.** The MR liquidity change was the one allowed re-test, pre-committed before the result was known — not a repeatable pattern for future disappointing numbers.

---

## COMPLETE — Value Investing Tab Phase 1 (Day 75 — v4.34)

**Purpose:** Standalone value lens (Buffett/Graham/Lynch/Damodaran). Zero impact on swing verdict.

| Component | File | Status |
|-----------|------|--------|
| Backend endpoint | `backend/backend.py` — `/api/value/<ticker>` | ✅ Day 75 |
| API service | `frontend/src/services/api.js` — `fetchValueData()` | ✅ Day 75 |
| Tab component | `frontend/src/components/ValueTab.jsx` | ✅ Day 75 |
| Tab wiring | `frontend/src/App.jsx` — 💎 Value tab | ✅ Day 75 |
| Design spec | `docs/claude/design/VALUE_TAB_SPEC.md` | ✅ Day 75 |

**Metrics (Phase 1):** ROIC, ROE (DuPont leverage flag), Graham Number, P/E, PEG/PEGY, FCF yield.
**Phase 2 (deferred):** AV earnings history, interest coverage, EV/EBIT, ROE 5yr median.
**Phase 3 (deferred):** DCF Lite + Margin of Safety.

---

## COMPLETE — Price Structure Card Behavioral Test (Day 75 — v4.35)

**5/5 tickers passed.** Two bugs found and fixed in `priceStructureNarrative.js`:
1. ATH breakout rule now requires TT >= 5 (was firing on any no-resistance case)
2. RSI overbought watch item (Priority 6) added — fires when RSI > 70 and not near support

## COMPLETE — N1 + N2 + Flip Default View (Day 75 — v4.35)

| Item | Change | File |
|------|--------|------|
| N1: Two-price entry labels | Primary Entry (white) + Averaging Entry (blue) in both Trade Setup cards | `App.jsx` |
| N2: Nirmal watchlist preset | "👁 Nirmal's Watchlist" at top of Scan dropdown — 20 tickers, parallel cached SR fetches | `App.jsx` |
| Flip default view | `analysisView` default `'full'` → `'simple'` — simple checklist shown first | `App.jsx` |

---

## COMPLETE — UI Code Quality Fix Plan (Day 82–83)

**Source:** 3 parallel Fable-model audits (Analyze page Full Analysis cards, Scan Market tab, Tradier API evaluation), Day 82. Plan: `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` (now historical/reference — all tasks done, each with its own verification note).

| Group | Result |
|-------|--------|
| A — 6 real bugs | Scan tab/paper-trading candidate-set divergence (an `order_by()` override bug) fixed; Trade Setup Card's negative-stop-price bug fixed; Price Structure Card's dead "pattern forming" watch item fixed; 3 inconsistent liquidity thresholds unified into `liquidityThresholds.js`; Nirmal watchlist's silent-failure bug fixed; MR Signal Card's stale condition labels fixed. |
| B — 6 DRY violations | Pattern Detection Card + Categorical Assessment tiles both de-duplicated into shared components (`PatternMiniCard.jsx`, `AssessmentTile.jsx`); the legacy 0.011-correlation `determineVerdict()` function deleted entirely (traced reachability first — confirmed its only consumer was dead code); RS Card's fake "percentile" relabeled; a dormant Canadian-ticker bug fixed in `live_signals.py`. |
| C — Dead code | ~7 unused functions/exports and ~37 debug `console.log` lines removed. |
| D — New capability | `backend/providers/tradier_provider.py` — a 3rd-tier OHLCV/quote fallback, verified with forced-failover tests (no real credentials touched). Reliability-only; no options/fundamentals scope creep (those belong to OptionsIQ / don't close STA's real gaps, per the Day 82 evaluation). |
| E — Polish | Breakout Status card gained a loading skeleton and now surfaces `breakoutLevel`/`warnings` (previously silently dropped); 2 stale-response-race bugs fixed (ticker search, Scan tab rescans); a footer note added for the Scan tab's 20-row breakout-badge cap. |

**Verification discipline:** every fix was checked live — either via Playwright against the running app (real tickers, zero console errors each time) or direct provider/API calls (e.g. the Tradier forced-failover test). Two commits: `c48d16d8` (Group A + B1), `b77e06ff` (Groups B2–B6, C, D1, E1–E4). Backend v2.36 → v2.39 across the arc.

---

## COMPLETE — Master Framework Watchlist (Day 85-86)

**Source:** User-requested Day 85 — a personalized screener sourced from the
user's Notion "Master Investment Framework Hub" (4 curated frameworks: AI
Supply Chain, CanGem, STRATUM, QUBIT). Full scope + verification writeup:
`docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md`.

| Component | Result |
|---|---|
| Ticker list | Read all 4 Notion frameworks via MCP, deduplicated, applied an "established names only" filter (dropped QUBIT entirely — self-labeled all-Stage-0-1 — and STRATUM's speculative raw-material tier), dropped 3 ASX/LSE tickers STA's scanner doesn't support. 77 scoped → **76 shipped** after exhaustive verification dropped 1 (`FLT.V`, no data in any provider). |
| Frontend | `MASTER_FRAMEWORK_WATCHLIST` array + new "🏛️ Master Framework Watchlist" Scan tab dropdown option, same pattern as the existing Nirmal watchlist. `fetchWatchlistCandidates()` extracted as a shared helper so both watchlists use one implementation instead of copy-pasted logic. |
| Verification | All 77 originally-scoped tickers checked against the live backend (not a spot-check) — caught and fixed 3 Canadian dual-class ticker format bugs (`GIB.A`→`GIB-A.TO`, `TECK.B.TO`→`TECK-B.TO`, `BBD.B.TO`→`BBD-B.TO`) before they could ship as silently-broken entries. |
| Sync model | Manual refresh — no live Notion calls during scans. Re-pull from Notion and update the array whenever the user's Notion pages change (their own cadence is weekly at most). |
| **Day 86 follow-up** | User's first live test found Name/Sector/Change/Volume/Market Cap all showing N/A. Volume and Change % were free to add (`/api/sr/<ticker>` already fetches the OHLCV needed — see `API_CONTRACTS_DAY86.md`), fixed and verified live for both this watchlist and Nirmal's. Name/Market Cap remain N/A by explicit user choice — they'd need a separate fundamentals call per ticker. |

---

## ACTIVE PRIORITY ORDER (Day 92 updated — forward-testing accumulation is the sole priority, all others parked)

| # | Item | Why | Effort |
|---|------|-----|--------|
| 1 | **Let paper trading accumulate** | SOLE FOCUS (Day 92 — user explicitly holds all other priorities below this until the bar clears) — automated engine (`backend/paper_trading/`) built and live Day 81, running unattended daily via launchd. Both momentum (PF 1.40) and MR (PF 1.16, post liquidity re-test) still need **100 live trades each** before capital allocation (raised from 50, Day 92 — see `PAPER_TRADING_PREREGISTRATION.md` Change Log). As of Day 92: momentum 0 closed, MR 5 closed — both far from either bar. Check in via the Forward Test tab's status panel (now with an expandable per-ticker table, Day 92) or `daily_job.py --report`. **Day 111 update: first two tracks crossed the bar, with sharply different results under scrutiny.** MR (broad): 138 closed, 79.71% WR, PF 3.0021 — genuinely confirmed, stress-tested via cluster removal (PF held at 2.24 excluding its largest 3-day cluster, WR *rose* to 80%). Momentum Path B: 117 closed, PF 1.2293 — clears the numeric bar on paper, but 66.7% of its entire sample (78 of 117 trades) entered in one 4-day window (Aug 3-7); excluding just those 4 days leaves PF 0.72 (net losing). **Not being treated as a clean confirmation** — see `KNOWN_ISSUES_DAY111.md` for the full finding and the still-open judgment call on what this means for the track going forward. | Ongoing (no build work) |
| 2 | **Decide fundamentals mitigation** | Task 3.2 measured 40.0% live↔backtest disagreement — user decision pending: align live-to-SimFin or backtest-to-TTM. Now also affects the automated engine's momentum leg. | Decision + implementation |
| 3 | **Confirm SimFin key rotation** | A possible new key was shared in conversation Day 79 but never confirmed as intentional or applied. | Small |
| 4 | **N3: Gap-fill detection — needs a design session first** | No spec exists yet (Day 87 finding) — only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`. Design, then build. | Design session, then Medium |
| 5 | **Value Tab Phase 2 — needs a batch-prefetch design session first** | Spec (`VALUE_TAB_SPEC.md`) requires nightly batch-prefetch infra (watchlist + schedule) for AlphaVantage's ~8-tickers/day budget; explicitly gated to build only post-freeze. On-demand fetching (Phase 1's pattern) would contradict the documented design. | Design session, then Low-Medium |
| 6 | **Build `/ibkr-scan` skill** | Research done (Day 77). Verify 52W High Proximity in IBKR first. | 1 session |
| 7 | **Price Structure Phase 3** | Visual chart via lightweight-charts (Phases 1-2 done as of Day 87). | Medium |
| 8 | **Canadian Analyze page** | Medium bug, data source redesign needed | High |
| 9 | ~~Scan tab batch breakout badges: distinguish NOT_READY from a failed fetch~~ | **DONE (Day 106)** — see Golden Rule 44. Four distinct outcomes (never checked / requested-no-result / data error / genuine NOT_READY) now render as four distinct honest labels instead of one collapsed "—". | Done |
| 10 | **Session 28 audit — remaining lower-priority findings** | Top-4 fixed Day 91 (see below). **Day 108 update:** ROE "Buffett/Damodaran" attribution question now resolved (Claim Audit found it MISLEADING, not fabricated — the code's "ChatGPT research validated" comment is actually the more accurate label; needs a UI wording decision, see `KNOWN_ISSUES_DAY108.md`). Validate/Data Sources "shows healthy without probing" finding now split: `/api/health`'s hardcoded-always-healthy status is fixed; the per-ticker provenance panel still can't distinguish "never checked" from "just failed" — the real surviving core of this finding, now tracked as its own HIGH-severity item. Remaining, unchanged: Sectors tab's `.toFixed(3)` false precision (the Rank #1 CTA/gate-bypass part fixed Day 92); Forward Testing's momentum-path trades store identical net/gross P&L (fee accounting not differentiated) and per-position fetch failures are silently dropped. Plus the audit's own "polish" list. | Small-Medium, batchable |
| 11 | ~~Volume-confirmation not in the core verdict~~ **SHIPPED Day 111.** | Found in a post-Day-91 first-principles review. Day 107's first design (`Config F`, a hard 1.5x-volume backtest gate) cut trades 75→5 — too strict, same failure mode Fundamentals/R:R/Regime already hit and were fixed by moving to Info instead of gating. **Day 111: same fix applied, live.** A dedicated Opus planning pass found the original plan's premise was wrong on two counts — RVOL wasn't "already on a Sizing Inputs grid / Technical Read card" (those exist only in the unimplemented redesign mockup) and the "shared 1.5x threshold" was actually 7 unlinked literal copies, no drift but no real sharing either. Corrected and shipped on the **live** page instead: a new note on the live Trade Setup card (`App.jsx:1808-1823`), reusing the live RVOL computation (`backend.py:1634-1637`) via a new shared module (`frontend/src/utils/volumeThresholds.js`), independent of the pre-existing chip's `tradeViability` gating so it renders where the chip doesn't. Zero backend changes, not a Golden Rule 18/20 re-tune. Verified live in-browser, 2 tickers, plus a zero-behavior-change regression check on Price Structure's watch items. See `KNOWN_ISSUES_DAY110.md` for full detail incl. the 7-copies finding (logged, not fixed — backend, out of scope). **Companion item, closed not deferred:** absolute/dual momentum (Antonacci) — `Config G` tested clean but only excluded 1 of 75 trades (the RS pipeline already mostly selects for it as a side effect) — decided Day 111 not to pursue, correct but pointless. `mean_reversion.py`'s ADX docstring/code mismatch remains open, unrelated doc fix. | Done |
| 12 | **RESOLVED via Path B parallel experiment (Day 95) — see `PAPER_TRADING_PREREGISTRATION.md` §8b.** Originally found via a live TradingView-screener deep dive: momentum's live R:R check (`compute_entry_levels()`'s flat+8%/ATR-clamped-stop proxy) rejected 81% of Config-C-qualifying candidates, 45% hitting an exact 0.80 ceiling. An early fix attempt (widen the stop clamp floor to entry×0.85) was tested via a quick backtest sanity check and proved **directionally backwards** — wider stop = bigger risk = worse R:R, confirmed empirically (worse PF/Sharpe/drawdown on identical trades). Investigating why the trade set didn't change at all led to the real finding: `backtest_holistic.py`'s actual Config C entry gate has never used `compute_entry_levels()` at all — it computes R:R from real support/resistance levels (`risk=price-nearest_support`, `reward=nearest_resistance-price`), with the flat/ATR formula being exit-management logic only. `live_signals.py` has substituted the wrong piece of logic as its entry gate since Day 81 — a live/backtest divergence in the same bug class as Golden Rule 19. Built **Path B**: a parallel forward-test variant using the real S&R-based gate (`check_sr_gate()`), tracked under its own `variant='B_revised_rr'` ledger tag, same candidate pool as Path A, own 100-trade bar, zero impact on Path A's frozen count. Not deferred — this is a live/backtest coherence bug fix (tracked as a new experiment, not a threshold re-tune), so it didn't need to wait for the freeze to lift. Ongoing: let Path B accumulate alongside Path A and compare. | Done (Day 95) — ongoing accumulation, not a backlog item |
| 13 | **IBKR real paper-trading execution — planned, parked pending user's additional research/review.** Full phased design doc: `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md` (Day 96). Goal: execute Path B's momentum signals as real bracket orders against the user's IBKR paper-trading account (via the Client Portal REST API), so fills come from IBKR's own paper engine — realistic slippage against live market data — instead of the internal simulator. Feasibility (gateway setup, auth flow, order-placement endpoints) and the CIRO Rule 3200 regulatory question (researched directly against CIRO's own published guidance — governs real orders to a real marketplace, doesn't appear to have anything to regulate in a pure paper account) are both resolved in the design doc. Hard constraint locked in: every order-placing code path must assert the target account ID starts with `DU` (paper-account prefix) before calling any order endpoint, no bypass. 4-phase plan (connectivity+one manual test order → wire into real signals, still manual → ledger/reporting integration → operational hardening, honest about the no-unattended-2FA gap). **Not started** — user wants to do more research/review before Phase 1 begins; the design doc's own "Open items" section notes confirming the CIRO paper-account question directly with IBKR support as the one loose end worth closing first. | Design done; 4-phase build once resumed |
| 14 | **HUB-65 curated-universe Mean-Reversion forward-test — DONE (Day 98), now accumulating toward its own 100-trade bar.** Same unchanged MR engine (Connors RSI(2)), run against a 65-ticker curated watchlist (semis, uranium/nuclear, fintech, China-EV, thematic ETFs — sourced from a sibling project's own screener research) instead of the broad ~150-ticker dynamic TradingView scan. One-shot backtest first (`backend/backtest/backtest_hub_mr.py`): 1,940 trades, PF 1.2574, Sharpe 1.5278, block-bootstrap p=0.0311, explicitly caveated as selection-biased. Forward-test tagged `variant='mr_hub65'` (reusing the ledger's `variant` column for a second, orthogonal meaning — universe, not gate — see Golden Rule 38), fully isolated from the broad MR track's count and cooldowns. Surfaced in `/api/paper-trading/status`'s new `mrHub` block and a distinctly-badged (teal, "Curated-65 Universe") Forward Test tab card, plus a new "HUB-65 Watchlist" Scan tab preset. Not a freeze exception — same category as Path B (Priority #12). | Done (Day 98) — ongoing accumulation, own 100-trade bar |
| 15 | **Scheduled/proactive breakout-alert watcher — idea only, not started (Day 100).** Both `/breakout-watch` (Claude Code skill) and the Scan tab's badge column already run the 8-state breakout engine (`breakout_detection.py`, `/api/breakout/batch`) against any ticker list on demand — the user's own list included, not just a fixed watchlist. What's missing: nothing runs on a schedule or notifies without being asked (the skill's own file states this explicitly: "no push notifications, no cron, no auto-trading"). User asked to mark this for the roadmap rather than build it now — would need its own design pass (delivery mechanism, schedule cadence, what "watchlist" means for this vs. the existing curated ones) before any implementation, same discipline as every other parked item below Priority #1. | Idea only — needs a design session before any build |
| 17 | **Analyze Page Redesign — design phase complete (Day 109), mockup built (Day 110), implementation not started.** Full decision record at `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`, interactive mockup at `docs/claude/design/mockups/analyze_page_redesign_mockup.html`: 17 locked decisions on which Analyze-page signals stay mechanical (Technical structure) vs. become informational (Fundamentals as a red-flag screen, Risk:Reward, position sizing), plus a default-view change (Simple→Full) and a full phased implementation plan with a freeze-safety audit confirming zero impact on `backend/support_resistance.py`, `categorical_engine.py`, or any of the 4 live forward-test tracks. A real bug was found and documented (not yet fixed): the Momentum entry panel's "half" position-size label has been hardcoded with zero computation behind it since Day 39. **Day 110 revision:** Market Regime no longer gets a hard gate — reversed to informational, same treatment as everything else, after the user directly challenged the hard-gate framing; kept expanded-by-default (not enforced) since it's portfolio-wide, not single-stock. The published mockup was **not** updated to match this reversal — still shows the pre-reversal "stand-down" copy, a known inconsistency to fix before implementation starts. **Not started** — build only when explicitly requested; this is freeze-independent display-layer work, same category as Days 93/101/103/105/106/108, but still gated behind Priority #1 like everything else on this list. | Design + mockup done; 6-phase build once resumed |
| 16 | **Day 108 full-audit parked findings — need a decision or bigger scope, not urgent.** Full detail: `docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md`, `KNOWN_ISSUES_DAY108.md`. Highest-priority: per-ticker provenance can't distinguish "never checked" from "just failed" (HIGH — needs new failure-tracking state). Also: VIX position-sizing never wired into the automated engine (verified zero impact on current live-track stats, ties into the parked IBKR plan); pivot S&R selects extreme not nearest levels (baked into both backtest and live Path B equally, not a divergence — revisit post-freeze); `ContextTab.jsx`'s bypass of the shared `api.js` fetch layer (needs `api.js`'s dead Context functions fixed to throw-not-swallow first); Value tab's "Buffett" ROE wording and FCF Yield's pass/fail badge (both need a copy/design decision); Settings' 2-5% risk slider vs. the app's own documented 2% Van Tharp ceiling; PMI/Business-Cycle cards missing the Day-91 date-alignment fix (same class, 2 more call sites); a latent `backtest_adapter.py` short-span logic gap (not currently triggered). | Small-Medium each, batchable, none urgent |

**Done as of Day 87:** Breakout Enhancement Plan (all phases), N4 Market Phase Synthesis, Price Structure Card Phase 2 — see their own COMPLETE sections above.
**Done as of Day 88:** Paper-trading ledger surfaced in the UI (Forward Test tab) with a manual trigger button — agreed as the one scoped exception to the freeze (directly aids the gate itself, not general product work).
**Done as of Day 91:** Session 28 audit's top-4 findings — Scan tab "Minervini" mislabel, Sectors tab false "100=parity"/data-source claims, Context tab CPI (real date-alignment bug, not caching) + PMI proxy relabel, paper-trading exit-rule integrity (replay now anchors to stored entry values). See Golden Rules 26-27.
**Done as of Day 92:** Paper-trading zombie-signal bug fixed (Golden Rule 28) + per-position ticker/entry/exit detail surfaced in the Forward Test tab. Confirmation bar raised 50→100 trades/system; forward-testing accumulation now the sole priority (Priority #1 below) — Priorities #2-11 explicitly parked until it clears.
**Done as of Day 93:** Sectors/Context tab audit — done independent of the freeze (pure UI/display work, no verdict/trading logic touched). Fixed the mid-cap-blind Cap Size banner, a bar-color/label contradiction, a full beginner-focused Sectors tab redesign, a real Day-91-regression composite bug and a Seasonal Regime text contradiction on the Context tab, and built a new Sectors↔Context macro-alignment connection plus a Market-Phase↔Macro-Regime reconciliation on the Context tab itself. Priority #10's "Rank #1 CTA" sub-item is now resolved (was stale-listed as open, corrected).
**Done as of Day 101:** "Sub-Industry Watch" — 21 sub-industry theme-cluster proxy ETFs on the Sectors tab, one level below the 11 broad GICS sectors. See its own COMPLETE section below. Same freeze-independent category as Day 93 (pure display/analysis).
**Done as of Day 103:** SRPS (Sector Rotation Pullback System) investigated end-to-end as a potential 5th automated forward-test track — failed its own pre-registered Gate 1 backtest, not built live. Pivoted to a discretionary Sectors-tab screener instead. See its own COMPLETE section below. Freeze-independent (never touched the 4 live tracks).
**Done as of Day 105:** Sub-Sector Pullback Screener — the Day 103 SRPS discretionary screener extended to the 21 Sub-Industry Watch clusters, at the user's explicit request. Also fixed a real Sectors-tab staleness bug (Golden Rule 43). See its own COMPLETE section below. Freeze-independent (never touched the 4 live tracks).
**Done as of Day 106:** Priority #9 (Scan tab breakout-badge dash ambiguity) — fixed, see Golden Rule 44. Also built the new Scan tab "STA Verdict" on-demand column (Retest Entry/Building Base rows only) and corrected the app's self-description (header tagline, empty-state caption, README opening paragraph) from an overclaimed "Minervini system" to the actual multi-engine picture. Freeze-independent.
**Done as of Day 107:** Built the "STA vs. 100 Years of Trading Principles" Artifact (3-source cross-checked research, 3-pass verified code audit) and ran a backtest-only research spike on its 2 findings (Priority #11's volume-confirmation and dual-momentum items) — neither shows a credible edge yet, both remain parked with real data behind the "not yet." New Golden Rules 45-46 (SimFin universe drift, cross-provider split-adjustment checks). No live app code touched, no version bump.
**Done as of Day 110:** Interactive mockup of the Analyze Page Redesign built and published (`docs/claude/design/mockups/analyze_page_redesign_mockup.html`), closing decision-doc §9's "no visual mockup" open item. Live forward-test clustering check across all 4 tracks found real single-day entry concentration in every one, most notably MR HUB-65 (48.5% of its sample on one semiconductor-heavy day, underperforming rather than inflating the track's number) — no code changed, informational finding only. Market Regime's Day 109 hard-gate decision reversed to informational after direct user pushback; decision doc updated, mockup not yet updated to match. New Golden Rule 52 (verify a claimed edit actually happened before treating it as done). Zero application code touched, no version bump.
**Done as of Day 109:** Analyze Page Redesign — design phase only. 17 decisions locked via an item-by-item Q&A process (new Golden Rule 49) plus a dedicated Opus validation pass (new Golden Rules 50-51, 4 real corrections caught). Full record at `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`. Zero application code touched — see Priority #17 above.
**Done as of Day 108:** Full 10-group system audit (all 9 tabs + core verdict engine + FWD-testing engine + providers package) — 27 items checked, 15 real bugs fixed (most severe: MTF Confluence's fabricated-dates bug, CRITICAL), 8 parked (Priority #16 above), 4 clean. Resolved the long-uncertain Canadian Analyze page question (confirmed fully working). New Golden Rules 47-48. v4.58→v4.59. Zero findings touched any of the 4 live tracks' frozen logic.

---

## COMPLETE — Sub-Sector Pullback Screener + Sectors-Tab Staleness Fix (Day 105)

**Source:** User request, after citing positive discretionary experience with the Day 103 sector-level Pullback Screener — "I found good results with sector screener results so far." Applied the PERSONA lens once before building (the mechanical rule set already failed its Gate 1 backtest at the broad-sector level, and the sub-industry universe has never been separately tested) — proceeded since this stays informational-only, same category as its sibling.

**Two judgment calls confirmed with the user before building** (bundled via `AskUserQuestion`, both recommended options taken):
- Overlapping clusters (Communication Services, Energy — thin proxies of sectors the broad screener already covers): included anyway for completeness, since their curated ticker lists surface a few names the broad TradingView query doesn't.
- Proxy-only clusters (Gold Miners/GDX, Biotech/XBI — the proxy ETF IS the theme, no underlying stock list): screened directly on the proxy ETF itself rather than silently skipped.

| Component | File | Result |
|---|---|---|
| Shared SRPS helpers | `backend/backend.py` | Extracted `_srps_true_rs()`/`_srps_evaluate_candidate()` from the existing sector-level screener's inline logic (Golden Rule 21) — verified behavior-preserving via live curl comparison before/after, not just code review. |
| New endpoint | `backend/backend.py` — `GET /api/sectors/sub-industry-pullback-screen` | Reuses each cluster's own hand-curated `tickers` list from `sub_industry_clusters.py` as candidate sourcing (previously informational-only — first real use). Capped at `MAX_CLUSTERS_PER_REQUEST=8` and a new per-cluster `LIVE_CANDIDATE_LIMIT=8` — a real Golden Rule 25/40 fan-out risk (Semis alone has 16 curated tickers) caught during the mandated three-pass review (Golden Rule 41) before shipping, not after. |
| Frontend | `frontend/src/components/SectorRotationTab.jsx`, `frontend/src/services/api.js` | New `SubIndustryPullbackScreenSection`, same collapsible/lazy-load pattern as its sector-level sibling. |

**Real bug found and fixed mid-session, not from the feature request itself:** the same three-pass review (Pass 2) surfaced a pre-existing gap in the *sector-level* screener — its `sectorsCappedFrom` field has been computed by the backend since Day 102 but the frontend never displayed it (Golden Rule 30 territory). Fixed alongside the new sub-industry version's equivalent field.

**Sectors-tab staleness fix, same session, from an unrelated user bug report:** "Refresh Session" correctly cleared the backend's `market_cache` but never told already-loaded frontend components (main sector state, both lazy-loaded sub-sections) to refetch — clicking it repeatedly showed identical numbers with no error. Fixed by threading a bump-able `refreshTrigger` prop from the button handler into every component holding independently-fetched sector data, plus a new scoped in-tab "🔄 Refresh" button (clears only sector-related cache via a new `POST /api/cache/clear?type=market` path, without Refresh Session's much larger blast radius). New **Golden Rule 43**.

**Cross-check against STA's own fuller engine (investigation, not a code change):** at the user's request, checked 3 live candidates the screeners produced (CGNX, GEV, RIVN) against the app's own Simple Checklist / Full Analysis. All 3 came back **"No Trade — avoid."** Found a real, generalizable structural gap: SRPS's target price is fixed at `entry + 2.5×risk` and never checks real chart resistance — STA's own Risk/Reward check (against actual support/resistance) came back at 0.48:1 and 0.27:1 for GEV/RIVN, nowhere near the screener's own implied 2.5:1. True of every candidate the screener will ever produce, not specific to these 3 tickers. Logged in `KNOWN_ISSUES_DAY105.md` and PERSONA.md's Feedback Log — not fixed (informational screen, not a live gate; a real fix would be a non-trivial rule change to SRPS's already-fixed, backtested-and-failed rule set).

**Verification discipline:** every fix was checked live, not just read — curl-verified the market-cache-only clear forces a real fresh fetch without touching OHLCV cache; browser-verified the Refresh button updates the tab and both sub-sections with zero console errors; curl-verified the sub-industry screener end-to-end (regime gate, cluster cap, per-cluster candidate cap, real candidates found); browser-verified both GEV and RIVN's Simple Checklist verdicts directly in the app rather than inferring them from raw API fields.

---

## COMPLETE — SRPS Investigation + Discretionary Screener (Day 103)

**Source:** User brought a fully-specified design doc (v1.2) for a new mechanical strategy — buy the strongest stocks in sectors that are just turning from Lagging to Improving, right as they pull back to their 21-day EMA, with an ATR/swing-low stop and a 2.5R target. Proposed as a potential 5th parallel forward-test track alongside Momentum Path A/B and MR broad/HUB-65.

**Gate 0 (signal frequency) — PASSED.** Built two prerequisites, both genuinely new: `backend/backtest/sector_quadrant_history.py` replays the sector quadrant classification for any historical date range (the live `/api/sectors/rotation` endpoint only ever computes *today's* quadrant — there was no historical replay path anywhere in the codebase before this). `scan_queries.py` gained `build_sector_query()` + `rank_candidates_by_rs()` — live sector-filtered, true-RS-ranked candidate sourcing. Found and fixed two real TradingView-taxonomy bugs while building the latter: Real Estate (XLRE) — TradingView's coarse `sector` field buckets every REIT under "Finance," fixed via the finer `industry` field; Communication Services (XLC) — no field-based fix exists at all (GOOGL/META/NFLX genuinely share TradingView's "Technology Services" bucket with real Technology names, no way to separate them by field value), fixed with a hand-curated 17-ticker override, live-verified against real S&P 500 membership (which also caught that 3 names drafted from memory — EA, IPG, MTCH — were no longer valid: EA went private, IPG merged into Omnicom, MTCH left the index). `srps_gate0_signal_count.py` combined both into the actual Gate 0 replay: ~143 qualifying signal-days/year over the trailing 12 months, comfortably clearing the design's own 60/year minimum.

**Gate 1 (full backtest) — FAILED.** Built `backend/backtest/srps_gate1_backtest.py`: a genuine day-by-day portfolio event loop over the Day-79 survivorship-free 400-ticker universe, 2020-2025, enforcing Rules 1-5 and a real max-6-concurrent-position cap. This is architecturally new — every existing backtest in this project (momentum, MR, HUB-65) runs each ticker fully independently with no cross-ticker concurrency limit; SRPS's design explicitly required one. Three real bugs found and fixed during the build, all via the newly-adopted three-pass review (Golden Rule 41):
- **Rule 3/Rule 5 whipsaw contradiction.** Rule 3 admits entries up to 3% below the 21-EMA; Rule 5's trailing exit fires on any close below the 21-EMA — so a large share of entries were already at or past their own exit trigger on day 1 (confirmed live: one ticker entered and exited within 1 day, three separate times, each a real loss). Fixed per explicit user choice with a 5-bar trail-activation delay, matching this project's own pre-existing, independently-motivated EMA-trail convention (`trade_simulator.py`'s Standard/Position configs already do this) — not a threshold tuned to chase a better number (Golden Rule 20's test).
- **A universe-construction bias that reintroduced survivorship bias.** Sector-tagging (via SimFin's company/industry data) ran *before* checking OHLCV availability, silently dropping any ticker with no SimFin sector classification — which turned out to include real historical bankruptcies with usable price history (ITT Educational Services, BurgerFi, Alta Mesa Holdings) that a survivorship-free backtest exists specifically to capture. Fixed by reordering: download price history for the full random sample first, tag sector only for price-history survivors.
- **A near-zero stop-distance bug.** No minimum stop-distance floor meant one trade's stop rounded to near-zero, producing a 331,408 R-multiple that silently dominated the average. Fixed with `STOP_MIN_PCT` (new `backend/srps_constants.py`, shared by both backtest scripts and the live screener) — a data-integrity/execution-realism floor, not a re-tune of the strategy's own economic thresholds.

**Real, final result** (411 closed trades, both fixes applied): **34.1% win rate** (design requires >45%), **Profit Factor 1.177** (design requires >1.2, missed narrowly), expectancy +0.10R (requires >0.15R). Internally consistent with the design doc's own corrected v1.1 expectancy math — not a surprising or broken number, the mechanism working exactly as that math predicted, just with a real win rate short of the bar. Per the design's own explicit rule ("if any minimum threshold is not met, the system is not allocated capital"), SRPS does **not** get built as a live automated forward-test track. Sub-industry expansion (the design's own Phase 2) explicitly not pursued — Phase 1 never passed its own backtest, and the failure was about the entry/exit rules, not the universe, so a finer-grained universe wouldn't address it.

**Pivot — discretionary screener, built and shipped.** Same rule logic (Rules 1-4, no exit simulation needed for a screener) repurposed as `GET /api/sectors/pullback-screen` + a new collapsible "🎯 Sector Pullback Screener" section on the Sectors tab. Surfaces candidates matching the mechanical criteria with a permanent, prominent disclaimer that the backtest failed and this is not a signal — the user applies their own judgment (regime, news, catalysts) before acting. No ledger, no automated entry/exit, no forward-test count; same informational-only category as the MR Signal Card / Price Structure Card. A three-pass review of this endpoint (the first real run of new Golden Rule 41) found and fixed two further real issues: a timezone-normalization fix that was silently discarded before reaching the data it needed to fix, and an unbounded per-sector data-fetch loop capped after confirming live (via the same 12-month quadrant history) that 8-9 sectors being simultaneously Improving happens ~4x/year, not hypothetically.

**Also produced this session, while working on SRPS-adjacent code:**
- **New Golden Rule 41** — escalating three-pass review (each pass strictly more critical than the last, not three parallel checklist items), adopted from the Trading Intelligence Hub's Session 34 standing rule, explicitly superseding Rule 32's older fixed-lens version. Now the standing process for every future fix in this project.
- **A real Forward Test tab bug fix** (user-reported): the closed-trades table and its "Show tickers (N)" button both silently under-reported MR/HUB-65 (71/28 real closed trades, only 20 ever shown, no indication) — fixed with a visible truncation note, matching the Scan tab's own existing 20-row-cap precedent.
- **A Forward Test data investigation** (user-reported "I think it's off"): confirmed the display was correct; traced Path A's real win-rate drop to a correlated 4-trade cluster (2 REITs + the GP/LP units of the same pipeline company) — a live materialization of the already-known correlation-gap Known Issue, not a new bug.
- **A Sector Rotation data-sourcing review** (investigation only, not fixed): confirmed the original 11-sector endpoint still has no provider fallback (unlike its two newer siblings) and its frontend fetch function is still a whitelist reconstruction — the exact pattern that already caused one real bug. Logged as Known Issues, offered as a future fix, not started.

**Verification discipline:** every gate, every bug fix, and the live screener were run for real, not just read — Gate 0 and Gate 1 both executed against real historical data with real output inspected line-by-line for plausibility (not just "did it run"); the screener was hit live via curl and verified in-browser with zero console errors both before and after each fix.

---

## COMPLETE — Sub-Industry Watch (Day 101)

**Source:** User request, prompted by seeing the Trading Intelligence Hub's own separate standalone "Sub-Industry Watch" panel (built for the Hub's own sector/theme advisory tool, `trading-intelligence-hub/research/sector_advisory/`). Full detail: `docs/claude/versioned/API_CONTRACTS_DAY101.md`, `docs/claude/status/PROJECT_STATUS_DAY101_SHORT.md`.

Built natively into STA rather than depending on the Hub's copy, for two reasons: STA already has its own `TRADIER_ACCESS_TOKEN` and working `TradierProvider` (Day 82-83), so no cross-repo credential sharing was needed; and STA's own RS-ratio formula (static-midpoint-normalized) differs from the Hub's (indexed to the start of the window), so building it natively — reusing STA's own formula via a newly-extracted shared helper, `compute_rs_ratio_and_quadrant()` — avoids the "different normalization epoch" caveat the Hub's report has to carry for tickers that appear in both places (XLE, XLK, XLC, XLY).

| Component | File | Result |
|---|---|---|
| Shared RS-ratio/quadrant helper | `backend/backend.py` | Extracted from the existing 11-sector endpoint's inline calc — one formula, not two, per Golden Rule 21. Verified byte-identical for the 11 broad sectors before/after via `test_sector_rotation.py`. |
| 21-cluster proxy mapping | `backend/sub_industry_clusters.py` (new) | Transcribed from the Hub's own hand-curated, Tradier-verified `ticker_themes.py` (Semis/SMH, Memory-Storage/DRAM, AI Infra-Power/GRID, Nuclear-Uranium/URA, Critical Materials/COPX, Gold Miners/GDX, Biotech/XBI, Financials-Fintech/XLF, Crypto/WGMI, Software-SaaS/IGV, China Internet ADR/KWEB, EV-Autonomous/DRIV, Space-Emerging/UFO, Optical-Connectivity/XLK, Enterprise Tech/XLK, Communication Services/XLC, Defense/ITA, Physical AI-Robotics/BOTZ, Industrials-Water/PHO, Energy/XLE, High-beta mega/XLY — plus 1 informational no-proxy cluster, Past survivors/POET). |
| New endpoint | `backend/backend.py` — `GET /api/sectors/sub-industry` | Uses STA's existing multi-provider orchestrator (TwelveData→yfinance→Tradier) per ticker rather than a single yfinance batch call, since several proxies (e.g. DRAM, launched Apr 2026) aren't reliably on the earlier tiers. Cached per trading day, same convention as the existing endpoint. |
| New test | `backend/test_sub_industry_rotation.py` (new) | Same live-server, structural-invariant convention as `test_sector_rotation.py` (also adopted this session — see below). |
| Frontend | `frontend/src/components/SectorRotationTab.jsx`, `frontend/src/services/api.js` | New collapsible "🔬 Sub-Industry Watch" section, Tier-2 style, collapsed by default, lazy-loaded only on first expand — a slower ~22-ticker fetch that shouldn't tax every page load. |

**Real bug found and fixed mid-build, not from a symptom report:** the first live run failed on 13 of 21 clusters with "0 bars aligned with SPY." Root cause: calling 22 tickers in one request trips TwelveData's rate limiter partway through (Golden Rule 25 territory), and the yfinance fallback for the remaining tickers returns a tz-aware index while the already-cached SPY series (from an earlier TwelveData fetch) is tz-naive — `.index.intersection()` silently returns zero rows instead of erroring. The project's own Day 52 tz lesson, recurring in a new shape a single-provider batch call never exposed. Fixed by normalizing to tz-naive at the alignment boundary. New **Golden Rule 40**.

**Adopted alongside it:** `backend/test_sector_rotation.py` — a hub-side test-coverage handoff for the *existing* `/api/sectors/rotation` endpoint (found zero automated coverage there). Independently re-verified against the actual `backend.py` logic before adoption, not trusted on the Hub's "verified live" claim alone.

**Verification:** three review passes per Golden Rule 32 — (1) both test scripts + live browser check (all 21 clusters, DRAM's short-history caveat, zero console errors); (2) grepped for other callers of the extracted helper (none), then closed a real gap by browser-verifying the Analyze Stock page's sector badge, the one other real consumer of `/api/sectors/rotation`; (3) grepped for other consumers of `SECTOR_ETF_MAP`/`GICS_TO_ETF` (confined to the one function). No changes to the automated paper-trading engine or any frozen threshold — pure Sectors-tab display/analysis work, same freeze-independent category as Day 93.

---

## COMPLETE — Breakout Enhancement Plan Phases 2–3 (Day 81)

**Source:** `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Tasks 2.1/2.2/3.1.

| Component | File | Result |
|-----------|------|--------|
| Batch breakout endpoint | `backend/breakout_routes.py` (`/api/breakout/batch`) | Added inside `register_breakout_routes()`, reusing its existing OHLCV-fetch helpers — no `backend.py` changes needed. Hard-capped at 20 tickers/request. Partial results on per-ticker failure (no 500 on one bad ticker). |
| Scan tab badge column | `frontend/src/App.jsx`, `frontend/src/services/api.js` | New "Breakout" column, one batch call for the top 20 rows after results render. Verified in a real headless-Chromium session (Playwright installed locally, no project run-skill existed for this app) — 20/20 badges rendered with correct colors/labels/tooltips, zero console errors, screenshot-confirmed. |
| `/breakout-watch` skill | `.claude/commands/breakout-watch.md` | Buckets tickers by state, most-actionable first; `NOT_READY` summarized in one line, never treated as an error. Deliberately reuses the new batch endpoint (didn't exist when this plan was first written) instead of N individual calls. Verified end-to-end against the live backend. |

Only Phase 1 (the "near breakout" scan preset) remains of the entire Breakout Enhancement Plan — gated on explicit user approval per the plan's own gating table (small feature, mid-freeze).

**Update (Day 87): Phase 1 shipped — the entire Breakout Enhancement Plan is now complete.** New `strategy=breakout` scan option (`/api/scan/tradingview`): Stage-2 stocks within 8% of 52-week high, market cap ≥$2B, price >$10, RSI 50-70, ADX≥20, avg dollar volume ≥$5M. The 8%-from-high and dollar-volume filters are post-filters (`scan_queries.parse_candidates()`) since TradingView's `col()` doesn't support the needed arithmetic — the query fetches a wider net (300 candidates) first so the post-filter isn't starved. All 50 returned candidates verified exhaustively against every filter (not spot-checked). `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` is now historical/reference only. See `API_CONTRACTS_DAY87.md`.

---

## COMPLETE — N4: Market Phase Synthesis (Day 76 research, Day 87 build)

**Source:** Research done Day 76 (`docs/claude/status/archive/PROJECT_STATUS_DAY76_SHORT.md`) — RSP/SPY confirmed as the correct breadth proxy (`^SPXA200R` is dead on yfinance), 5-phase framework designed. Built Day 87.

New `backend/market_phase_engine.py` + `GET /api/market/phase`. Classifies current market-wide conditions into one of 5 phases (Bull Rally / Late Bull / Distribution / Correction / Recovery) via a transparent 3×3 grid — SPY trend bucket (UP/FLAT/DOWN, from 200SMA position + 20d % change) × VIX level bucket (CALM/ELEVATED/HIGH) — with breadth (RSP/SPY ratio 20d change) and sector leadership (Growth XLK/XLY/XLC vs Defensive XLU/XLP/XLV, 20d returns) shown as supporting evidence rather than additional classification gates. Purely informational — zero impact on verdict/scoring, same pattern as the Context tab's other engines. Displayed via new `MarketPhaseBanner.jsx` at the top of the Context tab, cached per trading day.

**Verified:** grid classification exhaustively unit-tested (all 9 SPY×VIX cells, the DOWN+CALM refinement rule, and boundary values). Live endpoint + caching confirmed. Full contract: `API_CONTRACTS_DAY87.md`.

---

## COMPLETE — Price Structure Card Phase 2 (Day 72 spec, Day 87 build)

**Source:** `docs/claude/design/PRICE_STRUCTURE_CARD_SPEC.md` §Phase 2.

New `backend/market_structure_engine.py`, wired into `/api/sr/<ticker>`'s `meta.marketStructure`. HH/HL/LH/LL pivot-sequence classification (Uptrend/Downtrend/Range/Transition), trend age (bars since the current structure run began), volume-behavior-at-levels (rising/falling/flat).

**Deliberately does not reuse the spec's assumed `find_pivot_points()`** — no function by that name exists; the closest candidate, `support_resistance.py`'s `_detect_zigzag_pivots()`, sorts and deduplicates pivots by price (`sorted(list(set(...)))`), which destroys the chronological order this classification needs to tell a higher-high from a lower-high. Wrote a separate, self-contained detector instead of modifying the frozen core S&R engine.

**Bug caught by exhaustive testing (not spot-check):** the "was this an established trend" check for Transition detection didn't filter out unlabeled bootstrap pivots before its "all HH" check, so a genuine up→down reversal in a synthetic test case wasn't classified as Transition. Fixed before shipping.

Displayed in `PriceStructureCard.jsx` as a one-line structure/trend-age/volume-behavior addition to Section A. Verified live on 5 real tickers (AAPL, NVDA, JPM, COST, TSLA). Phase 3 (visual chart via lightweight-charts) remains deferred.

---

## COMPLETE — Breakout Enhancement Plan Phase 0 (Day 81)

**Source:** `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Task 0.1/0.2. Full results: `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY81.md`.

Config D (breakout-confirmed-only: `broken_out` status + volume-confirmed) and Config E (anticipatory-only: `at_pivot`/`forming`) added to `check_entry_signals()`, sharing Config B's pattern scan. Config C verified byte-for-byte unchanged before/after (git stash diff on quick-test). Walk-forward run on the default 60-ticker universe:

| Config | IS Trades | OOS Trades | IS PF | OOS PF |
|--------|-----------|------------|-------|--------|
| C (mixed, existing) | 29 | 42 | 2.01 | 1.64 |
| D (confirmed-only) | **0** | **0** | — | — |
| E (anticipatory-only) | 24 | 38 | 1.54 | 1.38 |

**Config D got zero trades — a genuine, root-caused finding, not a bug.** `pattern_detection.py`'s confidence score measures pre-breakout base quality (contraction, tightness, volatility contraction) — properties that structurally erode the instant price actually breaks out. Verified via a daily-granularity scan on AAPL/MSFT/META across 2019-2025: zero `broken_out`+confidence≥60 occurrences across all three pattern types. Config E alone captures 83-90% of Config C's real trades — most of the system's edge already lives in anticipatory entries, not confirmed breakouts.

**Verdict (against Task 0.2's pre-committed criteria):** third branch — "trade count collapses" (0%, more extreme than the <40% threshold) → keep Config C's current mixed logic unchanged, and Phases 2-3 should emphasize anticipatory/`at_pivot`-style states over confirmed-breakout states. **No change to the live/frozen system** — this is a backtest-only finding about the frozen system's own edge, not a threshold change.

**Scope note:** tests `pattern_detection.py`'s 3-status lifecycle (what Config C actually uses), not the separate, richer 8-state `breakout_detection.py` engine wired in Phase 1.5 — that engine's own `BREAKOUT_CONFIRMED` state has different, unbacktested gates and is a different question.

---

## COMPLETE — Automated Paper Trading Engine (Day 81)

**Source:** User-directed, same-session build (not a pre-planned roadmap item) — asked whether the system could generate paper-trading signals and a ledger itself instead of relying on manual Forward Test tab logging.

| Component | File | Result |
|-----------|------|--------|
| Exit-logic DRY (`live_mode`) | `backend/backtest/trade_simulator.py`, `mr_simulator.py` | Live engine replays the exact backtested exit function once per day instead of a second implementation. Verified byte-for-byte identical to batch backtest on 40 synthetic trades. |
| Shared scan query | `backend/scan_queries.py` (new) | Config C TradingView query factored out of `backend.py`'s scan route — live Scan tab and paper-trading engine use one implementation. Refactored route verified to return identical output. |
| SQLite ledger | `backend/paper_trading/ledger.py` (new) | `paper_positions` (pending_entry→open→closed) + `job_runs`. Stats via existing `metrics.compute_metrics()` — not reimplemented. |
| Live signal generation | `backend/paper_trading/live_signals.py` (new) | Momentum: TradingView pre-filter → live categorical assessment → R:R>=1.2. MR: `detect_mr_signal()` over `mean_reversion.DEFAULT_MR_UNIVERSE`. |
| MR liquidity gate fix | `backend/mean_reversion.py` | price>$5+500K shares → price>$10+20d ADV>$25M, matching the backtested gate. Closes the Day 80 known gap. |
| Daily orchestrator | `backend/paper_trading/daily_job.py` (new) | Activate at real historical next-day open → step open positions (self-healing replay) → generate new signals. Idempotent. `--report` flag. |
| Scheduler | `~/Library/LaunchAgents/com.sta.papertrading.daily.plist` | Weekdays 16:30 CT. Installed, loaded, confirmed firing. |

**First live run (2026-07-10):** 0 momentum signals (2 candidates, both correctly rejected on fundamentals/R:R), 2 MR signals queued (GOOGL, ABBV) — cross-checked against `/api/mr/scan` directly, matched.

**Known limitation (accepted, not a bug):** TradingView has no point-in-time query — a missed scheduled run self-heals existing open positions via historical replay, but cannot backfill entry signals for the missed day itself. See Golden Rule 21 and the new Data Integrity note in `GOLDEN_RULES.md`.

**Not done:** no UI surfacing of this ledger yet (separate from the manual Forward Test tab's localStorage) — deferred until trades accumulate (Priority #12 above).

---

## COMPLETE — Fable Review Remediation, ALL 5 PHASES (Day 78–80)

**Source:** Fable 5 full-system review, Day 78. Plan: `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` (now historical/reference — all tasks done).

| Phase | Result |
|-------|--------|
| 0 — Freeze & pre-register | RS threshold contradiction resolved (simple checklist 1.2→1.0, matching Config C). `PAPER_TRADING_PREREGISTRATION.md` created. |
| 1 — Repo hygiene | SimFin key → `.env`, `backend/venv` untracked, `BACKEND_VERSION` constant, 3 dead files deleted. |
| 2 — Backtest integrity | MR transaction costs added (PF 1.26→1.23 net). Gap-aware stop/target fills. `metrics.py` stats overhaul (scipy t-test, actual trades/year, block bootstrap, fixed-risk DD). JS↔Python verdict parity: 86,400-combo grid found 1 real bug (HOLD-fallback missing `Neutral` branch), fixed, now 100% parity. |
| 3 — Backtest↔live coherence | Fundamentals mismatch measured at 40.0% disagreement (mitigation pending user decision). Silent RS fallback fixed on both JS and Python sides. |
| 4 — Survivorship-free re-validation | 400-ticker random sample (seed=42) from SimFin's 3,788-ticker coverage. **Config C: PF 1.61→1.40 (edge survives directionally, not yet statistically significant). MR unrestricted: PF 1.23→0.99 (clean null).** |
| 5 — Paper-trading instrumentation | Entry-slippage logging (`signalClosePrice`/`entrySlippagePct`) + regime snapshot on every paper trade, wired into the Forward Test tab. |
| + MR liquidity re-test (Day 80, user-directed, one-time) | MR backtest entry had no dollar-volume gate at all. Added price>$10, 20d ADV>$25M (pre-committed, not a re-tune). **Result: PF 0.99→1.16, Sharpe -0.10→1.30 — real but still not significant (block bootstrap p=0.064).** MR now same tier as momentum. Live detector (`mean_reversion.py`) updated to match this gate Day 81 — see below. |

**Bottom line:** both momentum and MR are directionally positive, backtest-validated, and **not yet statistically confirmed**. Neither gets capital until 50+ live paper trades clear the pre-registered bar. Full detail: `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY79.md` (including addendum).

---

## COMPLETE — Breakout Engine Wired (Day 79)

A parallel session built a standalone 8-state breakout classifier (`backend/breakout_detection.py`, spec, Pine companion) but never registered its Flask route. Wired (`register_breakout_routes()` in `backend.py`) and validated on 5 real tickers + 1 edge case — see `API_CONTRACTS_DAY79.md` for the full contract. `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` reconciled and updated; Phases 2–3 now unblocked.

---

## PLANNED

### Simplicity Premium UI (Day 70B — PARTIALLY COMPLETE)
- **Priority:** MEDIUM
- **Source:** 4-LLM consensus: "simplicity premium" is real — fewer indicators, faster decisions, better execution
- **Completed (Day 70B):**
  1. ~~Progressive disclosure~~ — ✅ 3-tier collapsible sections implemented. Tier 1 always visible (Verdict, Trade Setup, Bottom Line, MR Signal, Quality Gates). Tier 2 collapsed. Tier 3 hidden until requested.
  2. ~~Decision Matrix view removed~~ — ✅ Full+simple views sufficient.
  3. ~~TradingView Chart removed~~ — ✅ Not adding value.
  4. ~~Sentiment informational-only~~ — ✅ "(info)" label + reduced opacity.
- **Remaining:**
  1. **Flip default view** — Make `analysisView: 'simple'` the default. Full analysis = "Show details" toggle.
- **Effort:** Low (30 min for remaining item)

### v4.0: Forward Testing UI
- **Priority:** HIGH (tracked since Day 25 as CRITICAL)
- **Description:** Track actual trades, record R-multiples, build SQN over time
- **Why:** Cannot validate system without tracking real performance
- **Effort:** High

### v4.1: TradingView Lightweight Charts
- **Priority:** MEDIUM
- **Description:** Interactive charts with S&R levels, RSI/MACD overlays
- **Technology:** TradingView Lightweight Charts (free, open source)
- **Effort:** Medium (4-6 hours)

### v4.2: Pattern Detection ✅ COMPLETED (Day 44)
- **Status:** Implemented in v4.0
- **Features:**
  - VCP (Volatility Contraction Pattern) detection
  - Cup & Handle pattern detection
  - Flat Base pattern detection
  - Minervini's 8-point Trend Template
- **Files:** `backend/pattern_detection.py`, `/api/patterns/<ticker>` endpoint

### v4.3: Options Tab
- **Priority:** LOW
- **Description:** Options data display if data sources available
- **Blocker:** Needs Greeks calculation, complex data sourcing
- **Research:** `docs/research/OPTIONS_TAB_FEASIBILITY_ANALYSIS.md`

### v4.4: Sentiment Integration ✅ COMPLETED (Day 44)
- **Status:** Implemented via Fear & Greed Index
- **Solution Used:** CNN Fear & Greed Index (free API, no key required)
- **Endpoint:** `/api/fear-greed` returns value (0-100), rating, assessment
- **Integration:** Part of v4.5 Categorical Assessment System

### v4.5: Categorical Assessment System ✅ COMPLETED (Day 44)
- **Status:** Replaced 75-point numerical scoring
- **Key Finding:** Score-to-return correlation = 0.011 (essentially ZERO)
- **New Approach:** Categorical assessments (Strong/Decent/Weak)
  - Technical: Based on Trend Template + RSI + RS
  - Fundamental: Based on ROE, Revenue Growth, Debt/Equity
  - Sentiment: Based on Fear & Greed Index (55-75 = Strong)
  - Risk/Macro: Based on VIX (<20) + SPY regime (>200 EMA)
- **Verdict Logic:** Need 2+ Strong categories with Favorable/Neutral risk for BUY
- **Files:** `frontend/src/utils/categoricalAssessment.js`

### v4.6: Perplexity Research Recommendations (Day 45-47)
- **Priority:** HIGH
- **Status:** ✅ COMPLETE (4/4 recommendations done)
- **Source:** `docs/research/Perplexity_STA_Analysis_result_Feb5_2026`
- **Recommendations Implemented:**

| # | Recommendation | Priority | Effort | Status |
|---|----------------|----------|--------|--------|
| 1 | **F&G Threshold Fix** - Expand neutral zone from 45-55 to 35-60 | HIGH | Low | ✅ DONE (Day 45) |
| 2 | **Entry Preference Logic** - ADX-based (>25 momentum, 20-25 pullback) | MEDIUM | Medium | ✅ DONE (Day 47) |
| 3 | **Pattern Actionability** - Only show patterns ≥80% formed | MEDIUM | Medium | ✅ DONE (Day 47) |
| 4 | **Structure > Sentiment Hierarchy** - Risk/Macro overrides F&G assessment | HIGH | Low | ✅ DONE (Day 45) |

**Day 47 Implementation (v4.6.2 + v4.7.1):**
- ADX-based entry preference: >25 = Momentum viable, 20-25 = Pullback preferred, <20 = Wait for trend
- Pattern actionability: Only patterns ≥80% confidence shown as "Actionable" with trigger/stop/target prices
- **Breakout Volume Confirmation (v4.7.1):** Volume ≥1.5x avg = confirmed, shows quality badge (High/Medium/Low)
- Files modified: `categoricalAssessment.js`, `App.jsx`, `pattern_detection.py`

**Key Findings Applied:**
- F&G at 44.7 vs 45.0 creates cliff behavior (0.3 point = different assessment) → Fixed
- Elder's Triple Screen: Structure determines IF, Sentiment determines HOW → Implemented
- ADX > 25 = trend confirmed, favor momentum; ADX 20-25 = favor pullback → Implemented
- Patterns < 80% have high false positive rate - don't show "75% forming" → Implemented

### v4.7: Forward Testing UI ✅ COMPLETE (Day 47)
- **Priority:** HIGH (tracked since Day 25 as CRITICAL)
- **Status:** ✅ IMPLEMENTED
- **Description:** Paper trading simulation with R-multiple tracking
- **Features:**
  - Add/close trades with entry, stop, target prices
  - Automatic R-multiple calculation on close
  - Van Tharp statistics: Win Rate, Avg Win R, Avg Loss R, Expectancy, SQN
  - Trade journal table with status tracking
  - Export to CSV functionality
  - LocalStorage persistence
- **Files:** `frontend/src/utils/forwardTesting.js`, Forward Test tab in `App.jsx`

### v4.8: Comprehensive Testing Framework (Day 45)
- **Priority:** MEDIUM (testing ongoing)
- **Status:** ACTIVE (baseline tests complete, validation ongoing)
- **Test Plan:** `docs/test/TEST_PLAN_COMPREHENSIVE.md`
- **Test Script:** `backend/test_categorical_comprehensive.py`
- **Categories:**
  - A: API Contract Tests (structure validation)
  - B: Categorical Logic Tests (threshold behavior)
  - C: Edge Case Tests (ETFs, extremes, missing data)
  - D: Cross-Validation (vs external sources)
  - E: Integration Tests (frontend-backend match)

**Test Tickers:**
- Tier 1: AAPL, NVDA, JPM, MSFT, COST (baseline)
- Tier 2: SPY, QQQ (ETFs)
- Tier 3: Technical extremes (RSI < 30, > 80)
- Tier 4: TSLA, AMC (fundamental extremes)
- Tier 5: Small caps (PLTR, SOFI)

---

## PLANNED (Research-Verified Features)

> **Source:** Day 48 Multi-AI Research Analysis (Grok/ChatGPT/Perplexity)
> **Principle:** Only implement what's VERIFIED by multiple sources

### v4.9: Enhanced Volume Analysis ✅ COMPLETE (Day 49)
- **Priority:** HIGH (verified useful by all 3 sources)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - OBV (On-Balance Volume) indicator with trend detection (Rising/Falling/Flat)
  - OBV vs Price divergence detection (Bullish/Bearish/None)
  - Enhanced RVOL display (shows "2.3x avg" not just "confirmed")
  - Tooltips explaining each indicator
- **Files Modified:** `backend/backend.py` (v2.16), `frontend/src/App.jsx`
- **Backend:** `calculate_obv()` function added, returns in `/api/sr/<ticker>` meta

### v4.10: Earnings Calendar Warning ✅ COMPLETE (Day 49)
- **Priority:** HIGH (verified - "event risk dominates technicals")
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - Flag stocks with earnings within 7 days (configurable)
  - Warning badge on analysis card (red pulse for ≤3 days, yellow for 4-7 days)
  - Recommendation text based on timing (CAUTION, AWARE)
  - Tooltip with earnings date and specific advice
- **Backend:** `/api/earnings/<ticker>` endpoint with multiple yfinance fallback methods
- **Files Modified:** `backend/backend.py`, `frontend/src/services/api.js`, `frontend/src/App.jsx`

### v4.11: Sector Rotation — Phase 1 + Phase 2 ✅ COMPLETE (Day 58 + Day 62)
- **Priority:** MEDIUM (verified - simple RS ranking is effective)
- **Status:** ✅ Phase 1 COMPLETE (Day 58) + Phase 2 COMPLETE (Day 62)
- **Research:** `docs/research/Sector_Rotation_analysis.md` (450+ lines, comprehensive)
- **Phase 1 (Day 58):** Sector context in existing views — NO new tab
  - Backend: `/api/sectors/rotation` — fetches 11 SPDR ETFs, calculates RS ratio vs SPY, RRG quadrant
  - Analyze page: Color-coded sector badge (Leading=green, Weakening=yellow, Lagging=red, Improving=blue)
  - Scan results: Sector column with quadrant label per stock
  - Hover tooltip: RS ratio, momentum, rank out of 11
  - Purely informational — does NOT change any trade signals or verdicts
- **Phase 2 (Day 62):** Dedicated 🔄 Sectors tab + "Scan for Rank 1" filter
  - `SectorRotationTab.jsx` (NEW): 11 sector cards ranked by RS, quadrant color-coding, rank badges (1-3 green, 4-7 yellow, 8-11 red)
  - RS Ratio + RS Momentum progress bars per card
  - **"Scan for Rank #1 Sector"** CTA — switches to Scan tab with sector filter active
  - Filter banner in Scan tab: "Showing: Technology sector (Rank #1 · Leading)" with ✕ to clear
  - **Bug fixed (Day 62):** TradingView returns SIC sector names ("Non-Energy Minerals") not GICS. Fixed `SECTOR_ETF_MAP.gics` + filter logic.
- **Key insight:** 70% of stock price movement comes from sector leadership (Faber study)
- **Files:** `backend/backend.py` (endpoint), `frontend/src/components/SectorRotationTab.jsx` (NEW), `frontend/src/App.jsx`

### v4.20: Cache Management Audit + UI Freshness Meter ✅ COMPLETE (Day 59)
- **Priority:** MEDIUM (data quality concern)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - Audited all cache TTLs — all reasonable (OHLCV 4hr, fundamentals 24hr, sectors per trading day)
  - New endpoint: `/api/data/freshness?ticker=AAPL` — returns cache age/status per data source
  - UI freshness meter: colored dots (green=fresh, yellow=aging, red=stale) on Analyze page
  - `fetchDataFreshness()` added as 10th parallel call in `fetchFullAnalysisData()`
- **Files:** `backend/backend.py`, `frontend/src/services/api.js`, `frontend/src/App.jsx`

### v4.24: Context Tab — Pre-Flight Macro Context ✅ COMPLETE (Day 62)
- **Priority:** MEDIUM (user-requested: informed decision-making layer)
- **Status:** ✅ COMPLETE (Day 62)
- **Principle:** PRE-FLIGHT CONTEXT ONLY — informs human, does NOT modify verdicts or categorical assessment
- **Architecture:** 3 new backend engines + 4 new endpoints + 5 new React components
- **Column A: Calendar & Yield Cycles** — 6 cards (FRED T10Y2Y + INDPRO + 4 calendar computations)
  - Yield Curve, Business Cycle, Presidential Year, Seasonal, FOMC Proximity, Quad Witching
  - Regime thresholds: FAVORABLE / NEUTRAL / ADVERSE per card
  - Options block detection: FOMC < 5d OR Quad Witching < 3d
  - Cache: 6h (FRED monthly data, calendar computed)
- **Column B: Economic Indicators** — 4 cards (FRED FEDFUNDS + CPIAUCSL + UNRATE + MANEMP)
  - Fed Funds Rate (direction), CPI YoY, PMI proxy (MANEMP), Unemployment
  - Historical composite box (regime combination → historical return description)
  - Options Block Status banner (green/red)
  - Cache: 6h
- **Column C: News Sentiment** — per ticker (Alpha Vantage + yfinance)
  - Aggregate sentiment: BULLISH / NEUTRAL / BEARISH with score breakdown
  - Article feed (up to 10 articles with emoji, score badge, clickable title)
  - Short interest: short % float + days to cover + assessment (High/Normal/Low)
  - ConflictCheck banner: ALIGNED / CONFLICT / PARTIAL
  - Cache: 4h per ticker (25 req/day Alpha Vantage free tier)
- **Overall Regime Banner:** Counts favorable/neutral/adverse across all 10 indicators
  - FAVORABLE if >= 5 favorable AND adverse < 2; ADVERSE if adverse >= 4; else NEUTRAL
- **Auth:** FRED_API_KEY (free, 1000/day), ALPHAVANTAGE_API_KEY (free, 25/day)
- **New Endpoints:** `/api/cycles`, `/api/econ`, `/api/news/<ticker>`, `/api/context/<ticker>`
- **Files Created:** `backend/cycles_engine.py`, `backend/econ_engine.py`, `backend/news_engine.py`, `frontend/src/components/ContextTab.jsx`, `RegimeBanner.jsx`, `CycleCard.jsx`, `ArticleRow.jsx`, `ConflictCheck.jsx`
- **Files Modified:** `backend/cache_manager.py` (+6 TTL wrappers), `backend/backend.py` (+4 endpoints), `frontend/src/App.jsx`, `frontend/src/services/api.js` (+4 fetch functions)
- **Pending (Day 63):** Option C Hybrid — filter news articles to reputable sources only (Reuters, Bloomberg, WSJ, FT, Barron's, etc.), show top 3 per sentiment category

### v4.12: TradingView Lightweight Charts
- **Priority:** MEDIUM
- **Status:** PLANNED
- **Description:** Interactive charts with S&R levels, RSI/MACD overlays
- **Technology:** TradingView Lightweight Charts (free, open source)
- **Effort:** 4-6 hours

### v4.13: Holding Period Selector + Bottom Line Summary ✅ COMPLETE (Day 53)
- **Priority:** HIGH (addresses core UX confusion)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - 3-way holding period toggle: Quick (5-10d) | Standard (15-30d) | Position (1-3mo)
  - Signal WEIGHTING by horizon (Quick=T:70%/F:30%, Standard=50/50, Position=T:30%/F:70%)
  - Verdict changes when Tech and Fundamental disagree (weighting tips the balance)
  - Bottom Line Card with action plan, what's good/risky, weight badges
  - Research-validated: arXiv 2512.00280 (40 bps monthly alpha from signal weighting)
- **Files Modified:** `categoricalAssessment.js`, `BottomLineCard.jsx`, `App.jsx`

### v4.15: Decision Matrix Tab ✅ COMPLETE (Day 53)
- **Priority:** HIGH (synthesis layer for 3 independent analysis systems)
- **Status:** ✅ IMPLEMENTED
- **Problem Solved:** 3 layers (Assessment, Patterns, Trade Setup) each produce correct output independently but nobody SYNTHESIZES them. Trader had to mentally cross-reference 4+ UI cards.
- **Features:**
  - 3-step workflow: "Should I Trade This?" → "When Should I Enter?" → "Does The Math Work?"
  - Surfaces 10 computed-but-hidden fields (RS interpretation, ADX analysis, signal weights, entry preference, fundamental metrics, sentiment subLabel)
  - Contradiction resolution: explains WHY backend says "Good setup" but R:R fails
  - Contextual action items based on verdict + viability + patterns
  - 3rd view toggle between Full Analysis and Simple Checklist
- **Files:** `frontend/src/components/DecisionMatrix.jsx` (new), `App.jsx` (3 edits)

### v4.16: Holistic 3-Layer System Backtest ✅ COMPLETE (Day 55) — ⚠️ see Day 79 re-validation below
- **Priority:** HIGH (cannot validate system without historical outcome testing)
- **Status:** ✅ IMPLEMENTED
- **Results (60 tickers, 2020-2025) — HINDSIGHT-UNIVERSE, kept for history, not canonical:**
  - Config A (Categorical only): 1108 trades, 51.53% WR, PF 1.41, p<0.000001
  - Config B (A + Patterns): 406 trades, 51.72% WR, PF 1.43, p=0.002
  - Config C (Full 3-layer): 238 trades, 53.78% WR, PF 1.61, Sharpe 0.85, p=0.002
  - **All 3 configs statistically significant — NOT random**
  - **⚠️ Day 79: this 60-ticker universe was hand-picked in 2026 and is dominated by 2020-2025 mega-winners. See "COMPLETE — Survivorship-Free Re-Validation (Day 79)" below for the canonical, unbiased-universe numbers.**
- **Walk-Forward:** OOS outperforms IS — system is NOT overfitted
- **Exit Optimization:** 10-day EMA trailing stop + breakeven stop, max drawdown 65.9% → 52.6%
- **Files:** `backend/backtest/` (5 new files: simfin_loader, categorical_engine, metrics, trade_simulator, backtest_holistic)

### v4.17: Production Coherence + Bear Regime ✅ COMPLETE (Day 56)
- **Priority:** HIGH (sync production with backtested thresholds)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - Frontend-backend coherence audit: 39/42 parameters matched
  - Pattern confidence threshold synced: 80% → 60% in production
  - Bear market regime: SPY 50 SMA declining caps risk at "Neutral"
  - 5th scan filter redesigned to match Config C criteria
- **Files Modified:** `categoricalAssessment.js`, `backend.py`, `App.jsx`, backtest files

### v4.14: Multi-Source Data Intelligence ✅ COMPLETE (Day 52)
- **Priority:** HIGH (eliminates single-source dependency)
- **Status:** ✅ IMPLEMENTED
- **Problem Solved:** STA relied 100% on yfinance (unofficial scraper, rate-limited, IP blocked)
- **Providers Implemented:**
  - TwelveData: 800 credits/day, 8/min - Primary OHLCV
  - Finnhub: Unlimited, 60/min - Primary fundamentals
  - FMP: 250/day - Fundamentals backup (epsGrowth, revenueGrowth)
  - yfinance: Free - Universal fallback
  - Stooq: Free via pandas_datareader - Last resort OHLCV
- **Fallback Architecture:**
  - OHLCV: TwelveData → yfinance → Stooq
  - Fundamentals: Finnhub → FMP → yfinance (field-level merge)
  - VIX: yfinance → Finnhub → stale cache
- **Infrastructure:**
  - `backend/providers/` package (13 files)
  - `DataProvider` orchestrator with singleton pattern
  - Circuit breaker per provider (3 failures → 5min cooldown)
  - Token-bucket rate limiting per provider
  - Cache-first strategy with stale cache fallback
  - Provenance tracking (`_field_sources` dict)
  - `backtest_adapter.py` for backtest scripts
- **Backend Integration:** All 9 yfinance call sites replaced with DataProvider + legacy fallback
- **Frontend:** All data source labels updated from "Defeat Beta" / "yfinance" to multi-source names
- **Files:** `backend/providers/` (13 files), `backend/backend.py` (v2.17), `backend/cache_manager.py`

---

### v4.18: S&P 500 / NASDAQ 100 / Dow 30 Index Filter ✅ COMPLETE (Day 56)
- **Priority:** MEDIUM (user-requested quality filter)
- **Status:** ✅ IMPLEMENTED
- **Features:**
  - User-selectable dropdown: All US Stocks / S&P 500 / NASDAQ 100 / Dow 30
  - TradingView native `Query().set_index()` — no maintenance needed
  - Correct index identifiers (verified via live testing):
    - S&P 500: `SYML:SP;SPX` (503 stocks)
    - NASDAQ 100: `SYML:NASDAQ;NDX` (101 stocks)
    - Dow 30: `SYML:DJ;DJI` (30 stocks)
  - Works with all 5 scan strategies
- **Files Modified:** `backend.py` (INDEX_MAP + market_index param), `api.js` (marketIndex param), `App.jsx` (dropdown)

---

## NIRMAL INTEGRATION OPPORTUNITIES (Day 73 — Research Complete)

**Source:** `docs/research/NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md`
**Validation:** `docs/research/NIRMAL_STA_VALIDATION_RESULTS.md` — 378 calls, BUY 15.3%, HOLD 40.2%, AVOID 44.4%
**Key finding:** Style difference, not system failure. STA covers Nirmal's Minervini-quality momentum plays perfectly. MR engine covers his oversold-recovery subset. Gaps are in gap-fill and market phase synthesis.

| # | Gap | Effort | Status |
|---|-----|--------|--------|
| N1 | **Two-price entry labels** in Trade Setup (Primary Entry + Averaging Entry) | Very Low (~2h) | **Approved — build next sprint** |
| N2 | **Nirmal watchlist preset** in Scan tab dropdown (15 core tickers) | Very Low (30 min) | **Approved — build next sprint** |
| N3 | **Gap-fill detection** — `detect_gaps()` backend, output to Price Structure Card or Trade Setup | Medium (1 session) | **Deferred — post paper trading** |
| N4 | **Market Phase synthesis** — synthesize VIX + SPY trend + sector RS + F&G into 5-phase label (Bull Rally / Profit Taking / Sector Rotation / Consolidation / Correction) | Medium (1 session) | **Needs validation first (Golden Rule #15)** |

**What NOT to build (per Nirmal's explicit cautions):**
- No auto-averaging losers
- No "it'll bounce back" signals on broken setups
- No overriding stop loss

**OptionsIQ note:** Nirmal's 223 options calls (`nirmal_options_recommendations.csv`) can validate OptionsIQ's recommendation logic before shipping.

---

---

### Value Investing Tab (Buffett/Damodaran Style — Day 73 IDEA, Research Needed)
- **Priority:** MEDIUM — post paper-trading, after N4
- **Status:** IDEA STAGE — needs research validation before any implementation
- **Purpose:** Separate "quality at a fair price" lens for long-term value buys. Zero impact on STA swing verdicts.
- **Design principle:** Branch off STA as a new tab — reuse existing data pipeline, add 2-3 new computed fields. Never touch categorical assessment or swing verdict.
- **What existing STA already has:** ROE, D/E, revenue growth (reusable)
- **Minimal new additions needed:**
  1. **Graham Number** — `sqrt(22.5 × EPS_ttm × BookValuePerShare)`. If price < Graham Number → potentially undervalued. Simple, reliable, no new data needed (EPS + BV already in Finnhub/yfinance).
  2. **DCF Lite** — Use FCF + 5yr growth rate estimate → discounted at 10%. Approximate intrinsic value. `yfinance.freeCashflow` available.
  3. **PEG Ratio** — P/E ÷ 5yr EPS growth. PEG < 1 = potentially undervalued relative to growth. Data available.
  4. **Quality Checklist** — ROE > 15% (consistent), D/E < 0.5, FCF positive, net margin stable. Reuses existing fundamentals.
  5. **Margin of Safety** — `(Intrinsic - CurrentPrice) / Intrinsic × 100`. Output: "28% margin of safety" or "Overvalued by 15%".
- **What NOT to build (too complex for v1):**
  - Full Damodaran 10-K DCF (needs multi-year income/balance/cashflow statements)
  - Moat analysis (qualitative, not automatable)
  - Sector-adjusted valuation multiples
- **New backend endpoint:** `/api/value/<ticker>`
- **New frontend:** `ValueTab.jsx` — standalone tab, no wiring into swing scoring
- **Research question:** Do Graham Number + DCF Lite + PEG correlate with actual 3-5yr returns? Need to validate against Damodaran's published datasets before building.
- **Source reference:** Damodaran's free datasets at `pages.stern.nyu.edu/~adamodar/` — valuation multiples by sector

---

## RESEARCH REQUIRED (Before Implementation)

### RSI/MACD Divergence Detection

### RSI/MACD Divergence Detection
- **Status:** RESEARCH NEEDED
- **Problem:** Generic false positive rates are unverifiable
- **Action:** If implementing, must compute OUR OWN FPR via backtest
- **Threshold:** Only implement if FPR < 40%

---

## DEFERRED (v2+ / Low Priority)

| Feature | Reason for Deferral |
|---------|---------------------|
| Full RRG Charts | Overkill - simple RS ranking achieves same goal (Day 48 research) |
| Candlestick Patterns | Research complete (Day 63). 4 viable patterns identified (Hammer 59.86%, Bullish Engulfing 60-68%, Morning Star 58-65%, Doji). Pure NumPy implementation required (pandas-ta/TA-Lib NOT installed). Deferred — not a current priority. |
| Full TradingView Integration | After Lightweight Charts validated |
| H&S Pattern Detection | Academic research "scarce and inconclusive" (NY Fed) |
| Seasonal Patterns | "Small edge", regime-dependent (ChatGPT) |
| Optimal Weighting System | No universal answer exists - varies by regime |

### v4.19: Basic Options Tab (LOWEST PRIORITY)
- **Priority:** LOW — build only when daily forward testing is running and system is in maintenance mode
- **Status:** RESEARCH COMPLETE (Perplexity deep research, Day 56)
- **Research doc:** `docs/research/OPTIONS_TAB_PERPLEXITY_PROMPT.md` (includes full results)
- **Scope:** 4 signals: Call Buy, Covered Call, Put Buy, Cash-Secured Put eligibility
- **Data:** yfinance chains + `py_vollib_vectorized` for local Greeks/IV computation
- **Key decisions:**
  - Binary "Eligible / Not Eligible" per strategy with bullet rationale
  - IV Rank/Percentile computed locally from stored IV history
  - Greeks via Black-Scholes (no vendor dependency)
  - No multi-leg strategies, no naked selling, no real-time dashboards
- **Prerequisite:** System must be in daily forward testing phase first

### v4.21: Canadian Market Support (TSX 60 + All Canadian) — SCAN ONLY ✅ (Day 59)
- **Priority:** MEDIUM (user requested Day 58)
- **Status:** ✅ SCAN TAB ONLY — Analyze page NOT yet supported
- **Scope 1 (DONE):** TSX 60 + All Canadian scan
  - TSX 60 scan: `set_index('SYML:TSX;TX60')` — uses america scanner (handles TSX indices natively)
  - All Canadian: `set_markets('canada')` — broader scan (TSX + TSXV + NEO exchanges)
  - Frontend: "TSX 60" and "All Canadian" dropdown options
  - Ticker mapping: `TSX:RY` → `RY.TO` for yfinance/TwelveData
  - Exchange filtering: `valid_exchanges` variable (TSX/TSXV/NEO for Canadian, NYSE/NASDAQ/AMEX for US)
  - 3 bugs fixed during implementation:
    1. `set_index` + `set_markets('canada')` combo fails — use `set_index` alone for tsx60
    2. `.TO` suffix triggered preferred stock filter — moved suffix append AFTER filter
    3. Hardcoded US exchanges — replaced with `valid_exchanges`
  - Verified: BMO.TO, SU.TO, NTR.TO returning correctly
- **Scope 2 (NOT STARTED): Analyze Page for Canadian Tickers**
  - Data source redesign needed: TwelveData/Finnhub/FMP may not cover `.TO` tickers — need yfinance-first fallback
  - Fundamentals: verify Canadian company coverage in free-tier APIs
  - Sector rotation: need Canadian sector ETF mapping or use US SPDRs as proxy
  - Fear & Greed: US-only — use as proxy or find Canadian equivalent
  - S&R, patterns, categorical assessment: math works but untested on `.TO` data
- **Scope 3 (DEFERRED):** CAD-Hedged US Tickers (CDRs on NEO exchange like MSFT.NE, AMZN.NE)
  - Research needed: CDR availability, technical analysis applicability (volume/patterns may differ)
- **What doesn't change:** All technical analysis, S/R clustering, pattern detection, decision matrix
- **Market hours:** TSX = same as NYSE (9:30-4:00 ET) — no timezone issues
- **Files Modified:** `backend/backend.py`, `frontend/src/App.jsx`

---

## RESEARCH COMPLETED

| Document | Topic | Day |
|----------|-------|-----|
| PERPLEXITY_RESEARCH_SYNTHESIS.md | Trading system validation | Day 41 |
| OPTIONS_TAB_FEASIBILITY_ANALYSIS.md | Options data requirements | Day 42 |
| SECTOR_ROTATION_IDENTIFICATION_GUIDE.md | Sector rotation methods | Day 42 |
| Perplexity_STA_Analysis_result_Feb5_2026 | UX/Trading system design (4 questions) | Day 45 |
| TEST_PLAN_COMPREHENSIVE.md | Quant-style testing methodology | Day 45 |
| Research_answers_For_Thinking_Journal.md | Multi-AI research (Grok/ChatGPT/Perplexity) | Day 48 |
| RESEARCH_ANALYSIS_CRITICAL_REVIEW.md | Critical analysis of research - verified vs unverified | Day 48 |
| ACTION_PLAN_FROM_RESEARCH.md | Implementation priorities from research | Day 48 |
| OPTIONS_TAB_PERPLEXITY_PROMPT.md | Options Tab: data sources, checklists, Greeks, decision matrix | Day 56 |
| UNIVERSAL_PRINCIPLES_SYNTHESIS.md | 4-LLM audit (35 claims, 5 domains) — surgical evolution from Minervini to universal quant framework | Day 69 |
| NIRMAL_STA_INTEGRATION_OPPORTUNITIES.md | Nirmal system gap analysis — 4 gaps, N1+N2 approved, N3-N4 deferred | Day 73 |
| NIRMAL_STA_VALIDATION_RESULTS.md | 378 calls validated — 15.3% BUY, style difference confirmed, not system failure | Day 73 |

---

## KEY INSIGHTS (Day 27 Philosophy + Day 44 Update)

From backtesting:
- **Entry signals = ~10% of results**
- **Position sizing = ~90% of results**
- Score-to-return correlation = 0.011 (essentially ZERO)
- 75-point scoring achieves ~50% win rate (essentially random)

**Day 44 Response (v4.5 Categorical Assessment):**
- Replaced 75-point numerical scoring with categorical assessments
- System works as a FILTER, not a RANKER
- Categories (Strong/Decent/Weak) honestly represent this reality
- Real Fear & Greed Index replaces placeholder sentiment

**Current Focus:**
- Better R:R through dual entry strategy
- Risk reduction through proper stops
- System measurement through forward testing
- Categorical filtering over numerical ranking

---

## UPDATE LOG

| Day | Changes |
|-----|---------|
| 42 | Created ROADMAP.md, added v4.4/v4.5 for placeholders |
| 44 | v4.2 Pattern Detection complete, v4.4 Sentiment (Fear & Greed) complete, v4.5 Categorical Assessment complete |
| 45 | v4.6 Perplexity Research Recommendations added, v4.7 Comprehensive Testing Framework added |
| 46 | v4.6 UI Testing complete, Issue #0 fixed (Recommendation Card alert prices), validated with 5-ticker 2nd iteration |
| 47 | v4.6.2 ADX Entry Preference + Pattern Actionability ≥80% complete, v4.7 Forward Testing UI complete |
| 48 | Multi-AI research analysis, added v4.9-v4.12 (OBV, Earnings, Sector Rotation, Charts), updated DEFERRED with research findings |
| 49 | v4.9 OBV+RVOL complete, v4.10 Earnings Warning complete, UI Cohesiveness test (92.8% pass), 5 issues fixed (support level, position sizing, VIABLE badge, R:R filter, null support zone) |
| 50 | Exhaustive UI re-test (21% true pass vs 92.8% spot-check), ALL 5 UI issues FIXED (v4.4), v4.13 Holding Period Selector plan created, n8n research notes added |
| 51 | v4.13 plan REVISED after research validation - RSI thresholds INVALIDATED, signal weighting VALIDATED, Golden Rule #15. v4.14 Multi-Source Data plan created - researched free tier limits, TwelveData+Finnhub primary, yfinance demoted to fallback |
| 52 | v4.14 Multi-Source Data Intelligence COMPLETE: 5 providers, 13 new files, backend v2.17, field-level merge, circuit breakers, rate limiting, frontend labels updated, Defeat Beta now redundant |
| 53 | v4.15 Decision Matrix COMPLETE, v4.13 Holding Period COMPLETE, Bugs #7/#8 fixed, Architectural audit: removed fundamentals from /api/stock/ (SRP), removed ~255 lines dead code, 5-field end-to-end reconciliation. Backend v2.18. |
| 54 | Pre-backtest audit (3 investigations): API data integrity (3 CRITICAL + 4 HIGH found), Decision Matrix coherence (ALL CLEAR), Simple Checklist review (50% SEPA alignment). Fixed 4 hardcoded fallbacks: sentiment 5→0, breadth 1→0, F&G 50→null, VIX 20→null. Golden Rule: silent fallbacks are invisible lies. |
| 55 | v4.16 Holistic 3-Layer Backtest COMPLETE: 60 tickers, 3 configs, all statistically significant. Config C: 53.78% WR, PF 1.61, Sharpe 0.85. Walk-forward validated. Exit optimization: trailing 10 EMA + breakeven stop, DD reduced -13.3%. |
| 56 | v4.17: 5th filter redesigned (Config C), coherence audit (39/42 match, pattern threshold 80→60), bear regime filter added. v4.18 S&P/NASDAQ/Dow index filter IMPLEMENTED. Options Tab research complete (v4.19, deferred). |
| 57 | Bear regime backtest VALIDATED (bear WR 71.4%). Quick+Position periods backtested and walk-forward validated. Full coherence audit (71 params, 96%). sma50Declining wired backend→frontend. yfinance 0.2.28→1.2.0. Sector rotation plan RETHOUGHT (Phase 1: embed in views, not new tab). |
| 58 | v4.19: Pattern trader descriptions (VCP/Cup&Handle/Flat Base). Sector Rotation Phase 1 COMPLETE: /api/sectors/rotation endpoint, RS ratio + RRG quadrant, badge on Analyze page + column in Scan results. Fixed: sector badge reliability (race condition), SQLite cache for sector data, scan transparency (empty vs error). Added v4.20 Cache Audit + Freshness Meter to roadmap. |
| 59 | v4.20 Cache Freshness Meter COMPLETE (endpoint + UI dots). v4.21 Canadian Market COMPLETE (TSX 60 + All Canadian scan, 3 bugs fixed). DVN Bottom Line entry type fix (R:R-based). AI Fluency Critical Analysis document. ADX 25 threshold logged as unvalidated assumption. |
| 60 | Simple Checklist 4→9 criteria COMPLETE (52-Wk Range, Volume, ADX, Market Regime, 200 SMA Trend — Minervini SEPA + backtest-validated). EPS/Revenue Growth QoQ→YoY fix COMPLETE + `_growth_to_pct()` format normalization. ADX `.toFixed()` crash fix. |
| 61 | 4-Layer Coherence Audit COMPLETE (87 fields, 10 tickers, 10 endpoints). 9 bugs fixed: NaN safety (3-layer defense), F&G thresholds synced, cache schema v2, earnings 500 on error, R:R DRY utility (riskRewardCalc.js), F&G fallback flag. API_CONTRACTS updated Day 53→Day 61. Version v4.23. |
| 62 | Sector Rotation Phase 2 COMPLETE: 11 sector cards + "Scan for Rank 1" filter. Context Tab COMPLETE: 3 columns (Calendar/Yield Cycles + Econ + News Sentiment), 3 new engines, 4 new endpoints, 5 new components. FRED API key activated. TradingView SIC sector name mismatch fixed (49 mapping entries). Option C Hybrid news filtering queued. Candlestick patterns queued as standalone post-flight check. Version v4.24. |
| 63 | Option C Hybrid COMPLETE: news_engine.py filters Alpha Vantage articles to 19 reputable sources (Reuters, Bloomberg, CNBC, WSJ, etc.), fetches pool of 50, curates top 3 per sentiment bucket. Candlestick research complete (4 viable patterns), deferred to low priority. PLTR force-fit analysis. Version v4.25 (BE v2.26). |
| 64 | Deep Audit COMPLETE — 18 bugs fixed (4 rounds): VCP strictly-decreasing + gate hybrid + pivot fix, Wilder EMA ATR, W-FRI resample, ATR stop floor ($0.01), Cup handle_below_lip, FOMC edge case, constants.py (single source), CAUTION/NOT_VIABLE distinction, All-Decent+Neutral→HOLD, bidirectional contradiction. Version v4.27 (BE v2.30, FE v4.14). Feature freeze + paper trading phase. |
| 66 | Size rotation strip added to Sectors tab (IWM/MDY/QQQ vs SPY RS). Sector card audit: RS bar scale, rank badge neutral gray, scan buttons quadrant-based. start.sh/stop.sh auto kill-port. Version v4.28 (BE v2.31). |
| 67 | Data Sources transparency audit: Full Finnhub→AlphaVantage→yfinance chain confirmed. FMP v3 confirmed dead (Aug 2025). 8 text references updated. 3 UI correctness fixes (provenance path, TwelveData ACTIVE, circuit-open guard). 4 provenance bugs fixed (hardcoded source, negative age, bare "0", JUST FETCHED badge). Version v4.30 (BE v2.32, FE v4.30). |
| 68 | System audit Layer 1+2: 15 README claims audited — 9 VERIFIED, 5 MISLEADING, 1 PLAUSIBLE. Doc framework 62% reduction. |
| 69 | 4-LLM Universal Principles synthesis. Tier 0 bug fixes + Tier 1 quick wins implemented. |
| 70 | Universal Principles Tier 2+3 complete. VIX sizing, blended RS (info only), MR engine + MRSignalCard. Version v4.31. |
| 70B | Simplicity premium UI: 3-tier progressive disclosure, Decision Matrix + TradingView Chart removed. Sentiment informational-only. Simple checklist: RS 1.0→1.2, cap-aware volume + stop distance. Version v4.32. |
| 72 | Price Structure Card Phase 1 COMPLETE: `PriceStructureCard.jsx` + `priceStructureNarrative.js`. Master Audit Framework created (5 audit types). levelScores in S/R API. Version v4.33. |
| 73 | Nirmal validation complete (378 calls). Integration gaps N1-N4 defined. N1+N2 approved. N3 deferred. N4 needs validation. Priority reordered (quant/trader lens). Value Investing tab idea documented. |
| 74 | Context session. TradingView scanner brief. No code changes. |
| 75 | Value Tab Phase 1 (isolated lens, v4.34). Gate 5 PASSED (1.9% overlap, 0.274 corr). Price Structure behavioral test PASSED 5/5 (2 bugs fixed). N1+N2+flip default view implemented. Version v4.35. |
| 78 | Fable 5 full-system audit: backtest edge likely overstated (survivorship universe, reused OOS, MR costs missing, RS 1.0/1.2 contradiction). Remediation plan + Breakout enhancement plan created. Golden Rule 18 added. Priority order rebuilt — remediation #1. No code changes. |
| 78B | Remediation Session 1: RS threshold RESOLVED — simple checklist reverted 1.2→1.0 (`simplifiedScoring.js`). The Day 70B "1.2" claim (PF 1.56→1.78, 20 tickers) has no reproducible script in the repo; `backtest_simplified.py` — the only candidate — tests 1.0 with unrelated params and predates the 9-criteria checklist. RS 1.0 is what Config C's 238-trade walk-forward-validated backtest actually uses. Full view and simple checklist now agree. Pre-registration doc, repo hygiene (SimFin key→.env, venv untracked, version string fixed, dead code removed) also completed this session. |
| 79 | Fable Remediation Phases 2–3 complete: MR transaction costs (PF 1.26→1.23 net), gap-aware fills, `metrics.py` stats overhaul (scipy t-test, actual trades/year, block bootstrap, fixed-risk DD), JS↔Python verdict parity grid (86,400 combos, 1 bug found + fixed, now 100% parity), fundamentals mismatch measured (40.0% disagreement — mitigation pending), silent RS fallback fixed both sides. Breakout engine wired (`/api/breakout/<ticker>` now functional) and validated on 5 tickers + edge case. Golden Rule 19 added (systematic grid-test parity). Version v4.37 (BE v2.36, FE v4.36). |
| 80 | Fable Remediation Phase 4 (survivorship-free re-validation: Config C PF 1.61→1.40, MR PF 0.99 clean null) + Phase 5 (paper-trading instrumentation: entry slippage + regime snapshot logging) — **plan complete, all 5 phases**. User-directed one-time MR liquidity re-test (price>$10, 20d ADV>$25M): PF 0.99→1.16, Sharpe -0.10→1.30, still not significant (p=0.064) — MR now same "real but modest, unconfirmed" tier as momentum. Golden Rule 20 added (pre-committed restriction vs re-tune distinction). Version v4.38 (BE v2.37, FE v4.37). |

---

---

## IBKR Screener Integration (Day 77 — Research Complete)

**Purpose:** Two-stage candidate pipeline. IBKR pre-screens 7,000+ stocks in real-time → `/ibkr-scan` skill runs survivors through STA → top 5–10 candidates.

**Research docs:**
- `docs/research/IBKR_SCREENER_INTEGRATION.md` — full factor reference + filter design
- `docs/research/IBKR_SCREENER_EXTERNAL_AUDIT_PROMPT.md` — external audit prompt
- `docs/research/IBKR_SCREENER_LLM_AUDIT.md` — 3-LLM synthesis (Perplexity + GPT + Gemini)

**Final 10 filters (3-LLM validated):**
Market Cap ≥1B · AvgVol($) ≥5M · Price/EMA(200) 1.05–1.65 · Price/EMA(50) 1.00–1.20 · ROE ≥15 · EarnGrw% ≥20 · Inst.Held 25–90 · 52W High Proximity ≤-25% · MACD Histogram ≥0 · Change% -2 to +8

**Skill design:** User pastes IBKR screenshot(s) → Claude reads tickers via vision → calls STA API → scores → outputs top 5–10.

**Status:** Research COMPLETE. Build pending verification of 52W High Proximity field in IBKR.

---

*This is the canonical roadmap. README.md roadmap should mirror this.*
*CLAUDE_CONTEXT.md includes this file in startup checklist.*
