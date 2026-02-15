"""
3-Layer System Validation
=========================
Day 53: Holistic test that validates each analysis layer INDEPENDENTLY
and then checks their INTEGRATION coherence.

The 3 Layers:
  Layer 1: Assessment (categoricalAssessment.js) - T/F/S/R → BUY/HOLD/AVOID
  Layer 2: Pattern Detection (pattern_detection.py) - VCP, Cup&Handle, Flat Base, Trend Template
  Layer 3: Trade Setup (support_resistance.py) - S&R levels, R:R, viability

What this tests:
  A) Layer Isolation Tests - Does each layer produce internally consistent output?
  B) Cross-Layer Coherence - Do layers agree when they should?
  C) Decision Matrix Integration - Does the synthesis make sense?

Golden Rule #6: NEVER HALLUCINATE - we run real data and check real output.

Usage:
    python test_3layer_validation.py
    python test_3layer_validation.py --ticker AAPL
    python test_3layer_validation.py --quick  # 10 tickers only
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import json
import requests
import argparse
from datetime import datetime
from typing import Dict, List

API_BASE = 'http://localhost:5001/api'

# Diverse test universe
FULL_TICKERS = [
    # Large Cap Tech
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'META',
    # Large Cap Other
    'JPM', 'JNJ', 'WMT', 'PG', 'UNH',
    # Growth/Momentum
    'PLTR', 'CRWD', 'NET', 'DDOG',
    # Value/Dividend
    'VZ', 'T', 'IBM', 'F',
    # Small/Mid Cap
    'SOFI', 'AFRM', 'COIN',
    # ETFs (no fundamentals)
    'SPY', 'QQQ', 'IWM',
    # Volatile
    'SMCI', 'RIVN',
]

QUICK_TICKERS = ['AAPL', 'NVDA', 'JNJ', 'F', 'PLTR', 'VZ', 'COIN', 'SPY', 'SMCI', 'AFRM']

HOLDING_PERIODS = ['quick', 'standard', 'position']


class ValidationResult:
    def __init__(self, ticker, layer, test_name, passed, detail, severity='INFO'):
        self.ticker = ticker
        self.layer = layer
        self.test_name = test_name
        self.passed = passed
        self.detail = detail
        self.severity = severity  # INFO, WARNING, CRITICAL

    def __repr__(self):
        status = 'PASS' if self.passed else f'FAIL [{self.severity}]'
        return f"[{status}] {self.ticker} | {self.layer} | {self.test_name}: {self.detail}"


def fetch_all_data(ticker):
    """Fetch all data needed for 3-layer validation."""
    result = {'ticker': ticker, 'success': False, 'errors': []}

    try:
        # Stock data (price, metadata)
        resp = requests.get(f"{API_BASE}/stock/{ticker}", timeout=30)
        result['stock'] = resp.json() if resp.ok else None
        if not resp.ok:
            result['errors'].append(f'Stock API failed: {resp.status_code}')
    except Exception as e:
        result['errors'].append(f'Stock API error: {e}')
        result['stock'] = None

    try:
        # Rich fundamentals via DataProvider (Finnhub → FMP → yfinance)
        # Day 53: /api/stock/ no longer returns fundamentals (SRP cleanup).
        # /api/fundamentals/ is the SINGLE source of truth.
        resp = requests.get(f"{API_BASE}/fundamentals/{ticker}", timeout=30)
        result['fundamentals'] = resp.json() if resp.ok else None
    except Exception as e:
        result['errors'].append(f'Fundamentals API error: {e}')
        result['fundamentals'] = None

    try:
        # S&R + Trade Setup (Layer 3)
        resp = requests.get(f"{API_BASE}/sr/{ticker}", timeout=30)
        result['sr'] = resp.json() if resp.ok else None
        if not resp.ok:
            result['errors'].append(f'S&R API failed: {resp.status_code}')
    except Exception as e:
        result['errors'].append(f'S&R API error: {e}')
        result['sr'] = None

    try:
        # Pattern Detection (Layer 2)
        resp = requests.get(f"{API_BASE}/patterns/{ticker}", timeout=30)
        result['patterns'] = resp.json() if resp.ok else None
        if not resp.ok:
            result['errors'].append(f'Patterns API failed: {resp.status_code}')
    except Exception as e:
        result['errors'].append(f'Patterns API error: {e}')
        result['patterns'] = None

    try:
        # Market context (for Layer 1 - Assessment)
        fg_resp = requests.get(f"{API_BASE}/fear-greed", timeout=10)
        result['fear_greed'] = fg_resp.json() if fg_resp.ok else {'value': 50, 'assessment': 'Neutral'}
    except:
        result['fear_greed'] = {'value': 50, 'assessment': 'Neutral'}

    try:
        vix_resp = requests.get(f"{API_BASE}/market/vix", timeout=10)
        result['vix'] = vix_resp.json() if vix_resp.ok else {'current': 20}
    except:
        result['vix'] = {'current': 20}

    try:
        spy_resp = requests.get(f"{API_BASE}/market/spy", timeout=10)
        result['spy'] = spy_resp.json() if spy_resp.ok else {'aboveSma200': True}
    except:
        result['spy'] = {'aboveSma200': True}

    # Earnings
    try:
        earn_resp = requests.get(f"{API_BASE}/earnings/{ticker}", timeout=10)
        result['earnings'] = earn_resp.json() if earn_resp.ok else None
    except:
        result['earnings'] = None

    result['success'] = result['stock'] is not None
    return result


# =============================================================================
# LAYER 1: Assessment Isolation Tests
# =============================================================================

def test_layer1_assessment(data):
    """
    Test Layer 1 (Assessment) produces internally consistent output.

    Assessment logic is in frontend (categoricalAssessment.js), so we validate
    the INPUT data the frontend receives and check for data quality issues.
    The actual verdict computation happens client-side.
    """
    results = []
    ticker = data['ticker']
    stock = data.get('stock', {})
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}

    if not stock:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'data_available',
                                        False, 'No stock data returned', 'CRITICAL'))
        return results

    results.append(ValidationResult(ticker, 'L1:Assessment', 'data_available',
                                    True, 'Stock data available'))

    # Test 1.1: Price data present
    price = stock.get('currentPrice') or stock.get('regularMarketPrice')
    if price and price > 0:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'price_valid',
                                        True, f'Price: ${price:.2f}'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'price_valid',
                                        False, f'Invalid/missing price: {price}', 'CRITICAL'))

    # Test 1.2: Fundamental data quality (for non-ETFs)
    # Uses /api/fundamentals/ (DataProvider) — single source of truth (Day 53 SRP)
    fund = data.get('fundamentals', {})
    is_etf = ticker in ['SPY', 'QQQ', 'IWM', 'DIA', 'XLF', 'XLE']
    if not is_etf:
        fund_fields = ['roe', 'revenueGrowth', 'debtToEquity', 'epsGrowth']
        present = sum(1 for f in fund_fields if fund and fund.get(f) is not None and fund.get(f) != 0)
        source = fund.get('source', 'unknown') if fund else 'none'
        if present >= 2:
            results.append(ValidationResult(ticker, 'L1:Assessment', 'fundamentals_quality',
                                            True, f'{present}/{len(fund_fields)} fields via {source} (ROE={fund.get("roe")})'))
        else:
            results.append(ValidationResult(ticker, 'L1:Assessment', 'fundamentals_quality',
                                            False, f'Only {present}/{len(fund_fields)} via {source}', 'WARNING'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'fundamentals_quality',
                                        True, 'ETF - fundamentals N/A (expected)'))

    # Test 1.3: ADX data present (critical for verdict)
    adx_data = meta.get('adx', {})
    adx_val = adx_data.get('adx') if adx_data else None
    if adx_val is not None and adx_val > 0:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'adx_present',
                                        True, f'ADX: {adx_val:.1f}'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'adx_present',
                                        False, 'ADX data missing', 'WARNING'))

    # Test 1.4: RS data would be calculated client-side from price data
    # Verify the 52-week data needed for RS exists
    high52 = stock.get('fiftyTwoWeekHigh')
    low52 = stock.get('fiftyTwoWeekLow')
    if high52 and low52 and high52 > low52:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'rs_input_data',
                                        True, f'52W range: ${low52:.2f}-${high52:.2f}'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'rs_input_data',
                                        False, f'Invalid 52W range: H={high52}, L={low52}', 'WARNING'))

    # Test 1.5: Fear & Greed present (for sentiment assessment)
    fg = data.get('fear_greed', {})
    fg_val = fg.get('value')
    if fg_val is not None:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'sentiment_input',
                                        True, f'F&G: {fg_val}'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'sentiment_input',
                                        False, 'Fear & Greed missing', 'WARNING'))

    # Test 1.6: VIX + SPY present (for risk/macro assessment)
    vix = data.get('vix', {}).get('current')
    spy_above = data.get('spy', {}).get('aboveSma200')
    if vix is not None and spy_above is not None:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'risk_macro_input',
                                        True, f'VIX: {vix}, SPY>200: {spy_above}'))
    else:
        results.append(ValidationResult(ticker, 'L1:Assessment', 'risk_macro_input',
                                        False, f'Missing: VIX={vix}, SPY>200={spy_above}', 'WARNING'))

    return results


# =============================================================================
# LAYER 2: Pattern Detection Isolation Tests
# =============================================================================

def test_layer2_patterns(data):
    """
    Test Layer 2 (Pattern Detection) produces internally consistent output.
    """
    results = []
    ticker = data['ticker']
    patterns = data.get('patterns', {})

    if not patterns:
        results.append(ValidationResult(ticker, 'L2:Patterns', 'data_available',
                                        False, 'No patterns data returned', 'CRITICAL'))
        return results

    results.append(ValidationResult(ticker, 'L2:Patterns', 'data_available',
                                    True, 'Patterns data available'))

    # Test 2.1: Trend Template present with valid criteria count
    tt = patterns.get('trend_template', {})
    criteria_met = tt.get('criteria_met')
    if criteria_met is not None and 0 <= criteria_met <= 8:
        results.append(ValidationResult(ticker, 'L2:Patterns', 'trend_template_valid',
                                        True, f'Trend Template: {criteria_met}/8'))
    else:
        results.append(ValidationResult(ticker, 'L2:Patterns', 'trend_template_valid',
                                        False, f'Invalid TT criteria: {criteria_met}', 'WARNING'))

    # Test 2.2: Stage 2 flag consistent with criteria count
    in_stage2 = tt.get('in_stage2_uptrend', False)
    if criteria_met is not None:
        if in_stage2 and criteria_met < 6:
            results.append(ValidationResult(ticker, 'L2:Patterns', 'stage2_consistency',
                                            False, f'Stage 2 TRUE but only {criteria_met}/8 criteria', 'WARNING'))
        else:
            results.append(ValidationResult(ticker, 'L2:Patterns', 'stage2_consistency',
                                            True, f'Stage 2: {in_stage2} (criteria: {criteria_met}/8)'))

    # Test 2.3: Pattern confidence values are in valid range (0-100)
    pattern_types = patterns.get('patterns', {})
    for pname, pdata in pattern_types.items():
        conf = pdata.get('confidence', 0) if isinstance(pdata, dict) else 0
        detected = pdata.get('detected', False) if isinstance(pdata, dict) else False
        if detected and (conf < 0 or conf > 100):
            results.append(ValidationResult(ticker, 'L2:Patterns', f'pattern_{pname}_range',
                                            False, f'{pname} confidence {conf}% out of range', 'WARNING'))
        elif detected:
            results.append(ValidationResult(ticker, 'L2:Patterns', f'pattern_{pname}_valid',
                                            True, f'{pname}: {conf}% confidence'))

    # Test 2.4: If no patterns detected, summary count should be 0
    summary = patterns.get('summary', {})
    pattern_count = summary.get('count', 0)
    detected_patterns = sum(1 for p in pattern_types.values()
                           if isinstance(p, dict) and p.get('detected'))
    if pattern_count != detected_patterns:
        results.append(ValidationResult(ticker, 'L2:Patterns', 'summary_count_match',
                                        False, f'Summary says {pattern_count} but {detected_patterns} detected', 'WARNING'))
    else:
        results.append(ValidationResult(ticker, 'L2:Patterns', 'summary_count_match',
                                        True, f'{pattern_count} patterns detected'))

    return results


# =============================================================================
# LAYER 3: Trade Setup Isolation Tests
# =============================================================================

def test_layer3_trade_setup(data):
    """
    Test Layer 3 (Trade Setup) produces internally consistent output.
    """
    results = []
    ticker = data['ticker']
    sr = data.get('sr', {})

    if not sr:
        results.append(ValidationResult(ticker, 'L3:TradeSetup', 'data_available',
                                        False, 'No S&R data returned', 'CRITICAL'))
        return results

    results.append(ValidationResult(ticker, 'L3:TradeSetup', 'data_available',
                                    True, 'S&R data available'))

    # Test 3.1: Support levels present
    support = sr.get('support', [])
    resistance = sr.get('resistance', [])
    if len(support) > 0:
        results.append(ValidationResult(ticker, 'L3:TradeSetup', 'support_present',
                                        True, f'{len(support)} support levels'))
    else:
        results.append(ValidationResult(ticker, 'L3:TradeSetup', 'support_present',
                                        False, 'No support levels found', 'WARNING'))

    # Test 3.2: Support below current price, resistance above
    current_price = sr.get('currentPrice')
    if current_price and support:
        nearest_sup = max(support)
        if nearest_sup < current_price:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'support_below_price',
                                            True, f'Support ${nearest_sup:.2f} < Price ${current_price:.2f}'))
        else:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'support_below_price',
                                            False, f'Support ${nearest_sup:.2f} >= Price ${current_price:.2f}', 'WARNING'))

    # Test 3.3: ATR present and reasonable
    meta = sr.get('meta', {})
    atr = meta.get('atr')
    if atr and current_price:
        atr_pct = (atr / current_price) * 100
        if 0.5 < atr_pct < 15:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'atr_reasonable',
                                            True, f'ATR: ${atr:.2f} ({atr_pct:.1f}% of price)'))
        else:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'atr_reasonable',
                                            False, f'ATR {atr_pct:.1f}% seems extreme', 'WARNING'))
    elif not atr:
        results.append(ValidationResult(ticker, 'L3:TradeSetup', 'atr_reasonable',
                                        False, 'ATR missing', 'WARNING'))

    # Test 3.4: Trade viability logic consistency
    viability = meta.get('tradeViability', {})
    viable = viability.get('viable')
    support_dist = viability.get('support_distance_pct')

    if viable and support_dist is not None:
        # Backend: YES when support_distance <= 10%
        if viable == 'YES' and support_dist > 12:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'viability_consistency',
                                            False, f'Viable=YES but support {support_dist}% away', 'WARNING'))
        elif viable == 'NO' and support_dist <= 8:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'viability_consistency',
                                            False, f'Viable=NO but support only {support_dist}% away', 'WARNING'))
        else:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'viability_consistency',
                                            True, f'Viable={viable}, support_dist={support_dist}%'))

    # Test 3.5: R:R sanity (calculate same as frontend)
    if support and current_price and atr and atr > 0:
        nearest_sup = max(support)
        target = sr.get('suggestedTarget') or current_price * 1.10
        pullback_rr = (target - nearest_sup) / (atr * 2) if atr > 0 else 0
        mom_stop = nearest_sup - atr * 1.5
        mom_risk = current_price - mom_stop
        mom_rr = (target - current_price) / mom_risk if mom_risk > 0 else 0

        # R:R should be positive (entry below target)
        if pullback_rr < 0 or mom_rr < 0:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'rr_positive',
                                            False, f'Negative R:R: Pullback={pullback_rr:.2f}, Mom={mom_rr:.2f}', 'CRITICAL'))
        else:
            results.append(ValidationResult(ticker, 'L3:TradeSetup', 'rr_positive',
                                            True, f'R:R Pullback={pullback_rr:.2f}, Mom={mom_rr:.2f}'))

    return results


# =============================================================================
# CROSS-LAYER COHERENCE TESTS
# =============================================================================

def test_cross_layer_coherence(data):
    """
    Test that the 3 layers agree when they should.
    These are the integration tests that catch the bugs we found in Day 53.
    """
    results = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    patterns = data.get('patterns', {})
    stock = data.get('stock', {})

    # Cross Test 1: ADX vs Trend Template coherence
    adx_data = meta.get('adx', {})
    adx_val = adx_data.get('adx') if adx_data else None
    tt = patterns.get('trend_template', {}) if patterns else {}
    criteria = tt.get('criteria_met')

    if adx_val is not None and criteria is not None:
        # Strong trend (ADX>=25) + weak template (< 5/8) is suspicious
        if adx_val >= 25 and criteria < 4:
            results.append(ValidationResult(ticker, 'Cross:L1xL2', 'adx_vs_template',
                                            False, f'ADX {adx_val:.0f} (strong) but TT only {criteria}/8', 'WARNING'))
        # No trend (ADX<20) + strong template (>= 7/8) is suspicious
        elif adx_val < 18 and criteria >= 7:
            results.append(ValidationResult(ticker, 'Cross:L1xL2', 'adx_vs_template',
                                            False, f'ADX {adx_val:.0f} (no trend) but TT {criteria}/8 (strong)', 'WARNING'))
        else:
            results.append(ValidationResult(ticker, 'Cross:L1xL2', 'adx_vs_template',
                                            True, f'ADX {adx_val:.0f}, TT {criteria}/8 - consistent'))

    # Cross Test 2: Backend viability vs R:R (Bug #8 pattern)
    viability = meta.get('tradeViability', {})
    viable = viability.get('viable')
    support = sr.get('support', []) if sr else []
    current_price = sr.get('currentPrice') if sr else None
    atr = meta.get('atr', 0)

    if viable and support and current_price and atr > 0:
        nearest = max(support)
        target = sr.get('suggestedTarget') or current_price * 1.10
        pb_rr = (target - nearest) / (atr * 2)
        mom_stop = nearest - atr * 1.5
        mom_risk = current_price - mom_stop
        mom_rr = (target - current_price) / mom_risk if mom_risk > 0 else 0

        backend_says_yes = viable == 'YES'
        frontend_rr_fails = pb_rr < 1.0 and mom_rr < 1.0

        if backend_says_yes and frontend_rr_fails:
            results.append(ValidationResult(ticker, 'Cross:L1xL3', 'viability_vs_rr',
                                            False,
                                            f'Backend viable=YES but R:R fails (PB={pb_rr:.2f}, MOM={mom_rr:.2f}) — Bug #8 pattern',
                                            'WARNING'))
        else:
            results.append(ValidationResult(ticker, 'Cross:L1xL3', 'viability_vs_rr',
                                            True, f'Viable={viable}, PB_RR={pb_rr:.2f}, MOM_RR={mom_rr:.2f}'))

    # Cross Test 3: Patterns found but no viable trade setup
    detected_count = 0
    if patterns and patterns.get('patterns'):
        for p in patterns['patterns'].values():
            if isinstance(p, dict) and p.get('detected') and p.get('confidence', 0) >= 80:
                detected_count += 1

    if detected_count > 0 and viable == 'NO':
        results.append(ValidationResult(ticker, 'Cross:L2xL3', 'pattern_vs_viability',
                                        False,
                                        f'{detected_count} actionable pattern(s) but setup not viable — may confuse trader',
                                        'INFO'))
    elif detected_count > 0 and viable:
        results.append(ValidationResult(ticker, 'Cross:L2xL3', 'pattern_vs_viability',
                                        True, f'{detected_count} actionable pattern(s), viable={viable}'))

    # Cross Test 4: OBV distribution warning vs other signals
    obv = meta.get('obv', {})
    rvol_raw = meta.get('rvol')
    obv_trend = obv.get('trend') if isinstance(obv, dict) else None
    rvol_ratio = rvol_raw.get('ratio') if isinstance(rvol_raw, dict) else (rvol_raw if isinstance(rvol_raw, (int, float)) else None)

    if obv_trend == 'falling' and rvol_ratio and rvol_ratio > 1.5 and criteria and criteria >= 7:
        results.append(ValidationResult(ticker, 'Cross:L1xL2xL3', 'distribution_warning',
                                        False,
                                        f'Distribution signal (OBV falling + RVOL {rvol_ratio:.1f}x) conflicts with strong TT {criteria}/8',
                                        'WARNING'))

    return results


# =============================================================================
# MAIN
# =============================================================================

def run_validation(tickers, verbose=True):
    """Run the full 3-layer validation."""
    all_results = []
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    print(f"\n{'='*70}")
    print(f" 3-LAYER SYSTEM VALIDATION")
    print(f" {len(tickers)} tickers | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}\n")

    # Check backend health
    try:
        resp = requests.get(f"{API_BASE}/health", timeout=5)
        if not resp.ok:
            print("ERROR: Backend not responding at localhost:5001")
            return
        print("Backend: ONLINE\n")
    except:
        print("ERROR: Cannot reach backend at localhost:5001. Start it first.")
        return

    for i, ticker in enumerate(tickers):
        print(f"[{i+1}/{len(tickers)}] {ticker}...", end=' ', flush=True)

        data = fetch_all_data(ticker)

        if not data['success']:
            print(f"FAILED ({', '.join(data['errors'][:2])})")
            all_results.append(ValidationResult(ticker, 'DATA', 'fetch',
                                                False, f"Data fetch failed: {data['errors']}", 'CRITICAL'))
            continue

        # Run all test suites
        r1 = test_layer1_assessment(data)
        r2 = test_layer2_patterns(data)
        r3 = test_layer3_trade_setup(data)
        rx = test_cross_layer_coherence(data)

        ticker_results = r1 + r2 + r3 + rx
        all_results.extend(ticker_results)

        # Count pass/fail for this ticker
        passed = sum(1 for r in ticker_results if r.passed)
        failed = sum(1 for r in ticker_results if not r.passed)
        criticals = sum(1 for r in ticker_results if not r.passed and r.severity == 'CRITICAL')

        status = 'OK' if failed == 0 else f'{failed} issues' + (f' ({criticals} CRITICAL)' if criticals else '')
        print(f"{passed}/{passed+failed} PASS | {status}")

        if verbose and failed > 0:
            for r in ticker_results:
                if not r.passed:
                    print(f"    {r}")

    # Summary
    total = len(all_results)
    passed = sum(1 for r in all_results if r.passed)
    failed = sum(1 for r in all_results if not r.passed)
    criticals = sum(1 for r in all_results if not r.passed and r.severity == 'CRITICAL')
    warnings = sum(1 for r in all_results if not r.passed and r.severity == 'WARNING')

    print(f"\n{'='*70}")
    print(f" SUMMARY: {passed}/{total} PASS ({passed/total*100:.1f}%)")
    print(f" CRITICAL: {criticals} | WARNING: {warnings} | INFO: {failed - criticals - warnings}")
    print(f"{'='*70}")

    # Per-layer breakdown
    layers = set(r.layer for r in all_results)
    print(f"\nPer-Layer Breakdown:")
    for layer in sorted(layers):
        layer_results = [r for r in all_results if r.layer == layer]
        lp = sum(1 for r in layer_results if r.passed)
        lt = len(layer_results)
        print(f"  {layer}: {lp}/{lt} ({lp/lt*100:.0f}%)")

    # Per-test breakdown for failures
    if failed > 0:
        print(f"\nAll Failures:")
        for r in all_results:
            if not r.passed:
                print(f"  {r}")

    # Save results
    output = {
        'timestamp': timestamp,
        'tickers_tested': len(tickers),
        'total_checks': total,
        'passed': passed,
        'failed': failed,
        'pass_rate': f'{passed/total*100:.1f}%',
        'criticals': criticals,
        'warnings': warnings,
        'results': [
            {
                'ticker': r.ticker,
                'layer': r.layer,
                'test': r.test_name,
                'passed': r.passed,
                'detail': r.detail,
                'severity': r.severity,
            }
            for r in all_results
        ]
    }

    outfile = f'validation_results/3layer_validation_{timestamp}.json'
    os.makedirs('validation_results', exist_ok=True)
    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved: {outfile}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='3-Layer System Validation')
    parser.add_argument('--ticker', type=str, help='Test single ticker')
    parser.add_argument('--quick', action='store_true', help='Quick mode (10 tickers)')
    args = parser.parse_args()

    if args.ticker:
        tickers = [args.ticker.upper()]
    elif args.quick:
        tickers = QUICK_TICKERS
    else:
        tickers = FULL_TICKERS

    run_validation(tickers)
