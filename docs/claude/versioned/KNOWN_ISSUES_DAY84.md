# Known Issues — Day 84 (July 13, 2026)

## Changes from Day 83

**Resolved this session — the entire UI Code Quality Fix Plan (Groups A-E):**
- ✅ Scan Tab and Paper-Trading Engine Could See Different Candidate Sets (Task A1) — fixed, verified byte-identical.
- ✅ Trade Setup Card Could Display a Negative Stop Price (Task A2) — fixed, verified with a synthetic edge case.
- ✅ Price Structure Card's "Pattern Forming" Watch Item Could Never Fire (Task A3) — fixed, verified live on JPM.
- ✅ Three Inconsistent Liquidity Thresholds (Task A4) — unified, verified live on ASIC. Also added a non-critical "RS Unavailable" gate.
- ✅ Nirmal Watchlist Scan Failed Silently (Task A5) — fixed, verified both directions.
- ✅ MR Signal Card Condition Labels Stale (Task A6) — fixed, verified live on ABBV.
- ✅ Duplicate candidate-parsing logic (Task B1) — consolidated.
- ✅ Pattern Detection Card 3x copy-paste + 2 unguarded `&&` renders (Task B2) — refactored + fixed.
- ✅ Zombie legacy verdict (Task B3) — `determineVerdict()` deleted entirely after confirming its fallback was permanently unreachable.
- ✅ RS Card's fake percentile row (Task B4) — relabeled.
- ✅ Categorical Assessment's 4 copy-pasted tiles (Task B5) — refactored into a shared component.
- ✅ Dormant Canadian-ticker bug in `live_signals.py` (Task B6) — fixed, verified.
- ✅ ~7 dead functions/exports + ~37 debug `console.log` lines (Group C) — removed.
- ✅ Tradier provider built (Task D1) — 3rd-tier OHLCV/quote fallback, verified with forced-failover tests.
- ✅ Breakout Status card polish (Task E1) — loading skeleton, styling, warnings surfaced.
- ✅ Ticker-search stale-response race (Task E2) — fixed via `useRef`-tracked request id.
- ✅ Scan-tab-rescan stale-response race (Task E3) — fixed via `useRef`-tracked scan id.
- ✅ Scan tab 20-row breakout-badge cap footer note (Task E4) — added.

**Deliberately left untouched (per the plan's own assessment, not oversights):**
- Task E5 (hoisting `BREAKOUT_BADGE_CONFIG`/`NIRMAL_WATCHLIST` to module scope) — plan explicitly said this isn't a real performance problem at this scale.
- Task E6 (3-way scan-strategy sync fragility) — plan explicitly said not worth a dedicated task.

**Doc drift fixed:** `ROADMAP.md`'s version line hadn't been updated since Day 81 (still said v4.39 while `CLAUDE_CONTEXT.md` had already moved to v4.42) — caught and corrected as part of this close.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision: (a) align live to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low: SimFin API Key Rotation Unconfirmed (carried from Day 79)
**Severity:** Low
**Description:** Key moved to `backend/.env`, but the OLD key is still in git history and was never confirmed rotated at simfin.com.
**Fix:** User to confirm rotation status.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: UI Code Quality Fix Plan — FULLY COMPLETE (Day 82-83)
**Severity:** Info (milestone)
**Description:** All 5 groups (A-E) of `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` are done and browser/API-verified. See "Changes from Day 83" above for the full list. Nothing left to triage from this plan.

### Info: Tradier Provider — Live, Reliability-Only (Day 83)
**Severity:** Info (milestone)
**Description:** `backend/providers/tradier_provider.py` is now the 3rd-tier OHLCV/quote fallback (after TwelveData, yfinance). Options and beta-tier fundamentals endpoints were evaluated (Day 82) but deliberately not integrated — options belong to OptionsIQ (separate repo), and fundamentals don't close STA's actual gaps (missing roic/revenueGrowth/epsGrowth/margins/marketCap).

### Info: Automated Paper Trading Engine — Still Accumulating (carried from Day 81)
**Severity:** Info (milestone, ongoing)
**Description:** `backend/paper_trading/` running unattended daily via launchd. Expected to take months to reach the 50-trade bar (~7 months MR, ~2.2 years momentum, both highly uncertain). `/sta-start` has a dead-man-switch warning if the job goes stale >3 days.

### Info: Breakout Plan Phase 1 — Only Remaining Phase (carried from Day 82)
**Severity:** Info (planned — gated on user approval)

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
