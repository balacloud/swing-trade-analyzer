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
