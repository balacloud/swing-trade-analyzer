# Known Issues — Day 72 (March 31, 2026)

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: Price Structure Card — Phase 1 Only (Day 72)
**Severity:** Info (known limitation)
**Description:** Phase 1 uses Trend Template score + ATR-relative proximity to infer structure state. Phase 2 (deferred) will add proper HH/HL/LH/LL market structure engine using existing `find_pivot_points()`. Phase 3 (future) will add visual chart via lightweight-charts.
**Deferred items:** Multi-scale swing detection, volume-at-levels, trend age, visual chart.

### Info: Price Structure — Behavioral Test Pending (Day 72)
**Severity:** Info (needs verification)
**Description:** Phase 1 built and compiles clean. Behavioral test against 5 real tickers (NVDA, SPY, SMCI, AAPL, F) not yet run. Narrative should be verified to match TradingView chart read before paper trading use.

### Info: Sentiment Removed from Verdict (Day 70)
**Severity:** Info (architectural decision)
**Description:** Sentiment (Fear & Greed) removed from `determineVerdict()` strong_count. Now informational only. Verdict uses T+F for scoring, R as gate. Reason: backtest hardcoded sentiment='Neutral' — never validated.

### Info: Gate 4 MR Standalone Backtest — PASSED
**Severity:** Info (validated)
**Description:** 520 trades across 20 tickers, 5yr. WR=62.9%, PF=1.26, avg hold=4.1 days. Gate 5 (combined system) still pending.

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
