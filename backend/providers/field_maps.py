"""
Field Normalization Maps - v4.14 Multi-Source Data Intelligence

Each provider returns data with different field names.
These maps translate raw API fields to our canonical FUNDAMENTALS_SCHEMA.

Format: { 'canonical_name': ('raw_api_field', transform_function) }
Transform is applied to the raw value. Use None for identity (no transform).
"""

import math


def _is_nan(val):
    """Check if value is NaN (handles float, numpy, and pandas NaN)"""
    try:
        return math.isnan(float(val))
    except (TypeError, ValueError):
        return False


def _pct_to_decimal(val):
    """Convert percentage (25.0) to decimal (0.25) if > 1"""
    if val is None or _is_nan(val):
        return None
    try:
        v = float(val)
        return v / 100.0 if abs(v) > 1 else v
    except (TypeError, ValueError):
        return None


def _growth_to_pct(val):
    """Convert growth decimal (0.15) to percentage (15.0).
    APIs (FMP, yfinance) return growth as decimals. Categorical assessment expects percentages.
    Uses abs(v) < 5 heuristic: values in [-5, 5] are treated as decimals (up to 500% growth)."""
    if val is None or _is_nan(val):
        return None
    try:
        v = float(val)
        return round(v * 100, 2) if abs(v) < 5 else round(v, 2)
    except (TypeError, ValueError):
        return None


def _identity(val):
    """Pass-through - no transformation"""
    if val is None or _is_nan(val):
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _to_int(val):
    """Convert to integer (for marketCap)"""
    if val is None or _is_nan(val):
        return None
    try:
        return int(float(val))
    except (TypeError, ValueError):
        return None


# =============================================================================
# FINNHUB FUNDAMENTALS MAP
# Source: GET /stock/metric?metric=all → response['metric']
# =============================================================================

FINNHUB_FUNDAMENTALS = {
    'pe':               ('peTTM', _identity),
    'forwardPe':        ('peBasicExclExtraTTM', _identity),
    'pegRatio':         ('pegRatio', _identity),
    'marketCap':        ('marketCapitalization', lambda v: _to_int(v * 1_000_000) if v else None),
    'roe':              ('roeTTM', _identity),          # Already percentage
    'roa':              ('roaTTM', _identity),          # Already percentage
    'roic':             ('roicTTM', _identity),         # Already percentage
    'epsGrowth':        (None, None),                   # NOT available in Finnhub
    'revenueGrowth':    (None, None),                   # NOT available in Finnhub
    'debtToEquity':     ('totalDebt/totalEquityQuarterly', _identity),
    'profitMargin':     ('netProfitMarginTTM', _pct_to_decimal),
    'operatingMargin':  ('operatingMarginTTM', _pct_to_decimal),
    'beta':             ('beta', _identity),
    'dividendYield':    ('dividendYieldIndicatedAnnual', _pct_to_decimal),
}


# =============================================================================
# FMP (Financial Modeling Prep) FUNDAMENTALS MAP
# Source: GET /key-metrics-ttm/{ticker} → response[0]
# =============================================================================

FMP_FUNDAMENTALS = {
    'pe':               ('peRatioTTM', _identity),
    'forwardPe':        (None, None),
    'pegRatio':         ('pegRatioTTM', _identity),
    'marketCap':        ('marketCapTTM', _to_int),
    'roe':              ('roeTTM', lambda v: v * 100 if v and not _is_nan(v) and abs(v) < 1 else (None if v is None or _is_nan(v) else v)),
    'roa':              ('returnOnTangibleAssetsTTM', lambda v: v * 100 if v and not _is_nan(v) and abs(v) < 1 else (None if v is None or _is_nan(v) else v)),
    'roic':             ('roicTTM', lambda v: v * 100 if v and not _is_nan(v) and abs(v) < 1 else (None if v is None or _is_nan(v) else v)),
    'epsGrowth':        (None, None),                   # Comes from /financial-growth endpoint
    'revenueGrowth':    (None, None),                   # Comes from /financial-growth endpoint
    'debtToEquity':     ('debtToEquityTTM', _identity),
    'profitMargin':     ('netProfitMarginTTM', _identity),  # Already decimal
    'operatingMargin':  ('operatingProfitMarginTTM', _identity),
    'beta':             (None, None),
    'dividendYield':    ('dividendYieldTTM', _identity),
}


# =============================================================================
# FMP GROWTH MAP
# Source: GET /financial-growth/{ticker}?period=annual&limit=1 → response[0]
# These fill the gaps Finnhub leaves (epsGrowth, revenueGrowth)
# =============================================================================

FMP_GROWTH = {
    'epsGrowth':        ('epsgrowth', _growth_to_pct),       # Decimal → Percentage (0.15 → 15.0)
    'revenueGrowth':    ('revenueGrowth', _growth_to_pct),   # Decimal → Percentage (0.10 → 10.0)
}


# =============================================================================
# YFINANCE FUNDAMENTALS MAP
# Source: yf.Ticker(ticker).info dict
# =============================================================================

YFINANCE_FUNDAMENTALS = {
    'pe':               ('trailingPE', _identity),
    'forwardPe':        ('forwardPE', _identity),
    'pegRatio':         ('pegRatio', _identity),
    'marketCap':        ('marketCap', _to_int),
    'roe':              ('returnOnEquity', lambda v: v * 100 if v and not _is_nan(v) and abs(v) < 1 else (None if v is None or _is_nan(v) else v)),
    'roa':              ('returnOnAssets', lambda v: v * 100 if v and not _is_nan(v) and abs(v) < 1 else (None if v is None or _is_nan(v) else v)),
    'roic':             (None, None),                   # Not in yfinance
    'epsGrowth':        ('earningsGrowth', _growth_to_pct),  # Decimal → Percentage (0.15 → 15.0)
    'revenueGrowth':    ('revenueGrowth', _growth_to_pct),   # Decimal → Percentage (0.10 → 10.0)
    'debtToEquity':     ('debtToEquity', _identity),
    'profitMargin':     ('profitMargins', _identity),   # Already decimal
    'operatingMargin':  ('operatingMargins', _identity),
    'beta':             ('beta', _identity),
    'dividendYield':    ('dividendYield', _identity),
}


# =============================================================================
# YFINANCE STOCK INFO MAP
# Source: yf.Ticker(ticker).info dict
# =============================================================================

YFINANCE_STOCK_INFO = {
    'name':             ('shortName', None),
    'sector':           ('sector', None),
    'industry':         ('industry', None),
    'fiftyTwoWeekHigh': ('fiftyTwoWeekHigh', _identity),
    'fiftyTwoWeekLow':  ('fiftyTwoWeekLow', _identity),
    'avgVolume':        ('averageVolume', _to_int),
    'avgVolume10d':     ('averageVolume10days', _to_int),
}


# =============================================================================
# HELPER: Apply field map to raw data
# =============================================================================

def apply_field_map(raw_data: dict, field_map: dict) -> dict:
    """
    Apply a field map to normalize raw API data to canonical fields.

    Args:
        raw_data: Raw API response dict
        field_map: Mapping of canonical_name -> (raw_field, transform_fn)

    Returns:
        Dict with canonical field names and transformed values
    """
    result = {}
    for canonical_name, mapping in field_map.items():
        if mapping is None or mapping[0] is None:
            result[canonical_name] = None
            continue

        raw_field, transform = mapping
        raw_value = raw_data.get(raw_field)

        if raw_value is None:
            result[canonical_name] = None
        elif transform is not None:
            try:
                result[canonical_name] = transform(raw_value)
            except Exception:
                result[canonical_name] = None
        else:
            result[canonical_name] = raw_value

    return result
