# Known Issues - Day 70 (March 19, 2026)

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: Sentiment Removed from Verdict (Day 70)
**Severity:** Info (architectural decision)
**Description:** Sentiment (Fear & Greed) removed from `determineVerdict()` strong_count. Now informational only. Verdict uses T+F for scoring, R as gate. Reason: backtest hardcoded sentiment='Neutral' — never validated. Removing aligns live with backtest.

### Info: Simplicity Premium UI — Progressive Disclosure (Day 70)
**Severity:** Info (UI improvement)
**Description:** Full analysis view reorganized into 3 tiers. Decision Matrix view and TradingView Chart removed. Tier 1 (always visible): Verdict, Trade Setup, Bottom Line, MR Signal, Quality Gates. Tier 2 (collapsed by default): Holding Period, Price & RS, Pattern Detection, Categorical Assessment. Tier 3 (hidden until requested): Technical Indicators. Sentiment card labeled "(info)" with reduced opacity.

### Info: Simple Checklist — Cap-Aware Thresholds + RS Tightened (Day 70)
**Severity:** Info (data-driven improvement)
**Description:** Three cap-aware improvements: (1) Volume threshold: $2M (small <$2B), $5M (mid $2-10B), $10M (large >$10B). Old flat $10M was MISLEADING per multi-LLM audit. (2) RS threshold tightened from 1.0 to 1.2 — backtest: PF 1.56→1.78, WR 49.7%→52.6%. RS 1.0 was MISLEADING per 2/2 LLMs (too permissive for Minervini/O'Neil). (3) Stop distance cap-aware: 7% large / 9% mid / 10% small. ATR analysis across 30 stocks showed 7% = only 1.4x ATR for small caps (below 2x noise minimum). Mid caps avg 4.4% ATR (7% = 1.6x, also too tight).

### Info: Gate 4 MR Standalone Backtest — PASSED
**Severity:** Info (validated)
**Description:** 520 trades across 20 tickers, 5yr. WR=62.9%, PF=1.26, avg hold=4.1 days. 73% exit via RSI(2)>70, 24% stop, 3% time. Gate 5 (combined system) still pending.

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library

### ~~Resolved: README Audit Fixes~~ (Day 71)
FMP → AlphaVantage throughout, version numbers updated (v4.32/v2.33/v2.10), Fundamental Strong description corrected (2+ of 3 metrics), 200 EMA → 200 SMA, verdict logic reflects Day 70 sentiment change, Decision Matrix → progressive disclosure, changelog extended through v4.32.

### Info: Blended RS Degrades Verdict Quality
**Severity:** Info (by design — informational only)
**Description:** Backtest showed blended RS (21d/63d/126d) degrades PF 1.90->1.51, Sharpe 1.17->0.68. Intentionally disabled for verdicts, kept as display-only. rs52Week remains sole verdict driver.

### Info: epsGrowth Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: forwardPe Not Shown in Categorical Assessment
**Severity:** Info (pre-existing from Day 53)

### Info: Negative D/E Edge Case in Scoring
**Severity:** Info (pre-existing from Day 53)

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)

### Info: Backtest Max Drawdown Still High
**Severity:** Info (backtest-only, not production)
**Description:** Config C max drawdown by period: Quick 39.4%, Standard 52.5%, Position 66.5%

### Info: Position Period Regime-Sensitive
**Severity:** Info (backtest finding)

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated
**Severity:** Info (assumption logged, advisory only)

### Info: yfinance Reliability for .TO Tickers
**Severity:** Info (monitoring needed)

### Info: ROE Heuristic Fails for ROE >= 100%
**Severity:** Info (edge case, found Day 61 audit)

### Info: _growth_to_pct Cliff at 500% Growth
**Severity:** Info (edge case, found Day 61 audit)

### Info: Dual Entry Cards R:R Still Inline
**Severity:** Info (accepted, Day 61)

### Info: 11 Unused Backend Fields in S&R Response
**Severity:** Info (found Day 61 audit)

### Info: Fundamentals Scorer Generates Verdict When All Data is Null
**Severity:** Info (found Day 61 audit Layer 4)

### Info: Alpha Vantage 25 req/day Limit
**Severity:** Info (by design)
**Description:** Context Tab Column C (news) uses Alpha Vantage free tier (25 req/day). 4h cache TTL means each unique ticker uses 1 request per 4h window.

### Info: FOMC Dates Hardcoded through 2027
**Severity:** Info (maintenance reminder)
**Description:** `cycles_engine.py` FOMC_DATES list covers 2026-2027 only. Needs update for 2028+.

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile
**Severity:** Info (documented, current values validated as optimal)
**Description:** rsi_low fragile at 55 (PF 0.83), stop_atr_multiple fragile at 1.5x (PF 0.98). Current parameters (rsi_low=30, stop_atr=2.0) are robust.
