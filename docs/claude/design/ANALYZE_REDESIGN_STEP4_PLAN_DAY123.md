# Analyze Page Redesign — Step 3 hardening + Step 4 plan (Day 123)

Status: DRAFT, for independent review (Fable) before any code is written.
Source of truth for the design: mockup v0.14
(`docs/claude/design/mockups/analyze_page_redesign_mockup.html`) and
`ANALYZE_PAGE_REDESIGN_DECISIONS.md` (Day 122–123 entries).

## 0. Engineering standard for every step from here (user, Day 123)

1. **Plan first, reviewed by Opus/Fable**, then code.
2. **No silent failures.** Every card has three distinct states: loading,
   "couldn't load (reason)", and real data. A missing input never turns into
   a plausible-looking number (no `|| 0`, `|| 50`, `* 1.10`).
3. **Logging.** Frontend: one `console.warn('[STA][<card>] <ticker>: <what is
   missing>')` per missing input per render cycle that changes the UI (not per
   re-render — guard with `useEffect` on the ticker+reason key). Backend:
   `logger.warning` with ticker when a field the UI needs comes back empty.
4. **Exception handling.** Pure helpers never throw on bad input; they return
   `{ state: 'unavailable', reason }`. Components never index into a possibly
   null object without a guard. No bare `catch {}`.
5. **Performance.** Helpers are pure and O(n) over at most 260 bars; the
   component memoizes derived reads with `useMemo` keyed on the input objects.
   No new network calls in Step 4.
6. **Genuine logic.** Every number shown traces to one engine function (Golden
   Rule 59). Every helper gets a Node unit check of its edge cases.
7. **Every UI element has backend data.** Table in §3 lists each one.

## 1. Step 3 hardening (Trade Setup, already built — fix before Step 4)

Findings from re-reading Step 3 against §0:

| # | Problem | Fix |
|---|---|---|
| H1 | `fetchSupportResistance` returns `null` on any error (`api.js:409`), and `App.jsx` renders the card only `{srData && …}`. A failed S&R fetch makes the whole Trade Setup card vanish, no message. | Keep returning null from the fetcher (other callers — scan, watchlist — rely on null-per-ticker), but render the card shell whenever an analysis result exists, with "Couldn't load support/resistance levels for TICKER. The rest of the page is unaffected." when `srData == null`. |
| H2 | `riskRewardCalc.js:32` `atr = meta.atr \|\| 0`. Missing ATR → stop = support, risk 0, ratio hidden, card still looks complete. | `atr` missing/≤0 → return `{ state: 'no_atr', entry, target }`; card shows Buy and Target, Stop tile says "ATR unavailable, can't place the stop". |
| H3 | `calculateRiskReward` returns bare `null` for both "no support" and "no srData". | Return `{ state: 'no_data' \| 'no_support' \| 'no_atr' \| 'ok', ... }`. PullbackPlan switches on `state`. |
| H4 | Backend `backend.py:1769` `atr_value = meta.get('atr') or 0` feeds `suggestedStop`. | Read it, confirm whether a 0 ATR can reach the Simple view's stop; if yes, return `suggestedStop: null` with `logger.warning`. (Investigate only; fix if confirmed.) |
| H5 | Chip row left mis-indented after Step 3. | Moved in Step 4 anyway (§2.4). |

## 2. Step 4 scope — Technical Read + Regime at the top

### 2.1 Regime band (Info, expanded by default)
- New `components/RegimeRead.jsx`, driven by existing
  `describeRegimeRead(categoricalResult.riskMacro)`. Three colours + gray
  Unavailable. Placed directly under the header card.

### 2.2 Technical Read card (new `components/TechnicalRead.jsx`)
Driven by `deriveTechnicalRead(categoricalResult.technical, adxData)` plus a
new pure helper. Sections, top to bottom (mockup v0.14):
1. **Read line:** Strong / Developing / Weak / Unavailable, plus the ADX
   modifier. Wording change already decided Day 122: "taking a breather:
   moving sideways for now (ADX n)" — update `deriveTechnicalRead`'s
   `adxModifier` text (display-only, not parity-tested).
2. **Four trend checks** (above 200-day SMA; 200-day SMA rising; above 50-day
   SMA; within 25% of 1-year high) — read from
   `patternsData.trendTemplate.criteria` (the same object the engine counts),
   values from `sma_values` / `price_position`.
3. **"Strong needs all three" tiles:** trend `criteria_met`/8 (needs 7+),
   RSI(14) (needs 50–70), RS vs S&P 500 (needs ≥1.0, shown as ±% =
   `(rs52Week − 1) × 100`). ✓/✗ computed with the **same comparisons as
   `assessTechnical` line 342**, via one exported helper
   `strongCriteria(technicalAssessment)` that line 342's values come from
   (`data.rsi`, `data.rs52Week`, pass count). No new threshold literals in
   the component.
4. **"momentum n/a"** when RSI is missing instead of the engine's silent
   `|| 50` (display only; engine untouched, decided Day 122).
5. **Entry checks (Info only):**
   - Timing: distance of price from the 21-day EMA in ATR units. Bands
     ≤1 ATR "close", 1–2 "extended" (still Yes), >2 "stretched" (Keltner
     default). Below the EMA → "Not yet, below it". Not Strong/Developing →
     "Not applicable: not in an uptrend". Labelled "rules of thumb, untested".
   - Volume: 20-day volume bars + 50-day average line, plus the three
     existing votes from `getVolumeDirectionRead` (day change, close
     location, OBV trend). Today's bar drawn hatched and excluded from the
     average while `meta.candle.barComplete === false` (Day 116 rule).
6. **"How this read was formed"** details (copy from mockup).

### 2.3 What moves / goes
- The Day 111/116 volume block moves from Trade Setup into Entry checks'
  "why?" area unchanged in logic (same helper calls, same prevBar guard).
- T/F/S/R letter row under the verdict badge: delete (duplicates the
  Assessment Breakdown header, Day 119 plan §E Phase 3).
- Verdict badge (BUY/HOLD/AVOID) in the Full view: replaced by the Technical
  Read chip, per Day 119 plan. **Open question for review:** Simple view keeps
  its verdict; confirm no other consumer reads the removed DOM.

### 2.4 Indicator chip row (ADX / 4H RSI / OBV / Vol / DIST)
Decision: ADX → already in the read line; OBV, Vol → already in Entry
checks votes; **DIST** → becomes a fourth line in Entry checks ("Heavy volume
with OBV falling: big holders may be selling") using the same
`distRvol ≥ 1.5 && obv.trend === 'falling'` expression, moved not copied.
**4H RSI** → dropped from the Analyze page (its tooltip refers to "momentum
entries", which no longer exist). Net: the chip row is deleted with nothing
lost except 4H RSI.

### 2.5 Dead code
Delete `cacheResult` (`App.jsx:288`), `getViabilityStyle` (879),
`generateActionableRecommendation` (910), `generateScoreExplanation` (1062),
`getSubScoreInfo` (1104). Grep each for callers first.

## 3. Data backing every element

| UI element | Source | Exists? |
|---|---|---|
| Read, detail | `assessTechnical` → `deriveTechnicalRead` | yes |
| 4 trend checks ✓/✗ | `patterns.trendTemplate.criteria` | yes |
| "$224.80 vs $196.40" | `trendTemplate.sma_values`, `price_position` | yes |
| "200-day up 2.1% from a month ago" | `sma_200_30d_ago` | **no — computed in `check_trend_template` but not returned.** Add `sma_200_30d_ago` to `sma_values` (additive key, backend). |
| Strong tiles | `technical.data.{trendTemplateScore,rsi,rs52Week}` | yes |
| 21-day EMA | `calculateEMA(closes, 21)` from `stock.priceHistory` (frontend, `technicalIndicators.js`) | yes, computed client-side |
| ATR | `srData.meta.atr` (same ATR the Trade Setup stop uses) | yes; missing → timing shows "ATR unavailable" |
| 20-day volume bars | `stock.priceHistory[].volume` | yes |
| votes | `srData.change`, `meta.candle.closeLocation`, `meta.obv.trend`, `meta.prevBar` | yes |
| barComplete | `srData.meta.candle.barComplete` | yes |
| Regime | `categoricalResult.riskMacro` → `describeRegimeRead` | yes |

Open data question for review: EMA21 from the frontend's `priceHistory` vs
the backend's own price frame — same provider chain? If priceHistory's last
bar is a partial bar, EMA uses a partial close. Acceptable (timing is about
"now") but must be stated.

## 4. New helper (pure, in `categoricalAssessment.js` display section)

`deriveEntryChecks({ technicalRead, priceHistory, currentPrice, srMeta, change })`
→ `{ timing: {state, emaValue, atrUnits, pctFromEma, answer} , volume: {state,
bars[20], avg50, todayPartial, votes[], agree, answer}, distribution: bool }`.
`state` ∈ `ok | unavailable` with `reason`. Never throws.

## 5. Verification

1. `npm run build`: 5 dead-function warnings gone, no new warnings.
2. `python backend/backtest/test_verdict_parity.py` green (engine untouched).
3. Node unit checks for `deriveEntryChecks`, `strongCriteria`, hardened
   `calculateRiskReward`: missing RSI, missing ATR, < 21 bars, partial bar,
   all-null votes, below-EMA, >2 ATR, not-uptrend.
4. Live in the app (Playwright): NVDA, one Weak ticker, one ETF (SPY), one
   all-time-high ticker, one bad ticker (forces S&R failure path). Screenshot
   desktop + 390px.
5. Cross-check on screen: tile ✓/✗ agrees with the read (Strong ⇔ all three
   ✓) for all 5 tickers.
6. Console: only the expected `[STA]` warnings.
7. Three escalating review passes (Golden Rule 41) on the diff.

## 6. Out of scope (later steps)
MR card (5), Fundamentals (6), default flip + Simple-view copy (7), test
scripts + docs (8), momentum no-cap backtest.

## 7. Independent review (Fable, Day 123) — GO WITH FIXES, all accepted

Reviewer claims 1, 2, 4, 10 re-verified against code before accepting.

| # | Finding | Plan change |
|---|---|---|
| R1 MUST | Missing RSI becomes 50 before display (`categoricalAssessment.js:314`, `runCategoricalAssessment :981`), so "momentum n/a" can't be detected; the engine also counts that 50 as a pass at :342. | Add additive `data.rsiAvailable` in `assessTechnical`. Tile shows "RSI unavailable, engine assumed 50 (counts as pass)" — honest about the engine, not ✗. **Logged as an engine bug** (fabricated neutral value, same class as Day 78 RS fix); fixing it changes verdicts, so it gets its own parity-tested change, not Step 4. |
| R2 MUST | `trendTemplateScore` is the string "7/8"; no numeric count to reuse. | Add additive `data.trendTemplatePassCount`; new `strongCriteria()` reads `passCount`, `rsi`, `rs52WeekAvailable && rs52Week >= 1.0` exactly as :342. Parity hook must stay green. |
| R3 MUST | Trend template missing has two causes: `/api/patterns` failed vs < 252 bars of history (`pattern_detection.py:247`), neither logged. | Backend `logger.warning` with ticker and bar count; card shows "under 1 year of history (n bars)" vs "pattern detection failed". |
| R4 SHOULD | H4 restated: backend substitutes a fake 3% stop when ATR is missing (`backend.py:1769-1774`), shown and used for sizing in Simple view. | `suggestedStop = None` + `logger.warning`; Simple view shows "stop unavailable (no ATR)". |
| R5 SHOULD | S&R levels, MTF badge, volume block all sit inside `{srData && …}`. | Card shell always renders; each S&R-dependent section shows "S&R data unavailable"; Entry-checks votes/DIST have their own unavailable state. |
| R6 SHOULD | EMA21 already computed in `scoringEngine.js:109`. | Read `analysisResult.breakdown.technical.indicators.ema21`; no second EMA. < 200 bars → timing "unavailable (under 200 days of history)". |
| R7 SHOULD | Two ATRs exist (scoringEngine vs `srData.meta.atr`). | Use `srData.meta.atr` only (same as the stop); never fall back to the other. State that it includes today's partial bar. |
| R8 SHOULD | barComplete comes from /api/sr, bars from /api/stock. | If srData missing, bar state is "unknown" (not assumed complete); warn if `priceHistory` last date ≠ `meta.candle`/`prevBar` date logic. |
| R9 SHOULD | "Not applicable: not in an uptrend" is false for Weak caused by RSI > 80 with 8/8 trend. | Wording: "Not shown: the read is Weak". |
| R10 SHOULD | rs52Week is a ratio of growth factors; (rs−1)×100 isn't "beat by X%". | Tile ✓ on ratio ≥ 1.0 (unchanged); text shows "stock +50% vs S&P +20%, past year" from `stockReturn52w`/`spyReturn52w` (equivalent test, ratio ≥1 ⇔ stock gain ≥ S&P gain). |
| R11 SHOULD | `ui-verify-checklist.js:93-111`, `ui-cohesiveness-test.js:207-226` scrape the verdict badge and T:X row. | Known breakage, rewritten in Step 8. `cacheResult`: drop binding, keep the `await`. |
| R12-14 NIT | null `sma_200_30d_ago` on cached responses; one shared `useMissingInputWarning` hook; SPY shows RS 1.00×. | Accepted. |

## 8. Code review (Fable, after build) — no MUST-FIX; all SHOULD-FIX applied

1. `priceStructureNarrative.js` `?? 1.0` RVOL fake → null; watch item says "volume unavailable". (`atr || 0` there is inert: `isNearLevel` returns false at 0.)
2. Missing SPY data read as "SPY below 200-day / downtrend" → additive `riskMacro.data.spyAvailable`; band says "SPY trend unavailable" and that the engine assumed a downtrend. **Engine bug logged** (same class as the RSI `|| 50`).
3. Young ticker (< 100 bars, `/api/patterns` 400) said "try again" → `deriveTrendChecks(patternsData, historyBars)` maps it to short history.
4. "Today:" on a past session (pre-market/weekend) → backend `candle.date`; labels say "Last session (date)" / "from the date session".
5. "the 4 below" → "the 4 above".
6. Empty priceHistory now warns.
7. Simple Checklist: with no stop it fails setup visibly ("Stop unavailable (ATR missing)") instead of switching formulas; Simple view says why the sizing button is missing.
8–10. Date-mismatch warning names the window difference; flat close not coloured green; RS shown to 1 decimal; "floored at $0.01" when the stop floor applies; bars require a date for keys.
9. Backend logging stays `print` with ⚠️ — backend.py has no logger; matching the file convention (a module logger is a separate cleanup).

Re-verified: 34 Node checks, parity 86,400/86,400, build clean, live LLY/NVDA/SPY.
