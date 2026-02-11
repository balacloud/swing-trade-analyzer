# Perplexity Research: Holding Period & RSI Thresholds

> **Created:** Day 51 (February 11, 2026)
> **Purpose:** Validate assumptions in HOLDING_PERIOD_SELECTOR_PLAN.md before implementation
> **Status:** RESEARCH IN PROGRESS

---

## Research Questions for Perplexity

### Question 1: RSI Thresholds by Holding Period

```
I'm building a swing trade analyzer. I need evidence-based RSI (Relative Strength Index) thresholds for different holding periods.

Current UNVERIFIED assumptions:
- 5-10 day trades: RSI 40-65 (strict)
- 15-30 day trades: RSI 35-70 (moderate)
- 1-3 month trades: RSI 30-75 (relaxed)

Questions:
1. Is there academic research supporting different RSI thresholds for different holding periods?
2. What RSI levels have been shown to predict mean reversion within:
   - 5-10 trading days?
   - 15-30 trading days?
   - 1-3 months?
3. Are there any backtested studies showing optimal RSI entry thresholds by timeframe?
4. What is the false positive rate for RSI overbought (>70) predicting pullbacks within 7 days?

Please cite specific studies, papers, or backtested results with sample sizes and timeframes.
```

### Question 2: Mean Reversion Timing

```
For swing trading stocks:
1. When RSI exceeds 70, what is the average number of days until a 3-5% pullback occurs?
2. When RSI exceeds 80, does the pullback timing differ significantly?
3. Is there research on "how long can overbought conditions persist" in trending stocks?
4. Does the relationship between RSI and pullback timing differ for:
   - Strong uptrend stocks (like 8/8 on Minervini's Trend Template)?
   - Weak trend stocks?

Looking for backtested data, not theoretical explanations.
```

### Question 3: Timeframe-Aware Trading Systems

```
Are there existing trading systems or research that adjust entry criteria based on intended holding period?

Specifically:
1. Do any systems use stricter technical filters for shorter holding periods?
2. Is there evidence that momentum strategies work better on longer timeframes?
3. What's the optimal RSI range for:
   - Day traders (1-5 days)
   - Swing traders (1-4 weeks)
   - Position traders (1-6 months)

I'm looking for systems that have been backtested with published results, not theoretical frameworks.
```

### Question 4: Minervini SEPA + RSI Validation

```
Mark Minervini's SEPA (Specific Entry Point Analysis) uses Stage 2 uptrends for swing trades.

Questions:
1. Does Minervini recommend different RSI thresholds for different holding periods?
2. What does his research show about entering overbought stocks (RSI > 70) in Stage 2 uptrends?
3. Is there backtested data on SEPA entries filtered by RSI level?
4. What is the typical holding period for SEPA trades, and does RSI affect expected returns?
```

### Question 5: Practical Trader Experience

```
From practitioner experience and trading forums:
1. What RSI levels do successful swing traders actually use for entries?
2. Is there consensus on avoiding RSI > X for short-term trades?
3. Do any trading platforms or tools provide timeframe-specific RSI recommendations?
4. What's the typical failure rate for entering stocks with RSI > 70 in swing trades?

Looking for real-world experience, not just academic theory.
```

---

## What We're Trying to Validate

| Assumption | Status | Evidence Needed |
|------------|--------|-----------------|
| RSI 65 is overbought for 5-10 day trades | UNVERIFIED | Backtest showing pullback frequency |
| RSI 70 is acceptable for 15-30 day trades | UNVERIFIED | Studies on trend persistence |
| RSI 75 is acceptable for 1-3 month trades | UNVERIFIED | Momentum research for longer holds |
| Mean reversion is faster in shorter timeframes | PLAUSIBLE | Statistical evidence |
| Strong trends (TT 8/8) tolerate higher RSI | PLAUSIBLE | Minervini research or backtest |

---

## How to Use This Document

1. Copy each question block to Perplexity
2. Record answers in the "Research Results" section below
3. Update HOLDING_PERIOD_SELECTOR_PLAN.md with validated thresholds
4. If thresholds can't be validated, design our own backtest

---

## Research Results

### Q1: RSI Thresholds by Holding Period
**Perplexity Response:**
```
[PASTE RESPONSE HERE]
## Executive Summary

There is **limited academic research** directly linking specific RSI thresholds to holding periods. Most published studies focus on RSI as a momentum indicator for trend reversals rather than timeframe-specific mean reversion. The empirical evidence suggests that **shorter RSI periods (2-10 days) with more extreme thresholds (15/85 or 20/80) outperform longer periods** for swing trading, but your proposed thresholds lack rigorous statistical support in peer-reviewed literature. [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

## Academic Research on RSI & Holding Periods

### Limited Peer-Reviewed Evidence

The most comprehensive academic study on RSI effectiveness was published in *Sensors* (2023), examining cryptocurrency markets over 4 years (2018-2022). This study tested RSI signals across multiple timeframes but **did not establish holding-period-specific thresholds** as you've hypothesized. Key findings: [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)

- **Short-term (1-7 days):** RSI oversold (<30) showed average returns of 0.49%-1.58% for Bitcoin after 1-7 days [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)
- **Medium-term (14 days):** Returns increased to 1.33%-4.59% [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)
- **Long-term (30-60 days):** Returns ranged 2.40%-8.86% [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)

However, the study examined **fixed RSI thresholds (30/70)** rather than adjusting thresholds by holding period as your model proposes.

### Critical Gap in Your Assumptions

**No academic study validates your specific tiered approach** (40-65 for 5-10 days, 35-70 for 15-30 days, 30-75 for 1-3 months). The research instead suggests the **opposite strategy may be more effective**: using more extreme thresholds for shorter timeframes. [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)

## Empirical Backtesting Results by Timeframe

### 5-10 Day Mean Reversion

A systematic backtest of the **5-day RSI strategy** on S&P 500 SPDRs (sector ETFs) found: [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)

- **Entry threshold:** RSI < 30
- **Exit thresholds tested:** RSI > 70, 75, 80
- **Result:** Higher exit thresholds (75-80) produced better returns than 70, suggesting trends extend further than standard thresholds predict [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)
- **Win rate:** The strategy showed profitability but specific win rates weren't disclosed

**Contradiction to your assumption:** The study did not support a narrower 40-65 range for short holding periods. Instead, it validated the traditional 30/70+ thresholds.

### 15-30 Day Holding Period

**No dedicated studies were found** for 15-30 day holding periods. Practitioners suggest using RSI periods of 14-25 for "medium-term swing trades (5-15 days)" with 30/70 or adjusted 60/40 thresholds, but these are **untested heuristics**. [tradersunion](https://tradersunion.com/interesting-articles/rsi-indicator-strategies/settings-for-swing-trading/)

### 1-3 Month Holding Period

The cryptocurrency study examined 30-60 day returns but found that **standard 30/70 thresholds remained optimal** even for longer timeframes. Relaxing thresholds to 30-75 as you propose lacks empirical support. [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)

## False Positive Rates: The Critical Missing Data

### RSI Overbought (>70) Pullback Prediction

**No studies quantify the false positive rate for RSI >70 predicting pullbacks within 7 days**. The available research reveals:

- The cryptocurrency study measured *returns* after overbought signals but did not calculate false positive rates [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)
- A backtest blog post (QuantifiedStrategies) claimed a **91% win rate** for a 2-day RSI strategy but did not disclose the false positive rate for individual signals [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
- Industry guidance acknowledges RSI >70 can persist in strong uptrends without triggering pullbacks, but **quantified false positive rates are not published** [luxalgo](https://www.luxalgo.com/blog/rsi-overbought-and-oversold-signals-explained/)

### Why This Data Doesn't Exist

Technical analysis research typically reports **strategy profitability** (Compound Annual Return, Sharpe Ratio) rather than signal accuracy metrics (false positive/negative rates). This is a significant methodological gap in the literature. [papers.ssrn](https://papers.ssrn.com/sol3/Delivery.cfm/4878676.pdf?abstractid=4878676&mirid=1)

## Optimal RSI Settings: What Research Actually Shows

### Period Length Matters More Than Thresholds

Backtested evidence from QuantifiedStrategies (testing stocks over multiple decades): [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

- **2-day RSI** with buy <15, sell >85: Produced 2x returns vs. 10-day RSI
- **10-day RSI** with buy <30, sell >70: Profitable but half the performance
- **Exposure:** Both strategies spent ~50% of time in the market

**Key insight:** Shorter RSI periods (2-10) require *more extreme* thresholds (15/85), not the moderate 40-65 range you proposed.

### Timeframe vs. Threshold Relationship

Trading practitioners suggest: [mc2](https://www.mc2.fi/blog/best-rsi-settings-for-swing-trading/)

- **1-5 day swings:** 4-hour charts, RSI 14, thresholds 30/70
- **5-15 day swings:** Daily charts, RSI 14-20, thresholds 30/70 or 60/40
- **Intraday (<2 days):** 1-hour charts, RSI 5-7, thresholds 80/20

However, these are **optimization heuristics from platform backtests**, not peer-reviewed findings with disclosed sample sizes. [tradesearcher](https://tradesearcher.ai/strategies/2302-rsi-mean-reversion-strategy)

## Data Quality & Behavioral Check

### Confirmation Bias Warning

Your assumptions appear to reflect **familiarity bias** toward moderate thresholds (40-65) that may feel "safer" but lack empirical support. The counter-evidence suggests:

- Extreme thresholds (15/85 for short-term, 20/80 for medium-term) historically outperform moderate ranges
- Relaxing thresholds for longer timeframes (your 30-75 proposal) contradicts the finding that 30/70 remains effective across timeframes [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

### The "Quant Reality" Check

**Zero peer-reviewed studies establish holding-period-adjusted RSI thresholds**. The available backtests focus on:

1. **Period length adjustment** (2 vs. 14 vs. 25 days) [tradersunion](https://tradersunion.com/interesting-articles/rsi-indicator-strategies/settings-for-swing-trading/)
2. **Fixed threshold optimization** (testing 70 vs. 75 vs. 80 exits) [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)
3. **Trend filters** (only taking RSI signals when broader trend conditions are met) [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)

Your three-tier threshold model is **novel but unvalidated**.

## Risk Assessment: Bear Case for Your Assumptions

1. **No academic foundation:** Your thresholds are not derived from published research
2. **Contradicts empirical evidence:** Shorter timeframes have historically required more extreme (not moderate) thresholds [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
3. **False positive data unavailable:** Cannot assess Type I error rates for 7-day pullback predictions
4. **Sample size unknown:** Practitioner backtests rarely disclose the number of signals tested or out-of-sample validation [tradesearcher](https://tradesearcher.ai/strategies/2302-rsi-mean-reversion-strategy)
5. **Market regime dependency:** The cryptocurrency study showed RSI effectiveness varies dramatically by market phase (bull/bear/sideways) [pmc.ncbi.nlm.nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC9920669/)

### Recommendation for Rigorous Testing

To validate your model, you must:

- Backtest on **10+ years of data** across multiple market regimes
- Report **signal count, win rate, false positive rate, and Sharpe ratio** for each threshold/timeframe combination
- Conduct **walk-forward analysis** to avoid overfitting
- Test on **multiple asset classes** (US equities, Canadian equities, Indian markets per your mandate)
```

**Key Findings:**
- [ ] Specific thresholds cited
- [ ] Sample size and timeframe
- [ ] Confidence level

---

### Q2: Mean Reversion Timing
**Perplexity Response:**
```
## Executive Summary

**The critical finding:** There is extremely limited peer-reviewed data quantifying the exact number of days from RSI overbought signals to specific pullback magnitudes (3-5%). However, recent empirical studies reveal that **RSI persistence in overbought zones varies dramatically by trend strength**—overbought conditions last significantly longer in strong trends, making traditional RSI thresholds unreliable for timing pullbacks in momentum stocks. [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)

***

## Pullback Timing: The Limited Data Available

### RSI >70 Pullback Timing

**No academic studies provide average days-to-pullback data** for RSI >70 to 3-5% corrections. However, related findings include:

- **Bitcoin (30-day window):** From 2022-2025, 250 overbought events (RSI >70) showed a win rate of ~65% by day 30, with cumulative returns of +6.4% versus benchmark +3.5%. This contradicts the expectation of immediate pullbacks—overbought conditions preceded *continued gains* rather than corrections. [ainvest](https://www.ainvest.com/aime/share/backtest-performance-buying-bitcoin-rsi-overbought-holding-30-trading-days-2022-1e3f1c/)

- **S&P 500 stocks (2023 data):** 68% of stocks hitting **RSI >80** experienced declines of **5%+ within two weeks** (14 trading days). This is the most specific backtest data available addressing your question, though it applies to RSI >80, not 70. [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

### RSI >80 Pullback Timing

The only quantified finding is the **2-week pullback statistic** cited above. This suggests: [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

- **RSI >80** creates a **68% probability** of a 5%+ decline within **14 days**
- **Implication:** RSI >80 does appear to significantly increase pullback risk compared to RSI 70-80, though the exact timing distribution (days 1-14) is not disclosed

### Critical Gap in Research

The literature focuses on **strategy profitability** (e.g., "buy when RSI <30, hold 30 days") rather than **signal-to-pullback timing** (e.g., "average days from RSI >70 to 3% correction"). This represents a major data void for your specific use case. [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

***

## Overbought Persistence in Trending vs. Weak Stocks

### Academic Study: Malaysian Market (2015-2024)

A 2024 peer-reviewed study analyzing the FTSE Bursa Malaysia Index and 10 stocks over 10 years provides the strongest evidence on RSI persistence: [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)

**Key Findings:**

- **Strong trends (ADX >25):** RSI remained in overbought zones (>70) for **significantly longer durations** compared to weak trends [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
- **Weak trends (ADX <20):** RSI durations in extreme zones were **significantly shorter**, supporting mean reversion expectations [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
- **Contradictory signals:** The study documented "overbought conditions during strong downtrends" and "oversold conditions during strong uptrends," demonstrating that **RSI extremes in trending markets are unreliable reversal signals** [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)

**Critical conclusion from researchers:** "RSI behavior challenges the conventional use of RSI as a reversal signal and suggests its interpretation should be complemented with other indicators". [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)

### Practical Evidence: RSI in Uptrends

- **Strong uptrends:** Technical analysts observe RSI can remain >70 for **days to weeks** without triggering meaningful pullbacks [abouttrading.substack](https://abouttrading.substack.com/p/i-backtested-a-powerful-strategy)
- **Momentum continuation:** One practitioner noted that in strong 36-month uptrends, overbought RSI readings are "more of a positive thing" for medium/long-term investors [youtube](https://www.youtube.com/watch?v=BRvxCkRlJd0)
- **Institutional behavior:** Quantitative funds reportedly interpret RSI >70 in trending regimes as a **buy signal** (momentum confirmation) rather than an exit signal [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

***

## Minervini Trend Template & RSI Overbought

### Empirical Observations on Strong Trend Stocks

Minervini's examples frequently feature stocks with **RSI >78**, well into overbought territory. However: [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

- **The contradiction:** While Minervini's template (RS ranking ≥70, above 50/150/200 MAs) successfully identifies outperformers, these stocks are often simultaneously in vulnerable overbought zones [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
- **Pullback risk:** The analysis notes that buying stocks meeting Minervini criteria at RSI 79-82 resulted in **10% pullbacks within one month** in some 2023 cases [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
- **The dilemma:** Stocks meeting all Minervini criteria often represent the **end phase** of a trend, not the beginning [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

### Trend Strength Differential: No Direct Backtest

**No study has systematically backtested RSI pullback timing comparing:**
- Strong trend stocks (8/8 Minervini criteria or ADX >30) vs.
- Weak trend stocks (fewer criteria met or ADX <20)

However, the Malaysian study's findings on ADX-categorized trends strongly suggest **pullbacks take longer in strong trends**. [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)

***

## RSI Strategy Performance: Institutional-Grade Context

### Why Traditional Thresholds Fail in Trends

Multiple backtests confirm RSI behaves differently in trending versus ranging markets: [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-range-momentum-trading-strategy/)

- **Range-bound markets:** RSI 70/30 thresholds work reliably for reversals [luxalgo](https://www.luxalgo.com/blog/rsi-overbought-and-oversold-signals-explained/)
- **Strong uptrends:** RSI typically ranges 40-80 (not 30-70), and pullbacks find support at RSI 40-50, not 30 [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-range-momentum-trading-strategy/)
- **Strong downtrends:** RSI ranges 20-60 [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-range-momentum-trading-strategy/)

### Exit Threshold Testing: 5-Day RSI

A backtest of S&P 500 sector ETFs tested different RSI exit thresholds: [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)
- **Entry:** RSI <30
- **Exit comparison:** RSI >70 vs. >75 vs. >80
- **Result:** Higher thresholds (75-80) outperformed 70, indicating trends extend beyond traditional overbought levels [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)

### 70/30 Strategy: Poor Performance

A 30-year backtest (1993-2023) of the 70/30 RSI strategy on S&P 500: [quantifiedstrategies](https://www.quantifiedstrategies.com/70-30-rsi-trading-strategy/)
- **Rules:** Buy when 5-day RSI <30, sell when >70
- **Results:** Only 191 trades, 1% average gain, 39% max drawdown
- **Conclusion:** Strategy "not particularly reliable or profitable" because it exits at RSI 70, missing continued momentum [quantifiedstrategies](https://www.quantifiedstrategies.com/70-30-rsi-trading-strategy/)

***

## Behavioral Finance Check

### Anchoring & Confirmation Bias

Your questions reveal potential **threshold anchoring**—fixating on 70/80 as immutable reversal triggers. The evidence suggests:

- These thresholds are **regime-dependent** (work in ranges, fail in trends) [luxalgo](https://www.luxalgo.com/blog/rsi-overbought-and-oversold-signals-explained/)
- You may be experiencing **confirmation bias** by seeking data supporting pullback expectations rather than investigating *when* RSI overbought conditions are unreliable

### Loss Aversion Warning

The desire for precise pullback timing (3-5% within X days) may reflect **risk aversion** leading to premature exits. The data shows:

- Exiting at RSI 70 in trending stocks **underperforms** holding for RSI 75-80 [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)
- Strong trend stocks (Minervini-quality) often experience 10%+ pullbacks *after months* at elevated RSI, not days [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

***

## Risk Assessment: Bear Case for Timing Pullbacks with RSI

1. **No quantified timing data:** The "average days to 3-5% pullback" metric you seek **does not exist in published research**
2. **68% accuracy at best:** Even the strongest data point (RSI >80 → 5% decline in 14 days) has a **32% false positive rate** [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
3. **Trend regime dependency:** Without confirming weak trend conditions (ADX <20), RSI >70 has **low predictive power** for pullbacks [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
4. **Survivorship bias:** Studies reporting RSI >70 followed by gains may reflect **cherry-picked time periods** (e.g., 2022-2025 crypto bull market) [ainvest](https://www.ainvest.com/aime/share/backtest-performance-buying-bitcoin-rsi-overbought-holding-30-trading-days-2022-1e3f1c/)
5. **Minervini paradox:** Stocks meeting institutional-grade trend criteria (8/8 template) are *by definition* overbought, yet outperform [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)

***

## What the Data Actually Supports

### Evidence-Based Conclusions

1. **RSI >80 is materially different from >70:** 68% pullback probability within 2 weeks for RSI >80 [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
2. **Trend strength matters more than RSI level:** Strong trends (high ADX) sustain overbought RSI for extended periods [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
3. **Weak trends mean-revert faster:** RSI durations in extremes are significantly shorter when ADX <20 [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
4. **No timeframe-specific thresholds validated:** Your proposed 5-10 day vs. 15-30 day vs. 1-3 month threshold adjustments lack empirical support

### Recommended Approach

Rather than relying on RSI thresholds alone:
- **Combine with ADX:** Only trade RSI mean reversion when ADX <20 (weak trend) [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
- **Use RSI divergence:** More reliable than absolute levels in trends [luxalgo](https://www.luxalgo.com/blog/rsi-overbought-and-oversold-signals-explained/)
- **Wait for pullback confirmation:** For Minervini-quality stocks at RSI >70, wait for actual pullback to 50-day MA before entering [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
- **Test your specific parameters:** Backtest your 5-10/15-30/1-3 month holding periods with disclosed sample sizes and out-of-sample validation
```

**Key Findings:**
- [ ] Average days to pullback from RSI >70
- [ ] Variance/reliability of prediction
- [ ] Trend strength impact

---

### Q3: Timeframe-Aware Trading Systems
**Perplexity Response:**
```
[## Executive Summary

**Yes, there are published systems with empirical evidence.** The most robust finding from peer-reviewed research is the **"12-18 month rule"**: momentum strategies perform optimally when formation period + holding period = 12-18 months, with longer formation periods paired with shorter holding periods. However, **no academic research validates specific RSI thresholds by holding period**—this represents an unexplored frontier in technical analysis. [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

***

## Systems That Adjust Entry Criteria by Holding Period

### Academic Research: The Formation/Holding Period Relationship

**Study 1: HIMCO & Newfound Research (2018)**  
Tested momentum strategies across developed country indices and U.S. industry groups from 1926-2018: [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

**Key Finding:** Performance peaks when **formation period + holding period = 12-14 months** [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

**Practical implications:**
- **5-month lookback → hold 7-9 months** (total 12-14)
- **12-month lookback → hold 1-3 months** (total 13-15)

**Evidence quality:** Replicated across 3 datasets (country indices, 12-industry groups, 49-industry groups), both long/short and long-only portfolios [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

***

**Study 2: York University Canadian Market Study (1961-1999)**  
Analyzed 14 TSE300 sectors with 1,296 different formation/holding combinations: [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**Key Findings:**
- **12-month formation + 3-month holding:** 1.05% monthly return, statistically significant [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)
- **12-month formation + 6-month holding:** 0.85% monthly return [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)
- **Stricter rule validated:** "Given the same length of return continuation, using a longer evaluation period and shorter holding period is much more reliable and profitable" [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**Specific performance metrics:**
- Annual returns: 7.78% to 12.64% for optimal combinations
- Beta: Near zero (0.105-0.164) for profitable strategies  
- Transaction cost breakeven: 3.89% per year (extremely high tolerance) [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

***

**Study 3: Jegadeesh-Titman (1993) - Seminal Paper**  
The foundational momentum study (cited 17,784 times) tested U.S. stocks 1965-1989: [bauer.uh](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)

**Finding:** 1.31% monthly returns using various formation/holding periods, with optimal performance at 6-12 month formations [bauer.uh](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)

***

### Why This Matters: Stricter Filters for Shorter Periods

The research **validates your intuition** about stricter criteria for shorter holding periods, but through a different mechanism than you proposed:

**For 1-4 week holds:**  
- Should use **9-12 month formation period** (not shorter RSI lookbacks)
- Reason: Longer formation period identifies stronger trends that persist into short-term holds [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**For 1-6 month holds:**  
- Optimal: **12-month formation + 3-6 month hold** [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)
- Returns: 0.65-1.05% monthly vs. 0.27-0.53% for shorter formations [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**Behavioral interpretation:** Shorter holding periods require **more rigorous momentum confirmation** (longer lookback), not relaxed criteria. This contradicts the common assumption that short-term trading should use short-term indicators. [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

***

## Momentum Performance by Timeframe

### Does Momentum Work Better on Longer Timeframes?

**The evidence is nuanced:**

**Short-term momentum (1-6 months):**  
- A 2014 study titled "Momentum is really short-term momentum" found that when excluding months 2 and 12 from lookback periods, **intermediate momentum (12-7 months) and recent momentum (6-3 months) showed no significant difference** across 26 international markets [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426614003252)
- **Conclusion:** Short-term momentum is equally powerful when properly measured [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426614003252)

**Long-term momentum (1-2 years):**  
- The Canadian study showed return continuation lasting **up to 24 months** (12-month formation + 12-month hold), after which reversals occurred [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)
- A 2025 paper on "Momentum at Long Holding Periods" demonstrated strategies can **reduce turnover, lower risk, and increase returns** by maintaining momentum exposure over long horizons [papers.ssrn](https://papers.ssrn.com/sol3/Delivery.cfm/5199701.pdf?abstractid=5199701&mirid=1)

**Critical risk: Momentum turning points**  
- Research from Morningstar (2023) found that **slow momentum strategies suffer more around turning points** despite better long-run performance, while fast strategies are more effective during regime changes [morningstar](https://www.morningstar.com/markets/achilles-heel-momentum-strategies)

***

## Optimal RSI Settings by Trading Style: Practitioner Evidence

### Day Traders (1-5 days)

**Backtested recommendations**: [goatfundedtrader](https://www.goatfundedtrader.com/blog/best-rsi-settings-for-day-trading)

| Strategy Type | RSI Period | Thresholds | Chart Timeframe |
|---------------|-----------|------------|----------------|
| Scalping | 5-7 | 20/80 | 1-5 minute |
| Intraday momentum | 9 | 25/75 | 5-15 minute |
| Trend-biased | 14 | 40/60 (pullbacks) | 15-60 minute |

**Evidence quality:** Based on "focused backtests" but sample sizes and win rates not disclosed [goatfundedtrader](https://www.goatfundedtrader.com/blog/best-rsi-settings-for-day-trading)

**Key insight:** Day traders use **shorter RSI periods with more extreme thresholds**, contradicting your assumption of moderate 40-65 ranges for short timeframes. [goatfundedtrader](https://www.goatfundedtrader.com/blog/best-rsi-settings-for-day-trading)

***

### Swing Traders (1-4 weeks)

**Published guidelines**: [tradersunion](https://tradersunion.com/interesting-articles/rsi-indicator-strategies/settings-for-swing-trading/)

| Holding Period | RSI Period | Thresholds | Chart Timeframe |
|---------------|-----------|------------|----------------|
| 1-5 day swings | 14 | 30/70 | 4-hour |
| 5-15 day swings | 14-25 | 30/70 or 60/40 | Daily |
| 15-30 day swings | 14-20 | 30/70 | Daily |

**Alternative backtested approach**: [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
- **2-day RSI with 15/85 thresholds:** 2x returns vs. 10-day RSI  
- **10-day RSI with 30/70 thresholds:** Profitable but half the performance  
- **Win rate claimed:** 91% (but methodology not peer-reviewed) [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

**Evidence quality:** Industry practitioners report these as "optimal settings" but lack published statistical validation with disclosed sample sizes. [mc2](https://www.mc2.fi/blog/best-rsi-settings-for-swing-trading/)

***

### Position Traders (1-6 months)

**No specific RSI research exists for position trading timeframes.** The academic literature instead focuses on:

- **Momentum factor exposure** (formation periods of 6-12 months) [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)
- **Moving average crossovers** rather than RSI for long-term signals [ewadirect](https://www.ewadirect.com/proceedings/aemps/article/view/5936)

**Why RSI is less studied for position trading:**  
A 2023 study on time-series momentum (2000-2022 S&P 500 data) found that **momentum strategies perform better when trends are stronger**, but focused on moving averages rather than RSI. This suggests long-term traders prioritize trend filters over oscillators. [ewadirect](https://www.ewadirect.com/proceedings/aemps/article/view/5936)

***

## Critical Gaps in Research: What Doesn't Exist

### No Published Systems Combine Both Approaches

**What you're seeking** (RSI thresholds adjusted by holding period) **has not been academically tested.** The literature divides into two separate camps:

1. **Momentum researchers:** Study formation/holding period optimization but ignore technical indicators like RSI [bauer.uh](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)
2. **Technical analysts:** Study RSI optimization but don't systematically vary thresholds by intended holding period [tradersunion](https://tradersunion.com/interesting-articles/rsi-indicator-strategies/settings-for-swing-trading/)

**The opportunity:** Your proposed framework (stricter RSI filters for shorter holds) represents **novel research territory** that bridges these two literatures.

***

### Backtesting Standards: What "Published Results" Actually Means

**Academic studies (highest rigor):**
- Disclose sample size, timeframe, statistical significance, out-of-sample testing [bauer.uh](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)
- **Example:** York study tested 468 months across 14 sectors = 6,552 observations [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**Practitioner backtests (lower rigor):**  
- Often report "win rates" (e.g., 91%) without disclosing number of trades, Sharpe ratio, or maximum drawdown [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
- May suffer from **optimization bias** (testing hundreds of filters to find best-performing) [reddit](https://www.reddit.com/r/algotrading/comments/17tij7t/how_to_backtest_common_strategy_filters_in_bulk/)
- Typically lack walk-forward validation [tradesearcher](https://tradesearcher.ai/strategies/2302-rsi-mean-reversion-strategy)

**Your analytical standard should demand:**  
1. Sample size (number of signals tested)  
2. Win rate + average gain/loss  
3. Sharpe ratio or return/risk ratio  
4. Maximum drawdown  
5. Out-of-sample validation period [quantinsti](https://www.quantinsti.com/articles/backtesting-trading/)

***

## Behavioral Finance Check

### Confirmation Bias Warning

Your initial question revealed **anchoring to the RSI paradigm**. The strongest academic evidence suggests:

- **For swing trading (1-4 weeks):** You should prioritize **9-12 month momentum formation** over RSI thresholds [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)
- **For day trading (1-5 days):** Extreme RSI thresholds (15/85) outperform moderate ranges [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)

This contradicts the assumption that shorter holding periods require moderate RSI ranges (40-65).

### Hindsight Bias in Backtesting

The practitioner community's "91% win rate" claims  likely suffer from: [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
- **Overfitting:** Testing hundreds of parameter combinations and reporting only the best [reddit](https://www.reddit.com/r/algotrading/comments/17tij7t/how_to_backtest_common_strategy_filters_in_bulk/)
- **Cherry-picked periods:** Not testing through 2008 crisis, 2020 crash, or 2022 bear market  
- **Survivorship bias:** Excluding delisted stocks or failed sectors

**The academic standard:** York University tested **1,296 combinations** transparently and reported that only strategies totaling 12-18 months were reliably profitable. [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

***

## Risk Assessment: Bear Case for RSI-Based Holding Period Systems

1. **No peer-reviewed validation:** Your proposed RSI threshold adjustments by holding period are untested [tradersunion](https://tradersunion.com/interesting-articles/rsi-indicator-strategies/settings-for-swing-trading/)

2. **Contradicts momentum research:** The "12-18 month rule" suggests long formation + short hold is optimal, which doesn't align with RSI mean reversion logic [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)

3. **Regime dependency:** RSI effectiveness varies dramatically by market volatility—the Canadian study found profitability ranked exactly opposite to volatility levels across sub-periods [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

4. **False precision:** Practitioner RSI "optimal settings" (e.g., period 14 vs. 15) lack statistical significance testing and may represent noise [mc2](https://www.mc2.fi/blog/best-rsi-settings-for-swing-trading/)

5. **Market structure changes:** The Jegadeesh-Titman 1993 study used data ending in 1989; momentum effects have **weakened as they became widely known** [bauer.uh](https://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)

***

## Actionable Recommendations

### If Building a Multi-Timeframe System

**Evidence-supported approach:**

**For 1-4 week swing trades:**
- **Primary filter:** 12-month momentum ranking (not RSI) [blog.thinknewfound](https://blog.thinknewfound.com/2018/07/momentums-magic-number/)
- **Entry timing:** RSI 14 pullback to 40-50 in uptrend (not oversold <30) [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-range-momentum-trading-strategy/)
- **Expected hold:** 3-6 months for maximum Sharpe ratio [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

**For 1-5 day swing trades:**  
- **Primary filter:** 9-month momentum + ADX >25 (strong trend confirmation) [mysitasi.mohe.gov](https://mysitasi.mohe.gov.my/journal-website/get-meta-article?artId=37f6b418-d79a-4d5d-a890-dcb2cf632e5c&formatted=true)
- **Entry timing:** 2-day RSI <15 or 5-day RSI <30 [quantifiedstrategies](https://www.quantifiedstrategies.com/rsi-trading-strategy/)
- **Exit:** RSI >75-80, not 70 (trends extend further) [articles.stockcharts](https://articles.stockcharts.com/article/articles-arthurhill-2016-07-testing-and-improving-the-5-day-rsi-mean-reversion-system-with-the-sector-spdrs/)

**For 1-6 month position trades:**  
- **Primary filter:** 12-month formation, skip month 12 and month 2 (reduces noise) [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426614003252)
- **Entry timing:** Pullback to 50-day MA (not RSI-based) [ainvest](https://www.ainvest.com/news/secret-formula-99-market-biggest-winners-mark-minervini-trend-template-decoded-2504/)
- **Expected performance:** 0.65-1.05% monthly if momentum confirmed [yorku](http://www.yorku.ca/mcao/cao_wei_momentum_CIR.pdf)

### Required Testing Before Live Implementation

Per institutional backtesting standards: [quantinsti](https://www.quantinsti.com/articles/backtesting-trading/)
- **Minimum 10 years of data** (15 years for position trading)  
- **Walk-forward optimization:** Train on 70% of data, test on remaining 30%  
- **Report all metrics:** Win rate, profit factor, Sharpe ratio, max drawdown, signal count  
- **Test across market regimes:** Bull market (2009-2021), bear market (2022), sideways (2015-2016)

***

## The Verdict

**Systems exist, but not the way you expected.** The published research validates **holding period optimization** through formation period adjustment (academic evidence) and **RSI period optimization** by trading style (practitioner evidence), but **no system combines both approaches** with disclosed backtest results.

Your hypothesis—stricter technical filters for shorter holds—is correct in principle but **inverted in application**: shorter holding periods require **longer momentum confirmation periods**, not tighter RSI ranges.]
```

**Key Findings:**
- [ ] Existing systems found
- [ ] Their threshold choices
- [ ] Performance data

---

### Q4: Minervini SEPA + RSI
**Perplexity Response:**
```
[## Executive Summary

**Minervini does NOT use RSI thresholds as a primary entry filter in SEPA methodology.** After examining comprehensive SEPA documentation, RSI is mentioned only once in passing as an optional "momentum confirmation" indicator, not as a systematic entry criterion. His framework prioritizes **Relative Strength ranking (>70, ideally 90+), moving average alignment, and price position relative to 52-week highs**—not RSI levels. The typical SEPA holding period is **weeks to months, occasionally 6-12 months for exceptional winners**. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

***

## The Critical Finding: RSI is Not Part of SEPA

### What Minervini Actually Uses

After reviewing detailed SEPA methodology documentation, **RSI does not appear in the Trend Template criteria** or systematic entry framework. The **eight-point Trend Template** that defines Stage 2 uptrends includes: [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

1. Price above 50-day, 150-day, and 200-day moving averages
2. 50-day MA above 150-day MA
3. 150-day MA above 200-day MA
4. 200-day MA trending upward for ≥1 month
5. **Price within 25% of 52-week high** (not RSI-based)
6. **Relative Strength rating >70** (ideally 90+) on 1-100 scale
7. Volume expansion on rallies, contraction on pullbacks
8. Above all moving averages with proper alignment

**Note:** "Relative Strength" in Minervini's system measures **price performance versus the market** (percentile ranking), not the RSI oscillator (14-day momentum). [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### The One RSI Mention in SEPA Literature

RSI appears only once in a generic description of entry timing: "Use momentum indicators like RSI, MACD, or stochastic, but don't rely on them blindly. What you're looking for is momentum divergence at extremes or momentum confirmation at key levels". [youtube](https://www.youtube.com/watch?v=QyGXt-4Hp3Q)

This is presented as **optional supplementary analysis**, not systematic criteria. The methodology continues: "For example, if price makes a lower low, but your RSI makes a higher low, that's [bullish divergence]". This describes discretionary pattern recognition, not threshold-based rules. [youtube](https://www.youtube.com/watch?v=QyGXt-4Hp3Q)

***

## Minervini's Approach to "Overbought" Stocks

### The Counterintuitive Reality

SEPA methodology **explicitly requires entering stocks that conventional analysis considers overbought**. The Trend Template mandates: [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

- **Within 25% of 52-week high** (criterion 7) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
- **Relative Strength >70** (top 30% of market performers) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
- **Above all moving averages** simultaneously [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

By these criteria, **SEPA stocks are systematically "overbought" by traditional RSI standards** when entering Stage 2 uptrends.

### Minervini's Rationale for Buying Strength

His direct quote on this approach: "Every time the stock pulls back just a little bit, it's met with buying because the institutions are looking at a much bigger picture and that stock has a very bright future". [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

The methodology rejects contrarian "buy low" thinking. As documented: "This counterintuitive approach challenges conventional investment wisdom—buying stocks making new highs rather than seeking bargains". [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### The Institutional Accumulation Signal

VCP patterns in Stage 2 stocks reveal **institutional buying during "overbought" conditions** through volume behavior: [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

- Volume **decreases** during each contraction (supply exhausting)
- Volume **expands** 40-50% above average on breakout (institutional demand)
- Follow-through volume remains elevated for 2-5 days post-breakout [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

Minervini's focus: "The difference between a breakout that pops out and comes back versus one that works is the difference between retail buying and institutional buying". [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

***

## Typical SEPA Holding Periods

### Documented Timeframes

The most specific guidance states: **"Weeks to months typically, occasionally extending to 6-12 months for exceptional winners"**. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-vs-william-o-neil-vs-warren-buffett-trading-style-comparison)

This positions SEPA as a **swing-to-position trading strategy**, not day trading or long-term investing. The comparison document explicitly states this distinguishes Minervini from Warren Buffett (multi-year holds) and day traders (intraday exits). [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-vs-william-o-neil-vs-warren-buffett-trading-style-comparison)

### What Determines Holding Period

**Catalysts, not RSI, determine hold duration**: [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

- **Weak catalysts:** Typical 20-30% gains over weeks
- **Strong catalysts:** 50-100%+ gains extending months
- **Exceptional setups with macro tailwinds:** 6-12 month holds

Minervini's guidance on winners: "When a stock breaks out from a VCP pattern with a genuine fundamental catalyst, the advance may extend for months rather than weeks. Trailing stops allow capturing these extended moves". [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### Exit Criteria: Not RSI-Based

Positions exit when: [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)

1. **7-8% stop-loss hit** (hard stop, non-negotiable) [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)
2. **Two Trend Template criteria fail** (e.g., price falls below 50-day MA and 150-day MA) [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)
3. **Market environment shifts bearish** (indices break below key moving averages) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
4. **Trailing stop violated** (as profits develop, stop trails under moving averages)

**RSI overbought readings are NOT exit triggers.** In fact, stocks remaining "overbought" while holding all Trend Template criteria are precisely the positions to hold. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

***

## Backtested Data on SEPA & RSI: The Evidence Gap

### No Published RSI-Filtered SEPA Studies

**Zero academic or practitioner studies backtest SEPA entries filtered by RSI thresholds.** The literature focuses on:

1. **VCP pattern recognition** (volatility contraction sequences) [trendspider](https://trendspider.com/learning-center/volatility-contraction-pattern-vcp/)
2. **Trend Template compliance** (moving average criteria) [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)
3. **Fundamental screens** (earnings growth >20%, margin expansion) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### What IS Backtested: The Academic Foundation

The SEPA documentation cites **momentum research supporting the methodology**: [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

- **Jegadeesh-Titman (1993):** Buying past winners generates 1% monthly returns over 3-12 month holds (cited earlier) [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)
- **Moskowitz-Grinblatt (1999):** Industry momentum generates 1.49% monthly risk-adjusted excess returns [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)
- **O'Neal (2000):** Mechanical relative strength selection outperforms discretionary methods [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)
- **Wang et al. (2017):** Confirmed momentum strategy profitability persists in modern markets using sector ETFs [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

**Critical point:** These studies validate **Relative Strength ranking** (Minervini's RS >70 criterion), not RSI oscillator analysis. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

### Minervini's Track Record

The documented performance: [x](https://x.com/markminervini/status/1929588320025133411)

- **220% average annual return** over 5.5 years using SEPA (total return: 33,500%)
- **334.8% annual return** in 2021 U.S. Investing Championship (verified, $1M+ category)
- **155% return** in 1997 U.S. Investing Championship

However, these results **do not isolate RSI's contribution** because RSI is not systematically used in the methodology. [x](https://x.com/markminervini/status/1929588320025133411)

***

## Why Minervini Doesn't Use RSI Thresholds

### The Philosophical Difference

SEPA focuses on **Stage identification** (trend structure) rather than **oscillator extremes** (mean reversion signals). [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

**RSI logic:** Overbought (>70) predicts pullbacks; oversold (<30) predicts bounces  
**Minervini logic:** Stage 2 uptrends sustain "overbought" readings for months; enter strength, not weakness

His quote on market environment: "When the market's in a correction, I go to cash. I don't fight it. I wait for the environment to improve". This reflects **regime-based thinking** (Stage 1-4 framework) incompatible with fixed RSI thresholds. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### The Moving Average Framework

Instead of RSI for timing, Minervini uses **moving average relationships**: [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

**Entry timing:**  
- Wait for VCP pattern completion (3-4 contractions with diminishing volatility)
- Enter on **volume-confirmed breakout** through pivot point (40-50% above average volume) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

**Pullback entries:**  
- Enter when price pulls back to **10-day or 20-day MA** in established Stage 2 uptrend [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)
- This provides "better risk/reward than chasing extended breakouts while maintaining trend confirmation" [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

**Exit signals:**  
- One Trend Template criterion fails: "alarm signal" (increased vigilance)
- Two criteria fail: "strong indication to close" [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

This creates a **moving average-based system** that adapts to volatility, whereas fixed RSI thresholds do not. [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

***

## Behavioral Finance Check

### Confirmation Bias Warning

Your question assumes **RSI is central to SEPA methodology when it demonstrably is not**. This represents potential **anchoring bias** to RSI-based thinking from other systems. [youtube](https://www.youtube.com/watch?v=QyGXt-4Hp3Q)

The evidence reveals:
- **You sought RSI thresholds by holding period** → Minervini uses moving averages, not RSI
- **You asked about entering RSI >70 stocks** → SEPA requires entering stocks >90 Relative Strength (different metric)
- **You wanted RSI-filtered backtest data** → The academic foundation validates Relative Strength ranking, not RSI oscillators

### The "Buy High, Sell Higher" Paradigm Shift

Minervini's documented statement: "Diversification is definitely not going to protect you. It's just going to dilute you". This extends to his rejection of mean reversion (buying oversold) in favor of momentum continuation (buying strength). [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

**Loss aversion implication:** Traders conditioned to "buy low" experience psychological discomfort entering stocks at/near 52-week highs. The data shows this discomfort is **counterproductive** in Stage 2 uptrends. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

The documented teaching: "Rather than diversifying across 20-30 positions, the methodology concentrates capital in 4-8 highest-conviction setups meeting all SEPA criteria". This requires overcoming **familiarity bias** toward diversification as risk management. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

***

## Risk Assessment: What SEPA Actually Requires

### The 7-8% Stop-Loss Rule

Minervini's non-negotiable risk parameter: **"Line in the sand at 8%"**. This is the **maximum acceptable loss**, typically implemented at 7-8% below entry. [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)

**His pivotal discovery:** "I went from having a 15% loss normalized to a 10% stop and my account would have been up 72% instead of being down". Tighter stops dramatically improved performance despite more frequent small losses. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

The math: Even **10 consecutive 7% losses = 70% of risk capital**, preserving the account for large winning trades. This is why the methodology rejects wider stops. [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)

### Position Sizing Formula

**Systematic calculation** working backward from risk tolerance: [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

\[
\text{Position Size} = \frac{\text{Account Size} \times \text{Risk \%}}{\text{Entry Price} - \text{Stop Price}}
\]

**Example:** $100,000 account, 1% risk ($1,000), entry at $50, stop at $46 (8% stop):

\[
\text{Position Size} = \frac{\$1,000}{\$50 - \$46} = \frac{\$1,000}{\$4} = 250 \text{ shares}
\]

This ensures **constant dollar risk** regardless of stock price or volatility. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### Market Environment Override

**Critical limitation:** "Even perfect SEPA setups fail during bearish markets. Statistical research shows 90.77% of successful breakouts occur when indices trade above monthly 10-period EMAs". [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

During corrections: "I go to cash. I don't fight it". This **regime-based approach** supersedes all stock-level analysis, including any RSI readings. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

***

## Direct Answers to Your Questions

### 1. Does Minervini recommend different RSI thresholds for different holding periods?

**No.** RSI thresholds do not appear in systematic SEPA methodology. Minervini uses **Relative Strength ranking (>70), not RSI oscillator**, as a Stage 2 filter. Holding periods are determined by **catalyst strength and trailing stop violations**, not pre-planned timeframes. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-vs-william-o-neil-vs-warren-buffett-trading-style-comparison)

### 2. What does his research show about entering overbought stocks (RSI >70) in Stage 2 uptrends?

Minervini's system **requires entering stocks that are technically "overbought"** by conventional standards:
- Within 25% of 52-week high [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
- Relative Strength >70 (ideally 90+) [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
- Above all moving averages simultaneously [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

His view: "Every time the stock pulls back just a little bit, it's met with buying" in Stage 2 stocks with strong fundamentals. **Traditional "overbought" readings are continuation signals, not reversal warnings** in SEPA. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

### 3. Is there backtested data on SEPA entries filtered by RSI level?

**No.** Zero published studies backtest SEPA with RSI filters. The academic foundation for SEPA validates **momentum persistence and Relative Strength ranking** (Jegadeesh-Titman, Moskowitz-Grinblatt, O'Neal), not RSI oscillator thresholds. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-s-sepa-methodology-complete-framework-explained)

### 4. What is the typical holding period for SEPA trades, and does RSI affect expected returns?

**Typical holding period: weeks to months, occasionally 6-12 months for exceptional winners**. [finermarketpoints](https://www.finermarketpoints.com/post/mark-minervini-vs-william-o-neil-vs-warren-buffett-trading-style-comparison)

**RSI does not affect expected returns** in SEPA because it's not a systematic component. Returns depend on: [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)
- **Catalyst strength** (product launches, FDA approvals extend holds to months)
- **Market environment** (bull markets extend holds; corrections trigger cash exit)
- **Trend Template compliance** (exit when 2+ criteria fail, not RSI levels)

***

## The Verdict

Your questions assumed RSI centrality to Minervini's SEPA methodology. **The evidence reveals this assumption is incorrect.** SEPA systematically uses:

1. **Relative Strength ranking** (market percentile, not 14-day momentum oscillator)
2. **Moving average alignment** (50/150/200-day relationships, not RSI)
3. **VCP volume patterns** (institutional accumulation signals, not oscillator extremes)
4. **Fundamental screens** (earnings growth >20%, margin expansion)
5. **Catalyst assessment** (product launches, regulatory approvals)

The methodology **explicitly enters stocks at/near 52-week highs with superior Relative Strength**—positions that traditional RSI analysis would label "dangerously overbought". This is **by design, not oversight**. [finermarketpoints](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide)

If you're building a swing trade analyzer using RSI thresholds by holding period, you're implementing a **fundamentally different philosophy** than Minervini's championship-winning SEPA methodology.]
```

**Key Findings:**
- [ ] Minervini's actual RSI guidance
- [ ] SEPA holding period data
- [ ] RSI impact on SEPA returns

---

### Q5: Practical Trader Experience
**Perplexity Response:**
```
[## Executive Summary

Practitioner experience reveals a **critical divide**: unsuccessful traders mechanically sell RSI >70 ("textbook rule"), while successful swing traders interpret RSI **contextually by market regime**. A documented case study shows that blindly exiting at RSI >70 in uptrends produced an **82.9% loss rate** (29 out of 35 losing trades), with missed rallies averaging 8.4% over the following two weeks. The consensus among profitable traders: **RSI >70 means different things in trending versus ranging markets**. [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)

***

## RSI Entry Levels Used by Successful Swing Traders

### The Regime-Based Framework

Profitable practitioners report using **different RSI interpretations by market structure**, not fixed thresholds: [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**In ranging/sideways markets:**
- **Avoid RSI >70** for long entries (mean reversion expected)
- **Buy near RSI 30** for oversold bounces
- **Standard thresholds:** 70/30 work in ranges [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**In trending markets:**
- **RSI >70 = momentum confirmation**, not exit signal [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)
- **Enter pullbacks to RSI 40-50** in established uptrends (not <30) [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- **Avoid shorting RSI >70** in strong uptrends [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)

### Documented Trader Strategies

**Strategy 1: Weekly/Daily Multi-Timeframe Approach** [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)

A Reddit trader with documented profitability reports:

- **Weekly chart:** Use RSI slope for trend direction
  - Upward slope + RSI approaching 30 = long opportunity
  - Downward slope + RSI near 70 = short opportunity
- **Entry rules:**
  - "Never buy when weekly RSI at 70 or above"
  - "Never sell when weekly RSI at 30 or below"
- **Daily chart:** Wait for RSI reversal signals (divergences, double bottoms/tops)
- **Key quote:** "I prefer going long when the weekly RSI approaches oversold conditions... [and] look for price action that clears out liquidity from old swing points" [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)

**Strategy 2: Extreme RSI Thresholds (Mean Reversion)** [reddit](https://www.reddit.com/r/CapitalistExploits/comments/1d590ut/rsi_trading_strategy_70_win_rate/)

Multiple practitioners report better performance with **more extreme thresholds**:

- **3-period RSI <20** for entries (not <30) [reddit](https://www.reddit.com/r/CapitalistExploits/comments/1d590ut/rsi_trading_strategy_70_win_rate/)
- **Exit at RSI >60** (not 70) [reddit](https://www.reddit.com/r/CapitalistExploits/comments/1d590ut/rsi_trading_strategy_70_win_rate/)
- **Backtest results:** 69.76% win rate, $2.33 profit factor, average 5-day hold [reddit](https://www.reddit.com/r/CapitalistExploits/comments/1d590ut/rsi_trading_strategy_70_win_rate/)

A trader testing 5,000+ trades found standard 70/30 thresholds **failed catastrophically**: [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)
- **Win rate: 42%** with RSI <30 buy / >70 sell
- **Profit factor: 0.8** (losing strategy)
- **Max drawdown: 40%**

Community feedback: "The 30/70 ratio is certainly a significant issue. Personally, I find that using a 10/90 mix works quite effectively". Another: "I suggest backtesting 80/20, 85/15, and 90/10". [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

**Strategy 3: RSI as Filter, Not Trigger** [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)

Experienced traders emphasize: "Relying on RSI and MACD in a standard manner may not yield effective results unless you are specifically trading divergences". [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)

The professional approach: "RSI is a filter, not a trigger—always require structural confirmation". This means using RSI to identify regime, then entering on **price action** (breakouts, volume surges, moving average bounces). [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

***

## Consensus on Avoiding RSI >X for Short-Term Trades

### The Documented Failure Pattern

**Case Study: "Sarah's $11,400 Disaster"** [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

The most detailed practitioner case study documents a 28-year-old trader who lost 40.7% of her account following textbook RSI rules:

**Strategy:** "RSI >70 = overbought, sell"  
**Results over 10 weeks:**
- **55 trades, 36.4% win rate**
- **29 out of 35 losses (82.9%)** came from selling RSI >70 stocks that continued rallying
- **Average rally after exit:** 8.4% over the next 2 weeks
- **Total opportunity cost:** $31,800 in missed gains [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**Worst trade:** Sold NVIDIA at RSI 75.8; stock rallied 4.6% **the same day** with RSI staying above 75 all day. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**Post-recovery:** After adopting regime-based RSI interpretation, her win rate jumped from 36.4% to **66.7%** over 4 months. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### What Professional Traders Actually Do

**Institutional behavior documented**: [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

- **Institutional algorithms BUY at RSI >70** in established uptrends (momentum confirmation)
- **Retail traders SELL at RSI >70** (following textbook rules), providing liquidity to institutions
- **Quote:** "When retail sells 'overbought' RSI in trends, institutional algos are programmed to BUY their selling" [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**Why institutions buy "overbought" stocks:**
- Momentum confirmation (strong trend in progress)
- Liquidity harvesting (retail shorting creates entry opportunities)
- Multi-factor stacking (RSI >70 + volume surge + trend filter = high-conviction entries) [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### The Asymmetry in Practice

**For swing trades (1-4 weeks):**

| Market Condition | RSI >70 Interpretation | Practitioner Action |
|------------------|------------------------|---------------------|
| **Strong uptrend** (above 50/200 MA) | Momentum confirmation | Hold or add on pullbacks to RSI 40-50  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |
| **Ranging market** (choppy, ADX <20) | Overbought, reversal risk | Avoid new longs; consider exits  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |
| **Weak uptrend** (near resistance, low volume) | Exhaustion warning | Wait for confirmation via volume/divergence  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |

**StockCharts practitioner guidance:** "Think 'overbought' means it's time to bail? Not always. Sometimes that 70+ RSI reading doesn't signal weakness, but strength". Their recommendation: Use **trend filters** (200-day SMA) first, then RSI crossing >70 as a **momentum confirmation to buy**, not sell. [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)

***

## Trading Platform RSI Recommendations

### ThinkOrSwim (TD Ameritrade)

**Default settings**: [toslc.thinkorswim](https://toslc.thinkorswim.com/center/reference/Tech-Indicators/studies-library/R-S/RSI)
- **RSI period:** 14
- **Overbought:** 70
- **Oversold:** 30
- **Customization:** Users can adjust thresholds in settings; platform allows enabling "show breakout signals" to highlight RSI crosses [youtube](https://www.youtube.com/watch?v=CWMCByVOP9g)

**Practitioner customization:** Trading educator Scott Reese uses **default 70/30 thresholds** but emphasizes: "I personally just use all of the default settings... if you just wanted to be more strict or less strict with those two criteria then you can change these two numbers". [youtube](https://www.youtube.com/watch?v=CWMCByVOP9g)

### TradingView

**Platform defaults**: [trendspider](https://trendspider.com/blog/how-to-trade-the-rsi-relative-strength-index-indicator/)
- **Standard RSI:** 14-period, 70/30 thresholds
- **For trending markets:** RSI ranges 40-80 in uptrends (not 30-70) [trendspider](https://trendspider.com/blog/how-to-trade-the-rsi-relative-strength-index-indicator/)
- **For bear markets:** RSI ranges 10-60 with 50 as resistance [trendspider](https://trendspider.com/blog/how-to-trade-the-rsi-relative-strength-index-indicator/)

**Custom indicators:** Minervini Stage 2 indicators on TradingView do **not include RSI thresholds**—they use moving average alignment and Relative Strength ranking instead. [tradingview](https://www.tradingview.com/script/hpGKYuWi-Minervini-Stage-2-Analysis/)

### Admiral Markets / OANDA

**Recommended timeframe-specific settings**: [admiralmarkets](https://admiralmarkets.com/education/articles/forex-indicators/relative-strength-index-how-to-trade-with-an-rsi-indicator)

| Timeframe | RSI Period | Thresholds | Strategy Type |
|-----------|-----------|------------|---------------|
| 1-5 minute | 6 | 80/20 | Scalping |
| 5-15 minute | 9 | 75/25 | Momentum day trading |
| 15-60 minute | 14 | 70/30 | Intraday swing trading |
| Daily | 14-25 | 70/30 or 60/40 | Multi-day swing trading |

**Practitioner note:** "Shorter RSI periods like RSI 9 or 10 respond faster to intraday momentum changes but also provide more false signals. Higher RSI periods like RSI 14 or 16 smooth out more data points". [admiralmarkets](https://admiralmarkets.com/education/articles/forex-indicators/relative-strength-index-how-to-trade-with-an-rsi-indicator)

### AXIORY

**Timeframe recommendations**: [axiory](https://www.axiory.com/en/trading-resources/technical-indicators/rsi-indicator-settings)
- **Smaller timeframes:** 9-period RSI with moving averages for trend filtering
- **Higher timeframes:** 14-period RSI to reduce false signals and market noise

**Critical guidance:** "For higher timeframes, it is better to use 14-period RSI and ensure fewer false signals". [axiory](https://www.axiory.com/en/trading-resources/technical-indicators/rsi-indicator-settings)

***

## Failure Rates for Entering RSI >70 in Swing Trades

### Quantified Failure Data

**Case Study: 82.9% Loss Rate** [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

The documented Sarah Kim case provides the most specific failure rate:

- **Strategy:** Sell/exit when RSI >70 in swing trades
- **Regime:** Mixed market (some trends, some ranges) during Jan-Mar 2024
- **Result:** **29 out of 35 losing trades (82.9%)** came from this approach
- **Context:** These were exits in uptrending stocks where RSI >70 signaled strength, not weakness [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### Backtest Performance: Standard 70/30 Threshold

**5,000+ Trade Backtest** [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

A practitioner tested the traditional strategy across thousands of trades:

**Rules:**
- Buy RSI <30
- Sell RSI >70
- 2 ATR stops and targets

**Results:**
- **Win rate: 42%** (losing majority)
- **Profit factor: 0.8** (lost $0.20 per dollar risked)
- **Max drawdown: 40%**
- **Conclusion:** "It failed hard" [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

**Community recommendations after this test:**
- "Test 80/20, 85/15, and 90/10" for better results [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)
- "The 10/90 mix works quite effectively for me" [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

### Contrarian Success: Buying RSI >70 in Trends

**StockCharts Manual Backtest Approach** [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)

Practitioner recommendation for **buying strength**:

**Filter 1:** Price above 200-day SMA (trend confirmation)  
**Filter 2:** RSI crosses **above 70** (momentum confirmation)  
**Entry:** On new highs or resistance breakout

**Interpretation:** "RSI >70 in uptrends = buy signal". This inverts the traditional approach. [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)

**Supporting data:** The documented institutional behavior shows algos programmed to **add positions** at RSI >70 in trends. This explains why retail traders shorting/exiting overbought conditions lose money—they're trading against institutional momentum. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### Context-Dependent Failure Rates

**Synthesis of practitioner experience:**

| Market Context | Entry at RSI >70 | Estimated Failure Rate | Source |
|----------------|------------------|------------------------|---------|
| **Strong uptrend** (above MAs, high volume) | Long entry | ~30-40% (works more than fails) |  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |
| **Ranging market** (choppy, no trend) | Long entry | ~58-70% (fails majority) |  [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/) |
| **Weak trend** (near resistance, declining volume) | Long entry | ~50-60% (coin flip) |  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |
| **Any market** | Short entry based on "overbought" | **82.9%** documented failure |  [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html) |

**Key insight:** The failure rate isn't determined by RSI level alone—it's determined by **regime + RSI combination**. RSI >70 in strong trends has a **lower failure rate** than RSI <30 in weak trends. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

***

## Real-World Practitioner Consensus

### What Successful Traders Agree On

**1. Regime identification is mandatory** [reddit](https://www.reddit.com/r/Trading/comments/1lz57s9/which_indicators_do_the_largest_traders_use/)

- Use ADX, moving averages, or volume to identify trending vs. ranging markets FIRST
- Then interpret RSI based on context
- **Quote:** "Regime determines interpretation (trending vs. ranging)" [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**2. Standard 70/30 thresholds are suboptimal** [reddit](https://www.reddit.com/r/Trading/comments/1lz57s9/which_indicators_do_the_largest_traders_use/)

- Multiple backtests show poor performance with default settings
- More extreme thresholds (80/20, 85/15, 10/90) outperform in mean reversion strategies
- **Community consensus:** "The standard 70/30 setup doesn't perform well at all" [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

**3. RSI alone is insufficient** [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)

- Require volume confirmation (institutional vs. retail buying)
- Require price action confirmation (breakouts, support bounces)
- Require multi-timeframe alignment (weekly + daily agreement)
- **Quote:** "Relying on RSI in a standard manner may not yield effective results unless trading divergences" [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)

**4. Avoid mechanical rules** [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)

- The "$11,400 disaster" case demonstrates the cost of following textbook rules blindly
- Successful traders adjust interpretation by market phase
- **Recovery lesson:** After switching from mechanical "sell at 70" to regime-based interpretation, win rate improved from 36.4% to 66.7% [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### What Losing Traders Do

**Common failure patterns identified**: [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)

1. **Fade RSI >70 in uptrends** (82.9% of losses in documented case)
2. **Use standard 70/30 without backtesting** (42% win rate, 0.8 profit factor)
3. **Ignore market regime** (trade RSI signals in all conditions)
4. **Trade RSI alone without confirmation** (high false positive rate)
5. **Exit winners too early** (missing 8.4% average follow-through rallies)

***

## Behavioral Finance Check

### Loss Aversion & Anchoring

Your question assumes avoiding RSI >70 reduces risk. The practitioner data suggests the **opposite in trending markets**:

- Avoiding RSI >70 longs = missing momentum (Sarah missed $31,800 in rallies) [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- Shorting RSI >70 = trading against institutions (82.9% loss rate) [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

This represents **loss aversion bias**: fearing the pain of buying "overbought" stocks more than the pain of missing strong trends.

### Confirmation Bias Warning

The traditional "RSI >70 = dangerous" belief persists despite **documented failure rates**. Practitioners who challenge this assumption (buying RSI >70 in trends) report better performance. [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)

**The cognitive dissonance:** Textbook training says "sell overbought," but profitable traders buy it. This explains why 90% of retail traders lose money—they follow rules that work in theory but fail in practice. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

***

## Risk Assessment: What Practitioners Learned the Hard Way

### The $11,400 Lesson

**What failed**: [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- Mechanical "sell at RSI 70" rule
- Ignoring trend context
- Treating all RSI >70 readings as bearish

**What worked**: [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- Identify regime first (trending vs. ranging)
- In uptrends: RSI >70 = strength (hold or add on pullbacks to 40-50)
- In ranges: RSI >70 = reversal risk (reduce or exit)
- Require multi-indicator confirmation (volume, price action, divergences)

### Position Sizing Implication

Practitioners emphasize **risk management supersedes RSI levels**: [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)

- Use **ATR-based stops** (not RSI-based exits) [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)
- **Maximum 7-8% stop-loss** regardless of RSI reading [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)
- **Position size** to risk 1-2% of account per trade [quantstrategy](https://quantstrategy.io/blog/sepa-strategy-explained-mastering-trend-following-with-mark/)

**Quote:** "You can determine your stop loss and take profit levels by utilizing the Average True Range (ATR)... Employing RSI in a conventional way may lead to significant losses". [reddit](https://www.reddit.com/r/Daytrading/comments/1miemlm/how_do_you_set_your_entry_position_in_swing/)

***

## Direct Answers to Your Questions

### 1. What RSI levels do successful swing traders actually use for entries?

**Regime-dependent approach**: [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)
- **Ranging markets:** Enter near RSI 30 (oversold), avoid >70
- **Uptrends:** Enter pullbacks to RSI 40-50 (not <30); RSI >70 = momentum confirmation to hold/add
- **Extreme thresholds:** 3-period RSI <20 / exit >60 (69.76% win rate) [reddit](https://www.reddit.com/r/CapitalistExploits/comments/1d590ut/rsi_trading_strategy_70_win_rate/)
- **Multi-timeframe:** Weekly RSI slope for direction, daily RSI for entry timing [reddit](https://www.reddit.com/r/Daytrading/comments/18q2a6b/unlocking_success_dive_into_my_proven/)

### 2. Is there consensus on avoiding RSI >X for short-term trades?

**No universal consensus—it depends on market regime:**
- **Avoid RSI >70 longs:** Only in ranging/choppy markets [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- **Embrace RSI >70:** In strong uptrends with volume confirmation [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)
- **Community split:** Unsuccessful traders mechanically avoid >70; profitable traders interpret contextually [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)
- **Documented failure:** Avoiding RSI >70 in uptrends = 82.9% loss rate on those trades [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

### 3. Do platforms provide timeframe-specific RSI recommendations?

**Yes, multiple platforms offer guidance:**

| Platform | Timeframe | RSI Period | Thresholds | Style |
|----------|-----------|-----------|------------|-------|
| Admiral Markets | 1-5 min | 6 | 80/20 | Scalping  [admiralmarkets](https://admiralmarkets.com/education/articles/forex-indicators/relative-strength-index-how-to-trade-with-an-rsi-indicator) |
| Admiral Markets | 5-15 min | 9 | 75/25 | Day trading  [admiralmarkets](https://admiralmarkets.com/education/articles/forex-indicators/relative-strength-index-how-to-trade-with-an-rsi-indicator) |
| Admiral Markets | 15-60 min | 14 | 70/30 | Swing trading  [admiralmarkets](https://admiralmarkets.com/education/articles/forex-indicators/relative-strength-index-how-to-trade-with-an-rsi-indicator) |
| AXIORY | Daily+ | 14 | 70/30 | Position trading  [axiory](https://www.axiory.com/en/trading-resources/technical-indicators/rsi-indicator-settings) |
| ThinkOrSwim | All | 14 (default) | 70/30 (adjustable) | Customizable  [toslc.thinkorswim](https://toslc.thinkorswim.com/center/reference/Tech-Indicators/studies-library/R-S/RSI) |

**However:** Practitioners report **default settings underperform** custom optimizations. [reddit](https://www.reddit.com/r/Trading/comments/1lz57s9/which_indicators_do_the_largest_traders_use/)

### 4. What's the typical failure rate for entering stocks with RSI >70 in swing trades?

**Context-dependent failure rates:**

- **In strong uptrends:** ~30-40% failure (works more than fails) [articles.stockcharts](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/)
- **In ranging markets:** ~58-70% failure (standard 70/30 strategy had 42% win rate) [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)
- **Shorting RSI >70 indiscriminately:** **82.9% documented failure rate** [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
- **Buying RSI >70 without trend confirmation:** ~50-60% failure [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

**The critical variable:** Market regime determines success/failure more than RSI level alone. [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

***

## The Verdict

Practitioner experience demolishes the textbook rule "avoid RSI >70." The documented evidence shows:

1. **Mechanically exiting RSI >70 = 82.9% loss rate** on those specific trades in mixed markets [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
2. **Standard 70/30 strategy = 42% win rate, 0.8 profit factor** across 5,000+ trades [reddit](https://www.reddit.com/r/Daytrading/comments/1pdj9f1/i_tested_that_rsi_oversold_strategy_on_5000/)
3. **Regime-based interpretation = 66.7% win rate** (same trader, different approach) [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)
4. **Institutional algos buy RSI >70 in trends** while retail sells, creating the failure asymmetry [education.signalpilot](https://education.signalpilot.io/curriculum/beginner/05-rsi-extremes.html)

Your original question sought consensus on avoiding RSI >70 for short-term trades. **The real-world consensus is the opposite**: profitable swing traders embrace RSI >70 in uptrends and only avoid it in confirmed ranging markets.]
```

**Key Findings:**
- [ ] Consensus thresholds from practitioners
- [ ] Common failure modes
- [ ] Platform recommendations

---

## Synthesis & Recommendations

### Validated Thresholds (from research)
| Holding Period | Overbought | Oversold | Source |
|----------------|------------|----------|--------|
| 5-10 days | ? | ? | TBD |
| 15-30 days | ? | ? | TBD |
| 1-3 months | ? | ? | TBD |

### Recommendations
1. [ ] Update HOLDING_PERIOD_SELECTOR_PLAN.md with validated thresholds
2. [ ] Design backtest if research is inconclusive
3. [ ] Document sources for future reference

---

## Backtest Design (If Research Inconclusive)

If Perplexity doesn't provide clear evidence, we'll design our own backtest:

```python
# Pseudo-code for RSI threshold backtest
def backtest_rsi_thresholds():
    """
    For each holding period (5-10d, 15-30d, 1-3mo):
    1. Find entries at various RSI levels (50, 55, 60, 65, 70, 75, 80)
    2. Measure returns after holding period
    3. Calculate win rate and average R-multiple
    4. Identify optimal RSI threshold for each period
    """

    thresholds_to_test = [50, 55, 60, 65, 70, 75, 80]
    holding_periods = [7, 21, 63]  # trading days

    for period in holding_periods:
        for threshold in thresholds_to_test:
            # Find all entries where RSI < threshold
            # Measure outcome after 'period' days
            # Record win rate, avg return, max drawdown
            pass

    # Output: Optimal threshold for each period
```

**Backtest Parameters:**
- Universe: S&P 500 or Russell 1000
- Timeframe: 5 years (2020-2025)
- Entry criteria: Stock in Stage 2 uptrend + RSI < threshold
- Exit: Fixed holding period OR stop loss hit
- Metrics: Win rate, Avg R, Max drawdown, Expectancy

---

*This research must be completed BEFORE implementing v4.13*
