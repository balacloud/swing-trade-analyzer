#!/bin/bash
# Day 5 Installation Script - Defeat Beta Integration
# Run from: /Users/balajik/projects/swing-trade-analyzer/backend

echo "========================================"
echo "Day 5: Defeat Beta Integration Setup"
echo "========================================"
echo ""

# Activate virtual environment
echo "1. Activating virtual environment..."
source venv/bin/activate

# Check Python version
echo ""
echo "2. Python version:"
python --version

# Install Defeat Beta
echo ""
echo "3. Installing defeatbeta-api..."
pip install defeatbeta-api

# Verify installation
echo ""
echo "4. Verifying installation..."
python -c "import defeatbeta_api; print('✅ defeatbeta-api installed successfully')" 2>/dev/null || echo "❌ Installation failed"

# Test import
echo ""
echo "5. Testing Defeat Beta with AVGO..."
python << 'EOF'
try:
    from defeatbeta_api.data.ticker import Ticker
    ticker = Ticker('AVGO')
    
    # Test price data
    prices = ticker.price()
    print(f"✅ Price data: {len(prices)} records")
    
    # Test income statement
    income = ticker.annual_income_statement()
    print(f"✅ Income statement loaded")
    
    # Test balance sheet
    balance = ticker.annual_balance_sheet()
    print(f"✅ Balance sheet loaded")
    
    print("\n🎉 Defeat Beta is working!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nIf DuckDB errors occur, try:")
    print("pip install --upgrade duckdb")
EOF

echo ""
echo "========================================"
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Replace backend.py with the new version"
echo "2. Replace frontend/src/services/api.js"
echo "3. Replace frontend/src/utils/scoringEngine.js"
echo "4. Restart backend: python backend.py"
echo "5. Test with AVGO - should now score 60+ with BUY"
echo "========================================"
