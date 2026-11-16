"""Unit tests for rrg.py (pure, no network). Run: cd backend && venv/bin/python test_rrg.py"""
import sys
import numpy as np
import pandas as pd
from rrg import compute_rrg, quadrant_for, weekly_rs

fails = []
def check(name, cond, detail=''):
    print(('PASS ' if cond else 'FAIL ') + name + (f'  {detail}' if detail and not cond else ''))
    if not cond: fails.append(name)

def series(vals, start='2024-01-01'):
    return pd.Series(vals, index=pd.bdate_range(start, periods=len(vals)))

N = 400
spy = series(np.full(N, 100.0))

# 1. fund rising steadily vs SPY -> Leading (ratio >= 100, momentum >= 0) or at least ratio above 100
up = series(100 * np.exp(np.linspace(0, 0.5, N)))
r = compute_rrg(up, spy)
check('steady outperformer: ratio above 100', r['rs_ratio'] > 100, r)
check('steady outperformer: not thin', r['thin'] is False)
check('tail has 5 points', len(r['tail']) == 5)
check('every tail point carries its corner', all(p['quadrant'] == quadrant_for(p['rs_ratio'], p['rs_momentum']) for p in r['tail']))
check('last tail point matches the headline', r['tail'][-1]['quadrant'] == r['quadrant'])
check('quadrant matches numbers', r['quadrant'] == quadrant_for(r['rs_ratio'], r['rs_momentum']))

# 2. fund falling steadily -> ratio below 100
dn = series(100 * np.exp(np.linspace(0, -0.5, N)))
r = compute_rrg(dn, spy)
check('steady underperformer: ratio below 100', r['rs_ratio'] < 100, r)

# 3. flat vs SPY -> exactly 100 / 0, no divide-by-zero
r = compute_rrg(series(np.full(N, 50.0)), spy)
check('flat fund: ratio 100, momentum 0', r['rs_ratio'] == 100 and r['rs_momentum'] == 0, r)

# 4. quadrant rule, all four corners + the exact cut
check('Leading', quadrant_for(101, 0.5) == 'Leading')
check('Weakening', quadrant_for(101, -0.5) == 'Weakening')
check('Lagging', quadrant_for(99, -0.5) == 'Lagging')
check('Improving', quadrant_for(99, 0.5) == 'Improving')
check('cut: 100 / 0 is Leading', quadrant_for(100, 0) == 'Leading')

# 5. a fund that was strong and is now fading = ratio above 100, momentum below 0 (Weakening)
x = np.concatenate([np.linspace(0, 0.4, 385), np.linspace(0.4, 0.385, 15)])  # 3-week fade
r = compute_rrg(series(100 * np.exp(x)), spy)
check('peak then fade: Weakening', r['quadrant'] == 'Weakening', r)

# 6. a fund that fell, then turns up = ratio below 100, momentum rising (Improving)
x = np.concatenate([np.linspace(0, -0.4, 385), np.linspace(-0.4, -0.385, 15)])  # 3-week bounce
r = compute_rrg(series(100 * np.exp(x)), spy)
check('bottom then bounce: Improving', r['quadrant'] == 'Improving', r)

# 7. thin history (young fund ~20 weeks) -> computed but flagged thin
short = series(100 * np.exp(np.linspace(0, 0.2, 100)))
r = compute_rrg(short, spy.iloc[-100:].set_axis(short.index))
check('20 weeks: computed and flagged thin', r['thin'] is True, r)

# 8. too little history -> ValueError, never a made-up number
try:
    compute_rrg(series(np.linspace(100, 110, 40)), series(np.full(40, 100.0)))
    check('8 weeks raises', False)
except ValueError:
    check('8 weeks raises', True)

# 9. no overlap with SPY -> ValueError
try:
    compute_rrg(series(np.linspace(100, 110, 200), '2020-01-01'), series(np.full(200, 100.0), '2024-01-01'))
    check('no common dates raises', False)
except ValueError:
    check('no common dates raises', True)

# 10. tz-aware fund index vs tz-naive SPY (Day 52 gotcha) works
tz = up.copy(); tz.index = tz.index.tz_localize('America/New_York')
r = compute_rrg(tz, spy)
check('tz-aware fund index ok', r['rs_ratio'] > 100)

# 11. NaN / zero SPY bars are dropped, not propagated
bad_spy = spy.copy(); bad_spy.iloc[50] = np.nan; bad_spy.iloc[60] = 0.0
r = compute_rrg(up, bad_spy)
check('NaN / zero SPY bars ignored', np.isfinite(r['rs_ratio']) and np.isfinite(r['rs_momentum']), r)

# 12. weekly bars: ~400 business days -> ~80 weekly bars
check('weekly resample', 75 <= len(weekly_rs(up, spy)) <= 85)

print('\n%d failed' % len(fails)); sys.exit(1 if fails else 0)
