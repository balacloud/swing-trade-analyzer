# Implementation Plan — Day 112: S&R `_pivot_sr` root fix → MTF Confluence → Pattern targets

> **Produced by:** Opus Plan agent, Day 112. To be implemented by Sonnet, per the
> "Opus-plans-then-Sonnet-implements" discipline.
> **Status:** PLAN COMPLETE — 8 open decisions need a human call before implementation starts (see §8).
> **Scope:** display + backtest only. Verified: no live forward-test track depends on S&R (§2).

---

## 1. Findings (verified vs. the original brief)

| Claim | Verdict | Detail |
|---|---|---|
| `_pivot_sr()` keeps extreme, not nearest, levels | **CONFIRMED** | `backend/support_resistance.py:1042-1050` (not 1048-1050). |
| Downstream: `assess_trade_viability()`, both entry panels' R:R, stop-loss suggestion | **CONFIRMED, and larger** | See "extra damage surface". |
| STA has an agglomerative S&R method with touch-count selection | **CONFIRMED, wrong name in brief** | Pipeline is `_detect_zigzag_pivots()` → `_cluster_with_agglom()` → `_score_levels()` → `_agglomerative_sr()` (`support_resistance.py:498-813`). `find_pivot_points()` is an unrelated scipy wrapper in `pattern_detection.py:56` — do not conflate. |
| MTF `mtf_daily_weight`/`mtf_weekly_weight` are dead config | **CONFIRMED** | Zero references outside their definition at `support_resistance.py:70-71`. |
| MTF confidence is a hardcoded binary multiplier | **CONFIRMED, and worse — the field is DEAD** | `_find_mtf_confluence()` sets `'strength': 1.0 if is_confluent else 0.6` (`:903`). `.strength` has ZERO readers in `frontend/src` or `backend.py`. Computed, serialized, shipped to browser, read by nobody. |
| Pattern price target is in `backend/pattern_detection.py` | **FALSE — brief's file pointer is wrong** | `pattern_detection.py` has NO target computation. The flat multiplier lives in the **frontend**: `frontend/src/utils/categoricalAssessment.js:61-89` (`buildActionablePattern`, `targetPrice = pivotPrice * targetMultiplier`), with 1.15 (VCP) / 1.20 (C&H) / 1.12 (Flat Base) hardcoded at call sites 119/135/151. Changes Fix 3's design — see §5. |
| Pattern recognition itself is fine | **CONFIRMED** | `detect_vcp`/`detect_cup_handle`/`detect_flat_base` already compute all depth data a measured move needs. |
| Path B retired this session; `check_sr_gate()` no longer called | **CONFIRMED** | See §2. |
| Backtest Config C gate computes R:R from real S&R | **CONFIRMED** | `backend/backtest/backtest_holistic.py:423-470`. |

### Extra damage surface the audit didn't name

**(a) Truncation happens BEFORE the support/resistance split.** `_pivot_sr` returns raw `highs`/`lows`; `compute_sr_levels:1286-1287` splits around price afterward. So `highs[-5:]` = the 5 highest pivot highs in the whole window; `lows[:5]` = the 5 lowest. Any pivot high between current price and the 5th-highest is **deleted before anyone can see it** — nearest resistance is structurally unrepresentable, not just "a far level."

Live proof (`backend/backend.log`, PYPL):
```
All Support: [38.22, 40.2, 41.65, 42.79, 43.19] | Actionable: [43.19]
All Resistance: [63.53, 69.7, 70.09, 76.68, 78.53] | Actionable: [63.53, 69.7]
Entry: 43.19, Stop: 39.25, Target: 63.53
```
Five supports at the bottom of the 2-year range (one survives the 20% proximity filter); five resistances at the top. Every R:R built on `Target = 63.53` is overstated.

**(b) The bug silently rewires which S&R method runs.** `compute_sr_levels:1311` falls through to agglomerative when no pivot support is within 20%. The bug keeps the deepest lows, so that gate fails constantly. Measured over 1,071 real requests: **854 agglomerative / 217 pivot ≈ 80/20**. Fixing the bug **flips a large share of tickers back to pivot** — that, not the level values alone, is the real magnitude of the change, in both UI and backtest.

**(c) `meta["level_scores"]` only exists on the agglomerative path** (`:801`). The Price Structure card's touch counts (`priceStructureNarrative.js:32-40`, via `backend.py:1748`) come from it. If Fix 1 makes pivot win more often without adding touch scoring, **touch counts silently vanish from Price Structure** for those tickers. Mandatory part of Fix 1.

**(d) `assess_trade_viability()` reads the UNFILTERED levels** (`:1318-1320`, `max(support)` on the raw list) while the API filter (`backend.py:1668-1674`) and `riskRewardCalc.js:23` use the filtered list. That divergence is what `hasViabilityContradiction()` (`riskRewardCalc.js:71-78`) papers over. Fix 1 should reduce that contradiction's firing rate — a verification signal.

### Two new bugs found while tracing (not in any Known Issues doc)

**BUG-A — `confluence_map` key-format mismatch kills the ★ confluence badge (~10% of levels).** Backend emits `str(round(k, 2))` (`:1014`) → `str(round(227.50, 2))` == `'227.5'`, `str(round(100.0, 2))` == `'100.0'`. `App.jsx:2041-2044` / `2065-2068` look up with `level.toFixed(2)` → `'227.50'` / `'100.00'`. Never matches for any level whose hundredths digit is 0. `priceStructureNarrative.js` is immune (uses a `parseFloat` tolerance scan) → same data renders confluent in one card, non-confluent in the other. GR30/47 shape. Belongs in Fix 2.

**BUG-B — Price Structure "key levels" shows the FARTHEST supports.** `priceStructureNarrative.js:116-138` docstring says "nearest first"; `addLevels` does `(prices||[]).slice(0,2)`. Support arrays are ascending → `slice(0,2)` = two lowest supports. Resistance is correct. `App.jsx:2042` sorts descending → the two cards disagree. GR53 recurring verbatim in the frontend. One-line fix.

---

## 2. Caller-graph + live-track safety (Golden Rule 54)

**Every importer of `support_resistance`:**
| File | Calls | Impact |
|---|---|---|
| `backend.py:130,1587` | `compute_sr_levels(df)` for `/api/sr/<ticker>` | Display only |
| `backtest/backtest_holistic.py:57,428` | `compute_sr_levels(df_lower)` in `check_entry_signals()` Config C/D/E gate | **Backtest — §3** |
| `paper_trading/live_signals.py:45,165` | imported, used only inside `check_sr_gate()` | **Now dead** |
| `market_structure_engine.py` | comments only; docstring says it deliberately does NOT reuse `_detect_zigzag_pivots()` | None |

**`check_sr_gate()` call sites:** grep returns 4 hits in `live_signals.py` — 3 comments + the `def`. **Zero call sites.** `git diff` confirms this session's uncommitted edit removed the call and the `B_revised_rr` gate append, narrowed the pre-filter to `A_frozen` only. Retirement is real, **in the working tree, not yet committed.**

**Four live forward-test tracks:**
| Track | Entry gate | Uses S&R? |
|---|---|---|
| Momentum Path A (`A_frozen`) | `compute_entry_levels()` flat/ATR proxy, `rr_a >= MIN_RR` | **No** |
| Momentum Path B (`B_revised_rr`) | `check_sr_gate()` — retired Day 112, no longer called | **No (dead)** |
| MR broad | `detect_mr_signal()`, RSI(2) | **No** |
| MR HUB-65 | same MR gate, different universe | **No** |

Exit management reads `initial_stop_price`/`initial_target_price` stored at entry (GR29), never S&R. Path B's 67 open + 15 pending wind down untouched.

`pattern_detection` importers: `backend.py:148` (display), `backtest_holistic.py:56`, `parameter_stability.py:121`, `live_signals.py:43` — which uses only `check_trend_template()`, never `detect_patterns()`.

### 🔒 Verdict
**No live forward-test track depends on `_pivot_sr`, `compute_sr_levels`, `assess_trade_viability`, or `detect_patterns`. No live-count reset. GR18 does not bite the forward tests.** This is a **display + backtest** fix. The only frozen-numbers exposure is the historical Config C backtest baseline (§3).

**Two caveats Sonnet must carry:**
1. `check_sr_gate()` is left intact for a possible future corrected-S&R parallel run. Fix 1 silently changes its behavior even though it's dead. Add a comment above it recording it was last validated against pre-fix `_pivot_sr`.
2. The Path B retirement is uncommitted. Confirm it's still in the tree (or committed) before relying on this verdict.

---

## 3. Fix 1 — S&R `_pivot_sr()` (the root fix)

### Alternatives weighed
- **Option A — fix in place with proximity-aware selection.** Split around price inside `_pivot_sr`, keep N nearest per side. Smallest diff; preserves `method:"pivot"` as an auditable path; trivially A/B-testable behind a flag; directly satisfies GR53. Must handle the spacing trap + add touch scoring.
- **Option B — delete `_pivot_sr`, defer to agglomerative.** One code path; agglomerative already does proximity-correct selection + touch filtering + serves ~80% of traffic. But: strictly larger backtest delta with no way to isolate cause; agglomerative's own magic numbers (`zigzag_percent_delta=0.05`, `merge_percent=0.02`) become load-bearing for 100% of traffic, un-A/B-tested; its `<2 pivots → KMeans → volume_profile` bail drops quiet names pivot currently catches.
- **Option C — hybrid: `_pivot_sr` generates levels, adopt agglomerative's merge + touch-score post-processing.**

### ✅ Recommendation: Option A executed as Option C — fix in place, reuse the agglomerative helpers (`_score_levels` already exists and is exactly the "touch-count logic" `KNOWN_ISSUES_DAY111.md:89` asked for), behind a feature flag so the backtest A/B is a same-commit comparison. Option B stays as a follow-up **if** the A/B shows corrected pivot still underperforms — decided from the result, not before it.

### Exact changes — `backend/support_resistance.py`

**1a. `SRConfig` (47-75)** — add, following the `use_agglomerative`/`use_mtf` convention:
```
pivot_nearest_selection: bool = True   # Day 112 / GR53: N nearest-to-price, not N most extreme. False = pre-Day-112.
touch_saturation: int = 5              # used by Fix 2
```
**Do NOT change `pivot_max_levels` (5) or `pivot_min_spacing_frac` (0.0025)** — tuning either while fixing a correctness bug is exactly the GR18/20 re-tune that's forbidden.

**1b. `_pivot_sr()` (1026-1071)** — after `highs`/`lows` built + de-duped (1042-1043), before the slice at 1048-1050:
- `price = float(df["close"].iloc[-1])`
- `res_pool = sorted(h for h in highs if h > price)`, `sup_pool = sorted(l for l in lows if l <= price)`
- **Merge, don't reject, on min spacing.** ⚠️ TRAP: the existing check (1052-1060) does `np.diff` over selected levels and returns `None` (abandons pivot entirely) if any gap < 0.25% of price. Under proximity selection the survivors cluster near price → gaps tighten → this fires far more, silently sending everything to agglomerative and making the fix a partial no-op. Replace with a greedy merge walking outward from price, keeping a candidate only if ≥ `price * pivot_min_spacing_frac` from the last kept level; on collision keep the higher touch count.
- `res_sel = merged_res[:pivot_max_levels]` (nearest above), `sup_sel = merged_sup[-pivot_max_levels:]` (nearest below)
- Gate on `cfg.pivot_nearest_selection`; `else:` = existing 1048-1060 verbatim.
- Return `res_sel, sup_sel, meta`. `compute_sr_levels:1286-1287` re-splits around price → now idempotent → no change needed there.

**1c. Touch scoring on the pivot path** — after selection:
```
scored = _score_levels(res_sel + sup_sel, df, cfg.touch_threshold)
meta["level_scores"] = {f"{round(l, 2):.2f}": s for l, s in scored}
```
Zero-padded 2-decimal keys. Apply the identical format to `_agglomerative_sr:801` and `_enrich_with_mtf:1014`'s `confluence_map` keys — one convention across all three maps.
Also add `meta["selection"] = "nearest" | "extreme"`.

**1d. `backend.py:1730-1760`** — add `'selection': sr_levels.meta.get('selection')` to the meta passthrough so it's visible in the API response.

**File: `frontend/src/utils/priceStructureNarrative.js`**
**1e. BUG-B** — in `addLevels` (~119): support `[...prices].sort((a,b)=>b-a).slice(0,2)`; resistance stays `slice(0,2)`. Fix the JSDoc.

### Backtest re-baseline
**(a) Routes through `_pivot_sr`? YES** — `backtest_holistic.py:428` calls `compute_sr_levels(df_lower)` with no `cfg` → default `SRConfig` → pivot branch first.
**(b) Re-run mandatory.** Config C gate (`:437-470`) reads `max(support)` / `min(resistance)` and `meta['trade_viability']['viable']` — both change. **Pre-registered directional prediction:** trade count should RISE (the bug pushed `support_distance_pct` > 20% → `viable="NO"` → gate fail). PF direction genuinely unknown.
**Command sequence** (GR45: seed=42 no longer reproduces Day 79 — do NOT compare to PF 1.40):
```bash
cd backend && source venv/bin/activate
# 0. smoke — measure runtime
python backtest/backtest_survivorship_free.py --sample-size 30 --seed 42
# 1. BASELINE on pre-fix code, FREEZE meta['universe'] from the output JSON as the shared list
python backtest/backtest_survivorship_free.py --sample-size 400 --seed 42
# 2. after Fix 1, re-run Config C ONLY on the FROZEN universe
python backtest/backtest_holistic.py --tickers $(<frozen_universe.txt) \
       --configs C --periods standard --scan-interval 2 --start 2020-01-01 --end 2025-12-31
```
Passing `--tickers` (not re-deriving from seed) guarantees comparability. MR unaffected, not re-run. Optional 3rd run with `pivot_nearest_selection=False` post-fix to prove the flag is a true no-op (GR21).
**(c) Framing:** NOT a GR18 violation — no threshold moves, it's a correctness fix to a mis-named primitive (GR53), decided before any result. GR20 obligation: run once, accept the answer, do NOT iterate on `pivot_max_levels`/spacing afterward.
**Docs updated:** ROADMAP.md canonical-numbers table (add a Day 112 row, keep the 1.40 row + a GR45 note); new `SR_PIVOT_FIX_REBASELINE_DAY112.md` (both runs, frozen universe, prediction, result); `KNOWN_ISSUES_DAY112.md` (close GR53); `PROJECT_STATUS_DAY112_SHORT.md`; `ANALYZE_PAGE_REDESIGN_DECISIONS.md` items 7/8.

### Phasing
1. Baseline backtest run (before any code). 2. `SRConfig` flag. 3. `_pivot_sr` proximity + merge + `_score_levels` + `meta["selection"]`. 4. Unify the 3 level-key formats. 5. `backend.py` meta passthrough. 6. `priceStructureNarrative.js` BUG-B. 7. 3-pass review. 8. Live browser verify. 9. Backtest re-run + re-baseline docs.

---

## 4. Fix 2 — MTF Confluence confidence score

### Decision: wire the weights into a real graduated score AND surface it — do NOT delete.
Deleting the config tidies nothing user-visible — the `confluence_pct` badge (`App.jsx:2023-2033`, 40%/20% thresholds) stays binary-derived and still counts synthetic ATR/Fib levels in its denominator. Depends on Fix 1: the graduated score's daily term is touch counts, which only exist on the agglomerative path today (finding (c)); Fix 1 step 1c is the enabler. Build after Fix 1.

### Exact changes — `backend/support_resistance.py`
**2a. `_find_mtf_confluence()` (858-906)** — new signature accepting `cfg`, `daily_scores`, `weekly_scores`. Keep every existing key (`confluent`, `weekly_match`, `distance_pct`). Add:
- `proximity` = `1 - (pct_distance / threshold)` clamped `[0,1]` — graduated, no hard step at 1.5%.
- `strength` = `cfg.mtf_daily_weight * norm(daily_touches) + cfg.mtf_weekly_weight * norm(weekly_touches) * proximity`, `norm(t) = min(t, cfg.touch_saturation) / cfg.touch_saturation`. **Fixed saturation, NOT max-in-set** — otherwise a level's score swings day to day as another level gains a touch (the "plausible but wrong" answer GR41 Pass 3 catches). New formula's endpoints reproduce the old 0.6/1.0 exactly; everything between becomes real.
- `strength_label` = banded `Strong|Moderate|Weak`. Surface the LABEL in UI (redesign wants descriptive states), keep the float in `meta`.

**2b. `_enrich_with_mtf()` (973-1023)** — `_score_levels()` on daily (or reuse `meta["level_scores"]` from Fix 1) + weekly frames, pass both through. Emit `confluence_map` keys as `f"{round(k,2):.2f}"` (BUG-A).

**2c. Exclude projected levels from the denominator.** `_enrich_with_mtf` is called after `_smart_project_resistance()`/`_project_support_levels()` inject synthetic levels — these can't be confluent with real weekly pivots, so they drag `confluence_pct` down and make the 40%/20% thresholds meaningless for ATH stocks. Pass `meta["resistance_projected"]`/`meta["support_projected"]` in, skip projected side from `confluence_map`, add `projected_excluded: <n>` (GR44 — don't collapse distinct reasons).

**2d. `_compute_weekly_sr()` (909-970)** — note for review: applies NO `min_touches_for_level` filter, so a weekly "level" can be single-touch. Decide explicitly whether to filter; record the decision.

### Frontend
**2e. BUG-A** — `App.jsx:2041-2044` / `2065-2068`: once 2b emits zero-padded keys, `toFixed(2)` matches. Belt-and-braces: export one shared `findLevelMeta(level, map)` tolerance helper (the `parseFloat` scan written twice in `priceStructureNarrative.js`) and use it in all four places (Architecture Rule 7).
**2f.** Render `strength_label` on the ★ tooltip / Weekly Levels section. Keep the `confluence_pct` badge; its denominator is now honest.

---

## 5. Fix 3 — Pattern price target

The flat multiplier is `frontend/src/utils/categoricalAssessment.js:66` in `buildActionablePattern`, multiplier from call sites 119/135/151. Consumers: `App.jsx:482` → `2270` (`targetPrice`), `2285` (`riskReward`), `496` (feeds pattern list into `generatePriceStructure`).

### Placement: frontend-only, all three targets, inside `buildActionablePattern`.
Rejected: backend `price_target` field — safe (additive keys can't touch gating; `api.js:699-703` passes objects through so GR30 is automatic) but edits a backtest-imported module for a value no backend consumer needs, and splits VCP (needs `srData`, frontend-only) from its siblings. Frontend-only = one place, zero backtest surface.

### 3a — Cup & Handle + Flat Base (INDEPENDENT of Fix 1, ship first)
| Pattern | Inputs (already in payload) | New target |
|---|---|---|
| Cup & Handle | `cup.left_lip_price`, `cup.bottom_price`, `pivot_price` (`pattern_detection.py:615-635`) | `pivot_price + (cup.left_lip_price - cup.bottom_price)` — O'Neil's rule |
| Flat Base | `base.high`, `base.low`, `pivot_price` (== `base.high`) (`:747-774`) | `base.high + (base.high - base.low)` |

In `buildActionablePattern`: replace `targetMultiplier` with a caller-supplied `targetPrice` (or `computeTarget` callback) + `targetBasis` string (`cup_depth`/`base_depth`).
**Null discipline (Architecture Rule 6):** missing depth fields → `targetPrice: null`, `riskReward: null`, `targetBasis: null`. Do NOT fall back to the old multiplier. Handle nulls at `App.jsx:2270` (add `—` branch) and `2285` (guard `R:R {riskReward}:1` → would render `R:R null:1`).
Expected: tight 8% flat base → target moves DOWN (8% not 12%); 30% cup → UP (~30% not 20%). Both correct — flag so it's not read as regression.
Also update `ANALYZE_PAGE_REDESIGN_DECISIONS.md` §11's "Caveat (Pattern Detection only)" (~line 419) — resolved by this fix.

### 3b — VCP (AFTER Fix 1)
No published measured move (Minervini uses trailing stops/R-multiples). Honest target is structural:
1. **Primary:** nearest real resistance above the pivot, from corrected S&R — `basis: 'resistance'`.
2. **Fallback:** no resistance above pivot within 30% (`RESISTANCE_PROXIMITY_PCT`) → largest contraction's measured move, `pivot_price + (contractions[0].high_price - contractions[0].low_price)` from `vcp.contractions[]` (`pattern_detection.py:355-361`) — `basis: 'base_depth'`.
3. **Neither:** `null`, UI says "no structural target" — never a flat percentage.
Plumbing: `App.jsx:482` has `srData` in scope. `getActionablePatterns(data.patterns, atr)` → `(data.patterns, atr, srData)`, thread into `buildActionablePattern`. Check `srData.meta.resistanceProjected` — synthetic resistance routes to fallback, not presented as "next resistance." Surface `targetBasis` as a caption (`Target = next resistance $X` / `Target = pivot + base depth`).

### 3c — optional follow-on, do NOT bundle
Cap C&H / Flat Base moves at nearest real resistance. Deferred — would make 3a depend on Fix 1 and kill its independence. Log, don't build.

---

## 6. Implementation order

```
Phase 0  Pre-work, no code
         · Re-confirm Path B retirement still in tree (§2)
         · Run BASELINE backtest, freeze the universe list   ← must precede any edit
         · Capture pre-fix /api/sr/<ticker> JSON for verification tickers

Phase 1  Fix 3a — C&H + Flat Base targets            [frontend only, INDEPENDENT, ships first]
Phase 2  Fix 1 — S&R _pivot_sr                        [THE ROOT FIX]
         config flag → proximity+merge → touch scoring → key-format unify
         → backend.py meta → BUG-B → 3-pass review → live verify → backtest re-run → re-baseline docs
Phase 3  Fix 2 — MTF graduated score                  [DEPENDS ON Phase 2]  (incl. BUG-A + projected-level exclusion)
Phase 4  Fix 3b — VCP target                          [DEPENDS ON Phase 2]
Phase 5  Deferred/logged: Fix 3c cap; Option B if the A/B says so
```
Edges: Phase 2 → 3, Phase 2 → 4. Phase 1 has no edges. 3 and 4 are independent of each other.
**Commits:** Phase 1 / Phase 2 code / Phase 2 backtest+docs / Phase 3 / Phase 4 — five separate. The re-baseline is its own commit so numbers are attributable to one diff.

---

## 7. Verification plan (GR6)

Backend `:5001` + frontend `:3000` both currently running.

### Fix 1 tickers (from real `backend.log`, not guessed)
| Ticker | Method | Why |
|---|---|---|
| PYPL | pivot | Clearest case — supports `[38.22…43.19]` (1 actionable), resistances `[63.53…78.53]` |
| META | pivot | Supports clustered ~519-556; resistances 709-788 |
| TSLA, AVGO | pivot | 2nd/3rd confirmations; AVGO also hits near-ATH/projection branch |
| AAPL, MSFT, GOOGL | agglomerative | **Regression control — must be byte-identical before/after** |
| SOXL | agglomerative | Low-price/high-vol → exercises merge-not-reject + `_is_high_volatility` |
| one `.TO` ticker | — | Canadian tickers work (Day 108), keep in the sweep |

**Method (GR31):** `/api/sr/` not cached but OHLCV is — leave the OHLCV cache alone for the A/B so both runs see identical bars. Diff full JSON before/after: `method`, `selection`, `allSupport`, `allResistance`, `support`, `resistance`, `suggestedEntry/Stop/Target`, `riskReward`, `meta.atr`, `meta.levelScores`, all of `meta.tradeViability`.

**Pass criteria:**
- PYPL/META/TSLA/AVGO: `selection == "nearest"`; ≥1 support and ≥1 resistance strictly between the old extremes and price appears.
- `meta.levelScores` non-empty on the pivot path (finding (c) guard).
- AAPL/MSFT/GOOGL: zero diff.
- No ticker newly returns `method: "kmeans"`/`"volume_profile"` — that means the merge over-rejects.
- Sweep 20-30 tickers, log method distribution vs. the historical 854/217; a large pivot-share increase is EXPECTED.

**Browser (Analyze, PYPL):** both entry panels' R:R + "R:R Context" line; S&R list levels moved toward price; viability banner (`viable`, distance %, stop suggestion); Price Structure card — touch counts still render, 2 support key-levels are now nearest 2 (BUG-B), matching S&R list top 2; `hasViabilityContradiction()` fires less often; zero console errors.

**Backtest:** paired A/B of §3. Report trade count, WR, PF, Sharpe for both + delta. Compare run 1 vs run 2 only — never vs PF 1.40 (GR45).

### Fix 2
- Real ticker with a `.X0` level (`$227.50`, `$100.00`) that IS confluent → confirm ★ now renders in `App.jsx` where it didn't (BUG-A's direct proof, demonstrated not asserted).
- Ticker with `meta.resistanceProjected == true` → `confluence_pct` rises, `projected_excluded > 0`.
- `strength` varies continuously (not just 0.6/1.0); heavily-touched confluent ≈ 1.0, light non-confluent well under 0.6.
- ★ state agrees between S&R list and Price Structure key-levels for the same level.

### Fix 3
- Do NOT assume a ticker has a pattern. Sweep `/api/patterns/<ticker>` across the Scan tab / Master Framework watchlist, collect names with `cup_handle.detected`/`flat_base.detected` true and `confidence >= 60`.
- Hand-check arithmetic to the cent against the payload.
- Verify the target MOVED from the old flat multiple.
- Force the null path — detected pattern missing depth fields → UI shows `—`, not `NaN`/`undefined`/`R:R null:1`.
- VCP: target == nearest post-fix resistance above pivot, `targetBasis == 'resistance'`; then an ATH VCP with no resistance → `base_depth` fallback + caption.

### Three-pass escalating review (GR41) — one full cycle per phase
- **Phase 1 (3a):** P2 → null/NaN paths at `App.jsx:2270/2285`, `belowThreshold` patterns; P3 → does removing `targetMultiplier` orphan any other `buildActionablePattern` caller.
- **Phase 2 (Fix 1):** P2 → spacing-merge trap, `level_scores` regression, `selection=False` true no-op; P3 → method-mix flip vs. anything reading `meta.methodUsed`; `check_sr_gate()`'s now-unvalidated behavior; `market_structure_engine.py` matching note.
- **Phase 3 (Fix 2):** P2 → key-format unification across 3 maps + 2 helpers; P3 → score stability day-over-day (fixed saturation), `_compute_weekly_sr`'s missing touch filter.
- **Phase 4 (3b):** P3 → `resistanceProjected` presenting a synthetic level as a real target.

---

## 8. Open decisions — need a human call before Sonnet starts

1. **🔴 Approve the S&R approach.** Option A/C (fix in place, recommended) vs Option B (retire `_pivot_sr`). Note the framing has CHANGED since `PROJECT_STATUS_DAY111` wrote this as "the single most important open decision" — all three options there were about protecting Path B's count, and Path B is now retired. The decision is materially cheaper now.
2. **🔴 Pre-commit the backtest interpretation before running it.** What if Config C's PF drops below baseline? Recommendation: whatever the number, it becomes the new canonical baseline; Day 79's PF 1.40 is formally retired as un-reproducible (GR45). Write this down before the number exists or the temptation to tune `pivot_max_levels` will be real.
3. **🔴 Start a corrected-S&R forward-test variant, or not?** `live_signals.py:325` anticipates it. Hard prerequisite: a new pre-registered §8c in `PAPER_TRADING_PREREGISTRATION.md` written BEFORE the first signal (GR18). Sonnet must NOT start it as a side-effect. **Default: no.**
4. **🟡 Freeze status.** Forward-testing accumulation is "the sole stated priority." These are display + backtest fixes with zero live-track impact (§2) so they don't violate it — but confirm the session should be spent here.
5. **🟡 MTF: graduated score vs. delete the dead config.** Recommend graduated, surfacing `strength_label` not the raw float. Needs sign-off (adds a number to a card the redesign wants descriptive).
6. **🟡 Scope of the two new bugs.** BUG-A + BUG-B are in-family and cheap. Fold in (recommended — BUG-B *is* GR53 recurring, BUG-A blocks Fix 2 verification) or log separately in `KNOWN_ISSUES_DAY112.md`?
7. **🟢 Backtest runtime unmeasured.** Run `--sample-size 30` smoke first, extrapolate before committing to two full runs.
8. **🟢 `--momentum-only` flag** on `backtest_survivorship_free.py` (mirroring `--mr-only`) halves re-run cost by skipping the MR leg (no S&R change affects it). Additive tooling — confirm it's acceptable.

---

## Critical files for implementation
- `backend/support_resistance.py` — `SRConfig` (47-75), `assess_trade_viability` (380-481), `_score_levels` (664-704), `_find_mtf_confluence` (858-906), `_enrich_with_mtf` (973-1023), **`_pivot_sr` (1026-1071)**, `compute_sr_levels` (1205-1417)
- `frontend/src/utils/categoricalAssessment.js` — `buildActionablePattern` (61-89) + 3 call sites (114-157)
- `frontend/src/utils/priceStructureNarrative.js` — `getTouches` (32-40), `isConfluent` (46-54), `buildKeyLevels` (116-138)
- `backend/backtest/backtest_holistic.py` — `check_entry_signals` Config C/D/E R:R gate (415-470)
- `backend/backend.py` — `/api/sr/<ticker>` proximity filter + response meta (1587, 1662-1760)
- `frontend/src/App.jsx` — pattern target render (2237-2300), S&R + MTF ★ list (2020-2110), viability banner (1699-1740)
