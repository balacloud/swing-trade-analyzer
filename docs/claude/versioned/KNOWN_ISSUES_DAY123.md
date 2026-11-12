# Known Issues — Day 123

> Supersedes `KNOWN_ISSUES_DAY122.md`. Analyze Page Redesign Steps 3–6 built (v4.63).

## Changes from Day 122

- **Resolved:** yfinance debt/equity arrived in percent (AAPL ≈154 read as heavily indebted)
  and was mixed with Finnhub/FMP ratios. Now ÷100 in `field_maps.py` (Golden Rule 61).
- **Resolved:** ROE/ROA/ROIC ≥100% displayed as "1.5%" (×100 only when `abs(v) < 1`). Now
  unconditional for yfinance/FMP. Fundamentals cache schema v3.
- **Resolved:** earnings `days_until` was off by one (−1 on the report day). Now NY calendar days.
- **Resolved:** earnings "every source failed" was reported as "no date found". Now
  `has_upcoming: null`.
- **Resolved:** MR card showed an ATR stop and an entry + 2 ATR target, never the tested rule,
  with a silent 2% ATR fallback. Replaced by the tested rules (`MR_RULES`).
- **Resolved:** fake fallbacks removed: 3% stop / ×1.10 target (`riskRewardCalc`), RVOL 1.0
  with no volume history (backend + Price Structure narrative), `suggestedStop` from a missing ATR.
- **Resolved:** cached forming bar could feed the MR signal between 16:05 and 16:30 ET. One rule
  now: `market_time.py`.
- **Resolved:** a past session's candle could be labelled "Today" (`meta.candle.date` added).
- **Resolved (removed by user decision):** the Holding Period selector silently re-weighted the
  verdict, including on the Scan tab. Selector, Breakdown, Quality Gates and Raw Indicators are
  gone, and so is BUY/HOLD/AVOID on every screen.
- **Corrected number (not a code bug):** MR forward-test PF 2.00 was priced at the entry-day
  close. At the next open: broad PF 1.50, HUB-65 PF 1.07 (Golden Rule 60). Docs corrected.
- **New (Medium) ×3:** RSI `|| 50` engine pass, missing SPY → Unfavorable, MNST split artifact
  in the ledger (below).
- **New (Low):** `frontend/scripts/ui-verify-checklist.js` and `ui-cohesiveness-test.js` scrape
  the removed verdict badge and T/F/S/R row, so they are fully broken now. They were already
  timing out. Fix in Step 8.
- **New (Low):** `scoringEngine.js` still computes `qualityGates` (line 499), which nothing
  renders. Step 8 cleanup.
- **New (Low):** `forwardPe` is mapped to Finnhub's `peBasicExclExtraTTM` (`field_maps.py:73`),
  a trailing P/E. Anything labelled "forward P/E" from Finnhub is wrong (old `scoringEngine`
  input). The Fundamentals card uses trailing P/E only.

---

## Open Issues

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Medium: `assessTechnical()` treats a missing RSI as 50, and 50 counts as a pass toward Strong (Day 123, upgraded from Low)
`categoricalAssessment.js:327` and `:1001` (`rsi || … || 50`). The display now says "momentum
n/a" (`technical.data.rsiAvailable`, Day 123), but the engine still scores the fake 50.
**Fix:** a parity-tested engine change (JS + `categorical_engine.py` together, Golden Rule 59).
Changes verdicts for tickers with missing RSI, so it needs a plan.

### Medium: `assessRiskMacro()` reads missing SPY data as "below its 200-day", so the market shows Unfavorable (Day 123)
The Regime Read card now says "SPY trend unavailable" (`riskMacro.data.spyAvailable`), but the
engine's regime input is still wrong on a SPY fetch failure. **Fix:** parity-tested engine
change, same as above.

### Medium: the MR ledger holds a fake MNST −50.8% loss (split artifact) (Day 123)
Found by `mr_open_entry_retest.py`. On today's data both re-test bases replay it correctly, so
the corrected PF 1.50 is unaffected. The stored ledger row and `daily_job.py --report`'s PF 2.00
still include it. **Fix:** not needed for any live use (program discontinued); document only.

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
Still live at `App.jsx:2074` (`<span>half</span>`, Momentum entry strategy). **Fix:** redesign
Step 7/8.

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

### Low: `assessSentiment()` silent-fallback display state (carried from Day 109)
`assessTechnical()`'s half is now shown on the Technical Read ("momentum n/a"); the engine side
is the Medium item above. `assessSentiment()`'s `fearGreed || 50` remains.

### Low: VIX position-size multiplier ladder duplicated verbatim (carried from Day 109)
`getVixPositionMultiplier()` exists (Day 121), but `App.jsx:345` and `:367` still carry inline
copies. **Fix:** swap both for the helper (redesign Step 8 cleanup).

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
