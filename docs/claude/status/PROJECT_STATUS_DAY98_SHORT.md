# Project Status — Day 98 (July 24, 2026)

## Version: v4.52 → v4.53 (Backend v2.45 → v2.46, Frontend v4.47 → v4.48, Backtest v4.19 → v4.20, API Service v2.11 unchanged)

---

## What Happened Today

User brought an external AI tool's "buy the 5% dip, sell on recovery" dashboard idea, sourced from a sibling project's own curated 65-ticker watchlist ("HUB-65" — semis, uranium/nuclear, fintech, China-EV, thematic ETFs). Recognized this as exactly the project's own already-built, already-validated Connors RSI(2) Mean-Reversion engine, just pointed at a different, curated universe — not a new strategy. Built both a one-shot backtest and a real parallel forward-test track, planned twice (once directly, once explicitly re-planned via a Plan agent with `model: "opus"` at the user's request to "see if new things surface" — which found real corrections, folded into the final approved plan).

### 1. `HUB_UNIVERSE` — single source of truth for the ticker list
Added to `backend/mean_reversion.py` (64 tradeable tickers, VIX excluded — not a tradeable equity; 6 ETFs kept). Also added `HUB_THEME_MAP` (ticker → theme, for backtest interpretability). Mirrored in `frontend/src/App.jsx` as `HUB_WATCHLIST` for the new Scan tab preset — verified programmatically byte-for-byte identical between the Python and JS copies.

### 2. Backtest — `backend/backtest/backtest_hub_mr.py` (new)
Imports (doesn't duplicate) `backtest_survivorship_free.py`'s `run_mr_on_universe()`/`_translate_mr_trades_for_metrics()` and `metrics.compute_metrics()`. Adds two interpretation aids without touching the frozen `metrics.py`: per-theme trade count/PF breakdown, and a distinct-entry-month count alongside the block-bootstrap p-value (fewer distinct blocks on 64 concentrated names = less trustworthy p-value than 400 diversified ones — surfaced, not hidden). Full run: **1,940 trades, WR 57.78%, PF 1.2574, Sharpe 1.5278, p=0.0311 (76 distinct months)**, DRAM correctly skipped as genuinely delisted. **Explicitly documented as selection-biased and not comparable to the survivorship-free baseline (PF 1.16)** — everywhere the number appears (docstring, JSON `meta.caveat`, UI caption, `PAPER_TRADING_PREREGISTRATION.md` §9b).

### 3. Forward test — `variant='mr_hub65'`
`live_signals.get_mr_signals()` gained a `variant='A_frozen'` parameter (backward-compatible). `daily_job.py`'s Step 3 gained a second call against the shuffled `HUB_UNIVERSE` (Golden Rule 25 — randomized per-run so a rate-limit cutoff can't silently starve the same tail tickers every day). New Golden Rule 38: the ledger's `variant` column now carries two different meanings depending on `system` (momentum = gate experiment, mr = universe) — documented explicitly in `ledger.py`'s schema comment and this session's `PAPER_TRADING_PREREGISTRATION.md` §9b addition, specifically so a future read of the column doesn't assume one meaning everywhere.

### 4. Reporting — backend `mrHub` block + distinctly-badged UI card
`/api/paper-trading/status` gained an additive `mrHub` key (pinned to `variant='mr_hub65'`, mirroring `momentumPathB`'s pattern exactly — see `API_CONTRACTS_DAY98.md`). `AutomatedPaperTradingPanel.jsx` gained a "Mean-Reversion (HUB-65)" card with a **teal** "Curated-65 Universe" badge — deliberately different color from Path B's amber "Experimental" badge, since this is a different universe, not a different gate.

### 5. Visible Scan tab watchlist
New "🔬 HUB-65 Watchlist — 64 curated picks" option, same `fetchWatchlistCandidates()` pattern as the existing Nirmal/Master Framework watchlists — no new backend endpoint, no new component.

### Verification (Golden Rule 32 — 3 review passes)
- Isolation test (throwaway SQLite db): broad MR track's pending/stats/cooldowns completely unaffected by HUB-65 additions; a ticker on cooldown in one variant is not blocked in the other.
- Real `daily_job.py --force` run: queued a genuine HUB-65 signal (AFRM, RSI(2)=0.47) plus 2 real Path B momentum signals (JOYY, EBC — Path B's first ever).
- Live `curl` of `/api/paper-trading/status`: `mrHub` key present, correctly isolated from `mr`.
- Live browser check (Forward Test tab): teal card renders correctly, expandable table shows the real AFRM pending row, zero console errors.
- Live browser check (Scan tab): HUB-65 Watchlist option runs a real scan, 63/64 tickers returned (DRAM correctly excluded, consistent with the backtest's delisted-ticker finding), one benign per-ticker console error (DRAM's S&R fetch, same tolerated pattern as any other watchlist).
- Pass 2 (what else calls the changed thing): grepped every `get_mr_signals()` caller — only the module's own `__main__` test block, unaffected by the new default-valued parameter.
- Pass 3 (what other state does this touch): confirmed in `backend.py` that the base `mr` block stays explicitly pinned to `variant='A_frozen'`, so `mr_hub65` trades can never blend into the broad MR numbers.

---

## Files Changed

| File | Change |
|---|---|
| `backend/mean_reversion.py` | New `HUB_UNIVERSE` (64 tickers) + `HUB_THEME_MAP` |
| `backend/backtest/backtest_hub_mr.py` | **New** — HUB-65 backtest script, reuses `backtest_survivorship_free.py`/`metrics.py` helpers |
| `backend/paper_trading/live_signals.py` | `get_mr_signals()` gained `variant` param, backward-compatible |
| `backend/paper_trading/daily_job.py` | Step 3 gained a second, shuffled HUB-65 call + `queued_mr_hub` counter + report line |
| `backend/paper_trading/ledger.py` | Schema comment documenting `variant`'s dual per-system meaning |
| `backend/backend.py` | `/api/paper-trading/status` gained additive `mrHub` block |
| `frontend/src/components/AutomatedPaperTradingPanel.jsx` | New teal-badged "Mean-Reversion (HUB-65)" card, `BADGE_STYLES` object |
| `frontend/src/App.jsx` | New `HUB_WATCHLIST` array + Scan tab dropdown option + dispatch block |
| `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` | New §9b documenting the HUB-65 experiment |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 38 (variant column dual-meaning documentation) |
| `docs/claude/stable/ROADMAP.md` | New Priority #14 (HUB-65, done, accumulating) |
| `docs/claude/stable/PERSONA.md` | Feedback Log entry — recognizing a repackaged idea, backtest-caveat discipline |
| `docs/claude/versioned/API_CONTRACTS_DAY98.md` | **New** — `mrHub` response shape |

---

## All Gates Status

Unchanged for Path A, Path B, and the broad MR track — this session added a new, independent track, it didn't touch any existing frozen threshold. HUB-65 uses the exact same MR gate/exit as the broad track (no re-tuning), just a different candidate universe.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority. HUB-65 is a new experiment, own 100-trade bar, not a freeze exception (same category as Path B).

---

## Paper Trading Status (end of session)

Path A Momentum 22 open/2 closed (unchanged). Path B Momentum 0 open/0 closed, 2 pending (JOYY, EBC — first real signals, will activate next run). Broad MR 3 open/25 closed (unchanged). **HUB-65 MR: 0 open/0 closed, 1 pending (AFRM, RSI(2)=0.47)** — brand new.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS** for Path A, Path B, broad MR, and now HUB-65 MR — all four tracks, each toward its own 100-trade bar.
2. IBKR paper-execution plan (`IBKR_PAPER_EXECUTION_PLAN.md`, ROADMAP Priority #13) remains **parked** — do not start Phase 1 unless the user explicitly raises it again.
3. Everything else remains parked: fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap (ROADMAP Priority #11), `/ibkr-scan`, Session 28 audit's remaining lower-priority findings (ROADMAP Priority #10).
