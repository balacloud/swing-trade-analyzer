# Known Issues - Day 57 (February 22, 2026)

## Open Issues

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

### Info: Simple Checklist Missing 5 Minervini Criteria
**Severity:** Info (enhancement, not bug)
**Description:** Simple Checklist has 4 criteria but lacks 52-week range, volume, ADX, market regime, ATR stops
**Action:** Enhance next session — backtest now validates what criteria matter

### Medium: EPS/Revenue Growth Using QoQ Instead of YoY
**Severity:** Medium (incorrect methodology)
**Description:** `yfinance_provider.py` calculates revenueGrowth QoQ instead of YoY
**Action:** Fix after backtest — methodology decision needed

### Info: Fear & Greed Index — Questionable Value
**Severity:** Info (architectural consideration)

### Info: Backtest Max Drawdown Still High
**Severity:** Info (backtest-only, not production)
**Description:** Config C max drawdown by period: Quick 39.4%, Standard 52.5%, Position 66.5%
**Context:** Per-trade sequential drawdown across all trades without portfolio-level position sizing
**Note:** Quick period has most reasonable drawdown; Position is regime-sensitive (mostly bear-period losses)
**Action:** User handling position sizing separately

### Info: Position Period Regime-Sensitive
**Severity:** Info (backtest finding)
**Description:** Position holding period (15-45d) has low WR (38.67%) but high avg winners (8.05%). Walk-forward showed IS profit factor of only 1.14 vs OOS 1.53 — highly dependent on market regime.
**Action:** Consider adding UI warning when selecting Position period outside bull regime

### Info: API_CONTRACTS_DAY53.md Outdated
**Severity:** Info (documentation)
**Description:** API contracts doc is 4 days behind. Missing: `sma50Declining` in SPY endpoint, `market_index` param in scan, version v2.20
**Action:** Update at next session that changes APIs

---

## Resolved Issues (Day 57 - This Session)

### Resolved: Backend SPY Missing sma50Declining ✅
**Fixed in:** Day 57
**Description:** Backend `/api/market/spy` didn't return `sma50Declining` field. Backtest used it for bear regime detection but production frontend couldn't.
**Fix:** Added sma50Declining calculation mirroring `trade_simulator.is_spy_50sma_declining()`

### Resolved: Frontend assessRiskMacro() Missing Bear Regime Check ✅
**Fixed in:** Day 57
**Description:** Frontend `assessRiskMacro()` didn't check `sma50Declining`. Backtest `categorical_engine.py` did — coherence gap.
**Fix:** Added early bear regime check — caps assessment at "Neutral" when SPY 50 SMA declining

### Resolved: api.js Dropping sma50Declining Field ✅
**Fixed in:** Day 57
**Description:** `fetchSPYData()` returned a subset of backend fields but didn't include `sma50Declining`
**Fix:** Added `sma50Declining: data.sma50Declining || false` to return object

### Resolved: yfinance 0.2.28 Completely Broken ✅
**Fixed in:** Day 57
**Description:** yfinance 0.2.28 incompatible with current Yahoo Finance API. All downloads returned 0 rows.
**Fix:** Upgraded to yfinance 1.2.0. MultiIndex columns already handled by backtest code.

### Resolved: Bear Regime Never Actually Backtested ✅
**Fixed in:** Day 57
**Description:** All prior backtests (Feb 17-18) ran BEFORE bear regime code was committed (Feb 19). Bear regime had never been validated.
**Fix:** Re-ran backtest with bear regime. Confirmed: removes 2 bad bear trades, improves bear WR from 55.6% → 71.4%.

---

## Resolved Issues (Prior Sessions)
(See KNOWN_ISSUES_DAY56.md for full history)

---

## Issue Statistics
| Category | Count |
|----------|-------|
| Open - Critical | 0 |
| Open - High | 0 |
| Open - Medium | 1 |
| Open - Low | 2 |
| Open - Info | 7 |
| **Total Open** | **10** |
| Resolved (Day 57 session) | 5 |
