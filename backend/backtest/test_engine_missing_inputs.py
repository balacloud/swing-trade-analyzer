"""
Day 131: missing RSI and missing SPY in the verdict engine (JS + Python copies).

Rules (docs/claude/design/ENGINE_MISSING_INPUTS_PLAN_DAY131.md):
  - Missing RSI (None / NaN) is never a fake 50: it cannot be Strong, may be
    Decent when the trend checks are 5+, else Weak. A real RSI of 0 is kept.
  - Missing SPY stays Unfavorable (no BUY while the market trend is unknown)
    but is described as "unavailable", not as "below the 200-day".

Run: python backend/backtest/test_engine_missing_inputs.py
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from categorical_engine import assess_technical, assess_risk_macro  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
fails = []


def check(name, cond, extra=''):
    if not cond:
        fails.append(name)
    print(('PASS ' if cond else 'FAIL ') + name + (f'  {extra}' if (extra and not cond) else ''))


# ---- Python: RSI
nan = float('nan')
for label, rsi in (('None', None), ('NaN', nan)):
    r = assess_technical(8, rsi, rs_52w=1.2)
    check(f'py rsi {label}, TT 8, RS ok -> Decent, not Strong', r['assessment'] == 'Decent', r['assessment'])
    check(f'py rsi {label} says unavailable', any('RSI unavailable' in x for x in r['reasons']), r['reasons'])
    check(f'py rsi {label} data flag', r['data']['rsi_available'] is False)
    r = assess_technical(4, rsi, rs_52w=1.2)
    check(f'py rsi {label}, TT 4 -> Weak (no crash)', r['assessment'] == 'Weak', r['assessment'])
r = assess_technical(8, 0, rs_52w=1.2)
check('py rsi 0 is a real value -> Weak (not 50)', r['assessment'] == 'Weak' and r['data']['rsi_available'] is True, r)
r = assess_technical(8, 60, rs_52w=1.2)
check('py rsi 60 -> Strong', r['assessment'] == 'Strong', r['assessment'])

# ---- Python: SPY
for vix in (15, 25, 35, None):
    r = assess_risk_macro(vix, None)
    check(f'py spy None, vix {vix} -> Unfavorable', r['assessment'] == 'Unfavorable', r['assessment'])
    check(f'py spy None, vix {vix} never says "below 200 SMA"', not any('below 200' in x for x in r['reasons']), r['reasons'])
    check(f'py spy None, vix {vix} says unavailable', any('unavailable' in x for x in r['reasons']), r['reasons'])
r = assess_risk_macro(15, False)
check('py spy False still says below 200 SMA', any('below 200 SMA' in x for x in r['reasons']))
r = assess_risk_macro(15, True)
check('py spy True, vix 15 -> Favorable', r['assessment'] == 'Favorable')

# ---- JS (same rules)
p = subprocess.run(['node', os.path.join(REPO, 'frontend', 'scripts', 'missing_inputs_check.mjs')],
                   capture_output=True, text=True, timeout=60)
if p.returncode != 0:
    print('FAIL node run', p.stderr[-500:])
    sys.exit(1)
js = json.loads(p.stdout)
for k in ('rsiNull', 'rsiUndefined', 'rsiNaN'):
    check(f'js {k} -> Decent, rsi null, unavailable', js[k]['a'] == 'Decent' and js[k]['rsi'] is None and js[k]['avail'] is False, js[k])
    check(f'js {k} says unavailable', 'RSI unavailable' in js[k]['reasons'], js[k])
check('js rsi 0 is real -> Weak', js['rsiZero']['a'] == 'Weak' and js['rsiZero']['rsi'] == 0 and js['rsiZero']['avail'] is True, js['rsiZero'])
check('js rsi 0 does not say oversold-crash', 'deeply oversold' in js['rsiZero']['reasons'], js['rsiZero'])
check('js rsi 60 -> Strong', js['rsi60']['a'] == 'Strong', js['rsi60'])
check('js rsi falls back to indicators.rsi', js['rsiFallback']['a'] == 'Strong' and js['rsiFallback']['rsi'] == 60, js['rsiFallback'])
for k in ('spyNull_vix15', 'spyMissing_vix35', 'spyNull_vixNull'):
    v = js[k]
    check(f'js {k} -> Unfavorable, spyAbove null, unavailable', v['a'] == 'Unfavorable' and v['spyAbove'] is None and v['spyAvail'] is False, v)
    check(f'js {k} never says below 200 SMA', 'below 200' not in v['reasons'] and 'unavailable' in v['reasons'], v)
check('js spy true vix 15 -> Favorable', js['spyTrue_vix15']['a'] == 'Favorable' and js['spyTrue_vix15']['spyAbove'] is True, js['spyTrue_vix15'])
check('js spy false says below 200 SMA', js['spyFalse_vix15']['a'] == 'Unfavorable' and 'below 200 SMA' in js['spyFalse_vix15']['reasons'], js['spyFalse_vix15'])

print(f"\n{'FAILED: ' + str(len(fails)) if fails else 'ALL PASSED'}")
sys.exit(1 if fails else 0)
