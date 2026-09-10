# S&R `_pivot_sr` fix — Config C backtest re-baseline (Day 112)

> **What this is:** the paired A/B backtest around the Golden Rule 53 fix to
> `support_resistance.py`'s `_pivot_sr()` (extreme-level selection → nearest-to-price
> selection). Run same session, same machine, same frozen universe, minutes apart.
> **Pre-registration:** direction of the trade-count change was written down BEFORE
> the post-fix run (see below). It was **wrong** — recorded honestly.

---

## The two runs

| | BASELINE (pre-fix) | POST-FIX |
|---|---|---|
| Command | `backtest_survivorship_free.py --sample-size 400 --momentum-only` | same |
| Code | `_pivot_sr` extreme selection (pre-Day-112) | `_pivot_sr` nearest selection (`pivot_nearest_selection=True`) |
| Result file | `backtest_results_holistic/survivorship_free_20260903_165616.json` | `survivorship_free_20260903_170923.json` |
| Universe sha1 | `67b1ec8fc4f8bb4b0929d22a534f7f0bd2c2b4fa` | **identical** (verified) |
| Runtime | 770s | 753s (no material slowdown from the added `_score_levels` call) |

| Config C / standard | BASELINE | POST-FIX | Δ |
|---|---|---|---|
| Trades | **75** (34W/37L/4BE) | **41** (15W/25L/1BE) | **−34** |
| Win rate | 45.33% | 36.59% | −8.7pp |
| **Profit factor** | **0.9729** | **0.5315** | **−0.44** |
| Sharpe | −0.20 | −0.98 | worse |
| Avg R-multiple | +0.0065 | −0.2418 | worse |
| Block-bootstrap p | 0.535 | 0.938 | (neither significant) |
| Skipped (no data) | 151/400 | 151/400 | — |

---

## Pre-registered prediction (written before the post-fix run)

> "Trade count should RISE — the bug pushed `support_distance_pct` past 20% →
> `viable: NO` → the Config C gate rejected setups it shouldn't have."

**This was wrong in direction.** Trade count *fell* 75 → 41.

### Why the prediction was wrong — the real mechanism

The Config C entry gate (`backtest_holistic.py:437-470`) is `is_viable AND rr_ratio >= 1.2`,
where `rr_ratio = (nearest_resistance − price) / (price − nearest_support)`.

The prediction reasoned about the `is_viable` term. The dominant effect is on `rr_ratio`:

- **Pre-fix (extreme levels):** `nearest_resistance` = the *highest high in 2 years*.
  So `reward = far_resistance − price` was huge, and `rr_ratio` was massively
  inflated. Direct spot-checks on the frozen universe:

  | Ticker | R:R with nearest levels | R:R with extreme (buggy) levels |
  |---|---|---|
  | NE | 0.42 | **128.3** |
  | XRAY | 0.53 | **14.4** |
  | MLYS | 1.25 | 9.54 |
  | ARIS | 0.10 | 0.84 |

  Trades passed the ≥ 1.2 gate because "reward" was measured against a
  resistance 20–130% above the entry — not a real 1.2:1 setup.

- **Post-fix (nearest levels):** `reward = near_resistance − price` is realistic
  (e.g. META R1 is 0.3% above price). Most momentum entries, measured against
  *real* overhead resistance, do **not** clear 1.2:1 R:R. 34 of the 75
  pre-fix trades were only qualifying on inflated reward. They are correctly
  excluded now.

The 41 that remain still lose (PF 0.53) — so even the momentum setups that
genuinely have ~1.2:1 R:R against real resistance show no edge on this
universe.

---

## Verdict

1. **The fix is correct.** Verified live: `_pivot_sr` now returns genuinely
   nearest levels (META R1 $612.43 / 0.3% above vs. the pre-fix extreme
   ~$745), the ★ confluence badge works (BUG-A), touch counts are restored on
   the pivot path, Price Structure shows the nearest supports (BUG-B). 50+
   liquid tickers and a thin-universe spot-check all resolve sanely; no
   `kmeans`/`volume_profile` regressions.

2. **The new number is the honest one.** Per Golden Rule 20 — run once, accept
   the answer. **No tuning of `pivot_max_levels` or `pivot_min_spacing_frac`
   to claw the trade count back.** The pre-fix PF 0.97 (and the long-dead
   canonical PF 1.40) were partly artifacts of the R:R-inflation bug.

3. **Config C's canonical baseline is now PF 0.53** on corrected levels.
   The Day 79 "PF 1.40" is formally retired — already un-reproducible since
   Day 107 (Golden Rule 45, SimFin universe drift), now also known to have
   been bug-inflated.

4. **This decides the "corrected-S&R momentum forward-test variant" question:
   NO.** The pre-committed gate was "if corrected-S&R Config C backtests
   *materially better*, pre-register a variant." It backtested materially
   *worse* (0.97 → 0.53). Momentum Path B's retirement (Day 112) stands as
   the final answer on gating momentum entries with real S&R — the backtest
   now agrees with the live forward test.

5. **Ship the fix anyway.** Config C is not a live forward-test track (Path A
   uses `compute_entry_levels()`'s flat/ATR proxy, not S&R — verified
   Golden Rule 54 check). No live track or capital depends on this backtest
   number. The fix is a correctness win for the human-facing Analyze page,
   and keeping the bug to preserve a flattering-but-fake reference PF is
   exactly what Golden Rules 18/53 exist to prevent.

---

## What this does NOT change
- MR (broad) — no S&R in its path, not re-run, still the only confirmed edge (PF ~2.5 live).
- Path A — frozen, flat/ATR proxy gate, untouched.
- The Analyze page's R:R display — already informational per the redesign
  (item 7); it will now honestly show sub-1.2 R:R where real resistance is
  close, instead of a fabricated 3:1.
