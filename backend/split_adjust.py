"""
Stock-split handling: ONE table, ONE classifier, ONE adjuster (Day 126).
Plan: docs/claude/design/SPLIT_MECHANISM_PLAN_DAY126.md (v2, §9 overrides).

Why: SOXL.NE split 3-for-1 on 2026-05-25 and Yahoo and EODHD both left the older prices unadjusted, so every indicator that looks back
past that day was wrong. STA only adjusts from `backend/reference/known_splits.json` (each row backed by an issuer notice): a guess that
is wrong would silently corrupt every indicator, which is worse than a visible warning.

Rules
- ratio = new shares per old share (3.0 = 3-for-1, 0.04 = 1-for-25). `date` = first split-adjusted trading day.
- A row is applied only when the one-day step is really in the data (the provider did NOT adjust). If the provider already adjusted, nothing is
  done, so a later provider fix cannot double-adjust, and applying twice equals applying once.
- The step on split day is (split factor) x (that day's real move), so the test tolerates a real move (leveraged funds move 30-50%).
- Anything unclear (adjusted the wrong way, ambiguous) is reported and NOT adjusted.
- The stored cache is never touched: callers get a copy.
"""
import json
import logging
import math
import os

import pandas as pd

logger = logging.getLogger(__name__)

TABLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reference', 'known_splits.json')
WINDOW = 2                    # bars either side of the first bar on/after the table date (issuer and provider dates can differ)
RESIDUAL = math.log(1.35)     # how far a step may sit from the split factor (a real move rides on top of the split)
SMALL_RATIO = math.log(1.5)   # |ln ratio| under this (3:2, 4:3): too close to a normal move, so exact bar and a tighter residual
SMALL_RESIDUAL = math.log(1.10)
SIGNATURE = math.log(1.02)    # detector: a step within 2% of an exact whole-number factor
SIGNATURE_KS = range(3, 51)   # k=2 is not flagged (a -50% crash looks the same); the table still handles 2:1

PRICE_COLS = ('open', 'high', 'low', 'close')

_cache = {'mtime': None, 'rows': [], 'errors': []}


# ------------------------------------------------------------------------------------------------ table
def load_table(path=None):
    """(rows, errors). Missing or unreadable file -> ([], [reason]) and one log line, never an exception."""
    path = path or TABLE_PATH
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        if _cache['mtime'] != 'missing':
            logger.warning('known_splits.json not found at %s: no splits will be adjusted', path)
        _cache.update(mtime='missing', rows=[], errors=['known_splits.json is missing'])
        return [], list(_cache['errors'])
    if path == TABLE_PATH and _cache['mtime'] == mtime:
        return list(_cache['rows']), list(_cache['errors'])
    rows, errors = [], []
    try:
        raw = json.load(open(path))
        if not isinstance(raw, list):
            raise ValueError('top level must be a list')
    except Exception as e:
        raw, errors = [], [f'known_splits.json unreadable: {type(e).__name__}: {e}']
    seen = set()
    for i, r in enumerate(raw):
        try:
            sym = str(r['symbol']).strip().upper()
            date = pd.Timestamp(r['date']).normalize()
            ratio = float(r['ratio'])
            if not sym or not math.isfinite(ratio) or ratio <= 0 or ratio == 1:
                raise ValueError('ratio must be > 0 and not 1')
            if not str(r.get('source_url') or '').strip():
                raise ValueError('source_url is required')
            if (sym, date) in seen:
                raise ValueError('duplicate symbol and date')
            seen.add((sym, date))
            rows.append({'symbol': sym, 'date': date, 'ratio': ratio, 'source_url': r['source_url'],
                         'verified_on': r.get('verified_on'), 'note': r.get('note')})
        except Exception as e:
            errors.append(f'row {i + 1} skipped: {type(e).__name__}: {e}')
    for e in errors:
        logger.warning('known_splits.json: %s', e)
    if path == TABLE_PATH:
        _cache.update(mtime=mtime, rows=rows, errors=errors)
    return list(rows), list(errors)


def rows_for(symbol, path=None):
    rows, errors = load_table(path)
    s = str(symbol or '').upper()
    return [r for r in rows if r['symbol'] == s], errors


def describe(row):
    """'3-for-1 on 2026-05-25' / '1-for-25 on ...'"""
    r = row['ratio']
    if r >= 1:
        txt = f'{r:g}-for-1'
    else:
        txt = f'1-for-{1 / r:g}'
    return f"{txt} on {row['date'].date()}"


# ------------------------------------------------------------------------------------------------ classify
def classify(df, row):
    """What does the data say about this table row?  Returns
    {status, bar, bar_date, step, residual}; status is one of
    unadjusted | already_adjusted | wrong_way | ambiguous | pending | not_applicable.
    `bar` is the integer position of the first split-adjusted bar when status == 'unadjusted'."""
    idx = pd.DatetimeIndex(df.index)
    if idx.tz is not None:                 # Yahoo sends America/Toronto-aware timestamps; the table dates are plain dates
        idx = idx.tz_localize(None)
    idx = idx.normalize()
    n = len(idx)
    D = row['date']
    if n >= 2 and not idx.is_monotonic_increasing:
        return {'status': 'ambiguous', 'note': 'the price history is not in date order, so the split step cannot be read'}
    if n < 2 or D <= idx[0]:
        return {'status': 'not_applicable', 'note': 'split date is before the first bar'}
    pos = int(idx.searchsorted(D, side='left'))
    if pos >= n:
        return {'status': 'pending', 'note': 'split date is after the last bar'}
    R = row['ratio']
    lnR = abs(math.log(R))
    small = lnR <= SMALL_RATIO + 1e-9          # 3:2 sits exactly on the threshold, so include it
    close = pd.to_numeric(df['close'], errors='coerce').to_numpy(dtype=float)
    lo, hi = (pos, pos) if small else (max(1, pos - WINDOW), min(n - 1, pos + WINDOW))
    tol = SMALL_RESIDUAL if small else RESIDUAL
    best_unadj = best_wrong = None
    candidates = 0
    unusable = 0
    for i in range(lo, hi + 1):
        if i < 1:
            continue
        if not (close[i] > 0 and close[i - 1] > 0):
            unusable += 1                               # a missing/zero close next to the split date: we cannot read the step
            continue
        s = close[i] / close[i - 1]
        ls = abs(math.log(s))
        if not small and ls < lnR / 2:
            continue                                    # no real step on this bar
        candidates += 1
        res = abs(math.log(s * R))                      # 0 when the old prices are still unadjusted
        if res <= tol and (small or res < ls / 2):
            if best_unadj is None or res < best_unadj[1]:
                best_unadj = (i, res, s)
        res_w = abs(math.log(s / R))                    # 0 when the provider adjusted the wrong way
        if res_w <= tol and (best_wrong is None or res_w < best_wrong[1]):
            best_wrong = (i, res_w, s)
    if best_unadj:
        i, res, s = best_unadj
        return {'status': 'unadjusted', 'bar': i, 'bar_date': idx[i], 'step': s, 'residual': res}
    if best_wrong:
        i, res, s = best_wrong
        return {'status': 'wrong_way', 'bar': i, 'bar_date': idx[i], 'step': s,
                'note': f'a step of x{s:.3f} on {idx[i].date()} matches the split applied the wrong way'}
    if candidates == 0 and unusable:
        return {'status': 'ambiguous', 'note': 'a close is missing next to the split date, so it cannot be told whether the provider adjusted it'}
    if candidates == 0:
        return {'status': 'already_adjusted', 'note': 'no step in the data: the provider adjusted it'}
    return {'status': 'ambiguous', 'note': 'a large move near the split date matches neither raw nor adjusted prices'}


# ------------------------------------------------------------------------------------------------ adjust
def adjust_for_splits(df, symbol, path=None):
    """(adjusted_copy, events). events: one dict per table row for the symbol:
    {date, ratio, text, status, applied(bool), bar_date, source_url, note}.  `df` itself is never modified.
    Never raises: on any failure it returns the unchanged copy and an event with status 'error'."""
    out = df.copy() if df is not None else df
    events = []
    if df is None or len(df) == 0:
        return out, events
    try:
        rows, errors = rows_for(symbol, path)
        for e in errors:
            events.append({'status': 'table_error', 'applied': False, 'note': e})
        for row in sorted(rows, key=lambda r: r['date']):
            c = classify(out, row)
            ev = {'date': str(row['date'].date()), 'ratio': row['ratio'], 'text': describe(row), 'status': c['status'], 'applied': False,
                  'bar_date': str(c['bar_date'].date()) if c.get('bar_date') is not None else None,
                  'source_url': row['source_url'], 'note': c.get('note')}
            if c['status'] == 'unadjusted':
                pos = c['bar']
                R = row['ratio']
                for col in PRICE_COLS:
                    if col in out.columns:
                        out[col] = out[col].astype(float)
                        out.iloc[:pos, out.columns.get_loc(col)] = out[col].iloc[:pos] / R
                if 'volume' in out.columns:
                    out['volume'] = out['volume'].astype(float)
                    out.iloc[:pos, out.columns.get_loc('volume')] = out['volume'].iloc[:pos] * R
                ev['applied'] = True
            events.append(ev)
    except Exception as exc:
        logger.warning('split adjustment failed for %s: %s', symbol, exc)
        return (df.copy() if df is not None else df), [{'status': 'error', 'applied': False, 'note': f'{type(exc).__name__}: {exc}'}]
    return out, events


def fix_frame(df, symbol):
    """For the emergency direct-Yahoo fallbacks in the routes: same adjustment, any column case, same column names back, never raises."""
    if df is None or len(df) == 0:
        return df
    try:
        orig = list(df.columns)
        low = df.copy()
        low.columns = [str(c).lower() for c in orig]
        out, _events = adjust_for_splits(low, symbol)
        out.columns = orig
        return out
    except Exception as exc:
        logger.warning('split fix failed for %s: %s', symbol, exc)
        return df


# ------------------------------------------------------------------------------------------------ detector
def possible_split_k(step):
    """Whole k (3..50) when a one-day close step is within 2% of exactly 1/k (forward split) or k (reverse split); else None.
    Real one-day moves on 3x funds (e.g. +47%, +55%, +70%) do not sit this close to an integer factor."""
    if not (step and step > 0 and math.isfinite(step)):
        return None
    for k in SIGNATURE_KS:
        if abs(math.log(step * k)) <= SIGNATURE:
            return k
        if abs(math.log(step / k)) <= SIGNATURE:
            return -k          # negative = reverse split (price rose by k)
    return None


def has_split_in_window(df, symbol):
    """True when the table lists a split for `symbol` dated inside this frame (so provider 52-week figures may mix pre- and post-split prices)."""
    if df is None or len(df) == 0:
        return False
    idx = pd.DatetimeIndex(df.index)
    first = (idx.tz_localize(None) if idx.tz is not None else idx).normalize()[0]
    return any(r['date'] > first for r in rows_for(symbol)[0])


def adjusted_52w(df, bars=252):
    """(high, low) over the last `bars` bars of an already-adjusted frame (None, None when too short)."""
    if df is None or len(df) == 0:
        return None, None
    t = df.tail(bars)
    hi, lo = pd.to_numeric(t['high'], errors='coerce').max(), pd.to_numeric(t['low'], errors='coerce').min()
    return (None if pd.isna(hi) else float(hi)), (None if pd.isna(lo) else float(lo))
