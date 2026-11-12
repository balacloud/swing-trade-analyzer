# API Contracts — Day 118 (consolidated, covers Day 116 + Day 118)

> All changes are additive fields on `GET /api/sr/<ticker>` — no field removed, renamed, or
> reshaped since Day 112. Every endpoint documented in prior `API_CONTRACTS_DAY*.md` files
> (latest: Day 112) is otherwise unchanged. `meta` is passed through wholesale by `api.js`
> (`meta: data.meta || {}`), so every field below reached the frontend automatically — no
> `api.js` change was needed for any of them.

---

## Changed — `GET /api/sr/<ticker>` (Day 116)

### 1. New field `meta.candle.barComplete` (additive)

Boolean. `true` unless the final bar in the 260-bar window is today's still-forming intraday
bar (an ET market-hours test, mirroring `paper_trading/live_signals.py`'s `_prepare_ohlcv()`
guard). `/api/sr` does **not** drop the forming bar the way `live_signals.py` does — it must
keep returning today's live price — it only labels it.

**Why:** `meta.rvol`, `candle.closeLocation`, `change`, etc. are all computed from
`df.iloc[-1]`, which has no partial-bar guard — mid-session this silently understated volume
conviction (measured: RVOL median 0.45 vs. 0.92 true) across the Volume Confirmation card, the
⚠️ DIST badge, and `priceStructureNarrative.js`'s breakout-watch line.

### 2. New field `meta.prevBar` (additive, nullable)

`{date, rvol, changePct, closeLocation, open, high, low, close}` — the last **complete** bar's
figures (`df.iloc[-2]`), computed the same way `candle`/`rvol` are for the current bar. `null`
when `len(df) < 3`.

**Consumer usage:** `App.jsx`'s Volume card and ⚠️ DIST badge, and
`priceStructureNarrative.js`'s breakout-watch item, all read `prevBar` instead of the
partial current bar whenever `barComplete` is `false`, with an explicit "last completed
session" label. `currentPrice`/`volume`/`change` (top-level, the Day 85 Nirmal/Master Framework
fields) are deliberately **unchanged** — still today's live values, not `prevBar`'s.

---

## Changed — `GET /api/sr/<ticker>` (Day 118)

### 3. New fields on `meta.mtf.confluence_map[level]` — `proximity`, `strength_label` (additive)

`confluence_map`'s per-level value dict gains two fields alongside the existing `confluent` /
`weekly_match` / `distance_pct` / `strength`:

| Field | Type | Meaning |
|---|---|---|
| `proximity` | float, 0-1 | How close the weekly match is to the threshold — 1.0 = exact match, 0 = no match or at the threshold edge. |
| `strength_label` | `"Strong"` \| `"Moderate"` \| `"Weak"` | `strength >= 0.75` / `>= 0.45` / else. Display label — `strength` (the float) is unchanged in shape, but its **values** changed (see below). |

**Breaking-in-value, not breaking-in-shape:** `strength` was previously always exactly `1.0`
(confluent) or `0.6` (not confluent) — now a continuous graduated score in `[0, 1]` blending
normalized daily/weekly touch counts with `proximity`. Any consumer that compared `strength`
against those two exact constants (none found — grep confirmed `App.jsx` only ever read
`.confluent`, never `.strength`) would need updating; none existed.

### 4. New field `meta.mtf.projected_excluded` (additive)

Integer — count of daily levels excluded from `confluence_map` because they were synthetic
(ATR/Fibonacci-projected, i.e. `meta.resistanceProjected`/`supportProjected` was true for that
side). Previously these levels were included in `confluence_map` and silently dragged down
`confluence_pct` for every near-ATH/ATL stock. `confluence_map`'s **key set** is now smaller by
this count on any ticker where it's nonzero (rare — 0/47 in this session's live sweep).

---

## Format note — `meta.mtf.confluence_map` keys (Day 112, restated for context)

Still zero-padded 2-decimal string keys (`"227.50"`, not `"227.5"`), per Day 112's fix. Days
116/118 added no new key-format changes.
