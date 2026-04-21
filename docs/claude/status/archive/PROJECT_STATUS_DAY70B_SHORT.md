# Project Status — Day 70B (March 19, 2026)

## Version: v4.32 (Backend v2.33, Frontend v4.32, Backtest v4.17, API Service v2.10)

## Session Focus: Simplicity Premium UI + Data-Driven Simple Checklist

### What Was Done
- **Sentiment removed from verdict**: `categoricalAssessment.js` + `categorical_engine.py` — Sentiment was never validated (backtest hardcoded Neutral). Verdict now uses T+F only. Risk/Macro remains as gate. Sentiment is informational-only.
- **BottomLineCard cleaned**: Removed all sentiment references from "What's Good" and "What's Risky" sections.
- **Decision Matrix view REMOVED**: Simplicity premium — full+simple views are sufficient.
- **TradingView Chart widget REMOVED**: Simplicity premium — not adding value.
- **Progressive disclosure (3-tier)**: Full analysis reorganized:
  - Tier 1 (always visible): Verdict, Trade Setup, Bottom Line, MR Signal, Quality Gates
  - Tier 2 (collapsed by default): Holding Period, Price & RS, Pattern Detection, Categorical Assessment
  - Tier 3 (hidden until requested): Technical Indicators
  - Sentiment card labeled "(info)" with reduced opacity
- **RS threshold tightened 1.0→1.2**: Backtest across 20 tickers — PF 1.56→1.78, WR 49.7%→52.6%
- **Volume threshold cap-aware**: $2M small / $5M mid / $10M large (old flat $10M was MISLEADING per multi-LLM audit)
- **Stop distance cap-aware**: 7% large / 9% mid / 10% small (ATR analysis: 7% = 1.4x ATR for small caps, below 2x noise minimum)

### Files Modified (5)
| File | Change |
|------|--------|
| `frontend/src/App.jsx` | Removed DecisionMatrix + TradingView, added 3-tier progressive disclosure, sentiment card "(info)" label |
| `frontend/src/utils/categoricalAssessment.js` | Removed sentiment from verdict strong_count (T+F only) |
| `frontend/src/utils/simplifiedScoring.js` | RS 1.0→1.2, cap-aware volume + stop distance thresholds |
| `frontend/src/components/BottomLineCard.jsx` | Removed sentiment from getWhatsGood() + getWhatsRisky() |
| `backend/backtest/categorical_engine.py` | Backend parity: removed sentiment from verdict |

### Files Updated (1)
| File | Change |
|------|--------|
| `docs/claude/versioned/KNOWN_ISSUES_DAY70.md` | Added entries for all Day 70B changes |

### No New API Endpoints
No backend API changes. No new endpoints. API_CONTRACTS_DAY70.md unchanged.

### Test Results
- Frontend build: PASS
- Backtest holistic RS validation: PASS (RS 1.2 = PF 1.78, WR 52.6%)
- ATR cap analysis: PASS (30 stocks, 3 cap tiers)

### Key Decisions
1. **Sentiment informational-only**: Backtest never validated sentiment (hardcoded Neutral). Removing aligns live system with backtest evidence.
2. **RS 1.2 optimal**: Data-driven — tested 6 RS thresholds (0.8-1.5). RS 1.2 maximizes PF while maintaining adequate trade count.
3. **Cap-aware stops**: ATR analysis proved 7% flat stop = only 1.4x ATR for small caps (below 2x noise floor). Cap-aware stops: 7%/9%/10%.
4. **No backtest re-run needed**: Backtest engine (`categorical_engine.py`) uses its own thresholds. Frontend simple checklist is a separate pre-flight human-facing tool. Changes are orthogonal.

### Next Priorities
1. **Paper trading** — System is frozen. Start logging real trades.
2. **README fixes** — 7 items from Day 68 audit (FMP refs, versions, etc.)
3. **Gate 5: Combined momentum+MR system test** — Still pending.
