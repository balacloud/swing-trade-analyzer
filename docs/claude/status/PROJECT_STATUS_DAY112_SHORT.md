# Project Status — Day 112

## Version: v4.60 → v4.61 (Backend v2.48 → v2.49, Frontend v4.55 → v4.56)

*(Backend/Frontend version constants in code were drifted at v2.47 / v4.54 —
caught and corrected to v2.49 / v4.56 this session.)*

---

## What Happened Today

A long session spanning a real-week gap. Three code changes shipped, all
verified live; one produced a significant honest negative result; a full Opus
plan was written for a fix chain, of which the first two phases were executed.
Five visual Artifacts touched (one new, four stale ones repaired).

### 1. Momentum Path B — RETIRED

Path B (the real S&R-based momentum entry-gate experiment, Day 95) reached 150
closed trades with no live edge — blended PF ~1.01, and the only lift it ever
had came from one Aug 3–7 2026 regime cluster (66% of the sample; ex-cluster PF
0.72). Experiment complete, answer recorded. `live_signals.get_momentum_signals()`
no longer appends the `B_revised_rr` gate; the redundant dual-variant cooldown
pre-filter was narrowed to Path A only; `check_sr_gate()` kept in code with an
explicit "re-validate before any Path-B successor" docstring warning. The 66
open + 15 pending positions wind down by their own exit rules (~3 weeks) — as of
2026-09-09 Path B shows 166 closed, all from that wind-down, **zero new
signals** (retirement verified working). `--report` label + the Forward Test
tab card relabeled to "Retired". `PAPER_TRADING_PREREGISTRATION.md` §8b + Change
Log updated. **Not deleted** — the row stays as a frozen historical record.

### 2. Pattern price targets — measured-move (Phase 1 of the S&R fix chain)

`categoricalAssessment.js`'s `buildActionablePattern()` no longer multiplies the
pivot by a flat percentage (1.20 C&H / 1.12 Flat Base — a made-up number never
checked against the chart). Cup & Handle now targets `pivot + (left_lip −
bottom)` (cup depth, O'Neil's rule); Flat Base targets `pivot + (high − low)`
(base height). Returns `null` when the geometry isn't in the payload rather than
falling back to a fabricated percentage (Architecture Rule 6). VCP keeps a flat
+15% with a visible "pending resistance-based fix" note (Phase 4). New
`targetBasis` field + a caption on the card showing where the number comes from.
`App.jsx` render made null-safe (`—` / `R:R —`). **Verified live on BKNG**: target
moved $263.70 → $289.74, caption + R:R 5.3:1 render correctly.

### 3. Support & Resistance `_pivot_sr` — nearest-level selection (Phase 2, Golden Rule 53)

The confirmed extreme-vs-nearest bug: `_pivot_sr()` kept the N *most extreme*
pivots in the lookback window, not the N *nearest* to price — and the truncation
happened *before* the caller split around price, so a resistance just overhead
was structurally unrepresentable. Fixed: split around current price inside
`_pivot_sr`, keep the N nearest per side with a greedy merge-not-reject on
minimum spacing (the old spacing check returned `None`, punting every ticker to
agglomerative). Added behind `SRConfig.pivot_nearest_selection` (default True;
False = pre-Day-112 rollback path, kept for the backtest A/B). Touch scoring
(`_score_levels`) now runs on the pivot path — touch counts had silently
vanished from the Price Structure card whenever pivot won. Three level-key maps
unified to zero-padded 2dp (`"227.5"` → `"227.50"`).

**Two new bugs found while tracing, both fixed in the same pass:**
- **BUG-A** — `_enrich_with_mtf`'s `confluence_map` keys were `str(round(k,2))`
  (drops trailing zeros) while `App.jsx` looked them up with `.toFixed(2)` —
  the ★ confluence badge silently never matched for any level ending in `.X0`
  (~10% of levels). Fixed via the key-format unification.
- **BUG-B** — `priceStructureNarrative.js`'s "nearest key levels" took
  `support.slice(0, 2)` on an ascending array = the two *deepest* supports.
  Golden Rule 53 recurring verbatim in the frontend. One-line fix.

**Caller-graph check (Golden Rule 54):** confirmed no live forward-test track
depends on `_pivot_sr` / `compute_sr_levels` / `detect_patterns` — Path A uses
the flat/ATR proxy, MR/HUB-65 use RSI(2), Path B is retired. This is a display
+ backtest fix, **no live-count reset.** New `--momentum-only` flag added to
`backtest_survivorship_free.py` (mirrors `--mr-only`).

**Verified live on META**: `Method: pivot`, R1 now $612.43 (0.3% above) vs. the
pre-fix extreme ~$745 (22% away); ★ badge renders on the $600.00 support
(BUG-A's exact failure case); `level_scores` populated on the pivot path;
50-ticker + thin-universe sweeps clean, no `kmeans`/`volume_profile`
regressions.

### 4. Config C backtest re-baseline — a significant honest negative

Paired A/B, same frozen universe (sha1 verified identical), `--momentum-only`:

| Config C / standard | Pre-fix | Post-fix |
|---|---|---|
| Trades | 75 | **41** |
| Win rate | 45.3% | 36.6% |
| **Profit factor** | **0.9729** | **0.5315** |
| Sharpe | −0.20 | −0.98 |

The **pre-registered directional prediction ("trades rise") was wrong** — trades
*fell*. Root cause of the miss: the prediction reasoned about the `is_viable`
gate term; the dominant effect is on `rr_ratio`. The bug set the reward target
to the *highest high in 2 years*, inflating R:R past the 1.2 gate on trades that
were never real 1.2:1 setups (NE R:R 128 with the bug vs. 0.42 corrected; XRAY
14.4 vs. 0.53). Fixing it correctly excludes 34 of the 75; the 41 that survive
still lose (PF 0.53). **This rhymes exactly with Path B's live failure and
Day 105's SRPS R:R finding** — momentum, gated on real S&R-based R:R, shows no
edge.

**Verdict (per Golden Rule 20):** run once, accept the answer, no tuning of
`pivot_max_levels` to claw the trade count back. The Day 79 "PF 1.40" is
formally retired — already un-reproducible since Day 107 (Golden Rule 45), now
also known to have been bug-inflated. **Config C's canonical baseline is
PF 0.53.** The fix ships anyway — Config C is not a live track, and keeping a
bug to preserve a flattering-but-fake reference number is exactly what
Golden Rules 18/53 exist to prevent. This also **decisively closes the
"corrected-S&R momentum forward-test variant" question: NO** (the pre-committed
gate was "backtests materially better → pre-register a variant"; it backtested
materially worse). Full write-up: `SR_PIVOT_FIX_REBASELINE_DAY112.md`.

### 5. Opus fix-chain plan

`SR_PIVOT_FIX_PLAN_DAY112.md` — a full Opus-authored implementation plan for
S&R + MTF Confluence + Pattern targets. Phases 1–2 executed this session;
Phases 3 (MTF Confluence graduated score + projected-level exclusion) and 4
(VCP resistance-based target) deferred as low priority (display polish on a
page whose R:R is already informational). New **Golden Rule 55** (scoped
Opus-plan-then-Sonnet-implement) came out of this.

### 6. Artifacts

New: **Forward-Test Track Board** (`https://claude.ai/code/artifact/906b779b-0440-4cf2-8de0-fb3d17f58678`)
— live state of the 4 tracks + Path B's PF-decay chart. Repaired 4 stale
artifacts (Decision Map, Audit Coverage Timeline, Data Provenance Map, Analyze
Page Mockup) and updated `SESSION_ARTIFACTS_INDEX_DAY111.md` — all 8 now
current.

---

## Files Changed

| File | Change |
|---|---|
| `backend/support_resistance.py` | `_pivot_sr` nearest-selection + merge + touch scoring + `meta["selection"]`; `SRConfig.pivot_nearest_selection` / `touch_saturation`; 3 level-key maps → zero-padded 2dp (BUG-A) |
| `backend/backend.py` | `meta.pivotSelection` on `/api/sr/<ticker>`; `BACKEND_VERSION` 2.47→2.49 |
| `backend/backtest/backtest_survivorship_free.py` | new `--momentum-only` flag |
| `backend/paper_trading/live_signals.py` | Path B gate removed from signal path; cooldown pre-filter → Path A only; `check_sr_gate()` re-validate warning |
| `backend/paper_trading/daily_job.py` | `--report` Path B label → "RETIRED" |
| `frontend/src/utils/categoricalAssessment.js` | measured-move pattern targets + null discipline (Phase 1) |
| `frontend/src/utils/priceStructureNarrative.js` | BUG-B — nearest 2 supports, not deepest |
| `frontend/src/App.jsx` | pattern target null-safe render + `targetBasis` caption; footer v4.54→v4.56 |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | Path B card → "Retired" (neutral gray badge) |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | §8b RETIRED note + Change Log row 112 |
| `docs/claude/design/SR_PIVOT_FIX_PLAN_DAY112.md` | New — Opus fix-chain plan |
| `docs/claude/versioned/SR_PIVOT_FIX_REBASELINE_DAY112.md` | New — Config C A/B + re-baseline |
| `docs/claude/design/SESSION_ARTIFACTS_INDEX_DAY111.md` | 8 artifacts, all current |

---

## All Gates Status (live, job last ran 2026-09-09)

| Track | Open | Closed | WR | PF | Status |
|---|---|---|---|---|---|
| Momentum Path A (frozen) | 39 | 74 | 43.24% | 1.1136 | Accumulating, 74/100 — marginal, slipped from 1.27 |
| Momentum Path B | 66 | 166 | 47.59% | 1.0669 | **RETIRED Day 112** — winding down, zero new signals |
| MR (broad) | 30 | 194 | 77.32% | 2.5551 | **Confirmed** — held steady across a week (was 2.53 at 161) |
| MR HUB-65 | 1 | 68 | 64.71% | 1.7360 | Accumulating, 68/100 — improving (was 1.61 at 51) |

**Freeze status:** unchanged — forward-testing accumulation remains the sole
stated priority. Day 112's changes touched zero live-track logic (verified,
Golden Rule 54). MR (broad) remains the only confirmed edge in the project.

---

## Next Session Priorities

1. **Let Path A finish its 100-trade bar.** 74/100. On the evidence (PF 1.11 and
   drifting, plus Path B null, plus the Day 112 corrected-S&R backtest at PF
   0.53) it is very likely to confirm as "no edge." Let it finish saying so,
   then formally close the momentum chapter — don't kill it early (the bar
   exists to prevent exactly that premature call).
2. **IBKR real paper-trading execution (ROADMAP Priority #13) — the real next
   work.** MR (broad) at 194 trades / PF 2.56 is the one confirmed edge and has
   earned deployment. Blocked on the user's own CIRO Rule 3200 research (the
   design doc's "Open items"). This is where effort should go, not more Analyze-
   page polish.
3. Phases 3–4 of the fix chain (MTF Confluence graduated score; VCP resistance-
   based target) — plan written (`SR_PIVOT_FIX_PLAN_DAY112.md` §4–5), low
   priority. Deck chairs on a page whose R:R is already informational.
4. Small cleanup batch, any order: 3 dead `App.jsx` functions, stale Data
   Sources "Defeat Beta API" doc, Value Tab investor-name relabeling.
5. Decide what Path B's cluster finding / retirement means for how the
   Analyze-page R:R is *framed* going forward (it will now honestly show sub-1.2
   R:R where real resistance is close, instead of a fabricated 3:1).
