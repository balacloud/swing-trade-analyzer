---
type: history
name: known-issues-low-and-resolved
description: Low, Info, resolved and per-day change sections moved out of KNOWN_ISSUES_DAY132.md on Day 133 (every heading triaged by hand). One living file; append new Low/resolved items by `## Day N` section.
last_updated: Day 133 (2026-11-24)
---

# KNOWN ISSUES: LOW, INFO AND RESOLVED (L3)

> Moved word for word from `KNOWN_ISSUES_DAY132.md`. Open Medium+ items live in the latest `versioned/KNOWN_ISSUES_DAY[N].md`. Read this file on request, or when an open item points here.

Original file header:



# Known Issues — Day 132

> Supersedes `KNOWN_ISSUES_DAY131.md`. Day 132: no STA code change; nothing resolved or added. v4.70 (Backend v2.58, Frontend v4.66). Day 131 (carried): the two Medium verdict-engine bugs fixed. Day 130 (carried): docs-only. Day 129 (carried): Tradier leveraged-fund rule, Alpaca first US source.

## Changes from Day 131

- **None.** No issue resolved, none added. The Day 132 session was spent on a non-STA task. Still open and next: Alpaca in-session bar check (needs a market day), DRAL RS1 smoke-audit row, refresh `data_audit_latest.json`.

## Changes from Day 131 (carried, as written Day 131)

## Changes from Day 130

- **Fixed (Day 131): missing RSI is no longer a fake 50.** `categoricalAssessment.js` `assessTechnical` / `runCategoricalAssessment` and `categorical_engine.py` `assess_technical`: a missing RSI (null, undefined, NaN, Infinity; Python also None or non-finite) is "unavailable". It cannot make a stock Strong; it can still be Decent when the trend checks are 5+ (same precedent as missing RS, Day 78), otherwise Weak. Missing is checked before any comparison (JS `null < 30` is true; Python `None < 30` raises). A real RSI of 0 is now kept (JS used to turn it into 50). `data.rsi` is null and `data.rsiAvailable` comes from the same value. A missing RSI can still reach BUY (Decent technical plus Strong fundamentals in position mode, `determineVerdict` ~:706): accepted. Only very young tickers (fewer than 15 bars, `calculateRSI` returns null) are affected in practice.
- **Fixed (Day 131): missing SPY is no longer described as "below its 200-day".** The RESULT is unchanged (Unfavorable, so no BUY while the market trend is unknown; user decision between this and "Neutral unless VIX > 30"). The reason text says "SPY trend unavailable, treated cautiously (no BUY until it loads)". `riskMacro.data.spyAbove200EMA` is now null when unknown (App.jsx:2001 and forwardTesting.js:387 already handle null); `spyAvailable` comes from the same value.
- **Fixed (Day 131): two false texts on the Technical Read card** (`TechnicalRead.jsx:77`, `:281`) that said "the engine assumed 50, which counts as a pass".
- **Tests (Day 131):** `test_verdict_parity.py` grid now has RSI 0 and None and SPY None (86,400 -> 172,800 rows, 0 mismatches); the original 86,400 rows give identical verdicts to a saved baseline, matched by input on technical, risk_macro and verdict; `test_engine_missing_inputs.py` (+ `frontend/scripts/missing_inputs_check.mjs`) covers None, NaN, 0, Infinity and SPY None in both copies. Mutation check: with the fixes stashed, parity broke on 17,280 rows and 5,184 rows showed a missing RSI as Strong. Plan and Opus review: `docs/claude/design/ENGINE_MISSING_INPUTS_PLAN_DAY131.md` (GO WITH CHANGES, applied).
- **Corrected (Day 131): the "Mean-Reversion route reads Yahoo directly" line (Days 128-130) was WRONG.** `/api/mr/signal` (`backend.py:3866-3875`) and `/api/mr/scan` (`:3940-3948`) call `get_data_provider().get_ohlcv()` first (Alpaca -> Twelve Data -> Yahoo -> Tradier); live `curl` gave `"dataSource": "DataProvider"`. Direct Yahoo is used only if the whole chain fails, and the answer then says `dataSource: "yfinance fallback"`. No code change. I repeated the stale line earlier this session before reading the code.
- **Fixed (Day 131): version strings were behind the docs.** App footer said v4.64 (now v4.70); `BACKEND_VERSION` said 2.57 (now 2.58, what the docs have claimed since Day 129). Trivial stamp.

### Low (new Day 131): other copies of the missing-input rules, not changed
- `backend/backtest/parameter_stability.py:172,181`: research script with its own overridden thresholds; its `50` only covers an out-of-range index.
- `trade_simulator.py:121`, `backtest_holistic.py:299`, `nirmal_validation.py:366` turn missing SPY into "above" (assume bull), the opposite rule, backtest-only. `scoringEngine.js:393` spyRegime score.
- `categorical_engine.assess_technical` raises `TypeError` if RSI is a non-number (a string); callers pass floats or None.
- `assessSentiment()`'s `fearGreed || 50` (informational, gates nothing) is the only `|| 50` left of this family.

## Changes from Day 130 (carried, as written Day 130)

## Changes from Day 129

- **Docs only, no app code, no API change, no version change (v4.69).**
- **Added (Day 130): `ENGINEER.md` "what has been missed" table now covers all days** (12 new themes from Golden Rules 18-61) and carries a note on the rule-numbering gap below.
- **Pushed (Day 130): 1,212 previously untracked files** (research docs, audit results, backtest outputs; commit `fa38621e`). Left out on purpose and still untracked: `.venv` and `node_modules` under `docs/Options_Reference_for_Build/backend` and `/frontend` (about 200 MB, another project), the `.db` there, all `.log` files (including `backend/paper_trading/logs/` and `validation_results/nightly/**/*.log`), `.playwright-mcp/`, `.vscode/`.
- **No change to any Day 129 open issue.** Alpaca in-session bar, the cache clear and the user decisions (Alpaca terms, Twelve Data key) all still wait.

### Low (new Day 130): Golden Rule numbering gap
`GOLDEN_RULES.md` has no Rule 27 (26 jumps to 28). The "replay reads stored entry values" rule is numbered 29 but cited as "Rule 27" in `CLAUDE_CONTEXT.md` (Day 91) and the ROADMAP. The header says 68 rules; there are 67. Not renumbered (rules are cited by number everywhere). User declined renumbering at close.

### Low (new Day 130): `CLAUDE_CONTEXT.md` update log has missing rows
No rows for Days 71 and 120-123, 126, 127 (they appear in the day summaries or other files). Not backfilled.

### Info (new Day 130): the engineer persona's record is built from Golden Rules, the persona log and the update log
The 112 status files were not read line by line, so small misses that never became a rule may be missing from the table.

## Changes from Day 129 (carried)

- **Fixed (Day 129): leveraged funds are never served by Tradier.** `providers/fallback_policy.py` (`NO_TRADIER`, 22 symbols); a 60-second failure memo for blocked tickers; stale Tradier copies refused; the Data Sources tab adds a `source` check when Tradier served the data (WARN, FAIL if blocked); audit C8 reads the tab's checks. 32 tests. Plan: `TRADIER_FALLBACK_RULE_PLAN_DAY129.md`.
- **Fixed / changed (Day 129): Alpaca is the first US source** (chain Alpaca -> Twelve Data -> Yahoo -> Tradier; Canada Yahoo only). Real-data acceptance on 79 US tickers: 100% of closes within 0.5% of Yahoo, 96% of Twelve Data. 66 tests. Plan: `ALPACA_PROVIDER_PLAN_DAY129.md`.
  This relieves the "Twelve Data keeps hitting its limit" issue below (not yet re-measured).
- **Fixed (Day 129): Twelve Data HTTP 404 counted as a provider failure.** Twelve Data answers 404 for symbols it lacks (`.TO`, `.NE`, `^VIX`, `BRK-B`); the code had no 404 branch, so each one was a false breaker failure (315 "404 Client Error" lines in `backend.log`; Golden Rule 36). Now `DataNotFoundError`, no failure; Canadian and `^` symbols make no call and take no limiter token; `-` is sent as `.`.
- **Fixed (Day 129): the Twelve Data API key was written to `backend/backend.log`** (324 lines containing `apikey=`, from the HTTPError URL). New errors carry no URL or key. **Old lines remain in the local, gitignored 11 MB log; rotating the key is the user's decision (open).**
- **Fixed (Day 129): the 4:00-4:30pm cache gap.** A frame whose newest bar is today (New York) and was fetched before 16:30 ET now expires at 16:30 (`cache_manager.set_cached_ohlcv`, `market_time.is_forming_bar`). The Day 128 entry "the 4:00-4:30pm cache gap" is resolved. 4 tests (16:05, 16:20, 11:00, 16:35); a mutation check gave 3 failures with the cap disabled.
- **Added (Day 129): `ENGINEER.md`** (surgeon's lens, checklists, table of past misses), loaded at `/sta-start`.
- **Corrected claims (Day 129):** (1) "Twelve Data's breaker opened about 82 times" mixed two causes (real rate limits plus false 404 failures); do not quote it as a pure rate-limit count. (2) The Tradier plan v1 said "about 25 tickers" (it is 21 at the time, 22 now) and "the tab shows no warning" (the tab already warned on some). (3) The first "after-close" audit re-run reused the morning cache and was discarded; the valid run is stamp `20261119_pm`.

## Changes from Day 127 (carried from Day 128 file)

- **Fixed (Day 128): a bar with no close price no longer reaches any card.** 15 cached Yahoo tickers (AAPL, MSFT, META, NVDA, AVGO, LLY, V, WMT, PG, HD, ABBV, KEYS, MRVL, VRT, ALAB) had a Nov 18 newest bar with
  open/high/low/close all empty and a normal volume, kept until the next close, so `/api/sr` answered `"currentPrice": NaN` (invalid JSON). The cache stays RAW; rows are dropped when a frame is SERVED
  (`market_time.drop_empty_close` in `orchestrator._deliver` and `split_adjust.fix_frame`); a frame with an empty newest close is cached 30 minutes only (`cache_manager.EMPTY_NEWEST_BAR_TTL_MIN`);
  `data_quality.check_history` takes "last bar" from the last bar WITH a price and FAILs `newest_close_missing` (Data Sources tab and audit C4); `/api/stock` answers 404, not a fake price of 0, when no bar has a close;
  page checker A14 fails on an unreadable or non-numeric price answer (the runner used to only warn). Tests: `test_empty_price_row.py` (44; 17 fail with the fix switched off). The 15 entries were refreshed (price history only).
  Plan: `docs/claude/design/EMPTY_PRICE_ROW_PLAN_DAY127.md` (Opus review applied).
- **Fixed (Day 128): Tradier HTTP 400 handling.** Tradier returns 400 (not 429) for BOTH a quota violation and a bad request; old code counted every 400 as a provider failure, so unknown tickers could open the breaker
  (Golden Rule 36). Now: body "symbol not found" -> `DataNotFoundError` (no failure); body "quota" or `X-Ratelimit-Available` 0 -> `RateLimitError` (+failure); any other 400 -> loud `ProviderError` (no failure);
  empty symbol -> no request. Tests: `test_tradier_errors.py` (61, against a throwaway state file). Plan: `TRADIER_ERROR_HANDLING_PLAN_DAY127.md` (Opus review applied).
- **Added (Day 128): the first full truth-free audit of the 117 tickers** (`docs/test/DataSources_20261119/REPORT.md`) and a draft fetched-versus-computed inventory for the Analyze page (`INVENTORY.md`).
- **Corrected claims (Day 128), kept here so nobody repeats them:** (1) "the audit used up Twelve Data's limit" is WRONG: the app cache already showed Yahoo for 61 of 97 US tickers before the audit ran, and the app log shows
  the Twelve Data breaker opened 82 times. (2) "Nothing checks for an empty row" was WRONG: `data_quality` already counted `nan_closes`, but "last bar" was taken from the empty row so freshness read "current".
  (3) "Yahoo had not finished the day" is a GUESS (the fetch was 5 hours after the close; other tickers fetched then are clean): cause unknown. (4) The "~8 minute" audit duration was never measured.

## Open Issues

### Low-Medium: not every API answer is NaN-safe (Day 128)
There is no custom Flask JSON provider, so any NaN that reaches a response goes out as invalid JSON. The serve-time drop fixes the price frames, but other NaN sources (indicators, OBV, ratios) are guarded one by one.
A single "NaN becomes null" encoder would be a safety net with a wide blast radius (every endpoint), so it needs its own plan.

### RESOLVED Day 129: the 4:00-4:30pm cache gap (Day 128, found by the Opus review)
A frame fetched between 16:00 and 16:30 ET is kept until the NEXT day's 16:30 (`cache_manager.calculate_ohlcv_expiry`), and after 16:30 `drop_forming_bar` treats that possibly partial bar as complete for the whole next day
(`market_time.py` cutoff vs the cache expiry). **Fixed Day 129** (see Changes above).

### Low: audit C9 includes the unfinished day (Day 128, found by the Opus review of the IBKR plan)
`backtest/audit_data_sources.py` (~:303) compares the last 20 common closes including today's forming bar when run mid-session, so two providers' different intraday prices read as a disagreement (QPUX -3.98% and DRAL +3.33% on Nov 19; both false). With the unfinished day excluded, 0 of 79 tickers differ by more than 1% on any completed day. Fix: drop the forming bar in C9 like C2 does (small, plan not needed beyond a three-pass), or run the audit after the close. Not changed.

### Low: leftovers from the empty-price-row fix (Day 128)
- The cause of Yahoo's empty Nov 18 bar is unknown (the fetch was 5 hours after the close and other tickers fetched then are fine). The serve-time drop and the 30-minute cache make the app safe, not the cause known.
- The page shows the previous day's price (and live-quote change measured from it) while a bad newest bar is dropped; the date shown is honest. `live_quote._last_close` could add a check against the expected last session.
- SO's first cached row (2024-11-18, volume 0) is a known Yahoo leading-empty-row artifact: a WARN, not a FAIL.
- `/api/stock`'s new "no bar has a close" 404 is a guard that is normally unreachable (the serve-time drop empties such a frame first and an earlier branch answers 404).
- The nightly audit does not read the app's cache (it fetches providers directly), so it cannot see a bad CACHED row; the Data Sources tab and the page checker (A14) do.
- ~~The Mean-Reversion route reads Yahoo directly~~ — WRONG, corrected Day 131: it goes through the provider chain first (see Changes above).

### Low: leftovers after Day 127
- Twelve Data intraday (4H RSI) is split-only while the Yahoo intraday fallback is adjusted.
- Fundamentals provider 404s under load (a retry was added Day 127, not a cure).
- Thin-ETF volume wording differs between the MR read and the Technical Read; ADX/RSI differ by up to 0.8 on young funds; liquidity (Yahoo avgVolume) vs bars is LOW.
- `compare_sr_engines.py` output is no longer comparable with the Day-126 table (the Buy can be the last close).
- Entry "last close" is not a fill price (Golden Rule 60: you get the next open); the card says "the last close".
- The Day-126 entry saying 52-week high/low "come from Yahoo's info" is out of date: `backend.py:1138-1150` computes them from the bars (Yahoo is only the short-history fallback); `avgVolume`/`avgVolume10d` are the fetched ones.

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

### ~~Medium: the Buy can disagree with the nearest support zone (Day 126)~~ — FIXED Day 127 (zone price is inside = distance 0; the Buy is the last completed close when it is inside the zone)
`simple_sr.pick` chooses the nearest support by distance to the zone EDGE and ignores `insideZone`, while the Buy is `max(support)` (riskRewardCalc.js:42, sr_plan.py:28) and the Support row
and shaded band follow the `nearest` flag. If price sits inside zone A near A.low and a width-capped neighbour B ends just below A, B is flagged nearest but the Buy is A.high.
The audit asserts "Buy == nearest zone's edge" per ticker (TS1b) and a planted fixture proves it fires. Engine change needed; not made.

### Low: leftovers from the phase-3a audit (Day 126)
- **VIX "(latest quote)"** has no quote time in `/api/market/vix`, so freshness cannot be checked; the band is chosen from the 2-dp value but the card shows 1 dp (24.96 would read "25.0 · elevated").
- **MR display rounding at the other cutoffs:** price `$9.995` or dollar volume `$24.95M` can display as the cutoff; RSI is fixed (one decimal), these two are not.
- **MR "FORWARD-TESTED" badge and "The plan, as tested"** (Buy / Stop / Sell steps) are claims and instructions the audit lists but does not verify; the MR route uses its own 1-year provider frame, not `/api/stock`.
- **Fundamentals provider fields** (sales, ROE, debt/equity) cannot be recomputed; Finnhub, Alpha Vantage and Yahoo define D/E and ROE differently (the yfinance ROE is one quarter, not trailing twelve months), so a cross-provider number check would fail on definitions. "Weaker signal for banks, utilities, REITs" has no code branch (reviewed copy, not tested).
- **Backdrop provenance:** the app's index history is Twelve Data's 504 bars while a Yahoo reference starts a few days later, so "largest in data back to <date>" is graded over the app's own span only.
- **Not yet audited:** the Data Sources tab (phase 3b), planted-payload branch tests through Playwright (signal true, VIX band edges, no-down-day, unavailable backdrop), other tabs.

### Low: leftovers from the phase-2 audit (Day 126)
- **Levels sit on a side of price using `/api/sr` currentPrice (today's live bar)**, the card's words use the last completed close; a zone between the two can sit on a different side than the words say (mid-session only).
- **Provider disagreement:** SMCI's Nov 16 close is 25.025 (Twelve Data) vs 25.03 (Yahoo); the header (quote path) and the cards (price bars) can read different providers within a minute and show $25.02 vs $25.03. The audit labels such one-cent gaps LOW.
- **Zone reference mismatches (UNVERIFIED):** the independent reference rebuilds all nearest zones for 6 of 7 tickers but one or two zones on F and SMH differ (a merge decision near the 0.5/1.0 ATR cut on 2-dp bars); inspect, not a failure.
- **Short history RS:** with 200 to 251 bars the stock's year-ago price is its FIRST bar while SPY uses 252 bars, so "RS vs S&P 500" compares different periods.
- **Breakout card fetches its own bars** (NaN volume dropped, not zero) and excludes the breakout day from its volume average; the Technical Read includes the bar itself. Now named in the words; one definition would be cleaner. "Retest holding" also fires when the low undercut the old high by any amount (breakout_detection.py:135).
- **Liquidity (Daily $)** is Yahoo's avgVolume x price: a provider field, not the bars, window unstated.
- **ADX displayed to 1 decimal then compared with 20** (F: 19.97 shown "20.0" reads "20 or more").

### Low: after the forming-bar fix, three small leftovers (Day 126)
- **52-week high/low** come from Yahoo's info and can include today's intraday high/low, while `currentPrice` is now the last completed
  close, so "% from 52-week high" mixes the two mid-session (tiny).
- **`/api/sr` keeps today's partial bar on purpose** for `currentPrice`, daily RSI, market structure, `change`, today's RVOL and the candle
  (the Day 85 watchlist needs them); levels, ATR, ADX and OBV now use completed bars (Statement Audit fixes, same day). Neither daily RSI nor market structure has a frontend consumer.
- **Averages are dividend-adjusted.** The 50/200-day averages, the ladder and the 1-year high/low use dividend-adjusted bars, so for a dividend payer they sit slightly below an unadjusted TradingView chart. The Technical Read explainer says so; no fix planned.
- **SOXL.NE's completed bars are flat** (open = high = low = close, volume 0): the day's close position is undefined and ATR/ADX come only from close-to-close gaps.
- **Early-close days** (next: Nov 27, 2026, the day after Thanksgiving): the 16:30 ET rule hides that day's final bar from about 13:00 to 16:30.

### ~~Medium: `assessTechnical()` treats a missing RSI as 50, and 50 counts as a pass toward Strong (Day 123)~~ — FIXED Day 131 (see Changes above)
`categoricalAssessment.js:327` and `:1001` (`rsi || … || 50`). The display now says "momentum
n/a" (`technical.data.rsiAvailable`, Day 123), but the engine still scores the fake 50.
**Fix:** a parity-tested engine change (JS + `categorical_engine.py` together, Golden Rule 59).
Changes verdicts for tickers with missing RSI, so it needs a plan.

### ~~Medium: `assessRiskMacro()` reads missing SPY data as "below its 200-day", so the market shows Unfavorable (Day 123)~~ — FIXED Day 131 (text only; result stays Unfavorable by decision)
The Regime Read card now says "SPY trend unavailable" (`riskMacro.data.spyAvailable`), but the
engine's regime input is still wrong on a SPY fetch failure. **Fix:** parity-tested engine
change, same as above.

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
was fixed Day 131. `assessSentiment()`'s `fearGreed || 50` remains.

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
- ~~**(Low) `|| 50` in `categoricalAssessment.js:92,766`** also turns a real RSI of 0 into 50~~ — FIXED Day 131.
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

## New open issues (Day 129)

### Low-Medium: Golden Rule 54 note for backtests (Day 129)
`backtest_adapter.download_ohlcv`, `mr_open_entry_retest.py`, `compare_sr_engines.py` and `backtest_adx_rsi_thresholds.py` read history (2y or less) through the orchestrator, which is now Alpaca-first. A re-run reads Alpaca data (closes within 0.04%, volume x0.85-1.01 of Twelve Data), so numbers can differ slightly from the documented ones (for example MR PF 1.50). Not changed.

### Low: Alpaca emits no zero-volume bars (Day 129)
Thin funds can miss whole sessions (BRKU 5, COPZ 2 in the real-data check) that Twelve Data fills with flat bars. Real thin-fund gaps, not an error.

### Low: thin-ETF "errors" are probably conventions (Day 129)
XDRV.TO and CARS.TO (Yahoo closes 2-3% off IBKR) are now believed to be no-trade-day conventions: two sources agree on traded days. Not yet re-checked with Questrade (trade-only candles). SOXL.NE could use Questrade's SOXL.TO as a source (Questrade prices are raw, not dividend-adjusted). FINN.NE (22 bad bars) and BRKU volume stay open.

### Low: Questrade and IBKR connectors are Claude-only (Day 129)
The Flask app cannot call them, so they help audits only, not serving.

## Day 133 (layering session, docs only)

### Low (new Day 133): `README.md` roadmap section is already stale
The README roadmap section did not mirror the ROADMAP before Day 133 and was left untouched by the layering. `/sta-end` Step 5 now says README mirrors the open priorities; fix it when ROADMAP next changes.

### Low (new Day 133): `.claude/commands/watchlist-report.md:53` cites a PERSONA.md phrase that no longer exists
The quoted phrase ("overfitting disguised...") is not in `PERSONA.md`. Not caused by the layering; left alone.

### Info (Day 133): code comments cite closed ROADMAP priorities
`App.jsx:1579`, `live_signals.py:227`, `backtest_holistic.py:103`, `mean_reversion.py:151`. The numbers resolve in `history/ROADMAP_HISTORY.md` ("Closed priority rows"). Do not edit them (editing code would trigger the three-pass hook).

## Day 134

### Resolved Day 134: Alpaca rollout left old sources in the cache (was Medium, Day 129)
Measured: of 138 cached OHLCV frames, 97 were Alpaca, 39 Yahoo, 2 Twelve Data. Only RIVN and RSP were old US frames (Twelve Data); the 37 other Yahoo frames are Canada tickers and `^VIX`, which use Yahoo by design. Cleared those two with `POST /api/cache/clear?ticker=X&type=ohlcv`; both refetched as Alpaca. AAPL, NVDA and SOXL had already refreshed.

### Low (new Day 134): the void banner can disappear after about 16:20 ET for NEO tickers while the Trade Setup levels stay stale
Once the quote state leaves `live` or `recent` the card goes back to the plain last-close plan, while `srData` is still the older bar. Facts-only fallback is the same as before the change; not fixed.

### Low (new Day 134): the mirror case is not shown (live price above the plan's target)
Same helper (`planStatus.js`) could take it later. Parked.

### Low (new Day 134): the void banner does not name the next support zone below the price
Optional. Only the broken zone is named. Parked.

### Info (Day 134): page-level 390px horizontal overflow and SOXL.NE close-only history
Existing items, unchanged by the void-plan work (verified at both widths).

## Day 135

Moved out of `KNOWN_ISSUES_DAY134.md` at the Day 135 close (resolved, or Info). Text word for word.

### FIXED Day 135 (was Low-Medium, Day 131): smoke audit DRAL "RS1" row is WRONG
**Fixed:** the audit was wrong, the page right. The card now adds a reason line between the RS rows ("Needs more than 200 days of price history (N loaded)..."), which broke the audit's adjacent-text pattern; it reported "a number" with no number on the card. `audit_cards.py` now allows the reason line, reports a number only when digits are captured, checks the quoted bar count, and reports UNVERIFIED for unknown text. Original note:
`run_all_checks.sh` fails its smoke audit on one row: DRAL, "a history of 105 bars (<= 200) cannot give a 52-week RS, shown 'a number' vs 'N/A'". Reproduced on the UNCHANGED code (changes stashed), so it is not from Day 131. Same family as "short-history RS" below. Not fixed. Every other check passed (page checker 60/60, UI verify 48/48, parity 172,800).


### FIXED Day 135 (was Medium, Day 134): a stale `.env` or launch environment can silently drop Alpaca again
**Fixed:** `backend/env_loader.py` now loads `.env` for all 6 callers; `.env` wins and the replaced key names are logged and shown in `/api/health` (`env_overridden`). Plan: `ENV_OVERRIDE_PLAN_DAY135.md`. Original note:
`load_dotenv` does not override variables already in the environment, so keys in an old parent process win over a fixed `.env`. Alpaca returned 401, the breaker opened, and the chain fell through to Twelve Data with no loud sign (found Day 133, about 4 days after rollout). Not fixed. Planned: a startup warning when the `.env` keys differ from the launch environment, or an explicit override. Needs a plan, an Opus review and the stamp.


### Low-Medium: `backend/reference/data_audit_latest.json` is stale (Day 129)
The Data Sources tab's reference file holds the Day 128 IBKR run (63 tickers); it has not been refreshed with the after-close or Alpaca results (needs plan + stamp).


### Info (Day 135): leveraged-fund audit state
After the Tradier fix and C11, no leveraged fund FAILs C5. Remaining: SOXL.NE C4 FAIL (Yahoo close-only, 100% flat zero-volume, known); NVDL and QPUX big jumps are real (NVDL +61.7% = 2 x NVDA +31.5%; QPUX +48% on 2026-05-21 matches IBKR). SPCL and QPUX have no matching underlying in the 117-ticker universe. GDXU.TO declared multiple unknown (fitted beta 1.9 vs GDX, corr 0.98). Map entries marked `measured` were identified by correlation, not by prospectus.


### Info (Day 135, later): thin Canadian ETFs now say so in the header
XDRV.TO (82% flat zero-volume bars), FINN.NE (28 malformed bars), SOXL.NE (close-only, no volume) and RBOT.TO, CARS.TO, COPP.TO, SGRD.TO (WARN) show the Data Sources integrity wording under the price. Data unchanged: Yahoo's close differs from IBKR by up to 2.15% (XDRV.TO) and 2.64% (CARS.TO) on settled days and no third source can say which is right; the fix needs the second Canada source (ROADMAP #30). FINN.NE's high/low are not repaired (closes match IBKR).


*Resolved Day 135 note for the "data_audit_latest.json is stale" item above:* refreshed by the 117-ticker audit after the Nov 24 close (offline replay with `--now 2026-11-24T17:00`), then again with the leveraged-fund tracking facts.
