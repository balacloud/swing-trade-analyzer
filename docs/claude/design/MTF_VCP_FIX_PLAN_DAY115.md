# Implementation Plan — MTF Confluence + VCP Target (Phases 3–4 of the S&R fix chain)

> **Status:** Ready to implement. Approach is Opus-authored (`SR_PIVOT_FIX_PLAN_DAY112.md` §4–5,
> written during the S&R `_pivot_sr` fix session); this document re-verifies every file/line
> reference and field name against the **current** codebase (Phase 1–2 shipped since then and
> shifted line numbers) before Sonnet implements — the discipline Golden Rule 55 exists for.
> **Context:** the paper-trading program was discontinued 2026-09-12 (`PAPER_TRADING_PREREGISTRATION.md`).
> Neither fix touches any forward-test track — both are pure Analyze-page display, already
> confirmed freeze-independent in the original plan's Golden Rule 54 check. That's unchanged;
> restated here only because the project's priorities shifted since the original plan was written.
> **Funding context:** this work is intended to use the Fable-5 usage-credit balance
> (expires 2026-09-19) rather than the Pro subscription's weekly quota — noted for the session,
> not something the plan itself depends on.

---

## 1. Re-verification against current code (Day 115)

Everything below was re-read from the live files just before writing this plan — not assumed
from the Day 112 document.

| Claim from the Day 112 plan | Still true? | Current location |
|---|---|---|
| `_find_mtf_confluence()` sets `'strength': 1.0 if is_confluent else 0.6`, unused by any consumer | **Confirmed, unchanged** | `support_resistance.py:865-913` (was 858-906) |
| `mtf_daily_weight`/`mtf_weekly_weight` are dead config | **Confirmed, unchanged** | `SRConfig:77-78` |
| `_enrich_with_mtf()` is called after `resistance_projected`/`support_projected` are already set in `meta`, at every call site | **Confirmed** | 4 call sites: `support_resistance.py:1377, 1423, 1444, 1463` |
| `confluence_map` keys are now zero-padded 2dp (BUG-A) | **Already fixed Day 112** — no longer an open item | `support_resistance.py:1021` |
| `App.jsx` reads `mtfInfo?.confluent` for the ★ badge, never `.strength` | **Confirmed** | `App.jsx:2044-2048` (support), `2067-2071` (resistance) |
| MTF confidence badge thresholds (40%/20%) | **Confirmed, unchanged** | `App.jsx:2026-2028` |
| VCP still on the flat +15% legacy multiplier with a "pending resistance-based fix" caption | **Confirmed — this is what Phase 4 replaces** | `categoricalAssessment.js:113-127` |
| `getActionablePatterns(patternsData, atr = null)` has no `srData` parameter yet | **Confirmed — needs adding** | `categoricalAssessment.js:138` |
| `App.jsx` calls `getActionablePatterns(data.patterns, atr)` right after `setSrData(data.sr)`, with `data.sr` in local scope | **Confirmed** | `App.jsx:477, 482` |
| VCP's `contractions[]` has `high_price`/`low_price`, passed through by `api.js` unchanged (no camelCase rename) | **Confirmed** | `pattern_detection.py:354-358`, `api.js:700` (`vcp: data.patterns.vcp`, whole-object passthrough) |
| `data.sr.resistance` is already the proximity-filtered (actionable) list; `data.sr.allResistance` is the unfiltered one | **Confirmed** | `api.js:396-399` |
| `data.sr.meta.resistanceProjected` is the correct (camelCase) field name for "this resistance is synthetic, not real" | **Confirmed** | `backend.py`'s meta passthrough (`resistance_projected` → `resistanceProjected`) |

**One correction from the original plan:** `_compute_weekly_sr()` (`support_resistance.py:916-977`) resamples to weekly internally via `_resample_to_weekly(df)` but does **not** return the weekly frame — only `(weekly_support, weekly_resistance)`. Phase 3's graduated score needs weekly touch counts, which need the weekly OHLCV frame. The original plan didn't flag this. Fix: `_compute_weekly_sr` has exactly one caller (`_enrich_with_mtf`) — change its return to `(weekly_support, weekly_resistance, weekly_df)` and update that one call site. Avoids a second, duplicate resample call (Golden Rule 7 — DRY).

---

## 2. Fix 1 — MTF Confluence graduated score (Phase 3)

### Decision (unchanged from the Day 112 plan): wire the weights into a real graduated score, exclude projected levels from the denominator. Do not just delete the dead config.

Two independent problems, both real, both fixed in this pass:
1. **The `strength` field is dead** — computed, serialized, read by nobody.
2. **The `confluence_pct` badge lies for ATH/ATL stocks** — `_enrich_with_mtf` is called after synthetic ATR/Fibonacci-projected levels are already mixed into `support`/`resistance`. Those can never be confluent with a real weekly pivot, so they silently drag the percentage down and make the 40%/20% badge thresholds meaningless whenever `resistanceProjected`/`supportProjected` is true.

### Exact changes — `backend/support_resistance.py`

**2a. `_compute_weekly_sr()` (916-977)** — return the weekly frame too:
```python
def _compute_weekly_sr(df, cfg) -> Tuple[List[float], List[float], Optional[pd.DataFrame]]:
    ...
    return weekly_support, weekly_resistance, weekly_df   # was: return weekly_support, weekly_resistance
    # early-return paths (lines ~943, ~958) become: return [], [], None
```

**2b. `_find_mtf_confluence()` (865-913)** — new signature, existing keys unchanged, new keys added:
```python
def _find_mtf_confluence(daily_levels, weekly_levels, threshold, daily_scores=None, weekly_scores=None, cfg=None):
    ...
    for daily_level in daily_levels:
        ... # existing best_match / min_distance logic, unchanged
        proximity = max(0.0, 1 - (min_distance / threshold)) if best_match is not None else 0.0
        daily_touch = (daily_scores or {}).get(daily_level, 0)
        weekly_touch = (weekly_scores or {}).get(best_match, 0) if best_match is not None else 0
        sat = (cfg.touch_saturation if cfg else 5)
        norm_daily = min(daily_touch, sat) / sat
        norm_weekly = min(weekly_touch, sat) / sat
        dw = cfg.mtf_daily_weight if cfg else 0.6
        ww = cfg.mtf_weekly_weight if cfg else 0.4
        strength = dw * norm_daily + ww * norm_weekly * proximity
        confluence_map[daily_level] = {
            'confluent': is_confluent,
            'weekly_match': best_match,
            'distance_pct': round(min_distance * 100, 3) if best_match else None,
            'proximity': round(proximity, 3),
            'strength': round(strength, 3),
            'strength_label': 'Strong' if strength >= 0.75 else 'Moderate' if strength >= 0.45 else 'Weak',
        }
```
**Fixed-saturation normalization is load-bearing** — normalize against `cfg.touch_saturation` (a constant, added Day 112), never against the max touch count *in this level set*. Normalizing against the local max would make a level's score swing day to day purely because a *different* level gained a touch — the "plausible but wrong" failure mode Golden Rule 41's Pass 3 exists to catch. **The new formula's endpoints must reproduce the old constants**: a non-confluent level with zero touches scores `0.6 * 0 = 0` at the floor and approaches `dw = 0.6` as daily touches saturate — matching the old non-confluent constant; a maximally-touched confluent level approaches `dw + ww = 1.0` — matching the old confluent constant. Worth a unit sanity check during Pass 1.

**2c. `_enrich_with_mtf()` (980-1029)** — thread scores through, exclude projected levels from the confluence set (not just the denominator label — from the *set itself*, so a projected level can never appear "non-confluent" when it was never real to begin with):
```python
def _enrich_with_mtf(meta, support, resistance, df, cfg):
    if not cfg.use_mtf:
        return
    try:
        weekly_support, weekly_resistance, weekly_df = _compute_weekly_sr(df, cfg)
        all_daily = support + resistance
        all_weekly = weekly_support + weekly_resistance

        daily_scores = dict(_score_levels(all_daily, df, cfg.touch_threshold)) if all_daily else {}
        weekly_scores = dict(_score_levels(all_weekly, weekly_df, cfg.touch_threshold)) if (all_weekly and weekly_df is not None) else {}

        confluence_map = _find_mtf_confluence(all_daily, all_weekly, cfg.mtf_confluence_threshold, daily_scores, weekly_scores, cfg)

        # Day 115: exclude synthetic (ATR/Fibonacci-projected) levels from the
        # confluence set entirely — they can never be confluent with a real
        # weekly pivot, so counting them in the denominator understates
        # confluence for every ATH/ATL stock (Day 111 finding).
        projected_prices = set()
        if meta.get('resistance_projected'):
            projected_prices.update(resistance)
        if meta.get('support_projected'):
            projected_prices.update(support)
        projected_excluded = len(projected_prices)
        if projected_excluded:
            confluence_map = {k: v for k, v in confluence_map.items() if k not in projected_prices}

        confluent_count = sum(1 for v in confluence_map.values() if v['confluent'])
        meta["mtf"] = {
            "enabled": True,
            "weekly_support": [round(s, 2) for s in weekly_support],
            "weekly_resistance": [round(r, 2) for r in weekly_resistance],
            "confluence_map": {f"{round(k, 2):.2f}": v for k, v in confluence_map.items()},
            "confluent_levels": confluent_count,
            "total_levels": len(confluence_map),
            "confluence_pct": round(confluent_count / len(confluence_map) * 100, 1) if confluence_map else 0,
            "projected_excluded": projected_excluded,   # Day 115 — visible, not silent (Golden Rule 44 shape)
        }
    except Exception as exc:
        logger.warning(f"MTF enrichment failed: {exc}")
```

**2d.** `_compute_weekly_sr` applies no `min_touches_for_level` filter (unlike `_agglomerative_sr`), so a weekly "level" can be a single-touch cluster — noted for the Pass-2 review, not changed in this pass (would be a second, separable decision about weekly level *selection*, not the confluence *scoring* this plan is about).

### Exact changes — `backend/backend.py`
Add `'projected_excluded': sr_levels.meta.get('mtf', {}).get('projected_excluded', 0)` is unnecessary — `meta["mtf"]` is already passed through wholesale at `backend.py`'s `'mtf': sr_levels.meta.get('mtf')` line, so `projected_excluded` and `strength_label` reach the API automatically. No backend.py change needed for this field — verify this assumption in Pass 1 by checking the actual response.

### Exact changes — `frontend/src/App.jsx`
**2e.** Line 2030-2033 (badge): append `, {mtf.projected_excluded} excluded` when `> 0`, so the badge doesn't read as a silent improvement with no explanation:
```jsx
({srData.meta.mtf.confluent_levels}/{srData.meta.mtf.total_levels} levels
{srData.meta.mtf.projected_excluded > 0 && `, ${srData.meta.mtf.projected_excluded} projected excluded`})
```
**2f.** Lines 2044-2048 / 2067-2071 (★ tooltip): add `strength_label` to the existing `title` attribute — `title={mtfInfo?.confluent ? \`Confluent with weekly level (${mtfInfo.strength_label})\` : 'Confluent with weekly level'}`. Surface the **label**, not the raw float — matches the redesign's descriptive-state convention (Regime, Technical Read, Fundamentals all do this already).

---

## 3. Fix 2 — VCP price target (Phase 4)

### Decision (unchanged from the Day 112 plan): frontend-only, three-tier fallback, reusing `data.sr` already in scope at the call site.

### Exact changes — `frontend/src/App.jsx`
**3a.** Line 482: `getActionablePatterns(data.patterns, atr)` → `getActionablePatterns(data.patterns, atr, data.sr)`. **Use the local `data.sr`, not the `srData` state variable** — `setSrData(data.sr)` on line 477 is async; reading `srData` state two lines later inside the same render pass risks the pre-update stale value (React state updates don't apply synchronously). This is a small but real correctness detail the Day 112 plan didn't call out.

### Exact changes — `frontend/src/utils/categoricalAssessment.js`
**3b.** `getActionablePatterns(patternsData, atr = null, srData = null)` — new third parameter, default `null` so every other caller (there are none besides `App.jsx`, verified — `grep getActionablePatterns` shows one call site) degrades gracefully to "no VCP target" rather than throwing.

**3c.** New helper, alongside `measuredMoveTarget`:
```js
/**
 * Day 115 (Phase 4): VCP has no published measured move (Minervini uses
 * trailing stops / R-multiples, not a projection). Honest target is
 * structural: the nearest real resistance above the pivot from the
 * corrected S&R engine (Day 112, Golden Rule 53). Falls back to the
 * largest contraction's depth if no real resistance exists above the pivot
 * within the app's own proximity ceiling. Returns null (never a flat %)
 * if neither is available.
 */
function vcpTarget(vcp, srData) {
  const pivot = vcp?.pivot_price;
  if (pivot == null) return null;

  const resistances = (srData?.resistance || []).filter(r => r > pivot);
  if (resistances.length > 0 && !srData?.meta?.resistanceProjected) {
    return { price: Math.min(...resistances), basis: 'resistance' };
  }

  const firstContraction = vcp?.contractions?.[0];
  const hi = firstContraction?.high_price, lo = firstContraction?.low_price;
  if (hi != null && lo != null && hi > lo) {
    return { price: pivot + (hi - lo), basis: 'vcp_contraction' };
  }

  return null;
}
```
Note the `!srData?.meta?.resistanceProjected` guard — if the *whole ticker* is flagged ATH (ATR/Fibonacci-projected resistance), even a level that happens to sit in `data.sr.resistance` above the VCP pivot is synthetic, not real overhead supply, and must fall through to the contraction-depth fallback rather than being presented as "next resistance."

**3d.** VCP call site — replace the flat-multiplier block:
```js
const vcpT = vcpTarget(vcp, srData);
actionablePatterns.push(buildActionablePattern({
  name: 'VCP',
  fullName: 'Volatility Contraction Pattern',
  patternData: vcp,
  atr,
  targetPrice: vcpT?.price ?? null,
  targetBasis: vcpT?.basis ?? null,
  description: `${vcp.contractions_count} contractions with ${vcp.base_tightness_pct}% base tightness`,
  action: /* unchanged */,
}));
```

### Exact changes — `frontend/src/App.jsx` (target-basis caption, added Phase 1)
**3e.** The existing `targetBasis` caption switch (added Phase 1, ~line 2278) needs two new branches:
```jsx
pattern.targetBasis === 'resistance' ? `Target = nearest real resistance ($${pattern.targetPrice?.toFixed(2)})` :
pattern.targetBasis === 'vcp_contraction' ? 'Target = pivot + largest contraction depth (no real resistance overhead)' :
```
placed alongside the existing `'cup_depth'` / `'base_depth'` / `'flat_pct_legacy'` branches (`'flat_pct_legacy'` branch is deleted entirely once VCP no longer uses it — confirm no other pattern still emits that basis string before removing the branch).

---

## 4. Implementation order

```
Phase 3a  _compute_weekly_sr returns weekly_df too (1 caller, low risk)
Phase 3b  _find_mtf_confluence: proximity + strength + strength_label
Phase 3c  _enrich_with_mtf: thread scores through + exclude projected levels
Phase 3d  App.jsx: badge "excluded" count + ★ tooltip strength_label
Phase 3e  3-pass review, live verify (see §5)

Phase 4a  categoricalAssessment.js: vcpTarget() helper
Phase 4b  getActionablePatterns() gains srData param; VCP call site rewired
Phase 4c  App.jsx: data.sr passed in; two new targetBasis caption branches
Phase 4d  3-pass review, live verify (see §5)
```
No dependency between Phase 3 and Phase 4 — either can go first. Two commits, not one, so each is independently attributable and revertable.

---

## 5. Verification plan (Golden Rule 6 — nothing is done on a code-read)

### Phase 3 (MTF)
- Pick a real ticker with a **near-ATH** setup (`resistanceProjected: true` in the current `/api/sr/<ticker>` response — sweep a few candidates first, don't assume one) and confirm: `projected_excluded > 0`, `confluence_pct` measurably higher than before the fix, badge shows the "N excluded" text.
- Pick a ticker with a real `.X0`-ending confluent level (proves BUG-A is still fixed) and confirm the ★ tooltip now shows `(Strong)` / `(Moderate)` / `(Weak)`, not just "Confluent with weekly level".
- Confirm `strength` varies continuously across a ticker's levels (spot-check 3-4 levels, not just min/max) rather than clustering at the old 0.6/1.0 constants.
- Zero console errors; confirm `weekly_df=None` (early-return path in `_compute_weekly_sr`) doesn't crash `_enrich_with_mtf`'s new `_score_levels(all_weekly, weekly_df, ...)` call — this is the one new failure mode Phase 3 introduces, test it directly (a ticker with <20 weekly bars / insufficient history).

### Phase 4 (VCP)
- Sweep `/api/patterns/<ticker>` across a real candidate list for `vcp.detected && vcp.confidence >= 60` (don't assume one exists — confirmed practice from the Day 112 session, VCP/C&H/FlatBase detections are sparse in practice).
- For a VCP with real resistance above its pivot: confirm target == `Math.min` of `data.sr.resistance` filtered `> pivot`, caption reads "nearest real resistance ($X)".
- For a VCP at/near ATH (`resistanceProjected: true`): confirm it falls through to the contraction-depth fallback, not the projected level.
- Force the null path (a VCP with a missing/malformed first contraction, or construct one) — confirm the UI shows `—` / `R:R —`, not `NaN`/`undefined`.

### Three-pass escalating review (Golden Rule 41)
- **Phase 3, Pass 2:** does `_compute_weekly_sr`'s changed return signature break anything else that might call it — reconfirm it truly has one caller before assuming the signature change is safe. Does the `projected_prices` exclusion set need `round()`-tolerant matching (the same float-identity question Phase 1-2 already solved once) or is exact float equality safe here since these are the same in-memory floats, never round-tripped through a string key first?
- **Phase 3, Pass 3:** does excluding projected levels ever make `confluence_map` empty (division by zero in `confluence_pct`)? The existing `if confluence_map else 0` guard already covers this — confirm it still fires correctly with the new filter.
- **Phase 4, Pass 2:** does `vcpTarget()` get called before `srData` has loaded on a slow connection (i.e. `data.sr` itself is null/undefined mid-flight)? `getActionablePatterns` is only called after `setSrData(data.sr)` in the same synchronous block — `data.sr` is already resolved by then (it's the just-fetched API payload, not a stale state read) — but verify this holds if `Promise.all`'s ordering ever changes.
- **Phase 4, Pass 3:** a VCP pattern whose pivot is *below* current price (already broken out, pulled back) — does `resistances.filter(r => r > pivot)` produce a sane result, or should the filter be `> currentPrice` instead? Decide and document explicitly; don't leave it implicit.

---

## 6. Open decisions before starting

1. **🟡 Confirm `backend.py` truly needs no change** (§2, the `projected_excluded` passthrough claim) — one grep/curl check before Pass 1 starts, not an assumption to build on.
2. **🟢 `strength_label` thresholds (0.75 / 0.45)** are a first-principles guess (matches the old 1.0/0.6 split roughly at the midpoint) — not backtested, doesn't need to be (this is a display label on an informational card, not a gate). Flag if the labels look wrong on real data during verification; adjust once, not iteratively.
3. **🟢 `vcp_contraction` vs `base_depth` as VCP's fallback basis string** — kept distinct from Flat Base's `base_depth` intentionally, since a VCP contraction depth and a Flat Base range are conceptually different measurements sharing an arithmetic shape. Confirm this reads clearly in the UI caption during verification.
