# Project Status — Day 78 (July 5, 2026)

## Version: v4.36 (Backend v2.35, Frontend v4.35, Backtest v4.18, API Service v2.11)
*No code changes this session — full-system audit + remediation planning.*

---

## What Happened Today

### 1. Fable 5 Full-System Review (Good / Bad / Ugly)

Deep review of intent, code, docs, and live-market viability by Claude Fable 5 — read the backtest engine (`backtest_holistic.py`, `trade_simulator.py`, `metrics.py`, `categorical_engine.py`, `simfin_loader.py`, `mr_simulator.py`), verdict logic (both JS and Python), and MR engine end-to-end.

**Verdict:** engineering honesty is real (point-in-time fundamentals, conservative fills ordering, self-flagging sanity checks). But the backtested edge (Config C PF 1.61) is **likely overstated** for live trading. Honest live expectation: PF ~1.1–1.3.

**Key findings:**

| Severity | Finding |
|----------|---------|
| Ugly | 60-ticker backtest universe hand-picked in 2026 = survivorship bias (NVDA, LLY, PLTR... — the winners, chosen with hindsight) |
| Ugly | Same walk-forward window reused across ~20 tuning sessions (Days 55–75) — OOS is no longer OOS |
| Bad | MR backtest + Gate 5 have **zero transaction costs** (momentum backtest has them) — PF 1.26 is gross |
| Bad | Stop fills modeled at exact stop price — gap-downs ignored (worst for MR, which buys oversold stocks) |
| Bad | t-test assumes iid trades (p=0.002 overstated); Sharpe hardcodes 25 trades/yr; max DD 52.6% is a modeling artifact |
| Bad | RS threshold contradiction: default (simple) view requires RS ≥ 1.2 — never validated by the flagship backtest (which used 1.0) |
| Bad | Backtest fundamentals (SimFin quarterly ×4) ≠ live fundamentals (Finnhub TTM) — live Config C ≠ backtested Config C |
| Hygiene | SimFin API key hardcoded in `simfin_loader.py:20` (in git history — needs rotation); `backend/venv/` tracked in git; `/api/health` reports '2.23' vs v2.35; dead components (`DecisionMatrix.jsx`, legacy scoring engines) |

### 2. Fable Review Remediation Plan Created

`docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` — self-contained, Sonnet-executable, 6 phases:
- **P0:** Freeze + pre-register config (resolve RS 1.0/1.2 first) — BEFORE paper trades are logged
- **P1:** Repo hygiene (key, venv, version string, dead code)
- **P2:** Backtest integrity (MR costs, gap-aware fills, scipy stats + block bootstrap, JS↔Python parity grid)
- **P3:** Backtest↔live coherence (fundamentals mismatch diagnostic, silent RS fallback fix)
- **P4:** Survivorship-free re-validation (SimFin universe, pre-committed interpretation criteria)
- **P5:** Paper-trading instrumentation (entry slippage logging, regime snapshots)

Paper trading starts immediately after remediation Session 1 (freeze) — Phases 2–5 run in parallel, don't block trade logging.

### 3. Breakout Trading Inventory + Enhancement Plan Created

Repo sweep confirmed breakout trading IS the core momentum entry model (VCP/Cup&Handle/Flat Base pivots, `check_breakout_quality()`, dual entry, backtested in Config B/C). Gaps: no near-pivot scan preset, no at-pivot flags in scan results, no EOD breakout watch, breakout-confirmed-only entries never isolated.

`docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` — 4 phases with a gating table:
- **P0:** Config D/E backtest (confirmed-only vs anticipatory-only vs mixed) — freeze-compatible, gated on remediation P2
- **P1:** "Near Breakout" scan preset (needs user OK during freeze)
- **P2–P3:** At-pivot scan badges + `/breakout-watch` skill (post-freeze)
- **P4:** pointer to N3 gap detection

### 4. GOLDEN_RULES Rule 18 Added

"Reused OOS is not OOS — freeze before forward test." Captures the review's core methodological lesson.

## Files Created/Changed Today

| File | Type | Content |
|------|------|---------|
| `docs/claude/design/FABLE_REVIEW_REMEDIATION_PLAN.md` | Created | 6-phase remediation plan, Sonnet-executable |
| `docs/claude/design/BREAKOUT_ENHANCEMENT_PLAN.md` | Created | 4-phase breakout plan with gating table |
| `docs/claude/stable/GOLDEN_RULES.md` | Modified | Rule 18 (reused OOS) |
| `docs/claude/stable/ROADMAP.md` | Modified | Priority order updated (remediation #1) |
| `README.md` | Modified | Roadmap mirror (current priorities) |
| `docs/claude/CLAUDE_CONTEXT.md` | Modified | Day 78 state, priorities, summaries |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) |
| Gate 4 | MR standalone (62.9% WR, PF 1.26) | ✅ PASSED (Day 70) — ⚠️ Day 78: gross of costs, net TBD (remediation Task 2.1) |
| Gate 5 | Combined momentum+MR (1.9% overlap, 0.274 corr) | ✅ PASSED (Day 75) — ⚠️ Day 78: gross of costs, net TBD |
| — | Survivorship-free re-validation | ⏳ NEW — remediation Phase 4 |

**Paper trading unblocked — but config must be frozen + pre-registered first (remediation Session 1).**

---

## Next Session Priorities

1. **Fable Remediation Session 1** — Task 0.2 (RS decision) → Task 0.1 (pre-registration) → Phase 1 hygiene. Then paper trading starts.
2. **Paper trading** — PRIMARY FOCUS once config is frozen.
3. **Remediation Sessions 2–3** — MR costs, gap fills, stats, parity grid.
4. **Breakout Plan Phase 0** — Config D/E backtest (after remediation Phase 2).
5. **Build N4 / `/ibkr-scan` / Value Tab P2 / Price Structure P2** — queued behind the above.
