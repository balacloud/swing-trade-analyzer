# Analyze Page Redesign — Step 5 plan: Mean-Reversion Read card (Day 123)

Status: DRAFT for independent review (Fable) before code.
Standard: §0 of `ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md` (no silent failures,
logging, never-throw helpers, real data behind every element, true to the
engine). Design: mockup v0.14 "Mean-Reversion Read"; decisions doc Day 123
"MR card redesigned".

## 1. What "the tested system" is (verified in code)

The PF 2.00 result is the forward test (paper-trading ledger, variant
`A_frozen`, 241 closed trades, 170 wins = 70.5%, PF 2.00 on net `pnl_pct`,
entries 2026-07-13 → exits 2026-09-25; queried live from
`backend/validation_results/paper_trading_ledger.db`). Its rules:

| Step | Rule | Source |
|---|---|---|
| Signal | RSI(2) < 10, close > 200-day SMA, close > $10, 20-day avg dollar volume > $25M, **on a completed daily bar** | `mean_reversion.detect_mr_signal`; `live_signals._prepare_ohlcv` drops today's forming bar |
| Buy | next session's **open** | `daily_job.py:72-76` (`entry_idx = signal_idx + 1`, `Open`) |
| Stop | 5% below the buy price, gap-aware | `daily_job.py:46,88`; `mr_simulator.simulate_mr_trade` |
| Sell | first close with RSI(2) > 70, or after 10 trading days | `mr_simulator.py:122,128`; `MR_MAX_DAYS = 10` |
| Target | none | `daily_job.py:89` |

## 2. Problems in the live card / endpoint today

| # | Problem | Evidence |
|---|---|---|
| P1 | Card shows `detect_mr_signal`'s stop (tighter of 5% or 1.5 ATR) and target (entry + 2 ATR). Neither is the tested rule. | `mean_reversion.py:212-221` |
| P2 | Same wrong stop/target on the Scan tab's MR list. | `App.jsx:2435-2436` |
| P3 | `/api/mr/signal` evaluates today's **forming** bar during market hours; the tested signal uses completed bars only. The card can say "buy" mid-day on a signal the tested system would not take. | `backend.py:3600-3616` (no forming-bar drop) |
| P4 | ATR fallback `current_price * 0.02` — a made-up ATR. | `mean_reversion.py:211` |
| P5 | NaN inputs (missing volume) make a condition silently `False`, read as "fails the rule". | `mean_reversion.py:186-198` |
| P6 | Card renders nothing on loading, error, or no signal — a failed fetch looks identical to "no signal". | `MRSignalCard.jsx:16-26` |
| P7 | MR rule numbers are literals in 4 places (detector, simulator default, daily_job constants, card labels). | as above |

## 3. Changes

### Backend
- **B1 Shared forming-bar helper.** New `backend/market_time.py`:
  `MARKET_TZ`, `MARKET_CLOSE_HOUR/MIN`, `is_forming_bar(last_bar_date)`,
  `drop_forming_bar(df) -> (df, dropped: bool)`. Used by `/api/mr/signal` and
  `/api/mr/scan`. The S&R route's inline check and `live_signals._prepare_ohlcv`
  are switched to import it too (same logic, one place; parity of behavior
  checked by unit test). `live_signals` is in the discontinued paper-trading
  program; the change there is import-only.
- **B2 One definition of the MR rules.** `mean_reversion.MR_RULES = {rsi2_entry:
  10, price_min: 10, dollar_volume_min: 25e6, stop_pct: 0.05, rsi2_exit: 70,
  max_hold_days: 10, entry: 'next_open'}`. `detect_mr_signal` uses it.
  `mr_simulator` defaults and `daily_job` constants are left as is (frozen
  backtest/ledger code) but a unit check asserts they equal `MR_RULES`.
- **B3 `detect_mr_signal` output.** Remove `stop`, `target`, `atr` and the
  2% ATR fallback (P1, P4). Add `rules: MR_RULES`, per-condition values
  (`pct_above_sma200`), and **tri-state conditions**: `True / False / None`
  (None = input missing, e.g. NaN volume; `signal` is False and
  `missing: [..]` lists why) (P5). Keep `adx`/`range_bound` in the payload
  (not displayed; not part of the tested rule).
- **B4 `/api/mr/signal`.** Drop the forming bar first; return `asOf`
  (signal bar date) and `barDropped`. Insufficient data stays a 200 with
  `error` + `reason`, now with `bars`. `print` warnings with ticker on
  provider fallback and insufficient data (file convention).
- **B5 Track record.** `get_mr_track_record()` in `mean_reversion.py` (or a
  small `mr_track_record.py`): reads the ledger (`system='mr'`,
  `variant='A_frozen'`, `status='closed'`) → `{trades, wins, winPct,
  profitFactor, firstEntry, lastExit, source}`, cached for the process
  lifetime (the program is discontinued, the ledger is final). Missing
  DB/table → `None` + warning. Returned as `trackRecord` in
  `/api/mr/signal`.
- **B6 `/api/mr/scan`.** Uses B1; rows carry `asOf`; no stop/target.

### Frontend
- **F1 `components/MRRead.jsx`** replaces `MRSignalCard.jsx` (deleted).
  Always rendered (P6), four states: loading skeleton / "Couldn't check:
  reason" / No signal / Buy the dip. Layout per mockup v0.14:
  - Answer + "n of 4 rules pass".
  - "Buy the dip needs all four" tiles: RSI(2) value (needs < 10), % above
    200-day (needs above), price (needs > $10), 20-day $ volume (needs >
    $25M). `None` condition → dashed "no data" tile, never ✗.
  - "As of the <asOf> close" line; when the forming bar was dropped: "today's
    bar is still forming; the signal is checked on completed days only".
  - On a signal: "The plan, exactly as tested" (buy tomorrow's open; stop 5%
    below your buy, ≈ close × 0.95 shown as an estimate; sell first close with
    RSI(2) > 70; or after 10 trading days; no target). All numbers from
    `rules`.
  - Track record line from `trackRecord` with its dates; absent → "track
    record unavailable". One honesty line: an 11-week forward test in mostly
    rising markets.
  - "How this read was formed" (mockup copy, numbers from `rules`).
  - `useMissingInputWarning('MRRead', ...)` for error / missing conditions /
    missing track record.
- **F2 Placement:** directly under the Technical Read (mockup order: Regime,
  Technical Read, MR Read, Trade Setup).
- **F3 Scan tab MR rows:** replace "Stop $x / Target $y" with the tested
  plan in words ("stop 5% below your buy · sell when RSI(2) > 70 or after 10
  days") and the `asOf` date.
- **F4 api.js `fetchMRSignal`:** check it surfaces `{error, reason}` rather
  than throwing/nulling; card shows the reason.

## 4. Data backing every element

| Element | Source |
|---|---|
| RSI(2), SMA200, price, $ volume, conditions | `detect_mr_signal` on completed bars |
| % above 200-day | new `pct_above_sma200` |
| As-of date, forming note | `asOf`, `barDropped` (B4) |
| Plan numbers | `rules` (B2) |
| Stop estimate | `current_price × (1 − stop_pct)`, labelled "≈ … if bought at $close" |
| Track record | ledger query (B5) |

## 5. Verification
1. Python unit checks: `detect_mr_signal` on synthetic frames (signal; no
   signal; NaN volume → None condition; < 200 bars); `drop_forming_bar` with a
   today-dated bar before/after 16:05 ET; `MR_RULES` == simulator/daily_job
   constants; track record matches the SQL above (241 / 70.5 / 2.00).
2. Golden Rule 54 caller check: every consumer of `stop`/`target`/`atr` from
   `detect_mr_signal` (App scan rows, MRSignalCard, live_signals) updated or
   confirmed unaffected.
3. Build clean; verdict parity green (untouched).
4. Live: a ticker with an active signal (find via `/api/mr/scan`), a no-signal
   ticker, a < 200-bar ticker, forced `/api/mr/signal` failure, 390px.
5. Three escalating review passes; Fable code review.

## 6. Fable review — NO-GO as written (Day 123), verified and accepted

**#1 (MUST-FIX), verified independently:** the forward test's PF 2.00 was
not measured on "buy at the next open". `daily_job.py` records the entry
day's **open** as `entry_price`, but the replay (`simulate_mr_trade`,
`mr_simulator.py:69`) prices the trade at the entry day's **close** and
starts exits the day after. 0 of 241 rows have `pnl_pct_gross` equal to
(exit / recorded open − 1). Quick recompute at the recorded open, exits
held fixed: PF ≈ 1.60, 160/241 wins, avg +0.96% (vs stored 2.00 / 170 /
+1.40%). The 2020–2025 backtest (PF 1.16) enters at the signal day's close —
a third basis.

**User decision (Day 123):** the card's plan is "buy at the next open", and
the forward test is re-run properly on that basis (stop 5% below the open,
entry-day bar counts for the stop and the RSI(2) exit, gap-aware), alongside
a close-basis replay that must reproduce the stored PF 2.00 as a harness
check. The card shows the re-tested number and the backtest PF 1.16. PF 2.00
is corrected wherever it is quoted.

**Pre-registered prediction (Golden Rule 56), written before running:**
open-basis PF **1.5–1.7** (point estimate 1.6), win rate **63–68%**, still
positive. Reasoning: the quick recompute holds exits fixed; letting the
entry-day bar trigger stops will add a few extra stop-outs, so the proper
number should land at or slightly below 1.6. If PF comes out below 1.3 the
"one confirmed edge" claim itself needs revisiting with the user.

Remaining findings #3–#13 accepted: show HUB-65 too (1.68 close-basis, to
be re-tested the same way); say the record is across a screened universe,
not this ticker; stop wording "5% below your fill, fills at the open on a
gap"; B1 scope narrowed (MR routes use the helper, S&R imports
`is_forming_bar` only, `live_signals` untouched); `_finite()` guard on every
input; drop forming bar before the 200-bar check and on every data path;
`fetchMRSignal` returns `{error, reason}`; no `entry` string in rules; add
cooldown to §1; RSI(2) shown to 1dp with ✓ only from backend conditions;
ledger dates, not "ended Sep 12".
