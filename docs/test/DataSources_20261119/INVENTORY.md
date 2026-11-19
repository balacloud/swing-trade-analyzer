# Fetched vs Computed inventory — Analyze page (Day 127, Round 2 step 1)

Status: DRAFT. Read from `backend/backend.py`, `breakout_routes.py`, `live_quote.py` (code read, nothing run yet).
Scope so far: the Analyze page endpoints only. Still to do: Scan, Sectors, Context, Value tabs and the ~17 direct-call bypasses outside backend.py.

FETCHED = comes from a provider. COMPUTED = built by us from daily bars.

## The one base input: daily bars
Every endpoint below asks the provider chain for its OWN copy of the 2-year daily bars (`dp.get_ohlcv(ticker, '2y')`):
Twelve Data -> Yahoo -> Tradier -> stale cache. Each also has a direct-yfinance fallback that skips the chain.
Endpoints with their own copy: `/api/stock`, `/api/sr`, `/api/patterns`, `/api/breakout`, `live_quote` (history leg), SPY/QQQ (`_index_history`).
Risk: two cards on one page can come from different providers (seen: 25.025 vs 25.03). Basis differs by provider
(Twelve Data dividend-adjusted; Tradier split-only).

## /api/stock
| Field | Kind | Source |
|---|---|---|
| currentPrice (last completed close), priceHistory, oldestDate/newestDate | COMPUTED/bars | chain above, forming bar dropped |
| price52wAgo, price13wAgo | COMPUTED | bars |
| fiftyTwoWeekHigh/Low | COMPUTED | bars (Yahoo only if too short) |
| name, sector, industry, quoteType, exchange, currency | FETCHED | Yahoo `info` via `dp.get_stock_info` (direct yfinance fallback) |
| avgVolume, avgVolume10d | FETCHED | Yahoo `info` — CANDIDATE to compute from bars (Liquidity row = Yahoo avgVolume x price) |
| instrumentClass | COMPUTED | from `info` fields |

## /api/sr (levels, indicators)
| Field | Kind | Source |
|---|---|---|
| S/R zones, ATR, ADX, OBV, RSI, market structure, RVOL, candle | COMPUTED | bars (today's partial bar kept for currentPrice/RSI/RVOL on purpose) |
| rsi_4h | FETCHED | intraday 1h bars (Twelve Data -> Yahoo), resampled. Spends a call on every `/api/sr`; Known Issues says no frontend consumer -> removal candidate |

## Other Analyze endpoints
| Endpoint | Kind | Source |
|---|---|---|
| `/api/quote/<t>` live price | FETCHED | Tradier first (US), Yahoo, Finnhub; Canada Yahoo only |
| `/api/fundamentals/<t>` | FETCHED | Finnhub -> Alpha Vantage -> Yahoo, field-level merge, units normalised in `field_maps.py` |
| `/api/earnings/<t>` | FETCHED | `dp.get_earnings`, then direct Yahoo calendar / earnings_dates / info (bypass) |
| `/api/market/vix` | FETCHED | `dp.get_quote('^VIX')`, then direct Yahoo (bypass) |
| `/api/market/spy`, `/api/market/index/<QQQ>` | FETCHED bars, trend COMPUTED | chain, then direct Yahoo |
| `/api/patterns`, `/api/breakout` | COMPUTED | their own copy of bars |
| `/api/mr/signal` | COMPUTED | own 1-year Yahoo frame (`auto_adjust=True`) — NOT the chain |

## Findings from this step
1. Single-source goal not met: 5+ separate fetches of the same bars per page load. A mismatch between cards is possible by design.
2. `/api/mr/signal` and `/api/mr/scan` read Yahoo directly, so the MR card can use different prices than every other card.
3. Yahoo `avgVolume` feeds the Liquidity row; the app already computes a 50-day average volume from bars. Decide: compute it.
4. `rsi_4h` costs an intraday call per `/api/sr` with no known consumer.
5. Fundamentals, earnings date, VIX, name/sector are FETCHED only; they cannot be recomputed, only cross-checked.

## Not yet verified
This is a code read. Per-ticker provider counts (which source actually served each of the 117) are step 2.2 and not done.
