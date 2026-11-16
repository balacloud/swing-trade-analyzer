"""
constants.py — shared numeric constants for STA backend.

Single source of truth. Import from here; don't hardcode in individual files.
"""

# ─── S&R Proximity Filter ─────────────────────────────────────────────────────
# Support: max distance below current price to be considered "actionable"
# Resistance: max distance above current price to be considered "actionable"
# Used in: support_resistance.py (pivot detection) and backend.py (API route)
SUPPORT_PROXIMITY_PCT  = 0.20   # 20% below current price
RESISTANCE_PROXIMITY_PCT = 0.30  # 30% above current price

# ─── S&R engine for /api/sr (Day 126) ─────────────────────────────────────────
# 'legacy' = support_resistance.py (pivot + 3 fallback methods, projections, MTF).
# 'simple' = simple_sr.py (swing highs/lows -> zones, nearest only, no projections).
# Switched to 'simple' Day 126 (user approved after the 30-stock old-vs-new review,
# docs/claude/design/SIMPLE_SR_SWITCH_PLAN_DAY126.md). /api/sr/<t>?engine=legacy
# still returns the old engine for one request, as a rollback/preview. backtest_holistic.py and the
# discontinued paper_trading/live_signals.py always use the legacy engine.
SR_ENGINE = 'simple'
