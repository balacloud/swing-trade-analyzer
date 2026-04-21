# Known Issues - Day 69 (March 18, 2026)

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)
**Description:** `backend/backend.py` still imports defeatbeta library

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

### Info: F&G Historical Data Divergence
**Severity:** Info (cannot fix)
**Description:** Live verdict uses real-time Fear & Greed; backtest uses static 'Neutral'. Divergence is real but cannot be fixed without a paid historical F&G API.

---

## Pending Bug Fixes — Universal Principles Audit (Day 69)

These 7 items were identified by the 3-LLM system audit (Day 68) and prioritized in the 4-LLM universal principles synthesis (Day 69). They should be fixed BEFORE any Tier 1+ evolution changes.

| # | Issue | File | Severity |
|---|-------|------|----------|
| 0A | "3.2x" hallucinated MTF claim in docs | docs/*.md | High (misinformation) |
| 0B | VCP missing volume dry-up check | pattern_detection.py | High (false positives) |
| 0C | TT uses 25% above 52w low (should be 30%) | pattern_detection.py | Medium |
| 0D | RS≥1.0 may be too permissive (test 1.1, 1.2) | categorical_engine.py, categoricalAssessment.js | Medium |
| 0E-F | RRG normalization + momentum center (0 vs 100) | sector rotation backend | Medium |
| 0G | F&G neutral zone 35-60 may be too wide | categorical_engine.py, categoricalAssessment.js | Medium |

---

## Resolved Issues (Day 67 Session)
(See KNOWN_ISSUES_DAY68.md for details — 7 issues resolved)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 1 |
| Open - Info | 16 |
| **Total Open** | **18** |
| Pending Bug Fixes (Tier 0) | 7 |
