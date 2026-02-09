# UI Cohesiveness Test Plan

**Created:** Day 49 (February 9, 2026)
**Purpose:** Systematically verify UI elements are logically coherent

---

## Test Tickers (10 Diverse Stocks)

Run analysis on each ticker, save as PDF, review for coherence issues.

| # | Ticker | Category | Why Selected |
|---|--------|----------|--------------|
| 1 | **NVDA** | Large Cap Tech | Strong momentum, likely high ADX |
| 2 | **JNJ** | Defensive Healthcare | Low volatility, different profile |
| 3 | **COIN** | Volatile Crypto-related | High RVOL, test distribution warning |
| 4 | **F** | Cyclical Auto | Low ADX, test "wait" messaging |
| 5 | **PLTR** | Growth Tech | Variable patterns |
| 6 | **XOM** | Energy Sector | Different sector behavior |
| 7 | **SPY** | ETF/Index | Market benchmark |
| 8 | **SMCI** | High Volatility | Extreme moves, test edge cases |
| 9 | **T** | Telecom/Dividend | Low growth, weak fundamentals |
| 10 | **AFRM** | Speculative Fintech | High RVOL + potential distribution |

---

## Checklist for Each Ticker

### Section 1: Trade Setup Card
- [ ] **VIABLE/NOT VIABLE matches entry strategy status**
  - If VIABLE, at least one entry strategy should be highlighted (not grayed out)
  - If both strategies grayed out, should NOT say VIABLE
- [ ] **Entry price uses nearest support**
  - Pullback Entry should match S1 (nearest support level)
  - Entry should NOT use S5 or distant support
- [ ] **R:R values are >= 1.0 for highlighted strategies**
  - Grayed out = R:R < 1.0
  - Highlighted = R:R >= 1.0
- [ ] **Position recommendation matches risk**
  - "full" should NOT appear with "wait for better entry" reason
  - If ADX < 20 and reason says "wait", position should say "reduced" or "wait"

### Section 2: Entry Strategy Cards
- [ ] **Pullback card styling matches R:R**
  - R:R >= 1.0: normal or highlighted
  - R:R < 1.0: grayed out + "⛔ R:R < 1" badge
- [ ] **Momentum card styling matches R:R**
  - Same as above
- [ ] **PREFERRED/VIABLE/CAUTION badges are logical**
  - ADX >= 25: Pullback should be "★ PREFERRED"
  - ADX 20-25 + RSI confirmed: Momentum can be "★ VIABLE"
  - ADX < 20: Momentum should show "⚠️ CAUTION"
- [ ] **When both R:R < 1.0, show "Wait for Better Setup"**
  - Neither card should be highlighted
  - Yellow warning box should appear

### Section 3: Pattern Detection
- [ ] **Trend Template message matches count**
  - 8/8: "In Stage 2 Uptrend (ideal for swing trades)"
  - 7/8: "Near Stage 2 Uptrend (7/8 criteria)" or similar
  - 6/8 or less: Should NOT say "In Stage 2 Uptrend"
- [ ] **Pattern confidence vs status**
  - If confidence >= 80%: "detected" status
  - If confidence < 80%: "forming" or "not_detected"

### Section 4: Indicator Badges
- [ ] **ADX badge color matches value**
  - ADX >= 25: Green (strong trend)
  - ADX 20-25: Yellow (weak trend)
  - ADX < 20: Gray (no trend)
- [ ] **OBV matches trend**
  - OBV ↑ with rising badge
  - OBV ↓ with falling badge
  - OBV → with flat badge
- [ ] **RVOL display matches value**
  - >= 2.0x: Green (high interest)
  - >= 1.5x: Light green
  - < 1.0x: Gray (low interest)
- [ ] **Distribution warning appears when appropriate**
  - RVOL >= 1.5x AND OBV falling: "⚠️ DIST" badge should appear

### Section 5: Verdict & Assessment
- [ ] **Verdict matches category assessments**
  - BUY requires 2+ Strong categories + Favorable/Neutral risk
  - HOLD appears when conditions partially met
  - AVOID appears when Weak categories dominate
- [ ] **"Why This Verdict?" explanation is accurate**
  - Should mention ADX if ADX < 20
  - Should reflect actual category counts

### Section 6: Recommendation Card
- [ ] **Action (BUY/HOLD/AVOID) matches verdict**
- [ ] **Alert price is logical**
  - For extended stocks: should be at support level
  - For stocks at support: should be current price or breakout level
- [ ] **Distance to alert price shown correctly**

---

## Known Issues to Verify Fixed

| Issue | Fixed? | How to Verify |
|-------|--------|---------------|
| Entry uses wrong support level | ❓ | Pullback Entry should = S1 (nearest support) |
| "Position: full" with "wait" reason | ❓ | Position should match reason |
| VIABLE shown when both strategies bad | ❓ | VIABLE only if R:R >= 1.0 for at least one strategy |
| 7/8 TT says "In Stage 2" without qualifier | ❓ | Should say "7/8" or "Near Stage 2" |

---

## Test Execution

1. Start frontend: `cd frontend && npm start`
2. For each ticker:
   - Enter ticker in search box
   - Wait for full analysis to load
   - Print to PDF (Cmd+P → Save as PDF)
   - Name file: `UI_Test_{TICKER}_{DATE}.pdf`
3. Review all PDFs against checklist
4. Document issues found

---

## After Testing

Report format for each issue:
```
Ticker: XXXX
Section: [Trade Setup / Entry Strategy / Pattern / etc.]
Issue: [Description of what's wrong]
Expected: [What should appear]
Actual: [What actually appeared]
Severity: [Critical / High / Medium / Low]
```
