"""
Indicator Coherence Test Suite
Day 49 (v4.10) - Self-correcting test to ensure all indicators work together logically

Tests 30 diverse stocks and checks for:
1. ADX vs Verdict coherence (ADX < 20 should not get BUY)
2. ADX vs Entry Strategy coherence (ADX < 25 should not suggest Momentum)
3. OBV vs Price trend coherence
4. R:R sanity check (never suggest R:R < 1.0)
5. Volume vs OBV coherence
6. Trend Template vs ADX coherence
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import json
import requests
from datetime import datetime
from typing import Dict, List, Tuple

# Test tickers - diverse mix
TEST_TICKERS = [
    # Large Cap Tech
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'META',
    # Large Cap Other
    'JPM', 'JNJ', 'WMT', 'PG', 'UNH',
    # Growth/Momentum
    'PLTR', 'CRWD', 'NET', 'SNOW', 'DDOG',
    # Value/Dividend
    'VZ', 'T', 'IBM', 'INTC', 'F',
    # Small/Mid Cap
    'SOFI', 'AFRM', 'RBLX', 'U', 'COIN',
    # ETFs
    'SPY', 'QQQ', 'IWM',
    # Volatile/Recent movers
    'CIEN', 'SMCI',
]

API_BASE = 'http://localhost:5001/api'


class CoherenceIssue:
    """Represents a coherence issue found during testing"""
    def __init__(self, ticker: str, issue_type: str, severity: str,
                 description: str, expected: str, actual: str, data: dict = None):
        self.ticker = ticker
        self.issue_type = issue_type
        self.severity = severity  # 'CRITICAL', 'WARNING', 'INFO'
        self.description = description
        self.expected = expected
        self.actual = actual
        self.data = data or {}

    def __repr__(self):
        return f"[{self.severity}] {self.ticker}: {self.issue_type} - {self.description}"


def fetch_analysis(ticker: str) -> dict:
    """Fetch full analysis data for a ticker"""
    try:
        # Fetch S&R data (includes ADX, RSI, OBV, RVOL)
        sr_resp = requests.get(f"{API_BASE}/sr/{ticker}", timeout=30)
        sr_data = sr_resp.json() if sr_resp.ok else None

        # Fetch patterns (includes Trend Template)
        patterns_resp = requests.get(f"{API_BASE}/patterns/{ticker}", timeout=30)
        patterns_data = patterns_resp.json() if patterns_resp.ok else None

        # Fetch stock data
        stock_resp = requests.get(f"{API_BASE}/stock/{ticker}", timeout=30)
        stock_data = stock_resp.json() if stock_resp.ok else None

        # Fetch Fear & Greed
        fg_resp = requests.get(f"{API_BASE}/fear-greed", timeout=10)
        fg_data = fg_resp.json() if fg_resp.ok else {'value': 50, 'assessment': 'Neutral'}

        # Fetch VIX
        vix_resp = requests.get(f"{API_BASE}/market/vix", timeout=10)
        vix_data = vix_resp.json() if vix_resp.ok else {'current': 20}

        # Fetch SPY
        spy_resp = requests.get(f"{API_BASE}/market/spy", timeout=10)
        spy_data = spy_resp.json() if spy_resp.ok else {'aboveSma200': True}

        return {
            'ticker': ticker,
            'sr': sr_data,
            'patterns': patterns_data,
            'stock': stock_data,
            'fear_greed': fg_data,
            'vix': vix_data,
            'spy': spy_data,
            'success': True
        }
    except Exception as e:
        return {'ticker': ticker, 'error': str(e), 'success': False}


def check_adx_verdict_coherence(data: dict) -> List[CoherenceIssue]:
    """
    Check: ADX < 20 with 2+ Strong categories should be HOLD, not BUY

    Logic: Even with good categories, choppy markets (ADX < 20) increase failure rate
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    adx_data = meta.get('adx', {})

    if not adx_data:
        return issues

    adx_value = adx_data.get('adx')
    if adx_value is None:
        return issues

    # We need to simulate the verdict logic here
    # For now, we'll flag cases where ADX < 20 but other indicators are strong
    patterns = data.get('patterns', {})
    trend_template = patterns.get('trend_template', {}) if patterns else {}
    criteria_passed = trend_template.get('criteria_met', 0)

    # Strong technical = 7-8/8 Trend Template
    is_strong_technical = criteria_passed >= 7

    if adx_value < 20 and is_strong_technical:
        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='ADX_VERDICT_MISMATCH',
            severity='WARNING',
            description=f'ADX {adx_value} < 20 (no trend) but Trend Template {criteria_passed}/8 is strong',
            expected='HOLD verdict due to no trend',
            actual=f'ADX={adx_value}, TT={criteria_passed}/8',
            data={'adx': adx_value, 'trend_template': criteria_passed}
        ))

    return issues


def check_adx_entry_strategy_coherence(data: dict) -> List[CoherenceIssue]:
    """
    Check: ADX < 25 should NOT suggest Momentum entry

    Logic: Momentum entries need confirmed trend (ADX >= 25)
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    adx_data = meta.get('adx', {})

    if not adx_data:
        return issues

    adx_value = adx_data.get('adx')
    if adx_value is None:
        return issues

    # Check if momentum would be incorrectly suggested
    if adx_value < 25:
        # ADX < 25 means momentum should NOT be viable
        # This is an info item - we'll check the frontend logic separately
        if adx_value < 20:
            expected_entry = 'Wait for trend development'
        else:
            expected_entry = 'Pullback preferred'

        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='ADX_ENTRY_CHECK',
            severity='INFO',
            description=f'ADX {adx_value} - verify entry strategy is correct',
            expected=expected_entry,
            actual=f'ADX={adx_value}',
            data={'adx': adx_value}
        ))

    return issues


def check_obv_price_coherence(data: dict) -> List[CoherenceIssue]:
    """
    Check: OBV trend should generally align with price trend (or flag divergence)

    Logic: OBV rising + Price rising = confirmation
           OBV rising + Price flat = bullish divergence (accumulation)
           OBV falling + Price rising = bearish divergence (distribution warning)
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    obv_data = meta.get('obv', {})

    if not obv_data:
        return issues

    obv_trend = obv_data.get('trend')
    divergence = obv_data.get('divergence')
    obv_change_pct = obv_data.get('obv_change_pct', 0)

    # Check for bearish divergence - this is a warning sign
    if divergence == 'bearish':
        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='OBV_BEARISH_DIVERGENCE',
            severity='WARNING',
            description='Bearish OBV divergence - price rising but volume distribution detected',
            expected='Caution in trade recommendation',
            actual=f'OBV trend: {obv_trend}, change: {obv_change_pct}%',
            data={'obv_trend': obv_trend, 'divergence': divergence, 'change': obv_change_pct}
        ))
    elif divergence == 'bullish':
        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='OBV_BULLISH_DIVERGENCE',
            severity='INFO',
            description='Bullish OBV divergence - accumulation detected',
            expected='Positive signal for entry',
            actual=f'OBV trend: {obv_trend}, change: {obv_change_pct}%',
            data={'obv_trend': obv_trend, 'divergence': divergence, 'change': obv_change_pct}
        ))

    return issues


def check_rr_sanity(data: dict) -> List[CoherenceIssue]:
    """
    Check: Risk/Reward ratio should be >= 1.0 for any suggested trade

    Logic: Never suggest a trade where risk > reward
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})

    if not sr:
        return issues

    risk_reward = sr.get('riskReward')

    if risk_reward is not None and risk_reward < 1.0:
        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='BAD_RISK_REWARD',
            severity='CRITICAL',
            description=f'Risk/Reward ratio {risk_reward} is below 1.0',
            expected='R:R >= 1.0 for any trade suggestion',
            actual=f'R:R = {risk_reward}',
            data={'risk_reward': risk_reward,
                  'entry': sr.get('suggestedEntry'),
                  'stop': sr.get('suggestedStop'),
                  'target': sr.get('suggestedTarget')}
        ))

    return issues


def check_volume_obv_coherence(data: dict) -> List[CoherenceIssue]:
    """
    Check: High RVOL should align with OBV trend confirmation

    Logic: RVOL > 2.0 with OBV falling is suspicious
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    obv_data = meta.get('obv', {})
    rvol = meta.get('rvol')

    if not obv_data or rvol is None:
        return issues

    obv_trend = obv_data.get('trend')

    # High volume but OBV falling = distribution
    if rvol >= 2.0 and obv_trend == 'falling':
        issues.append(CoherenceIssue(
            ticker=ticker,
            issue_type='HIGH_VOLUME_DISTRIBUTION',
            severity='WARNING',
            description=f'High RVOL {rvol}x but OBV falling - possible distribution',
            expected='High volume should confirm accumulation',
            actual=f'RVOL={rvol}x, OBV trend={obv_trend}',
            data={'rvol': rvol, 'obv_trend': obv_trend}
        ))

    return issues


def check_trend_template_adx_coherence(data: dict) -> List[CoherenceIssue]:
    """
    Check: Trend Template 8/8 with ADX < 15 is a paradox

    Logic: Perfect Stage 2 uptrend should have some trend strength
           Exception: After explosive moves, ADX can lag
    """
    issues = []
    ticker = data['ticker']
    sr = data.get('sr', {})
    meta = sr.get('meta', {}) if sr else {}
    adx_data = meta.get('adx', {})
    patterns = data.get('patterns', {})
    trend_template = patterns.get('trend_template', {}) if patterns else {}

    if not adx_data or not trend_template:
        return issues

    adx_value = adx_data.get('adx')
    criteria_passed = trend_template.get('criteria_met', 0)

    if adx_value is not None and criteria_passed == 8 and adx_value < 15:
        # Check if stock had a big recent move (52w return)
        stock = data.get('stock', {})
        price_52w_ago = stock.get('price52wAgo')
        current_price = stock.get('currentPrice')

        if price_52w_ago and current_price:
            return_52w = ((current_price - price_52w_ago) / price_52w_ago) * 100

            if return_52w > 100:
                # Explosive move explains the paradox
                issues.append(CoherenceIssue(
                    ticker=ticker,
                    issue_type='TT_ADX_PARADOX_EXPLAINED',
                    severity='INFO',
                    description=f'TT 8/8 with ADX {adx_value} - explained by {return_52w:.0f}% 52w gain (ADX lag)',
                    expected='ADX normally aligns with strong Trend Template',
                    actual=f'ADX={adx_value}, TT=8/8, 52w return={return_52w:.0f}%',
                    data={'adx': adx_value, 'trend_template': criteria_passed, 'return_52w': return_52w}
                ))
            else:
                # Genuine paradox
                issues.append(CoherenceIssue(
                    ticker=ticker,
                    issue_type='TT_ADX_PARADOX',
                    severity='WARNING',
                    description=f'Trend Template 8/8 but ADX only {adx_value} - conflicting signals',
                    expected='Strong Trend Template should have ADX > 20',
                    actual=f'ADX={adx_value}, TT={criteria_passed}/8',
                    data={'adx': adx_value, 'trend_template': criteria_passed}
                ))

    return issues


def check_all_coherence(data: dict) -> List[CoherenceIssue]:
    """Run all coherence checks on a ticker's data"""
    all_issues = []

    all_issues.extend(check_adx_verdict_coherence(data))
    all_issues.extend(check_adx_entry_strategy_coherence(data))
    all_issues.extend(check_obv_price_coherence(data))
    all_issues.extend(check_rr_sanity(data))
    all_issues.extend(check_volume_obv_coherence(data))
    all_issues.extend(check_trend_template_adx_coherence(data))

    return all_issues


def run_coherence_tests(tickers: List[str] = None) -> dict:
    """Run coherence tests on all tickers and return report"""
    if tickers is None:
        tickers = TEST_TICKERS

    print(f"\n{'='*60}")
    print(f"INDICATOR COHERENCE TEST SUITE")
    print(f"Testing {len(tickers)} tickers")
    print(f"{'='*60}\n")

    results = {
        'timestamp': datetime.now().isoformat(),
        'tickers_tested': len(tickers),
        'issues': [],
        'summary': {
            'critical': 0,
            'warning': 0,
            'info': 0
        },
        'ticker_data': {}
    }

    for i, ticker in enumerate(tickers):
        print(f"[{i+1}/{len(tickers)}] Testing {ticker}...", end=' ')

        data = fetch_analysis(ticker)

        if not data.get('success'):
            print(f"FAILED: {data.get('error', 'Unknown error')}")
            continue

        issues = check_all_coherence(data)

        # Store key data for analysis
        sr = data.get('sr', {})
        meta = sr.get('meta', {}) if sr else {}
        patterns = data.get('patterns', {})

        results['ticker_data'][ticker] = {
            'adx': meta.get('adx', {}).get('adx'),
            'obv_trend': meta.get('obv', {}).get('trend'),
            'obv_divergence': meta.get('obv', {}).get('divergence'),
            'rvol': meta.get('rvol'),
            'rsi_daily': meta.get('rsi_daily'),
            'rsi_4h': meta.get('rsi_4h', {}).get('rsi_4h') if meta.get('rsi_4h') else None,
            'trend_template': patterns.get('trend_template', {}).get('criteria_met') if patterns else None,
            'risk_reward': sr.get('riskReward') if sr else None,
            'issues_count': len(issues)
        }

        for issue in issues:
            results['issues'].append({
                'ticker': issue.ticker,
                'type': issue.issue_type,
                'severity': issue.severity,
                'description': issue.description,
                'expected': issue.expected,
                'actual': issue.actual,
                'data': issue.data
            })
            results['summary'][issue.severity.lower()] += 1

        status = '✓' if len(issues) == 0 else f'⚠ {len(issues)} issues'
        print(status)

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Tickers tested: {results['tickers_tested']}")
    print(f"Critical issues: {results['summary']['critical']}")
    print(f"Warnings: {results['summary']['warning']}")
    print(f"Info: {results['summary']['info']}")

    # Group issues by type
    issues_by_type = {}
    for issue in results['issues']:
        issue_type = issue['type']
        if issue_type not in issues_by_type:
            issues_by_type[issue_type] = []
        issues_by_type[issue_type].append(issue)

    print(f"\nIssues by Type:")
    for issue_type, issues in sorted(issues_by_type.items()):
        severities = [i['severity'] for i in issues]
        critical = severities.count('CRITICAL')
        warning = severities.count('WARNING')
        info = severities.count('INFO')
        print(f"  {issue_type}: {len(issues)} ({critical}C/{warning}W/{info}I)")

    # Show critical issues
    critical_issues = [i for i in results['issues'] if i['severity'] == 'CRITICAL']
    if critical_issues:
        print(f"\n{'='*60}")
        print("CRITICAL ISSUES (Must Fix)")
        print(f"{'='*60}")
        for issue in critical_issues:
            print(f"\n{issue['ticker']}: {issue['type']}")
            print(f"  Description: {issue['description']}")
            print(f"  Expected: {issue['expected']}")
            print(f"  Actual: {issue['actual']}")

    # Show warnings
    warning_issues = [i for i in results['issues'] if i['severity'] == 'WARNING']
    if warning_issues:
        print(f"\n{'='*60}")
        print("WARNINGS (Should Review)")
        print(f"{'='*60}")
        for issue in warning_issues:
            print(f"\n{issue['ticker']}: {issue['type']}")
            print(f"  {issue['description']}")

    # Save results to file
    output_file = f"coherence_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {output_file}")

    return results


def analyze_and_recommend(results: dict) -> dict:
    """Analyze test results and provide fix recommendations"""
    recommendations = []

    # Analyze issue patterns
    issues_by_type = {}
    for issue in results['issues']:
        issue_type = issue['type']
        if issue_type not in issues_by_type:
            issues_by_type[issue_type] = []
        issues_by_type[issue_type].append(issue)

    # Generate recommendations
    if 'BAD_RISK_REWARD' in issues_by_type:
        recommendations.append({
            'priority': 'CRITICAL',
            'issue': 'BAD_RISK_REWARD',
            'count': len(issues_by_type['BAD_RISK_REWARD']),
            'fix': 'Add R:R filter in frontend - never display entry strategy with R:R < 1.0',
            'file': 'frontend/src/App.jsx',
            'location': 'Entry Strategy cards section'
        })

    if 'ADX_VERDICT_MISMATCH' in issues_by_type:
        recommendations.append({
            'priority': 'HIGH',
            'issue': 'ADX_VERDICT_MISMATCH',
            'count': len(issues_by_type['ADX_VERDICT_MISMATCH']),
            'fix': 'Verify ADX < 20 properly downgrades to HOLD in categoricalAssessment.js',
            'file': 'frontend/src/utils/categoricalAssessment.js',
            'location': 'determineVerdict function'
        })

    if 'HIGH_VOLUME_DISTRIBUTION' in issues_by_type:
        recommendations.append({
            'priority': 'MEDIUM',
            'issue': 'HIGH_VOLUME_DISTRIBUTION',
            'count': len(issues_by_type['HIGH_VOLUME_DISTRIBUTION']),
            'fix': 'Add warning when RVOL high but OBV falling - distribution signal',
            'file': 'frontend/src/App.jsx',
            'location': 'OBV badge section'
        })

    print(f"\n{'='*60}")
    print("FIX RECOMMENDATIONS")
    print(f"{'='*60}")

    for rec in recommendations:
        print(f"\n[{rec['priority']}] {rec['issue']} ({rec['count']} occurrences)")
        print(f"  Fix: {rec['fix']}")
        print(f"  File: {rec['file']}")
        print(f"  Location: {rec['location']}")

    return recommendations


if __name__ == '__main__':
    # Run the tests
    results = run_coherence_tests()

    # Analyze and recommend fixes
    recommendations = analyze_and_recommend(results)

    print(f"\n{'='*60}")
    print("TEST COMPLETE")
    print(f"{'='*60}")
