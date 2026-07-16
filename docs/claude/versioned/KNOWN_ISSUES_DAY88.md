# Known Issues — Day 88 (July 16, 2026)

## Changes from Day 87

**Shipped this session (scoped freeze exception):**
- ✅ Paper trading ledger now visible in the UI — new panel in the Forward Test tab (`AutomatedPaperTradingPanel.jsx`), backed by two new endpoints (`/api/paper-trading/status`, `/api/paper-trading/trigger`). Resolves the "Surface paper-trading ledger in UI" item that was previously queued as optional/low-priority.
- ✅ Manual "Force Run Now" button for catching up a missed scheduled run — wraps the exact same `run_daily_job(force=True)` the launchd job already calls, no new trading logic.

**Freeze status:** unchanged — still in complete feature freeze. This was an explicitly agreed, narrowly-scoped exception (aids observing/operating the paper-trading gate itself), not a resumption of general feature work.

---

## Open Issues

Carried forward unchanged from `KNOWN_ISSUES_DAY87.md` — this session added ledger visibility only, no new bugs found or fixed, no trading-logic changes. See that file for the full list (fundamentals mismatch, Canadian Analyze page, SimFin key rotation, etc.).

### Info: Automated Paper Trading Ledger — Now Visible in UI (Day 88)
**Severity:** Info (milestone)
**Description:** Previously CLI/DB-only (`daily_job.py --report`). Now surfaced in the Forward Test tab via a read-only status panel + manual trigger button. The trigger endpoint is synchronous and can take 10-30+ seconds (live OHLCV fetches + TradingView scan) — no loading-state timeout issues observed in testing, but worth knowing if it ever feels "stuck."
