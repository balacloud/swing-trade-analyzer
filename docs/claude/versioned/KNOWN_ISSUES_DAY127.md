# Known Issues — Day 127

> Supersedes `KNOWN_ISSUES_DAY126.md`. Day 127: Statement Audit follow-through (inside-zone Buy plan, nearest-zone fix,
> RS N/A reason), one-command checks and a nightly universe audit, Data Source Audit Round 2 started
> (v4.67, Backend v2.56, Frontend v4.64).

## Changes from Day 126

- **Changed (Day 127): the Buy when price is already inside the support zone is the last completed close (persona decision, Opus review applied).** The old Buy was the zone's HIGH, above the market whenever price sat inside
  the zone (SOXL.NE +8.9%, AMD +5.3%, FCX +4.6%, ETN +3.9%, PLD +1.8%): a "wait for a dip" plan whose Buy fills at once, with risk and reward measured from a price you cannot get and "Size this plan" passing it on. Now
  `sr_plan.plan_entry(zones, last_close)` decides in ONE place: the last COMPLETED close is inside the nearest support zone -> the Buy is that close (`meta.entryBasis = 'last_close_inside_zone'`), otherwise the zone high as
  before (`'zone_high'`; legacy engine `'nearest_support'`). No clamping: the live price (which sets `insideZone`) and the last close can sit on different sides of an edge mid-session, so the label is true only when the CLOSE
  is inside. The stop stays 2 ATR below the Buy (always below the zone: zones are at most 1 ATR wide). The page reads `suggestedEntry` from the backend (the `max(support)` stays only as a fallback), the card header and Buy
  box follow `entryBasis` ("price is already at support", "the last close, inside the support zone"), page check A10 and the audit re-derive the Buy independently, and `validation/engine.py`'s "entry below price" check is now
  `<=` against the last completed close. Real numbers: AMD Buy 503.41 (was 530.13), stop 422.27, R:R 0.53 (was 0.2); SOXL.NE 12.36, 0.49; PLD 125.56, 1.26. Tests: `plan_entry`/`trade_plan` (63 checks), route test with
  frozen clock incl. mid-session and NaN (24), A10 fixtures (165), audit rows (35). Plan `docs/claude/design/INSIDE_ZONE_BUY_PLAN_DAY127.md`. `compare_sr_engines.py` re-runs are no longer comparable with the Day-126 table.
  The last close is not a fill price (Golden Rule 60: you get the next open); the card says "the last close", never "your buy price".
- **Fixed (Day 127): the Buy could disagree with the nearest support zone (PLD), plus three small honesty fixes.** Mid-session universe run (10:13 ET, 112 of 117 tickers on a live regular-session quote): no new
  problems; the live-price and unfinished-bar logic held. **Engine:** `simple_sr.pick` ranked zones by distance to their edge, so on PLD (price 125.56 inside the zone 125.38-127.82) a lower zone 122.60-124.69 won the
  `nearest` flag while the Buy was the inside zone's high; the card showed two different supports. Rule 3 says the zone price is inside IS the support. Fix: the zone price is inside counts as distance 0 (one helper
  used by `pick` and the `meta.zones` sort). Zones never overlap, so `max(support)` (the Buy) is unchanged; only the flag, list order and what reads them change. Plan
  `docs/claude/design/SR_INSIDE_ZONE_PICK_PLAN_DAY127.md` (Opus review applied: audit TS-inv rule, tests in `backtest/test_simple_sr.py` (53) wired into `run_all_checks.sh`, second sort). 25 of 115 tickers have price inside a
  zone; PLD was the only one affected. **Small fixes:** the RS card says why it is N/A ("needs more than 200 days of price history (N loaded)"); the Technical Read tile says "since <first date> (under a year of
  history)" instead of "past year" on short listings; `/api/fundamentals` retries once after an empty answer (about 10 large US stocks got "Can't check" under load). **Found by the tests:** a first draft of the retry would have
  crashed (`time` was not imported in backend.py). **Open for you to decide (design, not a bug):** when price is already inside a support zone the Buy is the zone's HIGH, i.e. above the current price (SOXL.NE +8.9%, AMD
  +5.3%, FCX +4.6%, ETN +3.9%): a "wait for a dip, then buy" plan with a buy above the market. Options: Buy at the last close, at the zone high (today), or at the zone low. Not changed.
- **Added (Day 127): two ways to run the existing checks without remembering to.** (1) `./run_all_checks.sh [--quick]`: every backend and frontend test suite, and (without `--quick`) the page checker and a smoke
  audit on 8 fixed tickers (`backend/audit_smoke.txt`); ends with one line "ALL OK" or "FAILED: ...". Not a hook. (2) `nightly_audit.sh`, scheduled by launchd (`com.sta.nightly.audit`, weekdays 18:00 Eastern;
  plist copy in `docs/claude/design/com.sta.nightly.audit.plist.txt`): the 117-ticker universe (`backend/audit_universe.txt`) through the three audits, output in `backend/validation_results/nightly/<date>/`, a
  one-line history in `nightly/history.csv`, "new WRONG rows since the last run" in `SUMMARY.txt` (`backend/audit_summary.py`), a desktop notification when anything is wrong or under 90% of tickers load. It needs the
  app running and does not start it. Runs after the close, so it does not exercise forming-bar/live-quote logic (run `nightly_audit.sh` or the smoke audit mid-session for that). Disable: `launchctl unload
  ~/Library/LaunchAgents/com.sta.nightly.audit.plist`. No new Golden Rules: these only automate the audits and rules that already exist.

## Open Issues

### Medium: the page audit proves the maths, not the data (Day 127; Data Source Audit Round 2 in progress)
The Statement Audit recomputes from the same bars the page received, so a wrong close, a missing day or a bad split at a provider passes. Round 1 (Day 126) compared 24 tickers with IBKR. Round 2
(`docs/claude/design/DATA_SOURCE_AUDIT_ROUND2_PLAN_DAY127.md`, Opus review applied) does all 117: step 0 DONE (both audit scripts take `--tickers-file backend/audit_universe.txt`, class from `data_quality.audit_class`),
next: the fetched-vs-computed inventory (all `backend/*.py`, about 17 fetches bypass the orchestrator), truth-free audit on 117, IBKR truth for the tickers with a watchlist contract id, the Tradier measurement
(Tradier ~34% of logged history fetches, split-only basis, wrong on reverse splits; Yahoo 52%; likely cause Twelve Data 8/min), Data Sources tab statement audit + Playwright rare states, framework Part 8.
Until then the nightly summary should read "data UNVERIFIED" (S4). Not yet changed.

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


### High: Per-ticker provenance can't distinguish "never checked" from "just failed" (carried from Day 108)
**Fix:** Not actioned — needs a new failure-tracking mechanism, its own session. Oldest open
item from the Day 108 full-system audit.

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
