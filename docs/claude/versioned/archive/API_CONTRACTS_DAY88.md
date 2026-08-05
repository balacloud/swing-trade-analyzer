# API Contracts — Day 88 (July 16, 2026)

> Supersedes nothing — these are two new endpoints. All endpoints
> documented in `API_CONTRACTS_DAY87.md` (and its predecessors) are
> unchanged.

---

## New — `GET /api/paper-trading/status`

### Purpose
Read-only status of the automated paper-trading ledger (`backend/paper_trading/`, built Day 81). Surfaces what was previously CLI-only (`daily_job.py --report`) for display in the Forward Test tab.

### Response shape

```json
{
  "lastRunDate": "2026-07-16",
  "systems": {
    "momentum": {
      "openPositions": 2,
      "closedTrades": 0,
      "stats": null
    },
    "mr": {
      "openPositions": 4,
      "closedTrades": 2,
      "stats": {
        "win_rate": 50.0,
        "profit_factor": 1.037,
        "expectancy_pct": 0.0931,
        "avg_r_multiple": 0.0186,
        "total_trades": 2,
        "warnings": ["Only 2 trades — insufficient for statistical significance"],
        "...": "full backend/backtest/metrics.compute_metrics() output"
      }
    }
  }
}
```

`stats` is `null` when `closedTrades` is 0 (no metrics to compute). When present, it's the exact output of `backend/backtest/metrics.compute_metrics()` — the same function the backtest itself uses, via `ledger.compute_stats()` (Golden Rule 19: one implementation, not a second one prone to drift).

Returns `503` if the paper trading module isn't importable.

### Verified (Day 88)
Live-tested before and after a real `/api/paper-trading/trigger` call — confirmed the two endpoints read/write the same underlying ledger (open position counts and `lastRunDate` changed as expected).

---

## New — `POST /api/paper-trading/trigger`

### Purpose
Manually force-run the daily paper-trading job — for catching up after a missed scheduled run (e.g. laptop asleep at the scheduled 16:30 CT launchd time). Calls the exact same `run_daily_job(force=True)` function the scheduler already invokes; no new trading logic, no duplicate implementation.

### Behavior
- Always passes `force=True` — a same-day re-run without it would be a no-op (the job's own idempotent check).
- **Synchronous.** Can take 10-30+ seconds: fetches live OHLCV for every open position, runs a fresh TradingView scan for new signals. Not backgrounded — the HTTP request blocks until it completes.
- Safe to call more than once per day — activation/stepping only acts on positions that need it; new-signal generation re-applies the existing cooldown check (`ledger.has_active_or_cooldown()`), so it won't double-queue the same ticker.

### Response shape

```json
{
  "summary": {
    "run_date": "2026-07-16",
    "activated": 3,
    "closed": 0,
    "still_open": 6,
    "queued_momentum": 0,
    "queued_mr": 0
  }
}
```

Returns `503` if the paper trading module isn't importable; `500` with `{"error": ...}` on any failure during the run (e.g. a data-provider outage mid-run — partial progress up to that point is still persisted in the ledger, since each step commits as it goes).

### Verified (Day 88)
Triggered live against the running backend: activated 3 pending signals that had been queued the prior day, confirmed via a follow-up `/api/paper-trading/status` call that open-position counts updated accordingly (momentum 1→2, MR 2→4) and `lastRunDate` advanced to the current day.

---

## Unchanged Endpoints

See `API_CONTRACTS_DAY87.md` for everything else.
