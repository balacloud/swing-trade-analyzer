# Project Status — Day 131 (Nov 23)

**Version:** App v4.70, Backend v2.58 (behavior unchanged; code constant corrected from 2.57), Frontend v4.66. No API change.

---

## What Happened Today

### 1. Session start and "is the Analyze tab good once the data is fixed?"
Ran `/sta-start` (Day 130 state; paper job last ran Nov 20, discontinued anyway). The user asked whether fixing data provenance makes the first Analyze tab good. Answer: no, data is one of three layers (data, math on the data, rules and wording). Listed what stays open above the data: two engine bugs and (as I then believed) the MR route reading Yahoo directly.

### 2. Plan, and a correction of my own claim
Entered plan mode, read the code. **The MR-route claim was wrong:** `/api/mr/signal` and `/api/mr/scan` already use the provider chain first (`backend.py:3866-3875`, `:3940-3948`); live `curl` showed `dataSource: "DataProvider"`. I had repeated a stale Known Issues line (Days 128-130) without reading the code. No MR code change.
Plan: `docs/claude/design/ENGINE_MISSING_INPUTS_PLAN_DAY131.md`. Opus review: GO WITH CHANGES (11 changes: two false on-card texts, check missing before comparing, a third RSI copy to name, grid with RSI 0, match the baseline by input, `is None` only in Python, and a warning that "Neutral" for missing SPY would loosen verdicts). The user chose the cautious option for SPY.

### 3. The two engine bugs, fixed in both copies
- **Missing RSI** (null/NaN/None) was counted as 50 and passed Strong; a real RSI of 0 also became 50 in JS. Now: unavailable, cannot be Strong, may be Decent when the trend checks are 5+, else Weak. Real 0 kept.
- **Missing SPY** was described as "below its 200-day". Now the result stays Unfavorable (no BUY) but the text says "SPY trend unavailable, treated cautiously".
- Two false texts on the Technical Read card fixed (`TechnicalRead.jsx`).
- Proof: parity grid 86,400 -> 172,800 rows, 0 mismatches; the original rows give identical verdicts to a saved baseline (matched by input); new unit tests (NaN, 0, None, Infinity, SPY None) in both copies; mutation check (fixes stashed: 17,280 parity mismatches, 5,184 false Strongs). Page checker 60/60, UI verify 48/48.
- Version strings: footer v4.64 -> v4.70, `BACKEND_VERSION` 2.57 -> 2.58 (the docs had been ahead of the code).

### 4. Found, not fixed
`run_all_checks.sh` smoke audit has one WRONG row (DRAL RS1, 105 bars shown "a number" instead of N/A). Reproduced on the unchanged code, so it predates today. Logged.

### Files changed
| Area | Files |
|---|---|
| Verdict engine (JS) | `frontend/src/utils/categoricalAssessment.js` |
| Verdict engine (Python) | `backend/backtest/categorical_engine.py` |
| Display text | `frontend/src/components/TechnicalRead.jsx` |
| Tests | `backend/backtest/test_verdict_parity.py` (grid), new `backend/backtest/test_engine_missing_inputs.py`, new `frontend/scripts/missing_inputs_check.mjs` |
| Versions | `frontend/src/App.jsx` footer, `backend/backend.py` `BACKEND_VERSION` |
| Docs | plan file, this file, `KNOWN_ISSUES_DAY131.md`, Golden Rule 69, `ENGINEER.md`, ROADMAP, README, CLAUDE_CONTEXT, status board |

### Review exemptions (`.claude/.review_log.tsv`)
- One `trivial` row today: `version: footer v4.64 to v4.70 and BACKEND_VERSION 2.57 to 2.58 to match docs` (2 code files).
- Plan rows: `IBKR_TRUTH_RUN_PLAN_DAY128.md`, `TRADIER_FALLBACK_RULE_PLAN_DAY129.md`, `ALPACA_PROVIDER_PLAN_DAY129.md`, and today's `ENGINE_MISSING_INPUTS_PLAN_DAY131.md` (6 files, "three passes done").

## All Gates Status
No live forward-test gates (program discontinued Day 113). From `daily_job.py --report`, pulled Nov 23 (last job run Nov 20):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. Check Alpaca's in-session daily bar on a market day (today Nov 23 was one; not done): today's bar, the Data Sources tab for 3 tickers, `cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`.
2. Fix or explain the DRAL RS1 smoke-audit row (short history: the page shows a 52-week RS from 105 bars).
3. Refresh `backend/reference/data_audit_latest.json` (plan, Opus review, stamp).
4. Thin-ETF cases (XDRV.TO, CARS.TO), SOXL.NE, FINN.NE, BRKU volume.
5. Re-measure Twelve Data pressure now that Alpaca is first; unused `rsi_4h` call (#22); Tradier stall retry (#23).
6. Data Sources tab statement audit, then Scan, Sectors, Context; the 117-ticker page audit.
7. Playbook research (#21) and page-layout review (#26).
8. Carried: 🔴 High per-ticker provenance (Day 108).

**Waiting on the user:** Alpaca terms of use; rotate the Twelve Data key; a go-ahead to clear the US OHLCV cache once.
