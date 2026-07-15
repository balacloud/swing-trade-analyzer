# TradingView Screener Implementation — Reference Doc

> **Purpose:** Explain how Swing Trade Analyzer (STA) uses the `tradingview-screener`
> Python library, where every piece of code lives, and what we learned building/
> auditing it — written so this pattern can be reused/taught in another project.
> **Source project:** `swing-trade-analyzer` (this repo)
> **Written:** Day 84 (July 15, 2026), on request, to hand this pattern to another project.

---

## 1. What it is

STA uses a free, open-source Python package —
[`tradingview-screener`](https://github.com/shner-elmo/TradingView-Screener)
(PyPI: `tradingview-screener`, we're on v3.0.0) — to query TradingView's own
screener backend directly (the same data source that powers tradingview.com's
web-based stock screener), without scraping HTML. It returns a pandas
DataFrame of tickers matching a set of filters (fundamentals, technicals,
exchange, index membership, etc.).

STA uses it for exactly one thing: **finding candidate tickers that match a
strategy's filter criteria**, market-wide, before running STA's own deeper
per-ticker analysis (Trend Template, S/R, patterns, categorical assessment) on
the survivors. It is a **pre-filter / funnel**, not the source of truth for
any trade decision — the screener narrows ~7,000+ US tickers down to a
double-digit candidate list; STA's own engines then decide what's actionable.

---

## 2. Where the code lives (file map)

```
backend/
├── scan_queries.py                    ← Shared query-builder module (READ THIS FIRST)
├── backend.py                         ← Flask route: GET /api/scan/tradingview
│                                          (imports `tradingview_screener` directly at
│                                          the top, ~line 87; route at line 1780)
└── paper_trading/
    └── live_signals.py                ← Calls scan_queries.build_best_query() directly
                                           (no HTTP hop — same process, same query)

frontend/
├── src/services/api.js                ← fetchScanResults(), fetchScanStrategies()
│                                          (~line 250-315)
└── src/App.jsx                        ← Scan tab UI: strategy dropdown, runScan(),
                                           results table (~line 110-115 state,
                                           ~line 512 runScan(), ~line 2570+ UI)
```

### 2.1 `backend/scan_queries.py` — the shared query builder (the core of this pattern)

This is the single most important file. It exports:

- `build_best_query(limit=50, market_index='all') -> (Query, is_canadian)` —
  builds an **unexecuted** `tradingview_screener.Query` object encoding STA's
  best-validated strategy ("Config C" — see §4). Returns the query, not the
  results; caller must call `query.get_scanner_data()`.
- `parse_candidates(results, is_canadian, strategy='best') -> list[dict]` —
  takes the raw pandas DataFrame `get_scanner_data()` returns and turns it
  into clean dicts: strips exchange prefixes, drops non-common-stock tickers
  (warrants, SPAC units, preferred shares, commodity-trust ETFs), appends
  `.TO` for Canadian tickers, computes `pctFromHigh`.

**Why this file exists as its own module (the actual lesson worth teaching):**
Originally, the query-building logic was written once, inline, inside the
Flask route (`backend.py`'s `scan_tradingview()`). Then a second system (the
automated paper-trading engine, `live_signals.py`) needed the *exact same*
candidate logic — not a "should behave the same" reimplementation, but
literally the same filters, in the same order, producing the same candidate
set on the same day. Two independent implementations of "what counts as a
candidate" is exactly the kind of thing that drifts silently (this project's
own Golden Rule 19: a JS/Python verdict-parity bug shipped for years before
a systematic test caught it). So the query construction was extracted into
`scan_queries.py` and **both** the live UI route and the paper-trading engine
import and call the same functions. One implementation, not two that can
diverge.

**A real bug this pattern still allowed (fixed Day 83, worth knowing about):**
Even with the shared builder, the Flask route had its own post-processing:

```python
# backend.py, scan_tradingview()
if strategy != 'best':                                    # ← guard added Day 83
    query = query.order_by('relative_volume_10d_calc', ascending=False)
    query = query.limit(limit)
```

Before the guard existed, this ran **unconditionally**, even for `'best'`
queries that had already set their own `order_by('ADX', ascending=False)`
inside `build_best_query()`. The `tradingview_screener` library's
`.order_by()` **replaces** rather than stacks with a prior sort. Since
TradingView truncates server-side at `.limit(n)`, and the "all stocks"
universe routinely has more than `n` qualifying candidates, the live Scan tab
and the paper-trading engine could end up looking at **two different top-N
sets** on the same day, from what was supposed to be "one implementation."
**Lesson:** factoring shared query logic into one module stops the filters
from drifting, but any code *downstream* of the shared builder (sorting,
truncation, post-processing) has to be equally disciplined — sharing the
builder alone isn't sufficient if each caller still bolts on its own
post-processing.

### 2.2 `backend/backend.py` — the HTTP route

`GET /api/scan/tradingview?strategy=<s>&limit=<n>&market_index=<idx>`
(route defined ~line 1780, full logic through ~line 1922)

- `strategy`: `reddit` | `minervini` | `momentum` | `value` | `best` — each is
  a different filter preset. Only `'best'` (Config C, the backtested one) is
  built from the shared `scan_queries.build_best_query()`; the other four are
  simpler filter sets defined inline in this route (not shared with anything
  else, since nothing else consumes them).
- `market_index`: `all` | `sp500` | `nasdaq100` | `dow30` | `tsx60` | `canada`
  — maps to `Query().set_index(...)` (specific index) or `.set_markets(...)`
  (broad market). Index identifiers are TradingView-specific strings, e.g.
  `SYML:SP;SPX` for S&P 500 — these had to be reverse-engineered/verified by
  live testing (see `INDEX_MAP` in `scan_queries.py`), they're not obviously
  documented anywhere.
- Response shape: `{ strategy, marketIndex, totalMatches, returned, candidates: [...], timestamp }`.
  `candidates` is the `parse_candidates()` output — flat dicts with
  `ticker, name, price, change, volume, marketCap, high52w, low52w, sma50,
  sma200, rsi, relativeVolume, sector, pctFromHigh, exchange, adx, ema10,
  ema21, perf52w`.

### 2.3 `backend/paper_trading/live_signals.py` — the second consumer

`get_momentum_signals()` (line ~95) calls `scan_queries.build_best_query()`
and `scan_queries.parse_candidates()` **directly as Python function calls**,
no HTTP round-trip — this runs inside a standalone daily cron-style job
(`daily_job.py`), not inside a Flask request. This is the reason the shared
module exists: the query needs to be callable both as "backend of an HTTP
route" and "step in an offline batch job," with identical output either way.

### 2.4 Frontend: `frontend/src/services/api.js` + `frontend/src/App.jsx`

- `fetchScanStrategies()` (api.js ~line 257) — `GET /api/scan/strategies`,
  returns the list of strategy names/descriptions for the dropdown.
- `fetchScanResults(strategy, limit, marketIndex)` (api.js ~line 288) —
  thin wrapper around `GET /api/scan/tradingview`.
- `App.jsx` — `selectedStrategy`/`selectedMarketIndex` state (~line 110-113),
  `runScan()` (~line 512) calls `fetchScanResults()` and populates the Scan
  tab's results table (~line 2570 onward). A separate follow-up call,
  `loadBreakoutBadges()`, batches an *unrelated* endpoint
  (`/api/breakout/batch`, STA's own OHLCV-based breakout-state engine — not
  part of the TradingView screener at all) for the top 20 rows only, to add
  a breakout-status badge column without blocking the initial table paint.

---

## 3. Request flow, end to end (strategy='best' example)

```
User clicks "Scan Market" (strategy=best, market_index=all)
        │
        ▼
frontend/App.jsx  runScan()
        │  fetchScanResults('best', 50, 'all')
        ▼
frontend/services/api.js  fetchScanResults()
        │  GET /api/scan/tradingview?strategy=best&limit=50&market_index=all
        ▼
backend/backend.py  scan_tradingview()
        │  strategy == 'best'
        │      → scan_queries.build_best_query(limit=50, market_index='all')
        │      → query.get_scanner_data()   [actual HTTP call to TradingView]
        │      → scan_queries.parse_candidates(results, is_canadian, 'best')
        ▼
JSON response  { candidates: [...], totalMatches, returned, ... }
        ▼
App.jsx renders results table + fires loadBreakoutBadges() for top 20 rows
```

The exact same `build_best_query()` + `parse_candidates()` pair, called
directly (no HTTP hop) from `paper_trading/live_signals.py`'s
`get_momentum_signals()`, runs once a day via `daily_job.py` (launchd-
scheduled) to generate paper-trading entry signals — independent of whether
anyone opens the Scan tab that day.

---

## 4. The "best" strategy's actual filter (Config C)

Defined in `scan_queries.build_best_query()`. This is the one strategy that's
backtest-validated (see this repo's `docs/claude/versioned/
SURVIVORSHIP_FREE_BACKTEST_DAY79.md` if porting the *strategy*, not just the
*plumbing*, matters to you):

| Filter | Condition |
|---|---|
| Exchange | NYSE / NASDAQ / AMEX (or TSX/TSXV/NEO for Canadian) |
| Market cap | ≥ $2B |
| Price vs SMA50 | `close > SMA50` |
| Trend | `SMA50 > SMA200` |
| ADX | ≥ 20 (trend strength) |
| RSI | 50–70 (band, not overbought/oversold extremes) |
| EMA cross | `EMA10 > EMA21` |
| 1-year performance | `Perf.Y > 0` |
| Relative volume (10d) | ≥ 1.0 |
| Order | `ADX descending` |
| Post-filter (code-side, not TradingView-side) | Drop anything >25% below 52-week high — `col()` objects don't support arithmetic in this library, so this can't be expressed as a `.where()` clause; it's applied in `parse_candidates()` after the DataFrame comes back |

The other four strategies (`reddit`, `minervini`, `momentum`, `value`) are
simpler, non-backtested filter presets defined inline in `backend.py` — they
exist for exploratory scanning, not for anything paper-trading or verdict
logic depends on.

---

## 5. Known gotchas (learned the hard way in this project)

1. **`col()` objects don't support arithmetic.** You can't write
   `col('close') / col('price_52_week_high')` — express percentage-from-high
   style logic as a post-filter in Python after `get_scanner_data()` returns,
   not as a `.where()` clause.
2. **1-year performance is `Perf.Y`, not `Perf.52W`** — an easy wrong guess.
3. **`.set_index()` resets the market.** Calling `.set_index('SYML:SP;SPX')`
   switches the query's market scope to `/global` — don't assume it composes
   cleanly with a prior `.set_markets()` call; verify the combination live.
4. **`.order_by()` replaces, it doesn't stack.** Calling it twice (e.g. once
   inside a shared query builder, once in a caller that "just wants a default
   sort") silently discards the first sort. This was a real, shipped bug in
   this project (§2.1 above) — audit every call site if more than one part
   of the codebase touches the same `Query` object's ordering.
5. **Multiple `.where()` calls can replace rather than append filters** in
   this library version — consolidate all filter conditions into **one**
   `.where(...)` call with multiple comma-separated conditions, not several
   chained `.where()` calls. (This project hit this early — Day 21 fix,
   documented in a code comment in `backend.py` above the `'reddit'` branch.)
6. **Data is delayed unless you authenticate.** Without passing TradingView
   account cookies to the `Query`, you get delayed data (commonly ~15
   minutes) even for tickers TradingView shows real-time for free on the
   website itself — confirmed via the library's own GitHub discussion #42.
   Fine for swing/position trading (this project's holding periods are
   15-30+ days); would matter for anything intraday/day-trading.
7. **Junk tickers need explicit filtering.** The raw screener returns SPAC
   units (`...U`), warrants (`...W`, `...WS`), preferred share series, and
   commodity-trust ETFs (GLD, SLV, PHYS, etc.) alongside normal common stock —
   `parse_candidates()`'s ticker-suffix checks exist specifically to strip
   these out before showing results as "stock candidates."
8. **No point-in-time query.** The screener only ever reflects the *current*
   market state — there's no way to ask "what would this screener have
   returned on a past date?" A scheduled job that misses a day can't
   backfill that day's candidate list; it's simply gone. (This shaped how
   this project's paper-trading engine handles missed runs — see Golden
   Rule 21 in `docs/claude/stable/GOLDEN_RULES.md` if porting a similar
   automated-signal-generation job.)

---

## 6. If porting this pattern to another project

The reusable shape, stripped of STA-specific strategy names:

1. One module (`scan_queries.py`-equivalent) that owns `Query` construction
   for any strategy more than one consumer needs (a live UI route AND an
   offline job, in this project's case). Export a `build_X_query()` that
   returns an **unexecuted** query plus any metadata the caller needs (here,
   `is_canadian`), and a `parse_X_results()` that turns the raw DataFrame into
   clean, JSON-safe dicts.
2. The Flask/HTTP layer calls the shared builder, executes it
   (`query.get_scanner_data()`), calls the shared parser, and does nothing
   else strategy-specific to the query object — any post-processing
   (sorting, limiting) that isn't already inside the shared builder needs an
   explicit "does this strategy already set its own?" guard, per the bug in
   §2.1.
3. Any offline/cron consumer imports the same module and calls the same two
   functions directly — no HTTP hop needed if it's in the same codebase.
4. Don't trust the library's data freshness without checking — verify
   whether your use case needs real-time (pass cookies) or delayed is fine
   (don't bother).
