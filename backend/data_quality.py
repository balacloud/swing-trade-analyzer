"""
Data-quality checks on a daily price history: ONE copy, used by the Data Sources tab and by the audit scripts.
Plan: docs/claude/design/DATA_SOURCES_TAB_V2_PLAN_DAY126.md §3.1 (Golden Rule 59: one rule, one place).

Two layers, kept apart on purpose:
  FACTS   check_history(df)  -> counts, dates and flags. No judgement.
  LEVELS  level_*()          -> PASS / WARN / FAIL for each fact. The audit and the tab call the same functions;
                                the tab passes tolerant=True for freshness because the backend has no holiday calendar.

Why it exists: on 2026-11-14 SOXL.NE had 311 of 311 flat zero-volume bars and an unadjusted 3:1 split, and the Data
Sources tab said "JUST FETCHED, yfinance, 311 points". Nothing could see it. These checks can.

Thresholds are the audit's (flat 2% warn / 20% fail, one-day move 40%, bar tolerance 0.1% of the close).
Never raises: on any error check_history returns {'state': 'error', 'reason': ...} and logs it with the ticker.
"""
import logging
import re

import numpy as np
import pandas as pd

from market_time import MARKET_TZ, drop_forming_bar

logger = logging.getLogger(__name__)

JUMP_PCT = 0.40            # a one-day close-to-close move this big needs explaining (split or real)
FLAT_WARN, FLAT_FAIL = 0.02, 0.20   # share of bars with high == low and zero volume
BAR_TOL = 0.001            # a high/low wrong by under 0.1% of the close is rounding (Tradier, ex-dividend days)
MIN_BARS_WARN, MIN_BARS_FAIL = 252, 60
ANALYZE_WINDOW = 260       # /api/stock and the Analyze page use hist.tail(260)
CLOSE_WARN, CLOSE_FAIL = 0.003, 0.01   # cross-source / broker close disagreement (audit scripts)

ORDER = ['PASS', 'WARN', 'FAIL']
ICON = {'PASS': '✅', 'WARN': '⚠️', 'FAIL': '❌', 'NA': '—'}


def worst(levels):
    """Worst of PASS/WARN/FAIL (ignores anything else, e.g. 'NA'); 'NA' if nothing gradable."""
    levels = [l for l in levels if l in ORDER]
    return max(levels, key=ORDER.index) if levels else 'NA'


# ---------------------------------------------------------------------------------------------- facts

def expected_last_session(now=None):
    """The most recent weekday on or before today in New York. No holiday calendar exists in the backend, so a
    market holiday makes a history look one or two sessions behind; callers that show this to a person pass tolerant=True."""
    now = now or pd.Timestamp.now(tz=MARKET_TZ)
    d = pd.Timestamp(now.date())
    while d.weekday() >= 5:
        d = d - pd.Timedelta(days=1)
    return d


def jump_moves(df):
    """{Timestamp: return} for every one-day close-to-close move over JUMP_PCT. Shared with the audit's cross-source check."""
    r = df['close'].pct_change(fill_method=None).dropna()
    return {d: float(v) for d, v in r.items() if abs(v) > JUMP_PCT}


def check_history(df, now=None, ticker=None):
    """Facts about one daily history (columns open, high, low, close, volume; DatetimeIndex).
    Today's still-forming bar is dropped first (market_time.drop_forming_bar) and reported, so a partial bar can
    neither trigger the zero-volume checks nor read as a fresh bar. Never raises."""
    try:
        if df is None or len(df) == 0:
            return {'state': 'error', 'reason': 'empty price history'}
        h = df.copy()
        h.columns = [str(c).lower() for c in h.columns]
        missing = [c for c in ('open', 'high', 'low', 'close', 'volume') if c not in h.columns]
        if missing:
            return {'state': 'error', 'reason': f'missing columns: {", ".join(missing)}'}
        if getattr(h.index, 'tz', None) is not None:
            h.index = h.index.tz_localize(None)
        h.index = pd.to_datetime(h.index).normalize()
        h = h[~h.index.duplicated(keep='last')].sort_index()
        for c in ('open', 'high', 'low', 'close', 'volume'):
            h[c] = pd.to_numeric(h[c], errors='coerce')
        h, dropped = drop_forming_bar(h, now=now)
        if len(h) == 0:
            return {'state': 'error', 'reason': 'only a forming bar, no completed history'}
        last = h.index[-1]
        exp = expected_last_session(now)
        flat = float(((h['high'] == h['low']) & (h['volume'].fillna(0) == 0)).mean())
        tol = BAR_TOL * h['close']
        bad = int(((h['high'] < h[['open', 'close']].max(axis=1) - tol) | (h['low'] > h[['open', 'close']].min(axis=1) + tol)).sum())
        window_start = h.index[-ANALYZE_WINDOW] if len(h) > ANALYZE_WINDOW else h.index[0]
        # Day 126: split awareness. Table rows for this ticker are classified against the RAW frame (the cache is raw);
        # a jump on the bar a row says STA adjusts is "covered"; a jump that sits on an exact whole-number factor and is not covered
        # is reported as a possible split.
        import split_adjust
        splits, table_errors = [], []
        if ticker:
            rows, table_errors = split_adjust.rows_for(ticker)
            for row in sorted(rows, key=lambda r: r['date']):
                c = split_adjust.classify(h, row)
                splits.append({'text': split_adjust.describe(row), 'status': c['status'], 'bar_date': str(c['bar_date'].date()) if c.get('bar_date') is not None else None,
                               'note': c.get('note'), 'source_url': row['source_url']})
        covered_dates = {x['bar_date'] for x in splits if x['status'] == 'unadjusted'}
        jumps = []
        for d, v in jump_moves(h).items():
            k = split_adjust.possible_split_k(1 + v)
            jumps.append({'date': str(d.date()), 'pct': round(v * 100, 1), 'in_last_260': bool(d >= window_start),
                          'split_k': k, 'covered': str(d.date()) in covered_dates})
        return {
            'state': 'ok',
            'bars': int(len(h)),
            'first_date': str(h.index[0].date()),
            'last_date': str(last.date()),
            'expected_last_date': str(exp.date()),
            'sessions_behind': int(max(0, np.busday_count(last.date(), exp.date()))),
            'forming_bar_dropped': bool(dropped),
            'flat_zero_volume_pct': round(flat * 100, 1),
            'zero_volume_last5': int((h['volume'].tail(5).fillna(0) == 0).sum()),
            'bad_rows': bad,
            'nan_closes': int(h['close'].isna().sum()),
            'jumps': jumps,
            'splits': splits,
            'split_table_errors': table_errors,
        }
    except Exception as e:   # never take the endpoint down; say what failed
        logger.warning('data_quality.check_history failed for %s: %s', ticker or '?', e)
        return {'state': 'error', 'reason': f'{type(e).__name__}: {str(e)[:120]}'}


# ---------------------------------------------------------------------------------------------- levels

def level_freshness(sessions_behind, forming_bar_dropped=False, tolerant=False):
    """Audit rule (tolerant=False): 2+ sessions behind FAIL, 1 WARN, a forming bar WARN.
    Tab rule (tolerant=True): 0-2 behind is fine (a holiday can explain it), 3+ WARN, 6+ FAIL; a forming bar is normal."""
    if tolerant:
        return 'FAIL' if sessions_behind >= 6 else 'WARN' if sessions_behind >= 3 else 'PASS'
    if sessions_behind >= 2:
        return 'FAIL'
    if sessions_behind == 1 or forming_bar_dropped:
        return 'WARN'
    return 'PASS'


def level_integrity(flat_pct, bad_rows, zero_volume_last5, nan_closes):
    if flat_pct / 100 > FLAT_FAIL or bad_rows > 3:
        return 'FAIL'
    if flat_pct / 100 > FLAT_WARN or bad_rows or zero_volume_last5 or nan_closes:
        return 'WARN'
    return 'PASS'


def level_history(bars):
    return 'FAIL' if bars < MIN_BARS_FAIL else 'WARN' if bars < MIN_BARS_WARN else 'PASS'


def _jumps_check(facts):
    """One-day moves over 40%, with split awareness (Day 126, plan §9 item 8):
    covered by known_splits.json -> not a warning (STA adjusts it, the tab says so);
    an exact whole-number factor in the last 260 bars and NOT covered -> FAIL (a possible unadjusted split);
    a table row that is wrong-way, ambiguous or malformed -> FAIL; any other big move -> WARN (a real move, or a split we cannot tell)."""
    j = [x for x in facts['jumps'] if not x.get('covered')]
    splits = facts.get('splits') or []
    bad_rows = [x for x in splits if x['status'] in ('wrong_way', 'ambiguous')]
    errs = facts.get('split_table_errors') or []
    possible = [x for x in j if x.get('split_k') and x['in_last_260']]
    parts, level = [], 'PASS'
    for x in possible:
        k = x['split_k']
        kind = f'{k}-for-1' if k > 0 else f'1-for-{-k}'
        parts.append(f"{x['date']} {x['pct']:+.0f}% looks like a possible {kind} split that is not in known_splits.json (prices before it may be wrong)")
    for x in bad_rows:
        parts.append(f"known split {x['text']}: {x['note']}; STA did not adjust it")
    for e in errs:
        parts.append(f'known_splits.json problem: {e}')
    if parts:
        level = 'FAIL'
    others = [x for x in j if x not in possible]
    if others:
        parts.append('; '.join(f"{x['date']} {x['pct']:+.0f}%" + ('' if x['in_last_260'] else ' (older than the last 260 bars)') for x in others)
                     + ': a real move, or an unadjusted split. Compare with a second source.')
        if level != 'FAIL':
            level = 'WARN'
    if not parts:
        return {'level': 'PASS', 'note': 'no one-day move over 40%' if not facts['jumps'] else 'every big one-day move is explained by known_splits.json'}
    return {'level': level, 'note': ' | '.join(parts)}


def quality_level(facts, tolerant=True):
    """The tab's summary of check_history() facts: {'level', 'checks': {name: {'level', 'note'}}}.
    Jumps: see _jumps_check (a split-like jump that the table does not cover is a FAIL; other big moves WARN)."""
    if facts.get('state') != 'ok':
        return {'level': 'FAIL', 'checks': {'history': {'level': 'FAIL', 'note': facts.get('reason', 'no history')}}}
    c = {}
    n = facts['sessions_behind']
    c['freshness'] = {'level': level_freshness(n, facts['forming_bar_dropped'], tolerant),
                      'note': f"last bar {facts['last_date']}" + (f', {n} session{"s" if n != 1 else ""} behind' if n else '')
                              + (' (a market holiday can explain 1-2)' if 0 < n <= 2 and tolerant else '')}
    c['integrity'] = {'level': level_integrity(facts['flat_zero_volume_pct'], facts['bad_rows'], facts['zero_volume_last5'], facts['nan_closes']),
                      'note': f"{facts['flat_zero_volume_pct']:.0f}% of bars flat with zero volume; {facts['bad_rows']} malformed bars; "
                              f"zero volume on {facts['zero_volume_last5']} of the last 5 days"}
    c['history'] = {'level': level_history(facts['bars']), 'note': f"{facts['bars']} bars from {facts['first_date']}"}
    c['jumps'] = _jumps_check(facts)
    return {'level': worst([v['level'] for v in c.values()]), 'checks': c}


# ---------------------------------------------------------------------------------------------- class

_CDR_RE = re.compile(r'\bCDR\b', re.I)
LEVERAGE_RE = re.compile(r'\b[23]X\b|\bDAILY\b|\bDLY\b|\bBETAPRO\b|\bBULL\b|\bBEAR\b|\bULTRA(PRO)?\b', re.I)


def classify_instrument(quote_type, name):
    """Stock / ETF / Leveraged ETF / CDR from Yahoo's quote type and name, with the basis. An INFERENCE: the tab says so.
    Checked on real Yahoo names (Day 126): all five CDRs say "CDR" (and Yahoo calls most of them ETF);
    all eight leveraged funds say 2X/3X or Daily. No price test (the tab has no US twin price)."""
    qt = (quote_type or '').upper()
    nm = name or ''
    if not qt and not nm:
        return {'class': 'Unknown', 'basis': 'no quote type or name'}
    if _CDR_RE.search(nm):
        return {'class': 'CDR', 'basis': "name contains 'CDR' (Canadian receipt of a US stock)"}
    if qt == 'ETF':
        hits = list(dict.fromkeys(m.group(0).upper() for m in LEVERAGE_RE.finditer(nm)))
        if hits:
            return {'class': 'Leveraged ETF', 'basis': 'ETF with ' + ', '.join(f"'{h}'" for h in hits) + ' in the name'}
        return {'class': 'ETF', 'basis': 'quote type ETF'}
    if qt == 'EQUITY':
        return {'class': 'Stock', 'basis': 'quote type EQUITY'}
    if not qt:
        return {'class': 'Unknown', 'basis': 'no quote type'}
    return {'class': 'Unknown', 'basis': f'quote type {qt}'}


# ---------------------------------------------------------------------------------------------- audit reference file
# backend/reference/ is tracked (backend/data/ is gitignored). Each audit script updates ONLY its own section per ticker;
# regeneration is manual (whoever runs the audit). Written atomically so a reader never sees half a file.
import json  # noqa: E402
import os  # noqa: E402
from datetime import date as _date  # noqa: E402

REFERENCE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reference')
AUDIT_LATEST = os.path.join(REFERENCE_DIR, 'data_audit_latest.json')


def _short(text, n=220):
    return text if len(text) <= n else text[: n - 1] + '…'


def _lead_segment(note):
    """A roll-up note joins one segment per source ("a || b || c") and per finding ("x | y"). Lead with the one that names
    the actual defect (an 'ONLY here ... split error' or an x3 level error) instead of the first one, which can be benign."""
    segs = [x.strip() for part in note.split(' || ') for x in part.split(' | ')]
    for marker in ('split error', 'ONLY here', '(x'):
        for seg in segs:
            if marker in seg:
                return seg
    return segs[0] if segs else note


def update_audit_reference(section, generated, report, tickers, path=AUDIT_LATEST):
    """tickers: {SYMBOL: [(check_id, level, note), ...]}. Merges into `section` ('truth_free' or 'vs_ibkr')."""
    try:
        data = json.load(open(path))
    except Exception:
        data = {'tickers': {}}
    for sym, checks in tickers.items():
        level = worst([c[1] for c in checks])
        # ONE line for the tab: the worst finding only (a FAIL beats a WARN), with the check id and a short note.
        bad = [c for c in checks if c[1] in ('WARN', 'FAIL')]
        top = max(bad, key=lambda c: ORDER.index(c[1])) if bad else None
        line = _short(f'{top[0]}: {_lead_segment(top[2])}', 150) if top else ''
        data['tickers'].setdefault(sym, {})[section] = {
            'date': generated[:10], 'report': report, 'level': level, 'line': line}
    data['updated'] = generated
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(data, f, indent=1)
    os.replace(tmp, path)


def read_audit_summary(symbol, path=AUDIT_LATEST, today=None):
    """One-line audit result for the tab, or None when the ticker was never audited or every section passed.
    {'level', 'line', 'date', 'age_days', 'report'}. Never raises."""
    try:
        sec = json.load(open(path))['tickers'].get(symbol.upper())
        if not sec:
            return None
        bad = {k: v for k, v in sec.items() if v.get('level') in ('WARN', 'FAIL')}
        if not bad:
            return None
        k, v = max(bad.items(), key=lambda kv: ORDER.index(kv[1]['level']))     # the worst section only
        age = ((today or _date.today()) - _date.fromisoformat(v['date'])).days
        return {'level': v['level'], 'line': v['line'], 'date': v['date'], 'age_days': age, 'report': v['report'], 'section': k}
    except Exception as e:
        logger.warning('read_audit_summary failed for %s: %s', symbol, e)
        return None
