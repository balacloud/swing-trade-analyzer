# Audit Report: Price Structure Card Design Spec

> **Audit Date:** March 30, 2026 (Day 72)
> **Target:** `docs/claude/design/PRICE_STRUCTURE_CARD_SPEC.md`
> **Framework:** STA Master Audit (Layer 1: Consistency + Layer 2: Correctness)
> **Auditor:** Claude (self-audit — questioning my own design)

---

## Layer 1: Consistency Audit (Does the spec match what the code actually does?)

### FINDING 1: `level_scores` NOT in API response — CRITICAL

**Claim (Spec Section 3):**
> Touch counts per level | `_score_levels()` | `meta.level_scores`

**Reality (Code):**
- `_score_levels()` computes touch counts at `support_resistance.py:664-704`
- `level_scores` is stored in the agglomerative meta at line 801: `"level_scores": {str(round(l, 2)): s for l, s in scored_levels[:10]}`
- **BUT** the API response at `backend.py:1603-1629` does NOT pass `level_scores` through to the frontend. It passes `mtf`, `adx`, `rsi_daily`, `rvol`, `tradeViability`, `atr` — but NOT `level_scores`.

**Verdict: [MISLEADING — CORRECTION]**
The spec claims touch counts are "already computed, no backend changes needed." The computation exists, but **the data doesn't reach the frontend**. This requires a backend change to `backend.py` to add `level_scores` to the meta response. Small change, but the spec said "no backend changes" for Phase 1, which is wrong.

**Fix required:** Add `'level_scores': sr_levels.meta.get('level_scores', {})` to the response meta dict at `backend.py:~1620`.

---

### FINDING 2: Pattern data NOT available in S/R endpoint — ARCHITECTURE FLAW

**Claim (Spec Section 5):**
> No new endpoint. Extend the existing `/api/support_resistance/<ticker>` response.
> `generate_price_structure()` takes `pattern_data: dict` as input.

**Reality (Code):**
- `/api/sr/<ticker>` (backend.py:1432) fetches OHLCV and computes S/R. It does NOT call pattern detection.
- `/api/patterns/<ticker>` is a completely separate endpoint.
- The frontend calls both in parallel via `fetchFullAnalysisData()` (api.js:376).

**Verdict: [MISLEADING — CORRECTION]**
The spec says "extend existing S/R endpoint" and "no new fetch needed." But to include pattern data in the narrative, we'd have to EITHER:

(a) **Call pattern detection inside the S/R endpoint** — Bad. Couples two independent computations. Violates single-responsibility. Doubles pattern computation time if both endpoints are still called.

(b) **Create a new `/api/price-structure/<ticker>` endpoint** — The spec explicitly rejected this citing "dual endpoints = divergence." But this isn't the same situation as Day 53. The S/R data and pattern data are already computed separately. This would be a new *composition* endpoint, not a duplicate.

(c) **Generate the narrative in the frontend** — The spec rejected this for testability reasons. BUT: `categoricalAssessment.js` already generates narrative strings (reasons, advice) in the frontend and it works fine. The "untestable" argument is partially invalidated by existing precedent.

(d) **Generate the narrative in the backend's `/api/analysis/<ticker>` or create a composition layer** — Most architecturally clean, but doesn't exist yet.

**This is the spec's biggest flaw.** The "extend S/R endpoint" decision seemed clean but ignored the data coupling problem.

---

### FINDING 3: Structure state derivation has ordering bugs

**Claim (Spec Section 3):**
```
IF trend_template.criteria_met >= 7 AND price near resistance:
  → "Uptrend testing resistance"
...
IF support_distance < 3% AND resistance_distance < 3%:
  → "Compression — breakout imminent"
```

**Problem:**
The compression check is LAST but should fire FIRST. If price is within 3% of both R1 and S1, the first rule (`criteria_met >= 7 AND price near resistance`) would match before compression is ever evaluated.

**Verdict: [MISLEADING — CORRECTION]**
The decision tree order matters. Compression is a higher-priority structural observation than trend + proximity. It should be checked first. Similarly, the ATH breakout case (no resistance above price) isn't in the tree at all — it falls through to "between levels" which is wrong.

**Corrected priority order:**
```
1. IF no S/R levels found → "Insufficient data"
2. IF price above ALL resistance (ATH) → "ATH breakout — blue sky"
3. IF price below ALL support (ATL) → "Below all support — freefall"
4. IF support_distance < 3% AND resistance_distance < 3% → "Compression"
5. IF trend_template >= 7 AND resistance_distance < 5% → "Uptrend testing resistance"
6. IF trend_template >= 7 AND support_distance < 5% → "Uptrend pulling back"
7. IF trend_template >= 7 → "Uptrend — between levels"
8. IF trend_template 4-6 AND support_distance < 5% → "Weakening — testing support"
9. IF trend_template 4-6 AND resistance_distance < 5% → "Transitioning — testing resistance"
10. IF trend_template 4-6 → "Mixed trend — between levels"
11. IF trend_template < 4 AND ADX < 15 → "Choppy — no trend"
12. IF trend_template < 4 → "Downtrend"
```

---

### FINDING 4: "Nearest first" vs "Strongest first" level ordering — UNRESOLVED

**Claim (Spec Section 4B):**
> Show max 2 resistance + 2 support levels (nearest first)
> The strongest (most touches + confluent) levels surface first.

**These two statements contradict each other.** Nearest ≠ strongest. R1 at $689 (3 touches) could be nearer than R2 at $720 (8 touches, confluent). Which is R1?

**Verdict: [MISLEADING — CORRECTION]**
Must decide: is R1 the nearest level or the strongest level? For a swing trader, **nearest matters more for immediate action**, strongest matters more for conviction.

**Recommended resolution:** R1/S1 = nearest actionable level (what the trader hits first). Show touch count + confluence so the trader can weigh strength themselves. Don't try to rank by composite score — that's editorializing.

---

## Layer 2: Correctness Audit (Is the logic sound?)

### FINDING 5: 1.5x volume threshold for breakout — PLAUSIBLE but hardcoded

**Claim (Spec Section 4C):**
> "needs volume > 1.5x for breakout conviction"

**Assessment:**
- O'Neil (CANSLIM) recommends 40-50% above average on breakout day = 1.4-1.5x. [PLAUSIBLE]
- Minervini uses similar thresholds in "Trade Like a Stock Market Wizard."
- Our own `check_breakout_quality()` in `pattern_detection.py:80` uses 1.5x as the threshold.
- **BUT** the narrative hardcodes "1.5x" as text. If someone changes `check_breakout_quality()` threshold to 2.0x, the narrative will diverge from the actual breakout logic.

**Verdict: [PLAUSIBLE — but FRAGILE]**
The threshold should be sourced from a constant, not hardcoded in narrative strings. The narrative should reference the same constant that `check_breakout_quality()` uses.

---

### FINDING 6: 5% proximity threshold — UNVERIFIED

**Claim (Spec Section 3):**
> `resistance_distance < 5%` → "near resistance"

**Assessment:**
- The existing `assess_trade_viability()` uses 10% and 20% thresholds (Minervini-aligned).
- Where does 5% come from? It's not in any existing code. The spec invented it.
- For a $200 stock, 5% = $10. For a $20 stock, 5% = $1. The percentage is scale-independent, which is good.
- But should "near" be ATR-relative, not percentage-relative? A stock with 8% ATR that's 5% from resistance is practically ON the level. A stock with 1% ATR that's 5% away has significant room.

**Verdict: [UNVERIFIED — NEEDS: ATR-relative proximity would be more sound]**

**Recommended fix:** "Near" = within 2x ATR of level. This is structurally sound — ATR measures noise, and "within the noise range" is what "near" means to a trader.

```python
def is_near_level(current_price, level, atr):
    distance = abs(current_price - level)
    return distance <= (2.0 * atr)
```

This uses data we already have (`meta.atr`) and is more rigorous than an arbitrary percentage.

---

### FINDING 7: "Breakout imminent" language — EDITORIALIZING

**Claim (Spec Section 3):**
> "Compression — breakout imminent"

**Assessment:**
The spec explicitly says: *"No editorializing. No 'this looks bullish.' Facts + structure + implications."*

"Breakout imminent" is a prediction, not an observation. Compression can resolve with a breakout OR a breakdown. The correct factual statement is "Compression — range narrowing between S1 and R1" or "Tight range ({X}%) — directional resolution expected."

**Verdict: [MISLEADING — CORRECTION]**
Replace "breakout imminent" with "directional move expected" or "range resolution pending." Compression doesn't imply direction.

---

### FINDING 8: Watch item Scenario 2 — RSI < 40 as "oversold" is WRONG for swing

**Claim (Spec Section 4C):**
> `if rsi < 40: "Testing S1 with RSI oversold"`

**Assessment:**
- RSI < 30 is the standard oversold threshold (Wilder's original definition).
- RSI 30-40 is "approaching oversold" not "oversold."
- Our own categorical assessment uses RSI 50-70 as the Strong zone.
- Calling RSI 38 "oversold" is factually wrong and could lead to premature bounce trades.

**Verdict: [MISLEADING — CORRECTION]**

Corrected thresholds:
- RSI < 30: "oversold"
- RSI 30-40: "approaching oversold"
- RSI 40-50: "weakening momentum"
- RSI > 70: "overbought"
- RSI 60-70: "approaching overbought"

---

### FINDING 9: The "10 seconds readable" claim vs actual content

**Claim (Spec Section 2):**
> "Readable in 10 seconds"

**Assessment:**
The expanded card in Section 6 shows: 2 lines of structure state, 4-5 lines of levels, 3 watch items with sub-lines. That's 10-12 lines of text. At average reading speed (~250 wpm), 10-12 lines of dense technical content = ~20-30 seconds.

**Verdict: [MISLEADING — CORRECTION]**
Either:
(a) Reduce content to truly fit 10 seconds (structure state + badge + 2 levels, no watch items in default)
(b) Change the claim to "scannable in 10 seconds" — meaning the structure state badge and level positions are glanceable, with watch items for deeper reading.

Option (b) is more honest. The badge ("Uptrend testing resistance") IS scannable in 2 seconds. The full card is a 20-second read. That's still faster than opening TradingView.

---

### FINDING 10: Backend vs Frontend — the "untestable" argument is overstated

**Claim (Spec Section 5):**
> "Frontend string concatenation is not testable."

**Assessment:**
- `categoricalAssessment.js` generates verdict reasons, advice strings, and assessment narratives — all in the frontend. It's been working since Day 44.
- These ARE testable — with Jest/React Testing Library.
- The pattern detection card renders pattern status strings from backend data — also frontend logic.
- `simplifiedScoring.js` generates the entire Simple Checklist — frontend logic, works fine.

The testability argument for backend is valid but overstated. The stronger argument for backend is: **the narrative depends on data from two separate API calls (S/R + patterns)**. Composing that narrative in the frontend after both calls resolve is actually the NATURAL place to do it, since `fetchFullAnalysisData()` already gathers all the data.

**Verdict: [MISLEADING — CORRECTION]**
The backend-vs-frontend decision should be revisited. The actual tradeoff:

| Factor | Backend | Frontend |
|--------|---------|----------|
| Data availability | Needs pattern data piped into S/R endpoint (coupling) | Already has all data in `fetchFullAnalysisData()` result |
| Testability | Python unit tests (strong) | Jest unit tests (adequate) |
| Iteration speed | Requires backend restart + API change | Hot reload, instant |
| Precedent | `assess_trade_viability()` (strings in backend) | `categoricalAssessment.js` (full narrative in frontend) |
| Coupling | Creates dependency between S/R and pattern engines | No new coupling |

**Revised recommendation:** Frontend generation in a new utility module `priceStructureNarrative.js`, following the `categoricalAssessment.js` pattern. This eliminates Finding 2 entirely (no endpoint architecture problem) and aligns with how the system already works.

The only backend change needed: expose `level_scores` in the S/R API response (Finding 1).

---

## Summary of Findings

| # | Severity | Finding | Spec Section | Fix |
|---|----------|---------|-------------|-----|
| 1 | **CRITICAL** | `level_scores` not in API response | Section 3 | Add to `backend.py` meta dict |
| 2 | **CRITICAL** | Pattern data not available in S/R endpoint | Section 5 | Switch to frontend generation |
| 3 | **HIGH** | Structure state decision tree ordering wrong | Section 3 | Reorder: edge cases first, then trend+proximity |
| 4 | **MEDIUM** | Nearest vs strongest level ordering contradiction | Section 4B | Clarify: nearest = R1/S1, show strength via touches |
| 5 | **LOW** | 1.5x volume hardcoded in narrative text | Section 4C | Source from constant |
| 6 | **HIGH** | 5% proximity threshold is arbitrary | Section 3 | Use ATR-relative proximity (2x ATR) |
| 7 | **MEDIUM** | "Breakout imminent" editorializes | Section 3 | "Directional resolution expected" |
| 8 | **HIGH** | RSI < 40 called "oversold" is wrong | Section 4C | Use correct Wilder thresholds (<30) |
| 9 | **LOW** | "10 seconds readable" is unrealistic | Section 2 | "Scannable in 10 seconds" |
| 10 | **HIGH** | Backend generation creates unnecessary coupling | Section 5 | Frontend utility module instead |

**Critical fixes before implementation: 4 (Findings 1, 2, 3, 6)**
**High-priority corrections: 3 (Findings 8, 10, and 6 overlap)**
**Medium/Low polish: 3 (Findings 4, 5, 7, 9)**

---

## Revised Architecture Recommendation

Based on this audit, the spec's architecture should change:

### Original Design:
```
Backend: price_structure.py → extends /api/sr/<ticker> response
Frontend: PriceStructureCard.jsx renders backend data
```

### Revised Design:
```
Backend: Add level_scores to /api/sr/<ticker> meta (1-line change)
Frontend: priceStructureNarrative.js (new utility, ~150 lines)
          → Takes sr data + pattern data + indicators from fetchFullAnalysisData()
          → Returns { structureState, keyLevels, watchItems, meta }
Frontend: PriceStructureCard.jsx renders the narrative
```

**Why this is better:**
1. No backend coupling problem (Finding 2 eliminated)
2. Follows existing pattern (`categoricalAssessment.js`)
3. All input data already available in frontend after `fetchFullAnalysisData()`
4. Only 1 backend change: expose `level_scores` (1 line)
5. Faster iteration (hot reload vs backend restart)
6. Still testable with Jest

---

*This audit should be reviewed before implementation begins. Update the spec with these corrections.*
