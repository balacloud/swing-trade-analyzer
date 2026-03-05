# OptionsIQ — Complete Build Plan
> **Status:** Planning phase — DO NOT build until this document is approved
> **Last Updated:** Day 65 (March 5, 2026)
> **Author:** Claude Sonnet 4.6 (with user input)

---

## 0. What This System Is

**Live-First Design Principle:**
This system is designed for live trading from day one. Paper trading uses the **exact same live data path** as production — no delayed mode, no special paper branch. The only difference between paper trading and live trading is whether a trade is recorded in the `paper_trades` table or sent to a broker (order execution is out of scope). This is deliberate: paper trades trained on live data = valid preparation for live trades.

A personal, standalone options analysis tool that:
1. Takes a stock ticker (from STA or manually entered)
2. Pulls the options chain from IBKR
3. Runs gate checks to validate if options entry conditions are met
4. Recommends the top 3 strike/expiry combinations for the chosen direction
5. Shows P&L table across 6 price scenarios
6. Records paper trades

**Four supported directions** (all from the user's learning foundation):

| Market View | Direction | Type | Gate Track |
|-------------|-----------|------|------------|
| Extremely Bullish | buy_call | Pay premium (debit) | Track A |
| Neutral to Bearish | sell_call | Collect premium (credit) | Track A |
| Extremely Bearish | buy_put | Pay premium (debit) | Track B |
| Neutral to Bullish | sell_put | Collect premium (credit) | Track B |

**Strike preference (from user's learning doc):**
- Buyers (buy_call, buy_put): prefer **ITM** (delta ~0.68) — intrinsic value buffers theta decay
- Sellers (sell_call, sell_put): prefer **ATM** — maximum theta decay works in their favor

**DTE window: 14 to 120 days**
- Minimum 14 days — avoids extreme theta burn near expiry
- Maximum 120 days — allows for position trades and longer swings
- Sweet spot for buyers: 45-90 days (time for move to develop)
- Sweet spot for sellers: 21-45 days (theta decay accelerating but not chaotic)

---

## 1. What We Know From Research

### 1A. IBKR Subscriptions (User's Account — Confirmed)

From the screenshot provided:

| Subscription | Cost | Status |
|---|---|---|
| US Securities Snapshot and Futures Value Bundle (NP,L1) | USD 10.00/month | Active (waived if commissions ≥ $30) |
| US Equity and Options Add-On Streaming Bundle (NP) | USD 4.50/month | Active |

**Implication:** The user has **live (real-time) options data**. `reqMarketDataType(1)` is the correct default. `modelGreeks` (delta, theta, vega, gamma) should be available from IBKR for most US equity options contracts.

However, we still build with **Black-Scholes fallback** because:
- `modelGreeks` can be `None` for some contracts (thin market, no quotes yet)
- In mock/delayed mode, Greeks are always None
- Paper trading tolerance for BS approximation is acceptable

### 1B. ib_insync Status (Perplexity Confirmed)
- `erdewit/ib_insync` is **archived** (original author passed away)
- Still widely used in production, community considers it "frozen but functional"
- **Pin version 0.9.86** in requirements.txt
- No clearly superior replacement yet — use ib_insync + our own circuit breaker
- `ib_async` exists but has less adoption and community

### 1C. reqTickers Latency Fix (Perplexity Confirmed)
- `reqTickers` in a Flask thread = serialized blocking = timeouts
- **Correct pattern:** Single dedicated IB worker thread that owns the IB() instance
- Flask routes publish to request queue, read from result queue with timeout
- This is a fundamental architectural fix vs what Codex built (ThreadPoolExecutor per request)

### 1D. Greeks with Delayed/Missing Data (Perplexity Confirmed)
- With live subscriptions: modelGreeks usually available
- modelGreeks can still be None for some contracts even with live data
- **Black-Scholes self-computation is the accepted community solution**
- IBKR provides even under delayed: underlying price, strikes, expiries, IV (sometimes), OI, volume

### 1E. Chain Fetch Pattern (Perplexity Confirmed)
- `reqSecDefOptParams` → filter expiries → filter strikes → `qualifyContracts` → `reqTickers` is the correct pattern
- Cap at ~60 contracts per `reqTickers` call to avoid pacing violations
- For 14-120 DTE window with ±10% strikes: typically 30-80 contracts — within safe limits

---

## 2. What's Wrong With What Codex Built

(Full audit from code review — see separate audit notes)

| # | Problem | Severity | Fix |
|---|---------|----------|-----|
| 1 | app.py is a 768-line God Object | Critical | Split into data_service + analyze_service |
| 2 | In-memory chain cache lost on restart | Critical | Persistent SQLite cache |
| 3 | mock_provider ignores ticker — always returns AME data | Critical | Dynamic mock pricing per ticker |
| 4 | Partial chain uses AME greeks for any ticker | Critical | Remove; return partial quality flag instead |
| 5 | _merge_swing() fabricates missing data silently | High | Reject with error if required fields missing |
| 6 | No yfinance middle tier — IBKR fails → AME mock | High | Add yfinance provider |
| 7 | QUICK_ANALYZE_MODE silently uses mock HV20 | High | Remove; always use real data for HV |
| 8 | fomc_days_away defaults to 30 — never computed | Medium | Pull from STA /api/context or hardcoded calendar |
| 9 | No constants.py — magic numbers everywhere | Medium | Extract all thresholds |
| 10 | No project documentation structure | Medium | CLAUDE_CONTEXT equivalent |
| 11 | reqTickers called in ThreadPoolExecutor per request | Medium | Dedicated IB worker thread |
| 12 | No Black-Scholes fallback for missing Greeks | Medium | Add bs_calculator.py |
| 13 | DTE hardcoded: smart=120, full=90 — inconsistent | Low | Respect user DTE window (14-120) |

**What to keep as-is (the math is correct):**
- `gate_engine.py` — all gate logic correct for all 4 directions
- `pnl_calculator.py` — P&L math correct for all strategy types
- `strategy_ranker.py` — delta targeting and spread construction correct
- `iv_store.py` — IVR percentile and HV20 computation correct
- `ibkr_provider.py` core chain logic — correct, just needs worker thread wrapping
- All 9 frontend components — correct structure, need minor cleanup

---

## 3. Final Architecture

### 3A. Project Structure

```
Options_Engine_Codex/
|
|-- CLAUDE_CONTEXT.md              <- Single reference (mirrors STA approach)
|
|-- docs/
|   |-- stable/
|   |   |-- GOLDEN_RULES.md        <- Project rules
|   |   |-- ROADMAP.md             <- Feature roadmap
|   |   `-- API_CONTRACTS.md       <- All endpoints + schemas
|   |-- versioned/
|   |   `-- KNOWN_ISSUES_DAY1.md   <- 13 issues from Codex audit
|   `-- status/
|       `-- PROJECT_STATUS_DAY1.md <- Starting state
|
|-- backend/
|   |-- app.py                     <- Routes ONLY (~120 lines max)
|   |-- constants.py               <- All thresholds, DTE limits, defaults
|   |-- data_service.py            <- Provider selection, cache, IB worker
|   |-- analyze_service.py         <- Analysis assembly (validate + run + respond)
|   |-- bs_calculator.py           <- Black-Scholes Greeks (NEW)
|   |-- ibkr_provider.py           <- Keep core; wrap in worker thread
|   |-- yfinance_provider.py       <- NEW middle tier
|   |-- mock_provider.py           <- Fix: dynamic pricing per ticker
|   |-- gate_engine.py             <- KEEP AS-IS
|   |-- strategy_ranker.py         <- KEEP AS-IS
|   |-- pnl_calculator.py          <- KEEP AS-IS
|   |-- iv_store.py                <- KEEP AS-IS
|   |-- requirements.txt           <- Pin ib_insync==0.9.86
|   |-- data/
|   |   `-- cache.db               <- Persistent SQLite (chains + paper trades)
|   `-- .env
|
`-- frontend/
    `-- src/
        |-- App.jsx                <- Keep structure, minor cleanup
        |-- components/
        |   |-- Header.jsx         <- Keep
        |   |-- SwingImportStrip.jsx <- Enhance: STA Live vs Manual
        |   |-- DirectionSelector.jsx <- Keep all 4 directions
        |   |-- MasterVerdict.jsx  <- Keep
        |   |-- GatesGrid.jsx      <- Keep
        |   |-- BehavioralChecks.jsx <- Keep
        |   |-- TopThreeCards.jsx  <- Keep
        |   |-- PnLTable.jsx       <- Keep
        |   `-- PaperTradeBanner.jsx <- Keep
        |-- hooks/
        |   `-- useOptionsData.js  <- Keep, minor cleanup
        `-- index.css              <- Keep dark theme
```

### 3B. Data Provider Hierarchy

**Default mode: `reqMarketDataType(1)` — live data always.**
Paper trading and live analysis use the same tier 1 data path. There is no "paper mode" switch that degrades data quality.

```
Request for ticker options chain (same path for paper trading AND live analysis):
    |
    v
[1] IBKR Live (reqMarketDataType=1)  ← DEFAULT FOR ALL OPERATIONS
    - Live bid/ask + live modelGreeks
    - If modelGreeks is None: compute via bs_calculator.py
    - Quality: "live"
    |
    | (IBKR timeout / circuit open / TWS not connected)
    v
[2] IBKR Cache (SQLite, TTL 2 min for chain, 6h for IV history)
    - Last known good chain data from IBKR
    - Trigger async background refresh
    - Quality: "cached" — user sees banner: "Using cached chain (Xm ago)"
    |
    | (no cache hit)
    v
[3] yfinance (emergency only)
    - Underlying price, strikes, OI, volume, IV (no live greeks from yf)
    - Compute all greeks via bs_calculator.py
    - Quality: "delayed" — user sees banner: "Live data unavailable — using yfinance"
    |
    | (yfinance fails)
    v
[4] Mock (development and CI testing ONLY — never used in paper trading)
    - Dynamic pricing: yfinance underlying price if available, else $100 default
    - Synthetic greeks from Black-Scholes
    - Quality: "mock"
    - Banner: "MOCK DATA — for testing only. Do not use for paper trades."
```

**Quality banners are mandatory at tiers 2, 3, 4.** The frontend must show a dismissible warning when data quality degrades below "live". This ensures the user always knows what they're trading on.

### 3C. IB Worker Thread Pattern (Fixes the Latency Problem)

```
App startup:
    IBWorker thread starts, connects to IB Gateway
    IBWorker owns the single IB() instance (thread-safe)

Flask route (POST /api/options/analyze):
    1. Check SQLite cache — if fresh (< 2 min): serve immediately
    2. If stale: put request on IBWorker.request_queue
    3. Wait for result on IBWorker.result_queue (timeout = 24s for smart, 32s for full)
    4. If timeout: serve stale cache OR fall to yfinance
    5. If result: update cache, proceed with analysis

IBWorker loop:
    while running:
        req = request_queue.get()
        contracts = build_contracts(req)
        ib.qualifyContracts(*contracts)
        tickers = ib.reqTickers(*contracts[:60])  # single bulk call
        result_queue.put(tickers)
```

This is the pattern Perplexity confirmed as correct. Single IB() instance, no per-request connections, no ThreadPoolExecutor.

---

## 4. Key Design Decisions

### 4A. Gate Logic Per Direction

Based on user's learning doc (buyers = ITM preference, sellers = ATM):

**Track A — Buy Call (Extremely Bullish)**
- Gate 1: IVR < 30% (cheap IV — good time to buy)
- Gate 2: HV/IV ratio < 1.20 (not overpaying vs realized vol)
- Gate 3: Theta burn ≤ 8% over hold period
- Gate 4: DTE aligned with VCP confidence + ADX
- Gate 5: Earnings/FOMC not within expiry window
- Gate 6: Liquidity (OI, volume, spread)
- Gate 7: Market regime (SPY above 200 SMA + 5-day return)
- Gate 8: Confirmed close above VCP pivot ← hard block, locks strategy cards
- Gate 9: Position sizing (1% risk rule)

**Track A — Sell Call (Neutral to Bearish)**
- Gate 1: IVR >= 50% (high IV — good time to sell premium)
- Gate 2: Strike above current price AND above resistance
- Gate 3: DTE 14-45 days (theta decay acceleration zone)
- Gate 4: Earnings/FOMC not within expiry window
- Gate 5: Liquidity
- Gate 6: Market regime STRICT (below 200 SMA OR 5-day return < -2%)
- Gate 7: Max loss defined (strike - premium, per lot ≤ 10% account)

**Track B — Buy Put (Extremely Bearish)**
- Gate 1: IVR < 30% (cheap IV to buy)
- Gate 2: HV/IV ratio
- Gate 3: Theta burn
- Gate 4: DTE selection (directional conviction needed)
- Gate 5: Earnings/FOMC calendar
- Gate 6: Liquidity
- Gate 7: Market regime INVERTED (SPY below 200 SMA or bearish trend)
- Gate 8: Confirmed close BELOW key support ← hard block
- Gate 9: Position sizing

**Track B — Sell Put (Neutral to Bullish)**
- Gate 1: IVR >= 50% (selling expensive premium)
- Gate 2: Strike safety (below S1 support level)
- Gate 3: DTE 14-45 days
- Gate 4: Earnings/FOMC calendar
- Gate 5: Liquidity
- Gate 6: Market regime strict (must be above 200 SMA, can't be breaking down)
- Gate 7: Max loss defined (strike - premium ≤ 10% account)

### 4B. Strategy Ranking Per Direction

**Buy Call** — 3 candidates:
1. ITM Call: delta closest to 0.68 — "Intrinsic value buffers theta. Best for momentum breakouts."
2. Bull Call Spread: ATM long / Target1 short — "Defined risk. Best cost-to-return if stock hits T1."
3. ATM Call: delta closest to 0.52 — "HIGH THETA warning. Only for explosive breakouts."

**Sell Call** — 3 candidates:
1. OTM Call above resistance (safest)
2. ATM Call (highest premium collected)
3. Bear Call Spread (defined risk version — long higher strike for protection)

**Buy Put** — 3 candidates:
1. ITM Put: delta closest to -0.68
2. Bear Put Spread: ATM long / S1 support short leg
3. ATM Put: delta closest to -0.52 with HIGH THETA warning

**Sell Put** — 3 candidates:
1. Put below S1 support (safest)
2. ATM Put (highest premium)
3. Bull Put Spread (defined risk version)

### 4C. DTE Window: 14-120 Days

**Smart profile (default):** 1 expiry, nearest at/above 21 DTE
**Full profile:** up to 3 expiries in 14-120 DTE window
**Strike window:** ±10% of underlying (smart), ±15% (full)
**Max contracts per reqTickers call:** 60

**Why 14-120 over 14-56:**
- Allows for 60-90 DTE ITM calls — best theta/delta ratio for swing buys
- Seller DTE still constrained by gate logic (14-45 for sellers, not 14-120)
- Chain fetching scoped to direction: buy_call → prefers 45-90, sell_put → prefers 21-45

### 4D. Black-Scholes Calculator

```python
# bs_calculator.py
import math
from scipy.stats import norm

def compute_greeks(S, K, T, r, sigma, right='C'):
    """
    S: underlying price
    K: strike price
    T: time to expiry in years (DTE / 365)
    r: risk-free rate (e.g., 0.053 for current T-bill)
    sigma: implied volatility as decimal (e.g., 0.22 for 22%)
    right: 'C' for call, 'P' for put
    Returns: dict with delta, gamma, theta, vega, price
    """
```

Used whenever `modelGreeks is None` in ibkr_provider output, or in yfinance/mock provider.

Risk-free rate: stored in constants.py, updated manually when materially different (currently ~5.3%).

### 4E. STA Integration — First-Class, Not Optional

STA at localhost:5001 is the primary data source for swing fields.

**What OptionsIQ needs from STA (existing endpoints, zero STA changes):**

| Field | STA Endpoint | Key |
|-------|-------------|-----|
| stop_loss | GET /api/sr/{ticker} | meta.tradeViability + levels |
| target1, target2 | GET /api/sr/{ticker} | resistance levels |
| s1_support | GET /api/sr/{ticker} | nearest support |
| adx | GET /api/stock/{ticker} | adx |
| vcp_confidence | GET /api/patterns/{ticker} | vcp.confidence |
| vcp_pivot | GET /api/patterns/{ticker} | vcp.pivot |
| swing_signal | GET /api/stock/{ticker} | categoricalVerdict |
| spy_above_200sma | GET /api/stock/SPY | trend template |
| fomc_days_away | GET /api/context/SPY | cycles.fomc_days |
| earnings_days_away | GET /api/earnings/{ticker} | days_away |
| pattern | GET /api/patterns/{ticker} | detected_pattern |

**In analyze_service.py:**
```python
def fetch_sta_data(ticker: str) -> dict | None:
    """Calls STA at localhost:5001. Returns swing fields or None."""
    # Tries 4 STA endpoints, assembles the payload
    # Returns None on connection error → UI shows Manual mode
```

**Frontend SwingImportStrip.jsx:**
- "Connect to STA" button → calls /api/integrate/sta-fetch/{ticker}
- Connected: green "● STA Live" badge, all fields read-only
- Manual: amber "✎ Manual" badge, all fields editable
- FOMC days shown explicitly (never silent default)

### 4F. Constants (No More Magic Numbers)

```python
# constants.py
# --- Gate thresholds ---
IVR_BUYER_PASS_PCT     = 30.0   # IVR < 30 = cheap IV for buyers
IVR_BUYER_WARN_PCT     = 50.0   # IVR 30-50 = moderate
IVR_SELLER_PASS_PCT    = 50.0   # IVR >= 50 = rich premium for sellers
IVR_SELLER_MIN_PCT     = 30.0   # IVR 30-50 = minimum viable for selling
HV_LOW_REGIME_PCT      = 15.0   # HV < 15% = special low-vol exception
HV_IV_PASS_RATIO       = 1.20
HV_IV_WARN_RATIO       = 1.30
THETA_BURN_PASS_PCT    = 8.0
THETA_BURN_WARN_PCT    = 12.0
SPREAD_WARN_PCT        = 5.0
SPREAD_FAIL_PCT        = 10.0
SPREAD_BLOCK_PCT       = 15.0
MIN_OPEN_INTEREST      = 1000
MIN_VOLUME_OI_RATIO    = 0.10
MIN_PREMIUM_DOLLAR     = 2.00
STRIKE_NEARNESS_PCT    = 0.05   # ATM = within 5% of underlying
MAX_LOSS_WARN_PCT      = 0.10   # 10% of account
MAX_LOSS_FAIL_PCT      = 0.20   # 20% of account

# --- Chain fetch ---
DEFAULT_MIN_DTE        = 14
DEFAULT_MAX_DTE        = 120
SMART_MAX_EXPIRIES     = 1
SMART_MAX_STRIKES      = 4
SMART_MAX_CONTRACTS    = 12
FULL_MAX_EXPIRIES      = 3
FULL_MAX_STRIKES       = 8
FULL_MAX_CONTRACTS     = 60
STRIKE_WINDOW_SMART    = 0.10
STRIKE_WINDOW_FULL     = 0.15

# --- Account defaults ---
DEFAULT_ACCOUNT_SIZE   = 25000  # user's actual account size
DEFAULT_RISK_PCT       = 0.01   # 1% per trade
DEFAULT_HOLD_DAYS      = 7

# --- Black-Scholes ---
RISK_FREE_RATE         = 0.053  # current T-bill rate, update manually

# --- Cache ---
CHAIN_CACHE_TTL_SEC    = 120    # 2 min for live chain
IV_HISTORY_CACHE_DAYS  = 365
PAPER_TRADE_MTM_TTL    = 300    # 5 min for mark-to-market

# --- Ports ---
BACKEND_PORT           = 5051
FRONTEND_PORT          = 3050
STA_BASE_URL           = "http://localhost:5001"
IB_WORKER_TIMEOUT_SEC  = 24    # smart profile
IB_WORKER_TIMEOUT_FULL = 32    # full profile
```

---

## 5. What NOT to Build (Kept Out of Scope)

- No auth layer — personal use, single user
- No multi-user / cloud deployment
- No Level 2 / order book data
- No order execution (analysis only, never sends orders to IBKR)
- No real-time streaming / WebSocket feed — polling on demand is sufficient for paper trading
- No Canadian market (STA constraint applies here too)
- No futures or index options (US equity calls and puts only)

---

## 6. Build Phases

### Phase 0 — Documentation (Day 1, before code)
- [ ] Create CLAUDE_CONTEXT.md for OptionsIQ
- [ ] Create GOLDEN_RULES.md
- [ ] Create ROADMAP.md
- [ ] Create API_CONTRACTS.md
- [ ] Create KNOWN_ISSUES_DAY1.md (13 issues from Codex audit)
- [ ] Create PROJECT_STATUS_DAY1_SHORT.md

### Phase 1 — Backend Foundation (Day 1)
- [ ] constants.py (all thresholds)
- [ ] bs_calculator.py (Black-Scholes greeks + price)
- [ ] Fix mock_provider.py (dynamic pricing, not hardcoded AME)
- [ ] Fix iv_store.py schema (add `entry_price`, `mark_price` to paper_trades table)

### Phase 2 — Data Layer (Day 1-2)
- [ ] ibkr_provider.py: wrap in IBWorker dedicated thread
- [ ] yfinance_provider.py: new middle tier
- [ ] data_service.py: provider selection + persistent cache + circuit breaker

### Phase 3 — Analysis Layer (Day 2)
- [ ] analyze_service.py: validation + assembly + STA fetch
- [ ] Update gate_engine.py: import thresholds from constants (no magic numbers)
- [ ] Update strategy_ranker.py: DTE window 14-120

### Phase 4 — API Layer (Day 2)
- [ ] app.py: routes only, delegate to analyze_service + data_service
- [ ] Remove QUICK_ANALYZE_MODE
- [ ] Add /api/integrate/sta-fetch/{ticker} endpoint

### Phase 5 — Frontend (Day 3)
- [ ] SwingImportStrip.jsx: STA Live vs Manual badge + FOMC field
- [ ] App.jsx: cleanup
- [ ] Keep all other components as-is

### Phase 6 — Documentation Close (Day 3)
- [ ] CLAUDE_CONTEXT.md updated
- [ ] API_CONTRACTS.md finalized
- [ ] KNOWN_ISSUES updated (mark resolved)
- [ ] git init + initial commit

---

## 7. Open Questions (Resolved)

1. **Sell call and buy put directions** → **Include all 4 from day 1.**
   User confirmed: all four directions (buy_call, sell_call, buy_put, sell_put) are required.
   Build all 4 gate tracks from Phase 3 onward.

2. **Strategy candidates for sellers** → **Use 3 strike distances.**
   Sellers rank by strike safety (risk), not by strategy type:
   - Rank 1: Far OTM (safest — furthest from current price, above resistance / below support)
   - Rank 2: Mid OTM (balanced — moderate premium, moderate risk)
   - Rank 3: Near ATM (highest premium — maximum theta, highest risk)
   Spread version (defined risk) is offered as a modifier on Rank 3 if max_loss gate would otherwise fail.

3. **fomc_days_away when STA offline** → **Hardcode FOMC calendar in OptionsIQ.**
   Copy the 2026–2027 FOMC list from STA's cycles_engine.py into OptionsIQ's constants.py.
   This makes OptionsIQ standalone — FOMC gate works even when STA is offline.
   Update this list in 2027 the same way we update it in STA.

4. **Account size** → **.env variable (required, no silent default).**
   `ACCOUNT_SIZE` must be set in `.env`. Application raises a clear error at startup if not set.
   No magic default — user must be explicit about their own account size for position sizing.

5. **Paper trade mark-to-market** → **IBKR live option price (same live data path).**
   Consistent with live-first design: paper trade MTM uses the same `reqTickers` call on the
   original contract. Falls back to Black-Scholes if IBKR data unavailable. Never skips MTM.

---

## 8. Decisions Made (Locked In)

| Decision | Value |
|----------|-------|
| All 4 directions | Yes — buy_call, sell_call, buy_put, sell_put |
| DTE window | 14 to 120 days |
| Strike preference for buyers | ITM (delta ~0.68) as Rank 1 |
| Strike preference for sellers | ATM as primary |
| Live-first design | Paper trading uses same live data path as production |
| Data source primary | IBKR live (reqMarketDataType=1) — always, including paper trades |
| Data source fallback | yfinance (emergency) → mock (dev/CI only, never for paper trades) |
| Greeks fallback | Black-Scholes when modelGreeks is None |
| ib_insync version | 0.9.86 pinned |
| IB connection pattern | Single dedicated worker thread (not per-request) |
| Cache | Persistent SQLite (not in-memory) |
| STA integration | First-class, not optional — manual fallback |
| Account size default | $25,000 |
| FOMC calendar | Pull from STA when connected; hardcoded 2026-2027 as fallback |
| Project docs | Same structure as STA (CLAUDE_CONTEXT + GOLDEN_RULES + ROADMAP) |
