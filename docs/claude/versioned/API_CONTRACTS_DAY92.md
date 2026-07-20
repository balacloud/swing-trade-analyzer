# API Contracts — Day 92 (July 20, 2026)

> Supersedes the `GET /api/paper-trading/status` shape documented in
> `API_CONTRACTS_DAY88.md` — additive only, no fields removed or renamed.
> Every other endpoint documented in `API_CONTRACTS_DAY88.md` (and its
> predecessors) is unchanged.

---

## Changed — `GET /api/paper-trading/status`

### What changed
Each system's object gains a `positions` field with per-position ticker/entry/exit detail (open, pending, closed) — previously the route computed these lists internally just to discard them down to a `len()` count. Built so the Forward Test tab's panel can show "what tickers, what price entered and exit" without a direct DB query.

### Response shape

```json
{
  "lastRunDate": "2026-07-20",
  "systems": {
    "momentum": {
      "openPositions": 10,
      "closedTrades": 0,
      "stats": null,
      "positions": {
        "open": [
          {
            "ticker": "SLF",
            "status": "open",
            "holdingPeriod": "standard",
            "signalDate": "2026-07-10",
            "signalPrice": 79.91,
            "entryDate": "2026-07-13",
            "entryPrice": 79.24,
            "currentStopPrice": 74.95,
            "daysHeld": 4,
            "exitDate": null,
            "exitPrice": null,
            "exitReason": null,
            "result": null,
            "pnlPct": null,
            "pnlR": null
          }
        ],
        "pending": ["... same shape, entryDate/entryPrice null ..."],
        "closed": ["... same shape, capped to the 20 most recent, newest first ..."]
      }
    },
    "mr": { "...": "same shape" }
  }
}
```

Field notes:
- `positions.open` / `positions.pending` / `positions.closed` are all the same row shape (`_position_row()` in `backend.py`) regardless of lifecycle stage — fields that don't apply yet are `null` (e.g. `entryDate` on a `pending` row, `exitDate` on an `open` row).
- `closed` is capped to the 20 most recent trades, newest first — this is a status view, not the full trade journal.
- `regime_snapshot`'s raw JSON blob and other internal-only ledger columns are deliberately excluded from `_position_row()` — only display-relevant fields are serialized.

### Verified (Day 92)
Confirmed live via direct `curl` against the running backend (new fields present, correct values for the just-repaired SLF/CNO rows) and in-browser via claude-in-chrome: both system cards' "▸ Show tickers (N)" tables render ticker/status/entry/exit/result correctly, zero console errors, momentum and MR tables both checked after expanding.

---

## Unchanged Endpoints

See `API_CONTRACTS_DAY88.md` for everything else, including `POST /api/paper-trading/trigger` (behavior unchanged this session).
