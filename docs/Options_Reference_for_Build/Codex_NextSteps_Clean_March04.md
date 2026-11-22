# OptionsIQ — Clean Next Steps Handoff (March 4, 2026)

## 1. Current Build Status
- Backend + frontend are implemented and running standalone.
- Ports:
  - Backend: `http://localhost:5051`
  - Frontend: `http://localhost:3050`
- Swing Trade Analyzer integration is optional and **not required** for core app usage.

## 2. What Is Working
- Flask API routes respond.
- React UI loads and can call backend.
- IBKR connectivity at session level works.
- Mock fallback path is stable (UI does not hang forever).

## 3. Verified Test Results (Executed)
### Health
Command:
```bash
curl http://localhost:5051/api/health
```
Observed:
```json
{"ibkr_connected":true,"mock_mode":false,"status":"ok","version":"2.0"}
```

### Analyze
Command:
```bash
curl -m 25 -X POST http://localhost:5051/api/options/analyze \
  -H "Content-Type: application/json" \
  -d '{"ticker":"AME","direction":"buy_call","vcp_pivot":242.05,"last_close":234.35,
       "vcp_confidence":70,"adx":40.2,"swing_signal":"BUY","stop_loss":192.93,
       "target1":254.62,"target2":278.36,"spy_above_200sma":true,
       "spy_5day_return":0.008,"earnings_days_away":45}'
```
Observed outcome:
- Response returns, but with fallback:
  - `data_source: "mock"`
  - `ibkr_connected: false` in analyze payload
- Backend log shows:
  - `IB chain request timed out after 12.0s`

## 4. Root Issue (Now Narrowed)
Not a full connectivity problem.

It is specifically **options chain retrieval under IBKR timing/entitlement constraints**:
- Health endpoint can connect to IB.
- Analyze path times out waiting for options chain/quotes and falls back to mock.
- Logs also show option market-data entitlement warnings/errors for AME options (`10089/10091` / delayed warnings).

## 5. Code Changes Already Applied
- Backend moved to port `5051`.
- `.env` is loaded reliably at app startup.
- IB provider init/retry/logging improved.
- Async patching enabled for ib_insync runtime stability.
- Analyze hard timeout added to prevent UI freeze.
- Chain request load reduced (caps on expiries/strikes/contracts).
- Read-only connect mode enabled.
- Delayed market data mode support (`IBKR_MARKET_DATA_TYPE`).

## 6. Current Gaps to Resolve
1. Keep `analyze` in `ibkr` mode (not mock) when delayed/partial options data is available.
2. Reduce first-call latency to target `< 5s` typical.
3. Handle entitlement-limited responses without treating them as hard provider failure.

## 7. Exact Ask for Perplexity (Use This)
Please provide a **delta plan** from current code (not a full rewrite) to solve this specific issue:

- Environment:
  - TWS API socket on `4001`
  - Backend `5051`, frontend `3050`
  - `ib_insync` already installed and IB session connects successfully.
- Problem:
  - `/api/health` is connected.
  - `/api/options/analyze` often returns mock due IB chain timeout or entitlement-limited option data.
- Need:
  1. A robust IB chain fetch strategy that degrades gracefully with delayed/partial fields.
  2. Keep `data_source="ibkr"` when core fields are present, even if some greeks/OI are missing.
  3. Define strict per-step timeout budget and fallback hierarchy (IB partial -> yfinance augment -> mock last).
  4. Caching plan for chain snapshots to avoid repeated expensive calls.
  5. Minimal patch set (specific functions/files) compatible with existing Flask/React code.

Also provide test matrix and pass criteria for:
- health connected,
- analyze live/partial,
- analyze fallback,
- frontend responsiveness under slow IB.

## 8. Recommended Immediate Runtime Config
Use/verify in `backend/.env`:
```env
IBKR_HOST=127.0.0.1
IBKR_PORT=4001
IBKR_CLIENT_ID=101
IBKR_MARKET_DATA_TYPE=3
ANALYZE_TIMEOUT_SEC=12
IBKR_MAX_EXPIRIES=2
IBKR_MAX_STRIKES_PER_EXPIRY=8
IBKR_MAX_CONTRACTS=32
IBKR_BATCH_SIZE=20
```

## 9. Restart Commands
```bash
cd /Users/balajik/projects/Options_Engine_Codex/backend
lsof -ti :5051 | xargs -n 1 kill -9
python3 app.py
```

```bash
cd /Users/balajik/projects/Options_Engine_Codex/frontend
npm start
```
