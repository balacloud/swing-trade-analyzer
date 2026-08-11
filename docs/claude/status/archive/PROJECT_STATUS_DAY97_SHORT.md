# Project Status — Day 97 (July 24, 2026)

## Version: v4.52 (Backend v2.45, Frontend v4.47, Backtest v4.19, API Service v2.11) — unchanged

---

## What Happened Today

Short research/planning-only session (no code changes) — user asked about connecting to IBKR for actual paper-trading execution (real bracket orders against IBKR's paper account, instead of the internal SQLite-simulated fills Path A/B currently produce).

### 1. Research: IBKR Client Portal REST API feasibility
Read a sibling project's (`trading-intelligence-hub`) IBKR REST API probe research — confirmed a working Client Portal Gateway setup already exists (port 5055, documented auth flow, order-placement endpoints via IBKR's own docs + `Voyz/ibind`). That research was about market-data fields (IV Rank), not order execution — no prior work existed on actually placing orders.

### 2. Regulatory research: CIRO Rule 3200
The user referenced a research file (`ibkr_auto_execution_research.md`) discussing a Canadian regulatory restriction on automated order execution — the file didn't exist on disk or in git history (likely only ever a pasted conversation snippet). Researched the actual regulation directly via web search rather than relying on a secondhand summary found in the hub project's session logs: **CIRO Dealer Member Rule 3200** prohibits a dealer member from letting Order-Execution-Only retail clients (a self-directed account, no advisor recommendation) run automated order systems that generate/send real orders on a pre-determined basis. Confirmed this governs real orders to a real marketplace through a real dealer-client relationship — reasoned that a pure paper/simulated account falls outside what the rule regulates (paper trading isn't within CIRO's regulatory perimeter at all), though flagged that a support ticket to IBKR would remove all doubt if the user wants zero ambiguity before implementing. New **Golden Rule 37**: verify a cited source directly when it can't be located, don't rely on a secondhand summary of it.

### 3. Full design plan produced (Plan mode + a Plan-agent architecture review)
Entered plan mode, spawned a Plan agent with full codebase context, then synthesized a 4-phase implementation plan: connectivity + one manually-verified test order → wire into real Path B signals (still manual) → ledger/reporting integration (new `variant='C_ibkr_paper'`, reusing all the Day 96 variant-generalized ledger plumbing) → operational hardening (honest about the no-unattended-2FA gap). Locked design decisions with the user: Path B signals only, $500/trade fixed notional, 1 manual test order before any automation, accepted that IBKR bracket orders can't replicate Path B's EMA-trailing-stop exit rule, no extra safety layer beyond the code-level `DU`-prefix account gate (paper accounts always start `DU`, live accounts `U` — verified directly).

**User explicitly parked implementation** — wants additional research/review before Phase 1 begins. Persisted as `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md` and tagged as ROADMAP Priority #13 ("planned, not started").

---

## Files Changed

| File | Change |
|---|---|
| `docs/claude/design/IBKR_PAPER_EXECUTION_PLAN.md` | **New** — full 4-phase design plan, parked pending further review |
| `docs/claude/stable/ROADMAP.md` | New Priority #13 pointing to the design doc |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 37 (verify a cited source directly rather than trusting a secondhand summary) |

**No code changes, no API changes, no version bump** — pure research and planning.

---

## All Gates Status

Unchanged — no trading-logic, threshold, or verdict changes. Today's work doesn't touch Path A, Path B, or MR at all; it's a design plan for a *future*, separate execution channel (`C_ibkr_paper`) that hasn't been built yet.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority for Path A/MR. The IBKR plan is explicitly parked, not started.

---

## Paper Trading Status (end of session)

Unchanged from Day 96: Momentum Path A 22 open/2 closed, Path B 0 open/0 closed, MR 3 open/25 closed.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS** for Path A and MR. Path B accumulates alongside.
2. IBKR paper-execution plan (`IBKR_PAPER_EXECUTION_PLAN.md`, ROADMAP Priority #13) is **parked** — do not start Phase 1 unless the user explicitly raises it again, since they want to do additional research/review first.
3. Everything else remains parked: fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap (ROADMAP Priority #11), `/ibkr-scan`, Session 28 audit's remaining lower-priority findings (ROADMAP Priority #10).
