
╔══════════════════════════════════════════════════════════════════════════════╗
║          CODEX BUILD PROMPT — OptionsIQ v2.0 Independent Module             ║
║          Peer-reviewed by Grok · Gemini · ChatGPT Deep Research             ║
╚══════════════════════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 0 — BUILD MANDATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Build a fully independent Python/Flask + React options analysis module called
OptionsIQ. It must run standalone (localhost:5050 backend, localhost:3050
frontend) with zero dependency on any external app. Later it will be connected
to an existing swing trade analyzer via a clean REST handshake. Build with
that integration seam in mind from day one.

Data source: Interactive Brokers API via ib_insync library (TWS/IB Gateway
socket). Fallback: static mock data when IB Gateway is not running (for UI
development and testing).

This is a PERSONAL USE tool. Non-commercial. One user. No auth layer needed.
Build for correctness and clarity over scale.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — PROJECT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

optionsiq/
├── backend/
│   ├── app.py                    # Flask app, all routes
│   ├── ibkr_provider.py          # IBKR ib_insync data layer
│   ├── mock_provider.py          # Static mock data (IB Gateway offline)
│   ├── gate_engine.py            # All 9 gate calculations (Track A + B)
│   ├── strategy_ranker.py        # Rank top 3 strategies
│   ├── pnl_calculator.py         # P&L table per 1 lot at each scenario
│   ├── iv_store.py               # SQLite store for historical IV (IVR calc)
│   ├── data/
│   │   └── iv_history.db         # SQLite database (auto-created)
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # Root component + ticker input
│   │   ├── components/
│   │   │   ├── Header.jsx        # Ticker info, price, tags
│   │   │   ├── SwingImportStrip.jsx  # Auto-import bar OR manual input
│   │   │   ├── DirectionSelector.jsx # 4 cards: Buy Call/Sell Put/Sell Call/Buy Put
│   │   │   ├── MasterVerdict.jsx     # Score bar, color, reason
│   │   │   ├── GatesGrid.jsx         # 9 gate cards
│   │   │   ├── BehavioralChecks.jsx  # 4 behavioral warnings
│   │   │   ├── TopThreeCards.jsx     # Strategy recommendation cards
│   │   │   ├── PnLTable.jsx          # P&L table per 1 lot
│   │   │   └── PaperTradeBanner.jsx  # Paper trade CTA
│   │   ├── hooks/
│   │   │   └── useOptionsData.js     # Data fetching hook
│   │   └── index.css             # Dark theme variables
│   └── package.json
├── start.sh
└── stop.sh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — BACKEND: IBKR PROVIDER (ibkr_provider.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use ib_insync library. Connect to IB Gateway at 127.0.0.1:7497 (paper) or
7496 (live). clientId=10 (avoid collision with other TWS sessions).

CLASS: IBKRProvider

METHOD: get_options_chain(ticker: str) -> dict
  1. reqSecDefOptParams(ticker) → get all expiries + strikes
  2. Filter expiries: return only those between 14 and 60 DTE from today
  3. For each viable expiry, qualify contracts for strikes within 10% of
     current underlying price
  4. reqMktData() with snapshot=True for each contract
  5. Receive ticks: bid, ask, last, delta, gamma, theta, vega, impliedVol,
     optPrice, undPrice, openInterest (tick types 10,11,12,13,14,24,106)
  6. Return structured dict (see SECTION 5 response schema)
  IMPORTANT: Use asyncio event loop properly. Cancel market data after
  snapshot received. Handle timeout (5s per contract).

METHOD: get_historical_iv(ticker: str, days: int = 252) -> list[dict]
  Use reqHistoricalData():
    whatToShow = "OPTION_IMPLIED_VOLATILITY"
    barSizeSetting = "1 day"
    durationStr = f"{days} D"
  Return list of {date: str, iv: float}

METHOD: get_underlying_price(ticker: str) -> float
  reqMktData() on stock contract, return midpoint of bid/ask

METHOD: is_connected() -> bool
  Return self.ib.isConnected()

FALLBACK PATTERN:
  Wrap every method with try/except. If IB Gateway not running, raise
  IBKRNotAvailableError. app.py catches this and calls mock_provider instead.
  Log clearly: "IB Gateway not available — using mock data"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — BACKEND: GATE ENGINE (gate_engine.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

All gate results must return this structure:
{
  "id": str,                # e.g. "ivr", "hv_iv", "theta_burn"
  "name": str,              # Display name
  "status": "pass"|"warn"|"fail",
  "computed_value": str,    # Human-readable computed value
  "threshold": str,         # What it was compared against
  "reason": str,            # Plain English one-liner
  "blocking": bool          # True = hard block, False = warning only
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRACK A GATES — BUY CALL (run when direction == "buy_call")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GATE 1 — IV RANK (ivr)
  ivr_pct = percentile_rank(current_iv, iv_history_last_252_days)
  PASS:  ivr_pct < 30    → "Cheap IV — ideal for buying options"
  WARN:  ivr_pct 30–50   → "Moderate IV — acceptable"
  FAIL:  ivr_pct > 50    → "IV elevated — IV crush risk on entry"
  FALLBACK (< 30 days history): use absolute IV
    IV < 20% → PASS, IV 20–35% → WARN, IV > 35% → FAIL
  blocking: True on FAIL

GATE 2 — HV/IV RATIO (hv_iv)
  hv_20 = std(log_returns_last_20_days) * sqrt(252) * 100
  ratio = current_iv / hv_20
  VCP_EXCEPTION: if hv_20 < 15.0, use absolute check: IV < 25% → PASS
  PASS:  ratio < 1.20    → "Options fairly priced vs recent realized vol"
  WARN:  ratio 1.20–1.30 → "Paying average vol risk premium"
  FAIL:  ratio > 1.30    → "IV significantly overpriced vs HV"
  blocking: True on FAIL

GATE 3 — THETA BURN RATE (theta_burn)
  extrinsic = max(0, premium - max(0, underlying_price - strike))
  theta_burn_7d = abs(theta_per_day * planned_hold_days) / premium * 100
  planned_hold_days = 7 (default, configurable)
  PASS:  theta_burn_7d <= 8%  → "Theta decay manageable over hold period"
  WARN:  theta_burn_7d 8–12%  → "Theta notable — need fast move"
  FAIL:  theta_burn_7d > 12%  → "Theta will erode gains — use longer DTE"
  blocking: True on FAIL

GATE 4 — DTE SELECTION (dte)
  vcp_confidence: float (0–100), adx: float, both passed in from swing input
  if vcp_confidence >= 80 and adx >= 40: recommended_dte = 21
  elif vcp_confidence >= 60: recommended_dte = 45
  else: recommended_dte = None (no trade)
  selected_expiry_dte = days until selected option expiry
  PASS:  recommended_dte is not None and selected_expiry_dte >= recommended_dte - 5
  WARN:  selected_expiry_dte < recommended_dte but >= 14
  FAIL:  vcp_confidence < 60 OR selected_expiry_dte < 14
  blocking: True on FAIL (no trade if vcp_confidence < 60)

GATE 5 — EVENT CALENDAR (events)
  earnings_days_away: int (from swing analyzer or yfinance fallback)
  fomc_days_away: int (hardcoded FOMC calendar 2026)
  PASS:  earnings_days_away > selected_expiry_dte AND fomc_days_away > 10
  WARN:  fomc_days_away 5–10 days away
  FAIL:  earnings within expiry window
  blocking: True if earnings within expiry window

GATE 6 — LIQUIDITY PROXY (liquidity)
  4-part check (no bid/ask fallback if IBKR unavailable):
  Part A: open_interest > 1000
  Part B: daily_volume / open_interest > 0.10
  Part C: premium >= 2.00
  Part D: abs(strike - underlying_price) / underlying_price <= 0.05
  IF IBKR AVAILABLE: also compute
    spread = ask - bid
    spread_pct = spread / ((bid + ask) / 2) * 100
    PASS:  spread_pct < 5%
    WARN:  spread_pct 5–10%
    FAIL:  spread_pct > 10%
  All 4 parts pass → PASS | Any 1 fails → WARN | 2+ fail → FAIL
  blocking: True if 2+ parts fail OR spread_pct > 15%

GATE 7 — MARKET REGIME (market_regime)
  Two-layer:
  7A: spy_above_200sma: bool (passed from swing input or computed)
  7B: spy_5day_return = (spy_price_today / spy_price_5d_ago) - 1
  PASS:  spy_above_200sma == True AND spy_5day_return > -0.02
  WARN:  spy_above_200sma == True AND spy_5day_return between -0.02 and -0.04
  FAIL:  spy_above_200sma == False OR spy_5day_return < -0.04
  blocking: True on FAIL

GATE 8 — CONFIRMED CLOSE ABOVE PIVOT (pivot_confirm)
  vcp_pivot: float (from swing input)
  last_close: float (from IBKR or yfinance)
  PASS:  last_close > vcp_pivot
  FAIL:  last_close <= vcp_pivot
  blocking: True on FAIL
  Note: This gate LOCKS the recommendation cards in the UI.
        No strategy shown until this passes.

GATE 9 — POSITION SIZING (position_size)
  account_size: float (from user settings, default 50000)
  risk_pct: float (default 0.01 = 1%)
  max_risk = account_size * risk_pct
  lots_allowed = floor(max_risk / (premium * 100))
  PASS:  lots_allowed >= 1
  WARN:  premium * 100 > max_risk * 1.5 (borderline)
  FAIL:  lots_allowed == 0 (trade too expensive for account)
  blocking: False (warn only, user decides)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRACK B GATES — SELL PUT (run when direction == "sell_put")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GATE 1 — IV RANK INVERTED (ivr_seller)
  PASS:  ivr_pct >= 50   → "Premium expensive — ideal for selling"
  WARN:  ivr_pct 30–49   → "Minimum viable IV for put selling"
  FAIL:  ivr_pct < 30    → "IV too cheap — insufficient premium"
  blocking: True on FAIL

GATE 2 — STRIKE SAFETY (strike_safety)
  s1_support: float (from swing input — S&R engine output)
  PASS:  strike <= s1_support * 0.995  → "Strike safely below S1 support"
  WARN:  strike between s1_support * 0.995 and s1_support
  FAIL:  strike > s1_support
  blocking: True on FAIL

GATE 3 — DTE FOR SELLERS (dte_seller)
  PASS:  14 <= selected_expiry_dte <= 21  → "Optimal theta decay window"
  WARN:  selected_expiry_dte between 21–35
  FAIL:  selected_expiry_dte > 45 OR selected_expiry_dte < 7
  blocking: True on FAIL

GATE 4 — EVENT CALENDAR (events) [same logic as Track A]

GATE 5 — LIQUIDITY (liquidity) [same logic as Track A]

GATE 6 — MARKET REGIME STRICT (market_regime_seller)
  Put sellers most exposed to drops — stricter regime check:
  PASS:  spy_above_200sma == True AND spy_5day_return > -0.01
  WARN:  spy_5day_return between -0.01 and -0.02
  FAIL:  spy_above_200sma == False OR spy_5day_return < -0.02
  blocking: True on FAIL

GATE 7 — MAX LOSS DEFINED (max_loss)
  For cash-secured put: max_loss = (strike - premium) * 100 per lot
  PASS:  max_loss * lots <= account_size * 0.10  (max 10% account)
  WARN:  max_loss * lots between 10–20% of account
  FAIL:  max_loss * lots > 20% of account
  blocking: True on FAIL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — STRATEGY RANKER (strategy_ranker.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For TRACK A (buy_call), rank these 3 candidates from the chain:

CANDIDATE 1 — ITM Call (Rank #1 Best Fit)
  Select strike where delta is closest to 0.68
  Name: "{strike}C · {expiry_month} {expiry_year}"
  Why: "Highest probability. Intrinsic value shields theta. Best for
       momentum breakouts per institutional quant review."

CANDIDATE 2 — Bull Call Spread (Rank #2 Defined Risk)
  Long leg: ATM strike (delta closest to 0.52)
  Short leg: strike closest to Target 1 price
  Net premium = long_premium - short_premium
  Why: "Lowest cost. Short strike caps at Target 1. Best % return
       to T1. Lowest theta burn for slower breakouts."

CANDIDATE 3 — ATM Call (Rank #3 High Leverage)
  Select strike where delta closest to 0.52
  Label with ⚠️ HIGH THETA warning
  Why: "Highest gamma. Best for explosive breakouts only. Theta
       burns fastest — must move within 5 days."

For each candidate, return:
  rank: int
  label: str
  strategy_type: "itm_call" | "spread" | "atm_call" | "sell_put"
  strike_display: str
  expiry_display: str
  premium_per_lot: float         (premium * 100)
  breakeven: float
  delta: float
  theta_per_day: float
  vega: float
  gamma: float
  implied_vol: float
  max_gain_per_lot: float | None  (None = unlimited for naked long)
  max_loss_per_lot: float
  spread_pct: float | None        (None if no bid/ask)
  why: str
  warning: str | None

For TRACK B (sell_put), rank by:
  1. Highest premium collected with strike safely below S1
  2. Highest credit / max_loss ratio

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — P&L CALCULATOR (pnl_calculator.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Compute P&L per 1 lot at expiry for 6 price scenarios.
Use Black-Scholes at expiry (time_to_expiry=0), so option value = intrinsic.

SCENARIOS (auto-populated from swing input):
  1. Stop Loss:     swing_stop_price     label="Stop Loss 🔴"
  2. Sideways:      current_price * 0.96 label="Sideways / -4%"
  3. Current Price: current_price        label="Current Price"
  4. VCP Pivot:     vcp_pivot_price      label="VCP Pivot ⚡"
  5. Target 1:      swing_target1        label="Target 1 ✅"
  6. Target 2:      swing_target2        label="Target 2 🎯"

For each scenario × each candidate (3 strategies):
  BUY CALL:    pnl = (max(0, scenario_price - strike) - premium) * 100
  BUY SPREAD:  pnl = (min(max(0, s-long_strike), short_strike-long_strike)
                      - net_premium) * 100
  SELL PUT:    pnl = (premium - max(0, strike - scenario_price)) * 100

Also compute:
  pnl_pct = pnl / (premium * 100) * 100
  theta_burn_at_hold = theta_per_day * 7 * 100  (7-day hold cost)

Return array of scenario rows, each with:
  scenario_label, stock_price, stock_move_pct,
  pnl_c1, pnl_pct_c1,
  pnl_c2, pnl_pct_c2,
  pnl_c3, pnl_pct_c3

Footer row:
  breakevens, 7-day theta burns, max losses, lots_at_1pct_risk

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — IV STORE (iv_store.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SQLite database at backend/data/iv_history.db

TABLE: iv_history
  ticker TEXT, date TEXT, iv REAL, source TEXT,
  PRIMARY KEY (ticker, date)

TABLE: ohlcv_daily (for HV computation)
  ticker TEXT, date TEXT, open REAL, high REAL,
  low REAL, close REAL, volume INTEGER,
  PRIMARY KEY (ticker, date)

METHODS:
  store_iv(ticker, date, iv, source="ibkr") → upsert
  get_iv_history(ticker, days=252) → list[{date, iv}]
  compute_ivr_pct(ticker, current_iv) → float (0-100)
    → percentile rank of current_iv in stored history
    → fallback if < 30 rows: return None (use absolute IV check)
  store_ohlcv(ticker, bars: list) → upsert all
  compute_hv(ticker, days=20) → float (annualized %)
    → std(log(close[i]/close[i-1])) for last N days × sqrt(252) × 100

SEEDING on first run:
  If IBKR connected: call get_historical_iv(ticker, 365) and store all
  This gives IVR from day 1 — no 30-day warmup needed (unlike Massive)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — FLASK API ROUTES (app.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PORT: 5050   CORS: enabled for localhost:3050

GET  /api/health
  Returns: {status, ibkr_connected, mock_mode, version}

POST /api/options/analyze
  Body: {
    ticker: str,                    # e.g. "AME"
    direction: str,                 # "buy_call"|"sell_put"|"sell_call"|"buy_put"
    account_size: float,            # default 50000
    risk_pct: float,                # default 0.01
    planned_hold_days: int,         # default 7

    # ── Swing Analyzer Fields (optional — manual if not connected) ──
    swing_signal: str,              # "BUY"|"HOLD"|"AVOID"
    entry_pullback: float,
    entry_momentum: float,
    stop_loss: float,
    target1: float,
    target2: float,
    risk_reward: float,
    vcp_pivot: float,
    vcp_confidence: float,          # 0-100
    adx: float,
    last_close: float,
    s1_support: float,
    spy_above_200sma: bool,
    spy_5day_return: float,         # e.g. 0.008 = +0.8%
    earnings_days_away: int,
    pattern: str                    # "VCP"|"Cup&Handle"|"FlatBase"|"None"
  }
  Returns: full analysis response (see SECTION 8)

GET  /api/options/chain/{ticker}
  Returns raw chain data for debugging

GET  /api/options/ivr/{ticker}
  Returns {current_iv, ivr_pct, hv_20, history_days, fallback_used}

POST /api/options/paper-trade
  Body: {ticker, direction, strategy_rank, strike, expiry,
         premium, lots, account_size}
  Saves to SQLite paper_trades table
  Returns: {success, trade_id}

GET  /api/options/paper-trades
  Returns list of all paper trades with current P&L (mark-to-market)

POST /api/options/seed-iv/{ticker}
  Manually trigger historical IV seed from IBKR
  Returns: {seeded_days, earliest_date, latest_date}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 8 — API RESPONSE SCHEMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "ticker": "AME",
  "direction": "buy_call",
  "track": "A",                         # A = buy call/sell call, B = buy put/sell put
  "underlying_price": 234.35,
  "data_source": "ibkr"|"mock",
  "ibkr_connected": true,
  "timestamp": "2026-03-03T14:30:00",

  "swing_data": {
    "signal": "BUY",
    "entry_pullback": 204.15,
    "entry_momentum": 234.35,
    "stop_loss": 192.93,
    "target1": 254.62,
    "target2": 278.36,
    "risk_reward": 4.50,
    "vcp_pivot": 242.05,
    "vcp_confidence": 70.0,
    "adx": 40.2,
    "last_close": 234.35,
    "s1_support": 225.80,
    "spy_above_200sma": true,
    "spy_5day_return": 0.008,
    "earnings_days_away": 45,
    "pattern": "VCP"
  },

  "verdict": {
    "status": "pass"|"warn"|"fail",
    "gates_passed": 7,
    "gates_total": 9,
    "blocking_gate": "pivot_confirm"|null,
    "score_label": "7/9",
    "headline": "CAUTION — Wait for pivot confirmation",
    "color": "amber"|"green"|"red"
  },

  "gates": [ ...array of 9 gate result objects... ],

  "behavioral_checks": [
    {
      "id": "gate8_block",
      "type": "hard_block"|"warning"|"info",
      "label": "Hard Block: Pivot Not Confirmed",
      "message": "Stock has not closed above VCP pivot $242.05..."
    }
    // always 4 behavioral checks, hardcoded, never skipped
  ],

  "top_strategies": [
    { ...strategy object rank 1... },
    { ...strategy object rank 2... },
    { ...strategy object rank 3... }
  ],

  "pnl_table": {
    "scenarios": [ ...6 rows... ],
    "footer": {
      "breakevens": [239.80, 238.80, 241.40],
      "theta_burns_7d": [126, 56, 154],
      "max_losses": [980, 380, 640],
      "lots_at_1pct": [0.5, 1.3, 0.8]
    }
  },

  "ivr_data": {
    "current_iv": 18.4,
    "ivr_pct": 22.0,
    "hv_20": 17.1,
    "hv_iv_ratio": 1.08,
    "history_days": 180,
    "fallback_used": false
  },

  "put_call_ratio": 0.92,          # sum(put OI) / sum(call OI) from chain
  "max_pain_strike": 230.0,        # informational only, never a hard gate
  "recommended_dte": 45,
  "direction_locked": ["sell_call", "buy_put"]  # disabled directions
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 9 — FRONTEND COMPONENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COLOR SYSTEM (CSS variables, dark theme):
  --bg: #0D1117         --bg2: #161B22       --bg3: #1C2333
  --green: #00C896      --red: #FF4444
  --amber: #F59E0B      --blue: #3B82F6      --purple: #A78BFA
  --border: #30363D     --text: #E6EDF3      --text-dim: #8B949E

KEY UI RULES (enforce in every component):

1. DIRECTION SELECTOR:
   - sell_call and buy_put cards are DISABLED (greyed, pointer-events:none)
     when swing_signal === "BUY". Show tooltip: "Locked: contradicts BUY signal"
   - buy_call is AUTO-SELECTED when swing_signal === "BUY"
   - sell_put remains manually selectable on BUY signal

2. STRATEGY CARDS:
   - ALL THREE cards show a "🔒 GATED OUT" overlay with red badge
     when gate_id "pivot_confirm" has status "fail"
   - Overlay is position:absolute, covers entire card with semi-transparent
     dark overlay + centered lock message
   - Cards only fully visible when ALL blocking gates pass

3. P&L TABLE:
   - Target rows (T1, T2, Pivot): green left border highlight
   - Stop loss row: red dimmed text
   - Profit cells: green (#00C896), font-family: monospace
   - Loss cells: red (#FF4444), font-family: monospace
   - Candidate 3 column: show ⚠️ HIGH THETA in header
   - When gate8 fails: all P&L values show "--" instead of numbers

4. BEHAVIORAL CHECKS:
   - Always rendered — cannot be hidden or dismissed
   - Purple left border accent
   - 4 hardcoded checks (adjust text dynamically):
     a. Gate 8 block (hard block warning, always shown)
     b. Entry timing conflict (if entry_momentum > entry_pullback * 1.1)
     c. VRP headwind (always shown — "53.78% stock win ≠ options win")
     d. Lottery bias (always shown — "Pick Δ0.68, not highest % return")

5. SWING IMPORT STRIP:
   - If connected to swing analyzer (swing_data.source === "swing_api"):
     Show green "● LIVE" badge, all fields read-only
   - If manual mode:
     Show amber "✎ MANUAL" badge, all fields editable inline
   - "Connect to Swing Analyzer" button → POST to /api/integrate/status

6. IBKR STATUS INDICATOR (top-right header):
   - Green dot "● IB Gateway" when ibkr_connected = true
   - Red dot "○ Mock Mode" when ibkr_connected = false
   - Click → shows modal: "Start IB Gateway on port 7497 (paper) or 7496 (live)"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 10 — INTEGRATION SEAM (for future swing analyzer connection)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This module will later be called by the swing analyzer at localhost:5001.
Design the integration seam now so it requires ZERO refactoring later.

IN SWING ANALYZER (future addition to backend.py at localhost:5001):
  GET /api/options/launch?ticker=AME
  This endpoint will:
    1. Gather current swing analysis output for the ticker
    2. POST it to OptionsIQ at localhost:5050/api/options/analyze
    3. Return redirect URL: http://localhost:3050?ticker=AME&auto=true

IN OPTIONSIQ (app.py):
  GET /api/integrate/ping
    Returns: {status: "ok", version: "2.0", accepts_swing_data: true}
  GET /api/integrate/schema
    Returns: the full list of accepted swing_data fields + types
    (This is what the swing analyzer reads to know what to send)

Frontend (App.jsx):
  On load, check URL params: ?ticker=AME&auto=true
  If auto=true: immediately call /api/options/analyze with ticker
  And pre-fill swing data from URL params if passed as JSON-encoded param

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 11 — MOCK PROVIDER (mock_provider.py)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Returns realistic test data for AME when IB Gateway is offline.
Mirrors exact schema of ibkr_provider output.

Mock chain for AME @ $234.35:
  Expiries: Mar 21 2026 (18 DTE), Apr 17 2026 (45 DTE)
  Strikes: 220, 225, 230, 235, 240, 245, 250, 255, 260
  Apr 230 Call: bid=9.60, ask=10.00, delta=0.68, gamma=0.021,
    theta=-0.18, vega=0.28, iv=0.184, oi=12400, volume=3100
  Apr 235 Call: bid=6.20, ask=6.60, delta=0.52, gamma=0.025,
    theta=-0.22, vega=0.34, iv=0.187, oi=8200, volume=2100
  Apr 255 Call: bid=1.90, ask=2.10, delta=0.24, gamma=0.016,
    theta=-0.11, vega=0.21, iv=0.195, oi=4100, volume=800

Historical IV mock: 180 days of realistic values (15–28% range)
Underlying mock: AME current price 234.35, HV20=17.1%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 12 — REQUIREMENTS + STARTUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

requirements.txt:
  flask>=3.0
  flask-cors>=4.0
  ib_insync>=0.9.86
  yfinance>=0.2.40         # fallback for SPY/earnings data
  numpy>=1.26
  python-dotenv>=1.0
  sqlite3                  # stdlib

.env.example:
  IBKR_HOST=127.0.0.1
  IBKR_PORT=7497           # 7497=paper, 7496=live
  IBKR_CLIENT_ID=10
  ACCOUNT_SIZE=50000
  RISK_PCT=0.01
  PLANNED_HOLD_DAYS=7
  SWING_ANALYZER_URL=http://localhost:5001   # future integration

start.sh:
  #!/bin/bash
  cd backend && python app.py &
  cd frontend && npm start &
  echo "OptionsIQ running: backend :5050 | frontend :3050"

stop.sh:
  #!/bin/bash
  pkill -f "python app.py"
  pkill -f "react-scripts"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 13 — BUILD ORDER (build in this exact sequence)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 1 — Backend Core (test with curl before touching frontend):
  Step 1: iv_store.py (SQLite setup + IVR math)
  Step 2: mock_provider.py (full mock data, no IB Gateway needed)
  Step 3: gate_engine.py (all 9 Track A gates + 7 Track B gates)
  Step 4: pnl_calculator.py (P&L math for all 6 scenarios)
  Step 5: strategy_ranker.py (rank 3 candidates)
  Step 6: app.py (wire all routes, use mock_provider first)
  TEST: curl -X POST localhost:5050/api/options/analyze with mock AME data

Phase 2 — IBKR Live (replace mock with real data):
  Step 7: ibkr_provider.py (connect, options chain, historical IV)
  Step 8: Test with IB Gateway running in paper mode
  Step 9: Seed iv_history.db with 1 year of historical IV for test tickers

Phase 3 — Frontend:
  Step 10: App.jsx + useOptionsData hook (fetch + state)
  Step 11: SwingImportStrip (manual input form)
  Step 12: DirectionSelector (4 cards, lock logic)
  Step 13: MasterVerdict + GatesGrid (9 gates)
  Step 14: BehavioralChecks (4 hardcoded)
  Step 15: TopThreeCards (with GATED OUT overlay)
  Step 16: PnLTable (6 scenarios × 3 strategies)
  Step 17: PaperTradeBanner + record trade flow

Phase 4 — Integration Seam:
  Step 18: /api/integrate/ping + /api/integrate/schema routes
  Step 19: URL param auto-load (?ticker=AME&auto=true)
  Step 20: Test full handshake from swing analyzer mock POST

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 14 — TEST CASES (verify these pass before calling done)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TC1: Gate 8 fail → All 3 strategy cards show GATED OUT overlay
TC2: Gate 8 pass → Cards fully visible, no overlay
TC3: IVR > 50 on buy_call → Gate 1 FAIL, blocking=True, verdict=red
TC4: sell_put direction → Track B gates run, Track A gates not shown
TC5: sell_call direction selected → UI shows "Locked: contradicts BUY signal"
TC6: IBKR offline → mock_provider used, header shows "○ Mock Mode"
TC7: P&L table at Stop Loss → all 3 strategies show -100% loss
TC8: IVR < 30 days history → fallback absolute IV check used, no crash
TC9: account_size=10000, premium=12.00 → lots_allowed=0, Gate 9 WARN
TC10: /api/integrate/ping returns 200 with correct schema

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END OF CODEX BUILD PROMPT — OptionsIQ v2.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
