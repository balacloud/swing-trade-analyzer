# API Contracts — Day 96 (July 24, 2026)

> Supersedes the `GET /api/paper-trading/status` shape documented in
> `API_CONTRACTS_DAY92.md` — additive only, no fields removed or renamed.
> Every other endpoint documented in prior `API_CONTRACTS_DAY*.md` files
> is unchanged.

---

## Changed — `GET /api/paper-trading/status`

### What changed
`systems` gains a new `momentumPathB` key, same shape as `systems.momentum`/`systems.mr`. Backend: `systems.momentum` and `systems.mr` are now explicitly filtered to `variant='A_frozen'` (previously unfiltered, but there was only one variant so it made no observable difference) — this is what keeps Path B from silently blending into the existing numbers now that a second variant exists in the ledger.

### Why
Day 95 added a parallel forward-test experiment ("Path B") that gates momentum entries on the real support/resistance-based R:R check the historical backtest actually validated, instead of Path A's flat-target/ATR-clamp proxy — tracked under a separate `variant='B_revised_rr'` tag in the same `paper_positions` table. Without an explicit filter, `ledger.get_open_positions()`/`get_closed_trades()`/`compute_stats()` would return a mix of both variants once Path B starts closing trades, silently corrupting the Forward Test tab's momentum numbers.

### Response shape

```json
{
  "lastRunDate": "2026-07-24",
  "systems": {
    "momentum": {
      "openPositions": 22,
      "closedTrades": 2,
      "stats": { "win_rate": 50.0, "profit_factor": 1.691, "expectancy_pct": 1.6345, "...": "..." },
      "positions": { "open": ["..."], "pending": ["..."], "closed": ["..."] }
    },
    "momentumPathB": {
      "openPositions": 0,
      "closedTrades": 0,
      "stats": null,
      "positions": { "open": [], "pending": [], "closed": [] }
    },
    "mr": {
      "openPositions": 3,
      "closedTrades": 25,
      "stats": { "win_rate": 92.0, "profit_factor": 10.8217, "...": "..." },
      "positions": { "open": ["..."], "pending": ["..."], "closed": ["..."] }
    }
  }
}
```

`momentumPathB`'s `positions.*` rows use the same shape as `momentum`'s (see `API_CONTRACTS_DAY92.md` for the full per-position field list) — `_position_row()` is variant-agnostic, reused as-is.

### Frontend
`frontend/src/services/api.js`'s `fetchPaperTradingStatus()` already passes the raw JSON through unmodified (`return response.json()`, no field whitelisting) — no frontend change needed there. `AutomatedPaperTradingPanel.jsx` reads `status.systems.momentumPathB` directly and renders a visually-distinct "Momentum (Path B)" card (dashed amber border, "EXPERIMENTAL" badge) only if the key is present — degrades gracefully if a caller's backend predates this change.

### Backend internals (not part of the public contract, noted for future consumers)
`paper_trading/ledger.py`'s `get_open_positions()`, `get_pending_signals()`, `get_closed_trades()`, `compute_stats()`, and `has_active_or_cooldown()` all gained an optional `variant` keyword parameter (default: unfiltered for the getters, `'A_frozen'` for `has_active_or_cooldown`/`queue_pending_signal`). `paper_positions` gained a `variant TEXT NOT NULL DEFAULT 'A_frozen'` column — migrated cleanly via `PRAGMA table_info` check + conditional `ALTER TABLE`, all pre-existing rows auto-backfilled to `'A_frozen'`.
