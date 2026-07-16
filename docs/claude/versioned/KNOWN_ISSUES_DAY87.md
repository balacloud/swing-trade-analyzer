# Known Issues — Day 87 (July 16, 2026)

## Changes from Day 86

**Shipped this session:**
- ✅ Breakout Enhancement Plan Phase 1 ("Near Breakout" scan preset) — the whole plan is now complete.
- ✅ N4 Market Phase Synthesis (`/api/market/phase`, Context tab banner).
- ✅ Price Structure Card Phase 2 (HH/HL/LH/LL market structure, `/api/sr/<ticker>`'s `meta.marketStructure`).

**Deferred this session (explicit user decision, not oversights):**
- N3 gap-fill detection — no design doc exists (only a placeholder pointer in `BREAKOUT_ENHANCEMENT_PLAN.md`). Needs its own design session before any code.
- Value Tab Phase 2 — spec requires nightly batch-prefetch infrastructure (watchlist + scheduled job), explicitly gated by `VALUE_TAB_SPEC.md` to "build only after feature freeze lift." Building on-demand instead would contradict the documented design and burn AlphaVantage's ~8-ticket/day free-tier budget fast.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low: AlphaVantage Daily Quota Exhausted Mid-Session (Day 87)
**Severity:** Low (transient, self-resolving)
**Description:** A diagnostic check to verify `BALANCE_SHEET`/`CASH_FLOW` field names (for Value Tab Phase 2 planning) made 3 direct API calls that bypassed the app's internal rate-limiter tracking (used raw `requests.get()`, not the provider class). 2 of 3 calls were rate-limited by AlphaVantage's own servers, confirming the account's real daily quota (25 req/day) was exhausted at the time. The app's own `rate_limit_state` table was unaffected (it only tracks calls made through the provider class), so this is a one-time diagnostic cost, not an ongoing bug — but it means AV-dependent features (growth metrics gap-filling) may have been degraded for the rest of Day 87 until the quota reset.
**Fix:** None needed — quota resets daily. Worth remembering: any future diagnostic AV calls should go through `check_rate_limit()` / the provider class, not raw `requests`, so the app's own tracking stays accurate.

### Low: SimFin API Key Rotation Unconfirmed (carried from Day 79)
**Severity:** Low
**Description:** Key moved to `backend/.env`, but the OLD key is still in git history and was never confirmed rotated at simfin.com.
**Fix:** User to confirm rotation status.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Low: Scan Tab Batch Breakout Badges Can't Distinguish NOT_READY From a Failed Fetch (carried from Day 85)
**Severity:** Low
**Fix:** Not yet requested — queued as ROADMAP optional item.

### Low: Master Framework Watchlist / Nirmal Watchlist — Name & Market Cap Not Populated (Day 85-86)
**Severity:** Low (known limitation, accepted)
**Fix:** Deferred by explicit user choice.

### Info: Breakout Enhancement Plan — FULLY COMPLETE (Day 87)
**Severity:** Info (milestone)
**Description:** All phases (0, 1, 1.5, 2, 3) done. `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` is now historical/reference only.

### Info: N4 Market Phase Synthesis — Built (Day 87)
**Severity:** Info (milestone)
**Description:** Research (Day 76) → build (Day 87). 5-phase classifier (Bull Rally/Late Bull/Distribution/Correction/Recovery) from SPY trend × VIX level, breadth/sector context as supporting evidence. See `API_CONTRACTS_DAY87.md`.

### Info: Price Structure Card Phase 2 — Built (Day 87)
**Severity:** Info (milestone)
**Description:** HH/HL/LH/LL structure classification via a new, separate `market_structure_engine.py` — does not reuse or modify `support_resistance.py`'s existing (price-sorted, non-chronological) pivot detector. Phase 3 (visual chart) still deferred.

### Info: Complete Feature Freeze Declared (Day 87)
**Severity:** Info (milestone/process)
**Description:** All backlog items that could reasonably be closed this session are closed — built (3 items) or explicitly deferred with a documented reason (2 items, both needing their own design sessions). Going forward: bug fixes and paper-trading monitoring only, until 50+ live trades confirm momentum/MR edges. See Golden Rule 24 for the process lesson this session surfaced.

### Info: Automated Paper Trading Engine — Still Accumulating (carried from Day 81)
**Severity:** Info (milestone, ongoing)
**Description:** `backend/paper_trading/` running unattended daily via launchd. Expected to take months to reach the 50-trade bar. `/sta-start` warns if the job goes stale >3 days.

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified (carried from Day 77)
**Severity:** Info (verify before building `/ibkr-scan`)

### Info: Value Tab — ROIC Null on Finnhub Free Tier (carried from Day 75)
**Severity:** Info (Phase 1 limitation)

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
