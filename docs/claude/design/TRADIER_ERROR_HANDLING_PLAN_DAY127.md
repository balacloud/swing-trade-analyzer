# Tradier HTTP-400 handling (plan, Day 127) — v2, Opus review applied (GO WITH CHANGES), see section 8. Section 3 is superseded by section 8.

Part of Data Source Audit Round 2 (ROADMAP #20). Not built.

## 1. Evidence (all measured Day 127, nothing assumed)
- Tradier docs (docs.tradier.com/brokerage-api/markets): over the limit returns **HTTP 400, not 429**, body "Quota Violation"; throttle with `X-Ratelimit-*` headers. Limit 120/min production (60 sandbox), per token, market-data calls. Docs say nothing about timeouts. (The dedicated rate-limit page and FAQ were 404 for us.)
- Live probe, our production token: quote 0.43 s, history 0.46 s, headers `X-Ratelimit-Allowed 120 / Used / Available / Expiry`.
- Live probe: unknown symbol -> **HTTP 400** `Invalid parameter, ZZZZNOTREAL: symbol not found.` Bad date range -> **HTTP 400** `Invalid parameter, end: must be on or after ...`. A request with NO symbol hung until our 15 s read timeout.
- Our code, `providers/tradier_provider.py:225-237` `_handle_http_errors`: 429 -> RateLimitError (+breaker failure); 401/403 -> AuthenticationError (+failure); >=500 -> ProviderUnavailableError (+failure); everything else -> `resp.raise_for_status()`. A 400 therefore raises `requests.HTTPError`, which the callers' `except Exception` (lines 113-115, and the quote paths) turns into `breaker.record_failure()` + ProviderUnavailableError.
- Our own limiter: `providers/rate_limiter.py:207` `'tradier': {'rate_per_minute': 100}` (below Tradier's 120), state shared across processes in SQLite (Golden Rule 22).
- Audit Day 127 (117 tickers, 79 US): Tradier 1 ok, 6 read-timeouts (15 s), 72 skipped by an open breaker.

## 2. Problems
A. A real quota 400 is not recognised as a rate limit (shows up as a generic failure).
B. Every other 400 (unknown symbol, bad parameter) counts toward the circuit breaker. That is the Golden Rule 36 mistake (a ticker with no data is not an unhealthy provider): three unknown tickers in a row would open the breaker for 5 minutes and block every healthy ticker.
C. Our limiter cannot see calls made by other programs using the same token (OptionsIQ, per the file's header comment); only the response headers can.
D. (Question, not a decision) 15 s read-timeouts count toward the breaker; 3 open it. Probably right, but 6 timeouts in one audit run is unexplained.

## 3. Proposed change (one file: `providers/tradier_provider.py`, one new test file)
In `_handle_http_errors`, before `raise_for_status()`:
1. `status == 400` and body contains "quota" (case-insensitive) -> `breaker.record_failure()`, raise `RateLimitError(..., "HTTP 400 quota violation")`. Same treatment as the existing 429 branch.
2. `status == 400` otherwise (symbol not found, bad parameter) -> raise `DataNotFoundError(self.name, <body text>, ticker)`; NO breaker failure.
3. Read `X-Ratelimit-Available` from every response; if it is below 10, record a short pause through the existing limiter (no new mechanism) so the next call waits. (Opus to say whether this is needed or over-built.)
4. No change to timeouts, to the chain order, or to the breaker thresholds.

## 4. Tests first (`backend/backtest/test_tradier_errors.py`, wired into `run_all_checks.sh`)
Fake `requests` responses: 200 ok; 429; 400 "Quota Violation" -> RateLimitError and breaker failure +1; 400 "symbol not found" -> DataNotFoundError and breaker failure +0; 400 "Invalid parameter, end" -> DataNotFoundError, +0; 401; 500; headers low -> pause. Each of the three call sites (history, quote, the second quote at line ~172) exercised. Plus: 3 consecutive "symbol not found" must leave the breaker CLOSED.

## 5. Blast radius to verify (Golden Rule 54)
- Callers of `TradierProvider` / the orchestrator chain: how do they treat DataNotFoundError vs ProviderUnavailableError (do they fall through to the next provider the same way)? Live quote is Tradier-first for US.
- `live_quote._chain`, `orchestrator.py` fallback order, `audit_data_sources.py`, `audit_vs_ibkr.py`, nightly audit.
- Does any code string-match the old error text?

## 6. Not in this plan
Rerouting providers, Tradier dividend basis, Twelve Data limits (separate item), timeout values.

## 7. Questions for the reviewer
1. Is matching the body text "quota" safe, or could a quota 400 carry a different body (check docs/known client libraries)? What if the body is XML or empty?
2. Is "every other 400 -> DataNotFoundError" correct, or could a 400 also mean a malformed request caused by OUR bug (e.g. a bad symbol mapping like BRK-B), which should surface loudly instead of silently falling through (Golden Rule 6)?
3. Is item 3 (header-based pause) worth building now?
4. Anything in the blast radius I missed?

## 8. Opus review, applied (Day 127; verdict GO WITH CHANGES, claims re-checked by us)
Checked by us after the review: the QUOTES endpoint answers an unknown symbol with **HTTP 200** and `unmatched_symbols` (not 400), so the 400 is a HISTORY-only behaviour; the 6 audit timeouts were CAT, BRK-B, JPM, JNJ, GEV, NFLX (only BRK-B has a dash, so the "audit sends BRK/B" idea does not explain them; cause still unknown).
Corrections to this plan: the `except Exception` blocks are at tradier_provider.py:114-116 (history), :161-163 and :193-195 (quotes); the "second quote" is `get_live_raw` (:165); Golden Rule 6 is "never hallucinate", the closest rule for silent fallbacks is Code Architecture Rule 6 (return null, not a plausible fake).

Changes accepted:
1. **Only a body containing "symbol not found" becomes `DataNotFoundError`** (no breaker failure). Any other 400 (bad date, empty or unknown body) is probably OUR bug: raise `ProviderError` with the body and a loud print, still no breaker failure. Reason: production sends the raw ticker, so a mapping bug (BRK-B) would otherwise hide as "no data" (Rule 6).
2. **Quota detection:** body contains "quota" (any case) OR header `X-Ratelimit-Available` is "0" -> `breaker.record_failure()` + `RateLimitError` (same as the 429 branch). Read `resp.text`; do not parse JSON (error bodies are plain text).
3. **Add `ProviderError` to the three re-raise tuples** (:111, :159, :191); otherwise the `except Exception` blocks catch it and count a breaker failure.
4. **Drop the header-based pause.** `TokenBucket` has no "pause" (rate_limiter.py:119-147); it would be new cross-process code (Rule 22). Only LOG `X-Ratelimit-Available` when a quota error happens.
5. **Empty-symbol guard:** the route regex (backend.py:1054) accepts `^`, which becomes `symbols=''` (:172), and an empty symbol hangs Tradier until the 15 s timeout (measured Day 127). Raise `DataNotFoundError` before sending the request in `get_quote` and `get_live_raw`.
6. **Tests must use a temporary state file.** Breaker and limiter state live in the real shared `data/provider_state.db` (circuit_breaker.py:35); a test that records failures could open the LIVE Tradier breaker. Point `circuit_breaker.DB_PATH` and `rate_limiter.DB_PATH` at a temp file before the first `get_breaker` call.
7. **Live quote consequence** (live_quote.py:91-92, :120-122): a Tradier not-found now counts in `not_found`; if every source says not-found the message becomes "no live price for this ticker" instead of "live price source unavailable". Add that case to `test_live_quote.py`. The orchestrator (orchestrator.py:181-184, :370-372) falls through the same way for every ProviderError subclass; nothing string-matches HTTPError.
8. Re-probe the quotes endpoint before assuming a 400 there: DONE (it is 200).

Tests (temp state file): 400 "Quota Violation" -> RateLimitError, failures +1; 400 empty body with Available "0" -> quota; 400 "symbol not found" -> DataNotFoundError, +0; 400 "Invalid parameter, end" -> ProviderError, +0; empty-body 400 -> ProviderError, +0; 429 / 401 / 500 / timeout still count; three "symbol not found" in a row leave the breaker CLOSED; each case through `get_ohlcv`, `get_quote`, `get_live_raw` where the endpoint can produce it; ticker "^" makes no network call; live quote with all sources not-found.
Open, not part of this change: why 6 of the first calls timed out at 15 s while single probes answer in 0.4 s.
