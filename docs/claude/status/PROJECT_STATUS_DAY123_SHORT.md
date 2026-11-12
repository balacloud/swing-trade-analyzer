# Project Status — Day 123 (Nov 11–12)

**Version:** App v4.63, Backend v2.52, Frontend v4.60 (from v4.62 / v2.51 / v4.59)

---

## What Happened Today

Analyze Page Redesign Steps 3–6 were built. Every step had a written plan reviewed by Fable,
then the build, a Fable code review, live checks on real tickers, and the user's sign-off. The
engineering standard set by the user (`ANALYZE_REDESIGN_STEP4_PLAN_DAY123.md` §0) applied: no
silent failures, logged warnings, distinct loading / couldn't-load / data states, real data
behind every UI element, and no invented fallback numbers.

### Step 3 hardening + Step 4 — Trade Setup, Regime Read, Technical Read
- `calculateRiskReward` returns an explicit state (`no_data` / `no_support` / `no_atr` / `ok`).
  The old 3% stop / ×1.10 target fallbacks are gone. Backend `suggestedStop` is null when ATR is
  missing; RVOL is null, not 1.0, with no 50-day volume.
- New `RegimeRead.jsx` and `TechnicalRead.jsx`: 4 trend checks, Strong tiles, timing and volume
  answers, distribution warning, and the existing volume detail moved in unchanged.
- Removed from the header: the verdict badge, the T/F/S/R row and the chip row.
- `useMissingInputWarning` hook: one `[STA][card]` console warning per distinct problem.
- Two engine bugs found and logged, not fixed, because fixing them changes verdicts:
  missing RSI → 50 counts as a pass; missing SPY → treated as below its 200-day.

### Step 5 — Mean-Reversion Read (tested rules only) and the PF correction
- **Finding:** the forward test's PF 2.00 priced every trade at the entry day's close
  (`simulate_mr_trade`). User chose: buy at the next open, re-test. Pre-registered PF 1.5–1.7.
  **Result: broad PF 1.50, WR 63.5%, +0.70%/trade (241); HUB-65 PF 1.07 (70).** Golden Rule 60.
- `market_time.py`: one forming-bar rule (cutoff 16:30 ET, matching cache expiry). `MR_RULES`
  is the single definition, asserted equal to the frozen simulator by `test_mr_rules.py`.
- `MRRead.jsx` replaces `MRSignalCard.jsx`: 4 rule tiles (missing = dashed, not a fail), a
  clock-aware entry line, and the track record per universe with its own dates. The Scan tab's
  MR rows show the tested plan.

### Step 6 — Fundamentals card + removals
- `FundamentalsRead.jsx`: 3 red flags (sales, ROE, D/E), P/E guide (never a flag), next
  earnings always shown, "Can't check" ≠ "No red flags", ETF via `quoteType`, per-field sources.
- **Data bugs fixed:** yfinance D/E in percent; ROE ≥100% shown as 1.5%; earnings days off by one;
  all-sources-failed earnings reported as "no date". Cache schema v3. Golden Rule 61.
- **Removed (user-decided):** Holding Period selector, Assessment Breakdown, Raw Indicators,
  Quality Gates, the fundamentals banner, the Simple-view verdict strip, and the Scan tab's STA
  Verdict column. BUY/HOLD/AVOID no longer appears on any screen; the engine and parity test are
  untouched.

| File | Change |
|---|---|
| `backend/market_time.py` | New: forming-bar rule |
| `backend/mean_reversion.py` | `MR_RULES`, tri-state conditions, track record, ATR stop/target removed |
| `backend/backend.py` | MR endpoints, earnings NY-day + failure contract, quoteType, null stop/RVOL, candle date |
| `backend/providers/field_maps.py`, `yfinance_provider.py`, `cache_manager.py` | Unit fixes, quoteType, NY earnings tz, schema v3 |
| `backend/pattern_detection.py` | `sma_200_30d_ago` |
| `backend/backtest/mr_open_entry_retest.py`, `test_mr_rules.py`, `test_data_units.py` | New re-test + 21 + 13 checks |
| `frontend/src/components/{RegimeRead,TechnicalRead,MRRead,FundamentalsRead}.jsx` | New cards |
| `frontend/src/components/{AssessmentTile,MRSignalCard}.jsx` | Deleted |
| `frontend/src/utils/{technicalReadChecks,mrEntryTiming,fundamentalsRead}.js`, `hooks/useMissingInputWarning.js` | New helpers |
| `frontend/src/App.jsx` | −1,278 net lines: new cards wired, removals |
| `frontend/src/utils/{categoricalAssessment,riskRewardCalc,simplifiedScoring,volumeThresholds,priceStructureNarrative}.js`, `services/api.js` | Display helpers, states, pass-through fields |
| `docs/claude/design/ANALYZE_REDESIGN_STEP{4,5,6}_PLAN_DAY123.md` | Plans + review tables |

**Verification:** parity 86,400/86,400 after every engine-file edit; 34 + 8 + 27 Node checks,
21 + 13 Python checks; build clean; live checks on AAPL, NVDA, LLY, XOM, RIVN, JPM, SMH, SPY,
forced failures, 390px.

---

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-12
(ledger values; MR rows are scored at the entry-day close, see note):

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — (2 positions still winding down) |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. **Redesign Step 7:** Full Analysis as the default view, Simple-view copy (PASS wording).
   Plan → Fable review → build.
2. **Redesign Step 8:** rewrite `ui-verify-checklist.js` / `ui-cohesiveness-test.js` (they scrape
   removed elements), drop scoringEngine's unrendered `qualityGates`, docs.
3. The two logged engine bugs (RSI `|| 50`, missing SPY → Unfavorable): each a parity-tested change.
4. 🔴 High: per-ticker provenance can't tell "never checked" from "just failed" (Day 108).
5. Momentum "RSI above 50, no cap" backtest (research, parked).
