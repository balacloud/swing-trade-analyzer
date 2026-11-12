# Simple Support/Resistance — Plan (Day 125)

**Status:** PLAN — awaiting Fable review, then user sign-off.
**Why:** User: "is the S&R code best in class simple? what's commonly used? weekly candles?" Today's `support_resistance.py` (~1,600 lines) uses
swing highs/lows as its main method, but adds 3 fallback methods (agglomerative, KMeans, volume
profile), ATR/Fibonacci projected levels, touch scoring and a weighted daily/weekly confluence.
A trader can't explain it in one sentence, and the extras are where its bugs were (Day 111 audit:
S&R 2/10, MTF 3/10). Goal: the levels most traders would draw by hand, in code a trader can read.
These are conventions, **not backtested** (same user decision as the breakout rules).

Process: plan → Fable review → test-first build → old-vs-new comparison on ~30 stocks shown to the
user → user approves the switch → Fable code review → live check → sign-off.

---

## 1. Widely agreed rules (sources: Day 125 research in ANALYZE_CLEANUP_PLAN_DAY125.md §2)
1. Levels sit at **swing highs and swing lows** (clear turning points).
2. **Weekly levels matter more** than daily ones for a multi-week hold; mark weekly first.
3. Swings that sit close together form **one zone**, not separate lines.
4. A level that price turned at **more than once** matters more.
5. Use the **nearest** level above and below; keep the chart clean.

## 2. Part A — `backend/simple_sr.py` (new, ~100–150 lines)

All on **completed** bars (`market_time.drop_forming_bar`).

| Step | Rule |
|---|---|
| Daily swings | Bar i is a swing high if its high is the highest of bars i-5 … i+5 (low: lowest). Last 252 daily bars. |
| Weekly swings | Same on weekly bars (W-FRI resample of the full 2-year fetch), 2 bars each side, last 104 weeks. |
| Zones | Sort all daily swing prices; merge neighbours closer than **0.5 × ATR(14)** into one zone. Zone low/high = min/max of its swings. A zone needs **2+ swings** ("turned here 2+ times"), OR one weekly swing. |
| Weekly ★ | Zone contains a weekly swing price (or one is within 0.5 × ATR of its edge). |
| Nearest | Support = the highest zone whose **high** is below the last close; resistance = the lowest zone whose **low** is above it. Price **inside** a zone → reported as `insideZone` (the card says "price is inside this zone"). Same 20% below / 30% above window as today. |
| None | No zone → `null`. **No projected/ATR/Fibonacci levels, no fallback methods.** |

Notes the build must handle and test: the last 5 daily bars (2 weekly) can't be confirmed swings
yet (standard for this method — say so in the card's "?" note); flat tops (equal highs) count once;
NaN rows dropped and logged; fewer than 60 bars → error, not a guess.

**Output (additive, same `/api/sr` route):** `support` / `resistance` arrays become zone
representative prices (zone **mid**), nearest first; new `meta.zones` = `[{low, high, mid, swings,
weekly, side}]`; `meta.engine = 'simple'`. `suggestedEntry` = nearest support zone **high** (buyers
step in at the top of the zone — open question for Fable, §5), `suggestedStop` = entry − 2×ATR
(unchanged formula), `suggestedTarget` = nearest resistance zone **low**. Removed when on the
simple engine: `levelScores`, `mtf.confluence_map`, `resistanceProjected` / `supportProjected`,
`projection_method`, `pivotSelection`. Kept untouched: ATR, ADX, RSI, RVOL, OBV, candle, prevBar,
market structure, proximity filter.

**Switch:** `SR_ENGINE = 'simple' | 'legacy'` in `backend/constants.py`. The old engine stays on
disk for `backtest_holistic.py` and the discontinued `paper_trading/live_signals.py`
(Golden Rule 54: they keep importing `compute_sr_levels`, unchanged).

## 3. Callers (Golden Rule 59 — what changes when the numbers change)
- **Simple Checklist** (`simplifiedScoring.js`): criterion 3 (entry near support, cap-aware max
  stop %) and criterion 4 (R:R from `riskReward`) read `/api/sr`. **The TRADE / No Trade verdict can
  flip.** Not part of the 86,400 verdict-parity grid (that is the categorical engine), so parity
  must still pass but doesn't protect this.
- **PullbackPlan.jsx** (buy/stop/target), **KeyLevels.jsx** (rows), `technicalReadChecks.js` /
  `TechnicalRead.jsx` / `volumeThresholds.js` (read `meta` volume/ADX fields only — verify).
- Not changed: categorical verdict, MR, breakout (own 60-day-high rule).

## 4. The comparison (before switching)
`backend/backtest/compare_sr_engines.py`: for ~30 tickers (the 5 verifier tickers + 25 across
sectors, price levels and volatility, incl. an ETF, a stock at its all-time high, a falling stock),
print old vs new nearest support/resistance, zone width, swings, ★, and the Simple Checklist
criteria 3/4 pass/fail under each. Output a Markdown table for the user. **The user decides the
switch from that table.**

## 5. Open questions for Fable
1. Merge distance 0.5 × ATR vs a fixed %: is ATR right for both a $13 RIVN and a $900 stock?
2. Entry at the support zone's high vs its mid: which matches "buy at support" without inflating R:R?
3. "2+ swings OR one weekly swing" as the minimum: too loose, too strict?
4. Should the 52-week high/low be added as levels even when not a confirmed swing (e.g. made in the last 5 bars)?

## 6. Part B — DROPPED (user + Claude, Day 125): no chart in the app
User asked: "will the chart really help me, or cause decision fatigue? How will you use it?"
Honest answer: Claude reads the exact numbers from the API, so a chart adds nothing for Claude. The
user already reads charts in TradingView; a second, smaller chart in STA is a second place to look,
and a new question when the two disagree. Same conclusion as Day 70 (TradingView chart removed, "not
adding value"). **Instead:** the §4 comparison gets a **one-time review page** (a published
artifact, not app code) with a small chart per stock, old levels next to new, so the user can judge
the switch by eye once. STA levels on a real chart, if ever wanted, belong in TradingView via the
existing `docs/pine_scripts/SwingTradeAnalyzer_SR.pine`, not in STA.

## 7. Out of scope
Changing the breakout rule; backtesting the levels; touching `backtest_holistic.py` or the paper job.

---

## 8. Fable plan review (Day 125) — verdict GO once #1–#6 are in the plan (done below)

Overrides §2–§4 where they differ. Chart findings (#13, #14, #21) are moot because Part B was dropped.

| # | Sev | Finding | Change to plan |
|---|---|---|---|
| 1 | MUST | `support[]` = zone mids but `suggestedEntry` = zone high → Trade Setup (`riskRewardCalc.js` uses `max(support)`) and the Simple Checklist would show two different Buy prices | Arrays carry the **zone edge nearest price** (support → zone high, resistance → zone low), nearest first; full zones in `meta.zones`. One Buy everywhere. |
| 2 | MUST | `keyLevels.js`/`KeyLevels.jsx`/`test_key_levels.mjs` read every removed field (fake ±0.5% band, levelScores, confluence_map, projected) | Rewrite to read `meta.zones`: row = `low – high · turned here N× · ★ weekly`; kinds `level / inside / weak / none`; footnote rewritten; tests rewritten. |
| 3 | MUST | Reference price ambiguous; route `tail(260)` too short for 104 weeks | Zones from `drop_forming_bar(full 2y frame)`; side/nearest/20–30% window judged against the route's **live** `current_price`, as today. Legacy path + market structure keep `tail(260)`. |
| 4 | MUST | 0.5×ATR merge chains into giant zones | Merge only if gap ≤ 0.5×ATR **and** resulting width ≤ 1.0×ATR; test 6 swings 0.4 ATR apart → ≥3 zones. |
| 5 | MUST | Comparison script could become a second scoring engine | Extract the route's entry/stop/target/R:R/proximity block into one function used by route + script. Table per ticker per engine: zones, entry, stop, stop% vs 7/9/10 caps, target, R:R vs 2.0/1.5, swings, ★, merge width % of price. Labelled "same arithmetic as simplifiedScoring.js 3/4, one-off". |
| 6 | MUST | Dead/false copy: PullbackPlan `targetProjected` branches + ATH help text, `riskRewardCalc.js` comments, `api.js` method doc, route docstring | Same commit. New copy: "No resistance within 30% above — the stock is at/near its highs; no target is shown." |
| 7 | SHOULD | ATR includes the forming bar | Wilder ATR(14) on completed bars, one shared helper (not importing sklearn's module); JS comment updated. |
| 8 | SHOULD | `SR_ENGINE_AVAILABLE` gate (sklearn not in requirements.txt) would block the new engine | Import `simple_sr` independently; 503 only for legacy. |
| 9 | SHOULD | Fractal edge blind spots | Fractals on the full frame, keep last 252 bars; `meta.confirmedThrough`; say the last-5-days / last-2-weeks blind spot in the "?" note. |
| 10 | SHOULD | Flat tops | `>=`, de-dupe equal prices within one 11-bar window; farther apart = 2 turns. Tests both. |
| 11 | SHOULD | Zone straddling price | Treat as support: entry = its high, `insideZone: true`; resistance = next zone above. |
| 12 | SHOULD | 2+-swing gate blanks trending names | Keep 1-swing zones; prefer 2+ or weekly; if none in the window, show the nearest 1-swing zone labelled "1 turn — weak". A swing high and a swing low at the same price count as 2 (role flip). |
| 15 | SHOULD | Verifier has no S&R check | Capture `/api/sr`; new A10: Buy == `suggestedEntry` == `max(support)`; rows == nearest `meta.zones`; ★ iff weekly; "No support" iff empty. |
| 16 | SHOULD | Tests not named | `backend/backtest/test_simple_sr.py` (edges, flat top, chain cap, straddle, min bars, NaN, weekly ★, none, forming bar, live-price nearest) + rewritten `test_key_levels.mjs`. |
| 17 | SHOULD | One-liner "near" is point-based | Pass zone edges; near = inside or within 2×ATR of the nearest edge. |
| 18 | SHOULD | Docs list | `API_CONTRACTS` (breaking), README (S&R section, sklearn, "Lightweight Charts queued"), route docstring, DEVELOPER_ONBOARDING, AUDIT_COVERAGE_LEDGER, cross-link ANALYZE_CLEANUP_PLAN §3.2 ("engine unchanged" superseded). |
| 19 | SHOULD | Contract loose ends | `method='simple'`; `allSupport/allResistance` = all zone edges per side; one min-bars rule on completed bars; window applied to the edge nearest price. |
| 20 | NICE | Scan watchlists call `/api/sr` 76× | Vectorised centred rolling max/min, no Python loops. |
| 22 | NICE | `lastSwingDate` | Additive in `meta.zones`. |

**§5 answers adopted:** (1) ATR merge, with the width cap, and show merge width as a % of price in the table; (2) entry at the support zone high, target at the resistance zone low — the conservative pair: R:R can only get stricter; (3) 2+ swings is a preference, not a gate (#12); (4) no 52-week high/low levels; when there's no resistance and the close is within ~3% of the 252-bar high, the copy says "the stock is at its 52-week high" as a fact.

## 9. Reddit check (user-run search, Day 125: r/Daytrading, r/technicalanalysis, r/swingtrading)

| Our rule | Reddit | Note |
|---|---|---|
| a) Levels = swing highs/lows | **Agree** | "places price repeatedly turned", "major higher-timeframe swing points", "edges of a well-defined range" |
| b) Weekly counts more | **Agree, with nuance** | Daily for swing structure, then zoom out to check bigger levels. Matches the design: daily zones + ★ when the weekly chart agrees |
| c) Zone, not a line | **Agree** | "not a fine precise line, rather a paint brush". Zone width not discussed; the ATR cap is our choice |
| d) 2+ turns preferred, 1 turn "weak" | **Mixed** | Repeated turns matter, but so does "a level that prompted a strong move". **Change:** drop the "weak" label; just show "turned here 1×" |
| e) Nearest few only | **Agree** | "a few levels that are obvious to everyone"; "if a level isn't obvious without zooming in, it probably isn't important" |
| f) No invented levels | Not discussed directly; consistent with "obvious levels" | Keep |

Also from the threads: a touch alone is not a trade signal ("observe what actually happens around those
areas"). That fits STA's stance that levels are a description, never a buy. The 50-day SMA is common
context, and the Technical Read already shows it. Evidence is light (one summary, no thread links),
but it is consistent with the books and with the plan.
