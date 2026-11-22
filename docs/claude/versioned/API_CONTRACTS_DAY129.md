# API Contracts — Day 129

> Changes since `API_CONTRACTS_DAY128.md`. Backend v2.57 → v2.58. Plans: `docs/claude/design/TRADIER_FALLBACK_RULE_PLAN_DAY129.md`, `ALPACA_PROVIDER_PLAN_DAY129.md`.

## Changed — `GET /api/provenance/<ticker>` (Data Sources tab quality block)
- `quality.checks` gains a **`source`** row, present only when the served frame came from **Tradier**: level **WARN** ("Served by Tradier, the backup source. Prices are not adjusted for dividends...") or **FAIL** when the ticker is a leveraged fund Tradier must never serve (`providers/fallback_policy.tradier_blocked`). Frames from any other source have no `source` row.
- `data_quality.quality_level(facts, tolerant=True, source=None, blocked=False)`: two new optional arguments (old calls unchanged). The route passes `source=_meta['source']` and `blocked=tradier_blocked(ticker)`.
- Frontend label: `CHECK_LABEL.source = 'Data source'`; `DISPLAY.alpaca = 'Alpaca'` (`frontend/src/utils/dataSourcesView.js`).

## Changed — provider status (`orchestrator.get_provider_status`, shown on the Data Sources tab / `/api/health`-style status)
- New **`alpaca`** entry, role `primary` (OHLCV, US only). Twelve Data's role is now `fallback (OHLCV), primary (intraday)`.

## Changed — price-history source order (all routes that read history through the orchestrator)
- US tickers: **Alpaca -> Twelve Data -> Yahoo -> Tradier** (was Twelve Data -> Yahoo -> Tradier). Canada (`.TO .V .NE .NEO .CN`) and `^` indexes: unchanged (Yahoo). Intraday chain (Twelve Data then Yahoo) and quote chain (Yahoo, Finnhub, Tradier) unchanged.
- Leveraged funds in `NO_TRADIER` are never served by Tradier (a 60-second failure memo applies when every other source fails; a stale Tradier copy is refused).
- Alpaca bars: `feed=sip`, `adjustment=all` (dividend and split adjusted), index normalized to midnight New York dates; volume is x0.85-1.01 of Twelve Data's.

## Changed — cache expiry (internal, every source)
- `cache_manager.set_cached_ohlcv(..., source='yfinance', now=None)`: a frame whose newest bar is today (New York) and was fetched before 16:30 ET expires at 16:30 ET.

## Changed — provider error contract (internal)
- Alpaca: 401/plain 403 `AuthenticationError` (+failure); 403 "subscription/permit" and any other 400 or 422 loud `ProviderError` (no failure); 400 "invalid symbol" and empty bars `DataNotFoundError`; 429 `RateLimitError` (+failure); 5xx/timeout `ProviderUnavailableError` (+failure); under 10 bars `InsufficientDataError`.
- Twelve Data: HTTP 404 `DataNotFoundError` (no failure); Canadian and `^` symbols make no call and take no limiter token; error text never contains the request URL or key.
- Rate limiter: `PROVIDER_LIMITS['alpaca'] = {'rate_per_minute': 150, 'daily_limit': 0}`.

## Changed — audit tooling (not an API)
- `backtest/audit_data_sources.py`: Alpaca is a fetch source for US tickers; C8 reads `/api/provenance` `quality.checks`. `backtest/audit_vs_ibkr.py` source lists include `alpaca`. `backend/reference/provider_coverage.json` has an `alpaca` entry.

Nothing else changed shape.
