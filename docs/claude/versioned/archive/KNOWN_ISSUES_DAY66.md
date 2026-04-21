# Known Issues - Day 66 (March 6, 2026)

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Low: FMP Free Tier 403 Errors
**Severity:** Low (gracefully handled)
**Description:** FMP returns HTTP 403 for some tickers on free tier
**Impact:** epsGrowth/revenueGrowth may come from yfinance instead of FMP
**Workaround:** Field-level merge fills gaps from yfinance automatically

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
**Mitigation:** Cache TTL is mandatory guard. If limit hit, `_fetch_av_news` returns None → graceful empty state.

### Info: FOMC Dates Hardcoded through 2027
**Severity:** Info (maintenance reminder)
**Description:** `cycles_engine.py` FOMC_DATES list covers 2026-2027 only. Needs update for 2028+.
**Action:** Low priority — can update in 2027.

### Info: F&G Historical Data Divergence
**Severity:** Info (cannot fix)
**Description:** Live verdict uses real-time Fear & Greed; backtest uses static 'Neutral'. Divergence is real but cannot be fixed without a paid historical F&G API.

---

## Resolved Issues (Day 65 - This Session)

*No code changes this session. README hybrid rewrite only.*

---

## Resolved Issues (Day 63-64)

### Resolved: Option C Hybrid News Filter (Day 63)
Reputable source filtering + 3-bucket curation (top 3 bullish/neutral/bearish) in `news_engine.py`.

### Resolved: BottomLineCard Coherence (Day 63-64)
`getEntryTypeLabel()` now uses trade viability as authority. CAUTION='CAUTION ENTRY', NOT_VIABLE='WAIT FOR ENTRY'.

### Resolved: 18 Deep Audit Bugs (Day 64)
VCP strictly decreasing, VCP pivot=last swing high, VCP gate hybrid, Cup&Handle index + handle validation,
W-FRI resample, Wilder EMA ATR, ATR stop + floor, FOMC edge case, constants.py extracted,
All-Decent+Neutral→HOLD, stop price $0.01 floor (FE+BE), unemployment threshold.

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY62.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 2 |
| Open - Info | 16 |
| **Total Open** | **19** |
| Resolved (Day 65 session) | 0 (no code changes) |
