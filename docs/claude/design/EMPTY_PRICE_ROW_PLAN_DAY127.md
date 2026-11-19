# Empty price row plan (Day 127) — v2, Opus review applied (GO WITH CHANGES). Section 3 is superseded by section 8.

Part of Data Source Audit Round 2 (ROADMAP #20). Plain English first; file names in section 6.

## 1. What went wrong (measured today, not guessed)
- Last night at 8:58 to 9:16pm, Yahoo gave us price history where the newest row (Nov 18) had **no prices at all** (open, high, low, close all empty) but did have a volume number. Yahoo had not finished that day yet.
- Nothing in the app checks for an empty row. It was saved in the app's cache. The cache is set to keep it until today's close (4:30pm), so the app used the broken row all day.
- Result: for 15 tickers the "price" is NaN ("not a number"). `/api/sr` then sends invalid JSON (`"currentPrice": NaN`) and the Support/Resistance numbers, today's change, and the volume reading can break.
- The 15 tickers: AAPL, MSFT, META, NVDA, AVGO, LLY, V, WMT, PG, HD, ABBV, KEYS, MRVL, VRT, ALAB. All Yahoo. One more (SO) has an old empty row from 2024 inside its history, not at the end.
- My audit missed it because the audit downloads fresh data from each provider; it never looked at the app's own saved copy.
- Not caused by the Tradier change. It was already there.

## 2. What we want
A bar with no close price should never reach a card, and the app should notice and fix itself, and the audit should shout if it ever happens again.

## 3. The change (three small parts)
**A. Stop saving empty rows.** When a provider's history comes in, remove rows with no close price before it is saved, and print one line saying how many were removed and for which dates. (If the newest row was removed, the cache entry is also made short-lived so the next request asks again.)
**B. Heal what is already saved.** When the cache is read and its newest row has no close price, treat the entry as "not saved" so the app fetches fresh data. If the fresh data still has an empty newest row, drop it and serve the older day, and print a warning. The 15 bad entries fix themselves on their next use; nobody has to delete anything. Rows with no close price in the MIDDLE of old history (like SO in 2024) are just removed, with no refetch.
**C. Tell us when it happens (audit).** The Data Sources tab quality check and the nightly audit get a new check: "newest row has no close" = FAIL, "any empty rows" = WARN. They read the cache directly, so they see what the app sees. The page checker also gets one check: no NaN anywhere in the `/api/sr` and `/api/stock` answers.

## 4. What we are NOT doing in this plan
- No change to the Flask JSON output for every endpoint (turning every NaN into null for all routes) — wider blast radius, separate decision (question 3 below).
- No change to provider order, cache times, or price basis.
- Rows where only open/high/low are empty but the close exists: left alone (the existing integrity check C4 already reports them).

## 5. Tests first
1. A frame whose last row is empty: not saved; log line; cache short-lived.
2. A saved entry with an empty last row: read returns "miss", provider is asked again.
3. Refetch still has an empty last row: it is dropped, the older day is served, and a warning is logged.
4. Empty row in the middle of history: removed, no refetch.
5. Normal frame, frame with 1 row, all-empty frame, the audit's "raw" reader still shows the empty row (the audit and Data Sources tab must be able to SEE the problem).
6. Real data: re-run `/api/sr` for the 15 tickers: valid JSON, no NaN, currentPrice is a number.

## 6. Where the code lives (for the builder and the reviewer)
- Providers hand frames to `providers/orchestrator.py::_get_ohlcv_locked` (writes the cache at `cache_manager.set_cached_ohlcv`, serves with `_deliver`).
- Cache reads: `cache_manager.get_cached_ohlcv` uses the shared `deserialize_ohlcv` (also used by the audit and the Data Sources tab readers: do NOT filter inside `deserialize_ohlcv`, or the audit goes blind).
- Other writers/readers to check: `backend.py` legacy direct-Yahoo paths (`/api/stock`, `/api/sr`, `/api/patterns`, `_index_history`, MR routes), `live_quote.py` (reads the frame), `_get_stale_ohlcv`, `breakout_routes.py`.
- `/api/stock` already skips empty-close rows when building `priceHistory`; `/api/sr` does not (it takes `df['close'].iloc[-1]`).
- Cache expiry (`calculate_ohlcv_expiry`): data fetched after the close is kept until the NEXT close + 30 min. That is why an unsettled after-close bar stays all day.

## 7. Questions for the reviewer
1. Best single place for A: orchestrator (after the provider returns), or `set_cached_ohlcv` (every write passes there, including legacy paths)? Cache must stay "raw" for the audit (Day 126 rule). Is dropping empty rows before saving a violation of that, or is an empty row not "data"?
2. B: is "treat as a miss and refetch" safe against the Twelve Data / Tradier rate limits (a mass refetch of many tickers at once; Golden Rule 25)? Should it be rate-spread or limited per request?
3. Should we ALSO make all API answers NaN-safe (null) now, as a safety net (Golden Rule "NaN is worse than null", Day 61), or leave it out of this change?
4. Which callers could change behaviour when the last row disappears (live_quote's last-close, the forming-bar logic, MR, the nightly audit)? Anything that expects `len(df)` to match the cached `rows` column?
5. Does the after-close expiry rule need a change (short-lived entry when the newest bar looks unsettled), or is A+B enough?

## 8. Opus review, applied (Day 127; verdict GO WITH CHANGES)
**Confirmed by the reviewer (and by us):** exactly the 15 tickers named, all Yahoo, cached 20:58-21:16 ET Nov 18, expiring Nov 19 16:30, last row NaN open/high/low/close with real volume; no Twelve Data entry has one; there is no custom Flask JSON provider, so NaN goes out as-is.

**Corrections to what v1 said (our mistakes):**
1. "Nothing checks for an empty row" was WRONG. `data_quality` already counts `nan_closes` (data_quality.py:116) and warns (:143). The real gap: it takes "last bar" from `h.index[-1]` (:82), which IS the empty row, so freshness read "current". (Verified by us.)
2. SO's empty row is its FIRST row (2024-11-18, volume 0), the known Yahoo leading-empty-row artifact, not a hole in the middle. (Verified by us.)
3. The nightly audit does NOT read the app cache. It fetches each provider directly and keeps its own JSON cache. It sees the app cache only through `/api/provenance`. The readers that use `read_ohlcv_entry` are the Data Sources tab, `_get_stale_ohlcv` and `audit_splits.py`.
4. "Yahoo had not finished that day" is a GUESS: the fetch was 5 hours after the close and Twelve Data / .TO tickers fetched in the same window are clean. Cause unknown.
5. "Volume can break" was wrong in the worse direction: the NaN bar has a normal-looking volume, so RVOL looks plausible while the price is empty. And `/api/stock` fills the price with 0 (backend.py:~1195), which breaks Code Architecture Rule 5 (null, not zero).

**Changes to the design:**
- **A (drop empty rows) moves from "when saving" to "when serving".** The cache stays RAW (Day 126), so the audit and the Data Sources tab still SEE the empty row. One new helper `market_time.drop_empty_close(df, ticker)` (Rule 59: one rule, one place), called first in `orchestrator._deliver` and in `split_adjust.fix_frame`; together these cover every orchestrator path and all six direct-Yahoo fallbacks (backend.py:1109, 1304, 1819, 2180, 3878, 3949; breakout_routes.py:56). A save-time drop would miss five of the six fallbacks. It logs the dates it dropped.
- **B (treat as a miss and refetch) is DROPPED.** It would refetch on every request (the refetch is saved raw again), a 1y MR read would loop on the bad 2y entry because a shorter fetch may not overwrite a fresh longer one (cache_manager.py:318-322), and Twelve Data's 8-a-minute limiter does not wait (a refused call falls through to Yahoo/Tradier; the limiter is per process).
- **B is replaced by a short expiry on save:** when the NEWEST close is NaN, `expires_at = min(expires_at, now + 30 min)` (same pattern as the Tradier 45-minute rule), with a log line. At most one refetch per ticker per 30 minutes. The 15 bad entries expire at 16:30 on their own; to fix them sooner, clear them one by one with `POST /api/cache/clear?ticker=...`.
- **C (audit):** `data_quality.check_history` takes `last_date` from `h['close'].last_valid_index()` and adds `newest_close_missing`, graded FAIL. Page checker gets "no NaN in the `/api/sr` and `/api/stock` answers". (Not the nightly audit: it does not read the cache; a later item may add a cache scan.)
- **`/api/stock`: the 0 fill becomes null** (Rule 5).
- **Making every API answer NaN-safe is a SEPARATE plan.** Wide blast radius.

**What changes for callers when the newest row is dropped at serve time:** `live_quote._last_close` goes from None (change hidden) to the Nov 17 close, so add a check against the expected last session; `/api/sr` price, change, candle, volume and RVOL all move together to Nov 17 and stay consistent; MR and patterns show Nov 17 in `asOf`; `/api/stock`, `breakout_detection.py:103` and `simple_sr.py:152-155` already skip NaN rows (no change); the `rows` column still matches `len(df)` because the cache stays raw; the 0.95 row tolerance and the per-ticker lock are unaffected.

**Known gap found by the reviewer, NOT in this change:** a fetch between 16:00 and 16:30 is kept until the NEXT day's 16:30, and after 16:30 `drop_forming_bar` treats that possibly-partial bar as complete (market_time.py:19 vs cache_manager.py:124). Logged for a separate decision.

**Tests:** `_deliver` and `fix_frame` drop a NaN last row and a NaN first row and log the dates; `set_cached_ohlcv` keeps the raw rows with expiry <= 30 min; `read_ohlcv_entry` still shows the NaN row; `check_history` gives FAIL with the right `last_date`; a 1y read against a bad 2y entry makes one provider call per 30 minutes, not one per request; edge frames (1 row, all-NaN gives an empty frame and a clean 404/503, capitalised columns); live_quote with a dropped bar; real data: the 15 tickers on `/api/sr` return valid JSON with a numeric currentPrice. Tests use a temporary state file (Golden Rule 22).
