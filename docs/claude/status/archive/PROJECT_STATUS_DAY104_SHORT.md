# Project Status — Day 104 (August 8, 2026)

## Version: v4.56 unchanged (Backend v2.45, Frontend v4.51) — no app code touched this session

---

## What Happened Today

### 1. Built `/watchlist-report` — a new Claude Code skill for thematic ETF watchlists (freeze-independent, not an STA app feature)
User pasted a 24-ETF IBKR/TWS watchlist (uranium, gold miners, AI infra/power, semiconductors, memory, copper, robotics/AI/quantum, EV/autonomous, space tech, clean edge) and asked for a report identifying catalysts, news, regime, and 10-day earnings risk — regenerated any time the same watchlist is pasted. Built `.claude/commands/watchlist-report.md` (8-step skill: parse → compute readiness indicators → group by theme → bucket by readiness state → per-theme catalyst/regime research (WebSearch) → earnings/event risk → market regime → build Artifact). Deliberately scoped separate from STA's own Sectors tab/Market Phase engine — thematic/niche ETFs don't map onto STA's 11 broad GICS sectors (confirmed with user before building). Published as a durable, living Claude Artifact (same URL updates in place on every re-run), not a live STA feature — no ledger, no automated signal, no buy/sell verdict.

### 2. Made the report actionable — researched sibling-project precedent before designing, per explicit user instruction
User asked how to make the report more useful for a trader without jumping straight to a build. Researched precedent first (Trading Intelligence Hub's Options Sieve gate pattern and Sector Advisory Panel's "alerting, never deciding" rule; STA's own `breakout_detection.py` most-actionable-first bucketing) and proposed the approach back to the user via `AskUserQuestion` before building: readiness bucketing (🟢 Ready / 🟡 Extended / 🔴 Below trend / ⚪ Unclassified) as a *state description, never a verdict* (PERSONA.md Core Principle 2 — risk-framing info, not a signal), plus 4 indicators (RSI(14), relative volume, ATR-based stop%, trend vs. 200-EMA). Both proposals confirmed by the user before implementation.

Found and fixed 2 real design bugs while live-testing the new indicators (not from a symptom report):
- **RSI(14)-alone understated a stretched long-term trend** — SMH/SOXX read RSI≈50-52 (neutral) while +21-23% above their 200-EMA, right after a real "stretched valuations" selloff the catalyst research had independently found. Fixed: "Extended" redefined as `RSI(14)≥65 OR Price/EMA(200)≥+15%` (an OR, not AND).
- **Relative volume's partial-bar problem** — `volume.iloc[-1]` from a same-day fetch is today's volume-so-far, not a completed session's, compared against a 20-day average of *complete* sessions — nearly every ticker read 0.3x-0.9x regardless of real conviction. Same failure family as Golden Rule 39 (paper-trading partial-bar contamination), new shape. Fixed: removed from bucket-gating logic, omitted from the displayed table.

Also found and fixed a rendering bug: the published Artifact rendered near-blank without an explicit `<meta charset="utf-8">` as the file's first line (the report's em-dashes/arrows/middle-dots broke without it) — confirmed by comparing a local `python3 -m http.server` render (garbled but readable) against the published Artifact (nearly empty). Fixed, verified clean on both after.

### 3. Re-sourced the report's indicator data from real IBKR account data, at the user's explicit instruction
User pasted a fresh intraday update of the same watchlist and, mid-update, said to use the IBKR MCP tools directly rather than yfinance, since the watchlist itself is sourced from the user's real IBKR/TWS account. Switched: `get_watchlists` → `get_watchlist` (real `contract_id_ex` per ticker) → `get_price_history` per contract (3-month daily OHLCV) → RSI(14)/ATR(20) computed via STA's own `calculate_rsi`/`calculate_atr_series` (reused, not reimplemented, same DRY discipline as the yfinance path).

**Found a real, non-project-specific bug**: a 24-call parallel batch of `get_price_history` did not reliably preserve call order in its results — two tickers' entire OHLCV series came back transposed relative to their `contract_id`. Caught by cross-verifying every result's own last-close and volume figures against the pasted watchlist's real numbers before using any of it, not by trusting positional order. Re-fetched the ambiguous subset in smaller, well-separated batches to resolve with certainty. New **Golden Rule 42** — the finding generalizes beyond IBKR to any parallel tool-call batch whose results are keyed by which call produced them.

Also caught 2 of my own transcription errors while manually compiling the verified data into a JSON file (COPP/DRAM data accidentally duplicated; DRIV/BOTZ arrays swapped) — found via a programmatic last-close verification script, not by eye, before any of it reached the report.

Updated the Artifact with the verified IBKR data throughout (all 24 rows cross-checked against the fresh paste), corrected the readiness buckets, and fixed one stale narrative figure a table update had left inconsistent (ORBX's Px/EMA50 cited in prose vs. table). **Republish did not render on the Artifact platform** (blank page, no console error) — isolated to a platform-side issue, not a file bug, by confirming a clean local-server render of the identical file. Reported to the user as an open item rather than claimed as done.

### 4. Wrote every real finding back into the skill file itself
`.claude/commands/watchlist-report.md` updated to document: IBKR MCP as the preferred data source (yfinance as fallback), the parallel-tool-result-ordering verification requirement (with the concrete failure mode spelled out), and the blank-render diagnostic procedure (serve locally first to isolate file bugs from platform issues) — so a future run of this skill doesn't repeat any of these three findings from scratch.

---

## Files Changed

| File | Change |
|---|---|
| `.claude/commands/watchlist-report.md` | New skill (built), then iterated: readiness bucketing + 4 indicators, IBKR MCP as preferred data source, parallel-result-ordering verification requirement, blank-render diagnostic procedure |
| `docs/claude/stable/GOLDEN_RULES.md` | New Rule 42 (parallel tool-call results aren't guaranteed to preserve call order — verify before trusting positionally) |

No `backend/` or `frontend/` files touched this session — the watchlist Artifact itself lives in this session's scratchpad (not the repo), consistent with `HOW_STOCK_PICKING_WORKS.html`'s own precedent (Day 100) of a living Artifact that isn't committed app code.

---

## All Gates Status

Unchanged for the 4 live forward-test tracks — nothing in this session touched STA's app code, any entry/exit gate, or any frozen threshold.

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority for the 4 live tracks.

---

## Paper Trading Status (live-pulled via `daily_job.py --report`, 2026-08-08)

| Track | Open | Closed | Win Rate | Profit Factor | Notes |
|---|---|---|---|---|---|
| Momentum Path A | 39 | 16 | 37.5% | 0.8827 | Unchanged from Day 103 — correlated 4-trade cluster still the last real driver, known correlation gap |
| Momentum Path B | 69 | 15 | 53.33% | 1.5871 | Unchanged from Day 103 |
| MR (broad) | 19 | 71 | 76.06% | 4.1386 | Unchanged from Day 103 — still past 70% of its 100-trade bar |
| MR (HUB-65) | 1 | 28 | 50.0% | 1.3668 | Unchanged from Day 103 |

Last job run: 2026-08-07 (job ran once since Day 103's close; no new closed trades landed).

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS for STA itself**, across all four tracks. MR (broad) is closest to its 100-trade bar at 71/100.
2. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit remainder, breakout-alert watcher (ROADMAP #15), Sector Rotation's original-endpoint orchestrator/pass-through fix (offered Day 103, not started).
3. If the `/watchlist-report` skill is used again: check whether the published Artifact URL (`https://claude.ai/code/artifact/03423c12-9a9c-4334-8e32-6b2b822f418e`) is rendering — it was blank at Day 104's close despite a verified-correct file; may resolve on its own or need a fresh publish.
4. SRPS's backtest infrastructure remains reusable tooling only, per Day 103 — not revisited this session.
