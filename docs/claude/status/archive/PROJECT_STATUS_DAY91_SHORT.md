# Project Status — Day 91 (July 19, 2026)

## Version: v4.48 (Backend v2.44, Frontend v4.43, Backtest v4.19, API Service v2.11)

---

## What Happened Today

Bug-fix session: found and triaged a hub-side audit doc, fixed its 4 top-priority findings. Still within the feature freeze — everything below is a correctness fix to an existing system, not a new feature.

### 1. Found HANDOFF_sta_audit_session28.md (untracked at repo root)
User asked "do you have a handoff document, search for it" at session start. Found a hub-side Fable audit (Jul 17-19) covering doc-vs-code coherence (Part 1, no urgent findings) and a deeper tab-by-tab methodology audit (Part 2 — 5 Fable agents + an Opus persona pass + an external ChatGPT review, 0 CRITICAL / 8 HIGH-equivalent findings). It had never been actioned or logged in the normal doc rotation.

### 2. Scoped and fixed the 4 top-priority findings (user's explicit call: "top priority only" this pass)

| Finding | File(s) | Fix |
|---|---|---|
| Scan tab's "Minervini SEPA/Stage 2 uptrend" mislabel — only checks 2 of 8 real Trend Template criteria | `backend/backend.py`, `frontend/src/App.jsx`, `README.md` | Renamed to "Large-Cap Momentum Filter" with an accurate description. Internal `id: 'minervini'` left unchanged (not user-visible, no downstream break). |
| Sectors tab's false "RS Ratio 100 = market parity" claim + wrong "Data from TwelveData" label (actual source is yfinance) | `frontend/src/components/SectorRotationTab.jsx` | Replaced with an accurate description ("100 = flat vs SPY over the lookback; >100 = outperformed since then") in 3 places; fixed data-source label to yfinance (verified against the actual `yf.download()` call in `backend.py`). |
| Context tab's CPI card showing stale-looking values (3.7%/2.8% vs. real BLS release 3.5%/2.6%) | `backend/econ_engine.py` | **Root-caused as a real bug, not a caching issue as the audit guessed.** A fresh, non-cached fetch reproduced the same wrong number, ruling out cache TTL. Traced to FRED withholding one month's observation (`2025-10-01: "."`), which silently shifted `_yoy()`'s fixed-list-index lookback onto the wrong calendar month once filtered out (June 2026 was being compared to May 2025, not June 2025). Fixed by matching year-ago values by calendar date instead of list position (`_at_months_ago()` helper, also applied to `_trend()` — same bug class, same file). Verified live: now correctly shows 3.5%/2.6%. New Golden Rule 26. |
| Context tab's "ISM PMI (proxy)" card implicitly compared against real-PMI-derived historical stats it was never part of | `backend/econ_engine.py` | Renamed to "Manufacturing Employment (PMI proxy)", removed the fabricated "(proxy PMI>52)" / "48-52" / "<48" band mappings, rewrote the `history`/`source` fields to state plainly this is an employment-count proxy, not calibrated PMI data. |
| Forward Testing's daily replay re-derives stop/target from current code instead of reading back what was locked in at entry | `backend/paper_trading/daily_job.py` | Passed the ledger's already-stored `initial_stop_price`/`initial_target_price`/`max_hold_days` into `simulate_trade()`/`simulate_mr_trade()` as overrides (the override params already existed, just weren't wired up). **Verification caught a live instance of the exact risk being fixed**: KRYS's freshly-recomputed stop (332.18) had already drifted from its stored entry value (333.37) due to an upstream provider data revision — the fix prevents that drift from silently propagating into the ledger. New Golden Rule 27. |

### 3. Verified the paper-trading fix end-to-end, live
Backed up the ledger manually, then force-ran the actual daily job (`daily_job.py --force`) to confirm the fix behaves correctly against the real 11 open positions — none incorrectly closed, `current_stop_price` for KRYS confirmed anchored to the correct stored value (333.37) post-run. This also served as today's paper-trading catch-up run (last scheduled run was Jul 17).

### 4. Paper trading check-in (after the catch-up run)
- **Momentum:** 3 open, 0 closed — 6 new signals queued today (pending activation), still far from the 50-trade bar.
- **MR:** 8 open, 5 closed — same early-stage stats as Day 90's check-in (75% WR / PF ~2.2 territory), no new closes this session.

---

## Files Changed

| File | Change |
|---|---|
| `backend/backend.py` | Minervini scan strategy label/description fix |
| `backend/econ_engine.py` | CPI YoY date-alignment fix (`_yoy`/`_trend`/new `_at_months_ago` helper), PMI proxy relabel |
| `backend/paper_trading/daily_job.py` | Replay now anchors to stored `initial_stop_price`/`initial_target_price`/`max_hold_days` instead of recomputing fresh |
| `frontend/src/App.jsx` | Scan tab dropdown fallback label fix |
| `frontend/src/components/SectorRotationTab.jsx` | 3 label/copy fixes (market-parity claim ×2, data-source label) |
| `README.md` | 1 line — `/api/scan/strategies` example JSON updated to match the renamed strategy |
| `HANDOFF_sta_audit_session28.md` | Newly tracked (was untracked at repo root) |

No API contract shape changes (field names/types unchanged — only string content and computed values were corrected), so no new `API_CONTRACTS_DAY91.md`.

---

## All Gates Status

Unchanged from Day 88/89 — no trading-logic, threshold, or gate criteria changed this session (all fixes were to display labels and replay-integrity plumbing, not to entry/exit rules). See `PROJECT_STATUS_DAY88_SHORT.md` for the full gates table.

**Feature freeze status:** still in effect. Today's changes are bug fixes to already-shipped systems, consistent with the freeze's "bug fixes... only" carve-out — not a resumption of general feature work.

---

## Next Session Priorities

1. **Let paper trading accumulate** — PRIMARY FOCUS. Momentum 3 open/0 closed; MR 8 open/5 closed. Check via the Forward Test tab's status panel or `daily_job.py --report`.
2. Decide fundamentals mitigation (40% live↔backtest disagreement, pending user decision).
3. Confirm SimFin key rotation.
4. N3 gap-fill detection / Value Tab Phase 2 — both need their own design sessions first.
5. `/ibkr-scan` skill, Price Structure Phase 3, Canadian Analyze page — queued.
6. **Session 28 audit's remaining lower-priority findings** (new backlog item #10 in ROADMAP.md) — Value tab badge attribution, Validate/Data Sources status-label honesty, Sectors CTA gating/precision polish, Forward Testing's fee-accounting/silent-failure items, plus the audit's general polish list. Batchable whenever a future session picks this up.
7. **(Not committed, noted for awareness)** README.md's own version footer is still Day 65/v2.33 — a pre-existing staleness issue the audit itself flagged as low-priority/non-urgent. Only the one directly-affected line (`/api/scan/strategies` example) was corrected this session; a full sync is its own future documentation pass, not done here.
