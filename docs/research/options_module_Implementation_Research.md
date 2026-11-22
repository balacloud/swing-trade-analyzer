# Options Module — Complete Research Compendium
### Swing Trade Analyzer | Options Tab Blueprint
**Version**: 1.0 | **Last Updated**: February 20, 2026  
**Context**: This document preserves all options-related research for the Swing Trade Analyzer project.  
Load this at the start of any new conversation to restore full context.

---

## PART 0 — SYSTEM CONTEXT (What Already Exists)

The Swing Trade Analyzer (React + Flask, v4.17) already provides:

| Data Point | Source | Endpoint |
|---|---|---|
| Verdict (BUY/HOLD/AVOID) | Categorical engine | Internal |
| Technical rating (Strong/Decent/Weak) | Minervini 8/8 Trend Template + RSI + RS + ADX | Internal |
| Fundamental rating | ROE, Revenue Growth, D/E | Internal |
| VIX level | yfinance/Finnhub | `/api/market/vix` |
| SPY regime (above/below 200 SMA) | TwelveData/yfinance | `/api/market/spy` |
| ADX value | OHLCV engine | Internal |
| RSI value | OHLCV engine | Internal |
| ATR value | OHLCV engine | Internal |
| Support levels S1–S4 | Agglomerative clustering + ZigZag (5% min) | `/api/sr/<ticker>` |
| Resistance level R1 | Same | `/api/sr/<ticker>` |
| Current price, 52W H/L | TwelveData → yfinance fallback | `/api/stock/<ticker>` |
| Avg daily stock volume, Liquidity ($) | Same | `/api/stock/<ticker>` |
| Earnings warning flag, Next earnings date | Finnhub/FMP | `/api/fundamentals/<ticker>` |
| Pattern detection (VCP 55%, C&H 0%, Flat 20%) | patterndetection.py | Internal |
| R:R ratio, Entry/Stop/Target | SR engine | `/api/sr/<ticker>` |

**Backtest validation (v4.16–v4.17)**:
- Config A (Categorical only): 1,108 trades, 51.53% WR, PF 1.41, p=0.000001
- Config B (A + Patterns): 406 trades, 51.72% WR, PF 1.43, p=0.002
- Config C (Full 3-layer): 238 trades, 53.78% WR, PF 1.61, p=0.002
- Walk-forward: out-of-sample OUTPERFORMS in-sample → system is NOT overfitted

---

## PART 1 — DATA ARCHITECTURE (Three Layers)

### Layer 0 — Already In Your System (Zero New Work)
Price, Volume, ATR, RSI, ADX, 52W H/L, Support/Resistance, VIX, SPY regime,
Verdict, Earnings date, Liquidity ($), Sentiment (Fear & Greed)

### Layer 1 — One New API Call Per Analysis (yfinance, zero new keys)

```python
import yfinance as yf

def fetch_options_chain(ticker: str, target_dte_min=30, target_dte_max=60):
    tk = yf.Ticker(ticker)
    expiries = tk.options
    today = pd.Timestamp.today()

    # Find expiry closest to 45 DTE within 30-60 window
    chosen_expiry = None
    for exp in expiries:
        dte = (pd.Timestamp(exp) - today).days
        if target_dte_min <= dte <= target_dte_max:
            chosen_expiry = exp
            break

    if not chosen_expiry:
        return None, None, None

    chain = tk.option_chain(chosen_expiry)
    calls = chain.calls[['strike','bid','ask','volume','openInterest','impliedVolatility']]
    puts  = chain.puts [['strike','bid','ask','volume','openInterest','impliedVolatility']]

    # Compute chain-wide liquidity
    total_volume = calls['volume'].sum() + puts['volume'].sum()
    total_oi = calls['openInterest'].sum() + puts['openInterest'].sum()

    return calls, puts, {
        'expiry': chosen_expiry,
        'dte': (pd.Timestamp(chosen_expiry) - today).days,
        'total_volume': total_volume,
        'total_oi': total_oi
    }
```

**Fields obtained per contract**: strike, bid, ask, volume, openInterest, impliedVolatility (per-strike IV from Yahoo)

### Layer 2 — Locally Computed (py_vollib + math, zero API cost)

```
pip install py-vollib-vectorized
```

| Metric | Formula | Library |
|---|---|---|
| Mid price | (bid + ask) / 2 | Pure math |
| Bid-ask spread % | (ask - bid) / mid × 100 | Pure math |
| Intrinsic value | max(S - K, 0) for call; max(K - S, 0) for put | Pure math |
| Extrinsic value | mid - intrinsic | Pure math |
| Delta (Δ) | BSM analytical | py_vollib |
| Gamma (Γ) | BSM analytical | py_vollib |
| Theta (Θ) | BSM analytical | py_vollib |
| Vega (V) | BSM analytical | py_vollib |
| IV Rank | (IV_now - IV_52w_low) / (IV_52w_high - IV_52w_low) × 100 | SQLite history |
| IV Percentile | % of days in past year where IV < today's IV | SQLite history |
| Expected move (1σ) | S × IV × √(DTE/365) | Pure math |
| Probability ITM | N(d2) from BSM | py_vollib |
| Premium as % of stock | mid / S × 100 | Pure math |
| Days-to-earnings | earnings_date - today | Layer 0 |
| DTE | expiry_date - today | Pure math |

```python
from py_vollib_vectorized import vectorized_black as vb, vectorized_implied_volatility as viv
from py_vollib_vectorized.greeks import vectorized_delta, vectorized_gamma, vectorized_theta, vectorized_vega

def compute_greeks(flag, S, K, t, r, iv):
    """
    flag: 'c' for call, 'p' for put
    S: spot price, K: strike, t: time in years (DTE/365)
    r: risk-free rate (e.g., 0.05 for 5%)
    iv: implied volatility as decimal (e.g., 0.25 for 25%)
    """
    delta = vectorized_delta(flag, S, K, t, r, iv, model='black_scholes', return_as='numpy')
    gamma = vectorized_gamma(flag, S, K, t, r, iv, model='black_scholes', return_as='numpy')
    theta = vectorized_theta(flag, S, K, t, r, iv, model='black_scholes', return_as='numpy')
    vega  = vectorized_vega (flag, S, K, t, r, iv, model='black_scholes', return_as='numpy')
    return {'delta': delta, 'gamma': gamma, 'theta': theta, 'vega': vega}
```

**One New SQLite Table** (add to existing cachemanager.py):
```sql
CREATE TABLE IF NOT EXISTS iv_history (
    ticker TEXT,
    date TEXT,
    atm_iv REAL,
    PRIMARY KEY (ticker, date)
);
```
Store ATM IV daily when Options tab is loaded. IV Rank/Percentile usable after ~20 trading days.

### Layer 3 — User Input (UI fields, no API)
- "I own 100 shares" toggle → enables Covered Call
- "I am willing to own 100 shares" toggle → enables CSP
- Account size (for portfolio % cap calculations)

---

## PART 2 — THE PRICING MODEL: BLACK-SCHOLES (BSM)

**Gold standard for retail options Greeks? YES — with important context.**

BSM is the universal quoting convention used by every major retail broker:
- Interactive Brokers: BSM confirmed as "backbone of modern option pricing"
- Tastytrade / Dough: BSM analytical for all displayed Greeks
- TD Ameritrade (thinkorswim): BSM + Bjerksund-Stensland for American options
- Schwab / Fidelity: BSM base for retail Greeks display

**BSM assumptions vs reality**:
| Assumption | Reality | Practical Impact for Your Screener |
|---|---|---|
| Flat IV across strikes | IV varies by strike (volatility smile/skew) | Feed per-strike IV from yfinance → problem solved |
| European exercise only | US equity options are American | Negligible for ATM 30-60 DTE → use BSM; flag deep ITM near dividends |
| Constant volatility over life | IV changes over time (term structure) | Using expiry-specific IV from market partially corrects this |
| Log-normal returns | Fat tails exist | Acceptable for screening; not market-making |

**Verdict**: BSM via py_vollib is the correct model for your use case. Matches what IBKR, Tastytrade, Schwab show retail users. Difference vs binomial for ATM 30-60 DTE calls is < 1-2 cents — negligible for eligibility screening.

**UI Disclosure**: "Greeks calculated using Black-Scholes model. For deep ITM American-style options near ex-dividend dates, values may differ slightly from broker quotes."

---

## PART 3 — THE FOUR IMMUTABLE LAWS (40-Year Practitioner Rules)

These are distilled from:
- Reddit r/options — hundreds of loss post-mortems (IV crush, theta burn, earnings gaps)
- Reddit r/thetagang — professional sell-side practitioner rules
- Fidelity/Schwab educational research
- Traders Exclusive 50 Rules for Option Traders
- CBOE / OCC practitioner guidelines
- Cross-validated against market maker behavior and retail loss patterns

### 🔴 LAW 1 — NEVER BUY EXPENSIVE VOLATILITY (The #1 Wealth Destroyer)

**The Rule**: Before buying ANY option (call or put), check IV Rank. If IV Rank > 60, you are paying a premium that the market has already inflated. You will lose money to IV crush even if direction is correct.

**Where Retail Traders Die**:
- Buy calls before earnings because "the stock will beat" → stock gaps up 5% → option down 60% (IV crush)
- "I was right on direction but still lost money" — said by 70% of new options buyers
- Reddit r/options: earnings IV crush is the single most frequently cited catastrophic loss cause
- Example: NVDA earnings, stock +$15, option DOWN 84% due to IV crush + theta

**The Math**:
- Stock rallies 5% → delta gain = 0.5 × $5 = +$2.50
- IV collapses from 80% to 25% → vega loss = 0.20 × (0.80 - 0.25) × 100 = -$11.00
- NET: You were right on direction, lost $8.50 per share equivalent

**The Immutable Check**:
- IV Rank ≤ 40 → GREEN (buy options here)
- IV Rank 40-60 → YELLOW (proceed with caution, size down)
- IV Rank > 60 → RED (do NOT buy options; consider selling instead)

**Applied to your system**: yfinance gives per-strike IV. Your SQLite iv_history table enables IV Rank computation after 20 days.

---

### 🔴 LAW 2 — THETA IS NOT AN OPINION, IT IS A GUARANTEED LOSS RATE

**The Rule**: Every day you hold a long option, theta is a guaranteed loss that is independent of price direction. ATM options at 30 DTE lose approximately 0.3-0.5% of their value per calendar day to theta alone. This compounds non-linearly — it accelerates in the final 30 days.

**Where Retail Traders Die**:
- Buy 30-DTE ATM call. Stock stays flat for 10 days. Option down 25-40% from theta alone.
- "I'll just wait for the move" → theta kills you before the move happens
- Fidelity identifies "not understanding time decay" as one of top 7 options trading mistakes
- Reddit r/swingtrading: "Even though you were right, IV crush ate almost everything" — documented case, Apple 0DTE, expired worthless

**The Math** (documented retail loss case from Reddit):
- Day 1: Option $350, Theta -$8/day
- Day 5: Option $310, -$40 from theta alone, stock unchanged
- Day 20: Theta accelerates to -$15/day, Option $140 (-60%)
- Day 30: Stock nearly at target, Option $0 — expired worthless

**The Immutable Checks**:
1. DTE ≥ 30 days minimum for any long option (buying a 30-DTE option means theta is already accelerating)
2. Preferred range: 45-60 DTE for swing trades (5-45 day hold periods)
3. Exit rule: Never hold long option past 21 DTE unless deep ITM (theta acceleration kills value)
4. Theta budget: Daily theta cost must be < 1% of premium per day at entry
5. DTE < 20 → RED (theta acceleration makes buy-side options lottery tickets)

**Applied to your system**: Compute theta via py_vollib at entry. Surface as "Daily cost: $X.XX/day" in UI.

---

### 🔴 LAW 3 — NEVER HOLD LONG OPTIONS THROUGH EARNINGS (Unless Intentional Event Trade)

**The Rule**: Earnings events cause IV to spike in the days before, then collapse the moment results are announced (IV crush). For long option holders, this is a guaranteed value destruction event unless the underlying moves MORE than the expected move already priced into the option. This is an independent risk layer that overrides all directional analysis.

**Where Retail Traders Die**:
- Reddit r/options (documented, 2025): "Held weekly calls during earnings. Company BEAT estimates, surged next morning. Calls plummeted 60% due to IV crush. Just because a stock moves doesn't guarantee that your options will react as anticipated."
- The "right on earnings, lost on options" phenomenon is the single most common educated beginner mistake
- Reddit r/thetagang confirms: IV crush after known binary events is the mechanism that transfers wealth from option buyers to sellers

**The Mechanics**:
- Pre-earnings: IV spikes to 80-100% (market pricing in uncertainty)
- Post-earnings: IV collapses to 25-35% (uncertainty resolved)
- If stock moves exactly in-line with expected move: option is FLAT (IV crush = directional gain)
- Stock must move > 1.5× the priced-in expected move for long option buyers to profit

**The Immutable Check**:
- Earnings > 10 trading days away → GREEN
- Earnings 5-10 trading days away → YELLOW ("Earnings in X days — IV is elevated, expected move is $Y")
- Earnings ≤ 5 trading days away → RED (block all new long calls/puts)
- Exception: User explicitly flags trade as "earnings event play" → allow with mandatory warning and size cap

**Applied to your system**: Your backend already has earnings warning flags within 7 days. Extend to 10-day window for options, add "earnings IV premium" estimate (IV - historical IV) as a display metric.

---

### 🔴 LAW 4 — LIQUIDITY IS NON-NEGOTIABLE (Wide Spreads Are Silent Commissions)

**The Rule**: Entering or exiting an illiquid option with a wide bid-ask spread can cost 5-15% of the option's value on EACH side of the trade (entry + exit = 10-30% round-trip cost). This makes profitable trading mathematically impossible regardless of how good the directional call is.

**Where Retail Traders Die**:
- Traders Exclusive 50 Rules: "Don't trade illiquid options. The bid-ask spread is a transaction cost that is usually the highest transaction cost a trader has."
- Reddit r/options: "Stay away from illiquid option chains and weeklies" — repeated in nearly every professional advice thread
- Economic Times: "30% of account size in premium on one trade — won't even take a 2% gap down for option to halve"

**The Immutable Checks**:
- Bid-ask spread ≤ 5% of mid → GREEN
- Bid-ask spread 5-8% → YELLOW
- Bid-ask spread > 8% → RED (do not trade this contract)
- ATM contract volume ≥ 50 contracts today → GREEN
- ATM contract volume < 20 → RED
- Open interest on strike ≥ 500 → GREEN
- Open interest < 200 → RED
- Chain-wide daily volume ≥ 500 contracts → minimum for any options activity

**Applied to your system**: Computed locally from yfinance bid/ask/volume/OI. Zero additional API calls.

---

### 🔴 LAW 5 — POSITION SIZING: OPTIONS ARE NOT STOCKS (The Leverage Trap)

**The Rule**: Options have asymmetric leverage. A 2% adverse move in the stock can cause a 30-50% loss in an ATM option. Retail traders consistently size options positions the same as stock positions — this is the mechanism that turns small directional errors into account-destroying losses.

**Where Retail Traders Die**:
- Fidelity: "Most position sizing errors stem from greed — trading a position size too large for account size"
- Reddit r/options loss posts: "I went all-in because I was confident" — recurring pattern in every major loss thread
- Reddit r/thetagang: "Don't go too big. Leave capital for buffer zone" — repeated in professional sell-side advice

**The Immutable Rule**:
- Long calls/puts: Maximum premium at risk = 2-3% of total portfolio per trade
- Total long options premium across ALL positions: Never exceed 10% of portfolio
- CSP: Cash reserved = strike × 100. Maximum obligation = 20-25% of portfolio
- Covered call: You already own the shares; no additional capital rule, but monitor assignment risk

**Applied to your system**: Your account size is already in Settings. Compute:
- Premium cost = mid × 100 × contracts
- Portfolio % = premium cost / account size × 100
- Flag if > 2% (yellow) or > 3% (red) for long options

---

### 🔴 LAW 6 — NEVER ADD TO A LOSING OPTIONS POSITION

**The Rule**: When an option position moves against you, averaging down by buying more contracts compounds a bad position with a decaying asset. Unlike stocks, which can theoretically recover over years, options have a fixed expiry — the deeper ITM a loser goes, the faster the decay accelerates, and there is no "wait it out."

**Where Retail Traders Die**:
- Reddit r/options (2025): "I would enter a trade, see it go negative, and convince myself that buying more contracts would 'lower my average.' When the price continued to move against me, the losses became significant. This was driven by emotion."
- This violates your existing swing trade Law #2 (cut losses, let winners run) at the options level

**The Immutable Rule**:
- Pre-define maximum loss at entry: 50% of premium paid (for long options)
- If option is down 50% from entry price → exit. Full stop. No exceptions.
- For CSPs: The "2× premium rule" — if mark-to-market loss reaches 2× the premium received, close the position
- Never buy a new call/put in the same underlying to "average the cost" of an existing loser

**Applied to your system**: Surface the pre-defined exit price in the UI: "Exit if option falls below $X.XX (50% of premium paid)"

---

### 🔴 LAW 7 — ASSIGN/SELL THE RIGHT STRATEGY TO THE RIGHT MARKET REGIME

**The Rule**: Options are not direction-only instruments. The correct strategy is determined by the combination of: direction + IV regime + time horizon. Using a long call in a high-IV environment, or selling options in a trending bull market without adjusting strikes, systematically produces bad outcomes regardless of directional accuracy.

**The IV Regime Map** (the matrix that professional traders actually use):

| IV Regime | Directional Bias | Correct Strategy | Wrong Strategy |
|---|---|---|---|
| LOW IV (Rank < 30) | Bullish (BUY) | Long Call (buy cheap vol) | Covered Call (sell cheap vol — bad premium) |
| LOW IV (Rank < 30) | Neutral | Do nothing / wait | Any option sell (premium too thin) |
| MEDIUM IV (Rank 30-60) | Bullish (BUY) | Long Call OR CSP below support | — |
| MEDIUM IV (Rank 30-60) | Neutral (HOLD) | Covered Call | Long directional call |
| HIGH IV (Rank > 60) | Bullish (BUY) | CSP (sell high IV, get paid to wait) | Long Call (IV crush will kill you) |
| HIGH IV (Rank > 60) | Neutral (HOLD) | Covered Call (maximize premium) | Long Call |
| HIGH IV (Rank > 60) | Bearish (AVOID) | Long Put ONLY if IV Rank < 70 (puts are most expensive in fear) | Any long option |
| EXTREME IV (Rank > 85) | Any | No new long options. Sell-side only with caution | ALL long options |

---

## PART 4 — THE FOUR CHECKLISTS (With Green/Yellow/Red)

### UNIVERSAL DISQUALIFIERS — Run FIRST, Block ALL Strategies

| Check | RED (Block All) | YELLOW (Warn) | GREEN (OK) | Data Source |
|---|---|---|---|---|
| Chain-wide daily options volume | < 200 contracts | 200-500 | ≥ 500 | Layer 1 — local sum |
| Avg daily underlying volume | < 500K shares | 500K-1M | ≥ 1M | Layer 0 |
| VIX extreme | > 40 | 30-40 | < 30 | Layer 0 |
| Earnings proximity | ≤ 5 days | 5-10 days | > 10 days | Layer 0 |
| Stock price | < $10 | $10-20 | ≥ $20 | Layer 0 |
| IV Percentile extreme | > 95 (no buys) | 85-95 (buys risky) | < 85 | SQLite history |
| Ticker type | Leveraged ETF / ETN | Thin ADR | Standard US stock | yfinance quoteType |

---

### STRATEGY 1: LONG CALL (Call Buy)
**Pre-condition**: Verdict = BUY, Technical = Strong. If not met → grey card "Not Applicable"

| # | Rule | GREEN | YELLOW | RED | Source | Local? |
|---|---|---|---|---|---|---|
| 1 | Underlying price | ≥ $20 | $10-20 | < $10 | Layer 0 | ✅ |
| 2 | Avg daily stock volume | ≥ 1M | 500K-1M | < 500K | Layer 0 | ✅ |
| 3 | Chain-wide options volume | ≥ 500 | 200-500 | < 200 | Layer 1 sum | ✅ |
| 4 | ATM contract volume | ≥ 50 | 20-50 | < 20 | Layer 1 | ✅ |
| 5 | ATM open interest | ≥ 500 | 200-500 | < 200 | Layer 1 | ✅ |
| 6 | Bid-ask spread % | ≤ 5% | 5-8% | > 8% | Layer 1 + calc | ✅ |
| 7 | **IV Rank** | ≤ 40 | 40-60 | > 60 | SQLite iv_history | ✅ |
| 8 | VIX level | < 20 | 20-30 | > 30 | Layer 0 | ✅ |
| 9 | DTE of chosen expiry | 30-60 | 20-30 or 60-90 | < 20 or > 90 | Layer 1 | ✅ |
| 10 | Delta of ATM call | 0.40-0.60 | 0.35-0.40 | < 0.35 or > 0.70 | py_vollib | ✅ |
| 11 | **Earnings proximity** | > 10 days | 5-10 days | ≤ 5 days | Layer 0 | ✅ |
| 12 | SPY regime | Above 200 SMA | ±2% of 200 SMA | Below 200 SMA | Layer 0 | ✅ |
| 13 | Expected move vs R1 gap | R1 gap ≥ 1.5× premium | 1.2-1.5× | < 1.2× | Layer 0 R1 + Layer 1 | ✅ |
| 14 | ADX | ≥ 25 | 20-25 | < 20 | Layer 0 | ✅ |
| 15 | **Daily theta cost** | < 0.5% of premium/day | 0.5-1.0%/day | > 1.0%/day | py_vollib | ✅ |
| 16 | Portfolio premium cap | ≤ 2% of account | 2-3% | > 3% | Settings + calc | ✅ |
| 17 | Pre-defined exit price | Set at 50% of premium | — | Not set | Calc | ✅ |

**Badge Logic**: Any RED → 🔴 NOT ELIGIBLE | 2+ YELLOW → 🟡 CAUTION | ≤1 YELLOW, 0 RED → 🟢 ELIGIBLE

---

### STRATEGY 2: COVERED CALL (Call Sell)
**Pre-condition**: Verdict = HOLD or neutral BUY, AND user owns ≥ 100 shares (UI toggle)

| # | Rule | GREEN | YELLOW | RED | Source | Local? |
|---|---|---|---|---|---|---|
| 1 | Owns ≥ 100 shares per contract | Yes | — | No | UI input | N/A |
| 2 | **IV Rank** | ≥ 60 | 40-60 | < 40 | SQLite iv_history | ✅ |
| 3 | Strike above R1 | Strike ≥ R1 | Strike between price & R1 | Strike < current price | Layer 0 R1 + Layer 1 | ✅ |
| 4 | Strike OTM % | 5-15% above spot | 2-5% or 15-20% | < 2% (assignment risk) | Layer 1 + Layer 0 | ✅ |
| 5 | DTE | 20-45 days | 15-20 or 45-60 | < 15 or > 60 | Layer 1 | ✅ |
| 6 | Call delta | 0.20-0.35 | 0.35-0.45 | > 0.45 | py_vollib | ✅ |
| 7 | Bid-ask spread % | ≤ 5% | 5-8% | > 8% | Layer 1 | ✅ |
| 8 | Open interest on strike | ≥ 500 | 200-500 | < 200 | Layer 1 | ✅ |
| 9 | **Earnings proximity** | > 10 days | 5-10 days | ≤ 5 days | Layer 0 | ✅ |
| 10 | Ex-dividend within 10 days + call ITM | No | — | Yes + ITM | yfinance dividends | ✅ |
| 11 | VIX | < 25 | 25-30 | > 30 | Layer 0 | ✅ |
| 12 | ADX | ≥ 20 | 15-20 | < 15 | Layer 0 | ✅ |
| 13 | **IV Rank minimum** | ≥ 40 (premium must be worth it) | 30-40 | < 30 | SQLite | ✅ |

---

### STRATEGY 3: LONG PUT (Put Buy)
**Pre-condition**: Verdict = AVOID, Technical = Weak. If not met → grey card "Not Applicable"

| # | Rule | GREEN | YELLOW | RED | Source | Local? |
|---|---|---|---|---|---|---|
| 1 | Clear downtrend | Price < 50 SMA < 200 SMA | Mixed signals | Uptrend | Layer 0 | ✅ |
| 2 | **IV Rank** | ≤ 40 | 40-60 | > 60 (puts expensive in fear) | SQLite | ✅ |
| 3 | VIX level | < 25 | 25-35 | > 35 | Layer 0 | ✅ |
| 4 | DTE | 30-75 days | 20-30 | < 20 or > 90 | Layer 1 | ✅ |
| 5 | Put delta (absolute) | 0.35-0.55 | 0.25-0.35 | < 0.25 (lottery) | py_vollib | ✅ |
| 6 | Strike just below S1 | Strike ≤ S1 and ≥ S2 | Strike = S1 | Strike > S1 | Layer 0 S1/S2 + Layer 1 | ✅ |
| 7 | Bid-ask spread % | ≤ 5% | 5-8% | > 8% | Layer 1 | ✅ |
| 8 | Open interest | ≥ 500 | 200-500 | < 200 | Layer 1 | ✅ |
| 9 | **Earnings proximity** | > 10 days | 5-10 days | ≤ 5 days | Layer 0 | ✅ |
| 10 | Portfolio put premium cap | ≤ 5% of account | 5-8% | > 10% | Settings + calc | ✅ |
| 11 | Underlying price | ≥ $10 | $5-10 | < $5 | Layer 0 | ✅ |
| 12 | ADX (trend down) | ≥ 20 | 15-20 | < 15 | Layer 0 | ✅ |
| 13 | **Daily theta cost** | < 0.5% of premium/day | 0.5-1.0%/day | > 1.0%/day | py_vollib | ✅ |
| 14 | Pre-defined exit price | Set at 50% of premium | — | Not set | Calc | ✅ |

---

### STRATEGY 4: CASH-SECURED PUT (Put Sell)
**Pre-condition**: Verdict = BUY or strong HOLD, price extended above R1 or near 52W high, user willing to own shares (UI toggle)

| # | Rule | GREEN | YELLOW | RED | Source | Local? |
|---|---|---|---|---|---|---|
| 1 | Willing to own 100 shares | Yes | — | No | UI toggle | N/A |
| 2 | Strike at or below S1 | Strike ≤ S1 | S1 < Strike < price | Strike ≥ price | Layer 0 S1 + Layer 1 | ✅ |
| 3 | Strike OTM % | 5-15% below spot | 3-5% | < 3% | Layer 1 + Layer 0 | ✅ |
| 4 | **IV Rank** | ≥ 50 | 35-50 | < 35 (premium too thin) | SQLite | ✅ |
| 5 | DTE | 20-60 days | 15-20 or 60-75 | < 15 | Layer 1 | ✅ |
| 6 | Put delta (absolute) | 0.25-0.40 | 0.20-0.25 | > 0.45 | py_vollib | ✅ |
| 7 | Cash required ≤ portfolio cap | Obligation ≤ 20% of account | 20-25% | > 25% | Settings + strike | ✅ |
| 8 | Bid-ask spread % | ≤ 5% | 5-8% | > 8% | Layer 1 | ✅ |
| 9 | Open interest | ≥ 500 | 200-500 | < 200 | Layer 1 | ✅ |
| 10 | **Earnings proximity** | > 10 days | 5-10 days | ≤ 5 days | Layer 0 | ✅ |
| 11 | Fundamental quality | Strong or Decent | — | Weak | Layer 0 | ✅ |
| 12 | VIX | < 30 | 25-30 | > 30 | Layer 0 | ✅ |
| 13 | **CSP loss rule** | Pre-set exit at 2× premium received | — | No exit plan | Calc | ✅ |

---

## PART 5 — THE DECISION MATRIX

Given system verdict + IV regime → recommended strategy (read this table before running any checklist):

| System Verdict | IV Rank | Recommended | Do NOT Use | Why |
|---|---|---|---|---|
| BUY | Low (< 30) | **Long Call** (cheap vol) | Covered Call | Premium too thin to sell |
| BUY | Medium (30-60) | **Long Call or CSP** | — | Balanced regime |
| BUY | High (> 60) | **CSP below support** (sell high IV) | Long Call | IV crush will destroy call buyers |
| HOLD | Low (< 30) | **Nothing / wait** | Any sell | Selling thin premium wastes the trade |
| HOLD | Medium (30-60) | **Covered Call** (5-15% OTM, 20-45 DTE) | Long directional | Neutral stock + decent premium = ideal CC |
| HOLD | High (> 60) | **Covered Call** (maximize premium) | Long Call | Premium rich, direction neutral |
| AVOID | Any | **Long Put only if IV Rank ≤ 40** | Long Call, CC, CSP | Long put when fear has NOT spiked yet |
| AVOID | High (> 60) | **Nothing** | Long Put (too expensive) | Puts priced with fear premium; IV crush kills |

---

## PART 6 — UI IMPLEMENTATION LOGIC

```
1. Load stock analysis result (already done by existing system)

2. Run Universal Disqualifiers (7 checks)
   → Any RED:  Show red banner "Options not eligible — [reason]"
   → All pass: Proceed to individual strategies

3. For each of the 4 strategies:
   a. Check pre-condition gate (verdict match + user toggles)
      → Gate fails: Grey card "Not applicable for [BUY/HOLD/AVOID]"
      → Gate passes: Run checklist (13-17 rules)

   b. Display each rule as a row:
      [🟢/🟡/🔴] Rule name | Your value | Threshold | Tooltip explanation

   c. Assign badge:
      - Any RED         → 🔴 NOT ELIGIBLE
      - 2+ YELLOW       → 🟡 CAUTION — proceed with care
      - 0-1 YELLOW      → 🟢 ELIGIBLE

4. Summary strip (top of Options tab):
   [Long Call: 🟢 ELIGIBLE] [Covered Call: ⬜ N/A] [Long Put: ⬜ N/A] [CSP: 🟡 CAUTION]

5. For ELIGIBLE strategies, show suggested contract:
   - Expiry: [date] ([X] DTE)
   - Suggested strike: $[K] ([Y]% OTM, Δ=[Z])
   - Mid price: $[P] | Spread: [S]%
   - Daily theta cost: $[T]/day
   - Pre-defined exit: $[P × 0.50] (50% stop)
   - Expected move by [target date]: ±$[EM]
   - IV Rank: [rank] / 100
```

---

## PART 7 — SPECIFIC RISK WARNINGS (Contextual, Not Generic)

These must appear inline in the UI, not in a footer:

| Trigger | Warning Text |
|---|---|
| IV Rank > 60, long option recommended | "⚠️ IV Rank is [X]/100 — options are expensive. You may lose money even if the stock moves in your favor (IV crush). Consider selling instead." |
| Earnings within 10 days | "⚠️ [TICKER] reports earnings on [DATE] ([N] trading days). IV is elevated by approx [X]% above historical. Options buyers risk IV crush regardless of earnings outcome." |
| Bid-ask spread > 5% | "⚠️ Spread is [X]% — you are paying $[Y] in transaction cost before the trade begins. This is [Z]% of the option's value." |
| VIX > 30 | "⚠️ Market stress (VIX [X]). Options are pricing in elevated uncertainty. All option prices are inflated above historical norms." |
| Any long option | "This position can lose 100% of the premium paid ($[X]). Maximum risk: $[X]. Pre-defined exit: $[X × 0.5] (50% stop)." |
| CSP | "If assigned, you will own 100 shares of [TICKER] at $[strike], a total obligation of $[strike × 100]. This represents [Y]% of your account." |
| Covered Call | "If the stock closes above $[strike] at expiry, your shares will be called away at $[strike] per share regardless of current market price." |

---

## PART 8 — WHAT NOT TO BUILD IN V1

| Feature | Reason to Exclude |
|---|---|
| Multi-leg spreads (verticals, iron condors, strangles) | Too complex; error-prone; hard to explain in a simple UI |
| Naked call selling | Unlimited upside risk; incompatible with retail safety mandate |
| Real-time gamma/vega dashboards | Encourages day-trading behavior; swing timeframe doesn't need intraday Greeks |
| Automatic roll logic | Requires full portfolio integration and user intent tracking |
| Leveraged/inverse ETFs, thin ADRs | Complex behavior, borrow constraints, path-dependent |
| 0DTE options | 70% of 0DTE options expire worthless (SSRN study); lottery, not strategy |
| Options on stocks under $10 | Options structure poor; manipulation risk high |

---

## PART 9 — GITHUB PROJECTS FOR IMPLEMENTATION

| Project | Use Case | Status |
|---|---|---|
| `py_vollib` / `py_vollib_vectorized` | BSM pricing, IV solver, all 4 Greeks — vectorized, fast | **PRIMARY — use this** |
| `yassinemaaroufi/MibianLib` | Alternative BSM implementation, simpler API | Secondary / fallback |
| `mh2rashi/OptionGreekPricing` | Educational reference for BSM + Binomial | Reference only |
| `alpacahq/options-wheel` | Wheel strategy (CSP → Covered Call) template | Mine for CSP/CC logic |
| `zeta-zetra/chart_patterns` | Chart pattern detection augmentation | For patterndetection.py upgrade |
| `louisnw01/lightweight-charts-python` | Candlestick + S/R + pattern overlay visualization | For React chart tab |

---

## PART 10 — WMT LIVE EXAMPLE (February 2026)

**From your swing trade analyzer output:**
- Price: $124.87 | 52W High: $134.65 | 52W Low: $79.81
- Technical: STRONG (8/8 TT, RSI 52, ADX 33.5, RS 1.07×)
- Fundamental: STRONG
- Verdict: BUY | Regime: Neutral
- S1: $121.62 | S2: $116.47 | R1: $134.69 (7.9% above)
- ATR: $4.02 | 8 EMA: $127.91 | 21 EMA: $125.16

**Long Call Eligibility — What You Already Know:**
| Check | Value | Status |
|---|---|---|
| Price ≥ $20 | $124.87 | 🟢 |
| Volume | $3.9B daily | 🟢 |
| ADX ≥ 25 | 33.5 | 🟢 |
| SPY regime | Neutral | 🟢 |
| R1 gap vs premium | $9.82 gap; ~3.5 premium = 2.8× | 🟢 |
| Verdict + Technical | BUY + Strong | 🟢 |
| Earnings | Need to verify WMT next date | ❓ |
| **IV Rank** | **Requires yfinance chain + history** | ❓ |
| **ATM volume/OI** | **Requires yfinance chain fetch** | ❓ |
| **Bid-ask spread** | **Requires yfinance chain fetch** | ❓ |
| **Theta cost** | **Requires py_vollib** | ❓ |

**Conclusion**: 3 of the most critical checks (IV Rank, liquidity, theta) require one new yfinance API call and py_vollib. Direction, trend quality, and R:R are confirmed by existing system. WMT is a probable GREEN candidate but cannot be confirmed without the options chain data.

---

## PART 11 — BUILD ORDER (Priority Sequence)

1. **Flask**: Add `iv_history` table to SQLite via cachemanager.py
2. **Flask**: Add `/api/options/<ticker>` endpoint — yfinance chain fetch, ATM identification, chain metrics
3. **Python**: Install py_vollib_vectorized; add `options_analytics.py` module for Greeks + IV Rank + spread %
4. **Flask**: Wire analytics into endpoint response — return full options JSON per strategy
5. **React**: Add "Options" tab to navigation
6. **React**: Implement Universal Disqualifiers banner
7. **React**: Implement 4 strategy cards with checklist rows (green/yellow/red icons)
8. **React**: Add summary strip and suggested contract display
9. **React**: Add contextual warnings (IV crush, earnings, spread, theta)
10. **Testing**: Run on WMT, NVDA, AAPL, PLTR, META (range of IV regimes and liquidity profiles)

---

*This document represents the complete research context for the Swing Trade Analyzer Options Module.*
*Load at the start of any new conversation to restore full project context.*
*Research sources: Reddit r/options, r/thetagang, r/swingtrading, Fidelity, Schwab, CBOE, Traders Exclusive, SSRN, Interactive Brokers Quant, Economic Times, InsiderFinance, Option Alpha.*
