# Known Issues — Day 122

> Supersedes `KNOWN_ISSUES_DAY120.md`. Consolidated close for Days 121–122 (Day 121 had no
> formal close). App code added: 4 display-only helpers, not yet imported, so no live behaviour
> changed.

## Changes from Day 120

- **New (Info):** IBKR daily volume is 46–65% of the consolidated count TwelveData/yfinance
  report (5 tickers × 12 days, Nov 10); closes match exactly. IBKR filters some trade types.
  STA's volume is correct; never mix IBKR volume into an RVOL/OBV calc with TwelveData volume.
- **New (Low):** `ui-verify-checklist.js:702` hard-codes its output to the untracked
  `docs/test/UI_Cohesiveness_Test_Day53_AllPeriods/VERIFICATION_REPORT.md`; the Day 121
  baseline run overwrote the Day 53 report (not recoverable). Fix in redesign Phase 6 (write to
  a dated folder).
- **New (Low):** `assessTechnical()` falls back to RSI 50 silently when RSI is missing. Fix
  decided Day 122 (show "momentum n/a" via `deriveTechnicalRead`), ships with the redesign.
- **Progress:** VIX multiplier ladder now has one exported `getVixPositionMultiplier()`
  (Day 121, Phase 1); the two `App.jsx` copies remain until Phase 2 wires it in.
- **New (Info):** the verdict rule now has a parity hook (`.claude/hooks/verdict_parity.sh`)
  that reruns `test_verdict_parity.py` on any edit to `categoricalAssessment.js` or
  `backtest/categorical_engine.py`. The other two 7-of-8 copies
  (`pattern_detection.py:282`, `backtest/parameter_stability.py:183`) are not covered by it.

---

## Open Issues

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Fix:** Not actioned. Likely moot now — the paper-trading engine it would wire into is
discontinued (Day 113). Worth a 2-minute check before ever planning a fix: confirm nothing else
reads this sizing path before spending effort on it.

### Medium: `ContextTab.jsx` bypasses the app's shared fetch layer (carried from Day 108)
**Fix:** Not actioned — needs `api.js`'s dead Context functions fixed to throw-not-swallow first.

### Medium: Value tab's "Buffett" ROE attribution overstates certainty — decision made, not implemented (carried from Day 111)
**Fix (decided, not implemented):** drop the investor-name labels, group the six metrics under
three functional headings (Efficiency & Quality, Valuation, Cash Generation). Frontend-only.

### Medium: Settings' risk slider allows up to 5%/trade against the app's own documented 2% Van Tharp ceiling (carried from Day 108)
**Fix:** Not actioned — needs a product decision.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Fix:** Mitigation choice still a pending user decision.

### Medium: Two batch endpoints (Sectors Rotation, Market Phase breadth) bypass circuit-breaker protection, no Tradier fallback (carried from Day 111)
**Fix:** Not actioned. `/api/mr/scan`'s bypass was fixed Day 111; these two remain.

### Low-Medium: `divergence`'s ±5% thresholds are scale-unstable across tickers (Day 116)
**Fix:** Not actioned — re-thresholding is a methodology change (Golden Rule 55), not a bug
fix; disclosed in the UI copy instead.

### Low-Medium: Momentum entry panel's position-size label is hardcoded, computed from nothing (carried from Day 109)
**Fix:** Queued as part of the Analyze Page Redesign implementation (now has a corrected,
ready-to-execute plan — see `ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md` Phase 2).

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call sites.

### Low: short-history tickers get a mismatched "52W Return" label on Full Analysis (Day 117)
`backend.py`'s `price_52w_ago` falls back to the oldest available bar when
`200 < len(hist_data) < 252` (e.g. a recent IPO), so Full Analysis's "Stock 52W Return" can be a
~250-bar return mislabeled as a full year, while the Simple Checklist correctly reports
"Insufficient data" for the same ticker. Live example: STUB, n=251. Not fixed — logged.

### Low: same-day effort-vs-result thresholds are unbacktested (Day 116)
`EFFORT_RESULT_LITTLE_PROGRESS_ATR`/`REAL_PROGRESS_ATR` (0.5/1.0 ATR) are first-principles
choices, disclosed as such in the rendered text. Display-only, gates nothing.

### Low: `meta.candle.barComplete`'s market-hours test assumes US/Canadian exchange hours (Day 116)
Tests against `America/New_York` market hours — correct for US/TSX, would misreport for any
non-North-American listing reaching `/api/sr`. Scope (which non-NA tickers actually reach this
endpoint) not audited. Document only.

### Low: Seven unlinked copies of the 1.5x volume-confirmation threshold (carried from Day 111)
**Fix:** Not actioned — backend files. `pattern_detection.py`'s message-string literal is the
most fragile.

### Low: Data Sources tab's field-source documentation is stale ("Defeat Beta API") (carried from Day 111)
**Fix:** Part of the small cleanup batch (see `CLAUDE_CONTEXT.md`'s Next Session Priorities).

### Low: `assessSentiment()` / `assessTechnical()` silent-fallback display states (carried from Day 109)
**Fix:** Display-layer only — queued alongside the redesign's context card
(`ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md` Phase 4).

### Low: VIX position-size multiplier ladder duplicated verbatim (carried from Day 109)
**Fix:** Extract to one exported `getVixPositionMultiplier()` — now scoped as part of the
redesign's Phase 1 (`positionSizing.js`).

### Low: Value tab's FCF Yield gets a pass/fail badge despite the spec saying it shouldn't (carried from Day 108)
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` latent short-date-range logic gap (carried from Day 108)
**Fix:** Worth a look before this function gets a new caller.

### Low / Info: Simple Checklist's "PASS" badge misleading at low pass counts (carried from Day 106)
**Fix:** Copy fix specified in the redesign's §7.5 — now scoped as part of the redesign's
Phase 5 (`ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`).

### Low / Info: SRPS screener's R:R structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer covers it.

### Low / Info: two independent 1-year-return calculations exist in the frontend, currently in agreement (Day 117)
`simplifiedScoring.js`'s inline RS calc and `rsCalculator.js` (Full Analysis) both span 251
bar-intervals; the backtested `Config G` filter spans 252. Measured bit-identical across 50
live tickers, traced to a shared origin in `backend.py`'s `hist.tail(260)` slice — two specific
conditions could desync them (NaN-row skipping; the short-history case above), neither observed
live. Do not "fix" the 251-vs-252 mismatch — that line drives the live Momentum gate.

### Low / Info: "Industry-Standard Report Card" Artifact's MTF/Pattern-Detection grades are stale (carried from Day 118)
The published Artifact grades MTF Confluence 3/10 and Pattern Detection's price target 1.5/10 —
both fixed Day 118. The index doc (`SESSION_ARTIFACTS_INDEX_DAY111.md`) is updated to flag this;
the Artifact page itself has not been republished. Also: 4 of the other 7 artifacts in that index
haven't been re-checked against Days 113-118's changes at all — worth a pass next time any of
them is touched, not urgent on its own.

### Low / Info items (carried forward, unchanged)
`mean_reversion.py`'s ADX docstring doesn't match its code (Day 92); Sector Rotation's original
endpoint has no provider fallback (Day 94/103); MR/momentum entry gates have no
regime/sector-correlation awareness (Day 100 — accepted design tradeoff); HUB-65 backtest is
selection-biased and not an independent sample from broad MR (Day 98); momentum stop/target
formula redesign still open (Day 95/96 — likely moot now, no live momentum track); paper-trading
launchd log doesn't capture manual/force-run activity (Day 95); IBKR paper-execution — **not
parked, DECLINED Day 113**, do not resume; no scheduled/proactive breakout alerting (Day 100);
SimFin key rotation unconfirmed; Defeat Beta import present; Master Framework / Nirmal / HUB-65
watchlist Name/Market Cap N/A by choice; a genuinely missed paper-trading job run 2026-07-14
(not recoverable, moot); FMP's `get_provider_status()` hardcodes unlimited quota (inert).
