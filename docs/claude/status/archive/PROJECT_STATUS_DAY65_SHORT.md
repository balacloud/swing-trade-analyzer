# Project Status — Day 65 Starting Point
> **Version:** v4.27 (Backend v2.30, Frontend v4.14, Backtest v4.17, API Service v2.9)
> **Last session:** Day 64 (March 5, 2026)
> **Next focus:** Paper trading — use the system daily to find real bugs

---

## What Was Done in Day 64

### 0. BottomLineCard Coherence Fix (from Day 63 carryover)
- **Bug:** `getEntryTypeLabel()` returned 'MOMENTUM ENTRY' via ADX fallback even when `tradeViability.viable = 'NO'`
- **Fix:** Early return `'WAIT FOR ENTRY'` when `viable !== 'YES'` — trade viability is now the authority
- Triggered by LMT: 8/8 Trend Template + BUY + green "READY" contradicting red "NOT VIABLE"

### 1. Comprehensive Module Audit — Round 1 (5 bugs) → BE v2.27

| # | File | Bug | Fix |
|---|------|-----|-----|
| 1 | `news_engine.py` | `[:10]` on `20260305T163000Z` → `20260305T1` | Added `_parse_date()`: `YYYY-MM-DD` extraction |
| 2 | `pattern_detection.py` | Cup & Handle: `df.iloc[right_lip_pos:]` (wrong base) | Changed to `recent.iloc[right_lip_pos:]` |
| 3 | `support_resistance.py` | `resample('W')` = Sunday week-end | Changed to `resample('W-FRI')` |
| 4 | `backend.py` | Stop hardcoded 3% vs structural 2×ATR | Now `entry - (2×ATR)` with 3% fallback |
| 5 | `econ_engine.py` | Unemployment trend threshold 0.1 (too sensitive) | Added `threshold` param; unemployment uses 0.3 |

### 2. Deferred Items Pushed to Fix — Round 2 (VCP + ATR) → BE v2.28

| # | File | Bug | Fix |
|---|------|-----|-----|
| 6 | `pattern_detection.py` | VCP `>=` allowed non-shrinking contractions | Changed to `>` (strictly decreasing) |
| 7 | `pattern_detection.py` | VCP pivot = 90-day max, not recent base top | Changed to `high.iloc[pivot_highs_idx[-1]]` (last swing high) |
| 8 | `support_resistance.py` | ATR = simple average, not Wilder EMA | Implemented Wilder EMA: `ATR_t = (ATR_{t-1} × 13 + TR_t) / 14` |

### 3. Remaining Deferred Items — Round 3 → BE v2.29, FE v4.13

| # | File | Bug | Fix |
|---|------|-----|-----|
| 9 | `cycles_engine.py` | FOMC today → 0 days remaining (confusing) | `d >= from_date` → `d > from_date` (exclusive) |
| 10 | `constants.py` (NEW) | `SUPPORT_PROXIMITY_PCT` duplicated in 3 places | Extracted to shared `constants.py` — single source of truth |
| 11 | `backend.py` / `support_resistance.py` | Local `SUPPORT_PROXIMITY_PCT` definitions | Now import from `constants.py` |
| 12 | `DecisionMatrix.jsx` | Signal weights labeled as if mathematical | Changed heading to "Emphasis:" — clarifies cosmetic nature |

### 4. Round 2 Deep Audit — 5 More Bugs Fixed → BE v2.30, FE v4.14

| # | File | Bug | Fix |
|---|------|-----|-----|
| 13 | `riskRewardCalc.js` | Stop price can be negative (low-price + high ATR stock) | `Math.max(0.01, nearestSupport - (atr × N))` floor added |
| 14 | `backend.py` | Same negative stop possible in backend too | `max(0.01, entry - (2 × atr))` floor added |
| 15 | `pattern_detection.py` | VCP AND gate rejected 35-45% real VCPs (too strict) | `volatility_contracting` removed from gate → confidence booster only. Gate = `decreasing_contractions AND tight_base` |
| 16 | `BottomLineCard.jsx` | CAUTION and NOT_VIABLE both showed 'WAIT FOR ENTRY' | CAUTION → 'CAUTION ENTRY', NOT_VIABLE → 'WAIT FOR ENTRY' (distinct labels) |
| 17 | `categoricalAssessment.js` | All-Decent + Neutral risk → AVOID (wrong) | Fixed: Tech=Decent + (Favorable OR Neutral) → HOLD |
| 18 | `pattern_detection.py` | Cup & Handle: handle high > right lip not validated | Added `handle_below_lip = handle_high <= right_lip_price × 1.02` to detection gate |

---

## Complete Fix Tally — Day 64

**18 bugs fixed across 9 files:**

| File | Count | Key Fixes |
|------|-------|-----------|
| `pattern_detection.py` | 5 | Cup&Handle index, Cup handle_below_lip, VCP strictly-decreasing, VCP pivot, VCP gate |
| `support_resistance.py` | 3 | W-FRI resample, Wilder EMA ATR, import constants |
| `backend.py` | 3 | ATR stop, stop floor, import constants |
| `riskRewardCalc.js` | 2 | Stop floor, bidirectional contradiction |
| `news_engine.py` | 1 | Date parsing |
| `econ_engine.py` | 1 | Unemployment threshold |
| `cycles_engine.py` | 1 | FOMC edge case |
| `BottomLineCard.jsx` | 1 | CAUTION label |
| `categoricalAssessment.js` | 1 | All-Decent HOLD |
| `constants.py` | NEW | Shared proximity constants |
| `DecisionMatrix.jsx` | 1 | "Emphasis" label |

**Still cannot fix:**
- F&G in live verdict vs static 'Neutral' in backtest — needs historical F&G API (not free)

**Flat Base contradictory thresholds:** Verified as non-issue. 15% range → std dev ~3.75% so both conditions are correlated.

---

## Current System State

### Backend (v2.30)
- `news_engine.py`: `_parse_date()` helper + corrected date parsing
- `pattern_detection.py`: Cup&Handle index + handle validation + VCP strictly decreasing + VCP pivot + VCP gate
- `support_resistance.py`: W-FRI resample + Wilder EMA ATR + import constants
- `backend.py`: ATR stop + stop floor + import constants
- `econ_engine.py`: `_trend(threshold=)` param + unemployment 0.3
- `cycles_engine.py`: FOMC exclusive `d > from_date`
- `constants.py`: NEW — `SUPPORT_PROXIMITY_PCT=0.20`, `RESISTANCE_PROXIMITY_PCT=0.30`

### Frontend (v4.14)
- `BottomLineCard.jsx`: viable authority + CAUTION/NOT_VIABLE distinction
- `categoricalAssessment.js`: All-Decent + Neutral → HOLD
- `riskRewardCalc.js`: Stop floor + bidirectional contradiction
- `DecisionMatrix.jsx`: "Emphasis:" label for signal weights

### Known Issues
- See `KNOWN_ISSUES_DAY62.md` — no new open issues
- F&G historical data divergence (tracked, blocked on external data)
- Trade viability vs proximity filter mismatch (low priority, deferred)

---

## Upcoming: New Parallel Project — Options Recommendation Engine

> **Announced Day 64 close.** Full spec to be provided at Day 65 start.

- **What it is:** A separate options recommendation engine that consumes STA outputs
- **Input from STA:** ticker verdict (BUY/HOLD/AVOID), S&R levels, ATR, sector, macro regime from Context Tab
- **Codex involvement:** User has been building this in parallel with OpenAI Codex — will share design/spec at next session
- **STA impact:** NONE. STA stays frozen. Options engine consumes existing `/api/*` endpoints as-is.
- **Architecture:** Separate codebase or module — to be decided when spec is shared

---

## Next Session Priority: Paper Trading

**Feature freeze is in effect.** Use the system for real analysis. Find bugs in the field.

**What to watch for:**
1. Does CAUTION ENTRY now show correctly for wide-stop scenarios?
2. Are news article dates now showing correctly as `YYYY-MM-DD` in Context Tab?
3. Does the suggested stop make sense now (ATR-based, floors at $0.01)?
4. Does VCP only trigger for genuinely contracting patterns now?
5. Are weekly S&R levels slightly different with W-FRI resampling?
6. Log first Forward Test trade in the Forward Test tab

**Stocks to analyze (suggested paper trading candidates):**
- Run 5-10 tickers this week across different sectors
- For each: note sector (Sectors tab), macro context (Context tab), then analyze
- If BUY verdict: log it in Forward Test tab with entry/stop/target

---

## Version History (Last 3 Sessions)
| Day | Version | Key Work |
|-----|---------|----------|
| 62 | v4.24 | Sector Rotation Phase 2, Context Tab (3 engines, 4 endpoints), FRED API |
| 63 | v4.25 | Option C Hybrid news filter, BottomLineCard coherence bug fix |
| 64 | v4.27 | Deep audit: 18 bugs fixed across 9 files (VCP, ATR, W-FRI, stops, patterns, labels) |
