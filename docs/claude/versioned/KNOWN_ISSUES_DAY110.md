# Known Issues — Day 110

## Changes from Day 109

**Resolved this session:** none — no application code was touched.

**New issues found this session:** none code-level. Two new informational
items added below (a design-doc/mockup sync gap, and a concrete new
instance of the already-known Day-100 correlation gap in MR HUB-65).

**Existing item updated, not resolved:** the Analyze Page Redesign's
Market Regime decision (design doc item 4) was reversed from a hard gate
to informational — this doesn't change any of the items below, since none
of them were about that decision's mechanism; it changes the design doc
and creates the new mockup-sync item added below.

**Freeze status:** unchanged — forward-testing accumulation remains the
sole stated priority. Live numbers pulled fresh this session (2026-08-20):
Path A 20 open/48 closed (54.17% WR, PF 1.71), Path B 64 open/69 closed
(56.52% WR, PF 1.45), MR broad 2 open/**99 closed** (76.77% WR, PF 2.68 —
one trade from its 100-trade bar), MR HUB-65 0 open/33 closed (57.58% WR,
PF 1.84).

---

## Open Issues

### Low: Analyze Page Redesign mockup out of sync with the decision doc's Regime reversal (new, Day 110)
**Severity:** Low
**Description:** `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`
item 4 was revised Day 110 — Market Regime moved from a hard gate to
informational (Info), no enforcement language. The published mockup
(`docs/claude/design/mockups/analyze_page_redesign_mockup.html`) was built
*before* this reversal and still shows the pre-reversal "stand-down"
banner copy with imperative language and a non-collapsible presentation.
**Fix:** Update the mockup's Regime band to match — drop the "stand-down"/
"deliberately not left to judgment" language, treat as Info, keep expanded
by default (not collapsed) since regime is portfolio-wide. Queued for next
time the redesign is picked up; not urgent since implementation hasn't
started either way.

### Low / Info: MR HUB-65 shows extreme single-day entry concentration that hurt, not inflated, its number (new, Day 110)
**Severity:** Low / Info
**Description:** 16 of HUB-65's 33 closed trades (48.5%) entered on a
single day (2026-07-28), heavily semiconductor-weighted (ALAB, AMAT, ASML,
CGNX, KLAC, LRCX, LSCC, MOD, TSM, plus SMH/SOXX sector ETFs). That cohort
ran 43.8% WR / −2.03% net, while the other 17 trades ran 70.6% WR / +62.55%
net — the concentrated bet dragged the track's headline PF (1.84) down
rather than inflating it, the opposite direction from the pattern already
known in MR broad (Day 93). Confirmed live via direct ledger queries, not
assumed. Same underlying structural gap as the Day 100 finding below — a
new, concrete instance of it, not a new gap.
**Fix:** Not actionable — this is the same accepted, not-fixed-mid-freeze
tradeoff (neither entry gate has sector/portfolio-correlation awareness).
Informational only.

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Severity:** High
**Fix:** Not actioned — needs a new failure-tracking mechanism, scoped as
its own session.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Severity:** Medium (verified zero impact on current live-track statistics)
**Fix:** Not actioned — ties into the parked IBKR execution plan.

### Medium: Pivot support/resistance method selects extreme levels, not nearest (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — revisit once the freeze lifts.

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
Fundamental labels — this figure is the load-bearing evidence behind the
Analyze Page Redesign's Fundamentals red-flag thresholds (design doc §5).
**Fix:** Mitigation choice still a pending user decision. Parked behind the
paper-trading focus.

### Low-Medium: Momentum entry panel's position-size label is hardcoded, computed from nothing (carried from Day 109)
**Severity:** Low-Medium
**Fix:** Queued as part of the Analyze Page Redesign implementation (§7.2
of the design doc). Not fixed standalone.

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Severity:** Low-Medium
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call
sites — a small, contained backend change.

### Low: `assessSentiment()` silently defaults to "Neutral" on fetch failure (carried from Day 109)
**Severity:** Low
**Fix:** Display-layer only — queued alongside the Analyze Page Redesign's
Fundamentals/Sentiment context card (§7.4).

### Low: `assessTechnical()` collapses "pattern detection unavailable" and genuine "Weak" into one state (carried from Day 109)
**Severity:** Low
**Fix:** A 4th display state ("Unavailable") is specified for the
redesigned Technical Read — not implemented yet.

### Low: VIX position-size multiplier ladder duplicated verbatim, silently defaults on missing data (carried from Day 109)
**Severity:** Low
**Fix:** Extract to one exported `getVixPositionMultiplier()`, queued as
part of the redesign's Phase 1. Not implemented.

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
**Fix:** Not actioned. Copy fix specified in the redesign's §7.5, not yet
applied.

### Low / Info: SRPS screener's R:R is structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer already covers
this.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); Sector
Rotation's original endpoint has no provider fallback (Day 94/103);
MR/momentum entry gates have no regime/sector-correlation awareness (Day
100, accepted design tradeoff — see the new HUB-65 instance above);
HUB-65 backtest is selection-biased by construction (Day 98); HUB-65 and
broad MR aren't independent samples (Day 98); momentum's stop/target
formula redesign still open (Day 95/96); paper-trading launchd log doesn't
capture manual/force-run activity (Day 95); IBKR paper-execution CIRO
question (Day 97); no scheduled/proactive breakout alerting (Day 100);
SRPS's Rule 6 earnings exclusion not applied in either backtest gate (Day
103, moot); SimFin key rotation unconfirmed; Defeat Beta import present;
Master Framework/Nirmal/HUB-65 watchlist Name/Market Cap N/A by choice; a
genuinely missed paper-trading job run on 2026-07-14 (confirmed, not
recoverable) and a second stale gap 2026-08-14→2026-08-20 (self-recovered
Day 110, missed days' entry signals not recoverable, same documented
limitation); FMP's `get_provider_status()` hardcodes its daily quota as
unlimited instead of the real 250/day limit (inert, not in any active
fallback chain); Pattern Detection card's per-pattern R:R uses a fixed
target multiple never checked against real resistance (Day 109, low
effort, not yet scheduled).
