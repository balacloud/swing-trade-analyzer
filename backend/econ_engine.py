"""
econ_engine.py — Context Tab Column B
Day 62, v4.24

4 Economic Indicator cards:
  1. Fed Funds Rate   (FRED FEDFUNDS)
  2. CPI Inflation    (FRED CPIAUCSL + CPILFESL)
  3. ISM PMI proxy    (FRED MANEMP — manufacturing employment as proxy)
  4. Unemployment     (FRED UNRATE)

Core STA engine is FROZEN. This file is additive / informational only.
"""

import os
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

FRED_API_KEY = os.environ.get('FRED_API_KEY')
FRED_BASE_URL = 'https://api.stlouisfed.org/fred/series/observations'

# Single source of truth for the PMI proxy card's name — _build_composite()
# looks a card up by this exact string. Day 91 renamed the card (from "ISM
# PMI (proxy)") but the composite's lookup string wasn't updated to match,
# so the lookup silently missed forever and pmi stayed stuck at the fallback
# 'NEUTRAL'. Both _pmi_card() and _build_composite() now reference this one
# constant, so a future rename can't cause the two to silently diverge again.
PMI_CARD_NAME = 'Manufacturing Employment (PMI proxy)'


# ─── FRED helper (same as cycles_engine) ─────────────────────────────────────
def _fetch_fred(series_id: str, limit: int = 14):
    """Fetch FRED series observations, newest first. Returns list of (date, float) tuples."""
    if not FRED_API_KEY:
        return None
    try:
        resp = requests.get(FRED_BASE_URL, params={
            'series_id': series_id,
            'api_key': FRED_API_KEY,
            'limit': limit,
            'sort_order': 'desc',
            'file_type': 'json',
        }, timeout=10)
        resp.raise_for_status()
        observations = resp.json().get('observations', [])
        result = []
        for o in observations:
            try:
                val = float(o['value'])
                result.append((o['date'], val))
            except (ValueError, TypeError):
                pass  # skip "." missing FRED entries
        return result
    except Exception as e:
        logger.warning(f"FRED fetch failed for {series_id}: {e}")
        return None


def _at_months_ago(series: list, latest_date, months: int):
    """Find the observation `months` calendar-months before latest_date, by
    date match rather than list position. FRED sometimes withholds a month's
    observation ('.', already filtered out by _fetch_fred), which silently
    shifts every later list index by one — a fixed-position lookback then
    lands on the wrong month. Confirmed live (Session 28 audit, Jul 2026):
    a missing 2025-10 CPI observation shifted the "12 back" index onto
    2025-05 instead of 2025-06, reporting CPI YoY as 3.7%/2.8% when the
    real year-over-year figure (correctly date-matched) is 3.5%/2.6%.
    """
    target_month = latest_date.month - months
    target_year = latest_date.year
    while target_month <= 0:
        target_month += 12
        target_year -= 1
    for date_str, val in series:
        d = datetime.strptime(date_str, '%Y-%m-%d')
        if d.year == target_year and d.month == target_month:
            return val
    return None


def _yoy(series: list, periods: int = 12):
    """Calculate YoY % change. series = [(date, val), ...] newest first.
    `periods` is a calendar-month count, matched by date via _at_months_ago,
    not a raw list index (see its docstring for why that distinction matters)."""
    if not series:
        return None
    latest_date = datetime.strptime(series[0][0], '%Y-%m-%d')
    latest = series[0][1]
    year_ago = _at_months_ago(series[1:], latest_date, periods)
    if year_ago is None or year_ago == 0:
        return None
    return ((latest - year_ago) / abs(year_ago)) * 100


def _trend(series: list, periods: int = 3, threshold: float = 0.1):
    """
    Returns 'rising', 'falling', or 'flat' comparing latest to `periods`
    calendar-months ago (date-matched via _at_months_ago, not list position).
    series = [(date, val), ...] newest first.
    threshold: minimum delta to call rising/falling (default 0.1 for Fed Funds bps;
               pass 0.3 for unemployment per spec 'rapidly rising = >0.3% in 3 months')
    """
    if not series:
        return 'flat'
    latest_date = datetime.strptime(series[0][0], '%Y-%m-%d')
    latest = series[0][1]
    old = _at_months_ago(series[1:], latest_date, periods)
    if old is None:
        return 'flat'
    delta = latest - old
    if delta > threshold:
        return 'rising'
    elif delta < -threshold:
        return 'falling'
    return 'flat'


# ─── Card builders ────────────────────────────────────────────────────────────
def _fed_funds_card():
    data = _fetch_fred('FEDFUNDS', limit=8)
    if data:
        latest_date, latest = data[0]
        # Compare latest to 6 months ago (approx 6 entries back)
        six_mo_ago = data[min(6, len(data) - 1)][1]
        delta = latest - six_mo_ago

        if delta < -0.1:
            regime = 'FAVORABLE'
            direction = 'Cutting'
            phase = f'{latest:.2f}% · Cutting (−{abs(delta):.2f}% in 6mo)'
            history = 'Cutting w/o recession = avg S&P +18% Yr1'
        elif delta > 0.1:
            regime = 'ADVERSE'
            direction = 'Hiking'
            phase = f'{latest:.2f}% · Hiking (+{delta:.2f}% in 6mo)'
            history = 'Hiking cycle = headwind for equities'
        else:
            regime = 'NEUTRAL'
            direction = 'Hold'
            phase = f'{latest:.2f}% · Hold (flat 6mo)'
            history = 'Hold with stable rate = typically neutral for equities'

        value_str = f'{latest:.2f}% · {direction}'
        raw_value = latest
    else:
        regime = 'NEUTRAL'
        value_str = 'N/A'
        phase = 'FRED data unavailable'
        history = 'Configure FRED_API_KEY'
        raw_value = None

    return {
        'name': 'Fed Funds Rate',
        'icon': '💵',
        'value': value_str,
        'phase': phase,
        'source': 'FRED FEDFUNDS',
        'series_id': 'FEDFUNDS',
        'history': history,
        'regime': regime,
        'raw_value': raw_value,
    }


def _cpi_card():
    headline_data = _fetch_fred('CPIAUCSL', limit=14)
    core_data = _fetch_fred('CPILFESL', limit=14)

    headline_yoy = _yoy(headline_data)
    core_yoy = _yoy(core_data)

    if headline_yoy is not None:
        if headline_yoy <= 3.0:
            regime = 'FAVORABLE'
            phase = f'Sweet spot (≤3%) — avg S&P +15.6%/yr'
        elif headline_yoy <= 5.0:
            regime = 'NEUTRAL'
            phase = f'Elevated inflation — equity headwind'
        else:
            regime = 'ADVERSE'
            phase = f'High inflation (>5%) — Fed forced to hike'

        core_str = f' · Core: {core_yoy:.1f}%' if core_yoy is not None else ''
        value_str = f'{headline_yoy:.1f}% YoY{core_str}'
        raw_value = headline_yoy
    else:
        regime = 'NEUTRAL'
        value_str = 'N/A'
        phase = 'FRED data unavailable'
        raw_value = None

    return {
        'name': 'CPI Inflation',
        'icon': '📈',
        'value': value_str,
        'phase': phase,
        'source': 'FRED CPIAUCSL · CPILFESL',
        'series_id': 'CPIAUCSL',
        'history': 'Sweet spot 2–3%: avg S&P +15.6%/yr historically',
        'regime': regime,
        'raw_value': raw_value,
    }


def _pmi_card():
    """
    Uses FRED MANEMP (manufacturing employment) as PMI proxy.
    MoM % change proxies for ISM PMI direction.
    Transparent labeling: "PMI proxy (MANEMP)".
    """
    data = _fetch_fred('MANEMP', limit=3)
    if data and len(data) >= 2:
        latest = data[0][1]
        prev = data[1][1]
        mom_pct = ((latest - prev) / prev) * 100 if prev else 0.0

        # Session 28 audit fix: the prior "(proxy PMI>52)" / "48-52" / "<48"
        # bands implied this MoM employment-count change had been calibrated
        # against the real ISM PMI diffusion index. It hasn't — these
        # thresholds were chosen for this proxy alone. Label the regime in
        # this proxy's own terms, not borrowed PMI numbers.
        if mom_pct > 0.15:
            regime = 'FAVORABLE'
            phase = f'{latest:.0f}K workers · +{mom_pct:.2f}% MoM · Expanding'
        elif mom_pct >= -0.05:
            regime = 'NEUTRAL'
            phase = f'{latest:.0f}K workers · {mom_pct:+.2f}% MoM · Flat'
        else:
            regime = 'ADVERSE'
            phase = f'{latest:.0f}K workers · {mom_pct:.2f}% MoM · Contracting'

        value_str = f'MANEMP {mom_pct:+.2f}% MoM'
        raw_value = mom_pct
    else:
        regime = 'NEUTRAL'
        value_str = 'N/A'
        phase = 'FRED data unavailable'
        raw_value = None

    return {
        'name': PMI_CARD_NAME,
        'icon': '🏭',
        'value': value_str,
        'phase': phase,
        'source': 'FRED MANEMP (manufacturing employment proxy, NOT real ISM PMI)',
        'series_id': 'MANEMP',
        'history': 'Employment-count proxy only — the "PMI 50-55 = +10.1% fwd 12m" historical stat was built from the real ISM PMI series and does not apply to this metric',
        'regime': regime,
        'raw_value': raw_value,
    }


def _unemployment_card():
    data = _fetch_fred('UNRATE', limit=5)
    if data:
        latest_date, latest = data[0]
        # threshold=0.3: spec says 'rapidly rising' = >0.3% over 3 months
        trend_dir = _trend(data, periods=3, threshold=0.3)

        if latest < 4.5 and trend_dir in ('falling', 'flat'):
            regime = 'FAVORABLE'
            trend_label = 'Stable' if trend_dir == 'flat' else 'Falling ↓'
        elif latest <= 5.5 or trend_dir == 'rising':
            regime = 'NEUTRAL'
            trend_label = 'Rising ↑' if trend_dir == 'rising' else 'Stable'
        else:
            regime = 'ADVERSE'
            trend_label = 'Rising ↑ (late cycle warning)'

        value_str = f'{latest:.1f}% · {trend_label}'
        phase = 'Rising trend = late cycle warning' if trend_dir == 'rising' else \
                'Low and stable = healthy labor market'
        raw_value = latest
    else:
        regime = 'NEUTRAL'
        value_str = 'N/A'
        phase = 'FRED data unavailable'
        raw_value = None

    return {
        'name': 'Unemployment',
        'icon': '👷',
        'value': value_str,
        'phase': phase,
        'source': 'FRED UNRATE',
        'series_id': 'UNRATE',
        'history': 'Rising unemployment = late cycle — reduce risk',
        'regime': regime,
        'raw_value': raw_value,
    }


# ─── Historical composite box ─────────────────────────────────────────────────
def _build_composite(cards):
    """Map current regime combination to historical description."""
    card_map = {c['name']: c for c in cards}
    fed = card_map.get('Fed Funds Rate', {}).get('regime', 'NEUTRAL')
    cpi = card_map.get('CPI Inflation', {}).get('regime', 'NEUTRAL')
    pmi = card_map.get(PMI_CARD_NAME, {}).get('regime', 'NEUTRAL')

    if fed == 'FAVORABLE' and cpi == 'FAVORABLE' and pmi == 'FAVORABLE':
        return {
            'title': 'Rising Growth + Falling CPI',
            'description': 'Historically BEST macro combo — Fed easing + low inflation + expanding economy.',
            'avg_return': 'Avg S&P forward 12m: +18–22%',
            'source': 'S&P Global 50yr factor study',
        }
    elif fed == 'ADVERSE' and cpi == 'ADVERSE':
        return {
            'title': 'Stagflation Risk',
            'description': 'High inflation + Fed hiking = most difficult environment for equities.',
            'avg_return': 'Avg S&P forward 12m: −5 to +2%',
            'source': 'Historical macro factor analysis',
        }
    elif cpi == 'FAVORABLE' and pmi == 'FAVORABLE':
        return {
            'title': 'Goldilocks Conditions',
            'description': 'Low inflation + expanding economy — equities typically perform well.',
            'avg_return': 'Avg S&P forward 12m: +12–16%',
            'source': 'Historical macro factor analysis',
        }
    elif pmi == 'ADVERSE':
        return {
            'title': 'Contractionary PMI',
            'description': 'Manufacturing contraction signals slowing growth — consider defensives.',
            'avg_return': 'Avg S&P forward 12m: +3–7% (range wide)',
            'source': 'Historical macro factor analysis',
        }
    else:
        n_favorable = sum(1 for c in cards if c['regime'] == 'FAVORABLE')
        n_adverse = sum(1 for c in cards if c['regime'] == 'ADVERSE')
        return {
            'title': f'Mixed Conditions ({n_favorable}/4 favorable)',
            'description': 'No dominant regime. Monitor for trend development.',
            'avg_return': 'Historical returns vary widely in mixed regimes',
            'source': 'Composite macro assessment',
        }


# ─── Main entry point ─────────────────────────────────────────────────────────
def get_econ():
    """
    Returns 4 economic indicator cards + historical composite.
    Column B data — global, no ticker needed.
    """
    cards = [
        _fed_funds_card(),
        _cpi_card(),
        _pmi_card(),
        _unemployment_card(),
    ]

    regimes = [c['regime'] for c in cards]
    summary = {
        'favorable': regimes.count('FAVORABLE'),
        'neutral': regimes.count('NEUTRAL'),
        'adverse': regimes.count('ADVERSE'),
    }

    composite = _build_composite(cards)

    return {
        'cards': cards,
        'composite': composite,
        'summary': summary,
        'timestamp': datetime.now().isoformat(),
        'fred_available': FRED_API_KEY is not None,
    }
