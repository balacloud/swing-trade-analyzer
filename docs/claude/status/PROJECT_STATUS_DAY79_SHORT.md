# Project Status — Day 79 (July 6, 2026)

## Version: v4.37 (Backend v2.36, Frontend v4.36, Backtest v4.18, API Service v2.11)
*Execution session — Day 78's audit/planning became today's code. Fable Remediation Plan Phases 0–3 complete + breakout engine wired and validated.*

---

## What Happened Today

### 1. Fable Remediation Plan — Phase 0 (Freeze & Pre-Register)

- **RS threshold contradiction resolved**: simple checklist reverted 1.2→1.0 (`simplifiedScoring.js`). The "1.2" claim had no reproducible backtest script anywhere in the repo — the only candidate script tests 1.0 with unrelated parameters and predates the current checklist. Aligned to Config C's actual validated threshold (238 trades, walk-forward).
- **`docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` created** — freezes every threshold (technical, fundamental, risk gate, verdict priority order, stops/targets, VIX sizing, MR rules) plus pre-committed success/failure criteria for the eventual paper-trading judgment.

### 2. Fable Remediation Plan — Phase 1 (Repo Hygiene)

- SimFin API key moved from hardcoded source to `backend/.env` (`SIMFIN_API_KEY`), loader fails fast if missing. **Key rotation at simfin.com still needs user confirmation.**
- `backend/venv/` untracked from git (9,315 files) — confirmed still functional on disk.
- Backend version drift fixed: `BACKEND_VERSION` constant added, `/api/health` no longer hardcodes a stale '2.23'.
- Deleted 3 confirmed-dead files: `DecisionMatrix.jsx`, `scoringEngine_day4.js`, `scoringEngine_v2.1.js`. Frontend build verified clean.

### 3. Fable Remediation Plan — Phase 2 (Backtest Integrity)

- **Transaction costs added to MR backtest** (`mr_simulator.py`, `gate5_combined.py` momentum leg — both had zero costs before). Full 60-ticker/5-year re-run: MR PF 1.26→1.23 net, Momentum PF 1.36→1.35 net. Gate 5 verdict unchanged (PASS). Edge survives costs.
- **Gap-aware stop/target fills** added to `trade_simulator.py` and `mr_simulator.py` — a gap through the stop/target now fills at the open price, not the theoretical level. Fixed a downstream cooldown-classification bug this exposed in `backtest_holistic.py`.
- **Statistics overhaul in `metrics.py`**: scipy `ttest_1samp` (was a hand-rolled approximation), actual trades/year computed from data (was hardcoded 25 — caught a real over-annualization bug: Sharpe dropped from an inflated 1.37 to an honest 0.06 on a thin sample), block-bootstrap p-value robust to regime/ticker clustering, and a second drawdown metric (2%-fixed-risk) alongside the old sequential-100%-equity one. Both surfaced in print output and HTML report.
- **JS↔Python verdict parity grid built** (`test_verdict_parity.py` + `verdict_grid.mjs`, 86,400 combinations). Found one real bug: `categorical_engine.py`'s HOLD-fallback only checked `risk_macro == 'Favorable'`, missing the `'Neutral'` branch JS has (7.08% mismatch rate, single root cause). **User approved the fix; applied and reverified: 0/86,400 mismatches — full parity achieved.**

### 4. Fable Remediation Plan — Phase 3 (Backtest↔Live Coherence)

- **Fundamentals data-source mismatch measured** (`diag_fundamentals_mismatch.py`, 20 liquid tickers): **40.0% disagreement rate** between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels — double the 20% flag threshold. Revenue growth is the dominant driver (TSLA sign-flips: +15.8% live vs −11.78% SimFin). Escalated in KNOWN_ISSUES from Low→Medium. **Mitigation choice (align live-to-SimFin vs backtest-to-TTM) intentionally left as a user decision, not made this session.**
- **Silent RS fallback fixed on both sides**: `categoricalAssessment.js` and `categorical_engine.py`/`backtest_holistic.py` no longer fabricate RS=1.0 when missing — now visibly caps the assessment below Strong with an explicit reason. Verified JS and Python produce identical behavior on a missing-RS test case. Fixed a knock-on `App.jsx` display bug.

### 5. Breakout Engine — Wired and Validated

A parallel session had built a standalone 8-state breakout classifier (`backend/breakout_detection.py`, spec, Pine companion) but never registered its Flask route. Reconciled `BREAKOUT_ENHANCEMENT_PLAN.md` against this work (redesigned Phases 2–3 to consume the richer engine), then executed the wiring:
- `register_breakout_routes()` registered in `backend.py` following the existing optional-import pattern.
- Validated on IBM, MSFT, NVDA, PLTR, INTC + one invalid-ticker edge case — all correct, no fabricated values, no false `BREAKOUT_CONFIRMED` on weak names.
- `/api/breakout/<ticker>` is now a real, working endpoint.

## Files Changed Today

| File | Type | Content |
|------|------|---------|
| `frontend/src/utils/simplifiedScoring.js` | Modified | RS threshold 1.2→1.0 |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | Created | Frozen config for paper trading |
| `backend/backtest/simfin_loader.py` | Modified | Env-based API key, fail-fast |
| `backend/.env`, `backend/.env.example` | Modified | `SIMFIN_API_KEY` |
| `.gitignore` | Modified | venv, verdict grid artifacts |
| `backend/backend.py` | Modified | `BACKEND_VERSION` constant, breakout routes wired |
| `frontend/src/components/DecisionMatrix.jsx` | Deleted | Dead code (unwired since Day 70) |
| `frontend/src/utils/scoringEngine_day4.js`, `scoringEngine_v2.1.js` | Deleted | Legacy dead code |
| `frontend/src/utils/riskRewardCalc.js` | Modified | Stale doc-comment fix |
| `backend/backtest/mr_simulator.py` | Modified | Transaction costs, gap-aware fills |
| `backend/backtest/gate5_combined.py` | Modified | Transaction costs (momentum leg) |
| `backend/backtest/trade_simulator.py` | Modified | Gap-aware fills |
| `backend/backtest/backtest_holistic.py` | Modified | Cooldown fix, new stats surfaced, RS fallback fix |
| `backend/backtest/metrics.py` | Modified | scipy t-test, actual trades/year, block bootstrap, fixed-risk DD |
| `backend/backtest/categorical_engine.py` | Modified | Verdict parity bug fixed, RS fallback fixed |
| `backend/backtest/test_verdict_parity.py` | Created | 86,400-combo JS↔Python parity grid |
| `frontend/scripts/verdict_grid.mjs` | Created | JS-side grid runner |
| `docs/claude/versioned/VERDICT_PARITY_GRID_FINDINGS_DAY78.md` | Created | Parity bug findings + fix record |
| `backend/backtest/diag_fundamentals_mismatch.py` | Created | Fundamentals mismatch diagnostic |
| `backend/backtest/diag_fundamentals_mismatch_result.json` | Created | Raw 20-ticker comparison data |
| `frontend/src/utils/categoricalAssessment.js` | Modified | RS fallback fixed |
| `frontend/src/App.jsx` | Modified | RS display fix |
| `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` | Modified | All Phase 0–3 tasks marked DONE with results |
| `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` | Modified | Reconciled with parallel session's engine; Phase 1.5 marked DONE |
| `docs/claude/versioned/KNOWN_ISSUES_DAY78.md` | Modified | Fundamentals mismatch escalated Low→Medium with measured data |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) |
| Gate 4 | MR standalone | ✅ PASSED — **now net of costs**: PF 1.26→1.23 |
| Gate 5 | Combined momentum+MR | ✅ PASSED — **now net of costs + gap-aware**: verdict unchanged |
| — | JS↔Python verdict parity | ✅ 100% parity (86,400/86,400), 1 bug found and fixed |
| — | Fundamentals live↔backtest coherence | ⚠️ MEASURED: 40.0% disagreement — mitigation choice pending |
| — | Survivorship-free re-validation | ⏳ Remediation Phase 4 — not yet started |

**Paper trading remains unblocked** — config is frozen and pre-registered (`PAPER_TRADING_PREREGISTRATION.md`). The 40% fundamentals mismatch is a known, documented caveat, not a blocker.

---

## Next Session Priorities

1. **Fable Remediation Phase 4** — survivorship-free re-validation (the big one: rebuild the backtest universe without hindsight bias, 1–2 dedicated sessions).
2. **Fable Remediation Phase 5** — paper-trading instrumentation (entry-slippage logging, regime snapshots on every paper trade).
3. **Decide fundamentals mitigation** (Task 3.2 finding) — align live-to-SimFin or backtest-to-TTM methodology.
4. **Confirm SimFin key rotation** — user needs to verify the old leaked key was rotated at simfin.com.
5. **Paper trading** — can begin any time now that the config is frozen.
6. **Breakout Plan Phase 0** (Config D/E backtest) — now unblocked (remediation Phase 2's gap-aware fills are done).
7. Breakout Plan Phases 2–3 (scan badges, `/breakout-watch` skill) — unblocked by the engine wiring done today.
8. N4 Market Phase synthesis / `/ibkr-scan` / Value Tab Phase 2 / Canadian Analyze page — still queued behind the above.
