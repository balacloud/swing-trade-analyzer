# Manual UI Validation Test Plan - 30 Diverse Tickers

> **Purpose:** Systematic manual validation of the Swing Trade Analyzer across 30 diverse tickers and all 3 holding periods. Test every UI section, verify internal consistency, and identify logic/display bugs.
>
> **Created:** Day 53 (February 11, 2026)
> **Priority:** TOP - This is our most important testing effort

---

## What Changes vs. Stays Same When Switching Holding Period

### CHANGES when you switch periods:
| Component | How It Changes |
|-----------|---------------|
| **Verdict (BUY/HOLD/AVOID)** | May change when Tech and Fundamental disagree (weighting tips the balance) |
| **Bottom Line Card** | Action label, weight badges (T:XX%/F:XX%), weight note, what's good/risky, action plan - all regenerate |
| **Weight Badges** | Quick=T:70%/F:30%, Standard=T:50%/F:50%, Position=T:30%/F:70% |

### CORRECTLY stays the same:
| Component | Why It Doesn't Change |
|-----------|----------------------|
| **Assessment Cards (T/F/S/R)** | Individual assessments are factual observations - only their weighting in verdict changes |
| **Pattern Detection** | Patterns are timeframe-agnostic (a VCP is a VCP regardless of holding period) |
| **Technical Indicators** | RSI, EMAs, SMAs are raw values - facts, not opinions |
| **Quality Gates** | RS < 0.8 or Below 200 SMA are structural issues regardless of period |
| **ADX/OBV/RVOL/4H RSI badges** | Market microstructure data - doesn't change with intent |

### KNOWN GAP - Stays same but arguably SHOULD change (NOT a bug, noted for future):
| Component | Current Behavior | Ideal Behavior |
|-----------|-----------------|----------------|
| **Stop distances** | Always 2×ATR (pullback), 1.5×ATR (momentum) | Quick: tighter (1-1.5 ATR), Position: wider (2.5-3 ATR or weekly S&R) |
| **Target prices** | Same target for all periods | Quick: nearest R1, Position: R2/R3 or 52wk high |
| **R:R ratios** | Fixed (tied to fixed stops/targets) | Should recalculate from period-adjusted stops/targets |
| **Viability badge** | Fixed (tied to R:R) | Would update if R:R changes |
| **S&R emphasis** | Daily levels shown for all | Position trades: weekly levels should be primary |

> **For testers:** When switching periods, note if the trade setup stays the same - that's expected current behavior. Flag it as "KNOWN GAP" not "BUG". Focus testing energy on whether the verdict change and Bottom Line Card content make logical sense for each period.

---

## Rules of Engagement (For Claude When Reviewing)

1. **Do NOT assume** - Only state what the screenshot and data show
2. **Do NOT hallucinate** - If something is unclear, ask for clarification
3. **Think critically** - Question whether the system's output makes logical sense
4. **No confirmation bias** - Actively look for things that are WRONG, not things that are right
5. **Think holistically** - When fixing code, consider ripple effects across all UI sections and backend
6. **Do NOT blindly fix** - Diagnose root cause before writing any code change
7. **Research and verify** - Cross-reference values against external data when possible
8. **Extract everything** - When reviewing a screenshot, extract ALL visible data points before analyzing

---

## Test Protocol

### For Each Ticker:

1. Enter ticker in search bar → Press Enter
2. Wait for full analysis to load
3. **Screenshot the FULL page** (scroll and capture all sections)
4. Test in **Standard (15-30d)** period first
5. Switch to **Quick (5-10d)** → note what changes
6. Switch to **Position (1-3mo)** → note what changes
7. Record observations using the template below
8. Provide screenshots + written observations to Claude

### What To Capture in Screenshots:
- Full verdict card (top section with ticker, price, verdict, T/F/S/R badges)
- Trade Setup card (viability badge, entry cards, S&R levels)
- Pattern Detection card (Trend Template, 3 patterns, actionable section)
- Bottom Line Card (action label, what's good, what's risky, action plan)
- Assessment card (all 4 categories expanded if possible)
- Technical Indicators card
- Quality Gate Warnings (if visible)
- Any earnings warning badge

---

## 30 Ticker Selection

### Rationale for Diversity

The tickers are chosen to cover every dimension: market cap, sector, trend state, ADX range, fundamental profile, and edge cases. Each ticker has an **expected behavior** listed - this is what we THINK the system should show. The test validates whether reality matches expectation.

---

### Group A: Large-Cap Tech (6 tickers)
*Tests: Strong fundamentals + various technical states*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 1 | **AAPL** | Tech | Benchmark mega-cap, should be baseline | Decent/Strong tech, Strong fund |
| 2 | **NVDA** | Tech/Semis | High-momentum leader, expensive | Strong tech (high RS), check if extended |
| 3 | **MSFT** | Tech | Steady compounder, less volatile | Likely Decent tech, Strong fund |
| 4 | **AMZN** | Consumer/Tech | High-growth, mixed margins | Check fundamental assessment accuracy |
| 5 | **GOOG** | Communication | Value-ish tech, strong balance sheet | Should have Strong fund |
| 6 | **TSLA** | Auto/Tech | Extreme volatility, polarizing fundamentals | Edge case - high ADX swings, check pattern detection |

### Group B: Financials & Healthcare (4 tickers)
*Tests: Non-tech sectors, different fundamental profiles*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 7 | **JPM** | Financials | Strongest bank, steady | Strong fund, moderate tech |
| 8 | **JNJ** | Healthcare | Defensive, high dividend | Weak tech (low RS?), Strong fund |
| 9 | **UNH** | Healthcare | Growth healthcare, expensive | Check if RS is strong vs SPY |
| 10 | **GS** | Financials | Cyclical financial, volatile | Check ADX-based entry preference |

### Group C: Energy & Industrials (4 tickers)
*Tests: Commodity-linked sectors, cyclical behavior*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 11 | **XOM** | Energy | Dividend value play | Likely low RS, check S&R level quality |
| 12 | **CVX** | Energy | Similar to XOM, test consistency | Should give similar assessment to XOM |
| 13 | **CAT** | Industrials | Infrastructure play, cyclical | Check if fundamental data sources work |
| 14 | **DE** | Industrials | Farm equipment, seasonal | Check if pattern detection finds anything |

### Group D: Consumer & Retail (3 tickers)
*Tests: Different growth profiles within same sector*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 15 | **COST** | Consumer Staples | Steady grower, premium valuation | Decent/Strong across board |
| 16 | **WMT** | Consumer Staples | Defensive, low beta | Low ADX expected, check "wait for trend" logic |
| 17 | **LULU** | Consumer Disc. | Growth retail, volatile | Check if RS captures relative strength properly |

### Group E: High-Volatility / Speculative (5 tickers)
*Tests: Edge cases, extreme values, data quality*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 18 | **COIN** | Fintech/Crypto | Extreme vol, earnings sensitive | Check earnings warning, high ADX |
| 19 | **SMCI** | Tech/Hardware | Massive swings, accounting concerns | Weak fund?, check if verdict reflects risk |
| 20 | **AFRM** | Fintech | Low price, speculative growth | Likely AVOID, check if all sections consistent |
| 21 | **MARA** | Crypto Mining | Bitcoin-correlated, low fundamentals | Should trigger quality gates (low RS?) |
| 22 | **RIVN** | EV/Auto | Pre-profit, high short interest | Weak fund (no earnings), check fundamental handling |

### Group F: Dividend / Defensive (3 tickers)
*Tests: Low-volatility stocks, position trade candidates*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 23 | **VZ** | Telecom | Low ADX, dividend play | ADX < 20 expected → "wait for trend" |
| 24 | **PG** | Consumer Staples | Ultimate defensive stock | Strong fund, check tech assessment for slow movers |
| 25 | **O** | REIT | Monthly dividend, rate-sensitive | Check if fundamental data works for REITs |

### Group G: Mid-Cap Growth (3 tickers)
*Tests: Mid-cap data quality, growth stock assessment*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 26 | **CRWD** | Cybersecurity | High-growth SaaS | Strong tech + fund? Check RS calculation |
| 27 | **DKNG** | Gaming/Tech | Speculative growth, volatile | Mixed signals expected, test verdict logic |
| 28 | **ENPH** | Solar/Energy | Beaten down from highs | May trigger Below 200 SMA quality gate |

### Group H: ETFs & Special Cases (2 tickers)
*Tests: ETF handling (no fundamentals), edge cases*

| # | Ticker | Sector | Why Selected | Expected Behavior |
|---|--------|--------|--------------|-------------------|
| 29 | **SPY** | ETF | S&P 500 index - RS should be ~1.0 | Fundamental should show N/A (ETF), RS ≈ 1.0 |
| 30 | **QQQ** | ETF | Nasdaq 100 - RS should be > 1.0 if tech leads | Same ETF handling check, compare RS vs SPY |

---

## Observation Template

Use this template for EACH ticker (copy-paste and fill in). You can abbreviate where needed.

```
### Ticker: [SYMBOL] | Period: [quick/standard/position]

**1. VERDICT CARD**
- Verdict: [BUY/HOLD/AVOID]
- Categories: T:[S/D/W] F:[S/D/W] S:[S/N/W] R:[F/N/U]
- Price: $___
- Sector/Industry: ___
- Earnings badge: [None / "EARNINGS IN X DAYS" / "EARNINGS TODAY"]

**2. TRADE SETUP**
- Viability badge: [BOTH VIABLE / PULLBACK OK / MOMENTUM OK / NOT VIABLE]
- Position size banner: [Visible with text / Hidden]
- ADX badge: ___ (color: ___)
- 4H RSI badge: ___ (color: ___)
- OBV badge: [↑/↓/→] (divergence: ___)
- RVOL badge: ___x
- Distribution Warning: [Yes/No]
- Pullback entry: Entry=$___ Stop=$___ Target=$___ R:R=___
- Momentum entry: Entry=$___ Stop=$___ Target=$___ R:R=___
- Pullback card: [Normal / Grayed ⛔ / ★ PREFERRED]
- Momentum card: [Normal / Grayed ⛔ / ★ VIABLE / ⚠ CAUTION]
- S&R levels count: S=___ R=___
- MTF confluence: ___% (N/M)
- AVOID+VIABLE conflict warning: [Yes/No/N/A]

**3. PATTERN DETECTION**
- Trend Template: ___/8
- Stage 2 confirmed: [Yes/No]
- VCP: [Not detected / X% confidence]
- Cup & Handle: [Not detected / X% confidence]
- Flat Base: [Not detected / X% confidence]
- Actionable patterns: [None / List with trigger/stop/target]
- Breakout quality: [N/A / High / Medium / Low / Approaching]

**4. BOTTOM LINE CARD**
- Action label: [READY - MOMENTUM / READY - PULLBACK / WAIT FOR PULLBACK / SKIP]
- Period shown: ___
- Weight badges: T:___% F:___%
- Weight note: [None / "text..."]
- What's Good count: ___ points
- What's Risky count: ___ points
- Action Plan steps: ___ steps
- Verdict reason: "___"

**5. ASSESSMENT CARDS (expand all 4)**
- Technical: [S/D/W] - Key reasons: ___
- Fundamental: [S/D/W/N/A] - Key reasons: ___
- Sentiment: [S/N/W] - F&G value: ___
- Risk/Macro: [F/N/U] - VIX: ___ SPY Regime: ___
- "Why This Verdict?" text: "___"

**6. TECHNICAL INDICATORS**
- RSI(14): ___
- 8 EMA: ___
- 21 EMA: ___
- 50 SMA: ___
- 200 SMA: ___
- ATR: ___

**7. QUALITY GATES**
- Triggered: [None / RS Below Threshold / Below 200 SMA / Low Liquidity]
- Values if triggered: ___

**8. DATA SOURCE STATUS**
- Banner: [None / "Fundamentals Unavailable" / "Using Backup Source: ___"]

**OBSERVATIONS / ISSUES:**
- [Free-form notes on anything that looks wrong, inconsistent, or surprising]

**HOLDING PERIOD COMPARISON** (after testing all 3):
- Quick verdict: ___ | Standard verdict: ___ | Position verdict: ___
- Did verdict change? [Yes/No] - Makes sense? [Yes/No/Questionable]
- Bottom Line action changed? [Yes/No]
- Weight note appeared? [Yes/No] - Accurate? [Yes/No]
```

---

## Validation Checks (What I Will Verify)

For each observation you submit, I will systematically check:

### Check 1: Verdict Consistency
- Does the verdict (BUY/HOLD/AVOID) logically follow from T/F/S/R categories?
- Does it match the documented verdict logic in `categoricalAssessment.js`?
- Cross-reference: BUY requires 2+ Strong with Favorable/Neutral risk
- Cross-reference: Weak tech = always AVOID
- Cross-reference: Unfavorable risk = HOLD at best

### Check 2: Holding Period Impact
- Does switching periods change the verdict when T and F disagree?
- Quick: Does Strong Tech + Weak Fund → BUY (tech 70%)?
- Position: Does Weak Fund → AVOID regardless of tech?
- Position: Does Strong Fund + Decent Tech → BUY (fund 70%)?
- Standard: Is it the balanced middle ground?
- Weight badges: Do they show correct percentages (70/30, 50/50, 30/70)?

### Check 3: Trade Setup Coherence
- Viability badge matches actual R:R values?
  - BOTH VIABLE: both R:R >= 1.0
  - PULLBACK OK: only pullback R:R >= 1.0
  - MOMENTUM OK: only momentum R:R >= 1.0
  - NOT VIABLE: both R:R < 1.0
- Position size banner HIDDEN when verdict=AVOID or ADX < 20?
- Entry cards grayed out (⛔) when R:R < 1?
- ★ PREFERRED on pullback when ADX >= 25 and pullback viable?
- Stop prices make physical sense (below support, not below zero)?
- Target prices make sense (above entry, not unreasonably far)?
- R:R ratios are mathematically correct: (Target - Entry) / (Entry - Stop)?
- AVOID verdict + VIABLE badge → conflict warning shown?

### Check 4: S&R Level Quality
- Are support levels BELOW current price?
- Are resistance levels ABOVE current price?
- Do the levels make sense for the stock's price range?
- Is MTF confluence badge shown when weekly levels overlap daily?
- Are ★ marks on MTF-confluent levels?
- At least 1 support and 1 resistance level present?

### Check 5: Pattern Detection Accuracy
- Trend Template: Does the X/8 score make sense given the stock's chart?
  - Uptrending stock should be 6-8/8
  - Downtrending stock should be 0-3/8
  - Sideways should be 3-5/8
- Are detected patterns realistic? (e.g., VCP shouldn't appear on a stock in freefall)
- Actionable patterns (>= 80%) - do trigger/stop/target prices make sense?
- Volume confirmation on breakout patterns - realistic?

### Check 6: Bottom Line Card Quality
- Does the action label match the verdict?
  - BUY → "READY - MOMENTUM" or "READY - PULLBACK" (based on ADX)
  - HOLD → "WAIT FOR PULLBACK"
  - AVOID → "SKIP THIS ONE"
- Are "What's Good" points actually good? (not contradicting the data)
- Are "What's Risky" points actually risks? (not missing obvious ones)
- Does the action plan give actionable prices (entry, stop, target)?
- Does the weight note accurately describe the holding period impact?
- Period label correct (matches selected period)?

### Check 7: Assessment Card Accuracy
- Technical: Does Strong/Decent/Weak match Trend Template + RSI + RS data?
  - Strong: High TT score + RSI in range + RS > 1.2
  - Decent: Medium TT + acceptable RSI + RS ~1.0
  - Weak: Low TT + poor RSI/RS
- Fundamental: Does the assessment match the reason bullets?
  - Check ROE, Revenue Growth, Debt/Equity thresholds
  - ETFs should show N/A
- Sentiment: Does F&G value match assessment?
  - Strong: 60-75 (or 55-75 per our logic)
  - Neutral: 35-60
  - Weak: < 35 or > 75
- Risk/Macro: Does VIX + SPY regime match assessment?
  - Favorable: VIX < 20 AND SPY > 200 EMA
  - Unfavorable: VIX > 30 OR SPY < 200 EMA
- "Why This Verdict?" text matches the actual verdict reason?

### Check 8: Technical Indicator Sanity
- RSI(14) between 0-100?
- Price > 200 SMA for uptrending stocks?
- 8 EMA > 21 EMA > 50 SMA > 200 SMA for strong uptrends?
- EMA/SMA values reasonable for the stock's price?
- ATR reasonable for the stock's volatility profile?

### Check 9: Quality Gate Triggers
- RS < 0.8 → quality gate shown?
- Price < 200 SMA → quality gate shown?
- Low volume stocks → liquidity gate shown?
- 2+ critical fails → auto-AVOID?

### Check 10: Data Source & Earnings
- Data source banner: shown only when fallback data used?
- Earnings warning: timing accurate (check against known earnings dates)?
- Earnings badge styling correct (red pulse ≤3 days, yellow 4-7 days)?

---

## Recommended Testing Order

### Phase 1: Baseline Stocks (Tickers 1-6, Day 1)
Start with the large-cap tech stocks. These have the most reliable data and should be the easiest to validate. Any issues found here are systemic.

**Deep dive all 3 periods:** AAPL, NVDA, TSLA (most likely to show verdict changes)
**Standard period only:** MSFT, AMZN, GOOG

### Phase 2: Sector Spread (Tickers 7-17, Day 1-2)
Test non-tech sectors. Focus on whether fundamental data arrives correctly from different providers and whether the assessment makes sense for non-tech stocks.

**Deep dive all 3 periods:** JNJ (defensive), XOM (energy), LULU (growth retail)
**Standard period + one other:** JPM, UNH, GS, CVX, CAT, DE, COST, WMT

### Phase 3: Edge Cases (Tickers 18-25, Day 2)
These are the most likely to expose bugs - volatile stocks, speculative names, REITs, telecoms.

**Deep dive all 3 periods:** COIN (earnings + volatile), RIVN (pre-profit), VZ (low ADX)
**Standard period + one other:** SMCI, AFRM, MARA, PG, O

### Phase 4: Special Cases (Tickers 26-30, Day 2-3)
Mid-cap growth and ETFs. ETFs are the most critical edge case for fundamental handling.

**Deep dive all 3 periods:** SPY (RS baseline check)
**Standard period + one other:** CRWD, DKNG, ENPH, QQQ

---

## Specific Things to Watch For

### Known Risk Areas (from previous testing)
1. **R:R badge graying** - Cards with R:R < 1 should be visually grayed (opacity-60). Check if the ⛔ badge appears AND the card looks dimmed.
2. **AVOID + VIABLE conflict** - If verdict is AVOID but a setup has R:R >= 1, a warning should appear. Check for this on any AVOID stock with decent S&R.
3. **Position size banner visibility** - Should be HIDDEN when AVOID or ADX < 20. Check especially for ADX 19-21 borderline stocks.
4. **Earnings warning accuracy** - COIN and any stock with upcoming earnings. Verify the date shown matches reality.
5. **ETF fundamental handling** - SPY and QQQ should show "N/A" for fundamentals, not "Weak" or error.
6. **Below 200 SMA quality gate** - Beaten-down stocks (ENPH, RIVN, MARA) should trigger this.
7. **Holding period verdict changes** - F stock (Day 53 testing) correctly showed BUY→HOLD→AVOID across periods. Verify this pattern for stocks where T and F disagree.

### Data Quality Red Flags
- Any `null`, `N/A`, `undefined`, or `NaN` in indicator values
- ATR = 0 or negative values
- S&R levels outside the stock's 52-week range
- RS ratio that seems implausible (e.g., RS = 0.1 for an outperforming stock)
- Missing sector/industry information
- Price data that seems stale (significantly different from known market price)

### Logic Red Flags
- BUY verdict with Weak technical (should be impossible)
- BUY verdict with Unfavorable risk (should be impossible)
- AVOID verdict but "READY" action in Bottom Line Card
- HOLD verdict but "SKIP THIS ONE" in Bottom Line Card
- Entry price in momentum card significantly different from current price
- Stop price ABOVE entry price
- Target price BELOW entry price
- R:R shown as negative

---

## How to Report Observations

### Format for Each Ticker Post:
```
**Ticker: [SYMBOL]**
**Date/Time tested:** [when]
**Periods tested:** [quick/standard/position]

[Paste filled observation template]

[Attach screenshots - label them clearly]

**My Key Observations:**
1. [Most important finding]
2. [Second finding]
3. ...
```

### Priority Labels:
- **BUG** - Something is clearly wrong (incorrect calculation, crash, missing data)
- **INCONSISTENCY** - Two parts of the UI contradict each other
- **QUESTIONABLE** - The system's output seems off but might be defensible
- **COSMETIC** - Visual/formatting issue that doesn't affect correctness
- **GOOD** - Something that works particularly well (helps identify strengths)

### Batch Size:
- Submit 3-5 tickers per batch for review
- I will review each batch thoroughly before you proceed
- This ensures we catch systemic issues early (no point testing 30 tickers if ticker #2 reveals a fundamental flaw)

---

## Success Criteria

At the end of 30 tickers:

| Metric | Target |
|--------|--------|
| Verdict consistency | 100% (no illogical verdicts) |
| Holding period impact | Correct weight change for all tested combos |
| R:R math accuracy | 100% (calculations must be correct) |
| S&R level sanity | 95%+ (levels below/above price correctly) |
| Quality gate triggers | 100% (must fire when conditions met) |
| Bottom Line Card coherence | 100% (action matches verdict) |
| Data source handling | No crashes, graceful fallback |
| Pattern detection plausibility | 90%+ (no obviously wrong patterns) |
| Technical indicator sanity | 100% (no NaN, null, impossible values) |
| ETF edge case handling | 100% (fundamentals show N/A) |

---

## Proactive Bug Checklist (Auto-Check Every Ticker)

> **Created:** Day 53 — Derived from patterns in Bugs #1-#6 found during testing.
> **Purpose:** These checks are AUTOMATED based on bug patterns we've seen. Apply to every ticker.

### Pattern A: Field Name Mismatches (Bugs #1, #2)
> After v4.14 DataProvider migration, yfinance field names changed. Any new field access needs verification.

- [ ] Stock name shows actual company name (not "TICKER - TICKER")
- [ ] Avg Volume / Liquidity shows a real number (not $0.0M for liquid stocks)
- [ ] Sector/Industry populated (not "Unknown" for common stocks)
- [ ] 52-week high/low values present and reasonable

### Pattern B: Array Ordering (Bugs #3, #6)
> Support array is sorted ascending. `[0]` = farthest, `Math.max()` = nearest.

- [ ] BottomLineCard "% above nearest support" uses realistic nearby level (not the farthest support)
- [ ] Recommendation card alert price is near current price (not 20%+ below)
- [ ] Pullback entry zone text shows a reasonable pullback level
- [ ] Action plan "pullback to $X" price is the nearest support, not the lowest

### Pattern C: Threshold Alignment (Bug #4)
> Different files used different thresholds for the same concept.

- [ ] ADX 25-30: BottomLineCard says "PULLBACK ENTRY" (not "MOMENTUM ENTRY")
- [ ] ADX >= 30: BottomLineCard says "MOMENTUM ENTRY"
- [ ] ADX < 20: Trade Setup says "wait for trend" and position size banner is HIDDEN
- [ ] F&G 35-60: Neutral gray color in Assessment card (not red/green)
- [ ] F&G 60-80: Green color in Assessment card
- [ ] F&G < 35 or > 80: Red color (extreme fear or extreme greed)

### Pattern D: Hardcoded Text vs Dynamic Data (Bug #5)
> Static messages that don't match the actual data values.

- [ ] If TT >= 7/8 but Tech = Weak: "What's Risky" says "in Stage 2 but weak RS/RSI" (NOT "not in Stage 2")
- [ ] If TT >= 7/8 but Tech = Weak: Action plan says "wait for RS to improve" (NOT "wait for Stage 2")
- [ ] If verdict = BUY + setup NOT VIABLE: Bottom Line says "wait for pullback" (NOT "momentum entry viable")
- [ ] "Strong stock" text only appears when Technical assessment IS actually Strong

### Pattern E: Independent System Contradictions (RIVN, AAPL cases)
> Three independent layers can legitimately disagree, but UI should explain why.

- [ ] If AVOID + trade setup VIABLE: Yellow warning "Stock not recommended" is visible
- [ ] If BUY + trade setup NOT VIABLE: Entry cards are grayed out + "wait for pullback" in action plan
- [ ] If Pattern Detection says "Stage 2" but Technical says "Weak": "What's Risky" explains the discrepancy
- [ ] Position Size banner is HIDDEN when verdict = AVOID
- [ ] Position Size banner is HIDDEN when ADX < 20

### Pattern F: Liquidity vs Volume Clarity
> Volume = shares traded (relative badge). Liquidity = dollar volume (Price Data card).

- [ ] Price Data card shows "Liquidity (Daily $)" label with dollar amount
- [ ] Liquidity color: Green >= $50M, Yellow >= $10M, Red < $10M
- [ ] Quality Gate triggers for Liquidity < $10M (shows warning banner)
- [ ] Vol badge (e.g., "Vol 1.14x") is separate and shows relative volume ratio

### Pattern G: Type Mismatches (Bug #7)
> A value computed as one type (number) compared as another (string). Fails silently — no error, just wrong behavior.

- [ ] RS Rating color: green ≥70, yellow ≥50, red <50 (NOT string comparison to 'Strong'/'Moderate')
- [ ] Pattern confidence values arrive as numbers, not strings (verify before `>=` comparisons)
- [ ] Any new backend field: check if arrives as string "42" vs number 42 (JSON parsing edge case)
- [ ] Boolean fields: verify `=== true` not `=== 'true'` (string vs boolean)

### Pattern H: Competing Truth Sources (Bug #8)
> Two independent systems claim authority over the same concept. User sees contradictory signals.

- [ ] Backend `viable: "YES"` + Frontend R:R < 1.0: Banner should say "Structural stop sound, R:R insufficient" (yellow, NOT green "Good setup")
- [ ] Backend `position_size_advice: "FULL"`: suppressed when verdict = AVOID or ADX < 20
- [ ] BottomLineCard entry type matches Trade Setup card (both say "pullback" or both say "momentum", not contradicting)
- [ ] Pattern Detection "Stage 2" (TT ≥ 7/8) vs Technical "Weak": Both can be true but "What's Risky" explains WHY
- [ ] Backend advice text does NOT contradict frontend R:R badge on the same card

### Pattern I: Computed-But-Hidden Data (Free Wins)
> Features already computed in JS but never surfaced to the trader. Each is a one-line fix.

- [ ] RS interpretation text shown under RS value (e.g., "Slight underperformance (momentum fading)")
- [ ] RS Rating color reflects actual numeric value (green/yellow/red based on 70/50 thresholds)
- [ ] ADX analysis recommendation accessible (tooltip or text below ADX badge)
- [ ] Signal weights displayed when holding period is NOT standard (explains why verdict differs)
- [ ] Sentiment subLabel shown: "Neutral (Optimistic)" vs "Neutral (Cautious)" — different implications

### Pattern J: Missing Interpretation Layer (Decision Gap)
> Raw numbers shown without trader-friendly meaning. The core gap the Decision Matrix will solve.

- [ ] R:R < 1.0: Does the UI explain "risk outweighs reward" or just show ⛔?
- [ ] Pattern 70% forming: Does the UI say what to DO (watchlist) or just show the percentage?
- [ ] ADX 23: Does the UI explain "moderate trend, pullback preferred" or just show the number?
- [ ] RS 0.95: Does the UI explain "underperforming S&P by 5%" or just show the ratio?
- [ ] "acceptable for position trade": Does it explain what this MEANS or just state it?

---

## Post-Test Action Plan

After all 30 tickers are tested:

1. **Compile all BUG and INCONSISTENCY findings** into a fix list
2. **Prioritize by frequency** (issues appearing across many tickers = highest priority)
3. **Root cause analysis** before any code changes
4. **Fix one issue at a time** → re-test affected tickers → confirm fix doesn't break others
5. **Re-run automated verification** (`node frontend/scripts/ui-verify-checklist.js`, rewritten Day 124 for the redesigned page) after fixes. Note: the verdict and entry-card items earlier in this plan describe the pre-Day-123 page.
6. **Update KNOWN_ISSUES document** with resolved/new issues
7. **Document any new Golden Rules** discovered during testing

---

## Test Results

### Ticker #1: AAPL | Period: Quick (5-10 days)
**Date:** Day 53 | **Verdict:** AVOID | **Categories:** T:D F:D S:N R:N

**Issues Found:**
- **BUG #1 (FIXED):** Low Liquidity $0.0M - false quality gate. Field name mismatch: `averageVolume` vs `avgVolume` after v4.14. Fixed in backend.py.
- **BUG #2 (FIXED):** "AAPL - AAPL" instead of "Apple Inc." Same field name mismatch: `shortName` vs `name`. Fixed in backend.py.
- **BUG #3 (FIXED):** BottomLineCard "22.0% above nearest support" used `support[0]` (lowest=$214.56) instead of `Math.max(...support)` (nearest=$259.24). Fixed in BottomLineCard.jsx.
- **QUESTIONABLE:** T:Decent/F:Decent/S:Neutral/R:Neutral → AVOID. No Strong categories → falls to default. Possibly should be HOLD for all-mediocre profiles.

---

### Ticker #22: RIVN | Period: Position (1-3 months)
**Date:** Day 53 | **Verdict:** BUY | **Categories:** T:S F:D S:N R:F

**1. VERDICT CARD**
- Verdict: BUY | Price: $17.64
- Sector: Consumer Cyclical • Auto Manufacturers
- Avg Daily $ Vol: $659M (green) — new field working correctly

**2. TRADE SETUP**
- Viability: NOT VIABLE (both R:R < 1)
- Pullback: Entry=$17.15 Stop=$15.19 Target=$18.60 R:R=0.74 (grayed ⛔)
- Momentum: Entry=$17.64 Stop=$15.68 Target=$18.60 R:R=0.49 (grayed ⛔)
- ADX 26.6 (green), 4H RSI 67.1 (green), OBV ↓ (red), Vol 0.06x
- S&R: S=5, R=2 | MTF: 46% (6/13)
- Reason text: "ADX 26.6 strong trend; pullback preferred"

**3. PATTERN DETECTION**
- Trend Template: 8/8 (Stage 2 confirmed)
- VCP: 45% forming (6 contractions)
- Cup & Handle: 25% not_detected
- Flat Base: 40% not_detected

**4. BOTTOM LINE CARD**
- Action: "READY - MOMENTUM ENTRY" for Position Trade (1-3 months)
- Weight: T:30% F:70%
- What's Good: 6 points (Stage 2, RS 1.19, RSI 60.2, ADX 26.6, Decent fund, Favorable macro)
- What's Risky: 0 points (none shown)
- Action Plan: "Momentum entry viable at current price ($17.64)"

**5. ASSESSMENT**
- Technical: Strong (8/8 TT, RS 1.19)
- Fundamental: Decent (ROE -59.9% Weak, Revenue Growth 0.8% Decent, D/E 0.88 Strong) — Data: finnhub
- Sentiment: Neutral (F&G: 40.7)
- Risk/Macro: Favorable
- Why: "Strong technicals with favorable macro conditions"
- Criteria shown: "Need 2+ Strong categories" (misleading — actual path was Strong Tech + Decent Fund + Favorable Risk)

**6. TECHNICAL INDICATORS**
- RSI 60.2 | 8 EMA $15.27 | 21 EMA $15.69 | 50 SMA $17.58 | 200 SMA $14.86 | ATR $0.98

**Issues Found:**
- **INCONSISTENCY (HIGH):** BUY verdict + "READY - MOMENTUM ENTRY" + "Momentum entry viable at $17.64" BUT Trade Setup = NOT VIABLE with both R:R < 1 grayed out. User gets contradictory signals. Root cause: categorical assessment (directional opinion) and trade viability (R:R math) are independent systems.
- **BUG (MEDIUM):** BottomLineCard shows "MOMENTUM ENTRY" for ADX 26.6, but Trade Setup correctly says "pullback preferred". BottomLineCard uses `adx >= 25` threshold, but the intent for ADX 25-30 is pullback preferred (momentum only at ADX >= 30).
- **KNOWN GAP:** For position trade (1-3 months), target R1=$18.60 (5.4% above) is too conservative. R2=$22.69 (28.6%) would be natural target, dramatically improving R:R. Documented gap - targets don't adjust by period.

---

### Ticker #1: AAPL | Period: Standard (15-30 days)
**Date:** Day 53 | **Verdict:** AVOID | **Categories:** T:W F:D S:N R:N

**1. VERDICT CARD**
- Verdict: AVOID | Price: $227.63
- Sector: Technology • Consumer Electronics
- Avg Daily $ Vol: ~$12.4B (green)

**2. TRADE SETUP**
- Viability: NOT VIABLE (both R:R < 1)
- Pullback: R:R=1.57 (green) | Momentum: R:R=0.96 (grayed ⛔)
- ADX 23.24, 4H RSI, OBV, RVOL badges visible

**3. PATTERN DETECTION**
- Trend Template: 7/8 (In Stage 2 Uptrend - green ✅)
- VCP: 70% forming
- Cup & Handle / Flat Base: not detected
- Stage 2 confirmed at 7/8

**4. BOTTOM LINE CARD**
- Action: SKIP for Standard Trade (15-30 days)
- Weight: T:50% F:50%
- What's Good: mentions Decent fundamentals, some positives
- What's Risky: **"Trend Template: 7/8 - not in Stage 2 uptrend"** ← BUG (7/8 IS Stage 2!)

**5. ASSESSMENT**
- Technical: Weak (RS < 1.0, RSI weak despite 7/8 TT)
- Fundamental: Decent
- Sentiment: Neutral
- Risk/Macro: Neutral
- Why: "Weak technical setup" → immediate AVOID

**Issues Found:**
- **BUG #5 (FIXED):** BottomLineCard `getWhatsRisky()` always says "not in Stage 2 uptrend" when Technical is Weak, regardless of actual TT score. AAPL has TT 7/8 (IS Stage 2 per Pattern Detection), but BottomLineCard contradicts this. Root cause: line 122-125 hardcoded "not in Stage 2" for all Weak tech stocks. Fixed to parse TT score and only say "not in Stage 2" when TT < 7.
- **OBSERVATION:** AAPL assessed as Weak Technical despite 7/8 TT because RS < 1.0 and RSI weak. This is CORRECT behavior — Stage 2 uptrend + poor relative strength means the stock is trending up but underperforming the market.
- **OBSERVATION:** Same verdict (AVOID) across Quick and Standard periods. Expected since T:Weak → immediate AVOID regardless of period weights.
- **QUESTIONABLE (from Quick):** T:Decent/F:Decent/S:Neutral/R:Neutral → AVOID on Quick period. All-mediocre should possibly be HOLD.

---

### Proactive Code Audit Findings (Day 53)
**Date:** Day 53 | **Method:** 5-agent parallel code analysis based on bug patterns

**Bugs Found & Fixed:**
- **BUG #6 (FIXED):** App.jsx:473 `generateActionableRecommendation()` uses `srData?.support?.[0]` (farthest/lowest support) instead of `Math.max(...support)` (nearest). Same pattern as Bug #3. Affects alert prices, pullback recommendation text, pct-from-support calculations. Fixed to `srData?.support?.length > 0 ? Math.max(...srData.support) : null`.
- **FIX:** F&G color thresholds in App.jsx (lines 1984-1995) mismatched categoricalAssessment.js. UI showed green at 55 but logic says Strong starts at 60. Aligned to 60-80 = green, 35-60 = gray, <35 or >80 = red.
- **FIX:** BottomLineCard action plan "Wait for Stage 2" was generic — now checks TT score and says "wait for RS to improve" when TT >= 7 (already in Stage 2).

**Confirmed Clean:**
- Pattern 1 (field names): No remaining mismatches in active code
- R:R threshold: Consistent >= 1.0 everywhere
- TT threshold: Consistent >= 7 for Stage 2 everywhere
- Liquidity threshold: Consistent $10M everywhere
- Position Size banner: Correctly hidden for AVOID and ADX < 20

**Known Threshold Differences (Intentional, Documented):**
- ADX >= 25 in categoricalAssessment (entry preference) vs >= 30 in BottomLineCard header (MOMENTUM ENTRY label). The 30 threshold is intentional — stricter for momentum label.
- RSI 40-65 in BottomLineCard "optimal entry" vs 50-70 in categoricalAssessment "Strong". The 40-65 is intentional — "optimal entry" is narrower than "acceptable range".
- RS >= 1.1 in BottomLineCard "What's Good" vs >= 1.0 in categoricalAssessment. The 1.1 is intentional — "outperforming" bar is higher than "market performer".

### Deep Pattern Analysis Findings (Day 53 - Session 2)
**Date:** Day 53 | **Method:** 3-agent parallel deep scan (type mismatches, hidden data, competing systems)

**Bugs Found & Fixed:**
- **BUG #7 (FIXED):** App.jsx:1089 RS Rating color compared `rsRating === 'Strong'` but rsRating is a NUMBER (0-100 from rsCalculator.js:100). Number never equals string → RS Rating was ALWAYS RED for every stock. Fixed to `rsRating >= 70` green, `>= 50` yellow, `< 50` red.
- **BUG #8 (FIXED):** Backend `support_resistance.py` returns `viable: "YES"` + `advice: "Good setup"` (based on support distance ≤ 10%), but frontend R:R badge shows "NOT VIABLE" (R:R < 1.0). User saw green "✅ Good setup" banner next to red "🚫 NOT VIABLE" badge. Fixed: when backend says YES but R:R fails, banner now shows yellow "⚠️ Structural stop is sound, but R:R insufficient at current price".
- **FREE WIN:** RS interpretation text (e.g., "Slight underperformance (momentum fading)") was computed in rsCalculator.js:187 but NEVER displayed. Added to RS card.

**Computed-But-Hidden Fields Discovered (10 "free wins"):**
- `rsData.interpretation` — NOW DISPLAYED (fixed above)
- `verdict.adxAnalysis` — full entry strategy recommendation, still hidden
- `verdict.signalWeights` — explains holding period impact, still hidden
- `verdict.entryPreference` — "Pullback preferred (ADX 23)", still hidden
- `rsData.rsTrend` — "improving"/"declining"/"stable", still hidden
- `technical.data.priceAbove200SMA` — Stage 2 confirmation badge, still hidden
- `fundamental.data` (ROE, RevGrowth, D/E) — actual metric values, only reasons shown
- `sentiment.data.subLabel` — "Optimistic" vs "Cautious", still hidden

**Competing Truth Sources Discovered (6 total):**
1. Viability: Backend support distance vs Frontend R:R — **FIXED (Bug #8)**
2. Entry Type: categoricalAssessment ADX≥25 vs BottomLineCard ADX≥30 — intentional (documented)
3. Stage 2: Minervini 8-point vs priceAbove200SMA — different definitions, needs documentation
4. Fundamentals: Backend doesn't assess, Frontend uses as veto — intentional
5. RS thresholds: Quality gate ≥0.8 vs Strong ≥1.0 — intentional (different quality levels)
6. Position Sizing: Backend advises "FULL" when Frontend says AVOID — **suppressed via Day 50 fix**

**New Patterns Added to Checklist:** G (Type Mismatches), H (Competing Truth Sources), I (Computed-But-Hidden), J (Missing Interpretation Layer)

---

*This test plan is the definitive guide for our 30-ticker manual validation effort.*
*Created Day 53 - Top Priority*
