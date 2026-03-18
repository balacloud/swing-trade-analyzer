# Universal Principles Research — Claude Opus Response

**Date:** 2026-03-18 (Day 69)
**Model:** Claude Opus 4.6
**Role:** 4th independent auditor (alongside GPT, Perplexity, Gemini)
**Caveat:** My training data has a knowledge cutoff of May 2025. I cannot verify papers published after that date, and I cannot browse the web to confirm DOIs in real-time. I will be explicit about this limitation per-claim.

---

## PROMPT 1: Binary Gating vs Continuous Factor Scoring

### Claim 1: "Binary pass/fail filters produce inferior risk-adjusted returns compared to continuous factor scoring with ranking."

> **Reasoning:** The quantitative factor investing literature overwhelmingly uses continuous scoring and ranking (decile/quintile portfolios). Fama & French (1993, "Common Risk Factors in the Returns on Stocks and Bonds"), Jegadeesh & Titman (1993, "Returns to Buying Winners and Selling Losers"), and AQR's published research all construct portfolios by sorting stocks into quantiles based on continuous factor scores, not binary gates. However, "inferior" is too strong — binary filters serve a different purpose (eliminating clearly unsuitable candidates) rather than competing directly with ranking for the same task. The comparison isn't well-studied head-to-head because most practitioners use them for different stages of the pipeline.
>
> **Verdict:** [MISLEADING — CORRECTION: Binary filters and continuous scoring serve different roles. Academic factor research uses continuous scoring for portfolio construction, but this doesn't mean binary filtering is "inferior" — it's a different tool. No head-to-head study was found comparing a 9-criterion binary gate vs continuous composite for swing trading specifically. The real issue is that binary gates discard information (a stock scoring 89/100 fails the same as 20/100 if one criterion misses), which is inefficient but not necessarily worse for risk-adjusted returns.]

### Claim 2: "The optimal approach is hybrid: binary filters as first pass, then rank survivors."

> **Reasoning:** This is standard practice in quantitative portfolio management. DeMiguel, Garlappi & Uppal (2009, "Optimal Versus Naive Diversification" in Review of Financial Studies) and Asness, Moskowitz & Pedersen (2013, "Value and Momentum Everywhere" in Journal of Finance) implicitly use this — they screen for investability (liquidity, price, market cap) then rank by factor score. AQR's published methodology papers describe screening for "investable universe" (binary filters on liquidity, market cap, ADR status) then ranking by combined value-momentum score. Yuval Taylor's practitioner work explicitly advocates "screen then rank."
>
> **Verdict:** [VERIFIED — SOURCE: This is standard practice in quantitative finance. AQR's methodology papers, Asness et al. (2013) "Value and Momentum Everywhere" (Journal of Finance), and multiple practitioner frameworks use binary investability screens followed by continuous factor ranking. The hybrid approach is not just documented — it's the dominant paradigm in systematic investing.]

### Claim 3: "Fama-French and AQR factor research applies to swing timeframes (5-30 days)."

> **Reasoning:** The canonical factor research (Fama-French 3-factor, Carhart 4-factor, AQR's momentum work) primarily uses monthly rebalancing with 3-12 month holding periods. Jegadeesh & Titman (1993) tested various formation/holding period combinations and found momentum profits at 3-12 month horizons, with short-term REVERSAL at 1-week to 1-month horizons. At the 5-30 day horizon specifically, we're in a transition zone: short-term reversal (Lehmann, 1990; Jegadeesh, 1990) dominates at the very short end (1-5 days), while medium-term momentum kicks in around 1-3 months. The 5-30 day window is where these two effects collide, making it the hardest horizon for simple factor application.
>
> **Verdict:** [MISLEADING — CORRECTION: Standard factor research does NOT directly apply to 5-30 day horizons. At this timeframe, you're in a transition zone between short-term reversal (1-5 days, well-documented by Lehmann 1990 and Jegadeesh 1990) and medium-term momentum (3-12 months, Jegadeesh & Titman 1993). Applying monthly-rebalanced factor strategies to weekly holding periods without adjustment is methodologically incorrect. The factors that matter at swing timeframes are likely: earnings momentum/drift (PEAD), short-term reversal, and liquidity — not the same as the standard Fama-French factors.]

### Claim 4: "~1 trade per week (238 trades over 4 years) is adequate signal frequency."

> **Reasoning:** Statistical significance in trading system evaluation requires sufficient sample size. A common rule of thumb in quantitative finance (Harvey, Liu & Zhu, 2016, "...and the Cross-Section of Expected Returns") is that you need at least 100+ independent trades for meaningful statistical inference. With 238 trades, you have enough for basic significance testing (your p=0.002 is strong). However, the question is also about PRACTICAL adequacy — can you compound capital effectively with 1 trade/week? For a discretionary swing trader managing 3-5 concurrent positions, 1 new signal per week is reasonable. For a fully systematic approach, it may be thin during drawdown recovery.
>
> **Verdict:** [PLAUSIBLE — REASON: 238 trades over 4 years provides sufficient statistical significance for backtesting validation. For a discretionary swing trader, ~1 signal/week is within normal operating range. However, this is on the LOW end — most systematic swing systems target 2-5 new signals per week to maintain portfolio deployment and recover from drawdowns faster. The adequacy depends on capital utilization goals. No published research defines an "optimal trades per year" specifically for swing systems.]

### Claim 5: "Day-to-day factor rankings are stable enough to trade on without persistence filters."

> **Reasoning:** Factor rankings at the daily level can be quite noisy. Novy-Marx & Velikov (2016, "A Taxonomy of Anomalies and Their Trading Costs") show that many anomalies lose profitability when traded at high frequency due to turnover costs. In practice, systematic funds typically require ranking persistence — a stock must remain in the top decile/quintile for multiple periods before entry, and must drop below a wider band before exit (hysteresis). This reduces turnover and improves signal quality.
>
> **Verdict:** [MISLEADING — CORRECTION: Daily factor rankings are NOT stable. Research on factor portfolio turnover (Novy-Marx & Velikov, 2016) shows that naive daily rebalancing destroys alpha through transaction costs. Practical implementations use: (a) rank persistence requirements (stock must rank in top N for 3-5 consecutive days), (b) hysteresis bands (enter at top 10%, only exit when dropping below top 25%), or (c) weekly/monthly rebalancing of a daily-computed score. Trading on a single day's ranking without a persistence filter is generally suboptimal.]

### Claim 6: "Factor weights can be determined from historical optimization without overfitting."

> **Reasoning:** Optimized factor weights almost always overfit in-sample. DeMiguel et al. (2009) famously showed that equal-weighted (1/N) portfolios outperform optimized-weight portfolios out-of-sample in most cases, because the estimation error in optimal weights exceeds the gains from optimization. The practical approach in quant finance is: (a) equal weighting as the default baseline, (b) inverse-volatility weighting for a slight improvement, (c) if you must optimize, use shrinkage estimators or Bayesian priors toward equal weights, and (d) the number of free parameters should be ≪ the number of independent observations (trades).
>
> **Verdict:** [MISLEADING — CORRECTION: Optimized factor weights are notorious for overfitting. DeMiguel, Garlappi & Uppal (2009, Review of Financial Studies) demonstrated that equal-weight (1/N) approaches outperform optimized allocations out-of-sample in most settings. The robust approach for a retail system is: START with equal weights, only deviate if you have overwhelming out-of-sample evidence. Cross-validation and shrinkage toward equal weights are standard guardrails. With only 238 trades, you do NOT have enough data to reliably optimize 4+ factor weights.]

---

## PROMPT 2: Universal Factor Set for Swing Trading

### Claim 1: "The top factors for 5-30 day returns are: cross-sectional momentum, short-term reversal, earnings momentum, volatility, liquidity, and market regime."

> **Reasoning:** Let me assess each:
> - **Cross-sectional momentum (3-12 month):** Well-documented (Jegadeesh & Titman 1993) but primarily at monthly+ horizons. At 5-30 days, the effect is weaker and contaminated by short-term reversal.
> - **Short-term reversal (1-5 days):** Documented by Lehmann (1990) and Jegadeesh (1990). Robust and persistent. But primarily a 1-5 day effect — weakens by 30 days.
> - **Earnings momentum / PEAD:** Post-Earnings Announcement Drift (Bernard & Thomas, 1989) is one of the most robust anomalies. 60-day drift after earnings surprises. Directly relevant to swing timeframes.
> - **Volatility:** Low-volatility anomaly (Baker, Bradley & Wurgler, 2011) is primarily a long-horizon effect. At swing timeframes, realized volatility is more useful as a risk filter than a return predictor.
> - **Liquidity:** Amihud (2002) illiquidity premium exists but is a longer-horizon effect. For swing trading, liquidity is better used as a filter (minimum volume) than a factor.
> - **Market regime:** Documented that trend-following works better in trending regimes. Not a stock-level factor per se, but a system-level switch.
>
> **Verdict:** [MISLEADING — CORRECTION: This list conflates stock-selection factors with system-level filters. For 5-30 day STOCK SELECTION specifically, the best-evidenced factors are: (1) Earnings momentum/PEAD (Bernard & Thomas 1989 — directly relevant), (2) Short-term reversal for mean-reversion entries (Lehmann 1990), (3) Medium-term price momentum (strongest at 3-6 months, weakening but present at 1-month), (4) Volume/liquidity as a quality filter. Volatility and regime are system-level controls, not stock-ranking factors.]

### Claim 2: "12-1 momentum (12-month minus last month) is the best momentum measure for swing trading."

> **Reasoning:** The 12-1 momentum formulation (Jegadeesh & Titman 1993, refined by Fama & French 2008) was designed to capture medium-term momentum while avoiding the short-term reversal effect of the most recent month. This is optimized for MONTHLY rebalancing with 3-12 month holding periods. For 5-30 day swing trades, the optimal momentum window is likely shorter. Empirical work by Novy-Marx (2012, "Is Momentum Really Momentum?") found that the 7-12 month intermediate component drives much of the momentum effect, while the 2-6 month component is also significant. For swing timing specifically, shorter formations (1-3 months) may be more responsive.
>
> **Verdict:** [MISLEADING — CORRECTION: 12-1 momentum is the academic standard for monthly-rebalanced factor portfolios, not for swing trading. For 5-30 day entries, you want a MORE RESPONSIVE momentum measure. Evidence suggests: (a) 3-month momentum for sector and stock selection (responsive enough for swing timeframes), (b) 52-week relative strength percentile (what you currently use — actually reasonable as a FILTER, not as a ranking factor), (c) 20-day rate of change for very short-term momentum. The "skip last month" rule matters less at daily granularity since you're already looking at recent price action.]

### Claim 3: "Chart patterns should be a scored factor, not a binary filter."

> **Reasoning:** Academic research on chart patterns is mixed. Lo, Mamaysky & Wang (2000, "Foundations of Technical Analysis") found statistical significance for some patterns using kernel regression, but effect sizes were small. Leigh et al. (2002) and other studies find marginal predictive power. The practical problem with patterns as continuous factors is that pattern "confidence" scores are inherently subjective — there's no consensus on how to score a "75% confident VCP" vs an "85% confident Cup & Handle." In contrast, binary pattern detection (pattern present/absent) is simpler and avoids the calibration problem.
>
> **Verdict:** [PLAUSIBLE — REASON: There is no clear evidence favoring patterns as continuous factors over binary filters. Lo et al. (2000) showed some patterns have statistical significance, but the effect is marginal compared to momentum and mean-reversion factors. Practically, keeping patterns as a binary filter (present = bonus, absent = no penalty) or an optional "setup quality" overlay is more robust than trying to score them on 0-100. The confidence scoring adds degrees of freedom without strong evidence that finer granularity improves outcomes.]

### Claim 4: "Fundamental quality metrics add value to swing trades beyond technicals."

> **Reasoning:** Novy-Marx (2013, "The Other Side of Value: The Gross Profitability Premium") showed that profitability (gross profits/assets) predicts returns independently of value. Asness, Frazzini & Pedersen (2019, "Quality Minus Junk") documented a quality factor. However, these operate at MONTHLY to QUARTERLY horizons. For 5-30 day swing trades, the evidence is weaker — fundamentals primarily prevent you from buying "junk" stocks that look technically strong but are fundamentally deteriorating. They act as a RISK FILTER more than a RETURN PREDICTOR at short horizons.
>
> **Verdict:** [PLAUSIBLE — REASON: Quality metrics (profitability, low leverage) have strong evidence at monthly+ horizons (Novy-Marx 2013, Asness et al. 2019). At swing timeframes, their primary value is DEFENSIVE — filtering out low-quality momentum stocks that are more likely to gap down on earnings or news. I cannot cite a study showing quality adds incremental short-term return prediction beyond momentum/trend, but the risk-reduction argument is well-supported. Keep quality as a filter, not a primary factor.]

### Claim 5: "CNN Fear & Greed is an adequate sentiment input."

> **Reasoning:** The CNN Fear & Greed Index is a composite of 7 market indicators (stock price momentum, stock price strength, stock price breadth, put/call ratio, junk bond demand, market volatility, safe haven demand). It's a simplification of several individually-documented sentiment measures. More granular sentiment inputs with published research backing include:
> - **Put/Call ratio:** Documented as contrarian indicator (Pan & Poteshman, 2006)
> - **VIX term structure:** Contango/backwardation signals documented in multiple practitioner studies
> - **Short interest:** Rapach, Ringgenberg & Zhou (2016, "Short Interest and Aggregate Stock Returns") — aggregate short interest predicts market returns
> - **Insider transactions:** Lakonishok & Lee (2001) — insider buying predicts returns, insider selling less informative
>
> **Verdict:** [PLAUSIBLE — REASON: F&G is a reasonable single-number proxy for market sentiment, and it aggregates several individually-documented signals. However, it's a blunt instrument. For a system evolution, the most impactful addition would be the VIX term structure (contango = complacency, backwardation = stress) and aggregate short interest ratio, both of which have stronger individual research backing than the composite F&G Index. The F&G is "adequate" for a simple system but is the first thing to upgrade if you want better sentiment resolution. That said, for a RETAIL system, the simplicity of F&G has practical value — you don't need to build 5 separate sentiment data feeds.]

### Claim 6: "SPY > 200 SMA + VIX levels is the best regime detection for swing trading."

> **Reasoning:** The 200-day MA as a regime filter is one of the most backtested simple rules in finance. Faber (2007, "A Quantitative Approach to Tactical Asset Allocation") documented that a 10-month SMA timing rule on the S&P 500 significantly reduces drawdowns with modest impact on long-term returns. Adding VIX levels gives volatility context. However, "best" is too strong. Alternatives with evidence:
> - **Market breadth:** % of stocks above 200 SMA gives earlier warning than the index itself (widely used by institutional traders, documented in Zweig's "Winning on Wall Street")
> - **Yield curve:** Has well-documented recession-prediction power (Estrella & Hardouvelis, 1991) but operates on much longer timeframes
> - **HMM:** More complex, published applications exist (Bulla et al., 2011) but prone to overfitting with small regime samples
>
> **Verdict:** [PLAUSIBLE — REASON: SPY > 200 SMA is one of the best-documented simple regime filters (Faber 2007). VIX adds useful context. This combination is "good enough" and has the virtue of simplicity. It's not provably "the best" — market breadth indicators (% stocks > 200 SMA) arguably give earlier signals and have practitioner support (Zweig). For a retail system, SPY > 200 SMA + VIX is a strong choice. The one evidence-based addition worth considering is market breadth, which we already partially capture via the Context Tab's economic indicators.]

### Claim 7: "Momentum and trend factors are too correlated; one should be dropped."

> **Reasoning:** 52-week RS vs SPY (momentum) and Price > 50 SMA > 200 SMA (trend) do overlap — both identify stocks in uptrends. However, they capture slightly different things: RS is RELATIVE (how this stock compares to the market), while SMA alignment is ABSOLUTE (is this stock in its own uptrend regardless of the market). In practice, a stock can have RS > 1.0 (outperforming SPY) while being below its 50 SMA (in a short-term pullback within a longer uptrend). These situations are actually interesting for entry timing.
>
> **Verdict:** [MISLEADING — CORRECTION: While these factors are positively correlated, they are NOT redundant. Relative momentum (RS) and absolute trend (SMA alignment) capture different information and can diverge meaningfully. The correct approach is NOT to drop one, but to: (a) measure their in-sample correlation (likely r=0.4-0.6, not 0.9+), (b) if correlation is below ~0.7, keep both with reduced weight, (c) if above 0.7, combine into a single "trend-momentum" composite. Do NOT drop trend just because it correlates with momentum — the marginal information is valuable for entry timing.]

---

## PROMPT 3: Mean-Reversion for Swing Traders

### Claim 1: "Mean-reversion works in range-bound markets, momentum works in trending markets."

> **Reasoning:** This is one of the most widely cited regime-strategy relationships. Moskowitz, Ooi & Pedersen (2012, "Time Series Momentum") documented that trend-following (time-series momentum) performs best in high-dispersion, trending environments. Mean-reversion strategies (buying losers, selling winners at short horizons) perform best in low-dispersion, range-bound environments. The challenge is DETECTION — identifying the current regime in real-time without hindsight bias.
>
> **Verdict:** [VERIFIED — SOURCE: Moskowitz, Ooi & Pedersen (2012, "Time Series Momentum," Journal of Financial Economics) and related work on momentum crashes (Daniel & Moskowitz, 2016) establish that momentum is regime-dependent and performs poorly in high-volatility reversals. Mean-reversion profitability in range-bound markets is documented in multiple short-term reversal studies (Lehmann 1990, Jegadeesh 1990). The regime-conditional strategy selection principle is well-established. The practical challenge — reliable real-time regime detection — remains an open problem.]

### Claim 2: "RSI < 30 oversold bounces are a proven mean-reversion entry."

> **Reasoning:** Larry Connors and Cesar Alvarez published extensive backtests on RSI-based mean-reversion in "Short Term Trading Strategies That Work" (2009) and "High Probability ETF Trading" (2009). Their research specifically tested RSI(2) < 10 and RSI(2) < 5 as entries for S&P 500 stocks and ETFs, showing significant edge. The standard RSI(14) < 30 is a weaker signal because 14-period RSI rarely reaches extreme levels. Connors' work used 2-period RSI specifically because it captures shorter-term oversold conditions more effectively.
>
> **Verdict:** [MISLEADING — CORRECTION: RSI(14) < 30 is a relatively weak mean-reversion signal for swing trading. The better-documented approach is RSI(2) < 10 or RSI(2) < 5, as backtested by Connors & Alvarez (2009). The shorter period captures sharper oversold conditions and produces better mean-reversion entry timing. However, even Connors' results should be treated cautiously — his backtests are in-sample demonstrations, not peer-reviewed academic research. The concept is sound (short-term oversold bounces), but the specific parameters need your own out-of-sample validation.]

### Claim 3: "Bollinger Band mean-reversion has empirical evidence of edge."

> **Reasoning:** Academic evidence for Bollinger Band strategies is weak. Lento & Gradojevic (2007) tested Bollinger Band trading rules and found mixed results, with performance highly dependent on market conditions and parameters. Most published backtests of Bollinger Band strategies show they work in specific conditions but fail to consistently outperform after transaction costs across broad market samples.
>
> **Verdict:** [PLAUSIBLE — REASON: Bollinger Bands capture the concept of statistical deviation from a mean, which IS related to short-term reversal. However, published evidence specifically for Bollinger Band STRATEGIES (buy at lower band, sell at upper) is weak and inconsistent. The underlying principle is sound, but Bollinger Bands are not the most efficient way to capture it. A simple z-score of returns or Connors' RSI(2) captures the same mean-reversion signal more cleanly. If you add mean-reversion, I'd recommend RSI(2)-based approaches over Bollinger Bands based on the available practitioner evidence.]

### Claim 4: "Mean-reversion trades need different risk parameters than momentum."

> **Reasoning:** This is well-established in practitioner literature. Momentum trades are BREAKOUT trades — they expect a large move in one direction, so they use wider stops (7-8%) and higher R:R targets (2:1+). Mean-reversion trades are BOUNCE trades — they expect a return to a mean, which is a smaller and more predictable move. Connors' work specifically recommends TIME-BASED exits for mean-reversion (exit after N days, or when RSI crosses above 70) rather than fixed price targets, because the "target" is the mean, which is a moving reference.
>
> **Verdict:** [PLAUSIBLE — REASON: Different risk management for different strategy types is standard in multi-strategy system design. Connors & Alvarez (2009) specifically use time-based exits (5-day, 10-day) and indicator-based exits (RSI crosses above threshold) for mean-reversion, not fixed price targets. This is consistent with the nature of mean-reversion: you're betting on a return to normal, not on a sustained move. Tighter stops (3-5% vs 7%), lower R:R targets (1.5:1 vs 2:1), and time-based exits (exit after X days regardless) are all well-documented practices for mean-reversion. However, I cannot cite a single paper that rigorously compares optimal risk parameters across strategy types in a controlled setting.]

### Claim 5: "Running momentum and mean-reversion simultaneously improves risk-adjusted returns."

> **Reasoning:** This is the core argument for multi-strategy diversification. The negative correlation between momentum and mean-reversion returns across regimes (momentum works in trending, mean-reversion in choppy) means combining them reduces drawdowns. AQR's published research on "Style Premia" (Asness, Moskowitz & Pedersen, 2013) demonstrates that combining uncorrelated or negatively-correlated strategies improves Sharpe ratios. However, the implementation complexity is significant — you need reliable regime detection to avoid running the wrong strategy in the wrong regime.
>
> **Verdict:** [VERIFIED — SOURCE: Asness, Moskowitz & Pedersen (2013, "Value and Momentum Everywhere") and broader multi-strategy literature demonstrate that combining negatively-correlated strategies improves risk-adjusted returns. The specific pairing of momentum + mean-reversion is supported by the regime-dependent performance documented in Moskowitz et al. (2012). The two approaches can run simultaneously (parallel) rather than requiring regime switching, with portfolio-level risk management ensuring neither dominates during adverse conditions.]

### Claim 6: "Mean-reversion has 60-70% win rates with smaller wins; momentum has 50-55% with larger wins."

> **Reasoning:** This characterization is consistent with practitioner literature and the mathematical nature of the strategies. Connors' backtested mean-reversion strategies show 65-75% win rates with average wins of 1-3%. Minervini-style momentum breakouts typically have 40-55% win rates with winners averaging 15-25% and losers cut at 7-8%. The relationship is an artifact of strategy design: mean-reversion bets on small, high-probability moves back to the mean; momentum bets on less frequent but larger trending moves.
>
> **Verdict:** [PLAUSIBLE — REASON: This win-rate characterization is consistent with published practitioner results (Connors for mean-reversion, Minervini for momentum) and the mathematical structure of the strategies. However, exact percentages depend heavily on implementation details (timeframe, stop loss, stock universe). The DIRECTION is verified (MR = higher win rate + smaller wins, Momentum = lower win rate + larger wins) but the specific ranges (60-70%, 50-55%) are generalizations, not precise empirical constants.]

### Claim 7: "Connors RSI or DV2 is the simplest evidence-based mean-reversion approach."

> **Reasoning:** Larry Connors' RSI(2) strategy is the most widely backtested simple mean-reversion approach for US equities. The basic version: buy when RSI(2) < 10 (or < 5) AND price is above 200 SMA (long-term uptrend filter), exit when RSI(2) > 70. This has been backtested extensively in his books and by independent researchers. DV2 (David Varadi's indicator) is another short-term oscillator with published backtests showing mean-reversion edge. Both are SIMPLE — single indicator + trend filter.
>
> **Verdict:** [PLAUSIBLE — REASON: Connors' RSI(2) strategy is probably the most widely-backtested simple mean-reversion approach for retail traders. It has published out-of-sample results spanning multiple market conditions (though from Connors' own publications, not peer-reviewed journals). The 200 SMA filter is critical — it prevents buying the dip in a downtrend. DV2 is less widely known but has similar published backing. For a "minimum viable mean-reversion" addition to your system, RSI(2) < 10 + Price > 200 SMA is the strongest candidate based on available evidence. CAVEAT: I cannot confirm whether this strategy's edge has survived post-2020 market structure changes — this needs your own backtest validation.]

---

## PROMPT 4: Regime-Adaptive Parameters

### Claim 1: "Regime-adaptive parameter tuning improves risk-adjusted returns."

> **Reasoning:** The evidence is mixed. On one hand, strategies that adapt to volatility regimes (e.g., targeting constant portfolio volatility by sizing inversely to VIX) have shown improved Sharpe ratios in published research (Moreira & Muir, 2017, "Volatility-Managed Portfolios," Journal of Finance). On the other hand, more granular parameter adaptation (changing entry thresholds, lookback periods, etc. based on regime) adds degrees of freedom that easily overfit.
>
> **Verdict:** [PLAUSIBLE — REASON: Volatility-managed portfolios (Moreira & Muir, 2017) demonstrate that simple regime adaptation — specifically POSITION SIZING inversely proportional to volatility — improves Sharpe ratios. However, adapting multiple parameters (entry thresholds, stop distances, lookback periods) simultaneously to regime is NOT well-supported and adds significant overfitting risk. The evidence supports adapting ONE or TWO parameters (position size and/or stop distance via ATR), not a full parameter overhaul per regime.]

### Claim 2: "Stops should adapt to volatility: wider in high-vol, tighter in low-vol."

> **Reasoning:** ATR-based stops inherently do this — they widen when volatility is high and tighten when it's low. This is mathematically equivalent to a fixed-ATR-multiple stop that auto-adapts. The alternative (fixed percentage like 7%) doesn't adapt and will get stopped out more frequently in high-vol environments. The Chandelier Exit (LeBeau & Lucas, 1992) and ATR Trailing Stop literature supports this approach.
>
> **Verdict:** [VERIFIED — SOURCE: ATR-based stops are volatility-adaptive by construction. LeBeau & Lucas (1992) documented the Chandelier Exit using ATR multiples. Moreira & Muir (2017) showed volatility-scaling improves risk-adjusted performance. Using ATR-based stops (which you already do with 2x ATR) IS regime-adaptive stop management. The key insight: you already have this — your 2x ATR stop IS volatility-adaptive. The 7% fixed stop is the non-adaptive one. Consider making ATR-based stops the PRIMARY method and the 7% a maximum cap.]

### Claim 3: "Position sizing is more impactful to adapt than entry/exit rules."

> **Reasoning:** Van Tharp ("Trade Your Way to Financial Freedom," 1998) and Ralph Vince ("Portfolio Management Formulas," 1990) both argue that position sizing has a larger impact on system outcomes than entry/exit rules. Moreira & Muir (2017) specifically showed that volatility-timing through position sizing improved ALL factor strategies they tested, while entry/exit modifications had mixed results. The intuition: during high-vol regimes, a smaller position size automatically reduces risk without changing any signals.
>
> **Verdict:** [VERIFIED — SOURCE: Van Tharp (1998) and Moreira & Muir (2017, Journal of Finance) both support position sizing as the highest-impact regime-adaptive parameter. Volatility-managed portfolios that scale position size inversely to recent volatility improved Sharpe ratios across momentum, value, and other strategies. This is the single most robust regime adaptation you can make — and it doesn't require changing any entry/exit logic.]

### Claim 4: "VIX < 20 / 20-30 / > 30 is the right tiering."

> **Reasoning:** The 20 threshold has empirical support (S&P's practitioner guide treats VIX 20 as the boundary between "moderate" and "high" volatility). However, absolute VIX levels shift over time with market structure changes. In 2017, VIX spent most of the year below 12 — your "Favorable" bucket would have included everything. In early 2020, VIX was above 30 for weeks. Using VIX PERCENTILE RANK relative to its trailing 1-year distribution would be more robust to structural shifts.
>
> **Verdict:** [PLAUSIBLE — REASON: Absolute VIX thresholds (20/30) are common in practitioner usage and have some empirical support. However, VIX levels drift over time with market structure. VIX percentile rank (e.g., below 30th percentile = low vol, above 70th = high vol) is more adaptive to structural changes but adds complexity. For a simple system, absolute tiers at 20/30 are adequate. If you want one improvement, consider using VIX relative to its 252-day moving average (VIX/VIX_MA > 1.2 = elevated, < 0.8 = suppressed) instead of fixed levels.]

### Claim 5: "Momentum lookback periods should adapt to market speed."

> **Reasoning:** There is some research on "adaptive momentum" — Huang, Jiang, Tu & Zhou (2015, "Investor Sentiment Aligned: A Powerful Predictor of Stock Returns") explored time-varying factor weights. However, adaptively changing LOOKBACK PERIODS specifically is less well-documented and adds a significant parameter (how do you determine the "right" lookback for the current regime?). Most robustness in momentum comes from COMBINING multiple lookback periods (e.g., averaging 1-month, 3-month, and 6-month momentum) rather than trying to select the "right" one dynamically.
>
> **Verdict:** [MISLEADING — CORRECTION: Rather than adapting lookback periods to regime (which is hard to do without overfitting), the evidence-based approach is to COMBINE multiple lookback periods into a composite momentum signal. Averaging short-, medium-, and long-term momentum is more robust than trying to dynamically select the right window. This is what AQR does in practice — their momentum strategies blend multiple horizons. For your system, consider using average(1-month ROC, 3-month ROC, 6-month RS) rather than trying to switch between them based on regime.]

### Claim 6: "More than 2-3 regime-adaptive parameters crosses into overfitting."

> **Reasoning:** This is consistent with the general principle of parsimony in model building. Each regime-adaptive parameter adds at least 2-3 new degrees of freedom (the threshold values for each regime). With 2-3 regime tiers and 4+ adaptive parameters, you quickly have 10+ new degrees of freedom that can all be overfit. Harvey, Liu & Zhu (2016) discuss the "multiple testing" problem in finance and argue for stringent significance thresholds when testing many parameters.
>
> **Verdict:** [PLAUSIBLE — REASON: While no paper specifically states "2-3 is the limit," the general principle of parsimony and the multiple testing problem (Harvey et al., 2016) strongly imply that each additional adaptive parameter must clear a high evidence bar. For a retail system with limited backtest data (~238 trades), adapting 1-2 parameters (position size + stop method) is defensible; adapting 4+ parameters across 3 regime tiers creates 12+ new degrees of freedom that cannot be reliably validated with your sample size.]

---

## PROMPT 5: What Separates Successful Systems from Failures

### Claim 1: "Top 5 failure modes: overfitting, transaction costs, regime change, slippage, behavioral deviation."

> **Reasoning:** This list is broadly consistent with practitioner literature but I'd refine the ordering:
> 1. **Overfitting** — universally cited as #1 (Harvey et al. 2016, Bailey et al. 2014 "Pseudo-Mathematics and Financial Charlatanism")
> 2. **Regime change / non-stationarity** — factors that worked stop working (McLean & Pontiff, 2016, "Does Academic Research Destroy Stock Return Predictability?")
> 3. **Transaction costs + slippage** — combined (Novy-Marx & Velikov, 2016)
> 4. **Behavioral deviation** — the trader overrides the system (documented in behavioral finance literature)
> 5. **Survivorship/selection bias in research** — backtests look good because they were selected from thousands of tested strategies
>
> **Verdict:** [PLAUSIBLE — REASON: The list is broadly accurate but I'd add SURVIVORSHIP/SELECTION BIAS (you only see the strategies that "worked" in backtesting) as a top-5 cause, ahead of slippage. McLean & Pontiff (2016) showed that factor returns decline by ~58% after publication, suggesting a large portion of documented alpha was either overfit or arbitraged away. The ordering should be: (1) Overfitting, (2) Regime change / alpha decay, (3) Selection bias, (4) Transaction costs, (5) Behavioral deviation.]

### Claim 2: "Walk-forward testing is sufficient to prevent overfitting."

> **Reasoning:** Walk-forward is necessary but NOT sufficient. It's one form of out-of-sample testing, but it can still be gamed if you run multiple walk-forward configurations and pick the best one (this is just overfitting at a higher level). Additional anti-overfitting measures include:
> - **Minimum trade count** — at least 100+ trades per configuration
> - **Parameter stability** — does the strategy work across a RANGE of nearby parameters? (e.g., does it still work with ADX ≥ 18 or ≥ 22, not just ≥ 20?)
> - **Cross-instrument testing** — does it work on different stock universes?
> - **Monte Carlo permutation** — shuffle trade entry dates randomly and compare
> - **Deflated Sharpe Ratio** (Bailey & López de Prado, 2014) — adjusts Sharpe for multiple testing
>
> **Verdict:** [MISLEADING — CORRECTION: Walk-forward testing is necessary but NOT sufficient. It prevents the most naive form of overfitting but can itself be overfit if multiple walk-forward configurations are tested. You need MULTIPLE anti-overfitting checks: (1) Walk-forward (you have this), (2) Parameter stability analysis (does it work at nearby parameter values?), (3) Minimum 100+ trades, (4) Deflated Sharpe Ratio (Bailey & López de Prado, 2014) to adjust for multiple testing. Your p=0.002 is strong, which is encouraging, but you should also verify parameter stability.]

### Claim 3: "Simpler systems outperform complex ones out-of-sample (simplicity premium)."

> **Reasoning:** DeMiguel et al. (2009) showed 1/N equal weighting beats optimized portfolios. The bias-variance tradeoff in machine learning directly applies: more complex models fit training data better but generalize worse. In trading specifically, Hsu, Kalesnik & Viswanathan (2015, "Is Sizing More Important Than Selecting?") showed that simple market-cap weighting outperforms many complex "smart beta" strategies. The general pattern is clear: simple, robust strategies with few parameters tend to survive out-of-sample better than complex multi-parameter systems.
>
> **Verdict:** [VERIFIED — SOURCE: DeMiguel et al. (2009, Review of Financial Studies) demonstrated that equal-weighted portfolios outperform optimized ones. The bias-variance tradeoff is well-established in statistical learning theory (Hastie, Tibshirani & Friedman, "Elements of Statistical Learning"). In trading specifically, fewer parameters = fewer degrees of freedom to overfit = better out-of-sample survival. This is the strongest argument for keeping your system SIMPLE during the evolution. Add factors/features only when the evidence is overwhelming.]

### Claim 4: "For $10M+ volume stocks, slippage is <5 bps per trade."

> **Reasoning:** For liquid US equities ($10M+ daily dollar volume) traded with limit orders at swing timeframes (not intraday), bid-ask spreads are typically 1-5 bps. Market orders add market impact. For a retail trader doing 1-5 trades/week with position sizes of $10K-$25K (from a $50-100K account), market impact is negligible relative to the stock's daily volume. Total cost per round-trip (in + out) for $10M+ volume stocks: approximately 5-15 bps including spread, commission ($0 at most brokers), and minor slippage.
>
> **Verdict:** [PLAUSIBLE — REASON: For retail-sized orders ($10K-$25K) in liquid stocks ($10M+ daily volume), slippage of <5 bps per side is reasonable with limit orders. With market orders, expect 5-10 bps per side. Round-trip costs of 10-20 bps are realistic for this setup. This is small relative to the 5-15% average win in swing trading, but compounds over many trades. I cannot cite a specific study benchmarking retail slippage at exactly these parameters, but the estimates are consistent with market microstructure literature on bid-ask spreads (Hasbrouck, 2007).]

### Claim 5: "Factors from 2010-2020 continue to work 2020-2026 with similar magnitude."

> **Reasoning:** McLean & Pontiff (2016, "Does Academic Research Destroy Stock Return Predictability?") showed that factor returns decline ~58% after academic publication as investors exploit the anomaly. Post-2020 specifically: momentum had a severe crash in Q4 2020 during the COVID recovery rotation, value had a historic resurgence in 2021-2022 after a decade of underperformance, and quality has remained relatively stable. The overall picture: factor PREMIA are smaller than historical backtests suggest, and they're more volatile across regimes.
>
> **Verdict:** [MISLEADING — CORRECTION: Factor returns have decayed significantly. McLean & Pontiff (2016) documented ~58% decay in anomaly returns post-publication. Momentum specifically experienced severe drawdowns in 2020 and 2023. Value had a historic reversal (underperformed 2010-2020, outperformed 2021-2022). The factors still "work" in the sense that they have positive long-run premia, but the MAGNITUDE is smaller and the VOLATILITY is higher than backtests suggest. Building a system that depends on a specific factor maintaining its historical Sharpe ratio is risky. Diversification across factors is the standard defense.]

### Claim 6: "Retail should avoid: intraday MR, stat arb, HF market making, options flow."

> **Reasoning:** These strategies require: (a) low-latency execution infrastructure (stat arb, market making), (b) real-time options data feeds costing thousands/month (options flow), (c) co-location or direct market access (HFT). A retail trader on Interactive Brokers with manual execution cannot compete. Edges STILL available to retail: (a) medium-term momentum (too slow for HFT to care about), (b) earnings drift (too small for large funds to pursue), (c) small/micro-cap stocks (too illiquid for institutional capital), (d) patience and holding period (most funds face redemption pressure and quarterly performance reviews).
>
> **Verdict:** [VERIFIED — SOURCE: This is well-established in market microstructure and trading strategy literature. Retail advantages are documented in Barber & Odean's behavioral finance research (their work also shows where retail DISADVANTAGES lie). The key retail edges — medium-term momentum in small/mid-caps, patience, and lack of redemption pressure — are genuinely structural advantages that institutions cannot easily replicate. Your system targeting 5-30 day momentum in liquid stocks is in the correct "edge space" for retail.]

### Claim 7: "Minimum viable system: 2-3 factors, equal-weighted, ATR stops, weekly rebalance."

> **Reasoning:** Based on all the evidence above: (1) Momentum (3-6 month) as primary factor — most robust anomaly at medium-term horizons, (2) Trend/regime filter (SPY > 200 SMA) to avoid bear markets, (3) ATR-based stops for risk management, (4) Equal-weight the factors to avoid optimization overfitting, (5) Weekly rebalancing to balance signal freshness with transaction costs.
>
> **Verdict:** [PLAUSIBLE — REASON: This is consistent with the evidence surveyed above. A minimal system of momentum + regime filter + ATR stops + equal weights is supported by: Jegadeesh & Titman (1993) for momentum, Faber (2007) for regime filtering, DeMiguel et al. (2009) for equal weighting, LeBeau & Lucas (1992) for ATR stops. The weakest link is the lack of a quality/fundamental filter — adding a simple profitability screen (Novy-Marx 2013) as a binary gate would improve robustness with minimal complexity. The minimum viable system is probably: Momentum (3-month ROC percentile rank) + Regime (SPY > 200 SMA) + Quality gate (gross profitability > median) + ATR stops.]

---

## CLAUDE'S KEY TAKEAWAYS (Cross-cutting themes)

### 1. The Simplicity Premium Is Real
Across all 5 prompts, the evidence consistently says: simpler is better out-of-sample. DeMiguel (2009) on equal weights, Harvey et al. (2016) on multiple testing, McLean & Pontiff (2016) on factor decay — all point the same direction. **Do NOT add complexity unless the evidence is overwhelming.**

### 2. Your System Is Closer to Universal Than You Think
Most of what you have maps directly to evidence-based factors:
- Trend Template → Trend factor (well-evidenced)
- RS vs SPY → Momentum factor (well-evidenced, but raise threshold)
- ROE/Revenue/D-E → Quality filter (well-evidenced at longer horizons)
- VIX + SPY > 200 SMA → Regime filter (well-evidenced)

The Minervini "skin" makes it LOOK practitioner-specific, but the underlying factors ARE universal.

### 3. The Biggest Bang-for-Buck Changes
In priority order:
1. **Position sizing by volatility regime** — most impactful, best-evidenced (Moreira & Muir 2017)
2. **Raise RS threshold** from 1.0 toward top-quartile — makes momentum factor more selective
3. **Add mean-reversion arm** (RSI(2) < 10 + Price > 200 SMA) — fills the "silent in choppy markets" gap
4. **Equal-weight factors** instead of optimized weights — prevents overfitting
5. **Combine multiple momentum horizons** (1-month, 3-month, 6-month average) — more robust than single lookback

### 4. What NOT to Do
- Don't optimize factor weights on your 238 trades — not enough data
- Don't add more than 1-2 regime-adaptive parameters
- Don't drop patterns entirely — keep as optional binary overlay, not primary signal
- Don't try to build a full cross-sectional ranking system — your signal frequency is fine for discretionary trading
