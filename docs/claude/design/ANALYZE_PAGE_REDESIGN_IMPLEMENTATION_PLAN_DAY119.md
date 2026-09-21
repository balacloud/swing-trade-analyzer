# Analyze Page Redesign — Implementation Plan (Day 119)

> **Status:** Opus plan per Golden Rule 55. Supersedes **only §7 and §8** of
>            `ANALYZE_PAGE_REDESIGN_DECISIONS.md` (the *execution* plan and
>            the *freeze-safety audit*). The **17 locked decisions in §2, and
>            the §5 threshold table, are unchanged and not re-litigated here.**
>            §6's copy is amended in two specific places where it would now
>            ship factually false statements — see Correction C1/C2.
> **Created:** Day 119
> **Source of truth for decisions:** `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`
> **Known-stale, do not build from:** `docs/claude/design/mockups/analyze_page_redesign_mockup.html`
>            (still shows the pre-Day-110 Regime "stand-down" gate framing)
> **No application code has been changed by this plan.**

---

## §A — Verdict on §7/§8: partially valid

**§7's phase structure and sequencing survive intact. §7.0/§8's freeze-safety
audit is obsolete in its *justification* but still correct in its
*conclusions*, for entirely different reasons. §6's copy contains two
now-false factual claims that would ship to users as lies.**

Broken down:

| Piece | Verdict | Why |
|---|---|---|
| §2's 17 locked decisions | **Valid, unchanged** | Nothing shipped Days 112-118 reverses any of them. Day 115/118 code comments explicitly cite this doc's own descriptive-state convention as the pattern they followed (`App.jsx:2132-2136`, `:2160-2164`) — the philosophy is already leaking into shipped code, which is evidence for it, not against. |
| §7.1-§7.7 phases + sequencing | **Valid in shape, needs anchor + naming corrections** | Every file:line anchor has drifted. One helper is named for a decision that was reversed. |
| §7.0 / §8 freeze-safety audit | **Obsolete as framed, conclusions survive** | The freeze it protects is gone (Day 113). But every "**NO**" in its table is still the right answer — for parity/backtest-harness reasons, not forward-test reasons. See §D. |
| §6's final copy | **Two blocks must be rewritten before use** | The pivot-S&R bug it apologizes for was fixed Day 112; the Pattern-Detection fixed-multiple R:R it describes was replaced Day 112/118. |
| §9's open items | **Two close, one resolvable now** | Pattern-Detection caveat: closed by Day 112/118. Negative-EPS flag: answerable from the code today, and the answer is "don't build it." Mockup: still stale. |

**Net: GO.** The redesign is safer to build today than it was on Day 109,
because the single most uncomfortable thing §8 had to disclose — "Fundamentals
will keep gating real, live trade entries even after the UI stops saying so" —
is simply no longer true.

---

## §B — Premises re-checked against current code

Every claim below was re-derived this session from the file, not from §7's
summary of it.

### B1. `analysisView` still defaults to `'simple'` — Golden Rule 51 CONFIRMED

`frontend/src/App.jsx:155`:
```js
const [analysisView, setAnalysisView] = useState('simple'); // 'full' or 'simple' — default simple (Day 75)
```
Doc says `:148`. Drift only; the finding holds. The Full Analysis view is
gated at `App.jsx:1386`, the Simple view at `App.jsx:2770`.

### B2. The composite verdict's 5 live consumers — all still present

| # | Consumer | §2 item 12's line | **Current line** | Disposition (unchanged) |
|---|---|---|---|---|
| 1 | "⚠️ Stock not recommended" (AVOID + viable) | 1660-1664 | **`App.jsx:1711-1715`** | Delete |
| 2 | `position_size_advice` suppression condition | 1699-1704 | **`App.jsx:1749-1756`** | Delete with its block |
| 3 | "💡 Why This Verdict?" | 2506-2521 | **`App.jsx:2675-2688`** | Reframe |
| 4 | Simple view "Full Assessment (for comparison)" | 2742-2755 | **`App.jsx:2928-2953`** | Delete strip, keep the "View Full Analysis →" button at `:2946-2951` |
| 5 | `categoricalVerdict` trade-log field | 3601 | **`App.jsx:3854`** | Keep unchanged |

**A 6th and 7th consumer §2 item 12 did not enumerate**, found this pass:
- **`App.jsx:1479-1487`** — the verdict badge itself, plus the T/F/S/R
  single-letter chip row at `:1488-1503` directly under it. The chip row
  survives the badge's removal only if it is explicitly re-homed or deleted;
  it is not mentioned anywhere in §7.
- **`frontend/scripts/ui-verify-checklist.js:92-101`** — scrapes the
  `text-4xl font-bold` div and asserts its text is one of `BUY/HOLD/AVOID`.
  This is a *test* consumer of the value being removed, and §7.6 correctly
  anticipated it. See B7 for why it is worse than §7.6 assumed.

### B3. `simplifiedResult.criteria` enumeration — Golden Rule 57 check, clean

`simplifiedScoring.js` builds a 9-key `criteria` object at `:33-43`. Three
generic enumerations depend on the key set:
- `:320` — `Object.values(results.criteria).filter(c => c.pass).length` → `passCount`
- `:329` — `.filter(c => !c.pass).map(c => c.label)` → the "Close but missing" string
- `App.jsx:2817` — `Object.entries(simplifiedResult.criteria).map(...)`, one card
  per key, rendered against the hardcoded `totalCriteria: 9` at
  `simplifiedScoring.js:46` / displayed at `App.jsx:2810`.

**§7's plan adds no top-level key to this object, and must not.** Phase 5
touches the Simple view (delete the comparison strip, flip the default, fix
the PASS-badge copy) — all three are outside `criteria` entirely. Day 117's
precedent is already in the file at `simplifiedScoring.js:112-125`
(`stockReturnPct` nested on `momentum`, with a comment explaining exactly
why). **This constraint is now written into Phase 5's verification step.**

`categoricalResult` (from `runCategoricalAssessment()`,
`categoricalAssessment.js:968-1009`) is **not** generically enumerated
anywhere — every read is a named field. Phase 1's helpers must still be
*standalone exports* that consume `categoricalResult`, never new keys on its
return object; that's what §7.1 already specified, and it's the right call.

### B4. Utility-file shapes confirmed

- `riskRewardCalc.js` — 95 lines. `calculateRiskReward()` `:24-64`,
  `hasViabilityContradiction()` `:71-78`, `getViabilityBadge()` `:86-95`.
  §7.0's line references for the two deletions are **still exact**. Both are
  imported at `App.jsx:46` and used at `:1692` and `:1727` — the import line
  must be edited in the same change or the build warns.
- `positionSizing.js` — 243 lines. `calculatePositionSize()` reads
  `options.vixMultiplier` at `:45`. The duplicated ladder §2 item 10 cites at
  `App.jsx:359`/`:381` is now at **`App.jsx:366`** and **`App.jsx:388`**,
  still byte-identical to each other, still defaulting to `1.0` when
  `vixCurrent == null`. Extraction target unchanged.
- `categoricalAssessment.js` — now **1009 lines**, not 914. §7.1's "append
  after line 914" must become "append after line 1009 (EOF)". The five names
  §1 constraint 1 protects are at `:302` (`assessTechnical`), `:427`
  (`assessFundamental`), `:553` (`assessSentiment`), `:646` (`assessRiskMacro`),
  `:780` (`determineVerdict`).
- `absoluteMomentum.js` — 96 lines, single export `getAbsoluteMomentumRead()`,
  consumed at **`App.jsx:1667`** (Full Analysis RS card) and inside the Simple
  view's Momentum criterion card (`App.jsx:2844+`). **Both call sites sit
  inside surfaces this redesign touches.** Neither is broken by any phase, but
  Phase 3's top-of-page rework and Phase 5's Simple-view edits must preserve
  them verbatim — they are two-day-old shipped work with their own plan doc.

### B5. Anchors inside `categoricalAssessment.js` that §2/§5 cite — all drifted

| §2/§5 cites | Current |
|---|---|
| `assessTechnical()` `:207-318` | `:302`ff |
| `trendTemplateAvailable` (item 1's Unavailable branch) | **`:311`** — exists, exactly as designed against |
| `determineVerdict()` ADX gate `:777-786` | **`:872-877`** (`if (adxValue !== null && adxValue < 20)` … `if (strongCount >= 2)`) — threshold 20 unchanged |
| `assessRiskMacro()` `:551-623` | `:646`ff |
| `getSignalWeight()` called at `:693` | **called at `:788`**, defined `:731` — §3 correction 3 holds, it is still live and still parity-covered |
| `strongCount` from `[technical, fundamental]` `:689-690` | **`:785`** — §2 item 5's "do not remove fundamentals from this array" warning holds |
| `assessFundamental()` ETF branch `:337-345` | **`:431-440`** |
| `assessFundamental()` `'Unknown'` returns `:350`/`:417` | **`:442-450`** and **`:508-515`** |
| ROE band `:383-385` / Revenue `:395-398` / D/E `:408-411` | **`:470-479` / `:484-493` / `:496-506`** |
| `assessSentiment()` silent-fallback `:463-470` | **`:561-562`** — `data.rating: 'Unavailable'` still exists, item 6's display fix still buildable |

### B6. Holding-period copy fix (item 13) — two sites, both present

`App.jsx:1396` (collapsed-header label, `… — Tech 50% / Fund 50%`) and
`App.jsx:1410` (each period button's `title` attribute, same string). §2 item
13 cites `:1366`/`:1379`. The re-assessment effect it says to keep is at
**`App.jsx:272-280`** (cited as `:263-273`).

### B7. Both UI verification scripts are almost certainly already broken

Not in §7. `ui-verify-checklist.js:573-580` and `ui-cohesiveness-test.js:146-151`
both block on `document.body.textContent.includes('Holding Period')` as their
"results have loaded" signal. **"Holding Period" renders only inside the Full
Analysis view** (`App.jsx:1395`, nested under the `analysisView === 'full'`
gate at `:1386`) — grep confirms it appears nowhere else in `src/`. Neither
script ever clicks the view toggle. The default has been `'simple'` since
Day 75; the last committed report from these scripts
(`docs/test/UI_Cohesiveness_Test_Day53_AllPeriods/VERIFICATION_REPORT.md`) is
Day 53. Neither is wired into `package.json`'s scripts.

**Implication, and it is a favourable one:** §7.6's "update the assertions"
task is larger than stated (the scripts need to *run at all* first), but
**Phase 5's default flip to `'full'` fixes their entry point for free.** This
changes the recommended sequencing — see §E.

---

## §C — Corrections found, with evidence

### C1 — §6's R:R below-1.0 note describes a bug that was fixed on Day 112 (MUST FIX)

§6 currently prescribes this permanent on-card text:

> • This ratio is computed from the S&R levels shown above. Those levels come
> from a pivot method that selects the most price-extreme levels in range, not
> the nearest ones — a known open issue (Day 108, now Golden Rule 53).

**This is false as of Day 112.** `backend/support_resistance.py:53-60`:
```python
pivot_max_levels: int = 5
# Day 112 (Golden Rule 53 remediation): select the N pivots NEAREST to …
pivot_nearest_selection: bool = True
```
and `:1130-1161`:
```python
if cfg.pivot_nearest_selection:
    res_pool = sorted(h for h in highs if h > price)                  # ascending — nearest first
    sup_pool = sorted((l for l in lows if l <= price), reverse=True)  # descending — nearest first
    ...
    selection = "nearest"
```
Confirmed closed in `docs/claude/versioned/KNOWN_ISSUES_DAY118.md` and
re-baselined in `SR_PIVOT_FIX_REBASELINE_DAY112.md`.

**Replacement copy must instead disclose what is *actually* uncertain about
the levels today**, using two fields that did not exist on Day 109:
- `meta.pivotSelection` (`backend/backend.py:1816`, values `"nearest"` /
  `"extreme"`) — tells the card which selection path produced these levels.
- `meta.resistanceProjected` (`backend/backend.py:1822`) — true when the
  ticker is at/near all-time highs and `suggestedTarget` is an ATR/Fibonacci
  **projection, not real overhead supply**. Since `calculateRiskReward()`'s
  reward leg is `srData.suggestedTarget` (`riskRewardCalc.js:27`), an
  ATH ticker's displayed R:R is built on a synthetic target — and **nothing
  on the Trade Setup card says so today.** That is the honest caveat this
  note should carry.

This is a copy correction, not a decision change: item 7 (R:R = Info) is
unaffected.

### C2 — §6's R:R footnote describes a Pattern-Detection formula that no longer exists (MUST FIX)

§6's persistent footnote says:

> The Pattern Detection card's R:R uses a fixed target multiple (1.12-1.20×
> pivot), not real resistance.

**False as of Day 112/118.** `categoricalAssessment.js:57-84`:
```
Day 112 (GR53 remediation, Phase 1): measured-move price target.
Replaces the old flat `targetMultiplier` (1.20 C&H / 1.12 Flat Base …)
```
`measuredMoveTarget()` at `:67-84` projects real cup depth / base height from
the pivot. `vcpTarget()` at `:112-128` returns **nearest real resistance**
above the pivot (guarded by `!srData?.meta?.resistanceProjected`), falling
back to measured contraction depth. `buildActionablePattern()` at `:143-146`
returns `riskReward: null` rather than fabricating one when no target exists.

§6's footnote must be rewritten to describe **three** R:R quantities that
genuinely still differ (pullback 2×ATR stop, momentum 1.5×ATR-below-support
stop, and the backend's `risk_reward_context` percentage ratio) — and Pattern
Detection should be *removed* from the "beware, it's fake" list, because it
isn't anymore.

### C3 — §2 item 11's caveat and §9's "Pattern Detection fixed-multiple R:R" open item are closed

Same evidence as C2. No work required; the open-items table should record them
as closed by Days 112/118, not scheduled.

### C4 — §9's negative-EPS open item is answerable now, and the answer is "don't build it"

§5's table leaves "Negative EPS" **OPEN — needs a data-shape check first**,
correctly citing Golden Rule 3. The check is now done:

- `backend/providers/base.py:31` — `'epsGrowth',  # EPS growth rate (decimal or %)`
- `backend/providers/yfinance_provider.py:166` —
  `data['epsGrowth'] = round(((current_eps - year_ago_eps) / abs(year_ago_eps)) * 100, 2)`
- `backend/providers/alphavantage_provider.py:13` —
  `EARNINGS → quarterly EPS → YoY epsGrowth (Q[0] vs Q[4])`

**`epsGrowth` is a YoY growth *rate*, never an earnings *level*.** A negative
value means earnings fell, not that the company is unprofitable — and the
`abs(year_ago_eps)` denominator makes the sign actively misleading when the
prior year's EPS was itself negative (a loss narrowing from −$2.00 to −$0.50
yields *positive* `epsGrowth`). **Decision: do not add a negative-EPS red
flag.** The red-flag screen ships with the three metrics §5 already specifies
(revenue ≤ −10%, D/E > 2.0, ROE < 0). §9's item closes as "checked, declined."

### C5 — §7.1's helper name `describeRegimeGate()` contradicts item 4's own Day 110 reversal

§7.1 tells the implementer to write `describeRegimeGate()`. Item 4's Day 110
revision makes Regime **Info, not a gate**, explicitly with "no enforcement
language." A function named `…Gate()` is exactly the kind of name-overstates-
the-computation problem Golden Rule 53 exists for. **Rename to
`describeRegimeRead()`** to match the Technical Read / Volume Read /
Absolute Momentum Read naming already shipped
(`getVolumeConfirmationRead`, `getObvHorizonRead`, `getAbsoluteMomentumRead`).

### C6 — §7.0's "5 parity-exported functions" is 4

`frontend/scripts/verdict_grid.mjs:20-25` imports exactly:
`assessTechnical`, `assessFundamental`, `assessRiskMacro`, `determineVerdict`.
`assessSentiment` is **not** imported — the script's own docstring (`:12-16`)
states sentiment is hardcoded `'Neutral'` throughout. §1 constraint 1's
protection of `assessSentiment()`'s signature is therefore a *convention*, not
a test contract. Item 6's display-layer Unavailable fix was already scoped as
display-only, so nothing changes in practice — but the plan should say 4, not
5, so nobody spends time "protecting" the wrong thing.

### C7 — §7.6's dead-code deletion should absorb the whole already-enumerated batch

§7.3 has the implementer delete `generateActionableRecommendation()`
(`App.jsx:910`, zero callers — re-confirmed by grep this session). But
`CLAUDE_CONTEXT.md`'s "Zero-risk cleanup batch" item 8 already names **five**
confirmed-dead `App.jsx` functions: `cacheResult`, `getViabilityStyle`,
`generateActionableRecommendation`, `generateScoreExplanation` (`:1062`),
`getSubScoreInfo` (`:1104`). The last two are the exact pair §9's
`scoringEngine.js` landmine entry says must be deleted "in the same pass as
item 3's other dead-code cleanup." **Delete all five in Phase 3**; that
closes a §9 open item at zero marginal cost.

### C8 — The ETF branch the red-flag screen depends on covers 26 hardcoded tickers

§5 display rule 2 says ETFs get "Not applicable — ETF," reusing the existing
`isETF` branch. That branch is
`categoricalAssessment.js:46-48` — a hardcoded 26-symbol array, **duplicated
verbatim** at `scoringEngine.js:33-36`. Any ETF outside those 26 (`SMH`,
`XBI`, `SOXX`, every sector proxy the Sectors tab itself uses) will fall
through to the real fundamentals path and can render **"No red flags found"**
for an instrument with no balance sheet — precisely the falsely-reassuring
collapse §5 display rule 1 forbids. Not a blocker, but Phase 4 must state
this limitation in the card's own honesty line rather than let the screen
imply coverage it doesn't have. (Deduplicating the two lists is a separate,
optional cleanup; it is *not* required for this redesign and touches
`scoringEngine.js`, which §9 already flags as a landmine.)

### C9 — Line-reference drift is total; treat §7's anchors as historical

Every file:line in §2/§7 predates roughly 400 lines of `App.jsx` growth
(4523 lines today) and 95 lines of `categoricalAssessment.js` growth. Tables
B2/B5/B6 above are the corrected anchor set. A future session should re-grep
rather than trusting either set blindly.

---

## §D — Freeze safety, re-answered

**Question: is this still safe to build now that the freeze is lifted?**
**Answer: yes — and the case is stronger than it was, not weaker.**

### D1. What actually changed

- `docs/claude/stable/ROADMAP.md` Priority #1 ("Let paper trading accumulate —
  SOLE FOCUS") now reads **`DISCONTINUED (Day 113)`**. The gate that held
  Priority #17 back is gone.
- `backend/paper_trading/daily_job.py:220` — `PROGRAM_DISCONTINUED = True`,
  with Step 3 (`live_signals.get_momentum_signals` / `get_mr_signals`) behind
  `if not PROGRAM_DISCONTINUED:`. **No new signals are generated on any track.**
- Therefore §1 constraint 2's claim ("gates a real, currently-open **Path B**
  signal … at ~44/100 trades") and §8's disclosure ("Fundamentals will keep
  gating real, live momentum-track entries") are **both false today.**
  Path B was retired Day 112; the program was discontinued Day 113.
- **This removes the one genuinely uncomfortable thing about this redesign.**
  §8 had to disclose a UI-says-vs-system-does gap. That gap no longer exists.

### D2. Golden Rule 54 discipline, run fresh — full caller graph

`compute_sr_levels()` — every caller in the repo:

| Caller | Status |
|---|---|
| `backend/backend.py:141` (import), `:1626` (call) | **Live** — the `/api/sr/<ticker>` route this redesign reads from |
| `backend/support_resistance.py:1572` | Module self-test `__main__` |
| `backend/backtest/backtest_holistic.py:57`, `:428` | **Live research harness** — produced Config C and the Day-112 re-baseline |
| `backend/paper_trading/live_signals.py:45`, `:172` | **Dormant** — reachable only via the `PROGRAM_DISCONTINUED`-gated Step 3 |

`categorical_engine`'s `run_assessment` / `determine_verdict` — every caller:

| Caller | Status |
|---|---|
| `backend/backtest/test_verdict_parity.py:31`, `:80` | **Live** — the 86,400-combo JS/Python parity grid |
| `backend/backtest/backtest_holistic.py:47`, `:332` | **Live** research harness |
| `backend/backtest/parameter_stability.py:28-29`, `:205` | **Live** sensitivity harness |
| `backend/backtest/nirmal_validation.py:38`, `:390` | **Live** validation script |
| `backend/backtest/diag_fundamentals_mismatch.py:36` | **Live** diagnostic (the 40%-mismatch measurement) |
| `backend/paper_trading/live_signals.py:47`, `:279` | **Dormant** |

**Finding: the "do not touch" conclusions survive the freeze being lifted,
but for a different reason.** The forward-test justification is gone; the
**parity contract and the backtest harness lineage** are not. Editing
`categorical_engine.py` or `categoricalAssessment.js`'s four exported
functions still breaks the Golden Rule 19 grid test and desynchronises every
backtest result this project has ever published, including the Day-112
re-baseline. Editing `support_resistance.py` still invalidates
`backtest_holistic.py`'s comparability. **Same table, new reasoning — and
the plan should say the new reasoning out loud, so that a future session
doesn't read "the freeze is over" and conclude these files are now fair game.**

### D3. Anything new the fresh check turned up

1. **The two UI verification scripts are silently non-functional** (§B7) —
   they are, in a real sense, "display support that turned out to be
   load-bearing" in reverse: a certification surface everyone assumes is
   green that hasn't been able to run since Day 75.
2. **The verdict badge's T/F/S/R chip row** (`App.jsx:1488-1503`) is a 6th
   consumer of `categoricalResult` sitting directly inside the element being
   removed, not enumerated in §2 item 12's disposition table.
3. **`getViabilityBadge`/`hasViabilityContradiction`'s import at
   `App.jsx:46`** must be edited alongside their deletion — a detail §7.0's
   file table doesn't carry.
4. **Nothing in `backend/paper_trading/` blocks this work.** The only remaining
   live path through that package is ledger wind-down (Steps 1-2), which
   touches neither S&R selection nor the verdict engine's *definition*.

### D4. Corrected §7.0 file table

| File | Touched? | Why (Day 119 reasoning) |
|---|---|---|
| `backend/support_resistance.py` | **NO** | Not forward-test protection anymore — `backtest_holistic.py:57/428` comparability, and this redesign needs nothing from it that Day 112 didn't already ship. |
| `backend/backtest/categorical_engine.py` | **NO** | Python half of the parity contract; 5 live backtest/diagnostic callers. |
| `backend/paper_trading/*` | **NO** | Wind-down only. Nothing to gain. |
| `backend/backend.py` | **NO** | `/api/sr` response shape unchanged. The frontend *starts reading* two already-shipped fields (`meta.pivotSelection`, `meta.resistanceProjected`) and *stops reading* two others (`position_size_advice`, `risk_reward_context`). Zero server change either way. |
| `frontend/src/utils/categoricalAssessment.js` | **ADD ONLY** | The four parity-exported functions stay byte-identical. New helpers appended after **line 1009** (EOF). |
| `frontend/src/utils/riskRewardCalc.js` | Yes | Delete `getViabilityBadge()` `:86-95`, `hasViabilityContradiction()` `:71-78`. `calculateRiskReward()` unchanged. |
| `frontend/src/utils/positionSizing.js` | Yes (small) | Add exported `getVixPositionMultiplier()`; `calculatePositionSize()` unchanged. |
| `frontend/src/utils/simplifiedScoring.js` | **NO** | Phase 5 touches the Simple *view*, never the scoring module. No new `criteria` key, ever (Golden Rule 57). |
| `frontend/src/utils/absoluteMomentum.js` | **NO** | Both call sites preserved verbatim. |
| `frontend/src/utils/volumeThresholds.js` | **NO** | Day 111/112/116 Volume block is re-homed as a whole, not rewritten. |
| `frontend/src/App.jsx` | Yes (bulk) | Display layer only. |
| `frontend/scripts/ui-verify-checklist.js`, `ui-cohesiveness-test.js` | Yes | Assert removed behaviour **and** can't currently reach the view they test (§B7). |
| `frontend/scripts/verdict_grid.mjs` | **NO** | Its 4 imports must keep resolving — that's the proof parity is untouched. |
| `backend/backtest/test_verdict_parity.py` | **NO** | Run it; don't edit it. |

---

## §E — Corrected phase plan

§7's numbering is kept where it holds. Phase 0 is new. Phase 5's position in
the sequence is changed.

### Phase 0 — Copy correction + baseline capture (NEW, do first, ~30 min)

Nothing user-visible ships in this phase. It exists because §6's copy is the
spec for Phases 2-5, and two blocks of it are currently false.

1. Rewrite §6's **"R:R below-1.0 note"** second bullet per Correction C1 —
   drop the pivot-bug apology, replace with a `meta.resistanceProjected`-driven
   caveat about synthetic ATH targets.
2. Rewrite §6's **"R:R footnote"** per Correction C2 — three quantities, not
   four; Pattern Detection removed from the unreliable list.
3. Record the C3/C4 closures in §9 (Pattern-Detection caveat: closed by Day
   112/118. Negative-EPS flag: checked, declined, with the `base.py:31` /
   `yfinance_provider.py:166` evidence).
4. Capture a baseline: run `python backend/backtest/test_verdict_parity.py`
   and record the pass result. Run both UI scripts and record that they
   currently time out (§B7) — so nobody later mistakes a pre-existing failure
   for a regression this work caused.

**Verification:** parity test green (baseline recorded); §6 contains no
sentence asserting an open bug that `KNOWN_ISSUES_DAY118.md` lists as resolved.

> These edits go in `ANALYZE_PAGE_REDESIGN_DECISIONS.md`'s §6/§9 **only** —
> its §2 decisions and §5 thresholds stay untouched, and its §7/§8 stay as the
> historical record, with a pointer added to this file.

### Phase 1 — Additive utilities (unchanged in intent; corrected anchors)

`frontend/src/utils/categoricalAssessment.js`, appended after **line 1009**:
- `deriveTechnicalRead(technicalAssessment, adxData)` → Strong / Developing /
  Weak / **Unavailable**, plus the ADX<20 modifier string. Reads
  `technical.data.trendTemplateAvailable` (`:311`) for the Unavailable branch.
  Reuses the existing `20` from `determineVerdict():872` — never re-derives it.
- `screenFundamentalRedFlags(fundamentalResult)` → one of four states
  (`no_flags` / `flags` / `unavailable` / `not_applicable`), from §5's three
  triggers. Consumes `assessFundamental()`'s already-computed output; never
  calls its internals.
- **`describeRegimeRead(riskMacroResult)`** (renamed per C5) → Favorable /
  Neutral / Unfavorable + §6's post-reversal copy. No imperative language.

`frontend/src/utils/positionSizing.js`:
- `export function getVixPositionMultiplier(vix)` — the exact `1.0 / 0.75 /
  0.50` ladder currently duplicated at `App.jsx:366` and `:388`, plus an
  explicit `{ multiplier, isDefault }` shape so the "VIX unknown → 1.0×" case
  can be surfaced rather than silently applied (§2 item 10).

**Verification for Phase 1:**
1. `python backend/backtest/test_verdict_parity.py` — still green. Nothing at
   or above `categoricalAssessment.js:1009` moved, so it must be.
2. `node frontend/scripts/verdict_grid.mjs` resolves its 4 imports.
3. `npm run build` — no new warnings; the new exports are defined but not yet
   imported anywhere (acceptable, and expected, at this phase).
4. **Zero visible change** in the app. Load a ticker; the page is identical.

### Phase 2 — Trade Setup card

Target: `App.jsx:1683-2097` (the `{srData && (` block).

- Delete the viability badge header block (`:1689-1720`), including the
  `getViabilityBadge` call at `:1692` and the "⚠️ Stock not recommended"
  warning at `:1711-1715` (consumer #1).
- Delete the `position_size_advice` block **with its suppression condition**
  (`:1749-1756`, consumer #2) and the "R:R Context" line (`:1762-1764`).
- Delete `hasViabilityContradiction` usage (`:1727`) and its contradiction
  branches in the advice banner's class/label logic (`:1731-1747`).
- Delete both `Position` rows — pullback `:2017-2022` (ADX-derived) and
  momentum `:2072-2075` (**the hardcoded `half`**, live since Day 39).
- Delete the `!pullbackViable` / `!momentumViable` opacity + `⛔ R:R < 1`
  treatments (`:1986-1993`, `:2040-2047`) — panels render at full opacity.
- Replace the R:R rows' color ramps (`:2015`, `:2070`) with plain gray.
- Add the Sizing Inputs grid (§6) with both unconditional CTAs wired to
  `autoFillPositionCalculator()` (`App.jsx:377`).
- Add the corrected below-1.0 note + footnote from Phase 0.
- **Leave the Day 111/112/116 Volume block (`:1844-1915`) exactly as-is.** It
  is two-plan-docs deep and already embodies the target pattern.
- Edit the import at `App.jsx:46` down to `calculateRiskReward` only.
- Delete `getViabilityBadge()` / `hasViabilityContradiction()` from
  `riskRewardCalc.js`.

**Verification for Phase 2:**
1. `grep -rn "position_size_advice\|risk_reward_context" frontend/src/` → **0 hits.**
2. `grep -rn "getViabilityBadge\|hasViabilityContradiction" frontend/src/` → **0 hits.**
3. `grep -rn "text-yellow-400\">half<" frontend/src/App.jsx` → **0 hits** (the
   Day-39 fabrication is gone).
4. Load a known-bad-R:R ticker: **both** entry panels render at full opacity,
   no `⛔`, no `NOT VIABLE` badge, R:R prints gray.
5. Load an at-all-time-highs ticker (`meta.resistanceProjected === true`): the
   card says so. Load a normal ticker: it doesn't.
6. `npm run build` clean.

### Phase 3 — Top of page (Technical Read + Regime read) + dead-code batch

- Replace the verdict badge (`App.jsx:1479-1487`) with the Technical Read
  chip driven by `deriveTechnicalRead()`. **Explicitly decide the T/F/S/R chip
  row at `:1488-1503`** (§D3 finding 2) — recommend deleting it; the same four
  letters already render in the Assessment Breakdown header at `:2521-2525`.
- Add the page subtitle and the Regime read band from
  `describeRegimeRead()`, expanded by default (item 4's one retained
  asymmetry — a display default, not a rule).
- Rewrite the holding-period label at `App.jsx:1396` **and** the per-button
  `title` at `:1410` to the horizon-only string (item 13's required copy fix).
- Demote the Fundamentals-unavailable banner (`:1516-1550`) into Phase 4's
  Context card.
- **Delete all five dead functions** (C7): `generateActionableRecommendation`
  (`:910`), `generateScoreExplanation` (`:1062`), `getSubScoreInfo` (`:1104`),
  plus `cacheResult` and `getViabilityStyle`. This closes §9's
  `scoringEngine.js` landmine item. Ordinary dead-code cleanup — **not** a UX
  claim (§3 correction 1).

**Verification for Phase 3:**
1. No `BUY`/`HOLD`/`AVOID` string renders anywhere in the Full Analysis view
   (`grep` the rendered DOM, not just the source — the Assessment Breakdown's
   reason text at `:2684` quotes `verdict.reason`, handled in Phase 4).
2. A ticker with `trendTemplateAvailable === false` shows **"Technical Read:
   Unavailable"**, not "Weak."
3. A ticker with ADX < 20 and Strong technicals shows the
   `· trend not yet confirmed (ADX x.x)` modifier.
4. `npm run build` — the five dead-function warnings are **gone** and no new
   ones appear.
5. `python backend/backtest/test_verdict_parity.py` — still green
   (`determineVerdict()` untouched).

### Phase 4 — Fundamentals context card + Assessment Breakdown

- New "Context — not part of the read" card: `screenFundamentalRedFlags()`
  output + the Sentiment read, prominence driven by `holdingPeriod`.
- Four states, never three (§5 display rule 1). **Include the C8 ETF-coverage
  caveat** in the card's honesty line.
- **No negative-EPS flag** (C4).
- `AssessmentTile` for Fundamental (`App.jsx:2538-2543`) gains
  `infoLabel="(info)"` + `opacityMuted`, matching Sentiment's existing
  treatment at `:2548-2559`.
- Sentiment card distinguishes `Neutral (F&G 47)` from `Unavailable` via
  `data.rating` (`categoricalAssessment.js:561-562`).
- Reframe "💡 Why This Verdict?" (`App.jsx:2675-2688`, consumer #3) to "How
  this read was formed" — neutral container, driven by the Technical Read +
  Regime read, **not** `categoricalResult.verdict.reason`. Remove the
  BUY-criteria line at `:2686-2687`.

**Verification for Phase 4:**
1. A ticker with no fundamentals returns **"Screen unavailable"**, never
   "No red flags found."
2. `SPY` returns **"Not applicable — ETF."** `SMH` (not in the 26-ticker list)
   is checked manually and the caveat line is confirmed present.
3. A ticker with revenue growth between −10% and 0% shows **no** flag
   (§5's deliberately-widened trigger), and the card's honesty line explains
   why the thresholds sit where they do.
4. `python backend/backtest/test_verdict_parity.py` — still green.

### Phase 5 — Simple-view reconciliation + default flip

*Sequencing note: still after Phase 3 (vocabulary consistency), but now
explicitly **before** Phase 6, because flipping the default is what makes
Phase 6's scripts able to reach the view they test (§B7).*

- Delete the "Full Assessment (for comparison)" strip (`App.jsx:2928-2953`,
  consumer #4); keep the "View Full Analysis →" button (`:2946-2951`).
- Change `App.jsx:155` `useState('simple')` → `useState('full')`.
- PASS-badge copy fix at `App.jsx:2807-2811`: `⏸️ PASS` →
  `{passCount}/9 criteria met — No Trade`. **Zero logic change** — do not
  touch `simplifiedScoring.js`.

**Verification for Phase 5:**
1. `grep -n "totalCriteria" frontend/src/utils/simplifiedScoring.js` → still
   `9`; `git diff --stat frontend/src/utils/simplifiedScoring.js` → **no
   changes at all**. (Golden Rule 57 guard.)
2. Load any ticker at `2/9`: the Simple view reads "2/9 criteria met — No
   Trade," never a bare "PASS."
3. Fresh page load lands on **Full Analysis**; the toggle still switches both
   ways; the Simple view's 9 cards and its Day-117 absolute-momentum sub-line
   (`App.jsx:2844+`) render unchanged.
4. Log a manual trade from the Trade Log tab — `categoricalVerdict`
   (`App.jsx:3854`, consumer #5) is still populated. This is the one consumer
   that must **survive**, and it's easy to break by accident while deleting
   the others.

### Phase 6 — Tests + docs (same commit as Phases 2-5)

- `ui-verify-checklist.js`: rewrite CHECK 1 (verdict is `BUY/HOLD/AVOID`),
  CHECK 4 (position-size banner visibility), CHECK 5 (R:R gray-out), CHECK 6
  (AVOID+VIABLE conflict) — **all four assert behaviour this redesign
  deliberately removes.** Note that its `waitForFunction` on "Holding Period"
  (`:573-580`) now works, because Phase 5 flipped the default.
- `ui-cohesiveness-test.js`: same wait condition at `:146-151`; the manual
  checklist it emits at `:342-344` asserts three removed behaviours.
- Update `HOW_STOCK_PICKING_WORKS.html`, `README.md`, `DEVELOPER_ONBOARDING.md`.
- Add the Scan-tab disclosure line under `App.jsx:3176`'s "STA Verdict" column
  header (§6, item 12's cross-tab resolution).
- `ROADMAP.md` Priority #17 → implemented; note the freeze framing is
  historical.
- Append a Day 119 entry to `ANALYZE_PAGE_REDESIGN_DECISIONS.md`'s §10 change
  log pointing at this file.

**Verification for Phase 6:**
1. Both scripts **run to completion** against 3+ tickers (they can't today).
2. Every rewritten assertion fails if the corresponding Phase 2-5 change is
   reverted — i.e. the tests actually test the new behaviour rather than
   passing vacuously.
3. `grep -rn "NOT VIABLE\|Position Size:\|R:R < 1" frontend/scripts/` → 0 hits.

### Sequencing (corrected)

```
Phase 0  (copy + baseline)      ─┐
Phase 1  (additive utilities)    ├─ must land first, in order
                                 ┘
Phase 2 ─┐
Phase 3 ─┼─ independent of each other, any order
Phase 4 ─┘   (Phase 4 consumes Phase 3's banner demotion — do 3 before 4)
Phase 5      after Phase 3
Phase 6      same commit as 2-5, always
```

Deviation from §7.7: Phase 4 now has a soft dependency on Phase 3 (the
Fundamentals-unavailable banner moves from the top of the page into Phase 4's
card), and Phase 6 is explicitly downstream of Phase 5's default flip.

---

## §F — Go / No-Go

### **GO.**

The 17 decisions are sound and unchanged. Nothing shipped Days 112-118
conflicts with them — Day 115 and Day 118's own code comments cite this
doc's descriptive-state convention as the pattern they were following
(`App.jsx:2132-2136`, `:2160-2164`), and Day 116/117 shipped two more
Info-not-gate reads on the very card Phase 2 rebuilds. The redesign is
finishing a direction the codebase has already been moving in for six days.

The freeze question resolves cleanly: the forward-test program is
discontinued, the sole-focus gate is lifted, and the one genuinely
uncomfortable disclosure in §8 has dissolved. The "don't touch the backend"
conclusions survive on parity-and-backtest-comparability grounds, which the
corrected §D4 table now states explicitly.

Three things must not be skipped:
1. **Phase 0 is not optional.** §6's copy currently contains two statements
   that were true on Day 109 and are false today. Shipping them would put a
   fabricated open bug and a fabricated "fixed multiple" formula in front of
   the user — in copy whose entire purpose is honesty.
2. **The `simplifiedResult.criteria` key set is frozen at 9.** No phase adds
   to it. Verified in Phase 5 by a `git diff --stat` that must come back empty
   for `simplifiedScoring.js`.
3. **Run `test_verdict_parity.py` at the end of every phase**, not just at
   the end. It is fast, it is the contract, and it is the single check that
   distinguishes "display-layer redesign" from "quietly edited the engine."

### The very first phase, and how to verify it before moving on

**Start with Phase 0, then Phase 1.**

Phase 1 is the right first *code* phase for the same reason §7.7 gave: it is
purely additive, it lands the helpers Phases 2-4 consume, and it is
independently verifiable with **zero visible change to the app**. That last
property is what makes it a good first move — if anything about the parity
contract is going to break, it breaks here, in a phase where nothing else is
in flight to confuse the diagnosis.

Before moving to Phase 2, a future session must confirm all four:

1. `python backend/backtest/test_verdict_parity.py` passes — same result as
   the Phase 0 baseline, all 86,400 combos.
2. `git diff frontend/src/utils/categoricalAssessment.js` shows **only**
   additions after line 1009. Nothing above it moved by even one line.
3. `npm run build` succeeds; the only new warnings are "defined but never
   used" for the three new helpers — which is correct at this stage, and
   should disappear by Phase 4.
4. Load three tickers in the browser (one Strong, one with ADX < 20, one ETF)
   and confirm the page is **pixel-identical** to the Phase 0 baseline.

If any of those four fails, stop and diagnose before Phase 2 — a parity break
at Phase 1 means a helper reached into an internal it shouldn't have, and it
is far cheaper to find there than after 400 lines of `App.jsx` have moved.
