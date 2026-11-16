# Live price in the Analyze header: Plan v2 (Day 126, revised after the Opus review)

**Status:** PLAN v2. Step 1 (plan) and step 2 (independent Opus review, verdict **GO with 6 must-fixes**) done; step 3 (build) and step 4 (three review passes) follow, after the user says go.
**Why (user, Day 126, IBKR screenshot):** NVDA showed **$156.10, -$6.75 (-4.14%)** at IBKR; STA showed **$162.85**. "A 15-minute delay is OK, but this is too much." The user also said: we have several data sources and Tradier sends live quotes, so use them.
**Rule:** the header shows a current price with its time. Every indicator, verdict, stop and backtest number stays on completed daily bars and does not change.

## 0. What is true today (verified Mon 2026-11-16, ~14:55 ET; the review re-verified)

| Fact | Evidence |
|---|---|
| STA's header price is the last daily bar, dated: NVDA 162.85, 2026-11-13. The gap to IBKR is about **one trading day**, not 15 minutes. | `/api/stock/NVDA`; -6.75 / 162.85 = -4.14% |
| Yahoo **daily** history already contains **today's forming bar** mid-session (NVDA `2026-11-16 156.175`). So "last completed close" must be built with `market_time.drop_forming_bar`, never read as the last row. The `/api/stock` Known Issue (Medium, Day 124) is the same root cause. | live check; `KNOWN_ISSUES_DAY126.md` |
| Yahoo 1-minute bars (`prepost=True`) are current to the minute, tz-aware, for NVDA **and** for SOXL.NE (318 bars up to 14:57 ET today) and GDXU.TO. "Close-only" applies to SOXL.NE's **daily** history only. | live check, both reviewers |
| `get_quote` has exactly two callers, both `^VIX` (`backend.py:1389`, `paper_trading/live_signals.py:98`); 1-hour cache, stale-serve, no timestamp. Not suitable; left untouched (Golden Rule 54). | grep, review |
| Tradier returns `last` and `trade_date` (ms); Finnhub returns `c` and `t` (s). Both timestamps are **thrown away today** (`tradier_provider.py:146-157`, `finnhub_provider.py:104-117`). Tradier and Finnhub are US only. Yahoo is the only Canadian source. | code |
| `market_time.py` is weekday-blind (a 16:30 cut-off only). There is no exchange calendar and no holiday table anywhere; `pandas_market_calendars` is not installed. | code |
| A 45 s cache works through `cache_manager._set_cached_market_ttl(key, data, ttl_hours=0.0125)` (now + TTL). The trading-day expiry belongs to `set_cached_market`, which must NOT be used. | `cache_manager.py:472-494` |
| The Yahoo circuit breaker and ~30/min limiter are **shared** with daily OHLCV and the VIX quote. | `yfinance_provider.py:374-383` |

## 1. Decision

A separate **live quote**, display only. `get_quote` stays as is.

### 1.1 Backend
- New provider method `get_live_quote(ticker)` -> `LiveQuote {price, last_trade_at (exchange time, tz-aware), age_minutes, change, change_pct, last_close {price, date}, session, currency, source}`.
- **Source order:** US tickers: **Tradier** (`last`, `trade_date`) -> **Yahoo 1-minute** (last bar) -> **Finnhub** (`c`, `t`). Canadian tickers (`.TO`, `.NE`, `.V`): **Yahoo 1-minute only**. First good answer wins. Every miss is logged `ticker, provider, reason` and counted by that provider's breaker. Yahoo's live calls use their **own breaker and rate budget** (`yfinance_live`), so three failed minute-fetches cannot block daily OHLCV.
- **One staleness rule (replaces the v1 contradiction):** the price carries its **last trade time**, labelled "last trade 2:41pm ET", never "delay". In the regular session a trade older than **20 minutes** gives `available:false, reason "no recent trades"` (thin or halted ticker); newer than that is shown with its age (2 min or less reads "Live"). 15-minute-delayed feeds therefore pass and are labelled honestly.
- **Session without a calendar:** derived from the quote's own timestamp against the exchange's usual hours (pre 04:00-09:30, regular 09:30-16:00, post 16:00-20:00 ET; Toronto the same clock). A last trade that is not today, or outside those hours, is `closed` ("Market closed, last close shown"), so weekends and holidays fall out naturally without a holiday table. Helper lives in `market_time.py` (one place). Known limit, accepted and documented: an early-close day shows "regular" until the old trade ages past 20 minutes.
- **`last_close`** comes from the orchestrator's `get_ohlcv(ticker, '2y')` (split-adjusted by `_deliver`, which matters for SOXL.NE) then `market_time.drop_forming_bar`. `change` and `change_pct` are computed in one place, from this `last_close`, for every provider (provider-supplied `prevclose` / `pc` are ignored). The header's "last close" line is the **same** value, so the two lines cannot disagree. Between 16:00 and 16:30 ET the existing 16:30 rule still treats today's bar as forming, so the change is measured from the previous close until 16:30, then flips with the close line together. Tested at both times.
- **Currency** comes from the existing `stock.currency` field of `/api/stock` (USD for NVDA, CAD for `.TO`/`.NE`), passed through, not guessed.
- `GET /api/quote/<ticker>` -> that object, or `{available:false, reason}` with HTTP 200. Never a guessed price. Cache **45 s** per ticker via `_set_cached_market_ttl`; nothing older than 5 minutes is served stale.

### 1.2 Frontend
- Header: `Now $156.05 (-4.17%) · last trade 2:51pm ET` and `Last close $162.85 · Nov 13` (the close line is taken from the quote response when available, else today's existing dated line). Only the change is coloured.
- States, all visible: `Live`, `Last trade N min ago`, `After hours` / `Pre-market`, `Market closed, last close shown`, `Live price unavailable (no recent trades / source down)`.
- Refresh: on ticker load, then every 60 s while the tab is visible and the session is open. When closed, **re-check every 5 minutes and on tab focus** (so a page left open over the weekend wakes up at the open). Abort on ticker change; drop any response whose `ticker` is not the current one.
- **Entry ruler:** the live price is added to the scale inputs (`technicalReadChecks.js`, the `all = [price, ...marks]` list) as a display-only input so the marker can never fall off the bar. The marker is a separate element with its own test id `live-tick` (NOT `timing-tick`: page check A12 caps `timing-tick` at 1-3), placed in a second label row so it cannot overlap the close bubble. A new page-check item asserts it exists only when a live quote exists.
- Plain English, no verdict words (Golden Rules 62/63).

### 1.3 What does NOT change
RSI, SMA/EMA, ATR, ADX, S&R, MR rules, Technical Read facts, volume card, backtests, verdict parity (86,400), `/api/stock`, the `/api/stock` forming-bar Known Issue (stays open, recommended as the very next separate fix: same root cause, but it changes indicator inputs mid-session, so it gets its own plan).

## 2. Callers checked (Golden Rule 54)
`get_quote`: two ^VIX callers, untouched. `describePriceAsOf`: `App.jsx:987` and `test_price_as_of.mjs` only. Page check A4 only looks for "Unknown"/ETF wording in the header. `currentPrice` consumers (entry timing, pullback plan, MR card) keep the close. To be re-grepped at build time: `currentPrice`, `price-as-of`, `timing-tick`, `live-tick`.

## 3. Engineering standard
- **No silent failure:** every provider miss is logged; the UI says "Live price unavailable", never the old close pretending to be current.
- **Performance:** one provider call per ticker per 45 s; one page asks at most once a minute. Tradier ~120/min.
- **Real data behind every element:** time is the quote's own trade time; age is measured. 
- **Time zones:** tz-aware throughout; ET for US, the listing's own clock for Canada.
- **Scope:** Analyze header + ruler only. The Scan tab and the leaderboard stay on closes.

## 4. Tests
- Backend (mocked providers): source order for US vs Canadian; fallthrough with logged reasons; trade older than 20 minutes -> unavailable; zero/negative/NaN price rejected; Tradier `trade_date` ms and Finnhub `t` s parsed; tz-aware vs naive; session for 03:59, 04:00, 09:29, 09:30, 15:59, 16:00, 20:00 ET, weekend, a holiday (old trade date); `last_close` = forming bar dropped (mid-session NVDA must give 162.85, not 156.18); 16:00-16:30 and after-16:30 `change_pct`; separate Yahoo breaker; cache hit within 45 s, miss after; `available:false` shape.
- Real-data run, same minute as IBKR: NVDA, AAPL, SOXL.NE (expect ~12.8 vs 14.69), GDXU.TO, a US ETF, a thin ticker; ^VIX path unchanged.
- Frontend: label/state builder (every state, wrong-ticker response dropped, NaN/null); ruler scale with a live price below the lowest average; page checker extended (live line present, never contradicts the close line; `live-tick` only with a quote); A12 still passes.
- Three passes; screenshots at 390 px and desktop.

## 5. Defaults I will take unless the user says otherwise
1. Show pre/post-market price, labelled (IBKR does).
2. Auto-refresh every 60 s while the tab is visible.
3. Analyze header and ruler only.

## 6. Risks
Yahoo throttling (45 s cache, own breaker, Tradier first for US); thin or halted tickers (20-minute rule, "no recent trades"); two prices confusing the reader (one clear "Now", one dated "Last close", both from the same source of truth); early-close days (documented).
