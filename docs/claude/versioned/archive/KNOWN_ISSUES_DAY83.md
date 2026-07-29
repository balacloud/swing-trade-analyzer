# Known Issues — Day 83 (July 12, 2026)

> **Mid-session update (July 13):** All 6 Group A items from the UI Code
> Quality Fix Plan (both High-severity issues + 4 Medium/Low) were fixed and
> browser-verified this session — moved from Open to Resolved below. Also
> did Task B1 (duplicate candidate parsing) alongside A1 since it touched
> the same code region. Groups B2-E remain untouched.

## Changes from Day 81
*(Day 82 patched Day 81's file in place rather than creating its own — see that file's header note. This is the first fresh KNOWN_ISSUES file since Day 81.)*

**Resolved:**
- ✅ Breakout Plan Phases 0, 2-3 — done (Day 82). Only Phase 1 remains.
- ✅ Git risk items (untracked provider, tracked node_modules) — fixed (Day 82).
- ✅ `BACKEND_VERSION` drift (code said 2.35, docs claimed 2.38) — corrected, now genuinely bumped to 2.37 this close.
- ✅ 5 data-source bugs (cache period mismatch, uncached MR signal route, AlphaVantage rate-limiter token waste, uncached VIX quotes, dead Stooq code) — fixed (Day 83).
- ✅ Rate-limiter/circuit-breaker per-process state architecture gap — Flask backend and the paper-trading job were silently not sharing rate-limit/circuit-breaker state. Rebuilt on shared SQLite (Day 83). New Golden Rule 22.
- ✅ Bottom Line Card redundancy (user-flagged) — deleted, confirmed safe via code read (Day 83).
- ✅ Breakout status missing from Analyze Stock page — added (badge in Simple view, card in Full Analysis view) (Day 83).
- ✅ Scan Tab and Paper-Trading Engine Could See Different Candidate Sets (Task A1) — order_by override guarded; verified byte-identical candidate sets. Also Task B1 (duplicate candidate-parsing logic) fixed alongside it.
- ✅ Trade Setup Card Could Display a Negative Stop Price (Task A2) — now sources stop/RR from `calculateRiskReward()`; verified with a synthetic negative-stop edge case.
- ✅ Price Structure Card's "Pattern Forming" Watch Item Could Never Fire (Task A3) — verified live on JPM.
- ✅ Three Inconsistent Liquidity Thresholds (Task A4) — unified via new `liquidityThresholds.js`; verified live on ASIC. Also added a non-critical "RS Unavailable" gate for missing RS data.
- ✅ Nirmal Watchlist Scan Failed Silently (Task A5) — verified both backend-down (shows error) and backend-up (renders normally) paths.
- ✅ MR Signal Card Condition Labels Stale (Task A6) — verified live on ABBV.

**New:**
- 🆕 UI Code Quality Fix Plan documented — `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`. 3 Fable audits (Analyze page cards, Scan Market tab, Tradier evaluation) synthesized into 6 real bugs, 6 DRY violations, a dead-code inventory, a Tradier provider build spec, and 6 polish items. **Not yet triaged or executed** — see individual entries below for the highest-severity items, pulled out for visibility.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision: (a) align live to SimFin's annualized-quarterly method, or (b) re-run the backtest with TTM-style fundamentals.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low: Dormant Canadian-Ticker Bug in Live Signals
**Severity:** Low (dormant — only matters if the automated engine is ever pointed at a Canadian market_index)
**Description:** `live_signals.py:111` hardcodes `is_canadian=False` regardless of the `market_index` parameter actually passed in.
**Fix:** Task B6 in the fix-plan doc. Not started.

### Low: SimFin API Key Rotation Unconfirmed (carried from Day 79)
**Severity:** Low
**Description:** Key moved to `backend/.env`, but the OLD key is still in git history and was never confirmed rotated at simfin.com.
**Fix:** User to confirm rotation status.

### Low: Defeat Beta Import Still Present (carried)
**Severity:** Low (no functional impact)

### Info: UI Code Quality Fix Plan — Group A Done, B-E Remain (Day 83)
**Severity:** Info
**Description:** `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` — Group A (all 6 real bugs, listed as Resolved above) plus Task B1 are done and browser-verified. Still open: 5 more DRY-violation cleanups (Group B — incl. a "zombie" legacy-verdict fallback that could theoretically render an unlabeled 0.011-correlation score as if it were the real verdict), a dead-code inventory (Group C), a fully-specified Tradier provider build (Group D — OHLCV/quote fallback only, no options/fundamentals scope creep), and 6 minor polish items (Group E, incl. two stale-response races on ticker search). See the doc directly when triaging what's next.

### Info: Tradier API Key Evaluated — Reliability Upgrade Available, Not Yet Built (Day 83)
**Severity:** Info
**Description:** User added a Tradier brokerage API key. Live-tested (12 API calls): production tier, 120 req/min, good OHLCV (not dividend-adjusted) + quote coverage (including index symbols like `VIX`), beta-tier fundamentals that do NOT close STA's existing gaps, and strong options data that's out of scope for STA (belongs to OptionsIQ). A concrete `TradierProvider` implementation is specified in Task D1 of the fix-plan doc as a 3rd-tier OHLCV/quote fallback — not built yet.

### Info: Automated Paper Trading Engine — Still Accumulating (carried from Day 81)
**Severity:** Info (milestone, ongoing)
**Description:** `backend/paper_trading/` running unattended daily via launchd. Still 0 closed trades as of last check — expected, per the Day 82 time-to-50-trades estimate (~7 months MR, ~2.2 years momentum, both highly uncertain). `/sta-start` now has a dead-man-switch warning if the job goes stale >3 days.

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
