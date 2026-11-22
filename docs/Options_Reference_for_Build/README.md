# OptionsIQ

Standalone options analysis module built with Flask + React.

- Backend: `http://localhost:5051`
- Frontend: `http://localhost:3050`
- IB integration: `ib_insync` (TWS/Gateway local socket)

## What This App Does
- Pulls options/underlying data (IB primary, fallback paths available)
- Runs gate logic for directional options decisions
- Ranks top 3 strategies
- Builds scenario-based P&L table
- Tracks paper trades
- Supports manual swing inputs (swing-analyzer integration optional)

## Intelligent Chain Profiles
- `smart` (default):
  - 1 expiry only
  - nearest expiry at/above `min_dte` (default `14`)
  - targeted strikes/contracts for low-latency analysis
- `full`:
  - broader expiry/strike/contract scope

Use in analyze payload:
```json
{
  "ticker": "AME",
  "direction": "buy_call",
  "chain_profile": "smart",
  "min_dte": 14
}
```

## Tech Stack
- Python 3
- Flask + flask-cors
- ib_insync
- SQLite
- React 18 (`react-scripts`)

## Project Structure
```text
Options_Engine_Codex/
├── backend/
│   ├── app.py
│   ├── ibkr_provider.py
│   ├── mock_provider.py
│   ├── iv_store.py
│   ├── gate_engine.py
│   ├── strategy_ranker.py
│   ├── pnl_calculator.py
│   ├── data/iv_history.db
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── package.json
│   ├── public/index.html
│   └── src/
│       ├── App.jsx
│       ├── hooks/useOptionsData.js
│       ├── components/*.jsx
│       ├── index.js
│       └── index.css
├── CHANGELOG.md
├── PROJECT_CONTEXT.md
├── SESSION_TRACKER.md
└── Docs/
```

## Prerequisites
- Python 3.9+
- Node.js + npm
- TWS or IB Gateway running locally

## Backend Setup
```bash
cd /Users/balajik/projects/Options_Engine_Codex/backend
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Frontend Setup
```bash
cd /Users/balajik/projects/Options_Engine_Codex/frontend
npm install
```

## Run
```bash
# Terminal 1
cd /Users/balajik/projects/Options_Engine_Codex/backend
python3 app.py

# Terminal 2
cd /Users/balajik/projects/Options_Engine_Codex/frontend
npm start
```

## Environment Configuration
Edit `backend/.env`.

Current recommended values:
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
WARM_TICKERS=AME
ACCOUNT_SIZE=24813
RISK_PCT=0.01
PLANNED_HOLD_DAYS=7
SWING_ANALYZER_URL=http://localhost:5001
```

## API Quick Checks
```bash
curl http://localhost:5051/api/health

curl -X POST http://localhost:5051/api/options/analyze \
  -H "Content-Type: application/json" \
  -d '{"ticker":"AME","direction":"buy_call","chain_profile":"smart","min_dte":14,
       "vcp_pivot":242.05,"last_close":234.35,"vcp_confidence":70,"adx":40.2,
       "swing_signal":"BUY","stop_loss":192.93,"target1":254.62,"target2":278.36,
       "spy_above_200sma":true,"spy_5day_return":0.008,"earnings_days_away":45}'

curl "http://localhost:5051/api/options/chain/AME?chain_profile=smart&direction=buy_call&min_dte=14&target_price=234.35"
```

## Data Source Modes
- `IB Live`: live chain path succeeded
- `IB Cache`: serving cached IB chain
- `IB Partial`: live IB available but chain retrieval degraded/timeout
- `Mock Fallback`: full mock mode

## Known Issues
- IB chain retrieval can still degrade under entitlement/latency constraints.
- Even with smart profile, long IB response times may trigger `ibkr_partial`.

## Troubleshooting
- If `pip` is missing, use `python3 -m pip ...`.
- If frontend shows fetch failures, verify backend is running on `5051`.
- If TWS shows API client disconnected, confirm backend process is running and using the configured socket/ID.

## Documentation
- Project context: `PROJECT_CONTEXT.md`
- Session tracking: `SESSION_TRACKER.md`
- Change log: `CHANGELOG.md`
- Perplexity handoff: `Docs/PERPLEXITY_HANDOFF_March04.md`
