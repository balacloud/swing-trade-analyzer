# Known Issues — Day 118

> Supersedes `KNOWN_ISSUES_DAY112.md`, which was edited in place across Days 116-118 as a
> stopgap (no formal close ran between Day 112 and this one). That file is kept for history;
> this one is the current canonical list, consolidated at the Day 118 close.

## Resolved since Day 112 (Days 113, 116-118)

- **Path B momentum forward-test track** — RETIRED Day 112, program **discontinued entirely
  Day 113** at the user's explicit direction. No forward-test gates exist anymore.
- **OBV `trend` sign bug** (Day 116) — was biased toward `'rising'` for negative cumulative
  OBV. Sign-safe band fix; proven the live ⚠️ DIST badge can't be affected (fires only on
  `'falling'`, which was bit-identical before/after across a 150-ticker sweep).
- **OBV's 20-day effort-vs-result sentence was live but invisible** (Day 116) — promoted from a
  hover-only tooltip to visible text on the Volume card.
- **`meta.rvol` read the still-forming intraday bar** (Day 116, found and fixed same session) —
  new `barComplete`/`prevBar` fields; fixed across the Volume card, the DIST badge, and
  `priceStructureNarrative.js`'s breakout-watch line.
- **Absolute momentum (dual momentum's 2nd leg) was invisible** (Day 117) — now a visible,
  informational read on both the Simple Checklist and Full Analysis view. The Day 111 decision
  not to *gate* on it is unchanged.
- **MTF Confluence's `strength` field was dead** (Day 118) — now a real graduated score
  (Strong/Moderate/Weak), and synthetic ATH/ATL-projected levels no longer silently drag down
  the confluence badge.
- **VCP's price target was a flat +15%** (Day 118) — now real nearest-resistance, falling back
  to measured contraction depth.

Full detail on each: `docs/claude/design/VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md`,
`ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md`, `MTF_VCP_FIX_PLAN_DAY115.md`.

---

## Open Issues

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Medium: VIX position-sizing was never wired into the automated paper-trading engine (carried from Day 108)
**Fix:** Not actioned. **Day 118 note:** likely moot now — the paper-trading engine it would
wire into is discontinued (Day 113). Worth a 2-minute check before ever planning a fix: confirm
nothing else reads this sizing path before spending effort on it.

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
**Fix:** Queued as part of the Analyze Page Redesign implementation.

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
**Fix:** Display-layer only — queued alongside the redesign's context card.

### Low: VIX position-size multiplier ladder duplicated verbatim (carried from Day 109)
**Fix:** Extract to one exported `getVixPositionMultiplier()`.

### Low: Value tab's FCF Yield gets a pass/fail badge despite the spec saying it shouldn't (carried from Day 108)
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` latent short-date-range logic gap (carried from Day 108)
**Fix:** Worth a look before this function gets a new caller.

### Low / Info: Simple Checklist's "PASS" badge misleading at low pass counts (carried from Day 106)
**Fix:** Copy fix specified in the redesign's §7.5, not applied.

### Low / Info: SRPS screener's R:R structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer covers it.

### Low / Info: two independent 1-year-return calculations exist in the frontend, currently in agreement (Day 117)
`simplifiedScoring.js`'s inline RS calc and `rsCalculator.js` (Full Analysis) both span 251
bar-intervals; the backtested `Config G` filter spans 252. Measured bit-identical across 50
live tickers, traced to a shared origin in `backend.py`'s `hist.tail(260)` slice — two specific
conditions could desync them (NaN-row skipping; the short-history case above), neither observed
live. Do not "fix" the 251-vs-252 mismatch — that line drives the live Momentum gate.

### Low / Info: "Industry-Standard Report Card" Artifact's MTF/Pattern-Detection grades are stale (new, Day 118)
Found while checking `SESSION_ARTIFACTS_INDEX_DAY111.md` for staleness during this close. The
published Artifact grades MTF Confluence 3/10 ("arbitrary hardcoded multiplier") and Pattern
Detection's price target 1.5/10 ("flat percentage") — both fixed Day 118. The index doc is
updated to flag this; the Artifact page itself has not been republished. Also: 4 of the other
7 artifacts in that index (#5/#6/#7/#8) haven't been re-checked against Days 113-118's changes
at all — worth a pass next time any of them is touched, not urgent on its own.

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
