# Perplexity Deep Research Prompt — Options Tab for Swing Trade Analyzer

> **Instructions to user:** Copy everything below the line into Perplexity Deep Research. Also upload your README.md for full system context.

---

## Context: What Our System Already Does

We have a **Swing Trade Analyzer** (React + Python Flask) that scans US stocks using TradingView data and produces categorical assessments (BUY/HOLD/AVOID) based on:
- **Technical analysis**: Trend Template (Minervini 8-criteria), RSI, ADX, Relative Strength vs SPY, EMA/SMA structure
- **Fundamental analysis**: ROE, Revenue Growth, Debt/Equity, EPS Growth
- **Risk/Macro**: VIX level, SPY vs 200 SMA, market regime detection
- **Pattern detection**: Cup & Handle, Flat Base, VCP, High Tight Flag with breakout quality scoring
- **Support/Resistance**: Agglomerative clustering for S&R levels, trade viability (R:R ratio)
- **Decision Matrix**: 3-layer verdict (Technical + Fundamental + Risk) → BUY/HOLD/AVOID with entry preference (Aggressive/Standard/Conservative)

The system already knows **support and resistance levels**, **trend direction**, **RSI**, **ADX**, and **relative strength** for every stock it analyzes. We want to extend it with a basic Options tab.

## What I Already Know (Don't Re-teach These Basics)

I understand:
- The 4 basic strategies: Call Buy (extremely bullish), Put Buy (extremely bearish), Call Sell/Covered Call (neutral-to-bearish, price stays below resistance), Put Sell/Cash-Secured Put (neutral-to-bullish, price stays above support)
- Buying = debit (pay premium), Selling = credit (collect premium)
- Strike selection ties to support/resistance levels
- Intrinsic value: Call = Spot - Strike, Put = Strike - Spot
- Extrinsic value decays over time (theta)
- Sellers prefer ATM strikes (exponential decay) with shorter expiry
- Buyers prefer ITM strikes (intrinsic cushion) with longer expiry
- Implied Volatility spikes around earnings, acquisitions, macro events
- For every buyer there's a seller; can exit before expiry

## What I Need From This Research

### Part 1: Free Data Sources for Options in the US Market

What Python-accessible data sources provide options chain data for US stocks? For each source, tell me:
- What data fields are available (strike, bid, ask, volume, OI, IV, Greeks, expiry dates)
- What's missing (e.g., IV Rank, IV Percentile, historical IV)
- Rate limits and reliability
- Python package name and example code

Sources to evaluate: yfinance, CBOE directly, Tradier API (free tier), Polygon.io (free tier), Alpha Vantage, any other free source.

**Critical question**: Can we get Delta, Gamma, Theta, Vega from any free source? If not, can we calculate Greeks ourselves using Black-Scholes with the IV that yfinance provides? Is that calculation reliable enough for a basic screening tool?

### Part 2: Call Buy Eligibility Checklist

Given a stock our system already rates as **BUY** (Strong Technical + Favorable Risk), what additional criteria make it eligible for a **Call Buy** (long call) recommendation?

Provide an industry-standard, conservative checklist that minimizes the chance of a bad recommendation. For each criterion, explain:
- The threshold and why
- What data source provides it
- What happens if you skip this check (the risk)

Consider at minimum:
- Minimum average daily options volume (liquidity)
- Maximum bid-ask spread (percentage)
- Minimum open interest
- IV Rank / IV Percentile thresholds (are we buying expensive options?)
- Optimal DTE range for swing trades (5-45 day holding periods)
- Delta range for strike selection
- Earnings proximity (avoid or embrace?)
- Underlying stock minimum price (penny stocks with options?)
- How our existing support/resistance levels inform strike selection

### Part 3: Covered Call (Call Sell) Eligibility Checklist

For stocks our system rates as **HOLD** or where the verdict is "neutral-to-slightly-bullish" — what makes a stock eligible for a covered call recommendation?

Same format: criterion, threshold, data source, risk if skipped. Consider:
- Must own 100 shares (or this is hypothetical?)
- IV Rank thresholds (selling when premium is rich)
- Strike selection relative to resistance levels (our system provides these)
- DTE sweet spot for maximum theta decay
- Delta range (probability of assignment)
- Earnings filter (sell before or after?)
- Dividend considerations
- Maximum acceptable assignment risk

### Part 4: Put Buy Eligibility Checklist

For stocks showing **AVOID** signals or where the system detects bearish patterns — what criteria for a protective put or speculative put buy?

Same format. Consider:
- When is a put buy justified vs just avoiding the stock?
- IV considerations (puts are expensive during fear)
- Strike selection relative to support levels
- DTE range
- Delta range
- VIX level considerations (our system tracks VIX)
- Maximum percentage of portfolio in put buys

### Part 5: Cash-Secured Put (Put Sell) Eligibility Checklist

For stocks our system rates positively but that are "too expensive" at current price — what makes them eligible for a cash-secured put (selling put to get paid to wait for a pullback)?

Same format. Consider:
- Strike selection at or below support level
- IV Rank thresholds (sell puts when IV is elevated)
- Capital requirement calculations
- Maximum risk as percentage of portfolio
- DTE range
- Earnings proximity
- Assignment scenario planning (what if assigned?)

### Part 6: Universal Disqualifiers

What conditions should **automatically disqualify** ANY options trade regardless of strategy? Provide the "never trade options on this stock" checklist:
- Minimum average options volume across all strikes
- Minimum underlying stock volume
- Pending binary events (FDA approvals, merger votes, etc.)
- Halted or restricted stocks
- Extreme IV (above what percentile is "too expensive to buy"?)
- ADR/foreign stocks with options quirks
- Weekly vs monthly expiration considerations
- Any other red flags

### Part 7: Simple Decision Matrix

Given our system already produces: BUY/HOLD/AVOID verdict, support/resistance levels, RSI, ADX, trend direction, and market regime — provide a simple decision matrix:

| System Verdict | Market Regime | Recommended Options Strategy | Key Filter |
|---|---|---|---|
| BUY | Favorable | ? | ? |
| BUY | Neutral | ? | ? |
| HOLD | Favorable | ? | ? |
| HOLD | Neutral | ? | ? |
| AVOID | Any | ? | ? |

### Part 8: What NOT to Build (Scope Limitation)

For a basic, responsible options screener, what should we explicitly NOT include?
- Multi-leg strategies (spreads, iron condors, strangles)?
- Naked options selling?
- Options on ETFs vs individual stocks — any difference?
- Real-time Greeks monitoring?
- Position sizing for options?

What's the minimum viable options tab that's genuinely useful without being dangerous for a retail swing trader?

### Part 9: Risk Disclaimers

What specific disclaimers and warnings must an options screening tool display? Not generic "options are risky" but specific, actionable warnings:
- When IV is elevated (quantify)
- When earnings are within X days
- When liquidity is insufficient (quantify)
- When the recommendation conflicts with broad market conditions
- Maximum position size guidance

## Output Format

For each checklist, provide:
1. **The rule** (one clear sentence)
2. **The threshold** (specific number)
3. **Why** (one sentence explanation)
4. **Data needed** (which API field)
5. **Priority** (Must-Have vs Nice-to-Have)

Prioritize safety over opportunity. A missed trade is always better than a bad options recommendation. The goal is: if our system says "eligible for call buy," the user should be able to trust that the basic hygiene checks have been done.


--------------------------------------- RESULTS -----------------

## Part 1 – Python‑Accessible Options Data Sources (US)

### 1. yfinance (Yahoo Finance scrape)

- **Fields** – Expiries list, for each expiry: strike, lastPrice, bid, ask, change, percentChange, volume, openInterest, impliedVolatility, inTheMoney, contractSymbol. [youtube](https://www.youtube.com/watch?v=0xTbug30QsE)
- **Missing** – No official Greeks, no IV rank/percentile, no historical IV series; IV values can be noisy or inconsistent by strike/maturity. [github](https://github.com/schepal/yahoo_vol)
- **Rate limits / reliability** – Unofficial HTML/JSON scrape, subject to throttling and occasional incorrect IVs; fine for end‑of‑day screening but not guaranteed stable. [chasethedevil.github](https://chasethedevil.github.io/post/yahoo_finance_implied_volatility/)
- **Python package** – `yfinance`. [youtube](https://www.youtube.com/watch?v=0xTbug30QsE)

Example:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
expiries = ticker.options
chain = ticker.option_chain(expiries[0])   # first expiry
calls = chain.calls[['contractSymbol','strike','bid','ask',
                     'volume','openInterest','impliedVolatility']]
```

**Greeks?** Not provided; you must compute them (see below).

***

### 2. Tradier API (developer / free tier)

- **Fields** – For each option: symbol, strike, type, bid, ask, last, volume, open_interest, implied_volatility, greeks (delta, gamma, theta, vega, rho) on market‑data endpoints. [reddit](https://www.reddit.com/r/algotrading/comments/hgji59/free_api_for_option_chains/)
- **Missing** – No IV rank/percentile; historical IV/Greeks require storing your own history.  
- **Rate limits / reliability** – Public guidance and user reports: ~120 requests/min on free dev tiers; options Greeks often delayed (15–60 minutes), but adequate for swing‑timeframe analytics. [reddit](https://www.reddit.com/r/options/comments/1hrbbii/where_to_get_options_data_with_greeks/)
- **Python** – REST + any HTTP client; or community wrappers.

Example:

```python
import requests

base = "https://sandbox.tradier.com/v1/markets/options/chains"
params = {"symbol": "AAPL", "expiration": "2026-03-20", "greeks": "true"}
headers = {"Authorization": "Bearer YOUR_TOKEN",
           "Accept": "application/json"}

r = requests.get(base, params=params, headers=headers)
data = r.json()["options"]["option"]   # list of contracts
```

***

### 3. Polygon.io (free “Starter” plan)

- **Fields** – Option contract metadata and quotes/trades: symbol, underlying, strike, type, expiration, bid, ask, last, volume, open_interest; real‑time IV and Greeks (delta, gamma, theta, vega) available on options endpoints, but **historical Greeks/IV not yet supported**. [reddit](https://www.reddit.com/r/PolygonIO/comments/1k55sx4/does_polygon_io_also_provides_the_historical/mofozm2/)
- **Missing** – Historical IV / Greeks; IV rank/percentile; some features gated to paid plans.  
- **Rate limits / reliability** – Free plan is limited in request volume; fine for a few dozen chains per day (consult current docs). Historical quotes are available; Greeks real‑time only. [youtube](https://www.youtube.com/watch?v=87O9qxfMJ-g)
- **Python** – `polygon-api-client`. [youtube](https://www.youtube.com/watch?v=87O9qxfMJ-g)

Example:

```python
from polygon import RESTClient

client = RESTClient("YOUR_KEY")
resp = client.list_options_contracts(underlying_ticker="AAPL", limit=100)
for c in resp:
    print(c.symbol, c.strike_price, c.expiration_date)
```

(Then call quotes endpoint for bid/ask/greeks.)

***

### 4. Alpha Vantage (Options APIs)

- **Fields** – They advertise US options chains with IV and Greeks, but this lives under **“Realtime Options Premium API”**, i.e., paid tier only. [scribd](https://www.scribd.com/document/791952203/API-Documentation-Alpha-Vantage)
- **Missing on free tier** – Options chains; free plan is for stocks/FX/crypto/indicators only. [openpublicapis](https://www.openpublicapis.com/api/alpha-vantage)
- **Conclusion** – Not useful for free options data beyond maybe EOD under premium; skip for v1.

***

### 5. CBOE, TD Ameritrade/Schwab, others

- **CBOE website** – Public HTML option chains but no official free JSON API; scraping is brittle and likely against ToS for systematic use. Treat as out‑of‑scope for a robust backend.  
- **TD Ameritrade / Schwab API** – Provides full chains + Greeks for account holders via developer API; requires brokerage account and OAuth setup, not general‑purpose. [reddit](https://www.reddit.com/r/algotrading/comments/mhhxpd/free_api_for_options_data/)
- **Others** – Specialist vendors (Databento, Massive, etc.) have excellent options APIs but are paid/usage‑metered. [massive](https://massive.com/options)

***

### Greeks via Black‑Scholes

- Free APIs rarely give **all** Greeks with unconstrained use; Tradier and Polygon do, but with delays/plan limits. [reddit](https://www.reddit.com/r/options/comments/1hrbbii/where_to_get_options_data_with_greeks/)
- For a screening tool, **computing Greeks yourself is standard**:
  - Use market mid price, strike, spot, dividend yield, risk‑free rate, and time to expiry in a Black‑Scholes or Black‑Scholes‑Merton model. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
  - Either:
    - Use IV from yfinance (approximate; sometimes noisy), or [chasethedevil.github](https://chasethedevil.github.io/post/yahoo_finance_implied_volatility/)
    - Solve for IV numerically (e.g., `scipy.optimize.brentq`) given market option price. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
- For swing‑timeframes and ranking/screening (not intraday scalping), **BS Greeks from your own IV solver are more than good enough**—the model error is small relative to your other uncertainties. [chasethedevil.github](https://chasethedevil.github.io/post/yahoo_finance_implied_volatility/)

***

## Part 2 – Call Buy Eligibility Checklist (Long Call)

Assume underlying already has **BUY + Favorable Risk** in your engine. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)

#### 2.1 Liquidity / Market Quality

1. **Rule**: Only trade options where the **average daily options volume ≥ 500 contracts across the chain**.  
   - **Threshold**: ≥ 500 contracts (all strikes, last 20 trading days).  
   - **Why**: Ensures reasonable two‑sided interest; below this, fills and exits become uncertain.  
   - **Data needed**: Per‑contract volume → roll up by underlying using yfinance/Tradier/Polygon. [youtube](https://www.youtube.com/watch?v=FQ9hVHV_xV8)
   - **Priority**: **Must‑Have**.

2. **Rule**: Per‑contract **volume ≥ 50 contracts** on the specific strike you recommend.  
   - **Threshold**: ≥ 50 today + non‑zero OI.  
   - **Why**: Avoid illiquid strikes where spreads can blow out during volatility.  
   - **Data**: `volume`, `openInterest` from chain. [youtube](https://www.youtube.com/watch?v=0xTbug30QsE)
   - **Priority**: **Must‑Have**.

3. **Rule**: **Bid‑ask spread ≤ 8% of mid price** for that option.  
   - **Threshold**: (ask − bid) / mid ≤ 0.08.  
   - **Why**: Wide spreads can eat most of the theoretical edge on a swing‑trade timeframe.  
   - **Data**: `bid`, `ask`.  
   - **Priority**: **Must‑Have**.

4. **Rule**: **Open interest ≥ 500** on the target strike, ≥ 5,000 chain‑wide.  
   - **Threshold**: OI strike ≥ 500; total OI underlying ≥ 5,000.  
   - **Why**: OI indicates standing interest; very low OI raises slippage and early expiration risk.  
   - **Data**: `openInterest`.  
   - **Priority**: **Must‑Have**.

***

#### 2.2 Volatility / IV Regime

5. **Rule**: Only buy calls when **IV Rank ≤ 60** and **IV Percentile ≤ 70**.  
   - **Threshold**: IV rank 0–60, percentile 0–70 over 1‑year history.  
   - **Why**: Buying options when IV is extreme (≥ 70–80) means overpaying; theta and IV crush work against you. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
   - **Data**: Need to compute IV Rank/Percentile from your own stored IV history; raw IV from yfinance/Tradier/Polygon. [youtube](https://www.youtube.com/watch?v=FQ9hVHV_xV8)
   - **Priority**: **Must‑Have**.

6. **Rule**: Avoid long calls when **VIX > 30** (panic regime) unless explicitly speculating on volatility.  
   - **Threshold**: VIX ≤ 30 for standard swing calls.  
   - **Why**: Elevated VIX inflates premiums across the board; post‑event mean reversion crushes call value even if direction is right. [macro-ops](https://macro-ops.com/richard-dennis-turtle-trading-strategy-explained/)
   - **Data**: Your existing VIX endpoint. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
   - **Priority**: **Must‑Have**.

***

#### 2.3 Time & Strike Selection

7. **Rule**: Use expiries with **30–90 DTE** for swing trades with 5–45 day hold.  
   - **Threshold**: 30 ≤ days to expiry ≤ 90.  
   - **Why**: Shorter DTE (<20) has brutal theta; longer (>90) overpays for time you won’t use. 30–60 is most common sweet spot.  
   - **Data**: Expiry date vs current date.  
   - **Priority**: **Must‑Have**.

8. **Rule**: Choose **delta between 0.40 and 0.65**.  
   - **Threshold**: 0.40 ≤ |Δ| ≤ 0.65.  
   - **Why**: Balances leverage and intrinsic value; deeper ITM (Δ>0.7) behaves like stock; OTM (Δ<0.3) is lottery‑ticket behavior. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
   - **Data**: `delta` from Tradier/Polygon, or Black‑Scholes Δ.  
   - **Priority**: **Must‑Have**.

9. **Rule**: For bullish breakouts, pick a strike **just above nearest strong support and below first resistance**, so that your **profit target in the stock reaches at least 1.5× the option’s cost in intrinsic gain**.  
   - **Threshold**: Strike ≤ entry + 0.25× (R target in stock); ensure projected move to your system’s target (e.g., R1) creates ≥30–50% option gain at Δ level.  
   - **Why**: Aligns with your existing S/R engine and R:R logic. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
   - **Data**: Support/resistance levels from `apisr`, projected move, Δ.  
   - **Priority**: **Must‑Have**.

***

#### 2.4 Event & Underlying Filters

10. **Rule**: **No new call buys within ±5 trading days of earnings** unless explicitly tagged as “event‑speculative.”  
    - **Threshold**: |earnings_date − today| > 5 sessions.  
    - **Why**: Earnings IV spikes and subsequent crush dominate P/L; you don’t want your default screener implicitly recommending event gambling. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
    - **Data**: Next earnings date from Finnhub/FMP.  
    - **Priority**: **Must‑Have** (for non‑event profile).

11. **Rule**: Underlying stock **price ≥ $20** and **average daily stock volume ≥ 1M shares**.  
    - **Threshold**: Price ≥ 20; 20‑day avg volume ≥ 1,000,000.  
    - **Why**: Sub‑$20, low‑volume names have worse options microstructure, high spreads, and manipulation risk.  
    - **Data**: Your OHLCV provider (TwelveData/yfinance). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
    - **Priority**: **Must‑Have**.

12. **Rule**: Underlying must already meet **your BUY + Favorable Risk + ADX ≥ 20** criteria.  
    - **Threshold**: As defined in your Verdict engine (2 Strong categories, etc.). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
    - **Why**: Options magnify your stock edge; they don’t create one.  
    - **Data**: Internal categorical engine output.  
    - **Priority**: **Must‑Have**.

***

## Part 3 – Covered Call (Call Sell) Eligibility Checklist

For stocks rated **HOLD** or “neutral‑to‑slightly‑bullish”.

#### 3.1 Position & Liquidity

1. **Rule**: User must **own ≥100 shares per contract** (no naked calls).  
   - **Threshold**: share_count ≥ 100 × contracts.  
   - **Why**: Prevents unlimited upside risk from uncovered calls.  
   - **Data**: Portfolio input from user (not your data providers).  
   - **Priority**: **Must‑Have**.

2. **Rule**: Same liquidity rules as Part 2 (volume ≥50, OI ≥500, spread ≤8%) on chosen call strike.  
   - **Why**: Assignment and roll management are painful in illiquid contracts.  
   - **Priority**: **Must‑Have**.

***

#### 3.2 Volatility & Premium Richness

3. **Rule**: Only sell covered calls when **IV Rank ≥ 40 and preferably ≥ 60**.  
   - **Threshold**: IV Rank ≥40 (minimum), ≥60 (ideal).  
   - **Why**: Higher IV means richer premiums; you get paid more to cap upside. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)
   - **Data**: IV Rank from your IV history.  
   - **Priority**: **Must‑Have**.

4. **Rule**: Avoid selling covered calls when **VIX < 12** (ultra‑low volatility).  
   - **Threshold**: VIX ≥ 12.  
   - **Why**: In ultra‑calm markets, you collect very little premium for the upside you’re giving away.  
   - **Data**: VIX endpoint. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
   - **Priority**: **Nice‑to‑Have**.

***

#### 3.3 Strike, DTE, and Assignment Risk

5. **Rule**: Choose strikes **5–15% OTM**, preferably just above your nearest resistance cluster.  
   - **Threshold**: Strike / spot − 1 between 0.05 and 0.15; strike ≥ strongest resistance from your S/R engine.  
   - **Why**: You’re paid to wait while leaving room for modest upside; aligning with resistance reduces assignment probability before your technical exit.  
   - **Data**: Spot price, S/R levels, strike.  
   - **Priority**: **Must‑Have**.

6. **Rule**: Use expiries with **20–45 DTE**.  
   - **Threshold**: 20 ≤ DTE ≤ 45.  
   - **Why**: Good balance of annualized theta vs. flexibility; many covered‑call practitioners target 30–40 days.  
   - **Data**: Expiry dates.  
   - **Priority**: **Must‑Have**.

7. **Rule**: Target **delta between 0.20 and 0.35** on the call.  
   - **Threshold**: 0.20 ≤ Δ ≤ 0.35.  
   - **Why**: Represents ~20–35% probability of assignment by expiry; acceptable trade‑off for income vs. keeping shares.  
   - **Data**: Call Δ.  
   - **Priority**: **Must‑Have**.

8. **Rule**: Flag **earnings within 10 trading days** as “high assignment/IV risk” and default to **No Recommendation**.  
   - **Threshold**: earnings_date − today > 10.  
   - **Why**: Upside gap risk + IV crush can make covered calls behave unpredictably around earnings.  
   - **Data**: Earnings date.  
   - **Priority**: **Must‑Have**.

9. **Rule**: If the stock has a **near‑term ex‑dividend date**, indicate increased early‑assignment risk for ITM calls.  
   - **Threshold**: Ex‑div within 10 days and call ITM.  
   - **Why**: Call buyers exercise to capture dividends; users must be aware of this.  
   - **Data**: Dividend calendar + moneyness.  
   - **Priority**: **Nice‑to‑Have**.

***

## Part 4 – Put Buy (Long Put) Eligibility Checklist

For **AVOID** verdicts or bearish setups (Weak Technical, unfavorable risk). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)

1. **Rule**: Reserve long‑put signals for **clear downtrends** (Trend Template fails, price below 50 & 200 SMA, ADX ≥ 20 down).  
   - **Threshold**: Your AVOID logic + ADX trend strength.  
   - **Why**: Buying puts in chop wastes theta; needs strong directional bias.  
   - **Data**: Existing technical assessment.  
   - **Priority**: **Must‑Have**.

2. **Rule**: Only buy puts when **IV Rank ≤ 60** (avoid panic peaks).  
   - **Threshold**: IV Rank ≤ 60.  
   - **Why**: Fear already priced in makes puts very expensive; small reversals destroy them.  
   - **Data**: IV Rank.  
   - **Priority**: **Must‑Have**.

3. **Rule**: Avoid new put buys when **VIX ≥ 35** unless explicitly “crash hedge”.  
   - **Threshold**: Default max VIX 35.  
   - **Why**: Systemic fear regime where options are structurally overpriced.  
   - **Data**: VIX.  
   - **Priority**: **Must‑Have**.

4. **Rule**: Choose **DTE 30–75** and **delta −0.35 to −0.65** for swing puts.  
   - **Threshold**: 30 ≤ DTE ≤ 75; 0.35 ≤ |Δ| ≤ 0.65.  
   - **Why**: Similar logic to calls; enough time to capture swing, avoids ultra‑OTM lotto.  
   - **Data**: Expiry, Δ.  
   - **Priority**: **Must‑Have**.

5. **Rule**: Strike selection should be **just below nearest strong support**, such that a move to your next support/target yields ≥1.5×–2× option price gain.  
   - **Threshold**: strike slightly below S1; projected move to S2 or weekly support gives ≥50% gain.  
   - **Why**: Aligns with your S/R map and risk/R framework.  
   - **Data**: Your support levels, Δ.  
   - **Priority**: **Must‑Have**.

6. **Rule**: Cap **allocated premium for long puts at ≤ 5–10% of total portfolio**.  
   - **Threshold**: Sum(long_put_costs) ≤ 0.10 × portfolio.  
   - **Why**: Long puts have negative expectancy as insurance; they’re a hedge, not a core asset.  
   - **Data**: Portfolio size, premium per trade.  
   - **Priority**: **Must‑Have**.

7. **Rule**: Do not recommend puts on **micro‑cap / < $10 stocks**.  
   - **Threshold**: Price ≥ $10, market cap above chosen floor (e.g., $2B).  
   - **Why**: Options are often illiquid, easily manipulated.  
   - **Data**: Price, market cap (you already fetch).  
   - **Priority**: **Must‑Have**.

***

## Part 5 – Cash‑Secured Put Eligibility Checklist

For fundamentally decent/strong stocks your system likes, but that are extended / near resistance. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)

1. **Rule**: Only on stocks rated **BUY or strong HOLD with Favorable/Neutral Risk**.  
   - **Threshold**: No Weak Technical, no Unfavorable Risk.  
   - **Why**: You must be willing to own on assignment.  
   - **Data**: Verdict engine.  
   - **Priority**: **Must‑Have**.

2. **Rule**: Choose **strike at or below strong support**, ideally **5–15% below current price**.  
   - **Threshold**: Strike ≤ nearest strong support (S1/S2) and 0.05–0.15 below spot.  
   - **Why**: Your S/R engine already identifies attractive pullback zones; assignment then equals “buying the dip”.  
   - **Data**: Support levels, spot.  
   - **Priority**: **Must‑Have**.

3. **Rule**: Only sell when **IV Rank ≥ 40, preferably ≥ 60**.  
   - **Threshold**: IV Rank ≥40; highlight ≥60 as “rich premium”.  
   - **Why**: Short options benefit from elevated IV that later mean‑reverts.  
   - **Data**: IV Rank.  
   - **Priority**: **Must‑Have**.

4. **Rule**: Use **20–60 DTE** expiries.  
   - **Threshold**: 20 ≤ DTE ≤ 60.  
   - **Why**: Good theta/annualized return; very short DTE reduces premium; very long increases exposure window.  
   - **Data**: Expiry.  
   - **Priority**: **Must‑Have**.

5. **Rule**: Target **delta between −0.25 and −0.40**.  
   - **Threshold**: 0.25 ≤ |Δ| ≤ 0.40.  
   - **Why**: 25–40% probability of assignment; acceptable for “paid limit order”.  
   - **Data**: Δ.  
   - **Priority**: **Must‑Have**.

6. **Rule**: Verify **cash on hand ≥ strike × 100 × contracts** (cash‑secured, not naked).  
   - **Threshold**: cash_available ≥ obligation.  
   - **Why**: Prevents margin/naked risk.  
   - **Data**: User portfolio input.  
   - **Priority**: **Must‑Have**.

7. **Rule**: Flag **earnings within 10 trading days** as “heightened gap risk”; default to **No Recommendation**.  
   - **Threshold**: earnings_date − today > 10.  
   - **Why**: Earnings gaps can blow through support/strike, saddling user with unwanted shares.  
   - **Data**: Earnings date; your existing earnings flag. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
   - **Priority**: **Must‑Have**.

8. **Rule**: Limit **aggregate downside if assigned** to ≤ 20–25% of portfolio.  
   - **Threshold**: Sum(strike × 100 × contracts) ≤ 0.25 × portfolio.  
   - **Why**: Even if all puts are assigned, user must not be over‑concentrated.  
   - **Data**: Portfolio size; strike/contracts.  
   - **Priority**: **Must‑Have**.

***

## Part 6 – Universal Disqualifiers (Any Options Trade)

1. **Rule**: **Average underlying stock volume < 500k shares/day** → no options.  
   - **Threshold**: 20‑day avg volume ≥ 500,000.  
   - **Why**: Low underlying liquidity undermines options liquidity and price discovery.  
   - **Priority**: **Must‑Have**.

2. **Rule**: **Average daily options volume < 200 contracts chain‑wide** → no options.  
   - **Threshold**: ≥200 contracts across all strikes.  
   - **Why**: Indicates dead options market; spreads and jumps will dominate.  
   - **Priority**: **Must‑Have**.

3. **Rule**: **Any candidate contract with bid‑ask spread > 10% of mid** → reject that contract.  
   - **Threshold**: Spread/mid ≤ 10%.  
   - **Why**: Frictional costs too high.  
   - **Priority**: **Must‑Have**.

4. **Rule**: **Upcoming binary event within 5 trading days** (earnings, FDA panel, merger vote, known court ruling) → no options by default.  
   - **Threshold**: flagged_event = True & days_to_event ≤ 5.  
   - **Why**: Event risk dominates edge; tools should not encourage roulette.  
   - **Priority**: **Must‑Have**.

5. **Rule**: **Trading halt, volatility pause, or regulatory restriction** → no options.  
   - **Threshold**: status != “normal”.  
   - **Why**: Execution risk unacceptable.  
   - **Data**: Exchange status if available, or detection via zero quotes.  
   - **Priority**: **Must‑Have**.

6. **Rule**: **Extreme IV: IV Percentile ≥ 95** → do not buy options; only allow “sell‑side only” label with strong warning.  
   - **Threshold**: IV percentile ≥95.  
   - **Why**: Buying here is almost always negative‑EV; only pros sell into this IV.  
   - **Priority**: **Must‑Have**.

7. **Rule**: **Underlying price < $10** or **micro‑cap** → no options.  
   - **Threshold**: Price ≥ 10, market cap above set floor.  
   - **Why**: Outright speculative playground; typical screener user shouldn’t be there with options.  
   - **Priority**: **Must‑Have**.

8. **Rule**: **Exotic/ill‑understood underlyings** (thin ADRs, leveraged/inverse ETFs, ETNs) → default to “not supported” for v1.  
   - **Threshold**: Only plain US stocks + major ETFs.  
   - **Why**: Borrow constraints, path‑dependent behavior, complex distributions.  
   - **Priority**: **Must‑Have**.

***

## Part 7 – Simple Decision Matrix

Assuming all universal disqualifiers and strategy‑specific filters are respected.

| System Verdict | Market Regime (VIX & SPY) | Recommended Options Strategy | Key Filter |
|---|---|---|---|
| BUY | Favorable (SPY>200SMA, VIX<25) [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md) | **Optional Long Call** (30–60 DTE, Δ 0.4–0.6) or **Cash‑Secured Put** below support | IV Rank ≤60 for calls; IV Rank ≥40 for CSPs |
| BUY | Neutral (SPY>200SMA, VIX 20–30) | **Prefer Stock**; only CSPs when IV Rank ≥50 | Avoid long calls if IV Rank >60 |
| HOLD | Favorable | **Covered Call** (20–45 DTE, Δ 0.2–0.35, strike above resistance) | Own ≥100 shares; IV Rank ≥40 |
| HOLD | Neutral | **Light Covered Call or Do Nothing** | Avoid if earnings <10 days |
| AVOID | Any | **No bullish options; allow Long Put only if strong downtrend + IV Rank ≤60** | Cap put premium ≤10% of portfolio |

You can embed this as a read‑only suggestion card on the Options tab.

***

## Part 8 – What NOT to Build in v1 (Scope Guardrails)

1. **No multi‑leg structures** (verticals, iron condors, butterflies, calendars).  
   - Too many moving parts; hard to express cleanly in a simple tab; users mis‑size risk.

2. **No naked option selling** (naked calls or cashless puts).  
   - Unlimited or very large downside; incompatible with “safety first” posture.

3. **No automatic recommendations on leveraged/inverse ETFs, micro‑caps, or illiquid ADRs.**  
   - Complex behavior and borrow constraints; high gap risk.

4. **No real‑time gamma/vega risk dashboards.**  
   - Overkill for swing timeframe; encourages day‑trader behavior.

5. **No position‑sizing engine for options in v1** (beyond simple “do not exceed X% of portfolio in this trade”).  
   - Position sizing for options (due to convexity) is non‑trivial; for v1, simply cap premium or assignment exposure as % of portfolio.

6. **No automatic roll logic** (e.g., covered call rollups/rollouts).  
   - Requires full portfolio integration and user intent; defer to later version.

**Minimum viable Options tab**:

- For each supported strategy, **binary “Eligible / Not Eligible” flag** + brief rationale.  
- Show **one or two best candidate contracts** (e.g., top delta strike that passes all checks).  
- Prominent **warnings** when any non‑fatal issue exists (earnings soon, high IV, wide spread).

***

## Part 9 – Concrete Risk Disclaimers & Warnings

These should be surfaced contextually in the UI, not just in a footer.

1. **High IV Warning**  
   - **Trigger**: IV Rank > 60 (yellow), >80 (red).  
   - **Message**: “Implied volatility is elevated (Rank XX). Option premiums may collapse quickly if volatility normalizes, even if price moves in your favor.”  
   - **Why**: Makes IV crush explicit. [youtube](https://www.youtube.com/watch?v=Rxw7nCWV6-I)

2. **Earnings/Event Proximity Warning**  
   - **Trigger**: Earnings or major event within 10 trading days.  
   - **Message**: “This contract expires or spans a major event (earnings/FDA/merger). Price gaps and volatility spikes can cause large, unpredictable P/L swings.”  
   - **Why**: Clarifies binary‑event nature.

3. **Liquidity Warning**  
   - **Trigger**: Bid‑ask spread >5% (yellow) or >8% (red), or volume <50/OI <500.  
   - **Message**: “Low liquidity and/or wide spreads may prevent entering or exiting near quoted prices. You may incur substantial slippage.”  

4. **Market Regime Warning**  
   - **Trigger**: VIX > 30 or SPY below 200 SMA (bear regime). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/26027686/9553610c-4914-4ea7-b88d-b4cb880efc1e/README.md)
   - **Message**: “Broad market conditions are stressed (VIX XX / SPY trend). Options prices and correlations behave abnormally in these regimes.”  

5. **Position Size Guidance**  
   - **Trigger**: Any options recommendation.  
   - **Message** (call/put buys): “Total premium at risk in options should generally not exceed 2–5% of your portfolio per trade, and 10% in aggregate. Options can lose 100% of premium.”  
   - **Message** (CSP/covered calls): “If assigned, your stock exposure at strike price will be up to $YYY (ZZ% of your portfolio). Ensure you are willing and able to hold this position.”  

6. **Model & Data Limitations**  
   - **Message**: “Greeks and implied volatility are computed using models (e.g., Black‑Scholes) and third‑party data. These values are estimates, not guarantees. Real trading outcomes may differ.” [chasethedevil.github](https://chasethedevil.github.io/post/yahoo_finance_implied_volatility/)

7. **Non‑advice Disclaimer**  
   - **Message**: “This tool provides **screening and educational analytics only**. It does not consider your full financial situation and is **not investment advice**. Always verify data and risk before trading.”

***

If you implement:

- **Data layer**: yfinance + Tradier or Polygon for richer chains/Greeks.  
- **Eligibility engines**: pure rule‑based filters as above, defaulting to “Not Eligible” when in doubt.  
- **UI**: show “Eligible / Not Eligible” per strategy, with 2–3 bullet reasons,

you’ll have a **conservative, production‑safe Options tab** tightly integrated with your existing Swing Trade Analyzer.

-------------------------------------------------------

“Locally computable” here = **anything you can derive on your own backend from spot price, option quote, strike, expiry, rate and (optionally) dividend yield**, without needing a vendor to give you the metric.

## What’s Locally Computable?

With just:
- Underlying spot price (S)
- Strike (K), expiry date (T)
- Option type (call/put)
- Market option price (last/mid)
- Risk‑free rate (r) and dividend yield (q, can be approximated)

you can reliably compute:

- **Black‑Scholes / BSM theoretical price** (given IV).
- **Implied volatility (IV)** by inverting Black‑Scholes to match the market price (root‑finding). [vollib](https://vollib.org)
- **Greeks** for each contract:
  - Delta, Gamma, Vega, Theta, Rho (and higher‑order greeks if you want) under Black, Black‑Scholes, or BSM. [github](https://github.com/vollib/py_vollib)
- **Intrinsic + extrinsic value**:
  - Intrinsic = max(\(S-K,0\)) or \(K-S\); Extrinsic = option price − intrinsic.
- **IV Rank / IV Percentile**:
  - Once you store daily IV for each underlying, IV rank & percentile are simple rolling statistics on your own history.
- **Probability metrics** (under log‑normal/normal assumptions):
  - Probability ITM at expiry (from \(N(d_2)\) in BS).
  - Probability of touching a strike (1 – probability that max/min never crosses).
- **Expected move**:
  - Approx \(S \times \text{IV} \times \sqrt{T}\) over horizon \(T\).
- **Put–call parity outputs**:
  - Implied forward price, implied dividend yield, etc.

So for your Options tab you do **not** need a vendor that “gives Greeks”. A clean options quote + your own BS/BSM layer is enough.

***

## GitHub / Python Projects That Already Do This Well

These are good building blocks to plug directly into your Flask backend.

### 1. `py_vollib` and `py_vollib_vectorized`

- **What it does**:  
  - Pricing, **implied volatility**, and **Greeks** for Black, Black‑Scholes, and Black‑Scholes‑Merton models, with both analytical and numerical Greeks. [github](https://github.com/vollib/py_vollib)
  - `py_vollib_vectorized` adds NumPy/pandas‑friendly, vectorized versions for thousands of contracts at once, with Numba speedups. [pypi](https://pypi.org/project/py-vollib-vectorized/)
- **Why it’s ideal for you**:
  - Battle‑tested, finance‑grade math; designed exactly for “compute IV and Greeks locally from quotes”.
  - Vectorized variant is perfect for scanning whole chains in one shot.
- **Docs**: GitHub repo and vollib docs show APIs like:

```python
from py_vollib.black_scholes import black_scholes
from py_vollib.black_scholes.implied_volatility import implied_volatility
from py_vollib.black_scholes.greeks.analytical import delta, gamma, vega, theta, rho
# or use py_vollib_vectorized.greeks.vectorized_delta(...)
```


***

### 2. MibianLib (`mibian`)

- **What it does**:  
  - Python options pricing library implementing **Black‑Scholes, Garman‑Kohlhagen, Merton** models for European options on stocks and FX. [github](https://github.com/yassinemaaroufi/MibianLib/blob/master/setup.py)
  - Convenience classes for **option prices and Greeks** (Delta, Gamma, Vega, Theta, etc.). [youtube](https://www.youtube.com/watch?v=T6tI3hVks5I)
- **Why it’s useful**:
  - Very simple API; great for prototyping or computing a handful of contracts per request.
  - Widely used in tutorials for computing Greeks in Python. [marketcalls](https://www.marketcalls.in/python/computing-option-greeks-using-openalgo-and-mibian-a-python-guide-for-traders.html)

***

### 3. `option-greek-pricing` (OptionGreekPricing)

- **What it does**:  
  - Python package exposing **Put‑Call Parity, Binomial Trees, Black‑Scholes** and a dedicated `Greeks` class for Delta, Gamma, Vega, Theta, Rho, etc. [github](https://github.com/mh2rashi/OptionGreekPricing)
- **Why it’s useful**:
  - Good for educational clarity and alternative models (binomial, Monte Carlo) if you ever want to sanity‑check BS/BSM results.
- **Install/usage**: `pip install option-greek-pricing` then use `BlackScholes` + `Greeks` APIs. [github](https://github.com/mh2rashi/OptionGreekPricing)

***

### 4. `yahoo_vol`

- **What it does**:  
  - Helper toolkit built around Yahoo options data to analyze options markets — includes **implied volatility extraction** from Yahoo chains. [github](https://github.com/schepal/yahoo_vol)
- **Why it’s useful**:
  - Good reference if you want to see how others scrape & interpret Yahoo’s option chain data, and how they handle IV from that source.
- **Caveat**:
  - More about workflow around Yahoo than a pure math library; still a nice reference implementation. [github](https://github.com/schepal/yahoo_vol)

***

### 5. QuantLib Python (heavyweight but comprehensive)

- **What it does**:  
  - Full‑blown quant library with **Black‑Scholes and more advanced engines** (term structures, stochastic volatility, exotic options), including Greeks. [youtube](https://www.youtube.com/watch?v=FtiWYcmqsaU)
- **Why to consider / not consider**:
  - Overkill for a v1 options screener; heavier dependency and steeper learning curve.
  - Great if you later want term‑structure‑aware pricing or non‑BS models.

***

## How This Maps to Your Stack

Given your current architecture:

- **Locally computable layer**:
  - Use `py_vollib_vectorized` (recommended) or `MibianLib`/`option-greek-pricing` for:
    - IV solve from market mid
    - Δ, Γ, Vega, Θ, Rho (per contract)
    - Theoretical price and expected move
  - Store daily IV snapshots per underlying → compute **IV Rank/Percentile** yourself.

- **Data layer**:
  - Use yfinance/Tradier/Polygon for **raw option quotes (bid/ask/last, OI, volume, expiries)**. [youtube](https://www.youtube.com/watch?v=0xTbug30QsE)
  - Feed those into your local BS/Greeks engine.

That gives you a fully **vendor‑agnostic, locally computable options analytics stack**:

- Vendor: raw chain + underlying price
- Your code (`py_vollib`/`mibian`): IV, Greeks, probabilities
- Your DB: IV history → IV Rank/Percentile
- Swing Trade Analyzer: filters/rules on top

If you want one “batteries‑included” starting point, **`py_vollib_vectorized` is the best fit** for your use case. [pypi](https://pypi.org/project/py-vollib-vectorized/)