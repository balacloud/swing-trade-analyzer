# Known Issues — Day 112

> **Note (Day 116):** the OBV/volume entries below were updated in place — 3
> resolved, 3 new findings logged — for the Day 116 volume effort-vs-result
> work (`docs/claude/design/VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md`).
> **Note (Day 117):** below that, 3 more findings logged for the absolute-
> momentum informational read (`docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md`).
> This file's other entries still reflect Day 112; Day 113 (paper-trading
> program discontinued) and Day 114-115 changes are not otherwise captured
> here — no formal session close has run since Day 112. See
> `CLAUDE_CONTEXT.md` for the authoritative current-day pointer.

### RESOLVED (Day 117): absolute/dual momentum — gate decision unchanged, read now surfaced
**Was:** parked, low priority (Day 107/111). The Day 111 decision not to gate on Antonacci's
absolute-momentum leg (`Config G` backtested clean but excluded only 1 of 75 trades) **stands,
unchanged.** What changed: the read itself is now shown to the user — both the Simple
Checklist's Momentum card and the Full Analysis RS card display the stock's own trailing 1-year
return against a 5% cash proxy, informational only, sourced from the real Config G backtest
constant (`backtest_holistic.py:108`), not an invented number. Zero backend changes — both views
already had the underlying return computed; this exposes it. New module
`frontend/src/utils/absoluteMomentum.js`. Full writeup, including the algebraic reason the gate
barely mattered: `docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md`.

### Low: short-history tickers get a mismatched "52W Return" label on Full Analysis (new, Day 117)
**Severity:** Low. `backend.py`'s `price_52w_ago` falls back to the oldest available bar when a
ticker has `200 < len(hist_data) < 252` bars (e.g. a recent IPO) — so the Full Analysis view's
"Stock 52W Return" can be a ~250-bar return mislabeled as a full year, while the Simple
Checklist's Momentum criterion (which requires a true 252-bar history) correctly reports
"Insufficient data" for the same ticker. Live example found while verifying this session: STUB
(StubHub), n=251. Pre-existing (not introduced by Day 117's work), inherited by the new
absolute-momentum read on the Full Analysis side only. Not fixed — logged.

### Info: two independent 1-year-return calculations exist in the frontend, currently in agreement (new, Day 117)
`simplifiedScoring.js`'s inline RS calculation spans 251 bar-intervals (`n-1` to `n-252`);
`rsCalculator.js`'s (used by the Full Analysis view) spans the same 251 via `currentPrice`/
`price52wAgo`; the backtested `Config G` filter in `backtest_holistic.py` spans 252. Measured
bit-identical across 50 live tickers on 2026-09-16, with a traced common origin in `backend.py`'s
single `hist.tail(260)` slice — but two specific conditions could desync them (NaN-row skipping;
the short-history case above). Not a live bug today. Do not "fix" the 251-vs-252 mismatch by
changing `simplifiedScoring.js` — that line drives the live Momentum gate, and changing it is a
methodology change (Golden Rule 55), not a bug fix.

## Changes from Day 111

**Resolved / shipped this session:**
- **S&R `_pivot_sr()` extreme-vs-nearest bug (Golden Rule 53)** — FIXED.
  Nearest-to-price selection + merge-not-reject, behind `SRConfig.pivot_nearest_selection`.
  Verified live (META R1 $612.43 / 0.3% above vs. pre-fix extreme ~$745).
- **BUG-A** — `confluence_map` key-format mismatch that silently killed the ★
  confluence badge for ~10% of levels — FIXED (3 level-key maps unified to
  zero-padded 2dp). Verified live (★ renders on META's $600.00 support).
- **BUG-B** — Price Structure card's "nearest key levels" showed the two
  *deepest* supports — FIXED (`priceStructureNarrative.js`, one line).
- **Touch counts vanishing from the Price Structure card when the pivot S&R
  method won** — FIXED (`_score_levels` now runs on the pivot path).
- **Pattern Detection's flat-percentage price target (graded 1.5/10)** —
  Cup & Handle + Flat Base FIXED (measured-move: cup depth / base height from
  the pivot). VCP still on a flat +15% with a visible caveat — Phase 4.
- **The S&R fix scope decision (carried from Day 111)** — RESOLVED. Fix in
  place, accept the (now-moot) count reset — Path B was retired the same
  session, so `compute_sr_levels()` no longer feeds any live entry gate.
- **"What does Path B's cluster finding mean for the track"** — RESOLVED. Path B
  retired.

**New issues / findings this session:**
- Config C backtest canonical baseline moved **PF 0.97 → 0.53** on corrected
  S&R levels (the pre-fix number was partly a bug artifact — R:R inflated by a
  far resistance target). Not a bug — the honest number. Day 79's "PF 1.40"
  formally retired. See `SR_PIVOT_FIX_REBASELINE_DAY112.md`.

**Freeze status:** unchanged — forward-testing accumulation remains the sole
stated priority. Live numbers 2026-09-09: Path A 39 open / 74 closed
(43.24% WR, PF 1.1136), Path B (retired) 66 open / 166 closed (47.59% WR,
PF 1.0669, winding down), MR broad 30 open / 194 closed (77.32% WR, PF 2.5551 —
confirmed), MR HUB-65 1 open / 68 closed (64.71% WR, PF 1.7360).

---

## Open Issues

### Medium: MTF Confluence's confidence score is a hardcoded binary multiplier + counts synthetic projected levels in its denominator (carried from Day 111, plan written Day 112)
**Severity:** Medium
**Fix (planned, not actioned — Phase 3 of `SR_PIVOT_FIX_PLAN_DAY112.md` §4):**
wire `mtf_daily_weight`/`mtf_weekly_weight` into a real graduated score
(surface a Strong/Moderate/Weak *label*, keep the float in `meta`); exclude
`resistance_projected`/`support_projected` levels from `confluence_pct`'s
denominator (they can never be confluent with real weekly pivots and make the
40%/20% badge thresholds meaningless for ATH stocks). Also noted: the `strength`
field is currently *dead* — computed, serialized, read by nobody. Graded 3.0/10.
Low priority — display polish on an informational page.

### Low-Medium: Pattern Detection's VCP price target is still a flat +15% (carried from Day 111, C&H/Flat Base fixed Day 112)
**Severity:** Low-Medium
**Fix (planned — Phase 4 of the plan, §5):** primary = nearest real resistance
above the pivot from the corrected S&R; fallback = largest contraction's
measured move; neither → `null` + "no structural target" (never a flat %).
Needs `srData` threaded into `getActionablePatterns()`. Low priority.

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Severity:** High
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Severity:** Medium (verified zero impact on current position-size-invariant stats)
**Fix:** Not actioned — ties into the parked IBKR execution plan.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty — decision made, not implemented (carried from Day 111)
**Severity:** Medium
**Fix (decided, not implemented):** drop the investor-name labels, group the six
metrics under three functional headings (Efficiency & Quality, Valuation, Cash
Generation). Frontend-only.

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs a product decision.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Fix:** Mitigation choice still a pending user decision. Parked behind the paper-trading focus.

### Medium: Two batch endpoints (Sectors Rotation, Market Phase breadth) bypass circuit-breaker protection, no Tradier fallback (carried from Day 111)
**Severity:** Medium
**Fix:** Not actioned. `/api/mr/scan`'s bypass was fixed Day 111; these two remain.

### RESOLVED (Day 116): OBV trend direction was biased toward "rising" when cumulative OBV is negative
**Was:** Low-Medium. **Fix:** Shipped — `backend.py`'s `calculate_obv()` now compares
`current_obv` against `obv_sma ± 2%·abs(obv_sma)` instead of `obv_sma·1.02`/`obv_sma·0.98`,
which is sign-independent. Measured blast radius before shipping: 5/150 tickers changed
(all `rising`→`flat`, zero `rising`↔`falling` flips), and the `falling` set was verified
**bit-identical** before/after across the same 150-ticker sweep — proving the ⚠️ DIST badge
(the "needs its own review" blocker noted above) cannot change behavior, since it fires only
on `trend === 'falling'`. That review is done; this is why the fix was safe to ship. Full
writeup: `docs/claude/design/VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md` Section 3.

### RESOLVED (Day 116): calculate_obv()'s 20-day effort-vs-result read was live but invisible
**Was:** not previously logged as an issue, but functionally the same "volume gap" the Day
106/107 research spike investigated. `calculate_obv()`'s `signal` field (Day 49) already
computed the Wyckoff effort-vs-result comparison and already emitted "Bearish divergence -
distribution warning" / "Weak trend - price rising without volume support" — reachable only
by hovering the 30px OBV arrow chip. **Fix:** promoted into visible text on the Volume card
("Last 20 days: ...") via `getObvHorizonRead()` in `volumeThresholds.js`. Also added one
genuinely new read — same-day effort (RVOL) vs. same-day result (price move ÷ ATR%) via
`getEffortVsResultRead()` — since no existing function crossed those two. See
`VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md` Sections 4-5.

### NEW (Day 116) — RESOLVED same day: `meta.rvol` was computed from the still-forming intraday bar
**Severity was Medium.** `/api/sr`'s `rvol`/`candle` fields read `df.iloc[-1]` with no
partial-bar guard, unlike `paper_trading/live_signals.py`'s `_prepare_ohlcv()` (Day 99 fix,
same bug class, never ported to the display path — Golden Rule 47). Measured mid-session
2026-09-15: RVOL median 0.45 vs. 0.92 true (using the prior complete bar) — meant the Volume
Confirmation card, the ⚠️ DIST badge, and `priceStructureNarrative.js`'s breakout-watch line
all read as "light volume" for most of every trading day, regardless of actual participation.
**Fix:** `backend.py` now exposes `meta.candle.barComplete` (bool, ET market-hours test
mirroring `live_signals.py`'s guard) and `meta.prevBar` (the last complete bar's rvol/OHLC/
changePct/closeLocation). All three consumers above now read `prevBar` instead of the partial
bar when `barComplete` is false, with an explicit "last completed session" label so nothing
reads today's number under a today's-date claim. `currentPrice`/`volume`/`change` (the Day 85
Nirmal/Master Framework fields) deliberately left untouched — still today's live values.

### Low-Medium: `divergence`'s ±5% thresholds are scale-unstable across tickers (new, Day 116)
**Severity:** Low-Medium. `obv_change_pct`'s denominator (`abs(prev_obv)`) is an arbitrary
cumsum offset reset 260 bars ago, not a comparable scale between tickers — measured
`|obv_change_pct|` p50 = 20.6%, p90 = 99.5%, p99 = 1228% across 150 names. The ±5% divergence
threshold sits below the median for some tickers and is effectively unreachable for others.
**Direction is sound** (confirmed sign-safe, uses `abs()` in the denominator — does not share
the `trend` sign bug above), **magnitude is not**. **Fix:** Not actioned — re-thresholding is
a methodology change (Golden Rule 55), not a bug fix; disclosed in the UI copy instead
(`getObvHorizonRead()`'s JSDoc + the Volume card's tooltip).

### Low: same-day effort-vs-result thresholds are unbacktested (new, Day 116)
**Severity:** Low. `EFFORT_RESULT_LITTLE_PROGRESS_ATR`/`REAL_PROGRESS_ATR` (0.5/1.0 ATR) are
first-principles choices, disclosed as such in the rendered text ("thresholds are
first-principles, not backtested"). Display-only, gates nothing. Revisit if a future session
wants to calibrate against real trade outcomes.

### Low: `meta.candle.barComplete`'s market-hours test assumes US/Canadian exchange hours (new, Day 116)
**Severity:** Low. The new `barComplete` flag (`backend.py`) tests against `America/New_York`
market hours. Correct for US and TSX-listed tickers (hours match); would misreport for any
non-North-American listing reaching `/api/sr` (e.g. an NSE name whose session closed hours
earlier would still show `barComplete: false` all US trading day). Not fixed this pass — scope
unclear (which non-NA tickers actually reach this endpoint wasn't audited). Document only.

### Low-Medium: Momentum entry panel's position-size label is hardcoded, computed from nothing (carried from Day 109)
**Severity:** Low-Medium
**Fix:** Queued as part of the Analyze Page Redesign implementation.

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Severity:** Low-Medium
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call sites.

### Low: Seven unlinked copies of the 1.5x volume-confirmation threshold (carried from Day 111)
**Fix:** Not actioned — backend files. `pattern_detection.py`'s message-string literal is the most fragile.

### Low: Data Sources tab's field-source documentation is stale ("Defeat Beta API") (carried from Day 111)
**Fix:** Not actioned — part of the small cleanup batch.

### Low: `assessSentiment()` / `assessTechnical()` silent-fallback display states (carried from Day 109)
**Fix:** Display-layer only — queued alongside the redesign's context card.

### Low: VIX position-size multiplier ladder duplicated verbatim (carried from Day 109)
**Fix:** Extract to one exported `getVixPositionMultiplier()`.

### Low: Value tab's FCF Yield gets a pass/fail badge despite the spec saying it shouldn't (carried from Day 108)
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` latent short-date-range logic gap (carried from Day 108)
**Fix:** Worth a look before this function gets a new caller.

### Low: Analyze Page Redesign mockup's Regime band — RESOLVED Day 112 (was carried from Day 110)
Synced to the post-Day-110-reversal Info wording when the mockup artifact was
repaired this session.

### Low / Info: Simple Checklist's "PASS" badge misleading at low pass counts (carried from Day 106)
**Fix:** Copy fix specified in the redesign's §7.5, not applied.

### Low / Info: SRPS screener's R:R structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer covers it. *Day 112 note:*
the same class of issue as the `_pivot_sr` R:R inflation just fixed on the
Analyze page — the SRPS screener still uses `entry + 2.5×risk`, unchecked.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92);
Sector Rotation's original endpoint has no provider fallback (Day 94/103);
MR/momentum entry gates have no regime/sector-correlation awareness (Day 100 —
accepted design tradeoff; Path B's Aug 3–7 finding was a regime/timing variant);
HUB-65 backtest is selection-biased and not an independent sample from broad MR
(Day 98); momentum stop/target formula redesign still open (Day 95/96);
paper-trading launchd log doesn't capture manual/force-run activity (Day 95);
IBKR paper-execution CIRO question (Day 97); no scheduled/proactive breakout
alerting (Day 100); SimFin key rotation unconfirmed; Defeat Beta import present;
Master Framework / Nirmal / HUB-65 watchlist Name/Market Cap N/A by choice;
a genuinely missed paper-trading job run 2026-07-14 (not recoverable); FMP's
`get_provider_status()` hardcodes unlimited quota (inert, not in any active chain).
