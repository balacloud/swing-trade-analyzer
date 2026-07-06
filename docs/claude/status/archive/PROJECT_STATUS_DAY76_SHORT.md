# Project Status — Day 76 (May 18, 2026)

## Version: v4.36 (Backend v2.35, Frontend v4.35, Backtest v4.18, API Service v2.11)

---

## What Happened Today

### 1. Session Start Protocol Failure — Diagnosed and Fixed

Discovered that the session start protocol was not being followed correctly. GOLDEN_RULES.md was being read but CLAUDE_CONTEXT.md (the orchestrating file that defines the full 4-file checklist) was being skipped. This caused jumping to raw yfinance calls without checking the DataProvider architecture.

**Fix:** Updated MEMORY.md to point to CLAUDE_CONTEXT.md as the true first read. Added GOLDEN_RULES Rule 17. Saved feedback memory `feedback_session_start_protocol.md`.

### 2. N4 Market Phase Synthesis — Research Phase

Researched data availability and designed the 5-phase framework before building.

**Key finding:** `^SPXA200R` (S&P breadth tracker) is dead on yfinance. RSP/SPY ratio is the correct breadth proxy (RSP = equal-weight S&P; underperforming = narrow/mega-cap-driven rally).

**Correct data architecture confirmed:**
- Price signals (SPY, VIX, sector ETFs, RSP) → DataProvider OHLCV chain (TwelveData → yfinance → Stooq)
- Macro signals (yield curve, FEDFUNDS, CPI) → already computed in `cycles_engine` + `econ_engine` via FRED
- N4 is a synthesizer on top of existing infrastructure — no new data sources needed

**5-phase framework designed:**

| Phase | SPY | VIX | Breadth (RSP/SPY) | Sectors |
|-------|-----|-----|-------------------|---------|
| Bull Rally | Above 200SMA, rising | <20, falling | Rising >2% | Growth leading >5% |
| Late Bull | Above 200SMA, slowing | 20–25, rising | Flat | Mixed |
| Profit Taking / Distribution | Topping/flat | Rising | Falling >2% | Defensive emerging |
| Correction | Below 200SMA | >25 | Falling | Defensive leading |
| Recovery | Recovering from lows | Falling | Expanding | Growth re-emerging |

**Current market snapshot (May 18):** SPY +9.8% above 200 SMA, VIX 18.4 (slightly rising), Growth sectors +13.2% vs Defensive -1.1%, RSP/SPY -4.7% (breadth narrowing) → **Late Bull** phase.

**Not yet built.** Research validated. Build is next session.

### 3. Two Project Skills Built

| Skill | File | Purpose |
|-------|------|---------|
| `/sta-start` | `.claude/commands/sta-start.md` | Automates full session start protocol — reads 5 files in order, outputs formatted summary |
| `/sta-end` | `.claude/commands/sta-end.md` | Automates full session close protocol — 9 steps, creates all docs, commits and pushes |

---

## Files Changed Today

| File | Type | Change |
|------|------|--------|
| `.claude/commands/sta-start.md` | Created | Session start skill |
| `.claude/commands/sta-end.md` | Created | Session end skill |
| `docs/claude/stable/GOLDEN_RULES.md` | Modified | Rule 17: Read CLAUDE_CONTEXT.md first at session start |
| `memory/feedback_session_start_protocol.md` | Created | Feedback memory: full startup checklist |
| `memory/MEMORY.md` | Modified | Updated FIRST THING pointer to CLAUDE_CONTEXT.md |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) |
| Gate 4 | MR standalone (62.9% WR, PF 1.26) | ✅ PASSED (Day 70) |
| Gate 5 | Combined momentum+MR (1.9% overlap, 0.274 corr) | ✅ PASSED (Day 75) |

**All gates cleared. Paper trading is unblocked.**

---

## Next Session Priorities

1. **Paper trading** — PRIMARY FOCUS. All gates cleared.
2. **Build N4: Market Phase synthesis** — Research done. Architecture confirmed. Use DataProvider for price signals, consume existing context engines for macro. New file `market_phase_engine.py` + `/api/market/phase` endpoint.
3. **Value Tab Phase 2** — AV earnings history, interest coverage, EV/EBIT, ROE 5yr median.
4. **Price Structure Phase 2** — HH/HL/LH/LL engine using `find_pivot_points()`.
