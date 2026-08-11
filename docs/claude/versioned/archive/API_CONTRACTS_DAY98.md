# API Contracts — Day 98 (July 24, 2026)

> Supersedes the `GET /api/paper-trading/status` shape documented in
> `API_CONTRACTS_DAY96.md` — additive only, no fields removed or renamed.
> Every other endpoint documented in prior `API_CONTRACTS_DAY*.md` files
> is unchanged.

---

## Changed — `GET /api/paper-trading/status`

### What changed
`systems` gains a new `mrHub` key, same shape as `systems.mr`/`systems.momentumPathB`. Backend: pinned to `variant='mr_hub65'`, exactly mirroring how `momentumPathB` is pinned to `variant='B_revised_rr'` — the existing `systems.mr` block remains pinned to `variant='A_frozen'` (unchanged from Day 96), so `mr_hub65` trades never blend into the broad MR numbers.

### Why
Day 98 added a parallel forward-test experiment ("HUB-65") that runs the exact same, unchanged Mean-Reversion engine (Connors RSI(2)) against a curated 65-ticker watchlist instead of the broad ~150-ticker dynamic TradingView scan — tracked under a separate `variant='mr_hub65'` tag in the same `paper_positions` table. Unlike Path B (which varies the *entry gate* on the same universe), HUB-65 varies the *universe* on the same, unchanged gate — the `variant` column now carries two different meanings depending on `system` (see `ledger.py`'s schema comment and new Golden Rule 38).

### Response shape

```json
{
  "lastRunDate": "2026-07-24",
  "systems": {
    "momentum": { "...": "unchanged, see API_CONTRACTS_DAY96.md" },
    "momentumPathB": { "...": "unchanged, see API_CONTRACTS_DAY96.md" },
    "mr": { "...": "unchanged, still pinned to variant='A_frozen'" },
    "mrHub": {
      "openPositions": 0,
      "closedTrades": 0,
      "stats": null,
      "positions": {
        "open": [],
        "pending": [
          {
            "ticker": "AFRM",
            "signalPrice": 70.70,
            "signalDate": "2026-07-23",
            "entryDate": null,
            "exitDate": null,
            "result": null,
            "pnlPct": null
          }
        ],
        "closed": []
      }
    }
  }
}
```

`mrHub`'s `positions.*` rows use the same shape as every other system's (`_position_row()` is variant-agnostic, reused as-is — no new per-position fields).

### Frontend
`frontend/src/services/api.js`'s `fetchPaperTradingStatus()` already passes the raw JSON through unmodified — no frontend change needed there (same as Day 96's `momentumPathB` addition; this is the exact failure mode Golden Rule 30 warns about, and there's still no whitelist to update). `AutomatedPaperTradingPanel.jsx` reads `status.systems.mrHub` directly and renders a "Mean-Reversion (HUB-65)" card only if the key is present — degrades gracefully if a caller's backend predates this change. Uses a **teal** "Curated-65 Universe" badge, deliberately distinct from Path B's amber "Experimental" badge (`BADGE_STYLES` object, `badgeColor` prop) — the color difference is a conflation safeguard: amber alone would read as "another experimental gate variant," when HUB-MR is actually a different universe running the identical, unchanged strategy.

### Backend internals (not part of the public contract, noted for future consumers)
`paper_trading/live_signals.py`'s `get_mr_signals()` gained a `variant='A_frozen'` keyword parameter (backward-compatible — the module's own `__main__` test block and all pre-existing callers keep working unchanged), passed through into `ledger.has_active_or_cooldown()` and stamped onto each returned signal dict. `daily_job.py`'s Step 3 gained a second `get_mr_signals()` call against `mean_reversion.HUB_UNIVERSE` (64 tickers, shuffled per-run via `random.Random(today).shuffle(...)` — Golden Rule 25, so a rate-limit cutoff mid-loop doesn't silently starve the same tail tickers every day since HUB-65 runs last in the job after momentum's and the broad MR scan's rate budget is spent).

---

## New — `backend/backtest/backtest_hub_mr.py` (script, not an HTTP endpoint)

One-shot (re-runnable) CLI script, not wired into any Flask route. `--smoke-test` (5 tickers) or full run (64 tickers, `HUB_UNIVERSE`). Imports `run_mr_on_universe()`/`_translate_mr_trades_for_metrics()` from `backtest_survivorship_free.py` and `compute_metrics()` from `metrics.py` — no logic duplicated. Writes JSON to `backend/backtest_results_holistic/hub_mr_<timestamp>.json`, including a `meta.caveat` field with the full selection-bias warning text (not comparable to the survivorship-free baseline). Full run result (Day 98): 1,940 trades, WR 57.78%, PF 1.2574, Sharpe 1.5278, block-bootstrap p=0.0311 (76 distinct entry-months), DRAM skipped as genuinely delisted.
