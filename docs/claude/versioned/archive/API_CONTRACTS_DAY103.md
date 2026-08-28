# API Contracts — Day 103 (August 7, 2026)

> Adds one new endpoint. Every endpoint documented in prior `API_CONTRACTS_DAY*.md`
> files is unchanged.

---

## New — `GET /api/sectors/pullback-screen`

### What it is
SRPS (Sector Rotation Pullback System) discretionary screener. **Not a forward-test
track and not the automated paper-trading engine.** SRPS's mechanical rule set was
fully backtested (survivorship-free, 400 tickers, 2020-2025) and failed its own
pre-registered bar (34.1% win rate vs. required >45%, Profit Factor 1.177 vs. required
>1.2), so it was never built as a live automated track. This endpoint repurposes the
same rule logic (Rules 1-4: regime gate, sector-quadrant gate, pullback-zone/trend/
RS/volume, stop-distance sanity) as a pure informational screen for manual judgment —
no ledger, no automated entry/exit, no forward-test count.

### Why
User requested a screen surfacing SRPS's mechanical candidates so they could apply
their own judgment (regime, news, catalysts) rather than have the system decide.

### Request

```
GET /api/sectors/pullback-screen
```

No query parameters. Fixed 1-year OHLCV lookback, fixed rule thresholds
(`backend/srps_constants.py`).

### Response shape

```json
{
  "regimeOk": true,
  "regimeMessage": "SPY above 200-SMA — Rule 1 regime gate open",
  "spyClose": 768.53,
  "spySma200": 702.46,
  "improvingSectorCount": 2,
  "sectorsCappedFrom": null,
  "sectors": [
    {
      "etf": "XLC",
      "sector": "Communication Services",
      "quadrant": "Improving",
      "error": null,
      "candidates": [
        {
          "ticker": "LYV",
          "rsRatio": 1.034,
          "price": 181.77,
          "stopPrice": 176.79,
          "targetPrice": 194.22,
          "riskPct": 2.74,
          "volumeVsAvg20d": 0.55,
          "daysUntilEarnings": null,
          "earningsWarning": null
        }
      ]
    }
  ],
  "disclaimer": "Informational screen only — SRPS's mechanical backtest (2020-2025, survivorship-free) failed its own pre-registered bar (34.1% win rate, PF 1.177, both below the required minimum). This is not a buy signal and not an automated forward-test track. Apply your own judgment (regime, news, catalysts) before acting on anything shown here.",
  "timestamp": "2026-08-07T08:45:48.810175"
}
```

### Field notes

- `regimeOk` / `regimeMessage` — Rule 1 (SPY vs. 200-SMA). When `false`, candidates
  are still shown (not hidden — matches this project's "visible state over hidden"
  convention), with the message flagging that the mechanical rule says stand aside.
- `sectors` — only sectors currently in the `Improving` RRG quadrant appear here (Rule
  2). Only the **6 strongest** Improving sectors by RS ratio are processed per
  request, even if more are Improving — `sectorsCappedFrom` is the true count when
  truncation happened (`null` otherwise). Added Day 103 after confirming via the
  actual 12-month quadrant history that 8-9 sectors being simultaneously Improving is
  real (~4x/year), not hypothetical — an uncapped loop would fan out to too many
  per-ticker provider calls in one request (same risk class as Golden Rule 25/40).
- `candidates` — up to 3 per sector (top RS-ranked names passing Rules 3-4). An empty
  array means the sector's top RS names aren't currently in a pullback zone, not an
  error.
- `earningsWarning` — Rule 6 (earnings exclusion), **applied here** unlike the
  historical backtest scripts (live earnings-calendar data exists per-ticker; a
  historical equivalent across ~400 tickers x multiple years does not, cheaply).
- Sourcing: `scan_queries.build_sector_query()` (TradingView, sector-filtered) +
  per-candidate OHLCV via the multi-provider orchestrator (`get_data_provider()`) —
  unlike the original `/api/sectors/rotation` endpoint, this one has full
  TwelveData→yfinance→Tradier fallback.
- Cached per trading day, same convention as `/api/sectors/rotation` and
  `/api/sectors/sub-industry` (SQLite `market_cache`, key `SRPS_PULLBACK_SCREEN`).

### Errors

- `503` — data provider unavailable.
- `500` — SPY fetch failed, or insufficient SPY history (<200 bars).
- A single candidate or sector failing (provider error, insufficient history) does
  not fail the whole request — that sector's `error` field is set and/or the
  candidate is silently dropped from ranking.
