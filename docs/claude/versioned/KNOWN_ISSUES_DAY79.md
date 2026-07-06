# Known Issues — Day 79 (July 6, 2026)

## Changes from Day 78

**Resolved this session:**
- ✅ MR Backtest + Gate 5 Have No Transaction Costs — fixed (Tasks 2.1, 2.2). Net-of-cost figures now primary; gap-aware fills added.
- ✅ RS Threshold Contradiction — resolved (Task 0.2). Simple checklist aligned to RS ≥ 1.0, matching Config C.
- ✅ Statistical Methodology Weaknesses in metrics.py — fixed (Task 2.3). scipy t-test, actual trades/year, block bootstrap, honest 2%-risk drawdown.
- ✅ JS↔Python Verdict Parity Held by Only 5 Vectors — fixed (Task 2.4). 86,400-combo grid built; 1 real bug found (HOLD-fallback missing `Neutral` risk branch) and fixed; now 100% parity.
- ✅ Repo/Version Hygiene — fixed (Tasks 1.2–1.4). venv untracked, `BACKEND_VERSION` constant added, dead code deleted.
- ✅ Silent RS fallback (both JS and Python) — fixed (Task 3.3). Missing RS now visibly caps assessment below Strong with an explicit reason instead of faking neutral 1.0.

**Partially resolved:**
- ⚠️ SimFin API Key Hardcoded in Git — code fixed (key moved to `.env`, Task 1.1), but **user rotation at simfin.com not yet confirmed**. Downgraded to Low pending confirmation.

**Escalated:**
- ⬆️ Backtest↔Live Fundamentals Data-Source Mismatch — measured at **40.0%** disagreement (Task 3.2). Stays Medium; mitigation choice is a pending user decision.

**New milestone:**
- `/api/breakout/<ticker>` wired and validated — a previously-built-but-unregistered breakout classification engine is now a real, working endpoint.

---

## Open Issues

### Medium: Backtest Universe Survivorship Bias (carried from Day 78 — Fable review)
**Severity:** Medium (validity of headline metrics)
**Description:** The 60-ticker universe in `backtest_holistic.py:55-80` was hand-picked in 2026 and is dominated by 2020–2025 winners. Config C PF 1.61 is likely overstated; honest live expectation ~1.1–1.3. Same walk-forward window also reused across ~20 tuning sessions (Days 55–75), eroding OOS validity.
**Fix:** Remediation Phase 4 (survivorship-free re-validation) — NOT YET STARTED. Now unblocked (Phase 2's gap-aware fills are done, so re-validation will use the corrected simulator).

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch — MEASURED (Day 78, session 4)
**Severity:** Medium
**Description:** Measured via `backend/backtest/diag_fundamentals_mismatch.py` on 20 liquid tickers (15 comparable, 5 skipped — no SimFin data for GS/BAC/JNJ/2 others): **40.0% disagreement rate** (6/15 mismatched Fundamental label: AAPL, TSLA, MA, UNH, LLY, KO). Revenue growth is the dominant driver — TSLA sign-flips (+15.8% live vs −11.78% SimFin). SimFin also returns `None` for debt/equity on several mega-caps (AMZN, META, NVDA, MA) where live data has no gap.
**Meaning:** "Live Config C" and "backtested Config C" are meaningfully different systems for the Fundamental category on ~40% of names.
**Fix:** Mitigation choice is a user decision, not yet made: (a) align live fundamentals to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals. Full data: `backend/backtest/diag_fundamentals_mismatch_result.json`.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low: SimFin API Key Rotation Unconfirmed (Day 79)
**Severity:** Low (downgraded from Medium — code-side fix done, this is the remaining user action)
**Description:** Key moved to `backend/.env` (Task 1.1), but the OLD key is still in git history and was never confirmed rotated at simfin.com. A new key (`1114f20f-...`) was shared in conversation Day 79 but not yet confirmed as the intended replacement or applied to `.env`.
**Fix:** User to confirm rotation status and, if applicable, provide explicit go-ahead to update `.env`.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: Breakout Plan Phase 0 — Config D/E Backtest Not Yet Run (carried, now unblocked)
**Severity:** Info (planned)
**Description:** Whether breakout-confirmed-only entries beat mixed entries is unmeasured. `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Phase 0 — prerequisite (remediation Phase 2 gap-aware fills) is now done, so this can run any time.

### Info: Breakout Engine Wired — Phases 2–3 Ready (Day 79)
**Severity:** Info (milestone)
**Description:** `/api/breakout/<ticker>` registered and validated (IBM, MSFT, NVDA, PLTR, INTC + 1 invalid-ticker edge case, all correct). Breakout Plan Phases 2 (scan badges) and 3 (`/breakout-watch` skill) are now unblocked.

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified (carried from Day 77)
**Severity:** Info (verify before building `/ibkr-scan`)

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built (carried from Day 76)
**Severity:** Info (planned — queued behind remediation Phase 4/5 + paper trading)

### Info: /ibkr-scan Skill — Design Complete, Not Yet Built (carried from Day 77)
**Severity:** Info (planned)

### Info: Price Structure Card — Phase 1 Only (carried from Day 72)
**Severity:** Info (known limitation)

### Info: Value Tab — ROIC Null on Finnhub Free Tier (carried from Day 75)
**Severity:** Info (Phase 1 limitation)

### Info: Value Tab Phase 2 Deferred (carried from Day 75)
**Severity:** Info (planned)

### Info: Gate 5 Combined Sharpe Measurement Artifact (carried from Day 75)
**Severity:** Info (methodological note — Sharpe/DD methodology broadly improved by Task 2.3, but this specific Gate 5 combined-portfolio Sharpe note stands independently)

### Info: Sentiment Removed from Verdict (carried from Day 70)
**Severity:** Info (architectural decision)

### Info: Gates 4+5 PASSED — Paper Trading Unblocked, Config Frozen (Day 78/79)
**Severity:** Info (milestone)
**Description:** All gates cleared. Config frozen and pre-registered (`docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md`). Gate 4/5 figures are now net-of-cost and gap-aware (Task 2.1/2.2) — see updated numbers in PROJECT_STATUS_DAY79_SHORT.md.

### Info: Blended RS Degrades Verdict Quality (carried)
**Severity:** Info (by design)

### Info: Backtest Max Drawdown — Now Reported Two Ways (Day 79)
**Severity:** Info (methodological improvement)
**Description:** `metrics.py` now reports both the original sequential-100%-equity DD (a modeling artifact, kept for continuity) and a new fixed-2%-risk-per-trade DD (more honest). See Task 2.3.

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated (carried)
**Severity:** Info

### Info: FOMC Dates Hardcoded through 2027 (carried)
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile (carried)
**Severity:** Info (documented, current values validated)
