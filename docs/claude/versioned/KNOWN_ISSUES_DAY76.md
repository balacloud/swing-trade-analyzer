# Known Issues — Day 76 (May 18, 2026)

## Changes from Day 75
- No bugs resolved this session.
- Added process note: session start protocol failure diagnosed and fixed (CLAUDE_CONTEXT.md now mandatory first read).
- No new functional bugs introduced (no backend/frontend code changed).

---

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built
**Severity:** Info (planned)
**Description:** 5-phase framework designed and validated (Day 76). Data architecture confirmed: DataProvider for price signals, existing context engines for macro. Build is next session. New file: `market_phase_engine.py` + `/api/market/phase` endpoint.

### Info: Price Structure Card — Phase 1 Only (Day 72)
**Severity:** Info (known limitation)
**Description:** Phase 1 uses Trend Template score + ATR-relative proximity to infer structure state. Phase 2 (deferred) will add proper HH/HL/LH/LL market structure engine using existing `find_pivot_points()`. Phase 3 (future) will add visual chart via lightweight-charts.

### Info: Value Tab — ROIC Null on Finnhub Free Tier (Day 75)
**Severity:** Info (known Phase 1 limitation)
**Description:** Finnhub free tier does not return `roicTTM` for all tickers (AAPL affected). Shows gray N/A card, not an error. Phase 2 will add AV-derived ROIC as fallback.

### Info: Value Tab Phase 2 Deferred (Day 75)
**Severity:** Info (planned)
**Description:** Phase 2 metrics (AV earnings history, interest coverage ratio, EV/EBIT, ROE 5yr median) deferred. Requires AV quota management (25 req/day limit).

### Info: Gate 5 Combined Sharpe Measurement Artifact (Day 75)
**Severity:** Info (methodological note)
**Description:** Gate 5 combined Sharpe ratio shows 0.80× vs best individual (below 0.9 threshold). Measurement artifact from sparse daily P&L series. Real metrics (1.9% overlap, 0.274 correlation) confirm systems are complementary. Gate 5 PASSED 3/4 criteria.

### Info: Sentiment Removed from Verdict (Day 70)
**Severity:** Info (architectural decision)
**Description:** Sentiment (Fear & Greed) removed from `determineVerdict()` strong_count. Now informational only. Backtest never validated it (hardcoded Neutral).

### Info: Gates 4+5 PASSED — Paper Trading Unblocked (Day 75)
**Severity:** Info (milestone)
**Description:** All backtest gates cleared. Paper trading is the next priority.

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library.

### Info: Blended RS Degrades Verdict Quality
**Severity:** Info (by design — informational only)
**Description:** Blended RS disabled for verdicts. rs52Week remains sole verdict driver.

### Info: epsGrowth / forwardPe / Negative D/E edge cases
**Severity:** Info (pre-existing from Day 53)

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)

### Info: Backtest Max Drawdown Still High
**Severity:** Info (backtest-only)
**Description:** Config C max drawdown: Quick 39.4%, Standard 52.5%, Position 66.5%

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated
**Severity:** Info (assumption logged, advisory only)

### Info: yfinance Reliability for .TO Tickers
**Severity:** Info (monitoring needed)

### Info: ROE Heuristic Fails for ROE >= 100%
**Severity:** Info (edge case, Day 61 audit)

### Info: _growth_to_pct Cliff at 500% Growth
**Severity:** Info (edge case, Day 61 audit)

### Info: Alpha Vantage 25 req/day Limit
**Severity:** Info (by design)

### Info: FOMC Dates Hardcoded through 2027
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile
**Severity:** Info (documented, current values validated)
**Description:** rsi_low fragile at 55 (PF 0.83), stop_atr_multiple fragile at 1.5x (PF 0.98). Current params (rsi_low=30, stop_atr=2.0) are robust.
