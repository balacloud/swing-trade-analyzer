# Behavioral Audit — Day 71 (March 24, 2026)

> **Purpose:** Verify all universal principles changes (Day 69-70B) work correctly at runtime
> **Method:** 12 tests across code inspection + API calls + data flow tracing
> **Iterations:** 2 (1 defect found in iteration 1, fixed, re-verified in iteration 2)

---

## Test Results

| # | Test | Iter 1 | Iter 2 | Detail |
|---|------|--------|--------|--------|
| 1 | Sentiment out of verdict | PASS | PASS | `assessments = [technical, fundamental]` — sentiment excluded. `(info)` label + `opacity-75` on card. Criteria text: "T+F". |
| 2 | BottomLineCard clean | PASS | PASS | 4 matches for "sentiment" — 2 destructures (unused), 2 comments. Zero active logic. |
| 3 | Progressive disclosure | PASS | PASS | `expandedSections` state, `toggleSection` helper, 4 collapsible sections, indicators hidden-until-click. |
| 4 | Decision Matrix removed | PASS | PASS | Import commented out. No view toggle button. No render block. |
| 5 | TradingView Chart removed | PASS | PASS | Widget block gone. |
| 6 | RS >= 1.2 threshold | PASS | PASS | `rsRatio >= 1.2` in simplifiedScoring.js. Soft message for 1.0-1.19 range. |
| 7 | Cap-aware volume | **DEFECT** | **PASS** | `stockData.marketCap` was always undefined — lives in `stockData.fundamentals.marketCap`. All tickers treated as small-cap. |
| 8 | Cap-aware stop distance | **DEFECT** | **PASS** | Same root cause as #7 (shared `marketCap` variable). |
| 9 | VIX position sizing | PASS | PASS | `vixMultiplier` computed in App.jsx. `positionSizing.js` applies it. |
| 10 | MR Signal Card | PASS | PASS | `/api/mr/signal/AAPL` returns proper data. `MRSignalCard` rendered at line 1992. |
| 11 | Blended RS informational | PASS | PASS | Computed in `rsCalculator.js`, stored in scoring engine. NOT in verdict logic. |
| 12 | Backend parity | PASS | PASS | `categorical_engine.py`: `assessments = [technical, fundamental]`. Matches frontend. |

---

## Defect Found

### DEFECT #1: marketCap unreachable in simplifiedScoring.js
- **Root cause:** `stockData.marketCap` is always `undefined`. The `marketCap` field lives at `stockData.fundamentals.marketCap` (attached by `fetchFullAnalysisData()` in `api.js` line 391).
- **Impact:** Every ticker treated as small-cap. AAPL got $2M volume threshold and 10% stop instead of $10M and 7%.
- **Fix:** `const marketCap = stockData.fundamentals?.marketCap || stockData.marketCap || 0;`
- **Fallback:** If fundamentals fetch fails, `marketCap = 0` → small-cap (most permissive thresholds — safe default).
- **Commit:** `caf81bb9` — "Day 71: Fix cap-aware logic — marketCap was unreachable in simplifiedScoring"

---

## Verified Data Flow (Post-Fix)

| Ticker | marketCap | Cap Tier | Volume Threshold | Stop Distance |
|--------|-----------|----------|-----------------|---------------|
| AAPL | $3.65T | large-cap | $10M | 7% |
| UPST | $2.6B | mid-cap | $5M | 9% |
| STEM | $89M | small-cap | $2M | 10% |

---

## Lesson
This is exactly the Day 50 pattern: build passes, code looks right, but **data contract is wrong**. The variable `stockData.marketCap` was never populated — it was a phantom path. Without behavioral audit, paper trading would have used wrong thresholds for every large/mid-cap stock.
