# Project Status — Day 99 (July 27, 2026)

## Version: v4.53 → v4.54 (Backend v2.46 → v2.47, Frontend v4.48 → v4.49, Backtest v4.20 unchanged, API Service v2.11 unchanged)

---

## What Happened Today

User asked what an Opus 5 review would be best spent on. Answer: the paper-trading ledger/exit-replay integrity path — the highest-stakes code in the project (silently accumulating real trade counts toward the 100-trade bars), and every prior review pass on it had come from the same session's Claude, never a fresh, unprimed pass. The review found a real, HIGH-severity bug: **the data provider returns a partially-formed bar for the current session while the market is open, and neither `simulate_trade()` nor `simulate_mr_trade()` checked whether the final bar was complete before reading it.** A mid-session manual run (`--force` or the "Force Run Now" UI button — the scheduled 17:30 ET job was always safe) could write an intraday, not-yet-final price into the ledger as that day's closing price and permanently close a position (`close_position()` is one-way).

### 1. Diagnosis
Full diagnosis + evidence written to `docs/claude/design/PARTIAL_BAR_LEDGER_CONTAMINATION_FIX_PLAN.md` before any code changed. Exhaustive re-replay of all closed trades against complete history (not a spot-check) found the natural experiment cleanly: trades written *after* the exit bar was already final reproduced exactly (0.00pp delta); every trade written *mid-session* differed. 19 of the then-25 closed MR trades were affected — 4 wrong at the decision level (one, MS, should still have been an open position — a phantom closed trade) and 15 with wrong P&L (up to +3.83pp).

### 2. Fix — 4 phases, plan-approved before implementation
- **Phase 1** (`live_signals.py`): renamed `_to_capitalized_ohlcv` → `_prepare_ohlcv`, added a guard that drops the final bar whenever it's today's date and the market (`America/New_York`, explicit `zoneinfo`) hasn't closed yet. Applied at all 5 OHLCV call sites in the paper-trading engine (confirmed via repo-wide grep — used nowhere else). Verified: guard correctly drops today's bar mid-session; the 6 known-clean trades still reproduced at exactly 0.00pp after the change (no regression).
- **Phase 2** (`repair_partial_bar_exits.py`, new): backs up the DB, re-replays every closed row (both systems) against now-complete history using the ledger's own stored entry values, dry-run by default, `--apply` to write, JSON audit trail. Dry-run shown to the user before applying. **Applied: 20 corrections** (the closed set had grown from 25→29 between diagnosis and repair — see the live-fire note below). GEV's result flipped win→loss; MS and a brand-new contaminated trade (NVO) were both correctly reopened to `status='open'`. Post-repair: **all 27 remaining closed trades re-replay exactly (0.00pp)** — the ledger is now internally consistent, verified exhaustively, not sampled.
- **Phase 3** (`AutomatedPaperTradingPanel.jsx`): Force Run caption corrected from a stale "16:30 CT" (wrong since the Day 95 timezone fix) to "17:30 ET", plus a new line warning that mid-session runs use the last completed session's bar. Live-verified in-browser: renders correctly, matches the repaired numbers exactly, zero console errors.
- **Phase 4** (`daily_job.py`, `ledger.py`, `metrics.py`): momentum's live close path now nets transaction costs like MR already did (was storing gross into both `pnl_pct`/`pnl_pct_gross` — small magnitude, ~0.03–0.12%/trade, doesn't retroactively touch the 2 already-clean momentum closes). Two dead `.get(key, default)` fallbacks (the key always existed as a DB column, so `None` never fell through to the default) replaced with explicit `is None` checks in both files.

### 3. A live-fire confirmation, unplanned
While Phase 1 was mid-implementation, `backend.log` shows a real `POST /api/paper-trading/trigger` at 14:44:53 local — someone clicked Force Run Now in the browser during market hours, before Flask's debug reloader had picked up the fix (confirmed via file mtime vs. log timestamp). It closed NVO on today's partial bar in real time — an unplanned, independent reproduction of the exact bug, and the repair script (run afterward) caught and corrected it automatically.

### 4. Not built this session
User asked to brainstorm ways to speed up forward-testing pace without loosening any gate/threshold. Landed on a genuinely legitimate idea — momentum's `PAPER_TRADING_PREREGISTRATION.md` §7 already fully specifies a "Quick" holding period (5-day hold, already-frozen exit rule) that the live engine has never exercised (hardcoded to `standard`/15-day since Day 81). Planned in Plan Mode as a third parallel momentum track (own 100-trade bar, `variant='A_frozen'` unchanged + `holding_period='quick'` as a genuinely independent axis, matching the Path B/HUB-65 "new experiment, zero effect on existing count" pattern). **User stopped before plan approval — nothing was implemented.** The plan is not persisted anywhere except this session's transcript; if picked up later, it needs to be re-planned from scratch.

### Verification discipline (Golden Rule 32 — 3 passes on every phase)
- Pass 1 (works as intended): guard behavior confirmed live during market hours; repair script dry-run reviewed before apply.
- Pass 2 (what else calls the changed thing): repo-wide grep confirmed `_to_capitalized_ohlcv`'s old name has zero remaining callers; confirmed no other module imports it.
- Pass 3 (other state): `signal_date` stamping (Golden Rule 28) and next-day-open activation logic re-verified unaffected; MR's per-variant cooldown isolation re-verified intact; `mr`/`mrHub` blocks confirmed untouched by the momentum-only Phase 4 change.

---

## Files Changed

| File | Change |
|---|---|
| `backend/paper_trading/live_signals.py` | `_to_capitalized_ohlcv` → `_prepare_ohlcv`, added market-hours incomplete-bar guard |
| `backend/paper_trading/daily_job.py` | Import updated for rename; momentum close path now nets transaction costs |
| `backend/paper_trading/ledger.py` | Dead fallback fix in `compute_stats()` |
| `backend/paper_trading/repair_partial_bar_exits.py` | **New** — one-time repair script (backup, dry-run, `--apply`, audit trail) |
| `backend/backtest/metrics.py` | Dead fallback fix in `compute_metrics()` |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | Force Run caption: fixed stale schedule text, added mid-session warning |
| `docs/claude/design/PARTIAL_BAR_LEDGER_CONTAMINATION_FIX_PLAN.md` | **New** — full diagnosis + fix plan, written before implementation |
| `backend/validation_results/partial_bar_repair_20260727_145432.json` | **New** — repair audit trail (20 rows, before/after) |

No API contract changes — `/api/paper-trading/status`'s response shape is identical; only the underlying ledger data changed.

---

## All Gates Status

Unchanged — this session fixed a data-integrity bug in the replay/reporting layer, it didn't touch any entry/exit gate, threshold, or frozen config. No re-tuning occurred (Golden Rule 18/39 territory was explicitly avoided — see the new Golden Rule 39 rationale in `GOLDEN_RULES.md`).

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority across all four tracks.

---

## Paper Trading Status (end of session, post-repair)

**Momentum Path A:** 28 open / 2 closed (50% WR, PF 1.691 — still a 2-trade sample, no change in interpretation).
**Momentum Path B:** 6 open / 0 closed.
**MR (broad):** 3 open / **25 closed (84.0% WR, PF 8.0604)** — down from the pre-repair 27 closed/~92%WR/~PF 10.8; the drop is the repair working as intended (GEV flipped to a loss, MS and NVO both correctly left the closed set). Still flagged by the system's own sanity check as likely overfitting on a small, clustered sample (Day 93 finding still stands).
**MR HUB-65:** 2 open / 0 closed.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS**, now on a *corrected* ledger for the first time since the bug was introduced.
2. If the "Quick" momentum holding-period idea is raised again, it needs to be re-planned from scratch (nothing was persisted from today's stopped plan) — see this doc's §4 above for the design reasoning that was already worked out (reuse `variant='A_frozen'` + the already-existing `holding_period` column as an independent third axis; §7's Quick exit rule is already frozen and unused).
3. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit's remaining lower-priority findings.
