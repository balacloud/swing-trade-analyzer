# Perplexity Handoff — OptionsIQ (Updated March 5, 2026)

## Current Objective
Move from broad-chain retrieval to deterministic, low-latency chain selection while preserving analysis quality and explicit fallback semantics.

## Current Runtime
- Backend: `http://localhost:5051`
- Frontend: `http://localhost:3050`
- TWS/Gateway socket: `127.0.0.1:4001`
- Base IB client ID: `101` (auto-scan fallback IDs enabled)

## Implemented Since Prior Handoff
1. `chain_profile` support (`smart|full`) across provider and API.
2. Smart profile behavior:
   - exactly one expiry
   - nearest expiry with `dte >= min_dte` (default `14`)
   - targeted strike/contract scope
3. Profile-aware cache keys (`ticker/profile/direction`).
4. Profile-specific timeout controls (`smart` vs `full`).
5. Robust NaN normalization in IB provider to prevent hidden parsing failures.
6. Strategy ranking numeric hardening to prevent 500 when greeks are missing.
7. Partial fallback now respects profile constraints (smart fallback is compact and one-expiry).

## Verified State
- `GET /api/health` reports connectivity reliably.
- Analyze and chain endpoints accept `chain_profile` and `min_dte`.
- Smart profile behavior verified in direct provider diagnostics:
  - single expiry returned
  - min DTE respected
- Under live IB latency pressure, endpoint can still degrade to `ibkr_partial`, but now with profile-consistent fallback shape.

## Current Pain Point
- In long-running app flow, `ib.reqTickers(...)` can still exceed timeout budget even with smart scope.
- Result: frequent `ibkr_partial` despite successful IB connection.

## What We Need from Perplexity Next
Provide surgical recommendations for this exact architecture:

1. **IB data retrieval pattern optimization**
- How to reduce `reqTickers` latency in persistent Flask runtime with `ib_insync`.
- Whether staged subscription models (contract pre-qualify + selective tick requests) can outperform current batch call.

2. **Field reliability contract**
- Which fields should be mandatory for ranking/gates when `ibkr_partial`.
- How to score confidence when bid/ask/OI are absent but greeks are partially available.

3. **Adaptive timeout/caching strategy**
- Per-symbol dynamic timeout from observed response history.
- Better stale-while-revalidate policy under high-latency market data farms.

4. **Testing matrix**
- Deterministic pass/fail matrix for:
  - smart/full live chain
  - smart/full cached chain
  - smart/full partial chain
  - mock fallback

## Relevant Files
- `backend/app.py`
- `backend/ibkr_provider.py`
- `backend/strategy_ranker.py`
- `backend/mock_provider.py`
- `frontend/src/App.jsx`
- `frontend/src/hooks/useOptionsData.js`

## Current `.env` (active shape)
```env
IBKR_HOST=127.0.0.1
IBKR_PORT=4001
IBKR_CLIENT_ID=101
IBKR_MARKET_DATA_TYPE=1
CHAIN_PROFILE_DEFAULT=smart
IBKR_MIN_DTE=14
ANALYZE_TIMEOUT_SEC=18
ANALYZE_TIMEOUT_SMART_SEC=24
ANALYZE_TIMEOUT_FULL_SEC=28
IBKR_SMART_MAX_EXPIRIES=1
IBKR_SMART_MAX_STRIKES=4
IBKR_SMART_MAX_CONTRACTS=12
IBKR_SMART_STRIKE_WINDOW_PCT=0.10
IBKR_FULL_MAX_EXPIRIES=2
IBKR_FULL_MAX_STRIKES=8
IBKR_FULL_MAX_CONTRACTS=40
IBKR_FULL_STRIKE_WINDOW_PCT=0.12
IBKR_BATCH_SIZE=20
CHAIN_CACHE_TTL_SEC=120
IB_CHAIN_CB_FAILURE_THRESHOLD=2
IB_CHAIN_CB_COOLDOWN_SEC=45
IB_CHAIN_RETRY_ATTEMPTS=1
IB_CHAIN_RETRY_BACKOFF_SEC=0.6
ANALYZE_CACHE_FIRST=1
```

## Additional Context
- TWS setting still recommended for this workflow: uncheck `Download open orders on connection`.
- API client connected status in TWS/Gateway is session-lifecycle dependent.
