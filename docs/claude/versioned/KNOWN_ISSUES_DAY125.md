# Known Issues — Day 125

> Supersedes `KNOWN_ISSUES_DAY124.md`. Analyze cleanup (v4.65): simple support/resistance rows,
> trader-rule breakout, Price Structure / Pattern Detection / P/E guide / MR track record removed.

## Changes from Day 124

- **Resolved:** the one-line price state used the deepest support instead of the nearest (Day 112
  BUG-B, fixed then only in the old card's level list) and guessed "Downtrend" when trend data was
  missing. Moved to `keyLevels.js`, both fixed, tested.
- **Resolved:** the breakout check judged a still-forming bar mid-day (part-day volume, a price that
  isn't a close). It now uses completed bars only.
- **Resolved:** a failed breakout fetch made the card silently disappear (`fetchBreakout` returned
  null). It now says "Breakout check unavailable", on both views.
- **Resolved:** the Scan tab showed an unknown breakout status as "Not Ready". Now it shows the raw status.
- **Resolved (moot):** "Industry-Standard Report Card" artifact's stale MTF / Pattern-Detection
  grades. Both cards are removed from the page; the artifact is now history (Snapshot).
- **New (Low / Info):** Puppeteer's new headless mode hangs on `click()` (below).
- **New (Info):** breakout rules and S&R display are conventions, not tested (below).
- **Changed:** "Seven unlinked copies of the 1.5x threshold" now counts `breakout_detection.py`'s
  `RVOL_CONFIRM` (the breakout's own rule; the old `rvol_confirm` config is gone).

---

## Open Issues

### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Medium: `/api/stock` doesn't drop today's unfinished bar (Day 124)
`backend.py` `get_stock_data` takes `current_price` and `priceHistory` from the last row, and
neither the route nor the providers apply `market_time.drop_forming_bar` (the MR, pattern and
index-trend paths do). On a mid-day cache miss, the Analyze page may compute on a partial bar.
Seen live only as the cached case (yesterday's close, now labelled "Nov 11 close"). The header
labels a today-dated bar "intraday, not a close" (Day 124). **Fix:** confirm a mid-day cache
miss returns a partial bar, then apply the shared rule. Engine inputs change, so re-run parity.

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

### Low-Medium: PMI/Business-Cycle econ cards not covered by the Day-91 date-alignment fix (carried from Day 108)
**Fix:** Port the existing `_at_months_ago()` fix to the 2 remaining call sites.


### Info: breakout rules and the support/resistance display are trader conventions, not tested (Day 125)
User decision ("it's a rabbit hole"). Both cards say "Common trader rules, not tested". A steady
climber re-qualifies as a breakout about every 10 days (stated on the card). Not a bug; recorded so
nobody reads them as a proven edge. MR (broad) remains the only tested edge.

### Info: the S&R engine is due for replacement (Day 125)
`support_resistance.py` (~1,600 lines, 3 fallback methods, projections) is planned to be replaced
on the Analyze page by `simple_sr.py` (`SIMPLE_SR_PLAN_DAY125.md`). The Simple Checklist's criteria
3/4 read these levels, so TRADE / No Trade can flip. The switch waits for the ~30-stock comparison
and the user's decision. The legacy engine stays for `backtest_holistic.py` and the discontinued
paper job.

### Low / Info: Puppeteer new headless mode hangs on `click()` (Day 125)
After a few hours, `ui-verify-checklist.js` timed out on every ticker ("Runtime.callFunctionOn
timed out"). It reproduced on a one-input `data:` page, so it is not the app.
`headless: 'shell'` works. The likely cause is the Mac display sleeping. **Fix (if it recurs):** a
`--shell` flag or env switch on the verifier; until then, run a temporary copy with
`headless: 'shell'`.

### Low: the engine's regime input ignores the 50-day trend and the Nasdaq (Day 124)
`assessRiskMacro` uses SPY vs its 200-day and VIX 20/30 only. The page no longer shows that
label (user decision, Step 7), so nothing visible depends on it. But `regimeSnapshot.assessment`
is still saved with each logged trade and exported to CSV. Document only, unless the trade log's
regime field is ever used for analysis.

### Low: Finnhub `forwardPe` is mapped to a trailing P/E (Day 123)
`field_maps.py:73` maps `forwardPe` to Finnhub's `peBasicExclExtraTTM`, a trailing P/E. Anything
labelled "forward P/E" from Finnhub is wrong (an old `scoringEngine` input). The Fundamentals
card uses trailing P/E only. **Fix:** remap or drop the field.

### Low: page-level horizontal scroll at 390px (Day 123–124)
The top tab bar and the Analyze button make the whole page scroll sideways on a phone. The
cards themselves fit; the page verifier checks that (A9) and reports this one without failing.
**Fix:** wrap/scroll the tab bar.

### Low / Info: Context VIX (daily close) and Analyze VIX (latest quote) can differ slightly (Day 124)
Both use the same band words now (`vix_bands.py`), but the Context phase reads the daily
close while the Analyze backdrop shows the latest quote (labelled "latest quote"). Expected.

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

### Low: Value tab's FCF Yield gets a pass/fail badge despite the spec saying it shouldn't (carried from Day 108)
**Fix:** Needs a product decision.

### Low: `backtest_adapter.py` latent short-date-range logic gap (carried from Day 108)
**Fix:** Worth a look before this function gets a new caller.

### Low / Info: SRPS screener's R:R structurally disconnected from real support/resistance (carried from Day 105)
**Fix:** Not actioned — informational screen, disclaimer covers it.

### Low / Info: two independent 1-year-return calculations exist in the frontend, currently in agreement (Day 117)
`simplifiedScoring.js`'s inline RS calc and `rsCalculator.js` (Full Analysis) both span 251
bar-intervals; the backtested `Config G` filter spans 252. Measured bit-identical across 50
live tickers, traced to a shared origin in `backend.py`'s `hist.tail(260)` slice — two specific
conditions could desync them (NaN-row skipping; the short-history case above), neither observed
live. Do not "fix" the 251-vs-252 mismatch — that line drives the live Momentum gate.

### Low / Info (moot Day 125): "Industry-Standard Report Card" Artifact's MTF/Pattern-Detection grades are stale (carried from Day 118)
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
