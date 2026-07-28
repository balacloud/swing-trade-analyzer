# Partial-Bar Ledger Contamination — Diagnosis & Fix Plan

> **Created:** Day 99 (July 27, 2026) — found during an Opus 5 integrity review of the
> paper-trading ledger/replay path, requested by the user.
> **Status:** Diagnosed and evidenced. **Not yet fixed** — this document is the
> executable plan for the implementing session.
> **Severity:** High (contaminates the forward-test evidence base, which is the
> project's sole active priority).
> **Implementing model:** Sonnet is fine — the diagnosis work is done, the fix is
> mechanical. Follow Golden Rule 32 (3 review passes) and Golden Rule 13
> (exhaustive verification, not spot-check) as usual.

---

## 1. One-paragraph summary

The data provider returns a bar for the **current day while the market is still
open**. Neither `simulate_trade()` nor `simulate_mr_trade()` checks whether the
final bar is complete — the `live_mode` loop reads its `High`/`Low`/`Close`
directly. MR's `rsi2_exit` books `bar_close`, so when the daily job is run
mid-session, a **mid-session price is written to the ledger as that day's closing
price**, and the position is closed permanently (`close_position` is one-way).
The launchd-scheduled 17:30 ET run is safe; the contamination comes entirely from
manual `--force` runs and the **Force Run Now** UI button, both of which have been
used repeatedly during market hours. **19 of 25 closed MR trades are affected.**

---

## 2. Root cause — exact locations

| # | File | What's wrong |
|---|---|---|
| 1 | `backend/backtest/trade_simulator.py` (`simulate_trade`, live_mode loop ~line 312+) | Reads `High`/`Low`/`Close` at `check_idx` with no completeness check on the final bar. |
| 2 | `backend/backtest/mr_simulator.py` (~lines 96–130) | Same. `rsi2_exit` sets `exit_price = bar_close` (line ~123) — a mid-session close. |
| 3 | `backend/paper_trading/daily_job.py` (`step_open_positions`, `activate_pending_signals`) | Passes the raw provider DataFrame straight into the simulators. |
| 4 | `backend/paper_trading/live_signals.py` (`get_momentum_signals`, `get_mr_signals`, `get_market_regime`) | Same — signal generation also sees the partial bar. |

There is no single chokepoint that strips an incomplete bar. `_to_capitalized_ohlcv()`
is the closest thing to a shared entry point but it is only a column normalizer.

**Why this was never caught:** the engine was designed and reasoned about as a
once-daily post-close job (Day 81). Every review since has assumed that execution
context. The Force Run Now button (Day 88) and `--force` (Day 81) quietly broke the
assumption without anyone re-deriving what a mid-session run implies.

---

## 3. Evidence

### 3a. The mechanism is directly observable

At **2026-07-27 14:35 EDT (market open)**, `dp.get_ohlcv(tk, period='2y')` returned a
row dated `2026-07-27` for every ticker tested (BMO, HMN, NTB, BPOP, SRCE, GWW).
That row is an in-progress bar: its `Close` is the last trade, not the closing print.

### 3b. Natural experiment — after-close writes reproduce exactly, mid-session writes never do

All 25 closed MR trades were re-replayed against now-complete history using the
**same** `simulate_mr_trade()` code and the ledger's own stored entry values
(read-only; nothing was mutated):

| Write timing | Count | Result |
|---|---|---|
| Exit bar already complete when written (GOOGL, INTC, DE, KLAC, ADI, AXP) | 6 | delta **0.00pp** — exact reproduction |
| Written mid-session on the exit day | 19 | **every single one differs** |

`ADI` is the cleanest control: it *exited* 07-21 but was *written* on 07-22, so its
07-21 bar was already complete — delta 0.00. The twelve tickers that both exited and
were written on 07-21 mid-session all differ. This rules out provider data revision
as the driver; the split falls exactly on bar completeness.

### 3c. Four trades are wrong at the decision level, not just price

| Ticker | Ledger | Clean replay |
|---|---|---|
| **MS** | closed 2026-07-22, +1.23% | **should still be OPEN** — a phantom closed trade counting toward the 100-trade bar |
| **JNJ** | closed 2026-07-17, +2.00% | closes 2026-07-22, +2.25% (5 days early) |
| **CSCO** | closed 2026-07-22, +0.91% | closes 2026-07-23, +0.71% |
| **CAT** | closed 2026-07-22, +4.28% | closes 2026-07-23, +3.50% |

### 3d. Fifteen more have the right exit day but wrong P&L

Deltas (replay − ledger), all in percentage points:

```
MU   +3.83   AMD  +3.13   APH  +2.19   STX  +1.92   WDC  +1.81
TSM  +1.64   ARM  +1.40   MRVL +1.22   SMFG +0.34   AMAT +0.32
SAN  -0.04   QCOM -0.40   ABBV -0.73   GEV  -0.73   ANET -1.01
```

**`GEV` flips outcome: +0.69% (win) → −0.04% (loss).** Any repair must recompute the
`result` field, not just the P&L.

Net across the 21 same-exit-day trades: **+14.89pp total, ≈ +0.71pp/trade** — i.e. the
ledger currently **understates** MR. This is *not* what is propping up MR's 92% WR /
PF 10.82; the sector-clustering explanation in `PERSONA.md` still stands. The bias is
uncontrolled and simply happened to break negative because semis rallied into the
close on 07-21. Do not treat "it understates" as a reason to deprioritize.

### 3e. Scope beyond MR

- **Momentum (2 closed trades):** `WST` was written pre-market (safe). `KRYS` was
  written mid-session but exited `stop_hit`, whose `exit_price` is the deterministic
  stop level, and whose trigger is monotone in the intraday low — so the exit day is
  correct. **Both appear clean, but verify exhaustively rather than trusting this.**
- **Open positions (25 rows):** `days_held` / `current_stop_price` were last written
  from partial-bar replays, but these are recomputed from scratch every run, so they
  self-heal on the next clean run. No permanent damage.
- **Pending signals:** unaffected. `signal_date` is derived from the last bar
  (Golden Rule 28), so a mid-session run just stamps the previous complete day.

---

## 4. Fix plan

**Ordering is mandatory: Phase 1 must land and be verified before Phase 2 runs**, or
the repair will re-contaminate itself from the same partial bars.

### Phase 1 — Strip the incomplete final bar (the actual fix)

Add one shared helper and call it at every provider-fetch site in the paper-trading
engine.

```python
# backend/paper_trading/live_signals.py (next to _to_capitalized_ohlcv)
from zoneinfo import ZoneInfo   # stdlib in Python 3.9+, venv is 3.9

MARKET_TZ = ZoneInfo("America/New_York")
MARKET_CLOSE_HOUR, MARKET_CLOSE_MIN = 16, 5   # 16:05 ET — small buffer past the bell

def drop_incomplete_bar(df):
    """
    Remove the final bar when it is TODAY's still-forming intraday bar.

    Providers return a partial bar for the current session while the market is
    open; its High/Low/Close are not final. Feeding that into the live_mode
    replay writes mid-session prices into the ledger as closing prices and can
    close a position that should still be open (see this doc's Section 3).

    Golden Rule 33: use an explicit market timezone, never the machine's local
    time or a naive datetime.now().
    """
    if df is None or len(df) == 0:
        return df
    now_et = datetime.now(MARKET_TZ)
    last_bar_date = str(df.index[-1])[:10]
    if last_bar_date != now_et.strftime('%Y-%m-%d'):
        return df                      # last bar is a prior session — already final
    if (now_et.hour, now_et.minute) >= (MARKET_CLOSE_HOUR, MARKET_CLOSE_MIN):
        return df                      # after the close — today's bar is final
    return df.iloc[:-1]                # mid-session — drop the forming bar
```

**Call sites to update — grep `get_ohlcv(` under `backend/paper_trading/` and confirm
you have all of them:**

| File | Function |
|---|---|
| `daily_job.py` | `activate_pending_signals()` |
| `daily_job.py` | `step_open_positions()` |
| `live_signals.py` | `get_market_regime()` (SPY) |
| `live_signals.py` | `get_momentum_signals()` |
| `live_signals.py` | `get_mr_signals()` |

Cleanest implementation: apply it **inside** `_to_capitalized_ohlcv()`, since every
one of those sites already wraps its fetch in that call — but if you do, rename it
(e.g. `_prepare_ohlcv`) so the name still describes what it does, and update its
docstring. Do **not** leave a function called `_to_capitalized_ohlcv` that silently
also drops rows.

**Deliberate consequence, accept it:** during a mid-session run, a signal from
yesterday will no longer activate until the post-close run. That is correct — it
makes the engine's behavior identical regardless of *when* it is invoked, which is
the invariant we actually want. The one-day slip only materialises if the scheduled
17:30 ET run never happens, which `/sta-start`'s dead-man check already covers.

**Do NOT** try to be clever by allowing the partial bar's `Open` through for
activation while blocking High/Low/Close for exits. It is more surgical but far more
error-prone, and the determinism argument above is worth more than one day of latency.

### Phase 2 — One-time repair of the 19 contaminated rows

Model this on the Day 92 zombie-signal repair. Write
`backend/paper_trading/repair_partial_bar_exits.py`:

1. `ledger.backup_db()` **first**, unconditionally.
2. For every closed row (both systems — do not assume momentum is clean), re-run the
   same simulator with the ledger's stored `entry_price` / `initial_stop_price` /
   `max_hold_days` against complete history, exactly as `step_open_positions()` does.
3. **Dry-run by default.** Print a full before/after diff. Require an explicit
   `--apply` flag to write.
4. On apply, for rows whose replay differs:
   - Price/day differences → update `exit_date`, `exit_price`, `exit_reason`,
     `pnl_pct`, `pnl_pct_gross`, `pnl_r`, `days_held`, and **`result`**
     (`GEV` flips win→loss — recompute from `res['win']`, don't carry the old label).
   - **`MS`** → revert `status` to `'open'`, null out `exit_date` / `exit_price` /
     `exit_reason` / `result` / `pnl_*`, and restore `days_held` /
     `current_stop_price` from the replay's open snapshot.
5. Write a JSON audit trail to `backend/validation_results/` recording every row's
   before/after, so the repair itself is reviewable later.

**Accepted, do not try to undo:** re-entry cooldowns were evaluated against the old
exit dates, so a handful of subsequent entries may not match what a clean history
would have produced. That is unrecoverable and not worth chasing — note it in the
audit trail and move on.

### Phase 3 — Force Run Now: warn, don't block

The Phase 1 guard makes mid-session runs *safe*, so blocking is unnecessary. Add a
visible notice in `AutomatedPaperTradingPanel.jsx` near the Force Run button, e.g.
*"Runs during market hours use the last completed session's bar — today's signals
appear after the 17:30 ET run."* Keeps the button useful without implying it produces
same-day results. (Golden Rule / UI principle: visible state over hidden — see
`feedback_ui_visible_state_over_hidden`.)

### Phase 4 — Two smaller findings from the same review (low priority, batch here)

**4a. Momentum live stats are gross of transaction costs; its benchmark is net.**
`backtest_holistic.py:604` applies `apply_transaction_costs()` and sets
`return_pct_net`, but `simulate_trade()` returns pure gross
(`trade_simulator.py:426`), and `daily_job.py:149` stores `result['return_pct']` into
**both** `pnl_pct` and `pnl_pct_gross`. `ledger.compute_stats()` then feeds that gross
number in as `return_pct_net`, which is what `compute_metrics()` actually uses. So
live momentum PF is measured gross against a net PF 1.40 benchmark — same class as
Golden Rule 35. **Magnitude is small** (cost model is $3 per 100 shares ≈
0.03–0.12%/trade), so it will not change any conclusion; fix for correctness, don't
alarm anyone. Fix by applying `apply_transaction_costs()` in `daily_job.py`'s momentum
close branch, mirroring what `mr_simulator` already does internally.
*(`KNOWN_ISSUES` currently lists this as a cosmetic "identical net/gross" item — it is
actually a small live/backtest divergence. Update that wording.)*

**4b. Two dead defensive fallbacks.** `ledger.py:305`
`t.get('pnl_pct_gross', t.get('pnl_pct'))` and `metrics.py:104`
`t.get('return_pct_net', t.get('return_pct', 0))` — the key always exists (it is a
column / always-set dict key), so a NULL value returns `None` rather than the intended
fallback. Latent, not currently firing. Use an explicit `if ... is None` instead.

---

## 5. Verification checklist

Golden Rule 13 — check every item, not a sample. Golden Rule 32 — three passes.

- [ ] **Phase 1, pass 1:** With the market open, confirm `drop_incomplete_bar()`
      removes today's row; with a mocked post-16:05 ET clock, confirm it does not.
      Confirm a weekend/holiday run is unaffected (last bar ≠ today).
- [ ] **Phase 1, pass 2 (what else calls this):** grep every caller of
      `_to_capitalized_ohlcv` / `get_ohlcv` across the **whole** backend, not just
      `paper_trading/` — `backend.py`'s scan and analyze routes intentionally *want*
      live intraday data. Do not change their behavior.
- [ ] **Phase 1, pass 3 (other state):** confirm `signal_date` still derives from the
      last bar and still matches an OHLCV index entry (Golden Rule 28 must not
      regress), and that `activate_pending_signals()` still enters at the correct
      next-day open after a multi-day gap.
- [ ] **Regression proof:** after Phase 1, re-run the Section 3b experiment — replay
      every closed trade and confirm the 6 known-clean rows still reproduce at 0.00pp.
- [ ] **Phase 2:** dry-run diff reviewed by the user before `--apply`. Backup exists.
      Post-apply, re-replay all closed trades: **every** row should now reproduce
      exactly.
- [ ] **Phase 2 sanity:** MR stats will move (GEV flips win→loss; MS leaves the closed
      set). Report the before/after WR / PF / trade count explicitly — do not let the
      headline numbers change silently.
- [ ] **Phase 3:** live browser check, zero console errors.

---

## 6. What this is NOT

- **Not a threshold change.** No entry/exit rule, gate, or parameter is being
  re-tuned. Golden Rules 18/20 are not in play — this is a data-correctness fix to the
  replay's *inputs*, in the same family as Golden Rule 29 (anchor the replay to what
  was actually decided) and Golden Rule 35 (verify parity directly, don't assume it).
- **Not a freeze exception.** It repairs the forward-test evidence base, which is the
  sole active priority — the same rationale that justified Days 88/89/92.
- **Not a reason to restart any track's count.** The trade *entries* were all
  legitimate; only their exits were mis-recorded, and the correct exits are
  deterministically recoverable. Trade counts toward the 100-trade bars stand, minus
  `MS` returning to open.

---

## 7. Session-close bookkeeping for whoever implements this

- Add to `KNOWN_ISSUES_DAY[N].md` as **High** until Phase 1+2 land, then move to
  resolved with a pointer here.
- Add a ROADMAP priority entry (this is real work, not a backlog one-liner).
- Strong Golden Rule candidate once fixed, roughly: *"A live engine that replays
  historical bars must verify the last bar is closed — a provider will hand you a
  partial one, and a job that can be run manually will eventually be run mid-session."*
  Let the implementing session word it from what it actually learned.
- `PERSONA.md` Feedback Log entry is warranted: the review that found this was
  prophylactic, targeted at the highest-stakes silently-accumulating code precisely
  *because* nothing looked broken — and the bug it found was invisible from the UI,
  from the code read alone, and from the aggregate stats.
