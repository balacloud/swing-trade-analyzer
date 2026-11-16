# Entry timing uses the live price: Plan v2 (Day 126, revised after the Opus review)

**Status:** PLAN v2. Step 1 (plan) and step 2 (independent Opus review, verdict **GO with 3 must-fixes**) done; step 3 (build) and step 4 (three passes) follow, after the user says go.
**Why (user, Day 126, screenshot):** NVDA header says Now $156.14, but the Entry checks card still says "$162.85 is 16.1% below its 21-day average" with a white $162.85 bubble. "This still shows 162 instead of 156?" The card contradicts the header. The live price (commit 846cd4b6) was added to the ruler only as a small amber mark, with a note "the numbers above use the last close".
**Rule:** the entry-timing block compares the live price to the averages when a live price exists. The averages and the ATR stay on completed daily bars. No indicator, verdict, stop or backtest number changes.

## 0. What is true today
| Fact | Where |
|---|---|
| The sentence, the white bubble, "N of a normal day's move" and the blue span all come from `deriveEntryTiming({price: analysisResult.currentPrice})` = the `/api/stock` price (the last bar). | `TechnicalRead.jsx:223`, `technicalReadChecks.js:100` |
| `livePrice` is already a scale input and gets the amber `live-tick`; it never changes `atrUnits`, `pctFromEma`, `side`. Tested in `test_entry_timing.mjs`. | commit 846cd4b6 |
| Page check A12 asserts the white bubble text equals `api.stock.currentPrice`, 1 to 3 `timing-tick` marks. A13 asserts exactly one `live-tick` when a usable live price and a ruler exist. | `analyzeChecks.js` |
| Other readers of the price on the page: Trade Setup / Pullback plan (`srData.currentPrice`, "support X% below now"), Key Levels, ATR % (`TechnicalRead.jsx:203`), header lines 1092/1104/1128 (dollar volume), MR card (`App.jsx:589`, `1988`). All on the last bar. | grep |

## 1. Decision
When a usable live price exists (`live.price != null`), `deriveEntryTiming` measures from it:
- `price` (the compared price) = the live price; new field `basis` = `'live'`; the close is kept as `lastClose` (the bar price passed in).
- Sentence: `$156.14 is 19.6% below its 21-day average ($194.17)`; sub-line: `That is 3.7 of a normal day's move below it ...`; the white bubble shows the live price; the blue span runs live price to the 21-day line.
- The close becomes a small grey note under the ruler: `Last close $162.85 · Nov 13` (replaces the amber-mark note). The amber `live-tick` marker and its row go away (the bubble is now the live price, so a second marker would repeat it).
- Without a live price (closed, unavailable, none): exactly today's behaviour on the close. Basis `'close'`.
- A short label on the bubble row says which basis is shown: `now` vs `last close`, so the reader never has to guess.

What does NOT change: EMA21 / SMA50 / SMA200 / ATR inputs (completed bars), the Trade Setup and Pullback plan, Key Levels, volume card, header, MR card, verdict parity, backtests, A12's check that closed-state behaviour is as before.

### 1.1 Open decision, default taken
Trade Setup / Pullback plan "support X% below now" and Key Levels still use the last close (`srData.currentPrice`). Default: leave them (Trade Setup stops and buy level are plans built from completed bars; a minute-by-minute price there would churn a plan the user acts on). The page would then show the live price in the header and entry block and the close in the plan. The plan card text already says "today's price"; to be fixed in wording only if the review asks. User may say to move them too (separate plan).

## 2. Code changes
- `utils/technicalReadChecks.js`: `deriveEntryTiming` takes `livePrice`; when valid it is the compared `price` (so `atrUnits`, `pctFromEma`, `side`, `lo/hi` all follow it); return `basis`, `lastClose` (the bar price). Remove the live-only scale logic and the `live` field (no second marker). Validation unchanged (finite, > 0 else ignored).
- `components/TechnicalRead.jsx`: pass `price` + `livePrice`; bubble text and basis label; remove the `live-tick` row and the amber stroke; add `data-testid="timing-close-note"` with `Last close $X · date`. Pass the last-close date from the quote.
- `App.jsx`: pass `live.lastClose` date label (or null).
- Page checks: A12 expects bubble = live price when a usable quote exists, else `api.stock.currentPrice`; A13 loses `live-tick`, gains `timing-close-note` present only with a usable live price, and the close note price equal to the quote's `last_close`. `live-tick` must be absent. Ruler `timing-tick` marks (1 to 3) unchanged.
- Tests: `test_entry_timing.mjs` (live drives side, pctFromEma, atrUnits, scale, fallback with every bad value, boundary at the 21-day line, live above all marks, live equals close); `test_analyze_checks.mjs` updated cases.

## 3. Callers (Golden Rule 54, re-grep at build)
`deriveEntryTiming`: `TechnicalRead.jsx` only (plus `test_entry_timing.mjs`). `timing-price` / `timing-sentence`: `analyzeChecks.js`, `ui-verify-checklist.js`. `live-tick`: A13, `TechnicalRead.jsx`, tests.

## 4. Risks
- The block now moves every minute while open; the sentence flips between "above" and "below" the average on a cross. Accepted; the time is in the header.
- A flicker-free wording: `side` has an "at" band of 0.05%.
- Two prices on one page (header live, Trade Setup close): the labels say which is which; open decision 1.1.
- `/api/stock` forming-bar Known Issue: not touched here; the fallback (no live price) still reads the same bar as before.

## 5. Tests and checks
Frontend unit tests above; page checker on AAPL, SOXL.NE, NVDA, RIVN (A12 and A13 updated); screenshots at 390 px and desktop with a live price and with the market closed (mock the quote closed to see the fallback); three passes; Known Issues entry; commit.

## 6. Review result and v2 changes (Opus, verdict GO with must-fixes; decision 1.1 stays)
Verified by the reviewer: one caller of `deriveEntryTiming`; nothing here feeds an indicator, verdict or stop; validation and the 0.05% "at" band are as the plan says; removing the amber marker is right.

**Must-fixes now part of the build**
1. **One meaning of "last close".** The note comes from the quote's own `last_close` (`live.lastClose`, a completed bar), never from the `/api/stock` price (which can be a partial bar, Known Issue Medium). `deriveEntryTiming` does not return a `lastClose` field.
2. **"Now" means the live price only.** `PullbackPlan.jsx` shows a "NOW" tick (line 111) and says "below now" (125), "today's price" (22, 169) on the close. Reword those to "last close" (wording only, no logic). Same for Key Levels wording if it says now/today. This is what makes decision 1.1 (leave Trade Setup on the close) safe.
3. **Same-card contradiction.** The "Is it in an uptrend?" rows above the ruler use the close (`price_position.current`). Keep them on the close (it is the engine's count) and label that block "at the last close ($X, date)".

**Should-fixes taken**
4. Basis label follows the state: `now` only for Live; `pre-market` / `after hours` for those sessions; `last trade 2:51pm ET` for a trade older than 2 minutes; `last close` in the fallback. Reuse the header's status words (one source, `describeLiveQuote`).
5. Do not claim the averages and ATR are always completed bars: while the forming-bar Known Issue is open, a mid-day cache miss can include today's partial bar in them. Say so in the Known Issues entry.
6. Page checker work listed: `ui-verify-checklist.js` reads `timing-close-note` and the basis label instead of `live-tick`; A13 fixture and cases rewritten.
7. A12 strengthened: `timing-sentence` starts with the same price as the bubble; the basis label is "last close" whenever there is no usable live price.
8. Flaky-check guard: the page polls each minute while the checker compares to one captured quote. The checker reads the page right after the captured response and accepts the next captured response too.
