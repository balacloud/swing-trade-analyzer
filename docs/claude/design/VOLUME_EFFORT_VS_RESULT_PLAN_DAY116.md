# Volume Effort-vs-Result: OBV Sign Fix + Surfacing + Same-Day Read — Day 116

> **Status:** Ready to implement, with 4 open decisions in §8 needing sign-off first.
> **Author:** Opus Plan agent, spawned Day 115/116 session to investigate whether STA
>            has a genuine "Wyckoff effort vs. result" gap, independently verify the
>            OBV `trend` sign bug, and plan a fix — read-only investigation, no code
>            changed by the agent itself.
> **Additive to** `docs/claude/design/MTF_VCP_FIX_PLAN_DAY115.md` — does not replace it,
>            does not touch its Phases 3–4. Zero file overlap except `App.jsx` (different
>            line ranges: this plan touches 1766–1835, that one touches 2026–2071/2278).
> **Context:** paper-trading discontinued 2026-09-12. Golden Rule 18 does not apply (no
>            live forward-test track to reset). Golden Rule 54 discipline applies and
>            **found a caller the original brief missed** — the ⚠️ DIST badge, §1.2.
> **Hard constraint honored throughout:** nothing here gates, suppresses, ranks, or
>            alters BUY/HOLD/AVOID, the Simple Checklist, or any score. Informational
>            only, per the user's explicit direction Day 115/116 ("volume as a signal
>            is good, don't want it as a gate").

---

## 1. Findings — verified vs. assumed

### 1.1 Thing 1 — `calculate_obv()` (backend.py:416-511) already does effort-vs-result

Confirmed present and live exactly as the brief described: `trend` at 471-474 (the buggy
comparison), 20-day price-change % vs 20-day OBV-change % (480 vs 464), the two sentences
("Bearish divergence - distribution warning", "Weak trend - price rising without volume
support") at 492/498 — code uses plain hyphens, not em-dashes. OBV badge at `App.jsx:1766-1779`.
One call site (`backend.py:1628`). No other backend file consumes OBV.

**Live proof it already answers the ask** — 150-ticker sweep, 2026-09-15, exact `calculate_obv`
logic on the exact 260-bar window `/api/sr` uses: `divergence` fires on 22/150 (14.7%). Live
bearish: DKNG, MRK, RIVN, TWLO. Live bullish: INTC, F, KO, ABBV, PLTR, TSM, WFC, C, ARM, SMCI,
BMY, CHTR, DASH, VRTX, ENPH, ADI, AFRM, BIIB.

**Conclusion: the "it's missing" framing is ~80% wrong; "it isn't useful to me" is 100% right.**
Thing 1 is a real, working, live effort-vs-result read whose output is reachable only by
hovering a 30px badge. This is a surfacing problem plus a bug, not an absence.

### 1.2 Golden Rule 54 caller check — a consumer the brief missed

`meta.obv.trend` has **three** frontend consumers, not two:

| # | Consumer | Location | Reads |
|---|---|---|---|
| 1 | OBV arrow badge (Day 49) | `App.jsx:1767-1779` | `trend`, `divergence`, `signal`/`obv_change_pct` |
| 2 | **⚠️ DIST distribution-warning badge (Day 49)** | **`App.jsx:1794-1800`** | **`rvol >= 1.5 && obv.trend === 'falling'`** |
| 3 | `getVolumeDirectionRead()` | `volumeThresholds.js:102-105` | `trend` → ±1/0 vote |

Consumer #2 is not in the brief; it's why `KNOWN_ISSUES_DAY110.md:310` deferred the fix
("feeds a shipped, live badge, needs its own review"). §3.3 resolves it.

`priceStructureNarrative.js` reads no OBV field — unaffected by this plan, affected by §1.5's
RVOL finding instead. A fourth, unrelated volume surface exists (`market_structure_engine.py`
`_volume_behavior_at_latest_pivot()` → "Volume into levels" on the Price Structure card) —
magnitude only, never compared to price, not touched here. **Five volume surfaces on the page
total.**

### 1.3 The `trend` sign bug — real, but narrower than assumed

With `obv_sma < 0`, `obv_sma*1.02` is *more* negative and `obv_sma*0.98` is *less* negative,
so the two bands overlap instead of leaving a dead zone, and `if` (evaluated first) claims the
whole overlap for `rising`. **The bug can only turn `flat` into `rising` — it can never flip
`rising`↔`falling`.** Proven analytically and empirically. `flat` is unreachable whenever
`obv_sma < 0` (0/52 negative-`obv_sma` tickers in the sweep reported `flat`).

Corrections to `KNOWN_ISSUES_DAY110.md:299-318`: "fires almost automatically" is overstated
(only above the 1.02 threshold); "regardless of actual trend" is wrong (can't flip
rising↔falling); severity is Low on the label itself, but the downstream impact (§3.3) is
what justifies fixing it. The `# regression slope` comment (line 467) is false — no regression
is computed; fix in the same pass.

### 1.4 Quantified blast radius — measured, 150 tickers, 260-bar window, 2026-09-15

| Metric | Value |
|---|---|
| `obv_sma < 0` (bug reachable) | 52/150 = 34.7% |
| Shipped label ≠ sign-safe label (bug fires) | **5/150 = 3.3%** — CMG, COIN, DIS, SLB, TMUS |
| Direction of all 5 | `rising` where the answer is `flat`, zero exceptions |
| `trend == 'falling'` count, before vs. after fix | **87 vs 87 — bit-identical** |
| `trend == 'flat'` count, before vs. after | 7 vs 12 |

**Decisive de-risking result: the `falling` set is bit-identical before/after.** The ⚠️ DIST
badge fires only on `trend === 'falling'` — therefore the fix **provably cannot** create a
false DIST or suppress a true one. This clears the only stated blocker on the deferred fix.

### 1.5 NEW, unlogged, higher-severity finding: `meta.rvol` reads the still-forming intraday bar

Not in the brief, not in any KNOWN_ISSUES file. `backend.py:1564` (`hist.tail(260)`) has no
incomplete-bar guard; `1634-1636` computes `rvol` from the final (today's, partial) bar; so do
`current_price` (1596), `change` (1607-1610), `candle.closeLocation` (1652-1657). Neither
provider drops a partial bar.

Measured 13:58 ET, live Tuesday session, 20 large caps:

| | min | median | max |
|---|---|---|---|
| RVOL from last (partial) bar | 0.27 | **0.45** | 0.87 |
| RVOL from prior (complete) bar | 0.65 | **0.92** | 2.06 |

Not one of 150 names exceeded RVOL 1.20 intraday; max was CRWD at 1.20.

**Live consequences today:** `getVolumeConfirmationRead()` prints "below-average, worth
noting" for essentially every ticker, every intraday session — literally true of the partial
bar, materially misleading as a statement about the day. The ⚠️ DIST badge (needs `rvol>=1.5`)
is structurally unable to fire before roughly the last third of the session.
`priceStructureNarrative.js:170-173` has the same issue. The card's tooltip already says the
bar is "still partial" in prose — unhandled in code; the visible sentence still asserts a
conclusion.

**The project already has this exact fix, elsewhere.** `paper_trading/live_signals.py:61-83`
`_prepare_ohlcv()` drops the still-forming bar using an explicit `MARKET_TZ` test (Golden Rule
33), added Day 99 after the partial-bar ledger contamination fix. **Applied to the forward-test
path, never to the Analyze-page display path.** Golden Rule 47's exact failure shape.

This is the single most consequential finding in the plan for §5 — a same-day
effort-vs-result read built on `meta.rvol` as it exists today would be wrong most of every
trading day.

### 1.6 `divergence` — sign-safe (confirmed), but threshold-unstable (new finding)

`obv_change_pct` uses `abs(prev_obv)` in the denominator — sign-safe for any sign of
`prev_obv`; `divergence`/`signal` do **not** have the sign bug. But `prev_obv` is a cumsum
reset to zero 260 bars ago, so its magnitude is arbitrary: measured `|obv_change_pct|` p50 =
20.6%, p90 = 99.5%, p99 = 1228%. The ±5% divergence thresholds sit below the median for some
tickers and are near-unreachable for others. **Directionally trustworthy, quantitatively
meaningless.** Not in scope to re-threshold (methodology change, Golden Rule 55) — logged as
a new issue, stated in the UI copy instead.

### 1.7 Thing 2 (`volumeThresholds.js`) — confirmed as described, two new problems

(a) **Thing 1 and Thing 2 can visibly contradict.** MRNA: badge shows gray `OBV →` (`trend`=
'flat') while the hover tooltip says "Strong confirmation - volume supports uptrend" and
`obv_change_pct=+141.2%`. Same function, two fields, opposite stories, only one visible
without hovering.

(b) **The sign bug reaches a sentence.** `obvTrend` casts +1/0/-1 in `getVolumeDirectionRead`'s
3-vote lean; a wrong +1 can flip the rendered sentence from "no clear lean" to "leans toward
buying pressure" for the 3.3% of affected tickers. Stronger argument for the fix than the badge
color.

### 1.8 Docstring drift (free fix, same pass)

`calculate_obv`'s docstring says `'obv_change'`; the function returns `'obv_change_pct'`. No
caller reads the wrong key (inert), but stale per Golden Rule 47.

---

## 2. Scope

| Does | Does not |
|---|---|
| Fix the `trend` sign bug (§3) | Re-threshold `divergence` (§1.6 → Decision 3) |
| Surface Thing 1's `signal` as readable text (§4) | Change `meta.rvol`'s definition anywhere except the new read's own input (§1.5 → Decision 1) |
| Add a same-day effort-vs-result read (§5), conditional on Decision 1 | Touch `volumeBehavior`, MTF/VCP, or any verdict/score/checklist |

---

## 3. Fix 1 — the OBV `trend` sign bug

**Decision: sign-safe absolute band** (`obv_sma ± 2%·abs(obv_sma)`) — bit-identical to today
for `obv_sma > 0`, restores the intended dead band for `obv_sma < 0`. 5/150 labels change (all
`rising`→`flat`), **zero** `rising`↔`falling` flips.

**Explicitly rejected: re-basing `trend` on `obv_change_pct`.** Looks equivalent, isn't — it's
a methodology change disguised as a bug fix: 23/150 labels change including **14 hard
rising↔falling flips** (would move the DIST badge — the exact risk the deferred fix was
worried about), and inherits §1.6's scale instability (p99 = 1228%, so a ±2% band on that basis
is noise for half the universe).

Exact diff at `backend.py:466-476`: replace the `if current_obv > obv_sma*1.02` / `<obv_sma*0.98`
comparison with `obv_band = abs(obv_sma)*0.02; if current_obv > obv_sma+obv_band: rising elif
current_obv < obv_sma-obv_band: falling else: flat`. Fix the false regression-slope comment and
the `obv_change`→`obv_change_pct` docstring key in the same pass. Decide explicitly at
implementation time what happens when `obv_sma == 0` (band vanishes to a knife edge) — don't
leave it unconsidered, that's exactly the shape of the original bug.

**Downstream impact (Golden Rule 54):**

| Consumer | Impact | Risk |
|---|---|---|
| Badge glyph/color | 5/150: green `↑` → gray `→`, only when `divergence==='none'` | Cosmetic, correct |
| ⚠️ DIST badge | **None — provably** (falling set bit-identical) | Zero |
| `getVolumeDirectionRead()` | 5/150: `obvTrend` vote +1→0, lean can shift | Intended — this is the fix's point |
| Everything else (paper trading, backtest, patterns, breakout, market structure, any verdict) | None — no OBV consumption anywhere else | Zero |

---

## 4. Decision — surface Thing 1 *inside* Thing 2's card, don't merge the functions

**(a) Do not merge** `calculate_obv()` and `volumeThresholds.js` into one computation — they
answer genuinely different-horizon questions (20-day accumulation vs. today's bar), and the
project already keeps same-shape-different-question things separate on purpose
(`volumeThresholds.js:20-22` vs. `breakout_detection.py`'s `rvol_confirm`). Merging would
destroy "20-day accumulation fine, today weak" as a sayable thing.

**(b) Promote Thing 1's `signal` into Thing 2's card as a labelled third line:**
```
Today: 0.54× the 50-day average — below-average, worth noting
Today's lean: closed down 0.5%, settled near the day's high, OBV falling — mixed signals
Last 20 days: net volume falling 27% over 20 sessions — bearish divergence, distribution warning
Informational only — this does not change the verdict.
```

**(c) Keep the `OBV ↑/↓/→` chip** — scannable peer to ADX/4H RSI/Vol, don't remove it, just
stop making it the *only* route to the sentence.

**(d) Keep the ⚠️ DIST badge as-is** — distinct, narrower, provably unaffected by §3.

New `getObvHorizonRead(obv)` in `volumeThresholds.js` — pure function, reuses the backend's own
`signal` string rather than re-deriving one in JS (avoids the JS/Python parity drift Golden
Rule 19 names), returns `null` when `meta.obv` is absent, no color/className/boolean, never
gates.

**Pass-3-level defect found and flagged, not silently resolved:** `getVolumeDirectionRead`
votes on `obv.trend` (position-vs-20-day-average) while the new `getObvHorizonRead` would
report `obv_change_pct` (endpoint-to-endpoint) — **these can genuinely disagree in sign on the
same ticker** (DIS: `trend==='falling'` while `obv_change_pct===+31.8%`). Recommended
resolution: `getObvHorizonRead` prints only the backend's `signal` sentence, drops the
self-derived "net volume rising/falling N%" head — removes the contradiction entirely, loses
only a number §1.6 already showed isn't comparable across tickers. **Flagged for sign-off,
Decision 2 — do not pick silently.**

---

## 5. Fix 3 — the genuine remaining gap: a same-day effort-vs-result read

Thing 1 is 20-session; it cannot answer the actual Day 107 question — "heavy volume today, no
price progress." Thing 2 has both ingredients (rvol=effort, price/closeLocation=result) but
never compares them. One additive read: effort (RVOL) crossed against result (today's price
move ÷ ATR%, so 1% means different things for KO vs. RIVN).

**🔴 Blocked on §1.5 (Decision 1).** On today's `meta.rvol`, this read would classify
essentially every ticker, all day, as "light volume" — not a gate-failure but a
signal-that-always-says-the-same-thing failure. Three options, in order of preference:

- **1A (recommended).** Backend adds `meta.candle.barComplete` + `meta.prevBar` (volume, rvol,
  OHLC, changePct, closeLocation, date) from `df.iloc[-2]`. New read uses today's bar when
  complete, else the last complete bar, and says which. Reuses `live_signals._prepare_ohlcv()`'s
  ET-timezone test (Golden Rule 33/7) — copies the *condition*, not the drop (`/api/sr` must
  keep returning today's live price). ~15 backend lines, additive.
- **1B.** Frontend-only: render nothing intraday, gated on the one new boolean. Cheapest, worst
  UX (nothing during the session the user most wants it).
- **1C.** Elapsed-session volume projection. **Recommend against** — new unvalidated
  methodology, same failure shape as the Day 99 partial-bar contamination the project already
  got burned by once.

New `getEffortVsResultRead({rvol, changePct, atrPct, closeLocation, barComplete, asOf})` in
`volumeThresholds.js` — returns `{state, text}`, thresholds `EFFORT_RESULT_LITTLE_PROGRESS_ATR
= 0.5`, `EFFORT_RESULT_REAL_PROGRESS_ATR = 1.0` explicitly labelled **first-principles, not
backtested** in both the JSDoc and, if shipped, the UI copy — no color/className/boolean/score,
never gates (Decision 4 covers whether unbacktested numbers are acceptable to ship at all).

Backend (1A): `MARKET_TZ` constant + `barComplete` computed in the `/api/sr` handler right
after `candle_meta` is built, plus `prevBar` from `df.iloc[-2]` when `len(df)>=3`. `api.js`
needs no change (`meta` passes through wholesale) — **verify with a live curl before building
on it**, same caution the Day 115 plan flagged for the identical assumption.

---

## 6. Implementation order

```
Phase A   backend.py: OBV trend sign fix + docstring/comment corrections     (§3)
Phase A'  3-pass review, live-verify vs. §7.1's named tickers → commit 1 (standalone, revertable)

Phase B    volumeThresholds.js: getObvHorizonRead()                          (§4)
Phase B'   volumeThresholds.js: drop "Volume: " prefix (1 call site, verify by grep)
Phase B''  App.jsx: horizon-labelled 3-line card + import
Phase B''' 3-pass review, live-verify → commit 2

  ---- HARD STOP: Decision 1 must be answered before Phase C ----

Phase C   backend.py: candle.barComplete + meta.prevBar                      (§5)
Phase D   volumeThresholds.js: getEffortVsResultRead() + 2 constants
Phase E   App.jsx: 4th line + call site
Phase F   3-pass review, live-verify intraday AND after the close → commit 3

Phase G   KNOWN_ISSUES: OBV trend bug → RESOLVED with the "DIST is immune" reasoning
          recorded. Log 3 new findings: meta.rvol partial bar (§1.5, Medium),
          obv_change_pct scale instability (§1.6, Low-Medium), correct the
          DAY110/112 entry's overstated mechanism (§1.3).
```

Phase A is independent of B–F and must be its own commit — a 3.3%-blast-radius behavior
change kept separately revertable from purely-additive display work. No overlap with the Day
115 plan (different files/line-ranges throughout); either plan can go first.

---

## 7. Verification plan (nothing is "done" on a code-read alone)

**Phase A:** 5 named tickers (CMG, COIN, DIS, SLB, TMUS as of 2026-09-15 — re-sweep before
verifying, these drift daily) must flip `rising`→`flat` via live `curl`. Control group of 5
positive-`obv_sma` tickers (AAPL, INTC, NVDA, NFLX, PLTR) must be **byte-identical**
before/after. Re-run the full 150-ticker sweep and assert the `falling` set (Counter) is
identical — this is the DIST-badge-immunity claim, must be tested not inferred. Confirm the
DIST badge itself renders identically on a live `falling` ticker (may need to check after
market close, since RVOL≥1.5 rarely fires intraday per §1.5).

**Phase B:** Live bearish (DKNG/MRK/RIVN/TWLO) and bullish (INTC/F/KO/PLTR/etc.) divergence
sentences must render as visible text, no hover required — single acceptance criterion for the
whole surfacing task. Null path (`meta.obv==null`, e.g. a recent IPO) must render nothing, no
`undefined`/`NaN`.

**Phase C–F:** Intraday check (`barComplete===false`, line describes prior session, states the
date, `meta.rvol` itself stays untouched). After-close check (`barComplete===true`, `prevBar.date`
== today). Live example needed for the `effort_without_result` case specifically (the case the
user asked for by name) — **if no live example exists that day, construct one from historical
bars rather than shipping the branch unexercised.** Non-gating constraint tested, not asserted:
record verdict/score/checklist for 5 tickers before and after — must be byte-identical.

**3-pass review flags an unresolved question for Phase C–F:** the `MARKET_TZ`/`barComplete`
test assumes US equity hours. STA serves **Canadian tickers** (confirmed working, Day 108) and
has Indian-market watchlists — TSX hours match NYSE so it's fine there, but for any
non-North-American listing the label would read wrong (`barComplete` false all day for an NSE
name whose session closed hours ago). Must scope the flag to North American listings or
document the limitation explicitly — named as the "silent timezone drift" persona-scar pattern,
Golden Rule 41.

---

## 8. Open decisions — sign-off needed before implementation

1. **🔴 Blocks Phase C–F.** `meta.rvol`'s partial-bar problem (§1.5) — choose 1A (recommended),
   1B, or 1C (recommend against). **Separately:** should the *existing* surfaces (the "below-
   average, worth noting" sentence, the DIST badge's `rvol>=1.5` gate, the price-structure
   narrative's watch line) get the same fix, or does that stay a distinct follow-up plan? The
   Opus plan deliberately left those alone and logged the finding rather than folding it in.
2. **🔴** Recommended resolution for the `trend`-vs-`obv_change_pct` contradiction (§4): print
   only the backend's `signal` sentence, drop the self-derived "rising/falling N%" head. Confirm
   or pick another option.
3. **🟡** Leave `divergence`'s ±5% thresholds alone this pass (§1.6), log as a new Low-Medium
   known issue, state the limitation in copy. Confirm.
4. **🟡** `EFFORT_RESULT_LITTLE_PROGRESS_ATR`/`REAL_PROGRESS_ATR` (0.5/1.0 ATR) are
   unbacktested first-principles guesses, disclosed as such in the copy. OK to ship display-only,
   or hold Phase C–F entirely until later calibration?
5. **🟢** Keep both the OBV chip and the DIST badge as-is (§4c/d) — low-stakes, default yes.
6. **🟢** Confirm this file's path (`docs/claude/design/VOLUME_EFFORT_VS_RESULT_PLAN_DAY116.md`)
   since implementation-time code comments cite it directly.

---

## 9. One-paragraph answer to the question as asked

**It is not missing.** `calculate_obv()` has computed the Wyckoff effort-vs-result comparison
since Day 49 and already emits the exact sentences asked for — live today on DKNG, MRK, RIVN,
TWLO ("bearish divergence, distribution warning") and TSLA ("price rising without volume
support"). It fires on ~15% of tickers and is invisible unless you hover a 30px arrow. So the
work is: fix the sign bug (small, measured, provably can't touch the DIST badge), promote the
existing sentence into visible text next to the Day 111-112 card with explicit horizon labels,
and add exactly one genuinely new read — today's volume against today's price progress — which
nothing currently computes. The one thing that would make that new read useless is that
`meta.rvol` is silently taken from the still-forming intraday bar, an unlogged bug that needs a
decision before anything is built on it.

---

### Critical files for implementation
- `backend/backend.py` (`calculate_obv` 416-511, esp. 437, 466-476; `/api/sr` handler
  1511-1770, esp. 1564, 1634-1636, 1652-1657, 1763)
- `frontend/src/utils/volumeThresholds.js` (whole file, 119 lines — append 2 functions, edit
  strings at 39/42/45)
- `frontend/src/App.jsx` (OBV chip 1767-1779; DIST badge 1794-1800 — the missed caller; Volume
  card 1808-1835; import block)
- `backend/paper_trading/live_signals.py` (57-83 — the partial-bar/`MARKET_TZ` guard to mirror)
- `docs/claude/versioned/KNOWN_ISSUES_DAY112.md` (89-91, entry to resolve) and
  `docs/claude/versioned/KNOWN_ISSUES_DAY110.md` (299-318, overstated mechanism to correct)
