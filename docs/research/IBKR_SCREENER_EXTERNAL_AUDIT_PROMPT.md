# IBKR Screener Parameters — External Validation Prompt

> Paste this entire document into Perplexity / Grok / ChatGPT / Gemini and ask for feedback.
> Goal: validate that the 10 filter parameters are well-calibrated for a Minervini-style swing trading system.

---

## Context: What We Are Building

I run a swing trading system called STA (Swing Trade Analyzer) built on Mark Minervini's SEPA methodology. It has been backtested on 60 tickers over 5 years (2021–2026) and produces:
- Config C: 53.78% win rate, Profit Factor 1.61, Sharpe 0.85, p=0.002 (statistically significant)
- Walk-forward validated (out-of-sample outperforms in-sample — not overfitted)

The system uses:
- Minervini's 8-point Trend Template (price above 200/150/50/20 EMA, EMA slope, 52W range)
- RS52W > 1.2 (stock outperforming SPY over 52 weeks)
- Fundamental quality: ROE > 15%, revenue growth > 10%, D/E < 1.0
- Risk gate: VIX < 25, SPY above 200 SMA
- Holding period: 15–30 days (standard swing)

## The Problem

STA does deep per-ticker analysis but requires tickers to be fed in manually. The US market has 7,000+ stocks. I need a pre-screening step that narrows this to 30–80 high-quality candidates before STA runs its deep analysis.

## The Solution: IBKR 2.0 Market Screener

Interactive Brokers' Market Screener has real-time data and the following factors not available in my STA system:
- EarnGrw% (earnings growth %, not just revenue)
- Inst. Percent Held (institutional ownership %)
- Quick Ratio (short-term liquidity)
- MACD Histogram (real-time momentum confirmation)
- Average Option Volume (options market activity)
- 52 Week IV Rank (implied volatility percentile)

IBKR's MultiSort allows 10 filter+sort parameters simultaneously.

---

## The 10 Proposed IBKR Filters

These are designed to pre-select stocks that STA is likely to give a BUY verdict, using data IBKR has in real-time that STA cannot access at market-wide scale.

### Tier 1 — Structure (6 filters)
| # | Factor | FROM | TO | Sort Preference | Rationale |
|---|--------|------|----|-----------------|-----------|
| 1 | Market Cap | 1.00 B | max | No Preference | Avoid micro-caps: institutional coverage, reliable data, STA stops work properly |
| 2 | Average Volume ($) | 5.00 M | max | Higher Values | Minimum daily dollar liquidity for institutional-grade entries/exits |
| 3 | Price/EMA(200) | 1.05 | 2.00 | Higher Values | Minervini TT#1: above 200 EMA. 1.05 buffer ensures EMA is rising. 2.00 cap avoids parabolic/extended entries |
| 4 | Price/EMA(50) | 1.00 | 1.30 | Higher Values | Minervini TT#4: above 50 EMA (implies 50>200 EMA if combined with #3). 1.30 cap avoids overextended |
| 5 | ROE | 15 | 100 | Higher Values | Capital efficiency floor. >100% is usually financial engineering (buybacks distorting equity base) |
| 6 | EarnGrw% | 10 | 150 | Higher Values | Earnings acceleration drives institutional accumulation. >150% likely non-recurring (comp distortion) |

### Tier 2 — Quality (2 filters)
| # | Factor | FROM | TO | Sort Preference | Rationale |
|---|--------|------|----|-----------------|-----------|
| 7 | Inst. Percent Held | 25 | 95 | Higher Values | Minervini's explicit sponsorship requirement. <25% = no institutional accumulation phase |
| 8 | Quick Ratio | 1.00 | max | No Preference | Liquidity health: covers current liabilities with liquid assets. D/E alone misses short-term cash risk |

### Tier 3 — Real-Time Momentum (2 filters)
| # | Factor | FROM | TO | Sort Preference | Rationale |
|---|--------|------|----|-----------------|-----------|
| 9 | MACD Histogram | 0 | max | Higher Values | MACD histogram > 0 = momentum accelerating above signal line right now. Confirms Stage 2 active today |
| 10 | Change % | -2 | 8 | Higher Values | -2 floor = falling knife prevention. 8 cap = avoids news-driven parabolic spikes |

### MultiSort Priority Order
Survivors are ranked in this order:
1. Price/EMA(50) — Higher (best RS proxy available in IBKR)
2. EarnGrw% — Higher (earnings acceleration magnitude)
3. Inst. Percent Held — Higher (accumulation phase conviction)
4. Average Volume ($) — Higher (institutional footprint)

---

## What Was Deliberately Excluded and Why

| Factor | Why Excluded |
|--------|-------------|
| Price/EMA(20) > 1.0 | Weakest of 3 EMA filters — STA validates this. Dropped to stay within 10-item limit |
| Last > $10 | Redundant — Market Cap > $1B already ensures meaningful price |
| Analyst Target/Price Disparity % > 10% | Lagging signal — analysts update monthly. Real-time momentum filters are more reliable |
| Average Option Volume > 100 | Shown as display column for OptionsIQ flagging, not needed as a filter |

---

## Questions for External Review

1. **Threshold calibration** — Are the FROM/TO ranges well-calibrated for Minervini-style swing trades? Specifically:
   - Is ROE > 15% the right floor, or should it be higher/lower?
   - Is EarnGrw% > 10% too low (lets in slow-growth stocks) or too high (misses early-acceleration)?
   - Is Inst. Percent Held > 25% appropriate, or does Minervini use a different threshold?
   - Is Price/EMA(200) cap at 2.00 appropriate, or should it be tighter (1.50) to avoid extended stocks?
   - Is Price/EMA(50) cap at 1.30 appropriate for swing entries?

2. **Missing filters** — Given that we only have 10 slots and the IBKR factor list includes: Dividends, EarnGrw%, Insider Percent Owned, Payout Ratio%, Quick Ratio, ROE, 52 Week High/Low, Average Option Volume, Opt. IV%, 52 Week IV Rank, Put/Call Volume, Average Price Target, Average Rating, Analyst Target/Price Disparity%, Social Sentiment Score, Fee Rate, Utilization, Change%, Market Cap, Average Volume ($), EMA(20/50/100/200), MACD, MACD Histogram, Price/EMA ratios — **are we missing a critical factor that would significantly improve candidate quality?**

3. **Filter order / redundancy** — Is any filter redundant given the others? For example:
   - Does MACD Histogram > 0 add signal beyond Price/EMA(50) > 1.0?
   - Does Quick Ratio > 1.0 add signal beyond ROE > 15%?

4. **Survivor count** — In a typical bull market, how many US stocks (from 7,000+) would you expect to survive these 10 filters simultaneously? Is 30–80 a reasonable estimate?

5. **Upper bounds** — I added upper bounds (2.00 on Price/EMA(200), 1.30 on Price/EMA(50), 150% on EarnGrw%, 100 on ROE) to avoid parabolic/extended setups. Are these caps correct, or do they risk cutting the best momentum stocks?

6. **Sort priority** — Is ranking by Price/EMA(50) → EarnGrw% → Inst. Percent Held → Average Volume ($) the right priority order? What would you change?

7. **What Minervini actually uses** — Mark Minervini's SEPA methodology is our foundation. From your knowledge of his published work (Trade Like a Stock Market Wizard, Think & Trade Like a Champion), what pre-screening criteria does he recommend that we may have missed?

---

## Expected Output from STA After IBKR Pre-Screen

After IBKR produces ~30–80 survivors, each is run through STA which adds:
- Full 8-point Trend Template score (0–8)
- RS52W vs SPY (exact ratio, not EMA proxy)
- RSI (14) — looking for 30–70 range at entry
- Support/Resistance levels + touch counts
- Pattern detection (VCP, Cup & Handle, Flat Base)
- Trade setup: entry, stop, target, R:R ratio
- Verdict: BUY / HOLD / AVOID
- Position sizing (VIX-adjusted)
- Earnings proximity warning

The IBKR filters are designed so that >70% of survivors should receive a BUY or strong HOLD verdict from STA. If the hit rate is lower, the IBKR filters need tightening.

---

## One-Line Summary

"A 10-factor IBKR screener designed to pre-select Minervini Stage 2 stocks with strong earnings growth and institutional backing, feeding a backtested swing trade analysis system."
