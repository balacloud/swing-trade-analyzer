# Comprehensive Test Plan - Swing Trade Analyzer

> **Version:** 1.0
> **Created:** Day 45 (February 5, 2026)
> **Purpose:** Systematic testing of v4.5 Categorical Assessment System
> **Approach:** Quant developer methodology - edge cases, validation, diverse tickers

---

## Executive Summary

This test plan validates the Swing Trade Analyzer after implementing Perplexity research recommendations:
1. **F&G Threshold Fix** - Expand neutral zone (35-60)
2. **Entry Preference Logic** - ADX-based recommendation
3. **Pattern Actionability** - Only show ≥80% patterns
4. **Sentiment/Structure Hierarchy** - Structure overrides sentiment

---

## Test Categories

| Category | What We Test | How We Test |
|----------|-------------|-------------|
| A. API Contract | Backend returns expected structure | Automated validation scripts |
| B. Categorical Logic | Assessment thresholds work correctly | Unit tests + manual verification |
| C. Edge Cases | Unusual stocks, missing data, extremes | Curated ticker list |
| D. Cross-Validation | Our data matches external sources | Validation engine |
| E. Integration | Frontend displays match backend | Manual + screenshot comparison |
| F. Forward Testing | Track real signal performance | Forward test tracker |

---

## CATEGORY A: API Contract Tests

### Test A1: Core Endpoints Return Expected Structure

| Endpoint | Expected Fields | Test Command |
|----------|-----------------|--------------|
| `/api/stock/<ticker>` | prices, technicals, fundamentals | `curl http://localhost:5001/api/stock/AAPL` |
| `/api/fear-greed` | value, rating, source | `curl http://localhost:5001/api/fear-greed` |
| `/api/market/vix` | current, regime | `curl http://localhost:5001/api/market/vix` |
| `/api/market/spy` | aboveSma200, prices | `curl http://localhost:5001/api/market/spy` |
| `/api/patterns/<ticker>` | trend_template, vcp, cup_handle | `curl http://localhost:5001/api/patterns/AAPL` |
| `/api/fundamentals/<ticker>` | roe, revenueGrowth, debtToEquity | `curl http://localhost:5001/api/fundamentals/AAPL` |

### Test A2: Error Handling

| Scenario | Expected Behavior |
|----------|-------------------|
| Invalid ticker (XXXXX) | Returns error gracefully, no crash |
| OTC ticker (TCEHY) | Returns data or graceful error |
| ETF (SPY) | Fundamentals marked as N/A |
| Delisted ticker | Returns error message |

---

## CATEGORY B: Categorical Logic Tests

### Test B1: Sentiment (Fear & Greed) Thresholds

**Current Thresholds (PROBLEMATIC):**
```
Strong:  55-75
Neutral: 45-55
Weak:    25-45 OR <25 OR >75
```

**Proposed Thresholds (TO IMPLEMENT):**
```
Strong:  60-80
Neutral: 35-60  ← EXPANDED buffer zone
Weak:    <35 OR >80
```

**Test Cases:**

| F&G Value | Current Assessment | Expected Assessment | Issue |
|-----------|-------------------|---------------------|-------|
| 44.7 | Weak | Neutral (Cautious) | Cliff at 45 |
| 45.0 | Neutral | Neutral | OK |
| 35 | Weak | Neutral (Cautious) | New lower bound |
| 55 | Strong | Neutral (Optimistic) | Move threshold |
| 60 | Strong | Strong | OK |
| 80 | Strong | Weak | Extreme greed |
| 25 | Weak | Weak | OK (extreme fear) |

### Test B2: Technical Assessment Thresholds

| Trend Template | RSI | RS | Expected Assessment |
|----------------|-----|----|--------------------|
| 8/8 | 55 | 1.2 | Strong |
| 7/8 | 65 | 1.0 | Strong |
| 6/8 | 50 | 1.0 | Decent |
| 5/8 | 45 | 0.9 | Decent |
| 4/8 | 35 | 0.8 | Weak |
| 0/8 | 25 | 0.6 | Weak |
| 7/8 | 85 | 1.0 | Decent (RSI overbought) |
| 7/8 | 25 | 1.0 | Weak (RSI oversold) |

### Test B3: Risk/Macro Assessment

| VIX | SPY vs 200 EMA | Expected Assessment |
|-----|----------------|---------------------|
| 15 | Above | Favorable |
| 18 | Above | Favorable |
| 22 | Above | Neutral |
| 25 | Above | Neutral |
| 35 | Above | Unfavorable |
| 15 | Below | Unfavorable |
| 25 | Below | Unfavorable |

### Test B4: Verdict Logic

| Technical | Fundamental | Sentiment | Risk/Macro | Expected Verdict |
|-----------|-------------|-----------|------------|------------------|
| Strong | Strong | Strong | Favorable | BUY |
| Strong | Strong | Neutral | Favorable | BUY |
| Strong | Decent | Strong | Favorable | BUY |
| Strong | Decent | Weak | Favorable | HOLD |
| Decent | Decent | Neutral | Favorable | HOLD |
| Weak | Strong | Strong | Favorable | AVOID |
| Strong | Strong | Strong | Unfavorable | HOLD |
| Decent | Weak | Weak | Favorable | AVOID |

---

## CATEGORY C: Edge Case Test Tickers

### Tier 1: Standard Large-Cap (Baseline)
| Ticker | Why Selected | Expected Behavior |
|--------|-------------|-------------------|
| AAPL | High-quality data | All assessments work |
| NVDA | High volatility | RSI extremes possible |
| JPM | Financial sector | Different debt metrics |
| MSFT | Mega-cap | Strong fundamentals |
| COST | Retail | Steady performer |

### Tier 2: Edge Cases - Data Quality
| Ticker | Why Selected | What We Test |
|--------|-------------|--------------|
| SPY | ETF | Fundamentals = N/A |
| QQQ | ETF | Fundamentals = N/A |
| BRK.B | No dividend, unique structure | Handles special cases |
| GOOGL | Class A shares | vs GOOG class C |
| TCEHY | OTC/ADR | Data availability |

### Tier 3: Edge Cases - Technical Extremes
| Ticker | Why Selected | What We Test |
|--------|-------------|--------------|
| (Any oversold) | RSI < 30 | Weak technical assessment |
| (Any overbought) | RSI > 80 | RSI warning |
| (Any downtrend) | Below 200 SMA | Stage 4 detection |
| (Any new high) | Breaking out | Strong technical |

### Tier 4: Edge Cases - Fundamental Extremes
| Ticker | Why Selected | What We Test |
|--------|-------------|--------------|
| TSLA | Extreme P/E | Handles outliers |
| AMC | Negative earnings | Weak fundamental |
| (High debt stock) | D/E > 2.0 | Debt warning |
| (Turnaround stock) | Negative ROE | Handles negative ROE |

### Tier 5: Edge Cases - Pattern Detection
| Ticker | Why Selected | What We Test |
|--------|-------------|--------------|
| (VCP forming) | Pattern detection | Shows 80%+ only |
| (Cup & Handle) | Pattern detection | Actionable trigger |
| (No pattern) | Baseline | No false positives |

---

## CATEGORY D: Cross-Validation Tests

### Test D1: Run Existing Validation Engine

```bash
# Run validation with default tickers
curl -X POST http://localhost:5001/api/validation/run

# Check results
curl http://localhost:5001/api/validation/results
```

**Target Metrics:**
- Coverage Rate: > 90%
- Accuracy Rate: > 95%
- Quality Score: > 90%

### Test D2: Spot-Check Against External Sources

| Metric | Our Source | Validation Source | Tolerance |
|--------|------------|-------------------|-----------|
| Current Price | yfinance | StockAnalysis | 2% |
| ROE | Defeat Beta | Finviz | 20% |
| Revenue Growth | Defeat Beta | Finviz | 85% |
| 52-Week High | yfinance | StockAnalysis | 1% |
| RSI | Local calc | TradingView | 5% |

### Test D3: Fear & Greed Consistency

```bash
# Check our F&G value matches CNN
curl http://localhost:5001/api/fear-greed

# Manual verification: https://edition.cnn.com/markets/fear-and-greed
```

---

## CATEGORY E: Integration Tests (Frontend-Backend)

### Test E1: Categorical Assessment Display

For each test ticker, verify:
1. **Technical assessment** shows correct color (green/yellow/red)
2. **Fundamental assessment** shows correct reasons
3. **Sentiment assessment** shows correct F&G value
4. **Risk/Macro assessment** shows VIX and SPY status
5. **Verdict** matches expected logic

### Test E2: Entry Strategy Display

For each ticker with Technical Strong/Decent:
1. Both Pullback and Momentum entries shown
2. Stop levels are reasonable (below support)
3. Targets are reasonable (R:R > 1.5)
4. Entry preference is stated (if ADX logic implemented)

### Test E3: Pattern Detection Display

For each ticker:
1. Pattern only shown if ≥80% formed (if implemented)
2. Actionable trigger price shown
3. Stop level shown
4. No "75% forming" without action

---

## CATEGORY F: Forward Testing Framework

### Test F1: Signal Recording

```bash
# Record a test signal
curl -X POST http://localhost:5001/api/forward-test/record \
  -H "Content-Type: application/json" \
  -d '{
    "ticker": "AAPL",
    "signal_type": "BUY",
    "entry_price": 180.00,
    "stop_price": 170.00,
    "target_price": 200.00
  }'

# Retrieve signals
curl http://localhost:5001/api/forward-test/signals
```

### Test F2: Outcome Tracking

Track signals over time to measure:
- Win rate by verdict (BUY vs HOLD signals)
- Average R-multiple achieved
- Time to outcome (hit target, hit stop, timed out)

---

## Test Execution Schedule

### Phase 1: Pre-Fix Baseline (Today)
1. Run validation engine - capture current metrics
2. Test 5 Tier 1 tickers - document current behavior
3. Note F&G cliff behavior at current thresholds

### Phase 2: Implement F&G Fix
1. Update categoricalAssessment.js thresholds
2. Re-run Test B1 cases
3. Verify 44.7 now shows "Neutral (Cautious)"

### Phase 3: Full Test Suite
1. Test all 20+ edge case tickers
2. Run cross-validation
3. Document any failures

### Phase 4: Forward Testing Setup
1. Record 10 current BUY signals
2. Set up tracking schedule (daily price check)
3. Document outcomes over 2-4 weeks

---

## Automated Test Script

Create `backend/test_categorical_comprehensive.py`:

```python
#!/usr/bin/env python3
"""
Comprehensive Categorical Assessment Test Suite
Day 45 - Tests all assessment logic with edge cases
"""

import requests
import json

BASE_URL = "http://localhost:5001/api"

# Test Tickers by Category
TIER_1_STANDARD = ["AAPL", "NVDA", "JPM", "MSFT", "COST"]
TIER_2_ETFS = ["SPY", "QQQ"]
TIER_3_TECHNICAL = []  # To be populated based on current market
TIER_4_FUNDAMENTAL = ["TSLA", "AMC"]
TIER_5_PATTERNS = []  # To be populated

def test_api_health():
    """Test A1: API health check"""
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    print("✅ API health check passed")

def test_fear_greed():
    """Test F&G endpoint returns expected structure"""
    r = requests.get(f"{BASE_URL}/fear-greed")
    data = r.json()
    assert "value" in data
    assert "rating" in data
    print(f"✅ Fear & Greed: {data['value']} ({data['rating']})")
    return data['value']

def test_stock_full(ticker):
    """Test full stock analysis"""
    r = requests.get(f"{BASE_URL}/stock/{ticker}")
    data = r.json()

    # Check structure
    assert "prices" in data or "error" not in data
    print(f"✅ {ticker}: Stock data retrieved")
    return data

def test_patterns(ticker):
    """Test pattern detection endpoint"""
    r = requests.get(f"{BASE_URL}/patterns/{ticker}")
    data = r.json()

    # Check trend template
    if "trend_template" in data:
        tt = data["trend_template"]
        print(f"  Trend Template: {tt.get('criteria_met', 0)}/8")
    return data

def test_fundamentals(ticker):
    """Test fundamentals endpoint"""
    r = requests.get(f"{BASE_URL}/fundamentals/{ticker}")
    data = r.json()

    if "error" not in data:
        roe = data.get("roe", "N/A")
        rev = data.get("revenueGrowth", "N/A")
        print(f"  Fundamentals: ROE={roe}, RevGrowth={rev}")
    return data

def test_categorical_logic():
    """Test B1-B4: Categorical assessment logic"""
    # This tests the frontend logic - manual verification needed
    print("\n📋 Categorical Logic Tests (verify in UI):")
    print("  - F&G 44.7 should be Neutral (Cautious), not Weak")
    print("  - VIX < 20 + SPY > 200 EMA = Favorable")
    print("  - Technical Weak = AVOID regardless of other factors")

def run_tier_tests(tickers, tier_name):
    """Run tests for a tier of tickers"""
    print(f"\n{'='*50}")
    print(f"Testing {tier_name}")
    print('='*50)

    results = []
    for ticker in tickers:
        print(f"\n--- {ticker} ---")
        try:
            stock_data = test_stock_full(ticker)
            pattern_data = test_patterns(ticker)
            fund_data = test_fundamentals(ticker)
            results.append({
                "ticker": ticker,
                "status": "PASS",
                "data": {"stock": stock_data, "patterns": pattern_data, "fundamentals": fund_data}
            })
        except Exception as e:
            print(f"❌ {ticker}: {str(e)}")
            results.append({"ticker": ticker, "status": "FAIL", "error": str(e)})

    return results

def main():
    print("="*60)
    print("COMPREHENSIVE CATEGORICAL ASSESSMENT TEST SUITE")
    print("Day 45 - Swing Trade Analyzer")
    print("="*60)

    # Test A1: Health
    test_api_health()

    # Test F&G
    fg_value = test_fear_greed()

    # Test Tier 1
    tier1_results = run_tier_tests(TIER_1_STANDARD, "Tier 1: Standard Large-Cap")

    # Test Tier 2 (ETFs)
    tier2_results = run_tier_tests(TIER_2_ETFS, "Tier 2: ETFs")

    # Test Tier 4 (Fundamental extremes)
    tier4_results = run_tier_tests(TIER_4_FUNDAMENTAL, "Tier 4: Fundamental Extremes")

    # Test categorical logic
    test_categorical_logic()

    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    all_results = tier1_results + tier2_results + tier4_results
    passed = sum(1 for r in all_results if r["status"] == "PASS")
    failed = sum(1 for r in all_results if r["status"] == "FAIL")
    print(f"Passed: {passed}/{len(all_results)}")
    print(f"Failed: {failed}/{len(all_results)}")
    print(f"Current F&G: {fg_value}")

    # Run validation engine
    print("\n--- Running Validation Engine ---")
    try:
        r = requests.post(f"{BASE_URL}/validation/run", timeout=60)
        if r.status_code == 200:
            val_data = r.json()
            print(f"✅ Validation: {val_data.get('overall_pass_rate', 'N/A')}% pass rate")
    except Exception as e:
        print(f"⚠️ Validation engine: {str(e)}")

if __name__ == "__main__":
    main()
```

---

## Success Criteria

| Metric | Target | Current |
|--------|--------|---------|
| API Contract Pass Rate | 100% | TBD |
| Categorical Logic Accuracy | 100% | TBD |
| Edge Case Handling | 90%+ | TBD |
| Cross-Validation Quality | 90%+ | 92.3% ✅ |
| F&G Threshold Behavior | No cliffs | TBD |

---

## Post-Test Actions

After testing:
1. Document any failures in KNOWN_ISSUES
2. Update ROADMAP with findings
3. Prioritize fixes based on severity
4. Re-run affected tests after fixes

---

## Next Steps: Forward Testing UI (v4.0 Priority)

After validation complete:
1. Design Forward Test UI component
2. Display tracked signals with outcomes
3. Calculate running SQN (System Quality Number)
4. Show win rate, average R, expectancy

---

*This test plan follows quant developer methodology: diverse tickers, edge cases, automated validation, manual spot-checks.*
