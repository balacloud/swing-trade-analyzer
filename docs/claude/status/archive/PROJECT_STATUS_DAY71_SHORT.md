# Project Status — Day 71 (March 27, 2026)

## Version: v4.32 (Backend v2.33, Frontend v4.32, Backtest v4.17, API Service v2.10)

## Session Focus: Behavioral Audit + README Fixes + Label Corrections

### What Was Done
- **Behavioral audit (12 tests, 2 iterations)**:
  - 1 defect found: `stockData.marketCap` always undefined in `simplifiedScoring.js` — marketCap lives in `stockData.fundamentals.marketCap`. All tickers were treated as small-cap. Fixed: reads `fundamentals?.marketCap` with safe fallback.
  - 11 other tests PASS (sentiment removal, progressive disclosure, Decision Matrix removed, TradingView removed, RS 1.2, VIX sizing, MR signal, blended RS, backend parity).
  - Audit documented: `docs/claude/versioned/BEHAVIORAL_AUDIT_DAY71.md`
- **README audit fixes (7 items from Day 68 — RESOLVED)**:
  - FMP → AlphaVantage (17 references across README)
  - Version numbers: Frontend v4.32, Backend v2.33, API v2.10
  - Fundamental Strong description corrected (2+ of 3 metrics, not all 3)
  - 200 EMA → 200 SMA (README)
  - Verdict logic updated (T+F only, sentiment info-only)
  - Decision Matrix → progressive disclosure
  - Changelog extended through v4.32
- **200 EMA → SMA label fix (in code)**: `categoricalAssessment.js` and `BottomLineCard.jsx` displayed "SPY below 200 EMA" but code uses 200 SMA. Caught during paper trade inspection of MSFT/META screenshots.
- **Before/After reference document**: `docs/claude/status/UNIVERSAL_PRINCIPLES_BEFORE_AFTER.md` — comprehensive comparison of STA pre and post universal principles evolution.

### Files Modified (3)
| File | Change |
|------|--------|
| `frontend/src/utils/simplifiedScoring.js` | Fix: `stockData.fundamentals?.marketCap` (was `stockData.marketCap`) |
| `frontend/src/utils/categoricalAssessment.js` | Label: "200 EMA" → "200 SMA" (10 occurrences) |
| `frontend/src/components/BottomLineCard.jsx` | Label: "200 EMA" → "200 SMA" |

### Files Created (2)
| File | Purpose |
|------|---------|
| `docs/claude/versioned/BEHAVIORAL_AUDIT_DAY71.md` | 12-test behavioral audit results |
| `docs/claude/status/UNIVERSAL_PRINCIPLES_BEFORE_AFTER.md` | Before/after reference for universal principles |

### Files Updated (2)
| File | Change |
|------|--------|
| `README.md` | 7 audit items resolved (FMP, versions, descriptions, labels) |
| `docs/claude/versioned/KNOWN_ISSUES_DAY70.md` | README audit marked resolved |

### Commits (4)
1. `caf81bb9` — Fix cap-aware logic (marketCap unreachable)
2. `40253847` — Universal principles before/after reference doc
3. `b5a0167c` — README audit fixes + behavioral audit doc
4. `9973270c` — Fix 200 EMA → 200 SMA labels

### Key Decisions
1. **Long-term value investing view — DECLINED**: User's friend suggested PE-based value view. Declined per feature freeze — swing system needs paper trade validation first. Buffett/Damodaran methodology requires multi-year fundamentals we don't have. Existing Fundamental card already shows the relevant data.
2. **PE ratio not relevant for swing**: Confirmed — PE is a valuation metric for long-term holders, not momentum/trend traders.

### Next Priorities
1. **Paper trading** — System is frozen and audited. Start logging real trades.
2. **Gate 5: Combined momentum+MR system test** — Still pending.
3. **Feature freeze holds** — No new features until paper trades logged.
