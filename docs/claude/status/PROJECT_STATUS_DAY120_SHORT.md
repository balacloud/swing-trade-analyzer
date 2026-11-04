# Project Status — Day 120

**Version:** App v4.62, Backend v2.51, Frontend v4.59 (unchanged — no STA app code touched)

---

## What Happened Today

Day 120 ran over 2026-11-02 to 11-04. Both pieces of work were standalone Artifact pages, not
STA application changes.

### Leveraged ETF Board (new Artifact, live IBKR data)
A page that runs the user's adopted Reddit and 100-year-canon rules in JavaScript against live
IBKR daily bars. It has a read-only `mcp` capability with only `get_price_history`, so it can't
place orders, consistent with the Day 113 no-execution decision.
- v1 used the **US** SOXL/GDXU (Direxion/MicroSectors) by mistake, because their conids came from
  `search_contracts`. The user holds the **Canadian BetaPro** funds (CAD, Cboe Canada/TSX).
  v2 rebuilt the board from the user's IBKR watchlist "AI_Leveraged" (id 122), which has 8 funds,
  and added each fund's underlying. This is the origin of **new Golden Rule 58**.
- The JS formulas (SMA, EMA adjust=False, RSI pandas ewm, ATR 14-day SMA of TR) are a second copy
  of STA's Python. They were checked bit-identical on SOXL, GDXU, DRAL and SMH.
- Splits noted: Canadian SOXL and GDXU 3:1 (2026-05-25), QPUX 1:3 reverse (2026-03-23). IBKR bars
  are already adjusted.
- Scope set by the user: the page shows a count only ("X of 4 checkable rules") with no verdict,
  and the user decides how many rules must agree. Claude watches for splits and explains stops
  and sizing. Claude doesn't nag about fundamentals, holding period, backtests or rule count.

| File | Change |
|---|---|
| `docs/claude/design/LEVERAGED_ETF_BOARD.html` | New. Published at https://claude.ai/artifact/HdErxTqUhq8KYs6McSU5V7 |

### Beginner Trading Starter Playbook (new Artifact, for the user's friend)
A light-theme playbook with 8 tabs for a total beginner. It replaces an earlier Claude Docs
version, which still exists, unused.
1. Trader type
2. US–Canada macro (ChatGPT-style assessment table plus a "how markets usually react" guide)
3. Reddit rules
4. 100-year canon
5. Top-10 coding rules (drawn from STA, without naming it)
6. General ("Anatomy of a Market Move")
7. Live data sources plus one scored gamification example
8. Build it with Claude Code (system design, FastAPI and React, Lightweight Charts placement)

The macro numbers come mostly from secondary sources, and the page says so. The US 10Y figure
(4.95%) is live from IBKR TNX. The Canada 5Y figure (3.57%) is from another AI's summary and is
flagged as unchecked. The tab 8 Python snippet was tested on synthetic data.
The page is shared as anyone-with-the-link.

On Nov 4 the "Build it" tab was invisible: the tab bar scrolled sideways with a hidden
scrollbar. The tabs now wrap onto a second row instead (v12).

| File | Change |
|---|---|
| `docs/claude/design/STARTER_PLAYBOOK.html` | New. Published at https://claude.ai/artifact/CfnNDEEs8jS112MuTU4HPp (v12) |

### Docs
| File | Change |
|---|---|
| `docs/claude/stable/GOLDEN_RULES.md` | New Golden Rule 58 (take broker conids from the user's own watchlist) |
| `docs/claude/stable/PERSONA.md` | Feedback Log entry on the leveraged-ETF scope |
| `docs/claude/design/STA_STATUS_BOARD.html` | Republished. Final MR result corrected to PF 2.00 (241 trades, 70.54% win rate); the old "~2.5" was stale. |

---

## All Gates Status
No live forward-test gates exist (program discontinued Day 113). Final ledger, from
`daily_job.py --report`, last run 2026-11-03:

| Track | Closed | Win % | PF | Note |
|---|---|---|---|---|
| MR (broad) | 241 | 70.54% | 2.00 | The one confirmed edge. Supersedes the stale "PF ~2.5" in older docs. |
| MR HUB-65 | 70 | 64.29% | 1.67 | |
| Path A | 120 | 39.17% | 0.70 | 2 positions still winding down |
| Path B | 232 | 42.24% | 0.87 | Retired Day 112 |

## Next Session Priorities
Unchanged from Day 119. See `CLAUDE_CONTEXT.md`.
1. Analyze Page Redesign: Phase 0, then Phase 1, per `ANALYZE_PAGE_REDESIGN_IMPLEMENTATION_PLAN_DAY119.md`.
2. 🔴 High: per-ticker provenance can't tell "never checked" from "just failed" (Day 108).
3. 🟡 6 Medium findings with no plan written.
4. 🧹 Zero-risk cleanup batch.
