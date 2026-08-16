# Known Issues — Day 109

## Changes from Day 108

**Resolved this session:** none — this was a design-only session, zero
application code touched. Nothing from Day 108's list was fixed.

**New issues found this session** (via direct code tracing while designing
the Analyze Page Redesign — see
`docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` for full detail on
each): a hardcoded, uncomputed position-size label; two silent-fallback
states in the categorical assessment engine; a duplicated VIX-multiplier
threshold ladder. Added below.

**Existing item updated, not resolved:** the "3 different R:R minimums"
non-finding (closed Day 108) now has much fuller documentation as "4
different R:R formulas" in the new design doc's §4 — the closed item's own
entry is left as-is below since it's still correctly closed as not-a-bug;
the fuller documentation lives in the design doc, not here.

**Freeze status:** unchanged — forward-testing accumulation remains the sole
stated priority. Live numbers not re-pulled this session; last live check
remains Day 108 (2026-08-14): Path A 34 open/30 closed, Path B 81 open/44
closed, MR broad 6 open/**90 closed** (closest to its 100-trade bar), MR
HUB-65 2 open/30 closed.

---

## Open Issues

### Low-Medium: Momentum entry panel's position-size label is hardcoded, computed from nothing (new, Day 109)
**Severity:** Low-Medium
**Description:** `App.jsx:1939-1940` — the Momentum entry-strategy panel's
"Position" field renders a literal `<span className="text-yellow-400">
half</span>`, with a tooltip implying it's a computed recommendation
("'Half' = reduced position due to higher risk..."). It is not computed
from anything — no ADX, ATR, or risk calculation feeds it. Confirmed by
direct code read. On screen, unchanged, since Day 39 (60+ days).
**Fix:** Queued as part of the Analyze Page Redesign implementation
(§7.2 of the design doc) — the entire `Position` row is being deleted from
both entry panels in favor of raw sizing inputs. Not fixed standalone this
session since the redesign's implementation hasn't started.

### Low: `assessSentiment()` silently defaults to "Neutral" on fetch failure (new, Day 109)
**Severity:** Low
**Description:** `categoricalAssessment.js:463-470` returns
`assessment: 'Neutral'` with reason "Fear & Greed data unavailable -
defaulting to neutral" when the F&G fetch fails — indistinguishable in the
UI from a genuine Neutral reading. The data already carries a distinct
`rating: 'Unavailable'` field (`:468`) that isn't surfaced. Same
silent-fallback shape `GOLDEN_RULES.md`'s Data Integrity section already
names (Day 54: "VIX=20 on failure, F&G=50 on error mask real problems").
**Fix:** Display-layer only — queued alongside the Analyze Page Redesign's
Fundamentals/Sentiment context card (§7.4), not fixed standalone.

### Low: `assessTechnical()` collapses "pattern detection unavailable" and genuine "Weak" into one state (new, Day 109)
**Severity:** Low
**Description:** `categoricalAssessment.js:274-275` and `:293-294` — both
"the backend's pattern detector failed to return trend template data" and
"this stock is in a genuine Stage-4 decline" render identically as a red
`Weak` assessment. Same failure shape as Golden Rule 44 (a status that can
be empty for more than one reason must not collapse into one glyph), one
card over from where it was already fixed on the Scan tab.
**Fix:** A 4th display state ("Unavailable") is specified for the
redesigned Technical Read (design doc, item 1) — not a change to
`assessTechnical()` itself, so no parity risk. Not implemented this
session.

### Low: VIX position-size multiplier ladder duplicated verbatim, silently defaults on missing data (new, Day 109)
**Severity:** Low
**Description:** The identical `vixMultiplier` threshold ladder
(`vix<20→1.0, 20-30→0.75, >30→0.50`) is hand-copied at `App.jsx:359` and
`App.jsx:381` (Code Architecture Rule 7 DRY violation). Both read
`rawAnalysisData?.vix?.current`, which is `undefined` if the calculator is
opened without first analyzing a stock — silently defaulting to `1.0×`
(full size) with no indication VIX was actually unknown, another Day-54
silent-fallback shape.
**Fix:** Extract to one exported `getVixPositionMultiplier()` in
`positionSizing.js` with an explicit "VIX unknown" path, queued as part of
the redesign's Phase 1 (§7.1). Not implemented this session.

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Severity:** High
**Fix:** Not actioned — needs a new failure-tracking mechanism, scoped as
its own session.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Severity:** Medium (verified zero impact on current live-track statistics)
**Fix:** Not actioned — ties into the parked IBKR execution plan.

### Medium: Pivot support/resistance method selects extreme levels, not nearest (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — revisit once the freeze lifts. Note: this same
finding is now also documented in the Analyze Page Redesign's §4 R:R
landscape table, since every R:R shown on the Analyze page is built on
these levels.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to
throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs the user's call on replacement copy.

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs a product decision.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live and backtested
Fundamental labels — this exact figure is now also the load-bearing
evidence behind the Analyze Page Redesign's Fundamentals red-flag
thresholds (design doc §5).
**Fix:** Mitigation choice still a pending user decision. Parked behind the
paper-trading focus.

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Severity:** Low-Medium
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call
sites — a small, contained backend change.

### Low: Value tab's FCF Yield gets a pass/fail badge despite the design spec saying it shouldn't (carried from Day 108)
**Severity:** Low
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` has a latent short-date-range logic gap (carried from Day 108)
**Severity:** Low
**Fix:** Worth a proper look before this function gets a new caller.

### Low / Info: Volume confirmation — first design tested, too restrictive as implemented (carried from Day 107)
**Fix:** Not actioned — needs a genuinely different design.

### Low / Info: Dual/absolute momentum — tested clean, near-inert in practice (carried from Day 107)
**Fix:** Not actioned — low priority.

### Low / Info: SimFin ticker-universe drift affects seed-based backtest reproducibility (carried from Day 107)
**Fix:** Not actionable — informational.

### Low / Info: Simple Checklist's "PASS" badge is misleading at low pass counts (carried from Day 106)
**Severity:** Low / Info
**Fix:** Not actioned. **Update, Day 109:** the exact zero-risk copy fix
(`0/9 criteria met — No Trade`) is now specified in the Analyze Page
Redesign's §7.5 as a bundled bonus fix — still not applied, since
implementation hasn't started.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer already covers
this.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); Sector
Rotation's original endpoint has no provider fallback (Day 94/103);
MR/momentum entry gates have no regime/sector-correlation awareness (Day
100, accepted design tradeoff); HUB-65 backtest is selection-biased by
construction (Day 98); HUB-65 and broad MR aren't independent samples (Day
98); momentum's stop/target formula redesign still open (Day 95/96);
paper-trading launchd log doesn't capture manual/force-run activity (Day
95); IBKR paper-execution CIRO question (Day 97); no scheduled/proactive
breakout alerting (Day 100); SRPS's Rule 6 earnings exclusion not applied
in either backtest gate (Day 103, moot); SimFin key rotation unconfirmed;
Defeat Beta import present; Master Framework/Nirmal/HUB-65 watchlist
Name/Market Cap N/A by choice; a genuinely missed paper-trading job run on
2026-07-14 (confirmed, not recoverable); FMP's `get_provider_status()`
hardcodes its daily quota as unlimited instead of the real 250/day limit
(inert, not in any active fallback chain); Pattern Detection card's
per-pattern R:R uses a fixed target multiple never checked against real
resistance, same structural shape as the SRPS R:R gap above (new, Day 109,
design doc item 11 caveat — low effort, not yet scheduled).
