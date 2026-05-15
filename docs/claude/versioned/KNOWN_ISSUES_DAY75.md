# Known Issues — Day 75 (May 15, 2026)

## Changes from Day 74
- Gate 5 PASSED → updated Gate 4 info entry (removed "Gate 5 pending")
- Added Gate 5 PASSED info entry
- Added Value Tab Phase 1 info entries
- Resolved: dividend yield 36.22% bug (fixed Day 75)

---

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: Price Structure Card — Behavioral Test Pending (Day 72)
**Severity:** Info (needs verification)
**Description:** Phase 1 built and compiles clean. Behavioral test against 5 real tickers (NVDA, SPY, SMCI, AAPL, F) not yet run. Narrative should be verified to match TradingView chart read before paper trading use. **This is the next session's first task.**

### Info: Price Structure Card — Phase 1 Only (Day 72)
**Severity:** Info (known limitation)
**Description:** Phase 1 uses Trend Template score + ATR-relative proximity to infer structure state. Phase 2 (deferred) will add proper HH/HL/LH/LL market structure engine using existing `find_pivot_points()`. Phase 3 (future) will add visual chart via lightweight-charts.
**Deferred items:** Multi-scale swing detection, volume-at-levels, trend age, visual chart.

### Info: Value Tab — ROIC Null on Finnhub Free Tier (Day 75)
**Severity:** Info (known Phase 1 limitation)
**Description:** Finnhub free tier does not return `roicTTM` for all tickers (AAPL affected). Shows gray N/A card, not an error. Quality verdict still computes from ROE alone when ROIC is unavailable. Phase 2 will add AV-derived ROIC as fallback.

### Info: Value Tab Phase 2 Deferred (Day 75)
**Severity:** Info (planned)
**Description:** Phase 2 metrics (AV earnings history, interest coverage ratio, EV/EBIT, ROE 5yr median) deferred. Requires AV quota management (25 req/day limit). Phase 1 (Finnhub + yfinance) is fully functional.

### Info: Gate 5 Combined Sharpe Measurement Artifact (Day 75)
**Severity:** Info (methodological note)
**Description:** Gate 5 combined Sharpe ratio shows 0.80× vs best individual (below 0.9 threshold). This is a measurement artifact from sparse daily P&L exit-day series — individual Sharpes are inflated when exit days are sparse, then deflated when combined. Real metrics (1.9% overlap, 0.274 correlation) both confirm systems are complementary. Gate 5 PASSED 3/4 criteria.

### Info: Gate 5 Momentum Proxy vs Config C (Day 75)
**Severity:** Info (methodological note)
**Description:** Gate 5 used a simplified momentum proxy (no SimFin fundamentals: TT+RSI14+ADX+RS52W only). This proxy shows 52.2% WR, PF 1.34 vs Config C's 53.78% WR, PF 1.61. The gap is expected — Config C's fundamental filter is the source of its extra edge. Gate 5 tested system independence, not momentum system accuracy. Config C remains the authoritative momentum backtest.

### Info: Sentiment Removed from Verdict (Day 70)
**Severity:** Info (architectural decision)
**Description:** Sentiment (Fear & Greed) removed from `determineVerdict()` strong_count. Now informational only. Verdict uses T+F for scoring, R as gate. Reason: backtest hardcoded sentiment='Neutral' — never validated.

### Info: Gates 4+5 PASSED — Paper Trading Unblocked (Day 75)
**Severity:** Info (milestone)
**Description:** Gate 4 (MR standalone: 520 trades, 62.9% WR, PF 1.26) and Gate 5 (combined system: 1.9% overlap, 0.274 P&L correlation) both passed. All backtest gates cleared. Paper trading is the next priority.

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library.

### Info: Blended RS Degrades Verdict Quality
**Severity:** Info (by design — informational only)
**Description:** Blended RS (21d/63d/126d) degrades PF 1.90→1.51. Disabled for verdicts, display only. rs52Week remains sole verdict driver.

### Info: epsGrowth / forwardPe / Negative D/E edge cases
**Severity:** Info (pre-existing from Day 53) — not shown in categorical assessment.

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
