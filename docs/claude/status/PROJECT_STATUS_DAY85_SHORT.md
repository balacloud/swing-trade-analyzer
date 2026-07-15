# Project Status — Day 85 (July 15, 2026)

## Version: v4.43 (no bump — reliability fix + display fix + reference doc, not a versioned feature)

---

## What Happened Today

### 1. Backend/frontend reliability fix — `start.sh` didn't detach its processes
User reported the newly-added Breakout Status card (Day 83) showed nothing for CCJ. Investigation found the *actual* root cause was much broader than the breakout card: the backend process had no stdout/stderr file descriptors at all (`lsof` showed only fd 0). `start.sh` ran `python backend.py &` / `npm start &` with no output redirection, inheriting the launching terminal's stdout. When that terminal closed, the backend survived (reparented to launchd/PID 1) but every `print()` call — used throughout the codebase for request-scoped logging, including inside exception handlers — threw `OSError: [Errno 5] Input/output error` and turned into a 500. Confirmed this wasn't breakout-specific: `/api/patterns/<ticker>` failed the same way.
- **Fix:** `start.sh` now runs both processes as `nohup <cmd> >> logfile 2>&1 & disown`, redirecting output to `backend/backend.log` / `frontend/frontend.log` and detaching from the controlling terminal. Backend and frontend both restarted and verified healthy (`/api/breakout/CCJ` returns 200, frontend compiles clean).
- **New Golden Rule 23** codifies this for future backgrounded processes.
- `frontend/frontend.log` added to `.gitignore` (matches the existing `backend/*.log` pattern).

### 2. Breakout NOT_READY status was silently hidden, not shown as "checked"
Root cause above was masking a second, smaller issue: even after the backend was healthy, CCJ's Breakout Status card and header badge still didn't appear — because `App.jsx` explicitly hid the card/badge whenever `status === 'NOT_READY'`. Per the engine's own spec (`BREAKOUT_ENGINE_SPEC.md` §13), NOT_READY is supposed to get a "Muted" badge treatment, not be hidden — hiding it made "checked, nothing interesting" indistinguishable from "broken/never ran," which is exactly the confusion that started this investigation.
- **Fix:** `BREAKOUT_BADGE_CONFIG` gained a `NOT_READY` entry (muted gray). Both render sites — the ticker-header badge and the full Breakout Status card — now show it instead of hiding it.
- **Deliberately left alone:** the Scan tab's batch badge column (20-row table) still collapses NOT_READY and a failed fetch into a shared "—" dash. Flagged to the user as the same bug class, not yet requested to fix — added to ROADMAP as a low-priority optional item (#13).

### 3. TradingView screener research + new reference doc
User asked what Fable said about the TradingView screener integration, and separately asked about live market-data delay. Findings:
- Confirmed (external research, `shner-elmo/TradingView-Screener` library docs/discussions) that without passing an authenticated `sessionid` cookie, the library returns delayed data (~15 min) even for tickers TradingView shows real-time for free on its own website. STA's `Query()` calls pass no cookies, so all scan data is delayed.
- User decided **not** to wire up cookie-based real-time auth — the delay costs nothing for STA's EOD-based indicators, and it would add an account-session-credential dependency (expiring `sessionid`, unofficial/unsupported use, ongoing manual refresh) for no practical benefit. No code change from this thread.
- Wrote `docs/claude/design/TRADINGVIEW_SCREENER_IMPLEMENTATION.md` — a self-contained reference doc (file map with line numbers, request-flow diagram, Config C filter table, 8 documented gotchas including the real `order_by()`-replaces-not-stacks bug from Day 83) intended to be portable to another project.

### 4. New roadmap item queued (not started)
User wants a personalized screener built around a curated ticker list they maintain in Notion, instead of (or alongside) TradingView's market-wide filter criteria. Not yet scoped — added as ROADMAP priority #2, pending a Notion connection and a design decision on how the list feeds the existing `scan_queries.py` pipeline (the Nirmal watchlist feature is the closest existing precedent).

---

## Files Changed

| File | Type | Content |
|------|------|---------|
| `start.sh` | Modified | Both `start_backend()`/`start_frontend()` now use `nohup ... >> logfile 2>&1 & disown` |
| `.gitignore` | Modified | Added `frontend/frontend.log` |
| `frontend/src/App.jsx` | Modified | `BREAKOUT_BADGE_CONFIG` gained a `NOT_READY` entry; removed the `status !== 'NOT_READY'` exclusion at both render sites (ticker-header badge, Breakout Status card) |
| `docs/claude/design/TRADINGVIEW_SCREENER_IMPLEMENTATION.md` | Created | Reference doc: screener implementation, file map, gotchas, portable pattern |
| `docs/claude/stable/GOLDEN_RULES.md` | Modified | New Rule 23 (backgrounded servers need output redirection); "Last Updated" bumped |
| `docs/claude/stable/ROADMAP.md` | Modified | New priority #2 (Notion screener), new optional item #13 (Scan tab NOT_READY ambiguity), version-line note, "Last Updated" bumped |
| `README.md` | Modified | Current Priorities list mirrors ROADMAP's new item; header day bumped |

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
| — | **Backend/frontend process reliability** | **✅ DONE (Day 85)** — `start.sh` now detaches both servers; Golden Rule 23 added |
| — | **Breakout NOT_READY display fix** | **✅ DONE (Day 85)** — muted badge shown instead of hidden, matches spec §13 |

Paper trading itself: still accumulating, expected to take months — this session found nothing that changes that estimate.

---

## Next Session Priorities

1. **Let paper trading accumulate** — nothing to build; `daily_job.py --report` to check in.
2. **Scope the personalized Notion-based screener** — connect to the user's Notion, understand the ticker list's structure, decide how it feeds the scan pipeline.
3. **Decide fundamentals mitigation** — 40% live↔backtest disagreement, still pending.
4. **Confirm SimFin key rotation.**
5. **Breakout Plan Phase 1** (scan preset) — needs explicit user go-ahead.
6. N4 Market Phase synthesis, `/ibkr-scan` skill, Value Tab Phase 2, Price Structure Phase 2, N3 gap-fill, Canadian Analyze page — queued.
7. (Optional, low priority) Scan tab batch breakout badges: distinguish NOT_READY from a failed fetch.
