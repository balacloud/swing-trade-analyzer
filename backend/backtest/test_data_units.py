"""
Data-unit checks behind the Fundamentals card (Day 123, redesign Step 6).
Run: cd backend && venv/bin/python backtest/test_data_units.py
"""
import os
import sys
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from providers.field_maps import (apply_field_map, YFINANCE_FUNDAMENTALS, FMP_FUNDAMENTALS,
                                  FINNHUB_FUNDAMENTALS, YFINANCE_STOCK_INFO)

passed = 0


def check(name, cond):
    global passed
    assert cond, name
    passed += 1
    print('ok', name)


yf = apply_field_map({'returnOnEquity': 1.5, 'debtToEquity': 154.5, 'trailingPE': 38.2}, YFINANCE_FUNDAMENTALS)
check('yfinance ROE 1.5 -> 150%', abs(yf['roe'] - 150) < 1e-9)
check('yfinance D/E 154.5% -> 1.545x', abs(yf['debtToEquity'] - 1.545) < 1e-9)
check('yfinance P/E trailing passthrough', yf['pe'] == 38.2)
yf = apply_field_map({'returnOnEquity': -1.8}, YFINANCE_FUNDAMENTALS)
check('yfinance ROE -1.8 -> -180%', abs(yf['roe'] + 180) < 1e-9)
yf = apply_field_map({'returnOnEquity': 0.25}, YFINANCE_FUNDAMENTALS)
check('yfinance ROE 0.25 -> 25%', abs(yf['roe'] - 25) < 1e-9)
yf = apply_field_map({'returnOnEquity': float('nan'), 'debtToEquity': None}, YFINANCE_FUNDAMENTALS)
check('NaN / None stay None', yf.get('roe') is None and yf.get('debtToEquity') is None)
fmp = apply_field_map({'roeTTM': 1.2, 'debtToEquityTTM': 0.8}, FMP_FUNDAMENTALS)
check('FMP ROE 1.2 -> 120%, D/E ratio unchanged', abs(fmp['roe'] - 120) < 1e-9 and fmp['debtToEquity'] == 0.8)
fh = apply_field_map({'roeTTM': 127.6, 'totalDebt/totalEquityQuarterly': 0.71}, FINNHUB_FUNDAMENTALS)
check('Finnhub ROE already % and D/E ratio unchanged', fh['roe'] == 127.6 and fh['debtToEquity'] == 0.71)
info = apply_field_map({'quoteType': 'ETF', 'shortName': 'X'}, YFINANCE_STOCK_INFO)
check('quoteType passes through', info['quoteType'] == 'ETF')

import backend as app_module  # noqa: E402  (imports Flask app; routes not started)
cdu = app_module.calendar_days_until
today = date(2026, 11, 11)
check('same day = 0', cdu(datetime(2026, 11, 11, 0, 0), today) == 0)
check('two days out at any hour = 2', cdu(datetime(2026, 11, 13), today) == 2)
check('past = negative', cdu(datetime(2026, 11, 9), today) == -2)
check('date object accepted', cdu(date(2026, 11, 26), today) == 15)

print(f"\n{passed} checks passed")
