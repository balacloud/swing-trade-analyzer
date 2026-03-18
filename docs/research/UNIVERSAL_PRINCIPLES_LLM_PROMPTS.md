# Multi-LLM Research: Universal Swing Trading Principles

**Created:** 2026-03-18 (Day 69)
**Purpose:** Before pivoting from a Minervini-specific system to universal trading principles, validate our planned architecture changes with external LLMs.
**Context:** We have a working swing trade analyzer built primarily on Minervini/O'Neil methodology. A 3-LLM audit revealed the system is ~70% practitioner-specific and ~30% quant-standard. We want to broaden the lens WITHOUT over-engineering.

**Workflow:**
1. Copy each prompt below into GPT, Perplexity, and Gemini
2. Collect responses
3. Bring back to Claude for synthesis before writing any code

| Prompt | Topic | Best LLM |
|--------|-------|----------|
| 1 | Binary Gating vs Factor Scoring for Swing Trading | Perplexity (academic research) |
| 2 | Universal Factor Set for Swing/Position Trading | GPT Deep Research or Perplexity |
| 3 | Mean-Reversion: When and How for Swing Traders | Perplexity |
| 4 | Regime-Adaptive Parameters in Trading Systems | Any |
| 5 | What Separates Successful Quant Systems from Failures | GPT or Gemini |

---

## PROMPT 1: Binary Gating vs Continuous Factor Scoring

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed. State what evidence would confirm it.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but framed in a way that leads to wrong conclusions.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found. State what benchmark, paper, or test would resolve it.
- [HALLUCINATED — FLAG: <why fabricated>]: The claim has no basis and likely was invented. Explain the tell.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Is the claim directionally consistent with established principles but uncited? → [PLAUSIBLE]
3. Is the claim partially true but misleadingly framed? → [MISLEADING]
4. Is the claim unconfirmable without a specific test or paper? → [UNVERIFIED]
5. Does the claim contain fabricated specifics (fake benchmarks, fake paper names, invented APIs)? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---

## SYSTEM UNDER RESEARCH: Binary Gating vs Continuous Factor Scoring for Swing Trading

### Context
I have a working swing trading system (5-30 day holding period, US equities).
Currently it uses a BINARY GATING approach: 9 criteria must ALL pass for a
trade signal (e.g., Price > 50 SMA > 200 SMA, ADX ≥ 20, RS ≥ 1.0, R:R ≥ 2:1,
etc.). If any single criterion fails, no trade.

I'm considering switching to a CONTINUOUS FACTOR SCORING approach: each factor
produces a 0-100 score, scores are weighted into a composite, stocks are RANKED
by composite score, and the top N are trade candidates.

### CLAIMS TO AUDIT (answer each with verdict label):

1. **"Binary pass/fail filters produce inferior risk-adjusted returns compared
   to continuous factor scoring with ranking."**
   Is there published research comparing binary gating vs continuous scoring
   head-to-head in systematic trading? What does the evidence actually say?

2. **"The optimal approach is hybrid: binary filters as a FIRST PASS to
   eliminate clearly bad stocks, then RANK the survivors by factor score."**
   Is this hybrid approach documented in academic or practitioner literature?
   What do AQR, Two Sigma's published research, or factor investing literature say?

3. **"Fama-French and AQR factor research applies to swing timeframes (5-30 days)."**
   Most factor investing research focuses on monthly or quarterly rebalancing.
   For 5-30 day holding periods, do the same factors (momentum, value, quality)
   still have predictive power? Are there factors that work BETTER at shorter horizons?

4. **"A system producing ~1 trade per week (238 trades over 4 years) has
   adequate signal frequency for a swing trading system."**
   What does research say about the relationship between signal selectivity
   and system robustness? Is there an optimal "trades per year" range?

5. **"Day-to-day rankings by composite factor score are stable enough to
   trade on without requiring rank persistence filters."**
   How stable are factor rankings day-to-day? Do quant systems typically
   require a stock to maintain its rank for N days before acting?
   What's the research on "rank persistence" as a quality filter?

6. **"Factor weights (e.g., 40% momentum, 30% trend, 20% quality, 10% sentiment)
   can be determined from historical optimization without overfitting."**
   How do quant researchers determine robust factor weights?
   What methods prevent overfitting the weights to historical data?
   (Equal weighting? Cross-validation? Bayesian priors?)
```

---

## PROMPT 2: Universal Factor Set for Swing/Position Trading

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Is the claim directionally consistent with established principles but uncited? → [PLAUSIBLE]
3. Is the claim partially true but misleadingly framed? → [MISLEADING]
4. Is the claim unconfirmable without a specific test or paper? → [UNVERIFIED]
5. Does the claim contain fabricated specifics? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---

## SYSTEM UNDER RESEARCH: Universal Factor Set for Swing Trading

### Context
I'm redesigning a swing trading system (5-30 day US equities) to use
universal, evidence-based factors instead of methodology-specific rules
(currently Minervini/O'Neil focused).

**Current factors (Minervini-derived):**
- Trend: Price > 50 SMA > 200 SMA (Stage 2)
- Momentum: 52-week RS vs SPY ≥ 1.0
- Pattern: VCP, Cup & Handle, Flat Base detection
- Quality: ROE > 15%, Revenue Growth > 10%, D/E < 1.0
- Volatility: ADX ≥ 20
- Sentiment: CNN Fear & Greed 60-80
- Risk: VIX < 20 + SPY > 200 SMA

### CLAIMS TO AUDIT (answer each with verdict label):

1. **"The top factors with strongest empirical evidence for 5-30 day equity
   returns are: cross-sectional momentum, short-term reversal, earnings
   momentum, volatility, liquidity, and market regime."**
   For each factor listed: name the key paper(s) with DOI or title, report
   the Sharpe or information ratio if available, and state whether the alpha
   has decayed post-2015. If a factor is NOT well-evidenced at swing
   timeframes, say so.

2. **"For swing trading, 12-1 momentum (12-month return minus last month)
   is the best momentum measure."**
   We currently use 52-week RS vs SPY. Alternatives: 1-month, 3-month,
   6-month, 12-1 (Jegadeesh & Titman style), ROC variants.
   Which has the best evidence specifically for 5-30 day forward returns?

3. **"Chart patterns (VCP, Cup & Handle) should be treated as a separate
   factor in a composite scoring system, not as a binary filter."**
   In a factor-based framework, does research support pattern detection as:
   (a) A scored factor, (b) A binary filter, or (c) Dropped entirely in
   favor of pure quantitative momentum/trend factors?

4. **"Fundamental quality metrics (ROE, Revenue Growth, D/E) add meaningful
   predictive value to swing trades beyond pure technical factors."**
   For 5-30 day holding periods, does adding fundamental quality to technical
   momentum improve returns? Or do fundamentals only matter at longer horizons?

5. **"The CNN Fear & Greed Index is an adequate sentiment input for a swing
   trading system."**
   What sentiment indicators have stronger empirical backing for short-term
   trading? Audit each: put/call ratio, VIX term structure, short interest,
   social media sentiment, options flow, insider transactions. Which have
   published research supporting predictive power at swing timeframes?

6. **"SPY > 200 SMA + VIX levels is the best regime detection method for
   swing trading."**
   Compare to alternatives: HMM, breadth indicators (% stocks > 200 SMA),
   yield curve, volatility regime clustering. What regime detection approach
   has the best evidence for improving swing trade selection?

7. **"Our momentum and trend factors are too correlated and one should be
   dropped or they should be combined."**
   Momentum (52-week RS) and trend (Price > 50 > 200 SMA) likely overlap.
   How should we test for and handle factor correlation? Should correlated
   factors be combined into one, or does keeping both add value?
```

---

## PROMPT 3: Mean-Reversion for Swing Traders

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Directionally consistent but uncited? → [PLAUSIBLE]
3. Partially true but misleading? → [MISLEADING]
4. Unconfirmable without a specific test? → [UNVERIFIED]
5. Contains fabricated specifics? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---

## SYSTEM UNDER RESEARCH: Mean-Reversion Strategy for Swing Trading

### Context
Our swing trading system is 100% momentum/trend-following. In range-bound
or choppy markets, it produces ZERO signals (by design — ADX < 20 kills
everything). We want to understand whether adding a mean-reversion strategy
is evidence-based or just adds complexity.

### CLAIMS TO AUDIT (answer each with verdict label):

1. **"Mean-reversion strategies work best in range-bound/low-volatility
   markets, while momentum works best in trending/high-dispersion markets."**
   What does published research say about regime-conditional strategy
   selection? How do you reliably detect when to switch?

2. **"RSI < 30 oversold bounces are a proven mean-reversion entry for
   swing trading US equities."**
   What RSI threshold is best evidenced? Are RSI-based mean-reversion
   strategies robust post-2015, or has the edge decayed?

3. **"Bollinger Band mean-reversion (buy at lower band, sell at upper)
   has empirical evidence of edge in swing timeframes."**
   Is this verified or just popular? What does the academic literature say?

4. **"Mean-reversion trades should use different risk parameters than
   momentum trades: tighter stops, lower R:R, time-based exits."**
   Is there published evidence that mean-reversion and momentum strategies
   require fundamentally different risk management approaches?

5. **"Running momentum and mean-reversion simultaneously in one system
   improves risk-adjusted returns through strategy diversification."**
   How do published multi-strategy systems allocate between momentum
   and mean-reversion? Regime-based switching vs running both in parallel?

6. **"Mean-reversion systems have 60-70% win rates with smaller average
   wins, while momentum systems have 50-55% win rates with larger wins."**
   Is this characterization accurate? What does research show for
   swing-timeframe strategies specifically?

7. **"Connors RSI or the DV2 indicator represents the simplest
   evidence-based mean-reversion approach for US equities."**
   What is the SIMPLEST mean-reversion strategy with published evidence
   of edge over the last 10-20 years? Is it still working?
```

---

## PROMPT 4: Regime-Adaptive Parameters

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Directionally consistent but uncited? → [PLAUSIBLE]
3. Partially true but misleading? → [MISLEADING]
4. Unconfirmable without a specific test? → [UNVERIFIED]
5. Contains fabricated specifics? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---

## SYSTEM UNDER RESEARCH: Regime-Adaptive Parameter Tuning

### Context
Our swing trading system uses FIXED parameters regardless of market regime:
- Stop loss: always 7% or 2x ATR
- RS threshold: always ≥ 1.0
- ADX threshold: always ≥ 20
- Holding period weights: always 70/30 or 50/50

We're considering making these regime-adaptive.

### CLAIMS TO AUDIT (answer each with verdict label):

1. **"Varying strategy parameters based on market regime (e.g., VIX level)
   improves risk-adjusted returns vs fixed parameters."**
   Is there published evidence for regime-adaptive parameter tuning
   in equity trading systems? Or does it mainly add overfitting risk?

2. **"Stop loss distance should adapt to volatility: wider in high-vol,
   tighter in low-vol (ATR-based stops naturally do this)."**
   Does research support volatility-scaled stops over fixed-percentage stops?
   What is the evidence on ATR-based vs fixed stops for swing trading?

3. **"Position sizing is the most important parameter to adapt to regime,
   more impactful than adjusting entry/exit rules."**
   What does the evidence say about which parameter to adapt first?
   Is position sizing adaptation more robust than entry criteria adaptation?

4. **"VIX < 20 / 20-30 / > 30 is the right tiering for regime classification."**
   Should adaptation use discrete tiers, continuous scaling (f(VIX)),
   or VIX percentile rank? What does research recommend?

5. **"Momentum lookback periods should shorten in fast-moving markets
   and lengthen in slow-moving markets."**
   Is there evidence for adaptive momentum windows? Or do fixed
   lookback periods perform just as well?

6. **"More than 2-3 regime-adaptive parameters crosses into overfitting
   territory for a retail swing trading system."**
   At what point does regime adaptation become curve-fitting?
   What guardrails do researchers recommend?
```

---

## PROMPT 5: What Separates Successful Quant Systems from Failures

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Directionally consistent but uncited? → [PLAUSIBLE]
3. Partially true but misleading? → [MISLEADING]
4. Unconfirmable without a specific test? → [UNVERIFIED]
5. Contains fabricated specifics? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---

## SYSTEM UNDER RESEARCH: Building a Robust Retail Swing Trading System

### Context
I'm a retail swing trader evolving my system from a Minervini/O'Neil-specific
implementation to a more universal, evidence-based approach. I want to learn
from the FAILURES as much as the successes. My constraints: no co-location,
no real-time options flow, ~$50-100K capital, manual execution, 5-30 day holds.

### CLAIMS TO AUDIT (answer each with verdict label):

1. **"The top 5 reasons systematic trading systems fail in live trading are:
   overfitting, transaction costs, regime change, execution slippage, and
   behavioral deviation from rules."**
   Based on published research and fund performance data, are these the
   actual top 5? What does the evidence say are the REAL primary failure modes?

2. **"Walk-forward testing is sufficient to prevent overfitting."**
   Beyond walk-forward, what other anti-overfitting techniques have
   empirical support? (Cross-validation, parameter stability analysis,
   Monte Carlo simulation, minimum trade count requirements, etc.)

3. **"Simpler trading systems (fewer parameters, fewer factors) outperform
   more complex ones out-of-sample."**
   Is there evidence for a "simplicity premium" in systematic trading?
   What is the optimal complexity budget for a retail system?
   Cite studies if they exist.

4. **"For a swing system doing 1-5 trades/week in stocks with $10M+ daily
   volume, transaction costs and slippage are negligible (<5 bps per trade)."**
   What realistic slippage and cost assumptions should I use?
   Does this change for market orders vs limit orders?

5. **"Factors that worked in 2010-2020 (momentum, value, quality) continue
   to work in 2020-2026 with similar magnitude."**
   What's the evidence on factor decay in recent years? Which factors
   have weakened? Which remain robust? Has market structure evolution
   (HFT, passive investing, options growth) degraded specific edges?

6. **"A retail swing trader should NOT try to compete on: intraday mean-reversion,
   statistical arbitrage, high-frequency market making, or options flow trading
   because these require institutional infrastructure."**
   What edges are genuinely unavailable to retail? And critically —
   what edges are STILL available to retail swing traders that
   institutions can't easily exploit?

7. **"The minimum viable evidence-based swing trading system for retail is:
   2-3 factors (momentum + trend + regime filter), equal-weighted, with
   ATR-based stops and 7% max loss, rebalanced weekly."**
   If you had to design the simplest possible swing system for
   ~$50-100K capital with manual execution, what would it look like?
   Ground your answer in cited evidence, not opinion.
```

---

## After Collecting Responses

Bring all responses back to Claude and say:

```
Here are the research results from 3 LLMs on universal trading principles.
All responses used the AUDIT MODE framework with verdict labels.
Please:
1. Synthesize into a REVISED ARCHITECTURE SPEC for the Phase 2 evolution
2. Create a cross-LLM verdict matrix (like the audit synthesis)
3. Identify the MINIMUM VIABLE changes to move from narrow to universal
4. Create a specific implementation plan that preserves our existing infrastructure
5. Flag any findings that suggest we should NOT make a planned change
6. Highlight conflicts between LLMs and resolve them
```

# Groks Response 
**PROMPT 1: Binary Gating vs Continuous Factor Scoring**

> **Claim:** "Binary pass/fail filters produce inferior risk-adjusted returns compared to continuous factor scoring with ranking."  
> **Reasoning:** Step 1: Searched for direct head-to-head comparisons in systematic trading literature (binary gating/all-must-pass vs. composite scoring + ranking). No paper provides an explicit, reproducible benchmark comparing the two approaches in equity swing or systematic contexts. Step 2: Cross-sectional factor literature consistently emphasizes accurate ranking of assets (e.g., learning-to-rank algorithms improve Sharpe ratios ~3× over traditional heuristics in cross-sectional momentum strategies). Step 3: One recent deployment paper contrasts binary regime gates vs. continuous uncertainty scaling and finds binary abstention outperforms continuous modulation in regime shifts, but this is regime-level, not per-factor gating. Step 4: No citable source directly tests “9 criteria must ALL pass” vs. weighted composite ranking for 5-30 day US equity holds. Directionally consistent with quant practice (ranking avoids binary elimination of near-miss stocks), but unconfirmed for the exact claim.  
> **Verdict:** [PLAUSIBLE — REASON: Consistent with ranking emphasis in cross-sectional systematic strategies and learning-to-rank improvements; a head-to-head backtest on US equities (binary all-pass vs. composite rank, 5-30 day holds, risk-adjusted metrics) would confirm or refute.]

> **Claim:** "The optimal approach is hybrid: binary filters as a FIRST PASS to eliminate clearly bad stocks, then RANK the survivors by factor score."  
> **Reasoning:** Step 1: Searched for hybrid binary-then-rank in AQR/Two Sigma or factor literature. No direct documentation or recommendation from AQR or Two Sigma publications. Step 2: One 2026 arXiv paper on uncertainty-aware deployment uses a binary regime gate (trade/abstain) followed by position-level caps, but not per-stock binary filters then ranking. Step 3: Cross-sectional papers stress ranking as core; no evidence hybrid is “optimal” or documented as standard. Step 4: Practitioner intuition (cheap screen then rank) exists but lacks academic/practitioner citation.  
> **Verdict:** [UNVERIFIED — NEEDS: Published AQR/Two Sigma paper or reproducible benchmark showing hybrid outperforms pure ranking or pure binary on risk-adjusted returns.]

> **Claim:** "Fama-French and AQR factor research applies to swing timeframes (5-30 days)."  
> **Reasoning:** Step 1: Classic Fama-French (and AQR extensions) are constructed with monthly rebalancing; value/profitability factors decay slowly. Step 2: Momentum factor shows variants at shorter horizons (weekly/daily momentum papers exist), but short-term reversal dominates at 1-month, and full Fama-French 5-factor alphas are tested monthly. Step 3: Factor-momentum and time-series momentum papers confirm some persistence at 1-6 months, but no source states classic Fama-French factors retain identical predictive power or Sharpe at 5-30 day holds. Step 4: Swing-specific application is extrapolation, not direct evidence.  
> **Verdict:** [MISLEADING — CORRECTION: Classic monthly-rebalanced Fama-French factors do not directly apply unchanged; shorter-horizon momentum/reversal effects exist but differ in strength and require separate testing.]

> **Claim:** "A system producing ~1 trade per week (238 trades over 4 years) has adequate signal frequency for a swing trading system."  
> **Reasoning:** Step 1: Robustness literature stresses minimum trade counts (e.g., ≥50 trades in IS for statistical power; trades/day ≥5 in one walk-forward protocol) to avoid luck. Step 2: No paper defines “adequate” as exactly 1/week or 238/4 years. Step 3: Selectivity vs. robustness trade-off is discussed (fewer signals can reduce costs but risk under-diversification or overfitting to rare events), but no optimal range is established for swing systems.  
> **Verdict:** [UNVERIFIED — NEEDS: Research linking specific trades-per-year ranges to out-of-sample robustness metrics (e.g., Sharpe stability, Calmar) in equity swing systems.]

> **Claim:** "Day-to-day rankings by composite factor score are stable enough to trade on without requiring rank persistence filters."  
> **Reasoning:** Step 1: No direct research on day-to-day rank stability for composite swing factors. Step 2: Cross-sectional papers assume monthly/weekly rebalancing; daily re-rank volatility is acknowledged in high-frequency contexts but not quantified for 5-30 day swing. Step 3: Persistence filters (hold rank N days) appear in some practitioner protocols but lack cited academic backing for swing composites.  
> **Verdict:** [UNVERIFIED — NEEDS: Empirical study of daily rank autocorrelation or decay in composite momentum/trend/quality scores for US equities.]

> **Claim:** "Factor weights (e.g., 40% momentum, 30% trend, 20% quality, 10% sentiment) can be determined from historical optimization without overfitting."  
> **Reasoning:** Step 1: Quant literature uses cross-validation, walk-forward, Bayesian priors, or equal-weighting to mitigate overfitting. Step 2: No source claims arbitrary historical optimization (e.g., 40/30/20/10) is robust without guards. Step 3: Papers explicitly recommend regularization, stability tests, or priors to prevent curve-fitting.  
> **Verdict:** [MISLEADING — CORRECTION: Historical optimization alone overfits; robust methods require cross-validation/walk-forward/Bayesian shrinkage/equal weighting.]

**PROMPT 2: Universal Factor Set for Swing/Position Trading**

> **Claim:** "The top factors with strongest empirical evidence for 5-30 day equity returns are: cross-sectional momentum, short-term reversal, earnings momentum, volatility, liquidity, and market regime."  
> **Reasoning:** Step 1: Short-term momentum/reversal papers exist (e.g., Medhat et al. on 1-month momentum among liquid stocks; intraday/cross-sectional reversal studies). Earnings momentum (PEAD/SUE) is documented but very short-horizon. Volatility/liquidity have predictive roles in some short-horizon papers. Step 2: No single paper ranks exactly these six as “top” for 5-30 day US equities with post-2015 Sharpe/IR and decay analysis. Step 3: Market regime is regime-dependent, not a standalone factor.  
> **Verdict:** [PLAUSIBLE — REASON: Individual components have short-horizon evidence; a comparative paper listing Sharpe/IR/decay for precisely these six at 5-30 day holds would verify.]

> **Claim:** "For swing trading, 12-1 momentum (12-month return minus last month) is the best momentum measure."  
> **Reasoning:** Step 1: Jegadeesh & Titman (1993) established 3-12 month (often implemented as 12-1) as standard to avoid 1-month reversal. Step 2: Recent papers compare horizons; 12-1 remains widely used, but short-term momentum (1-month lagged) shows separate edge in liquid stocks. No source declares 12-1 “best” specifically for 5-30 day forward returns over 6-month/3-month/ROC variants.  
> **Verdict:** [UNVERIFIED — NEEDS: Head-to-head comparison of momentum horizons vs. 5-30 day forward returns (Sharpe, t-stats, post-2015 decay).]

> **Claim:** "Chart patterns (VCP, Cup & Handle) should be treated as a separate factor in a composite scoring system, not as a binary filter."  
> **Reasoning:** Step 1: Pattern detection appears in ML papers (SVM for Cup & Handle, kernel regression for technical patterns), but these are detection methods, not alpha-generating factors. Step 2: No academic evidence shows scored VCP/Cup & Handle adds predictive value beyond momentum/trend in composite models; Lo et al. (2000) found statistical patterns but no exploitable edge after costs. Practitioner use is binary.  
> **Verdict:** [UNVERIFIED — NEEDS: Paper showing scored pattern factor improves composite Sharpe/IR over pure quant momentum/trend at swing horizons.]

> **Claim:** "Fundamental quality metrics (ROE, Revenue Growth, D/E) add meaningful predictive value to swing trades beyond pure technical factors."  
> **Reasoning:** Step 1: Novy-Marx (2015) shows earnings momentum/ROE explains price momentum, but at quarterly horizons. Step 2: Short-term (5-30 day) literature emphasizes technical/liquidity signals; fundamentals change slowly and show weaker daily/weekly predictability. No source confirms incremental value at swing holds after controlling for price momentum.  
> **Verdict:** [UNVERIFIED — NEEDS: Regression or portfolio test showing ROE/growth/D/E alpha incremental to technical factors at 5-30 day holds.]

> **Claim:** "The CNN Fear & Greed Index is an adequate sentiment input for a swing trading system."  
> **Reasoning:** Step 1: One 2026 practitioner paper backtests it as a global trend signal with profitable long/short rules. Step 2: No academic research validates predictive power at swing horizons; index is composite of momentum/VIX/put-call etc., but components (not the index itself) have some evidence. Alternatives (VIX term structure, put/call, short interest) have scattered papers; social media/options flow/insider have limited or no swing-specific academic backing.  
> **Verdict:** [PLAUSIBLE — REASON: One backtest shows profitability; stronger academic evidence exists for VIX/put-call components, but none directly for CNN index at swing timeframes.]

> **Claim:** "SPY > 200 SMA + VIX levels is the best regime detection method for swing trading."  
> **Reasoning:** Step 1: VIX and 200 SMA are common practitioner filters. Step 2: HMM, breadth (% >200 SMA), yield curve, and volatility clustering appear in regime-detection papers; no study declares SPY 200 SMA + VIX “best” by any metric (Sharpe improvement, regime classification accuracy).  
> **Verdict:** [UNVERIFIED — NEEDS: Comparative study of regime methods (VIX tiers vs. HMM vs. breadth) on swing-system performance.]

> **Claim:** "Our momentum and trend factors are too correlated and one should be dropped or they should be combined."  
> **Reasoning:** Step 1: Momentum (52-week RS) and trend (price >50>200 SMA) overlap by construction. Step 2: Literature handles correlation via orthogonalization, PCA, or weighting; no rule mandates dropping one. Keeping both can add value if low correlation in residuals. Testing (correlation matrix, variance inflation) is standard, not automatic combination.  
> **Verdict:** [PLAUSIBLE — REASON: Overlap exists; standard practice is correlation testing + weighting/orthogonalization, not automatic drop/combine.]

**PROMPT 3: Mean-Reversion for Swing Traders**

> **Claim:** "Mean-reversion strategies work best in range-bound/low-volatility markets, while momentum works best in trending/high-dispersion markets."  
> **Reasoning:** Step 1: Regime-conditional papers (time-series momentum stronger in high-vol/trending; short-term reversal stronger in low-vol) exist. Step 2: Reliable detection (HMM, VIX, breadth) is discussed but no single “best” switch method is consensus-verified.  
> **Verdict:** [PLAUSIBLE — REASON: Consistent with regime literature; needs explicit regime-switch benchmark.]

> **Claim:** "RSI < 30 oversold bounces are a proven mean-reversion entry for swing trading US equities."  
> **Reasoning:** Step 1: RSI mean-reversion is popular; academic short-term reversal exists but not specifically RSI<30. Step 2: Post-2015 decay is widely suspected (HFT, liquidity) but no cited paper quantifies RSI threshold robustness post-2015.  
> **Verdict:** [UNVERIFIED — NEEDS: Post-2015 backtest of RSI thresholds with transaction costs on US equities.]

> **Claim:** "Bollinger Band mean-reversion (buy at lower band, sell at upper) has empirical evidence of edge in swing timeframes."  
> **Reasoning:** Step 1: Popular technical rule; no academic paper verifies net-of-cost edge at swing horizons after 2010.  
> **Verdict:** [UNVERIFIED — NEEDS: Reproducible academic or practitioner paper with post-cost Sharpe >0 for Bollinger bands on US equities.]

> **Claim:** "Mean-reversion trades should use different risk parameters than momentum trades: tighter stops, lower R:R, time-based exits."  
> **Reasoning:** Step 1: No published evidence directly compares risk parameters across strategy types for swing. Plausible due to higher win-rate/lower hold-time of mean-reversion.  
> **Verdict:** [PLAUSIBLE — REASON: Logical given strategy characteristics; requires empirical test.]

> **Claim:** "Running momentum and mean-reversion simultaneously in one system improves risk-adjusted returns through strategy diversification."  
> **Reasoning:** Step 1: Multi-strategy papers show diversification benefits; regime-switching vs. parallel allocation both appear. No swing-specific evidence.  
> **Verdict:** [PLAUSIBLE — REASON: Consistent with portfolio theory; needs swing-specific allocation study.]

> **Claim:** "Mean-reversion systems have 60-70% win rates with smaller average wins, while momentum systems have 50-55% win rates with larger wins."  
> **Reasoning:** Step 1: Typical practitioner characterization; no cited research confirms exact ranges for swing-timeframe US equities.  
> **Verdict:** [UNVERIFIED — NEEDS: Large-sample study of win-rate distributions for both strategy types.]

> **Claim:** "Connors RSI or the DV2 indicator represents the simplest evidence-based mean-reversion approach for US equities."  
> **Reasoning:** Step 1: Both are practitioner indicators (Larry Connors); no academic evidence of edge over last 10-20 years net of costs. Simplest verified short-term reversal is 1-month return sort.  
> **Verdict:** [UNVERIFIED — NEEDS: Published backtest with decay analysis for Connors RSI/DV2.]

**PROMPT 4: Regime-Adaptive Parameters**

> **Claim:** "Varying strategy parameters based on market regime (e.g., VIX level) improves risk-adjusted returns vs fixed parameters."  
> **Reasoning:** Step 1: Regime-adaptive papers exist (volatility scaling, HMM filters); overfitting risk is explicitly warned. No universal proof it “improves” without guards.  
> **Verdict:** [PLAUSIBLE — REASON: Some evidence in regime literature; needs walk-forward test vs. fixed.]

> **Claim:** "Stop loss distance should adapt to volatility: wider in high-vol, tighter in low-vol (ATR-based stops naturally do this)."  
> **Reasoning:** Step 1: ATR-based stops are standard in quant literature and naturally volatility-scale; volatility-scaled risk is supported over fixed %.  
> **Verdict:** [VERIFIED — SOURCE: Standard in quantitative trading literature (e.g., volatility-scaling in position sizing and stop literature; ATR implementation is common).]

> **Claim:** "Position sizing is the most important parameter to adapt to regime, more impactful than adjusting entry/exit rules."  
> **Reasoning:** Step 1: Kelly/volatility sizing literature emphasizes sizing as primary lever; entry/exit adaptation secondary in some papers. No direct ranking of “most important.”  
> **Verdict:** [PLAUSIBLE — REASON: Consistent with risk-management priority; no source ranks it strictly above entry rules.]

> **Claim:** "VIX < 20 / 20-30 / > 30 is the right tiering for regime classification."  
> **Reasoning:** Step 1: Common practitioner tiers; literature uses continuous VIX, percentiles, or HMM instead. No consensus “right” discrete tiers.  
> **Verdict:** [UNVERIFIED — NEEDS: Comparative performance of discrete VIX tiers vs. continuous/HMM.]

> **Claim:** "Momentum lookback periods should shorten in fast-moving markets and lengthen in slow-moving markets."  
> **Reasoning:** Step 1: Some adaptive-window papers exist; fixed lookbacks often perform comparably in robustness tests.  
> **Verdict:** [UNVERIFIED — NEEDS: Evidence that adaptive lookbacks outperform fixed in out-of-sample swing tests.]

> **Claim:** "More than 2-3 regime-adaptive parameters crosses into overfitting territory for a retail swing trading system."  
> **Reasoning:** Step 1: Overfitting guardrails (parameter stability, minimum trades, walk-forward) are recommended; no exact “2-3” threshold.  
> **Verdict:** [UNVERIFIED — NEEDS: Study quantifying overfitting risk vs. number of adaptive parameters.]

**PROMPT 5: What Separates Successful Quant Systems from Failures**

> **Claim:** "The top 5 reasons systematic trading systems fail in live trading are: overfitting, transaction costs, regime change, execution slippage, and behavioral deviation from rules."  
> **Reasoning:** Step 1: These are frequently cited in practitioner guides (e.g., Chan’s Quantitative Trading). Step 2: No single published research/fund-performance study ranks exactly these as “top 5” with data.  
> **Verdict:** [PLAUSIBLE — REASON: Matches common failure modes discussed; no source confirms exact ranking or top 5.]

> **Claim:** "Walk-forward testing is sufficient to prevent overfitting."  
> **Reasoning:** Step 1: Walk-forward is recommended but insufficient alone; additional techniques (cross-validation, Monte Carlo, parameter stability, min-trade thresholds) are required.  
> **Verdict:** [MISLEADING — CORRECTION: Walk-forward helps but must be combined with other guards.]

> **Claim:** "Simpler trading systems (fewer parameters, fewer factors) outperform more complex ones out-of-sample."  
> **Reasoning:** Step 1: Simplicity premium is discussed; optimal complexity budget for retail is not quantified in literature.  
> **Verdict:** [PLAUSIBLE — REASON: Consistent with robustness literature; no exact “simplicity premium” study for swing.]

> **Claim:** "For a swing system doing 1-5 trades/week in stocks with $10M+ daily volume, transaction costs and slippage are negligible (<5 bps per trade)."  
> **Reasoning:** Step 1: Realistic assumptions depend on order type (market vs. limit), liquidity, and broker. 5 bps often non-negligible at scale; literature stresses realistic cost modeling.  
> **Verdict:** [MISLEADING — CORRECTION: Costs/slippage are material; use realistic per-side estimates (market orders higher).]

> **Claim:** "Factors that worked in 2010-2020 (momentum, value, quality) continue to work in 2020-2026 with similar magnitude."  
> **Reasoning:** Step 1: Factor decay (especially momentum post-2009, crowding from passive/HFT) is documented. Post-2020 robustness varies; no source claims “similar magnitude.”  
> **Verdict:** [MISLEADING — CORRECTION: Decay/crowding evidence exists; magnitudes have weakened for several factors.]

> **Claim:** "A retail swing trader should NOT try to compete on: intraday mean-reversion, statistical arbitrage, high-frequency market making, or options flow trading because these require institutional infrastructure."  
> **Reasoning:** Step 1: Consensus in practitioner literature: HFT/SA/options flow need co-location, low-latency, data feeds unavailable to retail. Step 2: Retail edges (low-frequency momentum, regime filters, manual execution) remain viable.  
> **Verdict:** [VERIFIED — SOURCE: Standard in quantitative trading texts and practitioner discussions (retail infrastructure limitations documented).]

> **Claim:** "The minimum viable evidence-based swing trading system for retail is: 2-3 factors (momentum + trend + regime filter), equal-weighted, with ATR-based stops and 7% max loss, rebalanced weekly."  
> **Reasoning:** Step 1: No citable evidence defines this exact configuration as “minimum viable.” Step 2: 2-3 factors, equal weighting, ATR stops, regime filter, and weekly rebalance align with robustness principles but are not proven minimal.  
> **Verdict:** [UNVERIFIED — NEEDS: Cited backtest or study establishing this as simplest evidence-based retail system.]

All verdicts follow the required decision tree and rules. No claims were fabricated or assumed true without evidence. Where sources exist, they are real and linked via search results; most swing-specific claims lack direct academic or citable practitioner benchmarks because literature focuses on monthly or intraday horizons.

# Gemini response

Engineering Robust Alpha: A Systematic Audit of Factor-Based Selection, Regime Adaptation, and Operational Resilience in Equities Swing Trading
The transition from discretionary swing trading frameworks to fully systematic, quantitative implementations represents a paradigm shift in both risk management and capital allocation efficiency. Traditional methodologies, while providing a conceptual foundation for identifying high-momentum growth stocks, often lack the statistical rigor required to survive evolving market structures characterized by algorithmic dominance and compressed alpha cycles. This comprehensive report audits the architectural trade-offs between binary and continuous selection models, the empirical validity of universal factor sets across a 5-30 day horizon, the mechanics of regime-dependent parameter tuning, and the primary failure modes of retail quantitative systems.

Comparative Analysis of Binary Gating and Continuous Factor Scoring
The foundational architecture of a trade selection engine dictates how a system processes market information and translates it into portfolio weights. Discretionary systems frequently rely on binary rules—sets of mandatory conditions that must be satisfied before a trade is initiated. However, modern quantitative research suggests that this approach may be sub-optimal compared to continuous factor scoring and ranking.

Claim: "Binary pass/fail filters produce inferior risk-adjusted returns compared to continuous factor scoring with ranking."
Reasoning: Binary gating mechanisms impose hard thresholds that treat all securities meeting the criteria as identical, regardless of the magnitude of their factor loadings. Academic research into dichotomized outcome measures consistently demonstrates that transforming continuous data into binary indicators results in a significant loss of information and statistical power. For instance, a stock with a relative strength (RS) of 1.01 and a stock with an RS of 1.99 are treated identically in a binary "RS ≥ 1.0" filter, despite the latter possessing a substantially stronger alpha signal. Continuous factor scoring, by contrast, maps signals to a numerical range (e.g., z-scores or 0-100 ranks), enabling the capture of the "alpha gradient". This allows the system to prioritize the highest-conviction candidates. Furthermore, practitioners like Rob Carver and researchers at AQR note that continuous signals facilitate more nuanced position sizing and permanent factor exposure, whereas binary systems can suffer from signal scarcity during choppy market regimes. Performance comparisons in medical and recruitment domains confirm that scoring models are more effective at minimizing false positives and maximizing predictive accuracy than binary pass/fail gates.
Verdict:    

The debate between these paradigms is not merely theoretical; it has practical implications for portfolio construction. A stock that passes nine different binary gates may still be a weaker candidate than a stock that fails one gate slightly but exhibits extreme outperformance in the remaining eight.

Claim: "The optimal approach is hybrid: binary filters as a FIRST PASS to eliminate clearly bad stocks, then RANK the survivors by factor score."
Reasoning: This hybrid approach is extensively documented in both academic literature and institutional practitioner whitepapers. AQR research emphasizes that efficient portfolios should exclude stocks that have negative loadings on other factors—effectively a binary screen—to ensure that the primary alpha source is not neutralized. In a 50-stock S&P 500 implementation, systems using "Sharpe-gated trade activation" (binary filter) followed by regime-aware optimization (ranking) consistently outperformed baseline benchmarks. This methodology provides a "survivorship gate" to ensure liquidity and basic trend alignment, while the ranking layer optimizes for signal strength. In non-financial domains like high-volume recruitment or genomic epimutation prediction, hybrid models that use filtering for initial reduction followed by machine learning for final ranking demonstrate superior precision and model fitness compared to using either method in isolation.
Verdict:    

The applicability of classical factor research to shorter timeframes is often questioned by swing traders. While the Fama-French and AQR models were originally designed for monthly or quarterly rebalancing, their core principles remain relevant, albeit with modifications for decay.

Claim: "Fama-French and AQR factor research applies to swing timeframes (5-30 days)."
Reasoning: While the foundational papers utilized longer rebalancing periods, subsequent research has successfully "sped up" these factors for higher-frequency horizons. The 12-1 momentum factor, traditionally a monthly anomaly, has been approximated via daily returns and shown to maintain predictive power at a 21-day (one month) horizon. Specifically, a "short-term momentum" factor (e.g., the 21-5 daily momentum strategy) can produce an attractive Sharpe ratio of 0.83, significantly contributing to portfolio performance net of transaction costs. Factors such as "short-term reversal" and "earnings momentum" are particularly effective at horizons of 5-30 days, as they capture behavioral underreactions and liquidity-driven price pressures. However, value and quality factors tend to have longer half-lives (10-25 months), meaning their impact on a 5-day trade is secondary to momentum and regime signals.
Verdict:   

Signal selectivity is another critical component of system robustness. A retail trader must balance the desire for frequent activity with the statistical need for high-quality signals.

Claim: "A system producing ~1 trade per week (238 trades over 4 years) has adequate signal frequency for a swing trading system."
Reasoning: Adequacy depends on the statistical significance of the results. Research suggests that at least 1,000 trades are typically required to establish confidence in a strategy's expectancy and to distinguish skill from luck. A sample size of 238 trades over 4 years yields approximately 60 trades per year, which may be insufficient to capture a representative sample of different market regimes. In systematic backtesting, a "high and tight" dispersion of results across thousands of signals is preferred to ensure that performance is not driven by a handful of outliers. A frequency of 1 trade per week risks being highly sensitive to a few "home run" trades, reducing the overall robustness of the system out-of-sample.
Verdict:   

One of the challenges of continuous scoring is the potential for high turnover if factor rankings fluctuate wildly day-to-day. Practitioners must determine if "rank persistence" is a necessary filter.

Claim: "Day-to-day rankings by composite factor score are stable enough to trade on without requiring rank persistence filters."
Reasoning: Empirical analysis of factor rankings shows varying levels of stability. In institutional contexts, rank persistence (the consistency of a security's rank over time) is often high for structural factors (year-to-year correlation > 0.75), but short-term alpha signals are more volatile. For a swing trader, using raw day-to-day rankings without a persistence filter or "hysteresis" often leads to "flip-flopping" near ranking boundaries, which can generate excessive transaction costs that wipe out gross gains. To mitigate this, many systems use a "snapshot" mechanism—locking in a signal once it passes a threshold rather than letting the position size float with every minor ranking change.
Verdict:   

The final step in constructing a multi-factor system is determining factor weights. Optimization is a double-edged sword that can easily lead to curve-fitting.

Claim: "Factor weights (e.g., 40% momentum, 30% trend, 20% quality, 10% sentiment) can be determined from historical optimization without overfitting."
Reasoning: Direct historical optimization of weights is highly prone to overfitting because the "best" weights in a backtest are often specific to the idiosyncratic noise of that period. Quant researchers instead utilize methods like "Equal Weighting," "Equal Risk Contribution" (Risk Parity), or "Bayesian Priors" to prevent the model from over-relying on any single factor. More sophisticated approaches employ hierarchical risk parity (HRP) or "learning-to-rank" algorithms that focus on the ordering of assets rather than the exact return magnitude, which has been shown to improve out-of-sample stability.
Verdict:   

Comparison of Factor Weighting Methodologies
Methodology	Primary Advantage	Overfitting Risk	Recommended Use Case
Equal Weighting (1/N)	Most robust out-of-sample	Very Low	
Base case for retail traders.

Risk Parity (1/σ)	Balances volatility contribution	Low	
Multi-asset portfolios with varied volatility profiles.

Historical Return Optimization	Maximizes in-sample CAGR	Extremely High	Rarely recommended without heavy regularization.
Bayesian Shrinkage	Incorporates economic priors	Moderate	
Institutional systems with long data histories.

  
Establishing a Universal Factor Set for Swing Trading horizons
To evolve from methodology-specific rules to an evidence-based framework, a trader must identify factors with documented predictive power on a 5-30 day horizon.

Claim: "The top factors with strongest empirical evidence for 5-30 day equity returns are: cross-sectional momentum, short-term reversal, earnings momentum, volatility, liquidity, and market regime."
Reasoning: Each of these factors has a distinct foundation in academic literature.

Cross-sectional Momentum: Documented by Jegadeesh and Titman (1993), with significant persistence over 3-12 month formation periods that can be captured at shorter holding horizons.   

Short-term Reversal: Proposed by De Bondt and Thaler (1985) and refined for 1-month horizons by Jegadeesh (1990); it captures price overextensions that mean-revert.   

Earnings Momentum: Captures the "post-earnings announcement drift" (PEAD), where stocks underreact to earnings news, leading to multi-week trends.   

Volatility (Low-Vol Anomaly): Research by Ang et al. (2006) shows that low-volatility stocks often outperform high-volatility ones on a risk-adjusted basis.   

Liquidity: The "illiquidity premium" suggests that less liquid stocks may offer higher returns, though for swing traders, this must be balanced against high transaction costs.   

Market Regime: Regime-switching models (Hamilton, 1989) are essential for identifying shifts between trending and mean-reverting states.
Alpha for several of these (notably short-term reversal and price momentum) has decayed since 2015 due to institutional crowding and HFT activity.
Verdict:    

Momentum remains the "premier" anomaly, but the specific implementation details—lookback and lag—are critical for swing traders.

Claim: "For swing trading, 12-1 momentum (12-month return minus last month) is the best momentum measure."
Reasoning: While 12-1 is the standard "Carhart" momentum measure used to avoid the 1-month reversal effect, research into short-term horizons shows that shorter lookbacks (e.g., 1-month or 3-month) may capture faster trend changes. For holding periods of 5-30 days, "short-term momentum" (21-day return) and "intermediate momentum" often show higher information coefficients (RankIC) than 12-month measures. Performance peaks for certain strategies have been found at 25-50 days of lookback.
Verdict:   

The inclusion of chart patterns (VCP, Cup & Handle) is a staple of discretionary trading, but their systematic utility requires discretization.

Claim: "Chart patterns (VCP, Cup & Handle) should be treated as a separate factor in a composite scoring system, not as a binary filter."
Reasoning: Advanced AI research using Convolutional Neural Networks (CNNs) has demonstrated that visual patterns can be classified with up to 99% accuracy. However, evidence suggests that explicitly detecting known patterns (binary approach) does not significantly improve performance over using raw data or technical indicators alone. Some researchers argue that chart patterns are best treated as confirmation filters (option (b)) because their efficacy is highly regime-dependent—breakout patterns (like VCP) work well in bullish trends but fail in range-bound markets.
Verdict:   

Fundamental factors are often dismissed in short-term trading, but they may serve as a critical secondary signal.

Claim: "Fundamental quality metrics (ROE, Revenue Growth, D/E) add meaningful predictive value to swing trades beyond pure technical factors."
Reasoning: Empirical findings suggest that fundamental ratios can provide a "conditioning" mechanism for technical signals. For instance, the Piotroski F-Score and earnings quality metrics help identify firms where value and momentum signals are more reliable. During high-volatility periods like the 2020 pandemic, quality factors (high profitability, low leverage) emerged as the dominant drivers of resilience. While technical factors drive the timing of the 5-30 day trade, fundamental quality metrics act as a risk shield, ensuring the stock has institutional support and reducing the likelihood of catastrophic failure.
Verdict:    

Sentiment indicators provide a gauge of market extremes. The trader must distinguish between media-driven indices and data-driven flow indicators.

Claim: "The CNN Fear & Greed Index is an adequate sentiment input for a swing trading system."
Reasoning: The CNN Fear & Greed Index is a useful heuristic for detecting contrarian reversal opportunities when it reaches "Extreme Fear" (0-25) or "Extreme Greed" (75-100). However, researchers often prefer indicators with direct links to market activity.   

Put/Call Ratio: High ratios (>1.3-1.5) indicate extreme fear and potential upward reversals.   

VIX Term Structure: Slope of the VIX curve (front month vs. back month) is a strong signal of impending volatility.   

Short Interest: High short interest can lead to "short squeezes" (extreme momentum).   

Options Flow/Insider Transactions: These provide signals of institutional or informed positioning.
Published research supports the predictive power of the put/call ratio and short interest at swing timeframes more strongly than the composite CNN index.
Verdict:   

Market regimes dictate the success of momentum versus mean-reversion. Detecting these regimes is a prerequisite for strategy selection.

Claim: "SPY > 200 SMA + VIX levels is the best regime detection method for swing trading."
Reasoning: While price-above-SMA and VIX levels are popular heuristics, they are "lagging" indicators that may fail during rapid regime shifts. Alternatives such as Hidden Markov Models (HMM) and Gaussian Mixture Models (GMM) use probabilistic state inference to detect "crisis," "neutral," and "stable" regimes in near real-time. Breadth indicators (e.g., % of stocks above 200-day SMA) provide a more comprehensive view of "market quality" than a single index price. Institutional funds like Medallion utilize rapid parameter updates (1-3 day holding periods) to adapt to new regime data before losses compound.
Verdict:   

Factor correlation must be managed to avoid unintentional concentration in a single return driver.

Claim: "Our momentum and trend factors are too correlated and one should be dropped or they should be combined."
Reasoning: Momentum (return-based) and trend (moving average-based) are mathematically related but capture different nuances of market drift. "Correlation risk" arises when factors move in lockstep, reducing diversification. Factor analysis in the "factor zoo" reveals that while momentum effects are pervasive, some combinations exhibit high correlation (e.g., 0.61 between 21-day and 252-day momentum). Researchers recommend handling this through "orthogonality" checks: only adding factors with low conditional correlations (e.g., combining Value with Momentum) or using Principal Component Analysis (PCA) to extract independent signals.
Verdict:    

Factor Hierarchy for Swing Trading (5-30 Day Horizon)
Category	Primary Metric	Economic Rationale	Half-Life
Drift/Trend	3-Month RS	Captures persistent institutional flow	~3 Months
Short-Term Drift	21-Day ROC	Exploits high-frequency persistence	< 1 Month
Reversion	ConnorsRSI	Captures temporary overextensions	3-5 Days
Resilience	ROE / Low D/E	Quality filter during volatility regimes	> 1 Year
Risk	VIX / PCR	Gauges collective fear/optimism	Variable
Mean-Reversion Mechanics and Strategy Integration
Our primary system is momentum-oriented, leading to performance gaps in non-trending markets. Integrating mean-reversion requires an understanding of how these strategies differ in their return distributions and risk profiles.

Claim: "Mean-reversion strategies work best in range-bound/low-volatility markets, while momentum works best in trending/high-dispersion markets."
Reasoning: This characterization is fundamentally supported by the "regime-conditional" nature of returns. Mean-reversion thrives when asset prices oscillate within boundaries, allowing for high win-rate "snap-back" trades. Momentum, conversely, requires "high dispersion"—wide gaps between winners and losers—to generate alpha. Strategy selection can be automated by monitoring the Hurst Exponent (fractal dimension) or ADX; high values signal trends, while low values suggest range-bound behavior.
Verdict:    

The classic "oversold" entry for mean-reversion typically utilizes the Relative Strength Index (RSI).

Claim: "RSI < 30 oversold bounces are a proven mean-reversion entry for swing trading US equities."
Reasoning: Traditional 14-period RSI at the 30 threshold is widely popular, but research by Larry Connors suggests that shorter lookbacks (2-period or 3-period RSI) are far more effective for identifying short-term equity bounces. Specifically, an RSI(2) value less than 10 is considered a more reliable indicator of an oversold condition than the standard RSI(14) < 30. While these signals remain profitable, their edge has been impacted by "volatility clustering," where oversold markets can become even more oversold during liquidity crises (the "falling knife" problem).
Verdict:   

Bollinger Bands are often paired with RSI to provide volatility context.

Claim: "Bollinger Band mean-reversion (buy at lower band, sell at upper) has empirical evidence of edge in swing timeframes."
Reasoning: In a normal distribution, ~95% of price action occurs within 2 standard deviations of the mean. Bollinger Band entries (buying the lower band) have demonstrated 71% win rates in ranging forex and large-cap equity markets. However, the academic literature warns that Bollinger Bands are non-continuous and can lead to "band-walking" during strong trends, where the price stays pinned to the lower band as it continues to drop.
Verdict:    

Risk management for mean-reversion is structurally different from trend-following.

Claim: "Mean-reversion trades should use different risk parameters than momentum trades: tighter stops, lower R:R, time-based exits."
Reasoning: Mean-reversion strategies typically exhibit a "negative skew" return distribution—many small wins punctuated by occasional large losses. Because the edge comes from a temporary overextension, time-based exits (closing after X days) are often superior to wide price-based stops, which can allow a "mean-reversion trade" to turn into a "losing investment". Conversely, momentum strategies require wide stops to "let winners run" and capture asymmetric positive skew (big wins vs. small losses).
Verdict:    

The potential for strategy diversification is high when combining momentum and reversion.

Claim: "Running momentum and mean-reversion simultaneously in one system improves risk-adjusted returns through strategy diversification."
Reasoning: The goal of a "multi-strategy" system is to generate orthogonal exposures—return streams that are uncorrelated. Backtests often show that combining trend-following with mean-reversion improves the Sharpe ratio by 15-30% because these strategies suffer drawdowns at different times (e.g., mean-reversion wins when momentum is getting "chopped up"). Parallel execution is generally more robust than "switching" because regime detection has an inherent lag.
Verdict:    

Expectations for win rates and return distributions should be calibrated correctly.

Claim: "Mean-reversion systems have 60-70% win rates with smaller average wins, while momentum systems have 50-55% win rates with larger wins."
Reasoning: This characterization accurately reflects the empirical profiles of these paradigms. Mean-reversion strategies (like Bollinger Bands + RSI) frequently report win rates of 60-80% but have a lower reward-to-risk ratio. Momentum strategies (like breakouts or trend-following) often have lower win rates (35-50%) but depend on a "fat right tail" of outsized returns to achieve profitability.
Verdict:    

For a trader seeking simplicity, one indicator stands out as the benchmark for reversion.

Claim: "Connors RSI or the DV2 indicator represents the simplest evidence-based mean-reversion approach for US equities."
Reasoning: ConnorsRSI is a composite of three components (RSI, streak duration, and ROC rank) that has demonstrated consistent edge in S&P 500 stocks over decades. Backtests from 2002-2016 showed that the top decile of ConnorsRSI variations produced compound annual returns (CAR) of ~26%, outperforming simple benchmark strategies. While the "DV2" (2-day variation) is less documented in recent snippets, the "RSI(2)" component of ConnorsRSI remains a gold standard for simple, high-win-rate reversion models.
Verdict:    

Principles of Regime-Adaptive Parameter Tuning
Fixed parameters are often the "Achilles' heel" of systematic strategies. Market conditions change, and a static 7% stop loss may be too tight in one month and too loose in another.

Claim: "Varying strategy parameters based on market regime (e.g., VIX level) improves risk-adjusted returns vs fixed parameters."
Reasoning: Dynamic adaptation is a hallmark of sophisticated institutional systems. Renaissance Technologies' Medallion Fund famously adapts its risk and positioning daily based on regime state inference. Research shows that regime-adaptive gradient ensembles (RAGe-ENS) can improve Sharpe ratios by up to 80% over static models by adjusting weights and parameters to match the prevailing environment. However, the primary risk is "overfitting" the adaptation rules to historical noise.
Verdict:    

Volatility scaling is perhaps the most critical adaptive parameter.

Claim: "Stop loss distance should adapt to volatility: wider in high-vol, tighter in low-vol (ATR-based stops naturally do this)."
Reasoning: Average True Range (ATR)-based stops provide a "volatility-normalized" risk buffer. In high-volatility regimes, price swings are wider, and fixed-percentage stops (e.g., 7%) are frequently hit by "market noise" rather than a genuine trend change. Using 2x ATR stops ensures that the distance to the stop is proportional to the stock's current "personality".
Verdict:    

There is an order of importance for which parameters to adapt first.

Claim: "Position sizing is the most important parameter to adapt to regime, more impactful than adjusting entry/exit rules."
Reasoning: "Regime-aware risk management" focuses on scaling total exposure rather than trying to find the "perfect" entry. Bayesian updating of regime probabilities allows for continuous adjustments to position sizing, which is cited as a primary driver of outperformance during market crashes like March 2020. Adapting entries/exits is more complex and prone to data-mining, whereas position sizing is a direct function of portfolio risk limits.
Verdict:    

Defining the boundaries of a regime is often handled through volatility thresholds.

Claim: "VIX < 20 / 20-30 / > 30 is the right tiering for regime classification."
Reasoning: This is a common industry standard for discrete regime classification.

VIX < 20: Stable/Calm; often favorable for "tight" range trading.   

VIX 20-30: Elevated/Nervous; "flashing yellow light" indicating wider swings.   

VIX > 30: Crisis/Panic; signals potential market bottoms for mean-reversion or a "flight to cash" for momentum traders.
However, modern researchers recommend continuous scaling based on VIX percentile rank or probabilistic HMM states to avoid "cliff effects" near boundaries.
Verdict:    

Lookback windows are another candidate for adaptation.

Claim: "Momentum lookback periods should shorten in fast-moving markets and lengthen in slow-moving markets."
Reasoning: This theory is known as "Automated Polymorphic Momentum." The logic is that "fast" breakouts require responsive signals, while "slow" secular trends benefit from smoothed data. While there is some evidence that peak performance for different assets occurs at different lookback time constants (e.g., 25 days vs. 50 days), obtaining statistically significant results for dynamic switching remains difficult and is often criticized for lack of interpretability.
Verdict:   

A crucial guardrail is the number of adaptive parameters utilized.

Claim: "More than 2-3 regime-adaptive parameters crosses into overfitting territory for a retail swing trading system."
Reasoning: Model flexibility comes at a high price of increased variance. Over-optimized strategies lose up to 80% of their profits when going live. Researchers recommend maintaining a " Strong and Simple" framework, focusing on the 2-3 most impactful adaptations (e.g., position sizing and stop losses) while keeping core entry logic static.
Verdict:    

Identifying the Divide Between Success and Failure
retail traders often struggle with the "research-to-live" gap. Understanding why systems fail is as important as understanding why they succeed.

Claim: "The top 5 reasons systematic trading systems fail in live trading are: overfitting, transaction costs, regime change, execution slippage, and behavioral deviation from rules."
Reasoning: Empirical data and institutional post-mortems (like Knight Capital) support these failure modes.   

Overfitting: Backtest results with near-zero predictive power.   

Transaction Costs/Slippage: Ignoring the "implicit" costs of bid-ask bounce and market impact.   

Regime Change: DataSource non-stationarity—past return properties not matching future ones.   

Operational/Execution Issues: Coding errors or server downtime.   

Behavioral Deviation: Human intervention during drawdowns.
Published surveys confirm these are the primary risks, with "leverage commonality" and "crowded trades" also acting as major systemic failure drivers for funds.
Verdict:    

Many traders rely solely on walk-forward testing to prevent overfitting.

Claim: "Walk-forward testing is sufficient to prevent overfitting."
Reasoning: Walk-forward testing is a powerful validation tool, but it is not a "silver bullet." It can be "manually overfitted" if the researcher runs multiple walk-forward trials and selects the winner. Robust systems require additional layers of validation:   

Monte Carlo Simulations: Testing the system's sensitivity to randomized trade order or minor parameter permutations.   

Cross-Validation: Training on different subsets of assets and time segments.   

Parameter Stability Analysis: Ensuring that performance doesn't collapse with a small change in a moving average window.
Verdict:   

The "simplicity premium" suggests that a complexity budget is essential.

Claim: "Simpler trading systems (fewer parameters, fewer factors) outperform more complex ones out-of-sample."
Reasoning: There is strong empirical evidence for a simplicity premium. In graph-based volatility forecasting, sparse models with 74% fewer "edges" (connections) achieved 5.1% higher accuracy than fully-connected dense models. Principled simplicity filters "noise" from weak relationships that more complex models mistakenly "memorize". For retail traders, the " Strong and Simple" vision emphasizes delivering resilience at lower costs through addressing the "complexity problem".
Verdict:    

Transaction costs are often the "silent killer" of retail alpha.

Claim: "For a swing system doing 1-5 trades/week in stocks with $10M+ daily volume, transaction costs and slippage are negligible (<5 bps per trade)."
Reasoning: This claim is inaccurate for retail execution. While $100M+ ADV stocks (large caps) may have 2-5 bps slippage, stocks with $10M ADV exhibit significantly higher execution friction. For a $100k retail order in a $10M ADV name, the order represents 1% of the daily volume, which can trigger visible market impact and slippage of 20-50+ bps. Total costs (bid-ask + slippage + commission + fees) can easily exceed 20-30 bps in mid-cap names, which is a meaningful "drag" for a strategy targeting a 100-200 bps swing.
Verdict:   

Retail Slippage Estimates by Volume and Order Size
Average Daily Volume (ADV)	Order Size	Market Order Slippage	Limit Order Tip
$100M+ (Large Cap)	$10k	< 1-2 cents	
"Passive fill" 

$100M+ (Large Cap)	$100k	3-5 bps	
"Aggr. Limit" 

$10M (Mid/Small Cap)	$10k	5-15 bps	
Split order 

$10M (Mid/Small Cap)	$100k	20-50+ bps	Avoid Market Orders
  
Alpha decay is a persistent reality in the institutional era.

Claim: "Factors that worked in 2010-2020 (momentum, value, quality) continue to work in 2020-2026 with similar magnitude."
Reasoning: There is evidence of significant decay in traditional factors. The "factor momentum" and "factor timing" literature notes that assets in dispersion (like volatility arbitrage) tripled between 2021-2024, leading to smaller edges (2-5% annual expected return vs. 100% in the 1990s). Traditional individual stock momentum has weakened as institutional demand for "factor-pure" ETFs has eliminated much of the mispricing. Only "fraud-mitigated" quality factors or high-frequency "short-term momentum" have remained robust through 2024.
Verdict:   

Identifying the "retail edge" involves recognizing which domains are unavailable to individuals.

Claim: "A retail swing trader should NOT try to compete on: intraday mean-reversion, statistical arbitrage, high-frequency market making, or options flow trading because these require institutional infrastructure."
Reasoning: These strategies rely on sub-millisecond execution, co-location, and deep order-book analysis. HFT firms dominate market making and ticker tape trading. However, retail swing traders have a genuine edge in "Liquidity Provision" to institutional blocks that need to move over hours or days. Because retail capital is small, it can move in and out of $10M-$50M ADV stocks that are too "thin" for a $10B hedge fund to trade efficiently. This "liquidity edge" allows retail traders to capture premiums that institutions cannot exploit due to their own market impact.
Verdict:    

Designing the Minimum Viable Systematic System
For a retail trader with ~$50k-$100k capital, the objective is to balance evidence-based alpha with manual execution constraints.

Claim: "The minimum viable evidence-based swing trading system for retail is: 2-3 factors (momentum + trend + regime filter), equal-weighted, with ATR-based stops and 7% max loss, rebalanced weekly."
Reasoning: This architecture aligns with the "simplicity premium" and the "Strong and Simple" vision of high-quality sparse connectivity.   

2-3 Factors: Research shows that 22-27% of factors exhibit strong return continuation; a multi-style composite (e.g., 50% technical/momentum + 50% defensive/quality) reduces cyclicality.   

Equal-Weighted: This is the most robust allocation for retail traders with limited data.   

ATR-Based Stops: Essential for volatility normalization.   

Weekly Rebalancing: Balances the need to maintaining factor exposure with the constraint of minimizing transaction costs.
Verdict:    

Proposed System Design: "The Hybrid Pivot Strategy"
Based on the audited claims, a robust retail implementation would follow this workflow:

Qualified Universe (Binary Gate):

S&P 500 or Russell 1000 members (ensures baseline liquidity).

Price > 150-Day SMA (filters Stage 4 downtrends).   

Daily dollar volume > $20M (limits retail slippage to < 10 bps).   

Factor Scoring (Ranking Layer):

Factor A: 21-Day ROC (Short-term persistence).   

Factor B: 3-Month Relative Strength (Intermediate drift).   

Factor C: Piotroski F-Score (Fundamental risk shield).   

Scores are standardized to z-scores and equally weighted.

Risk Management (Adaptive Layer):

Stop Loss: 2.5x ATR (volatility-normalized).

Position Sizing: Scaled inversely to the VIX (reduce exposure when VIX > 30).   

Execution: Weekly rebalance using limit orders placed 0.5% below the midquote.   

Advanced Technical Implementation: Bayesian State Inference
For traders seeking institutional-grade regime detection, the Hidden Markov Model (HMM) offers a formal framework for inferring the unobserved "state" of the market (S 
t
​
 ). The model parameters θ={A,B,π} (transition matrix, emission probabilities, and initial state distribution) are estimated using the Baum-Welch algorithm.   

P(S 
t
​
 ∣O 
1:t
​
 )∝B(O 
t
​
 ∣S 
t
​
 )⋅ 
S 
t−1
​
 
∑
​
 A(S 
t
​
 ∣S 
t−1
​
 )⋅P(S 
t−1
​
 ∣O 
1:t−1
​
 )
This "Bayesian updating" allows the system to transition to defensive cash positions (S 
t
​
 =Crisis) within 2-3 days of a volatility spike, a capability that fixed moving average filters lack. The Sortino ratio is used as the primary performance yardstick, as it prioritizes returns relative to downside volatility, which is the primary concern in regime-shifting markets.   

Conclusions and Practical Implications
The transition from discretionary methodologies to systematic factor frameworks is necessitated by the increasing efficiency of modern equity markets. The audit results establish that a continuous scoring architecture, supported by a hybrid binary filter, provides the most robust foundation for capturing alpha gradients. For the swing trader operating on a 5-30 day horizon, momentum and short-term reversal are the primary drivers of returns, while fundamental quality serves as a conditional risk filter.   

Success in live trading is determined not by the complexity of the alpha factor, but by the rigor of the execution assumptions and the ability to adapt to regime shifts. Retail traders must respect the non-linear costs of slippage in mid-cap names and resist the temptation to over-optimize weights. By embracing the "simplicity premium"—maintaining a sparse network of high-quality factors and utilizing adaptive risk controls—traders can build a system that achieves resilience through structural diversification rather than architectural sophistication.   


# Perplexity answers
Below are verdicts for each claim, using your required format. Citations are illustrative, not exhaustive.

***

## PROMPT 1: Binary Gating vs Continuous Factor Scoring

> **Claim:** *“Binary pass/fail filters produce inferior risk-adjusted returns compared to continuous factor scoring with ranking.”*

> **Reasoning:**  
> Empirical factor and score-based investing research overwhelmingly implements *continuous* scores and *ranking* (e.g., F‑score, quality scores, composite factor scores) rather than hard binary gates, and shows that portfolios formed from ranked scores can outperform the market and naive benchmarks. Stock screeners and quant platforms likewise use filters mainly to define a universe, then rely on continuous scores and ranking to choose and size positions. However, there is no specific head‑to‑head published test that directly compares “pure binary gating” versus “continuous scoring + ranking” on the same signal set across many markets and horizons. [marketbeat](https://www.marketbeat.com/stock-screener/)

> **Verdict:** [UNVERIFIED — NEEDS: A controlled study that implements the *same* underlying signals in (a) strict binary‑gated form and (b) continuous composite score with ranking, and compares risk‑adjusted performance and turnover across multiple universes and periods.]

***

> **Claim:** *“The optimal approach is hybrid: binary filters as a FIRST PASS to eliminate clearly bad stocks, then RANK the survivors by factor score.”*

> **Reasoning:**  
> In practice, most factor and quant implementations *do* use a hybrid pattern: coarse binary/universe filters on liquidity, price, basic quality, etc., and then *ranking* of survivors by continuous factors or composite scores (e.g., factor models, quality scores, stock selection tutorials on QuantConnect, etc.). This suggests hybrid design is *standard practice*, but the word “optimal” implies provable superiority over pure ranking or pure filtering, and there is no general theorem or large‑scale study establishing that hybrid is always best. [nature](https://www.nature.com/articles/s41599-024-03888-4)

> **Verdict:** [MISLEADING — CORRECTION: Hybrid filter‑then‑rank architectures are widely used and well supported in practice, but there is no general proof that they are globally “optimal”; they are a robust, conventional design rather than a mathematically established best.]

***

> **Claim:** *“Fama-French and AQR factor research applies to swing timeframes (5-30 days).”*

> **Reasoning:**  
> Classic Fama‑French and AQR factor research (value, size, momentum, quality, profitability, etc.) is mostly tested with **monthly or longer rebalancing**, not 5–30‑day holding periods. Short‑horizon literature finds *different* anomalies—weekly reversal, very short‑term momentum, intraday vs overnight effects—that often behave differently from standard monthly 12‑1 momentum and value factors. There is some evidence that short‑term reversal and certain forms of short‑term momentum have predictive power at weekly horizons, but this is not the same as saying the canonical FF/AQR factor sets “apply unchanged” at 5–30 days. [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426621000261)

> **Verdict:** [MISLEADING — CORRECTION: Standard Fama‑French/AQR factors are documented mainly at monthly/quarterly horizons; some related short‑term anomalies exist at 5–30 days, but you cannot assume the full FF/AQR toolkit carries over with similar strength without explicit horizon‑specific testing.]

***

> **Claim:** *“A system producing ~1 trade per week (238 trades over 4 years) has adequate signal frequency for a swing trading system.”*

> **Reasoning:**  
> Statistical testing literature emphasizes the need for a *sufficient number* of independent trades to estimate edge and Sharpe reliably, but does not fix a universal “trades per year” target. 238 trades over four years (~60 trades/year) is enough to estimate performance with some confidence, but sampling error remains material, especially if trades are clustered in particular regimes or asset types. No published paper specifies that ~1 trade/week is *generally* “adequate” for all swing systems; adequacy depends on effect size, volatility, and dependence structure. [rpc.cfainstitute](https://rpc.cfainstitute.org/research/cfa-digest/2016/06/does-academic-research-destroy-stock-return-predictability-digest-summary)

> **Verdict:** [UNVERIFIED — NEEDS: A formal power analysis or bootstrap on your own backtest to quantify confidence intervals for Sharpe and win rate at 238 trades; there is no universal research‑backed “1 trade per week is enough” rule.]

***

> **Claim:** *“Day-to-day rankings by composite factor score are stable enough to trade on without requiring rank persistence filters.”*

> **Reasoning:**  
> Factor and stock‑selection literature discusses *turnover* and *signal stability*, and some work (e.g., factor momentum, regime‑switching models) shows that factor returns and rankings can be quite time‑varying, particularly at daily horizons. Many practitioners explicitly use **monthly or weekly rebalancing** and simple holding periods rather than acting on every daily ranking change, and some strategies include buffer bands or holding rules to reduce churn. There is no broad empirical statement that daily composite rankings are always stable enough to act on without any rank‑persistence or buffer logic; stability is highly implementation‑ and universe‑dependent. [rodneywhitecenter.wharton.upenn](https://rodneywhitecenter.wharton.upenn.edu/wp-content/uploads/2018/03/Juhani.pdf)

> **Verdict:** [UNVERIFIED — NEEDS: Empirical measurement of your own composite rank autocorrelation and turnover at daily vs weekly horizons, and a comparison of performance with and without persistence/buffer rules.]

***

> **Claim:** *“Factor weights (e.g., 40% momentum, 30% trend, 20% quality, 10% sentiment) can be determined from historical optimization without overfitting.”*

> **Reasoning:**  
> The portfolio and factor‑investing literature repeatedly shows that **in‑sample optimization of weights is prone to overfitting**, especially with many parameters and limited data; this is why simple or equal‑weight factor combinations often match or beat optimized ones out‑of‑sample. Robust approaches include cross‑validation, shrinkage/Bayesian priors, and constraints (e.g., limiting how far weights can deviate from equal), but even then overfitting risk remains if the signal‑to‑noise ratio is low. The claim that you can simply optimize weights historically “without overfitting” contradicts this body of evidence. [robeco](https://www.robeco.com/files/docm/docu-robeco-factor-performance-2010-2019-a-lost-decade.pdf)

> **Verdict:** [MISLEADING — CORRECTION: Historical optimization can suggest factor weights, but by itself it is *high‑risk* for overfitting; robust practice uses simple or constrained weights plus cross‑validation and stability checks rather than trusting unconstrained in‑sample optimization.]

***

## PROMPT 2: Universal Factor Set for Swing/Position Trading

> **Claim:** *“The top factors with strongest empirical evidence for 5-30 day equity returns are: cross-sectional momentum, short-term reversal, earnings momentum, volatility, liquidity, and market regime.”*

> **Reasoning:**  
> There is strong evidence that **short‑term reversal** (weekly/monthly) and short‑term momentum exist in equity returns. Earnings‑related drift (“earnings momentum”) is documented mostly at multi‑month horizons, while volatility, liquidity, and regime variables are widely used as *conditioning* factors rather than primary 5–30‑day alpha signals. However, there is no canonical paper that ranks “top factors for 5–30‑day returns” in exactly this set or order, and most factor surveys are framed at monthly or longer rebalancing. [alphaarchitect](https://alphaarchitect.com/what-drives-momentum-and-reversal/)

> **Verdict:** [UNVERIFIED — NEEDS: A systematic, horizon‑specific study that evaluates a broad menu of candidate factors specifically for 5–30‑day forward returns and ranks them by information ratio; current literature does not provide this exact ranking.]

***

> **Claim:** *“For swing trading, 12-1 momentum (12-month return minus last month) is the best momentum measure.”*

> **Reasoning:**  
> The classic Jegadeesh & Titman result shows that **12‑1 momentum** (12‑month return skipping the most recent month) is very effective for *3–12 month* holding periods, with about 1%/month abnormal returns. Their own work and follow‑ups focus on monthly portfolios, not 5–30‑day swings. Short‑term studies find both weekly reversal and shorter‑horizon momentum effects that may favor different lookbacks than 12‑1. No study was found that proves 12‑1 is *the* best momentum definition specifically for 5–30‑day forward equity returns. [morningstar](https://www.morningstar.com/markets/achilles-heel-momentum-strategies)

> **Verdict:** [MISLEADING — CORRECTION: 12‑1 momentum is strongly supported for medium‑term (multi‑month) strategies, but its superiority for 5–30‑day swing trading is unproven; alternative lookbacks (e.g., 3–6 months, shorter‑term trends) may be more relevant and require direct testing.]

***

> **Claim:** *“Chart patterns (VCP, Cup & Handle) should be treated as a separate factor in a composite scoring system, not as a binary filter.”*

> **Reasoning:**  
> Academic work on chart pattern detection focuses on algorithmic recognition and, more recently, deep‑learning approaches, and often treats patterns as *features* or labels in prediction tasks rather than prescriptive trading rules. However, there is essentially no peer‑reviewed literature comparing “pattern as graded factor in a composite score” versus “pattern as binary filter” in a factor model context, let alone specifically for Minervini/O’Neil patterns like VCP and Cup & Handle. [arxiv](https://arxiv.org/pdf/1808.00418.pdf)

> **Verdict:** [UNVERIFIED — NEEDS: A study that encodes patterns as (a) binary flags and (b) graded confidence scores inside a composite factor model, and compares their incremental predictive value and stability for 5–30‑day returns.]

***

> **Claim:** *“Fundamental quality metrics (ROE, Revenue Growth, D/E) add meaningful predictive value to swing trades beyond pure technical factors.”*

> **Reasoning:**  
> Quality and profitability factors (e.g., high ROE, low leverage) show robust evidence of **multi‑year** and **multi‑month** excess returns, especially post‑1990, and are widely used in factor indexes. But most studies examine monthly or quarterly rebalancing; the incremental predictive power of these slow‑moving fundamentals for 5–30‑day returns on top of technical/momentum signals is far less documented. Hybrid models that mix fundamentals and technicals can show improvements in some AI/ML studies, but the horizon is often longer and results are model‑specific. [man](https://www.man.com/insights/questioning-quality)

> **Verdict:** [UNVERIFIED — NEEDS: A horse‑race where technical‑only vs technical+fundamental models are compared specifically on 5–30‑day forward returns, controlling for turnover and costs; current evidence for fundamentals is strong at longer horizons but sparse for swing‑length horizons.]

***

> **Claim:** *“The CNN Fear & Greed Index is an adequate sentiment input for a swing trading system.”*

> **Reasoning:**  
> Documentation on the CNN Fear & Greed Index describes it as a **broad composite sentiment gauge** (breadth, options, credit, volatility, etc.) but does not provide peer‑reviewed evidence of short‑term predictive power for individual stock or sector returns. In contrast, there is published research on sentiment proxies such as put/call ratios, short interest, volatility term structure, news and social media sentiment, and analyst revisions affecting near‑term returns. Without studies showing that changes in the Fear & Greed Index improve 5–30‑day trading decisions, calling it “adequate” is more convenience than evidence. [msci](https://www.msci.com/downloads/web/msci-com/research-and-insights/paper/factor-indexing-through-the-decades/factor-indexing-through-the-decades.pdf)

> **Verdict:** [MISLEADING — CORRECTION: The CNN Fear & Greed Index is a useful high‑level sentiment gauge but lacks specific, documented edge for swing‑timeframe trading; more empirically studied sentiment inputs (e.g., option‑based, news/sentiment scores) are better candidates if evidence‑based design is the goal.]

***

> **Claim:** *“SPY > 200 SMA + VIX levels is the best regime detection method for swing trading.”*

> **Reasoning:**  
> There is substantial evidence that **SPY (or index) > 200‑day SMA** as a trend filter reduces drawdowns and changes risk characteristics, and practitioner/academic pieces support its use as a simple regime filter. VIX levels and thresholds are also widely used heuristics for volatility regimes, but research emphasizes that fixed cuts (20, 30) are conventions rather than optimized boundaries. Hidden Markov models, breadth‑based indicators, and clustering approaches provide alternative regime classifications and can outperform simple rules in some studies. No source shows that SPY>200d+VIX tiers is *the* best regime method for swing trading. [ideas.repec](https://ideas.repec.org/a/eee/ecmode/v122y2023ics0264999323000494.html)

> **Verdict:** [MISLEADING — CORRECTION: SPY>200‑day and VIX bands are reasonable, well‑known regime filters, but they are not uniquely best; more sophisticated methods (HMMs, breadth, volatility clustering) can outperform in some contexts and should be evaluated empirically.]

***

> **Claim:** *“Our momentum and trend factors are too correlated and one should be dropped or they should be combined.”*

> **Reasoning:**  
> 52‑week relative strength and moving‑average trend conditions (e.g., price > 50 > 200 SMA) are both derivatives of sustained price movement and are likely to be **positively correlated** in most universes, which reduces incremental information if used separately. Standard factor‑model practice is to assess redundancy via correlations and *incremental* predictive power (e.g., adding one factor to a model already containing the other) rather than assuming correlated factors must be dropped. Sometimes combining correlated indicators into one composite “trend/momentum” score is cleaner, but whether you “should” drop one depends on actual incremental performance and stability tests. [rpc.cfainstitute](https://rpc.cfainstitute.org/research/cfa-magazine/2003/fundamental-vs-technical-analysis)

> **Verdict:** [PLAUSIBLE — REASON: Momentum and trend factors are likely correlated and may be profitably merged or de‑duplicated, but you should verify this via correlation and incremental‑alpha tests rather than assume that one must be removed.]

***

## PROMPT 3: Mean-Reversion for Swing Traders

> **Claim:** *“Mean-reversion strategies work best in range-bound/low-volatility markets, while momentum works best in trending/high-dispersion markets.”*

> **Reasoning:**  
> Regime‑switching and theoretical models show that markets can exhibit alternating periods where **short‑term momentum or short‑term reversal dominates**, and that strategy performance is regime‑dependent. Practitioner and backtest articles explicitly show higher mean‑reversion effectiveness in sideways/bearish conditions and better momentum performance in trending/bull regimes, including ETF strategies that switch rules based on regime indicators. However, the mapping between “range‑bound/low‑vol” vs “trending/high‑dispersion” and strategy edge is approximate and model‑dependent. [fortraders](https://www.fortraders.com/blog/momentum-vs-mean-reversion-strategies-for-challenges)

> **Verdict:** [PLAUSIBLE — REASON: There is both theoretical and empirical support that mean‑reversion and momentum perform differently across regimes, with MR better in choppy markets and momentum better in strong trends, but this is not a universal law and requires regime‑definition and strategy‑specific validation.]

***

> **Claim:** *“RSI < 30 oversold bounces are a proven mean-reversion entry for swing trading US equities.”*

> **Reasoning:**  
> Many educational pieces present RSI(14) < 30 as an “oversold” condition and suggest buying for mean reversion, but robust evidence on simple 30/70 rules delivering consistent edge is mixed. In contrast, multiple backtests and practitioner research show more consistent performance for **very short‑term RSI(2) or RSI(2–3)** with much lower thresholds (e.g., <5, <10) combined with trend filters (Connors‑style systems) on indices and large‑cap ETFs. Academic and quasi‑academic tests of simple RSI(14) < 30 rules often find that edges are fragile or disappear after costs. [interactivebrokers](https://www.interactivebrokers.com/campus/ibkr-quant-news/mean-reversion-strategies-introduction-trading-strategies-and-more-part-i/)

> **Verdict:** [MISLEADING — CORRECTION: RSI(14) < 30 is a standard oversold heuristic, but the best‑documented RSI mean‑reversion edges use very short‑period RSI (e.g., RSI(2)) with much more extreme thresholds and trend filters; “RSI<30” alone is not robustly “proven” for swing equity trading.]

***

> **Claim:** *“Bollinger Band mean-reversion (buy at lower band, sell at upper) has empirical evidence of edge in swing timeframes.”*

> **Reasoning:**  
> Bollinger Bands are widely cited in mean‑reversion tutorials as a way to define overbought/oversold zones, and some broker/education content gives example strategies. However, there is little peer‑reviewed, large‑sample evidence that the naïve rule “buy near lower band, sell near upper band” systematically outperforms after costs across equities at 5–30‑day horizons. Most serious research is either indicator‑agnostic or focuses on RSI‑style or price‑based MR rules rather than Bollinger‑specific ones. [blog.quantinsti](https://blog.quantinsti.com/mean-reversion-strategies-introduction-building-blocks/)

> **Verdict:** [UNVERIFIED — NEEDS: A broad, transparent study testing standard Bollinger‑band MR rules across large equity universes and multiple decades, with realistic costs, to demonstrate persistent risk‑adjusted edge.]

***

> **Claim:** *“Mean-reversion trades should use different risk parameters than momentum trades: tighter stops, lower R:R, time-based exits.”*

> **Reasoning:**  
> Strategy descriptions and backtests of mean‑reversion systems (e.g., Connors RSI variants, intraday MR strategies) typically show **higher win rates with smaller average wins and losses**, often using relatively tight stops and modest profit targets or time‑based exits. Momentum systems generally have lower win rates with larger average winners, tolerating deeper pullbacks to avoid being shaken out. While these patterns are widely observed in practice, there is limited formal research that codifies a universal risk‑parameter template by strategy class. [mql5](https://www.mql5.com/en/articles/17636)

> **Verdict:** [PLAUSIBLE — REASON: Empirical behavior of MR vs momentum strategies supports using different stop/target/time‑exit logic, but exact parameter choices are strategy‑specific rather than dictated by a universal rule.]

***

> **Claim:** *“Running momentum and mean-reversion simultaneously in one system improves risk-adjusted returns through strategy diversification.”*

> **Reasoning:**  
> Regime‑switching and mixed‑strategy examples show that combining momentum and mean‑reversion rules on different assets or in different regimes can yield Sharpe ratios >1 and smoother equity curves than either strategy alone. Theoretical models also highlight that momentum and reversal correspond to different underlying dynamics and risks, so their return streams are not perfectly correlated. That said, benefits depend on implementation quality, costs, and whether the two strategies truly diversify each other. [priceactionlab](https://www.priceactionlab.com/Blog/2024/01/mean-reversion-and-momentum-regime-switching/)

> **Verdict:** [PLAUSIBLE — REASON: There is concrete evidence from specific regime‑switching and two‑factor models that combining momentum and MR can improve risk‑adjusted returns, but this is not guaranteed and must be validated for your universe, signals, and costs.]

***

> **Claim:** *“Mean-reversion systems have 60-70% win rates with smaller average wins, while momentum systems have 50-55% win rates with larger wins.”*

> **Reasoning:**  
> Published and transparent backtests of Connors‑style mean‑reversion on indices and large ETFs often report win rates in the 60–75% range with relatively small per‑trade profit targets and rare large winners. Momentum anomalies in the academic literature (e.g., 12‑1 momentum) typically translate to modest per‑trade edge and about half of trades being winners, not 70%+. However, these are general tendencies, not hard rules; win rates and payoff distributions can vary widely across implementations, universes, and time periods. [breesefine7110.tulane](https://breesefine7110.tulane.edu/wp-content/uploads/sites/16/2015/10/Momentum-2001.pdf)

> **Verdict:** [MISLEADING — CORRECTION: It is *typical* but not guaranteed that MR strategies show higher win rates with smaller wins while momentum has lower win rates with larger winners; these are empirical patterns from many backtests, not fixed properties that all MR or momentum systems will exhibit.]

***

> **Claim:** *“Connors RSI or the DV2 indicator represents the simplest evidence-based mean-reversion approach for US equities.”*

> **Reasoning:**  
> Multiple independent backtests of **Connors RSI(2)‑style rules** on SPY/indices show persistent, transparent mean‑reversion behavior over long samples, suggesting a real and well‑documented edge under certain assumptions. DV2 (a 2‑day volatility/RSI hybrid) and similar indicators are popular variants, but comparative research against other simple MR rules (e.g., basic RSI(2), price‑MA deviations) is sparse. No formal study ranks Connors RSI or DV2 as *the* simplest or best evidence‑based MR method. [trade2win](https://www.trade2win.com/threads/backtest-results-for-connors-rsi2-strategy.242688/)

> **Verdict:** [UNVERIFIED — NEEDS: A systematic comparison of several candidate “simple MR rules” (RSI(2), Connors RSI, DV2, price‑MA z‑scores, etc.) over large universes and decades; existing evidence shows Connors‑style rules work, but not that they are uniquely simplest or best.]

***

## PROMPT 4: Regime-Adaptive Parameters

> **Claim:** *“Varying strategy parameters based on market regime (e.g., VIX level) improves risk-adjusted returns vs fixed parameters.”*

> **Reasoning:**  
> Some explicit regime‑switching studies (e.g., models that switch between momentum and mean‑reversion based on a regime indicator) do report higher Sharpe ratios and better drawdown profiles than static single‑regime strategies. However, these results are model‑ and dataset‑specific, and there are also many anecdotal examples where over‑tuned regime rules fail out‑of‑sample. There is no broad consensus that regime‑adaptive parameters *always* beat fixed ones; the edge depends heavily on regime‑detection quality and the number of adaptive knobs. [papers.ssrn](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3997837)

> **Verdict:** [PLAUSIBLE — REASON: Well‑designed regime‑adaptive systems can improve risk‑adjusted returns in specific studies, but they also carry overfitting risk; benefits are not guaranteed without rigorous out‑of‑sample validation.]

***

> **Claim:** *“Stop loss distance should adapt to volatility: wider in high-vol, tighter in low-vol (ATR-based stops naturally do this).”*

> **Reasoning:**  
> Practitioner and educational sources emphasize that ATR‑based stops scale with volatility—widening in high‑vol regimes and tightening in low‑vol—and that fixed‑percent stops can be overly tight in volatile names and overly loose in calm ones. A thesis‑level study on stop‑loss mechanisms in trading finds that volatility‑scaled exits can materially change drawdown and risk characteristics, though results are sensitive to design and not uniformly superior for all systems. There is support for the logic of volatility‑scaled stops, but no universal conclusion that they always dominate fixed‑percent stops on a risk‑adjusted basis. [trendspider](https://trendspider.com/learning-center/atr-trailing-stops-a-guide-to-better-risk-management/)

> **Verdict:** [PLAUSIBLE — REASON: Volatility‑scaled (e.g., ATR‑based) stops are conceptually and empirically reasonable, but their superiority over fixed‑percent stops is strategy‑ and asset‑specific and must be validated.”

***

> **Claim:** *“Position sizing is the most important parameter to adapt to regime, more impactful than adjusting entry/exit rules.”*

> **Reasoning:**  
> Risk‑management literature and portfolio construction work (e.g., risk parity, volatility targeting) show that **position sizing and leverage adjustments** can strongly affect portfolio volatility, drawdowns, and Sharpe. However, there is no hard ranking of “importance” between sizing versus entry/exit parameters; edges and failure modes can originate from both. Some regime‑switching studies change entry rules, others change exposure; both levers matter, and their relative impact is system‑dependent. [priceactionlab](https://www.priceactionlab.com/Blog/2024/01/mean-reversion-and-momentum-regime-switching/)

> **Verdict:** [MISLEADING — CORRECTION: Position sizing is a highly impactful lever and a good candidate for regime adaptation, but research does not establish it as universally “most important” compared with adjusting entry/exit rules; both should be considered.]

***

> **Claim:** *“VIX < 20 / 20-30 / > 30 is the right tiering for regime classification.”*

> **Reasoning:**  
> CBOE and S&P educational material often refer to VIX levels below ~12 as low, above ~20 as high, and above ~30 as stressed, and practitioners commonly bucket VIX into low/normal/high zones for narrative purposes. But these boundaries are conventions based on historical U.S. equity experience, not statistically optimized cutoffs for trading performance, and recent research highlights the value of *percentile* or *model‑based* volatility regimes instead of fixed integers. [spglobal](https://www.spglobal.com/spdji/en/education-a-practitioners-guide-to-reading-vix.pdf)

> **Verdict:** [MISLEADING — CORRECTION: VIX tiers like <20 / 20–30 / >30 are reasonable descriptive categories, but not demonstrably “right”; for regime‑adaptive systems, continuous scaling or percentile‑based regimes are often more robust and should be tested.]

***

> **Claim:** *“Momentum lookback periods should shorten in fast-moving markets and lengthen in slow-moving markets.”*

> **Reasoning:**  
> Some work examines **short‑term vs long‑term momentum** and finds that different horizons add diversification, but does not provide a widely accepted scheme for dynamically shortening or lengthening lookbacks based on volatility or “speed”. There is little published evidence that adaptive lookbacks systematically outperform well‑chosen fixed horizons once transaction costs and model risk are considered. [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0378426614003252)

> **Verdict:** [UNVERIFIED — NEEDS: An explicit comparison of adaptive‑lookback momentum rules (where window length is a function of volatility or regime) versus fixed‑lookback benchmarks across long samples and multiple markets.]

***

> **Claim:** *“More than 2-3 regime-adaptive parameters crosses into overfitting territory for a retail swing trading system.”*

> **Reasoning:**  
> Overfitting risk clearly increases with the number of free parameters, especially in low‑signal domains like short‑term trading, but there is no formal research that sets a hard limit such as “2–3 adaptive parameters = OK; 4+ = overfitting”. Best practice guidance suggests limiting degrees of freedom, using cross‑validation, and favoring simpler models, but not a specific numeric cap of adaptive rules. [rpc.cfainstitute](https://rpc.cfainstitute.org/research/cfa-digest/2016/06/does-academic-research-destroy-stock-return-predictability-digest-summary)

> **Verdict:** [UNVERIFIED — NEEDS: A meta‑analysis or simulation study relating number of adaptive parameters to out‑of‑sample degradation specifically for retail‑scale swing systems; current literature only provides qualitative guidance.]

***

## PROMPT 5: What Separates Successful Quant Systems from Failures

> **Claim:** *“The top 5 reasons systematic trading systems fail in live trading are: overfitting, transaction costs, regime change, execution slippage, and behavioral deviation from rules.”*

> **Reasoning:**  
> Research on the “disappearing” of anomalies and strategies often points first to **data‑snooping/overfitting** and failure to account for realistic costs as key reasons paper edges vanish in live trading. Transaction costs and slippage are widely documented as critical, especially for high‑turnover strategies; even for lower turnover, ignoring them can materially bias backtests. Regime change (e.g., factor performance shifts post‑2010) and human behavioral deviations from rules are also frequently cited in practitioner and behavioral finance literature. But there is no canonical ranking that formally identifies these *exact five* as the “top” causes across all systems. [stratzy](https://stratzy.in/blog/untitled-13/)

> **Verdict:** [PLAUSIBLE — REASON: These five are well‑supported as major failure modes in both academic and practitioner discussions, but there is no definitive empirical ranking; other issues (e.g., model mis‑specification, data/implementation errors) can also be primary causes.]

***

> **Claim:** *“Walk-forward testing is sufficient to prevent overfitting.”*

> **Reasoning:**  
> Data‑snooping and model‑validation literature emphasizes that **no single technique**, including walk‑forward analysis, is sufficient by itself to guarantee robustness; overfitting can still occur if many models or parameter sets are tried and only the best is reported. Robust workflows combine multiple safeguards: cross‑validation, parameter stability checks, reality‑checked economic logic, minimum trade counts, and often out‑of‑sample + out‑of‑time testing. [thesis.dial.uclouvain](https://thesis.dial.uclouvain.be/entities/masterthesis/61e583f3-a6f1-4765-8174-dbb333b07590)

> **Verdict:** [MISLEADING — CORRECTION: Walk‑forward testing is a useful tool but not sufficient alone to prevent overfitting; it must be combined with other safeguards (cross‑validation, robustness checks, realistic costs, and conservative degrees of freedom).]

***

> **Claim:** *“Simpler trading systems (fewer parameters, fewer factors) outperform more complex ones out-of-sample.”*

> **Reasoning:**  
> Portfolio and forecasting research often finds that **simple or naive models** (e.g., equal‑weight, limited parameter sets) perform competitively with or better than highly optimized complex models out‑of‑sample due to overfitting risk, especially when data is limited. That said, complexity can add value when justified by strong signal and sufficient data; there is no universal theorem that “simpler always wins.” [nature](https://www.nature.com/articles/s41599-024-03888-4)

> **Verdict:** [PLAUSIBLE — REASON: Evidence supports a practical “simplicity premium” in many settings, but simpler is not guaranteed to outperform in every case; optimal complexity is context‑dependent, and this claim should be treated as a strong heuristic, not a law.]

***

> **Claim:** *“For a swing system doing 1-5 trades/week in stocks with $10M+ daily volume, transaction costs and slippage are negligible (<5 bps per trade).”*

> **Reasoning:**  
> Transaction cost and execution literature shows that slippage and costs depend on spreads, volatility, order type, and broker/venue; they can be low for liquid, large‑cap names and modest trade sizes, but even then, spreads and small price impacts add up. There is no generic guarantee that costs are <5 bps per trade; many brokers and market conditions will produce higher total frictions, especially if using market orders in volatile periods. [analystprep](https://analystprep.com/study-notes/cfa-level-iii/implications-involving-cost/)

> **Verdict:** [UNVERIFIED — NEEDS: Empirical measurement of your actual effective costs using your broker and order types (e.g., comparing execution price vs mid‑quote) to validate whether <5 bps is realistic; literature only provides directional guidance, not this universal bound.]

***

> **Claim:** *“Factors that worked in 2010-2020 (momentum, value, quality) continue to work in 2020-2026 with similar magnitude.”*

> **Reasoning:**  
> Analyses of factor performance show that **momentum and some quality/profitability factors** remained effective in the 2010s, but classic value (and some low‑vol and dividend factors) severely underperformed, leading to discussions of “factor alpha decay.” More recent reports indicate continued cyclicality and, in some cases, further pressure on traditional value and quality spreads, while momentum has generally held up better but with drawdown episodes. There is no strong evidence that factor premia from 2010–2020 carried through 2020–2026 with *similar magnitudes*; if anything, dispersion and crowding have changed their realized performance. [nomuranow](https://www.nomuranow.com/portal/site/nnextranet/en/IWM/resources/files/cio-corner/CIO-Office-Perspective/2025-05-27/Why%20Momentum%20Investing%20Has%20Dominated%20the%20Past%20DecadeAnd%20Why%20Your%20Portfolio%20Needs%20It.pdf)

> **Verdict:** [MISLEADING — CORRECTION: While some factors (especially momentum and certain profitability measures) remain positive, value and parts of quality have experienced significant headwinds; factor premia in 2020–2026 are not simply a continuation of 2010–2020.]

***

> **Claim:** *“A retail swing trader should NOT try to compete on: intraday mean-reversion, statistical arbitrage, high-frequency market making, or options flow trading because these require institutional infrastructure.”*

> **Reasoning:**  
> HFT, intraday stat‑arb, and options‑flow‑driven microstructure strategies generally require colocation, ultra‑low latency, large data feeds, and sophisticated infrastructure, which are well‑documented as being dominated by institutional players. Retail traders face higher latency, higher relative costs, and less access to raw order‑flow data, making it extremely hard to sustain an edge in those domains. That said, some intraday mean‑reversion strategies with lower frequency and larger holding periods may be implementable by retail, so the boundary is fuzzy rather than absolute. [msci](https://www.msci.com/downloads/web/msci-com/research-and-insights/paper/factor-indexing-through-the-decades/factor-indexing-through-the-decades.pdf)

> **Verdict:** [PLAUSIBLE — REASON: Competing directly with institutional HFT/stat‑arb/flow‑trading is realistically out of reach for retail; focusing on slower, less infrastructure‑intensive edges is better supported by structural considerations.]

***

> **Claim:** *“The minimum viable evidence-based swing trading system for retail is: 2-3 factors (momentum + trend + regime filter), equal-weighted, with ATR-based stops and 7% max loss, rebalanced weekly.”*

> **Reasoning:**  
> The suggested architecture aligns with many robust design principles: use of momentum/trend, a simple regime filter (e.g., index > 200‑day MA), volatility‑scaled stops, and limited complexity with equal weighting. However, “minimum viable” and this exact configuration (2–3 factors, weekly rebalance, 7% cap) are design choices; no published study identifies this specific combination as the unique or minimal evidence‑based template for retail swing trading. [quantifiedstrategies](https://www.quantifiedstrategies.com/200-day-moving-average/)

> **Verdict:** [UNVERIFIED — NEEDS: A transparent backtest and robustness analysis comparing this simple template to alternative minimal designs (e.g., pure momentum + regime, different rebalance frequencies, different stop rules) to justify it as the preferred minimum viable architecture for your constraints.]