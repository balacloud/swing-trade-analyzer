# Project Status — Day 105 (August 11, 2026)

## Version: v4.56 → v4.57 (Backend v2.45 → v2.46, Frontend v4.51 → v4.52)

---

## What Happened Today

### 1. Fixed a real Sectors-tab staleness bug (user-reported, not from a symptom guess)

User reported the Sectors tab "looks stale" and that "Refresh Session" wasn't reflecting proper info. Traced to a real bug, not stale data: the Sectors tab's data (main sector cards, Sub-Industry Watch, SRPS Pullback Screener) is fetched once on mount and held in React state — nothing ever re-fetches it. "Refresh Session" *did* correctly clear the backend's server-side cache, but never told the already-loaded frontend components to discard their stale copy and re-pull. New **Golden Rule 43**.

Fixed in `frontend/src/App.jsx` / `frontend/src/components/SectorRotationTab.jsx` / `frontend/src/services/api.js`:
- "Refresh Session" now also re-pulls sector data and bumps a `sectorRefreshTrigger` that the two lazy-loaded sub-sections (Sub-Industry Watch, SRPS Pullback Screener) watch to discard their own stale `data` and refetch.
- Added a dedicated **🔄 Refresh** button directly in the Sectors tab header — clears only the sector-related backend cache (new `POST /api/cache/clear?type=market` usage via a new `clearMarketCache()` helper) and re-pulls, without "Refresh Session"'s much larger blast radius (full cache wipe + resets ticker input/scan results).
- While fixing this, found and fixed a second, pre-existing instance of the same failure family (Golden Rule 30 territory): the sector-level SRPS Pullback Screener's `sectorsCappedFrom` field has been computed by the backend since Day 102 but the frontend never displayed it. Fixed alongside the new sub-industry version's equivalent field.

Verified live: curl-confirmed the new market-cache-only clear forces a real fresh backend fetch without touching OHLCV cache; browser-confirmed the Refresh button updates "Last refreshed" to "just now" and both sub-sections re-fetch while staying expanded, zero console errors.

### 2. Built the Sub-Sector Pullback Screener (user-requested extension)

User explicitly asked to extend the SRPS discretionary screener (Day 102) from the 11 broad GICS sectors down to the 21 Sub-Industry Watch clusters, citing subjectively good results with the sector-level version so far. Per PERSONA.md, flagged once before building that the mechanical rule set already failed its own pre-registered backtest at the broad-sector level and the sub-industry universe has never been separately tested at all — proceeded since this stays informational-only, same as the sector-level version.

Two judgment calls confirmed with the user before building (bundled via `AskUserQuestion`, both recommended options taken):
- Overlapping clusters (Communication Services, Energy — thin proxies of sectors the broad screener already covers) — included anyway for completeness.
- Proxy-only clusters (Gold Miners/GDX, Biotech/XBI — the proxy ETF IS the theme, empty curated ticker list) — screened directly on the proxy ETF itself rather than silently skipped.

Built `backend/backend.py`:
- Extracted `_srps_true_rs()` and `_srps_evaluate_candidate()` as shared module-level helpers (Golden Rule 21) — refactored the existing sector-level screener to use them (verified behavior-preserving via live curl before/after) instead of forking the logic a second time.
- New `GET /api/sectors/sub-industry-pullback-screen` — reuses each cluster's own hand-curated `tickers` list from `sub_industry_clusters.py` as candidate sourcing (previously documented there as informational-only; this is the first thing that actually queries them), capped at `MAX_CLUSTERS_PER_REQUEST=8` and a new per-cluster `LIVE_CANDIDATE_LIMIT=8` (Semis alone has 16 curated tickers — a real Golden Rule 25/40 fan-out risk caught in a 3-pass review before shipping, not after).
- New frontend section `SubIndustryPullbackScreenSection` in `SectorRotationTab.jsx`, same collapsible/lazy-load pattern as the sector-level one, plus a new `fetchSubIndustryPullbackScreen()` in `api.js`.

Three-pass review (Golden Rule 41) found two real issues before shipping: the sector-level screener's own `sectorsCappedFrom` display gap (above), and the missing per-cluster candidate cap (Semis' 16-ticker list vs. the sector version's own 8-ticker safety margin). Both fixed same-session.

Live result at ship time: 10 sub-industry clusters were Improving, capped to top 8, 1 qualifying candidate (CGNX, Physical AI/Robotics).

### 3. Cross-checked 3 SRPS/sub-industry screener candidates against STA's own Simple Checklist — 3 for 3 "No Trade"

At the user's request, checked CGNX (from the sub-industry screener) and later GEV + RIVN (today's fresh sub-industry screener run) through the app's own Full Analysis / Simple Checklist engine, not just the SRPS screener's own narrower rules.

All three came back **"No Trade — avoid"** (4/9 or fewer criteria met), each failing on ADX (no real trend), a much worse real Risk/Reward than the SRPS screener's own by-construction 2.5:1 target, and (for CGNX/RIVN) a Failed Breakout flag from a completely separate engine the SRPS rules have no visibility into.

**Real, generalizable finding, not specific to these 3 tickers:** SRPS's target price is *defined* as entry + 2.5×risk — it never checks whether real chart resistance sits anywhere near that price. STA's own Risk/Reward check (against actual support/resistance) came back at 0.48:1 (GEV) and 0.27:1 (RIVN) — nowhere close to 2.5:1. This is a structural gap in how the screener computes "R:R" on every candidate it will ever produce, not a one-off. Logged in KNOWN_ISSUES_DAY105.md and in PERSONA.md's Feedback Log (Core Principle 5 applied to Claude's own new tooling's output, not just a trading-system result).

Investigation only — no SRPS rule changes made (would be exactly the kind of re-tune Golden Rule 18/20 already forbids without a principled, pre-committed reason).

### 4. Ran `/watchlist-report` on a new leveraged-ETF watchlist (not an STA app feature)

User pasted a different real IBKR watchlist ("AI_Leveraged," 8 tickers) and asked to run the existing skill on it, then separately asked for a cross-check against the new Sub-Sector Pullback Screener. Flagged before running that every ticker in this watchlist is a 2×/3× daily-reset leveraged ETF — a different risk profile than the 1× thematic ETFs the skill's readiness framework was built for — and made sure the published report carried that caveat prominently, not just in the footer disclaimer.

Sourced real OHLCV via IBKR MCP (`get_watchlists`→`get_watchlist`→`get_price_history`, cross-verified each result's identity against the pasted watchlist's own last-close before trusting it — Golden Rule 42), researched all 8 themes (including correcting my own initial misreading of `QPUX` as a "quant" fund when its real holdings are quantum-computing names), and published a new, separate Artifact (distinct from the existing AI Supply Chain ETF report). New Golden Rule 43 note: n/a here, this was clean execution of existing rules, no new lesson.

Cross-check against the Sub-Sector Pullback Screener found only 1 of 8 leveraged tickers' underlying themes had an actual qualifying candidate that day, with 3 more excluded purely by the screener's own top-8 cap rather than genuinely disqualified — reported plainly rather than overstating the day's read.

No `backend/`/`frontend/` files touched by this item — lives in the skill file + this session's scratchpad Artifact only, same convention as Day 104.

---

## Files Changed

| File | Change |
|---|---|
| `backend/backend.py` | New `_srps_true_rs()`/`_srps_evaluate_candidate()` shared helpers; refactored `get_srps_pullback_screen()` to use them; new `GET /api/sectors/sub-industry-pullback-screen` endpoint; `BACKEND_VERSION` 2.45→2.46 |
| `frontend/src/App.jsx` | New `sectorRefreshTrigger`/`sectorRefreshing` state + `handleSectorRefresh()`; `loadSectorRotation()` wired into `handleSessionRefresh()`; footer version 4.51→4.52 |
| `frontend/src/components/SectorRotationTab.jsx` | New `SubIndustryPullbackScreenSection`; `refreshTrigger` prop threaded into `SubIndustryWatchSection`/`SrpsPullbackScreenSection`; new header "🔄 Refresh" button; `sectorsCappedFrom` display added to the sector-level screener |
| `frontend/src/services/api.js` | New `clearMarketCache()`, new `fetchSubIndustryPullbackScreen()` |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 43 (cache-clear ≠ frontend state invalidation) |
| `docs/claude/stable/PERSONA.md` | New Day 105 Feedback Log entry |
| `docs/claude/stable/ROADMAP.md` | New COMPLETE section for the Sub-Sector Pullback Screener |
| `README.md` | Mirrors the ROADMAP addition |

No paper-trading engine, ledger, or frozen threshold touched. No `.claude/commands/watchlist-report.md` changes this session (clean run of already-documented behavior).

---

## All Gates Status

Unchanged for the 4 live forward-test tracks — nothing in this session touched any entry/exit gate or frozen threshold. The new Sub-Sector Pullback Screener is explicitly informational-only, same category as its sector-level sibling — not a forward-test track, no ledger.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority for the 4 live tracks.

---

## Paper Trading Status (live-pulled via `daily_job.py --report`, 2026-08-11)

| Track | Open | Closed | Win Rate | Profit Factor | Notes |
|---|---|---|---|---|---|
| Momentum Path A | 35 | 24 | 41.67% | 0.9697 | Up from 16 closed (Day 103/104) — 8 new closed trades landed |
| Momentum Path B | 85 | 26 | 61.54% | 1.9825 | Up from 15 closed |
| MR (broad) | 8 | 83 | 79.52% | 4.5809 | Up from 71 closed — now 83/100, closest to its bar |
| MR (HUB-65) | 2 | 29 | 51.72% | 1.4306 | Up from 28 closed |

Last job run: 2026-08-10.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS for STA itself.** MR (broad) now 83/100, closest to its 100-trade bar by a wide margin — plausibly clears it within the next few sessions.
2. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit remainder, breakout-alert watcher, Sector Rotation's original-endpoint orchestrator/pass-through fix.
3. **New, freeze-independent, offered-not-required item:** the SRPS screener's (both sector- and sub-industry-level) R:R math is structurally disconnected from real support/resistance (see KNOWN_ISSUES_DAY105.md) — 3-for-3 candidates checked so far failed STA's own fuller engine. Not urgent (screener is explicitly informational, disclaimer already covers this), but worth fixing if the screener keeps getting used for real judgment calls.
4. If `/watchlist-report` is used again on a leveraged-ETF watchlist, the leverage-decay handling built ad hoc into this session's AI_Leveraged report (a dedicated warning band, not just a footer line) could be promoted into the skill file itself as a documented pattern — not done this session since it was only exercised once.
