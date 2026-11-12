# Analyze Page Redesign — Step 7 plan: Market Backdrop card, default view, PASS wording (Day 124)

Status: REVISED after Fable review (Day 124) — findings #1–#12 folded in (see §6). Awaiting
user sign-off before code.
Standard: §0 of `ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md` (no silent failures, logged
warnings, distinct loading / couldn't-load / data states, real data behind every element,
no invented fallback numbers).

User decisions, Day 124 (2026-11-12):
- The Regime card shows **long-term and short-term trend separately**, plus the Nasdaq-100,
  because a 4–6% index drop on Nov 5 was invisible behind "Market: Favorable … calm and
  healthy".
- **No Favorable / Neutral / Unfavorable label on the card.** "I will take final decision."
  The card shows facts; the user judges.
- The engine (`assessRiskMacro`, `categorical_engine.py`, parity test, backtest numbers) is
  **not touched**.
- Step 7's original scope stays: Full Analysis becomes the default view; Simple-view PASS
  wording.

## 1. Facts verified in code and data

| Fact | Evidence |
|---|---|
| Nov 5 closes: SPY −4.41%, QQQ −6.49%, HXQ.TO −5.98%. Nov 11 close vs 50-day SMA: SPY −0.6%, QQQ −4.0%, HXQ.TO −2.5% | yfinance daily closes, run Day 124 |
| Card label + sentence come from `assessRiskMacro()` → `describeRegimeRead()`; Favorable = VIX < 20 AND SPY > 200-day AND SPY's 50-day SMA not down > 1% over 20 days | `categoricalAssessment.js:662-735`, `:1246-1300`; `backend.py:1212-1221` |
| One crash day barely moves a 50-day *average*, so `sma50Declining` stayed false | same |
| The engine's regime label is shown **only** on `RegimeRead`; the only other consumer is the trade log's `regimeSnapshot` (saved, not displayed) and `determineVerdict` (no longer displayed anywhere since Day 123) | grep of `riskMacro` across `frontend/src` |
| `describeRegimeRead` is used only by `RegimeRead.jsx` | grep (code); other hits are docs |
| `/api/market/spy` returns 260 daily closes (`priceHistory`), `sma200`, `aboveSma200`, `sma50Declining`; no 50-day SMA, no QQQ anywhere for regime | `backend.py:1156-1240` |
| `fetchSPYData()` is a whitelist reconstruction (Golden Rule 30) — new fields must be added to it or they vanish | `api.js:113-139` |
| `fetchSPYData()` throws on failure and sits in `fetchFullAnalysisData`'s `Promise.all` without a `.catch` → a SPY failure fails the whole Analyze page | `api.js:425-430` (pre-existing; not changed here, noted) |
| `/api/market/vix` already buckets VIX: <15 `low_volatility`, <20 `normal`, <25 `elevated`, <30 `high`, else `extreme` | `backend.py:1280-1289` |
| SPY endpoint does not drop the forming bar; intraday the last bar is today's partial bar | `backend.py` (no `market_time` call); `market_time.is_forming_bar()` exists |
| Default view is Simple | `App.jsx:145` `useState('simple')` |
| Simple badge: `⏸️ PASS` with "x/9 criteria met" under it; rule line "Any NO = PASS" | `App.jsx:1764-1766`, `:1887` |
| The hardcoded "half" position label (Known Issue, "App.jsx:2074") is **already gone** — no match for `half` in `App.jsx` or components | grep, Day 124 |

## 2. Changes

### 2.1 Backend: index trend facts (additive)

New helpers in `backend.py` (one copy, Golden Rule 59):
- `_index_snapshot(ticker)` — provider chain (`get_ohlcv(ticker,'2y')` → yfinance fallback)
  shared by both routes, so SPY and QQQ can't drift apart.
- `_index_trend_facts(hist)` — computed on **completed bars only**
  (`market_time.drop_forming_bar`, the Day 123 rule). Reason: `get_ohlcv` serves a cached
  frame until close + 30 min, so a "today so far" number could be a 09:45 snapshot shown all
  day (Fable #2). No new thresholds.

| Field | Meaning |
|---|---|
| `sma50` | mean of the last 50 closes (null if < 50 bars) |
| `aboveSma50` | `currentPrice > sma50` (null if `sma50` null) |
| `pctVsSma50`, `pctVsSma200` | % distance, 1 decimal (null if the SMA is null) |
| `asOfDate` | `YYYY-MM-DD` of the last **completed** bar |
| `biggestDrop10d` | `{date, pct}` — the most negative one-day close-to-close change in the last 10 completed bars; `{noDownDay: true}` if none is negative; null if fewer than 11 bars. Always reported, even if small (no "shock" threshold) |
| `biggestDrop10dSince` | date of the most recent bar **strictly before** the drop date with a drop at least as large, searched over the **full 2-year frame** (not the 260-bar `hist_data` tail); null if none → card says "largest in the last 2 years" |

All facts are computed in one place, in their own `trend` sub-object, so legacy keys keep
their meaning:
- `/api/market/spy`: add `trend: {...}`. Legacy `currentPrice / sma200 / aboveSma200 /
  sma50Declining` are **unchanged** (they still include the forming bar and feed the engine).
- `GET /api/market/index/<ticker>` with whitelist `{SPY, QQQ}` (400 otherwise): returns
  `{ticker, trend: {...}}`. The frontend uses it for QQQ. 500 with `{error}` on failure
  (never 200-on-error), logged with `print` + traceback.
- The SPY 50-day SMA here is display-only. It is **not** fed into `assessRiskMacro`.
- VIX stays a live quote (`/api/market/vix`). The card labels it "now" separately from the
  index lines' "as of <date> close", so the two as-ofs are visible, not blended.

Why QQQ and not HXQ.TO: QQQ is the Nasdaq-100 reference the rest of the app already uses
(Sectors size rotation); HXQ.TO tracks the same index in CAD. The card names it
"Nasdaq-100 (QQQ)".

### 2.2 Frontend data path

- `fetchSPYData()`: switch to pass-through of the JSON (Golden Rule 30/47). Safe: every
  reader uses named keys (`rsCalculator.js`, `simplifiedScoring.js`, `scoringEngine.js`,
  `assessRiskMacro`); nothing enumerates `spy`'s keys (Golden Rule 57); backend always
  emits a bool for `sma50Declining`.
- New `fetchIndexTrend('QQQ')`: throws on failure. In `fetchFullAnalysisData`, wrapped in
  `.catch(err => ({ error: err.message }))` so a QQQ failure never takes the page down
  (Golden Rule 32 lesson). Returned as `data.qqq`.
- **Second whitelist (Fable #1):** raw SPY/VIX live in `rawAnalysisData`, a hand-built
  literal (`App.jsx:498-507`). Add `qqq: data.qqq` there; the card reads
  `rawAnalysisData.{spy, qqq, vix}`.
- Golden Rule 43: re-analyze goes through `fetchFullAnalysisData`, so QQQ refetches with
  SPY/VIX. Check `handleSessionRefresh` (`App.jsx:263+`) — it doesn't null
  `rawAnalysisData` today; confirm the card can't show the old ticker's backdrop next to a
  new analysis (backdrop is market-wide, so staleness = old date, shown by the as-of line).
- Legacy `fetchAnalysisData` (`api.js:212`) also calls `fetchSPYData`; confirm dead and
  note it (pass-through covers it either way).

### 2.3 `RegimeRead.jsx` → Market Backdrop card

New display helper `describeMarketBackdrop(spy, qqq, vix)` in `categoricalAssessment.js`'s
display section (replaces `describeRegimeRead`, which is deleted along with its doc
references in code comments). Returns `{ lines, summary, missing }`.

Card layout (neutral grey band, **no Favorable/Neutral/Unfavorable, no band colour**), a
small table so long-term and short-term sit in separate columns (Fable #10):

```
Market backdrop                                   ◇ INFO · NEVER GATES THIS PAGE
               Long-term (200-day)   Short-term (50-day)   Biggest 1-day drop, last 10 days
S&P 500        ↑ above  +4.8%        ↓ below  −0.6%        −4.4% Nov 5 (largest since <date>)
Nasdaq-100     ↑ above  +x.x%        ↓ below  −4.0%        −6.5% Nov 5 (largest since <date>)
VIX 18.2 · normal range (now)                         Index figures as of Nov 11 close
```

- At < `sm` width each row stacks label-over-value so 390px doesn't wrap into prose.
- Per-fact direction glyph/colour (↑ green / ↓ red) describes a fact, not a verdict.
- VIX wording uses the backend's own `regime` bucket (`low`, `normal range`, `elevated`,
  `high`, `extreme`), with an explicit fallback: unknown/missing → "VIX: couldn't load",
  never `undefined`. No new threshold.
- `{noDownDay:true}` → "no down day in the last 10 sessions".
- **No composed summary sentence** (Fable #5). "Uptrend intact" / "short term weak" are
  inferences; the user decides. The table is the summary. No imperative language.
- States (§0):
  - **Loading**: card skeleton while analysis loads (existing page-level loading).
  - **Partial**: a missing piece shows "couldn't load" on its own line (dashed), never
    dropped silently: QQQ error → "Nasdaq-100: couldn't load"; VIX null → "VIX: couldn't
    load"; SPY 50-day null (short history) → "not enough history".
  - **Unavailable**: all of SPY/QQQ/VIX missing → "Couldn't load market data."
- `useMissingInputWarning('Market', ticker, missing)` for each missing piece.
- Engine-label leftovers removed: "Market: Favorable", the green/yellow/red band, the
  "engine assumed below" text (the card no longer shows the engine's call; the engine bug
  stays logged in Known Issues).

### 2.4 Default view + Simple-view wording

- `App.jsx:145`: `useState('simple')` → `useState('full')`; comment updated (Day 124).
  Toggle still works both ways.
- `App.jsx:1764`: `⏸️ PASS` → `⏸️ No Trade` (the "x/9 criteria met" line under it stays).
  `✅ TRADE` unchanged.
- `App.jsx:1887`: "Any NO = PASS" → "Any NO = no trade".
- `App.jsx:1126` comment ("Simple view keeps its own TRADE/PASS checklist verdict") updated
  to the new wording.
- `analysisView` isn't persisted anywhere, so the default flip is the one-line change.
- Per-criterion `PASS`/`FAIL` chips (`:1792`) unchanged — there PASS means the criterion
  passed.
- **Zero change** to `simplifiedScoring.js` (Golden Rule 57).

### 2.5 Not changed (explicit)

`assessRiskMacro`, `determineVerdict`, `categorical_engine.py`, `test_verdict_parity.py`,
`simplifiedScoring.js`, the trade log's `regimeSnapshot` (still records the engine's
assessment — a saved field, not displayed), MR/Technical/Fundamentals cards.

## 3. Risks and how they're handled

| Risk | Handling |
|---|---|
| Card and engine now say different things (engine may still compute "Favorable") | Engine label isn't displayed anywhere (verified grep). Documented in Known Issues: the engine's regime input still ignores the 50-day and the Nasdaq; only matters if a verdict is ever shown again |
| New QQQ fetch adds a provider call per analysis | Same cached provider path as SPY (daily OHLCV cache); one extra symbol, not a loop (Golden Rule 25/40 n/a) |
| tz mix between SPY/QQQ series | Each endpoint computes its own facts from its own series; no cross-series alignment |
| Forming bar / stale cached partial shown as "now" | Index facts use completed bars only; as-of date shown; VIX labelled "now" separately |
| Analyze and Context tabs carry two independent SPY-trend reads (`market_phase_engine.py:139-156` uses full-2y rolling(200), no forming-bar drop) | Accepted; recorded in API_CONTRACTS; never claim the two pages agree on a cross day |
| `fetchSPYData` pass-through drops a renamed field | Pass-through keeps every existing key; diff the object before/after on a live call |
| "largest since <date>" search wrong at series edges | Unit test with synthetic series (no earlier larger drop; tie; drop on first bar) |

## 4. Verification

1. Backend unit test `backtest/test_index_trend.py`: `_index_trend_facts` on synthetic
   series — <50 bars (nulls), exact SMA values, biggest-drop with ties, no down day,
   "since" search at both edges (strictly earlier; none in 2 years), forming bar dropped
   with injected `now`.
2. Live curl `/api/market/spy` and `/api/market/index/QQQ`: numbers match the Day 124
   yfinance check within provider rounding; legacy SPY keys byte-identical to before;
   `/api/market/index/XYZ` → 400; forced provider failure → 500 `{error}`.
3. Parity: `test_verdict_parity.py` 86,400/86,400 (engine untouched; hook reruns anyway).
   `git diff --stat` on `simplifiedScoring.js`, `categorical_engine.py` → empty.
4. Live browser (AAPL, NVDA, SMH, RY.TO, 390px): Full Analysis is the landing view; card
   shows 4 fact lines + summary + as-of; no "Favorable" text anywhere on the page.
5. Forced failures: block `/api/market/qqq` → Nasdaq line "couldn't load", page still
   renders, one `[STA][Market]` console warning; VIX null → same.
6. Simple view: a 2/9 ticker shows "⏸️ No Trade" and "2/9 criteria met"; never bare PASS.
7. Trade Log: log a manual trade → `categoricalVerdict` and `regimeSnapshot` still saved.
8. Three escalating review passes (Golden Rule 41), then Fable code review, then sign-off.

## 5. Docs at close

Known Issues: close "hardcoded half label" (already gone, `KNOWN_ISSUES_DAY123.md:87`);
update the "Simple Checklist PASS badge" Low/Info item to resolved; add Low "engine regime
input ignores the 50-day and the Nasdaq — no visible effect while no verdict is shown;
`regimeSnapshot.assessment` is saved and CSV-exported (`forwardTesting.js:386-389`), not
rendered". API_CONTRACTS: full entries for `/api/market/spy` (incl. new `trend`),
`/api/market/vix` (none exist today), new `/api/market/index/<ticker>`; note the separate
Context-tab SPY read.

## 6. Fable review (Day 124) — disposition

| # | Sev | Finding | Disposition |
|---|---|---|---|
| 1 | Should-fix | `rawAnalysisData` is a second whitelist; QQQ would be dropped | Folded (§2.2) |
| 2 | Should-fix | Cached partial bar shown all day as "now"; VIX live vs index cached | Folded: completed bars only, two labelled as-ofs (§2.1) |
| 3 | Should-fix | No-down-day case; "since" search limited to 260 bars | Folded (§2.1, §4) |
| 4 | Should-fix | QQQ route would copy the SPY route | Folded: `_index_snapshot` + `/api/market/index/<ticker>` |
| 5 | Should-fix | Summary sentence is inference, not fact | Folded: sentence cut |
| 6 | Nit | `regimeSnapshot` is CSV-exported | Folded (§5) |
| 7 | Nit | Context tab has its own SPY read | Accepted, recorded (§3, §5) |
| 8 | Nit | Legacy `fetchAnalysisData` | Folded (§2.2) |
| 9 | Nit | No spy/vix API_CONTRACTS entries; no PASS Known Issue to "close" by that name | Folded (§5) |
| 10 | Nit | Two indexes per line wrap at 390px | Folded: table layout |
| 11 | Nit | Stale comment; VIX bucket fallback | Folded (§2.3, §2.4) |
| 12 | Nit | `analysisView` not persisted | Noted (§2.4) |

## 7. Build notes + Fable code review (Day 124)

Built test-first: `backend/backtest/test_index_trend.py` (26 checks) and
`frontend/scripts/test_market_backdrop.mjs` (22 checks) were written and seen failing before
the code. Parity 86,400/86,400; build clean; live AAPL / NVDA / SMH, forced QQQ 500, 390px.

Deviations from §2 (accepted by the code review): helpers live in new modules
`backend/index_trend.py` and `frontend/src/utils/marketBackdrop.js` (engine file untouched
apart from deleting `describeRegimeRead`); backend helpers are `_index_history` +
`_safe_trend_facts` (the latter isolates a trend failure so it can't 500 `/api/market/spy`);
VIX is tagged "(latest quote)", not "(now)", since pre-market it is the prior close.

| # | Sev | Finding | Disposition |
|---|---|---|---|
| 1 | Should-fix | "largest in the last 2 years" assumed, not reported | Fixed: backend emits `searchedFrom`; card says "largest in data back to <date>" |
| 2 | Should-fix | `dropna()` before changes merged two sessions into a fake 1-day drop | Fixed: changes on the raw series, NaN changes skipped, `nanCloses` reported + logged |
| 3 | Nit | Ties compare 2-dp rounded pcts | Documented in `_pct` docstring (by design) |
| 4 | Nit | Three wordings for the drop label | Fixed: "Biggest 1-day drop, last 10 sessions" everywhere |
| 5 | Nit | Unrounded SMAs in payload | Fixed: 2 dp |
| 6 | Nit | Record deviations | This section |
| 7 | Nit | `.copy()` vs old in-place rename | Checked: OHLCV cache is rebuilt from SQLite per call, no shared frame; no behaviour change |
| 8 | Nit | §5 docs | At `/sta-end` |
