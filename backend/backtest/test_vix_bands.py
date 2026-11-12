"""
Checks for vix_bands.vix_band (Day 124): the one VIX band definition shown on screen.
Run: cd backend && venv/bin/python backtest/test_vix_bands.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from vix_bands import vix_band

passed = 0


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


# Same cut-offs /api/market/vix used inline before Day 124 (15 / 20 / 25 / 30).
cases = [(9.0, 'low_volatility'), (14.99, 'low_volatility'), (15.0, 'normal'), (18.2, 'normal'),
         (19.99, 'normal'), (20.0, 'elevated'), (24.99, 'elevated'), (25.0, 'high'),
         (29.99, 'high'), (30.0, 'extreme'), (80.0, 'extreme')]
for value, band in cases:
    check(f'{value} -> {band}', vix_band(value) == band)
check('None -> None (never a made-up band)', vix_band(None) is None)
check('NaN -> None', vix_band(float('nan')) is None)

print(f'\n{passed} checks passed')
