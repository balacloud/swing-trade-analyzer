# Trade Setup card: say so when the live price has already broken the plan (Day 133)

## Context
User screenshot, SOXL.NE, 2026-11-24 afternoon. Entry checks says **$8.54 (now)**. Trade Setup says **Buy $10.73, "2.4% below the last close", reward:risk 0.3:1, "wait for a dip to support"**. SOXL US fell 22% today (43.21 -> 33.65) and SOXL.NE fell the same 22% (10.99 -> 8.54), so the price is real (measured: Alpaca bars, `/api/stock/SOXL.NE`).

Measured cause: two cards use two "now" prices.
- Entry checks uses the live quote (`useLiveQuote`, Day 126 live-entry-timing plan).
- Trade Setup (`PullbackPlan.jsx`, `KeyLevels.jsx`) uses the last COMPLETED close ($10.99, Nov 23). `/api/sr` returns `currentPrice` 10.99 and `entryBasis: zone_high` (checked with curl).
- This was a deliberate Day 126 choice ("a minute-by-minute price there would churn a plan the user acts on", `LIVE_ENTRY_TIMING_PLAN_DAY126.md` line 26), with the note "user may say to move them too (separate plan)". It fails when price falls THROUGH the whole plan: live $8.54 is below the support zone ($9.22-$10.73), so support has broken, yet the card still reads as an actionable "pullback" plan with a Buy that cannot be filled from above.

Outcome wanted: when the live price is already through the plan, the card says so in plain words, shows the plan as "set at the last close, no longer applies", and stops offering it for sizing. The plan numbers do NOT move with live ticks (that stays as designed).

## Decision (recommended; no tuned numbers)
A plan is **void** when a usable live price is
1. below the nearest support zone's low (`meta.zones`, the zone with `nearest && side==='support'`, the same one the card shades) -> reason `below_support` ("support broke"), or
2. no zone known and below the plan's own stop -> reason `below_stop`.
When both hold, reason is `below_support` and the text adds "and below the stop ($X)". Strict `<` (price equal to the zone low is not void). Only the plan's own levels are used, so there is no new threshold to defend (Persona principle 6).
Not void: price inside the zone below the Buy (that is the pullback arriving), price above everything, market closed or no live price (card behaves exactly as today).

## Changes (frontend only; no backend, engine, verdict or backtest change)
1. **New `frontend/src/utils/planStatus.js`**: pure `planStatus({ entry, stop, zones, livePrice })` -> `{ void: bool, reason: 'below_support'|'below_stop'|null, zoneLow, belowStop }`. Never throws; ignores a live price that is not a finite number > 0; missing entry/stop/zone returns `void:false`. One rule in one place (Golden Rule 59).
2. **`PullbackPlan.jsx`**: new props `livePrice` (number|null), `liveTradeTime` (string|null), `lastCloseLabel`. When void:
   - a red banner `data-testid="plan-void"` at the top of the card: "Price is now $8.54 (last trade 2:51pm ET), below the support zone ($9.22-$10.73). Support has broken, so this plan no longer applies. The numbers below were set at the last close ($10.99, Nov 23)."
   - heading sub-label replaced ("wait for a dip to support" would be false);
   - Buy/Stop/Target grid and reward:risk stay visible but muted (opacity), per the "visible state over hidden" rule;
   - a "NOW" tick at the live price on the bar, scale widened to include it (`lo = min(stop, now, live)`); label text is just "NOW" (no price) so the audit's bar regex still reads;
   - "Size this plan ->" is replaced by muted text "Sizing is off while the plan is void." (it would feed a dead Buy into the calculator).
   When not void: output identical to today (regression-tested by snapshot of the rendered text).
3. **`KeyLevels.jsx`**: optional prop `stalePriceNote` (string). When set, render a separate muted line ABOVE the "Price is" row: "Measured at the last close ($10.99), not the live price." The "Price is ..." row text is unchanged, because `audit_cards.py:247` matches `Price is (.*?)(?= Resistance )`.
4. **`App.jsx` (~line 1238)**: compute `planStatus` once from `srData` (via `calculateRiskReward`) and `live.price`, pass `livePrice`, `liveTradeTime`, `stalePriceNote` to both cards. `live` already exists at line 92.
5. **`backend/audit_cards.py`**: bar regex line 139 accepts `(?: CLOSE| NOW)*`; new check `TS-V`: when the page shows the void banner, assert its live price is below the support zone low it quotes, and that the Buy/Stop/Target numbers equal the same values as without it. `test_audit_cards.py` gets the matching cases.
6. **Tests**: new `frontend/scripts/test_plan_status.mjs` (auto-run by `run_all_checks.sh` line 34 glob). Page checker `ui-verify-checklist.js`: new check A14 with a mocked quote (Playwright route override on `/api/quote/<t>`).

## Caller / copy check (Golden Rules 54, 59) - done
- `PullbackPlan` is mounted once (`App.jsx:1238`); `onSizePlan` only calls `autoFillPositionCalculator`.
- Copies of "measured at the last close": `PullbackPlan.jsx`, `KeyLevels.jsx` (via `srData.currentPrice`), `audit_cards.py` (independent mirror). Covered above.
- Nothing reads this for a gate: no verdict, no backtest, no paper-trading code touches the card (grep of `calculateRiskReward`, `entryBasis`, `plan-buy-value`).
- Entry checks already uses the live price, so after this the page says one story: live price in the header and Entry checks, plan marked void against it.

## Edge cases to test (Engineer checklist)
live = zone low (not void), zone low - 0.01 (void), = stop, 0, negative, NaN, string, null, Infinity; no zones; zone present but `entry` null (no_support state: unchanged); `no_atr` state with a void price (banner still shown, no stop); pre-market and after-hours quotes (price present, so void applies, text shows the trade time); a quote for a different ticker (dropped by `acceptQuote`, so no banner); currency mismatch not possible (same provider symbol); CAD/NE ticker; 390px width (banner wraps, no horizontal scroll).

## Verification
1. `cd frontend && node scripts/test_plan_status.mjs`; mutation check: reverse the `<` and watch the boundary cases fail.
2. `backend/test_audit_cards.py`; `./run_all_checks.sh --quick`.
3. Real page, SOXL.NE, with the quote mocked to 8.54 (the market is closed after 16:00 ET, so a real quote would read "closed"): banner, muted numbers, NOW tick, no Size link; same page with the real closed quote: identical to today. Screenshots at 390 px and desktop.
4. `node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN` (48/48 today plus A14).
5. Hand check against the numbers measured today: zone 9.22-10.73, live 8.54 -> void `below_support`; stop 6.78 not crossed so no stop clause.

## Out of scope / parked (to Known Issues)
- The mirror case: live price ABOVE the target (plan done). Same helper can take it later.
- Recomputing zones from the live price (rejected: churns the plan, and zones need completed bars).
- SOXL.NE history is close-only (flat bars, volume 0 on Nov 20): its zones rest on thin data (already known).

## Rollback
Remove the three new props from the `App.jsx` call: the cards return to today's behaviour. No data or API change.

## Process (Golden Rules 55, 64)
After approval: copy this plan to `docs/claude/design/PLAN_VOID_BELOW_SUPPORT_PLAN_DAY133.md`, run the Opus review, apply it and tell the user what changed; then build, `/three-pass`, stamp with `--plan`. Touches a shipped live card with two consumers, so the plan and review are required (Rule 55 b, c).

## Opus review (Day 133): VERDICT: GO WITH CHANGES. All changes applied below.
Reviewer checked the plan against the code. Core idea confirmed (frontend helper, plan numbers stay frozen, nothing gates on it). Verified by us in the code before applying: A14 is taken (`test_analyze_checks.mjs:350`), `audit_cards.py:247` matches the first "Price is", `unclaimed()` flags unclaimed numbers (`audit_cards.py:87-94`), pre/post-market quotes have no age limit (`live_quote.py:16`), regular session cuts at 20 min (`live_quote.py:30`), `basisLabel` and `formatZoneRange` exist.

### Changes applied to the plan (supersede the text above where they differ)
1. **Premise corrected.** KeyLevels does NOT use the last close: it uses `srData.currentPrice`, which mid-session is the forming bar (`backend.py:1857`), and the backend picks each zone's side/nearest/insideZone from that same price. So the zones were already re-sided at page load for tickers that have a forming bar. SOXL.NE hit this only because its `/api/sr` had no forming bar (currentPrice 10.99). Void fires when price moves through the zone after the levels loaded, or when the provider has no forming bar. The stale note names the price the levels were really measured at (`srData.currentPrice`, "when the levels loaded"); it says "last close" only when `candle.barComplete !== false`.
2. **Banner wording = facts, not verdicts** (user rule, Day 126; and an undercut-and-reclaim is the classic shakeout entry). Text: "Last trade $8.54 (2:51pm ET) is below the support zone ($9.22 – $10.73). This plan was set at the last close ($10.99, Nov 23); its Buy is above the price now." No "Support has broken, so this plan no longer applies". Banner does NOT start with "Price is" (would hijack `audit_cards.py:247`).
3. **Void applies only in the `live` and `recent` quote states.** For `pre`/`post` (no age limit, thin) show at most a muted fact line, no void styling, no Size removal.
4. **Audit/page checks.** New page check is **A15** (A14 exists); add mustPass/mustFail fixtures in `test_analyze_checks.mjs` (line 102 asserts every CHECK_ID runs). In `audit_cards.py` the banner and note numbers are claimed with ` § ` by a new TS-V check (otherwise U-TS flags them). The NOW tick is rendered LAST in the DOM (after the target span) so neither bar regex (lines 139 and 222) needs a change.
5. **One label, one number.** Zone range via `formatZoneRange` (" – "); "last close ($10.99, Nov 23)" from the card's own `now` and `prevBar.date`/`candle.date`, not `live.lastClose`; bar label from `basisLabel(live)`, not a fixed "NOW".
6. **`no_atr` state** returns early (`PullbackPlan.jsx:53-61`): banner added there explicitly; `no_price` (line 45) unchanged, no banner. Tested.
7. **Size link:** replaced by a visible muted, disabled-looking line (not removed), per "visible state over hidden".
8. **390px label guard:** the new tick gets the same kind of guard as `nowNearEntry` against the BUY label (bottom row) and the stop/target labels (top row).
9. Legacy engine (no zones) uses the `below_stop` rule; a non-empty `support` always means a nearest support zone exists in the simple engine; a zone low is always at or below `currentPrice`, so "close already below the zone" is the `no_support` state (confirmed by reviewer).

### Parked (Known Issues): after about 16:20 ET NEO tickers get "no recent trades", so the banner disappears while `srData` stays stale until the next analysis; mirror case (price above the target); name the next support zone below in the banner (optional).
### Docs to update at close: pointer in `LIVE_ENTRY_TIMING_PLAN_DAY126.md` section 1.1, Known Issues entry, ENGINEER.md row, AUDIT_COVERAGE_LEDGER.
### Could not verify (reviewer): whether Playwright `route.fulfill` responses reach the checker's response capture (`ui-verify-checklist.js:85`); the exact SOXL.NE live payload; `market_time.session_for` around 16:00-16:20. We test these in the build.
