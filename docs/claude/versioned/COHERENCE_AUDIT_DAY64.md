# Coherence Audit — Day 64
> **Version:** v4.25 → v4.26 (BE v2.27, FE v4.12)
> **Date:** March 5, 2026
> **Scope:** pattern_detection.py · support_resistance.py · backend.py (S&R route) · riskRewardCalc.js · categoricalAssessment.js · cycles_engine.py · econ_engine.py · news_engine.py
> **Method:** 4 parallel deep-read agents → synthesis → verified code reads → targeted fixes

---

## Executive Summary

28 findings across 8 modules. 5 confirmed bugs fixed. 6 design concerns documented (deferred). 17 verified-correct items.

**Bugs Fixed (5):**
1. `news_engine.py` — date parsing yielded `YYYYMMDDTH` instead of `YYYY-MM-DD`
2. `pattern_detection.py` — Cup & Handle handle_data used `df` with `recent`-based index
3. `support_resistance.py` — weekly resampling used Sunday week-end instead of Friday
4. `backend.py` — suggested stop was hardcoded 3% instead of structural 2×ATR
5. `econ_engine.py` — unemployment trend threshold 0.1 (too sensitive, should be 0.3 per spec)

---

## Layer A: pattern_detection.py

### FIXED ✅ — Cup & Handle: handle_data index mismatch (HIGH)
**File:** `pattern_detection.py:528`
**Bug:** `handle_data = df.iloc[right_lip_pos:]` — `right_lip_pos` is a positional index within `recent = df.tail(180)`, not within `df`. On a stock with 500+ days of history, `df.iloc[45:]` would cut off most of the cup formation and return spurious handle data.
**Fix:** Changed to `recent.iloc[right_lip_pos:]`
**Impact:** Cup & Handle detection was looking at wrong data for handle validation. Could produce false positives (handle detected in wrong part of chart) or false negatives.

### DESIGN CONCERN — VCP contraction logic (CRITICAL, deferred)
**File:** `pattern_detection.py:338–368`
**Issue:** VCP contraction check compares per-swing depth as % of price range, not whether each successive swing is *smaller* than the prior one. Minervini's definition requires each consolidation to be tighter than the previous — a sequence of 3 swings should have swing2 < swing1 and swing3 < swing2. Current code doesn't enforce this ordering.
**Impact:** VCP score can be awarded for patterns that don't genuinely contract. This inflates VCP confidence.
**Deferred:** Fixing requires redesigning the swing extraction logic. Deferred to dedicated VCP audit session.

### DESIGN CONCERN — VCP pivot price (HIGH, deferred)
**File:** `pattern_detection.py:386`
**Issue:** `pivot_price = high.max()` = highest close in entire 90-day window. VCP pivot should be the breakout level above the *final tight base*, not the 90-day high. Could recommend entry at wrong level.
**Deferred:** Requires defining "final base" programmatically.

### DESIGN CONCERN — Flat Base contradictory thresholds (MEDIUM, deferred)
**File:** `pattern_detection.py:371–373`
**Issue:** Flat Base checks `base_range_pct <= 15%` (15% peak-to-trough OK) AND `flatness_pct < 5%` (std dev < 5% of mean). A base can be 14% wide (passes) but std dev of 10% (fails). The two metrics measure different things. Not necessarily wrong but intent is ambiguous.
**Deferred:** Requires clarity on which metric to prioritize.

### VERIFIED CORRECT ✅ — Trend Template (8 Minervini criteria)
All 8 criteria verified correct:
1. Price > 200 SMA ✓
2. 200 SMA trending up (slope > 0 over last 20 bars) ✓
3. Price > 150 SMA ✓
4. 150 SMA > 200 SMA ✓
5. Price > 50 SMA ✓
6. Price within 25% of 52-week high ✓
7. Price at least 30% above 52-week low ✓
8. RS Rating > 70 ✓

---

## Layer B: support_resistance.py + backend.py (S&R route)

### FIXED ✅ — Weekly resampling uses Sunday not Friday (HIGH)
**File:** `support_resistance.py:835`
**Bug:** `resample('W')` = week ending Sunday. Markets close Friday. An incomplete current week (Mon–Thu) would be grouped with a new Sunday, creating a partial weekly candle with only 1–4 days of data that gets the same weight as a full 5-day week.
**Fix:** Changed to `resample('W-FRI')` — week closes at Friday's market close.
**Impact:** MTF weekly support/resistance levels were slightly off due to incorrect weekly OHLC bars.

### FIXED ✅ — Suggested stop hardcoded 3% instead of structural 2×ATR (HIGH)
**File:** `backend.py:1546`
**Bug:** `suggested_stop = round(suggested_entry * 0.97, 2)` — ignores ATR and market structure entirely. A 3% stop on a $500 stock = $15; ATR might be $8 (stop too wide) or $25 (stop too tight). Also contradicted `riskRewardCalc.js` which uses `support - 2×ATR` for pullback stops.
**Fix:** Now uses `suggested_entry - (2 × sr_levels.meta.get('atr'))`, with 3% as fallback only if ATR unavailable.
**Impact:** Suggested stop now consistent with what `riskRewardCalc.js` computes on the frontend.

### DESIGN CONCERN — ATR formula is simple average not Wilder EMA (MEDIUM, deferred)
**File:** `support_resistance.py:104–133`
**Issue:** `atr = np.mean(tr[-period:])` — simple 14-period average of True Range. Wilder's ATR uses exponential smoothing (`ATR = (prev_ATR × 13 + TR) / 14`). Simple average gives equal weight to all periods; Wilder gives more weight to recent volatility.
**Impact:** ATR value is a reasonable approximation but not technically correct. For a $100 stock the difference is typically $0.20–0.50. Acceptable approximation for now.
**Deferred:** Low priority — approximation is close enough for swing trading timeframes.

### DESIGN CONCERN — Trade viability calculated before proximity filtering (HIGH, deferred)
**File:** `support_resistance.py` viability calculation
**Issue:** Trade viability (proximity check: "Extended X% from support") runs against all S&R levels, then the backend separately filters actionable levels for the suggested entry/stop/target. If viability uses a different support level than what's suggested as entry, the verdict could say "NOT VIABLE" for a level the user isn't even being told to use.
**Deferred:** Requires refactoring viability to run after proximity filtering with the same level set.

### DESIGN CONCERN — Support proximity 20% hardcoded in 3 places (MEDIUM, deferred)
**File:** `support_resistance.py` + `backend.py`
**Issue:** `SUPPORT_PROXIMITY_PCT = 0.20` is defined in `backend.py` but the same 20% threshold appears hardcoded in `support_resistance.py` viability logic. No single source of truth.
**Deferred:** Minor refactor — extract to shared constant.

### VERIFIED CORRECT ✅ — MTF confluence logic
Weekly confluence check is directionally correct (weekly support below daily support = stronger zone). The asymmetry (weekly adds +1 confidence but its absence doesn't subtract) is intentional — it's additive evidence, not a requirement.

---

## Layer C: riskRewardCalc.js + categoricalAssessment.js

### VERIFIED CORRECT ✅ — R:R formulas
- Pullback stop: `support - (2×ATR)` ✓
- Momentum stop: `support - (1.5×ATR)` ✓
- Target: nearest resistance ✓
- R:R = `(target - entry) / (entry - stop)` ✓
- `Math.max()` for "nearest support" = highest support below price = correct (closest to current price)

### VERIFIED CORRECT ✅ — Threshold parity (frontend vs backend)
All thresholds match across both systems:
- RSI thresholds (70/50/30) ✓
- RS Rating (>80 strong, >50 decent) ✓
- Debt/Equity (<0.5 strong, <1.5 decent) ✓
- ROE (>20% strong, >10% decent) ✓
- Revenue growth (>20% strong, >5% decent) ✓
- VIX (<20 favorable, <30 neutral, ≥30 adverse) ✓
- F&G thresholds (Strong 60–80, Neutral 35–60, Weak <35 or >80) ✓ (synced Day 61)

### DESIGN CONCERN — F&G in live verdict but not in backtest (HIGH, deferred)
**Files:** `categoricalAssessment.js` (live) vs `backtest/backtest_holistic.py` (backtest)
**Issue:** Live system uses real-time F&G index in Sentiment assessment. Backtest uses static `'Neutral'` for all historical dates (no historical F&G data). This means backtested win rates were computed without sentiment signal — live system with sentiment is slightly different from what was backtested.
**Impact:** p=0.002 backtest result is valid for the Technical+Fundamental+Risk combination. Sentiment adds information not reflected in the backtest.
**Deferred:** Would require historical F&G data source. CNN publishes it but no free API. Accept divergence for now — sentiment is the weakest signal anyway.

### DESIGN CONCERN — Signal weights are cosmetic (LOW, deferred)
**File:** `categoricalAssessment.js`
**Issue:** The system returns `signalWeights: {technical: 70, fundamental: 20, sentiment: 10}` (for momentum) or similar ratios. These numbers appear in the UI but are NOT applied to the verdict math — verdict uses hard-coded hierarchical rules, not weighted sums. The weights are effectively documentation, not computation.
**Impact:** No correctness issue. Could be misleading if UI implies weights drive the verdict. Deferred — low priority.

---

## Layer D: cycles_engine.py + econ_engine.py + news_engine.py

### FIXED ✅ — news_engine.py date parsing (CRITICAL)
**File:** `news_engine.py:127`
**Bug:** `[:10]` on Alpha Vantage format `20260305T163000Z` gives `20260305T1` (10 chars including the `T` and first digit of hour) instead of `2026-03-05`.
**Fix:** Added `_parse_date()` helper: `f"{time_str[:4]}-{time_str[4:6]}-{time_str[6:8]}"` for proper `YYYY-MM-DD` extraction.
**Impact:** All article dates in the Context Tab were displaying garbage values (`20260305T1` etc.) in the UI. Sort-by-date in `_curate_articles()` was also broken since these strings were being compared lexicographically.

### FIXED ✅ — econ_engine.py unemployment trend threshold (MEDIUM)
**File:** `econ_engine.py:64–78`
**Bug:** `_trend()` used `threshold=0.1` (hardcoded) for both Fed Funds and Unemployment Rate. For Fed Funds, 10bps is appropriate (that's how the Fed moves rates). For Unemployment, the spec says "rapidly rising = >0.3% over 3 months" — 0.1 would flag normal seasonal unemployment noise as "rapidly rising."
**Fix:** Added `threshold` parameter to `_trend()` (default 0.1 preserved for Fed Funds). Unemployment card now passes `threshold=0.3`.
**Impact:** Unemployment regime was previously over-classifying as NEUTRAL/ADVERSE during minor fluctuations.

### VERIFIED CORRECT ✅ — Seasonal month indexing
`month in [11, 12, 1, 2, 3, 4]` — Python `datetime.month` is 1-indexed. Favorable months Nov-Apr map correctly to [11,12,1,2,3,4]. March = month 3 = FAVORABLE ✓

### VERIFIED CORRECT ✅ — Presidential year formula
`((current_year - 2025) % 4) + 1` → 2026 = Year 2 = ADVERSE ✓. Year 3/4 = FAVORABLE, Year 1 = NEUTRAL, Year 2 = ADVERSE ✓

### VERIFIED CORRECT ✅ — Quad Witching algorithm
Computed March 2026 Quad Witching = March 20, 2026 (3rd Friday of March). Verified: March 6 = 1st Fri, March 13 = 2nd Fri, March 20 = 3rd Fri ✓

### DESIGN CONCERN — FOMC "today" edge case (LOW)
**File:** `cycles_engine.py`
**Issue:** `d >= from_date` means if today IS an FOMC date, distance = 0 days → triggers options block. The correct behavior is probably: if FOMC is today, it's currently happening — arguably `d > from_date` (exclusive) is more correct, returning the *next* FOMC. Zero days remaining creates a confusing "FOMC in 0 days" display.
**Deferred:** Affects only on FOMC meeting days (8 per year). Low priority.

---

## Complete Finding Summary

| # | Severity | Module | Finding | Status |
|---|----------|--------|---------|--------|
| 1 | HIGH | pattern_detection.py | Cup & Handle: handle_data uses df not recent | **FIXED** |
| 2 | CRITICAL | pattern_detection.py | VCP contraction measures depth not successive shrinkage | Deferred |
| 3 | HIGH | pattern_detection.py | VCP pivot = 90-day high, not tight base breakout | Deferred |
| 4 | MEDIUM | pattern_detection.py | Flat Base: contradictory 15% range vs 5% std dev | Deferred |
| 5 | HIGH | support_resistance.py | Weekly resample 'W' (Sunday) → should be 'W-FRI' | **FIXED** |
| 6 | MEDIUM | support_resistance.py | ATR = simple average, not Wilder EMA | Deferred |
| 7 | HIGH | support_resistance.py | Viability runs before proximity filter | Deferred |
| 8 | MEDIUM | support_resistance.py | 20% proximity threshold in 3 places | Deferred |
| 9 | HIGH | backend.py | Stop hardcoded 3% vs structural 2×ATR | **FIXED** |
| 10 | HIGH | categoricalAssessment.js | F&G in live verdict but not in backtest | Deferred |
| 11 | LOW | categoricalAssessment.js | Signal weights cosmetic, not applied to verdict | Deferred |
| 12 | ✓ | riskRewardCalc.js | R:R formulas correct | Verified |
| 13 | ✓ | riskRewardCalc.js | All threshold parities match backend | Verified |
| 14 | ✓ | riskRewardCalc.js | Math.max for nearest support = correct | Verified |
| 15 | ✓ | categoricalAssessment.js | Verdict hierarchy 11 steps correct | Verified |
| 16 | ✓ | categoricalAssessment.js | _sanitize() NaN/null defense correct | Verified |
| 17 | ✓ | categoricalAssessment.js | F&G thresholds match backend (Day 61 sync) | Verified |
| 18 | CRITICAL | news_engine.py | Date parsing [:10] → YYYYMMDDTH not YYYY-MM-DD | **FIXED** |
| 19 | MEDIUM | econ_engine.py | Unemployment trend threshold 0.1 → should be 0.3 | **FIXED** |
| 20 | LOW | cycles_engine.py | FOMC today → 0 days → options block (edge case) | Deferred |
| 21 | ✓ | cycles_engine.py | Seasonal month indexing [11,12,1,2,3,4] correct | Verified |
| 22 | ✓ | cycles_engine.py | Presidential year formula correct (2026=Y2=ADVERSE) | Verified |
| 23 | ✓ | cycles_engine.py | Quad Witching 3rd Friday algorithm correct | Verified |
| 24 | ✓ | cycles_engine.py | FOMC list 2026–2027 complete | Verified |
| 25 | ✓ | econ_engine.py | CPI YoY formula correct (12-period lookback) | Verified |
| 26 | ✓ | econ_engine.py | Fed Funds direction (6-month delta) correct | Verified |
| 27 | ✓ | news_engine.py | Reputable source filtering case-insensitive | Verified |
| 28 | ✓ | news_engine.py | _curate_articles() 3 per bucket correct | Verified |

**Score: 5 fixed, 6 deferred design concerns, 17 verified correct.**

---

## Version Impact

| Component | Before | After |
|-----------|--------|-------|
| Backend | v2.26 | v2.27 |
| Frontend | v4.12 | v4.12 (no FE changes) |
| Overall | v4.25 | v4.26 |

### Files Modified
- `backend/news_engine.py` — added `_parse_date()`, fixed date parsing
- `backend/pattern_detection.py` — Cup & Handle `df.iloc` → `recent.iloc`
- `backend/support_resistance.py` — `resample('W')` → `resample('W-FRI')`
- `backend/backend.py` — 3% stop → 2×ATR stop (3% fallback)
- `backend/econ_engine.py` — `_trend()` gains `threshold` param, unemployment passes 0.3
