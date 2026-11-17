# Known Issues — Day 126

> Supersedes `KNOWN_ISSUES_DAY125.md`. Day 126: indicator formula audit, stock-split mechanism, Validate tab
> deleted / Forward Test tab hidden, Technical Read turned into plain facts, price ruler on real averages,
> three-pass review hook (v4.66, Backend v2.55, Frontend v4.63).

## Changes from Day 125

- **Fixed (Day 126, Statement Audit findings, all four): zero-volume data, dividend-adjusted high, ADX forming bar, threshold rounding, plus three more the re-run caught.**
  Plan `docs/claude/design/STATEMENT_AUDIT_FIXES_PLAN_DAY126.md` (Opus review: 11 points applied).
  1. **Zero volume (SOXL.NE printed "50.00x normal volume").** `/api/sr` now reports `meta.volume {available, daysWithVolume, windowBars}`: volume is usable only when at least
     `MIN_VOLUME_BARS` (40, imported from breakout_detection.py) of the last 50 COMPLETED bars have volume > 0 (NaN = missing). Otherwise RVOL, its display text, OBV and the prior-bar RVOL are
     None and a log line says why. The card shows "No volume data: the data source reports no shares traded on N of the last 50 days, so the volume checks are left out." and hides the bars,
     tally and detail. `pickVolumeBar` (technicalReadChecks.js) is the one place that chooses which bar's numbers are read; the three `?? today's` fallbacks are gone.
  2. **1-year high / 52-week low.** `/api/stock` always takes them from the same adjusted bars as the Technical Read (Golden Rule 63), not Yahoo's unadjusted figure (F: $17.38 on both cards, was $17.38 vs $17.78).
  3. **ADX and OBV on completed bars** in `/api/sr` (was 0.5-1.1 ADX points off mid-session). Intended behaviour change: during the trading day a stock near ADX 20 (the HOLD gate), 25 (entry preference) or 15 (KeyLevels "choppy") can read on the other side of a line compared with before; it now matches the backtests, MR, `/api/stock` and `/api/patterns`. After the close nothing changes.
  4. **closeLocation** is no longer rounded to 2 decimals (AAPL 0.2526 was called "near the day's low").
  5. **Caught by the re-run:** effort-vs-result divided ATR by TODAY's live price (now the described bar's close); the quote's last close rounded to 4 dp so SMCI read $25.02 beside $25.03 (now 2 dp like the bars); and **one money format for the page** (`utils/formatMoney.js`): the header used `toLocaleString` and the cards `toFixed`, so RIVN at $12.045 read "$12.05" in the header and "$12.04" in the Entry block, and $1,234.56 read without the comma on the cards. Header, Technical Read, pullback plan and MR rows now share one formatter.
  Tests: `backend/test_sr_volume_unavailable.py` (18), `test_audit_statements.py` (25), `test_live_quote.py` (63), frontend `test_entry_timing.mjs` (84), `test_format_money.mjs` (6). Statement Audit re-run on 7 tickers: 266 PASS, 0 WRONG, 0 MISLEADING, 12 UNVERIFIED (two sentence rules not mirrored yet). Page checker 55/55 (5 tickers).
- **Added (Day 126): the Statement Audit** (MASTER_AUDIT_FRAMEWORK Part 7). Triggered by "+1.5% from a month ago" (really 30 trading days, fixed: "over 30
  trading days"). Recomputes every number on the Technical Read from raw bars and checks the words against the window the code uses; every number token on the card is
  claimed or listed. First run, 7 tickers: `docs/test/Statement_Audit_20261117/REPORT.md` (254 PASS, 5 WRONG, 8 MISLEADING, 15 UNVERIFIED). Findings are logged below.
  Plan `docs/claude/design/STATEMENT_AUDIT_PLAN_DAY126.md` (Opus review v2). Files: `backend/audit_ref.py`, `audit_statements.py`, `test_audit_statements.py` (22 checks),
  `frontend/scripts/dump_page_statements.js`. The pattern_detection.py docstring "at least 1 month" now says 30 trading days.
- **Fixed (Day 126): `/api/stock`, `/api/market/spy` and `/api/patterns` now leave out today's unfinished bar (completed bars only).**
  Measured first: mid-session the partial bar made ATR read 0-1.5% low (worst 3.4%), EMA21 off by under 0.5%, SMA50/200 ~0. The Opus review
  found the plan's first version would have mixed bases (SPY and `/api/patterns` did not drop it), so all three routes got the same
  `market_time.drop_forming_bar` rule: relative strength now compares the stock and SPY over the same days, and the trend rows match the
  "last close" shown. An IPO with only today's bar gets a clear 404, not a crash. `/api/stock` adds `formingBarDropped` (nothing in the UI
  reads it). Volume card: `deriveEntryVolume` now treats the last bar as complete when S&R says "partial" and its prior-bar date equals the
  history's last date (no false warning, 50-day average includes that bar); the 16:30 race and real mismatches still warn. Plan:
  `docs/claude/design/STOCK_FORMING_BAR_PLAN_DAY126.md`. Tests: `backend/test_forming_bar_routes.py` (16), entry-timing 69, page checker 44/44.
  The earlier caveat in the live-price entries (partial bar in averages/ATR) no longer applies. Cache untouched (raw).
- **Changed (Day 126): Entry checks "Price vs its 21-day average" is now a gauge plus a ladder (display only).** The old price ruler was
  hard to read. The gauge places the price and the 21, 50 and 200-day averages by how many normal day-moves they sit from the 21-day
  average (scale -5 to +3; the 21-day average is at 62.5%); anything beyond the scale is pinned to the edge with an arrow and its real
  distance written out. Under it a ladder (real table) lists the real prices highest first, the compared price at its true place, with
  "N% above/below" the same base and sign as the sentence. Row name comes from the same basis label as the sentence (Now / After hours /
  Last trade… / Last close). Colours only name lines (sky = price, amber = 21-day, violet = 50-day, pink = 200-day), never good/bad.
  Plan: `docs/claude/design/ENTRY_GAUGE_LADDER_PLAN_DAY126.md` (v2, Opus review: 13 points applied). `deriveEntryTiming` lost price
  `lo`/`hi`, gained `unitsMin/unitsMax`, per-mark `units/off/gapPct`, `ladder`, `priceOff`. Page check A12 now also checks the ladder
  against the gauge marks and the dot (page against itself: the averages are computed in the browser). 60 + 160 unit checks, page
  checker 44/44 (AAPL, SOXL.NE, NVDA, RIVN), screenshots at 390px and 1280px checked. Not changed: any number, rule, stop or verdict.
- **Changed (Day 126): the Entry-checks block measures from the live price.** The sentence, the white bubble and the
  "normal day's move" distance use the live price when one exists, labelled `(now)` / `(pre-market)` / `(after hours)` /
  `(last trade 2:51pm ET)`; without one they use the last bar, labelled `(last close)`. A grey `Last close $X · date`
  note (from the quote's completed bar) sits under the ruler; the amber marker was removed. The "Is it in an uptrend?"
  rows stay on the close and say so. Pullback plan wording changed from "now / today's price" to "last close" (wording
  only, Trade Setup numbers unchanged). Averages and ATR are still the engine's inputs. A12/A13 updated. Plan:
  `docs/claude/design/LIVE_ENTRY_TIMING_PLAN_DAY126.md`. (The forming-bar caveat was fixed later on Day 126.)
- **Added (Day 126): live price in the Analyze header and ruler.** NVDA showed Friday's close ($162.85) while IBKR showed
  $156.10 (-4.14%): a one-day gap, not a delay. New display-only `GET /api/quote/<ticker>` (`backend/live_quote.py`):
  US = Tradier -> Yahoo 1-minute -> Finnhub; Canadian = Yahoo 1-minute only; own `yfinance_live` breaker and rate budget;
  45 s cache; a regular-session trade older than 20 min is "no recent trades". Change is measured from the last COMPLETED
  daily bar (forming bar dropped). Header shows `Now $X (-Y%) · last trade 2:51pm ET` and `Last close $X · date`; an amber
  `live-tick` marker on the ruler; page check A13. Indicators, verdicts and stops are untouched. Plan:
  `docs/claude/design/LIVE_QUOTE_PLAN_DAY126.md`. Real-data run: NVDA 155.99 vs IBKR 156.10, SOXL.NE and GDXU.TO current.
- **Resolved:** SOXL.NE (BetaPro 3x semiconductor, 3-for-1 split on 2026-05-25) had unadjusted history at Yahoo and
  EODHD, so ATR, RSI, S&R and the 52-week high were wrong. Fixed by the split mechanism (table, classifier, adjuster,
  detector). Live: 05-22 close 47.28, 52-week high 74.21, ATR about 2.01.
- **Resolved:** the Data Sources "how indicators are calculated" table was wrong (it did not match the code). Rebuilt
  from `indicator_catalog.py`; 36 tests pin it; no live number changed (golden snapshot 816 values identical).
- **Resolved:** "Simple S&R engine due for replacement" (Day 125 Info) was already done earlier on Day 126.
- **Resolved (by design):** the Technical Read card no longer says Strong / Developing / Weak, and the volume card no
  longer says Yes / Mixed / No. They list plain facts and "N volume signals: a up, b down". The engine's verdict
  calculation is unchanged and parity-tested (86,400); only what the card shows changed.
- **Changed:** the entry ruler now marks the real 21, 50 and 200-day averages instead of +1 / +2 "normal day"
  steps, and always fits the price on the ruler.
- **Changed (display only):** the Mean-Reversion Read card on Analyze was rebuilt as four plain questions, each with a
  bar (2-day RSI, trend vs 200-day average, price, trading volume). Wording uses "2-day RSI", labelled bar ends and a
  one-line reason per rule. Rows come from `frontend/src/utils/mrReadRows.js` (23 tests). Pass / fail still comes
  from the backend `conditions`; `mean_reversion.py` is untouched, so backtest numbers do not move.
- **Resolved (display):** SOXL.NE showed "$0/day" and a failed volume rule. Its provider reports zero volume on every
  bar, so it is now shown as "no volume data" (not checked), not as a fail. The backend still computes 0 there.
- **Changed (user-directed, no backtest check):** sector rotation now follows the standard RRG design (Bloomberg /
  StockCharts style) instead of STA's old "middle of a 6-month window = 100" variant. One shared function in
  `backend/rrg.py` (weekly closes; RS-Ratio = 10-week average of fund/SPY over its 26-week average; RS-Momentum = the
  ratio vs 4 weeks ago; corners cut at 100/100). It is the public approximation, not the proprietary JdK formula.
  Used by the 11 sectors, the QQQ/MDY/IWM size strip (its inline copy of the old formula is gone) and the 21
  sub-industry clusters. Data fetch went from 6mo to 2y. New fields: `tail` (5-week trail), `thinHistory`, `weeks`.
  `rsMomentum` stays centred on 0 so every existing consumer works. Sectors tab gained the RRG chart with trails.
  Today's corner changes: sectors XLE, XLF, XLB, XLY, XLC, XLRE, XLU moved; 7 of 21 sub-industry clusters moved.
  Size signal went Neutral -> Risk-Off (IWM minus QQQ is -2.87; gap threshold is now 1.0 on the new scale).
- **Changed (Sectors tab trimmed to facts):** the takeaway sentence, "Scan Top Sector" button, corner-count chips, macro
  line, Risk-On/Risk-Off label and the "most trade-ready / avoid" hints are gone. The 11 sector cards became one compact
  table (corner, ratio, momentum, 1 wk, 1 mo, Scan link); the cap-size strip shows numbers and its corner. The two
  pullback screeners are hidden (`SHOW_PULLBACK_SCREENERS = false`, same idea as the hidden Forward Test tab); their
  endpoints still work. Sub-Industry Watch gained its own RRG chart + table; the 6 clusters that use a broad-sector ETF
  (Optical, Enterprise Tech, Financials, Communication Services, Energy, High-beta mega) are computed but flagged
  `coveredBySector` and listed in one line instead of repeating a sector row. Cached rotation responses carry
  `rrgVersion` (2); older cached rows are ignored. Independent Opus review of the change: 5 findings, 3 fixed
  (cache version, pullback screener keeps all 21 clusters, size strip corner now comes from the backend), 2 logged below.
- **Changed (Sectors tab layout, user-chosen from a mock-up):** the compact table became a ranked leaderboard
  (`SectorLeaderboard.jsx`, row model in `utils/leaderboardRows.js`, 23 tests): per row a strength bar centred on 100, a
  momentum arrow, a 5-week line, the corner pill, and "Moved: A -> B this week" when the corner changed a week ago. Tap a
  row for the 5 weekly values, 1 wk / 1 mo change and the Scan link. The RRG chart sits behind "Show chart". Same layout
  for Sub-Industry Watch. Each trail point from the backend now carries its own `quadrant` (so the UI never repeats the
  corner rule); `rrgVersion` is 3, so older cached rows are ignored.
- **Added (process):** a Stop hook blocks the end of a turn when code changed and no three-pass review stamp exists
  (`.claude/hooks/three_pass_check.sh`, `/three-pass`, Golden Rule 64).
- **New (Low / Info):** the items below under "Day 126 — Technical Read and volume card".

## Open Issues

### Low: live quote limits (Day 126)
No exchange calendar exists, so the session comes from the trade's own time. On an early-close day the session reads
"regular" until the last trade is older than 20 minutes. Pre/post-market trades have no age limit (thin by nature). The
Scan tab, leaderboards and the Technical Read card's own numbers still use closes. The header "Last close" line comes from
the quote answer. (The `/api/stock` forming-bar issue that used to make them differ was fixed later on Day 126.)

### Low: `backtest/sector_quadrant_history.py` is out of step with the live RRG (Day 126)
It replays 126-day windows through `compute_rs_ratio_and_quadrant`; the new weekly formula needs about 16+ weeks, so
the replay and SRPS Gate-1 numbers no longer match the live formula (the script now carries a warning in its docstring).
The pullback screeners' quadrant gate also uses the new RRG corners, not the rule that was backtested. Research tooling
only; not fixed (user does not rely on backtests).

### Low: dead verdict text and loose bounds left in the rotation backend (Day 126)
`/api/sectors/rotation` still computes `size_signal`, `size_signal_detail` and `macro_alignment` (verdict-style text) that no
screen shows; `macro_alignment` still calls the cycles and econ endpoints on every fresh fetch. `test_sector_rotation.py`
still checks `size_signal`, and its ratio sanity bounds (40-300; sub-industry 30-350) no longer catch a units bug on the
new ~94-106 scale. The cache key ignores `?period=`, so one odd-period call could cache for the day (pre-existing).
yfinance 2y returns ~502 rows, under the cache's 504-row minimum, so 2y OHLCV never hits cache (pre-existing).

### Info: sector corners are sensitive to the RRG window choice (Day 126)
With the 10 / 26 / 4 week windows several sectors sit near the lines; a different window moves them. Guidance only,
like the rest of the page. `indicator_catalog.py` still lists `compute_rs_ratio_and_quadrant` under the RS 52W row
as a "live copy"; the formula behind it is now `rrg.py`.


### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

### Low: after the forming-bar fix, three small leftovers (Day 126)
- **52-week high/low** come from Yahoo's info and can include today's intraday high/low, while `currentPrice` is now the last completed
  close, so "% from 52-week high" mixes the two mid-session (tiny).
- **`/api/sr` keeps today's partial bar on purpose** for `currentPrice`, daily RSI, market structure, `change`, today's RVOL and the candle
  (the Day 85 watchlist needs them); levels, ATR, ADX and OBV now use completed bars (Statement Audit fixes, same day). Neither daily RSI nor market structure has a frontend consumer.
- **Averages are dividend-adjusted.** The 50/200-day averages, the ladder and the 1-year high/low use dividend-adjusted bars, so for a dividend payer they sit slightly below an unadjusted TradingView chart. The Technical Read explainer says so; no fix planned.
- **SOXL.NE's completed bars are flat** (open = high = low = close, volume 0): the day's close position is undefined and ATR/ADX come only from close-to-close gaps.
- **Early-close days** (next: Nov 27, 2026, the day after Thanksgiving): the 16:30 ET rule hides that day's final bar from about 13:00 to 16:30.

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

### ~~Info: the S&R engine is due for replacement (Day 125)~~ — DONE Day 126 (simple engine live; the Simple Checklist that read the levels was removed)
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

### Day 126 — indicator audit findings (logged, NOT fixed; no live number changed)
Source: `design/INDICATOR_FORMULA_AUDIT_PLAN_DAY126.md`, `docs/test/Indicators_20261114/REPORT.md`. Tests: `backtest/test_indicators.py` (inventory test fails on any new indicator file not in `indicator_catalog.py`).
- **(Low) Paper-trading stops use a different ATR than the Analyze stop.** `trade_simulator.calculate_atr_at` (pandas `ewm`, 51-bar window) vs `simple_sr.wilder_atr` (full history): median 0.63%, max 2.85% apart on 24 tickers. Golden Rule 60 applies to paper results; no change (program discontinued Day 113).
- **(Low) One verdict rule, three RSI sources.** Analyze uses JS `calculateRSI`; paper trading takes RSI/ADX from TradingView; backtests use pandas `ewm`. JS vs backend differ by at most 0.03 at the last bar, up to 1.5-3.8 on 20-30 bar histories. A flat history gives 100 (JS) vs 50 (Python).
- **(Low) Backend `calculate_rsi` / `calculate_rsi_4h` have no consumer**; the 4H one spends an intraday call (Twelve Data first) on every `/api/sr`. Candidate removal.
- **(Low) ADX copies differ on tie bars** (up move = down move > 0): `backend.py` counts neither, `mean_reversion.py` and the backtests count -DM; worst gap 1.2 points (AMD.TO). Pinned by a test; consolidation needs its own plan.
- **(Low) Avg volume 50 / RVOL include today's unfinished bar** (ATR is the only indicator that leaves it out). RVOL reads low mid-session.
- **(Low) RS "52 weeks" is 251 bars back**; under 252 bars it silently uses the oldest bar. Python `calculate_rs_52w` (`shift(252)`, used by paper trading) is one bar different from the JS copy.
- **(Low) `/api/value` hard-codes `'source': 'finnhub'` for PEG** (`backend.py` ~4057) even when Alpha Vantage, Yahoo or the local fallback supplied it.
- **(Low) `|| 50` in `categoricalAssessment.js:92,766`** also turns a real RSI of 0 into 50 (sits next to the Day 123 item).
- **(Low) Dead code, one cleanup item:** `pattern_detection.calculate_atr`, JS `calculateATR`, `analyzeTrendStructure`, `calculateTradeSetup`. The Leveraged ETF Board's ATR comment cites the dead `pattern_detection` function, so re-point it first. Frontend `calculateATR` is a simple mean: 10% median / 17% max away from the live ATR.
- **(Low) Four ATR implementations and several ETF-rule copies remain** (Golden Rule 59 map is in the catalog `copies`); reference JSON files under `backend/reference/` are refreshed by hand.

### Day 126 — split mechanism (built; items below are what it does NOT cover)
Plan `design/SPLIT_MECHANISM_PLAN_DAY126.md` (v2), tests `backtest/test_split_adjust.py` (81), sweep `backtest/audit_splits.py` (74 cached histories: only SOXL.NE had an unadjusted split).
- **(Medium) The table is hand-kept.** A split is adjusted only after someone verifies it and adds a row. Unknown splits are caught by the Data Sources tab (FAIL) only for tickers the user opens; a weekly watchlist-wide scan would remove that dependence (not built).
- **(Low) 3:2 / 4:3 splits are invisible to the detector** (the 40% threshold cannot see them); only the table can handle them.
- **(Low) Bulk Yahoo downloads are not split-adjusted by STA** (sector rotation `backend.py` `yf.download`, `scan_queries.py` RS ranking, `market_phase_engine.py`): US symbols that Yahoo adjusts. Backtests and the TradingView scan are out of scope.
- **(Low) Paper-trading ledger rows that cross a split are wrong** (MNST -50.8% "stop_hit_gap", SOXX); the program is discontinued, so not repaired.
- **(Low) SOXL.NE stays FAIL on the tab** (100% flat bars, zero volume: close-only data, ATR is an approximation). Seven `.NE` CDR symbols (ANET, ASML, AVGO, GEV, MU, SNDK, WDC) have no usable cached history (the CDRs trade on `.TO`).
- **(Low) Tradier applied QPUX's 1-for-3 reverse split the wrong way, one bar early**; it is not in the price chain for SOXL.NE, and the classifier would flag it `wrong_way`. A Tradier jump guard is still not built.

### Day 126 — tabs removed / hidden
- **(Info) Validate Data tab deleted** (frontend only: tab, state, handler, `runValidation`, `fetchValidationHistory`). The backend `/api/validation/run|results|history` routes, the `validation/` package and `validation_available` in `/api/health` are now dead code, left for a separate cleanup.
- **(Info) Forward Test tab hidden** (button removed from the tab bar; its code stays, unreachable). `/api/paper-trading/*` routes and the daily job are unchanged.

### Day 126 — Technical Read and volume card (new, Low / Info)
- **(Info) Verdict wording still exists inside the engine.** `deriveTechnicalRead` / `assessTechnical` (Strong / Decent / Weak) and
  `getVolumeDirectionRead` (buying / mixed / selling) still compute a lean; the cards no longer show it. Other consumers (Scan, the
  verdict column, backtest parity) still use it. Removing the engine verdict is a separate, parity-tested change.
- **(Low) The volume card's numbers (OBV trend, relative volume, close location) were read from `/api/sr` but their backend formulas were
  not independently re-tested this session.** The indicator audit covered the eight table indicators (SMA, EMA, RSI, ATR, ADX, avg
  volume/RVOL, RS, PEG), not OBV.
- **(Low) The ruler mixes a fast 21-day average (exponential) with simple 50 and 200-day averages**, as the indicator table already says.
  The card explainer states it.
- **(Info) The orange "heavy volume while OBV is falling" box still appears.** It states a fact and says it is not a sell signal.
- **(Info) Three-pass hook limits:** it forces the review and records it; it cannot judge review quality. A second consecutive Stop is let
  through so a session never loops. The stamp covers every changed code file in the working tree, including earlier uncommitted work.
