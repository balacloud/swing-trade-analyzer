# Data Sources tab v2: Plan (Day 126, revised after the Opus review)

**Status:** PLAN v2. Step 1 (plan) and step 2 (independent Opus review) done; step 3 (build) and step 4 (three review passes) follow.
**Why (user, Day 126):** "how good is our Data Sources tab? ... are we getting accurate info for individual stocks, ETFs, leveraged, Canadian stocks, ETFs, leveraged?"
**Inputs:** `DATA_SOURCE_TESTING_PLAN_DAY126.md` §1, §7–9; `INSTRUMENT_MASTER_DAY126.md`; `docs/test/DataSources_20261114/REPORT.md` and `REPORT_vs_IBKR.md`.
**Review:** Opus, verdict GO with 11 must-fixes and 8 wrong premises. Every claim I spot-checked held (cache reader hides 38 of 50 cached entries; cache hits label the source `'cache'`; `backend/data/` is gitignored; `/api/stock` builds an explicit dict; the tab render crashes on an `{error}` object). All adopted below; log in §11.

## 0. What is wrong today (verified)

| # | Problem | Evidence |
|---|---|---|
| 1 | The tab cannot tell good data from bad. SOXL.NE shows `JUST FETCHED, yfinance, 311 points`; its history is 311/311 flat zero-volume bars with an unadjusted 3:1 split. | Live tab; audit `REPORT.md` |
| 2 | No identity (exchange, currency, fund type). US SOXL ($55.97 USD) and SOXL.NE ($14.10 CAD) look alike. | `/api/stock` has `quoteType` only |
| 3 | "Fundamentals: CACHED, yfinance" for SOXL.NE is an **all-null stub** that `/api/fundamentals` treats as empty. | `cache.db fundamentals_cache`; `backend.py:1122` `_is_fundamentals_empty` |
| 4 | The Data Source Map is hard-coded in `App.jsx`: lists dead **Stooq**, omits **Tradier** (about 3,600 fetches). The backend `provenance.data_sources` block is hard-coded too; nothing reads it. | `orchestrator.py:88-97` |
| 5 | "live from twelvedata" is the last call for ANY ticker (global). | `orchestrator.py:539-543` |
| 6 | `fetchDataProvenance()` returns `null` on error, so a failure is a blank. | `api.js:681-695` |
| 7 | No view of which source serves which market, and no per-source known issues (Tradier reverse split ×3). | Audit reports |

Kept as is: cache numbers, per-provider health, `daily_remaining`, circuit-breaker state.

## 1. Design rules
1. **Every element is backed by a real field; unknown says "unknown".**
2. **No silent failure:** each block has loading / error (reason + Retry) / empty / data states; any exception is logged with the ticker and returned as `{state:'error', reason}`.
3. **No provider calls when the tab opens** (free quotas). Quality comes from the cached frame through a **side-effect-free reader**; identity comes from `/api/stock` (already called by Analyze).
4. **One rule, one place (Golden Rule 59).** Checks live in `backend/data_quality.py`; the audit scripts import them (§8 lists every copy and its fate).
5. **Facts vs levels.** `check_history()` returns facts (counts, dates, flags). Each caller maps facts to PASS/WARN/FAIL: the audit keeps its C2 rule, the tab shows a 1-session lag as a note (no holiday calendar exists).
6. **Inferred is labelled inferred**; the tab decides nothing and gates no route (routing is a separate step).
7. **Less to read (user's decision-fatigue rule):** passes collapse, details sit behind disclosures.

## 2. What the tab shows (final layout, after the cuts)

| Block | Content | Source |
|---|---|---|
| **A. Identity strip** | symbol · exchange (Yahoo's own name: Toronto, Cboe CA, NYSEArca) · currency · class (Stock / ETF / Leveraged ETF / CDR, with "inferred from quote type and name") · **data from** `<source>` (the provider that produced the cached bars) · `cached` / `expired, refetch on next analysis` / `not cached` | `/api/stock` (new `exchange`, `currency`, `instrumentClass`), `provenance.ohlcv` |
| **B. Data quality** | Verdict pill. Header: "Checked N bars (period P) · cached T · last bar D (N sessions behind)". **Only WARN/FAIL rows are shown**, each with value and one plain sentence; passes collapse into "N checks passed". Rows: flat zero-volume %, zero volume in last 5 days, one-day moves over 40% (date, %, "split? check"; marked if inside the last 260 bars that Analyze uses), malformed bars, short history, stale last bar. One extra line only when the ticker was audited and did not pass ("Audit Nov 14: Tradier ❌ reverse-split error"). Fundamentals line: "No fundamentals for a fund" or source and age. | `provenance.quality` (`data_quality.check_history`), `provenance.fundamentals`, `backend/reference/data_audit_latest.json` |
| **C. Source chain and health** | Price and fundamentals chains by default (toggle for intraday, quote, info, earnings): the real ordered chain, per provider health, calls left, disabled flag, **markets it covers with "tested <date>"** and its known issue. TradingView (market scanning) as one line from `/api/health.tradingview_available`. Stooq only as "disabled". | `/api/health.providers` (new `chains`, `disabled`) + `backend/reference/provider_coverage.json` |
| **D. Details** (collapsed) | Cache panel; "How indicators are calculated" table | `/api/cache/status`; table as today |

Cut from v1 of this plan: the separate "Last audit" block, the separate "Coverage matrix" (merged into C), duplicate status lines between A and D.

## 3. Backend changes

1. **`backend/data_quality.py` (new, pure).**
   - `check_history(df, now=None)` first calls `drop_forming_bar`, then returns facts: `bars, first_date, last_date, sessions_behind, forming_bar_dropped, flat_zero_volume_pct, zero_volume_last5, bad_rows (0.1% tolerance), jumps:[{date,pct,in_last_260}]`. Never raises; on error returns `{state:'error', reason}` and logs.
   - `quality_level(facts)` (the tab's mapping) and the audit keeps its own mapping from the same facts.
   - `classify_instrument(quote_type, name)`: CDR if the name has `CDR`; Leveraged if ETF and name matches `2X|3X|DAILY|DLY|BETAPRO|BULL|BEAR|ULTRA`; ETF; Stock (EQUITY); else Unknown, each with a `basis` string. Verified on real Yahoo names (all 5 CDRs say "CDR"; 8 of 8 leveraged funds say 2X/3X or Daily).
   - Shared thresholds and `worst`, `ORDER`, `ICON`.
2. **`cache_manager.read_ohlcv_entry(ticker)`:** returns `(df, {period, rows, source, cached_at, expires_at, expired})`. No expiry gate, no row gate, no `cache_stats` logging, no deletion. `orchestrator._get_stale_ohlcv` (`orchestrator.py:396-418`, a second copy of the deserializer) is repointed to it. Same for **`read_fundamentals_entry`** (no schema-mismatch delete, no events).
3. **`/api/stock`:** add `exchange` (Yahoo `fullExchangeName`), `currency`, `instrumentClass` + `classBasis`. Four places: `YFINANCE_STOCK_INFO` (`field_maps.py:169`), the response dict (`backend.py:1094-1111`), `fetchStockData()` in `api.js:35-53` (Golden Rule 30), and the API contracts doc.
4. **`/api/provenance/<t>`:** add `quality` (from `read_ohlcv_entry`), `fundamentals.has_data`, `fundamentals.applicable`, `audit` (one-line from the reference file or null). **Freeze `provenance.ohlcv.{source,rows,status}`** (the audit's tab check reads them). Remove the hard-coded `data_sources` block (no reader). Do **not** add `identity` (stock info is an uncached `.info` call).
5. **`/api/health.providers`:** add `chains` (data type → ordered names, from the orchestrator's real lists) and `disabled`. `active_sources` stays but is no longer read by the tab (documented).
6. **`backend/reference/` (tracked; `backend/data/` is gitignored):** `provider_coverage.json` (curated from the audit: per provider and market, tested date, report path, known issue) and `data_audit_latest.json` (`{generated, report, tickers:{SYM:{truth_free:{...}, vs_ibkr:{...}}}}`). Merge rule: each audit script updates only its own key per ticker. Regeneration is manual, by whoever runs the audit; the tab shows the date and "N days old" over 30.
7. Labels: `_cache_status` value `live` now renders as "not cached / expired, will refetch on next analysis"; the key is unchanged.

## 4. Frontend changes (one commit, so the null→{error} change cannot crash)
1. New `components/DataSourcesTab.jsx` + pure `utils/dataSourcesView.js` (`describeQuality`, `describeChain`, `describeFundamentals`, labels) with node tests. Extracted from `App.jsx`.
2. `fetchDataProvenance` returns `{error}`; **both call sites** (`App.jsx:257-259`, `919-923`) and the render change together.
3. `api.js` `fetchStockData` passes `exchange`, `currency`, `instrumentClass`, `classBasis`.
4. Delete the hard-coded map, its footer, and the duplicated indicator fallback at `App.jsx:2702-2713` (formulas come from `provenance.indicators` only; if absent, show "unavailable", not a second copy).

## 5. Data-backing table

| Element | Source | Exists today? |
|---|---|---|
| exchange, currency | Yahoo `fullExchangeName`, `currency` via `/api/stock` | needs the four edits (§3.3) |
| class + basis | `classify_instrument(quoteType, name)` | new, pure |
| data from / bars / period / cached / expired | `read_ohlcv_entry` (the cache row's `source`) | row exists; reader new |
| served this session | `last_sources[T_ohlcv]` is `'cache'` on a hit and `'stale_cache'` on fallback, so used only as "this session: live / from cache" | yes |
| quality facts | `check_history(frame)` | new |
| audit line | `data_audit_latest.json` | to write |
| chain, disabled | orchestrator lists | to expose |
| calls left, health | `get_provider_status()` | yes |
| markets covered, known issue | `provider_coverage.json` | to write |
| fundamentals applicable / has_data | `quoteType` + `_is_fundamentals_empty` via `read_fundamentals_entry` | yes + new reader |

## 6. Silent-failure table

| Situation | Shown |
|---|---|
| `/api/provenance` fails | "Couldn't load provenance (reason)" + Retry; chain, health and cache still render |
| Ticker not cached | A: "not cached"; B: "Analyze this ticker first" |
| Cached frame has 311 bars (under 504) | **checked normally** (the old reader would have hidden it), with the bar count shown |
| Cached frame period is 1y or a VIX 3mo overwrite | B header says "period P"; no claim about 2 years |
| Cached frame is expired | still checked, labelled "expired" |
| Frame under 60 bars / empty | quality FAIL with the reason |
| `quoteType` missing | class "Unknown (no quote type)" |
| Audit file missing or ticker absent | audit line omitted |
| Audit older than 30 days | "audit N days old" |
| `last_sources` empty after restart | "this session: unknown" (the cache row still names the source) |
| Health feed fails | chain from `chains` if present, else "health unavailable" |
| `check_history` raises | logged with ticker; `quality:{state:'error', reason}`; UI shows it |

## 7. Tests and verification
1. `backend/backtest/test_data_quality.py`: clean stock; all-flat close-only history (SOXL.NE shape, FAIL); 3× split step; short history (100 bars); stale last bar; one-cent rounding (no warn); NaN rows; empty frame; **forming intraday bar** (dropped, fact set); **1y-period frame**; **311-row frame (must not be "not loaded")**; **expired frame**; **`stale_cache` row**; class rules incl. real Yahoo names (CDR variants, 8 leveraged, ETF, stock, missing quote type).
2. `read_ohlcv_entry` test: returns a 311-row frame, writes **no** `cache_stats` event, deletes nothing.
3. **Audit regression:** add `--date`, `--now` and `--offline` to `audit_data_sources.py` (offline replays the saved tab claims from `data_audit_20261114.json`, no network). Checksum the baseline cache first; the `checks` JSON must be identical to the saved file.
4. `frontend/scripts/test_data_sources_view.mjs`, including the `{error}` → Retry state.
5. **Page checker A11:** open the Data Sources tab for the 5 standard tickers + SOXL.NE + QPUX. Assert: identity strip present; class/exchange/currency right (SOXL.NE = Leveraged ETF · Cboe CA · CAD); SOXL.NE shows FAIL with the flat-bars reason; AAPL shows no WARN/FAIL; no "Stooq" in the chain; Tradier listed.
6. `npm run build`, all node tests, verdict parity 86,400, live look at US/Canada × stock/ETF/leveraged + a CDR.
7. Three escalating review passes after the build (Golden Rule 41).

## 8. Every copy of the rules (Golden Rule 59): canonical vs fate

| Copy | Fate |
|---|---|
| `audit_data_sources.py` `source_checks` / thresholds | replaced by `data_quality.py` imports |
| `audit_vs_ibkr.py` `CLOSE_WARN/FAIL, ORDER, worst, ICON` | import from `data_quality.py` (its `CLASS` lookup table stays: it is data) |
| `identify_instruments.py` `LEVERAGE_RE`, `classify` | name regex imported from `data_quality.py`; the price-ratio CDR test stays there (offline tool, has the IBKR description and US twin) |
| Frontend ETF rules: `detectEtf` (`fundamentalsRead.js:36`), `describeClassification` (`App.jsx:72`), `scoringEngine.isETF`, `categoricalAssessment ETF_TICKERS` | **left alone**, logged as Known Issue (copies); the tab uses the backend class. A node check asserts they agree on ETF vs not for the 80-instrument master. |
| Indicator formulas: `backend.py:957-969` and `App.jsx:2702-2713` | the App.jsx copy deleted. Four ATR implementations exist (`pattern_detection.py:47`, `simple_sr.py:52`, `support_resistance.py:113`, `technicalIndicators.js:51`): logged as Known Issue, formula text not changed in this build |
| `/api/data/freshness` (`backend.py:787-830`, labels by cache age) | not touched; the new row is labelled "Last bar: N sessions behind", never "freshness" (Golden Rule 63) |

## 9. Build phases (each verifiable alone)
- **A.** `data_quality.py` + tests + `read_*_entry` readers + audit refactor + regression.
- **B.** Backend endpoints, field-map edits, reference files.
- **C.** Frontend component, helpers, tests, `api.js`, App.jsx call sites (one commit).
- **D.** Page checker A11, live checks across classes.
- **E.** Docs (API contracts, README, onboarding, ledger, Known Issues).

## 10. Out of scope
Routing changes (SOXL.NE bars, Tradier 40% guard): step 3 of the data plan. New providers. Fundamentals accuracy. A holiday calendar. Making the tab call providers on open. Changing the other frontend ETF rules.

## 11. Review log (Opus, Day 126): all 11 MUST adopted
1 cache reader gates → side-effect-free `read_ohlcv_entry` (§3.2). 2 frame may differ from what the analysis used → period/rows/cached shown, last-260 tag (§2B). 3 source used → cache row's source (§2A, §5). 4 forming bar → dropped in `check_history` (§3.1). 5 gitignored folder → `backend/reference/` + merge rule (§3.6). 6 identity cost → dropped from provenance (§3.4). 7 field-map edit incomplete → four places (§3.3). 8 fundamentals read side effects → `read_fundamentals_entry` (§3.2). 9 `{error}` crash → one commit, both call sites (§4.2). 10 regression not reproducible → `--date/--now/--offline` (§7.3). 11 unlisted copies → table (§8). SHOULD/NICE: class from name only (§3.1), 1-session lag as a note (§1.5), logging on error (§1.2), TradingView line (§2C), `live` label (§3.7), extra fixtures (§7.1). Decision-fatigue cuts adopted (§2).
