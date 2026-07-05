# Breakout Trading Enhancement Plan

> **Purpose:** Actionable plan to close STA's breakout-trading gaps: candidates are found too late (no pivot-proximity scan), heard about too late (no EOD breakout watch), and the breakout-only entry variant has never been isolated in a backtest. Written to be executed by Claude (Sonnet) across sessions with no additional context needed.
> **Source:** Day 78 repo sweep (July 5, 2026) — inventory of existing breakout capability + gap analysis.
> **Location:** `docs/claude/design/`
> **Status:** NOT STARTED
> **Last Updated:** Day 78 (July 5, 2026)

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
| 2 — At-pivot flags in scan results | ❌ Feature — post-freeze | Phase 0 done + user lifts freeze (or explicitly approves) |
| 3 — EOD breakout watch skill | ❌ Feature — post-freeze | Phase 0 done + Phase 2 done |
| 4 — Gap-breakout detection (N3 tie-in) | ❌ Deferred post paper trading (already on roadmap as N3) | Paper trading underway + N3 research |

If the user says "start the breakout plan" without qualification: do Phase 0 now (if remediation Phase 2 is done), then ASK before building Phase 1+.

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

**The gaps this plan closes:**
- **G1:** No scan preset that finds *near-pivot* candidates market-wide — user finds breakouts only by analyzing tickers one at a time.
- **G2:** No visibility in scan results of which survivors are `at_pivot` right now.
- **G3:** No end-of-day "which watchlist stocks broke out today with volume" check.
- **G4:** Never isolated whether entering ONLY on confirmed breakouts (`broken_out` + volume confirmed) beats the current mixed entry (`forming` counts too).

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

## Phase 2 — At-Pivot Flags in Scan Results (post-freeze)

**Goal (G2):** after any scan, show which survivors have an actionable breakout setup *right now*, so the user analyzes the right 5 instead of eyeballing 50.

### Task 2.1 — Batch pattern-status endpoint
- **Status:** NOT STARTED
- **Effort:** 1 session
- **Files:** `backend/backend.py` (new endpoint `/api/patterns/batch`), reuse `detect_patterns()` unchanged
- **Design:**
  - POST with `{"tickers": [...]}`, hard cap 20 tickers per request (rate-limit protection).
  - For each ticker: fetch OHLCV through the existing DataProvider/cache path (cache-first — most scan survivors were just fetched), run `detect_patterns()`, return per ticker: best pattern name, status, confidence, pivot price, distance-to-pivot %, volume_confirmed.
  - Return partial results with per-ticker error entries rather than failing the batch (500-on-total-failure only, per Day 61 rule).
  - Respect provider rate limits: sequential with the existing rate limiter, or small thread pool ONLY if the N2 watchlist parallel-fetch pattern in `App.jsx`/backend already established one — read that code first and copy its approach.
- **Acceptance:** batch call for 10 known tickers returns statuses matching individual `/api/patterns/<ticker>` calls for at least 3 spot-checked tickers.

### Task 2.2 — Scan results badge column
- **Status:** NOT STARTED
- **Effort:** half session
- **Files:** `frontend/src/App.jsx` (scan results table), `frontend/src/services/api.js` (new `fetchPatternsBatch()`)
- **Design:**
  - After scan results render, fire ONE batch call for the top 20 rows (don't block initial render — badge column fills in when ready, mirroring the sector-badge async pattern already in the scan table).
  - Badge: `🎯 At Pivot` (yellow) / `🚀 Broken Out` (green, only if volume_confirmed — else gray "unconfirmed") / `— ` for none. Weight the emphasis per the Task 0.2 outcome (update this line after Phase 0).
  - React falsy gotcha: use explicit `!= null` checks, never `{value && ...}` with numeric distance values (Day 68 lesson).
- **Acceptance:** run a real scan; badges appear; clicking a badged row and opening full analysis shows the same pattern status (frontend-backend coherence spot-check on 3 tickers).

---

## Phase 3 — `/breakout-watch` EOD Skill (post-freeze)

**Goal (G3):** answer "which of my watchlist stocks broke out today?" on demand — no push infrastructure, no cron, deliberately minimal.

### Task 3.1 — Build the skill
- **Status:** NOT STARTED
- **Effort:** half session
- **Files:** `.claude/commands/breakout-watch.md` (follow the structure of `.claude/commands/sta-start.md`)
- **Design (skill instructions, executed by Claude at runtime):**
  1. Ticker source: argument list if given, else the Nirmal watchlist preset (read the ticker array from `App.jsx` — grep `Nirmal`), else ask.
  2. For each ticker call `/api/patterns/<ticker>` (backend must be running — check `/api/health` first, offer `./start.sh` if down).
  3. Report three buckets, most actionable first: **Broke out today/recently** (status `broken_out`, include volume confirmed Y/N + quality badge), **At pivot** (include distance-to-pivot %), **Approaching** (within 5% below pivot). Everything else: one summary line ("12 others: no setup").
  4. For broken-out names, append the verdict from `/api/mr`-style quick check? NO — keep scope tight: patterns only, then suggest "run full analysis on X" as the follow-up.
- **Acceptance:** `/breakout-watch AAPL NVDA PLTR` produces the three-bucket report against the live backend; a ticker with no pattern lands in the summary line, not an error.

---

## Phase 4 — Gap-Breakout Detection (pointer only — owned by N3)

- **Status:** DEFERRED (post paper trading, per existing roadmap N3)
- Breakaway gaps ARE breakout events; N3's `detect_gaps()` should classify gap type (breakaway / continuation / exhaustion) and feed the Phase 2 badge + Phase 3 skill when built. When N3 is picked up, extend — do not duplicate — this plan's surfaces.
- **Action now:** none. This section exists so N3's designer knows the consumers.

---

## Explicitly OUT of Scope

- **No changes to verdict logic, Config C thresholds, stops, targets, sizing** — the paper-trading config is frozen (see `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` once created by the remediation plan).
- **No intraday/real-time alerting, no push notifications, no cron jobs** — EOD on-demand only. Real-time is a different system with different data costs; requires its own research doc first.
- **No new pattern types** (H&S etc. — already rejected Day 48 research) and no changes to `pattern_detection.py` detection logic itself.
- **No auto-trading / order placement** via IBKR tools — analysis and surfacing only.

---

## Suggested Session Sequencing

| Session | Tasks | Gate |
|---------|-------|------|
| 1 | 0.1 + 0.2 (Config D/E backtest + interpretation) | After remediation Phase 2 |
| 2 | 1.1 + 1.2 (scan preset, backend + frontend) | User approves building during freeze — otherwise post-freeze |
| 3 | 2.1 (batch endpoint) | Post-freeze |
| 4 | 2.2 (badges) + 3.1 (skill) | Post-freeze |

**Relative priority:** the Fable Remediation Plan (`FABLE_REVIEW_REMEDIATION_PLAN.md`) outranks this entire plan. Paper trading outranks Phases 1–3. Phase 0 can slot into any backtest-focused session after remediation Phase 2.

---

## Progress Log

| Day | Tasks Completed | Notes |
|-----|-----------------|-------|
| — | — | Plan created Day 78, nothing executed yet |
