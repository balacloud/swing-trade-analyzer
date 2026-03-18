# External LLM Audit — Synthesis & Action Plan

**Created:** 2026-03-17 (Day 68) | **Updated:** 2026-03-18 (Day 69, added Gemini)
**Sources:** GPT + Perplexity + Gemini — 3 independent LLM auditors
**Scope:** 45 questions across 5 modules

---

## Cross-LLM Verdict Matrix

### Prompt 1: Categorical Assessment & Verdict Logic (10 questions)

| # | Claim | GPT | Perplexity | Gemini | 3-Way Consensus |
|---|-------|-----|------------|--------|-----------------|
| 1 | Trend Template 7/8 = Strong | MISLEADING | MISLEADING | PLAUSIBLE | **2/3 MISLEADING** — Gemini more lenient (says common in screening tools) |
| 2 | RSI 50-70 optimal pullback | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | **3/3 PLAUSIBLE** — Heuristic, Cardwell's bull regime 40-80 supports direction |
| 3 | F&G 60-80 = Strong | PLAUSIBLE | PLAUSIBLE | VERIFIED | **2/3 PLAUSIBLE** — Gemini cites Baker & Wurgler 2006 for momentum in greed zones |
| 4 | F&G neutral 35-60 | MISLEADING | MISLEADING | PLAUSIBLE | **2/3 MISLEADING** — Gemini defends as noise-reduction engineering |
| 5 | VIX < 20 Favorable | VERIFIED | VERIFIED | VERIFIED | **3/3 VERIFIED** |
| 6 | SPY 50 SMA declining = early bear | UNVERIFIED | UNVERIFIED | PLAUSIBLE | **2/3 UNVERIFIED** — Gemini calls it "negative divergence" (known concept) |
| 7 | ADX < 20 = no trend | VERIFIED | VERIFIED | VERIFIED | **3/3 VERIFIED** |
| 8 | Score-to-return r=0.011 | MISLEADING | UNVERIFIED | PLAUSIBLE | **No consensus** — All 3 differ. Gemini says low R is expected for non-linear data. |
| 9 | Holding period 70/30 weighting | VERIFIED | MISLEADING | UNVERIFIED | **No consensus** — All 3 differ. Concept verified, specific splits heuristic, arXiv paper doesn't support exact numbers. |
| 10 | System as FILTER not RANKER | PLAUSIBLE | PLAUSIBLE | VERIFIED | **2/3 PLAUSIBLE** — Gemini cites Van Tharp directly |

### Prompt 2: Support & Resistance Module (8 questions)

| # | Claim | GPT | Perplexity | Gemini | 3-Way Consensus |
|---|-------|-----|------------|--------|-----------------|
| 1 | Agglomerative > KMeans for S&R | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | **3/3 PLAUSIBLE** |
| 2 | ZigZag 5% threshold | UNVERIFIED | MISLEADING | MISLEADING | **2/3 MISLEADING** — All 3 say should be volatility-adaptive |
| 3 | Touch-based scoring | VERIFIED | PLAUSIBLE | VERIFIED | **2/3 VERIFIED** — Murphy (1999) cited by Gemini |
| 4 | MTF Confluence 3.2x claim | UNVERIFIED | **HALLUCINATED** | **HALLUCINATED** | **2/3 HALLUCINATED** — Fabricated multiplier, no source exists |
| 5 | 2x ATR stop loss | VERIFIED | PLAUSIBLE | VERIFIED | **2/3 VERIFIED** — LeBeau & Lucas (1992) cited |
| 6 | Asymmetric proximity 20%/30% | UNVERIFIED | UNVERIFIED | UNVERIFIED | **3/3 UNVERIFIED** |
| 7 | Weekly resampling W-FRI | UNVERIFIED | VERIFIED | VERIFIED | **2/3 VERIFIED** |
| 8 | Minimum 150 bars | UNVERIFIED | PLAUSIBLE | VERIFIED | **Split** — Gemini cites TA-Lib warm-up requirements |

### Prompt 3: Pattern Detection Module (9 questions)

| # | Claim | GPT | Perplexity | Gemini | 3-Way Consensus |
|---|-------|-----|------------|--------|-----------------|
| 1 | VCP detection (range-only) | MISLEADING | MISLEADING | MISLEADING | **3/3 MISLEADING** — All say volume dry-up is missing |
| 2 | Handle ≤ 1.02x right_lip | PLAUSIBLE | PLAUSIBLE | VERIFIED | **2/3 PLAUSIBLE** — Gemini cites O'Neil 2009 directly |
| 3 | Cup depth acceptance range | MISLEADING | UNVERIFIED | *(not asked)* | **Likely too permissive** — Both who answered flagged it |
| 4 | Flat Base < 15% range | VERIFIED | VERIFIED | VERIFIED | **3/3 VERIFIED** |
| 5 | 60% confidence (from 80%) | MISLEADING | PLAUSIBLE | PLAUSIBLE | **2/3 PLAUSIBLE** — Valid if walk-forward tested (which we did) |
| 6 | Trend Template 8 criteria fidelity | MISLEADING | MISLEADING | VERIFIED | **CONFLICT** — GPT/Perplexity say 25%→30% deviation + missing RS≥70; Gemini says "perfectly matches" |
| 7 | Volume confirmation 50-day avg | PLAUSIBLE | VERIFIED | *(not asked)* | **VERIFIED lean** |
| 8 | Algorithmic vs human detection | PLAUSIBLE | PLAUSIBLE | *(not asked)* | **PLAUSIBLE** |
| 9 | Flat Base 20% prior uptrend | VERIFIED | PLAUSIBLE | *(not asked)* | **PLAUSIBLE lean** |

### Prompt 4: Sector Rotation & RRG Logic (7 questions)

| # | Claim | GPT | Perplexity | Gemini | 3-Way Consensus |
|---|-------|-----|------------|--------|-----------------|
| 1 | RS normalization at midpoint | MISLEADING | PLAUSIBLE | MISLEADING | **2/3 MISLEADING** — Original RRG uses EMA baseline, not static midpoint |
| 2 | 10-day momentum window | UNVERIFIED | UNVERIFIED | PLAUSIBLE | **2/3 UNVERIFIED** — Gemini says reasonable daily adaptation |
| 3 | Quadrant thresholds 100/0 | MISLEADING | MISLEADING | *(not asked)* | **2/2 MISLEADING** — Standard uses 100/100 |
| 4 | 6-month lookback | UNVERIFIED | PLAUSIBLE | *(not asked)* | **PLAUSIBLE lean** |
| 5 | Cap-size ±2 threshold | UNVERIFIED | UNVERIFIED | UNVERIFIED | **3/3 UNVERIFIED** |
| 6 | 11 SPDR sectors | VERIFIED | VERIFIED | *(not asked)* | **VERIFIED** |
| 7 | Sector as context only | UNVERIFIED | PLAUSIBLE | *(not asked)* | **PLAUSIBLE lean** |

### Prompt 5: 9-Criteria Binary Checklist (9 questions)

| # | Claim | GPT | Perplexity | Gemini | 3-Way Consensus |
|---|-------|-----|------------|--------|-----------------|
| 1 | All-or-nothing 9/9 | PLAUSIBLE | PLAUSIBLE | PLAUSIBLE | **3/3 PLAUSIBLE** — Conservative but defensible |
| 2 | 7% stop distance | VERIFIED | VERIFIED | VERIFIED | **3/3 VERIFIED** |
| 3 | R:R ≥ 2:1 | UNVERIFIED | PLAUSIBLE | *(not asked)* | **PLAUSIBLE lean** |
| 4 | Top 25% of 52-week range | VERIFIED | VERIFIED | *(not asked)* | **VERIFIED** |
| 5 | $10M daily dollar volume | MISLEADING | PLAUSIBLE | *(not asked)* | **Split** |
| 6 | SPY > 200 SMA regime filter | VERIFIED | VERIFIED | *(not asked)* | **VERIFIED** |
| 7 | 200 SMA rising 22 days | VERIFIED | PLAUSIBLE | VERIFIED | **2/3 VERIFIED** |
| 8 | ADX ≥ 20 trend confirmation | VERIFIED | PLAUSIBLE | *(not asked)* | **VERIFIED lean** |
| 9 | RS ≥ 1.0 (parity) | MISLEADING | MISLEADING | *(not asked)* | **MISLEADING** — Too permissive for Minervini/O'Neil standards |

---

## Summary Statistics (3 LLMs)

| Verdict | GPT | Perplexity | Gemini | 3-Way Agreement |
|---------|-----|------------|--------|-----------------|
| VERIFIED | 14 | 10 | 13 | 7 (all 3 agree) |
| PLAUSIBLE | 10 | 18 | 9 | 5 (all 3 agree) |
| MISLEADING | 9 | 8 | 3 | 2 (all 3 agree) |
| UNVERIFIED | 11 | 7 | 2 | 2 (all 3 agree) |
| HALLUCINATED | 0 | 1 | 1 | 1 (Perplexity + Gemini) |

**Key observation:** Gemini is the most lenient auditor (more VERIFIED, fewer MISLEADING). Perplexity is most strict/thorough with citations. GPT falls in the middle.

---

## REVISED ACTION PLAN (3-LLM Synthesis)

### A. MUST-FIX — All 3 LLMs agree or 2/3 flag as wrong

#### 1. VCP: Add volume dry-up requirement ⬆️ UNANIMOUS
- **Verdicts:** MISLEADING + MISLEADING + MISLEADING (3/3)
- **Issue:** VCP detection only checks decreasing price ranges. All 3 LLMs independently flagged that Minervini requires volume dry-up during each contraction AND volume surge on breakout.
- **Gemini quote:** "Without a volume dry-up check, you will catch 'failing flats' that haven't cleared supply."
- **File:** `backend/pattern_detector.py` (VCP detection function)
- **Fix:** Add volume contraction check per leg + breakout volume ≥ 1.4x 50-day avg.
- **Priority:** **CRITICAL** — Strongest consensus finding across all 3 LLMs

#### 2. MTF Confluence "3.2x" claim: REMOVE ⬆️ UPGRADED
- **Verdicts:** UNVERIFIED + HALLUCINATED + HALLUCINATED (2/3 HALLUCINATED)
- **Issue:** Gemini confirms: "The '3.2x' figure has no basis in published quantitative finance literature. Likely an internal backtest result presented as a universal fact."
- **File:** Wherever this claim appears in code comments or UI
- **Fix:** Remove the specific "3.2x" number entirely.
- **Priority:** **CRITICAL** — Two LLMs independently flagged as fabricated

#### 3. Trend Template: 25% above 52-week low → should be 30%
- **Verdicts:** MISLEADING + MISLEADING + VERIFIED (2/3 MISLEADING)
- **Note:** Gemini said our template "perfectly matches" — but GPT and Perplexity specifically identified the 25% vs 30% discrepancy. Gemini may not have checked this granularly.
- **File:** `frontend/src/utils/simplifiedScoring.js` + `frontend/src/utils/categoricalAssessment.js`
- **Fix:** Change `0.25` to `0.30` in the 52-week low check.
- **Priority:** HIGH

#### 4. RS ≥ 1.0 is too permissive
- **Verdicts:** MISLEADING + MISLEADING + *(not asked)*
- **Issue:** Both GPT and Perplexity agree. Minervini/O'Neil want top-quartile RS, not parity.
- **Fix:** Backtest RS ≥ 1.1 vs ≥ 1.2 first, then update.
- **Priority:** HIGH — Needs backtest before changing

#### 5. RRG: RS normalization uses wrong baseline
- **Verdicts:** MISLEADING + PLAUSIBLE + MISLEADING (2/3 MISLEADING)
- **Issue:** Original RRG (de Kempenaer) uses a 12-week or 26-week EMA of RS-Line as the 100-center, not the midpoint of a static window.
- **Gemini quote:** "The original RRG uses a 12-week or 26-week exponential moving average of the RS-Line as the 100-center point, not the midpoint price of a static window."
- **File:** `frontend/src/utils/sectorRotation.js`
- **Fix:** Document as deliberate variant OR switch to EMA-based normalization.
- **Priority:** MEDIUM

#### 6. RRG Quadrant: Momentum threshold should be 100, not 0
- **Verdicts:** MISLEADING + MISLEADING + *(not asked)* (2/2 MISLEADING)
- **Issue:** Standard RRG uses 100/100 for both axes.
- **Note:** Our 0-centered momentum IS mathematically equivalent (delta = 0 means "no change"), but should be documented as a variant.
- **Priority:** MEDIUM — Functionally correct, labeling issue

#### 7. F&G Neutral zone 35-60 is too wide
- **Verdicts:** MISLEADING + MISLEADING + PLAUSIBLE (2/3 MISLEADING)
- **Note:** Gemini defends it as "noise reduction engineering" — a valid counterpoint. But CNN's actual zones don't match ours.
- **Fix:** Narrow to 40-55. Backtest first.
- **Priority:** MEDIUM

---

### B. SHOULD-IMPROVE — Suboptimal but functional

#### 8. ZigZag: Make volatility-adaptive instead of fixed 5%
- **Verdicts:** UNVERIFIED + MISLEADING + MISLEADING (2/3 MISLEADING)
- **All 3 say it should be ATR-based.** Gemini: "5% is too wide for low-vol stocks (JNJ) and too narrow for high-beta (NVDA)."
- **Fix:** Replace `0.05` with `1.5 * ATR / price`. Needs testing.
- **Priority:** MEDIUM — Upgraded from LOW based on Gemini's strong recommendation

#### 9. Trend Template 7/8 → consider 8/8 for "Strong"
- **Verdicts:** MISLEADING + MISLEADING + PLAUSIBLE (2/3 MISLEADING)
- **Gemini's defense:** "7/8 is a common implementation in screening software (e.g., MarketSmith) to catch names just before a 'Power Play' setup."
- **Decision:** Keep 7/8 but label transparently: 8/8 = "Textbook SEPA", 7/8 = "Strong". Backtest impact.
- **Priority:** LOW — Gemini provides practical justification

#### 10. Cup depth: Verify and tighten acceptance range
- **Verdicts:** MISLEADING + UNVERIFIED + *(not asked)*
- **Fix:** Tighten to 12-35% max. O'Neil says 15-33%.
- **Priority:** LOW

#### 11. 60% confidence threshold: Document validation
- **Verdicts:** MISLEADING + PLAUSIBLE + PLAUSIBLE (2/3 PLAUSIBLE)
- **Gemini:** "As long as PF 1.61 holds in out-of-sample testing, it is a valid optimization."
- **Fix:** Document that we walk-forward validated this. No code change.
- **Priority:** LOW

#### 12. Trend Template: Missing RS ≥ 70 criterion
- **Verdicts:** Perplexity flagged, GPT flagged, Gemini missed
- **Overlap:** Ties into item #4 (RS threshold). Raising RS from 1.0 partially addresses this.
- **Priority:** LOW

---

### C. ACKNOWLEDGED — Known tradeoffs we accept

| # | Item | 3-LLM View | Why we accept |
|---|------|-----------|---------------|
| 13 | RSI 50-70 | 3/3 PLAUSIBLE | Cardwell bull regime supports direction. No "correct" range exists. |
| 14 | F&G 60-80 Strong | 2 PLAUSIBLE + 1 VERIFIED | Gemini cites Baker & Wurgler. Avoiding extremes IS supported. |
| 15 | SPY 50 SMA declining | 2 UNVERIFIED + 1 PLAUSIBLE | Conservative guard. Low harm. Gemini recognizes as "negative divergence." |
| 16 | Score r=0.011 | All 3 differ | Internal metric. Motivated our categorical switch. Not public claim. |
| 17 | Agglomerative clustering | 3/3 PLAUSIBLE | Better than KMeans for unknown cluster count. |
| 18 | Touch-based scoring | 2 VERIFIED + 1 PLAUSIBLE | Murphy (1999) cited. Standard TA wisdom. |
| 19 | Asymmetric proximity 20/30% | 3/3 UNVERIFIED | No harm. Revisit if S&R quality issues arise. |
| 20 | 150 bars minimum | UNVERIFIED + PLAUSIBLE + VERIFIED | Gemini cites TA-Lib warm-up. Reasonable. |
| 21 | 2x ATR stop | 2 VERIFIED + 1 PLAUSIBLE | LeBeau & Lucas (1992). Standard practice. |
| 22 | 6-month RS lookback | UNVERIFIED + PLAUSIBLE | Common RRG practice. |
| 23 | Cap-size ±2 threshold | 3/3 UNVERIFIED | Advisory only, doesn't affect verdicts. |
| 24 | All-or-nothing 9/9 | 3/3 PLAUSIBLE | Selective by design. Backtest validated. See note below. |
| 25 | R:R ≥ 2:1 | UNVERIFIED + PLAUSIBLE | Standard wisdom. |
| 26 | $10M volume | MISLEADING + PLAUSIBLE | Keep — ensures institutional liquidity. |
| 27 | W-FRI resampling | 2/3 VERIFIED | ISO standard. |
| 28 | Sector as context only | UNVERIFIED + PLAUSIBLE | Consistent with RRG creator's intent. |
| 29 | 200 SMA rising 22 days | 2 VERIFIED + 1 PLAUSIBLE | Good translation of "1 month." |
| 30 | ADX ≥ 20 vs Wilder's 25 | VERIFIED + PLAUSIBLE | 20-25 = "pullback preferred" captures nuance. |
| 31 | 70/30 holding period | All 3 differ | Concept universal. Exact splits are heuristic. |
| 32 | Handle ≤ 1.02x lip | 2 PLAUSIBLE + 1 VERIFIED | O'Neil 2009 supports per Gemini. |
| 33 | Flat Base 20% uptrend | VERIFIED + PLAUSIBLE | Slightly permissive (25-30% ideal). Monitor. |
| 34 | Algorithm vs human | 2/2 PLAUSIBLE | Backtest validates our implementation. |
| 35 | Filter not Ranker | 2 PLAUSIBLE + 1 VERIFIED | Van Tharp (1998) cited directly by Gemini. |

---

### Special Note: 9/9 Gating System Assessment

**All 3 LLMs rated the 9/9 all-or-nothing approach as PLAUSIBLE:**
- **GPT:** "Potentially impractical — may drastically reduce opportunities."
- **Perplexity:** "Unusually strict... superiority of an all-criteria pass rule is unproven and strategy-specific."
- **Gemini:** "Creates a 'Super-Heuristic.' While it limits trade frequency, it ensures the trader only enters Stage 2 breakouts with high RS — the core of CANSLIM/SEPA philosophy."

**Bottom line:** No LLM says it's wrong. All say it's extremely conservative. Gemini is most supportive (aligns with SEPA philosophy). The key risk is **missed opportunities**, not false signals. Our backtest (238 trades/4 years ≈ 1/week) shows it produces adequate signal frequency. Monitor during paper trading — if 0 signals in a bull week, consider 8/9 with "missing criterion" advisory.

---

## Implementation Priority Order (Revised)

| Priority | Item | Type | Effort | Change from 2-LLM |
|----------|------|------|--------|--------------------|
| 1 | Remove "3.2x" hallucinated claim (#2) | **CRITICAL** | 10 min | ⬆️ Upgraded (2/3 HALLUCINATED) |
| 2 | VCP: Add volume dry-up check (#1) | **CRITICAL** | 1-2 hrs | ⬆️ Upgraded (3/3 unanimous) |
| 3 | Trend Template: 25% → 30% above 52-wk low (#3) | HIGH | 15 min | Unchanged |
| 4 | RS threshold: Backtest 1.0 vs 1.1 vs 1.2 (#4) | HIGH | 1 hr | Unchanged |
| 5 | RRG normalization: Document or fix baseline (#5) | MEDIUM | 30 min | New (Gemini confirmed) |
| 6 | RRG Momentum: Document 0 vs 100 deviation (#6) | MEDIUM | 30 min | Unchanged |
| 7 | F&G Neutral zone: Narrow from 35-60 (#7) | MEDIUM | 30 min + backtest | Unchanged (Gemini dissents) |
| 8 | ZigZag: ATR-adaptive (#8) | MEDIUM | 2 hrs | ⬆️ Upgraded from LOW |
| 9 | Trend Template 7/8 labeling (#9) | LOW | 30 min | Downgraded (Gemini defends) |
| 10 | Document 60% walk-forward validation (#11) | LOW | 15 min | Unchanged |
| 11 | Cup depth: Verify and tighten (#10) | LOW | 30 min | Unchanged |

---

## Gemini-Specific Insights (New findings not from GPT/Perplexity)

| Finding | Value |
|---------|-------|
| RSI 50-70 supported by **Andrew Cardwell's** bull regime research (40-80 range) | Strengthens our RSI choice |
| F&G 60-80 backed by **Baker & Wurgler (2006)** sentiment-momentum research | Upgrades from PLAUSIBLE toward VERIFIED |
| 50 SMA declining recognized as **"Negative Divergence"** (known TA concept) | Upgrades from UNVERIFIED |
| Filter vs Ranker directly cited **Van Tharp (1998)** "Trade Your Way to Financial Freedom" | Upgrades to VERIFIED |
| Touch-based scoring cited **Murphy (1999)** "Technical Analysis of the Financial Markets" | Strengthens VERIFIED |
| 2x ATR cited **LeBeau & Lucas (1992)** Chandelier Exit | Additional source |
| 150 bars cited **TA-Lib documentation** for indicator warm-up | Practical justification |
| Cup handle 1.02x cited **O'Neil (2009)** directly | Strengthens VERIFIED |
| 7/8 trend template defended as **"MarketSmith common implementation"** | Practical counterpoint to strict 8/8 |

---

## Feature Freeze Note

STA is in feature freeze. Items 1-4 (CRITICAL/HIGH) are **correctness fixes**, not new features, and are appropriate to implement. Items 5-11 require documentation or backtesting and should wait for paper trading results.
