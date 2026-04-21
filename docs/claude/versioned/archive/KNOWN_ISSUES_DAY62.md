# Known Issues - Day 62 (March 1, 2026)

## Open Issues

### Medium: News Articles Unfiltered — Option C Hybrid Pending
**Severity:** Medium (noise in news sentiment column)
**Description:** Alpha Vantage NEWS_SENTIMENT returns articles from all sources including low-quality/random news sites. FinBERT sentiment scoring works correctly but the signal-to-noise ratio is poor.
**Decision:** Keep Alpha Vantage but filter to reputable sources only. Show top 3 bullish + 3 neutral + 3 bearish.
**Reputable sources:** Reuters, Bloomberg, AP, WSJ, FT, Barron's, MarketWatch, CNBC, Yahoo Finance, Morningstar, Seeking Alpha, The Motley Fool.
**Action:** Implement in `backend/news_engine.py` Day 63. Add `REPUTABLE_SOURCES` filter list + sort-and-slice logic.

### Info: Candlestick Patterns — Queued as Standalone Post-Flight Check
**Severity:** Info (planned feature, not yet implemented)
**Description:** Candlestick patterns requested as a standalone post-flight check widget. NOT to be integrated into full analysis, decision matrix, or simple checklist.
**Decision:** Perplexity deep research first → implementation plan → Day 63 implementation.
**Action:** Research prompts written in `docs/research/CANDLESTICK_PATTERNS_PERPLEXITY_PROMPTS.md`. Run research, then implement.

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

---

## Resolved Issues (Day 62 - This Session)

### Resolved: FRED_API_KEY Configured
**Was:** Medium (FRED data unavailable — all 6 cycle + 4 econ cards showed "FRED data unavailable").
**Resolution:** User added `FRED_API_KEY=461030cd9da7e2ccb3b1838435ca93e7` to `backend/.env`. Backend restarted. Stale CYCLES/ECON_INDICATORS cache cleared via SQLite DELETE. All 10 FRED-powered cards now live.

### Resolved: Sector Filter Zero Results Bug
**Was:** Scan tab showed "41 of 277 matches" but zero rows rendered when sector filter active.
**Root cause:** (1) Count used raw scan count, not filtered count. (2) TradingView SIC sector names ("Non-Energy Minerals") didn't match GICS names ("Materials") used in `SECTOR_ETF_MAP`.
**Resolution:** Extended `SECTOR_ETF_MAP.gics` arrays with TradingView SIC names (49 entries total). Changed filter to `getSectorContext(s.sector)?.etf === sectorFilter.etf`. Fixed count to show filtered count.

### Resolved: Sector Rotation Phase 2 (Context Feature)
Added dedicated 🔄 Sectors tab with 11 sector cards, quadrant color-coding, "Scan for Rank 1" filter.

### Resolved: Context Tab (Full Feature — Additive Only)
Added 🔭 Context tab: Calendar/Yield Cycles (Column A) + Economic Indicators (Column B) + News Sentiment (Column C).
Backend: 3 new engine files + 4 new endpoints. Frontend: 5 new components + ContextTab.

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY61.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 2 |
| Open - Low | 2 |
| Open - Info | 15 |
| **Total Open** | **19** |
| Resolved (Day 62 session) | 4 (2 features shipped + FRED key + sector filter bug) |
