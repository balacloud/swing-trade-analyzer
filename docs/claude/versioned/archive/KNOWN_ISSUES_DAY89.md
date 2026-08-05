# Known Issues — Day 89 (July 16, 2026)

## Changes from Day 88

**Shipped this session (scoped freeze exception, continuing Day 88's theme):**
- ✅ MR arm's automated live universe widened from a static 54-ticker list to a dynamic ~150-ticker TradingView liquid scan — measured to yield 8 signals in one clean run vs. the historical 0-2/day.
- ✅ Momentum's raw-candidate scan limit raised 50→150 (tested clean, limited real-world impact — see below).
- ✅ Fixed a real scaling bug found via live testing: an initial limit=300 attempt tripped TwelveData's rate limiter, cascading to yfinance/Tradier, silently failing ~35% of tickers (always the same tail-end names, due to deterministic market-cap-descending sort). Recalibrated to limit=150.
- ✅ Confirmed both Tradier and TwelveData are genuinely functional (not just configured) — direct provider tests returned real, current data; both circuit breakers self-healed as designed once real calls succeeded after cooldown.

**Freeze status:** unchanged — still in complete feature freeze. Scoped as the same kind of exception as Day 88 (directly aids the paper-trading gate's sample-accumulation rate), not general product work.

---

## Open Issues

Carried forward unchanged from `KNOWN_ISSUES_DAY88.md` — no new bugs in the reviewed system, no trading-logic/threshold changes. See that file for the full list.

### Info: MR Universe Widened, Rate-Limit Ceiling Found and Calibrated Around (Day 89)
**Severity:** Info (milestone + documented constraint)
**Description:** The live MR scan's default candidate-pool size (150) is a measured ceiling against the current shared provider rate limits (TwelveData's being the binding constraint), not an arbitrary choice. If the app's overall API usage pattern changes materially (e.g., much higher concurrent traffic elsewhere), this ceiling may need re-measuring — a bigger number isn't free even though the code would accept it without complaint.
**Fix:** None needed now. Re-verify if MR signal counts unexpectedly drop or provider circuit breakers start tripping during the scheduled daily run (visible via the Forward Test tab's status panel or backend logs).

### Info: Momentum Scan Limit Increase Has Limited Practical Effect (Day 89)
**Severity:** Info (expectation-setting)
**Description:** Raising momentum's raw-candidate limit from 50 to 150 was tested live and found only 5 stocks market-wide met Config C's pre-filter criteria that day — confirming momentum signal rarity is a property of market conditions and the strategy's own selectivity, not the scan limit. Don't expect this change alone to meaningfully increase momentum's signal rate on a typical day.
