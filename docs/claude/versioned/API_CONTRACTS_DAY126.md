# API Contracts — Day 126

> Changes since `API_CONTRACTS_DAY125.md`. One **breaking** change: `GET /api/sr/<ticker>` now
> defaults to the simple S&R engine. Backend v2.54 → v2.55. Nothing else changed shape.
> Plans: `docs/claude/design/SIMPLE_SR_PLAN_DAY125.md` (§2, §8, §10), `SIMPLE_SR_SWITCH_PLAN_DAY126.md`.

---

## Changed (breaking) — `GET /api/sr/<ticker>`

Engine chosen by `constants.SR_ENGINE` (now `'simple'`), or per request with
`?engine=simple|legacy` (anything else: 400). `?engine=legacy` returns the old response unchanged
(diffed before/after on 5 tickers). `backtest_holistic.py` and the discontinued paper job still call
`compute_sr_levels()` directly; they are not affected.

**Simple engine** (`backend/simple_sr.py`, common trader rules, not backtested): swing highs/lows
(5 bars each side, last 252 completed daily bars) grouped into zones (neighbours within 0.5 ATR, zone
no wider than 1 ATR); the nearest zone below/at price and the nearest above, inside the existing
20% below / 30% above window. No weekly levels, no projected/ATR/Fibonacci levels, no fallback methods.

| Field | Simple engine |
|---|---|
| `method` | `'simple'` |
| `support` | zone HIGH of every in-window zone below/at price, **nearest first** (was ascending on legacy) |
| `resistance` | zone LOW of every in-window zone above price, nearest first |
| `allSupport` / `allResistance` | every zone's edge on that side, no window |
| `suggestedEntry` | `max(support)` = the nearest support zone's high |
| `suggestedStop` | entry − 2×ATR (`sr_plan.trade_plan`, same formula as before; null without ATR) |
| `suggestedTarget` | `min(resistance)` = the nearest resistance zone's low; null when none |
| `riskReward` | `(target − entry) / (entry − stop)`; null if any is missing |
| `meta.engine` | `'simple'` (new, also `'legacy'` on the old engine) |
| `meta.atr` | Wilder ATR(14) on **completed** bars (legacy included a forming bar) |
| `meta.zones` | new: `[{low, high, mid, swings, highs, lows, side, insideZone, nearest, lastSwingDate}]`, in-window zones nearest first; exactly one `nearest: true` per side that has a zone. `swings` = times price turned there |
| `meta.high52w`, `meta.nearHigh52w` | new: highest high of the last 252 bars; true when there is no resistance and price is within 3% of it |
| `meta.confirmedThrough` | new: `{daily}`: last bar that could be confirmed as a swing (the last 5 bars cannot be) |
| `meta.droppedFormingBar` | new: today's unfinished bar was left out of the zones |
| **Not sent** | `meta.levelScores`, `meta.mtf`, `meta.resistanceProjected`, `meta.supportProjected`, `meta.pivotSelection`, `meta.tradeViability` (legacy only) |
| Unchanged | `currentPrice`, `volume`, `change`, `dataPoints`, `timestamp`, `meta.proximityFilter`, `meta.adx`, `meta.rsi_4h`, `meta.rsi_daily`, `meta.obv`, `meta.rvol`, `meta.candle`, `meta.prevBar`, `meta.marketStructure` |

Errors: fewer than 60 clean completed bars → 400 `{error, message}` (legacy kept its 150-bar rule);
the simple engine imports without scikit-learn, so only `?engine=legacy` can return 503.

## Frontend

- Trade Setup reads `sr.meta.zones` (`utils/keyLevels.js`), shades the two nearest zones on the price
  bar (`zoneSpan`), and has no projected-target branch. An `/api/sr` response without `meta.zones`
  is shown as "unexpected format" and logged, never guessed.
- Page checker A10 compares the Buy tile and both level rows to this payload.
- The Simple Checklist (the only grader of stop width and R:R) was removed:
  `REMOVE_SIMPLE_CHECKLIST_PLAN_DAY126.md`.

---

## Changed (additive, one removal) — Data Sources tab v2 (Backend v2.55)

Plan: `docs/claude/design/DATA_SOURCES_TAB_V2_PLAN_DAY126.md`.

- **`GET /api/stock/<t>`** adds `exchange` (Yahoo `fullExchangeName`: "Toronto", "Cboe CA", "NYSEArca"), `currency`,
  `instrumentClass` (`Stock` | `ETF` | `Leveraged ETF` | `CDR` | `Unknown`) and `classBasis` (why; an inference from quote type and name).
  `fetchStockData()` in `api.js` rebuilds an object literal, so each is listed there (Golden Rule 30).
- **`GET /api/provenance/<t>`** adds:
  - `quality`: `{state: 'ok'|'not_cached'|'error', level: PASS|WARN|FAIL, checks:{freshness,integrity,history,jumps:{level,note}}, facts:{bars, first_date, last_date, sessions_behind, forming_bar_dropped, flat_zero_volume_pct, zero_volume_last5, bad_rows, nan_closes, jumps:[{date,pct,in_last_260}]}, period, rows, source, cached_at, expired}`. Computed from the cached frame with **no provider call and no cache event** (`cache_manager.read_ohlcv_entry`).
  - `fundamentals.has_data` (false for an all-null stub), `ohlcv.this_session` (`'cache'` | `'stale_cache'` | provider | null), `audit` (worst line from `backend/reference/data_audit_latest.json`, or null).
  - `indicators` (Day 126, rebuilt): 8 rows from `backend/indicator_catalog.py`, each `{name, source, formula, kind, computed_in}` (`source` = the plain "From" text, `formula` = the "How" line; `kind` = `local_bars | local_bars_spy | provider | provider_plus_local`; `computed_in` is not shown on the tab). New sibling `indicators_error`: null normally; if the catalog fails to build, `indicators` is null and the reason is here (the endpoint still answers 200).
  - **Removed:** the hard-coded `data_sources` block (nothing read it; it was wrong).
  - **Frozen:** `ohlcv.source`, `ohlcv.rows`, `ohlcv.status` (the audit script reads them). `status: 'live'` still means "not cached or expired".
  - `fetchDataProvenance()` now returns `{error}` instead of `null` on failure.
- **`GET /api/health` → `providers`** adds `chains` (data type → ordered provider names, from the orchestrator) and `disabled` (e.g. `["stooq"]`). `active_sources` is kept but is the last call for any ticker and is no longer read by the tab.
- **`GET /api/data-sources/coverage`** (new): `backend/reference/provider_coverage.json`, which provider serves which market as tested, dated, with known issues. 500 `{error}` if the file is unreadable.
- **New shared module** `backend/data_quality.py` (checks, levels, `classify_instrument`) used by the endpoint and both audit scripts.
- **Split mechanism (Day 126).** `backend/reference/known_splits.json` (hand-kept, each row has an issuer `source_url`; `ratio` = new shares per old share) + `backend/split_adjust.py` (one classifier, one adjuster). `DataProvider._deliver()` applies it at all four exits of `get_ohlcv` / `get_intraday_ohlcv` and returns a COPY; the SQLite cache and `/api/provenance` stay RAW. Emergency direct-Yahoo fallbacks call `split_adjust.fix_frame`. Adjusts only when the step is really in the data; a provider-adjusted split is a no-op; wrong-way / ambiguous / missing-close / unsorted cases are reported and NOT adjusted.
  - `/api/stock`: `fiftyTwoWeekHigh/Low` come from the adjusted frame when the table has a split inside the window (otherwise still Yahoo's).
  - `/api/provenance` `quality.facts` adds `splits:[{text,status,bar_date,note,source_url}]` (status `unadjusted` = STA adjusts it | `already_adjusted` | `wrong_way` | `ambiguous` | `pending` | `not_applicable`), `split_table_errors`, and each `jumps[]` item adds `split_k` (3..50, negative = reverse) and `covered`. `quality.checks.jumps` is now FAIL for an uncovered exact-factor jump in the last 260 bars (was always WARN).
  - Tab: one line "Split-adjusted by STA: 3-for-1 on 2026-05-25..." only when STA changed the prices (`view.splits`, test id `ds-split-note`).

