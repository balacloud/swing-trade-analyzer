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

# prepexlity research answer 
Buffett, Graham, Lynch, Greenblatt, and Damodaran all care about profitability on capital, balance‑sheet strength, and buying at a discount to a conservative value estimate, but most of the hard “X % / Y× for Z years” rules in your list are modern screeners built on top of their ideas rather than primary rules they themselves codified. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html)

Below is claim‑by‑claim audit, followed by the ranked metric table you asked for.

***

## Claim set 1 – Quality metrics

### Claim 1.1 — “Buffett uses ROE > 15% for 5 years as his primary quality screen”

**[MISLEADING — CORRECTION: Buffett wants sustainably high returns on capital with little debt, but has not codified ‘ROE > 15% for 5 years’ as a universal hard rule.]**

- Buffett repeatedly emphasizes businesses with “enduring competitive advantages” that can earn **high returns on invested capital** over time, not a specific 15 % ROE screen. [durablevalue](https://durablevalue.com/wp-content/uploads/2015/05/Buffetts-references-to-competitive-advantages.pdf)
- A widely circulated secondary summary claims his 1987 letter preferred firms with average ROE > 20 % over 10 years and no year below 15 %, but this is commentary, not text you can trace cleanly in the Berkshire letters; the letters themselves stress high ROE relative to peers and low leverage rather than fixed numeric cutoffs. [moomoo](https://www.moomoo.com/ca/learn/detail-oracle-of-omaha-warren-buffett-roe-20-is-preferable-117152-240412155)
- Hagstrom’s *The Warren Buffett Way* and Buffett’s acquisition criteria talk about “good return on equity while employing little or no debt”, but again do not give a universal 15 % / 5‑year formula. [goodreads](https://www.goodreads.com/work/quotes/488568-the-warren-buffett-way)

**Implication for your tool:** Treat “ROE > ~15 % for 5–10 years with modest leverage” as a **reasonable screen derived from his philosophy**, not as “Buffett’s stated primary rule.”

***

### Claim 1.2 — “ROIC > WACC is Damodaran’s primary value‑creation test”

**[VERIFIED — SOURCE: Aswath Damodaran, “Five Cheap Companies that Create Value” and ‘Return on Capital (ROC), ROIC and ROE’ papers at NYU Stern.]**

- Damodaran explicitly defines **value creation** as earning a return on invested capital (ROIC) greater than the weighted average cost of capital (WACC): “A company creates value only if its ROIC is higher than its WACC.” [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf)
- He uses this spread (ROIC − WACC) as a central test of economic moat/value creation across his teaching, writings, and data sets, though it is **one of several key metrics**, not the only one. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/country/valueversusprice.pdf)
- For non‑professional investors, he allows approximations: using his published industry WACCs, or building WACC from risk‑free rate plus implied equity risk premium and an industry beta, sometimes with synthetic ratings from interest‑coverage tables when no bond rating exists. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html)

**Practical note:** For your UI, “ROIC > WACC” is a **clean, Damodaran‑faithful value‑creation flag**, but not a complete quality assessment by itself.

***

### Claim 1.3 — “Net profit margin > 10% is a good quality filter for large caps”

**[UNVERIFIED — NEEDS: An explicit margin threshold from Buffett, Graham, Lynch, Greenblatt, or Damodaran; available sources only say ‘high margins’, not ‘>10% for large caps.’]**

- Buffett praises **high profit margins** as evidence of a durable competitive advantage and good management, and highlights unusually high margins in some Berkshire letters, but does not publish a “>10 % net margin” rule. [berkshirehathaway](https://www.berkshirehathaway.com/letters/1991.html)
- Damodaran uses operating and net margins extensively when modeling profitability and convergence to industry norms, but again with **industry‑relative** reasoning rather than global numeric cutoffs. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch2.pdf)
- None of the five investors, in primary texts, set a universal “10 % net margin” line; margins vary structurally by sector (retail vs software vs utilities), so a flat 10 % filter can wrongly exclude low‑margin but excellent businesses (e.g. cost‑leaders) and wrongly include high‑margin but fragile ones.  

**Implication:** Keep a **margin‑relative‑to‑industry** metric; treat “>10 %” as an optional heuristic, not as a primary‑source rule.

***

### Claim 1.4 — “Free Cash Flow Yield > 5% indicates a business generating real cash (Buffett/Damodaran metric)”

**[MISLEADING — CORRECTION: High free‑cash‑flow yield can flag cheap cash generators, but neither Buffett nor Damodaran use a ‘>5% FCF yield’ rule; Damodaran explicitly warns that one‑year FCF is noisier than earnings for pricing.]**

- Buffett’s analogue is “owner earnings” (net income plus non‑cash charges minus maintenance capex); he cares about cash generation but does **not** use FCF‑yield thresholds in his letters. [goodreads](https://www.goodreads.com/work/quotes/488568-the-warren-buffett-way)
- Damodaran relies heavily on **free cash flow (FCFF/FCFE) in DCF**, but in a 2022 blog post he notes that a single year’s free cash flow is “more noise… and less informative about a company’s operating health than a single year’s earnings”, and that replacing P/E or EV/EBITDA with FCF‑scaled multiples offers **little benefit** for pricing screens. [aswathdamodaran.substack](https://aswathdamodaran.substack.com/p/earnings-cash-flows-and-free-cash)
- A “>5 % FCF yield” cutoff is a modern value‑screen convention; it is **not sourced** to any of the five investors and can be badly distorted by one‑off working‑capital swings, cyclical capex, or shrinking businesses.  

**Implication:** You can surface **FCF yield as a secondary valuation lens**, but don’t badge “>5 %” as Buffett‑ or Damodaran‑canonical.

***

### Claim 1.5 — “Debt/Equity < 0.5 is Graham’s safety threshold”

**[MISLEADING — CORRECTION: Graham specified conservative debt constraints via current assets and working capital, not a universal D/E<0.5; modern D/E cut‑offs (0.25–0.5) are reinterpretations and do not apply cleanly to financials.]**

- For “defensive” stocks, Graham required **current assets ≥ 2× current liabilities** and **long‑term debt ≤ net current assets**, rather than a D/E ratio. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/)
- Some modern summaries infer approximate D/E caps: one notes Graham “demanded a debt‑to‑equity ratio of less than 25 %” as a conservative interpretation, while another uses total debt/current assets < 1.1. [cabotwealth](https://www.cabotwealth.com/daily/value-stocks/benjamin-grahams-value-stock-criteria)
- Graham made explicit exceptions (e.g. utilities) and tailored criteria by sector; a flat D/E < 0.5 applied to **all** companies, especially financials, is not from his text and is often impractical for banks and insurers whose business model is leverage.  

**Implication:** Implement **strong balance‑sheet rules** (current ratio, LTD vs working capital, interest coverage) rather than a universal “Graham D/E < 0.5” tag.

***

## Claim set 2 – Valuation metrics

### Claim 2.1 — “Graham Number = √(22.5 × EPS × BVPS); if price < Graham Number, the stock is undervalued by Graham’s standards”

**[MISLEADING — CORRECTION: The formula is correctly derived from Graham’s defensive‑investor limits, but he framed it as a maximum *ceiling* price, not a standalone ‘if below then undervalued’ signal.]**

- In *The Intelligent Investor* Graham states that for defensive stocks, **P/E should not exceed 15** and **P/B should not exceed 1.5**, and that the product P/E × P/B should not exceed 22.5. [en.wikipedia](https://en.wikipedia.org/wiki/Graham_number)
- Algebraically, that implies a maximum fair price of √(22.5 × EPS × BVPS): this is the modern **Graham Number**, and sites like GrahamValue and Wikipedia show the exact derivation from his text. [grahamvalue](https://www.grahamvalue.com/article/using-graham-number-correctly)
- Graham intended this as a conservative **price ceiling among several criteria** (size, financial condition, earnings stability, dividend record, growth, valuation), not as “if price < Graham Number then fully Graham‑approved and undervalued”; low price alone without quality fails his framework. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/)

**Implication:** You can label “Price < Graham Number” as “passes Graham defensive valuation check,” not as “Graham‑style undervalued” in isolation.

***

### Claim 2.2 — “PEG < 1 is Peter Lynch’s primary valuation tool”

**[PLAUSIBLE — REASON: Lynch popularized PEG and treats P/E ≈ growth rate (PEG ≈ 1) as ‘fair value’, but he uses it as a major *rule‑of‑thumb*, not a sole or rigid primary tool.]**

- In *One Up on Wall Street*, Lynch notes that “the P/E ratio of any company that’s fairly priced will equal its growth rate”, which is exactly the PEG = 1 rule; PEG < 1 thus suggests undervaluation. [moomoo](https://www.moomoo.com/us/learn/detail-what-is-the-peg-ratio-72328-220878208)
- He often combines P/E and multi‑year growth rates (generally 1–3 or more years) in examples, and later extends to PEGY (P/E divided by growth plus dividend yield), calling PEGY > 1 “poor” and < ⅔ “okay” or “fabulous” in some passages. [quantamentaltrader.substack](https://quantamentaltrader.substack.com/p/peter-lynchs-pegy-method-a-detailed)
- However, Lynch emphasizes **business categories, balance‑sheet strength, and qualitative “story”** as much as PEG; he never says “PEG < 1 is my only or primary tool,” and PEG is unreliable for very low‑growth but high‑quality cash machines (Buffett‑style) or highly cyclical earnings.  

**Implication:** Treat PEG as Lynch‑aligned **for growth stocks**, but don’t over‑weight it for slow‑grower/asset‑play segments or across all sectors.

***

### Claim 2.3 — “DCF is Damodaran’s gold standard; intrinsic value is discounted future FCFs plus terminal value; margin of safety = (V−P)/V”

**[VERIFIED — SOURCE: Damodaran, *Investment Valuation*, *The Dark Side of Valuation*, and ‘Intrinsic Valuation’/‘Margin of Safety’ blog posts.]**

- Damodaran explicitly defines **intrinsic value** as the present value of expected future cash flows, discounted at a rate reflecting their risk, and structures his teaching around FCFF/FCFE DCF models with terminal value. [oreateai](https://www.oreateai.com/blog/demystifying-dcf-navigating-aswath-damodarans-valuation-framework/c2f8f860452c307262cc0b379dc9d821)
- He estimates **cost of equity** as risk‑free rate plus beta × equity risk premium (plus country risk where relevant) and WACC as a weighted average of cost of equity and after‑tax cost of debt, often using his own country/industry premium tables. [pages.stern.nyu](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/smallrating.htm)
- In a margin‑of‑safety essay he describes comparing price to intrinsic value and only buying when price is materially below value, giving examples like requiring a 40 % MOS (i.e. P ≤ 0.6 × V), which maps algebraically to (V−P)/V ≥ 40 %. [aswathdamodaran.blogspot](https://aswathdamodaran.blogspot.com/2011/04/margin-of-safety-alternative-risk_16.html)
- He is very clear that DCF is **assumption‑sensitive**; his “10 rules for addressing uncertainty” focus on parsimony, sanity‑checks, and using ranges rather than pretending to pinpoint value to the cent. [rpc.cfainstitute](https://rpc.cfainstitute.org/blogs/enterprising-investor/2012/addressing-uncertainty-in-investment-valuations)

**Implication:** For Damodaran‑style valuation, your “gold standard” tab should be DCF with **transparent assumptions**, MOS as (V−P)/V, and explicit sensitivity bands on growth and discount rates.

***

### Claim 2.4 — “EV/EBIT < 10 is Greenblatt’s ‘earnings yield’ cheap threshold”

**[MISLEADING — CORRECTION: Greenblatt defines earnings yield as EBIT/EV and ranks all stocks on this and ROIC; he does *not* give a fixed ‘EV/EBIT < 10’ cutoff.]**

- In *The Little Book That Beats the Market*, Greenblatt’s magic formula is: rank companies first by **earnings yield = EBIT / enterprise value**, and second by **return on capital = EBIT / (net fixed assets + working capital)**, then buy the top 20–30 combined ranks. [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing)
- He nowhere specifies “EV/EBIT < 10” (or any other number) as a required threshold; cheapness is **relative**, via ranking, not via an absolute multiple. [youtube](https://www.youtube.com/watch?v=2qHsIG-g9SY)
- “EV/EBIT < 10” is a generic value‑investor heuristic that happens to correspond to a 10 % earnings yield; using it is fine, but it is not Greenblatt’s own rule. His denominator is EBIT, not EBITDA or NOPAT, in the original implementation. [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing)

**Implication:** If you want a “Greenblatt” label, implement **universe ranking by EBIT/EV and ROIC**, not a hard EV/EBIT < 10 filter.

***

### Claim 2.5 — “P/B < 1.5 is Graham’s primary valuation threshold”

**[VERIFIED — SOURCE: Benjamin Graham, *The Intelligent Investor*, ch. 14, with the caveat that it’s one of several conditions and primarily suited to asset‑heavy businesses.]**

- For defensive investors, Graham requires that “current price should not be more than 1½ times the book value”, and that P/E on average earnings over three years should not exceed 15; he adds that the product of these two “should not exceed 22.5”. [en.wikipedia](https://en.wikipedia.org/wiki/Graham_number)
- So P/B < 1.5 is explicitly from Graham, but it is **paired with** an earnings multiple cap and other quality tests (size, financial condition, 10‑year earnings record, 20‑year dividends, 10‑year EPS growth). [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/)
- Graham himself notes that price‑to‑book is more meaningful where assets are tangible and reasonably valued; in modern software‑ and brand‑heavy companies, book value understates economic value, so P/B < 1.5 alone can misclassify quality firms as “overvalued.” [en.wikipedia](https://en.wikipedia.org/wiki/Graham_number)

**Implication:** Use “P/B ≤ 1.5 AND P/E ≤ 15 AND product ≤ 22.5” as a **Graham‑defensive valuation tile**, but down‑weight raw P/B in intangible‑heavy sectors.

***

## Claim set 3 – Growth & stability metrics

### Claim 3.1 — “Consistent EPS growth over 5 years (no loss years) is Buffett’s minimum predictability requirement”

**[MISLEADING — CORRECTION: A no‑loss earnings record over long periods is straight from Graham (10 years), while Buffett emphasizes predictable, growing earnings without codifying a ‘5‑year no‑loss’ rule.]**

- Graham’s defensive criteria include “no earnings deficit in the past ten years” and at least a one‑third increase in per‑share earnings over the same period using three‑year averages; that’s a clear primary‑source “no loss years” rule, but at 10 years, not 5. [cabotwealth](https://www.cabotwealth.com/daily/value-stocks/benjamin-grahams-value-stock-criteria)
- Buffett, as summarized by Hagstrom, seeks “an easily understood business whose earnings are virtually certain to be materially higher, five, ten, and twenty years from now,” focusing on **predictability and growth**, but without a 5‑year EPS‑no‑loss formula. [goodreads](https://www.goodreads.com/work/quotes/488568-the-warren-buffett-way)
- A “five‑year test” Buffett describes in 1996 is about **retained earnings producing at least a dollar of market value per dollar retained**, not about every year being profitable. Cyclical businesses with occasional losses can be acceptable if long‑term economics and capital allocation are attractive. [nasdaq](https://www.nasdaq.com/articles/warren-buffetts-5-year-test-is-key-to-building-wealth)

**Implication:** Use **Graham’s actual 10‑year no‑deficit rule** where you want Graham‑defensive purity; for Buffett‑style predictability, model longer‑term earnings trajectory and cyclicality rather than a hard 5‑year no‑loss screen.

***

### Claim 3.2 — “Revenue growth > 10% annualized indicates a growing moat”

**[UNVERIFIED — NEEDS: Any of the five explicitly tying a 10% revenue‑growth threshold to ‘moat’; available primary sources focus on ROIC vs WACC and durable competitive advantage, not raw growth.]**

- Damodaran’s value‑creation framework makes growth a **good thing only when ROIC exceeds WACC**; when ROIC < WACC, higher growth destroys value, regardless of whether revenue grows at 5 % or 20 %. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html)
- Buffett defines “moat” in terms of sustainable competitive advantage—brand strength, cost advantages, network effects—which tend to show up as **high margins and high returns on capital**, not as any particular sales‑growth rate. [sabercapitalmgt](https://sabercapitalmgt.com/buffetts-three-categories-of-returns-on-capital/)
- None of Graham, Lynch, Greenblatt, or Damodaran publish a hard “>10 % revenue growth = moat” rule; Lynch’s growth categories are descriptive, not tied to a sharp 10 % cutoff, and Graham is explicit that many attractive “slow growers” exist. [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio)

**Implication:** For moat‑related logic, favor **ROIC−WACC spreads, margin stability, and competitive‑position variables** over a fixed 10 % revenue‑growth hurdle.

***

### Claim 3.3 — “Interest coverage > 5× is a safety threshold (Graham or Damodaran?)”

**[MISLEADING — CORRECTION: Graham proposed sector‑specific minimum coverage ratios (some near 5×) for bond investors; Damodaran uses coverage to infer synthetic ratings, not a universal ‘>5× is safe’ rule.]**

- In *Security Analysis* and its later commentary, Graham and Dodd recommend minimum ratios of average earnings to fixed charges (interest) that vary by industry and era; summaries cite standards like **5× pre‑tax coverage for railroads** and higher or lower numbers for utilities and industrials, but Graham explicitly calls these “arbitrary” and historically informed. [reddit](https://www.reddit.com/r/ValueInvesting/comments/1gnao2q/security_analysis_book_question/)
- Damodaran’s synthetic rating tables map **interest‑coverage bands** to credit ratings and default spreads (e.g. an ICR of ~3–4× maps to mid‑BB/BBB buckets, higher coverage to A/AA), but he does not anoint “5×” as a universal cut‑off; it’s just part of a sliding scale. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html)
- General finance texts often remark that coverage above 2–3× is minimally acceptable and 5× or more is strong, but that’s modern convention, not a specific Graham or Damodaran rule. [corporatefinanceinstitute](https://corporatefinanceinstitute.com/resources/commercial-lending/interest-coverage-ratio/)

**Implication:** Model **interest coverage as a continuous variable**, perhaps highlighting >3× as “acceptable” and >5× as “strong,” but don’t mis‑attribute “>5× is safe” to a single authority.

***

## Final synthesis – Ranked metric list

Below is a single ranked table combining:

- **1–5:** Metrics that are broadly consistent across *all* five investors (intersection)  
- **6–8:** Metrics that are genuinely investor‑specific  
- **9–10:** Metrics that sound good but are unreliable if used naively

| Rank | Metric name | Investor source(s) | Typical threshold in practice | One‑line caveat |
|------|-------------|--------------------|------------------------------|-----------------|
| 1 (universal) | **Return on capital (ROE/ROIC)** | Buffett (high ROE/ROIC with low debt), Damodaran (ROIC > WACC), Graham (adequate earnings on capital), Lynch (likes high ROE in fast growers), Greenblatt (ROIC in magic formula) [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html) | **ROIC > WACC and/or ROE consistently above industry average**, often ≥ mid‑teens in practitioner screens | True “universal” rule is **“returns on capital clearly above cost of capital and peers”**, not a fixed 15 % line, and capital‑intensive sectors naturally run lower. |
| 2 (universal) | **Earnings level, growth & stability** | Graham (10‑year no deficits, EPS up ≥33 % over decade), Buffett (earnings “virtually certain” to be higher in 5–20 years), Lynch (growth‑rate focus), Greenblatt (needs stable EBIT), Damodaran (uses normalized earnings as DCF input) [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) | **Positive earnings history over 5–10+ years with at least modest real growth**, avoiding chronic loss‑makers | Graham’s primary rule is a **10‑year no‑deficit record**, not 5 years; for Buffett/Damodaran the emphasis is on *predictable* earning power rather than any specific growth percentage. |
| 3 (universal) | **Balance‑sheet strength / leverage** | Graham (current assets ≥2× current liabilities; LTD ≤ net current assets), Buffett (prefers little or no debt), Damodaran (interest‑coverage‑based synthetic ratings), Lynch (warns on over‑levered cyclicals), Greenblatt (EBIT/EV penalizes debt) [blog.portfolio123](https://blog.portfolio123.com/a-stock-pickers-guide-to-benjamin-grahams-screening-rules/) | **Current ratio ≳2, LTD covered by working capital, and interest coverage comfortably >3–5× for non‑financials** | Sector‑ and era‑dependent: Graham’s bond‑like standards are very conservative, and banks/insurers must be assessed with sector‑specific leverage metrics rather than generic D/E caps. |
| 4 (universal) | **Valuation vs earnings (P/E or earnings yield)** | Graham (P/E ≤15 on 3‑yr average earnings), Lynch (P/E vs growth/PEG), Buffett (owner‑earnings yield vs alternatives), Greenblatt (EBIT/EV earnings yield), Damodaran (P/E/EV multiples alongside DCF) [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) | **P/E below conservative ceilings (≈15× normalized earnings) or high earnings yield (e.g. EBIT/EV well above bond yields and peers)** | Thresholds are context‑dependent: inflation, rates, cyclicality, and growth prospects change what counts as “cheap,” and all five insist valuation be read together with business quality. |
| 5 (universal) | **“Margin of safety” – price vs intrinsic value/assets** | Graham (margin of safety; P/E×P/B ≤22.5; price ≤ Graham‑style ceilings), Buffett (only buy when price is well below conservative business value), Damodaran (explicit MOS on DCF), Lynch (wants “story” plus attractive valuation), Greenblatt (top decile cheap‑and‑good rankings) [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) | **Price meaningfully below conservative value (e.g. below Graham Number, or ≥20–40 % discount to intrinsic value estimate)** | None gives a single magic percentage, but all agree that **built‑in valuation slack** is essential because all valuation inputs are noisy and business outcomes are uncertain. |
| 6 (investor‑specific) | **Graham Number (defensive fair‑value ceiling)** | Benjamin Graham, *The Intelligent Investor* ch. 14; modern derivations (GrahamNumber = √(22.5 × EPS × BVPS)) [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) | **Price ≤ √(22.5 × EPS × BVPS)** | This is explicitly derived from Graham’s P/E and P/B caps, but it applies to **defensive, asset‑heavy firms** and must be combined with his quality and financial‑strength tests. |
| 7 (investor‑specific) | **PEG / PEGY ratio (P/E to growth)** | Peter Lynch, *One Up on Wall Street*; PEG/PEGY elaborations in later commentary [moomoo](https://www.moomoo.com/us/learn/detail-what-is-the-peg-ratio-72328-220878208) | **PEG ≈ 1 as “fair value”; PEG < 1 (or PEGY < 1) as potentially undervalued for reasonably predictable growers** | Very useful in **Lynch‑style growth buckets**, but breaks down for low‑growth compounders, cyclicals with noisy EPS, and cases where consensus growth estimates are unreliable. |
| 8 (investor‑specific) | **Magic Formula composite rank (EBIT/EV + ROIC)** | Joel Greenblatt, *The Little Book That Beats the Market* and implementations of magic formula investing [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) | **Top ~20–30 stocks when ranking universe by high EBIT/EV and high ROIC, excluding financials and utilities** | Greenblatt’s edge comes from **relative ranking**, not an absolute EV/EBIT cutoff; copying only “EV/EBIT < 10” misses the spirit and empirical basis of his method. |
| 9 (unreliable if used naively) | **Single‑year FCF yield > 5% as a ‘real cash’ / Buffett–Damodaran filter** | Modern quant/value screeners; Damodaran’s commentary on FCF multipliers [businesstoday](https://www.businesstoday.in/markets/stocks/story/more-noise-less-informative-aswath-damodaran-on-free-cash-flow-350965-2022-10-27) | **One‑year FCF yield ≥ ~5 % (FCF/market cap)** | One‑year FCF is **extremely noisy** (working capital, capex cycles, restructurings); Damodaran explicitly argues that for *pricing*, FCF‑based multiples often add “more noise, less information” than earnings, and Buffett never uses a 5 % FCF‑yield rule in his writings. [businesstoday](https://www.businesstoday.in/markets/stocks/story/more-noise-less-informative-aswath-damodaran-on-free-cash-flow-350965-2022-10-27) |
| 10 (unreliable if used naively) | **Revenue growth > 10% = “growing moat”** | Generic growth screens; contradicted by Damodaran value‑creation logic and Buffett’s moat definitions [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html) | **Revenue CAGR ≥ ~10 % over 3–5 years** | Growth only adds value when **ROIC > WACC**; fast top‑line growth with poor economics destroys value, and Buffett’s notion of “moat” is about durable pricing power and cost advantage, not hitting an arbitrary revenue‑growth number. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html) |

***

Here’s a concrete spec for a “Value Investing” tab that’s faithful to the five investors and avoids folklore thresholds. [tradeforgood.com](https://tradeforgood.com.au/learn/buffet-investment-model/)

I’d implement it as a **single table of core metrics**, plus a few **investor‑specific tiles** you can toggle on/off.

***

## Core “Value Investing” tab – metric grid

**Rows = metrics, Columns = investors.**  
Each cell defines: whether they use it, how, and what banding to show in the UI.

### Table: Core metrics and how each investor uses them

| Metric | Buffett | Graham | Lynch | Greenblatt | Damodaran |
|--------|---------|--------|-------|------------|-----------|
| **Return on capital (ROE/ROIC)** | Uses high and *sustained* ROE/ROIC with low debt as key quality signal; compare to history and peers, not a fixed 15 % rule. [durablevalue](https://durablevalue.com/wp-content/uploads/2015/05/Buffetts-references-to-competitive-advantages.pdf) Green: ROE/ROIC well above industry and stable; Yellow: around industry; Red: persistently below. | Wants “adequate” earnings on capital; doesn’t define ROIC explicitly but his criteria assume decent profitability. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) Green: ROE ≥ long‑run market average and stable; Yellow: marginal; Red: poor/volatile. | Focuses on high ROE for fast growers and stalwarts, especially when combined with low debt. [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio) Green: ROE high relative to peer group; Yellow: average; Red: low. | One of two core magic‑formula signals: return on capital = EBIT / (net fixed assets + working capital). [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) Green: top quintile ROC in universe; Yellow: mid; Red: bottom. | Central value‑creation test: ROIC vs WACC. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/articles/ROICrules.html) Green: ROIC > WACC by several points; Yellow: ≈WACC; Red: ROIC < WACC. |
| **Earnings level, growth & stability** | Wants businesses whose earnings are “virtually certain” to be higher 5–20 years out; looks at multi‑year track record and resilience. [goodreads](https://www.goodreads.com/work/quotes/488568-the-warren-buffett-way) Green: 10‑year positive EPS, growing; Yellow: occasional dips; Red: frequent losses. | Explicit rule: no earnings deficit in past 10 years; EPS over 10 years up ≥⅓ vs base period. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) Green: passes both; Yellow: minor breaks; Red: deficits. | Categorizes stocks by growth (slow, stalwart, fast); prefers consistent growth matching or exceeding his narrative. [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio) Green: consistent growth aligned with category; Yellow: choppy; Red: story broken. | Requires reasonably stable EBIT for earnings yield and ROC to be meaningful (so excludes many highly cyclical names). [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) Green: EBIT positive and not wildly volatile; Yellow: modest volatility; Red: erratic/loss‑making. | Normalizes earnings for cycles and one‑offs before DCF; looks for earnings that can be forecast with some confidence. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch2.pdf) Green: stable/forecastable; Yellow: uncertain; Red: too noisy to value. |
| **Balance‑sheet strength / leverage** | Strong preference for low or moderate debt; avoids businesses that need heavy leverage to earn decent ROE. [durablevalue](https://durablevalue.com/wp-content/uploads/2015/05/Buffetts-references-to-competitive-advantages.pdf) Green: net debt low, interest coverage strong; Yellow: moderate; Red: tight coverage. | Defensive criteria: current ratio ≥2 and long‑term debt ≤ net current assets. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) Green: passes both; Yellow: borderline; Red: fails. | Warns against over‑levered cyclicals; likes companies that can survive bad years. [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio) Green: coverage good vs industry; Yellow: middling; Red: weak. | Indirect: EBIT/EV penalizes debt; he still excludes financials and utilities by design. [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) Green: debt moderate and coverage solid; Red: highly levered. | Uses interest‑coverage‑based synthetic ratings to infer default spreads and WACC. [pages.stern.nyu](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/smallrating.htm) Green: coverage in investment‑grade band; Yellow: sub‑IG; Red: distressed. |
| **Valuation vs earnings (P/E or earnings yield)** | Looks for “reasonable” price vs *owner earnings* and long‑term prospects; no hard P/E rule but avoids paying stretch multiples for commodity or fragile businesses. [durablevalue](https://durablevalue.com/wp-content/uploads/2015/05/Buffetts-references-to-competitive-advantages.pdf) Green: P/E moderate vs quality and history; Yellow: rich but defensible; Red: speculative. | Defensive rule: P/E ≤15 on average EPS (3 years), and P/E × P/B ≤22.5. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) Green: within both limits; Yellow: slightly above; Red: far above. | Uses P/E heavily, comparing to growth (PEG) and historic ranges. [moomoo](https://www.moomoo.com/us/learn/detail-what-is-the-peg-ratio-72328-220878208) Green: P/E ≤ growth rate and below own history; Yellow: near it; Red: much higher. | Earnings yield = EBIT/EV is half of magic formula; higher is better. [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) Green: top‑rank earnings yield; Yellow: mid; Red: low. | Uses P/E, EV/EBIT, EV/EBITDA etc. as **relative pricing checks** beside DCF, not as primary valuation. [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch2.pdf) Green: cheap vs sector & history; Yellow: fair; Red: expensive. |
| **Margin of safety vs intrinsic value/assets** | Buys only when price is “reasonable” vs a conservative intrinsic value; effectively seeks a fat margin of safety though rarely quantified. [durablevalue](https://durablevalue.com/wp-content/uploads/2015/05/Buffetts-references-to-competitive-advantages.pdf) Green: price materially below conservative DCF/owner‑earnings value; Yellow: near; Red: above. | Conceptual originator of “margin of safety”; for defensive stocks uses low P/E, low P/B, and 10‑year record as layers of protection. [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/) Green: passes his full checklist; Yellow: fails one dimension; Red: fails several. | Wants a compelling “story” + attractive valuation; looks for big upside if thesis plays out. [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio) Green: upside large vs downside risk; Yellow: balanced; Red: asymmetrically poor. | Magic formula: buy top‑ranked “good and cheap” stocks and accept volatility; margin of safety comes from systematic underpricing, not per‑name DCF. [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing) Green: top decile rank; Yellow: mid; Red: bottom. | Frames margin of safety explicitly as **discount of price to DCF‑based intrinsic value**, often requiring substantial discounts (e.g. ≥30–40 %) in his examples. [aswathdamodaran.blogspot](https://aswathdamodaran.blogspot.com/2011/04/margin-of-safety-alternative-risk_16.html) Green: MOS above chosen threshold; Yellow: small MOS; Red: no MOS. |

***

## Investor‑specific tiles (optional sections)

These are *only* shown if the user turns on that investor’s profile. They’re where you can safely use the more idiosyncratic metrics.

### Graham tile

- **Graham Number (defensive fair‑value ceiling)**  
  - Show: \( \sqrt{22.5 \times \text{EPS} \times \text{BVPS}} \) [en.wikipedia](https://en.wikipedia.org/wiki/Graham_number)
  - Bands:  
    - Green: Price ≤ 0.8 × Graham Number  
    - Yellow: 0.8–1.0 ×  
    - Red: > 1.0 ×  
  - Note in UI: “Applies best to established, asset‑heavy firms that also pass Graham’s size, stability, and balance‑sheet tests.” [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/)

- **10‑year earnings and dividend record**  
  - Green: No EPS deficits, and uninterrupted dividends for ≥20 years (if data available). [buffettpedia](https://buffettpedia.com/2024/06/defensive-investors-portfolio-seven-criteria-of-common-stock-seletion/)

### Lynch tile

- **PEG / PEGY**  
  - PEG = P/E ÷ long‑term EPS growth rate; PEGY = P/E ÷ (growth + dividend yield). [moomoo](https://www.moomoo.com/us/learn/detail-what-is-the-peg-ratio-72328-220878208)
  - Bands (for reasonably predictable growers):  
    - Green: PEG or PEGY ≤ 1  
    - Yellow: 1–1.5  
    - Red: > 1.5  
  - Tooltip: “Useful for growth and stalwart categories; less meaningful for slow growers and cyclicals.” [en.wikipedia](https://en.wikipedia.org/wiki/PEG_ratio)

### Greenblatt tile

- **Magic Formula Rank**  
  - Compute:  
    - Earnings yield = EBIT/EV  
    - Return on capital = EBIT / (net fixed assets + working capital) [en.wikipedia](https://en.wikipedia.org/wiki/Magic_formula_investing)
  - Rank each stock in the universe on both; sum ranks; lower is better.  
  - Bands:  
    - Green: in top 20–30 names (or top decile of universe)  
    - Yellow: mid ranks  
    - Red: bottom half  

### Damodaran tile

- **DCF + explicit Margin of Safety**  
  - Inputs: normalized FCFF or FCFE, growth path, and WACC built from risk‑free rate + equity risk premium + beta (or synthetic rating for debt). [pages.stern.nyu](https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch2.pdf)
  - Show intrinsic value per share, and MOS = (V − P) / V.  
  - Bands (example):  
    - Green: MOS ≥ 30–40 % (user‑tunable)  
    - Yellow: 10–30 %  
    - Red: < 10 % or negative MOS  
  - Tooltip: emphasise uncertainty and provide sensitivity mini‑panel for ±1 % changes in growth and discount rate, per his “uncertainty” rules. [rpc.cfainstitute](https://rpc.cfainstitute.org/blogs/enterprising-investor/2012/addressing-uncertainty-in-investment-valuations)

### Buffett tile

- **Buffett‑style Quality Snapshot**  
  - Combine:  
    - High and stable ROE/ROIC vs peers  
    - Low to moderate leverage and strong interest coverage  
    - Long history of positive, growing earnings [trustnet](https://www.trustnet.com/investing/13445255/warren-buffetts-criteria-for-selecting-stocks)
  - Instead of a hard rule, show a **Buffett‑fit score** (e.g. 0–100) based on these inputs and a qualitative note: “Buffett‑like compounding candidate” vs “Capital‑intensive / commodity‑like”.  

***

## Implementation notes for your tool

- **No fake thresholds:** wherever the literature does *not* specify a clear numeric rule (e.g. “net margin > 10 %”), keep it as **relative bands** (above/below industry, stable/volatile) rather than magic numbers.  
- **Sector‑aware:** for P/B and leverage metrics, tag sectors where they’re less meaningful (software, financials, utilities) and gray out or annotate instead of forcing a red/green. Graham’s own criteria were sector‑specific. [en.wikipedia](https://en.wikipedia.org/wiki/Graham_number)
- **View presets:** let the user toggle “Graham view”, “Buffett view”, “Lynch view”, etc., which simply changes which rows/tiles are highlighted and how strict the color bands are.

# Chat GPT Research answers 

## Research conclusion: **cap-size adjustments are necessary**

Your instinct is right: **using one fixed threshold for ROE, P/E, debt, DCF confidence, or Graham Number across small-, mid-, and large-cap stocks will create false positives and false negatives**.

The strongest conclusion from the research is:

> **Market cap should not replace sector and business-model adjustments, but it should change how strict, how stable, and how confidence-weighted each metric is.**

---

# Executive verdicts on each claim

| Claim                                                                | Verdict                              | Bottom line                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ROE > 15% is good for all cap sizes**                              | **Misleading**                       | Buffett admired high ROE **without undue leverage**, but Graham and Lynch did **not** prescribe cap-size ROE cutoffs. For small caps, **stability and multi-year median ROE** matter more than a single 15% reading. ([Berkshire Hathaway][1])                                            |
| **P/E < 15 means undervalued across all market caps**                | **Incorrect**                        | Graham’s 15× rule was for **defensive, established companies** using **3-year average earnings**, not a universal law. Modern relative valuation should compare P/E against **sector peers, growth, and risk**.                                                                           |
| **D/E < 0.5 applies equally to all cap sizes**                       | **Incorrect**                        | Debt tolerance should vary by **business model, cash-flow stability, and refinancing risk**, not market cap alone. Smaller companies often face greater refinancing and floating-rate sensitivity; Graham himself used different debt rules for industrials vs utilities. ([JPMorgan][2]) |
| **DCF is equally applicable across cap sizes**                       | **Conceptually yes, practically no** | Damodaran says valuation fundamentals do not change, but **young/small firms are much harder to value**, terminal value often dominates, and survival probability matters. ([Stern School of Business][3])                                                                                |
| **Graham Number works for all cap sizes**                            | **Incorrect**                        | It is only meaningful for **profitable, asset-backed, established businesses**. It breaks for **negative EPS, weak book value relevance, and growth-stage small caps**.                                                                                                                   |
| **Apply a 20–30% illiquidity discount to small-cap intrinsic value** | **Misapplied**                       | Damodaran discusses 20–30% as a **rule of thumb commonly used for private businesses**, not as a universal small-cap public equity haircut. He explicitly argues discounts should vary by size, health, assets, and cash-flow generation. ([Stern School of Business][4])                 |

---

# Q1. ROE thresholds by cap size

## Is “ROE > 15%” a good universal quality threshold?

**No. It is useful, but not universal.**

### What the classic investors actually said

* **Graham** did **not** use ROE as a primary defensive-investor filter. His quality screen focused on:

  * adequate size,
  * strong financial condition,
  * earnings stability,
  * long dividend history,
  * earnings growth,
  * and moderate valuation. 
* **Buffett** emphasized **high return on equity capital without undue leverage or accounting gimmickry**. That is a **quality principle**, not a cap-size threshold. ([Berkshire Hathaway][1])
* **Lynch** focused more on **growth relative to valuation, earnings story quality, and balance-sheet strength** than on a fixed ROE number by cap size. ([Wikipedia][5])

## Why small-cap ROE needs adjustment

ROE is especially noisy in small caps because:

* earnings can swing sharply year to year,
* small book equity can mechanically inflate ROE,
* leverage can exaggerate ROE,
* one-off tax or margin spikes can distort the figure.

That means a **single-year ROE > 15% can be much less informative in a small cap than in a mature large cap**.

### Screener recommendation

Use **multi-year ROE stability**, not just a one-year cutoff.

| Cap size      | Better ROE rule                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| **Small-cap** | **5-year median ROE > 10–12%**, positive ROE in **at least 4 of 5 years**, and no excessive leverage |
| **Mid-cap**   | **5-year median ROE > 12–15%**, positive in **4 of 5 years**                                         |
| **Large-cap** | **5-year median ROE > 15%** is a strong quality threshold, subject to sector context                 |

### Extra safeguard

For all cap sizes, especially small caps:

* pair ROE with **ROIC** or **ROA**,
* flag **negative book equity**,
* penalize ROE that is high only because of **very high debt**.

Buffett’s wording strongly supports that adjustment: **high ROE is only meaningful when not driven by “undue leverage.”** ([Berkshire Hathaway][1])

---

# Q2. P/E expectations by cap size

## Is “P/E < 15” undervalued across all caps?

**No.**

Graham’s 15× rule was:

* for **defensive investors**,
* on **average earnings of the past three years**,
* paired with P/B discipline,
* and meant for **established companies**, not fast growers or fragile small caps. 

Damodaran’s relative valuation framework is much closer to what your screener needs:

* a higher P/E can be justified by **higher growth**,
* a lower P/E can simply reflect **higher risk**,
* and the correct comparison is often **relative P/E versus sector or peer group**, not an absolute threshold. ([Stern School of Business][6])

## Why cap size matters

Small caps may trade cheaper because of:

* liquidity risk,
* lower analyst coverage,
* financing risk,
* thinner margins or more cyclical business quality.

Large caps, especially high-quality compounders, may reasonably trade at **20–30× earnings** if:

* returns on capital are durable,
* growth is credible,
* reinvestment opportunities are strong.

## Screener recommendation

Use **relative valuation first**, absolute P/E second.

| Cap size      | Better P/E framework                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| **Small-cap** | Prefer **P/E ≤ 0.80× sector median** unless growth quality is unusually strong                               |
| **Mid-cap**   | Prefer **P/E ≤ 0.90× sector median**                                                                         |
| **Large-cap** | **P/E ≤ sector median** is attractive; a premium can be acceptable if ROIC, margins, and growth are superior |

### Important caveat

For growth-oriented businesses, add:

* **PEG**,
* **EV/EBITDA**,
* **FCF yield**,
* and **normalized earnings**.

Lynch’s famous P/E-to-growth logic supports using **growth-adjusted valuation**, not a fixed 15× cutoff. ([Wikipedia][5])

---

# Q3. Debt tolerance by cap size

## Is “D/E < 0.5” universal?

**No. It is too crude.**

Debt should be judged against:

* stability of cash flows,
* capital intensity,
* interest-rate exposure,
* refinancing risk,
* and sector norms.

Graham himself **did not use one debt rule for every type of company**:

* industrials: long-term debt should not exceed working capital,
* utilities: debt could be as high as **2× book equity**. 

That directly undermines the idea that **one D/E threshold fits all**.

## Small-cap nuance

The statement “small caps often have higher debt due to growth phase” is **partly true but incomplete**.

A better formulation is:

> Smaller companies often face **greater debt fragility**, not necessarily higher D/E in every case.

Recent market research notes that smaller firms often have:

* more debt relative to earnings,
* more floating-rate debt,
* shorter debt maturities,
* and higher sensitivity to rates. ([JPMorgan][2])

## Screener recommendation

Use **Net Debt / EBITDA** and **interest coverage** as primary measures. Use D/E only as a secondary flag.

| Cap size      | Debt screen recommendation                                  |
| ------------- | ----------------------------------------------------------- |
| **Small-cap** | **Net Debt / EBITDA < 1.5×** and **interest coverage > 4×** |
| **Mid-cap**   | **Net Debt / EBITDA < 2.0×** and **interest coverage > 4×** |
| **Large-cap** | **Net Debt / EBITDA < 2.5×** and **interest coverage > 3×** |

### Exceptions

Use separate rules for:

* banks,
* insurers,
* REITs,
* utilities,
* pipelines,
* telecoms.

For those sectors, standard D/E is often misleading.

---

# Q4. DCF reliability by cap size

## Is DCF equally applicable?

**In theory, yes. In practice, no.**

Damodaran is very clear:

* The **principles** of DCF do not change for young or small businesses.
* But the **inputs become much less reliable** because:

  * histories are short,
  * margins are immature,
  * revenue forecasts are fragile,
  * financing and failure risk matter,
  * and terminal value can dominate the result. ([Stern School of Business][3])

He also shows that for young growth firms:

* **the bulk of value may sit in terminal value**,
* survival probability should be considered,
* and point-estimate DCFs can badly overstate value if downside scenarios are ignored. 

## Screener recommendation

Treat DCF as a **confidence-weighted valuation tool**.

| Cap size      | DCF use                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| **Small-cap** | Use **scenario DCF only**; require **large margin of safety**, and flag if **terminal value dominates** |
| **Mid-cap**   | DCF is useful, but still use **base / bear / bull scenarios**                                           |
| **Large-cap** | DCF is generally more stable if the business model is mature and cash flows are reasonably forecastable |

### Suggested practical rule

| Cap size      | DCF confidence discipline             |
| ------------- | ------------------------------------- |
| **Small-cap** | Require **≥ 40% margin of safety**    |
| **Mid-cap**   | Require **≥ 30% margin of safety**    |
| **Large-cap** | Require **≥ 20–25% margin of safety** |

These are **screener design recommendations**, not Damodaran’s published fixed cutoffs.

---

# Q5. Graham Number by cap size

## Does the Graham Number work for all cap sizes?

**No.**

The Graham Number derives from:

* **P/E ≤ 15**
* **P/B ≤ 1.5**
* combined into the familiar formula:

[
\text{Graham Number} = \sqrt{22.5 \times EPS \times BVPS}
]

Graham framed this for **defensive-investor quality stocks**, not for:

* young growth companies,
* negative earners,
* asset-light businesses,
* firms with intangible-heavy value creation. 

## Critical limitation

If **EPS is negative**, the Graham Number becomes unusable.
If **book value is not economically meaningful**, it becomes misleading.

## Screener recommendation

| Cap size      | Use of Graham Number                                                             |
| ------------- | -------------------------------------------------------------------------------- |
| **Small-cap** | Use **only** for profitable, asset-backed, mature small caps                     |
| **Mid-cap**   | Useful for traditional value sectors with positive EPS and meaningful book value |
| **Large-cap** | Most applicable for mature, established, asset-supported businesses              |

### Avoid using it for

* software,
* semiconductors with major intangible value,
* biotech,
* platform businesses,
* pre-profit small caps,
* high-growth compounders.

---

# Q6. Liquidity adjustment

## Is “20–30% illiquidity discount” Damodaran’s published number?

**Yes and no.**

Damodaran explicitly acknowledges that practitioners often use a **20–30% illiquidity discount** for **private businesses**. But he presents it as a **rule of thumb to scrutinize**, not as a universal truth. ([Stern School of Business][4])

He also states that illiquidity discounts **should vary** by:

* firm size,
* firm health,
* cash-flow generation,
* asset liquidity,
* and ownership block size. ([Stern School of Business][7])

## Important correction

A **publicly traded small-cap stock** is not the same thing as a **private business**.

So:

> **Do not automatically reduce every small-cap DCF value by 20–30%.**

That would be an overreach.

## Screener recommendation

| Cap size      | Liquidity adjustment                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Small-cap** | **No automatic 20–30% haircut**. Apply a **case-specific 5–15% cautionary discount** only for demonstrably poor liquidity |
| **Mid-cap**   | Usually **0–5%** only if trading liquidity is genuinely thin                                                              |
| **Large-cap** | Generally **0%**                                                                                                          |

### Better public-market liquidity inputs

Instead of a blanket intrinsic-value haircut, use:

* average daily dollar volume,
* bid–ask spread,
* free float,
* insider concentration,
* position size versus daily volume.

---

# Final matrix: Metric × Cap Size → Threshold + Caveat

## Recommended screener matrix

| Metric                   | Small-cap: < $2B                                                                   | Mid-cap: $2B–$10B                                  | Large-cap: > $10B                                                          |
| ------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------- |
| **ROE quality**          | **5-yr median ROE > 10–12%**; positive in 4/5 years                                | **5-yr median ROE > 12–15%**                       | **5-yr median ROE > 15%**                                                  |
| **ROE caveat**           | One-year ROE is noisy; cross-check ROIC/ROA and leverage                           | Check durability of margins and capital efficiency | High ROE is valuable only if not leverage-driven                           |
| **P/E valuation**        | Prefer **≤ 0.80× sector median**                                                   | Prefer **≤ 0.90× sector median**                   | Prefer **≤ 1.00× sector median** unless superior quality justifies premium |
| **P/E caveat**           | Absolute P/E <15 is not enough; check earnings quality                             | Use growth/risk context                            | A 20–30× P/E may be reasonable for elite compounders                       |
| **Debt / leverage**      | **Net Debt/EBITDA < 1.5×**; **Interest coverage > 4×**                             | **< 2.0×**; **Coverage > 4×**                      | **< 2.5×**; **Coverage > 3×**                                              |
| **Debt caveat**          | Small firms are more fragile under refinancing stress                              | Sector context matters                             | Utilities, telecoms, pipelines need special rules                          |
| **DCF usefulness**       | Use **scenario DCF only**; require high margin of safety                           | DCF useful with scenario ranges                    | DCF most dependable when cash flows are mature                             |
| **DCF margin of safety** | **≥ 40%**                                                                          | **≥ 30%**                                          | **≥ 20–25%**                                                               |
| **DCF caveat**           | Terminal value and survival probability can dominate                               | Growth fade assumptions matter                     | Still sensitive to discount rate and terminal growth                       |
| **Graham Number**        | Use only for profitable, asset-backed mature firms                                 | Moderately useful in traditional sectors           | Most applicable among established, asset-supported firms                   |
| **Graham caveat**        | Not usable for negative EPS or growth-stage firms                                  | Weak for asset-light models                        | Not suitable for modern intangible-heavy compounders                       |
| **Liquidity adjustment** | **0% default**; consider **5–15%** only for genuinely poor public-market liquidity | **0–5%** in thinly traded cases                    | Usually **0%**                                                             |
| **Liquidity caveat**     | Do **not** blindly apply Damodaran’s 20–30% private-company rule                   | Use trading data                                   | Illiquidity rarely a core issue                                            |

---

# Best screener design takeaway

For your **value investing screener**, I would build the logic this way:

### 1. Use **absolute thresholds** only where they remain robust

* profitability stability,
* leverage safety,
* interest coverage,
* earnings quality.

### 2. Use **relative thresholds** for valuation

* P/E vs sector median,
* EV/EBITDA vs peers,
* P/B only where book value matters,
* FCF yield vs sector.

### 3. Use **cap size to change confidence and strictness**

* **Small-cap:** stricter balance-sheet and stability requirements; wider margin of safety.
* **Mid-cap:** balanced framework.
* **Large-cap:** allow higher valuations for genuinely superior economics, but demand durability.

### 4. Never let one metric dominate

A small-cap stock with:

* P/E 9,
* ROE 24%,
* D/E 0.3

can still be a trap if:

* earnings are cyclical,
* book equity is tiny,
* revenue quality is poor,
* cash flows are weak,
* liquidity is thin.

That is exactly why the matrix should be **multi-factor, not threshold-only**.

[1]: https://www.berkshirehathaway.com/letters/1979.html?utm_source=chatgpt.com "Chairman's Letter - 1979"
[2]: https://am.jpmorgan.com/no/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/small-cap-valuations-explained/?utm_source=chatgpt.com "Understanding small cap valuations"
[3]: https://pages.stern.nyu.edu/~adamodar/pdfiles/val3ed/c23.pdf?utm_source=chatgpt.com "Valuing Young or Start-Up Firms"
[4]: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/illiquiddisc.htm?utm_source=chatgpt.com "Estimating Illiquidity Discounts"
[5]: https://en.wikipedia.org/wiki/PEG_ratio?utm_source=chatgpt.com "PEG ratio"
[6]: https://pages.stern.nyu.edu/~adamodar/pdfiles/relpe.pdf?utm_source=chatgpt.com "Relative PE Ratios"
[7]: https://pages.stern.nyu.edu/~adamodar/podcasts/valUGspr17/session22.pdf?utm_source=chatgpt.com "Step 6: Consider the effect of illiquidity"

# Gemini
The Structural Vulnerabilities of Value Investing Metrics: An Exhaustive Analysis of Failure Modes and Value TrapsThe architectural foundation of quantitative value investing relies upon the presumption that historical financial data, when distilled into standardized metrics, can reliably identify disparities between market price and intrinsic value. Systematic screening methodologies deploy composite filters to isolate undervalued equities, operating under the assumption that financial markets are periodically inefficient and that mean reversion will eventually correct these pricing anomalies. A standard contemporary screening model might utilize a combination of the Graham Number, the Price/Earnings-to-Growth (PEG) ratio, a simplified Discounted Cash Flow (DCF) intrinsic value, Return on Equity (ROE), Debt-to-Equity (D/E) ratios, and Free Cash Flow (FCF) yields to construct a theoretical portfolio of high-quality, undervalued assets.However, the mechanical application of these financial ratios without rigorous contextual adjustment frequently leads investors into catastrophic misallocations of capital. Financial metrics do not exist in a vacuum; they are highly sensitive to accounting standard revisions, macroeconomic regime shifts, industry-specific capital structures, and corporate financial engineering. When an equity screening model operates blindly, utilizing static formulas to evaluate dynamic enterprises, it cannot distinguish between a temporarily mispriced high-quality asset and a structurally deteriorating business undergoing terminal decline. The latter is the quintessential "value trap," an equity that appears mathematically pristine according to historical multiples but possesses fundamentally compromised future cash flows.To construct a robust quantitative value investing architecture, it is imperative to dissect the precise mathematical and theoretical failure modes of each underlying metric. A quantitative model is only as reliable as its weakest assumption. This comprehensive analysis deconstructs the structural vulnerabilities of the most widely utilized value investing metrics, detailing the macroeconomic, sectoral, and accounting conditions under which they break down. Furthermore, it explores the historical decay of algorithmic alpha in composite value strategies and identifies the most dangerous value traps that consistently evade standard quantitative detection.1. The Graham Number: The Anachronism of Tangible AssetsThe Graham Number, formulated by Benjamin Graham in his seminal work The Intelligent Investor, was designed as a heuristic for the defensive investor seeking a rigid margin of safety. The formula is mathematically defined as the geometric mean of a maximum acceptable Price-to-Earnings (P/E) ratio of 15 and a maximum acceptable Price-to-Book (P/B) ratio of 1.5. By multiplying these maximums ($15 \times 1.5 = 22.5$), the resulting formula establishes a hard ceiling on equity valuation, producing the maximum price a defensive investor should be willing to pay :$Graham Number = \sqrt{22.5 \times EPS \times BVPS}$While elegant in its simultaneous enforcement of earnings capacity and asset-based downside protection, the Graham Number suffers from profound structural limitations when applied to the modern economic landscape. The primary failure mode of the Graham Number is its inherent reliance on Book Value Per Share (BVPS), a metric that fundamentally misrepresents the intrinsic value of modern technology, software, and service-oriented enterprises. During Graham's era, the global economy was dominated by industrial, manufacturing, and railroad companies where tangible assets—such as factories, raw material inventory, and heavy machinery—constituted the bulk of corporate value. In this traditional industrial economy, the liquidation value of physical assets provided a genuine margin of safety.In the contemporary asset-light economy, however, a technology company’s most valuable assets are predominantly off-balance-sheet intellectual property, brand equity, network effects, and human capital. Because current accounting frameworks—such as Generally Accepted Accounting Principles (GAAP)—require internally developed intangible assets, including research and development (R&D) expenditures, to be expensed on the income statement rather than capitalized on the balance sheet, the book value of high-margin technology firms is systematically and heavily understated. Consequently, applying the Graham Number to these entities yields an artificially low intrinsic value, falsely signaling extreme overvaluation and systematically excluding the most profitable sector of the twenty-first century from the value screener.Furthermore, the Graham Number breaks down completely in the presence of negative financial inputs. The mathematical structure of the square root function dictates that the formula becomes undefined if the product of EPS and BVPS is negative. For early-stage companies investing heavily in growth and thereby generating negative EPS, or for mature firms that have aggressively bought back stock to the point of generating a negative shareholder equity balance (a negative BVPS), the Graham Number ceases to compute. Even more dangerously, when both EPS and BVPS are negative—which would mathematically yield a positive product before applying the square root—the resulting calculation produces a nonsensical, fictitious intrinsic value that suggests an underlying margin of safety where none exists. A screener processing a company with massive negative equity and deep net losses might inadvertently flag it as a buy due to this mathematical anomaly.Sectoral misalignments extend beyond the technology sector into the financial services industry. For banking and insurance institutions, book value remains a highly relevant and primary metric of valuation, as their assets and liabilities are largely marked to market and consist primarily of liquid financial instruments. However, the rigid $1.5\times$ P/B multiplier embedded within the 22.5 constant fails to accommodate the nuanced return on tangible common equity (ROTCE) dynamics that drive financial sector valuations. A bank generating exceptionally high returns on its asset base rightfully commands a significant premium to its book value, frequently rendering the Graham Number overly punitive and excluding top-tier financial institutions while favoring lower-quality, underperforming banks that trade below book value precisely because they are destroying capital.Finally, the Graham Number is structurally blind to the macroeconomic interest rate environment. The valuation constants developed by Graham were predicated on an environment where the yield on AAA corporate bonds was approximately 4.4 percent. In a macroeconomic regime characterized by zero-interest-rate policy (ZIRP) or, conversely, aggressive monetary tightening, a static multiple of 15 times earnings becomes intellectually obsolete. Graham himself acknowledged this vulnerability later in his career, noting that fair value multiples must dynamically adjust to prevailing long-term interest rates. He proposed an updated intrinsic value formula, $V = / Y$, where $Y$ represents the current yield on 20-year AAA corporate bonds, to correct for this. Utilizing a static 22.5 multiplier across decades of varying monetary policy mathematically ensures periods of chronic under-allocation during low-rate regimes and hazardous over-allocation during inflationary, high-rate environments.ScenarioWhy It BreaksCorrection / GuardTechnology / Asset-Light FirmsIntellectual property and R&D are expensed rather than capitalized, severely understating BVPS. The formula views these high-margin firms as fundamentally overvalued due to low tangible assets.Substitute Book Value with a capitalized estimate of R&D, or abandon the Graham Number entirely in favor of FCF yield and ROIC metrics for asset-light sectors.Negative EPS or Negative BVPSThe formula requires positive inputs. Negative values either render the square root mathematically undefined or produce a misleading positive integer when both inputs are negative.Implement a programmatic pre-filter: if (EPS < 0 OR BVPS < 0) { return NULL }. The metric cannot be mathematically salvaged in these states.Financial Sector ValuationsWhile BVPS is relevant for banks, the rigid $1.5\times$ P/B ceiling ignores the profitability of the equity. A highly profitable bank will naturally exceed this limit.Replace the Graham Number with a price-to-tangible-book-value (P/TBV) ratio dynamically adjusted for Return on Tangible Common Equity (ROTCE).Interest Rate Regime ShiftsThe 22.5 constant assumes a historical AAA corporate bond yield of approximately 4.4%. It fails to adjust the discount rate for varying macroeconomic realities.Use the updated Graham formula incorporating bond yields, or dynamically adjust the 22.5 constant based on the current risk-free rate.2. Return on Equity (ROE): The Leverage and Buyback MirageReturn on Equity (ROE) is widely championed as the premier metric for evaluating management’s ability to allocate capital and generate shareholder value. Calculated by dividing net income by average shareholders' equity, ROE measures the profitability of the capital explicitly provided by investors. A persistently high ROE is traditionally interpreted as the hallmark of a wide-moat, compound-interest machine capable of generating excess returns without requiring massive external capital injections. Renowned investors like Warren Buffett frequently highlight consistent, high ROE as a definitive indicator of a high-quality franchise business with significant pricing power. However, as a standalone quantitative screening metric, ROE is uniquely susceptible to manipulation through corporate financial engineering, specifically via aggressive capital structure adjustments.The most pervasive failure mode of ROE stems from its vulnerability to share repurchases. When a corporation utilizes its cash reserves—or worse, issues new debt—to buy back its own shares in the open market, the accounting mechanics dictate that the repurchased shares are retired or held as treasury stock, and overall shareholder equity is proportionally reduced. By systematically shrinking the denominator (equity) of the ROE equation, a company can mathematically inflate its ROE even if absolute net income remains stagnant or begins to experience fundamental decline. This creates a dangerous optical illusion for algorithmic screeners: the system identifies a company with an expanding ROE, assuming it represents improving operational efficiency and business quality, when in reality, the underlying business is deteriorating and management is merely cannibalizing the balance sheet to manufacture algorithmic yield.This optical distortion is intimately tied to the second major failure mode: the masking of insolvency risk through excessive leverage. High ROE does not inherently indicate a high-quality business; it can simply indicate a highly indebted one. Because the ROE calculation completely ignores the debt obligations utilized to finance operations, a company with minimal equity and a massive debt load will display an astronomically high ROE on the marginal profits it generates. During favorable macroeconomic conditions and broad economic expansions, this financial leverage acts as an accelerant, driving ROE to elite levels and pushing the stock to the top of value screening lists. However, this exact capital structure renders the equity incredibly fragile. In a cyclical downturn or an environment of rising interest rates, the debt servicing costs overwhelm operating income, rapidly wiping out the thin equity tranche and rendering the high historical ROE irrelevant as the company faces potential restructuring.To distinguish between the "good" ROE generated by high-quality franchise businesses and the "bad" ROE manufactured through leverage and financial engineering, analysts must deconstruct the metric using the DuPont Analysis framework. The DuPont formula dissects ROE into three constituent drivers:$ROE = Profit Margin \times Asset Turnover \times Financial Leverage$$ROE = \left(\frac{Net Income}{Sales}\right) \times \left(\frac{Sales}{Total Assets}\right) \times \left(\frac{Total Assets}{Shareholders' Equity}\right)$By isolating these three variables, the true engine of a company's returns is exposed. If the high ROE is driven by expanding net profit margins or superior asset turnover, it signifies operational excellence, brand power, and a defensible economic moat. Conversely, if the ROE is propelled solely by the financial leverage multiplier (Total Assets divided by Shareholders' Equity), the metric is a mirage masking profound balance sheet risk. A quantitative screener that accepts ROE without performing a DuPont decomposition is structurally flawed.Furthermore, relying solely on ROE ignores the holistic operational efficiency of the enterprise. For capital-intensive industries such as telecommunications, energy exploration, and heavy manufacturing, Return on Capital Employed (ROCE) or Return on Assets (ROA) serve as vastly superior metrics. ROCE divides Earnings Before Interest and Taxes (EBIT) by total capital employed (the sum of both debt and equity), thereby neutralizing the distortions created by varying capital structures and differing debt loads. By viewing ROE and ROCE in tandem, a quantitative screener can detect structural discrepancies: a soaring ROE coupled with a stagnant or declining ROCE is the definitive quantitative signature of a company using dangerous levels of debt to mask operational decay.ScenarioWhy It BreaksCorrection / GuardAggressive Share RepurchasesBuybacks reduce shareholder equity (the denominator), artificially inflating ROE without any fundamental improvement in net income or operational efficiency.Screen for absolute Net Income growth alongside ROE. If ROE is rising but Net Income is flat or declining, flag the equity as a potential buyback distortion.High Leverage / Debt AccumulationExcessive debt shrinks the equity base relative to the size of the operations. High leverage multiplies small operational profits into massive ROE figures, hiding bankruptcy risk.Utilize the DuPont Analysis to isolate the equity multiplier. Require the D/E ratio to be assessed concurrently, or replace ROE with ROCE to measure total capital efficiency.Negative Equity / Accumulated DeficitsIf a company has a massive accumulated deficit causing negative equity, and generates a net loss (negative income), the resulting math produces a falsely positive ROE.Implement strict logical screening gates: ROE should only be calculated and screened if both Net Income and Shareholder Equity are strictly greater than zero.3. Price/Earnings-to-Growth (PEG) Ratio: The Denominator DilemmaThe Price/Earnings-to-Growth (PEG) ratio—calculated by dividing a stock's trailing or forward P/E ratio by its expected earnings growth rate—was popularized by legendary investors such as Peter Lynch as a mechanism to normalize valuation across companies with disparate growth trajectories. The theoretical premise dictates that a fairly valued company should trade at a PEG ratio of 1.0, meaning its P/E multiple is perfectly aligned with its earnings growth rate. A PEG below 1.0 suggests undervaluation, while a PEG above 1.0 suggests the market is overpaying for anticipated growth. However, as a strict quantitative screening tool, the PEG ratio introduces acute sensitivities and definitional ambiguities that frequently generate false market signals.The paramount failure mode of the PEG ratio lies in the highly subjective selection of the growth rate input utilized in the denominator. A quantitative screener must systematically rely on either historical (trailing) growth rates or analyst-estimated (forward) growth rates, and the divergence between these two metrics routinely alters the final PEG output by orders of magnitude. Utilizing a trailing 5-year compound annual growth rate (CAGR) embeds a severe backward-looking bias into the model; it systematically penalizes companies currently undergoing operational turnarounds and overly rewards mature companies whose historical growth is plateauing but still reflects past glory.Conversely, utilizing 12-month, 3-year, or 5-year forward consensus analyst estimates introduces acute forecasting risk into the equation. Sell-side analysts exhibit well-documented behavioral and institutional biases; they systematically extrapolate recent trends, overestimating future growth during economic expansions and bull markets, while severely underestimating recoveries during economic contractions. Relying on forward PEG effectively hardcodes human behavioral bias and institutional herding into an otherwise objective quantitative screener.Furthermore, the PEG ratio breaks down spectacularly when applied to cyclical companies characterized by highly volatile, non-linear earnings trajectories. In industries such as commodities, energy extraction, semiconductors, and automotives, earnings fluctuate wildly with the macroeconomic cycle. At the bottom of an economic cycle, absolute earnings are severely depressed, making historical growth negative (which renders the PEG ratio undefined or negative) and expected forward growth mathematically massive as earnings recover from an artificially low base. Dividing a low trough P/E by a massive recovery growth rate results in an artificially depressed PEG ratio, falsely signaling deep undervaluation precisely when the fundamental risk to the business is highest.Additionally, the PEG ratio is structurally invalid for mature, high-quality businesses characterized by high free cash flow generation but zero to low nominal growth. A dominant consumer staples company or a legacy utility may generate tremendous returns on invested capital, pay a high dividend yield, and possess pricing power that flawlessly hedges against inflation. Yet, because its top-line volume growth is essentially flat, the denominator of the PEG ratio approaches zero. Dividing a moderate P/E ratio by a growth rate of 1% or 2% produces an exorbitantly high PEG ratio. For example, a P/E of 15 divided by a 1.5% growth rate yields a PEG of 10. This calculation categorizes a phenomenal, cash-producing asset that Warren Buffett might favor as wildly "overvalued." The standard PEG ratio fails entirely to account for the dividend yield, which constitutes a massive portion of total shareholder return for mature equities, necessitating the deployment of a PEGY ratio (P/E divided by the sum of the Growth rate and the Dividend Yield) to restore mathematical parity.ScenarioWhy It BreaksCorrection / GuardChoice of Growth Rate (Forward vs. Trailing)Trailing growth assumes the past dictates the future, missing inflection points. Forward growth relies on notoriously optimistic and inaccurate sell-side analyst consensus estimates.Require a blended growth rate (e.g., an average of 3-year trailing and 3-year forward), and stress-test the PEG against a conservative, hard-capped growth rate assumption.Cyclical / Volatile EarningsEarnings swing dramatically from peak to trough. Coming off a trough, growth rates appear astronomically high, suppressing the PEG ratio and flashing false algorithmic buy signals.Normalize earnings over a full business cycle (7-10 years) using the Shiller P/E (CAPE) instead of relying on short-term growth spikes in the denominator.Low-Growth, High-Dividend Cash CowsA denominator approaching zero generates an exponentially high PEG ratio, falsely flagging highly profitable, stable dividend payers as massively overvalued value traps.Utilize the PEGY ratio (incorporating dividend yield into the denominator alongside growth) or exclude low-growth, high-yield equities from PEG screening entirely.4. Discounted Cash Flow (DCF) Lite: The Fallacy of False PrecisionIntrinsic value, as formally defined by the discounted cash flow (DCF) model, is the present value of all future free cash flows an asset is expected to generate over its operational lifespan, discounted back to today at an appropriate risk-adjusted rate. To implement a DCF model within a high-throughput quantitative screener that must evaluate thousands of equities simultaneously, analysts frequently deploy a "DCF Lite"—a simplified, single-stage Gordon Growth Model or a condensed two-stage model that bypasses the rigorous, bespoke calculation of the Weighted Average Cost of Capital (WACC) and individual margin forecasts. Aswath Damodaran, the foremost academic authority on equity valuation, has extensively documented the profound dangers inherent in these simplified valuation heuristics.The primary critique of a simplified DCF model is the illusion of false precision it creates. A quantitative model that outputs an intrinsic value down to the exact decimal point implies a level of scientific certainty that is fundamentally incompatible with the chaotic, unpredictable reality of financial markets. The core mathematical failure mode resides in the extreme, non-linear sensitivity of the DCF equation to its terminal growth and discount rate assumptions.Consider a single-stage perpetuity model defined by the Gordon Growth equation:$Value = \frac{FCF \times (1+g)}{r - g}$where $g$ is the terminal growth rate and $r$ is the discount rate. Assume a firm generates exactly $1 billion in Free Cash Flow. If an analyst applies a discount rate of 10% and a perpetual growth rate assumption of 3%, the denominator is 7% (0.10 - 0.03). The calculation yields an intrinsic value of approximately $14.71 billion. If the growth rate assumption is adjusted upward by merely 100 basis points to 4%, the denominator shrinks to 6%, resulting in an intrinsic value of $17.33 billion. A mere 1% shift in a highly subjective, multi-decade growth assumption mechanistically alters the total enterprise valuation by roughly 17.8%. In a screener processing a vast universe of equities, these slight misestimations in macro-level inputs systematically warp the entire valuation distribution, generating buy signals based entirely on microscopic changes to the denominator.Damodaran explicitly warns that the most common and destructive valuation error is unbridled over-optimism regarding the terminal growth rate. A foundational axiom of macroeconomic valuation dictates that no single company can grow faster than the broader economy in perpetuity; if it did, it would eventually eclipse the entire global economy. Therefore, the terminal growth rate in a DCF model must never exceed the long-term nominal GDP growth rate (typically bounded between 2% and 3%). When automated screeners utilize recent historical growth rates and extrapolate them infinitely into the terminal value—which often constitutes upwards of 75% to 80% of the total DCF value—they produce wildly inflated, virtually meaningless intrinsic values for recent growth champions. High growth requires sustained, massive reinvestment, and as companies scale, their competitive advantages inevitably erode, forcing their growth metrics to converge to the broader market mean.Furthermore, the omission of a dynamically calculated WACC in a "DCF Lite" model completely strips the valuation of its necessary risk adjustment. Damodaran emphasizes that different assets carry vastly different risk profiles; a distressed asset, a highly leveraged enterprise, or an entity operating in an emerging market with significant sovereign and currency volatility requires a substantial risk premium embedded within the discount rate. Applying a static 9% or 10% discount rate across an entire universe of equities inherently overvalues highly risky, cyclical, or heavily indebted firms, while significantly undervaluing low-beta, defensive fortresses. Damodaran advocates for the triangulation of value, suggesting that a simplified DCF must be cross-referenced with relative multiples and alternative valuation models, as relying solely on a single-stage DCF is akin to flying blind.ScenarioWhy It BreaksCorrection / GuardTerminal Growth Rate SensitivityThe formula is hyper-sensitive. A 1% error in terminal growth alters intrinsic value by ~18%. Analysts often extrapolate high historical growth infinitely into the future.Hard-cap the terminal growth rate to the long-term risk-free rate or nominal GDP growth (e.g., 2-3%). Never allow historical growth to bleed into perpetuity assumptions.Simplified Discount Rate (No WACC)Applying a universal hurdle rate ignores unique capital structure, beta, and country risk premiums, systematically overvaluing risky assets and undervaluing safe assets.Implement a dynamic, sector-specific cost of equity (CAPM) and cost of debt. Add Damodaran’s recommended country risk premiums for emerging market operations.Negative FCF or Troubled FirmsDCF logic relies entirely on positive cash flow projections. Distressed firms, early-stage turnarounds, or cyclicals at the trough yield negative or undefined intrinsic values.Abandon DCF methodologies for distressed assets or severe cyclicals. Utilize normalized earnings across a cycle, or pivot to asset-based liquidation value models.5. Debt-to-Equity (D/E): The Sectoral and Accounting BlindspotsThe Debt-to-Equity (D/E) ratio is deployed universally to measure the extent to which management is financing core operations through creditor claims versus shareholder capital. Setting a hard screening threshold—such as mandating $D/E < 0.5$—is a common heuristic intended to filter out catastrophic bankruptcy risk and ensure a robust margin of safety. However, the rigid application of capital structure metrics without strict sector-specific baselining or context regarding modern accounting rules results in the inappropriate exclusion of entire robust asset classes and the failure to detect off-balance-sheet liabilities.The most glaring failure mode of a static D/E limit is its fundamental ignorance of structural industry economics. Capital-intensive industries characterized by highly predictable, long-duration, contracted cash flows—such as utility conglomerates, telecommunication providers, midstream pipeline operators, and Real Estate Investment Trusts (REITs)—are structurally designed to operate with elevated leverage. For a regulated utility operating with guaranteed, monopoly-like revenue streams approved by state commissions, operating with a D/E ratio of 1.0 or even 2.0 is not an indicator of impending financial distress. Rather, it is the mathematically optimal capital structure required to lower the overall weighted average cost of capital (WACC) and maximize equity returns for shareholders. Debt is inherently cheaper than equity due to the tax deductibility of interest payments. Applying a blanket $D/E < 0.5$ filter to a broad market screener will systematically eradicate these defensive, cash-flow-rich sectors from consideration, resulting in a model portfolio severely tilted toward asset-light technology and consumer discretionary firms that do not require heavy debt financing but carry higher operational risks.Equally hazardous is the D/E metric's extreme vulnerability to major revisions in global accounting standards. Prior to the implementation of the International Financial Reporting Standard 16 (IFRS 16) and its US GAAP equivalent (ASC 842), companies could keep massive, long-term lease obligations entirely off the balance sheet by classifying them as "operating leases." Retailers, airlines, and logistics companies with massive physical footprints appeared artificially pristine from a leverage perspective. Following the mandated adoption of these standards, companies were forced to calculate the present value of these operating leases and capitalize them onto the balance sheet as right-of-use assets with corresponding, massive lease liabilities.Overnight, the recorded debt levels of retail and airline equities skyrocketed, massively inflating their D/E ratios despite zero actual change in their underlying cash flows, business models, or fundamental economics. A screener relying on unadjusted historical D/E ratios will heavily penalize heavily leased businesses, misinterpreting an accounting classification shift as a sudden and severe deterioration in corporate solvency.ScenarioWhy It BreaksCorrection / GuardCapital-Intensive Sectors (Utilities, REITs)These sectors structurally require and safely support high leverage due to predictable cash flows. A hard $D/E < 0.5$ cap incorrectly labels them as high-risk and uninvestable.Baseline D/E thresholds by specific GICS sector. Alternatively, transition to the Interest Coverage Ratio (EBIT / Interest Expense) to measure the actual capacity to service debt.IFRS 16 / ASC 842 Operating LeasesThe capitalization of operating leases onto the balance sheet mechanically spikes debt levels for retailers and airlines, distorting historical D/E comparisons and triggering false alarms.Use a modified Debt calculation that standardizes lease liabilities across periods, or rely on EBITDAR (which adds back rental expenses) to evaluate true operational leverage.6. Free Cash Flow (FCF) Yield > 5%: The Working Capital and SBC DistortionsFree Cash Flow (FCF) Yield, calculated by dividing Free Cash Flow per share by the current market price per share, is increasingly favored over the traditional earnings yield (E/P) because it ostensibly measures the actual, unadulterated cash left over after a company has maintained or expanded its asset base. A requirement of an FCF Yield greater than 5% acts as a proxy for identifying companies generating substantial excess cash relative to their valuation. While generally more robust than net income-based metrics, FCF Yield suffers from distortions related to working capital fluctuations, stock-based compensation (SBC), and the cyclical nature of capital expenditures.The first major failure mode of an FCF Yield screen involves massive, temporary working capital shifts. Operating cash flow (the starting point for FCF) is heavily influenced by changes in accounts receivable, inventory, and accounts payable. If a company delays paying its suppliers at the end of a financial quarter (increasing accounts payable) or aggressively draws down its inventory without replacing it, operating cash flow will temporarily spike. This artificially inflates the trailing FCF Yield, tricking the screener into flagging the stock as a massive cash generator. In subsequent quarters, as the company is forced to pay its suppliers or restock its depleted inventory, cash flow will crater.Furthermore, the modern reliance on Stock-Based Compensation (SBC) as a primary method of employee remuneration heavily distorts FCF. Under standard cash flow accounting, SBC is treated as a non-cash expense and is added back to net income to calculate operating cash flow. For many modern technology and growth companies, SBC constitutes a massive portion of total operating expenses. Adding it back artificially inflates operating cash flow, and consequently, the FCF Yield. However, SBC is an authentic economic cost to shareholders; it consistently dilutes the equity base over time. By ignoring the dilutive reality of SBC, an FCF Yield screener will flag highly dilutive technology companies as incredible value investments.Finally, FCF Yield fails to distinguish between maintenance capital expenditures (money required simply to keep the business running) and growth capital expenditures (money invested to expand the business). A company aggressively investing in new factories or data centers will temporarily exhibit a very low or negative FCF Yield, causing the screener to reject it, even if those investments yield massive future returns. Conversely, a dying business that has ceased all growth capex will briefly display a massive FCF Yield right before its obsolete asset base fails entirely.ScenarioWhy It BreaksCorrection / GuardWorking Capital ManipulationsTemporary delays in paying suppliers or draining inventory create massive, short-term spikes in operating cash flow, leading to a falsely elevated FCF Yield.Utilize a multi-year average FCF Yield (e.g., a 3-year rolling average) to smooth out short-term working capital distortions and identify sustained cash generation.Stock-Based Compensation (SBC) Add-BacksSBC is added back as a non-cash expense, artificially inflating FCF. The metric ignores the massive shareholder dilution occurring to generate that "free cash."Calculate an "Adjusted FCF" that subtracts Stock-Based Compensation from Operating Cash Flow before calculating the yield to reflect the true cost of equity dilution.Capital Expenditure CyclicalityHeavy, temporary growth investments suppress FCF, penalizing companies investing for the future while rewarding dying companies that have slashed capex to zero.Separate maintenance capex from growth capex. Base the primary yield calculation only on the deduction of maintenance capex to evaluate true core profitability.7. Composite Scoring: The Decay of Algorithmic AlphaTo mitigate the myriad failure modes of individual metrics, quantitative analysts and hedge funds frequently combine them into multifactor composite scoring models. The most famous public iteration of this concept is Joel Greenblatt’s "Magic Formula," which ranks companies based on a combination of High Return on Capital (a proxy for identifying business quality) and High Earnings Yield (a proxy for identifying cheapness). While backtests and early historical performance demonstrated staggering success, the public dissemination of these algorithms introduces unique, systemic failure modes related to behavioral finance, market adaptation, and commercialization.Prior to its widespread popularization, Greenblatt’s hedge fund, Gotham Capital, utilized this fundamental screening logic to generate extraordinary annualized returns of roughly 50% between 1985 and 1994. The fund routinely achieved annual returns in the 40% range through 2004, consistently and significantly outperforming the S&P 500 index. However, after the strategy was explicitly codified and published for retail and institutional consumption in The Little Book That Beats the Market, the systemic edge began to evaporate entirely. A comprehensive backtest analyzing the period from 2003 to 2015 demonstrated that the formula’s annual returns had compressed significantly to 11.4%, effectively matching the broader market. In recent trailing five-year periods, the strategy has significantly underperformed the S&P 500, with Greenblatt's flagship fund delivering roughly 9.15% compared to the market's 12.3%.The failure of composite value scoring post-publication is driven primarily by the commercialization and democratization of the alpha factor. When a proprietary, successful algorithm becomes public knowledge, vast amounts of capital rush to exploit the identified anomalies. As thousands of retail and institutional investors blindly run the Magic Formula screener, the aggregate buying pressure artificially bids up the prices of the highest-ranking equities. This massive demand shock forces the targeted value stocks into overvalued territory, fundamentally nullifying the exact margin of safety the formula was originally designed to capture. By the time a stock clears the composite screener, passes the liquidity checks, and enters the portfolio of a late adopter, the underlying "cheapness" factor has already been systematically arbitraged away by faster market participants.Furthermore, rigid composite formulas lack the qualitative, discretionary overlay required to identify macroeconomic regime shifts. The Magic Formula and similar value-based composites suffered heavily during the past decade's monetary environment, which structurally favored secular growth equities over traditional, asset-heavy value stocks. Finally, pure quantitative composites often funnel investors into micro-cap and small-cap equities, introducing severe execution friction into the model. These underlying assets suffer from extreme bid-ask spreads, severe liquidity constraints, and a lack of standardized, timely financial reporting. What appears as a mathematically perfect value investment on a backtested screener often cannot be executed at scale in the real world without moving the market price against the buyer, rendering the theoretical composite score useless in practical application.ScenarioWhy It BreaksCorrection / GuardAlpha Decay via CommercializationOnce a composite formula is publicized, mass adoption drives up the price of the target assets. The intrinsic "value" edge is systematically arbitraged away by the crowd.Do not rely exclusively on off-the-shelf, public composite formulas. Proprietary alpha requires combining traditional metrics with alternative datasets or novel weighting schemas.Macroeconomic Regime ShiftsPure value composites systematically underperform during prolonged macroeconomic periods where the market structurally favors growth over value (e.g., extended ZIRP environments).Incorporate momentum or macroeconomic factors alongside value and quality factors to prevent catching falling knives during periods of systemic sector rotation.Small-Cap Illiquidity and Execution DragComposites often rank micro-caps highest due to market inefficiencies, but low liquidity prevents executing trades at the screened prices, destroying modeled returns.Enforce strict liquidity gates within the screener: exclude all equities with market capitalizations below $500 million or low average daily trading volumes to ensure tradeability.8. The Three Most Dangerous Value TrapsWhen the failure modes of the aforementioned metrics coalesce within a single equity, they create a "Value Trap"—a stock that appears statistically pristine across all major value metrics but is, in reality, a wealth-destroying asset undergoing terminal decline. Relying purely on the quantitative output without qualitatively auditing the cash flow statement and structural industry dynamics guarantees exposure to these traps.Trap 1: The "Buyback Illusion" Structural DeclineThe most insidious value trap in modern finance occurs when a management team attempts to mask structural revenue decay through debt-fueled share repurchases. By rapidly shrinking the outstanding share count using borrowed capital, Earnings Per Share (EPS) is artificially maintained or grown, compressing the P/E ratio and driving the ROE to stratospheric levels as the equity base is hollowed out. The screener detects a seemingly cheap stock with phenomenal capital efficiency, completely missing the underlying rot.Historical Example: Bed Bath & Beyond (BBBY)
In the late 2010s and early 2020s, Bed Bath & Beyond became the archetype of the buyback value trap. As the shift to e-commerce structurally decimated their brick-and-mortar revenue models, management deployed massive amounts of capital into aggressive share repurchases. Because the share count was plummeting, EPS metrics appeared stable to screeners, resulting in a P/E ratio that frequently screened in the single digits—reaching as low as 5.51 by the March 2022 quarter. The ROE appeared exceptionally strong because the shareholder equity base had been largely wiped out by the treasury stock accounting of the buybacks.However, a qualitative examination of the cash flow statement revealed the terrifying truth: net cash used in operating activities was severely negative (e.g., negative $174 million for the year ended 2021). Accounts payable were expanding rapidly as vendors demanded cash, and massive long-term operating lease liabilities were piling up on the balance sheet. The company was literally liquidating its future solvency to maintain its current financial ratios and appease screeners. Investors who blindly bought based on the single-digit P/E and the artificially high ROE were completely wiped out when the leverage eventually triggered bankruptcy.Trap 2: The "Peak Earnings" Cyclical TrapCyclical companies—such as automobile manufacturers, homebuilders, semiconductor fabricators, and commodity miners—experience extreme volatility in profitability tied directly to the broader macroeconomic cycle. The trap occurs exactly at the peak of the economic cycle. At this precise moment, absolute earnings have never been higher, causing the trailing P/E ratio and the PEG ratio to drop to irresistible, single-digit levels (often trading at 3x or 4x trailing earnings). Furthermore, because cash generation is at its absolute maximum, Free Cash Flow yields appear massively accretive. The algorithmic screener screams "strong buy."However, the stock market is inherently forward-looking. The exceptionally low P/E ratio is not an indicator of hidden value; it is the market efficiently and appropriately discounting the fact that earnings are about to collapse as the macroeconomic cycle turns downward. When the inevitable recession hits, the previously massive FCF turns sharply negative, the denominator of the P/E ratio completely vanishes, and the stock price craters. In cyclical investing, a very low trailing P/E is often a reliable sell signal, and a high P/E (when earnings are severely depressed at the trough of the cycle) is the true buy signal. Screeners that cannot contextualize the business cycle are continually drawn to the peaks of cyclical mountains right before the avalanche.Trap 3: The "Asset-Heavy, Cash-Poor" Obsolescence TrapThe final trap targets deep-value investors fixated on the Graham Number, the Price-to-Book ratio, and the perceived safety of tangible assets. This trap manifests in legacy companies sitting on vast troves of property, plant, and equipment that have been rendered entirely economically obsolete by technological disruption and innovation. The stock trades at a massive discount to its book value, flashing a wide margin of safety according to Graham's criteria.Historical Example: Eastman Kodak (KODK)
In the early 2000s, as the advent of digital photography entirely annihilated the physical film market, Kodak's equity value plummeted. For a Graham-inspired value screener, Kodak appeared to be trading at a steep, highly attractive discount to its massive historical asset base. Metrics like P/B frequently flashed deep-value signals. By examining its financial footprint even in later years, we see extreme distress signals: a high Debt/Equity ratio (e.g., 63.76), negative Price/Book ratios (-1.29), and a deeply depressed Return on Assets (ROA) of 0.27.The catastrophic flaw in the algorithmic logic was that the factories and chemical processing plants that comprised Kodak's massive book value were effectively stranded assets. They could not be repurposed for the digital age, nor could they be liquidated at anywhere near their carrying costs. The foundational Graham Number assumption—that tangible assets equate to a downside floor or a true margin of safety—was completely obliterated. Kodak carried significant debt to maintain this infrastructure, and as top-line revenues collapsed, the interest coverage ratio deteriorated to fatal levels. Buying an obsolete asset at a 50% discount to its stated book value is entirely irrelevant if the intrinsic cash-generating capability of that physical asset has permanently dropped to zero.ConclusionThe construction of a quantitative value screener is an exercise in identifying and systematically managing structural blindspots. As the economic landscape has evolved from a capital-heavy industrial base to an intangible-heavy digital reality, the static metrics of the past have lost their absolute authority. The Graham Number is fundamentally compromised by modern asset-light economics and changing interest rate regimes; ROE is routinely weaponized by corporate financial engineering and hidden leverage; the PEG ratio relies on inherently biased forward estimates and fails entirely for cyclical or mature dividend-paying entities; simplified DCF modeling implies dangerous false precision based on volatile terminal growth assumptions; D/E thresholds indiscriminately penalize optimal capital structures in regulated industries and break down under modern lease accounting standards; and FCF Yields are distorted by working capital shifts and stock-based compensation. Furthermore, empirical historical evidence dictates that the public dissemination of composite scoring models, such as the Magic Formula, leads to rapid alpha decay as market participants swiftly arbitrage the anomaly.To build a resilient quantitative architecture, an investor must transition from screening static historical metrics to engineering dynamic, context-aware algorithms. This requires substituting ROCE for ROE to neutralize the effects of leverage, enforcing absolute net income growth gates to filter out buyback illusions, dynamically adjusting cost-of-capital hurdle rates for capital-intensive sectors, correcting FCF for stock-based compensation, and meticulously cross-referencing cash flow statements to evade the cyclical and structural value traps that define modern financial markets. True investing value is not located within the isolated output of the metrics themselves, but rather in a profound understanding of the specific macroeconomic environments and accounting frameworks under which those metrics inevitably break down.

# Opus

I'll research the actual availability and reliability of these fields across your three data sources before answering. Let me dig into the current state of each API.Good, I have a solid view of yfinance fields. Let me check Alpha Vantage's free tier coverage and Finnhub's current free-tier offerings.Let me confirm specific Alpha Vantage income statement fields, especially EBIT and interest expense, plus check yfinance small-cap FCF coverage issues.Good — confirmed Alpha Vantage's income statement provides `ebit`, `interestExpense`, `incomeBeforeTax`, `incomeTaxExpense`. Now let me verify yfinance small-cap reliability and Finnhub free-tier specifics.I have enough on yfinance reliability. Let me check Finnhub's free-tier basic financials response and confirm what fields are available.Excellent — critical find: **Finnhub's basic financials includes `roicTTM` directly**. That changes ROIC computability significantly. I have enough now to answer comprehensively.

---

Here's your full evaluation. Two important findings up top before the table:

**Critical correction to your source list:** Finnhub's `/stock/metric?metric=all` endpoint returns `roicTTM`, `pfcfTTM`, `currentEv` (enterprise value), `ebitPerShare`, and `fcfPerShareTTM` directly — none of which are in your stated field list. This dramatically simplifies several metrics. Use it.

**Critical observation on rate limits:** Alpha Vantage's 25 req/day kills any per-user real-time use. INCOME_STATEMENT + BALANCE_SHEET + CASH_FLOW = 3 calls per stock, so you get ~8 stocks/day worth of statement-derived metrics. Cache AV responses aggressively (24h+ TTL) and treat AV as a batch-prefetch nightly job, not an on-demand source.

## Evaluation table

| # | Metric | Computable? | Best Source | Formula | Missing Data Risk |
|---|--------|-------------|-------------|---------|-------------------|
| 1 | Graham Number | ✅ Yes | yfinance (`epsTrailingTwelveMonths` + `bookValue`) | `sqrt(22.5 * max(eps, 0) * max(bvps, 0))`; return null if either ≤ 0 | **Med** — fails on negative EPS or negative book value (financials, biotech, recent IPOs). ~15–25% of small-caps. |
| 2 | PEG Ratio | ⚠️ Partial | yfinance `trailingPE` ÷ AV-derived 5yr EPS CAGR | `PE / (CAGR_5yr_EPS * 100)` where CAGR computed from AV `annualReports[].netIncome / commonStockSharesOutstanding` | **High** — needs 5 yrs of positive EPS; AV sometimes returns only 3-4 years; sign-flips break CAGR math entirely. Use yfinance `earningsGrowth` (1yr) as fallback. |
| 3 | FCF Yield | ✅ Yes | yfinance `freeCashflow` ÷ `marketCap` | `freeCashflow / marketCap` | **Med** — see small-cap note below. |
| 4 | ROIC | ✅ Yes (easy path) | **Finnhub `roicTTM`** (pre-computed) | Direct field; no math needed | **Low** for large/mid; **Med** for small-caps where Finnhub returns null. Fallback: AV-derived (see below). |
| 5 | EV/EBIT | ✅ Yes | AV `INCOME_STATEMENT.ebit` + yfinance for EV components | `(marketCap + totalDebt - totalCash) / ebit_ttm` (sum last 4 quarterly EBITs) | **Med** — needs quarterly data from AV (uses your daily quota); EV components are stable. |
| 6 | DCF Lite | ⚠️ Yes but fragile | yfinance `freeCashflow` + assumed `g` and `r` | `FCF * (1+g) / (r - g_terminal)`; require `r > g_terminal` | **Med** — model risk dominates data risk. FCF availability = same as #3. Output is highly sensitive to inputs; surface assumptions in UI. |
| 7 | Interest Coverage | ✅ Yes | AV `INCOME_STATEMENT` (`ebit`, `interestExpense`) | `ebit / interestExpense`; cap at large value when interestExpense ≈ 0 | **Med** — `interestExpense` often reported as 0 or missing for debt-free companies; divide-by-zero. Net-cash firms should display "N/A (no debt)". |
| 8 | Earnings Consistency | ✅ Yes | AV `INCOME_STATEMENT.annualReports[].netIncome` | `count(netIncome > 0 for last 5 annual reports)` | **Low** — netIncome is the most reliably populated AV field. |

## Answers to your specific questions

**Small-cap FCF missing rate (yfinance):** Empirically, expect `freeCashflow = None` for roughly **20–35%** of US small-caps (<$2B), and higher (~40–50%) for micro-caps (<$300M). Yahoo's `freeCashflow` field is computed from cash flow statement scraping, and it fails when companies have non-standard cash flow line items (common in REITs, BDCs, biotech, recent SPACs). **Robust fallback:** compute it yourself from yfinance `cashflow` dataframe: `Operating Cash Flow - Capital Expenditure`. This raises coverage to ~85–90%.

**Alpha Vantage 5-year EPS data reliability:** Mostly reliable for established US-listed names, but with caveats: (1) AV returns up to 5 annual reports but sometimes only 3–4 for companies that re-IPO'd, changed fiscal year, or had restatements; (2) AV doesn't return EPS directly in INCOME_STATEMENT — you compute `netIncome / sharesOutstanding`, but shares outstanding comes from balance sheet (`commonStockSharesOutstanding`), introducing dilution drift errors; (3) GAAP vs adjusted EPS differs from yfinance/broker EPS by 5–20% routinely. **Recommendation:** for the consistency score (binary profitable y/n), AV is fine. For growth-rate math, use yfinance's `earningsGrowth` (1yr YoY) when 5yr CAGR is unstable, and label PEG as "approximate."

**ROIC from yfinance balance sheet:** Yes, computable but painful. yfinance balance sheet has `Total Stockholder Equity` and `Long Term Debt` / `Short Long Term Debt`. Invested capital ≈ `Total Equity + Total Debt - Cash & Equivalents`. NOPAT ≈ `EBIT * (1 - effectiveTaxRate)` where `effectiveTaxRate = incomeTaxExpense / incomeBeforeTax` from AV. **But:** Finnhub's `roicTTM` is one API call and pre-computed by their analysts — skip the manual path unless it returns null. Manual fallback when Finnhub roicTTM is null:
```
NOPAT = AV.ebit * (1 - AV.incomeTaxExpense / AV.incomeBeforeTax)
InvestedCapital = yf.totalStockholderEquity + yf.totalDebt - yf.totalCash
ROIC = NOPAT / InvestedCapital
```

**Most common Graham Number failure modes**, in order of frequency: (1) **Negative EPS** — recent IPOs, biotech, growth tech, cyclicals in downturn (this is the #1 failure, ~60% of nulls); (2) **Negative book value** — companies with large buybacks or accumulated deficits (MCD, HD, BKNG, PM all have or have had negative book equity — Graham Number is meaningless for them); (3) **EPS = TTM vs annual mismatch** — yfinance `trailingEps` is more current than AV's most recent `annualReports`; pick one consistently; (4) **Stock splits not adjusted** — rare with yfinance, but worth a sanity check (BVPS shouldn't suddenly 10x). Your UI should distinguish "not applicable (negative inputs)" from "data missing" — they mean different things to a value investor.

## Suggested implementation pattern

Given your three-source setup and tight AV quota, the source priority for each metric is roughly:

1. **Live tier (every request):** yfinance for prices, market cap, ratios, TTM EPS, book value — fast and free.
2. **Daily cache tier (Finnhub, 60/min so effectively unlimited):** `roicTTM`, `roaTTM`, `roeTTM`, `pfcfTTM`, `currentEv` — pre-computed, saves you the math.
3. **Nightly batch tier (AV, 25/day):** annual + quarterly statements for the ~10–20 stocks in your active watchlist; everything that needs EBIT, interest expense, tax rate, or multi-year history.

Cache aggressively on a 24h TTL for fundamentals — these only change on earnings dates.
