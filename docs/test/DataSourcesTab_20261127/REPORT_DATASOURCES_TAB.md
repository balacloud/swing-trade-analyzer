# Data Sources tab Statement Audit

Run: 2026-11-27T06:54 · dumps: AAPL, SOXL.NE, VFV.TO

Verdicts: PASS 94 · WRONG 0 · MISLEADING 1 · UNVERIFIED 25

Method: the tab's own text (read from the page) against the cache DB, the provider state DB (breaker, limiter), provider_coverage.json and the orchestrator's chains. Read-only.

| Ticker | ID | Claim | Shown | Recomputed | Verdict | Severity | Note |
|---|---|---|---|---|---|---|---|
| VFV.TO | DS-4b | "just fetched" says a fetch happened | just fetched | a recorded fetch | MISLEADING | HIGH | the word is guessed from cache age under 5 minutes (backend.py _cache_status); nothing records a fetch. Another process or a restart can make it wrong either way |
| AAPL | DS-15-alpaca | Alpaca "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| AAPL | DS-15-tradier | Tradier "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| AAPL | DS-15-twelvedata | Twelve Data "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| AAPL | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| AAPL | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| AAPL | DS-18b | Coverage chips are CURRENT truth | 2026-11-14 | a re-test | UNVERIFIED | INFO | a hand-kept file dated by its own test run; not re-measured here (Alpaca "works" was measured 2026-11-21) |
| AAPL | DS-21 | Hit rate (24h) is computed from cache_stats events | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.8%Hit rate (24h) | - | UNVERIFIED | INFO | not traced |
| AAPL | DS-2b | Exchange, currency and fund type are TRUE (vs the broker) | NasdaqGS / USD | IBKR contract | UNVERIFIED | INFO | needs the broker contract record; the IBKR truth run covered closes, not these fields |
| SOXL.NE | DS-15-alpaca | Alpaca "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| SOXL.NE | DS-15-tradier | Tradier "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| SOXL.NE | DS-15-twelvedata | Twelve Data "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| SOXL.NE | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| SOXL.NE | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| SOXL.NE | DS-18b | Coverage chips are CURRENT truth | 2026-11-14 | a re-test | UNVERIFIED | INFO | a hand-kept file dated by its own test run; not re-measured here (Alpaca "works" was measured 2026-11-21) |
| SOXL.NE | DS-21 | Hit rate (24h) is computed from cache_stats events | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.6%Hit rate (24h) | - | UNVERIFIED | INFO | not traced |
| SOXL.NE | DS-2b | Exchange, currency and fund type are TRUE (vs the broker) | Cboe CA / CAD | IBKR contract | UNVERIFIED | INFO | needs the broker contract record; the IBKR truth run covered closes, not these fields |
| VFV.TO | DS-15-alpaca | Alpaca "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| VFV.TO | DS-15-tradier | Tradier "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| VFV.TO | DS-15-twelvedata | Twelve Data "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| VFV.TO | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| VFV.TO | DS-15-yfinance | Yahoo (yfinance) "ok" means it has answered | ok | breaker closed | UNVERIFIED | INFO | a closed breaker also reads "ok" for a provider that was never called; no per-provider call record exists |
| VFV.TO | DS-18b | Coverage chips are CURRENT truth | 2026-11-14 | a re-test | UNVERIFIED | INFO | a hand-kept file dated by its own test run; not re-measured here (Alpaca "works" was measured 2026-11-21) |
| VFV.TO | DS-21 | Hit rate (24h) is computed from cache_stats events | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.5%Hit rate (24h) | - | UNVERIFIED | INFO | not traced |
| VFV.TO | DS-2b | Exchange, currency and fund type are TRUE (vs the broker) | Toronto / CAD | IBKR contract | UNVERIFIED | INFO | needs the broker contract record; the IBKR truth run covered closes, not these fields |
| VFV.TO | DS-4 | Cache state label | just fetched | cached | UNVERIFIED | INFO | differs only because time passed between the dump and this audit |
| - | DS-22 | Static line: cache lifetime | Prices are cached until the next market close (4pm ET + 30 min). Fundamentals for 7 days. | rule in cache_manager | PASS |  | no short-lived rows right now; the exceptions still exist in code |
| - | DS-23 | Static line: "Fundamentals for 7 days" | Fundamentals for 7 days | FUNDAMENTALS_TTL_DAYS = 7 | PASS |  |  |
| AAPL | DS-1 | Symbol | AAPL | AAPL | PASS |  |  |
| AAPL | DS-10 | Last-audit line equals the reference file entry | Last audit (2026-11-24): C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) | C6: yfinance: 501 bars from 2024-11-25; starts 5 days after alpaca (2024-11-20, 504 bars); starts 5 days after twelvedata (2024-11-20, 504 bars) | PASS |  |  |
| AAPL | DS-11 | Fundamentals line | Fundamentals from Finnhub, 4 days old. | Fundamentals from Finnhub | PASS |  |  |
| AAPL | DS-12 | Price chain order | alpaca → twelvedata → yfinance → tradier | alpaca → twelvedata → yfinance → tradier | PASS |  | orchestrator._ohlcv_chain built fresh |
| AAPL | DS-13 | Fundamentals chain order | finnhub → alphavantage → yfinance | finnhub → alphavantage → yfinance | PASS |  |  |
| AAPL | DS-14-alpaca | Alpaca health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| AAPL | DS-14-alphavantage | Alpha Vantage health word = circuit breaker state | circuit open | circuit open | PASS |  | breaker table state: open |
| AAPL | DS-14-finnhub | Finnhub health word = circuit breaker state | degraded | degraded | PASS |  | breaker table state: half_open |
| AAPL | DS-14-tradier | Tradier health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| AAPL | DS-14-twelvedata | Twelve Data health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| AAPL | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| AAPL | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| AAPL | DS-16-alphavantage | Alpha Vantage calls left today (within 10: the count moves) | 21 | 21 | PASS |  |  |
| AAPL | DS-16-tradier | Tradier calls left today (within 10: the count moves) | None | none shown | PASS |  |  |
| AAPL | DS-16-twelvedata | Twelve Data calls left today (within 10: the count moves) | 725 | 725 | PASS |  |  |
| AAPL | DS-17-alpaca | Alpaca coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| AAPL | DS-17-tradier | Tradier coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| AAPL | DS-17-twelvedata | Twelve Data coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| AAPL | DS-17-yfinance | Yahoo (yfinance) coverage chips = provider_coverage.json | all present | US: works, Toronto: works, Cboe Canada: partial | PASS |  |  |
| AAPL | DS-18 | Coverage line: tested date and report | Each source is tried in order. Markets covered are as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md). | as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md) | PASS |  |  |
| AAPL | DS-19 | Disabled line | Disabled: Stooq (not in any chain). | Disabled: Stooq (not in any chain). | PASS |  |  |
| AAPL | DS-2 | Exchange / currency / class equal what /api/stock sent | NasdaqGS / USD / Stock | NasdaqGS / USD / Stock | PASS |  |  |
| AAPL | DS-20 | OHLCV entries = rows in ohlcv_cache | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.8%Hit rate (24h) | 161 | PASS |  | the cache moves while the audit runs; a small difference is expected |
| AAPL | DS-3 | "Data from" = the source stored on the cache row | Alpaca | Alpaca | PASS |  | read straight from ohlcv_cache.source |
| AAPL | DS-4 | Cache state label | cached | cached | PASS |  |  |
| AAPL | DS-4b | "just fetched" says a fetch happened | cached | a recorded fetch | PASS |  | not shown for this ticker; the rule still guesses |
| AAPL | DS-5 | Session source = the server's last-source record | cache | cache | PASS |  | both from the running server's memory (/api/health last_sources); null after a restart |
| AAPL | DS-5b | Session sentence on the page | present | served from cache this session | PASS |  |  |
| AAPL | DS-6 | Verdict pill = verdict of the quality builder run again on the cached bars | PASS | PASS | PASS |  | same builder as the tab (shared on purpose, Day 135); the builder's own maths is graded by the C-checks in audit_data_sources.py, not here |
| AAPL | DS-7 | Header: bars, period and last bar date | Checked 504 bars (period 2y) · cached Nov 26, 6:03 PM · last bar 2026-11-25, 2 sessions behind | Checked 504 bars (period 2y) ... last bar 2026-11-25 | PASS |  |  |
| AAPL | DS-8 | Rows listed = the checks at WARN or FAIL | 0 rows | 0 (none) | PASS |  |  |
| AAPL | DS-9 | "All N checks passed" | All 4 checks passed. | All 4 checks passed. | PASS |  |  |
| SOXL.NE | DS-1 | Symbol | SOXL.NE | SOXL.NE | PASS |  |  |
| SOXL.NE | DS-10 | Last-audit line equals the reference file entry | Last audit (2026-11-24): C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 5 | C4: yfinance: flat zero-volume 100%; bad OHLC rows 0; zero-volume in last 5: 5 | PASS |  |  |
| SOXL.NE | DS-11 | Fundamentals line for a fund | No fundamentals for a fund. | No fundamentals for a fund. | PASS |  |  |
| SOXL.NE | DS-12 | Price chain order | alpaca → twelvedata → yfinance → tradier | alpaca → twelvedata → yfinance → tradier | PASS |  | orchestrator._ohlcv_chain built fresh |
| SOXL.NE | DS-13 | Fundamentals chain order | finnhub → alphavantage → yfinance | finnhub → alphavantage → yfinance | PASS |  |  |
| SOXL.NE | DS-14-alpaca | Alpaca health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| SOXL.NE | DS-14-alphavantage | Alpha Vantage health word = circuit breaker state | circuit open | circuit open | PASS |  | breaker table state: open |
| SOXL.NE | DS-14-finnhub | Finnhub health word = circuit breaker state | degraded | degraded | PASS |  | breaker table state: half_open |
| SOXL.NE | DS-14-tradier | Tradier health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| SOXL.NE | DS-14-twelvedata | Twelve Data health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| SOXL.NE | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| SOXL.NE | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| SOXL.NE | DS-16-alphavantage | Alpha Vantage calls left today (within 10: the count moves) | 21 | 21 | PASS |  |  |
| SOXL.NE | DS-16-tradier | Tradier calls left today (within 10: the count moves) | None | none shown | PASS |  |  |
| SOXL.NE | DS-16-twelvedata | Twelve Data calls left today (within 10: the count moves) | 725 | 725 | PASS |  |  |
| SOXL.NE | DS-17-alpaca | Alpaca coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| SOXL.NE | DS-17-tradier | Tradier coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| SOXL.NE | DS-17-twelvedata | Twelve Data coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| SOXL.NE | DS-17-yfinance | Yahoo (yfinance) coverage chips = provider_coverage.json | all present | US: works, Toronto: works, Cboe Canada: partial | PASS |  |  |
| SOXL.NE | DS-18 | Coverage line: tested date and report | Each source is tried in order. Markets covered are as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md). | as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md) | PASS |  |  |
| SOXL.NE | DS-19 | Disabled line | Disabled: Stooq (not in any chain). | Disabled: Stooq (not in any chain). | PASS |  |  |
| SOXL.NE | DS-2 | Exchange / currency / class equal what /api/stock sent | Cboe CA / CAD / Leveraged ETF | Cboe CA / CAD / Leveraged ETF | PASS |  |  |
| SOXL.NE | DS-20 | OHLCV entries = rows in ohlcv_cache | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.6%Hit rate (24h) | 161 | PASS |  | the cache moves while the audit runs; a small difference is expected |
| SOXL.NE | DS-3 | "Data from" = the source stored on the cache row | Yahoo (yfinance) | Yahoo (yfinance) | PASS |  | read straight from ohlcv_cache.source |
| SOXL.NE | DS-4 | Cache state label | cached | cached | PASS |  |  |
| SOXL.NE | DS-4b | "just fetched" says a fetch happened | cached | a recorded fetch | PASS |  | not shown for this ticker; the rule still guesses |
| SOXL.NE | DS-5 | Session source = the server's last-source record | cache | cache | PASS |  | both from the running server's memory (/api/health last_sources); null after a restart |
| SOXL.NE | DS-5b | Session sentence on the page | present | served from cache this session | PASS |  |  |
| SOXL.NE | DS-6 | Verdict pill = verdict of the quality builder run again on the cached bars | FAIL | FAIL | PASS |  | same builder as the tab (shared on purpose, Day 135); the builder's own maths is graded by the C-checks in audit_data_sources.py, not here |
| SOXL.NE | DS-7 | Header: bars, period and last bar date | Checked 320 bars (period 2y) · cached Nov 26, 6:01 PM · last bar 2026-11-26, 1 session behind | Checked 320 bars (period 2y) ... last bar 2026-11-26 | PASS |  |  |
| SOXL.NE | DS-8 | Rows listed = the checks at WARN or FAIL | 2 rows | 2 (integrity, jumps) | PASS |  |  |
| VFV.TO | DS-1 | Symbol | VFV.TO | VFV.TO | PASS |  |  |
| VFV.TO | DS-11 | Fundamentals line for a fund | No fundamentals for a fund. | No fundamentals for a fund. | PASS |  |  |
| VFV.TO | DS-12 | Price chain order | alpaca → twelvedata → yfinance → tradier | alpaca → twelvedata → yfinance → tradier | PASS |  | orchestrator._ohlcv_chain built fresh |
| VFV.TO | DS-13 | Fundamentals chain order | finnhub → alphavantage → yfinance | finnhub → alphavantage → yfinance | PASS |  |  |
| VFV.TO | DS-14-alpaca | Alpaca health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| VFV.TO | DS-14-alphavantage | Alpha Vantage health word = circuit breaker state | circuit open | circuit open | PASS |  | breaker table state: open |
| VFV.TO | DS-14-finnhub | Finnhub health word = circuit breaker state | degraded | degraded | PASS |  | breaker table state: half_open |
| VFV.TO | DS-14-tradier | Tradier health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| VFV.TO | DS-14-twelvedata | Twelve Data health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| VFV.TO | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| VFV.TO | DS-14-yfinance | Yahoo (yfinance) health word = circuit breaker state | ok | ok | PASS |  | breaker table state: closed |
| VFV.TO | DS-16-alphavantage | Alpha Vantage calls left today (within 10: the count moves) | 21 | 21 | PASS |  |  |
| VFV.TO | DS-16-tradier | Tradier calls left today (within 10: the count moves) | None | none shown | PASS |  |  |
| VFV.TO | DS-16-twelvedata | Twelve Data calls left today (within 10: the count moves) | 725 | 725 | PASS |  |  |
| VFV.TO | DS-17-alpaca | Alpaca coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| VFV.TO | DS-17-tradier | Tradier coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| VFV.TO | DS-17-twelvedata | Twelve Data coverage chips = provider_coverage.json | all present | US: works, Toronto: no, Cboe Canada: no | PASS |  |  |
| VFV.TO | DS-17-yfinance | Yahoo (yfinance) coverage chips = provider_coverage.json | all present | US: works, Toronto: works, Cboe Canada: partial | PASS |  |  |
| VFV.TO | DS-18 | Coverage line: tested date and report | Each source is tried in order. Markets covered are as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md). | as tested on 2026-11-14 (docs/test/DataSources_20261114/REPORT_vs_IBKR.md) | PASS |  |  |
| VFV.TO | DS-19 | Disabled line | Disabled: Stooq (not in any chain). | Disabled: Stooq (not in any chain). | PASS |  |  |
| VFV.TO | DS-2 | Exchange / currency / class equal what /api/stock sent | Toronto / CAD / ETF | Toronto / CAD / ETF | PASS |  |  |
| VFV.TO | DS-20 | OHLCV entries = rows in ohlcv_cache | 161OHLCV entries / 123Fundamentals entries / 50572 KBDatabase size / 96.5%Hit rate (24h) | 161 | PASS |  | the cache moves while the audit runs; a small difference is expected |
| VFV.TO | DS-3 | "Data from" = the source stored on the cache row | Yahoo (yfinance) | Yahoo (yfinance) | PASS |  | read straight from ohlcv_cache.source |
| VFV.TO | DS-5 | Session source = the server's last-source record | cache | cache | PASS |  | both from the running server's memory (/api/health last_sources); null after a restart |
| VFV.TO | DS-5b | Session sentence on the page | present | served from cache this session | PASS |  |  |
| VFV.TO | DS-6 | Verdict pill = verdict of the quality builder run again on the cached bars | PASS | PASS | PASS |  | same builder as the tab (shared on purpose, Day 135); the builder's own maths is graded by the C-checks in audit_data_sources.py, not here |
| VFV.TO | DS-7 | Header: bars, period and last bar date | Checked 503 bars (period 2y) · cached Nov 27, 6:52 AM · last bar 2026-11-26, 1 session behind | Checked 503 bars (period 2y) ... last bar 2026-11-26 | PASS |  |  |
| VFV.TO | DS-8 | Rows listed = the checks at WARN or FAIL | 0 rows | 0 (none) | PASS |  |  |
| VFV.TO | DS-9 | "All N checks passed" | All 4 checks passed. | All 4 checks passed. | PASS |  |  |
