# Project Status — Day 124 (Nov 12)

**Version:** App v4.64, Backend v2.53, Frontend v4.61 (from v4.63 / v2.52 / v4.60)

---

## What Happened Today

**The Analyze Page Redesign is complete** (Steps 7 and 8, plus two follow-ups). Same process
as Day 123 for each step: a written plan, a Fable plan review, a test-first build, a Fable code
review, live checks, and user sign-off.

### Step 7 — Market backdrop card, Full Analysis by default (`c55e3f38`)
- User decision: **no market verdict.** The Regime band's "Market: Favorable … a good
  environment for new trades" was a judgment. It's replaced by facts: S&P 500 and Nasdaq-100
  long-term (200-day) and short-term (50-day) trend, the biggest 1-day drop in the last 10
  sessions (e.g. SPY −4.41% Nov 5, the largest since Apr 4, 2025), and VIX. It's the first card.
- New backend `index_trend.py` (completed bars only), `/api/market/index/<ticker>`, and a
  `trend` field on `/api/market/spy`. A QQQ failure is isolated to its row.
- Full Analysis is the default view. Simple says "⏸️ No Trade" (was "PASS"). An ETF says
  "Exchange-traded fund (ETF)" (SMH showed "Unknown • Unknown").

### One VIX wording, honest MR figures, backdrop → Context link (`2263edb3`)
- `backend/vix_bands.py`: one display band table for `/api/market/vix` and the Context banner
  ("normal range", not "calm"). The engine (20/30) and phase-grid (20/25) scales stay separate
  on purpose.
- The Forward Test tab shows the MR next-open figures (PF 1.50 / 1.07) under the ledger's
  close-priced ones (`openBasis`). The Scan tab no longer quotes "PF 2.56".
- "More market context →" link from the backdrop to the Context tab.

### Step 8 — page checker, cleanup, docs (`c4d6c460`)
- `ui-verify-checklist.js` rewritten: 8 checks in a pure, unit-tested module
  (`scripts/lib/analyzeChecks.js`, 69 unit checks). It compares the screen with the exact JSON
  the page received, writes a dated report folder, and exits 1 on any failure.
  **Live: AAPL, NVDA, SMH, JPM, RIVN 40/40.** Deliberate breaks (backdrop moved, "PASS"
  restored, MR card emptied) were all caught. `ui-cohesiveness-test.js` (PDFs) fixed. Both
  scripts are tracked in git for the first time.
- One VIX position-size ladder (`getVixPositionMultiplier`). The calculator says "VIX not
  loaded" instead of silently sizing at 1.0×.
- Unused `qualityGates` removed from `scoringEngine.js`.
- Docs: README, DEVELOPER_ONBOARDING (how to run the tests), UI test plan, HOW_STOCK_PICKING_WORKS
  (republished, v3), ROADMAP #17 DONE.

### Header price date (`28c53763`)
- User spotted AVGO at $345.45 on STA vs $361.64 on Google. The header price is the last bar's
  close, but it had no date. It now reads "$345.45 · Nov 11 close", or "intraday, not a close"
  for a bar dated today before 16:30 ET (`/api/stock` doesn't drop the forming bar itself).

### Housekeeping
- `PROJECT_INSTRUCTIONS.md` deleted for good (`62554c74`, stale since Day 21).
- **Golden Rule 62:** explain to the user in very simple English.

| File | Change |
|---|---|
| `backend/index_trend.py`, `backend/vix_bands.py` | New (+ `backtest/test_index_trend.py` 26, `test_vix_bands.py` 13) |
| `backend/backend.py` | `/api/market/index`, SPY `trend`, VIX band, `openBasis`, v2.53 |
| `backend/market_phase_engine.py` | `signals.vix.band` |
| `frontend/src/components/RegimeRead.jsx` | Rewritten as the Market backdrop |
| `frontend/src/utils/{marketBackdrop,priceAsOf}.js` | New display helpers |
| `frontend/src/components/{MarketPhaseBanner,AutomatedPaperTradingPanel}.jsx` | Band word; next-open note |
| `frontend/src/components/{TechnicalRead,MRRead,FundamentalsRead,PriceStructureCard}.jsx` | Test hooks only |
| `frontend/src/App.jsx` | Card order, default view, No Trade, classification, VIX helper, price date, test hooks |
| `frontend/src/utils/{positionSizing,scoringEngine,categoricalAssessment}.js` | VIX helper; `qualityGates` removed; `describeRegimeRead` removed |
| `frontend/src/services/api.js` | `fetchIndexTrend`, SPY pass-through, QQQ in the full fetch |
| `frontend/scripts/*` | Verifier, PDF script, `lib/analyzeChecks.js`, 4 new unit-test files |
| `docs/claude/design/ANALYZE_REDESIGN_STEP{7,8}_PLAN_DAY124.md` | Plans + review tables + build notes |

**Verification:** parity 86,400/86,400; Node 69 + 17 + 22 + 9 checks; Python 26 + 13; live
verifier 40/40 (+ AVGO 8/8); build clean except the old ValueTab warning.

---

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-12
(ledger values, unchanged from Day 123; MR rows are scored at the entry-day close):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — (2 positions still winding down) |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. The two logged engine bugs (RSI `|| 50` counts as a pass; missing SPY → Unfavorable). Each is
   a parity-tested change: plan → Fable review → build.
2. 🔴 High: per-ticker provenance can't tell "never checked" from "just failed" (Day 108).
3. `/api/stock` doesn't drop today's unfinished bar (neither do the providers), unlike
   `/api/mr`, patterns and index trend. Check first whether a mid-day cache miss really
   returns a partial bar; if so, apply `drop_forming_bar` (the header already labels it honestly).
4. Page-level horizontal scroll at 390px (tab bar + Analyze button).
5. Momentum "RSI above 50, no cap" backtest (research, parked).
