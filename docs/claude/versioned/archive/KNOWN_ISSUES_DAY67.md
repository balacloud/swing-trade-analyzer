# Known Issues - Day 67 (March 9, 2026)

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

## Resolved Issues (Day 66 - This Session)

### Resolved: RS Bar Scale Bug (Day 66)
RS bars in SectorRotationTab were all showing max width — values (95–125) mapped to [0.5, 1.5] range instead of correct [85, 130]. Fixed threshold to 100 (not 1.0), momentum threshold to 0.

### Resolved: Rank Badge Color Confusion (Day 66)
Rank badge showed red for #10 Improving sector — conflicting color signals. Fixed: rank badge is now neutral gray (#N is position only; quadrant badge carries color meaning).

### Resolved: Scan Button on Weakening Sectors (Day 66)
Scan buttons appeared on Weakening sectors (rank ≤ 4 included negative-momentum sectors). Fixed to quadrant-based: `Leading || Improving` only.

### Resolved: Port Auto-Kill (Day 66)
Manual `lsof | xargs kill` needed when ports already in use. Fixed: `start.sh` and `stop.sh` now auto-kill ports 5001/3000 via `kill_port()` helper.

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY66.md for full history)

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
| Resolved (Day 66 session) | 4 |
