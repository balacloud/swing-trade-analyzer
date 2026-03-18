# External LLM Audit Prompts — Swing Trade Analyzer

**Created:** 2026-03-17 (Day 68)
**Purpose:** Feed these prompts to external LLMs (Perplexity, GPT, Gemini) for independent validation of our system's logic against academic research and established trading methodologies.

**Workflow:**
1. Copy each prompt section below
2. Paste into the target LLM
3. Collect responses
4. Bring back to Claude for synthesis and action plan

| Prompt | Module | Recommended LLM |
|--------|--------|-----------------|
| 1 | Categorical Assessment & Verdict Logic | Perplexity (best for research citations) |
| 2 | Support & Resistance Module | Perplexity or GPT Deep Research |
| 3 | Pattern Detection Module | Perplexity (can verify against O'Neil/Minervini books) |
| 4 | Sector Rotation & RRG Logic | GPT (good for RRG methodology) |
| 5 | 9-Criteria Binary Checklist | Any — most criteria are well-documented |

---

## PROMPT 1: Categorical Assessment & Verdict Logic

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), say so.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: Specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

---

## SYSTEM UNDER AUDIT: Categorical Assessment Engine for Swing Trading

### What It Does
A swing trade recommendation system that replaces numerical scoring (which showed
0.011 score-to-return correlation) with categorical assessments across 4 dimensions.
The system works as a FILTER (pass/fail), not a RANKER.

### The 4 Assessment Dimensions

**1. Technical Assessment**
- Strong: Minervini 8-point Trend Template >= 7/8 AND RSI(14) 50-70 AND
  52-week Relative Strength vs SPY >= 1.0
- Decent: Trend Template >= 5/8 AND RSI 40-80
- Weak: Below thresholds

**2. Fundamental Assessment**
- Strong: 2 of 3 metrics strong (ROE > 15%, Revenue Growth > 10%,
  Debt/Equity < 1.0) with 0 weak
- Decent: Mixed (1 strong or all moderate: ROE 8-15%, RevGrowth 0-10%, D/E 1.0-2.0)
- Weak: 2+ metrics weak (ROE < 8%, negative growth, D/E > 2.0)

**3. Sentiment (Fear & Greed Index)**
- Strong: 60-80 (greed but not extreme)
- Neutral: 35-60 (expanded zone to eliminate cliff at 45)
- Weak: <35 (fear) or >80 (extreme greed, contrarian risk)

**4. Risk/Macro**
- Favorable: VIX < 20 AND SPY > 200 SMA
- Neutral: VIX 20-30 with SPY > 200 SMA
- Unfavorable: VIX > 30 OR SPY < 200 SMA
- Early bear cap: If SPY 50 SMA declining, Favorable → Neutral

### Verdict Logic
- BUY: 2+ Strong categories + Favorable/Neutral Risk + ADX >= 20
- HOLD: Mixed signals, ADX < 20 (no trend), or Unfavorable risk overrides
- AVOID: Weak Technical (non-negotiable) OR Weak Fundamental with no offsetting strength

### Holding Period Signal Weighting
- Quick (5-10 days): 70% Technical / 30% Fundamental
- Standard (15-30 days): 50/50
- Position (1-3 months): 30% Technical / 70% Fundamental

### ADX Entry Preference
- ADX >= 25: Momentum entry viable
- ADX 20-25: Pullback preferred
- ADX < 20: HOLD regardless of other signals (no trend)

### Backtest Results (2020-2024, walk-forward validated)
- Config C (Full 3-layer): 238 trades, 53.78% WR, PF 1.61, Sharpe 0.85, p=0.002
- Walk-forward: Out-of-sample outperforms in-sample

---

## QUESTIONS TO AUDIT (answer each with verdict label):

1. **Trend Template 7/8 threshold for "Strong"**: Is Minervini's 8-point trend
   template at 7/8 a reasonable threshold for institutional-quality setups?
   What does the literature say about the predictive power of trend template criteria?

2. **RSI 50-70 as "optimal pullback range"**: We use RSI 50-70 for Strong technical.
   Is this supported by research? Why not 40-60 or 50-80?

3. **Fear & Greed 60-80 as "Strong" sentiment**: We call F&G 60-80 bullish for
   momentum. Is there research supporting that moderate greed (not extreme) is
   optimal for swing trade entries?

4. **F&G neutral zone 35-60**: We expanded from 45-55 to 35-60 to "eliminate cliff
   at 45." Is a wider neutral zone empirically justified? What does contrarian
   indicator research say about these thresholds?

5. **VIX < 20 for "Favorable"**: Is VIX 20 the right threshold? Academic research
   on VIX regime thresholds — what levels are empirically significant?

6. **SPY 50 SMA declining as early bear signal**: We cap Risk at Neutral when SPY
   50 SMA is declining even if SPY > 200 SMA. Is this a known indicator?
   Does research support using 50 SMA slope as a leading bear indicator?

7. **ADX < 20 = no trade**: We HOLD on all signals when ADX < 20 regardless of
   categorical strength. Is ADX 20 the empirically validated threshold for
   "no trend"? What does Wilder's original research and subsequent studies say?

8. **Score-to-return correlation of 0.011**: We claim our original 75-point
   numerical scoring had essentially zero predictive power (r=0.011). Is this
   consistent with what academic literature says about composite stock scoring
   systems and their predictive ability?

9. **Holding period weighting (70/30 split)**: We weight Technical 70% for quick
   swings and Fundamental 70% for position trades. Is there research supporting
   that technical signals dominate short-term and fundamentals dominate long-term?
   We cite arXiv 2512.00280 — verify if this paper exists and supports this claim.

10. **"System as FILTER not RANKER"**: We abandoned ranking stocks by score in favor
    of binary pass/fail filtering. Is this approach supported by trading system
    design literature (Van Tharp, etc.)?
```

---

## PROMPT 2: Support & Resistance Module

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), say so.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: Specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

---

## SYSTEM UNDER AUDIT: Support & Resistance Detection Engine

### What It Does
Detects support and resistance levels using a multi-method approach with failover:

### Method 1: Pivot-Based Detection (Primary)
- Uses scipy.signal.argrelextrema to find local highs/lows
- Parameters: left=5, right=5 bars for pivot confirmation
- Minimum spacing: 0.25% of price between levels
- Maximum 5 levels per side

### Method 2: Agglomerative Clustering (Secondary)
- Replaced KMeans clustering (Day 30)
- Uses sklearn AgglomerativeClustering with distance_threshold (adaptive cluster count)
- Input: ZigZag-filtered pivot points (5% minimum price change threshold)
- Touch-based scoring: Levels ranked by historical price touches
- Claims 100% detection rate (was 80% with KMeans)

### Method 3: Volume Profile (Tertiary)
- Identifies high-volume price zones as support/resistance magnets
- 40 bins across price range

### Multi-Timeframe Confluence (MTF)
- Computes S&R on both daily AND weekly timeframes
- A level is "confluent" if it appears on both timeframes
- Confluence badge shows % of levels confirmed by weekly data
- Claims "3.2x stronger predictive power" for confluent levels

### Trade Setup Generation
- Conservative Entry: Wait for pullback to support
- Aggressive Entry: Enter at current price
- Stop Loss: Entry - (2 x ATR) with min floor of $0.01
- Target: Nearest resistance above entry
- Risk/Reward ratio calculated from these

### ATR Calculation
- Uses Wilder's EMA ATR (exponential smoothing), 14-period
- Applied to stop loss placement: 2 ATR below entry

### Key Parameters
- Proximity thresholds: Support 20%, Resistance 30% of ATR
- ZigZag threshold: 5% minimum price change
- ATR period: 14

---

## QUESTIONS TO AUDIT:

1. **Agglomerative vs KMeans for S&R**: Is agglomerative clustering with
   distance_threshold a better approach than KMeans for price level detection?
   What does the quantitative finance literature say about clustering methods
   for S&R identification?

2. **ZigZag 5% threshold**: We use 5% minimum price change to filter noise in
   pivot detection. Is 5% empirically justified for daily timeframe swing trading?
   Should this be volatility-adaptive (e.g., ATR-based) instead of fixed?

3. **Touch-based scoring**: We rank S&R levels by number of historical price
   touches. Is this approach supported by market microstructure research?
   Are more-touched levels actually stronger?

4. **MTF Confluence "3.2x stronger predictive power"**: We claim confluent
   levels (appearing on both daily and weekly) are 3.2x more predictive.
   Can you find the source for this claim? Is MTF confluence for S&R
   empirically validated?

5. **2 ATR stop loss**: We place stops at Entry - 2xATR(14). Is 2 ATR a
   well-researched stop distance for swing trades? What does the literature
   suggest? Too tight? Too wide?

6. **Support proximity 20% of ATR, Resistance 30% of ATR**: We use different
   proximity thresholds for support vs resistance. Is there research suggesting
   asymmetric proximity is appropriate?

7. **Weekly resampling using W-FRI**: We resample daily OHLCV to weekly using
   Friday as the week boundary. Is this standard practice? Does the choice of
   week boundary affect S&R quality?

8. **Minimum 150 bars requirement**: We require 150 daily candles minimum for
   S&R computation. Is this sufficient for reliable level detection in swing
   trading context? Too many? Too few?
```

---

## PROMPT 3: Pattern Detection Module

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), say so.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: Specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

---

## SYSTEM UNDER AUDIT: Chart Pattern Detection Engine

### Patterns Detected

**1. VCP (Volatility Contraction Pattern) — Mark Minervini**
- Looks for successive contractions in price range (each tighter than previous)
- Requires minimum 2 contractions
- Base tightness measured as percentage range
- Pivot price = last swing high
- Gate condition: ranges must be decreasing AND base must be tight
- Breakout quality: High/Medium/Low based on volume confirmation
- Volume ratio checked against 50-day average

**2. Cup & Handle — William O'Neil**
- Cup detection: V or U shaped recovery over 30-180 days
- Cup depth: typically 15-33% (we accept wider range)
- Handle: 5-25 day consolidation after right lip of cup
- Handle constraint: handle_high <= right_lip x 1.02 (handle must stay below lip)
- Uses recent 180-day price slice with iloc on that slice (not full DataFrame)
- Pivot price: handle high or right lip
- Breakout: price above pivot with volume confirmation

**3. Flat Base — Consolidation Pattern**
- Range: tight consolidation (typically < 15% range)
- Duration: 20-65 days
- Requires prior uptrend (minimum 20% advance)
- Pivot: top of consolidation range
- Breakout: price above range with volume

### Trend Template (Minervini's 8-Point)
- 8 binary criteria checked:
  1. Price > 200 SMA
  2. 200 SMA trending up (over 22 days)
  3. Price > 150 SMA
  4. 150 SMA > 200 SMA
  5. Price > 50 SMA
  6. 50 SMA > 150 SMA
  7. Price within 25% of 52-week high
  8. Price at least 25% above 52-week low

### Confidence Scoring
- Each pattern has a confidence score (0-100%)
- Actionability threshold: >= 60% (was 80%, lowered after backtesting showed
  Config C at 60% produced: 238 trades, 53.78% WR, PF 1.61, p=0.002)
- Patterns below 60% shown in "below threshold" section for transparency

---

## QUESTIONS TO AUDIT:

1. **VCP detection logic**: We detect VCPs by checking that successive price
   contractions decrease in range. Is this faithful to Minervini's original
   description? Are we missing any key VCP characteristics
   (e.g., volume dry-up at pivot)?

2. **Cup & Handle handle_high <= right_lip x 1.02**: We allow handle to be at
   most 2% above the cup's right lip. Is this consistent with O'Neil's original
   criteria? What does the literature say about acceptable handle depth/height?

3. **Cup depth acceptance range**: O'Neil specifies 15-33% cup depth for ideal
   patterns. What range do we actually accept? Is our range too permissive?

4. **Flat Base range < 15%**: We define flat base as < 15% price range during
   consolidation. Is this threshold consistent with O'Neil/IBD methodology?
   IBD typically says 10-15%.

5. **60% confidence threshold**: We lowered from 80% to 60% after backtesting
   showed better results. Is this a valid approach (optimizing threshold on
   backtest data)? What is the risk of overfitting the threshold?

6. **Trend Template 8 criteria**: Are our 8 criteria faithful to Minervini's
   published SEPA methodology? Compare against "Trade Like a Stock Market Wizard"
   chapter on Trend Template.

7. **Volume confirmation on breakout**: How does our implementation check for
   volume surges? Is volume_ratio against 50-day average the standard approach?

8. **Algorithmic pattern detection reliability**: What does academic research
   say about the reliability of algorithmic chart pattern detection vs. human
   identification? Are there known failure modes?

9. **Prior uptrend requirement for Flat Base**: We require a 20% prior advance.
   Is this consistent with IBD's flat base criteria? What's the standard
   minimum prior advance?
```

---

## PROMPT 4: Sector Rotation & RRG Logic

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), say so.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: Specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

---

## SYSTEM UNDER AUDIT: Sector Rotation Module with RRG Quadrants

### What It Does
Tracks 11 SPDR sector ETFs (XLK, XLF, XLV, XLI, XLY, XLP, XLE, XLB, XLU, XLRE, XLC)
and ranks them by Relative Strength vs SPY.

### RS Ratio Calculation
- Formula: RS_line = ETF_close / SPY_close (daily ratio over 6 months)
- Normalization: RS_normalized = (RS_line / RS_line[midpoint]) x 100
  - Uses MIDPOINT of 6-month period as baseline (not start)
  - RS = 100 means at parity with SPY
  - RS > 100 = outperforming, RS < 100 = underperforming

### RS Momentum
- Change in RS_normalized over last 10 trading days
- Positive = gaining strength, Negative = losing strength

### RRG (Relative Rotation Graph) Quadrants
- Leading: RS >= 100 AND Momentum >= 0 (strong & gaining)
- Weakening: RS >= 100 AND Momentum < 0 (strong but fading)
- Lagging: RS < 100 AND Momentum < 0 (weak & falling)
- Improving: RS < 100 AND Momentum >= 0 (weak but recovering)

### Cap-Size Rotation Strip
- Tracks QQQ (Large Cap Growth), MDY (Mid Cap), IWM (Small Cap R2000)
- Size Signal: Risk-On if IWM RS > QQQ RS + 2, Risk-Off if QQQ RS > IWM RS + 2

### Integration with Trade Decisions
- Sector column appears in scan results with quadrant color
- "Scan for Rank #1 Sector" filters to top-performing sector
- Scan buttons appear only for Leading/Improving sectors
- Context only — does NOT modify BUY/HOLD/AVOID verdicts

---

## QUESTIONS TO AUDIT:

1. **RS normalization at midpoint vs start**: We normalize RS to 100 at the
   midpoint of our 6-month window (not the start). Is this standard for RRG
   implementations? The original RRG by Julius de Kempenaer uses what baseline?

2. **10-day momentum window**: We compute RS momentum as the 10-day delta in
   RS_normalized. Is 10 trading days the standard RRG momentum period?
   What does RRG literature recommend?

3. **RRG quadrant thresholds at exactly 100 and 0**: We use RS=100 and
   Momentum=0 as quadrant boundaries. Standard RRG implementations —
   do they use these same boundaries?

4. **6-month lookback period**: We use 6 months of daily data for RS calculation.
   Is this appropriate for swing trading timeframes? Too short? Too long?

5. **Cap-size rotation signal (+/-2 threshold)**: We call Risk-On when IWM-QQQ
   RS diff >= 2 and Risk-Off when <= -2. Is there research supporting specific
   thresholds for cap-rotation signals?

6. **11 SPDR sectors as universe**: Are the 11 GICS-based SPDR ETFs the
   standard choice for sector rotation analysis? Are we missing any important
   sectors or alternative ETF sets?

7. **Sector rotation as pre-flight context only**: We explicitly do NOT let
   sector rotation modify verdicts. Is this the right design choice, or should
   sector momentum influence BUY/HOLD/AVOID decisions?
```

---

## PROMPT 5: 9-Criteria Binary Checklist

```
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), say so.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: Specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with principles but not directly confirmed.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but misleading.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found.
- [HALLUCINATED — FLAG: <why fabricated>]: No basis, likely invented.

---

## SYSTEM UNDER AUDIT: 9-Criteria Binary Trading Checklist

### Philosophy
ALL 9 criteria must pass for a TRADE signal. Based on:
- Minervini SEPA methodology
- Academic momentum research (AQR, Fama-French)
- Turtle Trading principles
- Validated against holistic 3-layer backtest (Config C)

### The 9 Criteria

1. **TREND**: Price > 50 SMA > 200 SMA (Stage 2 uptrend)
2. **MOMENTUM**: 52-week Relative Strength vs SPY >= 1.0
3. **SETUP**: Stop loss within 7% of entry price
4. **RISK/REWARD**: R:R ratio >= 2:1
5. **52-WEEK RANGE**: Price in top 25% of 52-week range (>= 75th percentile)
6. **VOLUME**: Average daily dollar volume >= $10 million
7. **ADX**: ADX(14) >= 20 (confirmed trend)
8. **MARKET REGIME**: SPY > 200 SMA (bull market filter)
9. **200 SMA TREND**: Stock's 200 SMA rising over past 22 trading days

### Verdict
- ALL 9 pass = TRADE (high probability setup)
- 7-8 pass = PASS with "close but missing: [X, Y]"
- < 7 pass = PASS (no trade)

---

## QUESTIONS TO AUDIT:

1. **All-or-nothing approach**: Requiring ALL 9 criteria is extremely
   selective. What does system design literature say about requiring
   100% pass vs. weighted scoring? Does this lead to too few signals?

2. **7% stop distance threshold**: We require stop within 7% of entry.
   Is 7% empirically justified for swing trades? What stop distances
   do Minervini and O'Neil actually recommend?

3. **R:R >= 2:1 minimum**: Is 2:1 the right minimum? Academic literature
   on risk/reward ratios in swing trading — what's the consensus?

4. **Top 25% of 52-week range**: Minervini requires stocks near highs.
   Is top 25% (>= 75th percentile) the right threshold? What does
   Minervini specifically require?

5. **$10M daily dollar volume**: We require $10M+ daily dollar volume.
   Is this appropriate for retail swing traders? What thresholds do
   Minervini/O'Neil recommend for liquidity?

6. **SPY > 200 SMA as market regime**: We use SPY > 200 SMA as bull/bear
   filter. Is this the standard approach? Are there better regime filters
   (e.g., Breadth indicators, SPY > 50 SMA, etc.)?

7. **200 SMA rising over 22 trading days**: We check that the stock's
   200 SMA is rising over the past ~1 month. Is this Minervini's actual
   criterion? Does he specify 22 days?

8. **ADX >= 20 as trend confirmation**: Wilder's original threshold vs.
   modern research — is 20 still the right number, or has market
   structure evolution changed optimal ADX thresholds?

9. **RS >= 1.0 (parity with SPY)**: We require RS at or above parity.
   Minervini and O'Neil typically want stocks outperforming significantly
   (top quartile RS). Is >= 1.0 too permissive?
```

---

## After Collecting Responses

Bring all 5 LLM responses back to Claude and say:

```
Here are the external audit results for our 5 modules. Please:
1. Synthesize all findings into a single action plan
2. Separate into: (a) Must-fix (logic errors), (b) Should-improve (suboptimal but functional), (c) Acknowledged (known tradeoffs we accept)
3. For each Must-fix, propose the specific code change
4. Flag any conflicting opinions between LLMs
```


## Response from GPT 

Prompt 1: Categorical Assessment & Verdict Logic
Trend Template 7/8 threshold for “Strong”: [MISLEADING — Correction: Mark Minervini’s original 8-point trend template required all eight criteria to define a confirmed Stage-2 uptrend
. Relaxing it to 7/8 weakens this strict filter. We found no independent study showing that meeting 7 of 8 yields institutional-quality signals. In fact, Minervini himself emphasized all eight criteria must pass, so a 7/8 rule is a heuristic relaxation, not a validated enhancement. No academic research was found quantifying predictive power of partial trend-template compliance.]
RSI 50–70 as “optimal pullback range”: [PLAUSIBLE — Reasoning: Many traders interpret RSI >50 as bullish and approaching 60 as strengthening momentum
. We did not find academic papers specifically identifying 50–70 as optimal. Standard technical literature marks 30/70 for oversold/overbought. Using 50–70 is a reasonable heuristic (it ensures the stock isn’t oversold or overextended) but lacks formal research validation. Other ranges (e.g. 40–60 or 50–80) would also be arbitrary; we simply found no studies that clearly favor 50–70 over alternatives.]
Fear & Greed 60–80 as “Strong” sentiment: [PLAUSIBLE — Reasoning: Sentiment studies show extremes matter: very high F&G (>80) often signal topping (short-term negative returns) and very low (<20) signal reversals
. Moderate greed (60–80) is not extreme, so it’s plausible to favor it. We found no formal research that calls exactly 60–80 a sweet spot, but one analysis notes that F&G above 80 increases short-term reversal risk
. Thus avoiding extremes is sensible, but the 60–80 window is largely a practitioner’s rule rather than a statistically proven boundary. (In other words, no academic paper prescribes 60–80; it’s a heuristic that avoids “extreme greed”.)]
F&G neutral zone 35–60: [MISLEADING — Correction: CNN’s Fear & Greed Index typically defines neutral roughly as 46–55
. Expanding neutral to 35–60 departs from this convention. We found no empirical study justifying such a broad neutral band. Sentiment research generally highlights only extremes (fear vs greed). Widening the neutral zone to 35–60 is a heuristic to avoid category flips, but it isn’t backed by published evidence. In fact, sources list “fear” as 25–45 and “greed” as 56–75
, so 35–60 spans two traditional zones and lacks academic support.]
VIX < 20 for “Favorable”: [VERIFIED — Source: Analysts often use VIX 20 as a volatility regime threshold. For example, S&P’s practitioner guide notes VIX above 20 is considered “high” volatility (with below-12 low, 12–20 moderate)
. Thus VIX<20 is a common cut-off indicating a calmer market. We saw multiple industry sources treating VIX ~20 as the bull/bear threshold. This aligns with our filter (VIX<20 = favorable) and is consistent with both practice and commentary from market professionals
.]
SPY 50 SMA declining as “early bear” signal: [UNVERIFIED — Needs evidence: We found no published research on using the 50-day SMA slope as a standalone bear warning. Intuitively, a falling 50-day MA suggests short-term weakness even if SPY>200. However, most studies focus on crossovers (e.g. the 50/200 “death cross”) rather than the slope of the 50-SMA itself. We did not find academic or official technical references endorsing the 50-day MA trend as a leading bear indicator, so this rule appears to be a trading heuristic without documented validation.]
ADX < 20 means “no trend”: [VERIFIED — Source: Wilder’s original ADX interpretation and later technical guides agree: ADX values below about 20 indicate a non-trending or sideways market
. For example, Investopedia explains that “below 20” generally signals a range-bound market
. Therefore using ADX <20 as a no-trade condition is consistent with both Wilder’s guidance and industry usage.]
Score-to-return correlation ~0.011: [MISLEADING — Correction: Many empirical trading studies (e.g. Piotroski’s F-score, multi-factor screens) show that composite rating systems can generate above-market returns
. A near-zero correlation suggests our scoring method is not capturing those known effects. The literature does not say composite scores should have zero predictive power; quite the opposite, systematic value/momentum screens often beat the market. Thus claiming “essentially zero predictive power” conflicts with published evidence that well-designed score-based strategies can work. It implies our score may be poorly calibrated rather than a universal truth.]
Holding period weighting (70/30 split): [VERIFIED — Source: Recent research supports the idea that short-horizon moves are driven by technical/momentum factors, whereas long-horizon returns reflect fundamentals. For instance, a Dec 2025 preprint (arXiv:2512.00280) finds that short-term investors rely on technical signals and sentiment, while long-term investors focus on fundamentals
. This matches our weighting (technical emphasis for 5–10-day swings, fundamental emphasis for months). The paper explicitly notes that “short-horizon investors operate on technical signals… long-horizon on fundamental information”
.]
System as FILTER not RANKER: [PLAUSIBLE — Reasoning: The literature on system design stresses using strict filters as a first step. For example, Yuval Taylor advises applying absolute rules (filters) to winnow the universe before ranking the remainder
. This suggests filtering (pass/fail screens) is indeed a recognized practice. We found no sources saying that scoring/ranking must be used. In fact, experts recommend filtering to remove undesirable candidates up front
. Thus treating the model as a binary filter is consistent with that advice, though many strategies still rank the survivors for final selection. No academic paper directly compares filter-vs-rank, but practitioner guidance supports heavy filtering first.]
Prompt 2: Support & Resistance Module
Agglomerative vs KMeans for S&R: [PLAUSIBLE — Reasoning: We found no quantitative finance study on clustering S/R levels. In generic data science, Agglomerative clustering is known to handle clusters of irregular size and doesn’t require specifying the number of clusters upfront
. KMeans requires fixing K and assumes similar-shaped clusters. For price levels (unknown count, potentially uneven spacing), Agglomerative is a reasonable choice. While no trading research compares them, using a distance-threshold agglomeration is consistent with best practices for unsupervised detection of unknown cluster count
.]
ZigZag 5% threshold: [UNVERIFIED — Needs evidence: We found no academic justification for exactly 5%. This parameter is typically chosen ad hoc to smooth noise. Some charting studies suggest linking breakouts to volatility metrics, but there is no canonical fixed-percent rule. Using a fixed 5% on daily data is a heuristics; one could argue ATR-based thresholds would adapt to volatility better, but we found no research dictating the optimal level. Without published guidance, this remains an arbitrary, backtest-chosen parameter.]
Touch-based scoring: [VERIFIED — Source: Technical analysis guides explicitly say that repeated tests strengthen a level. For example, a capital markets educational site notes: “The more times a zone has been tested and held… the more reliable it becomes”
. In other words, S/R levels with more historical touches are traditionally viewed as stronger. We found this principle widely stated in TA literature, even if not in academia. Thus scoring by touches is supported by common technical wisdom
.]
MTF Confluence “3.2× predictive power”: [UNVERIFIED — Needs evidence: We could not find any source for a “3.2×” figure or rigorous analysis of MTF confluence. Multi-timeframe confirmation is a popular concept, but no academic paper was found claiming a quantitative multiplier for confluence. This specific claim appears to be internal or anecdotal. In short, we found no published validation that daily+weekly confluence yields exactly 3.2 times higher predictivity, so this number must be treated as unsubstantiated.]
2×ATR stop loss: [VERIFIED — Source: Using multiples of ATR for stops is a standard technique. Wilder’s ATR-based stop rules often employ 2× or 3× ATR. For example, one trading platform explains that an ATR-based trailing stop typically multiplies ATR by 2 or 3 to set the stop distance
. This matches our use of 2×ATR. The literature on volatility stops commonly cites 2×ATR as a balanced choice (neither too tight nor too loose), so our stop rule is well within conventional practice
.]
Support proximity 20% ATR vs resistance 30% ATR: [UNVERIFIED — Needs evidence: We found no research suggesting asymmetry between support and resistance proximity thresholds. Using 20% ATR for support and 30% for resistance is a heuristic choice. The idea might be that one expects bounces closer to support and breakouts need more space, but this distinction isn’t documented in technical literature. Without empirical backing, the specific 20%/30% split appears arbitrary. No source was found arguing for such asymmetry, so this remains an implementation detail rather than a proven rule.]
Weekly resampling using Friday boundary: [UNVERIFIED — Needs evidence: We are unaware of any study on how the choice of weekly boundary affects S/R analysis. In practice, aggregating daily data into weekly (often ending on Friday) is a common convention, but the boundary choice is mostly arbitrary. The quality of identified levels should not significantly depend on whether weeks are taken Mon–Fri or Tue–Mon. We found no academic reference on this; it’s likely a minor modeling choice. Thus we mark it unverified, as no evidence was found that boundary choice materially changes S/R detection.]
Minimum 150 bars requirement: [UNVERIFIED — Needs evidence: There is no consensus on an “enough data” threshold. 150 daily bars (~7 months) seems minimal for swing trading, but is not a documented standard. Some analysts use longer histories (1–2 years) to capture major pivots. We did not find research specifying an optimal history length for S/R reliability. The appropriate lookback likely depends on trading style and instrument volatility. In short, 150 is a plausible minimum, but we found no studies to confirm it as sufficient or optimal.]
Prompt 3: Pattern Detection Module
VCP detection logic: [MISLEADING — Correction: Our VCP criteria emphasize shrinking price ranges, but Minervini’s original pattern also requires volume to dry up on each contraction. In his description, “volatility and volume gradually decrease” through the base
. We check contraction in range, but unless we explicitly enforce lower volume each leg, we miss a core aspect. Proper VCP screening should include declining volume with each contraction
. Without that, our VCP rule is incomplete per Minervini’s definition.]
Cup handle_high ≤ 1.02×right_lip: [PLAUSIBLE — Reasoning: O’Neil’s Cup & Handle rule is that the handle should not climb above the cup’s rim. Some sources say a slight breach is tolerable. We allowed up to +2% above the right lip. This is a reasonable compromise; we found no formal percentage given by O’Neil, but trading guides often impose similar small allowances. In practice, restricting the handle to just under the lip (or a few percent above) is common. Thus our 1.02 rule is in line with O’Neil’s loose guideline, albeit we couldn’t find a published exact limit beyond “not much above.”]
Cup depth acceptance range: [MISLEADING — Correction: O’Neil strongly prefers shallow cups. He suggests a typical depth of 15–33%, and ideally not more than 40%. We accept a wider range (implying deeper cups). This contradicts the ideal pattern definition. For example, one IBD summary says the cup “does not correct more than 10%–15%” in a flat base context
, and other sources say up to ~33% depth for a C&H. Allowing deeper cups risks poorer-quality patterns, so our criterion is too permissive compared to the original guidance. (No evidence supports including very deep cups.)】
Flat Base range < 15%: [VERIFIED — Source: This matches IBD’s rule of thumb. Flat bases are defined as tight consolidations (typically 5–8 weeks) that do not retrace more than 10–15%
. Our <15% range is exactly the standard O’Neil guideline (often quoted as “less than 10–15%”). Thus our threshold is faithful to the original methodology
.]
60% confidence threshold (vs 80%): [MISLEADING — Correction: Adjusting the confidence cutoff based on backtest results is a form of curve-fitting. Trading literature warns that optimizing parameters on historical data can overfit the strategy
. For example, one practitioner’s cautionary example shows that tuning filters to maximize a backtest yield produces a strategy that fails out-of-sample
. Lowering the threshold to get more trades may improve in-sample stats, but without separate validation it risks over-optimizing to the data. This is a serious data-mining concern. (We found no source advocating retuning confidence levels purely for backtest performance.)】
Trend Template 8 criteria fidelity: [MISLEADING — Correction: We have one discrepancy: Minervini’s published template requires price ≥30% above the 52-week low, whereas our code uses 25%
. In other words, we lowered his bar. He explicitly lists “Price at least 30% above its 52-week low”
. Using 25% weakens the requirement. Otherwise, our eight conditions match Minervini’s list. But this criterion should be 30% per the original SEPA formula, so 25% is not faithful to his rule.】
Volume confirmation on breakout: [PLAUSIBLE — Reasoning: We compare breakout volume to a 50-day average, which is a common approach. The literature does not mandate a specific multiplier, but many chartists use volume relative to recent average to confirm breakouts. For instance, some analysts look for volume at least 30–50% above normal. We found no official standard, but using a rolling average (50-day) is in line with typical practice. Thus our method (volume ratio vs 50-day MA) is reasonable though not the only valid technique.]
Algorithmic pattern detection reliability: [PLAUSIBLE — Reasoning: There is limited academic work on automated pattern recognition vs human. In general, algorithms offer consistency and backtestability, but may miss nuances. One expert article notes that algorithmic backtesting can quantify pattern reliability under various conditions
, suggesting automation improves objectivity. We found no formal study on error rates, but it’s understood that humans can spot irregular patterns and algorithms excel at volume. No clear quantitative failure modes were found in research; it’s accepted that algorithmic detection is imperfect but can be validated via backtesting
.]
Prior uptrend requirement (20%): [VERIFIED — Source: This aligns with O’Neil’s rule. A flat base typically comes after a substantial prior advance. For example, IBD notes a flat base usually follows a 20%+ move
. We require a 20% prior rise, which matches the standard (O’Neil often says at least a 20–25% uptrend before a base). Our criterion is consistent with published C&H/flat-base setups
.]
Prompt 4: Sector Rotation & RRG Logic
RS normalization at midpoint vs start: [MISLEADING — Correction: Standard RRG conventions normalize RS so that 100 represents parity with the benchmark
. The original RRG doesn’t use the midpoint of the lookback window; rather 100 is a fixed baseline (often based on a moving average or initial value). We found no RRG source using the midpoint as the normalization point. According to Julius deKempenaer, RS-Ratio values above 100 indicate outperformance and below 100 weakness
, implying 100 is the pivot, not the window midpoint. So midpoint normalization is a nonstandard choice, not documented in RRG literature. (No evidence supports using the midpoint as the 100-baseline.)】
10-day momentum window: [UNVERIFIED — Needs evidence: Traditional RRG uses a momentum indicator (JdK RS-Momentum) that is essentially the rate-of-change of the RS-Ratio, but its time constant is not specified as exactly 10 days in the literature. We found no official recommendation for a 10-day delta. Some implementations use a ~1-month ROC or similar. Without a source, this is a heuristic choice. We did not find RRG documentation prescribing a fixed 10-trading-day momentum period, so this appears to be a custom parameter.】
RRG quadrant thresholds at 100 and 0: [MISLEADING — Correction: In classic RRG charts, both RS-Ratio and RS-Momentum are normalized around 100, not 0. The quadrant boundaries are RS=100 and Momentum=100
. For example, RS-Momentum crossing above 100 signals improving relative performance
. Using a 0 threshold for momentum is not standard. Our implementation should treat momentum>100 as up and <100 as down. We found no precedent for using 0 in RRG; the literature consistently places the pivot at 100 for both axes. This discrepancy indicates our quadrant logic is off by 100 points.】
6-month lookback period: [UNVERIFIED — Needs evidence: There is no hard rule for the optimal lookback in RRG. Julius deKempenaer’s examples often use one year of data (52 weeks) for sector RRGs, but that’s not mandatory. A 6-month window is reasonable for shorter-term analysis, but we found no study saying 6 months is either ideal or insufficient. Whether 6 months is too short or too long depends on the desired sensitivity. In summary, the 6-month choice is arbitrary without a supporting citation; no academic or official RRG guideline mandates a specific window.】
Cap-size rotation signal (±2 threshold): [UNVERIFIED — Needs evidence: We found no empirical research setting a “+2” RS spread as a canonical risk-on/off trigger. Cap-rotation is a known concept, but no study defines a numeric gap. This appears to be a custom threshold. It is plausible that a large RS gap between IWM and QQQ signals risk mode, but a +/-2 cutoff is arbitrary. Without a source (e.g. academic paper) backing this exact value, we can only call it heuristic. The literature does not specify a particular RS point gap for such signals.】
11 SPDR sectors as universe: [VERIFIED — Source: Yes. Using the 11 GICS-based sector SPDR ETFs is standard practice. RRG analyses typically track all GICS sectors, e.g. XLK, XLF, XLV, XLI, XLY, XLP, XLE, XLB, XLU, XLRE, XLC. DeKempenaer and others often refer to “Sector SPDRs” explicitly
. Our list of 11 matches the common sector ETF set. No major US equity sector is omitted; this is the accepted universe for sector rotation.】
Sector rotation as context only (no verdict override): [UNVERIFIED — Needs evidence: We found no explicit source saying sector momentum must override stock signals. Many practitioners do incorporate sector strength (for example, focusing on stocks in leading sectors), but this is a design choice. The RRG literature describes how to visualize sector strength, not how to algorithmically fold it into buy/sell rules. Thus treating sector information as contextual only is not contradicted by a known reference. There is no citation that it must feed into the final trade signal, so we cannot call it verified or false. It’s a strategic choice rather than an empirically established rule.】
Prompt 5: 9-Criteria Binary Checklist
All-or-nothing approach: [PLAUSIBLE — Reasoning: We found no academic analysis of 100%-pass filters vs weighted scores. However, trading-system design literature generally cautions that requiring all criteria often produces very few signals. Experts like Van Tharp emphasize designing for a reasonable trade frequency. Our rule is extremely selective, which may drastically reduce opportunities. No source explicitly endorses 100% filters; in fact, many strategies use partial pass rules or point systems. While no paper directly addresses this, it’s reasonable to question whether requiring all 9 kills too many trades. We did not find any citation for or against 100% pass, so we classify it as plausible but potentially impractical.】
7% stop distance threshold: [VERIFIED — Source: The “7–8% rule” is well known from CAN SLIM and O’Neil’s teachings. For example, one review states that traders following O’Neil cut losses when a stock falls 7–8%
. O’Neil himself found most winners did not dip more than ~8% from buy points
. Thus a 7% stop is consistent with the conventional wisdom of Minervini and O’Neil, and is explicitly cited in trading guides as a risk-control rule
.]
R:R ≥ 2:1 minimum: [UNVERIFIED — Needs evidence: There is no universal academic consensus on minimum R:R, but 2:1 is a common rule-of-thumb. Many trading sources suggest targeting ≥2:1 to ensure positive expectancy given typical win rates. We found no scholarly study stating that 2:1 is optimal; it’s largely conventional wisdom. Without a specific research citation, we cannot verify that exactly 2:1 is scientifically “correct.” It’s a reasonable discipline (widely advised), but evidence is anecdotal rather than formally established.】
Top 25% of 52-week range (≥75th percentile): [VERIFIED — Source: Yes. Minervini requires stocks to be near their highs. In his trend template (and O’Neil’s criteria), a common rule is that price should be within 25% of the 52-week high
. Equivalently, this means price is in the top 25% of its range. Our threshold matches that guidance exactly. We confirmed this with a source listing “within 25% of high” as a criterion
.]
$10M daily dollar volume: [MISLEADING — Correction: We found no source that requires exactly $10M. O’Neil and others emphasize liquidity, but often in terms of shares (e.g. 400k shares) or smaller dollar amounts. A $10M/day threshold is higher than typical published cutoffs. For example, CAN SLIM says “average daily dollar volume in millions” but doesn’t give a fixed number. Many traders use $2–5M as a minimum. Requiring $10M seems more restrictive than any rule we found. No academic justification exists for $10M specifically. This criterion may screen out legitimate opportunities; it is not a documented standard.]
SPY > 200 SMA market regime: [VERIFIED — Source: Yes. Using the S&P (or SPY) above its 200-day SMA as a bull filter is a classic approach. Technical analysts widely apply this rule. For instance, Investopedia notes that a stock (or index) above its 200-day MA is generally considered in an uptrend
. Likewise, many trading systems (including O’Neil’s CAN SLIM) adopt the 200-day index filter. Our usage of SPY>200 as the bull market condition is in line with well-known practice
.]
200 SMA rising over 22 trading days: [VERIFIED — Source: This matches Minervini’s published template. He explicitly requires the 200-day MA to be rising (higher than it was 30 days ago)
. Our implementation checks that the 200-day SMA is up over ~22 days, which is essentially the same (about one trading month). Thus we are faithful to the original criterion
.]
ADX ≥ 20 as trend confirmation: [VERIFIED — Source: As noted above, ADX ≥20 indicating a trend is standard. Our previous answer covered this: ADX below ~20 is range-bound
. So requiring ADX≥20 is indeed in line with Wilder’s guidance and technical literature, which we confirmed with Investopedia
. (This is the same rationale as in Prompt 1.)]
RS ≥ 1.0 (parity): [MISLEADING — Correction: O’Neil and Minervini want stocks outperforming the market (often among the best). Requiring just RS≥1.0 means matching SPY’s performance, which is weaker than their intent. In RRG terms, RS=100 is merely parity. The creator of RRG notes that truly leading securities often have RS well above 100
. Thus ≥1.0 is too permissive by those standards. Research and practice suggest focusing on stocks with RS significantly above 1.0 (top quartile or decile), not merely equal to the index. Our threshold should be higher to align with the high-RS bias of these methodologies.

# Response from Gemini 

Gemini said
This audit evaluates the logic, mathematical consistency, and alignment with established financial literature for the provided trading system modules.

PROMPT 1: Categorical Assessment Audit
#	Question	Verdict	Reasoning
1	7/8 Trend Template	[PLAUSIBLE — REASON: Heuristic refinement]	While Minervini’s official SEPA® requirement is 8/8 for a "Stage 2" profile, a 7/8 threshold is a common implementation in screening software (e.g., MarketSmith) to catch names just before a perfect "Power Play" setup. Literature (Minervini, 2013) emphasizes the trend over the absolute count.
2	RSI 50-70 Range	[PLAUSIBLE — REASON: Bullish regime indicator]	Research by Andrew Cardwell suggests that in a bull market, RSI tends to find support at 40 and resistance at 80. The 50-70 range effectively filters for "momentum pullbacks" where the asset stays in the upper half of the range.
3	F&G 60-80 "Strong"	[VERIFIED — SOURCE: CNN Business / Investopedia]	CNN’s Fear & Greed Index classifies 60-75 as "Greed" and 75+ as "Extreme Greed." Momentum research (Baker & Wurgler, 2006) confirms that returns often persist during optimistic sentiment but face mean reversion risk in "Extreme" zones.
4	F&G Zone 35-60	[PLAUSIBLE — REASON: Noise reduction]	Expanding the neutral zone is a standard engineering technique to prevent "oscillation" (frequent flipping) at a single point (45). This reduces churn in the "Neutral" classification.
5	VIX < 20	[VERIFIED — SOURCE: CBOE Whitepapers]	The level of 20 is the long-term historical average. A VIX below 20 is empirically associated with lower realized volatility and higher probability of sustained equity uptrends (Whaley, 2000).
6	50 SMA Slope	[PLAUSIBLE — REASON: Momentum lead/lag]	A declining 50 SMA while price is above the 200 SMA is a classic "Negative Divergence" or a "Non-Confirmation." It indicates the intermediate-term momentum is slowing, even if the long-term trend is intact.
7	ADX < 20	[VERIFIED — SOURCE: Wilder, 1978]	J. Welles Wilder, the creator of ADX, explicitly stated in New Concepts in Technical Trading Systems that a reading below 20 indicates a non-trending, range-bound market.
8	0.011 Correlation	[PLAUSIBLE — REASON: Non-linearity]	Academic studies on "Composite Alpha Factors" often show very low linear correlation (R) to returns because market returns are non-linear and non-stationary. Binary filters often outperform linear scorers in noisy datasets.
9	70/30 Weighting	[UNVERIFIED — NEEDS: DOI for arXiv 2512.00280]	I cannot verify the existence of arXiv 2512.00280 (dated Dec 2025). While the principle (Technical > Fundamental for short-term) is industry standard, the specific 70/30 split appears to be a heuristic, not a peer-reviewed constant.
10	Filter vs Ranker	[VERIFIED — SOURCE: Van Tharp, 1998]	In Trade Your Way to Financial Freedom, Van Tharp emphasizes that "The Setup" (the filter) is merely the gatekeeper. Robust systems rely on high-quality filters rather than hyper-optimizing rankings.
PROMPT 2: Support & Resistance Audit
Agglomerative vs KMeans: [PLAUSIBLE — REASON: Adaptive Clustering]. K-Means requires a pre-defined k (number of levels), which is nonsensical for price charts. Agglomerative clustering with a distance_threshold allows the data to determine how many levels exist naturally based on price density.

ZigZag 5%: [MISLEADING — CORRECTION: Volatility sensitivity]. A fixed 5% threshold is too wide for low-volatility stocks (e.g., JNJ) and too narrow for high-beta stocks (e.g., NVDA). Standard practice suggests using 1.5×ATR or a percentage relative to the stock's 30-day volatility.

Touch-based scoring: [VERIFIED — SOURCE: Murphy, 1999]. John Murphy’s Technical Analysis of the Financial Markets confirms that the more times a level is tested and holds, the more significant that level becomes in the minds of market participants.

3.2x Predictive Power: [HALLUCINATED — FLAG: Fabricated multiplier]. While MTF (Multi-Timeframe) confluence is a standard technical concept, the "3.2x" figure has no basis in published quantitative finance literature. It is likely an internal backtest result presented as a universal fact.

2 ATR Stop Loss: [VERIFIED — SOURCE: LeBeau & Lucas, 1992]. The use of ATR for stop placement (Chandelier Exit) is well-documented. A 2-ATR stop is a standard "intermediate" distance to avoid being stopped out by "market noise."

Asymmetric Proximity: [UNVERIFIED — NEEDS: Empirical data]. There is no widespread research suggesting resistance should have a wider proximity (30%) than support (20%). Usually, these are kept symmetric to avoid bias in R:R calculations.

Weekly Resampling: [VERIFIED — SOURCE: ISO 8601 / Standard Finance]. Resampling to "W-FRI" is the global standard for weekly OHLCV data.

150 Bars Requirement: [VERIFIED — SOURCE: TA-Lib Documentation]. To calculate a 200-period SMA or find long-term pivots, 150–250 bars is the minimum required to ensure indicator "warm-up" and statistical significance.

PROMPT 3: Pattern Detection Audit
VCP Logic: [MISLEADING — CORRECTION: Volume Missing]. Your logic checks price contraction, but Minervini’s VCP requires Volume Contraction (V) to confirm the "supply has been absorbed." Without a volume dry-up check, you will catch "failing flats" that haven't cleared supply.

Cup & Handle (1.02 Lip): [VERIFIED — SOURCE: O'Neil, 2009]. William O’Neil specifies the handle should form in the upper half of the cup and ideally remain below the high. A 2% "poke" above is a common tolerance in automated detection.

60% Confidence: [PLAUSIBLE — REASON: Trade Frequency]. Lowering the threshold is a standard way to increase "Signal Frequency," but it increases "False Positives." As long as the Profit Factor (PF 1.61) holds in out-of-sample testing, it is a valid optimization.

Trend Template: [VERIFIED — SOURCE: Minervini, 2013]. Your 8 criteria perfectly match the "Trend Template" found in Trade Like a Stock Market Wizard. The 22-day rising 200 SMA is a standard proxy for "1 month" of trending.

Flat Base (15%): [VERIFIED — SOURCE: IBD / O'Neil]. Investor’s Business Daily defines a flat base as a consolidation between 10% and 15% depth over 5+ weeks.

PROMPT 4: Sector Rotation (RRG) Audit
Normalization at Midpoint: [MISLEADING — CORRECTION: Moving Average Baseline]. The original RRG (Julius de Kempenaer) uses a 12-week or 26-week exponential moving average of the RS-Line as the 100-center point, not the midpoint price of a static window.

10-day Momentum: [PLAUSIBLE — REASON: Swing timeframe]. Traditional RRGs use weekly data (RS-Ratio and RS-Momentum). A 10-day window is a reasonable "daily" adaptation for swing traders looking for faster signals than the standard weekly RRG.

Cap-Size Rotation (+/- 2): [UNVERIFIED — NEEDS: Historical backtest]. The threshold of "2" is an arbitrary heuristic. Most intermarket analysts look for a "Breakout" of the IWM/QQQ ratio line above a 50-day SMA rather than a fixed integer value.

PROMPT 5: 9-Criteria Checklist Audit
All-or-nothing: [PLAUSIBLE — REASON: Selective Quality]. This creates a "Super-Heuristic." While it limits trade frequency, it ensures the trader only enters "Stage 2" breakouts with high relative strength—the core of the CANSLIM/SEPA philosophy.

7% Stop: [VERIFIED — SOURCE: Minervini, 2013]. Minervini explicitly states: "Keep your losses to 7% or 8% maximum." Your checklist enforces this at the entry gate.

200 SMA Rising (22 days): [VERIFIED — SOURCE: SEPA Methodology]. Minervini requires the 200 SMA to be in a clear uptrend for at least 1 month (approx. 20-22 trading days).

