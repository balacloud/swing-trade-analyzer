# API Contracts — Day 111 (August 28, 2026)

> Adds one field to one existing endpoint's response. Every endpoint documented in
> prior `API_CONTRACTS_DAY*.md` files (latest: Day 108) is otherwise unchanged.
> `/api/mr/scan` also changed internally this session (its data-fetch path was
> fixed to use the shared orchestrator instead of a direct yfinance call) — no
> request/response shape change, not documented here as a contract change.

---

## Changed — `GET /api/sr/<ticker>`

### What changed

New field `meta.candle`, additive, non-breaking.

### Why

Built to support the new Volume Confirmation + Direction read on the Analyze
page's Trade Setup card (Day 111-112). The direction read needs to know where
the day's close landed within its own high-low range — that data wasn't
previously returned by this endpoint, only used internally elsewhere (the
Breakout engine's `candle_quality_ok` check, which isn't reachable from this
route without a second SPY-benchmark fetch). Computed from the same OHLCV
frame already fetched for this route's existing `rvol` field — no new
provider call.

### Response shape (unchanged except `meta.candle`)

```json
{
  "support": [...],
  "resistance": [...],
  "meta": {
    "obv": { "obv": 123456, "obv_prev": 98765, "obv_change_pct": 12.3, "trend": "rising", "divergence": "none", "signal": "..." },
    "rvol": 1.8,
    "rvol_display": "1.8x avg",
    "candle": {
      "closeLocation": 0.87,
      "open": 224.50,
      "high": 226.90,
      "low": 221.36
    }
  }
}
```

`candle.closeLocation` is `(close - low) / (high - low)`, rounded to 2
decimals — `1.0` means the close sat at the day's high, `0.0` means it sat
at the low. It is `null` when `high == low` (a halted or limit-locked bar).
`open`/`high`/`low` are included alongside it so a consumer can show its
work rather than trust the ratio blind.

### Consumers

- `frontend/src/App.jsx` — the new Volume Confirmation + Direction note on
  the Trade Setup card reads `srData.meta.candle.closeLocation` alongside
  `srData.change` and `srData.meta.obv.trend`.
- No other consumer exists yet. `meta` is passed through wholesale by
  `frontend/src/services/api.js`'s `fetchSupportResistance()` (`meta: data.meta || {}`),
  so this addition required no `api.js` change.

### Not changed

`support_resistance.py`'s `compute_sr_levels()` itself, its fallback chain,
or any of its existing output fields. This is additive only — the S&R
selection logic (including the confirmed extreme-vs-nearest bug, Golden
Rule 53) is untouched.
