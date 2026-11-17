# One price basis, one cached history per day (Day 126) — PLAN v1
Source: the 117-ticker universe run (`docs/test/Universe_Audit_20261117/FINDINGS.md`): most WRONG rows are two cards on ONE page reading different histories (CAT: /api/stock 52-week high 1073.46 vs /api/patterns 1068.93; AAPU, DUK, SO, PG, CVX, COP, JNJ, LIN, GE...).

## Evidence (measured, DUK, 504 bars)
- Twelve Data `time_series` is requested WITHOUT `adjust` (providers/twelvedata_provider.py:95-100); its default adjusts splits only. Yahoo `history()` default auto-adjusts for dividends too.
- Twelve Data default vs Yahoo(adjusted): median difference 3.49%, max 7.23%. Twelve Data with `adjust=all` vs Yahoo(adjusted): median 0.029%, max 0.061% (rounding).
- `cache_manager._period_to_min_rows('2y') = 2 x 252 = 504`, but Yahoo returns 501 rows for 2y, so every cached Yahoo history is "too short": `get_cached_ohlcv` returns None and each route refetches ("cache has 501 rows, need 504+ ... treating as miss"). Each route (stock, patterns, breakout, MR, sr, spy...) then calls providers separately and, with the Twelve Data breaker flapping, can get a different provider and basis within one page load.

## Change
1. `twelvedata_provider.py`: add `'adjust': 'all'` to the DAILY `time_series` params (not intraday). One basis (split + dividend adjusted) for every provider that adjusts (Yahoo, Twelve Data). Tradier (last fallback) does not adjust for dividends: log it as a known limit, and print a one-line warning when it serves a history.
2. `cache_manager._period_to_min_rows`: 2y = 480 rows (about 95% of 504; a calendar year has 250-252 trading days so '1y' = 238, '6mo' = 119 ...): `int(trading_days * 0.95)`. Keeps the Day-82 protection (a 1y entry must not serve a 2y request: 252 < 480) while accepting Yahoo's 501.
3. One-time: expire the OHLCV cache so unadjusted Twelve Data entries are not served until 16:30 ET (Golden Rule 43: the frontend refetches on the next Analyze; list every dependent refetch path before clearing).
4. Do NOT change: indicators, verdict code, Yahoo calls, the `known_splits.json` mechanism (applied after delivery; with `adjust=all` Twelve Data already adjusts splits, so the fix_frame must not double-adjust: check `split_adjust.fix_frame` against a Twelve Data history of a symbol in known_splits).

## Tests
- `backend/test_price_basis.py`: (a) `_period_to_min_rows` table (1y 238, 2y 480, 6mo 119, 5d 4, unknown 252*0.95?) and the Day-82 case (a 252-row entry is a miss for 2y, a 501-row entry is a hit); (b) the Twelve Data daily request carries `adjust=all` and the intraday request does not (patch `requests.get`); (c) `fix_frame` not double-adjusting (symbol in known_splits).
- Live: DUK/CAT/AAPU via /api/stock, /api/patterns, /api/breakout, /api/mr/signal agree on last close, 52-week high and 200-day average to the cent; second call is a cache HIT (log line).
- Re-run the Statement Audit on the 117-ticker universe: the T6-T9, BO1-BO5, MR-sma, RS-toggle clusters must disappear. Page checker 55/55.

## Risks for the review
1. Does `adjust=all` change anything else Twelve Data returns (volume adjusted for splits, column names, number of rows) and does Twelve Data's free plan honour it (it did in the measurement)?
2. Which code paths read the OHLCV cache with a different period string ('3mo', '1y', '2y') and assumed the old 504/252 thresholds (MR scan, momentum scans, paper trading frozen code, backtest warm-ups)?
3. Cache expiry mechanics and anything keyed on `rows`; the Data Sources tab ("Checked N bars") and provenance C8.
4. Is clearing the cache safe for `known_splits` (SOXL.NE keeps cache raw, adjusted after delivery)?
5. Tradier fallback basis, and any place where a mixed basis could still appear (e.g. SPY/QQQ index routes, intraday).
