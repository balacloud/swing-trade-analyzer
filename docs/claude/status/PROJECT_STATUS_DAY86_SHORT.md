# Project Status — Day 86 (July 15, 2026)

## Version: v4.44 (Backend v2.40, Frontend v4.40, Backtest v4.19, API Service v2.11)

---

## What Happened Today

This is a continuation of the same calendar session as Day 85's close — substantial additional work happened after that close, so it gets its own day rather than being folded silently into Day 85's record.

### 1. Master Framework Watchlist — user-tested, gap found, fixed
User ran the new "🏛️ Master Framework Watchlist" Scan tab preset (built and closed out under Day 85) for the first time live. Result: 76/76 tickers matched, real prices, Breakout badges rendering correctly for the top 20 rows — the core deliverable worked. But the summary table's Name/Sector/Change/Volume/Market Cap columns all showed "N/A" or the bare ticker symbol.
- Explained this was identical, pre-existing Nirmal Watchlist behavior (not a regression) — both curated-ticker-list scans bypass TradingView's market-wide query entirely and use `/api/sr/<ticker>` instead, which only ever fetched OHLCV price history, never company metadata.
- User asked "is there a fix?" — investigated and found Volume and Change % were actually free to add (the route already fetches the OHLCV bars needed, just wasn't returning them). Name/Sector/Market Cap genuinely require a separate fundamentals call per ticker (added latency + provider rate-limit cost across 76 tickers).
- User chose the free fix only.

### 2. Fix shipped and verified live
- `backend/backend.py`'s `/api/sr/<ticker>` route now computes and returns `volume` (today's raw share volume) and `change` (day change %) from the OHLCV frame it already fetches — no new provider call.
- `frontend/src/services/api.js`'s `fetchSupportResistance()` field whitelist updated to pass these two fields through (previously silently dropped them even after the backend started returning them — caught before it could ship as a silent no-op).
- `frontend/src/App.jsx`'s `fetchWatchlistCandidates()` now reads `d.volume`/`d.change` instead of hardcoding `null`.
- **Verified live** against the running backend: GEV → volume 526,156 / change -1.0%; CCO.TO → volume 800,496 / change -0.92%; PLTR, TECK-B.TO, NVDA also spot-checked.
- User asked whether the remaining N/A fields (Name, Market Cap) meant "TradingView is unable to fetch it" — clarified this has nothing to do with TradingView: it's never called in this code path at all. The gap is architectural (this endpoint was only ever built to compute price-derived S/R levels), not a data-source failure.

---

## Files Changed

| File | Type | Content |
|------|------|---------|
| `backend/backend.py` | Modified | `/api/sr/<ticker>` now returns `volume`/`change` (computed from the already-fetched OHLCV frame); `BACKEND_VERSION` → 2.40 |
| `frontend/src/services/api.js` | Modified | `fetchSupportResistance()`'s field whitelist now passes through `volume`/`change` |
| `frontend/src/App.jsx` | Modified | `fetchWatchlistCandidates()` reads real `volume`/`change` instead of `null` |
| `docs/claude/design/MASTER_FRAMEWORK_WATCHLIST_SCOPE.md` | Modified | Added user-testing + follow-up-fix sections |
| `docs/claude/versioned/KNOWN_ISSUES_DAY85.md` | Modified | Marked the N/A-columns item partially resolved |
| `docs/claude/status/PROJECT_STATUS_DAY85_SHORT.md` | Modified | Updated next-session priority wording |

---

## All Gates Status

| Gate | Description | Status |
|------|-------------|--------|
| G1-G9 | Original holistic/coherence backtests | ✅ All passed (Day 55-64) — hindsight-universe, historical |
| — | Survivorship-free re-validation | ✅ DONE (Day 79) — Config C PF 1.40, MR liquidity-restricted PF 1.16, both unconfirmed |
| — | Fable Remediation Plan | ✅ ALL 5 PHASES COMPLETE (Day 80) |
| — | Automated paper trading engine | ✅ BUILT AND LIVE (Day 81) — accumulating trades daily, unattended |
| — | Breakout Enhancement Plan | ✅ Phases 0, 2-3 DONE (Day 82) — only Phase 1 remains, gated on approval |
| — | Fable hygiene audit | ✅ DONE (Day 82) |
| — | Data-source review | ✅ DONE (Day 83) |
| — | UI Code Quality Fix Plan | ✅ ALL GROUPS (A-E) DONE (Day 83) |
| — | Backend/frontend process reliability | ✅ DONE (Day 85) |
| — | Breakout NOT_READY display fix | ✅ DONE (Day 85) |
| — | Master Framework Watchlist | ✅ BUILT, USER-TESTED, GAP FIXED (Day 85-86) — Volume/Change now populate live; Name/Market Cap deferred by user choice |

Paper trading itself: still accumulating, expected to take months — this session found nothing that changes that estimate.

---

## Next Session Priorities

1. **Let paper trading accumulate** — nothing to build; `daily_job.py --report` to check in.
2. **Decide fundamentals mitigation** — 40% live↔backtest disagreement, still pending.
3. **Confirm SimFin key rotation.**
4. **Breakout Plan Phase 1** (scan preset) — needs explicit user go-ahead.
5. N4 Market Phase synthesis, `/ibkr-scan` skill, Value Tab Phase 2, Price Structure Phase 2, N3 gap-fill, Canadian Analyze page — queued.
6. (Optional, low priority) Scan tab batch breakout badges: distinguish NOT_READY from a failed fetch.
7. (Optional, low priority) Master Framework Watchlist's Name/Market Cap columns still N/A — would need a separate fundamentals call per ticker; deferred by user choice, revisit only if it becomes annoying in daily use.
