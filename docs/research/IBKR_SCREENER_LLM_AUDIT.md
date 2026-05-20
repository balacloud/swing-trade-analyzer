# IBKR Screener — Multi-LLM Audit Results

> Same methodology as Universal Principles audit (Day 69). Collect all LLM responses, synthesize into final validated filter set.
> Created: Day 76 (May 20, 2026)

---

## Comparison Table

| # | Factor | Our Original | Perplexity | GPT | Gemini | Notes |
|---|--------|-------------|------------|-----|--------|-------|
| 1 | Market Cap | 1.00B → max | ✅ Keep | ✅ Keep | ✅ Keep | **3/3 unanimous** |
| 2 | Average Volume ($) | 5.00M → max | ✅ 5M | 🔧 10M | ✅ 5M | 2/3 say 5M — GPT outlier |
| 3 | Price/EMA(200) | 1.05 → 2.00 | 🔧 → 1.75 | 🔧 → 1.60 | 🔧 → 1.50 | **3/3 tighten cap** — range 1.50–1.75 |
| 4 | Price/EMA(50) | 1.00 → 1.30 | 🔧 → 1.20 | 🔧 → 1.25 | 🔧 → 1.15 | **3/3 tighten cap** — range 1.15–1.25 |
| 5 | ROE | 15 → 100 | 🔧 17 | ✅ 15 | ✅ 15 | 2/3 say 15 |
| 6 | EarnGrw% | 10 → 150 | 🔧 floor 20 | 🔧 floor 15 | 🔧 floor 25 | **3/3 raise floor** — range 15–25 |
| 7 | Inst. Percent Held | 25 → 95 | 🔧 30 → 80 | ✅ 25 → 95 | ✅ 25 → 95 | 2/3 keep 25 floor |
| 8 | Quick Ratio | 1.00 → max | 🔄 RS vs SPY +10% | 🔄 52W High proximity | 🔄 52W High proximity | **3/3 replace QR** — 2/3 prefer 52W High |
| 9 | MACD Histogram | 0 → max | ✅ Keep | ✅ Keep | 🔄 Replaced by EMA(20) | 2/3 keep MACD |
| 10 | Change % | -2 → 8 | ✅ Keep | ✅ Keep | ✅ Keep | **3/3 unanimous** |

---

## Perplexity Analysis — Key Points

### What Perplexity agreed with (4/10 unchanged)
- Market Cap ≥ $1B ✅
- Average Volume ($) ≥ $5M ✅
- MACD Histogram ≥ 0 ✅
- Change % -2 to 8 ✅

### What Perplexity tightened (3 changes)
**Price/EMA(200) cap: 2.00 → 1.75**
- Rationale: Minervini looks for stocks in the early-to-mid Stage 2, not late parabolic runs. At 2.00x (100% above 200 EMA), the stock has likely already made its big move.
- Assessment: Reasonable. Tighter cap = better entry timing.

**Price/EMA(50) cap: 1.30 → 1.20**
- Rationale: More than 20% above the 50 EMA = extended for a swing entry. Best Minervini setups are consolidations near (but above) the 50 EMA.
- Assessment: Agree. 1.20 is tighter but more actionable.

**Inst. Percent Held: 25→95 → 30→80**
- Floor raised to 30%: Minervini's actual published threshold is closer to 30%+.
- Cap lowered to 80%: >80% institutional ownership leaves little room for NEW institutional buying to drive price. Smart money already in = less fuel.
- Assessment: Both changes are well-reasoned.

### What Perplexity raised the floor on (2 changes)
**ROE: 15 → 17**
- Marginal. Likely reflects Minervini's actual published floor being slightly above 15%.
- Assessment: Minor, probably fine either way.

**EarnGrw%: 10 → 20**
- Significant change. 20% floor is more aggressive.
- Rationale: Minervini explicitly looks for earnings acceleration of 20-30%+ in the most recent quarters. 10% is mediocre growth.
- Assessment: Valid for pure Minervini style. Risk: might cut too many good stocks in recovery markets where 15% growth is excellent.

### What Perplexity replaced (1 major change)
**Quick Ratio → 52W RS vs SPY > +10%**
- Rationale: RS vs SPY is the single most important Minervini criterion. Quick Ratio is a financial health metric but less relevant for swing trading (we're in for 15-30 days, not years). RS > SPY is what actually drives Stage 2 institutional accumulation.
- Assessment: **Directionally correct** — RS vs SPY is more aligned with STA's core thesis (backtested RS > 1.2). However: ⚠️ **need to verify IBKR has "52W RS vs SPY" as a direct factor**. It was not visible in the screenshots. If IBKR doesn't have it natively, this replacement isn't possible.

---

## Key Open Question: Does IBKR Have 52W RS vs SPY?

This is the most important question before adopting Perplexity's recommendation #8.

**If YES (IBKR has RS vs SPY as a factor):**
- Replace Quick Ratio with RS vs SPY > +10% (i.e., stock outperformed SPY by at least 10% over 52 weeks)
- This directly maps to STA's backtested RS52W > 1.2 threshold (20%+ SPY outperformance proxy)
- ⚠️ Note: our STA threshold is RS > 1.2 (ratio), which means stock return / SPY return > 1.2. A "+10%" disparity is not exactly the same metric — need to clarify IBKR's definition.

**If NO (IBKR doesn't have it natively):**
- Keep Quick Ratio > 1.0 as a financial health gate
- RS validation falls to STA (which computes it precisely)
- The Price/EMA(200) + Price/EMA(50) combination remains the best available RS proxy in IBKR

**Action: Check IBKR factor list for any "relative performance", "RS", or "performance vs index" field.**

---

## Preliminary Scoring: Perplexity Recommendations

| Change | Confidence | Adopt? |
|--------|-----------|--------|
| Tighten Price/EMA(200) cap to 1.75 | High | ✅ Likely yes |
| Tighten Price/EMA(50) cap to 1.20 | High | ✅ Likely yes |
| Raise ROE floor to 17 | Low (marginal) | 🤷 Either way |
| Raise EarnGrw% floor to 20 | Medium | ⏳ Wait for GPT/Gemini |
| Tighten Inst. Held to 30→80 | High | ✅ Likely yes |
| Replace Quick Ratio with RS vs SPY | High IF available | ⚠️ Verify IBKR first |

---

## GPT Analysis — Key Points

### What GPT agreed with (5/10 unchanged)
- Market Cap ≥ $1B ✅
- ROE 15 → 100 ✅
- MACD Histogram ≥ 0 ✅
- Change % -2 to 8 ✅
- Inst. Percent Held 25 → 95 ✅ (kept original, unlike Perplexity)

### What GPT changed
**Average Volume ($): 5M → 10M floor**
- Rationale: $10M daily dollar volume is the institutional tradability threshold. $5M still allows stocks where institutions can't build meaningful positions without moving the market.
- Assessment: Strong argument. $10M ensures we're in liquid, institutionally-tradable names.

**Price/EMA(200) cap: 2.00 → 1.60**
- Rationale: >60% above 200 EMA = already extended for swing entry. Best actionable setups are in the 5–40% zone.
- Assessment: Tighter than Perplexity's 1.75 — GPT is most conservative here. Defensible.

**Price/EMA(50) cap: 1.30 → 1.25**
- Between our 1.30 and Perplexity's 1.20. Minor difference.

**EarnGrw% floor: 10 → 15 (not 20 like Perplexity)**
- GPT takes the middle ground. 15% is a reasonable earnings quality floor without being too aggressive.
- Assessment: More balanced than Perplexity's 20. Depends on market regime.

**Filter #8: Replace Quick Ratio with 52W High/Low Proximity**
- Rationale: Minervini explicitly requires price within 25% of 52W high (TT criterion 5). Quick Ratio is financial health (5-year horizon), not relevant to a 15–30 day swing.
- Proposed: Use IBKR's "52 Week High" factor to filter stocks within 25% of their high.
- ⚠️ Implementation question: IBKR shows "52 Week High" as an absolute price value, not a ratio. Need to check if IBKR has a "% from 52W High" or "Price/52W High" ratio field.

### GPT vs Perplexity key disagreements
| Point | Perplexity | GPT | Edge |
|-------|-----------|-----|------|
| Volume floor | 5M | 10M | GPT — more institutional |
| EarnGrw% floor | 20% | 15% | GPT — less aggressive, more survivors |
| Inst. Percent Held | 30 → 80 | 25 → 95 | Perplexity — Minervini threshold |
| Filter #8 replacement | RS vs SPY | 52W High proximity | Both valid — depends on IBKR availability |
| ROE floor | 17 | 15 | Minor — either works |

## Gemini Analysis — Key Points

### What Gemini kept (4/10)
- Market Cap ≥ 1B ✅
- Average Volume ($) 5M → max ✅ (agrees with Perplexity, not GPT's 10M)
- ROE ≥ 15 ✅
- Change % -2 to 8 ✅

### What Gemini changed
**EarnGrw% floor: 10 → 25 (most aggressive)**
- Rationale: "Minervini standard for hyper-growth." Minervini's published methodology explicitly targets stocks with 25%+ EPS growth as a primary requirement.
- Assessment: Most aligned with Minervini's actual published text. Aggressive but defensible.

**Price/EMA(200) cap: 2.00 → 1.50 (tightest of all 3)**
- Rationale: Avoids climax runs. >50% above 200 EMA = late Stage 2 or Stage 3 top.
- Assessment: Most conservative. Combined with all others: consensus range is 1.50–1.75.

**Price/EMA(50) cap: 1.30 → 1.15, sort preference = LOWER**
- Most aggressive cap. The Lower sort is the key insight: Gemini wants stocks CLOSE to their 50 EMA (in consolidation/base). This is the VCP setup profile — stock near the 50 EMA in a tight base, not extended above it.
- Assessment: Philosophically correct for Minervini VCP setups. Very different from GPT/Perplexity's Higher sort.

**Dropped MACD Histogram, replaced with Price/EMA(20)**
- Gemini brings back the filter we dropped to stay within 10 items. Short-term trend confirmation via EMA(20) is simpler and directly maps to TT criterion 7.
- Assessment: Valid trade — Price/EMA(20) > 1.0 is cleaner than MACD Histogram for TT alignment.

**Filter #8: 52W High Proximity within -25% (not Quick Ratio)**
- Agrees with GPT: Minervini TT criterion 5 (within 25% of 52W high). Rejects Perplexity's RS vs SPY.
- Implementation format: FROM -25% TO max (meaning price is no more than 25% below 52W high).
- ⚠️ Same availability question as GPT: need to verify IBKR has a % proximity field, not just absolute 52W High value.

---

## Final Validated Filters — 3-LLM Synthesis

### Decision rules applied
- **3/3 agree** → adopt as-is
- **2/3 agree** → adopt majority, note the outlier
- **Split with range** → take the median value
- **Availability unknown** → flag for IBKR verification before adopting

| # | Factor | Final FROM | Final TO | Sort | Basis |
|---|--------|-----------|---------|------|-------|
| 1 | Market Cap | 1.00 B | max | No Preference | 3/3 unanimous |
| 2 | Average Volume ($) | 5.00 M | max | Higher Values | 2/3 (GPT's 10M would over-cut mid-caps) |
| 3 | Price/EMA(200) | 1.05 | **1.65** | No Preference | 3/3 tighten; median of 1.50/1.60/1.75 |
| 4 | Price/EMA(50) | 1.00 | **1.20** | No Preference | 3/3 tighten; median of 1.15/1.20/1.25 |
| 5 | ROE | **15** | 100 | No Preference | 2/3 say 15; Perplexity's 17 is marginal |
| 6 | EarnGrw% | **20** | max | Higher Values | Median of 15/20/25; balances signal vs survivors |
| 7 | Inst. Percent Held | **25** | **90** | No Preference | Floor: 2/3 keep 25. Cap: median of 80/95/95 = 90 |
| 8 | 52W High Proximity | **-25%** | max | Higher Values | 2/3 (GPT+Gemini) prefer this over RS vs SPY. ⚠️ Verify in IBKR |
| 9 | MACD Histogram | **0** | max | Higher Values | 2/3 keep; Gemini's EMA(20) alternative is valid if MACD unavailable |
| 10 | Change % | -2 | 8 | Higher Values | 3/3 unanimous |

---

### Key unresolved: IBKR availability check needed

**Before applying filter #8**, verify in IBKR whether either of these exists as a filterable factor:
- "52W High Proximity %" or "% from 52W High" or "Price/52W High" — this is what GPT + Gemini recommend
- The screenshots only show "52 Week High" and "52 Week Low" as absolute price values

**If 52W High Proximity IS available:** use as filter #8 (FROM -25%, TO max)
**If NOT available:** use MACD Histogram as #8 and add Price/EMA(20) > 1.0 as #9, drop Change % to a display column (it's a sanity filter STA handles anyway)

---

### What changed most from our original
| Factor | Original | Final | Why |
|--------|----------|-------|-----|
| Price/EMA(200) cap | 2.00 | **1.65** | All 3 LLMs agree: 2.00 lets in extended/climax stocks |
| Price/EMA(50) cap | 1.30 | **1.20** | All 3 LLMs agree: tighter = cleaner VCP/base setups |
| EarnGrw% floor | 10 | **20** | All 3 raise it — 10% is mediocre growth, not Minervini |
| Filter #8 | Quick Ratio | **52W High Proximity** | All 3 replace QR — wrong metric for 15-30 day swing |
| Inst. Held cap | 95 | **90** | Minor tighten — marginal |

### What held up well from our original
- Market Cap 1B, Average Volume 5M, ROE 15, MACD Histogram ≥ 0, Change % -2 to 8 — all validated by majority

---

### Expected survivor count with final filters
| Market Condition | Estimate |
|-----------------|---------|
| Bull Trend (current May 2026) | 40–70 stocks |
| Late Bull / Distribution | 20–40 stocks |
| Correction | 5–15 stocks |

Self-calibrating: fewer survivors in bad markets = fewer trades = correct behaviour.
