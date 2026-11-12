# API Contracts — Day 125

> Changes since `API_CONTRACTS_DAY124.md`. One **breaking** change: the breakout endpoints'
> `status` values and fields. Backend v2.53 → v2.54. Nothing else changed shape.
> Plan + Fable review: `docs/claude/design/ANALYZE_CLEANUP_PLAN_DAY125.md` §7.1.

---

## Changed (breaking) — `GET /api/breakout/<ticker>`

The breakout check now uses simple, widely agreed trader rules, **not backtested** (user decision).
It runs on **completed** daily bars only: today's bar is dropped until 16:30 ET
(`breakout_detection.prepare_breakout_frame` → `market_time.drop_forming_bar`). This happens before
the 80-bar minimum check. The SPY benchmark fetch was removed (no RS gate any more).

Rules (t = last completed bar):
- **P** (`breakoutLevel`) = highest high of bars t-69 … t-10, the 60-day high that stood before the last 10 days.
- **b** = first bar in t-9 … t that closed above P.
- **rvol** = volume on bar b ÷ the average volume of the 50 bars before b. It is `null` when fewer
  than 40 of those 50 are known, or when the average is 0.

`status`, checked in this priority order:

| Status | When |
|---|---|
| `FAILED_BREAKOUT` | b exists and close < P |
| `EXTENDED_CHASE_RISK` | b exists and close more than 5% above P |
| `RETEST_ENTRY` | b exists, t > b, low within 1% above P, close > P |
| `BREAKOUT_CONFIRMED` | b exists, rvol ≥ 1.5, close within P … P+5% |
| `BREAKOUT_LIGHT_VOLUME` (new) | b exists, rvol < 1.5 or unknown, same band |
| `BREAKOUT_WATCH` | no b, close within 3% under P |
| `NOT_READY` | otherwise |

**Removed statuses:** `SUPPLY_WARNING`, `BUILDING_BASE`.

`200` fields: `status`, `humanAction`, `asOfDate` (last completed bar used), `currentPrice` (that
bar's close), `breakoutLevel` (P), `pctFromLevel` (close vs P, %, 2 dp), `breakoutDate`, `breakoutAge`
(bars since b), `rvol`, `timestamp`, `ticker`, `dataPoints`, `source`, `barDropped`, `apiTimestamp`.

**Removed fields:** `benchmark`, `checks`, `warnings`, `evidence`, `supportLevel`, `invalidation`,
`retestZoneLow`, `retestZoneHigh`, `atrPct`, `extensionFromSma50Pct`.

Errors: no data → `404 {error}`; fewer than 80 completed bars → `400 {error, message}`;
bad/missing OHLCV columns → `400 {error}`; other exceptions → `500 {error}` (logged).

## Changed (breaking) — `POST /api/breakout/batch`

- Per-ticker results are now `{ status, humanAction, breakoutLevel, rvol, asOfDate, source }` or
  `{ error }`. `checks` and `warnings` were removed.
- The top-level `benchmarkAvailable` field was removed, so the response is `{ results, requested, apiTimestamp }`.
- The forming bar is dropped per ticker, same as the single-ticker route.

## Frontend-only (no API change)

- `fetchBreakout()` now returns `{ error }` on any failure instead of `null`, so the Analyze
  Breakout card can say "Breakout check unavailable" instead of disappearing.
- Trade Setup reads `sr.meta.levelScores` (exact 2 dp keys), `sr.meta.mtf.confluence_map`,
  `sr.meta.resistanceProjected` / `supportProjected` and `sr.meta.proximityFilter` for the new
  floor/ceiling rows (`utils/keyLevels.js`). `/api/sr` itself is unchanged.
- `/api/patterns` is still fetched: its `trendTemplate` feeds the verdict and the Technical Read.
  Only the Pattern Detection card was removed.
