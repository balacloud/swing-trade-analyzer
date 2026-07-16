"""
Shared TradingView Screener Query Builders

Day 81: factored out of backend.py's /api/scan/tradingview route so both
the live Scan tab AND the automated paper-trading engine
(backend/paper_trading/live_signals.py) use the exact same Config C
candidate logic — one implementation, not two that can silently drift
(Golden Rule 19's lesson applied here proactively).

Behavior-preserving extraction: build_best_query()/parse_candidates() below
reproduce backend.py's original strategy='best' branch exactly.
"""
try:
    from tradingview_screener import Query, col
    TRADINGVIEW_AVAILABLE = True
except ImportError:
    TRADINGVIEW_AVAILABLE = False

INDEX_MAP = {
    'sp500': 'SYML:SP;SPX',
    'nasdaq100': 'SYML:NASDAQ;NDX',
    'dow30': 'SYML:DJ;DJI',
    'tsx60': 'SYML:TSX;TX60',
}
CANADIAN_MARKETS = {'tsx60', 'canada'}
CANADIAN_EXCHANGES = ['TSX', 'TSXV', 'NEO']
US_EXCHANGES = ['NYSE', 'NASDAQ', 'AMEX']


def _safe_float(value, default=None):
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return float(value.item())
        return float(value)
    except (TypeError, ValueError):
        return default


def _safe_int(value, default=None):
    try:
        if value is None:
            return default
        if hasattr(value, 'item'):
            return int(value.item())
        return int(value)
    except (TypeError, ValueError):
        return default


def build_best_query(limit=50, market_index='all'):
    """
    Config C-matching momentum query (Day 55, v4.16): price>SMA50>SMA200,
    ADX>=20, RSI 50-70, EMA10>EMA21, positive 52W performance, RVOL>=1.

    Returns (query, is_canadian) — query is unexecuted; call
    query.get_scanner_data() to run it.
    """
    is_canadian = market_index in CANADIAN_MARKETS
    valid_exchanges = CANADIAN_EXCHANGES if is_canadian else US_EXCHANGES

    query = Query()
    if market_index in INDEX_MAP:
        query = query.set_index(INDEX_MAP[market_index])
    elif market_index == 'canada':
        query = query.set_markets('canada')
    else:
        query = query.set_markets('america')

    query = query.select(
        'name', 'close', 'volume', 'market_cap_basic',
        'price_52_week_high', 'price_52_week_low',
        'SMA50', 'SMA200', 'RSI', 'relative_volume_10d_calc',
        'sector', 'change', 'exchange',
        'ADX', 'EMA10', 'EMA21', 'Perf.Y'
    )

    query = query.where(
        col('exchange').isin(valid_exchanges),
        col('market_cap_basic') >= 2_000_000_000,
        col('close') > col('SMA50'),
        col('SMA50') > col('SMA200'),
        col('ADX') >= 20,
        col('RSI') >= 50,
        col('RSI') <= 70,
        col('EMA10') > col('EMA21'),
        col('Perf.Y') > 0,
        col('relative_volume_10d_calc') >= 1.0
    )
    query = query.order_by('ADX', ascending=False)
    query = query.limit(limit)
    return query, is_canadian


def parse_candidates(results, is_canadian, strategy='best'):
    """
    Row cleanup identical to scan_tradingview(): strips exchange prefix,
    drops preferred/warrant/SPAC-unit tickers and commodity trusts, appends
    .TO for Canadian names, computes pctFromHigh, and (strategy='best')
    drops anything more than 25% below the 52-week high.
    """
    candidates = []
    for _, row in results.iterrows():
        try:
            ticker = row.get('ticker', '')
            exchange_prefix = ''
            if ':' in str(ticker):
                exchange_prefix = str(ticker).split(':')[0]
                ticker = str(ticker).split(':')[-1]

            if '/' in ticker:
                continue  # Preferred stock (e.g., BAC/PL, KKR/PD)
            if len(ticker) >= 4 and ticker.endswith('U'):
                continue  # SPAC unit
            if len(ticker) >= 4 and ticker.endswith('W'):
                continue  # Warrant
            if len(ticker) >= 5 and ticker.endswith('WS'):
                continue  # Warrant series
            if len(ticker) >= 5 and ticker[-1] in 'PMNOL' and ticker[-2].isupper():
                continue  # Preferred stock series
            if ticker in ['PHYS', 'PSLV', 'GLD', 'SLV', 'IAU', 'GLDM', 'SGOL', 'SIVR']:
                continue  # Commodity trusts

            if is_canadian and exchange_prefix == 'TSX' and not ticker.endswith('.TO'):
                ticker = ticker + '.TO'

            current = row.get('close')
            high52w = row.get('price_52_week_high')
            pct_from_high = None
            if current and high52w and high52w > 0:
                pct_from_high = round(((current - high52w) / high52w) * 100, 1)

            if strategy == 'best' and pct_from_high is not None and pct_from_high < -25:
                continue

            # Day 87: avg dollar volume — 10d avg share volume * price, since
            # TradingView has no direct dollar-volume field.
            adv_10d = row.get('average_volume_10d_calc')
            avg_dollar_volume = None
            if current and adv_10d:
                avg_dollar_volume = current * adv_10d

            if strategy == 'breakout':
                if pct_from_high is None or pct_from_high < -8:
                    continue
                if avg_dollar_volume is None or avg_dollar_volume < 5_000_000:
                    continue

            candidates.append({
                'ticker': ticker,
                'name': row.get('name', ''),
                'price': _safe_float(row.get('close')),
                'change': _safe_float(row.get('change')),
                'volume': _safe_int(row.get('volume')),
                'marketCap': _safe_int(row.get('market_cap_basic')),
                'high52w': _safe_float(row.get('price_52_week_high')),
                'low52w': _safe_float(row.get('price_52_week_low')),
                'sma50': _safe_float(row.get('SMA50')),
                'sma200': _safe_float(row.get('SMA200')),
                'rsi': _safe_float(row.get('RSI')),
                'relativeVolume': _safe_float(row.get('relative_volume_10d_calc')),
                'sector': row.get('sector', 'N/A'),
                'pctFromHigh': pct_from_high,
                'exchange': row.get('exchange', 'N/A'),
                'adx': _safe_float(row.get('ADX')),
                'ema10': _safe_float(row.get('EMA10')),
                'ema21': _safe_float(row.get('EMA21')),
                'perf52w': _safe_float(row.get('Perf.Y')),
                'avgDollarVolume': _safe_float(avg_dollar_volume),
            })
        except Exception as e:
            print(f"scan_queries.parse_candidates: error parsing row: {e}")
            continue
    return candidates
