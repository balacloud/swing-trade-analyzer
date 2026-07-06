# Known Issues — Day 77 (May 20, 2026)

## Changes from Day 76
- No bugs resolved this session.
- No new functional bugs introduced (no backend/frontend code changed).
- Added: IBKR screener integration research complete. `/ibkr-scan` skill design ready to build.

---

## Open Issues

### Medium: Canadian Market — Analyze Page Not Yet Supported
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian Market support only works for **Scan Market** tab. Full **Analyze** page needs data source redesign for `.TO` tickers.

### Info: IBKR Filter #8 — 52W High Proximity Availability Unverified
**Severity:** Info (verify before building skill)
**Description:** 3-LLM audit recommends filter #8 as "52W High Proximity -25% to max." IBKR screenshots only showed "52 Week High" as an absolute price value. Need to confirm IBKR has a % proximity ratio field. If unavailable, fallback is Price/EMA(20) > 1.0.

### Info: N4 Market Phase Synthesis — Research Done, Not Yet Built
**Severity:** Info (planned)
**Description:** 5-phase framework designed and validated (Day 76). DataProvider for price signals, existing context engines for macro. Build is next session. New file: `market_phase_engine.py` + `/api/market/phase` endpoint.

### Info: /ibkr-scan Skill — Design Complete, Not Yet Built
**Severity:** Info (planned)
**Description:** Full skill design documented in `docs/research/IBKR_SCREENER_INTEGRATION.md`. Parses IBKR screenshot(s) via Claude vision, calls STA API for each ticker, ranks by verdict+R:R+pattern, outputs top 5–10.

### Info: Price Structure Card — Phase 1 Only (Day 72)
**Severity:** Info (known limitation)
**Description:** Phase 2 (deferred) adds HH/HL/LH/LL engine. Phase 3 adds lightweight-charts visual.

### Info: Value Tab — ROIC Null on Finnhub Free Tier (Day 75)
**Severity:** Info (Phase 1 limitation)
**Description:** Phase 2 will add AV-derived ROIC as fallback.

### Info: Value Tab Phase 2 Deferred (Day 75)
**Severity:** Info (planned)

### Info: Gate 5 Combined Sharpe Measurement Artifact (Day 75)
**Severity:** Info (methodological note)

### Info: Sentiment Removed from Verdict (Day 70)
**Severity:** Info (architectural decision)

### Info: Gates 4+5 PASSED — Paper Trading Unblocked (Day 75)
**Severity:** Info (milestone)

### Low: Defeat Beta Import Still Present
**Severity:** Low (no functional impact)

### Info: Blended RS Degrades Verdict Quality
**Severity:** Info (by design)

### Info: Backtest Max Drawdown Still High
**Severity:** Info (backtest-only)

### Info: ADX >= 25 Momentum Entry Threshold Unvalidated
**Severity:** Info

### Info: FOMC Dates Hardcoded through 2027
**Severity:** Info (maintenance reminder)

### Info: Parameter Stability — rsi_low and stop_atr_multiple Fragile
**Severity:** Info (documented, current values validated)
