# Pullback plan: the Buy when price is already inside the support zone (Day 127) — PLAN v1
User decision after the persona read (PERSONA: capital preservation, sizing over entry, Architect's Lens "one story, one rule, one place"): when price is already inside the nearest support zone, the Buy is the LAST CLOSE (clamped into the zone), not the zone's top.

## Problem (measured, universe run)
Buy = `max(support)` = the nearest support zone's HIGH. When price is inside that zone the Buy is ABOVE the market: SOXL.NE +8.9%, AMD +5.3%, FCX +4.6%, ETN +3.9%, PLD +1.8%. A plan titled "wait for a dip to support, then buy" with a Buy above price fills immediately; risk/reward are measured from a price you will not get, and "Size this plan" hands that entry and its stop to the position-size calculator.
Already codified elsewhere: `backend/validation/engine.py:~435` has a sanity check "Entry should be below current price".

## Change
1. `backend/sr_plan.py` `trade_plan(support, resistance, atr, entry_override=None)`: when `entry_override` is given it is the entry (rounded 2 dp); stop/target/R:R follow from it as today (stop = max(0.01, entry - 2 ATR), target = min(resistance), R:R = (target - entry)/(entry - stop)). Default behaviour unchanged (legacy engine, no zone).
2. `backend/backend.py` /api/sr (~2024): for the simple engine, when the nearest SUPPORT zone has `insideZone: true`, `entry_override = clamp(last COMPLETED close, zone.low, zone.high)` (last completed close from the forming-bar-dropped frame `df_done`, the same close the card calls "the last close"). Otherwise none. Add `meta.entryBasis`: `'zone_high'` (price above the zone, as today), `'last_close_inside_zone'`.
3. `frontend/src/utils/riskRewardCalc.js`: `entry = Number.isFinite(srData.suggestedEntry) ? srData.suggestedEntry : max(support)` (ONE place decides, the backend; the max() stays only as a fallback for an old cached payload). Stop/target/R:R arithmetic unchanged.
4. `PullbackPlan.jsx`: Buy box wording when `meta.entryBasis === 'last_close_inside_zone'`: "the last close; price is already inside the support zone ($a - $b)" (today: "top of the support zone; price is inside it at the last close"). The subtitle "wait for a dip to support" stays for the other case; for the inside case the card header says "price is already at support" (facts: no advice). "Size this plan" passes the new entry/stop (roundMoney).
5. Page check A10 (`analyzeChecks.js:~202-219`): expect `suggestedEntry` from the payload; when the nearest support zone is inside, require zone.low <= suggestedEntry <= zone.high instead of `== zone.high`; `entry === max(support)` replaced by `entry === suggestedEntry` with the inside rule.
6. Statement audit (`audit_cards.py`): TS1 expects `suggestedEntry` (S1) not max(support); TS1b: nearest zone edge equals entry, OR (inside zone) entry == clamp(last close, low, high); TS2 wording branch for the inside case; new row "Buy is not above the last close when price is inside the zone" (S3: wait for a dip vs already at support).
7. Docs: Known Issues (Changed), persona feedback log entry (Day 127), `INSTRUMENT`-style nothing else.
NOT changed: zone building, the `nearest` flag (Day 127 fix), `support` list values, the Key Levels rows, target, ATR, stop distance (still 2 ATR from the Buy), verdict code.

## Expected visible effect
Inside-zone tickers: Buy = last close (e.g. AMD $503.41 not $530.13), stop 2 ATR below it, R:R recomputed from the real fill (AMD 0.2 -> about 0.5 : 1). Not-inside tickers: nothing changes.

## Tests
`backtest/test_simple_sr.py` / new `test_sr_plan_inside_zone.py`: `trade_plan` with and without `entry_override`; route test (fake provider, frozen clock) for /api/sr: inside zone -> `suggestedEntry` = last completed close clamped into the zone, `meta.entryBasis`, stop = entry - 2 ATR, R:R; price above the zone -> unchanged (zone high); last close above zone high -> clamped to zone high; last close below zone low -> clamped to zone low; legacy engine unchanged; forming bar mid-session uses the completed close not the live price. JS: `riskRewardCalc` uses suggestedEntry, fallback to max(support); PullbackPlan wording (page checker A10 + planted). Audit tests: inside zone with entry = close passes TS1/TS1b; entry = zone high while inside fails.

## Review questions
1. Is clamp(last completed close, zone.low, zone.high) the right entry (vs the live price, the zone midpoint)? Any trading-logic hole (e.g. last close above the zone high while live price is inside)?
2. Every consumer of `suggestedEntry`, `support[0]`, `riskReward`, `suggestedStop`, `meta.zones`, plan entry: backend (validation/engine.py sanity check "entry below current price" — would it now fire?), `compare_sr_engines.py`, paper_trading/backtest (old engine?), frontend (api.js, App.jsx autoFillPositionCalculator "Size this plan", PullbackPlan, KeyLevels, scoring/simplified checks), page checks A10/A12, the audit. Any that assumes Buy == nearest zone high?
3. R:R/stop semantics for the inside case (stop 2 ATR below the close; zone low may be above or below that stop): should the stop reference the zone low instead? (Golden Rule 59: one rule one place.)
4. Wording (facts not verdicts, simple English), test gaps, cache/shape compatibility (old cached /api/sr payloads without `entryBasis`).
