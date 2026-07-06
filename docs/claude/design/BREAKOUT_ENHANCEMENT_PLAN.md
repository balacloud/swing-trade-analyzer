# Breakout Trading Enhancement Plan

> **Purpose:** Actionable plan to close STA's breakout-trading gaps: candidates are found too late (no pivot-proximity scan), heard about too late (no EOD breakout watch), and the breakout-only entry variant has never been isolated in a backtest. Written to be executed by Claude (Sonnet) across sessions with no additional context needed.
> **Source:** Day 78 repo sweep (July 5, 2026) — inventory of existing breakout capability + gap analysis.
> **Reconciled:** Day 78, session 2 (July 6, 2026) — a parallel session independently built a standalone breakout classification engine (`backend/breakout_detection.py` + `breakout_routes.py` + `BREAKOUT_ENGINE_SPEC.md` + Pine companion + human-in-the-loop workflow docs). See "Reconciliation" section below for what changed in this plan as a result.
> **Location:** `docs/claude/design/`
> **Status:** Phase 1.5 DONE (Day 78, session 3) — `/api/breakout/<ticker>` wired and behaviorally validated on 5 tickers + 1 edge case. Phase 0 NOT STARTED. Phase 1 NOT STARTED. Phases 2–3 ready to start (prerequisite met).
> **Last Updated:** Day 78, session 3 (July 6, 2026)

---

## How to Use This Document (instructions for executing Claude)

1. **Check the gating table first** (next section). Phases have different freeze/sequencing rules — do not start a gated phase early.
2. Execute phases in order; within a phase, tasks in order unless marked independent.
3. One task at a time: read the target file, make the change, verify acceptance criteria, update the task's Status line in this file (Golden Rules #2, #7, #13).
4. **Golden Rule #15 applies:** Phase 0 (validation) MUST complete before Phases 2–4 are built. Phase 1 is exempt (it is a funnel/filter, not a signal — it changes which tickers get analyzed, never what the verdict says).
5. **Never touch the frozen paper-trading config.** Nothing in this plan may alter Config C thresholds, verdict logic, stops, targets, or sizing. New configs (e.g., Config D) are additive backtest experiments only.
6. At session close, follow the SESSION CLOSE PROTOCOL in `CLAUDE_CONTEXT.md`.

---

## Gating: When Each Phase May Run

| Phase | Freeze-compatible? | Prerequisite |
|-------|-------------------|--------------|
| 0 — Breakout-only backtest validation | ✅ Yes (research/validation, no product code) | **Fable Remediation Plan Phase 2 complete** (gap-aware fills + MR costs) — validating on the optimistic simulator would repeat the mistake the remediation plan fixes |
| 1 — Breakout scan preset | ⚠️ Small feature — needs explicit user approval to build during freeze | User go-ahead |
| **1.5 — Wire `/api/breakout/<ticker>`** (NEW, Day 78 reconciliation) | ✅ Yes — read-only classification endpoint, zero verdict/scoring impact | ✅ **DONE (Day 78, session 3)** — wired + validated |
| 2 — At-pivot flags in scan results (REDESIGNED) | ❌ Feature — post-freeze | Phase 1.5 done (✅ met) + Phase 0 done |
| 3 — EOD breakout watch skill (REDESIGNED) | ❌ Feature — post-freeze | Phase 1.5 done + Phase 2 done |
| 4 — Gap-breakout detection (N3 tie-in) | ❌ Deferred post paper trading (already on roadmap as N3) | Paper trading underway + N3 research |

If the user says "start the breakout plan" without qualification: do Phase 0 now (if remediation Phase 2 is done), then ASK before building Phase 1+.

**Cross-reference:** a follow-on "Institutional Flow" context layer (`backend/institutional_flow.py`, `/api/flow/<ticker>` — states like `CONSTRUCTIVE_FLOW`/`DISTRIBUTION_WARNING`) is proposed in `docs/claude/design/BREAKOUT_FLOW_NEXT_STEPS_HANDOFF.md` §9–12, explicitly gated on Phase 1.5 being wired and validated first. It is NOT part of this plan — don't build it here, just don't duplicate it either if picked up later.

---

## Background: What Already Exists (do NOT rebuild)

Breakout trading is already STA's core momentum entry model:

| Capability | Where | Notes |
|------------|-------|-------|
| VCP / Cup & Handle / Flat Base detection with pivot prices | `backend/pattern_detection.py`, `/api/patterns/<ticker>` | Status lifecycle: `forming → at_pivot → broken_out`; trigger/stop/target at ≥60% confidence |
| Breakout quality (false-breakout defense) | `check_breakout_quality()` — `pattern_detection.py:80` | Volume ≥1.5x 50d avg, 3-day follow-through, High/Med/Low badge, "within 2% of pivot" watch state |
| Pivot point primitive | `find_pivot_points()` — `pattern_detection.py:56` | Also earmarked for Price Structure Phase 2 |
| Frontend surfacing | `categoricalAssessment.js:81-105` (actionable patterns), `priceStructureNarrative.js` ("Breakout watch: near R1…", ATH blue-sky rule TT≥5) | |
| Breakout vs pullback decision | ADX entry preference (≥25 momentum / 20–25 pullback) | In verdict output |
| Dual entry (breakout primary + averaging secondary) | N1 labels in Trade Setup; `docs/research/Dual_Entry_Strategy_Complete_Guide.md` | |
| Backtested | Config B/C require actionable pattern (`at_pivot`/`broken_out`/`forming`, ≥60% conf) | PF 1.61 is substantially a breakout-pattern result |
| IBKR pre-screen tie-in | Filter #8 "52W High Proximity" in `docs/research/IBKR_SCREENER_INTEGRATION.md` | Breakout-proximity filter at funnel stage |

### NEW (Day 78, session 2 reconciliation) — Standalone Breakout Classification Engine

A parallel session independently built a second, more sophisticated breakout classifier. It is **fully additive** — separate endpoint, does not touch `pattern_detection.py`, S&R engine, categorical assessment, or Config C. Zero collision with the frozen paper-trading config.

| Capability | Where | Notes |
|------------|-------|-------|
| 8-state breakout classifier | `backend/breakout_detection.py` — `detect_breakout()` | States: `NOT_READY`, `BUILDING_BASE`, `BREAKOUT_WATCH`, `BREAKOUT_CONFIRMED`, `RETEST_ENTRY`, `SUPPLY_WARNING`, `FAILED_BREAKOUT`, `EXTENDED_CHASE_RISK` — richer than `pattern_detection.py`'s 3-state lifecycle |
| Gates used | Trend (SMA50>SMA200 rising), RS vs SPY (ratio > 20-bar avg), volume (RVOL ≥1.5x, dry-up), ATR contraction, **candle quality** (close location, body%, upper wick%, range vs ATR), extension-from-SMA50 cap (12%), retest zone, failed-breakout detection | Candle-quality and RS-ratio-vs-its-own-MA gates are new — not present anywhere else in STA |
| Route (not wired) | `backend/breakout_routes.py` — `register_breakout_routes()`, target `GET /api/breakout/<ticker>` | **⚠️ NOT called from `backend.py` — confirmed via grep, zero matches. The endpoint does not work yet.** |
| Spec | `docs/claude/design/BREAKOUT_ENGINE_SPEC.md` | Single source of truth for state definitions — v1, explicitly "not yet performance-validated" (spec's own §19 audit verdict: PLAUSIBLE) |
| Handoff / next-steps doc | `docs/claude/design/BREAKOUT_FLOW_NEXT_STEPS_HANDOFF.md` | Says wiring the route is the smallest next step; explicitly defers frontend badge, institutional flow, IBKR automation until wired + validated on IBM/MSFT/NVDA/PLTR |
| Visual companion | `pine/sta_breakout_companion.pine` (v2, 167 lines) | TradingView Pine script mirroring the same states, for manual chart review |
| Manual review workflow | `docs/STA_BREAKOUT_HUMAN_IN_LOOP_WORKFLOW.md` + `prompts/STA_CLAUDE_CHART_REVIEW_PROMPT.md` | Screenshot → Claude/GPT review flow — a **different, manual modality** from this plan's Phase 3 (which is API-driven, not screenshot-driven). Complementary, not duplicated. |
| Responsibility split (per spec §2) | Screener = candidate discovery; Breakout Engine = state classification; Pine = visual mirror; Claude/GPT = contextual chart review; Human = decision; Forward Test = validation | Confirms Phase 1 (scan preset = discovery) and this engine (classification) are different layers, not duplicates |

**The gaps this plan closes (updated):**
- **G1:** No scan preset that finds *near-pivot* candidates market-wide — user finds breakouts only by analyzing tickers one at a time. **(Unaffected by the new engine — still a real gap; see spec's own responsibility-split table above.)**
- **G2:** No visibility in scan results of which survivors have an actionable breakout setup right now. **(REDESIGNED — Phase 2 now surfaces the new engine's 8-state classification instead of the plainer pattern-status data, once wired.)**
- **G3:** No end-of-day "which watchlist stocks broke out today with volume" check. **(REDESIGNED — Phase 3's skill now calls `/api/breakout/<ticker>` and buckets by its state vocabulary instead of pattern status.)**
- **G4:** Never isolated whether entering ONLY on confirmed breakouts (`broken_out` + volume confirmed) beats the current mixed entry (`forming` counts too). **(Unaffected — this tests the existing `pattern_detection.py`-based Config C entries, a different system from the new engine, which isn't backtested or wired yet.)**

---

## Phase 0 — Validation First: Isolate the Breakout-Only Edge (freeze-compatible)

**Why:** Config C currently fires on `forming` patterns too (`backtest_holistic.py:346` accepts `'at_pivot', 'broken_out', 'complete', 'forming'`). Nobody has measured whether waiting for the confirmed breakout is better or worse. This is cheap to answer with existing infrastructure and directly informs Phases 2–3.

### Task 0.1 — Add Config D (breakout-confirmed entries) to the holistic backtest
- **Status:** NOT STARTED
- **Effort:** half session
- **Prerequisite:** Fable Remediation Plan Tasks 2.1–2.2 complete (gap-aware fills). Verify before starting: `grep -n "open_day" backend/backtest/trade_simulator.py` should show the gap-fill logic. If absent, STOP and do remediation Phase 2 first.
- **Action:**
  1. In `backend/backtest/backtest_holistic.py`, add Config D to `check_entry_signals()`: same as Config C, but pattern status must be `broken_out` AND the pattern's breakout must be volume-confirmed. Pull volume confirmation from the pattern dict (`p.get('breakout', {}).get('volume_confirmed')` — verify the exact key by reading `pattern_detection.py` output structure first; do not guess, Golden Rule #3).
  2. Add `'D'` to the CLI `--configs` choices and the HTML report legend ("Config D: C but breakout-confirmed only — no forming/at_pivot entries").
  3. Also add Config E if cheap: C restricted to `at_pivot` + `forming` only (the complement), so the comparison is clean three-way: mixed (C) vs confirmed-only (D) vs anticipatory-only (E).
- **Acceptance:** `python backend/backtest/backtest_holistic.py --configs C D E --walk-forward` runs; results saved.

### Task 0.2 — Interpret with pre-committed criteria
- **Status:** NOT STARTED
- **Effort:** 1–2 hours (same session as 0.1)
- **Pre-committed interpretation (written before results exist, to prevent narrative-fitting):**
  - D meaningfully beats C (net PF ≥ +0.15 with ≥60% of C's trade count) → breakout confirmation adds edge → Phases 2–3 should emphasize `broken_out` + volume-confirmed states.
  - D ≈ C → confirmation is neutral → Phases 2–3 surface both `at_pivot` and `broken_out` equally.
  - D worse OR trade count collapses (<40% of C) → confirmation costs more (later entry) than it saves → keep current mixed logic, and Phases 2–3 emphasize `at_pivot` (early) candidates instead.
  - **In every case: change nothing in the live/frozen system.** This informs how new surfaces rank candidates, not the verdict.
- **Action:** Write results + verdict-per-criteria into `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY[N].md`. Update this plan's Phase 2/3 emphasis notes accordingly.
- **Acceptance:** results doc exists; ROADMAP gets a one-line entry under RESEARCH COMPLETED.

---

## Phase 1 — "Near Breakout" Scan Preset (small, isolated; needs user OK during freeze)

**Goal (G1):** a 6th scan strategy that finds Stage-2 stocks *approaching or crossing* new-high territory, market-wide, so the pattern engine has better raw material.

### Task 1.1 — Backend scan strategy `breakout`
- **Status:** NOT STARTED
- **Effort:** half session
- **Files:** `backend/backend.py` (scan endpoint strategy branch ~line 1830 + `get_scan_strategies()` ~line 1960)
- **Design (approximates "near pivot" with TradingView-available fields):**
  - Base quality: price > $10, avg dollar volume ≥ $5M, market cap ≥ $2B, price above SMA50 and SMA200 (Stage 2 basics — mirror the existing `minervini`/`best` strategy code style).
  - Proximity: price within **8% of its 52-week high** (Minervini: buy zones emerge near highs, not 25% below).
  - Not overextended: RSI 50–70 (reuse existing pattern from `momentum` strategy).
  - Trend: ADX ≥ 20 if available as a TradingView field; otherwise omit (STA computes ADX per-ticker later anyway).
- **⚠️ TradingView scanner gotchas (from hard-won project experience — see MEMORY):**
  1. `col()` objects do NOT support arithmetic → you cannot express `close >= High.52W * 0.92` in the query. **Workaround:** SELECT both `close` and the 52W-high field, fetch a wider result set (e.g., top 300 by volume), then filter `close >= high_52w * 0.92` in pandas after the query returns.
  2. Verify the exact 52W-high field name with a diagnostic query FIRST (Golden Rule #11) — candidates: `'High.52W'`, `'price_52_week_high'`. Print available columns on a 5-row test query before writing the filter.
  3. Do NOT combine with `set_index()` unless tested — index filter resets market to `/global` (known gotcha).
- **Acceptance:** `curl "localhost:5001/api/scan/tradingview?strategy=breakout"` returns a non-empty ticker list; spot-check 3 tickers manually — each must actually be within ~8% of its 52W high (exhaustive on the spot-check set, Golden Rule #13).

### Task 1.2 — Frontend dropdown entry
- **Status:** NOT STARTED
- **Effort:** 30 min
- **Files:** `frontend/src/App.jsx` (scan strategy dropdown — find by grepping for existing strategy ids `'minervini'`/`'best'`)
- **Action:** Add "🚀 Near Breakout" option wired to `strategy=breakout`. Description text: "Stage 2 stocks within 8% of 52-week high — candidates approaching a pivot."
- **Acceptance:** scan runs end-to-end from the UI; results render with existing sector/RS columns intact.

---

## Phase 1.5 — Wire the Standalone Breakout Engine (NEW, Day 78 reconciliation)

**Why this comes first:** a parallel session built `backend/breakout_detection.py` (8-state classifier — see inventory above) but never registered its route. Everything downstream in this plan's Phase 2–3 is redesigned to consume this engine instead of `pattern_detection.py`, so it must be wired and behaviorally validated before Phase 2 starts. This is also literally the next action specified in `BREAKOUT_FLOW_NEXT_STEPS_HANDOFF.md` §6, §16 — executing it here keeps both plans in sync instead of duplicating the instruction in two files.

### Task 1.5.1 — Register the breakout route in backend.py
- **Status:** DONE (Day 78, session 3) — wired exactly as specified: optional import block after the `pattern_detection` import (backend.py ~line 106), `register_breakout_routes(app, get_data_provider, yf, DATA_PROVIDER_AVAILABLE)` called right after `CORS(app)`. Backend starts clean, log shows "✅ Breakout Routes loaded successfully", `/api/health` still returns 200.
- **Effort:** 15 min
- **Files:** `backend/backend.py`
- **Action:** Read `backend/backend.py` in full first (Golden Rule #2/#3 — do not patch from the handoff doc's snippet alone). Add the optional import near the other optional-feature imports (same try/except pattern as `DATA_PROVIDER_AVAILABLE`, `VALIDATION_AVAILABLE`, etc.):
  ```python
  try:
      from breakout_routes import register_breakout_routes
      BREAKOUT_ROUTES_AVAILABLE = True
      print("✅ Breakout Routes loaded successfully")
  except ImportError as e:
      BREAKOUT_ROUTES_AVAILABLE = False
      print(f"⚠️ Breakout Routes not available: {e}")
  ```
  Then, after `app = Flask(__name__)` / `CORS(app)`:
  ```python
  if BREAKOUT_ROUTES_AVAILABLE:
      register_breakout_routes(app, get_data_provider, yf, DATA_PROVIDER_AVAILABLE)
  ```
  Do not refactor unrelated code. Do not modify `/api/sr/<ticker>` or `/api/patterns/<ticker>`.
- **Acceptance:** backend starts without crash; `curl localhost:5001/api/health` still returns 200.

### Task 1.5.2 — Behavioral validation on real tickers
- **Status:** DONE (Day 78, session 3). All 6 tickers returned HTTP 200 with complete, non-fabricated JSON (`status`/`checks`/`warnings`/`evidence` present; missing fields like `retestZoneLow/High` correctly `null`, not 0, when no recent breakout existed):
  - **IBM** → `FAILED_BREAKOUT` (recent breakout to 327.98 21 bars ago, current 289.52 well below retest tolerance — sane)
  - **MSFT** → `FAILED_BREAKOUT` (recent breakout to 450.33, pulled back hard to 390.49 — sane)
  - **NVDA** → `NOT_READY` (trendOk=false, rsStrong=false — no bullish signal fabricated)
  - **PLTR** → `NOT_READY` (weak candle, rejectionCandle=true — consistent, no false positive)
  - **INTC** (weak-downtrend pick) → `FAILED_BREAKOUT`, rsStrong=false, `breakoutConfirmed=false` — correctly did NOT return `BREAKOUT_CONFIRMED`
  - **Invalid ticker** (edge case, not in spec's matrix but checked anyway) → clean HTTP 404 `{"error": "No data found..."}`, no crash, no fabricated 200
  - Pine cross-check: NOT done (optional per the task; skip is acceptable per the plan's own wording).
- **Acceptance:** MET. No discrepancies found requiring diagnosis. Engine considered validated for Phase 2 badge consumption.

---

## Phase 2 — Breakout State Badges in Scan Results (post-freeze) — REDESIGNED Day 78

**Goal (G2):** after any scan, show which survivors have an actionable breakout setup *right now*, so the user analyzes the right 5 instead of eyeballing 50. **Now consumes the new 8-state `breakout_detection.py` engine instead of the plainer `pattern_detection.py` status** — richer signal (candle quality, RS-vs-benchmark, supply warnings, retest/failed-breakout), same UI slot.

### Task 2.1 — Batch breakout-status endpoint
- **Status:** NOT STARTED
- **Effort:** 1 session
- **Prerequisite:** Phase 1.5 complete (route wired + behaviorally validated).
- **Files:** `backend/backend.py` (new endpoint `/api/breakout/batch`), reuse `breakout_detection.detect_breakout()` unchanged
- **Design:**
  - POST with `{"tickers": [...]}`, hard cap 20 tickers per request (rate-limit protection).
  - For each ticker: fetch OHLCV + SPY benchmark through the existing DataProvider/cache path (cache-first — most scan survivors were just fetched — mirror `_fetch_ohlcv()` in `breakout_routes.py`), run `detect_breakout()`, return per ticker: `status`, `humanAction`, `breakoutLevel`, `rvol`, key `checks`/`warnings`.
  - Return partial results with per-ticker error entries rather than failing the batch (500-on-total-failure only, per Day 61 rule).
  - Respect provider rate limits: sequential with the existing rate limiter, or small thread pool ONLY if the N2 watchlist parallel-fetch pattern in `App.jsx`/backend already established one — read that code first and copy its approach.
- **Acceptance:** batch call for 10 known tickers returns statuses matching individual `/api/breakout/<ticker>` calls for at least 3 spot-checked tickers.

### Task 2.2 — Scan results badge column
- **Status:** NOT STARTED
- **Effort:** half session
- **Files:** `frontend/src/App.jsx` (scan results table), `frontend/src/services/api.js` (new `fetchBreakoutBatch()`)
- **Design:**
  - After scan results render, fire ONE batch call for the top 20 rows (don't block initial render — badge column fills in when ready, mirroring the sector-badge async pattern already in the scan table).
  - Badge per `BREAKOUT_ENGINE_SPEC.md` §13 frontend display rules: `BREAKOUT_CONFIRMED` green, `RETEST_ENTRY` blue, `BREAKOUT_WATCH` amber, `BUILDING_BASE` gray, `SUPPLY_WARNING`/`FAILED_BREAKOUT` red, `EXTENDED_CHASE_RISK` orange, `NOT_READY` muted/hidden. **Do not display a green badge as a buy recommendation** (spec's explicit rule) — badge text should read as state, not signal (e.g. "Breakout Confirmed" not "Buy").
  - React falsy gotcha: use explicit `!= null` checks, never `{value && ...}` with numeric distance values (Day 68 lesson).
- **Acceptance:** run a real scan; badges appear; clicking a badged row and opening full analysis is consistent with the badge state (frontend-backend coherence spot-check on 3 tickers).

---

## Phase 3 — `/breakout-watch` EOD Skill (post-freeze) — REDESIGNED Day 78

**Goal (G3):** answer "which of my watchlist stocks broke out today?" on demand — no push infrastructure, no cron, deliberately minimal. **Now buckets by the new engine's 8-state vocabulary.** This is a different, API-driven modality from the parallel session's screenshot-based `STA_CLAUDE_CHART_REVIEW_PROMPT.md` workflow — both are useful; this skill is faster for a daily watchlist sweep, the screenshot workflow is deeper for one ticker under real chart-visual review.

**Naming note:** the engine has a literal state called `BREAKOUT_WATCH`; the skill is named `/breakout-watch`. Not a real conflict (the skill reports across all 8 states, not just that one) but worth being precise about in the skill's own help text so a user doesn't conflate "run `/breakout-watch`" with "show me only `BREAKOUT_WATCH` tickers."

### Task 3.1 — Build the skill
- **Status:** NOT STARTED
- **Effort:** half session
- **Prerequisite:** Phase 1.5 complete.
- **Files:** `.claude/commands/breakout-watch.md` (follow the structure of `.claude/commands/sta-start.md`)
- **Design (skill instructions, executed by Claude at runtime):**
  1. Ticker source: argument list if given, else the Nirmal watchlist preset (read the ticker array from `App.jsx` — grep `Nirmal`), else ask.
  2. For each ticker call `/api/breakout/<ticker>` (backend must be running — check `/api/health` first, offer `./start.sh` if down).
  3. Report bucketed by state priority, most actionable first: **Confirmed breakouts** (`BREAKOUT_CONFIRMED` — include RVOL, human-readable action text), **Retest entries** (`RETEST_ENTRY`), **Watch** (`BREAKOUT_WATCH`), **Warnings** (`SUPPLY_WARNING`/`FAILED_BREAKOUT`/`EXTENDED_CHASE_RISK` — surface these prominently, they're risk flags not opportunities), **Building base** (`BUILDING_BASE`). Everything `NOT_READY`: one summary line ("12 others: not ready").
  4. Always append the engine's own `humanAction` text verbatim per ticker — do not paraphrase it into a stronger claim. Never state a green badge as a buy recommendation (per spec §13/§15 — this is a hard rule, not a style choice).
  5. Keep scope tight: breakout state only, then suggest "run full analysis on X" as the follow-up.
- **Acceptance:** `/breakout-watch AAPL NVDA PLTR` produces the bucketed report against the live backend; a ticker returning `NOT_READY` lands in the summary line, not treated as an error.

---

## Phase 4 — Gap-Breakout Detection (pointer only — owned by N3)

- **Status:** DEFERRED (post paper trading, per existing roadmap N3)
- Breakaway gaps ARE breakout events; N3's `detect_gaps()` should classify gap type (breakaway / continuation / exhaustion) and feed the Phase 2 badge + Phase 3 skill when built. When N3 is picked up, extend — do not duplicate — this plan's surfaces.
- **Action now:** none. This section exists so N3's designer knows the consumers.

---

## Explicitly OUT of Scope

- **No changes to verdict logic, Config C thresholds, stops, targets, sizing** — the paper-trading config is frozen (see `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md`, created Day 78 session 2). The new breakout engine (Phase 1.5–3) is exempt from this constraint since it's a read-only classification endpoint with no wiring into verdict/scoring — but do not let it grow into a verdict input without an explicit backtest + user decision.
- **No building the Institutional Flow layer** (`institutional_flow.py`, `/api/flow/<ticker>`) — proposed in the handoff doc but explicitly gated on Phase 1.5 being wired + validated. Not in scope for this plan.
- **No intraday/real-time alerting, no push notifications, no cron jobs** — EOD on-demand only. Real-time is a different system with different data costs; requires its own research doc first.
- **No new pattern types** (H&S etc. — already rejected Day 48 research) and no changes to `pattern_detection.py` detection logic itself.
- **No auto-trading / order placement** via IBKR tools — analysis and surfacing only.

---

## Suggested Session Sequencing

| Session | Tasks | Gate |
|---------|-------|------|
| 1 | 0.1 + 0.2 (Config D/E backtest + interpretation) | After remediation Phase 2 |
| 2 | **1.5.1 + 1.5.2 (wire + validate the existing breakout engine)** | None — smallest, highest-leverage next step; freeze-compatible |
| 3 | 1.1 + 1.2 (scan preset, backend + frontend) | User approves building during freeze — otherwise post-freeze |
| 4 | 2.1 (batch endpoint) | Post-freeze, needs Phase 1.5 done |
| 5 | 2.2 (badges) + 3.1 (skill) | Post-freeze |

**Relative priority:** the Fable Remediation Plan (`FABLE_REVIEW_REMEDIATION_PLAN.md`) outranks this entire plan. Paper trading outranks Phases 1–3. Phase 0 can slot into any backtest-focused session after remediation Phase 2.

---

## Progress Log

| Day | Tasks Completed | Notes |
|-----|-----------------|-------|
| — | — | Plan created Day 78, nothing executed yet |
| 78, session 2 | Reconciliation only (no plan tasks executed) | Discovered parallel session's standalone breakout engine (`breakout_detection.py`/`breakout_routes.py`/spec/Pine/handoff docs). Added new Phase 1.5 (wire + validate the engine — NOT STARTED). Redesigned Phase 2/3 to consume its 8-state classification instead of `pattern_detection.py` status. Phase 0/1/4 unaffected. Confirmed via grep: route is NOT wired into `backend.py` — `/api/breakout/<ticker>` does not work yet. |
| 78, session 3 | Tasks 1.5.1 + 1.5.2 (Phase 1.5 complete) | Wired `register_breakout_routes()` into `backend.py` per spec. Started backend, confirmed clean load ("✅ Breakout Routes loaded successfully"), validated `/api/breakout/<ticker>` on IBM/MSFT/NVDA/PLTR/INTC + 1 invalid-ticker edge case — all HTTP 200 (404 for invalid), no fabricated values, no false `BREAKOUT_CONFIRMED` on weak names. Stopped the test backend process cleanly afterward. Phase 2/3 now unblocked. |
