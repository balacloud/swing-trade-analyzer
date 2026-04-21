# Known Issues - Day 68 (March 16, 2026)

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
**Mitigation:** Cache TTL is mandatory guard. If limit hit, `_fetch_av_news` returns None → graceful empty state.

### Info: FOMC Dates Hardcoded through 2027
**Severity:** Info (maintenance reminder)
**Description:** `cycles_engine.py` FOMC_DATES list covers 2026-2027 only. Needs update for 2028+.
**Action:** Low priority — can update in 2027.

### Info: F&G Historical Data Divergence
**Severity:** Info (cannot fix)
**Description:** Live verdict uses real-time Fear & Greed; backtest uses static 'Neutral'. Divergence is real but cannot be fixed without a paid historical F&G API.

---

## Resolved Issues (Day 67 — This Session)

### Resolved: FMP v3 Permanently Dead — All References Updated
FMP v3 API deprecated August 31, 2025. Returns 403 "Legacy Endpoint" for all tickers. AlphaVantage already in `.env` (key: `ALPHAVANTAGE_API_KEY`) fully replaces FMP's role (revenue growth, EPS growth). All 8 user-facing/inline references updated from "FMP" to "AlphaVantage" across App.jsx, scoringEngine.js, api.js, backend.py (×2), orchestrator.py.
_Previously tracked as: "Low: FMP Free Tier 403 Errors"_

### Resolved: "Analyze a stock first" Provenance Placeholder Not Clearing
Root cause: `analysisResult?.stock?.ticker` path doesn't exist. `calculateScore()` returns a flat object `{ ticker, name, ... }` at top level — no nested `stock` object. Fixed both the `useEffect` dependency and tab click handler to use `analysisResult?.ticker`.

### Resolved: TwelveData Not Showing ACTIVE in Market Data Row
Market Data row serves two independent sub-types: TwelveData handles SPY OHLCV, yfinance handles VIX quote. Single `activeKey` couldn't capture both simultaneously. Fixed with `providerActiveKey` per-provider override: TwelveData uses `'ohlcv'`, yfinance uses `'quote'`. Both now show ACTIVE simultaneously.

### Resolved: "circuit open — skipped" on ACTIVE Providers
A provider can't logically be both ACTIVE and circuit-open. Added `!isActive` guard: circuit-open badge only renders when `health === 'open' && !isActive`.

### Resolved: OHLCV / Fundamentals Source Hardcoded 'yfinance' in Provenance
Provenance endpoint always returned `'source': 'yfinance'` regardless of actual provider. Fixed to read `ohlcv_cache.get('source', 'unknown')` and `fund_cache.get('source', 'unknown')` — real source from cache metadata.

### Resolved: Negative age_hours (-0.9h) in Provenance
Root cause: `expires_at` stored as timezone-aware ISO string; `cached_at` stored as naive local time. `.replace(tzinfo=ET)` reinterpreted naive local time as ET (wrong offset → negative delta). Fixed: `_naive()` helper strips tzinfo from both datetimes; `datetime.now()` (naive local) used for comparison. All 3 timestamps consistently naive.

### Resolved: "0" Rendered as Bare Text in Fundamentals Provenance Card
React `{age_days && <div>...</div>}` with `age_days=0` evaluates `0 && (...)` = `0` → React renders literal "0" as text. Fixed all 4 conditional renders to use `age_days != null && age_days > 0` pattern.

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY67.md for full history)

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
| Resolved (Day 67 session) | 7 |
