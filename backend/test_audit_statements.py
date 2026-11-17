"""Self-tests for the Statement Audit (Day 126). Run: cd backend && venv/bin/python test_audit_statements.py
Proves the auditor itself: reference maths against hand values, the window dictionary (the "a month = 30 bars" bug must be rejected),
that a planted wrong number / wrong word / unclaimed number is caught, and the static S3 checks on the real source."""
import json, os, sys
import audit_ref as R
import audit_statements as A

passed = failed = 0
def ok(c, m):
    global passed, failed
    if c: passed += 1; print(f'ok {m}')
    else: failed += 1; print(f'FAIL {m}')

# reference maths: hand-computed values
ok(R.sma([1, 2, 3, 4, 5], 3) == 4 and R.sma([1, 2, 3, 4, 5], 3, 1) == 3 and R.sma([1, 2], 3) is None, 'SMA, with a look-back and too-short input')
ok(abs(R.ema([10, 10, 10, 10], 3) - 10) < 1e-12 and abs(R.ema([0, 12], 3) - 6) < 1e-12, 'EMA span 3: flat series and one step (k = 0.5)')
ok(R.wilder_rsi([float(i) for i in range(1, 40)]) == 100.0, 'RSI of a straight rise = 100')
ok(abs(R.wilder_rsi([1.0, 2.0] * 20) - 50) < 4, 'RSI of an up/down zig-zag is near 50')
flat = [10.0] * 60
ok(R.wilder_atr(flat, flat, flat) == 0 and R.wilder_adx(flat, flat, flat) in (0.0, None), 'ATR and ADX of a flat series are 0')
up_h = [i + 1.0 for i in range(80)]; up_l = [i - 1.0 for i in range(80)]; up_c = [float(i) for i in range(80)]
ok(R.wilder_adx(up_h, up_l, up_c) > 90, 'ADX of a clean straight trend is very high')
ok(R.obv_trend([1, 2, 3, 4] * 10, [100] * 40) == 'rising' and R.obv_trend([4, 3, 2, 1] * 10, [100] * 40) is not None, 'OBV trend: rising on rising closes')
ok(R.obv_trend([5.0] * 30, [100] * 30) == 'flat', 'OBV trend: flat when nothing moves')

# the window dictionary: the real bug and its neighbours
ok(not A.window_ok('from a month ago', 30), 'REGRESSION: "a month ago" with a 30-bar comparison is rejected')
ok(A.window_ok('from a month ago', 21) and A.window_ok('a month ago', 22), '"a month ago" with 21-22 bars is accepted')
ok(A.window_ok('over 30 trading days', 30) and not A.window_ok('over 30 trading days', 21), '"30 trading days" must be 30 bars back')
ok(A.window_ok('past year', 251, 252) and not A.window_ok('past year', 205, 206), '"past year": a 252-bar span fits, a 206-bar history (first bar stands in) does not')
ok(A.window_ok('1-year high', 251, 252), '"1-year high" over 252 bars fits')
ok(A.window_ok('13-week', 63), '"13-week" = 63 bars')
ok(not A.window_ok('some words with no window', 5), 'unknown wording is not silently accepted')

# a planted card: wrong number, wrong word, unclaimed number
bars = 300
c = [100.0 + i * 0.5 for i in range(bars)]
ph = [{'date': f'2026-{1 + i // 28:02d}-{1 + i % 28:02d}', 'open': x, 'high': x + 1, 'low': x - 1, 'close': x, 'volume': 1000000} for i, x in enumerate(c)]
def dump(text):
    return {'ticker': 'TST', 'payloads': {'stock': {'body': {'priceHistory': ph}}, 'sr': {'body': {'meta': {}}}, 'patterns': {'body': {}}, 'quote': {'body': {'available': False}}, 'spy': {'body': {'priceHistory': ph}}},
            'tr': {'text': text}, 'gauge': {}}
last = c[-1]; s200 = sum(c[-200:]) / 200
good = f'Is it in an uptrend? Above its 200-day average x ${last:.2f} vs ${s200:.2f} · +{(last / s200 - 1) * 100:.1f}%'
a = A.Audit(dump(good)).run()
ok(any(r.sid == 'T6' and r.verdict == 'PASS' for r in a.rows), 'a correct 200-day row passes')
bad = good.replace(f'${s200:.2f}', f'${s200 + 5:.2f}')
ok(any(r.sid == 'T6' and r.verdict == 'WRONG' for r in A.Audit(dump(bad)).run().rows), 'a wrong average is caught (WRONG)')
badw = good.replace('Above', 'Below')
ok(any(r.sid == 'T6w' and r.verdict == 'MISLEADING' for r in A.Audit(dump(badw)).run().rows), 'a wrong word (Below when it is above) is caught (MISLEADING)')
unc = A.Audit(dump(good + ' and a stray 12345 figure')).run()
ok(any(r.sid == 'U1' and '12345' in r.shown for r in unc.rows), 'an unclaimed number on the card is reported (UNVERIFIED)')
ok(not any(r.sid == 'U1' for r in A.Audit(dump(good)).run().rows), 'a fully claimed card has no unclaimed numbers')
month = f'The 200-day average is still rising x +1.5% over 21 trading days'
ok(any(r.sid == 'T8w' and r.verdict == 'MISLEADING' for r in A.Audit(dump(month)).run().rows), 'words say 21 trading days but the code uses 30: caught (MISLEADING)')

# static S3 on the real source files: must pass today
rows = A.static_s3()
ok(all(r.verdict == 'PASS' for r in rows if r.sid in ('S3-1', 'S3-2', 'S3-3', 'S3-4', 'S3-5', 'S3-6')), 'static S3: the UI words match the code windows in the real source')

print(f'\n{passed} passed, {failed} failed')
sys.exit(1 if failed else 0)
