# Design Spec: Price Structure Card

> **Status:** Draft v2 — Post-audit revision
> **Author:** Claude (Day 72 design session)
> **Date:** March 30, 2026
> **Depends on:** Feature freeze lift after paper trading validation
> **Audit:** Self-audited via STA Master Audit Framework (10 findings, all addressed)
> **Audit report:** `PRICE_STRUCTURE_CARD_AUDIT.md` (same directory)

---

## 0. First Principles — Why This Card Must Exist

A swing trader's daily process is not "check 15 indicators." It's:

1. **Where is price?** — Relative to levels that matter
2. **How did it get here?** — Trending, ranging, or transitioning
3. **What happens next?** — Approaching a decision zone? Breaking out? Failing?
4. **Do I act?** — Only if structure + volume confirm

STA currently answers #1 and #4 through numbers (Trade Setup, Verdict). But #2 and #3 — the *narrative context* — require the trader to open TradingView and visually reconstruct what the numbers mean. That's the gap.

**The question I had to answer first:** Does STA need an embedded chart, or does it need to tell the trader what they'd see on a chart?

**Answer:** Narrative first. A trader who built STA to avoid opening TradingView needs structured context that saves the 5 minutes of S/R markup + trendline drawing they do for every ticker. If narrative proves insufficient, charting can be layered on later using lightweight-charts (ref: zero-sum-public repo pattern).

---

## 1. Card Identity

| Field | Value |
|-------|-------|
| **Card Name** | Price Structure |
| **Internal Key** | `priceStructure` (for `expandedSections` state) |
| **Tier Placement** | Tier 2 — collapsed by default, between Trade Setup (Tier 1) and Pattern Detection (Tier 2) |
| **Badge (collapsed)** | Structure state label: `Uptrend` / `Range` / `Breakdown` / etc. |
| **Color** | Teal-400 header (distinct from purple Pattern, blue Assessment) |

**Why "Price Structure" and not "Chart Narrative" or "TradingView"?**
- "Chart Narrative" is meta — describes the format, not the content
- "TradingView" is a brand name and misleading (we're not embedding TV)
- "Price Structure" is what traders call this analysis — where price is relative to key levels and market structure

---

## 2. What This Card Is NOT

Defining boundaries prevents scope creep:

| This card IS | This card IS NOT |
|-------------|-----------------|
| Structured narrative from computed data | AI-generated market commentary |
| Deterministic — same data = same output | Probabilistic or opinion-based |
| Built on existing S/R + pattern data | A new indicator or scoring system |
| Scannable in 10 seconds (badge + levels glanceable; full read ~20s) | A wall of text |
| Frontend-generated utility (follows `categoricalAssessment.js` pattern) | Backend string concatenation in API |

**Critical design constraint:** Every sentence must be traceable to a specific computed value. "R1 has been tested 7 times" → `level_scores["689.28"] = 7`. No editorializing. No "this looks bullish." Facts + structure + conditional implications only.

**Language rules:**
- "Approaching resistance" = factual observation (allowed)
- "Breakout imminent" = directional prediction (forbidden)
- "Directional resolution expected" = structural observation without predicting direction (allowed)
- "Oversold" = RSI < 30 only (Wilder's definition, not RSI < 40)

---

## 3. Data Inventory — What We Have vs. What We Need

### Already Computed and Available in Frontend

These data points are already returned by the backend API and available in the `fetchFullAnalysisData()` result object.

| Data Point | Source | Available In | Field Path |
|------------|--------|-------------|------------|
| S/R levels | `support_resistance.py` | `sr` | `sr.support[]`, `sr.resistance[]` |
| MTF confluence | `_find_mtf_confluence()` | `sr` | `sr.meta.mtf.confluence_map` |
| Proximity to nearest levels | `assess_trade_viability()` | `sr` | `sr.meta.tradeViability.support_distance_pct` |
| ATR (noise measurement) | `_calculate_atr()` | `sr` | `sr.meta.atr` |
| Trade viability | `assess_trade_viability()` | `sr` | `sr.meta.tradeViability.viable` |
| RVOL | S/R endpoint | `sr` | `sr.meta.rvol` |
| RSI | S/R endpoint | `sr` | `sr.meta.rsi_daily` |
| ADX + trend strength | S/R endpoint | `sr` | `sr.meta.adx` |
| Trend Template score | `pattern_detection.py` | `patterns` | `patterns.trendTemplate.criteria_met` |
| Pattern status | `pattern_detection.py` | `patterns` | `patterns.patterns.{vcp,cupHandle,flatBase}` |
| Actionable patterns | `pattern_detection.py` | `patterns` | `patterns.actionablePatterns[]` |
| Fibonacci extensions | `_smart_project_resistance()` | `sr` | `sr.meta.resistanceProjected` |
| 200 SMA position | Categorical assessment | `stock` | Computed in `categoricalAssessment.js` |

### NOT Available — Requires Backend Change

| Data Point | Source | Issue | Fix |
|------------|--------|-------|-----|
| **Touch counts per level** | `_score_levels()` | Computed in `support_resistance.py:801` but NOT passed through to API response in `backend.py:1603-1629` | Add 1 line: `'level_scores': sr_levels.meta.get('level_scores', {})` to meta dict |

**This is the ONLY backend change required for Phase 1.**

### Deferred to Phase 2 (New Computation)

| Data Point | Why Needed | Complexity | Phase |
|------------|-----------|------------|-------|
| **Market structure state** (HH/HL vs LH/LL) | Trend Template is binary (Stage 2: yes/no), doesn't tell trend age or freshness | Medium | Phase 2 |
| **Volume at levels** (directional) | Was volume rising or falling as price approached the level? | Medium | Phase 2 |
| **Trend age** | How long has the current structure persisted? | Low | Phase 2 |

### The Hard Question: Do We Need HH/HL/LH/LL Detection?

**Argument for:** It's the foundation of how traders classify trends. A fresh series of HH+HL is very different from 8 months of HH+HL that's starting to flatten.

**Argument against:** Trend Template (8-point Minervini criteria) is a battle-tested proxy. Adding HH/HL detection creates edge cases (what window? what's a "significant" pivot?). Marginal value over Trend Template may be low.

**Decision:** Defer to Phase 2. Phase 1 uses Trend Template score + ATR-relative proximity to infer structure state. Delivers ~80% of narrative value without new backend computation.

---

## 4. Structure State Derivation

**Critical: Evaluation order matters.** Edge cases first, then specifics.

### Proximity Definition — ATR-Relative (Not Arbitrary Percentage)

**Why ATR-relative?** A stock with 8% daily ATR that's 5% from resistance is practically ON the level. A stock with 1% ATR that's 5% away has significant room. Percentage-based proximity ignores volatility.

```javascript
function isNearLevel(currentPrice, level, atr) {
  const distance = Math.abs(currentPrice - level);
  return distance <= (2.0 * atr);  // Within 2x noise range = "near"
}
```

Uses existing `sr.meta.atr` — no new computation.

### Decision Tree (Strict Evaluation Order)

```
 1. IF no S/R levels found
    → "Insufficient data for structure analysis"
    → Card not rendered

 2. IF price above ALL resistance levels AND resistanceProjected === true
    → "ATH breakout — no overhead resistance"
    → (Fibonacci extensions shown if available)

 3. IF price below ALL support levels AND supportProjected === true
    → "Below all historical support"
    → (ATR-projected support shown)

 4. IF isNear(R1) AND isNear(S1)
    → "Compression — range narrowing between S1 and R1"
    → (Note: NOT "breakout imminent" — compression is direction-neutral)

 5. IF trendTemplate.criteria_met >= 7 AND isNear(R1)
    → "Uptrend testing resistance"

 6. IF trendTemplate.criteria_met >= 7 AND isNear(S1)
    → "Uptrend pulling back to support"

 7. IF trendTemplate.criteria_met >= 7
    → "Uptrend — between levels"

 8. IF trendTemplate.criteria_met 4-6 AND isNear(S1)
    → "Weakening trend — testing support"

 9. IF trendTemplate.criteria_met 4-6 AND isNear(R1)
    → "Transitioning — testing resistance"

10. IF trendTemplate.criteria_met 4-6
    → "Mixed trend — between levels"

11. IF trendTemplate.criteria_met < 4 AND adx.adx < 15
    → "Choppy — no clear trend"

12. IF trendTemplate.criteria_met < 4
    → "Downtrend"
```

---

## 5. Narrative Architecture

The card has **3 sections**, each answering one trader question. Every line maps to a data field.

### Section A: Structure State (1-2 lines)

**Question answered:** "What's the big picture?"

**Template:**
```
{TICKER} @ ${currentPrice} — {structureState}
Trend: {trendTemplateScore}/8 Minervini criteria | ADX {adxValue} ({trendStrength})
```

**Examples:**
```
SPY @ $669.89 — Uptrend testing resistance
Trend: 7/8 Minervini criteria | ADX 28 (Strong)

AAPL @ $178.50 — Pulling back to support in uptrend
Trend: 6/8 Minervini criteria | ADX 22 (Moderate)

SMCI @ $42.10 — Downtrend (2/8 criteria)
Trend: 2/8 Minervini criteria | ADX 14 (Weak)
```

**Data mapping:**
- `currentPrice` → `sr.currentPrice`
- `structureState` → derived (Section 4 decision tree)
- `trendTemplateScore` → `patterns.trendTemplate.criteria_met`
- `adxValue`, `trendStrength` → `sr.meta.adx`

### Section B: Key Levels (3-5 lines)

**Question answered:** "Where are the decision zones and how strong are they?"

**Template:**
```
▲ R1: ${level} — tested {touches}x {confluenceTag}  ({distance}% above)
  {R2 if exists, same format}
━ Current: ${currentPrice}
▼ S1: ${level} — tested {touches}x {confluenceTag}  ({distance}% below)
  {S2 if exists, same format}
```

**Confluence tag:** `[D+W]` if daily+weekly confluent (from `mtf.confluence_map`), blank if daily only.

**Example:**
```
▲ R1: $689.28 — tested 7x [D+W]  (2.9% above)
▲ R2: $720.00 — tested 3x         (7.5% above)
━ Current: $669.89
▼ S1: $637.06 — tested 4x [D+W]  (4.9% below)
▼ S2: $600.77 — tested 7x         (10.3% below)
```

**Rules:**
- **R1/S1 = nearest actionable level** (what the trader hits first). R2/S2 = next nearest.
- Show max 2 resistance + 2 support levels
- Only show levels within proximity window (20% support, 30% resistance — existing constants `SUPPORT_PROXIMITY_PCT`, `RESISTANCE_PROXIMITY_PCT`)
- Touch count from `sr.meta.level_scores` (requires Finding 1 backend fix)
- Confluence from `sr.meta.mtf.confluence_map`
- Distance % computed: `((level - currentPrice) / currentPrice) * 100`

**Why nearest first (not strongest)?** Nearest = what the trader encounters first when price moves. Touch counts and confluence tags communicate strength alongside position. The trader can see both proximity AND conviction at a glance.

**Why max 2+2?** A trader marking up a chart draws 2-3 key levels, not 8. More levels = more noise = worse decisions.

### Section C: What to Watch (2-3 lines)

**Question answered:** "What triggers action?"

This is the highest-value section — synthesizes multiple data points into conditional scenarios.

**Generation logic:**

```javascript
// Constants — sourced from same values used elsewhere in the system
const BREAKOUT_VOLUME_THRESHOLD = 1.5; // Same as pattern_detection.py check_breakout_quality()

function generateWatchItems(sr, patterns, atr) {
  const items = [];
  const { currentPrice, resistance, support, meta } = sr;
  const R1 = resistance[0], S1 = support[0];
  const { rvol, rsi_daily, tradeViability } = meta;

  // Priority 1: Compression (both levels near)
  if (isNear(currentPrice, R1, atr) && isNear(currentPrice, S1, atr)) {
    const rangePct = ((R1 - S1) / currentPrice * 100).toFixed(1);
    items.push(`Tight range between S1-R1 (${rangePct}%) — directional resolution expected`);
  }

  // Priority 2: Near resistance — breakout or rejection?
  if (isNear(currentPrice, R1, atr)) {
    if (rvol >= BREAKOUT_VOLUME_THRESHOLD) {
      items.push(`Breakout watch: near R1 ($${R1}) with volume confirming (${rvol}x avg)`);
    } else {
      items.push(`Approaching R1 ($${R1}, ${touches}x tested) — needs volume > ${BREAKOUT_VOLUME_THRESHOLD}x for conviction`);
    }
  }

  // Priority 3: Near support — bounce or break?
  if (isNear(currentPrice, S1, atr)) {
    if (rsi_daily < 30) {
      items.push(`Testing S1 ($${S1}, ${touches}x held) with RSI oversold (${rsi_daily}) — watch for bounce`);
    } else if (rsi_daily < 40) {
      items.push(`Testing S1 ($${S1}, ${touches}x held) with RSI approaching oversold (${rsi_daily})`);
    } else {
      items.push(`Drifting toward S1 ($${S1}) — break below invalidates setup`);
    }
  }

  // Priority 4: Extended from support (caution)
  if (tradeViability?.viable === "NO" && tradeViability?.support_distance_pct > 15) {
    items.push(`Extended ${tradeViability.support_distance_pct}% from support — pullback entry preferred over chase`);
  }

  // Priority 5: Pattern convergence
  const actionable = patterns?.actionablePatterns?.filter(p => p.confidence >= 60);
  if (actionable?.length > 0) {
    const best = actionable[0];
    items.push(`${best.name} forming (${best.confidence}%) — pivot at $${best.triggerPrice}`);
  }

  // Fallback: Mid-range, nothing imminent
  if (items.length === 0) {
    const rDist = ((R1 - currentPrice) / currentPrice * 100).toFixed(1);
    const sDist = ((currentPrice - S1) / currentPrice * 100).toFixed(1);
    items.push(`Between levels — no immediate trigger. R1 ${rDist}% above, S1 ${sDist}% below`);
  }

  return items.slice(0, 3); // Max 3 items
}
```

**RSI thresholds (Wilder's standard definitions):**
- RSI < 30: "oversold"
- RSI 30-40: "approaching oversold"
- RSI > 70: "overbought"
- RSI 60-70: "approaching overbought"

**Example outputs:**

*Near resistance with volume:*
```
⚡ Breakout watch: near R1 ($689.28, tested 7x) with volume 1.8x avg
   Break above $689.28 with close in upper half = confirmed breakout
   Failure here → likely retest S1 ($637.06, 4.9% below)
```

*Pulling back to support:*
```
⚡ Testing S1 ($175.50, tested 5x, D+W confluent) — RSI 28 oversold
   If S1 holds: R:R setup to R1 ($192.00) = 1.8:1
   Break below $175.50 → next support S2 ($168.00, 8.2% below)
```

*Extended, nothing to do:*
```
⚡ Extended 18% from nearest support — not actionable at current price
   Wait for pullback toward S1 ($145.00) before considering entry
   RVOL 0.7x — low conviction in current move
```

---

## 6. Architecture Decision: Frontend-Generated Narrative

> **Audit revision:** Original spec chose backend. Audit Finding 2 + Finding 10 identified that pattern data is not available in the S/R endpoint, and that `categoricalAssessment.js` already proves frontend narrative generation works well.

**Where does the narrative get assembled?**

| Factor | Backend | Frontend |
|--------|---------|----------|
| Data availability | Pattern data not in S/R endpoint — would need coupling | All data already in `fetchFullAnalysisData()` result |
| Testability | Python unit tests (strong) | Jest unit tests (adequate — `categoricalAssessment.js` precedent) |
| Iteration speed | Requires backend restart + API change | Hot reload, instant |
| Coupling | Creates dependency between S/R and pattern engines | No new coupling |
| Precedent | `assess_trade_viability()` | `categoricalAssessment.js`, `simplifiedScoring.js` |

**Decision: Frontend.**

**Implementation:**
```
frontend/src/utils/
├── priceStructureNarrative.js  <- NEW: narrative generation (~150 lines)
├── categoricalAssessment.js    <- existing precedent
├── simplifiedScoring.js        <- existing precedent
├── riskRewardCalc.js           <- existing precedent
```

**Single public function:**
```javascript
/**
 * Generate structured price narrative from computed analysis data.
 *
 * @param {Object} sr - S/R data from fetchSupportResistance()
 * @param {Object} patterns - Pattern data from fetchPatterns()
 * @returns {Object} { structureState, stateColor, trendContext, keyLevels[], watchItems[], meta }
 */
export function generatePriceStructure(sr, patterns) { ... }
```

**Why a structured object and not raw text?** The frontend needs structured data for proper formatting, colors, and icons. The `structureState` drives the badge color. The `keyLevels` array drives the level rendering with conditional styling. The `watchItems` strings contain the narrative sentences.

### Backend Change (Minimal)

One line added to `backend.py:~1620` in the S/R endpoint response meta:

```python
'level_scores': sr_levels.meta.get('level_scores', {}),
```

This exposes the touch counts that `_score_levels()` already computes. No other backend changes.

---

## 7. Frontend Card Design

### Collapsed State (Default)
```
┌──────────────────────────────────────────────────────────────┐
│ ▶ Price Structure            [Uptrend testing resistance]    │
└──────────────────────────────────────────────────────────────┘
```
- Teal-400 title
- Badge shows `structureState` with color coding:
  - Green: Uptrend states (rules 5, 6, 7)
  - Yellow: Transitioning / range / compression states (rules 4, 8, 9, 10)
  - Red: Downtrend / breakdown / choppy states (rules 2, 3, 11, 12)

### Expanded State
```
┌──────────────────────────────────────────────────────────────┐
│ ▼ Price Structure            [Uptrend testing resistance]    │
│                                                              │
│  SPY @ $669.89 — Uptrend testing resistance                  │
│  Trend: 7/8 Minervini criteria | ADX 28 (Strong)            │
│                                                              │
│  ▲ R1: $689.28 — tested 7x [D+W]         2.9% above        │
│  ▲ R2: $720.00 — tested 3x               7.5% above        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│  ▼ S1: $637.06 — tested 4x [D+W]         4.9% below        │
│  ▼ S2: $600.77 — tested 7x               10.3% below       │
│                                                              │
│  ⚡ Approaching R1 ($689.28, 7x tested) — needs volume      │
│     > 1.5x for breakout conviction (current: 1.2x)          │
│  ⚡ If rejected → S1 $637.06 (4.9% below, 4x held) is      │
│     the fallback level                                       │
│  ⚡ VCP forming (72%) — pivot $691.00 aligns with R1 zone   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Implementation Pattern
Same as existing collapsible cards:
```jsx
<div className="bg-gray-800 rounded-lg">
  <button onClick={() => toggleSection('priceStructure')} className="w-full ...">
    <span className="text-teal-400 font-semibold">Price Structure</span>
    <span className={`px-2 py-0.5 rounded text-xs ${stateColor}`}>{structureState}</span>
  </button>
  {expandedSections.priceStructure && (
    <div className="p-4 space-y-3">
      {/* Section A: Structure State */}
      {/* Section B: Key Levels */}
      {/* Section C: Watch Items */}
    </div>
  )}
</div>
```

---

## 8. Edge Cases

| Scenario | Rule # | Handling |
|----------|--------|----------|
| **No S/R levels found** (new IPO, < 150 bars) | 1 | Card not rendered. No partial state. |
| **Price above ALL resistance** (ATH breakout) | 2 | Use Fibonacci extensions from `_smart_project_resistance()`. State: "ATH breakout — no overhead resistance" |
| **Price below ALL support** (ATL breakdown) | 3 | Use ATR-projected support. State: "Below all historical support" |
| **Near both R1 and S1** (compression) | 4 | "Compression — range narrowing." **Not** "breakout imminent" (direction-neutral). |
| **No patterns detected** | — | Section C omits pattern convergence line — still has level-based watch items |
| **ADX < 15 (no trend)** | 11 | "Choppy — no clear trend." Watch: "Wait for ADX > 20 before directional commitment" |
| **All levels far away** (mid-range) | fallback | "Between levels — no immediate catalyst." |
| **`level_scores` empty** (method fallback to pivot/kmeans) | — | Touch counts show "N/A" instead of number. Levels still displayed. |
| **Trend Template data missing** (API failure) | — | Structure state: "Unable to determine trend." Card still shows levels. |
| **Earnings approaching** | — | Out of scope Phase 1 (we have earnings data via `fetchEarnings()` but cross-referencing is Phase 2). |

---

## 9. Testing Strategy

### Unit Tests (Jest — Frontend)

```javascript
// __tests__/priceStructureNarrative.test.js

describe('Structure State Derivation', () => {
  test('ATH breakout when price above all resistance', () => { ... });
  test('Compression when near both R1 and S1 (ATR-relative)', () => { ... });
  test('Uptrend testing resistance: TT >= 7 + near R1', () => { ... });
  test('Pullback to support: TT >= 7 + near S1', () => { ... });
  test('Downtrend: TT < 4', () => { ... });
  test('Choppy: TT < 4 + ADX < 15', () => { ... });
  test('Edge cases evaluated before trend rules', () => { ... });
});

describe('Watch Items', () => {
  test('Max 3 items regardless of conditions', () => { ... });
  test('RSI < 30 = oversold, RSI 30-40 = approaching oversold (Wilder)', () => { ... });
  test('Volume threshold matches BREAKOUT_VOLUME_THRESHOLD constant', () => { ... });
  test('Extended from support uses tradeViability.viable === NO', () => { ... });
  test('Pattern convergence only for confidence >= 60%', () => { ... });
  test('Fallback item when no conditions match', () => { ... });
});

describe('Key Levels', () => {
  test('Ordered by nearest first (not strongest)', () => { ... });
  test('Max 2R + 2S levels', () => { ... });
  test('Handles missing level_scores gracefully', () => { ... });
  test('Confluence tag from mtf.confluence_map', () => { ... });
});
```

### Behavioral Test (Integration)

Run against 5 real tickers representing different structural states:

| Ticker | Expected State | Why |
|--------|---------------|-----|
| **NVDA** | Uptrend (7-8/8 TT) | Momentum leader |
| **SPY** | Varies (range or trend) | Market barometer |
| **SMCI** | Weak/Downtrend (low TT) | Volatile, broken structure |
| **AAPL** | ATH zone or Uptrend | Mature trend, possibly ATH |
| **F** | Choppy (low ADX) | Sideways, no trend |

**Verification:** Does the narrative match what you'd say looking at the chart? If a 10-year trader would disagree with the structure state, the logic is wrong.

---

## 10. Implementation Phases

### Phase 1: Narrative from Existing Data (Target: 1 session)

**Backend (minimal):**
- Add `level_scores` to S/R API response meta — 1 line in `backend.py`

**Frontend:**
- Create `frontend/src/utils/priceStructureNarrative.js` (~150 lines)
  - `generatePriceStructure(sr, patterns)` → structured narrative object
  - ATR-relative proximity function
  - Structure state decision tree (12 rules)
  - Watch item generator (6 scenarios)
  - Key level formatter (nearest first, max 2+2)
- Create `frontend/src/components/PriceStructureCard.jsx` (~120 lines)
  - Collapsible card following existing pattern
  - Tier 2 placement
  - Renders structure state, key levels, watch items
- Wire into `App.jsx`:
  - Import and call `generatePriceStructure()` after analysis data loads
  - Add to `expandedSections` state
  - Place between Trade Setup and Pattern Detection

**No changes to:** `support_resistance.py`, `pattern_detection.py`, backtest, scoring, verdict engine

### Phase 2: Market Structure Engine (Target: 1-2 sessions, deferred)

**Backend:**
- Add `_detect_market_structure()` using existing `find_pivot_points()`
- HH/HL/LH/LL sequence analysis
- Classify: Uptrend / Downtrend / Range / Transition
- Track trend age (bars since last structure shift)
- Volume behavior at levels (rising/falling into S/R)

**Frontend:**
- Enhanced structure state with HH/HL context
- Optional: simple visual level indicator (no chart library)

### Phase 3: Visual Chart (Future — Separate Spec)

- lightweight-charts integration (ref: zero-sum-public repo)
- Overlay S/R levels, patterns, entry/stop/target on chart
- This is a major feature — requires its own design spec
- Only pursue if Phase 1+2 narrative proves insufficient

---

## 11. Self-Audit — Questions Answered

**Q: Is this just restating Trade Setup data in paragraph form?**
A: No. Trade Setup = trade plan (entry/stop/target/R:R). Price Structure = chart read (where price sits in structural context). Trade Setup tells you *what to do*. Price Structure tells you *why* and *when*.

**Q: Could this mislead by oversimplifying?**
A: Only if we editorialize. "Uptrend testing resistance" is factual. "About to break out" is editorializing. The spec forbids directional predictions — only structural observations and conditional triggers.

**Q: Why not just embed a chart?**
A: Charting is a 3-5 session effort with a new library dependency. Narrative card is 1 session. Ship 80% first. YAGNI until proven otherwise.

**Q: Does this change the Verdict engine?**
A: No. Zero impact on BUY/HOLD/AVOID scoring. This is display-only context.

**Q: What if structure state disagrees with Verdict?**
A: Good — that's valuable. "Verdict: BUY but Price Structure: Extended 18% from support" tells the trader to wait. The card adds timing nuance, not contradiction.

**Q: Why frontend and not backend?** (Audit revision)
A: Pattern data and S/R data come from separate API calls. `fetchFullAnalysisData()` already gathers both. Building narrative in frontend avoids coupling the two backend engines. `categoricalAssessment.js` proves this pattern works.

---

## 12. Open Questions for Discussion

1. **Should Phase 1 ship before or after paper trading?** Feature freeze says after. But this is display-only with zero Verdict impact. Could be argued as "paper trading support" — helping read the setup before placing paper trades.

2. **Volume at levels (directional):** Phase 1 uses RVOL (general). Phase 2 could analyze volume *specifically as price approaches a level* — accumulation or distribution? Worth the complexity?

3. **Integration with Context Tab:** Should the card reference FOMC dates or macro context? E.g., "Testing resistance into FOMC (3 days away)." We have this data (`fetchEarnings()` + `cycles_engine.py`). Or keep it purely price-structural?

4. **Earnings data in watch items?** We already fetch earnings calendar. "Earnings in 5 days — gap risk" is high-value. But crosses the boundary from price structure to event risk. Phase 1 or Phase 2?

---

*End of spec v2. Audit report: `PRICE_STRUCTURE_CARD_AUDIT.md` (same directory).*
*Next step: User review → finalize → schedule implementation post-feature-freeze.*
