#!/usr/bin/env python3
"""
Day 7 - Defeat Beta Deep Diagnostic
Explores the Statement object to find the correct way to access data
"""

def main():
    print("="*60)
    print("🔍 Defeat Beta Deep Diagnostic - Day 7")
    print("="*60)
    
    try:
        from defeatbeta_api.data.ticker import Ticker as DBTicker
        print("✅ Defeat Beta imported successfully\n")
    except ImportError as e:
        print(f"❌ Defeat Beta not installed: {e}")
        return
    
    ticker_symbol = "AVGO"
    print(f"📊 Testing {ticker_symbol}...\n")
    
    ticker = DBTicker(ticker_symbol)
    
    # =============================================
    # Explore the Statement object
    # =============================================
    print("="*60)
    print("1️⃣  EXPLORING ANNUAL INCOME STATEMENT OBJECT")
    print("="*60)
    
    try:
        annual_income = ticker.annual_income_statement()
        print(f"Type: {type(annual_income)}")
        print(f"\n📋 Available attributes/methods:")
        
        # List all attributes and methods
        for attr in dir(annual_income):
            if not attr.startswith('_'):
                try:
                    val = getattr(annual_income, attr)
                    if callable(val):
                        print(f"  🔧 {attr}() - method")
                    else:
                        val_type = type(val).__name__
                        val_preview = str(val)[:50] if val is not None else "None"
                        print(f"  📌 {attr}: {val_type} = {val_preview}")
                except Exception as e:
                    print(f"  ❌ {attr}: Error - {e}")
        
        # Try different ways to get data
        print(f"\n🔍 Trying to access data...")
        
        # Method 1: Try to_df()
        if hasattr(annual_income, 'to_df'):
            print("\n  Trying .to_df()...")
            try:
                df = annual_income.to_df()
                print(f"  Result type: {type(df)}")
                if df is not None:
                    if hasattr(df, 'columns'):
                        print(f"  Columns: {list(df.columns)[:3]}")
                        print(f"  Index (first 10): {list(df.index)[:10]}")
                    else:
                        print(f"  Value: {df}")
            except Exception as e:
                print(f"  Error: {e}")
        
        # Method 2: Try .data attribute
        if hasattr(annual_income, 'data'):
            print("\n  Trying .data attribute...")
            try:
                data = annual_income.data
                print(f"  Result type: {type(data)}")
                if isinstance(data, dict):
                    print(f"  Keys: {list(data.keys())[:10]}")
                elif hasattr(data, 'columns'):
                    print(f"  Columns: {list(data.columns)[:3]}")
            except Exception as e:
                print(f"  Error: {e}")
        
        # Method 3: Try .df attribute
        if hasattr(annual_income, 'df'):
            print("\n  Trying .df attribute...")
            try:
                df = annual_income.df
                print(f"  Result type: {type(df)}")
                if hasattr(df, 'columns'):
                    print(f"  Columns: {list(df.columns)[:3]}")
                    print(f"  Index (first 10): {list(df.index)[:10]}")
            except Exception as e:
                print(f"  Error: {e}")
        
        # Method 4: Try direct indexing
        print("\n  Trying direct indexing...")
        try:
            if hasattr(annual_income, '__getitem__'):
                print("  Has __getitem__, trying annual_income[0]...")
                print(f"  Result: {annual_income[0]}")
        except Exception as e:
            print(f"  Error: {e}")
            
        # Method 5: Try iteration
        print("\n  Trying iteration...")
        try:
            if hasattr(annual_income, '__iter__'):
                print("  Is iterable, getting first few items...")
                for i, item in enumerate(annual_income):
                    if i >= 3:
                        print("  ...")
                        break
                    print(f"  [{i}] {type(item)}: {str(item)[:80]}")
        except Exception as e:
            print(f"  Error: {e}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    # =============================================
    # Try quarterly statements instead
    # =============================================
    print("\n" + "="*60)
    print("2️⃣  TRYING QUARTERLY INCOME STATEMENT")
    print("="*60)
    
    try:
        quarterly = ticker.quarterly_income_statement()
        print(f"Type: {type(quarterly)}")
        
        if hasattr(quarterly, 'to_df'):
            df = quarterly.to_df()
            print(f"to_df() type: {type(df)}")
            if df is not None and hasattr(df, 'index'):
                print(f"Index (first 15): {list(df.index)[:15]}")
                print(f"Columns: {list(df.columns)[:4]}")
                
                # Try to get actual values
                print("\n🔍 Sample values:")
                for idx in list(df.index)[:5]:
                    try:
                        val = df.loc[idx].iloc[0]
                        print(f"  {idx}: {val}")
                    except:
                        pass
    except Exception as e:
        print(f"Error: {e}")
    
    # =============================================
    # Try other methods
    # =============================================
    print("\n" + "="*60)
    print("3️⃣  EXPLORING TICKER OBJECT METHODS")
    print("="*60)
    
    print("Available methods on Ticker object:")
    for attr in dir(ticker):
        if not attr.startswith('_') and callable(getattr(ticker, attr)):
            print(f"  🔧 {attr}()")
    
    # Try key_metrics if available
    if hasattr(ticker, 'key_metrics'):
        print("\n🔍 Trying key_metrics()...")
        try:
            metrics = ticker.key_metrics()
            print(f"Type: {type(metrics)}")
            if hasattr(metrics, 'to_df'):
                df = metrics.to_df()
                print(f"to_df() type: {type(df)}")
                if df is not None and hasattr(df, 'index'):
                    print(f"Index: {list(df.index)[:20]}")
        except Exception as e:
            print(f"Error: {e}")
    
    # Try ratios if available
    if hasattr(ticker, 'ratios'):
        print("\n🔍 Trying ratios()...")
        try:
            ratios = ticker.ratios()
            print(f"Type: {type(ratios)}")
            if hasattr(ratios, 'to_df'):
                df = ratios.to_df()
                print(f"to_df() type: {type(df)}")
                if df is not None and hasattr(df, 'index'):
                    print(f"Index: {list(df.index)[:20]}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "="*60)
    print("📋 DONE - Share this output with Claude!")
    print("="*60)

if __name__ == "__main__":
    main()
