# Simple S&R — the switch (Day 126)

**Status:** PLAN. Review: three escalating passes by Claude (user, Day 126: no Fable this time).
Build waits for the user's "switch". Suggested split: plan on Opus, build on Sonnet (Golden Rule 55).
**Inputs:** `SIMPLE_SR_PLAN_DAY125.md` (§2, §8, §9, §10 build notes), `SIMPLE_SR_COMPARISON_DAY126.md`,
review page https://claude.ai/artifact/UN9WP4ahzrc1T72JSjuNKn. The Simple Checklist is gone
(`REMOVE_SIMPLE_CHECKLIST_PLAN_DAY126.md`), so only Trade Setup reads the levels and nothing grades them.

## 0. Engine simplification first (judgment call, flagged to the user)

The 30-stock run showed ★ weekly on 89% of nearest zones, and still 89% when the weekly swing must
sit inside the zone. It carries no information. But it is not only a label: the engine's rule 4
"prefer a zone with 2+ turns **or ★**" uses it, so dropping only the display would leave a hidden
input (PERSONA Architect's Lens: display must match the engine). Since 89% of 1-turn zones are ★,
"prefer" already barely did anything.

**Change:** remove weekly swings and the preference rule from `simple_sr.py`. The engine becomes:
swing highs/lows (5 bars each side, last 252 daily bars) → zones (gap ≤ 0.5 ATR, width ≤ 1 ATR) →
the **nearest** zone below/at price and the nearest above, in the 20% / 30% window. Every zone keeps
its turn count, shown to the user as "turned here N×". The user judges whether 1 turn is enough
(Reddit §9 was mixed on it; this is "human judgment" applied to levels too).
Tests: drop the weekly and preference checks, add "nearest wins regardless of turn count" and
"turn count reported". Re-run `compare_sr_engines.py` and republish the review page so the user
decides on the final engine, not the earlier one.

## 1. Flip
`constants.SR_ENGINE = 'simple'`. `?engine=legacy` stays as a one-request rollback/preview.
`support_resistance.py` stays for `backtest_holistic.py` / the discontinued paper job (Golden Rule 54).

## 2. Frontend

| File | Change |
|---|---|
| `utils/keyLevels.js` | Read `meta.zones` (the `nearest: true` zone per side). Row = `low – high` (one price if equal) · % away · "turned here N×"; kinds `level` / `inside` ("price is inside this zone") / `none`. Remove the ±0.5% band, `levelScores`, `confluence_map`, `projected`. `deriveStructureState` gets zone edges; "near" = inside, or within 2 ATR of the nearest edge (§8 #17). |
| `components/KeyLevels.jsx` | New rows, no ★. Footnote: "Zones are where price turned before (swing highs and lows, last year). The last 5 trading days can't be confirmed yet. Common trader rules, not tested." |
| `utils/riskRewardCalc.js`, `components/PullbackPlan.jsx` | Remove `targetProjected` and every "projected" branch and the ATH help text. No resistance → "No resistance within 30% above"; if `meta.nearHigh52w`, add "the stock is at its 52-week high", no target. Keep "Size this plan →". |
| `components/PullbackPlan.jsx` price bar | **No chart (user, Day 126: "lets not do charts if it's too complex and going to add to decision fatigue; just wanted something better visually").** Instead, shade the nearest support zone (faint green) and resistance zone (faint red) on the existing Stop/Buy/Target/Now bar, same price scale. No new card, no new numbers. A zone outside the bar's range is not drawn (the row still lists it). |
| `services/api.js` | Docs only (fields; `meta.zones`, `meta.nearHigh52w`; no projections). Passes `meta` through already. |

## 3. Data backing (engineering standard)

| UI element | Source | Exists? |
|---|---|---|
| Support/Resistance rows | `/api/sr` `meta.zones[nearest]` | yes (built Day 126) |
| Buy / Stop / Target | `riskRewardCalc(srData)` = `max(support)` (zone high), `−2·ATR`, `suggestedTarget` (zone low) | yes |
| "at its 52-week high" | `meta.nearHigh52w` | yes |
| Zone shading on the price bar | same nearest zones as the rows (`meta.zones`) | yes |

## 4. Silent failures and states

| Situation | Shown |
|---|---|
| `/api/sr` failed | existing PullbackPlan `no_data` message; no rows, no shading |
| No support / no resistance | row says "None within 20% below" / "None within 30% above"; only existing zones are shaded |
| Price inside a zone | row "price is inside this zone"; the Now tick sits inside the green shading |

## 5. Checker and tests
- `test_simple_sr.py` updated (§0). `test_key_levels.mjs` rewritten for zones. Zone-shading positions come from PullbackPlan's existing `pos()` scale; a pure helper `zoneSpan(zone, lo, hi)` (clipped to the bar, null when outside) gets unit tests.
- Page checker **A10** (Simple S&R plan §8 #15): Buy == `suggestedEntry` == `max(support)`; Support/Resistance rows == the `nearest` zones; "None within" iff that side is empty. Runner captures `/api/sr` like the other API calls. Checks go 7 → 8.
- `npm run build`, all node tests, parity 86,400, checker on AAPL/NVDA/SMH/JPM/RIVN, live look at AAPL (no resistance, at 52-week high), RIVN (low price), SMH (ETF).

## 6. Docs
API_CONTRACTS (breaking: no `levelScores`/`mtf`/projected on the default engine), README S&R section,
route docstring, DEVELOPER_ONBOARDING, AUDIT_COVERAGE_LEDGER, ANALYZE_CLEANUP_PLAN §3.2 cross-link,
Day 125 Known Issue "S&R engine due for replacement" closes. Golden Rule 63 check: "Resistance" and
"Support" still mean one price each on the page; the breakout card's level stays "60-day high".

## 7. Three review passes (Golden Rule 41), run after the build
1. Does it do what this plan says (tests, checker, live)?
2. Edge cases: inside a zone, no zones, price above every zone, < 60 bars, ETF, $1 stock, NaN rows.
3. Adversarial: anything else reading the removed fields (grep `levelScores`, `confluence_map`, `resistanceProjected`, `mtf`, `weekly`); Scan tab's 76 `/api/sr` calls (payload size, speed); the shading and the rows can't show different prices.
