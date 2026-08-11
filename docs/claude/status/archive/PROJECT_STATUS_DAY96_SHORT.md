# Project Status — Day 96 (July 24, 2026)

## Version: v4.52 (Backend v2.45, Frontend v4.47, Backtest v4.19, API Service v2.11)

---

## What Happened Today

An unusually large single-day session (still calendar-dated July 24, 2026 — Day 95 rolled into Day 96 at close, not a new calendar day). Started as paper-trading monitoring, expanded into a full TradingView-screener deep dive, a data-provider reliability overhaul, and a new parallel forward-test experiment.

### 1. Paper-trading launchd schedule timezone fix
Machine's actual timezone is Eastern (America/Toronto), not Central as the plist assumed — job was firing at 4:30pm ET instead of 4:30pm CT, cutting the intended ~90-min post-close data-settling buffer to ~30 min. Fixed: schedule shifted to 17:30 ET, comment corrected, launchd reloaded. New Golden Rule 33.

### 2. Deep dive: how TradingView screener criteria actually drive Momentum/MR scans
Traced the full pipeline (`scan_queries.py` → `live_signals.py` → verdict engine) end to end. Found and measured a real structural finding: momentum's live R:R gate (`compute_entry_levels()`, flat+8%/ATR-clamped-stop) rejected 81% of Config-C-qualifying candidates, 45% hitting an exact 0.80 ceiling. Also measured that momentum's candidate-pool limit had almost no headroom (160 total matches vs. MR's 3,427).

### 3. Persona + Golden Rule 34: a trading-judgment lens
Built `docs/claude/stable/PERSONA.md` — a 30-year veteran trader persona (first-principles discipline, market "don'ts," behavioral-finance pitfalls each grounded in a real project moment) — wired into `/sta-start` (loaded each session) and `/sta-end` (Feedback Log updated at close). New Golden Rule 34.

### 4. Data-provider circuit-breaker fix (systemic, all 6 providers)
Investigating why Tradier "didn't help" during a forward-test run found every provider's circuit breaker miscounted ticker-specific `DataNotFoundError`/`InsufficientDataError` as provider-health failures — a couple of unlucky ticker misses (e.g. BRK.A/BRK.B) could take a perfectly healthy provider out of rotation for everyone else. Fixed across Tradier (5 sites), yfinance (6), TwelveData (1), Finnhub (2), AlphaVantage (1), Stooq (3) — FMP was already correct. Verified live: Tradier re-tested 10/10 clean after the fix, breaker self-healed correctly. New Golden Rule 36.

Also centralized `.env` loading into `providers/__init__.py` (previously only explicit in `backend.py`, everywhere else relied on fragile import-order side effects) — verified a bare provider import now loads its API key with zero explicit `load_dotenv()` call needed.

### 5. R:R gate investigation → a real live/backtest divergence bug → Path B
An attempt to fix momentum's R:R structural cap (widen the stop clamp floor) was tested via a quick backtest sanity check and found **directionally backwards** — wider stop = more risk = worse R:R, confirmed empirically (worse PF/Sharpe/drawdown on identical historical trades). Investigating why the trade set didn't change at all led to the real finding: `backtest_holistic.py`'s actual Config C entry gate has never used the flat/ATR formula — it computes R:R from real support/resistance levels, a completely different, never-wired-up piece of logic. `live_signals.py` has substituted the wrong formula as its entry gate since Day 81 (same bug class as Golden Rule 19's JS/Python parity finding). New Golden Rule 35.

**Fix:** built **Path B** — a parallel forward-test experiment using the real S&R-based gate (`check_sr_gate()`), same daily candidate pool as Path A, tracked under its own `variant='B_revised_rr'` ledger tag, own 100-trade bar, zero impact on Path A's frozen count. `paper_trading/ledger.py` gained a `variant` column (clean migration, all existing rows auto-tagged `A_frozen`). Surfaced in the UI: `AutomatedPaperTradingPanel.jsx` gained a visually-distinct "Momentum (Path B)" card with an "EXPERIMENTAL" badge — verified live in-browser, zero console errors.

**A real self-correction, logged honestly** in `PERSONA.md`'s Feedback Log and `KNOWN_ISSUES_DAY95.md` — the wrong first attempt was reverted cleanly, not defended.

---

## Files Changed

| File | Change |
|---|---|
| `~/Library/LaunchAgents/com.sta.papertrading.daily.plist` | Schedule 16:30→17:30 ET, comment corrected |
| `docs/claude/stable/PERSONA.md` | **New** — trading-judgment persona + Feedback Log |
| `docs/claude/stable/GOLDEN_RULES.md` | Rules 33-36 added |
| `backend/providers/tradier_provider.py` | 5 sites: `DataNotFoundError`/`InsufficientDataError` no longer trip the breaker |
| `backend/providers/yfinance_provider.py` | 6 sites, same fix |
| `backend/providers/twelvedata_provider.py` | 1 site, same fix |
| `backend/providers/finnhub_provider.py` | 2 sites, same fix |
| `backend/providers/alphavantage_provider.py` | 1 site, same fix |
| `backend/providers/stooq_provider.py` | 3 sites, same fix |
| `backend/providers/__init__.py` | Centralized `.env` loading |
| `backend/paper_trading/ledger.py` | New `variant` column + migration; every query/write function variant-aware |
| `backend/paper_trading/live_signals.py` | New `check_sr_gate()`; `get_momentum_signals()` now yields both Path A and Path B signals |
| `backend/paper_trading/daily_job.py` | Variant-aware signal queueing; `print_report()` shows both variants |
| `backend/backend.py` | `/api/paper-trading/status` gains `momentumPathB` key (additive) |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | New Path B card, "EXPERIMENTAL" badge |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | New §8b — Path B experiment, honestly documented including the reverted wrong attempt |
| `docs/claude/stable/ROADMAP.md` | Priority #12 marked resolved |

---

## All Gates Status

Unchanged for Path A / MR — no trading-logic threshold changed for the frozen systems. Path B is a new, separately-tracked, honestly pre-registered experiment (not a Golden Rule 18 violation — Path A's count is completely untouched).

**Freeze status:** unchanged — forward-testing accumulation remains the sole priority for Path A/MR. Path B is a parallel addition, not an exception to the freeze in the sense that matters (no existing frozen count was touched).

---

## Paper Trading Status (end of session)

- **Momentum Path A:** 22 open, 2 closed. 2/100 toward the bar.
- **Momentum Path B:** 0 open, 0 closed. New today — 0/100.
- **MR:** 3 open, 25 closed. 25/100 toward the bar.
- Both today's real daily-job runs produced 0 new signals for momentum (both variants) — consistent with Path A's own recent pace, not a red flag given the provider-reliability and R:R-gate context this session established.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS** for Path A and MR. Path B now accumulates alongside, its own separate bar.
2. Monitor Path B's first real signals once TradingView/market conditions produce a genuine S&R-viable setup — no action needed until then.
3. Confirm tomorrow's corrected 17:30 ET schedule fires as expected (one-time sanity check).
4. Everything else remains parked: fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap (ROADMAP Priority #11), `/ibkr-scan`, Session 28 audit's remaining lower-priority findings (ROADMAP Priority #10).
