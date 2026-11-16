# Indicator formula audit: Plan v2 (Day 126, revised after the Opus review)

**Status:** PLAN v2. Step 1 (plan) and step 2 (independent Opus review) done; step 3 (build) and step 4 (three review passes) follow.
**Why (user, Day 126):** "with OHLCV data, we can calculate all this locally?" Mostly yes, but the "How indicators are calculated" table on the Data Sources tab was never checked against the code, and it is wrong in several places.
**Rule:** the table must describe what the code does, a test must fail when they drift, and **no number that feeds a verdict, stop, signal or backtest changes in this build** (Golden Rules 18, 55, 59, 60).
**Review:** Opus, verdict GO with 7 must-fixes. I verified the load-bearing claims against the code (paper trading imports `calculate_atr_at`; `categoricalAssessment.js:766` takes the verdict RSI from the JS indicator; the ADX copies filter −DM differently; live `meta.atr` is `simple_sr.wilder_atr`; `avgvol20` exists in SRPS and MR). All adopted; log in §10.

## 0. What the code actually does (verified)

### 0.1 Rows of the tab's table that are wrong today (`backend.py` ~957-969, ~1020-1034)

| Row | Truth | Evidence |
|---|---|---|
| ATR 14 "EMA(TR,14)" | Live `meta.atr` = **Wilder** (first 14 true ranges averaged, then `(prev×13+TR)/14`) from `simple_sr.wilder_atr`, run on the **full 2-year frame with today's forming bar dropped**. It sets the Trade Setup stop (2×ATR). Not EMA. | `backend.py:1792`, `simple_sr.py:52-70,151` |
| Avg Volume 20 "local" | Not on the Analyze page. A 20-day average exists elsewhere (SRPS `avgvol20` `backend.py:2978`; MR gate `mean_reversion.py:206`), not computed for this table. | grep |
| Avg Volume 50 "local" | Local, but includes **today's forming bar** (`scoringEngine.js:117`, `backend.py:1850`). | read |
| RS 52W "return ÷ return" | `(stock_now / stock_251_bars_ago) / (spy_now / spy_251_bars_ago)`: a ratio of **growth factors**. The "52W ago" price is `iloc[-252]` = 251 bars back; with 201-251 bars it silently uses the oldest bar. | `rsCalculator.js:53-55`, `backend.py:1120-1122` |
| PEG "local: PE/(EPS growth×100)" | **Provider-supplied** through the fundamentals chain Finnhub → Alpha Vantage → Yahoo; that text is Yahoo's *fallback*. The Value tab computes PEGY locally when yield > 1.5%. | `orchestrator.py:94`, `yfinance_provider.py:215-219`, `backend.py:4038-4047` |
| RS Price Ratio "Stock ÷ SPY" | Exists only in the sector-rotation code (`rs_line`) and the Pine script, not on the Analyze page. | `backend.py:2583` |
| SMA, EMA, RSI | SMA right. EMA right but the seed (first close) and "run over all bars" are unstated. RSI "Wilder" is right for the JS copy that drives the verdict; the backend copy is pandas `ewm` and is **not consumed by any screen**. | `technicalIndicators.js:18-110`, `backend.py:315` |

### 0.2 Which copy matters (consumer map)

| Indicator | Copy that is **live** (changes what the user sees or trades) | Other copies |
|---|---|---|
| RSI 14 | **JS `calculateRSI`** → `categoricalAssessment.js:766` (Strong/Decent). Paper-trading RSI/ADX come from **TradingView** (`scan_queries.py:372,377`). | backend `calculate_rsi` + `calculate_rsi_4h` (**no consumer**; the 4H one spends an intraday call per `/api/sr`); backtest copies (`gate5_combined`, `nirmal_validation`, `parameter_stability`, `backtest_holistic`) |
| ATR 14 | **`simple_sr.wilder_atr`** (Analyze stop, Technical Read). **`trade_simulator.calculate_atr_at`** on a **51-bar window** (pandas `ewm`) sets **paper-trading stops** (`daily_job.py:84`, `live_signals.py:190,317`). | JS `calculateATR` (**no consumer**), `pattern_detection.calculate_atr` (**no callers**), legacy `support_resistance._calculate_atr` (only `?engine=legacy`), Leveraged ETF Board JS, SRPS ATR(20) `backend.py:2976-2995` |
| ADX 14 | `backend.calculate_adx` (Technical Read) and `mean_reversion.calculate_adx` (MR gate). **They differ**: backend filters −DM against the raw moves and adds `1e-10` to the DX denominator; MR and the backtests filter −DM against the already-zeroed +DM, so a tie bar (up = down > 0) counts. | `gate5_combined`, `nirmal_validation`, `backtest_holistic`, `backtest_adx_rsi_thresholds` |
| Avg volume / RVOL | `backend.py:1850` (RVOL), `scoringEngine.js:117`, `breakout_detection.py:49,122-127` (a second RVOL: 50 prior bars, breakout bar excluded), SRPS/MR 20-day | Pine `volAvg` |
| RS | JS `rsCalculator.js`; Python `backtest_holistic.calculate_rs_52w` (`shift(252)`, one bar off) used **live by paper trading** (`live_signals.py:272`) | `compute_rs_ratio_and_quadrant` `backend.py:2583` and an inline copy `:2716` (docstring says "exactly one"); `_srps_true_rs` `:2944` |
| SMA / EMA | JS; `pattern_detection.py:254-257` (Trend Template), `index_trend.py:39-40`, `market_phase_engine.py:154` | board JS |

### 0.3 Measured by the reviewer (read-only, 24 cached frames; I will reproduce these in Phase A)
- ATR: JS simple mean vs live Wilder, median 10% apart, max 17% (BRK-B). `trade_simulator` 51-bar `ewm` (paper stops) vs live: median 0.63%, max 2.9% (QPUX). `ewm` on the full history: 0.0000% on 22 tickers.
- RSI: JS vs backend at the last bar, max |Δ| 0.03; 0.16% of endpoints change a Strong/Decent band; short windows (20-30 bars) differ by 1.5-3.8 points. A flat history: JS says 100, Python 50.
- ADX: backend vs MR, 8 tie bars across 48 frames, worst gap 1.2 points (AMD.TO).

## 1. Goals and non-goals
**Goals:** (1) a **true, short** table; (2) tests that pin each documented formula and fail on drift; (3) an inventory test that fails when a new copy of an indicator appears that is not in the catalog (this is what enforces Golden Rule 59); (4) a before/after snapshot proving no live number changed; (5) a divergence register with a decision for each item; (6) Known Issues logged for everything found.
**Non-goals:** changing any indicator value anywhere (live, paper, backtest); deleting dead copies (separate cleanup: it adds review load to a docs-and-tests build, and the Leveraged ETF Board cites a dead function); consolidating copies; fixing the forming-bar volume average.

## 2. What the user reads: the table (after the cuts)
Scope: **numbers shown on the Analyze and Value tabs.** Three columns: **Indicator | From | How (one line)**. Eight rows:
SMA 50/200 · EMA 8/21 · RSI 14 ("sets the verdict's Strong/Decent") · ATR 14 ("sets the Trade Setup stop") · ADX 14 · Avg volume 50 / RVOL · RS 52W · PEG ("from a provider, not calculated").
No kind chip and no file column in the UI (both stay in the API/catalog as `kind`, `computed_in`). Notes carried in the one-liners: ATR uses completed bars only while RSI, SMA, EMA, ADX, OBV and RVOL include today's bar; RS "52 weeks" is shorter for funds under a year old.

## 3. Design

### 3.1 `backend/indicator_catalog.py` (new)
Entries: `{id, name, from_text, how, kind, computed_in:[...], consumers:[...], copies:{live:[], paper:[], frozen_research:[], external:[], dead:[]}}`. `kind` in `local_bars | local_bars_spy | provider | provider_plus_local`. `how` is written exactly as coded (seed, smoothing, window, forming bar).
`/api/provenance.indicators` is built from it; the hard-coded list in `backend.py` is deleted. Keys kept for compatibility: `name`, `source` (= `from_text`), `formula` (= `how`); added: `kind`, `computed_in`. **Failure state:** if the catalog cannot be built, provenance still returns 200 with `indicators: null` and `indicators_error: <reason>`; the tab shows the reason. Names are unique (the tab keys rows by name).

### 3.2 Tests (Golden Rules 19/21, 59)
- **`backend/backtest/test_indicators.py`:** independent textbook references written in the test (Wilder ATR, Wilder RSI, ADX, EMA, SMA, growth-factor RS) vs the production Python functions, on fixtures: 300-bar random walk; flat history; 60- and 100-bar histories; a gap; a **2-dp-rounded sub-$1 fund** (production JS runs on prices rounded to 2 dp with NaN volume→0 and NaN high/low→close, `backend.py:1105-1110`). Pins: ADX tie-bar difference between the backend and MR copies (its own fixture); the 51-bar `trade_simulator` ATR gap; JS flat-RSI = 100 vs Python 50; pandas RSI's bar-0 NaN→0-gain effect.
- **JS ↔ Python parity via the existing subprocess pattern** (`test_verdict_parity.py:110`): Python builds the inputs, runs a small `frontend/scripts/indicator_grid.mjs`, compares. Regenerated every run; **no committed fixture**.
- **Catalog honesty:** (1) every `computed_in` entry resolves (Python `module:function` by `getattr`, JS `file:export` by checking the export exists) or the test fails; (2) **inventory test**: grep `backend/`, `frontend/src`, `pine/` for indicator signatures (`ewm(alpha=1/`, a true-range `concat`, `rolling(14)`, `function rsi(`, `ta.atr`, ...) and fail on any file that is neither in the catalog `copies` nor in an explicit frozen-research allowlist; (3) names unique; (4) provenance survives a catalog failure.

### 3.3 Proof that nothing live changed
The 86,400-case verdict parity **cannot** detect an indicator change (indicators are inputs to its grid). So, **before any code change**, record a golden snapshot for the 24 cached tickers: `/api/sr` `meta.atr, meta.adx, meta.obv, meta.rvol`; JS `getIndicators` output (via node on the cached frames rounded as the backend does); RS fields; `trade_simulator.calculate_atr_at`. After the build, assert **bit-identical**.

### 3.4 Divergence report (small)
`backend/backtest/indicator_divergence.py` on the cached audit frames, no network: ATR and RSI value per implementation at the last bar and the % spread. Output a 3-line summary for the ledger plus a short REPORT; the user reads the 3 lines.

## 4. Divergence register (decision attached to each)
| # | Item | Decision |
|---|---|---|
| D1 | `trade_simulator` ATR (51-bar `ewm`) sets **paper stops**; Analyze stop uses Wilder on 2 years (median 0.63%, max 2.9% apart) | Unchanged. Golden Rule 60: paper results are priced on the simulator's ATR; log it; catalog lists paper trading as a consumer. |
| D2 | JS RSI (verdict) vs backend pandas RSI (unused) vs TradingView RSI (paper) | Unchanged. Log: one verdict rule gets RSI from three sources. Backend daily and 4H RSI unconsumed: log, and the 4H call wastes an intraday fetch per `/api/sr`. |
| D3 | ADX copies differ on tie bars (worst gap 1.2 points) | Pin with a test; consolidation = separate plan. |
| D4 | Avg volume 50 includes the forming bar (ATR is the only indicator that excludes it) | Say so in the table; fix = separate Known Issue. |
| D5 | RS: growth-factor ratio; 251-bar lookback; short-history fallback; JS vs Python off by one bar (paper vs Analyze) | Fix the text; log the off-by-one. |
| D6 | PEG from the provider chain; `/api/value` hard-codes `'source': 'finnhub'` (`backend.py:4057`) even when another provider supplied it | Fix the table text only; log the false label. |
| D7 | `Avg Volume 20`, `RS Price Ratio` | Dropped because they are not on the Analyze or Value tabs, not because nothing implements them. |
| D8 | `categoricalAssessment.js:92,766` `\|\| 50` also replaces a real RSI of 0 | Log next to the Day 123 known issue. |
| D9 | Dead code: `pattern_detection.calculate_atr`, JS `calculateATR`, `analyzeTrendStructure`, `calculateTradeSetup` | Log one cleanup item; do not delete here. |

## 5. Build phases (each verifiable alone)
- **A.** Golden snapshot (before); reproduce the reviewer's measurements; `indicator_catalog.py`.
- **B.** `test_indicators.py`, `indicator_grid.mjs`, inventory test; mutation-test them.
- **C.** Provenance builds from the catalog (with the failure state); the tab table shows the 3 columns; hard-coded list deleted.
- **D.** All suites; **golden after = bit-identical**; verdict parity 86,400; page checker (A11 extended: the table has 8 rows, none without a "From"); live look.
- **E.** Docs: API contracts, README, onboarding, Known Issues list for the close, ledger (3-line divergence summary).

## 6. Out of scope
Changing any value anywhere; deleting dead copies; consolidating copies; forming-bar volume fix; fundamentals; the intraday RSI feed.

## 7. Questions I want answered by the build, not assumed
Which copies have live consumers (Phase A confirms by caller grep); that the reviewer's measured numbers reproduce.

## 10. Review log (Opus, Day 126): 7 MUST adopted
1 `trade_simulator` ATR is live in paper trading on a 51-bar window (§0.2, D1). 2 JS RSI drives the verdict; backend RSIs unconsumed; paper uses TradingView (§0.2, D2). 3 ADX copies differ on tie bars (§0.2, D3, §3.2). 4 verdict parity cannot see indicator changes → before/after golden snapshot (§3.3). 5 inventory missed many copies → §0.2 rewritten, inventory test (§3.2). 6 D7 premise wrong → scope the table to Analyze and Value tabs (§2, D7). 7 PEG chain and the false `finnhub` label (§0.1, D6). SHOULD adopted: live ATR is `simple_sr` with the forming bar dropped (§0.1); do not delete dead code here (D9); RS facts (D5); subprocess parity with no committed fixture and extra fixtures (§3.2); inventory test and resolvable `computed_in` instead of string matching (§3.2); catalog failure state and unique names (§3.1). Decision-fatigue cuts: 8 rows, 3 columns, no chip or file column in the UI, 3-line divergence summary (§2, §3.4).
