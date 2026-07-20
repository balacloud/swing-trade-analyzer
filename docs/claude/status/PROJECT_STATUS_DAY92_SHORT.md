# Project Status — Day 92 (July 20, 2026)

## Version: v4.49 (Backend v2.45, Frontend v4.44, Backtest v4.19, API Service v2.11)

---

## What Happened Today

Continuation of Day 91's bug-fix posture, but the session's real outcome is a scope decision: **forward-testing accumulation is now the user's sole priority**, and the confirmation bar was raised from 50 to 100 trades per system. Everything else below happened in service of that (a first-principles review of the decision engine, and a real bug found while investigating a "Force Run did nothing" report).

### 1. First-principles review of the decision engine (no code changes)
Walked through `determineVerdict()` (`categoricalAssessment.js`), the Minervini Trend Template (`pattern_detection.py`), and `mean_reversion.py` against canonical swing-trading first principles. Confirmed the core verdict logic is solidly designed (real 8-criteria Trend Template, RS as a hard gate, regime as a gate not a vote, equal-weighting discipline, mechanical ATR-based exits, sentiment/blended-RS correctly demoted to informational after backtests showed they hurt performance). Found two real gaps, logged as ROADMAP.md Priority #11 (deferred until the paper-trading gate clears):
- **Volume confirmation is absent from both the Full Analysis verdict and the Simple Checklist's 9 criteria.** The checklist's "Volume" criterion is a liquidity gate (avg $ volume vs. cap-tier threshold), not a price/volume-confirmation signal — confirmed directly against `simplifiedScoring.js` after the user pointed at a screenshot. Neither view checks whether a move is backed by rising volume (accumulation) vs. thin volume.
- **`mean_reversion.py`'s docstring claims MR is "only active when ADX < 20 (range-bound)," but `detect_mr_signal()`'s actual `signal` condition never checks ADX** — it's returned as an informational `range_bound` flag only. Likely a doc-accuracy issue rather than a logic bug (the code's ungated behavior may be closer to Connors' actual published method).

### 2. Force-run investigation found and fixed a real bug (Golden Rule 28)
User force-ran the job and reported "looks like nothing happened." Two separate causes:
- A live TwelveData rate-limit cascade (same class as Golden Rule 25) had tripped yfinance's and Tradier's circuit breakers. Verified both self-heal on the next probe (OPEN → HALF_OPEN → CLOSED) — confirms Day 89's finding still holds.
- **A real, previously-undiscovered bug**: `live_signals.py` stamped every new signal's `signal_date` from `datetime.now()` (wall clock) instead of the OHLCV bar `signal_price` actually came from. A weekend or off-hours Force Run stamps a date that can never match a trading day, so `activate_pending_signals()` fails on that row forever — silently, with only a `print()` nobody sees. **8 of momentum's 11 pending signals were permanently zombied this way.**
- Fixed by deriving `signal_date` from the same OHLCV row `signal_price` comes from. Repaired the 8 already-stuck ledger rows by matching their stored `signal_price` back to the real bar it came from (SLF/CNO → 2026-07-10, USB/ASND/SMFG/L/WTFC/GD → 2026-07-17). Re-ran and confirmed 7/8 activated immediately — **momentum went from 3 open to 10 open in one run.**

### 3. Per-position ticker detail surfaced in the UI
User asked to see ticker/entry/exit detail without querying the DB. The data was already computed server-side (`ledger.get_open_positions()` / `get_closed_trades()` / `get_pending_signals()`) but discarded down to counts. Extended `/api/paper-trading/status` with a `positions` object (open/pending/closed) per system, and added an expandable "▸ Show tickers (N)" table to each `SystemCard` in `AutomatedPaperTradingPanel.jsx`. Verified live in-browser (claude-in-chrome): both tables render correctly, zero console errors, repaired SLF/CNO show correct entry dates.

### 4. Confirmation bar raised 50 → 100 trades/system
Explicit user decision, made with 0 momentum / 5 MR closed trades on the books — not a reaction to any interim result, and strictly more conservative than the original bar. Logged in `PAPER_TRADING_PREREGISTRATION.md`'s Change Log per Golden Rule 18. **Forward-testing accumulation is now the sole stated priority** — all other backlog items stay parked until it clears.

---

## Files Changed

| File | Change |
|---|---|
| `backend/paper_trading/live_signals.py` | `signal_date` now derived from the OHLCV bar `signal_price` came from, not `datetime.now()` (Golden Rule 28) |
| `backend/backend.py` | `/api/paper-trading/status` extended with per-position `positions` detail (open/pending/closed) |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | New expandable per-ticker table per system card |
| `docs/claude/stable/GOLDEN_RULES.md` | New Golden Rule 28 (stamp dates from data, not wall clock) |
| `docs/claude/stable/ROADMAP.md` | Priority #11 added (volume-confirmation gap, deferred); Priority #1 updated (bar raised to 100, sole focus) |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | Confirmation bar raised 50→100, Change Log entry added |
| `README.md` | Roadmap section refreshed to Day 92 state |
| `backend/validation_results/paper_trading_ledger.db` | Data repair only (not tracked in git) — 8 zombied rows' `signal_date` corrected |

No API contract *removals* or field renames — the `positions` field is additive. See `API_CONTRACTS_DAY92.md`.

---

## All Gates Status

Unchanged from Day 88/89/91 — no trading-logic or threshold changes this session (the signal_date fix corrects a bookkeeping bug, not an entry/exit rule; Sections 1-9 of the pre-registration are untouched). Only Section 10's trade-count bar changed (50→100). See `PROJECT_STATUS_DAY88_SHORT.md` for the full gates table.

**Feature freeze status:** superseded in practice — forward-testing accumulation is now the sole active priority (stricter than "bug fixes + monitoring only," since even bug-fix-adjacent backlog work like Priority #11 stays explicitly parked).

---

## Paper Trading Status (end of session)

- **Momentum:** 10 open, 0 closed, 5 pending. Up from 3 open at session start — the zombie-signal fix directly caused this jump.
- **MR:** 8 open, 5 closed (80% WR, PF 2.58, expectancy +1.593%/trade), 12 pending. The system's own sanity-check flags this as too small a sample to trust ("Win rate 80.0% > 70% — likely overfitting").
- **Confirmation bar:** 100 trades/system (raised from 50 today). Both systems are far from either the old or new bar.

---

## Next Session Priorities

1. **Let paper trading accumulate — SOLE FOCUS.** Do not propose or start other roadmap/backlog work unless the user raises it first. Check via the Forward Test tab's status panel (now with per-ticker detail) or `daily_job.py --report`.
2. If a force-run or scheduled run looks like it "did nothing" again, check `job_runs` and re-run in the foreground before assuming it's fine — today's zombie-signal bug looked identical to "no signals qualified today" from the aggregate UI alone.
3. Everything else (fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, the volume-confirmation gap, `/ibkr-scan`, Session 28 audit's remaining findings) stays parked until the 100-trade bar clears on both systems.
