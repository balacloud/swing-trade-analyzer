# Data Provenance Findings — Day 111

> **Scope:** A full data-source audit — every tab mapped to its actual external
>            data source(s), fallback chains, field-level provenance, and what's
>            computed locally. Triggered by a direct question about which sources
>            the app actually relies on. **Zero application code changed** — this
>            is a findings doc; fixes below are planned, not executed.
> **Companion:** See the published visual artifact (this session) for the full
>            per-tab field-level breakdown. This doc covers the *findings and
>            fix plans* that came out of building it.
> **Freeze status:** Some of these findings are pure infrastructure (freeze-
>            independent, same category as prior audits). One is explicitly
>            **not** — see Finding 3.

---

## Finding 1 — Two batch endpoints bypass the orchestrator's circuit-breaker protection

**Severity:** Medium
**Where:** `GET /api/sectors/rotation` (`backend.py:2360`, direct `yf.download()`
for 11 sectors + SPY/QQQ/MDY/IWM in one batch call) and Market Phase's
sector-leadership breadth check (`market_phase_engine.py:93`, a second direct
`yf.download()`, informational-only per its own docstring).

**Why the obvious fix is wrong:** swapping either into a per-ticker
`dp.get_ohlcv()` loop would mean 15 separate calls each trying TwelveData first
at its 8/min limit — the exact scenario Golden Rule 25 already documented
tripping the circuit breaker (Day 89, a 300-ticker scan cascaded TwelveData's
rate limit into yfinance and Tradier too).

**Fix (planned):** keep the batch `yf.download()` call — it's the right shape
for 15 tickers in one request — but register its failures against the shared
`provider_state.db` circuit-breaker/rate-limiter state so an outage here is
tracked like every other provider call, instead of invisible. Don't force a
15x rate-limit hit these endpoints don't need to take.

---

## Finding 2 — `/api/mr/scan` bypasses the orchestrator for no good reason

**Severity:** Low-Medium — **FIXED Day 111**
**Where:** `backend.py:3525-3534`, direct `yf.Ticker(ticker).history()` inside
a per-ticker scan loop — genuinely inconsistent with its own sibling endpoint,
`/api/mr/signal` (`backend.py:3479`), which correctly uses `dp.get_ohlcv()`.

**Fix:** swapped to `dp.get_ohlcv()` (orchestrator-first, yfinance-fallback,
matching the sibling endpoint's Day-82 fix exactly). Done in the same session
this was found, prompted by wiring `fetchMRScan()` to a real UI button for the
first time (see Priority note below) — the inconsistency stopped being a
theoretical gap the moment it got real traffic. Verified live: 54-ticker scan
completes in ~20s, 7 real signals returned (TXN, NVDA, INTC, BAC, RTX, LMT,
JPM), no errors.

---

## Finding 3 — Tradier's fallback position is defensible for Analyze, but leaves real capacity unused elsewhere

**Severity:** Info / strategic, not a bug
**The defensible part:** Tradier's OHLCV is split- but not dividend-adjusted
(`tradier_provider.py:21-23`) — a real accuracy concern for single-ticker
analysis on dividend payers. Keeping it 3rd-tier behind TwelveData/yfinance
for the Analyze page has a legitimate reason.

**The mismatch worth fixing:** Tradier's rate limit is 100/min
(`rate_limiter.py:202-204`) against TwelveData's 8/min — 12x the headroom,
sitting almost entirely idle, in exactly the wide-batch-scan scenario
(Golden Rule 25) that has actually caused a real incident before. Two
concrete, additive fixes:
1. Add Tradier as a fallback to the two orphaned endpoints in Finding 1 —
   they currently have **zero** Tradier coverage at all, not "low priority"
   Tradier coverage. Purely additive, doesn't touch any existing live path.
2. Consider Tradier absorbing some batch volume during wide multi-ticker
   scans specifically (MR universe scans, Sector Rotation) where TwelveData's
   ceiling is the documented bottleneck — **not** a blanket chain reorder.

**⚠️ Explicitly NOT freeze-independent if implemented as a chain reorder:**
any change to the actual OHLCV fallback *order* touches data the live
forward-test tracks read through `support_resistance.py`. That's the same
category of change as editing the S&R engine directly — needs the same
freeze-safety review, not a casual infra tweak. Finding 3.1 (adding Tradier
to the two currently-orphaned endpoints) does NOT have this constraint, since
neither endpoint feeds any live forward-test track.

**Bigger strategic thread, flagged not asserted:** the IBKR paper-execution
plan (`docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md`, Day 96) is parked
pending CIRO research, specifically to get real broker-side order execution.
Tradier is a real, already-integrated, already-credentialed brokerage. Nobody
has checked whether Tradier's own API tier supports order placement — if it
does, that's meaningfully less net-new integration work than building IBKR
from scratch. **Not verified — worth a direct check before more IBKR research
effort goes in, not a claim that Tradier definitely can do this.**

---

## Finding 4 — Data Sources tab's own field-source documentation is stale

**Severity:** Low
**Where:** `GET /api/provenance/<ticker>`'s static `data_sources` block
(`backend.py:922-934`) still lists `fundamentals_primary: 'Defeat Beta API'`
— a provider no longer in any active chain — and never mentions Tradier at
all, despite Tradier being a real, tested, active 3rd-tier fallback.

**Fix (planned):** update the static block to reflect the real chains
(Finnhub→AlphaVantage→yfinance for fundamentals; TwelveData→yfinance→Tradier
for OHLCV). The one tab whose entire job is transparency about data sourcing
is itself the thing currently misleading about it.

---

## Finding 5 — Dead code accumulating around fundamentals/config, consolidated list

Pulled together from this session's audits, not new discoveries:

| Item | What it is | Fix |
|---|---|---|
| `mtf_daily_weight`/`mtf_weekly_weight` (`support_resistance.py:70-71`) | Declared config implying real daily/weekly weighting; never referenced anywhere | Wire up for real, or delete |
| `generateScoreExplanation()` + `getSubScoreInfo()` (`App.jsx:1032-1091`) | Dead, orphaned legacy fundamentals-score display code, incl. an unused Forward P/E label | Delete, or reconnect deliberately — currently a landmine (see `ANALYZE_PAGE_REDESIGN_DECISIONS.md` §9) |
| `generateActionableRecommendation()` (`App.jsx:880-1028`) | Dead imperative-banner code, flagged Day 109, not yet deleted | Delete |
| FMP's `get_provider_status()` hardcoded quota (`orchestrator.py:505-511`) | Reports unlimited instead of the real 250/day, on a provider intentionally kept parked for a future paid tier | Fix the bug regardless of whether FMP itself stays parked |

---

## Status

**Finding 2 — DONE (Day 111).** Fixed as part of wiring the MR scanner to a
real Scan-tab button (the actual UI feature request that prompted revisiting
this doc) — see `frontend/src/App.jsx` (`runMrScan`, `mrScanResults` state,
results UI) and `frontend/src/services/api.js` (`fetchMRScan`, pre-existing,
now finally called). Live-verified in browser: button → 54-ticker scan (~20s)
→ 7 real signals rendered → click-through to Full Analysis, all working.

**Findings 1, 3, 4, 5 — still not actioned.** Informal priority unchanged:
Finding 4 (trivial) → Finding 5 (small, batchable) → Finding 1 (needs the
circuit-breaker wiring done carefully) → Finding 3.1 (additive, safe) → Finding
3's chain-reorder question (needs a freeze-safety review first, if ever raised).
