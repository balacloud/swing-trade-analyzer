"""
cycles_engine.py — Context Tab Column A
Day 62, v4.24

6 Calendar & Yield Cycle cards:
  1. Yield Curve      (FRED T10Y2Y)
  2. Business Cycle   (FRED INDPRO)
  3. Presidential Year (Calendar)
  4. Seasonal Regime  (Calendar)
  5. FOMC Proximity   (Hardcoded 2026-2027 dates)
  6. Quad Witching    (Computed — 3rd Friday Mar/Jun/Sep/Dec)

Core STA engine is FROZEN. This file is additive / informational only.
"""

import os
import requests
import logging
from datetime import date, datetime, timedelta

logger = logging.getLogger(__name__)

FRED_API_KEY = os.environ.get('FRED_API_KEY')
FRED_BASE_URL = 'https://api.stlouisfed.org/fred/series/observations'

# ─── FOMC 2026–2027 hardcoded dates ─────────────────────────────────────────
FOMC_DATES = [
    date(2026, 1, 28), date(2026, 3, 18), date(2026, 5, 6),  date(2026, 6, 17),
    date(2026, 7, 29), date(2026, 9, 16), date(2026, 11, 4), date(2026, 12, 16),
    date(2027, 1, 27), date(2027, 3, 17), date(2027, 5, 5),  date(2027, 6, 16),
    date(2027, 7, 28), date(2027, 9, 15), date(2027, 11, 3), date(2027, 12, 15),
]


# ─── FRED helper ─────────────────────────────────────────────────────────────
def _fetch_fred(series_id: str, limit: int = 13):
    """Fetch FRED series observations, newest first. Returns list of (date, value) tuples."""
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
                pass  # skip "." missing values
        return result
    except Exception as e:
        logger.warning(f"FRED fetch failed for {series_id}: {e}")
        return None


# ─── Calendar helpers ─────────────────────────────────────────────────────────
def _next_fomc(from_date: date):
    """Next FOMC date on or after from_date."""
    for d in FOMC_DATES:
        if d >= from_date:
            return d
    return None


def _next_quad_witching(from_date: date):
    """3rd Friday of Mar, Jun, Sep, Dec — on or after from_date."""
    for year in [from_date.year, from_date.year + 1]:
        for month in [3, 6, 9, 12]:
            first = date(year, month, 1)
            # weekday() 4 = Friday
            days_to_first_fri = (4 - first.weekday()) % 7
            third_friday = first + timedelta(days=days_to_first_fri + 14)
            if third_friday >= from_date:
                return third_friday
    return None


def _presidential_year(today: date):
    """
    2025 = Year 1 (Trump 47th term), 2026 = Year 2, 2027 = Year 3, 2028 = Year 4.
    Cycles every 4 years from 2025.
    """
    year_in_cycle = ((today.year - 2025) % 4) + 1
    return year_in_cycle


def _seasonal_regime(today: date):
    """Nov–Apr = FAVORABLE (Best 6 months), May–Oct = NEUTRAL."""
    return 'FAVORABLE' if today.month in [11, 12, 1, 2, 3, 4] else 'NEUTRAL'


# ─── Card builders ────────────────────────────────────────────────────────────
def _yield_curve_card(today: date):
    data = _fetch_fred('T10Y2Y', limit=5)
    if data:
        _, val = data[0]
        if val >= 0.5:
            regime = 'FAVORABLE'
            phase = 'Normal · Steepening ↑' if len(data) >= 2 and val > data[1][1] else 'Normal'
        elif val >= 0.0:
            regime = 'NEUTRAL'
            phase = 'Flat curve'
        else:
            regime = 'ADVERSE'
            phase = f'Inverted — recession risk'
        value_str = f'{val:+.2f}%'
        raw_value = val
    else:
        regime = 'NEUTRAL'
        phase = 'Data unavailable'
        value_str = 'N/A'
        raw_value = None

    return {
        'name': 'Yield Curve',
        'icon': '📈',
        'value': value_str,
        'phase': phase,
        'source': 'FRED T10Y2Y',
        'series_id': 'T10Y2Y',
        'history': 'Avg S&P +13.2%/yr when normal (>0.5%)',
        'regime': regime,
        'raw_value': raw_value,
    }


def _business_cycle_card(today: date):
    data = _fetch_fred('INDPRO', limit=3)
    if data and len(data) >= 2:
        latest = data[0][1]
        prev = data[1][1]
        mom_pct = ((latest - prev) / prev) * 100 if prev else 0.0
        if mom_pct > 0.2:
            regime = 'FAVORABLE'
            phase = f'INDPRO {latest:.1f} · +{mom_pct:.2f}% MoM · Expanding'
        elif mom_pct >= -0.1:
            regime = 'NEUTRAL'
            phase = f'INDPRO {latest:.1f} · {mom_pct:+.2f}% MoM · Plateau'
        else:
            regime = 'ADVERSE'
            phase = f'INDPRO {latest:.1f} · {mom_pct:.2f}% MoM · Contracting'
        raw_value = mom_pct
    else:
        regime = 'NEUTRAL'
        phase = 'Data unavailable'
        raw_value = None

    return {
        'name': 'Business Cycle',
        'icon': '🏭',
        'value': phase.split('·')[0].strip() if data else 'N/A',
        'phase': phase,
        'source': 'FRED INDPRO',
        'series_id': 'INDPRO',
        'history': 'PMI proxy — watch for sustained contraction',
        'regime': regime,
        'raw_value': raw_value,
    }


def _presidential_year_card(today: date):
    yr = _presidential_year(today)
    q = (today.month - 1) // 3 + 1
    labels = {1: 'NEUTRAL', 2: 'ADVERSE', 3: 'FAVORABLE', 4: 'FAVORABLE'}
    avg_returns = {1: '+6.5%', 2: '+3.3%', 3: '+19.8%', 4: '+7.5%'}
    regime = labels[yr]
    avg = avg_returns[yr]
    phase_desc = {1: 'honeymoon yr', 2: 'weakest yr', 3: 'pre-election yr (strongest)', 4: 'election yr'}

    return {
        'name': 'Presidential Year',
        'icon': '🏛️',
        'value': f'Year {yr} of 4 · Q{q}',
        'phase': phase_desc[yr],
        'source': 'Calendar computed',
        'series_id': None,
        'history': f'Year {yr} avg: S&P {avg}/yr historically',
        'regime': regime,
        'raw_value': yr,
    }


def _seasonal_card(today: date):
    regime = _seasonal_regime(today)
    if today.month in [11, 12, 1, 2, 3, 4]:
        season_name = 'Strong Season (Nov–Apr)'
        days_to_may = (date(today.year + (1 if today.month >= 5 else 0), 5, 1) - today).days
        phase = f'Best 6 months · {days_to_may} days to May'
        history = 'Avg S&P Nov–Apr historically +7.4% vs May–Oct +1.7%'
    else:
        season_name = 'Weak Season (May–Oct)'
        days_to_nov = (date(today.year + (1 if today.month >= 11 else 0), 11, 1) - today).days
        phase = f'"Sell in May" period · {days_to_nov} days to Nov'
        history = 'Historically weaker 6 months — reduced exposure justified'

    return {
        'name': 'Seasonal Regime',
        'icon': '📅',
        'value': season_name,
        'phase': phase,
        'source': 'Calendar computed',
        'series_id': None,
        'history': history,
        'regime': regime,
        'raw_value': today.month,
    }


def _fomc_card(today: date):
    next_fomc = _next_fomc(today)
    if next_fomc:
        days_away = (next_fomc - today).days
        value_str = f'Next: {next_fomc.strftime("%b %d")} · {days_away} days away'
        if 15 <= days_away <= 40:
            regime = 'FAVORABLE'
            phase = 'Ideal window — 15–40 days post-FOMC'
        elif 5 <= days_away < 15:
            regime = 'NEUTRAL'
            phase = 'Approaching FOMC — mild uncertainty'
        else:
            regime = 'ADVERSE'
            phase = f'FOMC in {days_away}d — options block active'
        raw_value = days_away
    else:
        regime = 'NEUTRAL'
        value_str = 'Date unavailable'
        phase = 'Update FOMC_DATES list'
        raw_value = None

    return {
        'name': 'FOMC Proximity',
        'icon': '🏦',
        'value': value_str,
        'phase': phase,
        'source': 'Hardcoded 2026–2027 FOMC dates',
        'series_id': None,
        'history': 'Ideal window: 15–40 days from FOMC meeting',
        'regime': regime,
        'raw_value': raw_value,
    }


def _quad_witching_card(today: date):
    next_qw = _next_quad_witching(today)
    if next_qw:
        days_away = (next_qw - today).days
        value_str = f'Next: {next_qw.strftime("%b %d")} · {days_away} days away'
        if days_away > 5:
            regime = 'FAVORABLE'
            phase = 'No pin risk on current positions'
        elif days_away >= 3:
            regime = 'NEUTRAL'
            phase = 'Approaching quad witching — mild volatility risk'
        else:
            regime = 'ADVERSE'
            phase = f'Quad witching in {days_away}d — options block active'
        raw_value = days_away
    else:
        regime = 'NEUTRAL'
        value_str = 'Calculation error'
        phase = 'Check quad witching logic'
        raw_value = None

    return {
        'name': 'Quad Witching',
        'icon': '⚡',
        'value': value_str,
        'phase': phase,
        'source': 'Computed — 3rd Fri Mar/Jun/Sep/Dec',
        'series_id': None,
        'history': 'Quad witching adds volatility within 3 days',
        'regime': regime,
        'raw_value': raw_value,
    }


# ─── Options block detection ──────────────────────────────────────────────────
def _compute_options_block(cards):
    fomc = next((c for c in cards if c['name'] == 'FOMC Proximity'), None)
    qw = next((c for c in cards if c['name'] == 'Quad Witching'), None)
    fomc_days = fomc['raw_value'] if fomc else 999
    qw_days = qw['raw_value'] if qw else 999
    block_active = (fomc_days is not None and fomc_days < 5) or \
                   (qw_days is not None and qw_days < 3)
    reason = None
    if fomc_days is not None and fomc_days < 5:
        reason = f'FOMC in {fomc_days} day(s)'
    elif qw_days is not None and qw_days < 3:
        reason = f'Quad Witching in {qw_days} day(s)'
    return {'has_options_block': block_active, 'reason': reason}


# ─── Main entry point ─────────────────────────────────────────────────────────
def get_cycles():
    """
    Returns 6 cycle cards with regime assessments.
    Column A data — global, no ticker needed.
    """
    today = date.today()

    cards = [
        _yield_curve_card(today),
        _business_cycle_card(today),
        _presidential_year_card(today),
        _seasonal_card(today),
        _fomc_card(today),
        _quad_witching_card(today),
    ]

    regimes = [c['regime'] for c in cards]
    summary = {
        'favorable': regimes.count('FAVORABLE'),
        'neutral': regimes.count('NEUTRAL'),
        'adverse': regimes.count('ADVERSE'),
    }

    options_block = _compute_options_block(cards)

    return {
        'cards': cards,
        'options_block': options_block,
        'summary': summary,
        'timestamp': datetime.now().isoformat(),
        'fred_available': FRED_API_KEY is not None,
    }
