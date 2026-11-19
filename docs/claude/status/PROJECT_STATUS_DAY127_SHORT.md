# Project Status — Day 127 (Nov 17–19)

**Version:** App v4.67, Backend v2.56, Frontend v4.64 (from v4.66 / v2.55 / v4.63)

---

## What Happened Today

The user's worry: "AI is non-deterministic, if I keep running the audit will I keep finding these things?" Answer: automate the checks that exist, add no new rules, and audit the data itself before trusting the page audit.

### 1. Statement Audit follow-through (117-ticker universe)
Universe runs went 177 → 61 → ~2 WRONG. Root causes fixed: one price basis (Twelve Data `adjust=all`), cache rules (stored period must cover the request, no short-over-long overwrite, Tradier 45-min TTL, per-ticker lock), stale fallback must cover the requested period, NaN-safe `price52wAgo`, `/api/stock` 503 vs 404, fundamentals retry. Dump script relaunches the browser after a crash.

### 2. Zone and Buy fixes
PLD: the zone the price is inside is now the nearest support (distance 0). **Then the persona decision:** when the last completed close is inside the nearest support zone, the Buy is that close (`meta.entryBasis`), not the zone top, which sat above the market on AMD/SOXL.NE/FCX/ETN/PLD (up to +8.9%). One backend function (`sr_plan.plan_entry`), A10 and the audit re-derive it, validation check updated. AMD: Buy 503.41, R:R 0.53 (was 0.2). Opus review changes all applied.

### 3. Automation, no new rules
`run_all_checks.sh [--quick]` and a nightly universe audit (`nightly_audit.sh`, launchd `com.sta.nightly.audit`, weekdays 18:00 ET; the app must be running). No per-edit or pre-commit hooks (user: no slow edits).

### 4. Data Source Audit Round 2 — plan + step 0
The page audit cannot catch a wrong provider close. Plan (`DATA_SOURCE_AUDIT_ROUND2_PLAN_DAY127.md`, Opus GO WITH CHANGES, all applied). Step 0 built: both audit scripts run on any ticker list; class from `data_quality.audit_class`; 117 classified (47 US stock, 19 US leveraged, 15 CA ETF, 13 CA stock, 13 US ETF, 8 CDR, 2 CA leveraged). Tradier: live quote is already first for US; history stays on dividend-adjusted sources (option A).

### 5. Playbook research prompt (draft v2)
`PLAYBOOK_RESEARCH_PROMPT_DAY127.md`: macro event → sector → stock over 1926–today, then a lookup for the user's 117 tickers; survivorship warning, graded findings. Not run.

### Files changed (main)
| Area | Files |
|---|---|
| Buy / zone | `backend/sr_plan.py`, `backend.py`, `simple_sr.py`, `validation/engine.py`, `frontend/src/components/PullbackPlan.jsx`, `utils/riskRewardCalc.js`, `App.jsx`, `scripts/lib/analyzeChecks.js` |
| Audits | `audit_cards.py`, `test_audit_cards.py`, `backtest/audit_data_sources.py`, `audit_vs_ibkr.py`, `data_quality.py`, `backtest/test_data_quality.py` |
| Automation | `run_all_checks.sh`, `nightly_audit.sh`, `audit_summary.py`, `audit_universe.txt`, `audit_smoke.txt` |
| Docs | `INSIDE_ZONE_BUY_PLAN_DAY127.md`, `SR_INSIDE_ZONE_PICK_PLAN_DAY127.md`, `DATA_SOURCE_AUDIT_ROUND2_PLAN_DAY127.md`, `PLAYBOOK_RESEARCH_PROMPT_DAY127.md` |

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-19:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. **Data Source Audit Round 2, step 1 onward:** fetched-vs-computed inventory (all `backend/*.py`), truth-free audit on the 117, IBKR truth for tickers with a watchlist contract id (list the missing ones first), Tradier measurement and the user's decision, tab statement audit + Playwright rare states, framework Part 8.
2. Then the 117-ticker page audit with "data verified" meaning something; audit Scan, Sectors, Context tabs.
3. Playbook research: user reviews the prompt, run it, review findings, plan, Opus review.
4. Optional: Context tab trim; formal Coherence Audit (ask before any Fable run); untracked-file housekeeping.
5. Carried: 🔴 High per-ticker provenance (Day 108); the two engine bugs (RSI `|| 50`, missing SPY → Unfavorable); page-level horizontal scroll at 390px.
