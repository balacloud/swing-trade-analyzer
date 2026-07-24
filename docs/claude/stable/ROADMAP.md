# ROADMAP - Canonical Version

> **Purpose:** Single source of truth for project roadmap - Claude reads this at session start
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 96 (July 24, 2026)
> **Note:** README.md roadmap should mirror this file for external users

---

## Current Version: v4.52 (Backend v2.45, Frontend v4.47, Backtest v4.19, API Service v2.11)
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
| 1 | **Let paper trading accumulate** | SOLE FOCUS (Day 92 — user explicitly holds all other priorities below this until the bar clears) — automated engine (`backend/paper_trading/`) built and live Day 81, running unattended daily via launchd. Both momentum (PF 1.40) and MR (PF 1.16, post liquidity re-test) still need **100 live trades each** before capital allocation (raised from 50, Day 92 — see `PAPER_TRADING_PREREGISTRATION.md` Change Log). As of Day 92: momentum 0 closed, MR 5 closed — both far from either bar. Check in via the Forward Test tab's status panel (now with an expandable per-ticker table, Day 92) or `daily_job.py --report`. | Ongoing (no build work) |
| 2 | **Decide fundamentals mitigation** | Task 3.2 measured 40.0% live↔backtest disagreement — user decision pending: align live-to-SimFin or backtest-to-TTM. Now also affects the automated engine's momentum leg. | Decision + implementation |
| 3 | **Confirm SimFin key rotation** | A possible new key was shared in conversation Day 79 but never confirmed as intentional or applied. | Small |
| 4 | **N3: Gap-fill detection — needs a design session first** | No spec exists yet (Day 87 finding) — only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`. Design, then build. | Design session, then Medium |
| 5 | **Value Tab Phase 2 — needs a batch-prefetch design session first** | Spec (`VALUE_TAB_SPEC.md`) requires nightly batch-prefetch infra (watchlist + schedule) for AlphaVantage's ~8-tickers/day budget; explicitly gated to build only post-freeze. On-demand fetching (Phase 1's pattern) would contradict the documented design. | Design session, then Low-Medium |
| 6 | **Build `/ibkr-scan` skill** | Research done (Day 77). Verify 52W High Proximity in IBKR first. | 1 session |
| 7 | **Price Structure Phase 3** | Visual chart via lightweight-charts (Phases 1-2 done as of Day 87). | Medium |
| 8 | **Canadian Analyze page** | Medium bug, data source redesign needed | High |
| 9 | **(Optional, low priority) Scan tab batch breakout badges: distinguish NOT_READY from a failed fetch** | Currently both render as a plain "—" dash (`App.jsx` ~line 2753) — same ambiguity class as the single-ticker card had before the Day 84 fix, just not yet asked for at the 20-row table. | Small |
| 10 | **Session 28 audit — remaining lower-priority findings** | Top-4 fixed Day 91 (see below). Remaining, from `HANDOFF_sta_audit_session28.md`: Value tab's ROE thresholds badged "Buffett/Damodaran" when the code comment says "ChatGPT research validated"; Validate/Data Sources tabs show "live"/"healthy" status without probing real fetch success (missing data renders identically to fresh data); Sectors tab's `.toFixed(3)` false precision (the Rank #1 CTA/gate-bypass part of this finding was fixed later Day 92, via `pickBestSector()` in the Sectors tab redesign — see `KNOWN_ISSUES_DAY92.md`); Forward Testing's momentum-path trades store identical net/gross P&L (fee accounting not differentiated) and per-position fetch failures are silently dropped. Plus the audit's own "polish" list (transparency blocks, composite-score recalculation, softened wording on a few cards). | Small-Medium, batchable |
| 11 | **Volume-confirmation not in the core verdict — needs a design + re-backtest session first** | Found in a post-Day-91 first-principles review of the decision engine (not part of the Session 28 audit). Neither the Full Analysis verdict tree (`determineVerdict()` in `categoricalAssessment.js`) nor the Simple Checklist's 9 criteria check whether a move is confirmed by rising volume (accumulation) vs. thin volume — the Simple Checklist's "Volume" criterion (`simplifiedScoring.js`) is a **liquidity gate** (avg $ volume vs. cap-tier threshold), not a price/volume-confirmation signal. OBV trend/divergence exists as a separate informational card (Day 49) and VCP/Cup&Handle's volume-dry-up check exists inside pattern detection, but neither feeds the verdict or the checklist pass count. Adding it as a new criterion is cheap to code (OBV data already computed) but touches the frozen, already-backtested verdict logic — per Golden Rule 18/24, needs a fresh walk-forward/survivorship-free re-backtest before shipping, which would also reset the relevance of in-flight paper-trading trades validating the *current* logic. **Explicitly deferred until after the paper-trading 100-trade gate (Priority #1) clears.** Companion, much smaller item found in the same review: `mean_reversion.py`'s docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX — it's computed and returned as a `range_bound` info flag only. Likely a doc-accuracy fix (the code's ungated behavior may actually be closer to Connors' published RSI(2) method, which trades dips within an established uptrend, not specifically range-bound markets) rather than a logic bug — resolve alongside the volume work, same freeze-timing logic applies if the resolution is to add an actual ADX gate (that would be a re-tested entry-condition change, not a doc fix). | Design + re-backtest session (volume); trivial doc fix or re-backtest (ADX), post-freeze |
| 12 | **RESOLVED via Path B parallel experiment (Day 95) — see `PAPER_TRADING_PREREGISTRATION.md` §8b.** Originally found via a live TradingView-screener deep dive: momentum's live R:R check (`compute_entry_levels()`'s flat+8%/ATR-clamped-stop proxy) rejected 81% of Config-C-qualifying candidates, 45% hitting an exact 0.80 ceiling. An early fix attempt (widen the stop clamp floor to entry×0.85) was tested via a quick backtest sanity check and proved **directionally backwards** — wider stop = bigger risk = worse R:R, confirmed empirically (worse PF/Sharpe/drawdown on identical trades). Investigating why the trade set didn't change at all led to the real finding: `backtest_holistic.py`'s actual Config C entry gate has never used `compute_entry_levels()` at all — it computes R:R from real support/resistance levels (`risk=price-nearest_support`, `reward=nearest_resistance-price`), with the flat/ATR formula being exit-management logic only. `live_signals.py` has substituted the wrong piece of logic as its entry gate since Day 81 — a live/backtest divergence in the same bug class as Golden Rule 19. Built **Path B**: a parallel forward-test variant using the real S&R-based gate (`check_sr_gate()`), tracked under its own `variant='B_revised_rr'` ledger tag, same candidate pool as Path A, own 100-trade bar, zero impact on Path A's frozen count. Not deferred — this is a live/backtest coherence bug fix (tracked as a new experiment, not a threshold re-tune), so it didn't need to wait for the freeze to lift. Ongoing: let Path B accumulate alongside Path A and compare. | Done (Day 95) — ongoing accumulation, not a backlog item |

**Done as of Day 87:** Breakout Enhancement Plan (all phases), N4 Market Phase Synthesis, Price Structure Card Phase 2 — see their own COMPLETE sections above.
**Done as of Day 88:** Paper-trading ledger surfaced in the UI (Forward Test tab) with a manual trigger button — agreed as the one scoped exception to the freeze (directly aids the gate itself, not general product work).
**Done as of Day 91:** Session 28 audit's top-4 findings — Scan tab "Minervini" mislabel, Sectors tab false "100=parity"/data-source claims, Context tab CPI (real date-alignment bug, not caching) + PMI proxy relabel, paper-trading exit-rule integrity (replay now anchors to stored entry values). See Golden Rules 26-27.
**Done as of Day 92:** Paper-trading zombie-signal bug fixed (Golden Rule 28) + per-position ticker/entry/exit detail surfaced in the Forward Test tab. Confirmation bar raised 50→100 trades/system; forward-testing accumulation now the sole priority (Priority #1 below) — Priorities #2-11 explicitly parked until it clears.
**Done as of Day 93:** Sectors/Context tab audit — done independent of the freeze (pure UI/display work, no verdict/trading logic touched). Fixed the mid-cap-blind Cap Size banner, a bar-color/label contradiction, a full beginner-focused Sectors tab redesign, a real Day-91-regression composite bug and a Seasonal Regime text contradiction on the Context tab, and built a new Sectors↔Context macro-alignment connection plus a Market-Phase↔Macro-Regime reconciliation on the Context tab itself. Priority #10's "Rank #1 CTA" sub-item is now resolved (was stale-listed as open, corrected).

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
