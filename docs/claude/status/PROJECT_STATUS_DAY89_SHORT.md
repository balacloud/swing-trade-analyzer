# Project Status — Day 89 (July 16, 2026)

## Version: v4.47 (Backend v2.43, Frontend v4.42 unchanged, Backtest v4.19, API Service v2.11)

---

## What Happened Today

Continuation of the same calendar session as Day 88's close. User asked how the automated paper-trading engine works and how to get at least 10 tickers/day of signal throughput to accumulate the 50-trade confirmation bar faster.

### 1. Explained the mechanics, then the honest constraint
Momentum already scans market-wide (TradingView pre-filter → full categorical assessment on survivors); MR only checked a **static, hardcoded 54-ticker list**. Explained the one legitimate lever — widen the *candidate pool*, not the frozen entry/exit thresholds (re-tuning thresholds to manufacture more signals would invalidate the whole point of the paper-trading test, per Golden Rule 18). User confirmed this approach.

### 2. Built and live-tested — found and fixed a real scaling bug
- New `scan_queries.build_mr_universe_query()` — dynamic TradingView scan of liquid US stocks, replacing the static list for the automated engine only (the manual `/api/mr/scan` UI endpoint still uses the static list, untouched). Momentum's raw-candidate limit also raised 50→150 (tested clean, but market conditions on the test day only had 5 qualifying raw candidates — confirms momentum's rarity is a market-condition property, not a limit issue).
- **First live test at limit=300 found a real bug**: TwelveData's rate limiter tripped partway through, opening its circuit breaker, cascading to yfinance and Tradier too — ~35% of ~231 tickers failed on every provider, not for lack of a signal. Because the query sorts by `market_cap_basic` descending, this would have silently and permanently excluded the same tail-end tickers every single day. **New Golden Rule 25.**
- Recalibrated to **limit=150** — the number that completed cleanly in the live test.
- **Re-verified at the new limit**: 8 real MR signals found in one clean run (~135s, zero rate-limit failures) — vs. the historical 0-2/day baseline.
- **Directly answered a user question about Tradier's real functionality** (skepticism from seeing "Circuit breaker OPEN" in logs): tested `TradierProvider` directly, bypassing the app's circuit-breaker wrapper — confirmed genuine, working connectivity (real AAPL quote $329.84, 64 real daily OHLCV bars, both dated/matching today). Also confirmed TwelveData genuinely works. Both breakers were legitimately open from the stress test, not broken — watched both self-heal live (OPEN → HALF_OPEN → CLOSED) once real calls succeeded after the cooldown.
- Logged in `PAPER_TRADING_PREREGISTRATION.md`'s change log as a breadth change, not a re-tune — Sections 1-9's actual frozen thresholds are untouched.

---

## Files Changed

| File | Type | Content |
|------|------|---------|
| `backend/scan_queries.py` | Modified | New `build_mr_universe_query()` (default limit=150, calibrated from a live rate-limit test) |
| `backend/paper_trading/live_signals.py` | Modified | New `_get_dynamic_mr_universe()` (with fallback to the static list); `get_mr_signals()` uses it by default; `get_momentum_signals()` default limit 50→150 |
| `backend/backend.py` | Modified | Updated stale comment near `/api/mr/scan` (Day 88's dynamic-universe change hadn't touched this manual endpoint — clarified why); `BACKEND_VERSION` → 2.43 |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | Modified | Change log entry — breadth widening, not a threshold re-tune |
| `docs/claude/stable/GOLDEN_RULES.md` | Modified | New Golden Rule 25 (rate-limit-aware batch scaling + deterministic-sort data-gap lesson) |

---

## All Gates Status

Unchanged from Day 88 — no trading-logic or threshold changes, only candidate-pool breadth for the MR arm and momentum's scan limit. See `PROJECT_STATUS_DAY88_SHORT.md` for the full gates table.

**Feature freeze status:** still in effect. Like Day 88's ledger-UI work, this was scoped as directly aiding the paper-trading gate (faster sample accumulation), not general product work.

---

## Next Session Priorities

Unchanged from Day 88 (see `PROJECT_STATUS_DAY88_SHORT.md`) — this session was entirely about the paper-trading engine's sample rate, not new backlog items:

1. **Let paper trading accumulate** — now at a meaningfully faster rate for the MR arm. Check via the Forward Test tab's status panel or `daily_job.py --report`.
2. **Decide fundamentals mitigation** — 40% live↔backtest disagreement, still pending.
3. **Confirm SimFin key rotation.**
4. **N3 gap-fill detection** / **Value Tab Phase 2** — both still need their own design sessions first.
5. `/ibkr-scan` skill, Price Structure Phase 3, Canadian Analyze page — queued.
6. **(New, low priority)** Consider whether the MR universe scan needs periodic re-verification against provider rate limits if the app's overall API usage pattern changes (e.g., more concurrent users) — the limit=150 calibration reflects today's measured throughput, not a permanent ceiling.
