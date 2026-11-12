# Analyze Page Cleanup + Simple Breakout Rules — Plan (Day 125)

**Status:** PLAN — awaiting Fable review, then user sign-off.
**Why:** User (Day 124 close, same conversation): too many words on the Analyze page cause
decision fatigue. Make support/resistance "simple and neat". Breakout should use the rules most
traders agree on, plainly, **without a backtest** ("it's a rabbit hole"). The rules are
conventions, labelled as such on the page, never claimed as a proven edge.

Process: this plan → Fable review → test-first build → Fable code review → live check → user sign-off.

---

## 1. Decisions taken in conversation (user, Day 124/125)

| # | Item | Decision |
|---|---|---|
| D1 | Fundamentals card | Stays on Analyze. **Remove the P/E guide** (one 15/25 scale is wrong across sectors; no trusted sector P/E data; P/E doesn't predict a 2-week move). Card keeps earnings date + 3 red flags. P/E stays on the Value tab. |
| D2 | Support/Resistance | Simple and neat: nearest floor + nearest ceiling only, each as a zone with a turn count and ★. |
| D3 | MTF Confluence | Remove the % badge, the Weekly Levels dropdown, the "Method / ATR / MTF: Weekly" small print. Keep the ★. |
| D4 | Price Structure card | Remove. Keep only its one-line state label inside Trade Setup. |
| D5 | Pattern Detection card | Remove from the page. Backend `/api/patterns` stays (feeds `generatePriceStructure`'s state? — see §3.4). |
| D6 | Breakout | Rewrite to the consensus rules (§4). No backtest. Say "common trader rules, not tested" on the card. |

## 2. External research (summary)

**Support/resistance** — sources agree on: levels sit at swing highs/lows where price turned
**more than once** (2+ touches; one touch is weak); treat a level as a **zone, not a line**;
**role reversal** — a broken ceiling becomes a floor, confirmed by a *close* through it, not a
wick; keep the chart clean (a few levels, not many). Disagreement: 2 vs 3 touches.
Sources: TradingView ("Support & Resistance — the mistake 90% make"), TMGM Academy,
Liberated Stock Trader, Capital.com "Reversal Zones", Wealthsimple.

**Breakout** — sources agree on: confirm on a **daily close** above the pivot/ceiling, not an
intraday poke; volume on breakout day **40–50%+ above the 50-day average** (today excluded);
**don't chase more than ~5% above the pivot** (O'Neil/MarketSmith "5% buy zone"; some use 10%);
a close **back below the pivot** soon after = failed breakout; many breakouts pull back to
retest the pivot (O'Neil: ~40%). These are repeated conventions from secondary sources, not
proven rules. Sources: MarketSmith India (5% zone, extended stocks), IBD/Yahoo ("don't wait for
8%"), LuxAlgo (volume confirms breakouts), Chartmill (7–8% rule), thepatternsite (Bulkowski,
volume).

## 3. Part A — page cleanup (frontend only, no engine change)

### 3.1 Fundamentals (D1)
- `FundamentalsRead.jsx`: remove the P/E guide block, its help paragraph, and the
  "P/E comes from the same feed" line. Keep `describePE`/`PE_GUIDE_BANDS` only if another caller
  exists (grep; else delete + their tests).
- `fundamentalsRead.js` `SOURCE_FIELDS`: drop `pe` so "fields reported" counts don't mention P/E.

### 3.2 Support/resistance in Trade Setup (D2, D3)
Replace the S1..Sn / R1..Rn lists (`App.jsx` ~1325–1432) with a new small component
`KeyLevels.jsx` and a pure helper `utils/keyLevels.js`:

```
Price is: Uptrend pulling back to support          ← the old Price Structure one-liner (D4)
Ceiling  $342.30 – $345.70   2.1% above   turned here 4×   ★ weekly
Floor    $318.40 – $321.60   4.3% below   turned here 3×
```
- **Nearest** level each side from `srData.resistance` (min above) / `srData.support` (max below).
  Same numbers PullbackPlan already uses (one source).
- **Zone** = level ± 0.5% — the S&R engine's own `touch_threshold` (`support_resistance.py:72`),
  so the zone and the turn count describe the same band. Display only; engine unchanged.
- **Turn count** from `srData.meta.level_scores[level.toFixed(2)]`. Missing key → omit the
  phrase (never "0×"). Note: the count is bars whose high/low came within 0.5% — say "touched".
- **★ weekly** from `meta.mtf.confluence_map[key].confluent` (existing). Tooltip keeps strength label.
- None on a side → "No ceiling found in the last year" / "No floor found…" (visible, not hidden).
- Remove: MTF % badge, Weekly Levels `<details>`, the Method/ATR/MTF footer.
- A one-line "?" note: "Levels are zones where price turned before. Common rules, not tested."

### 3.3 Remove Price Structure card (D4)
- Remove `<PriceStructureCard>` from App.jsx; delete `PriceStructureCard.jsx`.
- Keep `deriveStructureState` (export it) for the one-liner. Remove watch-items/keyLevels code
  if nothing else uses it (grep `generatePriceStructure`).
- **Golden Rule 59 check:** is `priceStructureNarrative` used by any engine/verdict/parity path?
  Expected no (display only). Verify by grep before deleting.

### 3.4 Remove Pattern Detection card (D5)
- Remove the card JSX and `PatternMiniCard.jsx` (if no other user).
- `/api/patterns` fetch: still needed? `deriveStructureState` uses trend-template count + ADX +
  levels, which come from the patterns payload (`trend_template`, `adx`)? → **verify**. If the
  one-liner needs them, keep the fetch; else keep it anyway if Technical Read uses it (it does:
  "Technical Read: Unavailable — pattern detection didn't return", decisions doc ~723). Expect:
  fetch stays, only the card goes.
- `getActionablePatterns` / `vcpTarget`: remove only if no remaining caller.

### 3.5 Tests / verifier
- `analyzeChecks.js` ORDER doesn't list these cards — no change expected; A6 body-text rule
  must still pass for Trade Setup and Fundamentals.
- New `test_key_levels.mjs`: nearest pick, zone math, missing level_scores key, no levels on a
  side, ★ key format (`toFixed(2)`, Day 112 BUG-A), unsorted input.
- `ui-cohesiveness-test.js`: drop any Pattern/Price Structure selectors.
- Parity test must stay 86,400/86,400 (engine untouched).

## 4. Part B — Breakout simple rules (backend `breakout_detection.py`)

### 4.1 Callers (Golden Rule 54/59)
`detect_breakout()` is called only by `breakout_routes.py` (single + batch). Consumers: Analyze
Breakout card, Scan tab badges, the `/breakout-watch` skill (`.claude/commands/breakout-watch.md`
lists state names). Not used by the engine verdict, parity test, or (discontinued) paper job.
`pine/sta_breakout_companion.pine` "mirrors" this Python — after this change it won't. Decision:
leave the Pine file, add a header note that the Python moved to the simple rules (Day 125).

### 4.2 The rules (all on **completed daily bars** — `market_time.drop_forming_bar`)

**Ceiling** = highest high of the 60 completed bars before the last bar (unchanged, honest name:
"60-day high"). Shown as "60-day high $X" so it isn't confused with Trade Setup's ceiling zone.

| State (key kept where meaning matches) | Rule (last completed close C, ceiling H, vol ratio V) |
|---|---|
| `FAILED_BREAKOUT` | A close above H happened in the last 10 bars, and C is now **below** H |
| `EXTENDED_CHASE_RISK` | C more than **5%** above H (breakout within last 10 bars) — "don't chase" |
| `RETEST_ENTRY` | Broke out in last 10 bars, today's low came within 1% of H, C still above H |
| `BREAKOUT_CONFIRMED` | C above H **and** V ≥ **1.5×** (50-day avg, today excluded) **and** C ≤ 5% above H |
| `BREAKOUT_LIGHT_VOLUME` (new) | C above H, V < 1.5× — "broke out on light volume, not confirmed" |
| `BREAKOUT_WATCH` | C within 3% below H |
| `NOT_READY` | everything else (more than 3% below H) |

Priority: Failed → Extended → Retest → Confirmed → Light volume → Watch → Not ready.
**Removed** (not consensus/too many words): `SUPPLY_WARNING`, `BUILDING_BASE`, RS-vs-SPY gate,
candle-quality gate (body/wick/1.2×ATR range), ATR contraction, trend template gate, EMA20.
SPY benchmark fetch in the routes becomes unused → remove it (one fewer network call).

Volume: V = last bar volume / mean(volume of the 50 bars before it). Fewer than 50 → V = null →
volume can't confirm → `BREAKOUT_LIGHT_VOLUME` text says "volume unknown" (never silently pass).

### 4.3 Output
- Keep: `status`, `humanAction`, `currentPrice`, `breakoutLevel`, `rvol`, `asOfDate` (new: the
  completed bar used), `warnings` → replaced by `rules` list of `{rule, met}` for the card.
- Drop `checks`/`evidence` internals no UI reads (verify Scan tab + skill first). API contract
  doc updated; this is a **breaking change** to `status` values → bump backend version.

### 4.4 Card (Analyze) — short
```
🚀 Breakout                               [Breakout Confirmed]
60-day high $342.10 · close $350.20 (2.4% above) · volume 1.8× normal   (Nov 11 close)
Common trader rules, not tested: close above the high, volume 1.5×+, no more than 5% above.
```
Scan tab badge config: add `BREAKOUT_LIGHT_VOLUME`, drop the two removed states.
`/breakout-watch` skill: update its state list.

### 4.5 Tests
New `backend/backtest/test_breakout_rules.py` (synthetic frames, one per state + priority
clashes + forming-bar dropped + <50 bars volume + NaN volume + no 60-bar history).

## 5. Out of scope
- Changing the S&R engine (`support_resistance.py`) — display only.
- Making Breakout's ceiling equal Trade Setup's ceiling — different questions (60-day high is the
  classic "top of the range"); both are labelled plainly instead.
- Any backtest of the breakout rules (user decision D6).
- `/api/stock` forming bar (separate priority), engine bugs (separate).

## 6. Risks
- Removing cards could leave orphan state/fetches → grep every removed identifier; build must be
  warning-clean (except the old ValueTab warning).
- Breaking `status` values could break the Scan badge map or the skill → both updated in the
  same commit; unknown status already renders as raw text (no crash).
- Verifier A2 forbids verdict words; "Breakout Confirmed" is an existing label — re-run live.

---

## 7. Fable plan review (Day 125) — all 16 findings accepted

Verdict: **GO once the 7 MUST-FIX items are in the plan** (done below). This section overrides
§3–§4 where they differ.

| # | Sev | Finding | Change to plan |
|---|---|---|---|
| 1 | MUST | Touch counts are at `srData.meta.levelScores` (camelCase, `backend.py:1907`), not `level_scores`. | Read `meta.levelScores[level.toFixed(2)]`. Agglomerative path emits top-10 only; pivot path all; projected never. Test both. |
| 2 | MUST | "turned here N×" is false: `_score_levels` counts every bar whose high/low was within ±0.5% over ~260 bars (a sideways week counts 5). | Copy: **"near it on N days (last year)"**. ★ tooltip: "a weekly level is within 1.5%". |
| 3 | MUST | Lists are proximity-filtered (≤30% above / ≥20% below) and can contain **projected** ATR/Fib levels (`meta.resistanceProjected`/`supportProjected`). | Projected → "No ceiling within 30% above; $X is a projected level, not a real one." Empty → "No ceiling within 30% above" / "No floor within 20% below". Tests for both. |
| 4 | MUST | `deriveStructureState` uses `support[0]` = the **deepest** support (BUG-B, fixed Day 112 only in `buildKeyLevels`). | Use `S1 = max(support)`, `R1 = min(resistance)`; unit test with ascending input. Display-only — no engine path imports it (GR59 checked). |
| 5 | MUST | Breakout ceiling H includes the breakout bars → a healthy breakout reads "Failed" on day 1. | Use the pivot definition below. |
| 6 | MUST | Volume was judged on today's bar, not the breakout bar. | V on the breakout bar b. |
| 7 | MUST | `warnings` IS read (red chips); batch route, api.js docs, `watchlist-report.md`, `BREAKOUT_ENGINE_SPEC.md` §11/13/15 not listed. | All updated in the same commit. Keep "state, not signal" `humanAction` wording (spec §15). Drop `benchmark`/`benchmarkAvailable` with the SPY fetch. |
| 8 | SHOULD | `/api/patterns` feeds the **verdict** (`trendTemplate` → `runCategoricalAssessment`) and Technical Read. | Fetch stays. Delete `getActionablePatterns`, `vcpTarget`, `actionablePatternsData`, `priceStructure` state, their toggles. |
| 9 | SHOULD | `test_analyze_checks.mjs` fixtures use `card-price-structure`. | Rename to a generic collapsed card; fix lib comment. |
| 10 | SHOULD | `drop_forming_bar(df, now=None) -> (df, dropped)` exists; must run before the `len<80` check and `.tail(260)` in both routes. Cutoff 16:30 ET. | Add `asOfDate`, `barDropped`; card shows "(Nov 11 close)". |
| 11 | SHOULD | `/api/breakout` was never in the live API contracts. | New `API_CONTRACTS_DAY125.md`; Backend 2.53→2.54, frontend v4.61→v4.62, app v4.64→v4.65. README breakout section + file tree, ROADMAP/CLAUDE_CONTEXT "P/E guide" mentions, mark `PRICE_STRUCTURE_CARD_SPEC.md` superseded, fix `backend.py:1757` comment. |
| 12 | SHOULD | P/E deletions are clean (no other callers, no tests). | Delete `describePE`, `PE_GUIDE_BANDS`, `PE_EXTREME`, `PEGuide`. |
| 13 | NICE | ±0.5% = engine `touch_threshold` — correct. | Keep. |
| 14 | NICE | Breakout card has no `data-testid`, so the verifier never checks it. | Add `card-breakout`; A2 allow-list for the state labels. |
| 15 | NICE | A steady climber re-qualifies as a breakout every ~10 bars. | Say so in the "?" note; synthetic-trend test. |
| 16 | NICE | Pine file and `breakout_detection.py` docstring both claim a mirror. | Header note in both. |

### 7.1 Breakout rules — final definition (replaces §4.2; completed bars only, t = last completed bar)
- **Pivot P** = highest high of bars `t-69 … t-10` (the 60-day ceiling that stood before the last 10 days). It never includes the breakout bars, so it doesn't move during the breakout.
- **Breakout bar b** = first bar in `t-9 … t` that closed above P. None → no breakout. `age = t − b`.
- **V** = volume on bar b ÷ average volume of the 50 bars before b; null if fewer than 50.
- Priority:
  1. `FAILED_BREAKOUT` — b exists and today's close < P.
  2. `EXTENDED_CHASE_RISK` — b exists and close > P + 5%.
  3. `RETEST_ENTRY` — b exists, age ≥ 1, today's low ≤ P + 1%, close > P.
  4. `BREAKOUT_CONFIRMED` — b exists, V ≥ 1.5, close between P and P + 5%.
  5. `BREAKOUT_LIGHT_VOLUME` — b exists, V < 1.5 or unknown, same band.
  6. `BREAKOUT_WATCH` — no b, close ≥ P − 3%.
  7. `NOT_READY` — otherwise.
- The episode ends by itself when b leaves the 10-day window. 80 bars minimum still enough.

---

## 8. Build notes (Day 125)

Test-first: `backend/backtest/test_breakout_rules.py` (46) and `frontend/scripts/test_key_levels.mjs` (28)
were written before the code and failed first.

- **Breakout** — `breakout_detection.py` rewritten to §7.1. `prepare_breakout_frame()` lowercases the
  columns, keeps only OHLCV and drops the forming bar; both routes call it before the 80-bar check. The
  SPY fetch was removed. `MIN_VOLUME_BARS = 40` (of the 50) so a few missing volumes don't null
  `rvol`. Rows with NaN high/low/close are dropped and logged. The `rules` list from §4.3 was not
  added: nothing on the card needs it.
- **Wording:** the breakout level is called **"60-day high"** everywhere (card + `humanAction`), so
  "Ceiling" only ever means Trade Setup's nearest real resistance. On RIVN the two differed
  ($14.31 vs $17.16) and both were labelled "ceiling".
- **One-line state:** the rule-2 labels "ATH breakout — blue sky" / "No overhead resistance" became
  "No ceiling above — strong/weak trend". The old label claimed a breakout while the Breakout card
  said "light volume, not confirmed" (AAPL). Missing trend data, or a weak trend with no ADX, now
  shows no line instead of a guessed "Downtrend".
- **Fetch failure is visible:** `fetchBreakout` returns `{error}`; the card shows "Breakout check
  unavailable: …". Before, the card silently disappeared.
- Scan tab: an unknown status shows the raw value. Before, it fell back to "Not Ready", which misreported it.
- `index.css`: body background set to the app's dark grey (white strip under a now-shorter page).
- Deleted: `PriceStructureCard.jsx`, `PatternMiniCard.jsx`, `priceStructureNarrative.js`,
  `getActionablePatterns`/`vcpTarget`/`measuredMoveTarget` (categoricalAssessment.js), the P/E
  guide (`describePE`, `PE_GUIDE_BANDS`, `PE_EXTREME`, `PEGuide`).

**Verification:** Python 46 + 26 + 13; Node 69 + 28 + 17 + 22 + 9; parity 86,400/86,400; build clean
except the old ValueTab warning; live verifier AAPL/NVDA/SMH/JPM/RIVN 40/40 and AAPL/AVGO/MSFT 24/24;
live `/api/breakout` for 6 tickers + batch (bad ticker isolated); live S&R rows checked on AAPL
(projected ceiling shown as projected), NVDA, RIVN.

## 9. Fable code review (Day 125) — verdict: correct; ship after #1–#4

| # | Sev | Finding | Done |
|---|---|---|---|
| 1 | MUST | "Near Ceiling" badge reused the word Trade Setup uses for a different price | Badge → "Near 60-day High"; skill + Pine notes say "60-day high" |
| 2 | SHOULD | `toFixed(1)` could show 1.45× as "1.5×" next to "light volume", or 5.04% as "5.0%" next to "more than 5%" | Card shows 2 dp (backend already rounds to 2 dp) |
| 3 | SHOULD | One-liner said "Below all support" / "No ceiling above" when the lists only cover 20% below / 30% above | Now "No floor within 20% below" / "No ceiling within 30% above — …", limits passed from the rows; test added |
| 4 | SHOULD | Simple-view header hid a failed breakout check | Muted "Breakout: unavailable" chip (error in tooltip); unknown status shown raw |
| 5 | SHOULD | ROADMAP/CLAUDE_CONTEXT versions and "P/E guide" mentions | Left for `/sta-end` (they describe Day 123/124 history; the version rows are updated at close) |
| 6 | NICE | `high60` emitted but never read | Removed (code, test, contract, README, api.js doc) |
| 7 | NICE | 40-of-50 volume rule vs plan's "50" | Contract already says "fewer than 40 of those 50"; kept |
| 8 | NICE | Steady climber re-qualifies every ~10 days, not said on the card | Added to the card note |
| 9 | NICE | Verifier A1 didn't require `card-breakout`; the collapsed-card branch is unreachable now | `card-breakout` added to ORDER + fixture; collapsed branch kept with a comment |
| 10 | NICE | Stale comment in volumeThresholds.js | Reworded |
| 11 | NICE | `rules` list from §4.3 not emitted | Deliberate (§8) |

**Verifier note:** after the fixes, the live verifier timed out on every ticker. Root cause was
not the app: Puppeteer's new headless mode hung on a plain `click()` even on a one-input
`data:` page, while the old headless shell worked (most likely the Mac display was asleep). Run
with `headless: 'shell'` (temporary copy, script unchanged): **AAPL/NVDA/SMH/JPM/RIVN 40/40, AVGO/MSFT 16/16**,
now including the Breakout card in A1.

**User follow-up (Day 125):** the row labels "Ceiling"/"Floor" became the standard **"Resistance"/"Support"**,
and the one-liner says "No resistance within 30% above" / "No support within 20% below". The Breakout card
keeps "60-day high", so "resistance" always means the Trade Setup level.

**User follow-up (Day 125):** the Mean-Reversion Read's track record box (forward-test PF 1.50 / 1.07,
2020–2025 backtest PF 1.16) was removed from the Analyze card: "not necessary, keep only how this read
was formed". The fold now points to the Forward Test tab, which still shows the next-open figures
(`openBasis`, Day 124). `/api/mr` still returns `trackRecord`; the card no longer warns when it's missing.
Verifier AAPL/RIVN 16/16.
