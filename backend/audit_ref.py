"""Statement Audit reference maths (Day 126). Plan: docs/claude/design/STATEMENT_AUDIT_PLAN_DAY126.md.
Written from the textbook definitions, importing NO app indicator code. RSI/ATR/EMA follow the references in backtest/test_indicators.py
(that file runs its tests at import, so it cannot be imported; these are copies, cited here). ADX, OBV trend and returns are new.
All inputs are plain lists of floats (oldest first)."""
from typing import List, Optional


def sma(c: List[float], n: int, back: int = 0) -> Optional[float]:
    """Simple average of the n bars that end `back` bars before the last bar."""
    end = len(c) - back
    return None if end - n < 0 or end > len(c) else sum(c[end - n:end]) / n


def ema(c: List[float], n: int) -> float:
    k = 2 / (n + 1)
    e = c[0]
    for x in c[1:]:
        e = x * k + e * (1 - k)
    return e


def wilder_rsi(c: List[float], n: int = 14) -> float:
    d = [c[i] - c[i - 1] for i in range(1, len(c))]
    g = [max(x, 0) for x in d]
    lo = [max(-x, 0) for x in d]
    ag, al = sum(g[:n]) / n, sum(lo[:n]) / n
    for i in range(n, len(d)):
        ag = (ag * (n - 1) + g[i]) / n
        al = (al * (n - 1) + lo[i]) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def true_ranges(h, l, c):
    return [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, len(c))]


def wilder_atr(h, l, c, n: int = 14) -> float:
    tr = true_ranges(h, l, c)
    a = sum(tr[:n]) / n
    for t in tr[n:]:
        a = (a * (n - 1) + t) / n
    return a


def wilder_adx(h, l, c, n: int = 14) -> Optional[float]:
    """Wilder's ADX: smoothed +DM/-DM/TR sums, DX, then Wilder average of DX."""
    if len(c) < 2 * n + 1:
        return None
    tr = [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, len(c))]
    pdm, mdm = [], []
    for i in range(1, len(c)):
        up, dn = h[i] - h[i - 1], l[i - 1] - l[i]
        pdm.append(up if (up > dn and up > 0) else 0.0)
        mdm.append(dn if (dn > up and dn > 0) else 0.0)
    def smooth(x):
        s = [sum(x[:n])]
        for v in x[n:]:
            s.append(s[-1] - s[-1] / n + v)
        return s
    st, sp, sm = smooth(tr), smooth(pdm), smooth(mdm)
    dx = []
    for t, p, m in zip(st, sp, sm):
        pi, mi = (100 * p / t, 100 * m / t) if t else (0, 0)
        dx.append(0.0 if pi + mi == 0 else 100 * abs(pi - mi) / (pi + mi))
    a = sum(dx[:n]) / n
    for v in dx[n:]:
        a = (a * (n - 1) + v) / n
    return a


def obv_trend(c, v, lookback: int = 20) -> Optional[str]:
    """On-Balance Volume vs its own recent average with a +/-2% dead band (the definition printed in backend.calculate_obv's comments)."""
    if len(c) < lookback + 1:
        return None
    obv, run = [0.0], 0.0
    for i in range(1, len(c)):
        run += v[i] * (1 if c[i] > c[i - 1] else -1 if c[i] < c[i - 1] else 0)
        obv.append(run)
    recent = obv[-lookback:]
    avg = sum(recent) / lookback
    band = abs(avg) * 0.02
    cur = obv[-1]
    if band == 0:
        return 'rising' if cur > 0 else 'falling' if cur < 0 else 'flat'
    return 'rising' if cur > avg + band else 'falling' if cur < avg - band else 'flat'


def pct(a: float, b: float) -> float:
    return (a / b - 1) * 100
