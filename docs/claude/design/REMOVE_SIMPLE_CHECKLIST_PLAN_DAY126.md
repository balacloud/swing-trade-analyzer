# Remove the Simple Checklist — Plan (Day 126)

**Status:** PLAN — for Fable review, then build.
**Why (user, Day 126):** "do we need simple check list, you can entirely remove it ... I don't want
decision fatigue." Earlier the same day: "leave risk reward ratio to human judgement and only focus
on building deterministic simple S&R."

**Claude's read (PERSONA):** agree. The checklist's "✅ TRADE / ⏸️ No Trade" (9 of 9) is the last
mechanical trade verdict on screen. BUY/HOLD/AVOID was removed everywhere on Day 123, and R:R was
made informational on Day 109; this finishes both decisions. The 9/9 rule was never shown to have an
edge. With honest nearest levels, check #4 (R:R ≥ 2) almost never passes (SIMPLE_SR_PLAN §10,
Finding 1), so the badge would read "No Trade" almost always: words with no decision value. The
discipline a checklist gives (same checks, same order) is kept by the Full Analysis cards.

Not changed: the categorical engine and its 86,400-combo parity test, Technical Read, Market
backdrop, Trade Setup's numbers, MR Read, Fundamentals, Breakout, all backend code.

---

## 1. What is removed

| Where | What |
|---|---|
| `frontend/src/App.jsx:43` | `import { calculateSimplifiedAnalysis }` |
| `App.jsx:150-151` | `simplifiedResult` and `analysisView` state |
| `App.jsx:280, 400, 441, 469` | resets, the `calculateSimplifiedAnalysis(...)` call, `setSimplifiedResult` |
| `App.jsx:~998-1022` | Full / Simple view toggle (only one view is left, so no toggle) |
| `App.jsx:1050` | `analysisView === 'full' &&` condition → always render the full view |
| `App.jsx:~1378-1556` | the whole Simple view block (verdict card, 9 criterion cards, "Trade Decision", methodology note, "View Full Analysis →") |
| `frontend/src/utils/simplifiedScoring.js` | deleted (only caller is App.jsx, verified by grep) |
| `frontend/scripts/lib/analyzeChecks.js` | check A8 "Simple view badge" removed; the check count changes from 8 to 7 (update the runner's expected total, its unit tests, and any "N/N" in docs) |
| Comments that cite `simplifiedScoring.js` as a source | `absoluteMomentum.js:8,69`, `liquidityThresholds.js:8`, `categoricalAssessment.js:815`: rewrite as history ("was also used by the Simple Checklist, removed Day 126"), and confirm none imports it |

## 2. Nothing unique may be lost (check each before deleting)

The 9 criteria and where the same fact already appears on Full Analysis. **Build step 1 confirms
each row in the live page; any "no" stops the build and comes back to the user.**

| Checklist item | Shown on Full Analysis by |
|---|---|
| Trend (price vs 50/200 SMA) | Technical Read |
| Momentum (RS vs SPY ≥ 1.0) + absolute-momentum read (Day 117) | RS / Technical Read (absoluteMomentum.js has its own Full-view path, line 69: verify) |
| Setup (stop % vs 7/9/10% cap) | Trade Setup shows the stop % from the buy (no cap judgment; that is the point) |
| Risk/Reward ≥ 2 | Trade Setup shows the ratio + rule-of-thumb text, no grade |
| 52-week range | Technical Read ("% off the high") |
| Volume | Trade Setup volume note / Technical Read |
| ADX | Technical Read (verify; if absent, list it, don't add it silently) |
| Market | Market backdrop card |
| 200 SMA trend | Technical Read |

## 3. What is moved, not lost

**The "Calculate Position Size →" button** (`App.jsx:1525-1536`) is the ONLY caller of
`autoFillPositionCalculator` (grep: one call site). It only appeared on a 9/9 TRADE, so in practice it
almost never showed. Move it to the **Trade Setup card** (`PullbackPlan.jsx`) as a small link, "Size
this plan →", shown when the plan has a buy and a stop (`plan.state === 'ok'`), using that card's own
`entry` and `stop` (Golden Rule 63: one Buy price, one Stop price). No verdict gates it. `PullbackPlan`
gets an `onSizePlan(entry, stop)` prop; App passes `autoFillPositionCalculator` bound to the ticker.

## 4. Docs (same commit)
README (Simple Checklist feature list, line ~77, ~156, architecture diagram ~280),
`DEVELOPER_ONBOARDING.md`, `HOW_STOCK_PICKING_WORKS` explainer (if it mentions the checklist),
ROADMAP Priority #18 text ("criteria 3/4 read these levels" no longer true), SIMPLE_SR_PLAN §3
(callers list), `compare_sr_engines.py` docstring (criteria 3/4 columns are now historical),
`sr_plan.py` docstring. `backtest/backtest_simplified.py` stays as a historical backtest: add one
header line that the live checklist it mirrored was removed Day 126 (Golden Rule 59: no live copy
left to drift from).

## 5. Verification
1. Grep: no `simplifiedResult`, `analysisView`, `calculateSimplifiedAnalysis`, `simplifiedScoring` left in `frontend/src`.
2. `npm run build` clean (only the known ValueTab warning).
3. Node unit tests (key levels, analyzeChecks, etc.) pass; parity 86,400 (untouched, run anyway).
4. Page checker (`node scripts/ui-verify-checklist.js`, `headless: 'shell'` if needed) on AAPL/NVDA/SMH/JPM/RIVN: all checks pass at the new count.
5. Live: Analyze AAPL shows no toggle, Full Analysis renders; "Size this plan →" fills the position calculator with the Trade Setup's exact Buy and Stop; a ticker with no support shows no link.
6. Three escalating review passes (Golden Rule 41), then Fable code review, then user sign-off.

## 6. Order with the S&R switch
Do this first. It removes the only place that graded R:R and stop width, so the S&R switch
(SIMPLE_SR_PLAN §10) then only has to change Trade Setup's rows and plan.

---

## 7. Fable plan review (Day 126) — GO with must-fixes. Overrides §1–§6 where they differ.

| # | Sev | Finding | Change |
|---|---|---|---|
| 1 | MUST | Visible text missed: Analyze empty-state footer "9-criterion Simple Checklist • …" (`App.jsx:1570`); comment `App.jsx:1192` | Add to §1 |
| 2 | MUST | `frontend/scripts/ui-cohesiveness-test.js:176-187,224,259` clicks the Simple toggle; after removal it prints `N/A` forever (silent) | Remove the block and the "Simple view" column; run it in §5 |
| 3 | MUST | ADX is genuinely lost when ≥ 20: Full view prints ADX only when < 20 (`categoricalAssessment.js:866`, `TechnicalRead.jsx:233`) | **User decided (Day 126): accept the loss.** The page speaks when ADX < 20; nothing added |
| 4 | MUST | README also at `:701` (user-guide step) and `:1683` (file tree); `:1439/:1574/:1577/:1579` are history/backlog lines that mention it | Add 701, 1683; update 1579 (Priority 14) wording; leave changelog history |
| 5 | SHOULD | §2 "Volume" row was **liquidity** ($ volume vs cap threshold), shown on the Price & RS card `App.jsx:1190-1205`, not RVOL | Fix row |
| 6 | SHOULD | 52-wk (checklist: % of range; Full: % below the high) and Trend (50>200 ordering only in the hidden 8-count) are the same fact with a different number | Mark "same fact, different number"; not a bug |
| 7 | SHOULD | Position-size link: pass `Number(entry.toFixed(2))`, `Number(stop.toFixed(2))` so shares match the shown inputs (GR 63). The link switches to the Settings tab (`App.jsx:383`) | Adopt; §5 asserts `calcTicker`, entry, stop filled |
| 8 | SHOULD | A8 exact touch list: `analyzeChecks.js:15,23,164-174,188`; runner `ui-verify-checklist.js:11,91,135-147,154,200-202`; tests `test_analyze_checks.mjs:60,192-198`. Unit 69 → 62, live 40/40 → 35/35. `DEVELOPER_ONBOARDING.md:139` "8 automated checks" changes; Day-124 dated docs stay | Replace A8 with an A2 assertion: fail if the page shows "Simple Checklist", "criteria met" or a Full/Simple toggle |
| 9 | SHOULD | Live docs: `HOW_STOCK_PICKING_WORKS.html` is titled after the checklist with a "Path 1 · Simple Checklist" panel (`:600-771`), published Artifact → rewrite + republish same URL, status board title. `KNOWN_ISSUES_DAY125:159` (two 1-year-return calcs) closes. `CLAUDE_CONTEXT.md:208` item moot. Comments `technicalReadChecks.js:5`, `volumeThresholds.js:207`, `absoluteMomentum.js:56-60,68`. `.claude/settings.local.json:54` stale permission (harmless; not edited by Claude) | Add to §4 |
| 10 | NICE | S&R switch adds verifier A10 (Buy == suggestedEntry == max(support)): checks go 8 → 7 → 8 | Note only; never re-add A8 |
| 11 | NICE | `autoFillPositionCalculator` returns silently on missing entry/stop (`App.jsx:363`) | `console.warn` |
| 12 | NICE | Removed line "Position sizing needs a stop … (ATR missing)" | PullbackPlan `no_atr` message adds "so it can't be sized" |
| 13 | NICE | `PAPER_TRADING_PREREGISTRATION.md:34,43` lists `simplifiedScoring.js` (frozen record) | Footnote only |

Verified by Claude against the code before adopting: #1 (`App.jsx:1570`), #2 (`ui-cohesiveness-test.js:176-178`), #3 (`categoricalAssessment.js:865-866`), #4 (README lines).
