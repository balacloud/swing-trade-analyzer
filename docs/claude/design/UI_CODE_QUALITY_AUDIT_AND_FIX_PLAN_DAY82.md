# UI Code Quality Audit + Fix Plan (Day 82)

> **Purpose:** Findings from three Fable-model audits (read-only, code + live-behavior verification) of the Analyze Stock page's Full Analysis view, the Scan Market tab, and a Tradier API integration evaluation — plus a concrete, executable fix plan. Written so a fresh Sonnet session with no memory of the audit conversation can pick this up and run with it.
> **Location:** `docs/claude/design/`
> **Source:** Three parallel Fable-model dispatches, Day 82 (July 12, 2026), triggered by user feedback that the Bottom Line Card (already removed same day) felt redundant — this is the "is there more of that?" follow-up.
> **Verification note:** One of the three audits ("Analyze page Full Analysis cards") came back flagged by the harness as reviewed without the normal safety classifier available. Two of its most consequential claims were spot-checked directly against the live codebase before this doc was written (see "Corrections" below) — one held up exactly as described, one was overstated and is corrected here. Treat any other single claim in this doc with the same "verify before acting" discipline the rest of this project applies to audit output (see Golden Rule 2/3, and the Day 82 fmp_provider.py correction as precedent).
> **Status:** ALL GROUPS DONE (A, B, C, D, E) and browser/API-verified Day 83, except E5/E6 which the plan itself said weren't worth a dedicated task (left as-is — see those entries). See per-task status markers below for what changed and how it was verified.
> **Last Updated:** Day 83 (July 13, 2026, session 2)

---

## How to use this document

1. Tasks are grouped by category (A: real bugs, B: duplication/DRY, C: dead code, D: new capability, E: polish), not by dependency chain — there is no Phase 0/1/2 gating like `BREAKOUT_ENHANCEMENT_PLAN.md` has, because none of this touches the frozen paper-trading verdict config. Work through groups in order (A first) but tasks within a group can be done in any order.
2. **Golden Rule 2/3 applies as always: read the current file before editing, don't trust line numbers below without re-verifying** — this doc was written at a point in time and the file will have moved on.
3. One correction is already baked in below (the MR Signal Card finding) — do not re-litigate it, the correct current state is documented.
4. Nothing here touches `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md`-frozen thresholds. Task A1 changes *which candidates get shown/scanned*, not any verdict/entry/exit threshold — still worth a moment's thought before touching, per Golden Rule 18's spirit, but it is not itself a frozen value.

---

## Corrections to the raw audit output (read this before A6)

**MR Signal Card — the audit overstated this.** The raw audit claimed `MRSignalCard.jsx` "advertises entry/stop/target for the *unrestricted* live detector (Price>$5, Vol>500K)... a strategy configuration known to have no edge (PF 0.99)." **This is not true as of Day 81.** `backend/mean_reversion.py`'s `detect_mr_signal()` was fixed earlier the same day to use `current_price > 10` and `avg_dollar_volume > 25_000_000` (the validated PF-1.16 liquidity-gated config) — verified directly by reading the current file (`mean_reversion.py:140-141`). **What's actually true and worth fixing (Task A6 below) is much smaller**: `MRSignalCard.jsx`'s `formatConditionName()` lookup table (lines 106-114) still has stale display labels — `'Price > $5'` and `'Vol > 500K'` — describing the *old* thresholds, even though the underlying signal logic is correct. This is a cosmetic label-text bug, not a live-money-adjacent risk.

**Verified true, no correction needed:** Trade Setup Card's missing stop-price floor (Task A2) — confirmed by reading both `riskRewardCalc.js:28` (has `Math.max(0.01, ...)`) and `App.jsx:1550` (does not) side by side. This one is real exactly as described.

---

## Group A — Real bugs (fix first)

### A1. Scan tab and the paper-trading engine scan different candidate sets
- **Status:** ✅ DONE (Day 83) — guarded the order_by override so 'best' keeps `build_best_query()`'s ADX sort; verified `/api/scan/tradingview?strategy=best&limit=15` returns tickers/order/ADX values byte-identical to calling `scan_queries.build_best_query()` directly.
- **Severity:** High — undermines the Day 81 "shared query, one implementation" guarantee (Golden Rule 19) between `backend.py`'s Scan tab route and `backend/paper_trading/live_signals.py`'s automated engine.
- **Files:** `backend/backend.py` (`scan_tradingview()`, locate current line range — was ~1838-1976 pre-audit), `backend/scan_queries.py` (`build_best_query()`)
- **Root cause:** `scan_queries.build_best_query()` sets `order_by('ADX', ascending=False)` and `.limit(limit)`. But `scan_tradingview()` then *unconditionally* runs, after calling `build_best_query()` for the `'best'` strategy:
  ```python
  query = query.order_by('relative_volume_10d_calc', ascending=False)
  query = query.limit(limit)
  ```
  `tradingview_screener`'s `order_by()` **replaces** the prior sort (confirmed in the installed library's `query.py`). Since TradingView truncates server-side at `limit` (default 50), and market_index='all' routinely has >50 qualifying candidates, **the Scan tab UI and the automated paper-trading engine end up looking at two different top-50 sets** whenever this happens. The `scan_queries.py` module docstring's claim of "one implementation, not two that can drift" is not currently true for candidate ordering.
- **Action:**
  1. Decide the canonical ordering for `'best'`/Config C candidates — ADX-desc (what `live_signals.py` uses, matching the backtested selection) or relative-volume-desc (what the Scan tab currently shows). Given the automated engine is the one actually generating the paper-trading record that matters, ADX-desc (i.e., what `scan_queries.build_best_query()` already sets) is almost certainly correct — the Scan tab should match it, not the other way around.
  2. In `scan_tradingview()`, only apply the `order_by('relative_volume_10d_calc', ...)` override for strategies that don't already set their own ordering (i.e., guard it so `'best'` keeps `build_best_query()`'s ADX sort). Remove the redundant `.limit(limit)` call too (already set inside `build_best_query()`).
  3. Also remove the now-dead query-construction block at the top of the `'best'` branch if any remnants remain from before the Day 81 extraction (the audit found leftover unused query-building code around this branch — verify and clean up).
- **Acceptance:** Call `/api/scan/tradingview?strategy=best&limit=50` and separately run `live_signals.get_momentum_signals()` (or inspect its TradingView query call) on the same day; the returned ticker sets and their order should match exactly for the same `limit`.

### A2. Trade Setup Card can display an impossible negative stop price
- **Status:** ✅ DONE (Day 83) — entry-strategy IIFE now calls `calculateRiskReward()` instead of re-implementing the math; verified with a synthetic edge case (nearestSupport=1.5, atr=1.2 → unfloored would be -$0.90, actual floored to $0.01) plus a live AAPL regression check (no negative values, no console errors). Also fixed the stale "Max stop cap: 7%" doc claim in `riskRewardCalc.js`.
- **Severity:** High — user-visible, can show self-contradictory numbers on the same screen (viability badge uses the floored value from `riskRewardCalc.js`, the entry-strategy display uses the unfloored inline duplicate).
- **Files:** `frontend/src/App.jsx` (Trade Setup Card, entry-strategy IIFE — was ~lines 1527-1697 pre-audit; also calls `calculateRiskReward()` twice per render at ~1379 and ~1415, worth consolidating to one call while in here), `frontend/src/utils/riskRewardCalc.js` (`calculateRiskReward()`, the correct source of truth)
- **Root cause:** `riskRewardCalc.js` was built Day 61 specifically to extract this math from 4 duplicated locations into one shared function, with an explicit floor: `const pullbackStop = nearestSupport ? Math.max(0.01, nearestSupport - (atr * 2)) : 0;` (line 28, with a comment: "Floor at $0.01 — stop price can never be negative or zero"). The Trade Setup Card's own entry-strategy display block re-implements the same calculation inline **without the floor**: `const pullbackStop = nearestSupport - (atr * 2);` — for a cheap, volatile stock this can go negative, and nothing stops it from rendering that way.
- **Action:** Delete the inline re-implementation in the entry-strategy IIFE. Call `calculateRiskReward(srData, currentPrice)` once (reuse the existing call already made for the viability badge — don't call it twice) and read `pullbackStop`/`momentumStop`/`pullbackRR`/`momentumRR`/etc. from its return value instead of recomputing. This also fixes the "displayed R:R can silently disagree with the viability badge's R:R" issue the audit noted, since they'll be reading the exact same computed numbers.
- **Also while here:** `riskRewardCalc.js`'s header comment claims "Max stop cap: 7% from entry" (line 10) — the audit found no such cap actually implemented in the function. Either add it or delete the claim from the comment; don't leave a doc/code mismatch.
- **Acceptance:** Find or construct a test case where `nearestSupport - (atr * 2)` would go negative (cheap, high-ATR ticker); confirm the displayed pullback stop is floored at $0.01, not negative, and matches what the viability badge shows.

### A3. Price Structure Card's "pattern forming" watch item can never fire
- **Status:** ✅ DONE (Day 83) — `generatePriceStructure()` gained a third param (`actionablePatternsList`) since it needed BOTH the raw payload (for `trendTemplate`) and the computed actionable-patterns array (option (b) from the Action list, not (a) — swapping the whole param would have broken `trendTemplate`/Minervini TT-based structure state derivation). Verified live on JPM: "Cup & Handle forming (100%) — pivot at $341.91" now renders. Also deleted the unused `key` var and the two no-op ATH/ATL projection branches.
- **Severity:** Medium — a documented, designed feature (Priority 5 in the card's priority-ordered rule list) is silently dead.
- **Files:** `frontend/src/utils/priceStructureNarrative.js` (lines ~190-196 and ~285-287 read `patterns?.actionablePatterns`), `frontend/src/App.jsx` (line ~390, the `generatePriceStructure(data.sr, data.patterns)` call site)
- **Root cause:** `generatePriceStructure()` is called with the *raw* patterns API payload (`data.patterns`), but its Priority-5 watch-item logic and `meta.patternsActive` both read `patterns?.actionablePatterns` — a field that only exists on the *frontend-computed* result of `getActionablePatterns()` (in `categoricalAssessment.js`), never on the raw backend payload. The condition can never be true.
- **Action:** Either (a) call `getActionablePatterns(data.patterns)` and pass its result into `generatePriceStructure()` instead of the raw payload, or (b) if `generatePriceStructure()` needs both the raw and the actionable-filtered view, add a second parameter. Check every other caller/consumer of `generatePriceStructure()` before changing its signature.
- **Also found in the same file (fold into this task, small):** `getTouches()` computes a `const key = ...` (line ~35) that's never used — delete. Lines ~250-251 assign `[]` to an already-empty array (no-op) — delete or fix if it was meant to do something.
- **Acceptance:** Construct or find a real ticker where a pattern is `forming` with confidence <60% (not yet actionable) near its pivot; confirm the Priority-5 watch item now actually renders on the Price Structure Card.

### A4. Three inconsistent liquidity thresholds on one page
- **Status:** ✅ DONE (Day 83) — new shared `frontend/src/utils/liquidityThresholds.js` (`getLiquidityThreshold(marketCap)`), adopted by `simplifiedScoring.js` (was already correct, now the source of truth), `scoringEngine.js` Quality Gates (was flat $10M), and `App.jsx`'s Price Card (was flat $10M/$50M, now cap-aware threshold ×1/×2 for yellow/green). Verified live on ASIC (small-cap, $1.8M/day): Quality Gates now says "threshold: > $2M" (was "$10M"), Simple Checklist Volume FAILs consistently, Price Card shows the same $2M-anchored value — all three agree. Also added the "RS Unavailable" non-critical gate entry for null/undefined rs52Week (previously silently skipped), rendered visually distinct (gray, not red) from real critical gates.
- **Severity:** Medium — same stock can pass a liquidity check in one view and fail it in another, on the same page, same session.
- **Files:** `frontend/src/utils/scoringEngine.js` (Quality Gates liquidity check, flat `$10M`, ~line 434), `frontend/src/utils/simplifiedScoring.js` (Simple Checklist's cap-aware `$2M small / $5M mid / $10M large`, ~line 203 — this is the Day 70B-validated correct version), `frontend/src/App.jsx` (Price Card's inline liquidity coloring, `$10M`/`$50M` thresholds, ~line 1320)
- **Action:** Align all three to the Day 70B cap-aware thresholds (`$2M small / $5M mid / $10M large`) that `simplifiedScoring.js` already implements correctly. Extract a single shared `getLiquidityThreshold(marketCap)` (or similar) utility function so there's exactly one place this logic lives, rather than three.
- **Also found in `scoringEngine.js`'s Quality Gates (fold into this task):** the RS gate (`if (rsData?.rs52Week && rs52Week < 0.8)`, ~line 412) silently skips the gate entirely when `rs52Week` is falsy (null, 0, or undefined) — a stock with genuinely uncomputable RS raises no warning at all, which is the opposite of what a quality *gate* should do on missing data. Add an explicit "RS unavailable" warning branch.
- **Acceptance:** Pick a ticker with market cap and volume such that it's a "small cap" under the Day 70B tiers but volume is between $5M-$10M (passes flat-$10M gates as a fail, but should pass under the correct $2M small-cap threshold, or vice versa) — confirm Quality Gates, Simple Checklist, and the Price Card all agree.

### A5. Nirmal watchlist scan fails silently instead of showing an error
- **Status:** ✅ DONE (Day 83) — now calls the shared `fetchSupportResistance()` from `api.js` (same `API_BASE_URL`) instead of a hardcoded `http://localhost:5001` fetch, and throws (propagating to the same `scanError` path other strategies use) when a majority of the 20 tickers fail. Verified both directions: backend stopped → red error box shown, no false "No stocks matched" text; backend up → all 20 rows render normally, zero console errors.
- **Severity:** Medium — misleading UX (a real backend outage looks identical to "no stocks matched").
- **Files:** `frontend/src/App.jsx` (`runScan()`'s `selectedStrategy === 'nirmal'` branch, ~lines 479-508), `frontend/src/services/api.js` (has the reusable pattern this branch should use instead — `fetchSupportResistance()`, ~line 381, and `API_BASE_URL` constant, line 16)
- **Root cause:** Every per-ticker fetch failure in this branch returns `null` and gets filtered out of the results array with no error propagation. If the backend is completely down, the other 5 scan strategies correctly show a red error box (via `fetchScanResults()`'s error path); this branch instead renders "No stocks matched the Nirmal's Watchlist criteria" — false information. It also hardcodes `http://localhost:5001` directly instead of using `API_BASE_URL` from `api.js` (meaning it would silently break in any non-default-port deployment), and fires 20 unthrottled parallel requests with no batching.
- **Action:** Rewrite this branch to use `fetchSupportResistance()` (or add a small dedicated `fetchNirmalWatchlist()` helper in `api.js` following the same conventions) instead of raw hardcoded `fetch()` calls. If most/all of the 20 requests fail, set `scanError` (the same state variable the other 5 strategies use) instead of silently returning an empty result set.
- **Acceptance:** Stop the backend, run a Nirmal watchlist scan; confirm the same red error box other strategies show now appears here too, not a fake "no matches" empty state.

### A6. MR Signal Card's condition labels are stale (see Corrections section above)
- **Status:** ✅ DONE (Day 83) — labels updated to 'Price > $10' / '20d Avg $ Volume > $25M'. Verified live on ABBV (active MR signal): both new labels render, no stale text, zero console errors.
- **Severity:** Low (cosmetic — the underlying gate is already correct, only the label text is wrong)
- **Files:** `frontend/src/components/MRSignalCard.jsx`, `formatConditionName()`, lines 106-114
- **Action:** Update the display strings to match the Day 81 gate actually enforced by `backend/mean_reversion.py:140-141`: `price_filter: 'Price > $5'` → `'Price > $10'`, `volume_filter: 'Vol > 500K'` → `'20d Avg $ Volume > $25M'`.
- **Acceptance:** Trigger a real MR signal in the UI (e.g. re-run the Analyze page on GOOGL or ABBV while they're pending in the paper-trading ledger) and confirm the condition list shows the correct current thresholds.

---

## Group B — Duplication / DRY violations

### B1. `backend.py`'s scan route still hand-duplicates candidate parsing
- **Status:** ✅ DONE (Day 83, done alongside A1 since it touched the same region) — `scan_tradingview()` now calls `scan_queries.parse_candidates()` instead of a second hand-maintained copy of the junk-ticker filters. Verified: calling `parse_candidates()` directly on the same query's results reproduced the exact same candidate list the route returns.
- **Files:** `backend/backend.py` (`scan_tradingview()`, the row-parsing loop, was ~lines 1889-1954 pre-audit — junk-ticker filters for warrants/preferred/SPAC-units/commodity-trusts), `backend/scan_queries.py` (`parse_candidates()`, already does this correctly and is what `live_signals.py` uses)
- **Action:** Replace the inline parsing loop in `scan_tradingview()` with a call to `scan_queries.parse_candidates()`. Also remove the duplicated `INDEX_MAP`/`CANADIAN_MARKETS`/exchange-list constants from `backend.py` if `scan_queries.py`'s copies can serve both call sites.
- **Acceptance:** Same candidate list, minus code duplication; diff the before/after output for a real scan call to confirm no behavior change beyond what Task A1 already intentionally changes.

### B2. Pattern Detection Card is a 3x copy-paste triptych
- **Status:** ✅ DONE (Day 83) — new `PatternMiniCard.jsx` (App.jsx side) and a shared `buildActionablePattern()` helper (`categoricalAssessment.js` side) replace the 3 copy-pasted blocks. Also fixed both unguarded `&&` renders (pivot_price, volumeRatio → `!= null`). Verified live on JPM: all 3 pattern tiles + the Actionable Patterns section render with correct data (Cup Depth 17.2%, Trigger/Stop/Target/R:R all matching the pre-refactor math), zero console errors.
- **Files:** `frontend/src/App.jsx` (VCP / Cup & Handle / Flat Base blocks, was ~lines 1864-2003 pre-audit), `frontend/src/utils/categoricalAssessment.js` (`getActionablePatterns()`, same triplication pattern, ~lines 72-187)
- **Action:** Refactor both the JSX blocks and the `getActionablePatterns()` logic to iterate over a small config array (`[{key: 'vcp', label: 'VCP', ...}, {key: 'cup_handle', ...}, {key: 'flat_base', ...}]`) instead of three near-identical hand-written blocks differing only in field names.
- **Also found in the same card (fold in, small, Golden Rule 4 pattern):** unguarded numeric `&&` renders at (pre-audit) lines ~1899, ~1946, ~1993 (`{pivot_price && (...)}`) and ~2051 (`{pattern.breakout?.volumeRatio && (...)}`) — should be `!= null` checks per the existing Golden Rule 4 ("Day 68: `{value && <div>}` with value=0 renders '0'").
- **Acceptance:** All three pattern types still render identically for known test tickers (VCP/Cup&Handle/Flat Base each triggered by at least one real ticker); confirm no visual regression.

### B3. Zombie legacy verdict can still silently reach the UI
- **Status:** ✅ DONE (Day 83) — traced reachability first: `categoricalResult` and `analysisResult` are always set together (same synchronous block) or reset together, never one without the other, so the fallback was confirmed permanently unreachable. Deleted `determineVerdict()` entirely (not just the fallback) since its only consumer was this dead code path — fully removed rather than relabeled. Verified live: Verdict Card and Simple view's "Full Assessment" line both still show real verdicts (BUY on AAPL) with zero console errors.
- **Files:** `frontend/src/utils/scoringEngine.js` (`determineVerdict()`, ~lines 456-505; header comment documenting 0.011 correlation, line 12), `frontend/src/App.jsx` (Verdict Card fallback `categoricalResult?.verdict?.verdict || analysisResult.verdict?.verdict`, ~lines 1215-1221, and a second occurrence in Simple view ~line 2578)
- **Root cause:** `scoringEngine.js`'s own header documents that its score-to-return correlation is 0.011 ("essentially zero") — this is why the Categorical Assessment system replaced it in Day 44. But `determineVerdict()` is still defined, still computes a BUY/HOLD/AVOID from the old 75-point score, and the Verdict Card still has a fallback path that would display it if `categoricalResult` were ever falsy — with **no visual indication to the user which verdict system produced the answer** if that fallback ever fires.
- **Action:** First confirm whether the fallback is genuinely reachable (trace whether `categoricalResult` can be null/undefined at the point the Verdict Card renders, given it's set synchronously in the same success path per `App.jsx` ~lines 363-387). If unreachable, delete the fallback expression entirely (dead code). If reachable in some edge case, either fix that edge case so `categoricalResult` is always set, or — if keeping a fallback is genuinely necessary — rename `determineVerdict()`'s output and label it visibly as "(legacy scoring, low reliability)" wherever it could appear, so it can never be silently mistaken for the real verdict.
- **Acceptance:** Grep confirms no code path can render an unlabeled legacy-system verdict as if it were the categorical verdict.

### B4. RS Card's "RS Rating" row is a relabeled duplicate, not a real percentile
- **Status:** ✅ DONE (Day 83) — relabeled to "RS Rating (scaled, not a percentile)" with an explanatory tooltip (chose relabel over delete, to preserve the visible info). Also unified the RS vs S&P 500 row's color and value to both key off `rs52Week` (was `rsRatio` for color, `rs52Week` for value). Verified live on AAPL: value unchanged (1.23), label updated, zero console errors.
- **Files:** `frontend/src/utils/rsCalculator.js` (lines ~97-100, has its own comment admitting: `// simplified version - ideally would be percentile vs all stocks`), `frontend/src/App.jsx` (RS Card, ~lines 1333-1368)
- **Root cause:** The "RS Rating" row shown is `(rs52Week - 0.5) * 80 + 10` — a linear rescale of the exact same `rs52Week` ratio shown one row above as "RS vs S&P 500." It's presented like an IBD-style percentile rank (1-99, vs all stocks) but is mathematically just the ratio in different units.
- **Action:** Either delete the "RS Rating" row (it adds no information beyond the ratio row above it) or relabel it clearly, e.g. "RS Rating (scaled ratio, not a percentile vs. market)" so it's not mistaken for something it isn't.
- **Also found in the same card:** the color at ~line 1339 keys off `rsData?.rsRatio` while the displayed value at ~line 1340 prefers `rs52Week` — they're aliased to the same number in `scoringEngine.js` (~lines 593-594) so there's no visible bug today, but it's fragile; consider using one name consistently.
- **Acceptance:** Row either removed or its label makes clear it's not an independent metric.

### B5. Categorical Assessment's 4 tile blocks are copy-paste
- **Status:** ✅ DONE (Day 83) — new `AssessmentTile.jsx` + shared `getAssessmentColor(assessment, variant)`. Deliberately did NOT force one color scheme on all 4 — Sentiment's 'Neutral' is intentionally gray (de-emphasized, informational-only per Day 70), Risk/Macro's 'Neutral' is intentionally yellow (an actual caution signal); `variant` preserves both. What WAS fixed: Technical's tile had no N/A/Unknown branch at all (unlike Fundamental's) — all "standard"-variant tiles now handle it the same way. Also applied the same shared color function to the 3 duplicate header-badge locations. Verified live: all 4 tiles render, clicking Technical correctly expands its detail panel, zero console errors.
- **Files:** `frontend/src/App.jsx`, Assessment Breakdown tiles (Technical/Fundamental/Sentiment/Risk-Macro), was ~lines 2167-2235 pre-audit
- **Action:** Extract a shared `<AssessmentTile category={...} assessment={...} reasons={...} />` component and a single `assessmentColor(level)` helper (the audit found the 'N/A' color case handled inconsistently between tiles — e.g. one tile guards it, the pre-existing Verdict Card grade-chip logic elsewhere does not — a shared helper fixes this for free).
- **Acceptance:** All 4 tiles render identically to before for a range of Strong/Decent/Weak/N/A combinations.

### B6. `live_signals.py` has a dormant Canadian-ticker landmine
- **Status:** ✅ DONE (Day 83) — now captures `is_canadian` from `build_best_query()`'s return instead of discarding it and hardcoding `False`. Verified directly: `market_index='all'` still resolves `is_canadian=False` (unchanged default behavior), `market_index='tsx60'` now correctly resolves `True` (previously impossible), and `get_momentum_signals()` still runs end-to-end without error.
- **Severity:** Low (dormant — only matters if/when Canadian tickers are scanned by the automated engine, which they currently are not by default)
- **Files:** `backend/paper_trading/live_signals.py`, line ~111 (`get_momentum_signals()` hardcodes `is_canadian=False` when calling `scan_queries.parse_candidates()`, regardless of what `market_index` was actually passed in)
- **Action:** Derive `is_canadian` the same way `scan_queries.build_best_query()` internally does (check `market_index in CANADIAN_MARKETS`), rather than hardcoding `False`.
- **Acceptance:** If the automated engine is ever pointed at a Canadian market_index, confirm `.TO` suffixes get correctly appended rather than every downstream OHLCV fetch failing.

---

## Group C — Dead code removal

**Status:** ✅ DONE (Day 83) — every item below removed, each re-verified via grep for zero references immediately before deletion (per Golden Rule 3, not taken on the original audit's word). Confirmed via brace/paren balance checks + full regression (AAPL/JPM/ABBV, zero console errors) after removal.

All verified via grep (no other references found) before listing here, but re-verify at execution time per Golden Rule 3:

- `frontend/src/App.jsx`: `getVerdictColor` (~line 568), `getScoreColor` (~line 578) — defined, never called.
- `frontend/src/App.jsx`: Trade Setup Card's viability IIFE (~line 1380) destructures `pullbackRRValue, momentumRRValue, pullbackViable, momentumViable, nearestSupport` — unused (only `anyViable` and the badge fields are read). Note: this destructuring may naturally disappear as part of Task A2's refactor — check before doing this as a separate cleanup.
- `frontend/src/App.jsx`: commented-out `calculateRelativeStrength` import (~line 63) and commented-out call (~lines 353-354) — delete, git history preserves it.
- `frontend/src/utils/priceStructureNarrative.js`: unused `const key` in `getTouches()` (~line 35) — already noted under A3, fold together.
- `frontend/src/utils/rsCalculator.js`: four exports never imported anywhere — `checkRSQualityGate`, `formatRS`, `getRSColor`, `getRSTrendIcon` (lines ~283-353). Confirm zero external imports, then delete.
- `frontend/src/utils/scoringEngine.js` + `frontend/src/utils/rsCalculator.js`: strip or gate behind a `DEBUG` flag — a ~15-line `console.log` dump on every single analysis in `scoringEngine.js` (~lines 541-559), plus roughly 22 more `console.log` lines spread across `rsCalculator.js`. Production noise, not itself a bug, but worth a pass.

**Note:** `determineVerdict()` in `scoringEngine.js` (Task B3) and the BottomLine-adjacent `generateActionableRecommendation` in `App.jsx` (already known-unused per an eslint warning, confirmed dead when BottomLineCard was removed Day 82) are related but tracked under B3, not here — B3 needs a decision (delete vs. relabel), not a blind deletion.

---

## Group D — New capability: Tradier provider

### D1. Build `TradierProvider` for OHLCV + quote resilience
- **Status:** ✅ DONE (Day 83) — `backend/providers/tradier_provider.py` built per the spec below, wired as the last entry in both `_ohlcv_chain` and `_quote_chain`. **Verified with forced-failover tests** (TwelveData + yfinance monkey-patched to raise, without touching real credentials): OHLCV chain correctly fell through to Tradier and returned 20 real bars for an uncached ticker (WING); quote chain correctly fell through to Tradier for `get_quote('VIX')` (16.28, matching a direct-provider-call sanity check). `get_provider_status()` reports the new `tradier` entry correctly (configured/health/role). Backend auto-reloaded cleanly, `/api/health` stayed green throughout (v2.38).
- **Priority reasoning:** This is a reliability fix (filling the gap Stooq's death left, plus a 3rd VIX/quote source), which is compatible with STA's feature freeze — unlike options-chain integration, which is a new feature and belongs to OptionsIQ's build stage, not STA. Do options integration separately, later, and probably in the OptionsIQ repo, not here.
- **Files:** New `backend/providers/tradier_provider.py`, modify `backend/providers/orchestrator.py` (chains at `__init__`, was ~lines 73-88 pre-audit), `backend/providers/rate_limiter.py` (`PROVIDER_LIMITS` dict, add a `tradier` entry)
- **Verified facts to build against** (from the Day 82 Tradier evaluation, 12 live API calls made):
  - The configured `TRADIER_ACCESS_TOKEN` in `backend/.env` is a **production brokerage token** (confirmed: works against `api.tradier.com`, not just `sandbox.tradier.com`; `/v1/user/profile` returned a real active margin account). Rate limit observed: 120 requests/min on market-data endpoints.
  - **OHLCV** (`GET /v1/markets/history?symbol={t}&interval=daily&start=...&end=...`): tested with AAPL, returned 2,896 daily rows spanning 2015-2026 in one call, no gaps. **Important caveat to document in the provider's docstring: split-adjusted but NOT dividend-adjusted.** Acceptable for a last-resort fallback provider, not for anything that needs to match a dividend-adjusted primary source exactly.
  - **Quotes** (`GET /v1/markets/quotes?symbols={t}`): includes bid/ask/volume/52wk-high/low. **VIX works as the plain symbol `VIX`** (not `$VIX.X`, which is unmatched) — same symbol-stripping convention `finnhub_provider.py` already uses for `^VIX` → `VIX`, reuse that pattern.
  - **Fundamentals** (`/beta/markets/fundamentals/*`): explicitly Tradier's "beta" tier, many null fields. Has `ROE`/`ROA`/`debt_equity`/`P/E`/`P/B` but **confirmed absent: `roic`, revenueGrowth, epsGrowth, margins, marketCap** — do not build on this endpoint, it doesn't fix the gaps STA actually has (AlphaVantage's growth-metrics role stays load-bearing).
  - **Options** (`/v1/markets/options/*`): full chains with Greeks (delta/gamma/theta/vega/rho), open interest, IV — confirmed working, out to Dec 2028 expirations. Real capability, but out of scope for this task (belongs to a separate, later, options-specific task — likely in OptionsIQ, not here).
- **Action:**
  1. Create `TradierProvider(OHLCVProvider, QuoteProvider)` in `backend/providers/tradier_provider.py`, modeled directly on `backend/providers/finnhub_provider.py` (the audit's recommended template for this codebase's conventions: circuit breaker via `get_breaker('tradier')` with `record_success()`/`record_failure()`, `check_rate_limit('tradier')`, `_handle_http_errors()` mapping 429→`RateLimitError`/401,403→`AuthenticationError`/5xx→`ProviderUnavailableError`, `_check_availability()` raising `AuthenticationError` if `TRADIER_ACCESS_TOKEN` is unset).
  2. `get_ohlcv(ticker, period='2y')`: call the history endpoint, map the `history.day` list to a lowercase-column DataFrame with a DatetimeIndex, return `OHLCVResult`. Handle the single-bar edge case where Tradier returns a dict instead of a list for one day of data. Raise `DataNotFoundError` if `history` is null.
  3. `get_quote(ticker)`: call the quotes endpoint, strip `^` prefix same as `finnhub_provider.py` does, map `last`→price and `prevclose`→previous_close, raise `DataNotFoundError` if the symbol comes back in `unmatched_symbols`.
  4. Send `Authorization: Bearer {token}` and `Accept: application/json` headers on every request (Tradier defaults to XML without the Accept header).
  5. Add `'tradier': {'rate_per_minute': 100, 'daily_limit': 0}` to `rate_limiter.py`'s `PROVIDER_LIMITS` (100/min as a conservative margin under the observed 120/min ceiling).
  6. Wire into `orchestrator.py`: append to `_ohlcv_chain` (after yfinance, replacing Stooq's old last-resort slot) and `_quote_chain` (after Finnhub). Add a `tradier` entry to `get_provider_status()`'s providers dict (role: "OHLCV last resort + quote fallback").
- **Acceptance:** With Stooq still absent from the active chain (per Day 82's earlier fix), confirm a forced TwelveData+yfinance failure now falls through to Tradier and returns real data (test by temporarily breaking the first two providers' circuit breakers or mocking their failure, not by actually degrading production credentials). Confirm `get_quote('VIX')` works end to end through the orchestrator.
- **Explicitly out of scope for this task:** any options-data endpoint, any fundamentals endpoint. Do not expand scope here even though the audit found those work — that's separate, larger, feature-freeze-relevant work.

---

## Group E — Minor polish (do opportunistically, low individual priority)

- **E1. ✅ DONE (Day 83).** Added a loading skeleton (`breakoutLoading` state, mirrors `MRSignalCard`'s `loading` prop pattern), matched neighbor styling (`p-6`/`text-lg`, was `p-4`/`text-sm`), surfaced `breakoutLevel` and the `warnings` object (previously fetched but silently dropped — now shown as red badges, e.g. verified live on SMCI: "Failed Breakout" + "Rejection Candle"), removed the double-margin `mb-4`. Loading skeleton verified via an artificially-delayed API route (Playwright route interception) — confirmed it shows during the delay and clears once data arrives.
- **E2. ✅ DONE (Day 83).** Added `latestTickerRequestRef` (a `useRef`, set synchronously at the start of every `analyzeStock()` call); both `fetchMRSignal()` and `fetchBreakout()`'s `.then()`/`.catch()`/`.finally()` callbacks now check it still matches their own `targetTicker` before calling any setter.
- **E3. ✅ DONE (Day 83).** Added `scanRequestIdRef` (incremented once per `runScan()` call); `loadBreakoutBadges()` now takes the scan's id and checks it still matches the ref's current value before calling `setBreakoutBadges`/`setBreakoutBadgesLoading`.
- **E4. ✅ DONE (Day 83).** Added a footer note ("Breakout status checked for top 20 results only.") shown when `filteredCandidates.length > 20`. Verified live with a 45-result momentum scan.
- **E5.** Left as-is per the plan's own assessment (not a real performance problem at this scale) — not touched.
- **E6.** Left as-is per the plan's own assessment (low priority, not worth a dedicated task) — not touched.

---

## Explicitly NOT recommended by the audits (for context, don't "fix" these)

- Categorical Assessment's "Why This Verdict?" footer restating the top verdict — judged acceptable *inside* an explanation card (unlike Bottom Line Card's standalone re-statement, which was removed).
- Trade Setup's and Price Structure's overlapping S/R level lists — flagged as a real overlap worth *considering* consolidating, but not a clear-cut bug; no action item created, revisit only if doing a larger Trade-Setup-area pass.
- MRSignalCard.jsx, Technical Indicators, Quality Gates JSX (structure, not the threshold-consistency issue in A4), the scan results table, sector badges, `/api/breakout/batch` — all explicitly rated well-built by the audits. Do not "improve" these without a specific new finding.

---

## Suggested execution order

1. Group A (real bugs) — A1 and A2 first (highest severity), then A3-A6.
2. Group C (dead code) — cheap, low-risk, can interleave with Group A since most items don't overlap files.
3. Group B (DRY cleanup) — B3 (zombie verdict) has the most product-risk if left alone; do it early within the group.
4. Group D (Tradier) — independent of everything else, can be done in parallel/any time.
5. Group E (polish) — opportunistic, no urgency.

Each task above is written to be actionable independently — a session picking up just one task should have everything it needs (files, root cause, concrete action, acceptance criteria) without needing to read this entire document's other sections, though reading the "Corrections" section first is strongly recommended regardless of which task is picked up.
