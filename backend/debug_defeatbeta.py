#!/usr/bin/env python3
"""Debug Defeat Beta API data extraction"""

import defeatbeta_api
from defeatbeta_api.data.ticker import Ticker as DBTicker
import warnings
warnings.filterwarnings('ignore')

def safe_float(val):
    if val is None:
        return None
    try:
        return float(val)
    except:
        return None

for ticker_symbol in ['AAPL', 'MSFT', 'NVDA']:
    print(f'\n{"="*60}')
    print(f'{ticker_symbol}')
    print(f'{"="*60}')

    ticker = DBTicker(ticker_symbol)

    # Get income statement
    annual_income = ticker.annual_income_statement()
    df = annual_income.data

    date_cols = [c for c in df.columns if c != 'Breakdown']
    print(f'Income date columns: {date_cols[:3]}')

    current_year = date_cols[0]
    prev_year = date_cols[1]

    # Revenue
    rev_row = df[df['Breakdown'] == 'Total Revenue']
    curr_rev = safe_float(rev_row[current_year].values[0])
    prev_rev = safe_float(rev_row[prev_year].values[0])
    print(f'Revenue: curr={curr_rev:,.0f}, prev={prev_rev:,.0f}' if curr_rev else 'Revenue: N/A')

    if curr_rev and prev_rev and prev_rev != 0:
        growth = ((curr_rev - prev_rev) / abs(prev_rev)) * 100
        print(f'Revenue Growth: {growth:.2f}%')

    # Net Income
    ni_row = df[df['Breakdown'] == 'Net Income Common Stockholders']
    net_income = safe_float(ni_row[current_year].values[0])
    print(f'Net Income: {net_income:,.0f}' if net_income else 'Net Income: N/A')

    # Diluted EPS
    eps_row = df[df['Breakdown'] == 'Diluted EPS']
    curr_eps = safe_float(eps_row[current_year].values[0])
    prev_eps = safe_float(eps_row[prev_year].values[0])
    print(f'EPS: curr={curr_eps}, prev={prev_eps}')

    if curr_eps and prev_eps and prev_eps != 0:
        eps_growth = ((curr_eps - prev_eps) / abs(prev_eps)) * 100
        print(f'EPS Growth: {eps_growth:.2f}%')

    # Balance sheet
    annual_balance = ticker.annual_balance_sheet()
    bdf = annual_balance.data

    balance_date_cols = [c for c in bdf.columns if c != 'Breakdown']
    print(f'Balance date columns: {balance_date_cols[:2]}')

    current_col = balance_date_cols[0]

    # Equity
    eq_row = bdf[bdf['Breakdown'] == "Stockholders' Equity"]
    equity = safe_float(eq_row[current_col].values[0])
    print(f'Equity: {equity:,.0f}' if equity else 'Equity: N/A')

    # Total Assets
    asset_row = bdf[bdf['Breakdown'] == "Total Assets"]
    total_assets = safe_float(asset_row[current_col].values[0])
    print(f'Total Assets: {total_assets:,.0f}' if total_assets else 'Total Assets: N/A')

    # Total Debt
    debt_row = bdf[bdf['Breakdown'] == "Total Debt"]
    total_debt = safe_float(debt_row[current_col].values[0])
    print(f'Total Debt: {total_debt:,.0f}' if total_debt else 'Total Debt: N/A')

    # Calculate ROE
    if net_income and equity and equity != 0:
        roe = (net_income / equity) * 100
        print(f'\n*** Calculated ROE: {roe:.2f}% ***')
    else:
        print(f'\n*** Cannot calculate ROE: net_income={net_income}, equity={equity} ***')

    # Calculate Debt/Equity
    if total_debt and equity and equity != 0:
        de = total_debt / equity
        print(f'*** Calculated D/E: {de:.2f} ***')
