# /api/stock: drop today's unfinished bar (Day 126) — PLAN v1

Status: user said "lets fix it" after the size was measured (Known Issues, Medium: ATR reads 0-3.4% low, EMA21 <0.5%, SMA50/200 ~0, mid-session).
Goal: the Analyze page's price history, averages, ATR and "last close" are always on COMPLETED daily bars, the same rule the MR, pattern and
index-trend paths already use. The live price (Day 126) stays the only live number.

## 1. Change
`backend/backend.py` `get_stock_data` (line ~1063): right after `hist` is obtained (provider, cache or legacy path) and before `hist.tail(260)`:
`hist, forming_dropped = market_time.drop_forming_bar(hist)`. The cache stays RAW (it already is). Rule = `is_forming_bar`: last bar dated today
(New York) and time < 16:30 ET. Add `formingBarDropped: bool` to the response (honest signal; no frontend dependency).
Nothing else in the route changes (52-week high/low from info, split fix, NaN handling).

## 2. What changes for the user (all intended)
- Mid-session, `currentPrice` and the last history bar are yesterday's completed close, dated yesterday. Header "Last close $X · date" and the
  entry block's "(last close)" row become TRUE (today they would show a partial price under that label).
- 21/50/200-day averages, ATR (via /api/sr, separate), RS vs market and the trend checks use completed bars only.
- After 16:30 ET, or before the open, or weekends: no change (no bar for today / bar is final).

## 3. Callers and risks to verify (grep the real graph, Golden Rule 54)
1. `frontend/src/utils/priceAsOf.js` / App.jsx header: today-dated bar was labelled "intraday, not a close"; after the fix that label should
   rarely or never appear. Check it still reads right when it does not appear.
2. `deriveEntryVolume` (technicalReadChecks.js): compares `/api/sr` `meta.prevBar.date` to history[-2]; and uses `barComplete`. After the fix
   history[-1] is already the last complete bar while /api/sr may still say today's bar is partial. Risk: the dates-disagree path marks the last
   bar 'unknown' and prints a new warning. Must trace and fix so volume votes still use the last complete bar with no false warning.
3. Other consumers of `priceHistory` / `currentPrice` from `/api/stock` (fetchAnalysisData, fetchFullAnalysisData, App.jsx, scoring engine, RS,
   volume card, Data Sources tab provenance, `dataSourcesView.js` mentions "intraday"): list each, confirm none needs today's bar.
4. Alignment with SPY/QQQ histories (different endpoints): they may still include today's partial bar or not. Check how RS and the market backdrop
   align by date so a one-bar offset does not appear.
5. `/api/sr` and `/api/patterns` already drop the forming bar: confirm both then agree with `/api/stock` on the last bar date.
6. Cache: nothing new is written; confirm the raw frame is not mutated (drop returns a slice, never mutates).
7. Index tz: `drop_forming_bar` uses `str(df.index[-1])[:10]`; confirm for provider frames (tz-aware / naive), Canadian tickers (.TO/.NE, same ET rule).
8. IPO / one-bar history: dropping the only bar must not return an empty frame to code that assumes rows (404 / short-history path).
9. Parity/golden rules: engine inputs change by tiny amounts mid-session only; check whether any backtest/parity test feeds `/api/stock` (grep tests).

## 4. Tests
- New `backend/test_stock_forming_bar.py`: freeze `now` (injectable via market_time) and test the route's helper path: mid-session with a today bar
  (dropped, flag true, currentPrice = prior close, newestDate = prior date), after 16:30 (kept), pre-market (no today bar, kept), weekend, single-bar
  frame (not emptied), tz-aware index, Canadian ticker.
- Frontend `test_entry_timing.mjs` / volume test: the history-without-today-bar + srData barComplete=false combination (risk 2) with the real expected result.
- Page checker A-checks that read the header close date and the entry block row (A12/A13) pass on live runs; run after hours AND, if possible, with a
  faked mid-session clock (route test covers the backend side).

## 5. Docs
Known Issues: move the Medium entry to Changes with the measured numbers; note the early-close day limitation is unchanged (16:30 rule).

## 6. Process
Plan -> Opus review -> build after the user says go -> three passes -> Known Issues entry -> commit.

## 7. Review result (v2) — Opus: GO WITH CHANGES, applied
- Plan item 5 was false: `/api/patterns` and `/api/market/spy` did NOT drop the forming bar, and `/api/sr` only drops it for levels and ATR. Fixing only
  `/api/stock` would have mixed completed and partial bars (RS offset by a day; trend rows disagreeing with the header). All three routes now use `drop_forming_bar`.
- `deriveEntryVolume` would have warned on every mid-session analysis; fixed (history last date == S&R prevBar date while S&R says partial = complete).
- Empty frame after the drop (IPO day) returns 404. Tests patch the clock via `market_time.is_forming_bar` and a fake provider (`backend/test_forming_bar_routes.py`).
- `formingBarDropped` is not read by the UI (`fetchStockData` lists fields, Golden Rule 30). Comments in `priceAsOf.js` and `technicalReadChecks.js` updated.
- Left as logged Low items: 52-week high/low mixed basis, `/api/sr` partial fields kept on purpose, early-close days (Nov 27, 2026).
