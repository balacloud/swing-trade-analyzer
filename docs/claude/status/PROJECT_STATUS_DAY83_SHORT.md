# Project Status — Day 83 (July 12, 2026)

## Version: v4.42 (Backend v2.37, Frontend v4.38, Backtest v4.19, API Service v2.11)
*Covers everything since the Day 81 status file — Day 82 had no dedicated status doc (see CLAUDE_CONTEXT.md's Day 82 narrative summary), so this consolidates Day 82's work plus this session's continuation.*

---

## What Happened

### 1. Breakout Enhancement Plan — essentially complete (Day 82)
- **Phase 0**: Config D (confirmed-breakout-only entries) backtested to **0 trades** on both IS and OOS — a genuine, root-caused finding, not a bug: `pattern_detection.py`'s confidence score measures pre-breakout base quality, which structurally can't coexist with `broken_out` status. Config E (anticipatory-only) captured 83–90% of Config C's real trades. Verified Config C's own numbers unchanged before/after. Full writeup: `docs/claude/versioned/BREAKOUT_CONFIG_D_BACKTEST_DAY81.md`.
- **Phases 2–3**: `/api/breakout/batch` endpoint (`breakout_routes.py`), a "Breakout" badge column on the Scan tab, and `.claude/commands/breakout-watch.md` — all built and verified in a real headless-Chromium session.
- Only Phase 1 (near-breakout scan preset) remains, gated on explicit user go-ahead.

### 2. Fable process/hygiene audit (Day 82)
User-requested holistic audit (goal fidelity, progress honesty, process bloat, codebase hygiene). Full report: `docs/claude/design/FABLE_AUDIT_DAY82_PROCESS_AND_DECLUTTER.md`. User approved 4 of 5 recommendation buckets:
- **Git risk items fixed**: `frontend/node_modules` (40,801 files) was tracked — untracked + gitignored. `backend/providers/alphavantage_provider.py` (live production provider) was untracked — now tracked. Checked and rejected the audit's claim that `fmp_provider.py` is dead code — verified it's a deliberate placeholder, still imported.
- **Stale docs reconciled**: `KNOWN_ISSUES_DAY81.md`, `MEMORY.md`, `PAPER_TRADING_PREREGISTRATION.md` corrected. `BACKEND_VERSION` drift caught and fixed (code said `2.35`, docs claimed `2.38`).
- **Safety nets added**: dead-man switch in `/sta-start` (warns if the paper-trading launchd job hasn't run in >3 days), automatic ledger backup after every `daily_job.py` run (30-copy rolling retention), time-to-50-trades estimate (~7 months MR, ~2.2 years momentum at backtest-implied rates — highly uncertain, re-estimate after 4-6 weeks of real data).
- **Dead code deleted**: `forward_tracker.py` + 3 orphaned routes, 5 old snapshot files, 12 one-shot scripts, a redundant backup zip, ~21 scratch artifacts.
- Declined by explicit user choice: consolidating the Golden Rules/doc-rotation process itself — deferred as a bigger, separate decision.

### 3. Data-source review — 5 bugs fixed + shared cross-process state (this session)
A light-touch Fable audit of the data-provider chain (TwelveData/Finnhub/AlphaVantage/yfinance) found and the user approved fixing all 5:
- Cache period mismatch, an uncached MR signal route, AlphaVantage rate-limiter token waste (`_check_availability()` was consuming a token on every non-HTTP check via `check_rate_limit()`, wasting 1 of every 3 tokens), uncached VIX quotes, and dead Stooq provider code removed (Stooq itself died earlier and was already out of the active chain).
- **Architecture gap found and fixed**: the rate-limiter and circuit-breaker were in-memory, per-process state. The Flask backend and the separate `daily_job.py` paper-trading process were silently *not* sharing rate-limit/circuit-breaker state with each other — each thought it had a fresh budget. Rebuilt `circuit_breaker.py` and `rate_limiter.py` on a shared SQLite store (`backend/data/provider_state.db`) so both processes see the same state. **New Golden Rule 22** codifies this lesson (see GOLDEN_RULES.md).

### 4. UI cleanup: removed Bottom Line Card, added Breakout status to Analyze page (this session)
User feedback (with screenshot): the Bottom Line Card duplicated the verdict (rendered 3x on one page — Verdict Card, Bottom Line's own banner, Categorical Assessment's "Why This Verdict?" footer) and its bullets just reworded facts the Categorical Assessment card already shows. Verified via code read it was a self-contained leaf component, safe to delete outright — deleted (`BottomLineCard.jsx`, 480 lines), its `HOLDING_PERIODS` config relocated into `App.jsx` (its only other consumer).

Separately: the single-ticker breakout endpoint (`/api/breakout/<ticker>`, live since Day 78) had never been wired to the Analyze Stock page — only the Scan tab's batch column used it (Day 81). Added `fetchBreakout()` to `api.js`, wired as a non-blocking parallel fetch alongside the existing MR signal fetch, surfaced two ways: a compact badge in Simple Checklist view's header, and a dedicated card in Full Analysis view (in the slot Bottom Line vacated). Verified in a real browser session — zero console errors, both views confirmed.

### 5. Deep Fable audit: Analyze page cards, Scan Market tab, Tradier API evaluation (this session)
Three parallel dispatches at the user's request, explicitly split rather than combined. Findings synthesized (with two verification corrections made directly against the code, not taken on the audit's word) into a single actionable document: **`docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`**. Not yet triaged or executed — documentation only, per explicit user request ("first document this... so sonnet can take and run with it"). Headline findings:
- **Real bug, confirmed true**: Trade Setup Card's entry-strategy display re-implements `riskRewardCalc.js`'s stop-price math inline *without* the `Math.max(0.01, ...)` floor the shared utility has — can display a negative stop price.
- **Real bug**: the Scan tab's `'best'` strategy branch calls `order_by('relative_volume_10d_calc', ...)` *after* `scan_queries.build_best_query()` already set `order_by('ADX', ...)` — `order_by()` replaces rather than adds to the sort, so the Scan tab UI and the automated paper-trading engine can see different top-50 candidate sets.
- **Correction made to the raw audit**: it claimed MR Signal Card shows entries from the null-edge, unrestricted MR config (PF 0.99) — verified false by reading `mean_reversion.py` directly; the live gate is already the correct PF-1.16 config (fixed Day 81). The real, much smaller issue is just two stale display-label strings.
- **Tradier evaluation** (12 live API calls against the user's newly-added key): confirmed production-tier brokerage token, 120 req/min. OHLCV good (split- but not dividend-adjusted). Quotes work for stock + index symbols (`VIX` as plain symbol). Fundamentals (beta tier) do NOT close STA's existing gaps (roic/revenueGrowth/epsGrowth/margins/marketCap all absent). Options data is the standout (full Greeks, OI, IV) but out of scope for STA (belongs to OptionsIQ). A concrete `TradierProvider` build spec (as an OHLCV/quote fallback, reliability-only, freeze-compatible) is in the fix-plan doc.

---

## Files Changed

| File | Type | Content |
|------|------|---------|
| `backend/providers/circuit_breaker.py` | Modified | Shared SQLite-backed state (was in-memory, per-process) |
| `backend/providers/rate_limiter.py` | Modified | Shared SQLite-backed state (was in-memory, per-process) |
| `backend/providers/alphavantage_provider.py` | Modified | Fixed rate-limiter token waste in `_check_availability()` |
| `backend/cache_manager.py` | Modified | Cache period mismatch fix, VIX quote caching |
| `backend/providers/orchestrator.py` | Modified | Uncached MR signal route fix, dead Stooq removal |
| `backend/backend.py` | Modified | BACKEND_VERSION → 2.37; supporting changes for the above fixes |
| `frontend/src/components/BottomLineCard.jsx` | Deleted | 480 lines — confirmed redundant, self-contained leaf component |
| `frontend/src/App.jsx` | Modified | BottomLineCard removed; breakout badge (Simple view) + card (Full Analysis view) added; `HOLDING_PERIODS` relocated in |
| `frontend/src/services/api.js` | Modified | New `fetchBreakout()` for single-ticker Analyze page use |
| `frontend/src/utils/riskRewardCalc.js` | Modified | Minor (see commit `8118c9ee`) |
| `docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` | Created | Synthesized 3-audit fix plan, 5 groups (A-E), not yet executed |
| `docs/claude/stable/GOLDEN_RULES.md` | Modified | New Golden Rule 22 — per-process state sharing |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) — hindsight-universe, historical |
| — | Survivorship-free re-validation | ✅ DONE (Day 79) — Config C PF 1.40, MR liquidity-restricted PF 1.16, both unconfirmed |
| — | Fable Remediation Plan | ✅ ALL 5 PHASES COMPLETE (Day 80) |
| — | Automated paper trading engine | ✅ BUILT AND LIVE (Day 81) — accumulating trades daily, unattended |
| — | Breakout Enhancement Plan | ✅ Phases 0, 2-3 DONE (Day 82) — only Phase 1 remains, gated on approval |
| — | Fable hygiene audit | ✅ DONE (Day 82) — 4 of 5 buckets fixed |
| — | Data-source review | ✅ DONE (Day 83) — 5 bugs fixed, cross-process state architecture fixed |
| — | Analyze/Scan/Tradier code-quality audit | ✅ Documented (Day 83) — fix plan written, NOT yet executed |

Paper trading itself: still 0 closed trades as of last check — unchanged, expected to take months (see estimate above).

---

## Next Session Priorities

1. **Let paper trading accumulate** — nothing to build; `daily_job.py --report` to check in.
2. **Triage the UI Code Quality Fix Plan** (`docs/claude/design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`) — decide which of Groups A-E to execute now vs. later. Group A (6 real bugs) is the natural starting point if picking one group.
3. **Decide fundamentals mitigation** — 40% live↔backtest disagreement, still pending (align live-to-SimFin or backtest-to-TTM).
4. **Confirm SimFin key rotation.**
5. **Breakout Plan Phase 1** (scan preset) — needs explicit user go-ahead.
6. N4 Market Phase synthesis, `/ibkr-scan` skill, Value Tab Phase 2, Price Structure Phase 2, N3 gap-fill, Canadian Analyze page — queued.
7. **(Deferred, user's own call)** Consolidating Golden Rules/doc-rotation process.
