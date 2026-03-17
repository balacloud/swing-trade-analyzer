# Project Status - Day 51 (February 11, 2026)

## Session Summary

### Completed Today
1. **v4.13 Holding Period Selector Plan REVISED** ✅
   - Researched Perplexity findings on RSI thresholds
   - Researched dual-horizon format validation
   - Found: Original RSI thresholds by holding period were INVENTED
   - Revised plan: Signal WEIGHTING by horizon (not threshold adjustment)

2. **Research Findings**
   - ❌ **INVALIDATED:** RSI 40-65/35-70/30-75 by holding period
     - Shorter periods need MORE EXTREME thresholds (15/85), not tighter
     - RSI interpretation varies by ADX REGIME, not holding period
   - ✅ **VALIDATED:** ADX-based regime messaging (already in v4.6.2)
   - ✅ **VALIDATED:** Signal weighting by horizon (arXiv 2512.00280)
     - Short-horizon = Technical signals dominate
     - Long-horizon = Fundamental signals dominate
     - Strategy earns ~40 bps monthly alpha
   - ✅ **VALIDATED:** Bottom Line summary card (UX research)
   - ❌ **NOT VALIDATED:** Kavout dual-horizon format (marketing, no research)

3. **Golden Rule #15 Added** ✅
   - Never implement without validation (research/backtest/practitioner consensus)
   - Example: Day 51 RSI thresholds sounded logical but were WRONG

4. **Backtest Script Created** ✅
   - `backend/backtest/backtest_adx_rsi_thresholds.py`
   - Tests 4 hypotheses from Perplexity research:
     1. ADX < 20 + RSI > 70 = mean reversion
     2. ADX > 25 + RSI > 70 = momentum continuation
     3. RSI > 80 = 68% pullback rate
     4. RSI > 80 + strong trend = lower pullback rate
   - **Status:** Could not run - yfinance API down

### Files Modified
- `docs/research/HOLDING_PERIOD_SELECTOR_PLAN.md` - REVISED with research findings
- `docs/claude/stable/GOLDEN_RULES.md` - Added Rule #15
- `docs/claude/stable/ROADMAP.md` - Updated v4.13 description, added Day 51 log
- `docs/claude/CLAUDE_CONTEXT.md` - Updated Day 51 summary
- `backend/backtest/backtest_adx_rsi_thresholds.py` - Created

### Key Learnings
1. **My RSI thresholds were invented** - I assumed shorter periods need "tighter" thresholds (40-65), research showed opposite (shorter = MORE extreme 15/85)
2. **Thresholds vary by regime, not timeframe** - ADX determines RSI interpretation, not holding period
3. **Kavout format is marketing** - No research backing, just presentation
4. **Signal weighting IS validated** - Short-term = tech signals, Long-term = fund signals (arXiv)
5. **Golden Rule #15 prevents this** - Never implement without validation

---

## Version Summary
- Frontend: v4.4 (App.jsx)
- Backend: v2.16 (backend.py)
- API: v2.7 (api.js)

---

## Next Session Priorities

### P1: Run ADX/RSI Backtest (when API recovers)
- Script ready: `backend/backtest/backtest_adx_rsi_thresholds.py`
- Validate 4 hypotheses from research
- yfinance API was down today

### P2: v4.11 Sector Rotation Tab
- Per ROADMAP
- Sector RS calculation, ETF tracking

### P3: v4.13 Implementation (after backtest)
- Use REVISED plan with signal weighting
- Bottom Line summary card
- ADX-based messaging preserved

### P4: v4.14 Multi-Source Data Intelligence
- Review `docs/research/DATA_SOURCE_INTELLIGENCE_OVERVIEW.md`
- Implement multi-provider fallback (TwelveData → Alpha Vantage → yfinance → Stooq)
- Add provenance tracking and cache policies
- Fix backtest scripts to use same infrastructure as main app

---

## Architecture Notes
- Backend running on port 5001
- Frontend running on port 3000
- Start/stop with `./start.sh` and `./stop.sh`
- yfinance API intermittent (retry later for backtest)
