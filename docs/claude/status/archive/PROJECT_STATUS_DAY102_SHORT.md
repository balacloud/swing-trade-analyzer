# Project Status — Day 102 (August 4, 2026)

## Version: v4.55 (Backend v2.48, Frontend v4.50) — unchanged

---

## What Happened Today

### 1. Forward-testing check-in (no code changes)
Ran `daily_job.py --report`. MR (broad) crossed the halfway point toward its 100-trade bar; all other tracks still well behind.

| Track | Open | Closed | Win Rate | Profit Factor | Notes |
|---|---|---|---|---|---|
| Momentum Path A | 34 | 9 | 55.56% | 1.7916 | |
| Momentum Path B | 33 | 6 | 50.0% | 0.9876 | Still near breakeven |
| MR (broad) | 14 | **61** | 73.77% | 3.3923 | Closest to the 100-trade bar; PF continuing to cool (8.26 Day 100 → 6.20 Day 101 → 3.39 today) as the sample grows — same healthy-cooling read applied again, see PERSONA.md Feedback Log |
| MR (HUB-65) | 2 | 26 | 50.0% | 1.3482 | |

### 2. Questrade Flow automation — real-money experiment, explicitly separate from STA
User is standing up a small (~$3K), simple ETF swing-automation experiment inside Questrade Pro's new "Flows" no-code automation feature, using a curated 11-ticker "AI Supply Chain ETF" IBKR watchlist (DRAM, XETM, SETM, SMH, GRID, URA, AIPO, COPX, XCHP, SOXX, SGRD). **User was explicit this is a separate exercise from STA — the paper-trading freeze and forward-testing accumulation are untouched.** Recorded here only because it happened in this session; full detail in memory (`project_questrade_flow_experiment.md`), not in STA's own docs, since it isn't STA functionality.

Key findings from directly querying the Questrade Flow assistant (not assumed from outside docs, per the user's explicit instruction each time):
- One workflow = one action (buy XOR sell, never both) — each ticker needs 2 separate Flows.
- No cross-trigger-type field comparison (can't compare Market Data price to Position avg cost in one condition).
- No formula/multiplier math within a trigger either (can't do `MARKET_VALUE >= AVG_PRICE * OPEN * 1.03`) — only a direct field-to-field or field-to-static-number comparison.
- Net effect: an automated %-above-average-cost take-profit sell isn't achievable if the position is allowed to average up via repeat buys (pyramiding) — only a **static** price/value target works, and it only stays correct if there's exactly one buy per name. User chose to cap at one buy per name specifically to keep the sell side genuinely self-adjusting-free (i.e., correct without needing manual edits).
- Real-money design settled on: buy $500 on a >3% single-day drop (Market Data trigger), sell the whole position once `MARKET_VALUE >= buy_size × 1.03` (Positions trigger) — dollar-based sizing means the sell target is knowable before the buy even fires, since it doesn't depend on the unknown fill price.
- First live flow built (XCHP.TO buy, $500, -3%/day trigger, Max 1 orders/day). **Two things flagged, unresolved as of session end:** (1) the account's own IBKR-adjacent watchlist ticker resolved to `XCHP.TO` (a `.TO`/Toronto listing) rather than `XCHP` (the intended US iShares Semiconductor ETF) — real risk of a US/Canadian ticker collision, user was asked to verify what `XCHP.TO` actually is before the sell flow or any further tickers are built; (2) "Max 1 orders/day" is a daily cap, not a lifetime cap — doesn't by itself enforce the intended "one buy per name ever," so the buy flow will need manual pausing after its first real fill.

---

## Files Changed

None — no STA code touched this session (forward-testing monitoring + a separate, non-STA real-money experiment).

---

## All Gates Status

Unchanged. No entry/exit gate, threshold, or frozen config was touched this session.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority for the automated engine tracks.

---

## Paper Trading Status (end of session)

| Track | Open | Closed | Win Rate | Profit Factor | Notes |
|---|---|---|---|---|---|
| Momentum Path A | 34 | 9 | 55.56% | 1.7916 | |
| Momentum Path B | 33 | 6 | 50.0% | 0.9876 | |
| MR (broad) | 14 | 61 | 73.77% | 3.3923 | Closest to 100-trade bar (61/100) |
| MR (HUB-65) | 2 | 26 | 50.0% | 1.3482 | |

Last job run: 2026-08-04 (today, healthy).

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS for STA itself**, across all four tracks. MR (broad) is now past the halfway point at 61/100.
2. Keep `docs/claude/design/HOW_STOCK_PICKING_WORKS.html` updated as real questions come up (unchanged from Day 101).
3. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit's remaining findings, the "Quick" momentum holding-period idea, the scheduled breakout-alert watcher (ROADMAP #15).
4. *(Not an STA item, tracked in memory only)* The Questrade Flow experiment has an open verification item — confirm what `XCHP.TO` actually is before building its sell flow or any of the other 10 tickers' flows.
