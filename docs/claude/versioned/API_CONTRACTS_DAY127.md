# API Contracts — Day 127

> Changes since `API_CONTRACTS_DAY126.md`. Backend v2.55 → v2.56. Plans: `docs/claude/design/INSIDE_ZONE_BUY_PLAN_DAY127.md`,
> `SR_INSIDE_ZONE_PICK_PLAN_DAY127.md`.

## Changed — `GET /api/sr/<ticker>`
- **`meta.entryBasis`** (new, string): why the Buy is what it is. `'last_close_inside_zone'` (the last COMPLETED close is inside the nearest support
  zone, so `suggestedEntry` IS that close, 2 dp), `'zone_high'` (simple engine, otherwise the nearest support zone's high), `'nearest_support'` (legacy engine).
- **`suggestedEntry`** / `suggestedStop` / `riskReward` follow the new basis. Stop stays 2 ATR below the Buy. Decided in one place: `sr_plan.plan_entry`.
- **Nearest support** now treats a zone the live price is inside as distance 0 (`simple_sr.pick`, `meta.zones` sort). `insideZone` / `nearest` flags unchanged in shape.
- Frontend reads `suggestedEntry` (the old `max(support)` is only a fallback).

## Changed — `GET /api/stock/<ticker>`
- Answers **503** (not 404) when every price source failed; **404** only when the providers say the ticker is unknown. `price52wAgo` / `price13wAgo` come from non-NaN closes.

## Changed — validation engine
- "Entry below price" sanity check is `entry <= last completed close` (was `<` current price), so the Buy equal to the close passes.

Nothing else changed shape.
