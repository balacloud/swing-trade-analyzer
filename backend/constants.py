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
