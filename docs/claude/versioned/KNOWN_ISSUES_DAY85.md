# Known Issues — Day 85 (July 15, 2026)

## Changes from Day 84

**Resolved this session:**
- ✅ Backend/frontend processes died silently after their launching terminal closed (`OSError: [Errno 5] Input/output error` on every `print()`-logging request path, 500s across many endpoints, not just breakout) — `start.sh` now uses `nohup ... & disown` with output redirected to log files. New Golden Rule 23.
- ✅ Breakout Status card/badge was completely hidden (not just muted) whenever a ticker's status was `NOT_READY`, indistinguishable from "broken" — now shows a muted "Not Ready" badge per the engine's own spec (§13).

**New, resolved same session:**
- ✅ Personalized Notion-based screener — scoped and built same session. 76-ticker "🏛️ Master Framework Watchlist" Scan tab option, sourced from the user's Notion investment frameworks. Exhaustive verification caught 3 ticker-format bugs + 1 unsupported ticker before shipping. User-tested live: 76/76 matched. See `docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md`.

**New, not yet acted on:**
- Scan tab's batch breakout badge column (20-row table) still can't distinguish `NOT_READY` from a failed fetch — both render as "—". Same bug class as the fix above, not yet requested at this location (ROADMAP optional item).
- Master Framework Watchlist's summary table shows "N/A" for Name/Sector/Change/Volume/Market Cap — identical pre-existing behavior to Nirmal's Watchlist (both bypass the TradingView query those fields come from). User explicitly chose to ship as-is.

**Investigated, no code change (by user's own decision):** TradingView screener market-data delay (~15 min without an authenticated `sessionid` cookie) — decided not to wire up cookie-based real-time auth, since it costs nothing for STA's EOD-based indicators and would add an expiring-credential dependency for no practical benefit.

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

### Low: Scan Tab Batch Breakout Badges Can't Distinguish NOT_READY From a Failed Fetch (new, Day 85)
**Severity:** Low
**Description:** `App.jsx`'s Scan tab batch badge column (~line 2753) renders both `status === 'NOT_READY'` and an actual fetch error (`b.error != null`) as the same plain "—" dash. The single-ticker Analyze page had this exact ambiguity and it was fixed today (Day 85); the Scan tab's 20-row table wasn't, since a muted badge on every non-candidate row could be noisy at that scale and the user hadn't asked for it there.
**Fix:** Not yet requested — queued as ROADMAP optional item #13.

### Info: Backend/Frontend Process Reliability Fixed (Day 85)
**Severity:** Info (milestone)
**Description:** `start.sh` previously left both dev servers' stdout/stderr attached to the launching terminal; closing that terminal broke their file descriptors and any subsequent `print()` call 500'd the request. Now both processes run via `nohup ... >> logfile 2>&1 & disown`. New Golden Rule 23.

### Info: Breakout NOT_READY Badge Now Shown, Not Hidden (Day 85)
**Severity:** Info (milestone)
**Description:** Matches `BREAKOUT_ENGINE_SPEC.md` §13's own "Muted" treatment for `NOT_READY` instead of hiding the card/badge entirely.

### Info: TradingView Screener Reference Doc Created (Day 85)
**Severity:** Info (milestone)
**Description:** `docs/claude/design/TRADINGVIEW_SCREENER_IMPLEMENTATION.md` — a portable writeup of the screener implementation (file map, request flow, gotchas) for reuse in another project.

### Info: UI Code Quality Fix Plan — FULLY COMPLETE (Day 82-83)
**Severity:** Info (milestone)
**Description:** All 5 groups (A-E) done and browser/API-verified. Nothing left to triage from this plan.

### Info: Tradier Provider — Live, Reliability-Only (Day 83)
**Severity:** Info (milestone)
**Description:** `backend/providers/tradier_provider.py` is the 3rd-tier OHLCV/quote fallback (after TwelveData, yfinance).

### Info: Automated Paper Trading Engine — Still Accumulating (carried from Day 81)
**Severity:** Info (milestone, ongoing)
**Description:** `backend/paper_trading/` running unattended daily via launchd. Expected to take months to reach the 50-trade bar (~7 months MR, ~2.2 years momentum, both highly uncertain). `/sta-start` has a dead-man-switch warning if the job goes stale >3 days.

### Info: Breakout Plan Phase 1 — Only Remaining Phase (carried from Day 82)
**Severity:** Info (planned — gated on user approval)

### Info: Master Framework Watchlist — Built and Verified (Day 85)
**Severity:** Info (milestone)
**Description:** 76-ticker Scan tab preset sourced from the user's Notion investment frameworks, built and user-verified live same session. See "Changes from Day 84" above and `docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md`.

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
