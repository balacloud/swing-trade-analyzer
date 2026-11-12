"""
VIX bands shown on screen (Day 124). One definition for every place that puts a word next to
the VIX number: /api/market/vix (Analyze page Market backdrop) and the Context tab's Market
Phase banner. Display only.

Not the same as two classification inputs, which stay separate on purpose:
- assessRiskMacro() / categorical_engine.py (verdict engine: 20 / 30) — parity-tested.
- market_phase_engine._vix_bucket() (phase grid: 20 / 25) — changing it would change phases.
"""
import math

# (upper bound exclusive, band); same cut-offs /api/market/vix used inline before Day 124.
VIX_BANDS = [(15, 'low_volatility'), (20, 'normal'), (25, 'elevated'), (30, 'high')]


def vix_band(value):
    """Band name for a VIX level, or None when the value is missing."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    for upper, band in VIX_BANDS:
        if value < upper:
            return band
    return 'extreme'
