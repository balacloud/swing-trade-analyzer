# Value Investing Research Prompt — Quality at a Fair Price

**Created:** April 21, 2026 (Day 73)
**Purpose:** Identify the minimum viable set of metrics to detect quality stocks at fair/undervalued prices — Buffett, Damodaran, and top 5 value investor frameworks. For small, mid, and large caps separately.
**Output target:** STA Value Investing Tab design spec

**Recommended LLMs:**
| Prompt | Recommended LLM | Why |
|--------|----------------|-----|
| Prompt 1: Metric validation | **Perplexity Deep Research** | Best for academic citations + investor primary sources |
| Prompt 2: Cap-size adjustments | **ChatGPT Deep Research** | Good at structured comparisons |
| Prompt 3: Data availability audit | **Claude Opus** | Best for reasoning about API feasibility |
| Prompt 4: Failure modes | **Gemini Deep Research** | Good at finding edge cases and counter-examples |

**Workflow:**
1. Run all 4 prompts
2. Collect responses
3. Bring back to Claude for synthesis → design spec for Value Tab

---

## PROMPT 1: Core Metric Validation (Run on Perplexity Deep Research)

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous financial research auditor. Your job is to be accurate, not agreeable.

### RULES:
1. Do NOT fabricate citations, book page numbers, or formula sources.
2. If a metric is investor-specific, cite the ORIGINAL source (book, letter, paper).
3. Express calibrated uncertainty. "Widely attributed" ≠ "verified primary source."
4. Reason step-by-step BEFORE issuing a verdict.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <book/paper/letter/DOI>]: Traceable to primary source.
- [PLAUSIBLE — REASON: <why>]: Consistent with philosophy but not directly cited.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but oversimplified.
- [UNVERIFIED — NEEDS: <what evidence required>]: Cannot find primary source.

---

## RESEARCH QUESTION: Minimum Viable Value Investing Metrics

I am building a "Value Investing" tab in a stock analysis tool. Goal: identify quality stocks
available at a fair or undervalued price. NOT a trading system — this is for 3-5 year holds.

I want to know: **what is the MINIMUM set of quantitative metrics that the top 5 most
successful value investors actually use, backed by their primary sources?**

### The 5 investors I want to cover:
1. **Warren Buffett** — Berkshire Hathaway letters, The Warren Buffett Way (Hagstrom)
2. **Aswath Damodaran** — Valuation textbooks, NYU datasets, blog posts
3. **Benjamin Graham** — The Intelligent Investor, Security Analysis
4. **Peter Lynch** — One Up on Wall Street, Beating the Street
5. **Joel Greenblatt** — The Little Book That Beats the Market (Magic Formula)

### For each investor, evaluate these claimed metrics:

---

### CLAIM SET 1: Quality Metrics (Is this a good business?)

**Claim 1.1:** ROE (Return on Equity) > 15% consistently over 5 years is Buffett's
primary quality screen.
→ Evaluate: Is this the right threshold? Is it consistently stated in Buffett's letters?
   Does it hold across sectors (banks, capital-intensive industrials)?

**Claim 1.2:** ROIC (Return on Invested Capital) > WACC is Damodaran's primary value
creation test.
→ Evaluate: Is this Damodaran's actual primary metric or one of many? What threshold?
   How is WACC approximated for retail investors without DCF tools?

**Claim 1.3:** Net Profit Margin > 10% is a good quality filter for large caps.
→ Evaluate: Is this threshold supported? Does it differ by sector? What did Buffett
   actually say about margins?

**Claim 1.4:** Free Cash Flow Yield > 5% indicates a business generating real cash.
→ Evaluate: Is FCF yield a Buffett/Damodaran metric or modern derivative?
   What threshold is actually used?

**Claim 1.5:** Debt/Equity < 0.5 is Graham's safety threshold.
→ Evaluate: Is D/E < 0.5 Graham's actual number or a simplification?
   Does this apply to financial sector stocks?

---

### CLAIM SET 2: Valuation Metrics (Am I paying a fair price?)

**Claim 2.1:** Graham Number = √(22.5 × EPS × Book Value per Share).
If current price < Graham Number → undervalued by Graham's standards.
→ Evaluate: Is this formula directly from Graham or a derivative?
   What's the 22.5 constant based on? Is it still valid today (interest rates)?

**Claim 2.2:** PEG Ratio < 1.0 means you are paying less than the growth rate justifies.
Peter Lynch's primary valuation tool.
→ Evaluate: Is PEG < 1.0 Lynch's threshold? What growth rate did he use (1yr? 5yr?)?
   Is PEG valid for low-growth, high-quality businesses (Buffett style)?

**Claim 2.3:** DCF (Discounted Cash Flow) is Damodaran's gold standard. Intrinsic value
= sum of discounted future free cash flows + terminal value. Margin of safety =
(Intrinsic - Price) / Intrinsic.
→ Evaluate: What discount rate did Damodaran use? 10%? Risk-free rate + premium?
   How sensitive is DCF to the growth assumption (1% change = how much value change)?
   Is DCF practical for retail investors or too assumption-dependent?

**Claim 2.4:** EV/EBIT < 10 is Joel Greenblatt's "earnings yield" cheap threshold.
→ Evaluate: Is EV/EBIT < 10 Greenblatt's actual threshold or approximate?
   What's the correct denominator (EBIT vs EBITDA vs NOPAT)?

**Claim 2.5:** Price/Book < 1.5 is Graham's primary valuation threshold for
undervalued stocks.
→ Evaluate: Is P/B < 1.5 Graham's stated number? From which edition of
   The Intelligent Investor? Does P/B still apply in an era of intangible assets
   (software companies with low book value but high earnings)?

---

### CLAIM SET 3: Growth & Stability Metrics

**Claim 3.1:** Consistent EPS growth over 5 years (no loss years) is Buffett's
minimum predictability requirement.
→ Evaluate: Is this accurately attributed to Buffett? What did he say about cyclical
   businesses that have loss years?

**Claim 3.2:** Revenue growth > 10% annualized indicates a growing moat.
→ Evaluate: Is 10% the right threshold? Did any of the 5 investors cite a
   specific revenue growth threshold?

**Claim 3.3:** Interest Coverage Ratio > 5x (EBIT/Interest Expense) is a safety threshold.
→ Evaluate: Is this Graham's or Damodaran's threshold? What's the primary source?

---

### FINAL QUESTION FOR PROMPT 1:

Based on your research, give me:
1. The **5 most universally agreed-upon** metrics across all 5 investors (the intersection)
2. The **3 metrics that are investor-specific** (only one of them uses it)
3. The **2 metrics that sound right but are actually unreliable** in practice

Format your answer as a ranked table with metric name, investor source, threshold,
and a one-line caveat.
```

---

## PROMPT 2: Cap-Size Adjustments (Run on ChatGPT Deep Research)

```
## RESEARCH QUESTION: Value Investing Metrics by Market Cap Size

I am building a value investing screener. I understand that the same valuation thresholds
(P/E, P/B, ROE) do not apply equally to small-cap, mid-cap, and large-cap stocks.

### Context:
- Small-cap: Market cap < $2B
- Mid-cap: Market cap $2B - $10B
- Large-cap: Market cap > $10B

### Questions:

**Q1: ROE thresholds by cap size**
Claim: "ROE > 15% is a good quality threshold for all cap sizes."
→ Is this accurate? Small-cap companies often have higher ROE volatility.
   What adjustments did value investors make for small-cap ROE?
   Did Graham, Buffett, or Lynch specifically address ROE thresholds by cap size?

**Q2: P/E ratio expectations by cap size**
Claim: "A P/E < 15 indicates undervaluation across all market caps."
→ Evaluate: Small-cap companies often trade at lower P/E due to liquidity risk.
   Large-cap quality companies often command P/E 20-30. What's the right
   relative valuation framework? Is P/E vs sector median more useful than
   absolute thresholds?

**Q3: Debt tolerance by cap size**
Claim: "D/E < 0.5 applies equally to all cap sizes."
→ Small-cap companies often have higher debt due to growth phase.
   Large-cap industrials carry structural debt. What adjustments should be made?

**Q4: DCF reliability by cap size**
Claim: "DCF is equally applicable to small, mid, and large-cap companies."
→ Evaluate: Small-cap growth rates are harder to project. Terminal value dominates
   small-cap DCF even more. What did Damodaran say about applying DCF to
   small/micro-cap companies?

**Q5: Graham Number applicability by cap size**
Claim: "Graham Number works for all cap sizes."
→ Evaluate: Graham developed his framework primarily for large, established companies.
   Does the Graham Number apply to growth-stage small-caps with negative earnings?

**Q6: Liquidity adjustment**
Claim: "Illiquidity discount of 20-30% should be applied to small-cap intrinsic values."
→ Evaluate: Is this Damodaran's published number? Where does it come from?

### Final output requested:
A matrix table: Metric × Cap Size (Small/Mid/Large) → Threshold + Caveat
```

---

## PROMPT 3: Data Availability Reality Check (Run on Claude Opus)

```
I am building a value investing tab in a stock analysis tool. My data sources are:
- **yfinance** (free, unofficial): EPS, P/E, P/B, revenue, bookValue, freeCashflow,
  debtToEquity, returnOnEquity, returnOnAssets, operatingMargins, earningsGrowth,
  revenueGrowth, grossMargins
- **Finnhub** (free tier, 60 req/min): Basic financials including roeTTM, roaTTM,
  debtEquityRatioAnnual, peNormalizedAnnual, pbAnnual, dividendYieldIndicatedAnnual,
  epsTTM, revenueGrowthTTMYoy
- **Alpha Vantage** (free tier, 25 req/day): Income statement, balance sheet,
  cash flow statement (annual + quarterly, last 5 years)

### For each metric below, tell me:
1. Is this metric computable from my available data sources?
2. Which source is most reliable for it?
3. What's the formula using available fields?
4. What's the failure rate (missing data risk)?

**Metrics to evaluate:**
1. Graham Number = √(22.5 × EPS_ttm × BookValuePerShare)
2. PEG Ratio = (P/E) ÷ (5yr EPS growth rate annualized)
3. FCF Yield = FreeCashFlow / MarketCap
4. ROIC = NOPAT / Invested Capital  (NOPAT = EBIT × (1 - tax rate))
5. EV/EBIT = (MarketCap + TotalDebt - Cash) / EBIT
6. DCF Lite = FCF × (1 + g) / (discount_rate - terminal_g)  [single-stage]
7. Interest Coverage = EBIT / InterestExpense
8. Earnings Consistency Score = count of profitable years in last 5 years

### Additional questions:
- For small-cap stocks (< $2B), how often is FCF data missing from yfinance?
- Is Alpha Vantage's 5-year income statement data reliable enough for EPS growth calculation?
- For ROIC, is the invested capital computable from yfinance balance sheet fields?
- What is the most common failure mode when computing Graham Number
  (negative EPS, negative book value, etc.)?

### Output format requested:
A table: Metric | Computable? | Best Source | Formula | Missing Data Risk (Low/Med/High)
```

---

## PROMPT 4: Failure Modes & Anti-Patterns (Run on Gemini Deep Research)

```
## RESEARCH QUESTION: Where Do Value Investing Metrics Fail?

I am building a value investing screener using these metrics:
- Graham Number (EPS × Book Value)
- PEG Ratio (P/E ÷ growth)
- DCF Lite (FCF-based intrinsic value)
- ROE > 15%
- D/E < 0.5
- FCF Yield > 5%

Before implementing, I want to understand where each metric breaks down.

### For each metric, evaluate:

**Q1: Graham Number failure modes**
- Does Graham Number work for technology companies with low book value?
- Does it work for financial companies (banks, insurance) where book value is primary?
- What happens with negative EPS? Negative book value?
- Is the Graham Number still valid after decades of interest rate changes since Graham's era?

**Q2: ROE failure modes**
- Can ROE be artificially inflated by share buybacks reducing equity?
  (Example: a company buying back shares reduces book equity, inflating ROE
  without improving underlying business quality)
- Does high ROE always indicate quality or can it mask leverage risk?
- How do you distinguish "good" high ROE (Buffett) from "bad" high ROE (excessive leverage)?

**Q3: PEG ratio failure modes**
- What growth rate to use: analyst estimate (forward), historical (trailing), or 5yr?
  Does the choice materially change the result?
- Does PEG work for cyclical companies with volatile earnings?
- Is PEG valid for zero-growth, high-quality businesses that Buffett would still buy?

**Q4: DCF failure modes**
- How sensitive is a single-stage DCF to the terminal growth rate assumption?
  Example: FCF=$1B, g=3% vs g=4% at 10% discount rate — how much does
  intrinsic value change?
- Is a simplified DCF (single-stage, no WACC computation) misleading vs
  providing useful directional guidance?
- What is Damodaran's published critique of simplified DCF models?

**Q5: D/E failure modes**
- Sector-specific: utilities, banks, REITs structurally carry high D/E.
  Does the D/E < 0.5 filter inappropriately exclude these?
- Does D/E capture off-balance-sheet debt (operating leases post-IFRS 16)?

**Q6: Composite scoring failure modes**
- If I combine these metrics into a composite "Value Score," what are the
  known failure modes of composite scoring?
- Did Greenblatt's Magic Formula (ROC + EY composite) outperform the market
  consistently after publication? What happened to the edge after it became known?

### Final question:
What are the 3 most dangerous "value traps" — stocks that look great on all these
metrics but are actually bad investments? Give real historical examples if possible.

### Output format:
For each metric: a failure mode table with Scenario | Why It Breaks | Correction/Guard
```

---

## SYNTHESIS INSTRUCTIONS (Bring back to Claude after running all 4 prompts)

Once you have responses from all 4 LLMs, paste them back and ask Claude to:

1. **Identify the consensus metric set** — what did all 4 LLMs agree is reliable?
2. **Flag the controversial metrics** — where did LLMs disagree?
3. **Design the minimum viable metric set** for small/mid/large cap separately
4. **Identify which metrics STA can compute today** vs which need new API calls
5. **Draft the Value Tab spec** based on validated metrics only

---

*This document is research-only. No implementation until synthesis is complete.*
*Golden Rule #15: Never implement without validation — require research, backtest, or practitioner consensus first.*
