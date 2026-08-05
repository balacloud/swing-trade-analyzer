# Known Issues — Day 86 (July 15, 2026)

## Changes from Day 85

**Resolved this session:**
- ✅ Master Framework Watchlist's Volume and Change % columns showed "N/A" — fixed for free (`/api/sr/<ticker>` already fetched the OHLCV needed, just wasn't returning it). Fixes both this watchlist and Nirmal's Watchlist at once. Verified live on 5 tickers.

**Investigated, deferred by explicit user choice (not a bug):**
- Name and Market Cap still show "N/A"/ticker-symbol for both curated watchlists. Root cause: `/api/sr/<ticker>` never fetches company metadata (name/sector/market cap) — it was only ever built to compute price-derived support/resistance levels from OHLCV bars. Not a TradingView failure — TradingView isn't called anywhere in this code path (curated watchlists deliberately bypass it). Fixing this would require a separate fundamentals API call per ticker (added latency + provider rate-limit cost across 76+ tickers) — user chose not to pay that cost.

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

### Low: Scan Tab Batch Breakout Badges Can't Distinguish NOT_READY From a Failed Fetch (carried from Day 85)
**Severity:** Low
**Description:** `App.jsx`'s Scan tab batch badge column (~line 2753) renders both `status === 'NOT_READY'` and an actual fetch error as the same plain "—" dash. The single-ticker Analyze page had this exact ambiguity fixed Day 85; the Scan tab's 20-row table wasn't, since a muted badge on every non-candidate row could be noisy at that scale.
**Fix:** Not yet requested — queued as ROADMAP optional item.

### Low: Master Framework Watchlist / Nirmal Watchlist — Name & Market Cap Not Populated (Day 85-86)
**Severity:** Low (known limitation, accepted)
**Description:** Both curated-ticker-list Scan presets show the bare ticker symbol for Name and "N/A" for Market Cap, since `/api/sr/<ticker>` never fetches company metadata. Volume and Change % were fixed for free (Day 86); Name/Market Cap would need a separate fundamentals call per ticker.
**Fix:** Deferred by explicit user choice — not worth the added latency/rate-limit cost for a curated-watchlist summary table. Revisit only if it becomes annoying in daily use.

### Info: Master Framework Watchlist — Built, Tested, Volume/Change Fixed (Day 85-86)
**Severity:** Info (milestone)
**Description:** 76-ticker Scan tab preset sourced from the user's Notion investment frameworks. User-tested live (76/76 matched), gap found and fixed same day. See `docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md`.

### Info: Backend/Frontend Process Reliability Fixed (Day 85)
**Severity:** Info (milestone)
**Description:** `start.sh` previously left both dev servers' stdout/stderr attached to the launching terminal; closing that terminal broke their file descriptors and any subsequent `print()` call 500'd the request. Now both processes run via `nohup ... >> logfile 2>&1 & disown`. Golden Rule 23.

### Info: Breakout NOT_READY Badge Now Shown, Not Hidden (Day 85)
**Severity:** Info (milestone)
**Description:** Matches `BREAKOUT_ENGINE_SPEC.md` §13's own "Muted" treatment for `NOT_READY` instead of hiding the card/badge entirely.

### Info: TradingView Screener Reference Doc Created (Day 85)
**Severity:** Info (milestone)
**Description:** `docs/claude/design/TRADINGVIEW_SCREENER_IMPLEMENTATION.md` — a portable writeup of the screener implementation (file map, request flow, gotchas) for reuse in another project.

### Info: UI Code Quality Fix Plan — FULLY COMPLETE (Day 82-83)
**Severity:** Info (milestone)

### Info: Tradier Provider — Live, Reliability-Only (Day 83)
**Severity:** Info (milestone)

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
