# OptionsIQ Project Context

## Project Identity
- Name: `OptionsIQ`
- Purpose: standalone options analysis module for personal use
- Backend: Flask + Python
- Frontend: React (`react-scripts`)
- Primary data source: Interactive Brokers via `ib_insync`
- Fallbacks: profile-aware partial fallback + mock fallback

## Runtime Topology
- Backend URL: `http://localhost:5051`
- Frontend URL: `http://localhost:3050`
- TWS/Gateway API socket: `127.0.0.1:4001`
- Preferred IB client ID base: `101` (auto-scan fallback IDs enabled)

## Document Update Order
Use this order at end of implementation sessions:
1. `CHANGELOG.md`
2. `SESSION_TRACKER.md`
3. `PROJECT_CONTEXT.md`
4. `README.md`
5. `Docs/PERPLEXITY_HANDOFF_March04.md`

## Current Architecture Highlights
- Intelligent chain fetch profiles:
  - `smart` (default): one expiry at/above min DTE, targeted strikes/contracts.
  - `full`: broader expiries/strikes/contracts.
- Cache key scope includes ticker/profile/direction.
- Circuit-breaker + retry + cache-first behavior for chain retrieval.
- API quality semantics:
  - `full`, `degraded`, `cached`, `partial`, `mock`
- Frontend shows data-source/quality status and does not crash on fetch failures.

## Current Code Layout
- Backend core:
  - `backend/app.py`
  - `backend/ibkr_provider.py`
  - `backend/mock_provider.py`
  - `backend/iv_store.py`
  - `backend/gate_engine.py`
  - `backend/strategy_ranker.py`
  - `backend/pnl_calculator.py`
- Frontend core:
  - `frontend/src/App.jsx`
  - `frontend/src/hooks/useOptionsData.js`
  - `frontend/src/components/*`
  - `frontend/src/index.css`

## Data / Storage
- SQLite DB: `backend/data/iv_history.db`
- Stores IV history, OHLCV history, paper trades

## Key API Endpoints
- `GET /api/health`
- `POST /api/options/analyze`
- `GET /api/options/chain/<ticker>`
- `GET /api/options/ivr/<ticker>`
- `POST /api/options/paper-trade`
- `GET /api/options/paper-trades`
- `POST /api/options/seed-iv/<ticker>`
- `GET /api/integrate/ping`
- `GET /api/integrate/schema`
- `POST /api/integrate/status`

## Environment Settings (active)
From `backend/.env`:
- `IBKR_HOST=127.0.0.1`
- `IBKR_PORT=4001`
- `IBKR_CLIENT_ID=101`
- `IBKR_MARKET_DATA_TYPE=1`
- `CHAIN_PROFILE_DEFAULT=smart`
- `IBKR_MIN_DTE=14`
- `ANALYZE_TIMEOUT_SEC=18`
- `ANALYZE_TIMEOUT_SMART_SEC=24`
- `ANALYZE_TIMEOUT_FULL_SEC=28`
- `IBKR_SMART_MAX_EXPIRIES=1`
- `IBKR_SMART_MAX_STRIKES=4`
- `IBKR_SMART_MAX_CONTRACTS=12`
- `IBKR_SMART_STRIKE_WINDOW_PCT=0.10`
- `IBKR_FULL_MAX_EXPIRIES=2`
- `IBKR_FULL_MAX_STRIKES=8`
- `IBKR_FULL_MAX_CONTRACTS=40`
- `IBKR_FULL_STRIKE_WINDOW_PCT=0.12`
- `IBKR_BATCH_SIZE=20`
- `CHAIN_CACHE_TTL_SEC=120`
- `IB_CHAIN_CB_FAILURE_THRESHOLD=2`
- `IB_CHAIN_CB_COOLDOWN_SEC=45`
- `IB_CHAIN_RETRY_ATTEMPTS=1`
- `ANALYZE_CACHE_FIRST=1`

## Current Behavior Snapshot
- Health endpoint reports IB status correctly (`ibkr_connected` true/false).
- Analyze now supports payload controls:
  - `chain_profile` (`smart|full`)
  - `min_dte`
- Smart fallback behavior is compact and expiry-constrained even when IB live chain times out.
- For AME test payload, Gate 8 fail condition remains intact.

## Known Constraints
- IB option chain response latency (`reqTickers`) can still force partial mode under timeout.
- Option quote/OI field completeness depends on IB market data entitlements and farm state.
- TWS “API Client connected” remains session-lifecycle dependent.

## Operational Notes
- Keep backend bound to `5051` to avoid conflict with other local engines.
- Keep frontend on `3050`.
- For data-only workflows, TWS setting `Download open orders on connection` should remain unchecked.
