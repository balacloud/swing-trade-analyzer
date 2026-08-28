# Known Issues — Day 111

## Changes from Day 110

**Resolved/shipped this session:**
- `/api/mr/scan` orchestrator bypass — fixed
- MR Scanner wired to the Scan tab — shipped, verified live
- Volume Confirmation (magnitude) — shipped, verified live
- Volume Direction (lean) — shipped, verified live
- Dual/absolute momentum — decided not to pursue, closed (not deferred)
- Value tab investor-attribution — decision made (not yet implemented)

**New issues found this session:** S&R pivot method graded 2.0/10, MTF
Confluence graded 3.0/10, Pattern Detection's price target graded 1.5/10
(all three: remediation plans written, not implemented); 5 data-provenance
findings (2 fixed, 3 open); OBV trend sign bug (new, real, not fixed); 7
unlinked copies of the 1.5x volume threshold; and the big one — **Momentum
Path B crossed its 100-trade bar and fails the same cluster stress-test
that MR (broad) passed.** See below.

**Freeze status:** unchanged — forward-testing accumulation remains the
sole stated priority. Live numbers pulled fresh at session close
(2026-08-28): Path A 25 open/59 closed (52.54% WR, PF 1.5799), **Path B 61
open/117 closed (50.43% WR, PF 1.2293 — crosses the numeric bar, see
finding below)**, **MR broad 20 open/138 closed (79.71% WR, PF 3.0021 —
genuinely confirmed)**, MR HUB-65 2 open/49 closed (61.22% WR, PF 1.661).

---

## Open Issues

### High: Momentum Path B crosses its confirmation bar numerically, but fails the cluster stress-test that MR (broad) passed (new, Day 111)
**Severity:** High
**Description:** Path B: 117 closed trades, 50.43% WR, PF 1.2293 — clears
the pre-registration's own "Confirmed" threshold (`PAPER_TRADING_
PREREGISTRATION.md` §10: PF≥1.2, positive expectancy, ≥100 trades) on
paper. But **78 of its 117 closed trades (66.7% of the entire sample)
entered in a single 4-day window, Aug 3-7 2026.** Excluding just those 4
days: 39 trades remain, 43.6% WR, **PF 0.72 — net losing**, well into the
pre-registration's own "Broken" tier (<0.9). Checked whether this is the
already-known sector-correlation gap (Day 100/HUB-65) — it isn't: the
cluster's tickers span energy, healthcare, financials, tech, and consumer
names, no sector concentration. This looks like a *regime/timing*
correlation instead — the entry gate fired heavily during one specific
market window, and the whole track's confirmed-looking statistics are
riding on that one window, not a diversified edge. Directly contrasts with
MR (broad)'s result the same session, which was stress-tested the same
way and held up clean (PF 2.24 even with its own largest cluster excluded,
win rate rose to 80%).
**Fix:** Not a code fix — a judgment call not yet made. Options for next
session: (a) treat Path B as not-yet-confirmed despite clearing the
numeric bar, and keep accumulating past 100 to see if the ratio dilutes
back toward the ex-cluster reality; (b) accept the confirmation as valid
per the pre-registration's own written criteria, which say nothing about
cluster concentration, and treat the caveat as informational; (c) formally
extend the pre-registration's own success criteria to include a cluster
check, the same way MR's have been informally stress-tested every
milestone this session. **Also connects directly to the parked S&R fix
decision below** — Path B's live entry gate is exactly the thing that
reads `compute_sr_levels()`, so this result is relevant context for that
decision, not a separate issue.

### High: The S&R fix itself — decision pending, not started (new, Day 111)
**Severity:** High (blocks 2 other planned fixes)
**Description:** `_pivot_sr()`'s extreme-vs-nearest bug (Golden Rule 53)
was scoped for a fix this session, but before any code was written, found
that `support_resistance.py`'s `compute_sr_levels()` is not purely
Analyze-page display support — Momentum Path B's live entry gate
(`paper_trading/live_signals.py`) imports it directly and gates real
trades on `sr_levels.meta['trade_viability']['viable']` and the R:R
computed from those same levels. Per Golden Rule 18, fixing the selection
logic in place would reset Path B's accumulated count. **New Golden Rule 54.**
**Fix:** Three options presented to the user, not yet decided: (1) fix in
place, accept the reset; (2) build a parallel corrected path, same pattern
as how Path B itself was created at Day 95 to avoid resetting Path A; (3)
scope the fix to display only, leave the live entry gate's behavior
untouched. **Worth weighing against the new Path B finding above** — a
track whose "confirmed" result doesn't survive its own stress-test is a
different cost-benefit calculation for "accept the reset" than a track
that was cleanly confirmed. Blocks: Pattern Detection's VCP target fix
(needs trustworthy `nearest_resistance`), and reduces confidence in MTF
Confluence's fix (confluence can only be as good as the levels it
confirms).

### Medium: MTF Confluence's confidence score is a hardcoded binary multiplier, not a real weighted score (carried from Day 111)
**Severity:** Medium
**Fix (planned, not yet actioned):** wire `mtf_daily_weight`/
`mtf_weekly_weight` into a real graduated score (or delete the dead
config), reuse the agglomerative method's existing touch-count logic.
Graded 3.0/10 against real methodology. Depends on the S&R fix above.

### Low-Medium: Pattern Detection's price target is a flat percentage, not a real computation (carried from Day 111)
**Severity:** Low-Medium
**Fix (planned, not yet actioned):** Cup & Handle and Flat Base can ship
independently (`target = pivot + cup_depth`/`base_depth`, reusing data
already computed for the pattern's own gate). VCP's fix depends on the
S&R decision above (needs trustworthy `nearest_resistance`). Graded
1.5/10; pattern recognition itself graded 8/10, matching published
Minervini/O'Neil criteria.

### Medium: Full data-provenance audit found 5 findings, 2 fixed (carried from Day 111)
**Severity:** Mixed
**Status:** `/api/mr/scan`'s orchestrator bypass — **fixed**. Remaining
open: two batch endpoints (Sectors Rotation, Market Phase breadth) bypass
circuit-breaker protection with no Tradier fallback; Tradier's real
capacity sits unused in the exact scenario that's already caused a
rate-limit incident; the Data Sources tab's own field-source documentation
is stale ("Defeat Beta API"). Full detail:
`docs/claude/versioned/DATA_PROVENANCE_FINDINGS_DAY111.md`.

### Low-Medium: OBV trend direction is biased toward "rising" when cumulative OBV is negative (carried from Day 111)
**Severity:** Low-Medium
**Fix:** Not actioned — feeds a shipped, live badge (the Distribution
Warning), needs its own review rather than a fix folded into another
change.

### Low: Seven unlinked copies of the 1.5x volume-confirmation threshold (carried from Day 111)
**Severity:** Low
**Fix:** Not actioned — backend files, out of scope for a display-only
change. `pattern_detection.py`'s message-string literal (line 191) is the
most urgent of the seven if ever touched — it can silently go stale
without affecting behavior at all.

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Severity:** High
**Fix:** Not actioned — needs a new failure-tracking mechanism, scoped as
its own session.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Severity:** Medium (verified zero impact on current live-track statistics)
**Fix:** Not actioned — ties into the parked IBKR execution plan.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to
throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty — decision made, not implemented (carried from Day 111)
**Severity:** Medium
**Fix (decided, not yet implemented):** drop the investor-name labels,
group the same six metrics under three honest functional headings
(Efficiency & Quality, Valuation, Cash Generation). Frontend-only.

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs a product decision.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Fix:** Mitigation choice still a pending user decision. Parked behind
the paper-trading focus.

### Low-Medium: Momentum entry panel's position-size label is hardcoded, computed from nothing (carried from Day 109)
**Severity:** Low-Medium
**Fix:** Queued as part of the Analyze Page Redesign implementation. Not
fixed standalone.

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Severity:** Low-Medium
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call
sites — a small, contained backend change.

### Low: `assessSentiment()` silently defaults to "Neutral" on fetch failure (carried from Day 109)
**Fix:** Display-layer only — queued alongside the redesign's Fundamentals/
Sentiment context card.

### Low: `assessTechnical()` collapses "pattern detection unavailable" and genuine "Weak" into one state (carried from Day 109)
**Fix:** A 4th display state ("Unavailable") is specified for the
redesigned Technical Read — not implemented yet.

### Low: VIX position-size multiplier ladder duplicated verbatim, silently defaults on missing data (carried from Day 109)
**Fix:** Extract to one exported `getVixPositionMultiplier()`, queued as
part of the redesign's Phase 1. Not implemented.

### Low: Value tab's FCF Yield gets a pass/fail badge despite the design spec saying it shouldn't (carried from Day 108)
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` has a latent short-date-range logic gap (carried from Day 108)
**Fix:** Worth a proper look before this function gets a new caller.

### Low: Analyze Page Redesign mockup's Regime band still shows pre-Day-110-reversal copy (carried from Day 110)
**Severity:** Low
**Fix:** One-line copy fix in the mockup HTML. The decision doc's own §6
already has the correct post-reversal wording — only the rendered mockup
lags. Not urgent since implementation hasn't started either way.

### Low / Info: Simple Checklist's "PASS" badge is misleading at low pass counts (carried from Day 106)
**Fix:** Not actioned. Copy fix specified in the redesign's §7.5, not yet
applied.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer already covers
this.

### Low / Info: SimFin ticker-universe drift affects seed-based backtest reproducibility (carried from Day 107)
**Fix:** Not actionable — informational.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); Sector
Rotation's original endpoint has no provider fallback (Day 94/103);
MR/momentum entry gates have no regime/sector-correlation awareness (Day
100, accepted design tradeoff — see Path B's Aug 3-7 finding above for a
regime/timing variant of the same underlying gap, and the Day 110 HUB-65
instance for a sector-flavored one); HUB-65 backtest is selection-biased
by construction (Day 98); HUB-65 and broad MR aren't independent samples
(Day 98); momentum's stop/target formula redesign still open (Day 95/96);
paper-trading launchd log doesn't capture manual/force-run activity (Day
95); IBKR paper-execution CIRO question (Day 97); no scheduled/proactive
breakout alerting (Day 100); SRPS's Rule 6 earnings exclusion not applied
in either backtest gate (Day 103, moot); SimFin key rotation unconfirmed;
Defeat Beta import present; Master Framework/Nirmal/HUB-65 watchlist
Name/Market Cap N/A by choice; a genuinely missed paper-trading job run on
2026-07-14 (confirmed, not recoverable) and a second stale gap
2026-08-14→2026-08-20 (self-recovered Day 110); FMP's
`get_provider_status()` hardcodes its daily quota as unlimited instead of
the real 250/day limit (inert, not in any active fallback chain).
