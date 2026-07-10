# Known Issues — Day 80 (July 8, 2026)

## Changes from Day 79

**Resolved this session:**
- ✅ Backtest Universe Survivorship Bias — Phase 4 complete. Canonical unbiased numbers: Config C PF 1.61→1.40 (not yet significant), MR PF 0.99 (clean null on unrestricted universe).
- ✅ MR Backtest Has No Liquidity Gate — found and fixed during the one-time re-test. Original entry had only `price > $5`, no dollar-volume filter. Added price>$10, 20d ADV>$25M (backtest only, see new issue below for the live-detector gap this creates).
- ✅ Fable Remediation Plan — **all 5 phases now complete.**

**Changed verdict (not a new issue, a correction):**
- 🔄 MR capital allocation status: was "do not allocate, edge does not survive" (Day 79 session 2) → now "real but modest, unconfirmed — same tier as momentum" (Day 79 session 4, after the liquidity re-test: PF 0.99→1.16, Sharpe -0.10→1.30). Still not statistically confirmed (block bootstrap p=0.064). See `SURVIVORSHIP_FREE_BACKTEST_DAY79.md` addendum.

**New:**
- ⚠️ Live MR detector (`mean_reversion.py`) does not have the new liquidity gate — only the backtest (`mr_simulator.py`) does. See below.
- Paper-trading instrumentation complete (Phase 5): entry slippage + regime snapshot logging now live in the Forward Test tab.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver.
**Fix:** Mitigation choice still a pending user decision: (a) align live to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Medium: Live MR Detector Missing Liquidity Gate (Day 80)
**Severity:** Medium (would matter as soon as MR moves toward live signals)
**Description:** The one-time MR liquidity re-test (Day 79 session 4) added price>$10 + 20d ADV>$25M to the **backtest** (`backend/backtest/mr_simulator.py`) only. The **live production detector** (`backend/mean_reversion.py`, behind `/api/mr/signal/<ticker>` and `/api/mr/scan`) still only filters `price > $5` — no dollar-volume gate. If MR proceeds to live paper trading before this is fixed, live signals would include the thin/illiquid names the backtest re-test specifically excluded to get its PF 1.16 result — meaning live signals would NOT be the same system that was validated.
**Fix:** Add the same liquidity gate to `mean_reversion.py`'s `detect_mr_signal()` before MR paper trading begins in earnest.

### Low: SimFin API Key Rotation Unconfirmed (carried from Day 79)
**Severity:** Low
**Description:** Key moved to `backend/.env` (Task 1.1), but the OLD key is still in git history and was never confirmed rotated at simfin.com. A new key was shared in conversation Day 79 but not yet confirmed as the intended replacement or applied.
**Fix:** User to confirm rotation status.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: Fable Remediation Plan — ALL 5 PHASES COMPLETE (Day 80)
**Severity:** Info (milestone)
**Description:** Phase 0 (freeze/pre-register) → Phase 1 (hygiene) → Phase 2 (backtest integrity) → Phase 3 (backtest↔live coherence) → Phase 4 (survivorship-free re-validation) → Phase 5 (paper-trading instrumentation), plus the user-directed MR liquidity re-test. Both momentum and MR are now backtest-validated-but-unconfirmed; live paper trading (50+ trades each) is the remaining test. See `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` for full history.

### Info: Breakout Plan Phase 0 — Config D/E Backtest Not Yet Run (carried, unblocked)
**Severity:** Info (planned)
**Description:** Whether breakout-confirmed-only entries beat mixed entries is unmeasured. Prerequisite (gap-aware fills) is done; can run any time.

### Info: Breakout Engine Wired — Phases 2–3 Ready (carried from Day 79)
**Severity:** Info (milestone)
**Description:** `/api/breakout/<ticker>` registered and validated. Breakout Plan Phases 2 (scan badges) and 3 (`/breakout-watch` skill) are unblocked, not started.

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified (carried from Day 77)
**Severity:** Info (verify before building `/ibkr-scan`)

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built (carried from Day 76)
**Severity:** Info (planned — queued behind paper trading)

### Info: /ibkr-scan Skill — Design Complete, Not Yet Built (carried from Day 77)
**Severity:** Info (planned)

### Info: Price Structure Card — Phase 1 Only (carried from Day 72)
**Severity:** Info (known limitation)

### Info: Value Tab — ROIC Null on Finnhub Free Tier (carried from Day 75)
**Severity:** Info (Phase 1 limitation)

### Info: Value Tab Phase 2 Deferred (carried from Day 75)
**Severity:** Info (planned)

### Info: Gate 5 Combined Sharpe Measurement Artifact (carried from Day 75)
**Severity:** Info (methodological note)

### Info: Sentiment Removed from Verdict (carried from Day 70)
**Severity:** Info (architectural decision)

### Info: Paper Trading Unblocked, Instrumented, Both Systems Unconfirmed (Day 80)
**Severity:** Info (milestone)
**Description:** Config frozen (`PAPER_TRADING_PREREGISTRATION.md`). Entry-slippage and regime-snapshot logging live (Phase 5). Both momentum (PF 1.40, p=0.094) and MR (PF 1.16, p=0.064) are directionally positive but not statistically confirmed by backtest alone — 50+ live trades each is the real test per the pre-registered criteria.

### Info: Blended RS Degrades Verdict Quality (carried)
**Severity:** Info (by design)

### Info: Backtest Max Drawdown — Reported Two Ways (carried from Day 79)
**Severity:** Info (methodological improvement)

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated (carried)
**Severity:** Info

### Info: FOMC Dates Hardcoded through 2027 (carried)
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile (carried)
**Severity:** Info (documented, current values validated)
