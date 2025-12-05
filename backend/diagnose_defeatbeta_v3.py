#!/usr/bin/env python3
"""
Day 7 - See actual DataFrame contents from Defeat Beta
"""

def main():
    print("="*60)
    print("🔍 Defeat Beta DataFrame Contents")
    print("="*60)
    
    try:
        from defeatbeta_api.data.ticker import Ticker as DBTicker
        print("✅ Defeat Beta imported\n")
    except ImportError as e:
        print(f"❌ Defeat Beta not installed: {e}")
        return
    
    ticker = DBTicker("AVGO")
    
    # =============================================
    # Income Statement
    # =============================================
    print("="*60)
    print("1️⃣  ANNUAL INCOME STATEMENT - .data DataFrame")
    print("="*60)
    
    try:
        annual_income = ticker.annual_income_statement()
        df = annual_income.data
        
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(f"\nAll rows in 'Breakdown' column:")
        
        if 'Breakdown' in df.columns:
            for i, row in df.iterrows():
                breakdown = row.get('Breakdown', 'N/A')
                # Get first value column
                value_col = [c for c in df.columns if c != 'Breakdown'][0]
                value = row.get(value_col, 'N/A')
                print(f"  [{i}] {breakdown}: {value}")
        else:
            print("No 'Breakdown' column, showing index:")
            for idx in df.index:
                print(f"  {idx}")
                
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    # =============================================
    # Balance Sheet
    # =============================================
    print("\n" + "="*60)
    print("2️⃣  ANNUAL BALANCE SHEET - .data DataFrame")
    print("="*60)
    
    try:
        annual_balance = ticker.annual_balance_sheet()
        df = annual_balance.data
        
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print(f"\nAll rows in 'Breakdown' column:")
        
        if 'Breakdown' in df.columns:
            for i, row in df.iterrows():
                breakdown = row.get('Breakdown', 'N/A')
                value_col = [c for c in df.columns if c != 'Breakdown'][0]
                value = row.get(value_col, 'N/A')
                print(f"  [{i}] {breakdown}: {value}")
        else:
            print("No 'Breakdown' column, showing index:")
            for idx in df.index:
                print(f"  {idx}")
                
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

    print("\n" + "="*60)
    print("📋 Share this output with Claude to fix backend.py!")
    print("="*60)

if __name__ == "__main__":
    main()
