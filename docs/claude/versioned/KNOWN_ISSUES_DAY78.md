# Known Issues — Day 78 (July 5, 2026)

## Changes from Day 77
- No code changed; no bugs resolved.
- **Added 8 issues from the Fable 5 full-system review** (4 Medium, 4 Low). All have assigned remediation tasks in `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md`.
- Gate 4/Gate 5 milestone entries annotated: results are gross of transaction costs.

## Updates (Day 78, sessions 2–4 — remediation execution)
- Remediation Phase 0 + Phase 1 + Phase 2 complete (RS threshold resolved, repo hygiene, MR transaction costs, gap-aware fills, statistics fixed, JS↔Python verdict parity: 1 bug found and fixed, now 100% parity across 86,400 combos).
- Remediation Phase 3 Task 3.2 complete: fundamentals mismatch **measured at 40.0%** (see updated entry below) — escalated from Low to Medium severity.
- SimFin API key rotation still pending (user action, not yet confirmed done).

---

## Open Issues

### Medium: Backtest Universe Survivorship Bias (Day 78 — Fable review)
**Severity:** Medium (validity of headline metrics)
**Description:** The 60-ticker universe in `backtest_holistic.py:55-80` was hand-picked in 2026 and is dominated by 2020–2025 winners. Config C PF 1.61 is likely overstated; honest live expectation ~1.1–1.3. Same walk-forward window also reused across ~20 tuning sessions (Days 55–75), eroding OOS validity.
**Fix:** Remediation Phase 4 (survivorship-free re-validation on SimFin universe with pre-committed interpretation criteria).

### Medium: MR Backtest + Gate 5 Have No Transaction Costs (Day 78 — Fable review)
**Severity:** Medium (validity — Gate 4 PF 1.26 is gross; net may be near breakeven)
**Description:** `mr_simulator.py` and `gate5_combined.py` apply zero costs, unlike the momentum backtest. Both simulators also fill stops at the exact stop price, ignoring gap-downs (worst for MR, which buys oversold stocks).
**Fix:** Remediation Tasks 2.1 (costs) + 2.2 (gap-aware fills). 50/50 capital split decision should be revisited if net MR PF < ~1.10.

### Medium: RS Threshold Contradiction — Default View Unbacktested (Day 78 — Fable review)
**Severity:** Medium (default screen enforces a threshold the flagship backtest never ran)
**Description:** Simple checklist (default view since Day 75) requires RS ≥ 1.2 (`simplifiedScoring.js:99`); full view Strong-Technical and backtested Config C use RS ≥ 1.0 (`categoricalAssessment.js:269`). ROADMAP cites contradictory validations for both values (Tier 0D on 5/3 trades vs Day 70B simplified backtest).
**Fix:** Remediation Task 0.2 — user decision, recommended: align simple view to 1.0. **BLOCKER for config pre-registration.**

### Medium: SimFin API Key Hardcoded in Git (Day 78 — Fable review)
**Severity:** Medium (security hygiene — key is in git history)
**Description:** Live API key at `simfin_loader.py:20`. Removing from HEAD does not un-leak it.
**Fix:** Remediation Task 1.1 — move to `.env` + user rotates key at simfin.com.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch — MEASURED (Day 78, session 4)
**Severity:** Medium (escalated from Low — measured disagreement exceeds the 20% flag threshold by 2x)
**Description:** Backtest ROE = SimFin quarterly ×4; live ROE = Finnhub/AlphaVantage/yfinance TTM. Measured via `backend/backtest/diag_fundamentals_mismatch.py` on 20 liquid tickers (15 comparable, 5 skipped — no SimFin data available for GS/BAC/JNJ/2 others): **40.0% disagreement rate** (6/15 mismatched Fundamental label: AAPL, TSLA, MA, UNH, LLY, KO). Revenue growth is the dominant driver — TSLA even sign-flips (+15.8% live vs −11.78% SimFin). SimFin also returns `None` for debt/equity on several mega-caps (AMZN, META, NVDA, MA) where live data has no gap.
**Meaning:** "Live Config C" and "backtested Config C" are meaningfully different systems for the Fundamental category on ~40% of names — a stock the backtest scored Strong/Decent may score differently live, and vice versa.
**Fix:** Remediation Task 3.2 marked DONE (diagnostic built + measured). Mitigation choice is a user decision, not yet made: (a) align live fundamentals computation to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals to match live. Full per-ticker data: `backend/backtest/diag_fundamentals_mismatch_result.json`.

### Low: Statistical Methodology Weaknesses in metrics.py (Day 78 — Fable review)
**Severity:** Low (measurement quality)
**Description:** t-test assumes iid trades (regime/ticker clustering → p=0.002 overstated); Sharpe hardcodes 25 trades/yr; max DD 52.6% is a sequential-100%-equity artifact; hand-rolled p-value approximation.
**Fix:** Remediation Task 2.3 (scipy + block bootstrap + honest 2%-risk DD metric).

### Low: JS↔Python Verdict Parity Held by Only 5 Test Vectors (Day 78 — Fable review)
**Severity:** Low (drift risk between live JS and backtested Python)
**Description:** `categorical_engine.py` `_verify_parity()` has 5 vectors for a 9-rule verdict tree × 3 holding periods. Also `categoricalAssessment.js:262` silently substitutes RS=1.0 when missing (violates Day 54 no-silent-fallback rule) — backtest does the same at `backtest_holistic.py:248`.
**Fix:** Remediation Tasks 2.4 (grid parity test) + 3.3 (visible RS-missing handling, both sides identically).

### Low: Repo/Version Hygiene (Day 78 — Fable review)
**Severity:** Low (no functional impact)
**Description:** `backend/venv/` tracked in git; `/api/health` reports version '2.23' vs documented v2.35; dead code (`DecisionMatrix.jsx`, `scoringEngine_day4.js`, `scoringEngine_v2.1.js`); `PROJECT_INSTRUCTIONS.md` deleted in worktree but never committed (pre-existing, needs user confirmation).
**Fix:** Remediation Tasks 1.2–1.4.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: Breakout Plan Phase 0 — Config D/E Backtest Not Yet Run (Day 78)
**Severity:** Info (planned)
**Description:** Whether breakout-confirmed-only entries beat mixed entries is unmeasured. `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` Phase 0 — gated on remediation Phase 2 (gap-aware fills).

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified (carried from Day 77)
**Severity:** Info (verify before building `/ibkr-scan`)

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built (carried from Day 76)
**Severity:** Info (planned — queued behind remediation + paper trading)

### Info: /ibkr-scan Skill — Design Complete, Not Yet Built (carried from Day 77)
**Severity:** Info (planned)

### Info: Price Structure Card — Phase 1 Only (carried from Day 72)
**Severity:** Info (known limitation)

### Info: Value Tab — ROIC Null on Finnhub Free Tier (carried from Day 75)
**Severity:** Info (Phase 1 limitation)

### Info: Value Tab Phase 2 Deferred (carried from Day 75)
**Severity:** Info (planned)

### Info: Gate 5 Combined Sharpe Measurement Artifact (carried from Day 75)
**Severity:** Info (methodological note — now also covered by remediation Task 2.3)

### Info: Sentiment Removed from Verdict (carried from Day 70)
**Severity:** Info (architectural decision)

### Info: Gates 4+5 PASSED — Paper Trading Unblocked (carried from Day 75)
**Severity:** Info (milestone — Day 78 annotation: config freeze/pre-registration required first; gross-of-costs caveat on Gate 4/5 numbers)

### Info: Blended RS Degrades Verdict Quality (carried)
**Severity:** Info (by design)

### Info: Backtest Max Drawdown Still High (carried)
**Severity:** Info (backtest-only — Day 78: metric itself is an artifact, see remediation Task 2.3)

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated (carried)
**Severity:** Info

### Info: FOMC Dates Hardcoded through 2027 (carried)
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile (carried)
**Severity:** Info (documented, current values validated)
