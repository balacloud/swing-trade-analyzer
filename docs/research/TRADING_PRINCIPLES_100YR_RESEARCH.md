# 100 Years of Trading Principles — External Research (for STA Comparison Artifact)

> **Purpose:** Raw material for a two-column Artifact comparing STA's actual code-verified
> behavior (see `docs/claude/plans/tender-popping-music.md` for the code audit, or that
> session's transcript) against long-established, cross-decade trading principles.
> **Status:** Perplexity's response received and stored 2026-08-13. **Still waiting on
> ChatGPT and Gemini** before the comparison Artifact gets built — do not build the artifact
> from Perplexity alone; the user explicitly wants all three cross-checked first.
> **Do not edit the content below** — it's the LLM's raw output, kept verbatim so it can be
> diffed against the ChatGPT/Gemini responses when they arrive.

---

## Source: Perplexity (2026-08-13)

### Executive Summary

These nine categories represent the most battle-tested, cross-decade trading principles — each has survived multiple market regimes and been independently rediscovered by different practitioners, which is the strongest evidence a rule is real rather than curve-fit. Below, each includes the mechanism, the numeric rule where one exists, its lineage, and the practical failure mode.

### Trend, Momentum & Mean Reversion

| # | Principle (one sentence) | Numeric rule | Source | Common failure |
|---|---|---|---|---|
| 1 | A security in an established uptrend (price above a rising long-term average) is statistically more likely to continue up than reverse, so trade with the prevailing trend rather than against it | Price above 200-day SMA = long-only bias; 50/200-day "golden cross" for regime shifts; moving-average "stack" (20>50>200) confirms strength | Dow Theory (Charles Dow, early 1900s), formalized in modern trend-following/CTA systems and the Turtle rules | People trade every crossover in choppy, non-trending markets, generating whipsaw losses; the MA works only when a genuine trend exists — a flat or "tangled" MA is a no-trade signal, not a signal to trade |
| 2 | Stocks already outperforming the broad market on a 6–12 month lookback tend to keep outperforming ("winners keep winning") | Buy only stocks with a Relative Strength Rating of 80+ (top 20% of all stocks by 12-month price performance), ideally 90+ | William O'Neil, CANSLIM ("L" = Leader), Investor's Business Daily RS Rating methodology | Traders buy the biggest RS-ranked names right after a sharp run-up without checking market ("M") context — CANSLIM's own emphasis is that the "M" (market in confirmed uptrend) overrides every other letter; ignoring it means buying leaders into a market-wide reversal |
| 3 | Short-term oversold extremes within a larger uptrend tend to snap back, so buy panic dips rather than breakouts | RSI(2) closes below 5–10 while price is above the 200-day MA = buy; exit when RSI(2) > 70 or price closes above the 5-day MA | Larry Connors & Cesar Alvarez, "Short Term Trading Strategies That Work" (RSI-2 system) | People apply mean reversion in downtrends or bear markets ("catching a falling knife") — Connors' own backtests only hold up with the 200-day trend filter in place; strip it out and the edge disappears in crashes |

### Volume, Sizing & Stops

**Volume confirmation.** A price move is only trustworthy if it's backed by proportionally rising volume; heavy volume with little price progress ("effort vs. result") signals absorption and a likely reversal, not continuation. Granville's rule of thumb was that "volume precedes price" — his On-Balance Volume (OBV) adds the day's volume when price closes up and subtracts it when price closes down, and a rising OBV alongside rising price confirms the trend while OBV divergence warns of thinning conviction. This traces to Richard Wyckoff's Law of Effort vs. Result (1910s–1930s, "Wyckoff Method") and Granville's 1963 OBV formalization, both extending Dow Theory's original volume-confirmation tenet. The most common misuse: treating raw volume spikes as automatically bullish — a huge-volume up-day that stalls near resistance is often distribution by large players, the opposite of what casual traders assume.

**Position sizing & risk per trade.** Size every trade so a stop-out costs the same fixed percentage of equity, regardless of the instrument's volatility. The standard is 1–2% of account equity risked per trade, with the Turtle Traders' variant risking 1% per "unit" sized as 1% ÷ (N × dollar-per-point), where N is the 20-day ATR. This traces to Richard Dennis & William Eckhardt's 1983 Turtle experiment and Van Tharp's "Trade Your Way to Financial Freedom," which formalized the R-multiple (loss at stop = –1R; no trade should risk more than 1R). The failure mode: sizing by conviction or account-balance intuition instead of the stop-distance formula — Tharp's core point is "your stop determines position size, not your confidence level," and violating this is the single most common cause of blow-ups even among traders with a positive-expectancy system.

**Stop-loss placement.** Cap every single position's loss at a predetermined percentage, decided before entry, and never move it further away once set. Livermore's rule was never let a loss exceed 10% of the capital deployed in a trade; O'Neil's CANSLIM variant uses 7–8% below purchase price as an automatic sell. This traces to Jesse Livermore (via Edwin Lefèvre's "Reminiscences of a Stock Operator," 1923) and Richard Wyckoff's "Stock Market Technique," both independently arriving at hard, pre-set stops as the "first line of defense." The classic error is widening a stop after the trade goes against you ("giving it more room") — Livermore's own writing stresses obeying the rule mechanically because "losses are twice as expensive to make up," and most large drawdowns trace to exactly this rationalized stop-widening.

### Regime, Sentiment & Rotation

**Volatility-based regime filters.** Scale position size inversely with market volatility (typically VIX) — smaller size and/or tighter risk budgets as VIX rises, larger size when VIX is calm. Common tiering: VIX under 15–20 = full size; 20–25 = cut ~25–50%; 25–35 = cut ~50–75%; above 35 = cut 75%+ or stand aside, only taking A-grade setups. This is grounded in Moreira & Muir's "Volatility-Managed Portfolios" (Journal of Finance, 2017), which found that scaling exposure down when volatility is high (and up when low) raises Sharpe ratios across equity, momentum, and other factors because volatility spikes are not proportionally offset by higher expected returns. The frequent mistake is treating VIX levels as a market-direction signal rather than purely a sizing/risk-budget input — the Moreira-Muir result is about risk-adjusted returns from de-risking into chaos, not a claim that high VIX predicts a crash or a bottom; conflating the two leads people to short markets purely because VIX is elevated.

**Sentiment as contrarian signal.** When investor sentiment reaches a statistical extreme (either fear or greed), the crowd is usually positioned wrong, and forward returns skew in the opposite direction. CNN's Fear & Greed Index — built from VIX level, put/call ratio, breadth, and AAII bull-bear spread among other inputs — treats readings below 20 as "Extreme Fear" (historically preceding above-average 1–3 month forward returns) and above 80 as "Extreme Greed" (elevated mean-reversion risk). This descends from classic contrarian-sentiment work built on VIX, put/call ratios, and AAII surveys as crowd-positioning proxies. The most common error is using sentiment as a precise timing tool rather than a probabilistic tilt — extremes can persist and deepen for weeks (sentiment can stay "extreme fear" through an entire crash leg), so traders who buy the first extreme-fear reading with full size, rather than scaling in, often get run over before the reversion plays out.

**Sector rotation / relative rotation.** Capital rotates through sectors in a repeating cycle tied to the economic cycle and relative strength; a Relative Rotation Graph (RRG) tracks each sector's relative strength (JdK RS-Ratio) against momentum (JdK RS-Momentum) across four quadrants — Improving → Leading → Weakening → Lagging → back to Improving, typically in a clockwise path. This traces to Julius de Kempenaer's Relative Rotation Graph methodology (built on the same relative-strength lineage as Dow Theory's sector-participation confirmation). The standard error is buying a sector already deep in the "Leading" quadrant near the top-right extreme — by the time a sector visibly leads, RS-Momentum is often already decelerating, and the highest-reward entries are actually in "Improving" before the crowd notices; chasing the obviously-strong quadrant means consistently buying late in the rotation.

### Behavioral Check

Applying these rules mechanically is where investors most often fail, not in understanding them intellectually.

- **Confirmation bias**: it's tempting to only search for RS-rating or RRG data that supports a stock you already like; the discipline is to check whether the "M" (market uptrend) and volume-confirmation conditions genuinely hold, not just the parts that flatter your thesis.
- **Anchoring**: Livermore's 10% stop and O'Neil's 7-8% stop exist precisely because traders anchor to entry price and rationalize "just a bit more room" — the entire point of a pre-set stop is removing that decision once the position is on.
- **Herd behavior**: buying a sector already in the RRG "Leading" quadrant, or a stock with RS 95+ that's extended far from its base, is often herd-driven momentum-chasing rather than principled trend-following — O'Neil's own system pairs high RS with a proper base/breakout structure, not just "it's going up fast."
- **Loss aversion**: mean-reversion (RSI-2) dip-buying only works statistically inside an established uptrend; loss-averse traders often apply it in downtrends hoping for a bounce that reverses the pain of an existing loss, which is exactly the scenario Connors' own data excludes.

### Bear Case

None of these rules is riskless, and several interact badly under stress.

- **Trend/momentum crowding**: RS-based momentum and CANSLIM systems tend to concentrate in the same crowded leadership names; when regime shifts sharply (as documented in momentum-crash research underlying Moreira & Muir's paper), high-RS leaders can reverse violently and simultaneously, and moving-average trend filters lag badly at turning points.
- **VIX-sizing regime risk**: de-risking as VIX rises can mean cutting exposure right before a V-shaped recovery, since VIX often peaks coincident with or just after the market bottom — the Sharpe-ratio benefit is a long-run statistical average, not a guarantee on any single episode.
- **Sentiment extremes can persist**: "Extreme Fear" bottoms are probabilistic, not mechanical; 2008 and March 2020 both saw extreme-fear readings weeks before the actual low.
- **Sector rotation whipsaws**: RRG quadrant transitions can reverse quickly in choppy macro conditions, generating false "Improving" signals that never reach "Leading."

---

---

## Source: ChatGPT (2026-08-13)

The durable core is consistent across these schools: follow established strength, buy weakness only inside a valid uptrend, confirm important moves, and determine position size from predefined risk—not conviction. None of these rules guarantees a 15% annual return.

### Nine durable trading principles

| # | Category | One-sentence principle | Common numeric implementation | Origin and evidence | Where traders get it wrong |
|---|---|---|---|---|---|
| 1 | Trend following / moving averages | Stay aligned with the primary trend and accept entering late rather than predicting reversals. | Check monthly: hold the asset when its month-end price is above its 10-month SMA (~200 trading days); move to cash/T-bills when below. | Livermore's "main movement," Dow Theory's primary trend, Faber's quantified 10-month rule; time-series momentum across 58 futures markets, data extending to 1880 (Faber; Moskowitz–Ooi–Pedersen; Hurst–Ooi–Pedersen). VERIFIED. | Treating the 200-day average as an exact support line; reacting to every daily crossover; over-optimizing the exact MA length until the backtest looks perfect. |
| 2 | Momentum and relative strength | Prefer securities already outperforming their peers instead of assuming laggards must catch up. | CAN SLIM: RS Rating ≥80 (top ~20% on trailing price performance). Academic momentum evidence strongest over ~1–12 months. | William O'Neil/CAN SLIM; Jegadeesh–Titman; Moskowitz–Ooi–Pedersen. VERIFIED. | Confusing relative strength with RSI; buying only because it already rose, ignoring valuation/earnings/regime/extension from support. |
| 3 | Mean reversion / buying dips | Buy short-term oversold conditions only when the longer-term trend remains positive. | Classic Connors template: price above 200-day SMA, RSI(2) below 5; exit when RSI(2) closes above ~70 or price closes above its 5-day SMA. | Larry Connors, *Short-Term Trading Strategies That Work*. VERIFIED. | Buying RSI weakness below the 200-day average; averaging down after fundamental deterioration; applying an ETF-tested rule to earnings-sensitive individual stocks. |
| 4 | Volume confirmation | A breakout is more credible when matched by meaningfully greater participation; high volume with little price progress is a warning, not confirmation. | O'Neil breakout rule: volume at least 40–50% above the preceding 50-session average. Wyckoff used no fixed %, just effort-vs-result. | Wyckoff's effort-vs-result law; O'Neil's breakout studies. VERIFIED. | Treating volume as automatically bullish; ignoring whether the stock closed near its high; using one abnormal block trade as confirmation. |
| 5 | Position sizing / risk per trade | Decide the maximum acceptable loss first, then calculate share/contract count from the entry-to-stop distance. | Common baseline: risk 1% of equity per trade (conservative portfolios often less). Shares = account equity × risk fraction ÷ per-share risk. | Van Tharp's position-sizing/R-multiple framework; the Turtles normalized units by volatility. VERIFIED. | Mistaking "risk 1%" for "invest only 1%"; ignoring gaps/slippage; stacking correlated 1%-risk trades and pretending total risk is still 1%. |
| 6 | Stop-loss placement | Place the stop where the setup is invalidated or beyond normal volatility; reduce size when that stop must be wider. | O'Neil: max 7–8% below purchase price. Turtles: initial stop 2N, N = 20-day smoothed true range. | O'Neil; Turtle Traders. VERIFIED. | Using one flat % for every asset; sizing before setting the stop; repeatedly widening a losing stop; assuming stop orders guarantee fill price during gaps. |
| 7 | Regime / volatility filters | Reduce exposure when estimated volatility rises — a risk-control overlay, not a directional price forecast. | Moreira–Muir: scale next month's exposure inversely with the **previous month's realized variance** (not VIX). Practical vol-targeting: weight = target-vol / realized-vol, capped by max leverage. | Moreira & Muir, *Journal of Finance* 2017. **Important correction to Perplexity's framing below.** VERIFIED, with a caveat. | Calling this "VIX sizing" (it's realized variance, a different input); using fixed VIX 20/30/40 thresholds untested; leveraging up hard after unusually quiet periods. |
| 8 | Sentiment as a contrarian signal | Use sentiment only when statistically extreme, ideally requiring price confirmation, not as a standalone entry. | AAII: "unusual" sentiment = more than 1 standard deviation from its historical/rolling mean. | Graham's "Mr. Market"; Baker–Wurgler; Brown–Cliff; AAII historical analysis. VERIFIED. | Shorting merely because optimism is high (or buying merely on fear); picking a threshold with hindsight; expecting sentiment to time the next few days. |
| 9 | Sector rotation / relative-strength rotation | Periodically own the strongest sectors, replace them only when their relative ranking deteriorates. | Faber: rank sectors monthly on 1/3/6/9/12-month total returns, equal-weight top 1–3, replace on rank drop. Optional: require sector/market above its own 10-month SMA. | Moskowitz–Grinblatt industry momentum; Faber's sector-rotation research. VERIFIED. | Ranking price returns instead of total returns; rotating weekly (too fast); concentrating in one fashionable sector; ignoring that every sector may be below trend at once. |

### Two important corrections ChatGPT flagged on its own claims

> **"The Turtles risked exactly 1% at their stop"** — MISLEADING. Their unit was sized so a 1N move ≈ 1% of equity, but their initial stop was ~2N away — so a full adverse move on one unit was closer to ~2% before slippage, not 1%. "1N = 1%" ≠ "1% max loss."

> **"Moreira & Muir proved traders should size positions using VIX"** — MISLEADING. Their principal rule scaled exposure by the *previous month's realized variance*, not the VIX (a 30-day options-implied measure) — a different input. Later research also found volatility-managed portfolios didn't reliably outperform in direct out-of-sample tests.

### Position-sizing formula (for reference)

`shares = floor((account × risk_fraction) / (|entry − stop| + slippage_allowance))`

Worked example: $100,000 account, 0.5% risk ($500), entry $50, stop $47.50, $0.25/share slippage → risk/share = $2.75 → 181 shares, $497.75 planned risk.

### Cross-source note (Perplexity vs. ChatGPT, both received 2026-08-13)

The two sources agree closely on 8 of 9 categories — same names (Wyckoff, O'Neil, Connors, Van Tharp, Turtles, Faber/Dow Theory, AAII/Graham, de Kempenaer/Moskowitz-Grinblatt), same rough numeric rules. **They disagree on how to characterize category 7 (regime/volatility filters):** Perplexity described Moreira & Muir's rule as "VIX-based position sizing." ChatGPT went back to the actual mechanism and corrected this — the paper's real input is the *previous month's realized variance*, not the VIX index itself, and flagged that later research found the effect doesn't reliably replicate out-of-sample. **Treat ChatGPT's correction as the more careful read** — worth reflecting honestly in the final artifact rather than repeating the simpler "VIX sizing" framing, and worth noting STA's own VIX-threshold position sizing (`trade_simulator.py:150-166`) is *inspired by* this research tradition but isn't literally the Moreira-Muir mechanism either (STA uses VIX directly, in discrete bands, not realized variance) — an honest nuance for that row, not a reason to drop the comparison.

---

---

## Source: Gemini (2026-08-13)

Full response preserved below (its trailing "Opens in a new window" link-chrome list was decorative UI noise with no working citation text, trimmed — everything substantive is kept). Framed as an institutional/quant research note rather than a plain-English summary, with explicit formulas per category.

### Nine principles, as formulated by Gemini

1. **Trend following** — Long when `P_t > SMA_200` (or 50-SMA crosses above 200-SMA), exit/short below it. Source: Dow Theory (Rhea); Faber (2007), *A Quantitative Approach to Tactical Asset Allocation* — a 10-month SMA filter cut max drawdowns >50% while keeping equity-like CAGR across asset classes. Failure point: over-optimizing the exact lookback (e.g. 173 days) into curve-fit noise; abandoning the system during choppy/non-trending stretches because win rate alone (typically 35-45%) looks bad — trend-following's edge is payoff skew, not accuracy.

2. **Momentum & relative strength** — Adds a real nuance the other two sources didn't emphasize as strongly: **dual momentum**. Top-quintile 12-month relative strength (skip the most recent month) *AND* that same 12-month return must beat 3-month T-bill yield (absolute momentum). Source: Jegadeesh & Titman (1993) for cross-sectional momentum; Gary Antonacci, *Dual Momentum Investing* (2014) for combining it with an absolute filter. Failure point: using relative strength alone — a stock can be the "strongest" in a falling market and still lose money; the absolute filter is what actually protects capital in a broad decline.

3. **Mean reversion** — RSI(2) < 5 (tighter than the 5-10 range Perplexity gave) while price > 200-SMA; exit above the 5-day SMA. Source: Connors, cites backtested win rates >75% on liquid equities/ETFs. Failure point: same as the other two sources — skipping the 200-SMA trend filter and buying RSI weakness in a structural downtrend.

4. **Volume confirmation** — Breakout volume ≥40% above the 50-day average, plus a rolling 20-day "more up-days-on-volume than distribution-days" accumulation check. Source: Wyckoff's effort-vs-result; O'Neil/CANSLIM. Failure point: a nuance worth keeping — high volume *late* in an extended advance is often institutional distribution into retail enthusiasm ("buying climax"), not confirmation; volume alone doesn't tell you which side is dominant without context.

5. **Position sizing** — States "exactly 1.0%" risk per trade as the standard, sized via `(equity × 1%) / (2×ATR_20)`. Source: Dennis & Eckhardt (Turtles); Van Tharp. **Note:** this is the same 1% figure Perplexity used and the one ChatGPT's own correction complicated — see cross-source note below.

6. **Stop-loss placement** — Trailing stop at `high − 2×ATR_20`, ratcheting up only. Source: Livermore (1940) for the hard-stop discipline itself; Turtles for the specific 2N mechanic. Failure point: a static % stop applied identically across low-beta and high-beta names — the same 2% stop sits outside normal noise for a utility stock and inside normal daily noise for a volatile tech name, causing needless shakeouts on the latter.

7. **Volatility regime filters** — Presents *both* variants side by side: `w_t = c/σ_t²` (realized variance) **or** `w_t = c × VIX_target/VIX_t` (implied vol), as two valid practical formulations of the same scaling principle. Source: Moreira & Muir (2017) for the academic result (50-100% higher factor Sharpe ratios, reduced recession drawdowns). Failure point: assuming higher variance automatically means higher expected return and staying fully levered through a vol shock — variance spikes far faster than the return premium during crises.

8. **Contrarian sentiment** — The most specific numeric rule of all three sources: AAII Bull-Bear Spread < −20% *and* 10-day Put/Call Ratio > 1.0 → contrarian bullish; Spread > +30% *and* Put/Call < 0.55 → reduce exposure. Source: Graham's "Mr. Market" (1949); Humphrey Neill, *The Art of Contrary Thinking* (1954); Ned Davis Research. Failure point: taking the contrarian trade on the sentiment reading alone, with no price confirmation — sentiment extremes can persist for a long time inside a strong trend.

9. **Sector rotation** — A genuinely different mechanism than the RRG/relative-strength rotation the other two sources described: **calendar-based seasonality** — cyclicals (Industrials/Tech/Discretionary/Materials) Nov-Apr, defensives (Staples/Healthcare) May-Oct ("Sell in May"), per Sam Stovall's S&P sector-seasonality research. Failure point: rotating into "seasonally favored" defensive sectors during a severe broad bear market still loses money if those sectors are declining too — seasonality needs an absolute trend overlay, same lesson as category 2.

### Cross-source synthesis (all three: Perplexity, ChatGPT, Gemini — 2026-08-13)

**Where all three agree closely (7 of 9 categories):** trend-following (200-day SMA / Dow Theory / Faber), momentum via relative strength (O'Neil/Jegadeesh-Titman), mean reversion (Connors RSI(2), trend-filtered), volume confirmation (Wyckoff/O'Neil), stop placement (Livermore/Turtles' ATR-based stops), and the general shape of position sizing (predefined risk, not conviction, ATR/volatility-scaled). This is exactly the kind of independently-triangulated agreement that makes a principle trustworthy rather than one source's opinion.

**Where the three usefully diverge or sharpen each other:**
- **Volatility regime filters (category 7):** Perplexity described Moreira & Muir as "VIX-based sizing." ChatGPT went back to the paper and corrected this — the actual academic mechanism is *prior-month realized variance*, not VIX, and called the VIX framing misleading. Gemini splits the difference usefully: it names realized variance as the paper's formulation *and* VIX-target scaling as a separate, legitimate practical variant of the same principle. **Best synthesis:** the original 2017 paper = realized variance; VIX-banded sizing (which is what STA actually does) is a widely-used, legitimate real-world implementation of the same *principle*, just not literally that paper's own tested rule. Worth stating precisely, not glossing over.
- **Momentum (category 2):** Gemini's dual-momentum framing (Antonacci) — requiring *both* relative strength *and* a positive absolute return vs. T-bills — is a real, independently-sourced refinement the other two didn't emphasize. Useful for the artifact: STA's RS≥1.0 check is relative-only; it doesn't have an explicit absolute-momentum/cash-filter equivalent.
- **Position sizing (category 5):** Perplexity and Gemini both state "1% (or 1-2%)" as the standard; ChatGPT's own self-correction shows the Turtles' *actual* per-unit risk (2N stop, 1N-sized unit) was closer to ~2% before slippage, not a clean 1%. The honest takeaway: 1-2% is the real range in practice, and even the "textbook" 1% figure doesn't perfectly describe the system historically credited with popularizing it.
- **Sector rotation (category 9):** Perplexity/ChatGPT described RRG/relative-strength-based rotation (de Kempenaer, Moskowitz-Grinblatt, Faber's total-return ranking) — this is the lineage STA's own sector-rotation feature actually matches. Gemini instead led with Stovall's calendar-seasonality rotation ("Sell in May") — a real, different, independently-documented mechanism, not a contradiction, just a different flavor of "rotate by sector." STA does not implement calendar seasonality at all — worth noting as a real principle STA doesn't touch, separate from the RRG gap analysis.
- **Sentiment (category 8):** Perplexity/ChatGPT both centered on CNN's Fear & Greed Index (which is what STA actually uses) with <20/>80 extremes. Gemini used a different, more specific instrument (AAII Bull-Bear Spread + CBOE Put/Call Ratio) with different numeric thresholds. Both are legitimate, independently-documented contrarian-sentiment traditions — not a disagreement, just different gauges of the same underlying principle. STA's implementation maps to the Perplexity/ChatGPT gauge (CNN F&G), not Gemini's.

## Still needed before the Artifact is built

- [x] Perplexity's response (2026-08-13)
- [x] ChatGPT's response (2026-08-13) — caught a real correction on Perplexity's VIX/Moreira-Muir framing
- [x] Gemini's response (2026-08-13) — added dual-momentum, calendar-seasonality rotation, and a more specific sentiment gauge as genuinely new angles
- [x] Cross-checked all three — see synthesis above
- [ ] Build the Artifact per the plan file (`~/.claude/plans/tender-popping-music.md`, Step 3)
