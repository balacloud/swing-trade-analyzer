# Known Issues — Day 91 (July 19, 2026)

## Changes from Day 90

**Resolved this session (Session 28 audit's top-4 findings):**
- Scan tab's "Minervini SEPA/Stage 2 uptrend" mislabel (only checked 2 of 8 real Trend Template criteria) — renamed to "Large-Cap Momentum Filter".
- Sectors tab's false "RS Ratio 100 = market parity" claim + wrong "Data from TwelveData" label (actual source: yfinance) — both corrected.
- Context tab's CPI card showing stale-looking values — root-caused to a real date-alignment bug (`_yoy()`'s fixed-list-index lookback silently misaligned by a withheld FRED observation), not a caching issue. Fixed; now shows the correct 3.5%/2.6%.
- Context tab's "ISM PMI (proxy)" card implicitly compared against real-PMI historical stats — relabeled to "Manufacturing Employment (PMI proxy)" with honest source/history text.
- Paper-trading's daily replay recomputed stop/target fresh each day instead of reading back the values locked in at entry — fixed to anchor to stored ledger values. Caught and prevented a live instance of exactly this drift (KRYS) during verification.

**Added this session:** none — no new bugs found; today's changes were all fixes.

**Freeze status:** unchanged — still in complete feature freeze. All changes above are bug fixes to existing systems, fitting the freeze's "bug fixes only" carve-out.

---

## Open Issues

### Medium: Backtest↔Live Fundamentals Data-Source Mismatch (carried from Day 78/79)
**Severity:** Medium
**Description:** 40.0% disagreement rate between live (Finnhub/AlphaVantage/yfinance TTM) and backtested (SimFin quarterly) Fundamental labels, measured on 20 liquid tickers. Revenue growth is the dominant driver. Also relevant to the automated paper-trading engine's momentum leg.
**Fix:** Mitigation choice still a pending user decision.

### Medium: Canadian Market — Analyze Page Not Yet Supported (carried from Day 59)
**Severity:** Medium (incomplete feature)
**Description:** v4.21 Canadian support only works for Scan tab. Analyze page needs data source redesign for `.TO` tickers.

### Low / Info: Session 28 audit's remaining lower-priority findings (new, Day 91)
**Severity:** Low
**Description:** Only the audit's 4 top-priority findings were fixed this session (user's explicit scope choice). Remaining, from `HANDOFF_sta_audit_session28.md`:
- Value tab's ROE thresholds badged "Buffett/Damodaran" in the UI, but the code comment for their actual origin says "ChatGPT research validated" — not those named sources.
- Validate/Data Sources tabs show "live"/"healthy" status labels without actually probing real fetch success; missing/never-fetched data renders identically to genuinely fresh data.
- Sectors tab's "Scan Rank #1" CTA bypasses the same Leading/Improving-only gate every per-sector button respects; RS Ratio precision is `.toFixed(3)` (false precision on an approximate number); no staleness visual weight past ~1 trading day.
- Forward Testing's momentum-path trades store identical net/gross P&L (fee accounting not actually differentiated for that path); per-position fetch failures are silently dropped rather than logged.
- General polish items: Sectors transparency block (source/lookback/smoothing disclosure), Context tab's composite-score recalculation once CPI/PMI are corrected (now done — worth re-checking the composite label reflects it), softened wording on a few cards, backtest-stat methodology disclosure.
**Fix:** Tracked as ROADMAP.md priority #10 — batchable whenever a future session picks it up. Not urgent; no trading-decision impact per the audit's own assessment.

### Low / Info items (carried forward, unchanged)
SimFin key rotation unconfirmed, Defeat Beta import present, Scan tab breakout badge NOT_READY vs failed-fetch ambiguity, Master Framework/Nirmal watchlist Name/Market Cap N/A by choice, README.md version footer stale (Day 65/v2.33 — pre-existing, low-priority, noted but not fixed this session beyond the one directly-affected `/api/scan/strategies` example line). See `KNOWN_ISSUES_DAY87.md` for full text of the pre-existing items.
