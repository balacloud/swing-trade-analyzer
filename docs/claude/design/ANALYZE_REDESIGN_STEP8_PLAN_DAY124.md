# Analyze Page Redesign — Step 8 Plan (Day 124)

Last step of the redesign. It covers the UI test scripts, two cleanups and the docs.
Process (Day 123 standard): this plan → Fable review → build test-first → review
passes → user sign-off.

Scope sources: Day 119 plan §B7 and Phase 6, the DECISIONS change log
(lines ~1283, ~1332, ~1408), and the Day 121 baseline (both scripts already
fail at their load wait).

---

## 1. What is wrong today

| # | Item | Evidence |
|---|------|----------|
| 1 | `frontend/scripts/ui-verify-checklist.js` checks the old page. All 8 checks scrape removed elements: the `text-4xl` BUY/HOLD/AVOID badge, the T:/F:/S:/R: chips, the "What's Good" bottom-line card, the momentum/pullback entry cards, the Position Size banner and the VIABLE badge. CHECK 1 also re-implements the old verdict cascade, a second copy of an engine rule (GR59). It waits for "Holding Period", which no longer exists, so it times out on every ticker. It always exits 0, even when every check fails, and it overwrites `docs/test/UI_Cohesiveness_Test_Day53_AllPeriods/VERIFICATION_REPORT.md` (Day 121 lost the Day 53 report this way). | file read Day 124 |
| 2 | `frontend/scripts/ui-cohesiveness-test.js` (PDF capture for manual review) has the same "Holding Period" wait, a `--holding` option that clicks buttons that no longer exist, scrapes the verdict and chips into its report, and emits a manual checklist made of 8 removed behaviours. | `:146-159`, `:189-256`, `:336-346` |
| 3 | `scoringEngine.js:499` computes `qualityGates` and returns it at `:538`. Nothing reads it, because Step 6 removed the Quality Gate Warnings panel. `checkQualityGates()` (`:412`) has no other caller. | grep: only the definition, the call and the return key; no `Object.keys/values/entries` or spread over `analysisResult` |
| 4 | `App.jsx:353` and `:375` contain two copies of the VIX position-size ladder (`<20 → 1.0`, `≤30 → 0.75`, else `0.50`). `positionSizing.js:255 getVixPositionMultiplier()` holds the same ladder (Day 121) but nothing calls it. When VIX is missing the calculator silently uses 1.0×, and redesign item 10 asks for that case to be shown. A NaN VIX falls through to 0.50× silently in both copies. | file read |
| 5 | Docs describe the old page. README lines 36/77/191/698 mention BUY/HOLD/AVOID as shown and the Holding Period selector. `HOW_STOCK_PICKING_WORKS.html` shows the Full Analysis verdict cascade as what the user sees (`:658-672`) and says "PASS" (`:726`). ROADMAP #17 says "Steps 7–8 left". `docs/test/UI_COHESIVENESS_TEST_PLAN.md` describes the old checklist. | grep |

Not in scope: the engine (`categoricalAssessment.js` / `categorical_engine.py`).
Parity stays at 86,400 and the engine still feeds `categoricalVerdict` in the
trade log. Also not in scope: the page-level 390px overflow from the tab bar
(a logged Known Issue).

---

## 2. Design

### 2a. Stable test hooks (display-neutral app change)

Add `data-testid` to each card's root element: `card-market-backdrop`,
`card-stock-header`, `card-technical-read`, `card-mr-read`,
`card-trade-setup`, `card-fundamentals`, `card-price-structure`, and
`card-simple-verdict` for the Simple view badge. Nothing visible changes. The
scripts select cards by these hooks instead of Tailwind class names. Class
scraping is what broke the old script: a restyle silently invalidated it.

### 2b. Checks as a pure module, unit-tested first

New file `frontend/scripts/lib/analyzeChecks.js` (CommonJS so the puppeteer
script can `require` it). It exports `runChecks(dom, api)`, which is pure. `dom` is
what the browser extracted and `api` holds the JSON payloads the page itself
received. The page's responses are captured with `page.on('response')` for
`/api/market/spy`, `/api/market/index/QQQ`, `/api/market/vix`,
`/api/stock/<T>` and `/api/earnings/<T>`. This compares the screen with the
exact payload behind it, so a live VIX tick between the page load and a
second fetch can't cause a false failure.

| ID | Check | Fails if… |
|----|-------|-----------|
| A1 | Card order | `card-market-backdrop` isn't the first card, or Technical Read → Mean-Reversion → Trade Setup → Fundamentals are missing or out of order |
| A2 | Removed elements absent | Any of these appear: a BUY/HOLD/AVOID verdict badge, a T:/F:/S:/R: chip, the text "Holding Period", a Favorable/Neutral/Unfavorable market label, a "Position Size:" banner, a VIABLE/NOT VIABLE badge, "Stock not recommended" |
| A3 | Backdrop matches API | For S&P 500 and QQQ, the ↑/↓ direction and the 1-dp % vs the 200-day and 50-day don't match `trend` from the captured payload, or the drop % and date don't match `biggestDrop10d`. The VIX value (1 dp) and band word must match `/api/market/vix` (`current`, `regime` → `VIX_BAND_LABELS`). A row whose payload failed must say "couldn't load". |
| A4 | Classification line | The header contains "Unknown", or the captured stock payload has `quoteType === 'ETF'` and the header doesn't say "Exchange-traded fund (ETF)" |
| A5 | Earnings badge | The badge's presence doesn't match `hasUpcoming` in the captured earnings payload |
| A6 | No blank cards | A card root holds nothing beyond its title, i.e. it shows neither content nor an explicit couldn't-load message |
| A7 | Data source shown | No provider or "Multi-Source" text (old CHECK 7, kept) |
| A8 | Simple view badge | After clicking Simple, the badge isn't `✅ TRADE` or `⏸️ No Trade` with `N/9`, or it reads TRADE with N < 9, or it says "PASS" |
| A9 | Cards fit at 390px | Any card root has `scrollWidth > clientWidth + 1` at a 390px viewport. Card scope only: the page-level tab-bar overflow is a Known Issue and is reported but not failed. |

`VIX_BAND_LABELS` is imported from `src/utils/marketBackdrop.js` (one place,
GR59). The script runs under Node with an ESM import shim, the same way
`test_market_backdrop.mjs` already imports app utils.

Test-first: `frontend/scripts/test_analyze_checks.mjs` feeds fixtures to
`runChecks` and runs before the browser script exists.
- A fixture of the current page passes every check.
- For each check, a pre-redesign fixture fails it (old verdict badge present,
  backdrop not first, PASS badge, "Unknown • Unknown", backdrop number off
  by 0.1, earnings mismatch, blank card, overflowing card). This meets the
  Day 119 Phase 6 criterion that every assertion fails if its change is
  reverted.
- If extraction can't find a card, the check reports `missing` and fails, never
  a pass by default.

### 2c. Browser runner `ui-verify-checklist.js` (rewrite)

- Wait condition: `[data-testid="card-technical-read"]` or the error banner
  (`bg-red-900/50 border-red-500`, unchanged). If neither shows within 60s,
  that ticker fails with the reason. The default view is now Full, so no
  toggle click is needed.
- Default tickers: AAPL, NVDA, SMH (ETF), JPM (bank), RIVN (negative ROE /
  young). Arguments override them. The `--holding` and `--all-periods` options
  are removed, with a clear error if someone passes them.
- Report goes to a new dated folder `docs/test/UI_Verify_<YYYYMMDD-HHMM>/REPORT.md`,
  so it never overwrites an earlier report.
- Exit code: 1 if any check fails or any ticker errors, 0 only if all pass.
  It prints one line per failure with the check ID and the expected vs actual
  values.
- Services check is unchanged (`/api/health`, frontend 200).

### 2d. `ui-cohesiveness-test.js` (PDF capture, kept, fixed)

- Uses the same wait condition. The `--holding` option is removed.
- Pulls page facts from the test hooks: ticker/name, price, classification
  line, and the Simple badge text (read from the API payload, not by toggling,
  so the PDF stays the Full view).
- Its manual checklist is replaced with the new page's review points: the
  backdrop comes first and is facts only, there is no verdict, each card says
  what it is based on, and couldn't-load states are explicit.
- Output folder is already dated (`UI_Cohesiveness_Test_<date>`). Unchanged.

### 2e. VIX ladder → shared helper

- `positionSizing.js getVixPositionMultiplier`: treat a non-finite value as
  unknown (`!Number.isFinite(vix)` → `{1.0, isDefault:true}`). That is the
  only rule change: NaN went to 0.50× and now goes to 1.0× marked unknown. NaN
  can't arrive over JSON today, so this is defensive only. The docstring is
  updated because the helper is now wired in.
- `App.jsx` `:353` and `:375` change to
  `const { multiplier: vixMultiplier, isDefault: vixUnknown } = getVixPositionMultiplier(rawAnalysisData?.vix?.current);`.
- The calculator result shows a muted line when `vixUnknown` is true: "VIX not
  loaded — no VIX size scaling applied (1.0×). Analyze a stock to load it."
  Every finite VIX gets the same multiplier as before.
- Unit test (`frontend/scripts/test_vix_multiplier.mjs`): the helper equals
  the old inline ladder at 0, 15, 19.99, 20, 25, 30, 30.01, 45. null and
  undefined give 1.0 with isDefault, and NaN gives 1.0 with isDefault (a
  deliberate change from the old 0.50).
- Thresholds stay 20/30. They match the engine's `assessRiskMacro` scale and
  are deliberately separate from the display bands in `vix_bands.py`, as the
  docstring there says.

### 2f. Remove `qualityGates`

Delete `checkQualityGates()` (`scoringEngine.js:409-~478`), its call at
`:499` and the `qualityGates` return key at `:538`. Before deleting, grep
the frontend, backend, scripts and `docs/claude/API_CONTRACTS*` (current
file) for `qualityGates` and `criticalFails` to confirm there are no readers,
and confirm `calculateScore` isn't serialized whole anywhere (trade log,
export). Build check: `npm run build` must show no new warnings, and the
unused-import list must shrink rather than grow.

### 2g. Docs

- README: the feature bullets (36, 77) say the page shows facts and the
  engine's categorical verdict is kept internally for the trade log, not shown.
  The Holding Period bullet (191) is marked removed on Day 123. The methodology
  section (428-494) stays, because it describes the engine that still runs,
  plus one line saying it is not displayed. A v4.64 entry is added.
- `HOW_STOCK_PICKING_WORKS.html`: the Full Analysis panel gets a note that the
  page no longer shows a verdict (facts per card, the user decides). The Regime
  tier text reads as the engine's internal input. "PASS" becomes "No Trade".
  Republish to the existing URL (pass `url` explicitly, per the memory note).
- `DEVELOPER_ONBOARDING.md`: add how to run the three Node unit tests and the
  browser verifier.
- `docs/test/UI_COHESIVENESS_TEST_PLAN.md`: replace the old 8-item checklist
  with A1–A9.
- ROADMAP #17 marked DONE. A Day 124 Step 8 entry goes in the DECISIONS
  change log, and this plan gets a build-notes section.
- Not in this step: API_CONTRACTS, KNOWN_ISSUES and the version bump happen at
  /sta-end as already listed.

---

## 3. Verification

1. Node unit tests: `test_analyze_checks.mjs` (all fixtures),
   `test_vix_multiplier.mjs`, plus the existing `test_market_backdrop.mjs`
   (22) and `verdict_grid.mjs`. Python tests 13/26 and parity 86,400 are
   re-run, unchanged.
2. `node scripts/ui-verify-checklist.js` against the 5 default tickers runs to
   completion and exits 0, with the report in a new dated folder.
3. Mutation proof against the live app: temporarily move `<RegimeRead>` below
   the header, run the verifier for AAPL, and expect A1 to fail with exit 1.
   Then revert. A second temporary change, restoring "PASS" text, should fail
   A8. Both reverts are confirmed with `git diff` before moving on.
4. `node scripts/ui-cohesiveness-test.js AAPL SMH` produces 2 PDFs and a report
   with no verdict/chip columns.
5. Settings calculator: with a stock analysed, the VIX value and multiplier
   match before and after (the limit text appears only when VIX ≥ 20). With no
   stock analysed, the "VIX not loaded" line shows.
6. `npm run build` passes with no new warnings.

## 4. Risks

| Risk | Mitigation |
|------|-----------|
| A3 rounding mismatch (UI `toFixed(1)` vs payload 1-dp) gives false failures | Format the payload with the same `toFixed(1)` in the check, and unit-test the boundary (e.g. 2.25) |
| A ticker's data provider is down during the run | That ticker reports an error and the run exits 1. The report states which ticker and why, and other tickers still run. |
| `data-testid` added to the wrong element (the wrapper vs the card) | A1/A6 fixtures plus the live run catch a missing or empty hook |
| ESM import of `marketBackdrop.js` from a CommonJS runner | The runner is `.js` CommonJS. The check module receives the label map as an argument, and the runner loads it with dynamic `import()`. |
| Removing `qualityGates` breaks a hidden reader | Pre-delete grep (2f) plus the build |

---

## 5. Fable plan review (Day 124): GO WITH FIXES. All 10 findings accepted.

Fable confirmed the plan's factual claims: `qualityGates` has no readers,
both ladders are byte-identical to the helper, and every card has a single
root where a `data-testid` can go. I spot-checked findings 1 and 2 myself
(`api.js:796/807/820`, `App.jsx:1808`).

| # | Sev | Finding | Change to the plan |
|---|-----|---------|--------------------|
| 1 | MUST | The earnings call is `/api/earnings/<T>?days=N` and the raw JSON says `has_upcoming`. The state is tri-state: `null` means the fetch failed. The badge has no stable hook. | Capture by URL prefix. A5 checks all three states: true → header badge (`data-testid="earnings-badge"`) present; false → no badge and Fundamentals says "No earnings date found"; error → no badge and Fundamentals says "Couldn't check the earnings calendar." |
| 2 | MUST | Every Simple criterion card says PASS/FAIL (`App.jsx:1808`), so a view-wide "no PASS" check would false-fail. | A8 is scoped to the `card-simple-verdict` badge. The testid goes on the wrapper at `:1745` so the badge and "N/9 criteria met" are read together. |
| 3 | MUST | A3's expected strings were underspecified. | Export `fmtPct`/`fmtDate` from `marketBackdrop.js` (RegimeRead imports them, one place, GR59). The check builds its expected text with `describeMarketBackdrop(captured payloads)` plus those formatters, not hand-built strings. Fixtures cover all row states (ok, no_down_day, no_history, unavailable) and VIX with a null label. Stated: SPY or VIX failure isn't isolated (the whole analysis errors, `api.js:433`), so a live "couldn't load" row can only happen for QQQ. |
| 4 | MUST | "VIX not loaded" had no data path, because `calculatePositionSize` doesn't return `isDefault`. | Pass `vixUnknown` through `options` and return it in the result next to `vixMultiplier`. Verification step 5 becomes "press Calculate with no stock analysed". |
| 5 | SHOULD | A7 passes vacuously, because "Multi-Source ✓" is in the app header on every tab. | Drop A7. Provenance is already per card (Fundamentals provider line, Pattern footer) and A6 covers blank cards. |
| 6 | SHOULD | The 390px tab-bar overflow isn't in KNOWN_ISSUES. | It goes into the /sta-end Known Issues list (already planned there). The wording in §1 is fixed. |
| 7 | SHOULD | Day 119 Phase 6's Scan-tab disclosure line under "STA Verdict" | Moot: Step 6 removed that column. Recorded as closed. |
| 8 | SHOULD | More doc consumers: repo-root `DEVELOPER_ONBOARDING.md`, `docs/test/MANUAL_TEST_PLAN_30_TICKERS.md:559`, `KNOWN_ISSUES_DAY123.md:31` (qualityGates). | Added to 2g. The KNOWN_ISSUES item is closed at /sta-end. |
| 9 | NIT | There is no ESM shim: `.mjs` imports directly and the CJS runner uses dynamic `import()`. | Wording fixed. |
| 10 | NIT | A4's "Unknown" guard can't trigger today. | Kept as a regression guard. Its mutation fixture uses the raw "Unknown • Unknown" string. |

Checks after review: A1–A6, A8, A9 (8 checks; A7 dropped).

---

## 6. Build notes (Day 124)

Built test-first: `test_analyze_checks.mjs` and `test_vix_multiplier.mjs` were written and
seen failing before the code they test.

**Changed files:** `scripts/lib/analyzeChecks.js` (new), `scripts/test_analyze_checks.mjs`
(new, 66 checks), `scripts/test_vix_multiplier.mjs` (new, 17 checks),
`scripts/ui-verify-checklist.js` (rewritten), `scripts/ui-cohesiveness-test.js` (fixed),
`src/utils/marketBackdrop.js` (exports `fmtDate`/`fmtPct`, moved from RegimeRead),
`RegimeRead.jsx` / `TechnicalRead.jsx` / `MRRead.jsx` / `FundamentalsRead.jsx` /
`PriceStructureCard.jsx` / `App.jsx` (`data-testid` hooks), `positionSizing.js`
(non-finite VIX → unknown; `vixUnknown` returned), `App.jsx` (two ladders → helper,
"VIX not loaded" note), `scoringEngine.js` (`checkQualityGates`, its call, its return key,
and the now-unused `getLiquidityThreshold` import removed).

**Found while building (deviations from the plan):**
1. The first live run failed A2 on AAPL: the Trade Setup's price bar labels the buy price
   "BUY $338.70". It's a price label, not a verdict. A2 now records which card each short
   label sits in and allows exactly "BUY" inside `card-trade-setup`. Tests were added: "BUY"
   in the header still fails, and "AVOID" inside Trade Setup still fails.
2. RIVN failed A6: the Price Structure card is folded closed by design, and its closed
   header ("▶ Price Structure · Downtrend") is under 40 characters. The card now carries
   `data-collapsed`, and a folded card must show at least 20 characters (its title plus a
   status word). Tests: title + status passes, title only fails.
3. The PDF script reads the Simple badge by toggling to Simple and back. The plan said
   "from the API payload", but the Simple verdict is computed in the browser and has no
   payload. A check confirmed the page is back on Full before the PDF is saved.
4. `getLiquidityThreshold` became an unused import once `checkQualityGates` was gone
   (the build warned), so it was removed. It's still used in App.jsx and simplifiedScoring.js.

**Verification:**
- Unit: analyze checks 66/66, VIX multiplier 17/17, market backdrop 22/22, VIX bands 13/13,
  index trend 26/26, verdict parity 86,400/86,400.
- Live verifier: AAPL, NVDA, SMH, JPM, RIVN → 40/40, exit 0. The page-level 390px overflow
  is reported on every ticker (Known Issue, not failed).
- Proof the checks bite: the backdrop was moved below the header and "PASS" restored, both
  at once. AAPL went 6/8: A1 and A8 failed, exit 1. App.jsx was restored from a backup and
  `git diff` showed only the real Step 8 edits.
- PDF script: AAPL and SMH produced 2 PDFs with the new report columns. SMH reads
  "Exchange-traded fund (ETF)".
- Calculator: Calculate with no stock analysed showed the "VIX not loaded" note. After
  AAPL loaded (VIX 18.99) there was no note and the same cap as before.
- `npm run build`: only the pre-existing ValueTab warning.
- `HOW_STOCK_PICKING_WORKS.html` was republished to the same artifact (version 3).

---

## 7. Fable code review (Day 124): SHIP WITH FIXES

| # | Sev | Finding | Disposition |
|---|-----|---------|-------------|
| 1 | MUST | A6 passed vacuously: each card's title row + subtitle alone are 40–130 characters. | **Fixed.** Title rows and subtitles carry `data-card-head`. The runner measures each card's body (its text without those parts), and an open card needs ≥20 body characters. A missing body measurement fails. New realistic fixtures (title + subtitle with an empty body, body not measured) failed first and pass after the fix (69/69). Live proof: emptying the MR card's body gave AAPL 7/8 with A6 failing. After restoring, the 5 tickers are 40/40. |
| 2 | MUST | README still told users to use the Holding Period selector (Usage step 5), and listed "3-tier progressive disclosure" and holding-period weighting as current. | **Fixed.** Step 5 now points to the Simple Checklist. The disclosure box reads "internal only since Day 123". The weighting line is struck through with a note that it was removed Day 123. Roadmap item 11 is marked DONE. |
| 3 | SHOULD | `PROJECT_INSTRUCTIONS.md` shows as deleted in the working tree. | It was already deleted before this session started (initial `git status`). Not part of Step 8 and **not staged**. It's left for the user to decide. |
| 4 | SHOULD | `docs/test/MANUAL_TEST_PLAN_30_TICKERS.md` is untracked. | Staged with this commit so the Day 124 note is kept. |
| 5 | NIT | A2's "BUY" price-label allowance has a blind spot (a "BUY" verdict badge inside Trade Setup would pass). | Documented in the check comment. |
| 6 | NIT | Node prints a module-type warning on every run. | Cosmetic. Left as is (`test_market_backdrop.mjs` already prints it). |

Fable verified clean: response capture (each payload fetched once, before the cards render),
A3/A5 state mirroring, the A8 emoji bytes, the VIX helper callers and GR57, the `qualityGates`
removal, `data-testid` placement on every render path, and the doc paths.
