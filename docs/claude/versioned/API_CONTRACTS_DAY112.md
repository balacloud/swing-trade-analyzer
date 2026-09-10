# API Contracts — Day 112 (September 10, 2026)

> One new field on one existing endpoint, plus a format change to two existing
> map fields on the same endpoint. Additive / low-impact — every consumer that
> matters was updated in the same session. Every endpoint documented in prior
> `API_CONTRACTS_DAY*.md` files (latest: Day 111) is otherwise unchanged.

---

## Changed — `GET /api/sr/<ticker>`

### 1. New field `meta.pivotSelection` (additive, non-breaking)

Records which pivot-selection strategy produced the levels:

| Value | Meaning |
|---|---|
| `"nearest"` | The Day 112 Golden-Rule-53 fix — N pivots nearest to current price per side. Default. |
| `"extreme"` | The pre-Day-112 rollback path (`SRConfig.pivot_nearest_selection=False`) — N most extreme pivots. Only appears if the flag is flipped. |
| `null` | The levels came from a non-pivot method (`agglomerative` / `kmeans` / `volume_profile`). |

**Why:** so the API response and logs record which selection logic was in
effect — essential for reading the backtest A/B and for any future audit of the
`_pivot_sr` behaviour.

### 2. Format change — `meta.levelScores` and `meta.mtf.confluence_map` keys

Both maps are keyed by price. The keys changed from `str(round(price, 2))` (which
drops trailing zeros — `"227.5"`, `"600.0"`) to a **zero-padded 2-decimal
string** (`"227.50"`, `"600.00"`).

**Why:** `App.jsx` looks these maps up with `level.toFixed(2)` (always 2dp), so
the old format silently failed to match for any level whose hundredths digit was
`0` — the ★ confluence badge and per-level touch counts were invisible for
~10% of levels (BUG-A). All three internal maps (`_pivot_sr`'s new
`level_scores`, `_agglomerative_sr`'s existing one, `_enrich_with_mtf`'s
`confluence_map`) now use the one padded format.

**Consumer impact:** `App.jsx` (`.toFixed(2)` lookup) — now matches, fixed.
`priceStructureNarrative.js` — was already immune (uses a `parseFloat` tolerance
scan). Any external consumer that string-matched the old unpadded keys would
need to switch to 2dp — none known.

### Response shape (unchanged except the two items above)

```json
{
  "support": [...],
  "resistance": [...],
  "meta": {
    "methodUsed": "pivot",
    "pivotSelection": "nearest",      // NEW — Day 112
    "levelScores": { "612.43": 31, "600.00": 12, ... },   // keys now zero-padded 2dp
    "mtf": {
      "confluence_map": { "598.93": { "confluent": true, ... }, ... }   // keys now zero-padded 2dp
    }
  }
}
```

---

## Not a contract change (noted for completeness)

- `frontend/src/utils/categoricalAssessment.js`'s `buildActionablePattern()`
  output gained a `targetBasis` string and `targetPrice`/`riskReward` may now be
  `null` — this is a *frontend-internal* computed object, not an API response.
- `backend/backtest/backtest_survivorship_free.py` gained a `--momentum-only`
  CLI flag — tooling, not an API.
