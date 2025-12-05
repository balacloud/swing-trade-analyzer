#!/usr/bin/env python3
"""
Day 7 - Defeat Beta Diagnostic Script
Run this in your backend venv to see what Defeat Beta actually returns

Usage:
  cd /Users/balajik/projects/swing-trade-analyzer/backend
  source venv/bin/activate
  python diagnose_defeatbeta.py
"""

def main():
    print("="*60)
    print("🔍 Defeat Beta Diagnostic - Day 7")
    print("="*60)
    
    try:
        from defeatbeta_api.data.ticker import Ticker as DBTicker
        print("✅ Defeat Beta imported successfully\n")
    except ImportError as e:
        print(f"❌ Defeat Beta not installed: {e}")
        print("Install with: pip install defeatbeta-api")
        return
    
    ticker_symbol = "AVGO"
    print(f"📊 Testing {ticker_symbol}...\n")
    
    ticker = DBTicker(ticker_symbol)
    
    # =============================================
    # TEST 1: Annual Income Statement
    # =============================================
    print("="*60)
    print("1️⃣  ANNUAL INCOME STATEMENT")
    print("="*60)
    
    try:
        annual_income = ticker.annual_income_statement()
        
        if hasattr(annual_income, 'to_df'):
            df = annual_income.to_df()
            print(f"✅ Got DataFrame with {len(df)} rows, {len(df.columns)} columns")
            print(f"\n📅 Columns (years): {list(df.columns)[:4]}")
            print(f"\n📋 All row indices:")
            for i, idx in enumerate(df.index):
                print(f"  [{i}] {idx}")
            
            # Try to find EPS
            print("\n🔍 Looking for EPS/Revenue values:")
            current_col = list(df.columns)[0]
            prev_col = list(df.columns)[1] if len(df.columns) > 1 else None
            
            for idx in df.index:
                idx_str = str(idx)
                if 'EPS' in idx_str or 'Revenue' in idx_str or 'Net Income' in idx_str:
                    current_val = df.loc[idx, current_col]
                    prev_val = df.loc[idx, prev_col] if prev_col else None
                    print(f"  {idx_str}: Current={current_val}, Previous={prev_val}")
        else:
            print(f"⚠️ Not a DataFrame, type: {type(annual_income)}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # =============================================
    # TEST 2: Annual Balance Sheet
    # =============================================
    print("\n" + "="*60)
    print("2️⃣  ANNUAL BALANCE SHEET")
    print("="*60)
    
    try:
        annual_balance = ticker.annual_balance_sheet()
        
        if hasattr(annual_balance, 'to_df'):
            df = annual_balance.to_df()
            print(f"✅ Got DataFrame with {len(df)} rows, {len(df.columns)} columns")
            print(f"\n📅 Columns (years): {list(df.columns)[:4]}")
            print(f"\n📋 All row indices:")
            for i, idx in enumerate(df.index):
                print(f"  [{i}] {idx}")
            
            # Try to find Equity, Assets, Debt
            print("\n🔍 Looking for Equity/Assets/Debt values:")
            current_col = list(df.columns)[0]
            
            for idx in df.index:
                idx_str = str(idx)
                if any(term in idx_str for term in ['Equity', 'Assets', 'Debt', 'Stockholder']):
                    val = df.loc[idx, current_col]
                    print(f"  {idx_str}: {val}")
        else:
            print(f"⚠️ Not a DataFrame, type: {type(annual_balance)}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # =============================================
    # TEST 3: Current Backend Fundamentals Endpoint
    # =============================================
    print("\n" + "="*60)
    print("3️⃣  CURRENT BACKEND OUTPUT (/api/fundamentals/AVGO)")
    print("="*60)
    
    try:
        import requests
        response = requests.get(f"http://localhost:5001/api/fundamentals/{ticker_symbol}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Backend returned:")
            for key, value in data.items():
                print(f"  {key}: {value}")
            
            # Check which values are None/0
            print("\n⚠️ Values that are None or 0:")
            for key, value in data.items():
                if value is None or value == 0:
                    print(f"  ❌ {key}: {value}")
        else:
            print(f"❌ Backend returned status {response.status_code}")
            print("Make sure backend is running: python backend.py")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend")
        print("Make sure backend is running: python backend.py")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "="*60)
    print("📋 SUMMARY")
    print("="*60)
    print("""
The issue is likely that the DataFrame index labels don't match
what the backend is looking for.

For example, backend looks for:
  - 'Diluted EPS' or 'Basic EPS'
  - 'Total Revenue' or 'Operating Revenue'
  - 'Stockholder' and 'Equity' (both in same label)
  - 'Total Assets'
  - 'Total Debt'

But the actual labels might be different (e.g., 'DilutedEPS' without space).

Share this output with Claude to fix the parsing!
""")

if __name__ == "__main__":
    main()
