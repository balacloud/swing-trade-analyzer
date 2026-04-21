# Project Status — Day 73 (April 20, 2026)

## Version: v4.33 (Backend v2.34, Frontend v4.33, Backtest v4.17, API Service v2.10)

## Session Focus: Research/Concept Session — Positional Trading vs Swing Trading

### What Was Done

**No code changes this session.**

**Research: Positional Trading vs Swing Trading**
- Fetched and analyzed Finvezto "20 Ways to Play in the Indian Market" article
- Key insight: 4 winning strategies in Indian market — Investing, Positional Trading, Hedged Options Selling, Portfolio Hedging
- Positional trading captures momentum factor (weeks–months, unleveraged) — same academic basis as STA's RS driver
- 97% of intraday traders are net losers (SEBI data) — validates STA's swing approach
- Two-filter test: Positive expectancy + No forced exits

**Swing vs Positional clarity:**
| | Swing (STA) | Positional |
|---|---|---|
| Hold | Days (3–10) | Weeks–months |
| Stop | Tight 7–10% | Wider/trailing |
| Entry precision | High (timing matters) | Lower (direction matters) |
| RS usage | RS > 1.2 at entry | Persistent RS over months |

STA's Config C backtest (53.78% WR, PF 1.61) validates the swing layer. Positional = same stocks, longer hold, wider stops — natural extension post paper trading.

### Files Created
None.

### Files Modified
None.

### Key Decisions
- None (concept session only)

### Next Priorities
1. **Behavioral test: Price Structure card** — Run NVDA, F, SPY, AAPL, SMCI. Verify narrative matches TradingView chart read before paper trading use.
2. **Paper trading** — System is frozen. Log real trades using Forward Testing tab.
3. **Gate 5** — Combined momentum+MR system test (pending).
4. **Flip default view to simple** — Last remaining simplicity premium item (30 min).
5. **Phase 2 (deferred)** — HH/HL/LH/LL market structure engine after paper trading validation.
