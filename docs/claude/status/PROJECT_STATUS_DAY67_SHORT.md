# Project Status — Day 67 Starting Point
> **Version:** v4.28 (Backend v2.31, Frontend v4.15, Backtest v4.17, API Service v2.9)
> **Last session:** Day 66 (March 9, 2026)
> **Next focus:** Paper trading — use the system daily to find real bugs

---

## What Was Done in Day 66

### Cap Size Rotation Strip (Sectors Tab)
Added compact size rotation indicator to the Sectors tab. Shows IWM / MDY / QQQ relative strength vs SPY with a single RISK-ON / RISK-OFF / NEUTRAL signal derived from IWM vs QQQ RS Ratio spread.

**Backend (`backend.py` v2.31):**
- IWM, MDY, QQQ added to existing `yf.download()` batch call (same request, no extra API hit)
- Identical RS Ratio + Momentum calc as 11 sector ETFs (midpoint-normalized to 100)
- Signal: IWM − QQQ diff ≥ +2 → Risk-On; ≤ −2 → Risk-Off; else Neutral
- Three new fields in `/api/sectors/rotation` response: `size_rotation`, `size_signal`, `size_signal_detail`

**Frontend (`SectorRotationTab.jsx` v4.15):**
- `SizeRotationStrip` component: 3-column grid (QQQ → MDY → IWM order), RS bar, value + arrow
- Signal headline with color border tint (green=Risk-On, red=Risk-Off, gray=Neutral)
- Positioned between main header block and "How to read this" explanation row
- Gracefully absent if `size_rotation` missing (e.g., old cached response)

### Sector Card Audit Fixes (also Day 66)
- Rank badge → neutral gray (position only, no color judgment)
- RS bar scale corrected: RS Ratio range [85,130] / threshold 100; Momentum range [-12,+12] / threshold 0
- Scan button logic → quadrant-based (`Leading || Improving`), was rank-based (`rank <= 4`)
- "How to read" text corrected to 100-based thresholds

### Infrastructure
- `start.sh` / `stop.sh`: both now auto-kill ports 5001/3000 via `lsof` before starting

**Files modified:**
- `backend/backend.py` — size_rotation calc + new response fields
- `frontend/src/components/SectorRotationTab.jsx` — SizeRotationStrip + sector card fixes
- `start.sh`, `stop.sh` — auto port kill

---

## Current System State

### Backend (v2.31) — `/api/sectors/rotation` updated
- All Day 64 fixes intact (18 bugs, 9 files)
- Size rotation added (isolated module, no core engine changes)

### Frontend (v4.15) — SectorRotationTab.jsx updated
- SizeRotationStrip component added
- Sector card color + scale + scan button fixes

### Known Issues
- See `KNOWN_ISSUES_DAY67.md` — no new open issues

---

## Next Session Priority: Paper Trading

**Feature freeze is in effect.**

1. Run 5-10 real tickers across different sectors
2. Check: CAUTION ENTRY label, ATR stops ($0.01 floor), VCP accuracy, news dates
3. Log first Forward Test trade if BUY signal found
4. Report any field bugs found — no new features until paper trading set is logged

---

## Version History (Last 3 Sessions)
| Day | Version | Key Work |
|-----|---------|----------|
| 64 | v4.27 | Deep audit: 18 bugs fixed across 9 files (VCP, ATR, W-FRI, stops, patterns, labels) |
| 65 | v4.27 | README hybrid rewrite (internal notes + developer setup guide) — no code changes |
| 66 | v4.28 | Cap size rotation strip (IWM/MDY/QQQ vs SPY) + sector card audit fixes |
