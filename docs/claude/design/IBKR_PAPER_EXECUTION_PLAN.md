# IBKR Paper-Trading Execution — Design Plan

> **Status:** Planned, not started. Parked pending the user's additional research/review before implementation begins.
> **Created:** Day 96 (July 24, 2026)
> **Source:** planned via a dedicated Plan-mode session with a Plan-agent architecture review, following direct research into IBKR's Client Portal REST API (order-placement flow) and the CIRO regulatory question (verified directly against CIRO's own published guidance, not a secondhand summary).

---

## Context

The existing automated paper-trading engine (`backend/paper_trading/`) simulates every fill internally against historical OHLCV bars — a simplified approximation of a real fill (no real slippage, no real bid/ask, no real market microstructure). The goal here: execute the exact same Path B momentum signals (the real support/resistance-based gate, see `PAPER_TRADING_PREREGISTRATION.md` §8b) as real bracket orders against the user's **IBKR paper-trading account**, so fills come from IBKR's own paper engine (realistic slippage against live market data) instead of the internal simulator.

This is a new subsystem — real broker connectivity and order placement — with one hard safety boundary: it must never be able to reach the live/real account.

## Research already done (Day 96, not re-derived, cited here for the record)

- **Feasibility confirmed**: a working IBKR Client Portal Gateway already exists (`/Users/balajik/projects/clientportal.gw`, port 5055), documented in a sibling project's research (`trading-intelligence-hub/research/ibkr_rest_api_probe/FINDINGS.md` and `IBKR_REST_API_REFERENCE.md`). Auth is always interactive (browser + 2FA, cannot be scripted). Sessions idle-timeout (~15-20 min) without a `/tickle` keep-alive.
- **Regulatory check done directly against CIRO's own published guidance** (not a secondhand summary — the user's referenced source file, `trading-intelligence-hub/research/ibkr_auto_execution_research.md`, didn't exist on disk or in git history, so this was researched live via web search): **CIRO Dealer Member Rule 3200** prohibits a dealer member from letting Order-Execution-Only retail clients (a self-directed account with no advisor recommendation — what a standard IBKR retail account is) use their own automated order system to generate/send **real** orders on a pre-determined basis. This governs real orders reaching a real marketplace through a real dealer-client relationship; a pure paper/simulated account has no real security trading and no real marketplace access, so it falls outside what the rule is regulating — this is a reasoned interpretation of the rule's stated purpose (CIRO doesn't address paper trading explicitly, since it's outside their regulatory perimeter, not something they've ruled on either way). Scope is paper-only throughout this plan, which is what keeps this outside the rule's concern. **If the user wants zero doubt before implementing, a support ticket to IBKR asking directly whether the Rule 3200 restriction extends to paper-trading-account API access would close this gap completely.**
  Sources: [Order Execution Only Dealers guidance](https://www.ciro.ca/newsroom/publications/order-execution-only-dealers-and-use-automation-account-opening-approval-process), [Rule 3200 text](https://www.ciro.ca/media/3310/download?inline=1)
- **Hard safety fact, verified**: IBKR paper account IDs always start with `DU` (e.g. `DU12345678`); live accounts start with `U` (e.g. `U12345678`) — same base number, different prefix. IBKR's own official docs use `"acctId": "DU***14"` as their example. This is the basis for the one non-negotiable safety gate below.
- **Order-placement flow, verified via IBKR's own docs + `Voyz/ibind`** (an independent open-source client library): `POST /iserver/account/{accountId}/orders` (supports bracket/OCA groups via `cOID`/`parentId`/`isSingleGroup`), returns `reply_id`(s) for precaution/warning messages that must each be confirmed via `POST /iserver/reply/{replyId}` (`{"confirmed": true}`) before the order actually transmits. `POST /iserver/account/{accountId}/orders/whatif` previews without submitting (margin/commission info). Example order body: `{"acctId": "DU...", "conid": ..., "orderType": "MKT"|"LMT"|"STP", "side": "BUY"|"SELL", "quantity": ..., "tif": "DAY"|"GTC", "price": ...}`.
- **No existing broker/order code in this repo** (confirmed via grep — zero real hits, no ibind/ib_insync dependency, no IBKR env vars).

## Locked decisions (from the user, Day 96)

| Decision | Choice |
|---|---|
| Signal source | **Path B only** (`variant='B_revised_rr'`) — Path A stays untouched, accumulating on the internal simulator |
| Position sizing | **Fixed $500/trade** notional, floor-divided by signal price for share count (env var `IBKR_PAPER_TRADE_NOTIONAL_USD=500`) |
| Pilot verification | **1 single manual test order** (whatif → place → reply-confirm → verified in IBKR's own paper UI → cancelled) before any automation is trusted |
| Exit-logic gap | **Accepted**: IBKR bracket orders use a plain fixed stop/target — Path B's internal EMA-trailing-stop exit rule has no order-type analog and is NOT replicated here. Disclosed via reporting labels, not hidden. |
| Extra safety layer | **None beyond the code-level `DU`-prefix gate** — no added manual "are you sure" step before the first unattended run, since the gate is hard/non-bypassable and Phase 1 proves it live first |

## Hard constraint (non-negotiable, drives the whole design)

**Every order-placing code path must assert the target account ID starts with `DU` before calling `place_order`/`whatif_order`, with no bypass flag, no env override, no exception path that swallows the check.** This is the single most important property of the whole feature — a bug here means real orders on a real brokerage account.

---

## Architecture

New top-level package `backend/ibkr/` (parallel to, but deliberately separate from, `backend/providers/` — this is an order-execution client with side effects on a brokerage account, not a read-only data-fetch provider, so it gets its own package even though it reuses the same circuit-breaker/rate-limiter/`.env`-loading infrastructure):

```
backend/ibkr/
    __init__.py       # centralized .env loading (mirrors providers/__init__.py), exposes get_ibkr_client()
    client.py         # IBKRClient: auth_status, tickle, search_conid, snapshot (promoted from the
                      #   already-proven research/ibkr_rest_api_probe/client.py), plus new:
                      #   get_accounts, whatif_order, place_order, confirm_reply, get_order_status, get_trades
    safety.py         # assert_paper_account(account_id) — the one non-bypassable gate
    session.py        # is_gateway_up(), is_authenticated(), keep_alive() (calls /tickle once at the
                      #   start of Step 4, not a background loop — see Phase 4)
    order_manager.py  # build_bracket_order(), place_bracket() (whatif -> place -> confirm flow),
                      #   reconcile_ibkr_positions()
    exceptions.py     # IBKRError hierarchy mirroring providers/exceptions.py, incl. IBKRSafetyViolation
```

New `.env` entries:
```
IBKR_GATEWAY_BASE_URL=https://localhost:5055/v1/api
IBKR_PAPER_ACCOUNT_ID=            # e.g. DU12345678 — must be set explicitly, never blank-defaulted
IBKR_PAPER_TRADE_NOTIONAL_USD=500
IBKR_EXEC_MOMENTUM_ENABLED=false  # both default off until Phase 2 manual testing passes
```

---

## Phase 1 — Connectivity, safety gate, one manually-verified test order

**Goal:** prove gateway → auth → whatif → place → reply-confirm → visible in IBKR's own paper UI works for exactly one hand-triggered, cheap order. Zero automation, zero ledger integration.

1. `client.py`: port the proven `auth_status()`/`tickle()`/`search_conid()`/`snapshot()` from `research/ibkr_rest_api_probe/client.py` into `backend/ibkr/client.py` as an `IBKRClient` class; add `get_accounts()`, `whatif_order()`, `place_order()`, `confirm_reply()`, `get_order_status()`, `get_trades()`. Wrap every network call with `circuit_breaker.get_breaker('ibkr')` + `rate_limiter.check_rate_limit('ibkr')` (new conservative `'ibkr'` entry in the rate limiter's provider table — this is a local gateway proxy, not a public API, but still worth not hammering). Keep `verify=False` for the self-signed localhost cert, same justification comment as the research script.

2. `safety.py`:
```python
def assert_paper_account(account_id: str) -> None:
    if not account_id or not account_id.startswith('DU') or len(account_id) < 4:
        raise IBKRSafetyViolation(
            f"Refusing to place/preview an order against account_id={account_id!r} — "
            f"paper accounts must start with 'DU'. This check has no bypass."
        )
```
   Called **twice** in the real call path: once when `IBKR_PAPER_ACCOUNT_ID` is read at client construction (fail fast on misconfiguration), and again immediately before every `place_order`/`whatif_order` network call — cross-checked against what `get_accounts()` independently reports the live session actually has trading access to, not just trusting the `.env` value. Refuse to proceed if the configured ID isn't in that list, or if any non-`DU` ID shows up in it at all.

   Unit tests: raises on `None`, `''`, `'U12345678'` (live prefix), `'DU'` alone (too short); passes only for well-formed `DU########`.

3. **Manual verification procedure** (from a Python REPL, not a script):
   - Start the gateway, authenticate interactively in browser, confirm `auth_status()` returns `authenticated: true`.
   - Call `get_accounts()`, manually confirm the only account present starts with `DU`. **Stop and investigate if any `U...` account is visible at all.**
   - Pick 1 share of a cheap, liquid ticker (e.g. SPY). Call `whatif_order()` first, manually read the commission/margin preview.
   - Call `place_order()`, manually read and resolve each `reply_id`'s precaution message by hand (don't auto-confirm blindly in this phase), then `confirm_reply(reply_id, confirmed=True)`.
   - Log into IBKR's own paper-trading web/desktop UI (independent of this code) and confirm the order/bracket appears correctly on the `DU` account at the expected quantity/price. Cancel or close it manually — don't leave it working unattended.
   - Phase 1 is done only once this single order has been placed, confirmed via IBKR's own UI, and manually closed. No loop, no scheduling yet.

---

## Phase 2 — Wire into real Path B signals (still manually triggered)

1. `order_manager.py`'s `build_bracket_order(signal, account_id, conid, quantity)`: takes the exact dict shape `live_signals.get_momentum_signals()` already produces for `variant='B_revised_rr'` — ticker, signal_price, and the stop/target already computed by the existing `compute_entry_levels()` (same function Path A/B already use for exit management — **not duplicated here**). Builds IBKR's bracket/OCA payload: parent MKT BUY (TIF=DAY, matching the existing "enter at tomorrow's open" convention), child STP SELL at `initial_stop_price` (TIF=GTC), child LMT SELL at `initial_target_price` (TIF=GTC), linked via `cOID`/`parentId`/`isSingleGroup`.

2. `place_bracket(signal, account_id)`: `assert_paper_account()` → resolve `conid` → compute quantity (`$500 / signal_price`, floor, min 1 share) → `whatif_order()` (log preview, abort on anything unexpected) → `assert_paper_account()` again → `place_order()` → confirm every returned `reply_id` (log the message actually seen each time, don't discard it) → record parent/child order IDs for Phase 3.

3. A CLI entry point (`python -m backend.ibkr.order_manager --ticker XYZ [--dry-run]`) so a human can manually run "take today's Path B signals through IBKR" and inspect results by hand, several times, before this goes anywhere near `daily_job.py`.

4. Only after several manually-triggered runs look correct: wire a guarded **Step 4** into `daily_job.py`, gated on `IBKR_EXEC_MOMENTUM_ENABLED=true`. The entire Step 4 call is wrapped so any exception (including a dead/unauthenticated session) is caught, logged, and turns into `summary['ibkr_exec_skipped_reason']` — Path A/B/MR's steps 1-3 must complete successfully regardless of IBKR's state.

---

## Phase 3 — Ledger integration and reconciliation

1. **Schema** (additive migration, same `PRAGMA table_info` + conditional `ALTER TABLE` pattern already used for `variant`): new nullable columns on `paper_positions` — `ibkr_account_id`, `ibkr_parent_order_id`, `ibkr_stop_order_id`, `ibkr_target_order_id`, `ibkr_last_status`, `ibkr_conid`. New variant value `'C_ibkr_paper'` — **no ledger function signature changes needed**, every function (`queue_pending_signal`, `get_open_positions`, `close_position`, `get_closed_trades`, `compute_stats`, `has_active_or_cooldown`, etc.) already takes `variant` as a parameter from the Path B work.

2. **`C_ibkr_paper` rows never go through `simulate_trade()`/`simulate_mr_trade()` replay** — their entry/exit prices come from IBKR's own reported fills via a new `reconcile_ibkr_positions()` in `order_manager.py`:
   - parent filled, no child filled → `activate_position()` using IBKR's reported fill price/time (not recomputed)
   - a child (stop or target) filled → `close_position()` using IBKR's reported fill price/time, `exit_reason='ibkr_stop_filled'`/`'ibkr_target_filled'`, pnl computed with the same math `daily_job.py`'s `step_open_positions()` already uses
   - still working → `update_open_position()`, `days_held` recomputed from `entry_date`

3. **Reporting** (all purely additive, mirroring the existing `momentumPathB` pattern exactly):
   - `backend.py`'s `/api/paper-trading/status`: add `systems['momentumIbkr']` using the same `get_open_positions(..., variant='C_ibkr_paper')` / `compute_stats(..., variant='C_ibkr_paper')` calls already used for `momentumPathB`.
   - `AutomatedPaperTradingPanel.jsx`: another `<SystemCard>` using the existing `badge` prop — label "IBKR Paper (real fills)" so the fidelity difference is visible, not just in code comments.
   - `daily_job.py --report`: one more `_print_variant_stats('momentum', 'C_ibkr_paper', 'IBKR paper execution (real fills)')` line.

---

## Phase 4 — Operational reality (no fake automation)

- `session.py`'s `keep_alive()` calls `/tickle` once at the start of Step 4 (not a background daemon — a once-daily batch job doesn't need one, and a permanently-running keep-alive process is a bigger piece of infrastructure than the ~15-20 min benefit justifies).
- `is_gateway_up()` / `is_authenticated()` gate Step 4 cleanly: gateway not running → skip + log; not authenticated → skip + log a clear "re-authenticate at https://localhost:5055" message. Three distinguishable daily-job outcomes: ran, skipped (no auth), errored — never a silent no-op.
- No attempt to script around 2FA — no credential storage, no TOTP automation. The user is expected to periodically re-authenticate via browser; this plan does not pretend otherwise.
- No `launchd` plist changes needed — Step 4 lives inside the existing `daily_job.py` process and no-ops safely when unauthenticated.
- A new `docs/claude/stable/IBKR_PAPER_EXECUTION.md` (operational doc, distinct from this design plan) should eventually document this honestly for day-to-day use, same pattern as `PAPER_TRADING_PREREGISTRATION.md`.

---

## Verification (end-to-end, how to know each phase actually works)

- **Phase 1**: the single test order must be independently visible and correct in IBKR's own paper-account web/desktop UI — not just "the API call returned 200."
- **Phase 2**: run the CLI entry point manually against a real day's Path B signal (or a synthetic one if none qualifies that day), confirm the bracket appears correctly in IBKR's UI, confirm `assert_paper_account()` unit tests pass.
- **Phase 3**: after a manually-placed bracket fills or hits its stop/target in IBKR's paper account, run `reconcile_ibkr_positions()` and confirm the local `paper_positions` row updates with IBKR's real fill data; confirm `/api/paper-trading/status` and the Forward Test tab show the new `momentumIbkr` card correctly (verify live in-browser, per this project's existing UI-verification discipline).
- **Phase 4**: kill/don't-authenticate the gateway deliberately and confirm `daily_job.py`'s Steps 1-3 still complete successfully with Step 4 cleanly skipped and logged.

## Critical files (for whenever implementation resumes)

- `backend/paper_trading/live_signals.py`, `ledger.py`, `daily_job.py` — existing engine, signal source, ledger pattern to extend
- `backend/providers/circuit_breaker.py`, `providers/__init__.py` — patterns to replicate for `backend/ibkr/`
- `backend/providers/tradier_provider.py` — closest existing example of a REST-client provider file
- `backend/backend.py` (~lines 2709-2762, `/api/paper-trading/status`) — endpoint to extend
- `frontend/src/components/AutomatedPaperTradingPanel.jsx` — UI card to add
- `/Users/balajik/projects/trading-intelligence-hub/research/ibkr_rest_api_probe/client.py` — already-proven starting point for `backend/ibkr/client.py`

---

## Open items before resuming (per the user's own request — additional research/review needed)

1. Confirm with IBKR directly (support ticket) whether the CIRO Rule 3200 automated-order restriction has any bearing on paper-trading-account API access, to remove all doubt beyond this doc's own reasoned interpretation.
2. Re-review this plan after that additional research, before Phase 1 begins.
