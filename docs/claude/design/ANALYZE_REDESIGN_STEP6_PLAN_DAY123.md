# Analyze Page Redesign — Step 6 plan: Fundamentals card + removals (Day 123)

Status: DRAFT for independent review (Fable) before code.
Standard: §0 of `ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md`. Design: mockup v0.14
Fundamentals card (P/E guide, earnings row). User decisions, Day 123:
- Remove the **Holding Period** selector and the **Assessment Breakdown** card
  (neither backs any new card).
- Remove the **BUY/HOLD/AVOID verdict from every screen** (option chosen:
  "everywhere"). Engine code and the parity test stay untouched.

## 1. Facts verified in code

| Fact | Evidence |
|---|---|
| `holdingPeriod`'s only consumer is `determineVerdict` (via `getSignalWeight`) | grep: `categoricalAssessment.js:751-952`; never read by riskRewardCalc, positionSizing, simplifiedScoring, the new cards |
| The composite verdict is displayed in: Assessment Breakdown "Why this verdict?" (`App.jsx` ~2026-2040), Simple view "Full Assessment (for comparison)" (~2286), Scan tab "STA Verdict" column + "Get Verdict" button (~2535, 2618-2660, `fetchScanVerdict` ~652-690, `scanVerdicts` state ~143) | grep |
| Scan's `fetchScanVerdict` silently uses the Analyze tab's `holdingPeriod` | `App.jsx:676` |
| Trade journal saves `categoricalVerdict` (Forward Testing tab, manual trades) | `App.jsx:3213` |
| Earnings: `/api/earnings` returns `earnings_date` + `days_until` even outside the 7-day window; `days_until < 0` when the found date is past; `{earnings_date: null}` when none found; frontend fetch returns `hasUpcoming: null` on error | `backend.py:1399-1525`, `api.js:774-806` |
| P/E: `pe` is trailing in all three providers (Finnhub `peTTM`, FMP `peRatioTTM`, yfinance `trailingPE`); reaches the frontend as `stock.fundamentals.pe` | `field_maps.py:72,95,130`, `api.js:93` |
| Red-flag screen exists (Phase 1): `screenFundamentalRedFlags(assessFundamental())` → `not_applicable / unavailable / flags / no_flags` with `checked` / `missing` | `categoricalAssessment.js` display section |
| ETF detection = hardcoded 26-ticker list; `/api/stock` has no quoteType; SMH's name is "VanEck Semiconductor ETF" | `categoricalAssessment.js:46`, live curl |
| "Quality Gate Warnings" come from the old 75-point scoring engine's AVOID gates ("Below 200 SMA", "RS below 0.8") — duplicates the Technical Read with different thresholds | `App.jsx` ~2099, `scoringEngine.js` qualityGates |
| "Show Raw Indicators" dumps scoringEngine inputs (RSI, EMA, SMA, ATR) | `App.jsx` ~2045 |
| Fundamentals-unavailable banner sits at the top of the page | `App.jsx` ~1485-1525 (Data Source Status Banner) |

## 2. Changes

### 2.1 New `components/FundamentalsRead.jsx` (mockup v0.14)
- Inputs: `categoricalResult.fundamental` (assessFundamental), raw
  `stock.fundamentals` (for `pe`, `source`), `earningsData`, `ticker`,
  `stock.name`.
- States from `screenFundamentalRedFlags`: **No red flags** (plain text, never
  green), **⚑ n red flag(s)** (amber), **Can't check** (fundamentals feed
  failed; "not the same as no flags"), **Not applicable** (ETF).
- Three tiles: Sales (revenueGrowth, flag ≤ −10%), Profitable (ROE, flag < 0),
  Debt (D/E, flag > 2.0) — values and ✓/⚑ from the helper; thresholds from
  `RED_FLAG_THRESHOLDS` (no literals). Missing metric → dashed "no data / not
  checked" tile.
- **P/E guide** strip (under 15 / 15–25 / 25+, labels cheap / typical / priced
  for growth), sentence "investors pay $X for each $1 of yearly profit", never a
  flag, never coloured. P/E ≤ 0 or missing with fundamentals present → "No P/E:
  the company isn't profitable over the last 12 months" only if ROE < 0 or
  `pe` is missing while other fields exist; otherwise "P/E not reported".
  Bands as named constants `PE_GUIDE_BANDS` with source note (Graham <15;
  S&P typical 15–25).
- **Next earnings** row, always shown: date + "in N days"; highlighted within
  the existing 7-day window (same `days` param, no new threshold); past date →
  "last report N days ago; next date not announced yet"; none found → "No
  date found"; fetch error (`hasUpcoming === null`) → "Couldn't check". Comes
  from a separate feed, so it still shows when fundamentals fail.
- Data note + "How these checks were chosen" (mockup copy; numbers from
  constants).
- ETF caveat: if not on the ETF list but `stock.name` matches `/\bETF\b/i`, show
  "Not applicable (looks like an ETF from its name)" instead of "Can't check".
  Display-only; the engine's ETF branch is unchanged.
- `useMissingInputWarning('Fundamentals', …)` for feed failure, missing
  metrics, earnings fetch error.
- Placement: after the Trade Setup card (mockup order: Regime, Technical Read,
  MR Read, Trade Setup, Fundamentals).

### 2.2 Removals (Full view + Scan + Simple)
- **Holding Period selector** + its `useState`, the `HOLDING_PERIODS` map, the
  re-assessment `useEffect`, the `expandedSections.holdingPeriod` key. All
  `runCategoricalAssessment` calls use the default `'standard'` (explicit
  argument kept, so the Scan path no longer couples to Analyze-tab state).
  `getSignalWeight` / `determineVerdict` untouched (parity).
- **Assessment Breakdown** card (T/F/S/R tiles, expanded details, "Why this
  verdict?") and its `expandedScore` state + `AssessmentTile` import if unused
  (check other importers first).
- **Scan tab STA Verdict column**: header, cell, `scanVerdicts` state,
  `fetchScanVerdict`. Breakout column untouched.
- **Simple view "Full Assessment (for comparison)" strip**; keep the "View Full
  Analysis →" button.
- **Quality Gate Warnings** card and **Show Raw Indicators** section (old
  scoring engine; duplicates the Technical Read with different thresholds —
  Golden Rule 59).
- **Fundamentals-unavailable banner** at the top: its information moves into
  the Fundamentals card's "Can't check" state (+ data source shown in the
  card footer when it is a fallback source).
- Kept on purpose: trade-journal `categoricalVerdict` field (stored history,
  not displayed as a recommendation); `categoricalResult` itself (feeds the new
  cards); Price & RS, Price Structure, Pattern Detection, Breakout Status cards.

### 2.3 Caller checks (Golden Rule 54) to run before deleting
grep each removed symbol across `frontend/src`, `frontend/scripts`, `backend`
(`AssessmentTile`, `getAssessmentColor`, `expandedScore`, `scanVerdicts`,
`fetchScanVerdict`, `HOLDING_PERIODS`, `holdingPeriod`, `qualityGates`,
`toggleSection('indicators'|'categorical'|'holdingPeriod')`). Known script
breakage (`ui-verify-checklist.js`, `ui-cohesiveness-test.js`) is Step 8.

## 3. Data backing every element

| Element | Source |
|---|---|
| Flag state, tile values | `screenFundamentalRedFlags(categoricalResult.fundamental)` |
| Thresholds | `RED_FLAG_THRESHOLDS` |
| P/E | `stock.fundamentals.pe` (trailing, all providers) |
| Earnings date / days | `earningsData.earningsDate/daysUntil/hasUpcoming` |
| Data source | `stock.fundamentals.source` / `fundamental.data.dataSource` |
| ETF | engine ETF list; name heuristic display-only |

## 4. Verification
1. Node checks for any new pure helper (P/E band, earnings line states, ETF
   name heuristic).
2. Build: no new warnings; removed-code warnings gone. Parity green.
3. Live: AAPL (no flags), a ticker with a flag (find one with revenue < −10%,
   e.g. scan a few), SPY (ETF list), SMH (name heuristic), a loss-making
   ticker (no P/E, ROE < 0), forced `/api/fundamentals` failure, earnings
   inside 7 days (NVDA "in 6 days" today), 390px.
4. Scan tab renders without the verdict column; Simple view has no comparison
   strip; no `BUY`/`HOLD`/`AVOID` text anywhere in the Full view DOM.
5. Three escalating review passes + Fable code review.

## 5. Fable review — GO WITH FIXES (Day 123), verified and accepted

| # | Finding (verified) | Plan change |
|---|---|---|
| 1 MUST | yfinance `debtToEquity` is in percent (AAPL ≈ 154) and mapped `_identity` (`field_maps.py` YFINANCE_FUNDAMENTALS); Finnhub/FMP are ratios. Orchestrator fills D/E from yfinance when Finnhub lacks it. | yfinance D/E ÷ 100. Pre-existing engine bug (also skewed `assessFundamental`'s D/E band); logged. Flush fundamentals cache. |
| 2 MUST | ROE/ROA converters only ×100 when abs(v) < 1, so ROE ≥ 100% (AAPL 1.5) shows "1.5%". | yfinance + FMP: unconditional ×100 (both decimals); Finnhub unchanged (already %). |
| 3 MUST | "No P/E = not profitable" is an inference. | Only "trailing earnings are negative" when `pe < 0`; otherwise "P/E not reported". Tile renamed "Return on equity", flag "Negative ROE" (a fact, not "profitability"). |
| 4 MUST | `days_until = (earnings_date - datetime.now()).days` is off by one and −1 on earnings day. | Backend: calendar-date difference in a pure helper (unit-tested); frontend uses `daysUntil` as returned, never re-parses the date. |
| 5 | Past date ≠ "last report". | "Last date in the feed: D (N days ago); no upcoming date listed." |
| 6 | Use yfinance `quoteType`, not a name regex. | Add `quoteType` to `YFINANCE_STOCK_INFO` and `/api/stock`; card: `quoteType === 'ETF'`; regex only when quoteType is absent. |
| 7 | revenueGrowth basis differs by source (yfinance = latest quarter YoY; FMP/AV = last fiscal year). | Pass `_field_sources` through `fetchFundamentals` (additive `fieldSources`); Sales tile names its basis from the source. |
| 8 | Fallback-source banner was dead. | Card footer shows the fundamentals source(s) whenever not Finnhub-only. |
| 9–11 | Quality-gate content all still visible elsewhere (200 SMA, RS → Technical Read; liquidity → Price & RS); delete `AssessmentTile.jsx` (no other importer); fix stale comment at App.jsx:54; P/E > 500 → ">500, earnings near zero". | Accepted. |
