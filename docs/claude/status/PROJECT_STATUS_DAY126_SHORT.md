# Project Status — Day 126 (Nov 14–16)

**Version:** App v4.66, Backend v2.55, Frontend v4.63 (from v4.65 / v2.54 / v4.62)

---

## What Happened Today

The user's rule for the day: "I make the decision as a human, you just help with data." STA is the
analysis engine; verdict words are out, facts are in. Same process as before for each build: a written
plan, an independent Opus review, the build, then three review passes. Plain English throughout.

### 1. Indicator formula audit
The Data Sources "how indicators are calculated" table was wrong. It is now built from one catalog
(`backend/indicator_catalog.py`, 8 rows: SMA 50/200, EMA 8/21, RSI 14, ATR 14, ADX 14, average volume
and RVOL, RS 52W, PEG) and pinned by 36 tests. **No live number changed:** golden snapshot of 816 values
identical, verdict parity 86,400/86,400. Findings logged, not fixed (see Known Issues): paper-trading
stops use a slightly different ATR (0.63% median), ADX copies differ on tie bars, RVOL and average volume
include the forming bar, and the JS ATR copy is dead code that is 10% off.

### 2. Stock-split mechanism (SOXL.NE)
The user asked whether SOXL.NE had split. Confirmed: **3-for-1 on 2026-05-25**; Yahoo and EODHD left the
old prices unadjusted, so ATR, RSI, S&R and the 52-week high were wrong. The equivalent US fund (SOXL on
NYSE Arca) tracks it with correlation 0.986. Built as a framework for every future split:
- `backend/reference/known_splits.json`: the only source for adjusting (one row, each backed by an issuer notice).
- `backend/split_adjust.py`: one classifier (unadjusted / already adjusted / wrong way / ambiguous /
  pending / not applicable), one adjuster (idempotent, returns a copy, never raises, cache stays raw).
- Applied at the single exit of the data layer (`orchestrator._deliver`) and at the six direct-Yahoo
  fallbacks; the 52-week high and low come from the adjusted frame when a split is in the window.
- `data_quality.py`: an uncovered split-sized jump in the last 260 bars is a FAIL; a covered one passes.
- Sweep of 74 cached histories: only SOXL.NE was unadjusted. Live result: 05-22 close 47.28, 52-week high
  74.21, ATR about 2.01. Real bug found and fixed on the first live run: Yahoo timestamps are tz-aware.

### 3. Tabs
Validate Data tab deleted (frontend only; the backend routes are dead code). Forward Test tab hidden.

### 4. Technical Read and volume card turned into facts
- Entry ruler: price against the real **21, 50 and 200-day averages** (replaced the +1/+2 "normal day"
  ticks after the user asked what they meant), with the price always on the scale. Labels stay inside the
  card on a phone.
- The Strong/Developing/Weak headline, its sentence and the "tiles disagree" banner are gone; a facts block
  (trend checks, RSI, vs S&P 500, ADX) is labelled "common rules of thumb, not tested by STA". The engine's
  verdict calculation is untouched (parity-tested); only the display changed.
- Volume card: "Are buyers behind the move?" with Yes / Mixed / No became "Volume behind the move" with
  "N volume signals: a up, b down" and the same three chips.

### 5. Process: three-pass review is now enforced (Golden Rule 64)
The passes were skipped on small follow-ups until the user asked. A Stop hook
(`.claude/hooks/three_pass_check.sh`) blocks the end of a turn when code changed and no review stamp
exists; `/three-pass` runs the passes and stamps (`/three-pass skip` for text-only changes). The passes on the
ruler and volume work found two real bugs ("1 volume signals", phone label overlap) and a 24-render
overlap test (3 widths x 8 tickers) found none.

| File | Change |
|---|---|
| `backend/indicator_catalog.py`, `backtest/test_indicators.py`, `indicator_golden.py`, `indicator_divergence.py` | New: indicator catalog and its tests |
| `backend/split_adjust.py`, `reference/known_splits.json`, `backtest/test_split_adjust.py`, `audit_splits.py`, `audit_vs_ibkr.py` | New: split mechanism, tests, sweep |
| `backend/data_quality.py`, `backtest/test_data_quality.py` | Split-aware jump check (uncovered split = FAIL) |
| `backend/backend.py`, `providers/orchestrator.py` | v2.55; `/api/provenance` indicators; split adjustment at the exits |
| `frontend/src/components/TechnicalRead.jsx`, `utils/technicalReadChecks.js` | Facts block, ruler on real averages, volume tally |
| `frontend/src/components/DataSourcesTab.jsx`, `utils/dataSourcesView.js` | Indicator table, split note |
| `frontend/src/App.jsx`, `services/api.js` | Validate tab removed, Forward Test hidden, SMA50/200 passed to the card |
| `frontend/scripts/` (`analyzeChecks.js`, `ui-verify-checklist.js`, `test_entry_timing.mjs`, `test_analyze_checks.mjs`, `test_data_sources_view.mjs`, `indicator_grid.mjs`) | Page checker A11/A12 extended; new unit tests |
| `.claude/hooks/three_pass_check.sh`, `.claude/commands/three-pass.md`, `.claude/settings.json` | Review gate |
| `docs/` | Plans, reports (`docs/test/Indicators_20261114`, `docs/test/Splits_20261115`), Known Issues, API contracts, Golden Rule 64 |

**Verification (final):** frontend tests 28 + 127 + 36 + 59; backend tests 36 indicators, 81 splits, 69 data
quality; production build compiles (old unused-variable warning only); live page checker 40/40 on AAPL,
SOXL.NE, NVDA, RIVN; ruler overlap test 24/24 clean; verdict parity 86,400/86,400.

---

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-16:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. Commit check and the user's next questions (the user said more questions follow).
2. Optional follow-ups (none urgent): weekly watchlist-wide split scan; Tradier 40% jump guard; delete the
   dead `/api/validation/*` routes; retire the engine verdict labels that no card shows any more.
3. The two engine bugs (RSI `|| 50` counts as a pass; missing SPY → Unfavorable), parity-tested.
4. `/api/stock` forming bar (confirm a mid-day cache miss first).
5. 🔴 High: per-ticker provenance can't tell "never checked" from "just failed" (Day 108).
6. Page-level horizontal scroll at 390px.
