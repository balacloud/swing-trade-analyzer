# API Contracts — Day 123

> Changes since `API_CONTRACTS_DAY118.md`. One breaking change (`/api/mr/signal` drops
> `stop` / `target` / `atr`, which were never the tested rule); everything else is additive or
> a corrected value. Only consumer of the removed fields was `MRSignalCard.jsx`, now deleted.

---

## Changed — `GET /api/mr/signal/<ticker>` (Step 5)

**Removed:** `stop`, `target`, `atr` (an ATR stop and an entry + 2 ATR target, with a silent 2%
ATR fallback). The tested system has a 5% stop from the fill and no target.

**Added:**

| Field | Type | Meaning |
|---|---|---|
| `conditions.<rule>` | `true \| false \| null` | Rules: `rsi2_oversold`, `above_200sma`, `price_filter`, `volume_filter`. `null` = input missing (not a fail). |
| `missing` | `string[]` | Inputs that could not be computed |
| `pct_above_sma200` | `number \| null` | Close vs 200-day SMA, percent |
| `rules` | object | `mean_reversion.MR_RULES`: `rsi2_entry` 10, `price_min` 10, `dollar_volume_min` 25e6, `stop_pct` 0.05, `rsi2_exit` 70, `max_hold_days` 10, `cooldown_days` 5 |
| `asOf` | `YYYY-MM-DD` | Date of the last completed bar used |
| `barDropped` | bool | A forming (intraday) bar was dropped before the check (`market_time.drop_forming_bar`, cutoff 16:30 ET) |
| `dataSource` | string | OHLCV provider |
| `trackRecord` | object \| null | `{variants: [{variant, label, trades, wins, winPct, profitFactor, avgPnlPct, firstEntry, lastExit}], basis, source, backtest}`, read from the latest `validation_results/mr_open_entry_retest_*.json` (next-open basis). `null` (logged) if unreadable. |

Values made nullable instead of crashing: `current_price`, `avg_volume`, `avg_dollar_volume`.

**Insufficient history:** `{error, reason: "only N days of history; the rules need 200", bars, signal: false}` (HTTP 200).

Frontend `fetchMRSignal` now returns `{error, reason, signal: false}` on any failure, never `null`.

## Changed — `GET /api/mr/scan`
Each row gains `asOf`. The forming bar is dropped on both data paths before scanning.

## Changed — `GET /api/earnings/<ticker>` (Step 6)
- `days_until` is now New York calendar days (`calendar_days_until`). It was
  `(earnings_date - datetime.now()).days`: off by one, and −1 on the report day itself.
  Timestamps are converted to `America/New_York` before taking the date.
- **New failure contract:** when every source raised, it returns `has_upcoming: null`,
  `earnings_date: null`, `days_until: null` and `recommendation: "Could not fetch earnings data"`.
  `has_upcoming: false` with `earnings_date: null` still means "no date found".

## Changed — `GET /api/stock/<ticker>`
Additive: `quoteType` (yfinance `info.quoteType`, e.g. `"EQUITY"`, `"ETF"`; may be null).
Frontend `fetchStockData` exposes it as `quoteType`.

## Changed — `GET /api/fundamentals/<ticker>` (values, not shape)
- yfinance `debtToEquity` is converted from percent to a ratio (÷100), matching Finnhub and FMP.
- yfinance and FMP `roe` / `roa` / `roic` are always ×100. The old rule (×100 only when
  `abs(v) < 1`) displayed 150% as 1.5%.
- Cache: `FUNDAMENTALS_SCHEMA_VERSION` 2 → 3, so values cached in the old units are discarded.
- Frontend `fetchFundamentals` now passes through the orchestrator's `_field_sources` as
  `fieldSources`. It already existed in the response.

## Changed — `GET /api/sr/<ticker>`
- `meta.candle.date` (additive): date of the bar the candle read describes.
- `meta.prevBar.date` is always `df.index[-2]` (the bar before the last row).
- `meta.rvol` / `rvolDisplay` are `null` when the 50-day average volume is 0. They were a fake `1.0`.
- `suggestedStop` is `null` (logged) when ATR is unavailable. It was a computed number from a missing input.

## Changed — `GET /api/patterns/<ticker>`
Additive: `trend_template.sma_values.sma_200_30d_ago` (nullable), used for the Technical Read's
"200-day average rising" line.
