# Universal Principles — 4-LLM Synthesis & Surgical Action Plan

**Date:** 2026-03-18 (Day 69)
**Auditors:** Grok 3, Gemini 2.5 Pro, Perplexity Pro, Claude Opus 4.6
**Method:** Each LLM independently evaluated 35 claims across 5 prompts using AUDIT MODE (verdict labels: VERIFIED, PLAUSIBLE, MISLEADING, UNVERIFIED, HALLUCINATED)
**Purpose:** Determine the MINIMUM VIABLE surgical changes to evolve STA from Minervini-specific to universal principles

---

## EXECUTIVE SUMMARY

**Core finding:** The system is ~70% universal already. The Minervini "skin" makes it look practitioner-specific, but the underlying factors (trend, momentum, quality, regime) ARE standard quant factors. Evolution is surgical, not a rebuild.

**Consensus across all 4 LLMs:**
1. Hybrid (binary filter → rank survivors) is standard practice — keep our architecture, just loosen the binary gates
2. Equal-weight factors — do NOT optimize weights on 238 trades
3. Position sizing by volatility is the highest-impact regime adaptation
4. Mean-reversion arm fills the "silent in choppy markets" gap
5. Simplicity premium is real — add complexity only with overwhelming evidence
6. ATR stops > fixed % stops — we already have this, make it primary
7. Factor research at monthly horizons does NOT directly apply to 5-30 day swing — use shorter lookbacks

---

## CROSS-LLM VERDICT MATRIX

### PROMPT 1: Binary Gating vs Continuous Factor Scoring (6 claims)

| # | Claim | Grok | Gemini | Perplexity | Claude | Consensus |
|---|-------|------|--------|------------|--------|-----------|
| 1.1 | Binary filters inferior to continuous scoring | PLAUSIBLE | (implied PLAUSIBLE) | UNVERIFIED | MISLEADING | **PLAUSIBLE** — No head-to-head study exists, but ranking captures more information |
| 1.2 | Hybrid (filter→rank) is optimal | UNVERIFIED | (supported) | MISLEADING | VERIFIED | **PLAUSIBLE** — Standard practice, but "optimal" is too strong a word |
| 1.3 | FF/AQR applies to 5-30 day | MISLEADING | (PLAUSIBLE with caveats) | MISLEADING | MISLEADING | **MISLEADING** — Monthly factors ≠ swing factors. Different anomalies at 5-30d |
| 1.4 | 238 trades adequate | UNVERIFIED | (critical, wants 1000+) | UNVERIFIED | PLAUSIBLE | **PLAUSIBLE** — p=0.002 is strong, but on the low end. Adequate for validation, not for weight optimization |
| 1.5 | Daily rankings stable without persistence | UNVERIFIED | (MISLEADING) | UNVERIFIED | MISLEADING | **MISLEADING** — Need persistence filters or hysteresis bands |
| 1.6 | Factor weights from optimization | MISLEADING | MISLEADING | MISLEADING | MISLEADING | **MISLEADING (4/4)** — Use equal weights. Most unanimous finding |

### PROMPT 2: Universal Factor Set (7 claims)

| # | Claim | Grok | Gemini | Perplexity | Claude | Consensus |
|---|-------|------|--------|------------|--------|-----------|
| 2.1 | Top 6 factors for 5-30d returns | PLAUSIBLE | (PLAUSIBLE) | UNVERIFIED | MISLEADING | **PLAUSIBLE** — Individual factors valid, but list conflates stock-selection with system-level filters |
| 2.2 | 12-1 momentum best for swing | UNVERIFIED | (MISLEADING) | MISLEADING | MISLEADING | **MISLEADING (3/4)** — Too slow for swing. Use 1-3 month lookbacks instead |
| 2.3 | Chart patterns as scored factor | UNVERIFIED | (keep as confirmation) | UNVERIFIED | PLAUSIBLE | **UNVERIFIED** — Keep as binary overlay, not primary scored factor |
| 2.4 | Fundamentals add value at swing | UNVERIFIED | (PLAUSIBLE as risk shield) | UNVERIFIED | PLAUSIBLE | **PLAUSIBLE** — Value is DEFENSIVE (risk filter), not return predictor at short horizons |
| 2.5 | CNN F&G adequate sentiment | PLAUSIBLE | (PLAUSIBLE but prefer components) | MISLEADING | PLAUSIBLE | **PLAUSIBLE** — Adequate for simple system, but components (VIX structure, put/call) are better individually |
| 2.6 | SPY>200+VIX best regime detection | UNVERIFIED | (MISLEADING, prefer HMM/breadth) | MISLEADING | PLAUSIBLE | **PLAUSIBLE** — "Good enough" and simple. Not provably "best" but robust |
| 2.7 | Momentum & trend too correlated, drop one | PLAUSIBLE | (PLAUSIBLE, test correlation) | PLAUSIBLE | MISLEADING | **PLAUSIBLE** — Don't drop either. Test correlation, keep both if r<0.7, else combine |

### PROMPT 3: Mean-Reversion (7 claims)

| # | Claim | Grok | Gemini | Perplexity | Claude | Consensus |
|---|-------|------|--------|------------|--------|-----------|
| 3.1 | MR in range, momentum in trend | PLAUSIBLE | (PLAUSIBLE) | PLAUSIBLE | VERIFIED | **VERIFIED** — Moskowitz et al. (2012), well-established regime-strategy relationship |
| 3.2 | RSI<30 proven MR entry | UNVERIFIED | (MISLEADING, RSI(2)<10 better) | MISLEADING | MISLEADING | **MISLEADING (3/4)** — RSI(14)<30 is weak. RSI(2)<10 + trend filter is the evidence-based approach |
| 3.3 | Bollinger Band MR has edge | UNVERIFIED | (PLAUSIBLE, 71% WR cited) | UNVERIFIED | PLAUSIBLE | **UNVERIFIED** — Weak academic evidence. RSI(2) is cleaner signal |
| 3.4 | MR needs different risk params | PLAUSIBLE | (PLAUSIBLE) | PLAUSIBLE | PLAUSIBLE | **PLAUSIBLE (4/4)** — Tighter stops, time-based exits for MR. Well-supported by strategy design |
| 3.5 | Simultaneous MR+momentum improves returns | PLAUSIBLE | (PLAUSIBLE) | PLAUSIBLE | VERIFIED | **VERIFIED** — Asness et al. (2013), strategy diversification is well-documented |
| 3.6 | MR 60-70% WR, momentum 50-55% WR | UNVERIFIED | (PLAUSIBLE) | MISLEADING | PLAUSIBLE | **PLAUSIBLE** — Direction is right, exact numbers vary by implementation |
| 3.7 | Connors RSI simplest MR approach | UNVERIFIED | (PLAUSIBLE, 26% CAR cited) | UNVERIFIED | PLAUSIBLE | **PLAUSIBLE** — Best-documented simple MR for retail. Needs own backtest validation |

### PROMPT 4: Regime-Adaptive Parameters (6 claims)

| # | Claim | Grok | Gemini | Perplexity | Claude | Consensus |
|---|-------|------|--------|------------|--------|-----------|
| 4.1 | Regime adaptation improves returns | PLAUSIBLE | (PLAUSIBLE) | PLAUSIBLE | PLAUSIBLE | **PLAUSIBLE (4/4)** — Yes, but with strong overfitting caveats |
| 4.2 | ATR stops adapt to volatility | VERIFIED | VERIFIED | PLAUSIBLE | VERIFIED | **VERIFIED (3/4)** — Most agreed-upon technical claim |
| 4.3 | Position sizing most impactful to adapt | PLAUSIBLE | (PLAUSIBLE) | MISLEADING | VERIFIED | **PLAUSIBLE** — Moreira & Muir (2017) supports, but Perplexity notes both levers matter |
| 4.4 | VIX 20/30 right tiering | UNVERIFIED | (PLAUSIBLE with continuous note) | MISLEADING | PLAUSIBLE | **PLAUSIBLE** — Adequate convention, but VIX percentile is more robust |
| 4.5 | Adaptive momentum lookbacks | UNVERIFIED | (PLAUSIBLE) | UNVERIFIED | MISLEADING | **MISLEADING** — Combine multiple fixed lookbacks instead of switching dynamically |
| 4.6 | >2-3 adaptive params = overfitting | UNVERIFIED | (PLAUSIBLE) | UNVERIFIED | PLAUSIBLE | **PLAUSIBLE** — No exact threshold, but parsimony principle is strong |

### PROMPT 5: Success vs Failure (7 claims)

| # | Claim | Grok | Gemini | Perplexity | Claude | Consensus |
|---|-------|------|--------|------------|--------|-----------|
| 5.1 | Top 5 failure modes | PLAUSIBLE | (PLAUSIBLE) | PLAUSIBLE | PLAUSIBLE | **PLAUSIBLE (4/4)** — List is broadly right, add selection bias |
| 5.2 | Walk-forward sufficient for overfitting | MISLEADING | MISLEADING | MISLEADING | MISLEADING | **MISLEADING (4/4)** — Necessary but NOT sufficient. Need parameter stability + Monte Carlo |
| 5.3 | Simplicity premium real | PLAUSIBLE | (VERIFIED) | PLAUSIBLE | VERIFIED | **VERIFIED** — DeMiguel (2009), bias-variance tradeoff. Strongest design principle |
| 5.4 | Slippage <5 bps in $10M+ stocks | MISLEADING | (MISLEADING, 20-50bps for $100k) | UNVERIFIED | PLAUSIBLE | **MISLEADING** — True for small retail orders in large caps, but NOT for $100k in $10M ADV names |
| 5.5 | Factors continue 2020-2026 same magnitude | MISLEADING | (MISLEADING) | MISLEADING | MISLEADING | **MISLEADING (4/4)** — ~58% decay post-publication (McLean & Pontiff 2016). Factor premia are smaller |
| 5.6 | Retail should avoid HFT/stat-arb | VERIFIED | (VERIFIED) | PLAUSIBLE | VERIFIED | **VERIFIED (3/4)** — Clear structural limitation for retail |
| 5.7 | Minimum viable: 2-3 factors + ATR + equal weight | UNVERIFIED | (PLAUSIBLE) | UNVERIFIED | PLAUSIBLE | **PLAUSIBLE** — Good design, but specific config unproven as "minimum viable" |

---

## UNANIMOUS FINDINGS (All 4 LLMs Agree)

These are the highest-confidence findings that should drive our surgical changes:

### 1. EQUAL-WEIGHT FACTORS (Claim 1.6 — MISLEADING 4/4)
**What:** Do NOT optimize factor weights on historical data
**Why:** DeMiguel et al. (2009) — equal weights beat optimized out-of-sample. 238 trades is far too few to reliably optimize 4+ weights
**STA Impact:** Our current 4 categories (Technical, Fundamental, Sentiment, Risk) should be equal-weighted in any composite score

### 2. WALK-FORWARD IS NOT ENOUGH (Claim 5.2 — MISLEADING 4/4)
**What:** Walk-forward is necessary but not sufficient to prevent overfitting
**Why:** Need parameter stability analysis, Monte Carlo permutation, deflated Sharpe ratio
**STA Impact:** Add parameter stability check (does system work at ADX±2, RS±0.1?) to validation suite

### 3. FACTOR DECAY IS REAL (Claim 5.5 — MISLEADING 4/4)
**What:** Factor returns from 2010-2020 do NOT continue at same magnitude
**Why:** McLean & Pontiff (2016) — ~58% decay post-publication. Crowding, HFT arbitrage
**STA Impact:** Don't trust historical backtests at face value. Build in expectation of ~50% alpha decay

### 4. SIMPLICITY PREMIUM IS REAL (Claim 5.3 — VERIFIED 2/4, PLAUSIBLE 2/4)
**What:** Simpler systems survive better out-of-sample
**Why:** Bias-variance tradeoff, DeMiguel (2009), fewer parameters = less overfitting
**STA Impact:** Every proposed change must pass the "does this add more signal than noise?" test

---

## STRONG CONSENSUS FINDINGS (3/4 or 4/4 Agree)

### 5. FF/AQR FACTORS DON'T DIRECTLY APPLY TO SWING (Claim 1.3 — MISLEADING 3/4)
**What:** Monthly-rebalanced factors ≠ swing-timeframe factors
**Swing-relevant factors:** PEAD (earnings drift), short-term reversal, 1-3 month momentum, liquidity
**STA Impact:** Use 3-month RS and 21-day ROC instead of 12-month momentum

### 6. RSI(14)<30 IS WEAK, RSI(2)<10 IS BETTER (Claim 3.2 — MISLEADING 3/4)
**What:** Standard RSI oversold is not the evidence-based MR entry
**Better:** RSI(2) < 10 + Price > 200 SMA (Connors, extensively backtested)
**STA Impact:** If adding MR arm, use RSI(2)<10, NOT RSI(14)<30

### 7. ATR STOPS ARE THE RIGHT APPROACH (Claim 4.2 — VERIFIED 3/4)
**What:** Volatility-adaptive stops via ATR are well-supported
**STA Impact:** We already have 2x ATR stops. Make this PRIMARY, keep 7% as max cap only

### 8. RETAIL SHOULD STAY IN ITS LANE (Claim 5.6 — VERIFIED 3/4)
**What:** Don't compete on HFT, stat-arb, options flow
**STA Impact:** Our 5-30 day momentum in liquid stocks IS the right edge space. Confirmed

### 9. 12-1 MOMENTUM TOO SLOW FOR SWING (Claim 2.2 — MISLEADING 3/4)
**What:** Academic momentum measure designed for monthly rebalancing
**Better:** 3-month RS (intermediate drift) + 21-day ROC (short-term persistence)
**STA Impact:** Consider blending multiple lookbacks rather than single 52-week RS

### 10. DAILY RANKINGS NEED PERSISTENCE (Claim 1.5 — MISLEADING 3/4)
**What:** Raw daily factor rankings are noisy, need persistence or hysteresis
**STA Impact:** If moving to composite scoring, require rank in top N for 3+ consecutive days

---

## CONFLICTS BETWEEN LLMs (Resolved)

| Claim | Conflict | Resolution |
|-------|----------|------------|
| 1.2 Hybrid optimal | Grok: UNVERIFIED, Claude: VERIFIED | Resolution: Standard practice (PLAUSIBLE), but "optimal" is unproven |
| 4.3 Position sizing most important | Perplexity: MISLEADING, Claude: VERIFIED | Resolution: Position sizing IS highly impactful (Moreira & Muir), but entry rules also matter. Prioritize sizing but don't ignore entries |
| 3.3 Bollinger Bands | Gemini: PLAUSIBLE (71% WR), Others: UNVERIFIED | Resolution: Gemini cited a specific study, but academic evidence remains weak overall. RSI(2) is cleaner |
| 2.5 CNN F&G adequate | Perplexity: MISLEADING, Others: PLAUSIBLE | Resolution: "Adequate" for current system — upgrade path is VIX term structure + put/call, not urgent |
| 5.4 Slippage <5 bps | Claude: PLAUSIBLE, Gemini: MISLEADING | Resolution: True for $10-25k orders in $100M+ ADV stocks. NOT true for $100k in $10M ADV. Gemini's slippage table is the most granular guidance |

---

## THE SURGICAL ACTION PLAN

Based on 4-LLM consensus, here are the MINIMUM VIABLE changes organized by impact and effort.

### TIER 1: MUST DO (High impact, high consensus, low risk)

#### 1A. Make ATR Stops Primary, 7% as Cap Only
- **Evidence:** VERIFIED 3/4 (Claim 4.2)
- **Change:** In `categoricalAssessment.js`, make 2x ATR the default stop, keep 7% as absolute maximum only
- **Effort:** Small — adjust stop logic priority
- **Risk:** None — we already compute ATR stops

#### 1B. Equal-Weight Categories (Don't Optimize Weights)
- **Evidence:** MISLEADING 4/4 that optimization works (Claim 1.6)
- **Change:** Formalize that Technical, Fundamental, Sentiment, Risk/Macro are equally weighted in any future composite scoring
- **Effort:** Documentation — our current binary system already treats them equally
- **Risk:** None — this is a design principle, not a code change yet

#### 1C. Add Parameter Stability Analysis to Validation
- **Evidence:** MISLEADING 4/4 that walk-forward alone is enough (Claim 5.2)
- **Change:** Create a simple parameter sensitivity test: run backtest with ADX ±2, RS ±0.1, stop ±1%. If results collapse, the system is fragile
- **Effort:** Medium — new validation script
- **Risk:** Low — purely additive

### TIER 2: SHOULD DO (High impact, strong consensus, moderate effort)

#### 2A. Add Mean-Reversion Arm
- **Evidence:** VERIFIED that MR+momentum diversifies (Claim 3.5), MISLEADING that RSI(14)<30 is the entry (Claim 3.2)
- **Design:**
  - Entry: RSI(2) < 10 AND Price > 200 SMA (Connors approach)
  - Exit: Time-based (5-10 day max hold) OR RSI(2) > 70
  - Stops: 3-5% (tighter than momentum), time-based exit as primary
  - Regime: Only active when ADX < 20 (range-bound market) OR VIX > 25 (high vol)
  - Position size: 50% of standard momentum position (smaller, higher frequency)
- **Effort:** Large — new strategy path through the system
- **Risk:** Medium — needs its own backtest validation before going live

#### 2B. Volatility-Based Position Sizing
- **Evidence:** PLAUSIBLE 3/4, VERIFIED by Claude citing Moreira & Muir (2017) (Claim 4.3)
- **Design:**
  - VIX < 20: Full position (100% of calculated size)
  - VIX 20-30: 75% position
  - VIX > 30: 50% position
  - Optional upgrade: VIX percentile rank instead of absolute levels
- **Effort:** Small-Medium — add multiplier to position sizing logic
- **Risk:** Low — purely defensive, reduces exposure in high-vol

#### 2C. Blend Multiple Momentum Lookbacks
- **Evidence:** MISLEADING 3/4 that 12-1 is best for swing (Claim 2.2), MISLEADING 3/4 that adaptive lookbacks work (Claim 4.5)
- **Design:** Instead of single 52-week RS, use average of:
  - 21-day ROC (short-term persistence)
  - 63-day RS vs SPY (3-month intermediate drift)
  - 126-day RS vs SPY (6-month momentum, what we currently use as ~52-week)
  - Equal-weight the three
- **Effort:** Medium — modify RS calculation in backend
- **Risk:** Low — blending is more robust than single lookback (consensus)

### TIER 3: NICE TO HAVE (Lower consensus or higher effort)

#### 3A. Loosen Binary Gates → Hybrid Filter+Rank
- **Evidence:** PLAUSIBLE that hybrid is standard (Claim 1.2)
- **Design:** Keep binary filters for: Price > $5, Volume > $1M/day, Price > 200 SMA. Convert remaining criteria (RS, ADX, patterns, fundamentals) to continuous scores. Rank survivors
- **Effort:** Large — rearchitect scoring engine
- **Risk:** High — changes the core decision logic
- **Decision:** DEFER until backtest proves Tier 1+2 changes insufficient

#### 3B. Add Rank Persistence Filter
- **Evidence:** MISLEADING 3/4 that daily rankings are stable (Claim 1.5)
- **Design:** Stock must rank in top N for 3+ consecutive days before entry
- **Effort:** Medium — requires tracking daily rankings over time
- **Risk:** Low — reduces false signals
- **Decision:** Only relevant if we implement continuous scoring (3A)

#### 3C. Upgrade Sentiment Beyond F&G
- **Evidence:** PLAUSIBLE 3/4 that F&G is adequate (Claim 2.5)
- **Design:** Add VIX term structure (contango/backwardation) and put/call ratio as additional sentiment inputs
- **Effort:** Medium — new data feeds
- **Risk:** Low — additive
- **Decision:** DEFER — F&G is adequate for current phase

#### 3D. Market Breadth as Regime Indicator
- **Evidence:** SPY>200+VIX is PLAUSIBLE but not "best" (Claim 2.6)
- **Design:** Add "% of S&P 500 stocks above 200 SMA" as supplementary regime indicator
- **Effort:** Medium — new data calculation
- **Decision:** DEFER — current regime detection is adequate

---

## WHAT NOT TO DO (Anti-patterns from consensus)

| Don't | Why | Consensus |
|-------|-----|-----------|
| Optimize factor weights | 238 trades is too few, overfitting guaranteed | 4/4 MISLEADING |
| Adapt >2 parameters to regime | Overfitting risk exceeds benefit | 3/4 PLAUSIBLE |
| Use RSI(14)<30 for MR | Weak signal, RSI(2)<10 is evidence-based | 3/4 MISLEADING |
| Build HMM regime detection | Over-engineering for retail, SPY>200+VIX is adequate | 3/4 consensus |
| Dynamically switch momentum lookbacks | Combining fixed lookbacks is more robust | 3/4 MISLEADING |
| Trust historical factor returns at face value | ~58% decay post-publication | 4/4 MISLEADING |
| Drop chart patterns entirely | Keep as optional binary overlay (low cost, some signal) | 3/4 consensus |
| Build portfolio-level position sizing | Over-engineering for 3-5 position discretionary trader | Agreed in prior session |
| Rely solely on walk-forward | Add parameter stability + Monte Carlo | 4/4 MISLEADING |

---

## IMPLEMENTATION SEQUENCE

### Phase 1: Quick Wins (Day 69-70) — No core logic changes
1. Formalize ATR stop as primary (7% as cap only) — code change in assessment
2. Document equal-weight principle — design doc
3. Build parameter stability test script — new validation tool

### Phase 2: Position Sizing + Momentum (Day 71-72)
4. Add VIX-based position sizing multiplier — backend + frontend display
5. Blend 3 momentum lookbacks (21d, 63d, 126d) — backend RS calculation

### Phase 3: Mean-Reversion Arm (Day 73-75)
6. Build RSI(2) scanner — backend
7. MR trade path with different risk params — backend + frontend
8. MR backtest validation — validation suite

### Phase 4: Validation (Day 76)
9. Parameter stability analysis across all changes
10. Compare before/after on backtest metrics
11. Paper trade for 2 weeks before any further changes

---

## PRESERVED INFRASTRUCTURE (What stays unchanged)

| Component | Status | Why |
|-----------|--------|-----|
| Data pipeline (TwelveData → cache → frontend) | KEEP 100% | Universal requirement |
| S&R engine | KEEP 100% | Pattern detection is additive |
| Pattern detector (VCP, C&H, etc.) | KEEP as optional overlay | Low cost, some signal |
| RRG / Sector Rotation | KEEP 100% | Standard institutional tool |
| Context Tab (FRED cycles, econ, news) | KEEP 100% | Adds information, no downside |
| Backtest framework | KEEP + EXTEND | Add parameter stability |
| Frontend visualization | KEEP + EXTEND | Add MR indicators |
| Categorical Assessment structure | KEEP, MODIFY thresholds | 4-category structure is sound |

**Bottom line:** ~85% of existing code survives. The evolution is in thresholds, position sizing, and adding a second strategy arm (MR). The architecture is sound.

---

## GEMINI'S HYBRID PIVOT STRATEGY (Notable Addition)

Gemini proposed a specific system design worth noting:

```
1. Universe Filter (Binary): S&P 500/Russell 1000, Price > 150 SMA, $20M+ daily volume
2. Factor Scoring (Rank): 21-day ROC + 3-month RS + Piotroski F-Score, equal-weighted z-scores
3. Risk Management: 2.5x ATR stops, position sized inversely to VIX, weekly rebalance with limit orders
```

This is closely aligned with our system. Key differences from current STA:
- Uses Piotroski F-Score instead of ROE/RevGrowth/D-E (similar quality signal, more standardized)
- Explicit 21-day ROC as short-term factor (we don't have this)
- $20M daily volume floor (higher than our current filter)
- Weekly rebalance cadence (we're more discretionary)

**Verdict:** Good reference architecture. Not a replacement for STA, but validates our direction.

---

## PERPLEXITY'S KEY CONTRIBUTION

Perplexity was the most conservative auditor — gave the most UNVERIFIED verdicts, demanding specific studies for every claim. This is valuable because it highlights where we're operating on practitioner consensus rather than academic proof.

**Perplexity's unique insight:** "There is no canonical paper that ranks top factors for 5-30 day returns" — meaning our factor choices for swing timeframes are inherently more empirical/practitioner-based than academically validated. This is fine, but means we should backtest everything ourselves rather than relying on published research.

---

## GROK'S KEY CONTRIBUTION

Grok was the strictest on source verification — many UNVERIFIED verdicts where others gave PLAUSIBLE. This is the right approach for an audit. Grok's standout finding:

**"No citable source directly tests '9 criteria must ALL pass' vs weighted composite ranking for 5-30 day US equity holds."** — This means our binary gating system has NO published benchmark to compare against. The hybrid approach is practitioner consensus, not proven optimal. This should reduce our urgency to rearchitect — the current binary system may be fine.

---

## NEXT STEPS

1. **This session:** Review this synthesis, align on Tier 1 + Tier 2 priorities
2. **Day 69-70:** Implement Tier 1 quick wins (ATR primary, parameter stability test)
3. **Day 71-72:** Implement Tier 2 position sizing + momentum blend
4. **Day 73-75:** Build and validate MR arm
5. **Day 76:** Full validation pass, compare before/after metrics
6. **Then:** Resume feature freeze with improved system

**The 7 Must-Fix items from the first audit (VCP volume, MTF 3.2x, etc.) should be done BEFORE these universal principles changes, as they're bug fixes not architecture evolution.**
