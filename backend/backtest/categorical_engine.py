"""
Categorical Assessment Engine — Python Port for v4.16 Holistic Backtest

Direct port of frontend/src/utils/categoricalAssessment.js verdict logic.
Pure functions, no API calls — deterministic with fixed thresholds.

Source of truth: categoricalAssessment.js (908 lines, Day 53 v4.13)

Categories:
  - Technical: Strong / Decent / Weak
  - Fundamental: Strong / Decent / Weak / Unknown
  - Sentiment: NOT USED in backtest (F&G is lagging, redundant with VIX)
  - Risk/Macro: Favorable / Neutral / Unfavorable

Verdict: BUY / HOLD / AVOID
"""


def assess_technical(trend_template_score, rsi, rs_52w=1.0, adx=None, total_criteria=8):
    """
    Assess technical strength.

    Strong: TT >= 7/8 AND RSI 50-70 AND RS >= 1.0
    Decent: TT >= 5/8 AND RSI 40-80
    Weak:   below thresholds

    Source: categoricalAssessment.js lines 229-328

    Args:
        trend_template_score: Number of Minervini criteria passed (0-8)
        rsi: RSI(14) value
        rs_52w: 52-week relative strength vs SPY (default 1.0)
        adx: ADX value (stored in data, not used for assessment)
        total_criteria: Total criteria count (default 8)

    Returns:
        dict with assessment, reasons, data
    """
    reasons = []
    data = {
        'trend_template_score': f"{trend_template_score}/{total_criteria}",
        'rsi': rsi,
        'rs_52w': rs_52w,
        'adx': adx,
    }

    pass_count = trend_template_score or 0
    rsi_val = rsi if rsi is not None else 50

    # Strong: 7-8/8 trend template, RSI 50-70, good RS
    if pass_count >= 7 and 50 <= rsi_val <= 70 and rs_52w >= 1.0:
        assessment = 'Strong'
        reasons.append(f"TT {pass_count}/8, RSI {rsi_val:.1f} (50-70), RS {rs_52w:.2f}")
    # Decent: 5-6/8 trend template, RSI 40-80
    elif pass_count >= 5 and 40 <= rsi_val <= 80:
        assessment = 'Decent'
        reasons.append(f"TT {pass_count}/8 (needs 7+ for Strong), RSI {rsi_val:.1f}")
    # Weak
    else:
        assessment = 'Weak'
        if pass_count < 5:
            reasons.append(f"TT {pass_count}/8 (needs 5+ for Decent)")
        if rsi_val < 30:
            reasons.append(f"RSI {rsi_val:.1f} deeply oversold")
        elif rsi_val < 40:
            reasons.append(f"RSI {rsi_val:.1f} oversold")
        elif rsi_val > 80:
            reasons.append(f"RSI {rsi_val:.1f} overbought")
        if rs_52w < 0.8:
            reasons.append(f"Weak RS {rs_52w:.2f} vs SPY")

    if not reasons:
        reasons.append('Mixed technical signals')

    return {'assessment': assessment, 'reasons': reasons, 'data': data}


def assess_fundamental(roe=None, revenue_growth=None, debt_equity=None, eps_growth=None):
    """
    Assess fundamental strength.

    Strong: 2+ strong metrics, 0 weak
    Decent: default (mixed)
    Weak:   2+ weak metrics
    Unknown: no metrics available

    Thresholds (from JS lines 383-419):
      ROE: >15% Strong, 8-15% Decent, <8% Weak
      Revenue Growth: >10% Strong, 0-10% Decent, <0% Weak
      D/E: <1.0 Strong, 1.0-2.0 Decent, >2.0 Weak

    Args:
        roe: Return on equity (percentage, e.g. 15.0 = 15%)
        revenue_growth: YoY revenue growth (percentage)
        debt_equity: Debt to equity ratio
        eps_growth: YoY EPS growth (stored in data, not directly scored in JS)

    Returns:
        dict with assessment, reasons, data
    """
    reasons = []
    data = {
        'roe': roe,
        'revenue_growth': revenue_growth,
        'debt_equity': debt_equity,
        'eps_growth': eps_growth,
    }

    strong_count = 0
    weak_count = 0
    evaluated = 0

    # ROE assessment
    if roe is not None:
        evaluated += 1
        if roe > 15:
            strong_count += 1
            reasons.append(f"ROE {roe:.1f}% (Strong > 15%)")
        elif roe >= 8:
            reasons.append(f"ROE {roe:.1f}% (Decent 8-15%)")
        else:
            weak_count += 1
            reasons.append(f"ROE {roe:.1f}% (Weak < 8%)")

    # Revenue Growth assessment
    if revenue_growth is not None:
        evaluated += 1
        if revenue_growth > 10:
            strong_count += 1
            reasons.append(f"Revenue Growth {revenue_growth:.1f}% (Strong > 10%)")
        elif revenue_growth >= 0:
            reasons.append(f"Revenue Growth {revenue_growth:.1f}% (Decent 0-10%)")
        else:
            weak_count += 1
            reasons.append(f"Revenue Growth {revenue_growth:.1f}% (Weak < 0%)")

    # Debt/Equity assessment
    if debt_equity is not None:
        evaluated += 1
        if 0 <= debt_equity < 1.0:
            strong_count += 1
            reasons.append(f"D/E {debt_equity:.2f} (Strong < 1.0)")
        elif debt_equity <= 2.0:
            reasons.append(f"D/E {debt_equity:.2f} (Decent 1.0-2.0)")
        else:
            weak_count += 1
            reasons.append(f"D/E {debt_equity:.2f} (Weak > 2.0)")

    # No metrics evaluated → Unknown
    if evaluated == 0:
        return {
            'assessment': 'Unknown',
            'reasons': ['No fundamental metrics available'],
            'data': data
        }

    # Determine overall
    if strong_count >= 2 and weak_count == 0:
        assessment = 'Strong'
    elif weak_count >= 2:
        assessment = 'Weak'
    else:
        assessment = 'Decent'

    data['strong_count'] = strong_count
    data['weak_count'] = weak_count

    return {'assessment': assessment, 'reasons': reasons, 'data': data}


def assess_risk_macro(vix, spy_above_200sma):
    """
    Assess risk/macro environment.

    Favorable:   VIX < 20 AND SPY > 200 SMA
    Neutral:     VIX 20-30 AND SPY > 200 SMA
    Unfavorable: VIX > 30 OR SPY < 200 SMA

    Source: categoricalAssessment.js lines 558-619

    Args:
        vix: VIX value (float or None)
        spy_above_200sma: bool — is SPY above its 200-day SMA?

    Returns:
        dict with assessment, reasons, data
    """
    reasons = []
    data = {
        'vix': vix,
        'spy_above_200sma': spy_above_200sma,
    }

    # VIX unavailable — assess on SPY alone
    if vix is None:
        if not spy_above_200sma:
            assessment = 'Unfavorable'
            reasons.append('VIX unavailable, SPY below 200 SMA (Bear regime)')
        else:
            assessment = 'Neutral'
            reasons.append('VIX unavailable, SPY above 200 SMA')
    # Unfavorable: high VIX or bear regime
    elif vix > 30 or not spy_above_200sma:
        assessment = 'Unfavorable'
        if vix > 30:
            reasons.append(f"VIX {vix:.1f} > 30 (extreme volatility)")
        if not spy_above_200sma:
            reasons.append('SPY below 200 SMA (Bear regime)')
    # Favorable: low VIX + bull regime
    elif vix < 20 and spy_above_200sma:
        assessment = 'Favorable'
        reasons.append(f"VIX {vix:.1f} < 20, SPY above 200 SMA")
    # Neutral: elevated VIX but still bull
    else:
        assessment = 'Neutral'
        reasons.append(f"VIX {vix:.1f} (20-30), SPY above 200 SMA")

    return {'assessment': assessment, 'reasons': reasons, 'data': data}


def get_signal_weight(holding_period):
    """
    Signal weights by holding period.

    Source: categoricalAssessment.js lines 632-642

    Returns:
        dict with technical and fundamental weights
    """
    if holding_period == 'quick':
        return {'technical': 0.7, 'fundamental': 0.3}
    elif holding_period == 'position':
        return {'technical': 0.3, 'fundamental': 0.7}
    else:  # standard
        return {'technical': 0.5, 'fundamental': 0.5}


def determine_verdict(technical, fundamental, risk_macro, adx=None,
                      holding_period='standard', sentiment='Neutral'):
    """
    Determine overall BUY / HOLD / AVOID verdict.

    Priority rules (from JS lines 681-844):
      1. Weak Technical = AVOID (non-negotiable)
      2. Unfavorable Risk = HOLD (structure override)
      3. Weak Fund + position = AVOID (fund 70% weight)
      4. ADX < 20 = HOLD (even with strong signals)
      5. Strong Tech + Strong Fund = BUY
      6. 2+ Strong + Favorable/Neutral = BUY
      7. Quick: Strong Tech + Weak Fund = BUY (tech 70%)
      8. Position: Decent Tech + Strong Fund = BUY (fund 70%)

    Args:
        technical: 'Strong', 'Decent', or 'Weak'
        fundamental: 'Strong', 'Decent', 'Weak', or 'Unknown'
        risk_macro: 'Favorable', 'Neutral', or 'Unfavorable'
        adx: ADX value (float or None)
        holding_period: 'quick', 'standard', or 'position'
        sentiment: 'Strong', 'Neutral', or 'Weak' (default Neutral for backtest)

    Returns:
        dict with verdict, reason, entry_preference, signal_weights, holding_period
    """
    signal_weights = get_signal_weight(holding_period)

    # Count strong assessments (tech, fund, sentiment — same as JS)
    assessments = [technical, fundamental, sentiment]
    strong_count = sum(1 for a in assessments if a == 'Strong')

    # ADX-based entry preference
    entry_preference = 'Either'
    if adx is not None:
        if adx >= 25:
            entry_preference = f"Momentum (ADX {adx:.0f} - strong trend)"
        elif adx >= 20:
            entry_preference = f"Pullback (ADX {adx:.0f} - moderate trend)"
        else:
            entry_preference = f"Wait (ADX {adx:.0f} - no trend)"

    def result(verdict, reason):
        return {
            'verdict': verdict,
            'reason': reason,
            'entry_preference': entry_preference,
            'signal_weights': signal_weights,
            'holding_period': holding_period,
            'adx': adx,
        }

    # --- AVOID conditions (highest priority) ---

    # 1. Weak Technical = AVOID (non-negotiable)
    if technical == 'Weak':
        return result('AVOID', 'Weak technical setup')

    # 2. Unfavorable Risk = HOLD (structure override)
    if risk_macro == 'Unfavorable':
        return result('HOLD', 'Unfavorable market conditions (regime caution)')

    # 3. Weak Fundamental handling — depends on holding period
    if fundamental == 'Weak':
        if holding_period == 'position':
            return result('AVOID', 'Weak fundamentals — critical for position trades (70% weight)')
        elif holding_period == 'quick' and technical == 'Strong':
            pass  # Let it fall through — tech dominates at 70%
        elif strong_count == 0:
            return result('AVOID', 'Weak fundamentals with no offsetting strengths')

    # 4. ADX < 20 suggests caution
    if adx is not None and adx < 20:
        if strong_count >= 2:
            return result('HOLD', f"{strong_count} strong but ADX {adx:.0f} < 20 (no trend)")

    # --- BUY conditions ---

    # 5. Strong Tech + Strong Fund = BUY
    if technical == 'Strong' and fundamental == 'Strong':
        reason = 'Strong Technical + Strong Fundamental'
        if adx is not None and adx >= 25:
            reason += f" + ADX {adx:.0f} confirms trend"
        return result('BUY', reason)

    # 6. 2+ Strong with Favorable/Neutral risk = BUY
    if strong_count >= 2 and risk_macro in ('Favorable', 'Neutral'):
        return result('BUY', f"{strong_count} strong categories with {risk_macro.lower()} conditions")

    # 7. Quick: Strong Tech + Weak Fund = BUY (tech 70%)
    if (holding_period == 'quick' and technical == 'Strong' and fundamental == 'Weak'
            and risk_macro in ('Favorable', 'Neutral')):
        return result('BUY', 'Strong technicals (70% for quick) offset weak fundamentals')

    # 8. Strong Tech + Decent Fund + Favorable = BUY
    if technical == 'Strong' and fundamental == 'Decent':
        if risk_macro == 'Favorable':
            return result('BUY', 'Strong technicals with favorable macro')
        if holding_period == 'quick' and risk_macro == 'Neutral':
            return result('BUY', 'Strong technicals (70% for quick) with neutral conditions')

    # 9. Position: Decent Tech + Strong Fund = BUY (fund 70%)
    if (holding_period == 'position' and technical == 'Decent' and fundamental == 'Strong'
            and risk_macro in ('Favorable', 'Neutral')):
        return result('BUY', 'Strong fundamentals (70% for position) with decent technicals')

    # --- HOLD conditions ---

    if strong_count >= 1:
        return result('HOLD', 'Mixed signals — wait for better setup')

    if technical == 'Decent' and risk_macro == 'Favorable':
        return result('HOLD', 'Decent setup — consider with proper sizing')

    # Default: AVOID
    return result('AVOID', 'Insufficient strength across categories')


def run_assessment(trend_template_score, rsi, rs_52w, adx,
                   vix, spy_above_200sma,
                   roe=None, revenue_growth=None, debt_equity=None, eps_growth=None,
                   holding_period='standard'):
    """
    Convenience wrapper — runs all assessments and returns complete result.

    Sentiment is always 'Neutral' for backtesting (F&G not used).

    Args:
        trend_template_score: Minervini criteria passed (0-8)
        rsi: RSI(14) value
        rs_52w: 52-week relative strength vs SPY
        adx: ADX value
        vix: VIX value
        spy_above_200sma: bool
        roe: ROE percentage (optional)
        revenue_growth: YoY revenue growth percentage (optional)
        debt_equity: D/E ratio (optional)
        eps_growth: YoY EPS growth percentage (optional)
        holding_period: 'quick', 'standard', or 'position'

    Returns:
        dict with technical, fundamental, risk_macro, verdict, holding_period
    """
    technical = assess_technical(trend_template_score, rsi, rs_52w, adx)
    fundamental = assess_fundamental(roe, revenue_growth, debt_equity, eps_growth)
    risk_macro = assess_risk_macro(vix, spy_above_200sma)

    verdict = determine_verdict(
        technical=technical['assessment'],
        fundamental=fundamental['assessment'],
        risk_macro=risk_macro['assessment'],
        adx=adx,
        holding_period=holding_period,
        sentiment='Neutral',  # F&G not used in backtest
    )

    return {
        'technical': technical,
        'fundamental': fundamental,
        'risk_macro': risk_macro,
        'verdict': verdict,
        'holding_period': holding_period,
    }


# --- Verification vectors (parity with JavaScript) ---

def _verify_parity():
    """
    5 test vectors to confirm parity with JS categoricalAssessment.js.
    Run: python categorical_engine.py
    """
    tests = [
        {
            'name': '1. Strong tech + Favorable risk + ADX 28 → BUY',
            'args': dict(trend_template_score=8, rsi=60, rs_52w=1.2, adx=28,
                         vix=15, spy_above_200sma=True,
                         roe=20, revenue_growth=15, debt_equity=0.5),
            'expected_verdict': 'BUY',
        },
        {
            'name': '2. Weak tech (TT=3, RS=0.7) → AVOID',
            'args': dict(trend_template_score=3, rsi=45, rs_52w=0.7, adx=22,
                         vix=18, spy_above_200sma=True,
                         roe=20, revenue_growth=15, debt_equity=0.5),
            'expected_verdict': 'AVOID',
        },
        {
            'name': '3. Strong tech + Unfavorable risk (VIX=35) → HOLD',
            'args': dict(trend_template_score=8, rsi=55, rs_52w=1.1, adx=30,
                         vix=35, spy_above_200sma=True,
                         roe=20, revenue_growth=15, debt_equity=0.5),
            'expected_verdict': 'HOLD',
        },
        {
            'name': '4. Strong tech + ADX 18 → HOLD (no trend)',
            'args': dict(trend_template_score=8, rsi=60, rs_52w=1.2, adx=18,
                         vix=15, spy_above_200sma=True,
                         roe=20, revenue_growth=15, debt_equity=0.5),
            'expected_verdict': 'HOLD',
        },
        {
            'name': '5. Decent tech + Favorable risk → HOLD',
            'args': dict(trend_template_score=6, rsi=55, rs_52w=1.0, adx=25,
                         vix=15, spy_above_200sma=True,
                         roe=10, revenue_growth=5, debt_equity=1.5),
            'expected_verdict': 'HOLD',
        },
    ]

    print("Categorical Engine — Parity Verification")
    print("=" * 60)

    all_passed = True
    for test in tests:
        result = run_assessment(**test['args'])
        actual = result['verdict']['verdict']
        expected = test['expected_verdict']
        passed = actual == expected

        status = 'PASS' if passed else 'FAIL'
        print(f"  [{status}] {test['name']}")
        if not passed:
            all_passed = False
            print(f"         Expected: {expected}, Got: {actual}")
            print(f"         Tech: {result['technical']['assessment']}, "
                  f"Fund: {result['fundamental']['assessment']}, "
                  f"Risk: {result['risk_macro']['assessment']}")
            print(f"         Reason: {result['verdict']['reason']}")

    print()
    if all_passed:
        print("All 5 parity tests PASSED")
    else:
        print("SOME TESTS FAILED — check logic")

    return all_passed


if __name__ == '__main__':
    _verify_parity()
