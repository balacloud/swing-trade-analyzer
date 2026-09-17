# Absolute Momentum Read (Dual Momentum's Second Leg) — Informational Only — Day 117

> **Status:** Ready to implement, with 4 open decisions in §9 needing sign-off first.
> **Author:** Opus plan agent, read-only investigation. No project file was created, edited, or moved.
> **Golden Rule 55 trigger:** (c) — the field being touched (`results.criteria.momentum`) has a
>            downstream consumer that iterates the object it lives on. Not (a)/(b)/(d): no
>            forward-test logic (program discontinued 2026-09-12), no shipped gate/badge
>            modified, no threshold changed.
> **Hard constraints, confirmed honored by this design (§7 proves each):** nothing here gates,
>            ranks, suppresses, scores, or alters BUY/HOLD/AVOID, the Simple Checklist's
>            pass/fail or `passCount`, or any existing threshold.
> **File/line overlap with live plans:** none. Day 116 (shipped, `e5a3f720`) occupies
>            `App.jsx:1818-1889` and `volumeThresholds.js`; Day 115
>            (`MTF_VCP_FIX_PLAN_DAY115.md`) occupies `App.jsx:477-482, 2026-2071, 2278`. This
>            plan touches `App.jsx:48, 1651, 2800` and `simplifiedScoring.js:110`. Disjoint
>            from both. `volumeThresholds.js` is not touched.

---

## 1. Findings — corrections to the brief, called out explicitly

### 1.1 The "5% risk-free proxy" exists in the repo, concretely, with a stored result — and the brief attributes it to the wrong day

The brief says "Day 111 … backtested against a 5% risk-free proxy." **The backtest was Day 107.
Day 111 is when the decision to close it was recorded.** The real artifacts:

| What | Where | Exact content |
|---|---|---|
| The constant | `backend/backtest/backtest_holistic.py:108` | `ABSOLUTE_MOMENTUM_RISK_FREE_RATE = 0.05  # mirrors metrics.py's compute_metrics() default` |
| The filter | `backend/backtest/backtest_holistic.py:491-501` | `stock_ret_252 = Close[i]/Close[i-252] - 1`; `if stock_ret_252 > 0.05: config_g = True` |
| Its provenance | `backend/backtest/metrics.py:68` | `def compute_metrics(trades, risk_free_rate=0.05)` |
| The runner | `backend/backtest/research_spike_volume_momentum.py` | Golden Rule 20 pre-committed, run-once discipline, 400 tickers, seed 42, 2020-2025, survivorship-free |
| **The stored result** | `backend/backtest_results_holistic/research_spike_volume_momentum_20260813_202107.json` | **Config C: 75 trades, PF 0.9731, WR 45.33. Config G: 74 trades, PF 0.9924, WR 45.95.** |
| The closure | `docs/claude/versioned/KNOWN_ISSUES_DAY110.md:336-342` | "Decided Day 111 — **not pursuing.** … Correct but pointless … Closing, not deferring." |
| Roadmap record | `docs/claude/stable/ROADMAP.md:310` | "Companion item, closed not deferred" |

So "~1% of trades" is precisely **1 of 75 = 1.3%**, from a real stored run. The brief's
characterization of the decision as closed-not-deferred is correct.

### 1.2 NEW — the algebraic reason it's near-inert, and the number that makes this feature worth shipping anyway

Nobody in the repo wrote this down. The Simple Checklist's gate is
`rsRatio = (1+stockReturn)/(1+spyReturn) >= 1.0`, which (for `spyReturn > -100%`) is **exactly
`stockReturn >= spyReturn`**.

Therefore: **whenever SPY's own trailing 252-day return already exceeds the cash bar, passing
the RS gate mathematically implies passing the absolute-momentum bar.** The read can only say
something new when SPY's own trailing year is below the bar. That is the mechanism behind "1 of
75," not a coincidence.

Measured how often that window is open — 24 years of SPY daily closes, 6,038 sessions,
2002-09-17 → 2026-09-16:

| SPY trailing 252-day return | Share of sessions (24y) | Share (last 10y) |
|---|---|---|
| `< 5%` (the Config G bar) | **24.7%** | 17.7% |
| `< 0%` | **17.2%** | 12.6% |

**This is the single most useful fact for the plan.** The read is informationally inert roughly
3 days out of 4 and is precisely the thing that speaks up in the 4th — the "strongest stock in a
falling market" case the principle exists for. It also sets honest expectations: **today, SPY's
trailing 252d return is +14.26%, so every RS-passing ticker on the Simple Checklist will read
"clears the bar." That is correct behavior, not a bug, and the implementer must not "fix" it.**

### 1.3 The brief's items 1-4 — verified, exact, with one field-name correction

| Brief claim | Verdict | Exact evidence |
|---|---|---|
| Criterion 2 at "~lines 85-113", inline `stockReturn`/`spyReturn`, gates on `rsRatio >= 1.0` | **Confirmed exactly** | `simplifiedScoring.js:85-113`; computation at `:100-103`, gate at `:105` |
| `stockReturn` only embedded in a formatted string, never returned raw | **Confirmed** | `:107` and `:109` — the only two uses |
| `rsCalculator.js` is a separate implementation from `price52wAgo`/`currentPrice` | **Confirmed** | `:26-27, 53-55, 82, 100` |
| `scoringEngine.js` ~171 and ~540-556 re-expose it | **Confirmed, exact** | call at `:171`, mapping at `:541-556`, `stock52wReturn: rsData.stockReturn52w` at `:547` |
| `App.jsx` ~1626-1632 renders both with no interpretation | **Confirmed, exact** | `:1624-1633`. **`formatPercent` is `App.jsx:841-844`** |

### 1.4 NEW correction, material to Decision 3 — the Full Analysis RS card is *two* clicks deep, not one

The brief frames Full-Analysis-only as "cheapest, but the secondary view." It's worse than
that. The RS card at `App.jsx:1607-1653` sits inside `{expandedSections.priceRS && (` at
`:1560`, and `expandedSections` is initialized `useState({})` at `:173` — **every collapsible
section is collapsed on load.** So the Full Analysis read requires: switch off the default
Simple view → scroll to "Price & Relative Strength" → click to expand. Full-Analysis-only is
not a viable sole surface.

### 1.5 The brief's parity-drift worry (item 5) is real in principle and **measured at exactly zero in practice**

Tested it live against the running backend (`localhost:5001`), 50 tickers, 2026-09-16, computing
both bases per ticker:

```
basis A (Simple Checklist):  priceHistory[n-1].close / priceHistory[n-252].close - 1
basis B (rsCalculator):      currentPrice / price52wAgo - 1
```

**Result: 50 of 50 tickers agreed to 0.00 basis points. Bit-identical, no exceptions.**

The mechanism, traced in `backend.py:1011-1075`: both fields derive from the *same*
`hist_data = hist.tail(260)` slice inside the same handler. `price_52w_ago` is
`hist_data.iloc[-252]['close']` (`:1058`), `current_price` is `hist_data.iloc[-1]['close']`
(`:1071-1075`), and `price_history` (`:1036-1050`) is that same frame row-by-row with the same
`round(x, 2)`. With `n = 260`, `priceHistory[n-252] == priceHistory[8] == hist_data.iloc[-252]`.
Same for SPY via `backend.py:1182-1206`. SPY verified separately: hist basis `0.1426` vs field
basis `0.1426`.

They can only diverge in **two identified cases**:

- **(a) NaN-row skipping.** `backend.py:1040-1042` drops NaN-close rows from `price_history`
  only — `hist_data.iloc[-252]` does not shift with them. Any `nan_rows_skipped > 0`
  desynchronizes the two indices. Rare; did not occur in any of 50 names.
- **(b) Short history, `200 < len(hist_data) < 252`.** `backend.py:1060-1062` falls back to
  `price_52w_ago = hist_data.iloc[0]`, while `simplifiedScoring.js:96` requires `>= 252` and
  reports "Insufficient data." **Found live today: STUB (StubHub), `n=251`, `oldestDate
  2025-09-17`.** Its Full Analysis card shows `-73.18%` labelled "Stock 52W Return" from a
  ~250-bar window; its Simple Checklist momentum criterion says insufficient data. See §8 —
  this is a pre-existing mislabeling in a shipped row, which the new read would inherit, and it
  is a **new finding** to log, not to fix here.

**Verdict on item 5: the Golden Rule 19 concern is correctly raised and currently has zero live
blast radius, with two named, testable mechanisms that would open it.** That is a much stronger
position than "assume they agree."

### 1.6 NEW, minor, do-not-fix: both frontend implementations span 251 bars, the backtest spans 252

`simplifiedScoring.js:100` uses indices `n-1` and `n-252` — 251 intervals.
`backtest_holistic.py:498` uses `date_idx` and `date_idx - 252` — 252 intervals. A one-bar
difference between the frontend's "1 year" and the backtested filter's "1 year." Both frontend
paths share the off-by-one *identically*, so the read and the gate stay consistent with each
other. **Do not "fix" this** — changing `simplifiedScoring.js:100` changes the live RS gate,
which is a methodology change (Golden Rule 55(d)), not in scope. Log it.

### 1.7 Backend assumption — verified, not assumed: **no Python changes are needed**

`stockReturn` and `spyReturn` are computed in JS from `priceHistory`, which already crosses the
API (`backend.py:1095`), and `price52wAgo` likewise (`:1089`). Both are already in `data.stock`
at `App.jsx:453`. The read is a pure function of a number that is already client-side on both
views. **Zero backend work.** The only backend-adjacent item is the 5% constant, which cannot be
shared across the JS/Python boundary — handled the same way `volumeThresholds.js:24` handles
`BREAKOUT_VOLUME_THRESHOLD`: one frontend definition, with the backend line cited in the comment.

### 1.8 Golden Rule 54 caller trace — full grep, and it found the thing that makes the obvious approach wrong

Grep scope: `frontend/src` + `backend`, excluding `venv`/`node_modules`.

| Symbol | Every consumer | Impact of this plan |
|---|---|---|
| `calculateSimplifiedAnalysis` | **One** call site: `App.jsx:457` | none |
| `simplifiedResult.criteria` | `App.jsx:2774` (`Object.entries(...).map`, one card per key); `simplifiedScoring.js:305` (`Object.values(...).filter(c => c.pass)` → `passCount`); `:314` (`.map(c => c.label)` → summary) | **see below — decisive** |
| `criteria.momentum` | no external reader; written at `:106,107,109,112` only | safe to extend |
| `rsData.stock52wReturn` | **one** reader: `App.jsx:1626-1627`. Produced `rsCalculator.js:100` → mapped `scoringEngine.js:547` | additive read only |
| `rsData.spy52wReturn` | one reader: `App.jsx:1632` | untouched |
| `rsData` generally | `scoringEngine.js:171-182` (score bands), `:414-429` (quality gate warning at `<0.8`), `categoricalAssessment.js:281` (`rs52Week` only) | none read any return field |
| persistence | none — `simplifiedResult` is never serialized; `forwardTesting.js` stores trades only, no checklist fields | none |
| tests | **none exist** — `frontend/package.json` has `react-scripts test` but zero `*.test.js` in the repo | verification is live-only, §8 |

**The decisive finding, which the brief did not name:** adding the new number as a *tenth key on
`results.criteria`* — the most natural-looking shape — would silently (i) render a tenth card at
`App.jsx:2774`, (ii) be counted by `passCount` at `:305` against a hardcoded
`totalCriteria: 9` at `:47`, and (iii) appear in the "Close but missing:" list at `:314`
whenever `pass` is falsy. That is a direct violation of the hard constraint, arriving through a
field addition nobody would call a gate change. **The design below therefore adds a sub-field
on the existing `momentum` object, never a key on `criteria`.** This is exactly the Golden Rule
54 shape.

---

## 2. Scope

| Does | Does not |
|---|---|
| Add one pure, non-gating read function in a new module (§4) | Add any gate, score, rank, color-decision, or boolean |
| Expose one raw number already computed by the Simple Checklist (§5) | Add a key to `results.criteria`, or touch `passCount`/`totalCriteria`/`verdict`/`summary` |
| Render it on the Simple Checklist's Momentum card and the Full Analysis RS card (§6) | Change `simplifiedScoring.js:100-105`'s RS math or gate, `rsCalculator.js`, or `scoringEngine.js` |
| Log 3 new findings (§8, Phase E) | Any backend/Python change; any MTF/VCP or Volume/OBV file; fix §1.6's 251-vs-252 bar span; fix §1.5(b)'s short-history mislabel |

---

## 3. The central design decision — which 1-year return does the read quote?

The brief frames this as an either/or. **The evidence collapses it: both options are the same
number, so take the one that is provably the gate's own on each surface.**

| Option | Trust property | New computation | Verdict |
|---|---|---|---|
| **A. Each surface quotes its own already-flowing number** — checklist quotes `criteria.momentum.stockReturnPct`, Full Analysis quotes `rsData.stock52wReturn` | The checklist sentence quotes *literally the same variable* the gate at `:105` just evaluated. Cannot ever contradict its own card. | **Zero** on both paths | **RECOMMENDED** |
| B. Both surfaces quote `rsData.stock52wReturn` | Full Analysis is fine; the checklist sentence would quote a number from a different source than the gate immediately above it. §1.5(b) proves that source can legitimately disagree (STUB, live today). | Zero | Rejected |
| C. A third shared implementation | Golden Rule 19/21's exact failure shape — a third "same" calculation to drift | New | Rejected |

Option A is not a compromise: because §1.5 measured the two bases as bit-identical across 50
tickers with a traced shared origin in `backend.py`, the two surfaces will say the same thing as
a matter of fact, while each remaining structurally tied to its own view's gate. Where they
*can* diverge (§1.5's two named cases), Option A gives the correct answer on each surface and
Option B does not.

**Both call sites feed the same single `getAbsoluteMomentumRead()`.** There is exactly one
definition of the read, and zero new definitions of the return.

---

## 4. Threshold decision: use 5%, not 0% — and correct the brief's premise for 0%

**The brief's stated case for 0% is factually wrong.** It says 0% is "the more standard
'absolute momentum = up at all' bar per Antonacci's original paper." This project's own
research file says otherwise: `docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md:112` —
*"that same 12-month return must beat 3-month T-bill yield (absolute momentum)."* Antonacci's
bar is the T-bill, not zero. A 5% static proxy is a (stale) approximation of the right bar; 0%
is a different, weaker rule.

**Recommendation: `5.0`, carried as one frontend constant that cites `backtest_holistic.py:108`.**
Four reasons:

1. It is the **only** absolute-momentum threshold in this repo with an actual run behind it
   (§1.1), and that run's "1 of 75" evidence — the very reason this is informational and not a
   gate — is evidence *about the 5% filter specifically*. Shipping 0% would make the on-screen
   read a filter this project has never tested while citing a backtest of a different one.
2. It has a provenance chain: `backtest_holistic.py:108` → `metrics.py:68`'s
   `risk_free_rate=0.05`.
3. Golden Rule 19/47 instinct: one value, one definition, backend line cited in the comment —
   the established `volumeThresholds.js:4-24` pattern.
4. **The 0%-preferring reader loses nothing.** The returned sentence always prints the actual
   signed return, and the copy has a distinct band for `< 0`. Anyone who wants the zero line
   reads it directly.

**Must be disclosed in both the JSDoc and the UI tooltip:** 5% is a *static proxy*, not a live
T-bill yield. STA has no risk-free-rate feed; adding one is a new data dependency, not a display
change. Decision 1 in §9.

---

## 5. Exact diffs

### 5.1 NEW FILE — `frontend/src/utils/absoluteMomentum.js`

House style per `volumeThresholds.js`: JSDoc explains *why*, no color/className/boolean
returned, `null` on missing data, explicit non-gating contract in the docstring.

```js
/**
 * Absolute momentum — dual momentum's second leg. Informational read only.
 *
 * Antonacci, Dual Momentum Investing (2014): relative strength is half the
 * rule. A stock can be the strongest name in a falling market and still lose
 * money, so the second leg asks whether the stock's OWN trailing return beat
 * a risk-free/cash return in absolute terms. STA has gated on the first leg
 * since Day 27 (simplifiedScoring.js Criterion 2, RS >= 1.0) and has never
 * had the second leg anywhere, gated or informational. This adds it as a
 * sentence a human reads. It is NOT a gate, and that is a closed decision:
 *
 * WHY NOT A GATE. Day 107's pre-committed research spike backtested exactly
 * this filter as Config G (backtest_holistic.py:491-501) — Config C plus
 * "trailing 252-day return > 5% risk-free proxy" — 400 tickers, seed 42,
 * 2020-2025, survivorship-free. Stored result:
 * backend/backtest_results_holistic/research_spike_volume_momentum_20260813_202107.json
 * — Config C 75 trades, Config G 74. It excluded exactly ONE trade. Day 111
 * closed the item "correct but pointless" (KNOWN_ISSUES_DAY110.md:336-342).
 *
 * WHY IT IS NEAR-INERT, ALGEBRAICALLY. The RS gate is
 * (1+stockRet)/(1+spyRet) >= 1.0, i.e. exactly stockRet >= spyRet. So
 * whenever SPY's own trailing 252-day return already clears the cash bar,
 * passing the RS gate ALREADY implies clearing this one — this read can only
 * say something new when SPY's own trailing year is below the bar. Measured
 * on 24 years of SPY (6,038 sessions, 2002-09-17..2026-09-16): SPY's trailing
 * 252-day return was under 5% on 24.7% of days and under 0% on 17.2%. So this
 * read is expected to agree with the gate roughly 3 days in 4 and to be the
 * one thing on the page that speaks up in the 4th. When SPY's year is strong,
 * every RS-passing ticker reading "clears the bar" is correct, not a bug.
 *
 * THE THRESHOLD. 5.0 is not chosen here. It is the same number
 * backtest_holistic.py:108 used for the Config G run above
 * (ABSOLUTE_MOMENTUM_RISK_FREE_RATE = 0.05, itself mirroring metrics.py:68's
 * compute_metrics(risk_free_rate=0.05) default). Frontend and backend can't
 * share a module, so this is the single frontend definition — same situation
 * and same handling as BREAKOUT_VOLUME_THRESHOLD (volumeThresholds.js:24).
 * It is a STATIC PROXY, not a live T-bill yield: STA has no risk-free-rate
 * feed, and adding one would be a new data dependency, not a display change.
 * Antonacci's literal bar is the 3-month T-bill (see
 * docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md:112), not zero; 5% is a
 * stale approximation of the right bar, 0% would be a different rule. The
 * text always prints the actual signed return, so a reader who prefers the
 * plain zero line can read it straight off the sentence.
 */
export const ABSOLUTE_MOMENTUM_CASH_PCT = 5.0;

/**
 * Pure, non-gating read of a stock's own ~1-year absolute return.
 *
 * Never returns a color, a className, or a pass/fail boolean — informational
 * only, and must not be used to gate, suppress, rank, or score anything. No
 * code path from here reaches the verdict, any score, or the Simple
 * Checklist's pass/fail outcome or passCount. `state` is a descriptive string
 * for copy selection and test assertions only, never a verdict.
 *
 * Deliberately says NOTHING about relative strength. Its two call sites sit
 * under different RS contexts (the Simple Checklist's RS >= 1.0 gate; the
 * Full Analysis RS card, which has no such gate), so any sentence claiming
 * the two legs "agree" would be false on one of them.
 *
 * Computes nothing: callers pass a 1-year return their own view already
 * has. This function exists so the two views can't word it differently, not
 * so a third calculation can exist (Golden Rule 19/21).
 *
 * @param {?number} returnPct - trailing ~1-year return in PERCENT (-3.64 for
 *                              -3.64%), NOT a ratio. Simple Checklist passes
 *                              criteria.momentum.stockReturnPct; Full
 *                              Analysis passes rsData.stock52wReturn.
 * @returns {?{state:'above_cash'|'below_cash'|'negative', text:string}}
 *          null when the return is unavailable — render nothing, not a claim
 *          about missing data. Same convention as volumeThresholds.js.
 */
export function getAbsoluteMomentumRead(returnPct) {
  if (typeof returnPct !== 'number' || !Number.isFinite(returnPct)) return null;

  const r = `${returnPct >= 0 ? '+' : ''}${returnPct.toFixed(1)}%`;

  if (returnPct < 0) {
    return {
      state: 'negative',
      text: `${r} over the past year — negative in absolute terms. Relative strength can pass in a falling market; dual momentum's second leg would not.`,
    };
  }
  if (returnPct < ABSOLUTE_MOMENTUM_CASH_PCT) {
    return {
      state: 'below_cash',
      text: `${r} over the past year — positive, but under the ${ABSOLUTE_MOMENTUM_CASH_PCT}% cash proxy. Roughly what a T-bill would have returned.`,
    };
  }
  return {
    state: 'above_cash',
    text: `${r} over the past year — clears the ${ABSOLUTE_MOMENTUM_CASH_PCT}% cash proxy, so absolute momentum is positive.`,
  };
}
```

### 5.2 `frontend/src/utils/simplifiedScoring.js` — insert between line 110 and line 111

The only change to this file. Additive; no existing line is edited.

```diff
       results.criteria.momentum.reason = `RS ${rsRatio.toFixed(2)} - underperforming SPY (Stock: ${(stockReturn * 100).toFixed(1)}% vs SPY: ${(spyReturn * 100).toFixed(1)}%)`;
     }
+
+    // Day 117: expose the raw 1-year return this criterion already computed
+    // at :100. Display-only — nothing reads it back, and `pass` is already
+    // final above. It exists so the absolute-momentum read
+    // (utils/absoluteMomentum.js — informational, never a gate) can quote
+    // THE SAME number this gate just used, instead of a second,
+    // differently-sourced one. Until now it survived only inside the
+    // formatted `reason` string.
+    //
+    // Deliberately a sub-field on `momentum`, NOT a tenth key on
+    // `results.criteria`: that object is filtered by `c.pass` into
+    // `passCount` at :305, mapped into the "missing" list at :314, and
+    // rendered one-card-per-key at App.jsx:2774 against a hardcoded
+    // totalCriteria: 9. A new key there would silently become a tenth
+    // checklist criterion. (Golden Rule 54.)
+    results.criteria.momentum.stockReturnPct = stockReturn * 100;
   } else {
     results.criteria.momentum.reason = 'Insufficient data for RS calculation';
   }
```

Note the `else` branch is untouched: on insufficient data `stockReturnPct` stays `undefined`,
`getAbsoluteMomentumRead(undefined)` returns `null`, and nothing renders. Null-path handled by
omission, per house convention.

### 5.3 `frontend/src/App.jsx` — import, after line 48

```diff
 import { getVolumeConfirmationRead, getVolumeDirectionRead, getObvHorizonRead, getEffortVsResultRead } from './utils/volumeThresholds'; // Day 111/112/116
+import { getAbsoluteMomentumRead } from './utils/absoluteMomentum'; // Day 117: dual momentum's second leg, informational only
```

### 5.4 `frontend/src/App.jsx` — Full Analysis RS card, insert between line 1651 (`)}`) and line 1652 (`</div>`)

```diff
                         </div>
                       )}
+                      {/* Day 117: absolute momentum — dual momentum's second leg
+                          (Antonacci 2014). Informational only: gates nothing, scores
+                          nothing, and is deliberately NOT wired into the RS colour
+                          bands above. Reuses rsData.stock52wReturn, already computed
+                          by rsCalculator.js:100 and mapped at scoringEngine.js:547 —
+                          no new arithmetic anywhere. Backtested as Config G
+                          (backtest_holistic.py:491-501) and deliberately NOT shipped
+                          as a gate: it excluded 1 of 75 trades. Full reasoning:
+                          docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md */}
+                      {(() => {
+                        const abs = getAbsoluteMomentumRead(analysisResult.rsData?.stock52wReturn);
+                        if (!abs) return null;
+                        return (
+                          <div
+                            className="mt-2 pt-2 border-t border-gray-700 text-xs text-gray-400"
+                            title="Dual momentum's second leg (Antonacci, 2014). Relative strength above asks whether the stock beat the market; this asks whether it beat cash. The 5% figure is a static risk-free proxy carried from this project's own Day 107 backtest, not a live T-bill yield. Informational only — it does not affect any score, the verdict, or the Simple Checklist."
+                          >
+                            <span className="text-gray-500">Absolute momentum (info only): </span>{abs.text}
+                          </div>
+                        );
+                      })()}
                     </div>
```

### 5.5 `frontend/src/App.jsx` — Simple Checklist Momentum card, insert between line 2800 (`</p>`) and line 2801 (`</div>`)

```diff
                       <p className="text-sm text-gray-300 mt-2">
                         {criterion.reason}
                       </p>
+                      {/* Day 117: absolute momentum — dual momentum's second leg,
+                          shown only on the Momentum card, using the SAME 1-year
+                          return the RS gate above just evaluated
+                          (simplifiedScoring.js:100, exposed at :111). Informational
+                          only: it is not a tenth criterion, it never changes
+                          `pass`, `passCount`, `totalCriteria`, `verdict` or
+                          `summary`, and no other criterion renders it (explicit
+                          `key === 'momentum'` rather than a generic field, so the
+                          shared card shape stays a pass/fail shape).
+                          docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md */}
+                      {key === 'momentum' && (() => {
+                        const abs = getAbsoluteMomentumRead(criterion.stockReturnPct);
+                        if (!abs) return null;
+                        return (
+                          <p
+                            className="text-xs text-gray-400 mt-2 pt-2 border-t border-gray-600/50"
+                            title="Dual momentum's second leg (Antonacci, 2014). The criterion above asks whether the stock beat SPY; this asks whether it beat cash. Note that whenever SPY's own trailing year is above the cash bar, passing the criterion above already implies clearing this one — this line only tells you something new in a flat or falling market. The 5% figure is a static risk-free proxy from this project's own Day 107 backtest, not a live T-bill yield. Informational only — it is not one of the 9 criteria and does not affect the pass/fail count or the verdict."
+                          >
+                            <span className="text-gray-500">Absolute momentum (info only, not one of the 9): </span>{abs.text}
+                          </p>
+                        );
+                      })()}
                     </div>
```

---

## 6. Where it surfaces — both, and why

**Recommendation: both surfaces, Simple Checklist first.**

- **Simple Checklist is required, not optional.** It is the default view (Day 75), it is where
  the RS gate actually fires, and it is the only place the read sits beside the thing it
  completes. Per §1.8 the cost is one sub-field addition with a fully traced, single-call-site
  caller graph — genuinely low risk, now demonstrated rather than assumed.
- **Full Analysis is worth the four extra lines** but cannot be the sole surface (§1.4: two
  clicks deep, behind a collapsed section, on the non-default view). Its independent value is
  real: that view has **no RS >= 1.0 gate** — `scoringEngine.js:171-182` only scores RS in bands
  and `:425-429` only warns below 0.8 — so a stock with RS 0.85 and a -10% year is fully
  displayable there, and the read discriminates on that page every day regardless of SPY.

---

## 7. Hard-constraint compliance — how each is structurally guaranteed

| Constraint | Guarantee |
|---|---|
| Never gates | `getAbsoluteMomentumRead` is imported only by `App.jsx` render expressions. `simplifiedScoring.js` does **not** import it. Verified by the grep in §1.8 plus the import added at §5.3 being the only one. |
| Never ranks/suppresses | Returns no boolean, no number used for ordering; both call sites return `null` → render nothing, or a `<p>`/`<div>` of text. No `sort`, `filter`, or conditional-hide touches it. |
| Never touches verdict/score | It is not referenced in `scoringEngine.js`, `categoricalAssessment.js`, or `simplifiedScoring.js`'s verdict block (`:302-324`). |
| Never touches Simple Checklist pass/fail | The only write to `results` is `results.criteria.momentum.stockReturnPct`, placed **after** `pass` is final (`:106`) and read by nothing in `:305/:314`. `totalCriteria: 9` at `:47` is untouched; `criteria` gains no key. |
| No existing threshold changed | `ABSOLUTE_MOMENTUM_CASH_PCT` is a brand-new constant. `1.0` at `:105`, `0.8`/`1.0`/`1.2`/`1.5` in `scoringEngine.js` and `rsCalculator.js`, and `volumeThresholds.js`'s constants are untouched. |
| No backend changes | §1.7. Verified: both inputs already cross the API. |
| No MTF/VCP or Volume/OBV overlap | Header note. `volumeThresholds.js` untouched; `App.jsx` line ranges disjoint from both plans'. |

---

## 8. Implementation order

```
Phase A   frontend/src/utils/absoluteMomentum.js — new file (§5.1)
Phase B   simplifiedScoring.js — one additive sub-field (§5.2)
Phase C   App.jsx — import (§5.3) + Simple Checklist render (§5.5)
Phase C'  3-pass review, live-verify §8.1 → this is the commit-worthy unit
Phase D   App.jsx — Full Analysis RS card render (§5.4)
Phase D'  Live-verify on the Full Analysis view → fold into the same commit
Phase E   Docs, same commit:
          - KNOWN_ISSUES (current: DAY112; open a DAY117 per convention):
            * re-open the closed "Dual/absolute momentum" entry NOT as a gate
              but as "surfaced informationally Day 117; the Day 111 closure of
              the GATE stands and is unchanged" — do not let this read up
              overwrite a correct closed decision.
            * NEW, Low: `price52wAgo` falls back to hist_data.iloc[0] when
              200 < len < 252 (backend.py:1060-1062) while the row is labelled
              "Stock 52W Return" — live today on STUB (n=251). Pre-existing,
              inherited by the new read, not fixed here.
            * NEW, Low/Info: frontend RS spans 251 bars (simplifiedScoring.js:100)
              vs. backtest_holistic.py:498's 252. Both frontend paths share the
              off-by-one identically. Do not fix — it would move the live gate.
            * NEW, Info: §1.2's algebraic redundancy + the 24-year SPY
              frequency figures, so nobody re-derives them.
          - README Priority #10 and CLAUDE_CONTEXT.md:150: change
            "*(parked, low priority)*" → shipped-as-info-only, gate still closed.
          - ROADMAP.md:310's "Companion item, closed not deferred" note: append
            the Day 117 informational-surface outcome; do NOT rewrite the closure.
```

Phases A-D are one revertable unit (no phase is independently useful). No hard stop; nothing
here is blocked on another decision beyond §9's sign-offs.

---

## 8.1 Verification plan — live tickers, measured today (2026-09-16, SPY 252d = +14.26%)

Nothing is "done" on a code read. There are no tests in this repo (§1.8), so all verification is
live in-browser against the running backend.

**Be explicit about what today cannot exercise.** Per §1.2, on the Simple Checklist
`RS >= 1.0` implies `stockReturn >= +14.26%` today, so **the interesting case — RS gate passes
while absolute momentum is below the bar — is mathematically unreachable on that view right
now.** Do not fake a pass to see it; do not conclude the feature is broken.

| Case | Ticker(s) | Expected |
|---|---|---|
| `above_cash`, checklist RS passes | AAPL (+39.6%, RS 1.222), MRK (+83.9%, RS 1.610) | Momentum card PASS + info line "clears the 5% cash proxy" |
| `above_cash`, borderline | F (+15.2%, RS 1.008), JPM (+15.0%, RS 1.007) | same; sanity that the read isn't keyed to the gate |
| `below_cash` (0-5%) — Full Analysis only today | PLTR +2.4%, MMM +3.9%, WMT +4.8%, CRM +4.9% | RS card info line "positive, but under the 5% cash proxy" |
| `negative` — Full Analysis, and checklist (criterion fails, line still renders) | HON -0.7%, MSFT -3.6%, NIQ -3.2%, TSLA -15.1%, KLAR -69.2% | "negative in absolute terms…"; KLAR has n=256 so the checklist computes it — confirms the line renders on a FAILING card without implying anything about the fail |
| **Insufficient data (null path)** | STUB (n=251, oldest 2025-09-17) | Checklist: "Insufficient data for RS calculation", **no info line at all, no `undefined`/`NaN`/`+NaN%`**. Full Analysis: still shows `-73.2%` + the read — this asymmetry is §1.5(b), expected, and is the new known issue, not a regression |
| The interesting combined case | not reachable live today | Exercise via a temporary browser-console call to `getAbsoluteMomentumRead(2.5)` / `(-8)` / `(12)`, or accept unexercised-on-checklist and document. **Decision 4.** |

**Non-gating constraint — tested, not asserted.** For 5 tickers spanning pass/fail (AAPL, MSFT,
PLTR, KLAR, STUB), record **before** the change and re-check **after**:
`simplifiedResult.verdict`, `.passCount`, `.totalCriteria`, `.confidence`, `.summary`, the number
of criterion cards rendered (**must be 9, not 10**), the "Close but missing:" list,
`analysisResult.totalScore`, and the categorical verdict. **All must be byte-identical.** The
card count is the specific check for §1.8's decisive finding.

**Re-measure before verifying.** Every return above drifts daily. Re-run the sweep first; do
not trust these as of the implementation date.

---

## 8.2 Three-pass review anchors (Golden Rule 41)

- **Pass 1 (mechanical).** Does `results.criteria` still have exactly 9 keys? Is
  `stockReturnPct` set *after* `pass`? Does `else`-branch `undefined` reach
  `getAbsoluteMomentumRead` and return `null`? Is `key === 'momentum'` evaluated before the IIFE
  (short-circuit, so 8 cards never call it)? Units: both call sites pass **percent**, not ratio
  — `criteria.momentum.stockReturnPct = stockReturn * 100` and `rsData.stock52wReturn` is
  already `stockPctChange52w` (`rsCalculator.js:82,100`). A missing `* 100` produces "+0.4% over
  the past year" for a +39.6% stock and would look plausible.
- **Pass 2 (semantic).** Does any sentence claim something about relative strength? It must not
  (§5.1's docstring says why). On the Full Analysis view, does any wording imply the stock
  passed a gate? There is no RS gate there. Does the tooltip disclose that 5% is static, not a
  live yield?
- **Pass 3 (adversarial — "what did we break that nobody asked about").** Re-grep
  `criteria.momentum`, `rsData.stock52wReturn`, `simplifiedResult.criteria` after the change and
  confirm the consumer list is identical to §1.8. Confirm `volumeThresholds.js` is
  byte-unchanged. Confirm `App.jsx:2767`'s `{passCount}/{totalCriteria}` still reads 9. Render a
  ticker where the Momentum card **fails** and check the info line does not read as a reason for
  the failure. Confirm the info line inside a red FAIL card isn't inheriting a red text class.

---

## 9. Open decisions — sign-off needed before implementation

1. **🔴 Threshold: 5% vs 0%.** Recommendation: **5%**, sourced from `backtest_holistic.py:108`,
   disclosed in copy as a static proxy not a live T-bill yield. The brief's premise for 0% is
   incorrect — Antonacci's bar is the T-bill, not zero (`TRADING_PRINCIPLES_100YR_RESEARCH.md:112`),
   and 0% would put an untested filter on screen while citing a backtest of a different one. The
   sentence always prints the signed return, so the zero line is readable regardless. Confirm
   or override — this is a real choice, not a formality.
2. **🔴 Surfaces.** Recommendation: **both**, Simple Checklist primary. Full Analysis alone is
   two clicks deep behind a default-collapsed section on the non-default view (§1.4). Confirm.
3. **🟡 Placement on the Simple Checklist.** Recommendation: **inside the Momentum card**,
   demarcated by a divider and prefixed "info only, not one of the 9" — it sits beside the RS
   number it completes. Alternative: a separate info block below the 9-card grid, matching the
   Day 116 volume card's visual language, at the cost of divorcing it from its context. Confirm.
4. **🟡 The unexercisable branch.** With SPY's trailing year at +14.26%, the "RS passes but
   absolute momentum doesn't" case cannot be produced live on the Simple Checklist today (§1.2).
   Recommendation: exercise the three copy branches from the browser console against the pure
   function AND accept the Full Analysis view's live `below_cash`/`negative` examples (PLTR,
   MMM, WMT, CRM, MSFT, HON) as sufficient branch coverage, documenting the limitation rather
   than holding shipping. Confirm — the Day 116 plan set the precedent that an unexercised
   branch should not ship silently.
5. **🟢 Do not fix in this pass:** §1.6's 251-vs-252 bar span, and §1.5(b)'s short-history "52W
   Return" mislabel. Both get logged. Default yes.
6. **🟢 Confirm this document's path** (`docs/claude/design/ABSOLUTE_MOMENTUM_READ_PLAN_DAY117.md`)
   — the code comments in §5.4/§5.5 cite it directly and must match whatever path it's persisted
   at. Day number: 117 (last shipped commit was Day 116).

---

## 10. One-paragraph answer to the question as asked

The missing leg is genuinely missing — nothing in STA, gated or informational, has ever asked
whether a stock beat cash — and the data to answer it is already sitting client-side on both
views, so this is a frontend-only change with zero backend work. The "5% risk-free proxy" from
the brief is real and locatable: `backend/backtest/backtest_holistic.py:108`, run as Config G on
400 survivorship-free tickers, with the result still on disk — 74 trades vs. Config C's 75, one
trade excluded, which is why it was closed as a gate on Day 111 and should stay closed. The
reason it excluded only one trade is algebraic and was never written down anywhere:
`RS >= 1.0` is exactly `stockReturn >= spyReturn`, so whenever SPY's own trailing year clears the
cash bar the RS gate already implies this one — the read can only speak up when SPY's year is
weak, which on 24 years of history is 24.7% of sessions at the 5% bar and 17.2% at zero. That is
the honest case for shipping it as information: it is silent three days in four and is the one
line on the page that objects in the fourth. The read should quote each view's own
already-flowing 1-year return rather than a shared third one — the two existing bases measured
bit-identical across 50 live tickers with a traced common origin in `backend.py`'s single
`hist.tail(260)` slice, with two specific conditions that would break that (NaN-row skipping,
and short history, live today on STUB at n=251). The one thing that would have quietly violated
the hard constraint is the obvious-looking shape: adding the number as a tenth key on
`results.criteria` would have rendered a tenth checklist card and been counted into `passCount`
against a hardcoded `totalCriteria: 9` — so it goes on the existing `momentum` object instead,
and the render is one explicit `key === 'momentum'` branch, not a generic field on a shape that
is otherwise purely pass/fail.

---

### Critical Files for Implementation
- `frontend/src/utils/absoluteMomentum.js` (new — §5.1)
- `frontend/src/utils/simplifiedScoring.js` (Criterion 2 at 85-113; insert between 110 and 111;
  **do not** touch 100-105, 305, 314, or `totalCriteria` at 47)
- `frontend/src/App.jsx` (import after 48; RS card insert at 1651/1652 — note the
  `expandedSections.priceRS` wrapper at 1560; checklist card insert at 2800/2801 — note the
  `Object.entries` map at 2774 and `passCount` render at 2767)
- `frontend/src/utils/volumeThresholds.js` (read-only reference — the house style and
  null/non-gating conventions this plan copies; **must remain byte-unchanged**)
- `backend/backtest/backtest_holistic.py` (read-only reference — the 5% constant at 108 and
  Config G at 491-501, cited by the new module's comments)
