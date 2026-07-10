# Project Status — Day 80 (July 8, 2026)

## Version: v4.38 (Backend v2.37, Frontend v4.37, Backtest v4.18, API Service v2.11)
*Execution session — Fable Remediation Plan Phases 4 + 5 complete (plan finished), plus a user-directed one-time MR liquidity re-test.*

---

## What Happened Today

### 1. Fable Remediation Plan — Phase 4 (Survivorship-Free Re-Validation)

Built `backend/backtest/backtest_survivorship_free.py`: random, seeded (42) 400-ticker sample from SimFin's full 3,788-ticker US coverage — no hand-picking, replacing the original hand-picked 60. Added a per-date liquidity gate (price > $5, 20d avg $ volume > $5M) to `backtest_holistic.py`'s `check_entry_signals()` — verified zero effect on the original megacap universe. Ran Config C (momentum) and MR on the same universe.

**Results (canonical, unbiased):**
- **Config C (momentum): PF 1.61 → 1.40**, 114 trades. Edge survives directionally but not statistically significant (block bootstrap p=0.094).
- **MR: PF 1.23 net → 0.99**, 6,151 trades. Clean, well-powered null result — net losing.

A 30-ticker smoke test caught a real bug first: MR trades use different field names than `compute_metrics()` expects, silently producing "0% WR, PF inf" — fixed with a translation layer before the full run.

Full analysis: `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY79.md`. ROADMAP updated with these as canonical numbers (old hindsight-universe figures kept, labeled as such).

### 2. Fable Remediation Plan — Phase 5 (Paper-Trading Instrumentation) — Plan Complete

`forwardTesting.js`'s `createTrade()` now logs:
- `signalClosePrice` / `entrySlippagePct` — execution-gap measurement, only populated when the loaded analysis matches the ticker being logged (never fabricated for manual entries)
- `regimeSnapshot` — reuses `categoricalResult.riskMacro` unchanged (VIX, SPY vs 200-SMA, 50-SMA declining, regime label), not reimplemented

New "Avg Entry Slippage" stat tile in the Forward Test Van Tharp block; both fields in CSV export. Caught and fixed a real bug during verification: the slippage aggregate lived inside the "zero closed trades" early-return, so it wrongly showed null even with valid open-trade data.

**This closes out all 5 phases of the Fable Remediation Plan.**

### 3. MR Liquidity Re-Test (user-directed, one-time)

User's call: kill MR, or restrict to liquid names and re-test once. The original MR backtest entry (`mr_simulator.py`) had **no dollar-volume liquidity gate at all** — only `price > $5` — unlike momentum's existing $5M ADV gate. Added a one-time, pre-committed gate (price > $10, 20d avg dollar volume > $25M — decided before seeing the result, a defensible execution constraint, not a re-tune) and re-ran on the **same seed=42 universe** via a new `--mr-only` flag.

**Result: PF 0.99 → 1.16, Sharpe −0.10 → 1.30, 3,210 trades.** A real, non-trivial improvement — but the robust block-bootstrap p-value (0.064) still narrowly misses 0.05 significance, and the fixed-risk drawdown is high (78%). **Verdict: not a clean kill, not a clean confirm — MR now sits in the same "real but modest, unconfirmed" tier as momentum.** Both systems require 50+ live paper trades before any capital allocation. No further MR backtest iteration — this was the one allowed re-test.

**Known gap:** only the *backtest* (`mr_simulator.py`) got the new liquidity gate. The live production detector (`backend/mean_reversion.py`, behind `/api/mr/signal` and `/api/mr/scan`) still only has `price > $5` — not yet updated. If MR proceeds toward live paper trading, that detector needs the same gate for consistency. Not done this session — flagged, not resolved.

Addendum added to `SURVIVORSHIP_FREE_BACKTEST_DAY79.md`; ROADMAP and memory updated to reflect the corrected verdict.

---

## Files Changed Today

| File | Type | Content |
|------|------|---------|
| `backend/backtest/backtest_survivorship_free.py` | Created | Survivorship-free universe builder + runner; `--mr-only` flag added later same session |
| `backend/backtest/backtest_holistic.py` | Modified | Per-date liquidity gate in `check_entry_signals()`; cooldown fix (from earlier Phase 2 carryover verification) |
| `backend/backtest/mr_simulator.py` | Modified | Liquidity gate added to `backtest_mr_strategy()` entry condition (price>$10, 20d ADV>$25M) |
| `frontend/src/utils/forwardTesting.js` | Modified | `signalClosePrice`/`entrySlippagePct`, `regimeSnapshot`, CSV export columns; early-return bug fixed |
| `frontend/src/App.jsx` | Modified | `createTrade()` call site wired with slippage/regime data; new stat tile in Van Tharp block |
| `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` | Modified | All Phase 4/5 tasks marked DONE with results; plan-level status now "ALL 5 PHASES DONE" |
| `docs/claude/versioned/SURVIVORSHIP_FREE_BACKTEST_DAY79.md` | Modified | MR liquidity re-test addendum added; original MR recommendation marked superseded |
| `docs/claude/stable/ROADMAP.md` | Modified | Phase 4 canonical numbers, MR liquidity re-test verdict, priority order updated |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) — hindsight-universe, historical |
| — | Survivorship-free re-validation (Config C) | ✅ DONE — PF 1.40, not yet significant (p=0.094) |
| — | Survivorship-free re-validation (MR, unrestricted) | ✅ DONE — PF 0.99, clean null |
| — | MR liquidity re-test (one-time) | ✅ DONE — PF 1.16, not yet significant (p=0.064) |
| — | Fable Remediation Plan | ✅ **ALL 5 PHASES COMPLETE** |

**Paper trading remains unblocked** — config frozen and instrumented. Both momentum and MR now require live confirmation (50+ trades) before capital allocation; neither is backtest-confirmed.

---

## Next Session Priorities

1. **Start paper trading** — config frozen, instrumented, both systems ready to accumulate live trades against the pre-registered criteria.
2. **Decide fundamentals mitigation** — Task 3.2's 40% live↔backtest disagreement, still pending (align live-to-SimFin or backtest-to-TTM).
3. **Confirm SimFin key rotation** — a possible new key was shared in conversation Day 79 but never confirmed/applied.
4. **Add liquidity gate to live MR detector** (`mean_reversion.py`) — only the backtest has it; needed before MR signals go live.
5. **Breakout Plan Phase 0** (Config D/E backtest) and **Phases 2–3** (scan badges, `/breakout-watch` skill) — all unblocked, none started.
6. N4 Market Phase synthesis, `/ibkr-scan` skill, Value Tab Phase 2, Price Structure Phase 2, N3 gap-fill, Canadian Analyze page — queued.
