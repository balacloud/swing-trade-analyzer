#!/usr/bin/env python3
"""
Diagnose why backend fails to extract Defeat Beta data for MSFT but works for AAPL.
This script mimics the exact backend code to find where it fails.
"""

import defeatbeta_api
from defeatbeta_api.data.ticker import Ticker as DBTicker
import warnings
import traceback
warnings.filterwarnings('ignore')

def safe_float(val):
    """Exactly as in backend.py"""
    if val is None:
        return None
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def diagnose_ticker(ticker_symbol):
    print(f"\n{'='*70}")
    print(f"DIAGNOSING: {ticker_symbol}")
    print(f"{'='*70}")

    try:
        ticker = DBTicker(ticker_symbol)

        result = {
            'source': 'defeatbeta',
            'roe': None,
            'roic': None,
            'roa': None,
            'epsGrowth': None,
            'revenueGrowth': None,
            'debtToEquity': None,
        }

        net_income = None
        total_equity = None
        total_assets = None
        total_debt = None
        total_revenue = None

        # === INCOME STATEMENT ===
        print("\n--- Income Statement ---")
        try:
            annual_income = ticker.annual_income_statement()
            print(f"Step 1: Got annual_income object: {type(annual_income)}")

            if hasattr(annual_income, 'data'):
                annual_df = annual_income.data
                print(f"Step 2: Got .data attribute, type: {type(annual_df)}")

                if annual_df is not None:
                    print(f"Step 3: annual_df is not None, shape: {annual_df.shape}")

                    if 'Breakdown' in annual_df.columns:
                        print(f"Step 4: 'Breakdown' column exists")

                        date_cols = [c for c in annual_df.columns if c != 'Breakdown']
                        print(f"Step 5: date_cols = {date_cols[:3]}")

                        if len(date_cols) >= 2:
                            current_year = date_cols[0]
                            prev_year = date_cols[1]
                            print(f"Step 6: current={current_year}, prev={prev_year}")

                            # Iterate through rows
                            for _, row in annual_df.iterrows():
                                breakdown = str(row.get('Breakdown', ''))

                                if breakdown == 'Diluted EPS':
                                    try:
                                        current_eps = safe_float(row.get(current_year))
                                        prev_eps = safe_float(row.get(prev_year))
                                        print(f"  Found Diluted EPS: curr={current_eps}, prev={prev_eps}")
                                        if current_eps is not None and prev_eps is not None and prev_eps != 0:
                                            result['epsGrowth'] = round(((current_eps - prev_eps) / abs(prev_eps)) * 100, 2)
                                            print(f"  -> EPS Growth = {result['epsGrowth']}%")
                                    except Exception as e:
                                        print(f"  EPS error: {e}")

                                if breakdown == 'Total Revenue':
                                    try:
                                        current_rev = safe_float(row.get(current_year))
                                        prev_rev = safe_float(row.get(prev_year))
                                        total_revenue = current_rev
                                        print(f"  Found Total Revenue: curr={current_rev}, prev={prev_rev}")
                                        if current_rev is not None and prev_rev is not None and prev_rev != 0:
                                            result['revenueGrowth'] = round(((current_rev - prev_rev) / abs(prev_rev)) * 100, 2)
                                            print(f"  -> Revenue Growth = {result['revenueGrowth']}%")
                                    except Exception as e:
                                        print(f"  Revenue error: {e}")

                                if breakdown == 'Net Income Common Stockholders':
                                    try:
                                        net_income = safe_float(row.get(current_year))
                                        print(f"  Found Net Income: {net_income}")
                                    except Exception as e:
                                        print(f"  Net Income error: {e}")

                        else:
                            print(f"FAIL: len(date_cols) < 2")
                    else:
                        print(f"FAIL: 'Breakdown' not in columns: {annual_df.columns.tolist()}")
                else:
                    print(f"FAIL: annual_df is None")
            else:
                print(f"FAIL: No .data attribute")
        except Exception as e:
            print(f"INCOME ERROR: {e}")
            traceback.print_exc()

        # === BALANCE SHEET ===
        print("\n--- Balance Sheet ---")
        try:
            annual_balance = ticker.annual_balance_sheet()
            print(f"Step 1: Got annual_balance object: {type(annual_balance)}")

            if hasattr(annual_balance, 'data'):
                balance_df = annual_balance.data
                print(f"Step 2: Got .data attribute, type: {type(balance_df)}")

                if balance_df is not None:
                    print(f"Step 3: balance_df is not None, shape: {balance_df.shape}")

                    if 'Breakdown' in balance_df.columns:
                        print(f"Step 4: 'Breakdown' column exists")

                        date_cols = [c for c in balance_df.columns if c != 'Breakdown']
                        print(f"Step 5: date_cols = {date_cols[:2]}")

                        if len(date_cols) >= 1:
                            current_col = date_cols[0]
                            print(f"Step 6: current_col = {current_col}")

                            for _, row in balance_df.iterrows():
                                breakdown = str(row.get('Breakdown', ''))

                                if breakdown == 'Total Assets':
                                    total_assets = safe_float(row.get(current_col))
                                    print(f"  Found Total Assets: {total_assets}")

                                if breakdown == "Stockholders' Equity":
                                    total_equity = safe_float(row.get(current_col))
                                    print(f"  Found Stockholders' Equity: {total_equity}")

                                if breakdown == 'Total Debt':
                                    total_debt = safe_float(row.get(current_col))
                                    print(f"  Found Total Debt: {total_debt}")

                            # Calculate ratios
                            if total_equity and total_equity != 0 and total_debt:
                                result['debtToEquity'] = round(total_debt / total_equity, 2)
                                print(f"  -> D/E = {result['debtToEquity']}")

                            if net_income and total_equity and total_equity != 0:
                                result['roe'] = round((net_income / total_equity) * 100, 2)
                                print(f"  -> ROE = {result['roe']}%")

                            if net_income and total_assets and total_assets != 0:
                                result['roa'] = round((net_income / total_assets) * 100, 2)
                                print(f"  -> ROA = {result['roa']}%")

                        else:
                            print(f"FAIL: len(date_cols) < 1")
                    else:
                        print(f"FAIL: 'Breakdown' not in columns")
                else:
                    print(f"FAIL: balance_df is None")
            else:
                print(f"FAIL: No .data attribute")
        except Exception as e:
            print(f"BALANCE ERROR: {e}")
            traceback.print_exc()

        # === FINAL RESULT ===
        print("\n--- FINAL RESULT ---")
        for key, val in result.items():
            print(f"  {key}: {val}")

        return result

    except Exception as e:
        print(f"FATAL ERROR: {e}")
        traceback.print_exc()
        return None


if __name__ == "__main__":
    for ticker in ['AAPL', 'MSFT', 'NVDA']:
        diagnose_ticker(ticker)
