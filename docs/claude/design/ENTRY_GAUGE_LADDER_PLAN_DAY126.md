# Entry checks: gauge + ladder (Day 126) — PLAN v2 (Opus review applied)

Status: user approved the mock-up (blend of A ladder + B gauge, "use fantastic colour combinations"). Mock-up: artifact 5qPzFFV5nAmJE5pHGJX8Xx.
Display only. No analysis, number or rule changes. Facts, not verdicts.

## 1. What changes
Replace `TimingRuler` (price-scale ruler) in `frontend/src/components/TechnicalRead.jsx` with `TimingGauge`:
- **Gauge (top):** scale = normal-day moves (ATR units) centred on the 21-day average. Range −5…+3, price outside range pins to the edge (dot + label clamp inside the card). One small tick per unit; bigger coloured ticks for 21d / 200d / 50d with short labels under them; dot for the compared price with `$price` above and `N.N days below|above` under it. Fill between dot and 21d tick.
- **Ladder (under):** rows 50-day, 200-day, 21-day (highest price first, i.e. sorted by price descending, any missing average is left out), then a highlighted row `Now` (live) or `Last close` (no live price). Columns: colour key, name, price, % the average sits above/below the compared price (`(avg - price) / price`, signed, 1 decimal).
- Sentence, sub-line (`That is N.N of a normal day's move below it. A normal day's move here is $X`), basis label, `timing-close-note`, uptrend heading note: unchanged.
- Gauge caption: "Each tick is one normal day's move. The coloured ticks are the averages."

## 2. Colours (identity, never good/bad)
No red/green: the colour names a line, it does not judge it. Dark card slate.
- Price (dot, price label, `Now` row, days label): sky `#38bdf8` with soft glow.
- 21-day average (reference): amber `#fbbf24`.
- 50-day: violet `#a78bfa`. 200-day: pink `#f472b6`.
- Gap fill: gradient sky → amber between the dot and the 21d tick.
- Ladder key marks and gauge ticks use the same colour per line, so the ladder is the legend.
Tailwind tokens where possible (sky-400, amber-400, violet-400, pink-400); inline style only for the gradient and glow.

## 3. Code
- `technicalReadChecks.js` `deriveEntryTiming`: keep inputs/outputs; add `gaugeX(v)` data: returns `marks` (key, price, caption, units = (price−ema21)/atr, gapPct = (avg−price)/price*100), `units` for the price, `lo=-5, hi=3`. Remove `lo/hi` price-pad fields only if no other caller uses them (grep first, Golden Rule 54).
- Clamp rule: `x = (clamp(units, -5, 3) + 5) / 8 * 100`. Marks use the same clamp (a 50-day far above 21d pins at the right edge; labels never overlap: labels that would sit closer than 14% drop to a second row).
- Test ids kept: `timing-ruler` (now the gauge wrapper), `timing-price` (the price label above the dot), `timing-tick` (1–3 coloured ticks, `data-key`, `data-price`), `timing-sentence`, `timing-basis`, `timing-close-note`. New: `timing-ladder-row` (`data-key`, `data-price`, `data-gap`), `timing-now-row`.

## 4. Checks
- A12: dot price label = compared price (unchanged); coloured ticks 1–3 and equal the real averages (unchanged); NEW ladder rows equal the same averages in descending price order, each gap equals `(avg−price)/price` within 0.1; the Now/Last close row price = compared price and its name matches the basis; no verdict wording.
- A13: close-note rule unchanged.
- Unit tests `test_entry_timing.mjs`: units, clamp at both edges, missing 50/200-day, gap % sign, descending order, price exactly at the 21-day average (`side: 'at'`), live vs close basis.

## 5. Risks to check
1. Page-level horizontal scroll at 390px (pre-existing Known Issue): the new block must add none; screenshot 390 and 1280.
2. Price far outside −5…+3 (RIVN-type gaps, SOXL leveraged): dot pinned at the edge; label still readable; sentence carries the real number.
3. Missing averages (short history): gauge still draws with fewer ticks; ladder shows fewer rows; no invented data.
4. ATR small / huge: units still finite; ATR ≤ 0 stays "unavailable".
5. Light theme / dark: app is dark only; check contrast of pink/violet on slate.
6. Phone width: labels 21d/200d/50d may crowd when the averages are close — second-row drop rule.
7. Accessibility: gauge gets an `aria-label` with the same sentence; ladder is a real table or `role="table"`.

## 6. Process
Plan → Opus review → build after the user says go → three passes → Known Issues entry → commit.

## 7. Review result and changes (v2) — Opus: GO WITH CHANGES, all 13 points accepted
1. **Gap % base.** Ladder gap = `pctDiff(price, avg)` = (price − avg)/avg, the same base and sign as the sentence and uptrend rows. Column header says "price vs it". Signed numbers, neutral colour (no red/green).
2. **Names.** Delete price `lo`/`hi`; new `unitsMin = -5`, `unitsMax = 3`. Rewrite the 7 tests in `test_entry_timing.mjs` that used `lo`/`hi`.
3. **Row label.** `Now` row name = `basisLabel(live)` capitalised ("Now", "After hours", "Pre-market", "Last trade 2:51pm ET", "Last close"). A12: row name equals the `timing-basis` text without brackets.
4. **Off-scale honesty.** A clamped dot or tick gets a visible off-scale mark (edge arrow "◂ / ▸") and its label carries the real number; aria-label states it. Items pinned at the same edge stack on separate rows. Tests: price + 200d both pinned left, 50d + price both pinned right.
5. **Label layout.** Dot label (`N.N day-moves below`) sits ABOVE the bar next to the price; tick labels under the bar, up to 3 rows, min gap measured in px not %. 390px screenshots: clustered averages, price near the 21d, price pinned.
6. **Wording.** "day-moves", not "days" ("1.5 day-moves below"). `side === 'at'` text: "at the 21-day average".
7. **Math.** mark units = `(mark.price − ema21) / atr` (21d = 0); price units = `(price − ema21)/atr`. Scale −5…+3 is NOT centred: the 21d sits at 62.5% (more room below, where pullbacks are); say so in the caption/code comment, not "centred".
8. **Ladder order.** True price order, descending, with the Now/Last close row at its REAL price position (not always last). A12 checks all rows descending.
9. **Files.** Also update `ui-verify-checklist.js` readers (ladder rows key/price/gap, now row price/name, dot label), `test_analyze_checks.mjs` fixture + new fail cases (gap sign wrong, ladder out of order, Now price ≠ dot, Now name ≠ basis), and A13 wording ("ruler" → "gauge").
10. **Honest A12.** The ticks are not compared to an outside source (averages come from the browser indicators). A12 checks the page against itself: ladder prices = tick prices (same key), Now row = dot price, gap = pctDiff within 0.1.
11. **Copy.** Rewrite the "Why" text ("The ruler marks … at their real prices") and the doc comments in `technicalReadChecks.js` and `TechnicalRead.jsx`: ticks sit at day-move distances, prices are in the ladder.
12. **Accessibility/phone.** Ladder is a real `<table>` (`<th scope>`, `timing-ladder-row` on `<tr>`); gauge ticks/dot `aria-hidden`, gauge wrapper `aria-label` with the sentence and any off-scale facts; no `overflow-hidden` clipping the glow (inset padding instead); `tabular-nums`, no fixed widths; check "$1,234.56" and "+123.4%" at 390px.
13. **Guards.** ATR ≤ 0 stays "unavailable" before gauge or ladder is built. "Last close" row uses the `/api/stock` price, same as the existing basis label (see LIVE_ENTRY_TIMING_PLAN_DAY126.md).
