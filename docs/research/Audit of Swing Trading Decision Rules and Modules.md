# Audit of Swing Trading Decision Rules and Modules

## PROMPT 1 – Categorical Assessment & Verdict Logic

Each item below addresses the specific question and issues a verdict label using the requested taxonomy.

### 1. Trend Template 7/8 threshold for “Strong”

Minervini’s published Trend Template is an 8‑point checklist; secondary summaries and code implementations consistently state that **all eight criteria must be met for a confirmed Stage 2 uptrend**, not 7 of 8. None of these sources recommends using a 7‑of‑8 threshold as an “institutional‑quality” cutoff, nor is there academic work testing “7 versus 8” pass‑rates as a predictive variable. The systematic literature on technical indicators and cross‑sectional returns treats specific indicators (moving averages, time‑series momentum, etc.) but does not analyze Minervini’s 8‑point template or any 7/8 relaxation.[^1][^2][^3][^4]

**Verdict:** [MISLEADING — CORRECTION: Minervini’s own methodology requires 8/8 criteria; 7/8 as a “Strong” institutional standard is a discretionary modification with no direct empirical backing.]

***

### 2. RSI 50–70 as “optimal pullback range”

Multiple practitioner and quantitative sources on RSI range analysis describe **bullish RSI regimes where RSI tends to oscillate between about 40–80, with pullbacks stabilizing around 40–50** in uptrends. These sources also treat 50 as a useful bull/bear line, with RSI > 50 confirming bullish momentum. However, none of the cited work provides evidence that **50–70 specifically** is an empirically optimal pullback band versus alternatives such as 40–60 or 40–80; the choice appears to be a heuristic grounded in typical bull‑range behavior, not a rigorously optimized threshold.[^5][^6][^7][^8]

**Verdict:** [PLAUSIBLE — REASON: RSI staying mostly above 50 and within a 40–80 bull range is well‑supported, but 50–70 as a precise “optimal” band is a reasonable heuristic, not directly validated against other ranges in formal studies.]

***

### 3. Fear & Greed Index 60–80 as “Strong” sentiment

CNN’s Fear & Greed Index and third‑party explanations define **0–24 or 0–25 as extreme fear, roughly 25–49 as fear, about 45–55 or 45–55 as neutral, 50–74 or 56–74 as greed, and ≥75 as extreme greed**. These ranges are descriptive labels; there is no published evidence that **entries when the index sits in 60–80 (“moderate greed”) maximize swing‑trade performance** relative to other zones. Available commentary frames the index as a broad sentiment gauge and often recommends contrarian behavior at extremes, but does not specify a 60–80 “sweet spot” for entry edges.[^9][^10][^11][^12]

**Verdict:** [UNVERIFIED — NEEDS: A study regressing subsequent short‑horizon returns on Fear & Greed levels, explicitly testing 60–80 versus other bands, to support the claim that this zone is optimal for bullish swing entries.]

***

### 4. Fear & Greed neutral zone 35–60

CNN’s own documentation and derivative explainers place neutral sentiment roughly between **45 and 55**, with fear and greed regimes outside that range, and extreme zones below ~25 or above ~75. There is no research establishing that widening “neutral” to **35–60** improves predictive behavior or “removes a cliff at 45”; the choice of wider symmetric bands is an implementation preference. Contrarian‑indicator research around sentiment more generally (AAII, flows, etc.) tends to focus on extremes rather than fine gradations inside a broad mid‑range.[^10][^11][^12][^9]

**Verdict:** [PLAUSIBLE — REASON: A wider neutral band around the middle of a 0–100 sentiment scale is conceptually reasonable to avoid over‑reacting to small moves, but the specific 35–60 choice and its alleged cliff‑removal are not empirically documented for the Fear & Greed Index.]

***

### 5. VIX < 20 for “Favorable” risk

CBOE and practitioner guides often describe **VIX < 12 as “low,” > 20 as “high,” and values in between as “normal”**, and institutional commentary frequently treats sustained readings above 30 as stressed regimes. These thresholds, however, are partly convention and partly calibrated to specific samples; an S&P white paper uses 20 as a high‑volatility marker but does not claim 20 exactly is a universal boundary for “favorable” versus “unfavorable” equity trading conditions. Academic work on VIX thresholds examines regime‑switching and dynamic cutoffs rather than endorsing a single static level of 20 as optimal.[^13][^14][^15][^16]

**Verdict:** [PLAUSIBLE — REASON: Treating VIX below ~20 as a benign/normal volatility regime is consistent with practitioner references, but VIX = 20 is a rule‑of‑thumb, not an empirically optimal boundary for swing‑trading profitability.]

***

### 6. SPY 50‑day SMA slope as an “early bear” cap

There is extensive practitioner use and some backtesting of **200‑day SMA crossovers on SPY** as bull/bear filters and regime identifiers, and these have been shown to change drawdown and volatility characteristics versus buy‑and‑hold. However, specific use of the **slope of the 50‑day SMA as a leading bear‑market signal while price remains above the 200‑day** is not a standard, documented indicator in academic literature; it appears mostly in discretionary technical commentary and strategy blogs, often without robust statistical testing. No rigorous paper was found that validates capping a risk regime at “Neutral” solely because the 50‑day slope has turned down while price is above the 200‑day.[^17][^18]

**Verdict:** [UNVERIFIED — NEEDS: A study explicitly testing SPY 50‑day SMA slope (sign and magnitude) conditional on SPY > 200‑day, and its impact on forward returns and drawdowns, to justify its role as an “early bear” filter.]

***

### 7. ADX < 20 = no‑trade condition

Welles Wilder’s original work and modern summaries interpret **ADX below about 20 as non‑trending or weak trend, and ADX above roughly 25 as a trending environment**, with a gray zone between 20–25. Many practitioner guides echo these values and advocate avoiding trend‑following entries when ADX is below ~20. However, these are rule‑of‑thumb thresholds; there is no widely cited academic paper that proves 20 is the optimal universal cutoff for “no trend” across markets and timeframes.[^19][^20][^21][^22]

**Verdict:** [PLAUSIBLE — REASON: Using ADX < 20 as a no‑trend filter aligns with Wilder’s guidance and common modern practice, but it remains a heuristic rather than an empirically optimized universal threshold.]

***

### 8. Score‑to‑return correlation of 0.011 for the 75‑point model

The claimed **0.011 score‑to‑return correlation** pertains to a proprietary internal system; there is no way to externally verify this statistic or its computation. Academic work on return predictors shows that carefully constructed composite signals (technical or fundamental) can have statistically significant predictive power, albeit often modest and fragile out‑of‑sample. At the same time, many ad‑hoc or overfitted composite scores fail to generalize and exhibit near‑zero or even negative out‑of‑sample correlation with returns. Thus, the existence of at least one 75‑point subjective scoring model with near‑zero predictive power is entirely plausible but not independently documented.[^4][^23][^24]

**Verdict:** [UNVERIFIED — NEEDS: Access to the original score series, return series, and methodology to replicate and confirm that the sample and out‑of‑sample correlations are indeed near 0.011.]

***

### 9. Holding‑period weighting (Technical vs Fundamental) and arXiv 2512.00280

Standard finance pedagogy and practitioner material describe **technical analysis as more commonly used for short‑term timing** and **fundamental analysis as more relevant for long‑term valuation**, and many sources explicitly associate technicals with short‑ to medium‑term trading and fundamentals with longer horizons. Empirical literature also finds that short‑horizon returns often exhibit momentum and technical‑signal predictability, while long‑horizon returns relate more to valuation and earnings information (for example, work on anchoring, PEAD, and value‑based predictors). However, no study was found that justifies **specific numeric weights such as 70/30 for 5–10‑day trades or 30/70 for multi‑month holds**; these allocations are implementation choices.[^25][^23][^26][^27][^28]

The cited arXiv paper **2512.00280, “Retail Investor Horizon and Earnings Announcements”**, discusses how retail investors with different self‑reported holding periods around earnings generate distinct price patterns and anomalies. It analyzes horizon‑segmented flows and post‑earnings drift versus reversal, but **does not propose or validate an explicit weighting scheme between technical and fundamental signals like 70/30 vs 30/70**.[^29]

**Verdict:** [MISLEADING — CORRECTION: The general idea that technicals matter more at short horizons and fundamentals at longer horizons is consistent with both practitioner consensus and some empirical evidence, but the specific 70/30 and 30/70 weights are heuristic design choices, and arXiv 2512.00280 does not provide direct support for these exact splits.]

***

### 10. “System as FILTER not RANKER”

Position‑sizing and trading‑system design literature (e.g., Van Tharp and other system‑design authors) often advocates **rule‑based filters that define a tradable universe** and then apply separate position‑sizing and risk rules; some discretionary approaches do not require fine‑grained rankings once a minimum edge is established. That said, quantitative portfolio construction research commonly uses ranking (e.g., momentum deciles, value quantiles) to extract cross‑sectional premia and to allocate more capital to stronger signals. There is little direct literature comparing “binary filter only” versus “rank‑based selection” for swing‑trading systems across the same signal set. The design choice to use the categorical engine purely as a pass/fail gateway is therefore a reasonable engineering decision, but not something explicitly endorsed or rejected by formal research.[^26][^28][^4]

**Verdict:** [PLAUSIBLE — REASON: Using categorical rules as a binary filter rather than a ranker is consistent with some system‑design philosophies, but there is no direct empirical literature proving that filtering is superior to ranking for this type of swing‑trading engine.]

***

## PROMPT 2 – Support & Resistance Module

### 1. Agglomerative vs K‑Means for S&R clustering

Clustering‑based S&R algorithms are an active practitioner topic; resources on algorithmic S&R frequently describe **pivot‑based detection, rolling‑window extrema, and clustering of swing points**, and some educational material highlights the limitations of K‑Means for 1‑D price clustering due to its need to pre‑specify cluster counts and sensitivity to initialization. Agglomerative clustering with a distance threshold is intuitively attractive for level detection because it does not require a fixed number of clusters and can group nearby price levels adaptively. However, the academic paper most directly studying S&R behavior focuses on formal definitions, bounce probabilities, and profitability of level‑based strategies, not on comparing clustering algorithms. No peer‑reviewed study was found that establishes agglomerative clustering as empirically superior to K‑Means for S&R level detection.[^30][^31][^32][^33]

**Verdict:** [PLAUSIBLE — REASON: Agglomerative clustering with a distance threshold is technically better suited than K‑Means for 1‑D adaptive price‑level grouping, but the claim that it is categorically “better for S&R” lacks direct empirical validation in the literature.]

***

### 2. ZigZag 5% threshold on daily timeframe

ZigZag‑style peak/trough detection is widely used to filter noise, with common practitioner thresholds in the 5–10% range for daily equity charts, but these are **rules of thumb rather than optimized values**. Academic S&R work defines levels via rolling‑window extrema and statistical tolerances, not fixed 5% swings, and emphasizes that level width and detection windows should adapt to asset volatility and sampling frequency. Some modern sources on dynamic S&R explicitly recommend **volatility‑adaptive widths** (e.g., based on average increments or ATR) instead of fixed percent movements.[^34][^31][^35][^30]

**Verdict:** [MISLEADING — CORRECTION: A 5% ZigZag threshold is a reasonable starting heuristic for daily swing‑trading charts, but it is not empirically justified as universally optimal and is likely better implemented as a volatility‑adaptive parameter rather than a fixed percent.]

***

### 3. Touch‑based scoring of S&R levels

Several quantitative S&R resources and education platforms describe **multi‑touch levels and zones tested three or more times** as intuitively stronger because repeated bounces suggest higher order‑flow concentration. Formal work on S&R by Chung et al. (and follow‑on discussions) defines support and resistance as intervals where the probability of a bounce exceeds penetration and analyzes the **number of bounces as a key statistic**, though it does not translate directly into heuristic “scores.” At the same time, at least one large empirical study of price‑level strategies finds that traditional support‑bounce rules do not generally produce robust trading edges, even when bounces are considered.[^31][^32][^35][^36][^37]

**Verdict:** [PLAUSIBLE — REASON: Ranking levels by historical touch/bounce count is conceptually consistent with both microstructure arguments and formal definitions of S&R, but its incremental predictive power over other features is not strongly established and may be weak.]

***

### 4. MTF Confluence “3.2× stronger predictive power”

Multi‑timeframe confluence is a common practitioner belief: overlapping levels from higher and lower timeframes are said to be more important, and various blog and indicator authors promote confluence‑based S&R tools. However, no peer‑reviewed paper or reproducible backtest was found that quantifies **“3.2× stronger predictive power”** for S&R levels that appear on both daily and weekly charts. The figure 3.2× does not appear in the cited academic work on S&R levels, which focuses more broadly on bounce probabilities and profitability of strategies built on these levels.[^38][^39][^36][^33][^37][^31]

**Verdict:** [HALLUCINATED — FLAG: The specific claim of “3.2× stronger predictive power” for confluent daily/weekly levels has no identifiable empirical source and appears to be an invented or unsubstantiated statistic.]

***

### 5. 2×ATR(14) stop loss distance

ATR‑based stops are widely discussed in practitioner literature; many sources describe **initial stops in the range of 1.5–3×ATR, with 2×ATR a particularly common rule of thumb** for balancing noise tolerance and risk control. Academic and thesis work on stop‑loss design, including comparisons of fixed‑percent versus ATR‑based stops, finds that stop‑loss parameters materially affect drawdowns and trade distribution but often **do not yield robust improvements in risk‑adjusted returns**, and no single multiple emerges as universally optimal. Thus, 2×ATR(14) is well‑within common practice but not uniquely validated.[^40][^41][^42][^43][^44]

**Verdict:** [PLAUSIBLE — REASON: A 2×ATR(14) stop is a widely used practitioner heuristic and empirically reasonable, but it is not singled out by research as the best stop distance for swing trades across assets and strategies.]

***

### 6. Asymmetric proximity thresholds: 20% ATR for support, 30% ATR for resistance

The literature on S&R and ATR stops confirms that **volatility‑scaled bands** (e.g., using ATR fractions) can make levels more consistent across assets and regimes. However, no identified work specifically recommends **different ATR‑scaled proximity windows for support vs resistance (20% vs 30%)**. Empirical S&R studies that examine bounce behavior do not generally distinguish symmetric versus asymmetric tolerances in this specific way.[^35][^33][^43][^37][^31]

**Verdict:** [UNVERIFIED — NEEDS: Backtests that explicitly compare symmetric and asymmetric ATR‑scaled proximity thresholds for support and resistance, showing a statistically significant benefit to the 20%/30% choice.]

***

### 7. Weekly resampling using Friday as boundary (W‑FRI)

Standard OHLCV resampling in charting platforms uses **calendar‑based weekly bars**, typically ending on Friday for U.S. markets, and this is common across both retail and institutional tools. Academic time‑series and technical papers that use weekly data usually rely on exchange week endings (again, functionally Friday for U.S. equities), though they rarely discuss the weekday choice as a material variable. There is no strong evidence that choosing Friday versus another weekday materially changes S&R quality, provided the convention is consistent; any differences would be subtle and largely due to minor intraperiod path variations.[^23][^45][^46][^18][^17]

**Verdict:** [VERIFIED — SOURCE: Using week‑ending Friday bars for weekly OHLCV is standard practice in charting and backtesting; no evidence suggests that a different weekday boundary systematically improves S&R detection.][https://shop.investors.com/images/promotional/flat-b-b_112408.pdf]

***

### 8. Minimum 150 daily bars for S&R computation

The S&R literature and practitioner resources emphasize that **detection windows must be long enough to capture multiple swings and regime changes**, but do not specify 150 days as a canonical minimum. For daily swing‑trading, 150 bars (~7 months) gives several intermediate‑term cycles, which is arguably reasonable; still, some strategies use shorter windows (e.g., 3 months) or longer ones (e.g., 1–2 years) depending on the desired horizon. No empirical study was found that tests performance as a function of lookback length and identifies 150 bars as optimal or minimally sufficient.[^32][^33][^31]

**Verdict:** [PLAUSIBLE — REASON: Requiring ~150 daily bars provides a reasonable amount of context for S&R detection in swing trading, but the specific cutoff is heuristic and not uniquely supported by formal research.]

***

## PROMPT 3 – Pattern Detection Module

### 1. VCP detection via successively smaller contractions

Authoritative descriptions of Minervini’s VCP emphasize **progressively contracting price swings (e.g., 18% → 12% → 6%) in a Stage 2 uptrend**, along with **volume dry‑up during pullbacks and expansion on breakouts** as essential characteristics. Detecting VCPs by verifying that each contraction’s percent range is smaller than the previous is therefore faithful to a core component of the pattern, but a **complete implementation must also incorporate volume behavior, context in a strong uptrend, and identification of a clear pivot point**. A purely price‑range‑based gate without explicit volume dry‑up and breakout volume criteria omits key elements described in Minervini’s methodology.[^47][^48][^49][^50][^51]

**Verdict:** [MISLEADING — CORRECTION: Decreasing contraction ranges capture an important VCP feature, but a faithful implementation must also require volume dry‑up in the base and volume expansion on breakout within a confirmed Stage 2 uptrend.]

***

### 2. Cup & Handle handle_high ≤ right_lip × 1.02

O’Neil’s and IBD‑derived material specify that a **proper handle forms in the upper half or upper third of the cup, with the handle high generally within about 10–15% of the cup’s high**, and that the handle is a relatively shallow pullback. These discussions focus on depth and vertical positioning (and duration) rather than allowing the handle to poke above the right lip; usually, the handle stays below or roughly at the lip before breakout. Allowing handle_high up to **2% above** the right lip is tighter than the 10–15% “within the high” guideline and is not explicitly stated in O’Neil’s work or IBD documentation.[^52][^53][^54][^55]

**Verdict:** [PLAUSIBLE — REASON: Constraining the handle high to be very close to the right lip (e.g., within +2%) is consistent with the idea that the handle should form near the old high, but this exact 2% threshold is a designer’s choice, not a documented O’Neil rule.]

***

### 3. Cup depth acceptance range

IBD and related O’Neil material describe **ideal cup‑with‑handle bases as having depths around 15–30% (or 15–33%), sometimes deeper (up to ~40–50%) in severe bear markets**. The question indicates that the system accepts a “wider range,” but does not specify how wide. Since O’Neil explicitly cautions against overly deep cups in normal markets, accepting significantly deeper cups (e.g., >40–50% in typical conditions) would deviate from the canonical pattern definition and likely introduce lower‑quality bases.[^56][^55][^52]

**Verdict:** [UNVERIFIED — NEEDS: Precise documentation of the engine’s actual allowed depth range and empirical backtests comparing that range to O’Neil’s 15–33% guideline under different market regimes.]

***

### 4. Flat Base range < 15%

IBD and related sources define a **flat base as a tight consolidation, typically no more than about 10–15% deep and at least 5–6 weeks long**. TraderLion and other CAN SLIM‑aligned education providers describe flat bases with **prior uptrends of ~30%+ and depth within roughly 10–15%**, matching IBD’s depth guidance. Thus, categorizing a flat base as < 15% range is closely aligned with published methodology.[^53][^54][^46][^57][^58]

**Verdict:** [VERIFIED — SOURCE: Defining flat bases as consolidations with less than ~15% depth matches IBD/William O’Neil guidance for this pattern type.][https://shop.investors.com/images/promotional/flat-b-b_112408.pdf]

***

### 5. 60% confidence threshold (lowered from 80%)

Optimizing an internal “confidence score” threshold based on backtest performance is a standard practice in model calibration, but it carries familiar risks of **overfitting and data‑snooping bias**, especially when thresholds are tuned on limited samples without proper cross‑validation. If the 60% threshold was selected because Config C performed best at that cutoff in the 2020–2024 backtest and then validated on separate walk‑forward periods, this is defensible; if not, it risks overstating genuine predictive power. The methodological literature stresses the importance of **out‑of‑sample and out‑of‑time validation** when adjusting such hyperparameters.[^24][^4]

**Verdict:** [PLAUSIBLE — REASON: Lowering the threshold from 80% to 60% based on backtests is a common but potentially overfitting‑prone practice; its validity depends on the rigor of walk‑forward and out‑of‑sample testing, which is not externally documented.]

***

### 6. Trend Template 8 criteria fidelity

Public summaries of Minervini’s Trend Template list eight criteria: **price above 150‑ and 200‑day SMAs, 150 > 200, 200‑day rising for at least one month, price above 50‑day, 50 > 150 and > 200, price at least 30% above 52‑week low, price within 25% of 52‑week high, and RS rating at least 70**. The engine’s 8‑point list replaces the RS‑rating requirement with “price at least 25% above 52‑week low” and “within 25% of 52‑week high,” but omits the RS ≥ 70 criterion and uses 50/150/200 alignment differently than some summaries. This is close but not identical to Minervini’s published criteria.[^2][^3][^51][^1]

**Verdict:** [MISLEADING — CORRECTION: The implemented 8 criteria approximate Minervini’s Trend Template but omit the explicit RS‑rating requirement and diverge from some of his published moving‑average conditions; they should be described as “inspired by” rather than “faithful” SEPA criteria.]

***

### 7. Volume confirmation on breakout via ratio to 50‑day average

Both Minervini and O’Neil‑style methodologies emphasize **breakout volume at least 40–50% above average (often daily or 50‑day average volume) as confirmation** of institutional buying. Trader and educator articles on VCP and CAN SLIM routinely implement volume confirmation using a multiple or percentage above a recent average volume, frequently a 50‑day mean. Using a **volume ratio to a 50‑day average** is therefore very much in line with standard practice for breakout confirmation.[^48][^49][^51][^57][^55][^47]

**Verdict:** [VERIFIED — SOURCE: Checking breakout volume against a 50‑day average to confirm patterns aligns with Minervini/O’Neil‑derived guidance for volume confirmation.][https://shop.investors.com/images/promotional/flat-b-b_112408.pdf]

***

### 8. Algorithmic pattern detection reliability vs humans

Academic and practitioner research on algorithmic chart‑pattern recognition shows that **machine‑based detection can match or exceed handcrafted rule algorithms and can sometimes identify patterns missed by rigid coders**, but overall profitability and robustness depend heavily on definitions, data, and avoidance of overfitting. At least one deep‑learning study on stock chart patterns (e.g., CNN/LSTM applied to candlestick images) demonstrates improved detection rates versus a hard‑coded algorithm, but does not conclusively show superior trading performance. Broader discussions of technical analysis factors suggest that some patterns contain predictive information, yet the statistical edge is often small and sensitive to implementation choices.[^59][^60][^33][^37][^30][^4]

**Verdict:** [PLAUSIBLE — REASON: Algorithmic detection can reduce human subjectivity and match or surpass rigid programmatic detectors, but there is no consensus that algorithmic pattern recognition is reliably superior to experienced human chartists across all markets and patterns.]

***

### 9. Prior uptrend requirement (20% advance) for Flat Base

IBD and CAN SLIM guidelines specify that valid bases generally **follow a prior uptrend of at least ~20–30%** before base formation, with flat bases typically appearing after a substantial advance. TraderLion and related educational content echo that a flat base should come after a **30%+ prior run**, not from lows. Therefore, requiring a **20% minimum prior advance** is somewhat on the low side of this range but directionally consistent with the principle that a quality flat base must be a continuation pattern after a significant uptrend.[^54][^46][^58][^52][^53]

**Verdict:** [PLAUSIBLE — REASON: A 20% prior advance requirement is slightly more permissive than the 25–30% commonly cited, but still aligned with the core idea that valid flat bases should follow a meaningful prior uptrend.]

***

## PROMPT 4 – Sector Rotation & RRG Logic

### 1. RS normalization at midpoint vs start in RRG

Official RRG documentation and StockCharts’ ChartSchool describe **JdK RS‑Ratio and RS‑Momentum as normalized indicators centered around 100**, with RS‑Ratio > 100 indicating relative outperformance and RS‑Momentum > 100 indicating positive momentum. The documentation does not state that normalization must occur at the **start** of the lookback window; it simply requires consistent normalization so that 100 serves as the neutral line. Using the midpoint of the lookback period as the base for normalization is an implementation detail, not addressed directly by Julius de Kempenaer’s public materials.[^61][^62][^63][^64]

**Verdict:** [PLAUSIBLE — REASON: Normalizing RS at the midpoint to 100 still satisfies the RRG requirement of a 100 baseline, but it deviates from typical implementations that implicitly normalize over the full history or a rolling window and is not explicitly recommended in official RRG references.]

***

### 2. 10‑day momentum window

RRG documentation defines RS‑Momentum as a **rate‑of‑change‑style measure of RS‑Ratio** but does not mandate a 10‑day or 10‑period window; implementation details are largely abstracted away in charting platforms. Example scripts and educational content sometimes use periods like 14 to compute relative‑strength measures or moving averages, but no canonical 10‑day standard for RRG momentum was identified. Julius de Kempenaer’s public materials emphasize **the concept of leading/lagging via RS‑Momentum crossing 100**, not a specific short lookback like 10 days.[^62][^65][^63][^66]

**Verdict:** [UNVERIFIED — NEEDS: Direct implementation notes or source code from official RRG providers specifying the default period used for RS‑Momentum; current public documentation does not endorse a 10‑day standard.]

***

### 3. Quadrant thresholds at RS = 100 and Momentum = 0

RRG quadrants in official documentation are defined by **RS‑Ratio and RS‑Momentum both normalized around 100, with the four quadrants corresponding to (>100,>100), (>100,<100), (<100,<100), and (<100,>100)**. That is, the horizontal and vertical axes use 100 as the neutral level, not 0. In this engine, RS is normalized to 100, but RS momentum is expressed as a **0‑centered change in RS_normalized**; quadrant thresholds are then set at RS = 100 and Momentum = 0. While this is a linear reparameterization of the vertical axis, it is not identical to the standard RRG convention, which uses 100/100 for both axes.[^63][^61][^62]

**Verdict:** [MISLEADING — CORRECTION: Using RS ≥ 100 as the horizontal boundary is consistent with RRGs, but RRG’s vertical axis is conventionally RS‑Momentum normalized around 100, not 0; mapping momentum to a 0‑centered metric is an implementation variant and should not be described as standard RRG.]

***

### 4. 6‑month lookback period

RRG examples and Julius de Kempenaer’s commentary show use of both **weekly and daily RRGs with various tail lengths**, often on the order of 3–6 months for trend and rotation analysis, but there is no fixed standard for lookback length. A 6‑month daily window is therefore within the range of common practice for sector rotation; whether this is ideal for **swing‑trading horizons of days to weeks** is more debatable. Many relative‑strength traders still use multi‑month lookbacks to capture persistent leadership, even if their holding period is shorter.[^67][^66][^62]

**Verdict:** [PLAUSIBLE — REASON: A 6‑month RS lookback is reasonable for sector rotation context, but it is not specifically optimized or endorsed for short‑term swing trading in the RRG literature.]

***

### 5. Cap‑size rotation signal with ±2 RS‑point threshold

Literature on size‑based rotation (small vs large caps) often examines relative performance of small‑cap versus large‑cap indices but does not specify **fixed RS‑score differences like “IWM RS > QQQ RS + 2”** as signal thresholds. RRG and other RS frameworks generally interpret movements qualitatively (leading vs lagging) using crossings of their neutral lines rather than hard numeric gaps between two assets’ RS scores. No empirical source was found that validates ±2 points in a normalized RS scale as an optimal trigger for risk‑on/off decisions.[^61][^62][^63][^23][^17]

**Verdict:** [UNVERIFIED — NEEDS: A study that defines RS scores for QQQ and IWM as in this engine, then backtests specific thresholds (e.g., ±2) for timing size‑rotation risk‑on/risk‑off signals and demonstrates statistical significance.]

***

### 6. 11 SPDR sectors as the rotation universe

The SPDR Select Sector ETFs (XLK, XLF, XLV, XLI, XLY, XLP, XLE, XLB, XLU, XLRE, XLC) are **direct representations of the 11 GICS sectors of the S&P 500**, and are widely used in sector rotation strategies by both retail and institutional investors. State Street and other providers explicitly market these 11 funds as a complete GICS sector suite. Alternative sector universes (e.g., iShares sector/industry ETFs) exist but map to the same high‑level sector taxonomy.[^68][^69][^70][^71]

**Verdict:** [VERIFIED — SOURCE: Using the 11 SPDR GICS sector ETFs as the sector‑rotation universe is standard and aligned with common industry practice.][https://www.ssga.com/us/en/institutional/capabilities/equities/sector-investing/gics-sector-and-industry-map]

***

### 7. Sector rotation as context only (not modifying BUY/HOLD/AVOID)

RRG originator Julius de Kempenaer and other RS practitioners often stress that **RRGs and sector rotation signals are best used as top‑down context to complement price and trend analysis, not as standalone buy/sell triggers**. For example, commentary repeatedly describes RRG as a tool for seeing “where leadership is improving or deteriorating” and for focusing attention, while actual trade execution still relies on price charts and risk management. This supports the philosophy of using sector rotation as **pre‑flight context** rather than as a hard filter on individual stock trade/no‑trade decisions.[^72][^62][^67]

**Verdict:** [PLAUSIBLE — REASON: Treating sector rotation purely as contextual information rather than directly modifying the core BUY/HOLD/AVOID engine is consistent with how RRG’s creator positions the tool, though alternative designs that integrate sector signals into entry rules are also reasonable.]

***

## PROMPT 5 – 9‑Criteria Binary Checklist

### 1. All‑or‑nothing (9/9) requirement

System‑design and money‑management literature emphasizes **defining a minimum edge and then managing risk**, but it does not insist on binary “all criteria or no trade” frameworks. Quantitative factor investing typically uses **weighted scores, ranks, and percentiles** (e.g., momentum or value deciles) to select and prioritize trades rather than requiring that every signal be simultaneously favorable. An all‑or‑nothing 9/9 checklist is therefore unusually strict and will materially reduce trade frequency; whether that is beneficial depends entirely on the specific backtest. There is no general evidence that such hard conjunction rules outperform softer, weighted approaches across strategies.[^28][^4][^26][^24]

**Verdict:** [PLAUSIBLE — REASON: A 9/9 binary gate is defensible as a conservative design choice, but system‑design literature more commonly supports weighted or ranked approaches; the superiority of an all‑criteria pass rule is unproven and strategy‑specific.]

***

### 2. 7% maximum stop distance from entry

Both William O’Neil and Mark Minervini advocate strict **7–8% maximum losses from proper buy points**, with O’Neil’s “7–8% sell rule” and Minervini’s similar 7–8% stop guidance widely cited. These rules are based on long‑term empirical observation of growth stocks and are central to CAN SLIM/SEPA‑style risk management. While the exact percentage is not tested across all strategies in formal academic literature, a 7% stop aligned to this tradition is strongly supported within the specific growth‑stock swing/position‑trading framework.[^73][^74][^75][^76][^77]

**Verdict:** [VERIFIED — SOURCE: A 7–8% maximum loss rule is explicitly recommended by O’Neil and Minervini for growth stocks; using ~7% as a hard stop distance is consistent with their published methodologies.][https://www.investors.com/how-to-invest/investors-corner/chart-reading-basics-how-a-buy-point-marks-a-time-of-opportunity/]

***

### 3. Minimum R:R ≥ 2:1

Risk‑management texts and trading education materials frequently recommend **aiming for reward‑to‑risk ratios of at least 2:1**, sometimes higher, to ensure positive expectancy in the presence of sub‑100% win rates. However, academic studies of stop‑loss and take‑profit policies show that the optimal R:R depends on win rate, edge, and market dynamics; very high R:R can reduce win rate too much, while low R:R can make the system fragile to transaction costs. Research does not identify 2:1 as universally optimal, but it is a widely used, conservative baseline.[^41][^42][^44][^26][^40]

**Verdict:** [PLAUSIBLE — REASON: A 2:1 minimum R:R is strongly supported as good practice in risk‑management literature, but it is not uniquely optimal across all strategies and markets.]

***

### 4. Top 25% of 52‑week range

Minervini and O’Neil‑style growth investing emphasize **buying stocks near their 52‑week highs**, with guidance such as “within 15–25% of the high” and “leading stocks making new highs,” rather than buying deep pullbacks. The Trend Template explicitly requires price within 25% of the 52‑week high, and IBD encourages focusing on stocks forming bases near highs rather than far below. Requiring price in the **top 25% of the 52‑week range (≥ 75th percentile)** is therefore consistent with these methodologies.[^78][^79][^3][^51][^55][^2]

**Verdict:** [VERIFIED — SOURCE: Using the top 25% of the 52‑week range as a requirement closely matches Minervini’s “within 25% of 52‑week high” and O’Neil/IBD guidance to focus on stocks near their highs.][https://edition.cnn.com/2025/04/07/business/what-is-cnn-fear-and-greed-index]

***

### 5. $10M average daily dollar volume

Liquidity guidelines in Minervini/O’Neil circles typically emphasize **sufficient daily dollar volume to allow institutional participation**, with many practitioners informally recommending thresholds from a few million up to $20–25M depending on account size. However, specific published thresholds vary; some IBD examples feature stocks with tens of millions in daily volume, but there is no canonical “$10M” line in O’Neil’s or Minervini’s books. For a retail swing trader, $10M+ in average daily dollar volume is generally considered adequate for execution with minimal slippage, but this is a heuristic.[^51][^26]

**Verdict:** [PLAUSIBLE — REASON: A $10M daily dollar‑volume minimum is a reasonable liquidity filter for retail swing trading and directionally consistent with growth‑stock methodologies, but the exact dollar amount is not explicitly codified in the cited authors’ texts.]

***

### 6. SPY > 200‑day SMA as market‑regime filter

Numerous studies and practitioner backtests examine strategies that **only take long equity exposure when the index is above its 200‑day moving average**, finding that such filters often reduce drawdowns and volatility, with mixed impact on long‑term CAGR. This simple trend‑filter is one of the most widely cited market‑regime indicators in both quantitative blogs and technical‑analysis education. While there are many alternative regime filters (e.g., breadth indicators, shorter MAs, volatility‑adjusted signals), SPY > 200‑day SMA is about as standard as it gets.[^80][^18][^17]

**Verdict:** [VERIFIED — SOURCE: Using SPY above its 200‑day SMA as a bull/bear market filter is well‑documented and widely backtested as a regime‑switching rule.][https://www.quantifiedstrategies.com/200-day-moving-average/]

***

### 7. 200‑day SMA rising over 22 trading days

Minervini’s trend template requires that the **200‑day moving average be trending up for at least 1 month, preferably 4–5 months**. One month in U.S. trading roughly corresponds to 21–22 sessions; checking that the 200‑day SMA has increased over the past 22 days is a natural discretization of this text requirement. While Minervini does not specify “22 trading days” numerically, the qualitative requirement (“up for at least 1 month”) supports this operationalization.[^3][^1][^2][^51]

**Verdict:** [PLAUSIBLE — REASON: Using a 22‑day rising condition for the 200‑day SMA is a reasonable translation of Minervini’s ‘rising for at least one month’ rule, though the exact day count is not formally specified in his writings.]

***

### 8. ADX ≥ 20 as trend confirmation

As noted earlier, Wilder’s guidance and many modern resources interpret **ADX below ~20 as non‑trending and above ~25 as trending**, with 20–25 as a transition zone. Using **ADX ≥ 20** as a minimal trend‑confirmation threshold is therefore somewhat more permissive than Wilder’s >25 rule but broadly consistent with the idea that higher ADX indicates stronger trend. There is no clear academic consensus that 20 is optimal; some traders adapt thresholds to volatility or asset class.[^20][^21][^22][^19]

**Verdict:** [PLAUSIBLE — REASON: ADX ≥ 20 as a trend confirmation is in line with many simplified interpretations of Wilder’s work, but the precise cutoff is heuristic rather than empirically optimized for modern markets.]

***

### 9. RS ≥ 1.0 (parity with SPY) as momentum criterion

Minervini and O’Neil typically want **leaders with high relative‑strength rankings (often RS ratings 70–90+)**, meaning strong outperformance versus the market, not just parity. Momentum and cross‑sectional technical‑indicator research also commonly forms portfolios of top deciles or quantiles, not merely those at or above average. Setting a cutoff at RS ≥ 1.0 (parity with SPY) is therefore **less strict** than canonical growth‑stock leaders criteria and may admit many average performers rather than top‑quartile winners.[^79][^78][^1][^2][^3][^4][^28][^51]

**Verdict:** [MISLEADING — CORRECTION: While requiring RS ≥ 1.0 ensures the stock is not underperforming SPY, Minervini/O’Neil frameworks generally target substantially stronger relative performers (e.g., top deciles or RS ratings ≥ 70), so parity is likely too permissive if the intent is to mirror their momentum standards.]

---

## References

1. [TwP: Mark Minervini Trend Template Criteria](https://in.tradingview.com/script/88aL78Qh-TwP-Mark-Minervini-Trend-Template-Criteria/) - In his book 'Think & Trade Like a Champion', Mark Minervini gave his famous Trend Template Criteria,...

2. [The Mark Minervini Trend Template: How to Find Winning Stocks](https://deepvue.com/screener/minervini-trend-template/) - What is the Minervini Trend Template? The Mark Minervini Trend Template is a comprehensive checklist...

3. [Mark Minervini's Trend Template Question](https://www.elitetrader.com/et/threads/mark-minervinis-trend-template-question.359356/) - Hi guys, Mark Minervini talks about his trend following template in his trading book. It looks like ...

4. [Technical indicators and cross-sectional expected returns](https://www.sciencedirect.com/science/article/abs/pii/S1044028322000837) - by H Zeng · 2023 · Cited by 5 — This study shows that 14 widely documented technical indicators expl...

5. [RSI Range-Momentum Trading Strategy (Backtest, Trading Rules ...](https://www.quantifiedstrategies.com/rsi-range-momentum-trading-strategy/) - The RSI is one of the most popular indicators used in technical analysis. However, most people use i...

6. [Conclusion: Make Rsi Work...](https://obside.com/trading-technical-analysis/rsi-indicator/) - Learn how to use the RSI indicator (Relative Strength Index) to read momentum, avoid overbought/over...

7. [What is the Relative Strength Index (RSI) in Trading? - ATFX](https://www.atfx.com/en/analysis/trading-strategies/relative-strength-index) - Learn how to use the Relative Strength Index (RSI) in trading to identify signals, spot trend revers...

8. [StockCharts Insider: How an “Overbought” RSI Can Be Your Best ...](https://articles.stockcharts.com/article/stockcharts-insider-how-an-overbought-rsi-can-be-your-best-buy-signal/) - Before We Dive In… Think “overbought” means it’s time to bail? Not always. Sometimes that 70+ RSI re...

9. [Growin Blog](https://blog.growin.tv/en/fear-and-greed-index-en/) - As an investor, have you ever felt yourself swayed by changes in market sentiments, worried about po...

10. [CNN's Fear & Greed Index — What it Means for Global ...](https://investingnews.com/what-is-cnn-fear-greed-index/) - Learn what the CNN Fear & Greed Index is, how the index is calculated, why it hit "extreme fear" and...

11. [Guide to Understand Fear and Greed Index for Investors](https://www.heygotrade.com/en/blog/understand-fear-and-greed-index) - How the Fear and Greed Index Is Calculated. The CNN Fear and Greed Index combines several market ind...

12. [Fear & Greed Index Explained: Signals, History and more](https://www.axiory.com/trading-resources/basics/fear-greed-index) - Fear and greed index is a composite measure scaled on a 0-100 that aims to capture collective market...

13. [A Practitioner's Guide to Reading VIX](https://www.spglobal.com/spdji/en/education-a-practitioners-guide-to-reading-vix.pdf) - One such example takes a VIX level below 12 to be “low,” a level above 20 to be “high,” and a level ...

14. [VIX Thresholds Enhance Stock Volatility Forecasts | PDF](https://www.scribd.com/document/867643814/Liu-et-al-FRL-2022-VIX-threshold-and-predictability) - This paper explores a novel method for forecasting stock market volatility by utilizing dynamic thre...

15. [The short-run impact of investor expectations' past volatility ...](https://www.sciencedirect.com/science/article/pii/S1042443124001501) - by B Dima · 2025 · Cited by 4 — The study examines the relationship between past volatility and curr...

16. [White Paper CBOE Volatility Index](https://www.sfu.ca/~poitras/419_VIX.pdf) - The VIX Index measures 30-day expected volatility of the S&P 500 Index. The components of the VIX In...

17. [200 Day Moving Average Trading Strategy – (With Backtest)](https://www.quantifiedstrategies.com/200-day-moving-average/) - Volatility above and under the 200 day moving average. Price behavior in most markets differs betwee...

18. [SystemTrader - Putting the 200-day Moving Average ... - StockCharts](https://articles.stockcharts.com/article/articles-arthurhill-2018-04-systemtrader---putting-the-200-day-moving-average-through-the-wringer/) - There were three big bull runs, two big bear markets and some other deep declines. A basic moving av...

19. [Understanding the Average Directional Index (ADX) Indicator](https://sgt.markets/understanding-the-average-directional-index-adx-indicator-a-powerful-tool-for-trend-analysis/) - According to Wilder, an ADX reading above 25 suggests the presence of a strong trend, while a readin...

20. [John Murphy's Law #9 — Trend or Not a Trend (Using ADX)](https://articles.stockcharts.com/article/stockcharts-insider-john-murphys-law-9-trend-or-not-a-trend-using-adx/) - How Many Other Traders Use the ADX. Welles Wilder offered a simple rule of thumb: above 25 = trendin...

21. [How to Trade with the ADX – (Average Directional Index)](https://www.tradingsim.com/blog/adx) - The ADX allows you to measure the strength of trend. Wilder instructed readings above 25 are trendin...

22. [What is ADX Indicator: Trading Strategy & Tips | Capital.com](https://capital.com/en-int/learn/technical-analysis/average-directional-index) - Learn about Average Directional Index (ADX) trading strategy. Discover how to use ADX to assess tren...

23. [Stock Return Predictability: New Evidence from Moving ...](https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Avramov-Kaplanski-Subra_2018_SSRN-id3111334.pdf) - by D Avramov · Cited by 19 — Our paper fits into this literature by proposing that the anchoring bia...

24. [Does Academic Research Destroy Stock Return ...](https://rpc.cfainstitute.org/research/cfa-digest/2016/06/does-academic-research-destroy-stock-return-predictability-digest-summary) - To address this issue, the authors study the return predictability of 97 variables shown to predict ...

25. [Technical vs Fundamental Analysis: Which One Should ...](https://www.heygotrade.com/en/blog/technical-vs-fundamental-analysis) - Technical analysis focuses on price action and market psychology. Rather than studying company funda...

26. [Fundamental vs. Technical Analysis](https://rpc.cfainstitute.org/research/cfa-magazine/2003/fundamental-vs-technical-analysis) - Fundamental analysis has more value than technical analysis because it provides a much deeper framew...

27. [Technical vs. fundamental analysis | Chart Your Course on ...](https://www.wealthsimple.com/en-ca/learn/technical-vs-fundamental-analysis) - Technical analysis predicts future price movements from previous data, while fundamental analysis ju...

28. [AQR Momentum Indices, Monthly](https://www.aqr.com/Insights/Datasets/Momentum-Indices-Monthly) - We have developed methodologies for U.S. and international markets that capture momentum in an intui...

29. [Retail Investor Horizon and Earnings Announcements](https://arxiv.org/abs/2512.00280) - by DF Vamossy · 2025 — These findings suggest that accounting for investment horizon helps disentang...

30. [Automating Chart Patterns: A Deep Dive into Three Essential Algorithms](https://medium.datadriveninvestor.com/automating-chart-patterns-a-deep-dive-into-three-essential-algorithms-9ecfafc710fa) - In the dynamic world of financial markets, traders often rely on chart patterns to forecast potentia...

31. [Evidence and Behaviour of Support and Resistance Levels in](https://arxiv.org/pdf/2101.07410v1.pdf)

32. [Support and Resistance: Algorithmic Detection - Kekkei](https://kekkei.com/course/technical-analysis-python/support-resistance-concepts) - Kekkei is a modern learning platform for quantitative finance and financial science. Study structure...

33. [Support Resistance Levels towards Profitability in Intelligent Algorithmic Trading Models](https://ntut.elsevierpure.com/en/publications/support-resistance-levels-towards-profitability-in-intelligent-al)

34. [Automating Chart Patterns: 3 Essential Algorithms](https://gist.ly/youtube-summarizer/automating-chart-patterns-3-essential-algorithms) - Explore 3 algorithms for identifying local tops and bottoms in price data. Learn about rolling windo...

35. [Dynamic SR Levels in Time Series](https://www.emergentmind.com/topics/dynamic-time-series-support-and-resistance-levels-identification) - Explore methodologies for identifying adaptive support and resistance levels in time series data usi...

36. [How To Perform A Multi TimeFrame Analysis + 5 Strategies](https://tradeciety.com/how-to-perform-a-multiple-time-frame-analysis) - Traders who make use of support and resistance levels on the higher timeframe typically either look ...

37. [Support and Resistance in Financial Markets for CME_MINI:NQ1! by EdgeTools](https://www.tradingview.com/chart/NQ1!/E9llteXp-Support-and-Resistance-in-Financial-Markets/) - An Empirical Investigation of Price Level Trading Across Asset Classes Abstract This essay evaluates...

38. [Support Resistance MTF Indicator: Multi-Timeframe Levels ...](https://pineify.app/resources/blog/support-resistance-mtf-indicator-tradingview) - Learn how to use the Support Resistance MTF indicator to identify key support and resistance zones a...

39. [Multi-Timeframe S/R Confluence - Enhanced](https://www.tradingview.com/script/nlnTaxjS-Multi-Timeframe-S-R-Confluence-Enhanced/) - A powerful tool designed to identify high-probability support and resistance zones for trading BTC/U...

40. [Backtesting the impact of stop-loss mechanisms on trading ...](https://thesis.dial.uclouvain.be/entities/masterthesis/61e583f3-a6f1-4765-8174-dbb333b07590) - This thesis investigates the impact of stop-loss settings on the performance of trading strategies a...

41. [Stop Loss Strategies for Algorithmic Trading - TradersPost](https://blog.traderspost.io/article/stop-loss-strategies-algorithmic-trading) - Master essential stop loss strategies for algorithmic trading including fixed stops, trailing stops,...

42. [5 ATR Stop-Loss Strategies for Risk Control - LuxAlgo](https://www.luxalgo.com/blog/5-atr-stop-loss-strategies-for-risk-control/) - Explore five effective ATR-based stop-loss strategies that help traders manage risk and adapt to mar...

43. [ATR Trailing Stops: A Guide to Better Risk Management - TrendSpider](https://trendspider.com/learning-center/atr-trailing-stops-a-guide-to-better-risk-management/) - Introduction The ATR Trailing Stop is a technical indicator designed to help traders set stop-loss l...

44. [I Tested 87 Different Stop Loss Strategies - And Found the 10 You ...](https://papertoprofit.substack.com/p/i-tested-87-different-stop-loss-strategies) - I discovered 10 new classes of stop loss strategies that all beat the state-of-the-art.

45. [Multi-Timeframe Analysis SIMPLIFIED!](https://www.youtube.com/watch?v=9rJ3GkpP6r4) - Joe Rabil of Rabil Stock Research shares how to use multi-timeframe analysis — Monthly, Weekly, and ...

46. [Chart Patterns: Flat Base](https://www.youtube.com/watch?v=uDoZgFf6D2A) - Learn to profit from the flat base, one of the three most common patterns top stocks form.

Investor...

47. [What is a VCP Pattern? Mark Minervini's Volatility ...](https://www.finermarketpoints.com/post/what-is-a-vcp-pattern-mark-minervini-s-volatility-contraction-pattern-explained) - ... volume. Volume dries up during contractions (supply exhausting) and surges 40-50% above average ...

48. [VCP Pattern Strategy: How to Trade Like Mark Minervini](https://arongroups.co/technical-analyze/vcp-pattern-strategy/) - VCP (Volatility Contraction Pattern), popularised by U.S. trading champion Mark Minervini, focuses o...

49. [Mastering the Volatility Contraction Pattern](https://traderlion.com/technical-analysis/volatility-contraction-pattern/) - This contraction tells you that supply is drying up, while demand could be building, setting the sta...

50. [Volatility Contraction Pattern (VCP): A Trader's Guide to ...](https://trendspider.com/learning-center/volatility-contraction-pattern-vcp/) - The VCP pattern is a visual representation of the market where price volatility and volume shrink, i...

51. [How Mark Minervini Screens For Winning Stocks](https://deepvue.com/screener/how-mark-minervini-screens-for-stocks/) - Mark Minervini focuses on buying high-momentum stocks that are already in an uptrend. He screens for...

52. [☕️ The Cup and Handle Pattern - Anatomy](https://substack.com/home/post/p-66930002) - The High of the handle should be within 15% of the high of the cup. The Depth of the handle should b...

53. [Ibd Chartpatterns PDF - Investments & Securities](https://www.scribd.com/document/465593625/IBD-CHARTPATTERNS-pdf) - The document discusses three profitable stock chart patterns: 1. Cup-with-handle pattern forms over ...

54. [How to Analyze a Base – Cup, Handle, and Beyond](https://beginners-in-stock-trading-ddb2b0.beehiiv.com/p/how-to-analyze-a-base-cup-handle-and-beyond-3e31) - Recognize the Patterns That Precede Powerful Breakouts—and Time Your Entries Like a Pro, Plus Market...

55. [The 3 Most Common and Profitable Chart Patterns - IBD Digital](https://shop.investors.com/Education/lesson.aspx?id=736315)

56. [Chart Patterns: Base Counting Notes | PDF | Market Trend](https://www.scribd.com/document/394598934/Trend-Determination) - Most are 3-6 months. ○ Depth in base usually 12%-15% (no more than 33%) in normal markets. A very sm...

57. [[PDF] Untitled](https://shop.investors.com/images/promotional/flat-b-b_112408.pdf)

58. [Master the Flat Base Pattern for Maximum Profits](https://traderlion.com/technical-analysis/the-flat-base-pattern/) - What is The Flat Base Pattern? A flat base is a chart pattern that often forms after a stock has mad...

59. [Stock Chart Pattern recognition with Deep Learning](https://arxiv.org/pdf/1808.00418.pdf)

60. [[PDF] Master Degree programme - in Economics and Finance - UNITesi](https://unitesi.unive.it/retrieve/62ceeeef-73b5-4845-a764-0308e15a8c01/887093-1271508.pdf)

61. [Relative Rotation - RRG JdK RS-Ratio & RS-Momentum](https://www.tradingview.com/script/11vu1lHA-Relative-Rotation-RRG-JdK-RS-Ratio-RS-Momentum/) - The RS-Ratio (red line) and RS-Momentum (green line) are plotted around a baseline of 100. The backg...

62. [Relative Rotation Graphs (RRG Charts) - ChartSchool](https://chartschool.stockcharts.com/table-of-contents/chart-analysis/chart-types/relative-rotation-graphs-rrg-charts) - Typically, RS-Momentum crosses above 100 when RS-Ratio is forming a trough and starting to move up. ...

63. [Unveiling the Building Blocks for RRG](https://relativerotationgraphs.com/educational/the-building-blocks-for-rrg/) - RS-Ratio is an indicator that measures the trend for relative performance. Similar to the price rela...

64. [rrg uitleg](https://www.bullnochbear.com/RRG/rrg%20uitleg.htm)

65. [RRG Charts | Support Center - StockCharts.com](https://help.stockcharts.com/charts-and-tools/other-charting-tools/rrg-charts) - Relative Rotation Graphs (RRG charts) show you a security's relative strength and momentum relative ...

66. [Using RRG in Different Time Frames | Julius de Kempenaer (12.20.22)](https://www.youtube.com/watch?v=ewNWukZDc7A) - In this video, Julius de Kempenaer explains the basics of the various time frames that can be used i...

67. [Julius de Kempenaer on RRGs: Spotting Sector Rotation Before It Hits the Headlines](https://www.youtube.com/watch?v=JMbjtIoXx1c) - Sector rotation doesn’t always show up clearly on the index chart—it often reveals itself underneath...

68. [11 SPDR Sector ETFs to Buy Now](https://www.yahoo.com/news/11-spdr-sector-etfs-buy-173054002.html) - The right sector ETFs can outperform the broad market.The stock market is a big place full of many d...

69. [GICS Sector and Industry Map - State Street Global Advisors](https://www.ssga.com/us/en/institutional/capabilities/equities/sector-investing/gics-sector-and-industry-map) - Consider ETFs for precise implementation of sector-based strategies. The SPDR family covers 11 GICS®...

70. [U.S. Sector Specific Allocations by BMO ETFs](https://www.bmoetfs.ca/articles/spdr-monthly-sector-landing-page)

71. [[PDF] Sector & sub-industry ETFs - iShares](https://www.ishares.com/us/literature/presentation/ishares-sector-and-industry-etfs.pdf)

72. [What RRG Charts Say About Market Uncertainty (And When It Might End)](https://www.youtube.com/watch?v=E8dk3H2dVsE) - Confused by mixed market signals? Julius de Kempenaer analyzes sector rotation, asset rotation, and ...

73. [3 Key Lessons from Trade Like a Stock Market Wizard ...](https://www.finermarketpoints.com/post/3-key-lessons-from-trade-like-a-stock-market-wizard) - Risk Management Priority: Minervini's success stems from strict 7-8% stop-losses, not high win rates...

74. [Mastering Risk: The 7% Cut-Loss Rule and Beyond in Top ...](https://www.ainvest.com/news/mastering-risk-7-cut-loss-rule-top-stock-investments-2508/) - - The 7% cut-loss rule, a foundational risk management strategy, limits losses by exiting trades aft...

75. [What is the 7% Rule in Stocks?](https://tradetron.tech/blog/what-is-the-7percent-rule-in-stocks) - According to this rule, if a stock falls 7–8% below your purchase price, you should sell it immediat...

76. [Trade Like A Stock Market Wizard](https://cdn.bookey.app/files/pdf/book/en/trade-like-a-stock-market-wizard.pdf) - When a stock falls below the stop-loss level, immediate action is required ... Answer:Traders should...

77. [10 Trading Tips from Legendary Investor William O'Neil](https://www.investing.com/analysis/10-trading-tips-from-legendary-investor-william-oneil-200660549) - 3. Cut Losses Quickly (7-8% Rule) One of O'Neil's most disciplined principles is cutting losses at 7...

78. [Mark Minervini's Stock Screener: What Indicators and ...](https://www.finermarketpoints.com/post/mark-minervini-s-stock-screener-what-indicators-and-criteria-does-he-use) - Written by Christopher Hall, AdvDipFP | Authorised Representative, AFSL 526688 | Updated March 2026M...

79. [What is Mark Minervini's Trading Strategy? The Complete SEPA ...](https://www.finermarketpoints.com/post/what-is-mark-minervini-s-trading-strategy-the-complete-sepa-vcp-guide) - Written by Christopher Hall, AdvDipFP | Authorised Representative, AFSL 526688 | Updated March 2026M...

80. [How I Rode a 200-Day Regime-Change Signal to Achieve 30 ...](https://papertoprofit.substack.com/p/how-i-rode-a-200-day-regime-change) - By rotating into equities on 200-day bull signals and moving to defensive assets on bear signals, I ...

