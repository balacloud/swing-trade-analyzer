# Known Issues — Day 112

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

### Low-Medium: OBV trend direction is biased toward "rising" when cumulative OBV is negative (carried from Day 111)
**Severity:** Low-Medium
**Fix:** Not actioned — feeds a shipped live badge (Distribution Warning), needs its own review.

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
