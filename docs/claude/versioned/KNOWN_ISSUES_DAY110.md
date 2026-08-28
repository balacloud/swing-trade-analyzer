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

### Medium: Pivot support/resistance method selects extreme levels, not nearest (carried from Day 108, remediation planned Day 111)
**Severity:** Medium
**Description:** `_pivot_sr()` (`support_resistance.py:1048-1050`) sorts highs/lows
ascending then slices `highs[-N:]`/`lows[:N]` — keeping the most EXTREME levels
in the lookback window, not the ones closest to price, despite every downstream
consumer calling the result "nearest support/resistance." Root cause of Golden
Rule 53. This is the primary (first-attempted) method in the fallback chain,
not a rare fallback.
**Fix (planned, not yet actioned):**
1. **The core fix — a few lines, no new dependency:** change the selection to
   sort candidate levels by `abs(level - current_price)` and keep the nearest
   N, instead of slicing by raw price extremity.
2. **Optional but worth it while touching this function:** replace the
   hand-rolled rolling-window pivot detector (a 5-bar local-max/min comparison)
   with `scipy.signal.find_peaks(prominence=..., distance=...)` — a well-tested,
   already-available primitive (scipy is already in the numpy/pandas stack) with
   built-in noise-handling the current rolling-window comparison doesn't have.
3. Populate `level_scores` (touch counts) for the pivot method too — currently
   silently `{}` whenever pivot is the active method (only the agglomerative
   method populates it), so Price Structure's Key Levels list loses touch-count
   context most of the time without any visible indication why.
4. Cite or backtest-derive the five uncited thresholds in `SRConfig`
   (`volatility_threshold`, `merge_percent`, `zigzag_percent_delta`,
   `touch_threshold`, `ath_threshold`) rather than leaving them unexplained
   magic numbers.
**Not actioned yet** — revisit once the freeze lifts. Graded 2.0/10 against
industry proximity/touch-weighted selection standards (Day 111 report card).

### Medium: MTF Confluence's confidence score is a hardcoded binary multiplier, not a real weighted score (new, Day 111)
**Severity:** Medium
**Description:** The Day 108 CRITICAL bug (weekly levels computed from
fabricated calendar dates) is genuinely fixed — verified directly against
`backend.py:1573-1584`. What's left: `_find_mtf_confluence()`
(`support_resistance.py:903`) marks a confirmed level `strength: 1.0` and an
unconfirmed one `0.6` — a flat, uncited binary boost, not a graduated score.
Worse, `SRConfig.mtf_daily_weight`/`mtf_weekly_weight` (`:70-71`, values
0.6/0.4) are declared — reading like a real weighted-confluence formula
exists — but grep confirms they're **never referenced anywhere else in the
file**. The config implies more sophistication than the code delivers.
**Fix (planned, not yet actioned):**
1. Either wire `mtf_daily_weight`/`mtf_weekly_weight` into a real graduated
   score, or delete them — don't leave dead config that misrepresents what
   the function actually does (Day-53 "dead code accumulates silently"
   pattern).
2. Replace the flat 1.0/0.6 multiplier with a graduated confidence score —
   reuse the agglomerative method's existing `_score_levels()` touch-count
   logic (already built, DRY per Code Architecture Rule 7) so confluence
   strength reflects how many times a level's actually been tested, not just
   whether a weekly level happens to fall within the threshold band.
3. Cite or backtest-derive `mtf_confluence_threshold` (currently 1.5%,
   tuned from 0.5% at Day 34 with no cited justification for either number).
4. **Depends on the S&R fix above** — confluence can only be as trustworthy
   as the levels it's confirming.
**Not actioned yet.** Graded 3.0/10 (Day 111 report card) — the concept is
sound and the critical bug is fixed; the scoring underneath it is arbitrary.

### Low-Medium: Pattern Detection's price target is a flat percentage, not a real computation (carried from Day 109, promoted to full entry + remediation planned Day 111)
**Severity:** Low-Medium
**Description:** `buildActionablePattern()` (`categoricalAssessment.js:61-89`)
computes `targetPrice = pivotPrice × targetMultiplier` — a flat, per-pattern
constant (VCP 1.15, Cup & Handle 1.20, Flat Base 1.12) — and never checks it
against a real resistance level. Confirmed directly. This is the number on
the page that looks the most precise (a specific dollar figure) while being
the least grounded — no chart geometry, no real ceiling, just a percentage.
**Fix (planned, not yet actioned) — real, decades-old technique, not a
library gap:**
1. **Cup & Handle:** switch to the actual published O'Neil formula —
   `target = pivot + cup_depth`. The cup's depth is already computed
   internally for the pattern's own gating logic (the 12-35% depth check,
   `pattern_detection.py:529`) — this reuses a number the function already
   has, doesn't fetch anything new.
2. **Flat Base:** same measured-move logic — `target = pivot + base_depth`,
   reusing the base range already computed for its own gate (`:688`).
3. **VCP:** different fix, because a flat measured-move isn't actually
   Minervini's own practice for this pattern — he targets the next real
   resistance level instead. Switch VCP's target to `nearest_resistance`
   from the S&R engine. **Depends on the S&R fix above** — this number is
   only trustworthy once "nearest" actually means nearest.
4. **Most honest version, optional:** compute both the measured-move number
   and the real-resistance check; if they disagree meaningfully, show both
   with a note — same pattern already adopted for the R:R footnote (§6 of
   `ANALYZE_PAGE_REDESIGN_DECISIONS.md`).
**Not actioned yet.** Graded 1.5/10 (Day 111 report card) against measured-move
target methodology (Edwards & Magee) — contrasted with the pattern-recognition
logic itself, which graded 8/10, matching published Minervini/O'Neil criteria.

### Medium: Full data-provenance audit found 5 findings — see dedicated doc (new, Day 111)
**Severity:** Mixed (1 Medium, 1 Low-Medium, 2 Low, 1 strategic/info)
**Description:** A complete tab-by-tab, field-level data-source map (Sections
1-10 of the Day 111 provenance artifact) found: two batch endpoints (Sectors
Rotation, Market Phase breadth) bypass the orchestrator's circuit-breaker
protection with no Tradier fallback at all; `/api/mr/scan` inconsistently
bypasses the orchestrator when its sibling endpoint doesn't; Tradier's real
capacity (100/min vs. TwelveData's 8/min) sits unused in exactly the
wide-scan scenario that's already caused a real rate-limit incident (Golden
Rule 25); the Data Sources tab's own field-source documentation is stale
("Defeat Beta API," a provider no longer in any active chain); and a
consolidated list of dead fundamentals-related code/config.
**Fix:** Full findings + fix plans, prioritized, in
`docs/claude/versioned/DATA_PROVENANCE_FINDINGS_DAY111.md`. Not actioned.
One sub-finding (adding Tradier to the two orphaned endpoints) is safely
additive; reordering the actual live OHLCV chain is explicitly flagged as
NOT freeze-independent and would need the same review as any change touching
`support_resistance.py`'s inputs.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Severity:** Medium
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to
throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty (carried from Day 108, decided Day 111)
**Severity:** Medium
**Decision (Day 111):** Checked whether the tab's 6 metrics are actually redundant with
each other first — they're not (each answers a genuinely different question: capital
efficiency, profitability, relative valuation, growth-adjusted valuation, intrinsic-value
ceiling, cash generation). The overload isn't the metric count, it's the docstring's
"Frameworks: Buffett / Graham / Lynch / Damodaran / Greenblatt" — five named investors
invoked for six simplified proxy metrics that aren't actually those investors' methods.
**Fix (decided, not yet implemented):** Drop the individual investor-name labels from
`ValueTab.jsx`; group the same six metrics under three honest functional headings instead
— **Efficiency & Quality** (ROIC, ROE), **Valuation** (P/E, PEG, Graham Number),
**Cash Generation** (FCF Yield). Same rigor, same numbers, no borrowed authority. Purely
a frontend labeling change — `backend.py`'s computations are untouched. Not yet
implemented; queued alongside other small Value Tab copy fixes (FCF Yield's pass/fail
badge, also open below).

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

### Low / Info: Volume confirmation — SHIPPED Day 111 (carried from Day 107)
**Fix:** DONE. The first design (Config F, a hard 1.5x-volume gate) failed the
same way Fundamentals/R:R/Regime originally did — too strict, threw away 93% of
trades. Same root cause, same fix: stop gating, start displaying.

**Correction to the original plan, found by the Opus planning pass:** RVOL was
NOT already shown on a "Sizing Inputs grid" or a "Technical Read card" — those
only exist in the unimplemented redesign mockup. On the **live** page, RVOL is
computed at `backend.py:1634-1637` and was already displayed as a small chip at
`App.jsx:1780-1790`, gated on `srData.meta?.tradeViability` being present (so it
silently disappeared on tickers where that field is absent). The new note was
built and shipped on the **live Trade Setup card** instead — `App.jsx:1808-1823`,
new module `frontend/src/utils/volumeThresholds.js` — independent of
`tradeViability`, so it renders even where the old chip doesn't.

**Also found and fixed:** the "shared 1.5x threshold" premise was only half
true — the number was consistent everywhere (no drift) but the *sharing* was
fiction: 7 separate unlinked literal copies across
`priceStructureNarrative.js`, `pattern_detection.py` (x2, one inside a message
string), `backend.py`, `App.jsx` (x2), and `backtest_holistic.py`, two of them
carrying comments claiming a link to each other that didn't exist in code.
Fixed on the frontend side: `priceStructureNarrative.js`'s module-local copy now
imports `BREAKOUT_VOLUME_THRESHOLD` from the new shared module instead of
re-declaring it. Backend copies (`pattern_detection.py`, `backend.py`,
`backtest_holistic.py`) are **out of scope** — JS/Python can't share a module,
and touching those files risks the frozen parity/entry-gate surface. Logged
below as its own Low/Info item.

Verified live in-browser on 2 tickers (NVDA 0.57x, TXN 0.14x) — number matches
the pre-existing chip exactly, renders on both a "NOT VIABLE" and a
"PULLBACK OK" ticker, neutral gray styling (no color-coded gate), Price
Structure/Pattern Detection/Breakout Status cards confirmed unaffected
(zero-behavior-change refactor check). See
`docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` §9 item 16.

**Day 112 extension — SHIPPED.** The magnitude read only says *how much*
volume there was, not *which way* it leaned. Added a second, independent
line — `getVolumeDirectionRead()` in the same module — combining three
already-computed daily-bar signals (day's price change vs. prior close,
close location within the day's range, OBV trend) into an honest LEAN, never
a verdict: "leans toward buying pressure" / "…selling pressure" / "mixed
signals, no clear lean" / "no clear lean either way." Explicitly disclosed
(in the tooltip) that daily bars cannot show real buy/sell order flow — this
is a lean from indirect evidence, not a determination. New backend field
`meta.candle` (`backend.py`, close-location arithmetic on the same OHLCV
frame already used for RVOL — no new provider call). A real disagreement
between signals (e.g. up-day + closed near the low) renders as "mixed," on
purpose — not averaged away, not hidden (same logic Day 84 already applied
to the breakout NOT_READY badge: silence is indistinguishable from "the data
didn't load").

Opus-planned first — the plan corrected 5 things in the brief before any code
was written (most importantly: `candle_quality_ok`'s close-location logic
needs an ATR + SPY-benchmark fetch to reach, so this was independently
reimplemented as plain arithmetic on data already in hand, not imported
across engines) and surfaced a real, separate pre-existing bug — see the new
entry below. Verified live: MSFT ("closed up 2.2%, settled near the day's
high, OBV rising — leans toward buying pressure") and TSLA ("closed down
1.6%, near the day's low, OBV rising — mixed signals, no clear lean," a
genuine 3-signal disagreement correctly surfaced, not hidden).

### Low-Medium: OBV trend direction is biased toward "rising" when cumulative OBV is negative (new, Day 112)
**Severity:** Low-Medium
**Description:** `calculate_obv()`'s trend classification (`backend.py`,
inside the OBV function) is `if current_obv > obv_sma * 1.02: 'rising' elif
current_obv < obv_sma * 0.98: 'falling' else: 'flat'`. OBV is a raw cumulative
sum from the start of the lookback window, so a stock that's been net
distributed sits below zero — and when `obv_sma` is negative,
`obv_sma * 1.02` is *more* negative than `obv_sma` itself, so the `>`
comparison in the first branch fires almost automatically, before the
`elif` ever gets evaluated. Net effect: **stocks with negative cumulative
OBV are structurally biased toward reporting "rising"** regardless of the
actual recent trend. Pre-existing — this already affects the live OBV chip
and the "⚠️ DIST" (Distribution Warning) badge (`App.jsx`), not introduced by
the Day 112 volume-direction feature, which was built to deliberately reuse
`meta.obv.trend` as-is (rather than switch to the sign-safe
`obv_change_pct`) specifically so the new sentence can never contradict the
OBV arrow chip sitting right above it on the same page.
**Fix:** Not actioned — `calculate_obv()` feeds a shipped, user-visible
badge; changing its trend logic is a behavior change, not a display
addition, and deserves its own review rather than a fix folded into this
one. Logged for a future session.

### Low / Info: Seven unlinked copies of the 1.5x volume-confirmation threshold (new, Day 111)
**Severity:** Low
**Description:** Found while shipping the item above. `pattern_detection.py:163`
(`volume_ratio >= 1.5`), `pattern_detection.py:191` (the *same* threshold
re-typed a second time, inside an f-string message — if #1 ever changes, this
message silently lies), `backend.py:1637`, `backtest_holistic.py:106`
(`VOLUME_CONFIRM_RATIO`), and the two now-fixed frontend copies were each
independent literals. All currently hold `1.5` — no numeric drift today, the
risk is entirely latent. Two of the backend copies' comments explicitly claim
a shared-constant relationship that has never existed in code.
**Fix:** Not actioned — out of scope for the Day 111 display-only change
(backend files, no shared JS/Python module possible). If ever touched, treat
`pattern_detection.py`'s message-string literal (line 191) as the most urgent
of the seven, since it's the one that can silently go stale without affecting
behavior at all.

### Low / Info: Dual/absolute momentum — tested clean, near-inert in practice (carried from Day 107)
**Fix:** Decided Day 111 — **not pursuing.** Re-applied Core Principle 6 (every
rule survives "why" three times): Config G tested clean but only excluded 1 of
75 trades, because the existing RS-based pipeline already mostly selects
positive-absolute-momentum stocks as a side effect. Correct but pointless —
real maintenance cost for a filter that changes nothing. Closing, not deferring.

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
fallback chain).
