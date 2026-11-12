# Project Status — Day 125 (Nov 12)

**Version:** App v4.65, Backend v2.54, Frontend v4.62 (from v4.64 / v2.53 / v4.61)

---

## What Happened Today

The user went card by card through the finished Analyze page and asked, for each one: does it help,
or does it just add words? The goal was less to read and less decision fatigue. Same process as
Days 123–124: a written plan, a Fable plan review, a test-first build, a Fable code review, live
checks, and user sign-off.

### Analyze cleanup (`057bd4e9`)
- **Support/resistance, simple and neat:** Trade Setup now ends with three lines: "Price is …", the
  nearest **Resistance** and the nearest **Support**. Each shows a ±0.5% zone, "near it on N days"
  and ★ when the weekly chart agrees. Projected (ATR/Fibonacci) levels are never shown as real
  ("No real resistance within 30% above. $X is a projected level"). Removed: the S1–Sn/R1–Rn lists,
  the MTF % badge, the weekly-levels dropdown and the method small print. The one-line state got
  two fixes. It used the deepest support instead of the nearest (Day 112 BUG-B again). It also
  guessed "Downtrend" when trend data was missing; it now shows no line.
- **Breakout, widely agreed trader rules, not backtested (user: "it's a rabbit hole"):** a close
  above the 60-day high (measured before the last 10 days, so the breakout bars never move it),
  volume 1.5× normal **on the breakout day**, no more than 5% above. Failed = a close back below;
  Retest = came back within 1% and held. 7 states (new `BREAKOUT_LIGHT_VOLUME`; `SUPPLY_WARNING`
  and `BUILDING_BASE` removed). Completed bars only (forming bar dropped); the SPY fetch was
  removed. The card says "Common trader rules, not tested". A failed check is shown, never hidden.
- **Removed cards:** Price Structure, Pattern Detection (the `/api/patterns` fetch stays because its
  trend template feeds the verdict), the P/E guide (one 15/25 scale is wrong across sectors; P/E
  stays on the Value tab), and the MR track-record box (still on the Forward Test tab).
- **Labels:** "Ceiling/Floor" → **Resistance/Support** (user). The breakout level is always
  "60-day high", so "resistance" means one thing on the page (new Golden Rule 63).

### Simple S&R engine — planned, not built
User: "is the S&R code best in class simple? what's commonly used? weekly candles?" Honest answer:
the main method (swing highs/lows) is standard, but `support_resistance.py` is ~1,600 lines, with
3 fallback methods, projections and weighted confluence. New plan `SIMPLE_SR_PLAN_DAY125.md`:
daily + weekly swing highs/lows, zones capped at 1 ATR, nearest only, no invented levels.
Fable-reviewed: GO, with 6 must-fixes folded in (one Buy price everywhere, the zone-width cap,
keeping 1-turn levels, a KeyLevels rewrite, one shared calculation for the comparison, removing
dead "projected" copy). A user-run Reddit check agreed with 5 of the 6 rules. It was mixed on
labelling a 1-turn level "weak", so that label was dropped. **The switch waits for a ~30-stock
old-vs-new table and a one-time review page; the user decides.**

### Chart: decided against
User: "will a chart really help me, or cause decision fatigue? How would you use it?" Claude reads
the numbers, so a chart adds nothing for Claude. The user already reads charts in TradingView, and
a second chart is a second place to look. Same conclusion as Day 70. The only chart will be on the
one-time review page, drawn in plain SVG with no library.

| File | Change |
|---|---|
| `backend/breakout_detection.py`, `breakout_routes.py` | Rewritten to simple rules; forming bar dropped; no SPY |
| `backend/backtest/test_breakout_rules.py` | New, 46 checks |
| `backend/backend.py` | v2.54; stale comment |
| `frontend/src/utils/keyLevels.js`, `components/KeyLevels.jsx` | New: nearest support/resistance + one-line state |
| `frontend/scripts/test_key_levels.mjs` | New, 29 checks |
| `frontend/src/App.jsx` | Cards removed; Breakout card rewritten; badge labels; Simple-view error chip; v4.62 |
| `frontend/src/components/{FundamentalsRead,MRRead}.jsx`, `utils/fundamentalsRead.js` | P/E guide and MR track record removed |
| `frontend/src/utils/categoricalAssessment.js` | Pattern helpers removed (only caller gone) |
| Deleted | `PriceStructureCard.jsx`, `PatternMiniCard.jsx`, `priceStructureNarrative.js` |
| `frontend/src/services/api.js` | `fetchBreakout` returns `{error}` instead of null |
| `frontend/scripts/lib/analyzeChecks.js` | A1 requires `card-breakout` |
| `.claude/commands/{breakout-watch,watchlist-report}.md`, `pine/sta_breakout_companion.pine`, `BREAKOUT_ENGINE_SPEC.md`, `PRICE_STRUCTURE_CARD_*.md` | States/superseded notes |
| `docs/claude/design/{ANALYZE_CLEANUP,SIMPLE_SR}_PLAN_DAY125.md` | Plans, reviews, build notes |

**Verification:** Python 46 + 26 + 13; Node 69 + 29 + 17 + 22 + 9; parity 86,400/86,400; build
clean except the old ValueTab warning. Live verifier: AAPL/NVDA/SMH/JPM/RIVN 40/40, AVGO/MSFT
16/16, AAPL/RIVN 16/16, run in the old headless mode (see Known Issues). `/api/breakout` was
checked live on 6 tickers plus a batch; a bad ticker stays isolated to its own row.

---

## All Gates Status
No live forward-test gates (program discontinued Day 113). `daily_job.py --report`, run 2026-11-12:

| Track | Closed | Win % | PF (ledger) | PF at next open (Day 123 re-test) |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | **1.50** (63.5% WR) |
| MR HUB-65 | 70 | 64.29% | 1.67 | **1.07** |
| Path A | 120 | 39.17% | 0.70 | — (2 positions still winding down) |
| Path B | 232 | 42.24% | 0.87 | — (retired Day 112) |

## Next Session Priorities
1. **Build the simple S&R engine** (`SIMPLE_SR_PLAN_DAY125.md` §2 + §8 + §9): tests first, then the
   build, then the ~30-stock comparison table and a one-time review page. **The user decides the
   switch.** Then a Fable code review and a live check.
2. The two engine bugs (RSI `|| 50` counts as a pass; missing SPY → Unfavorable), parity-tested.
3. `/api/stock` forming bar (confirm a mid-day cache miss first).
4. 🔴 High: per-ticker provenance can't tell "never checked" from "just failed" (Day 108).
5. Page-level horizontal scroll at 390px.
