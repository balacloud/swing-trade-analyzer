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


def build_mr_universe_query(limit=150):
    """
    Day 88: broad liquid-universe candidate pool for the automated paper
    trading engine's MR arm, replacing the previous hardcoded 54-name
    DEFAULT_MR_UNIVERSE. This is a breadth change only, not a threshold
    change — the actual MR entry gate (RSI(2)<10, price>$10, 20d ADV>$25M)
    is still enforced per-ticker by mean_reversion.detect_mr_signal()
    downstream; this query is just a cheap pre-filter so the daily job
    doesn't waste cycles fetching obviously-illiquid penny stocks.

    limit=150 (not larger) is a measured constraint, not an arbitrary
    choice: a live test at limit=300 (~231 parsed tickers) tripped
    TwelveData's rate limiter partway through, which opened its circuit
    breaker and cascaded to yfinance/Tradier too — ~35% of that run's
    tickers failed on ALL providers, not because they lacked a signal.
    Since results are ordered by market_cap_basic descending, that failure
    always hits the SAME tail-end tickers, not a rotating sample — a
    silent, deterministic gap. limit=150 is calibrated to what actually
    completed cleanly in that test.

    Same market-wide breadth pattern as build_best_query() for the
    momentum arm — no re-tuning of any frozen threshold in
    PAPER_TRADING_PREREGISTRATION.md, which locks entry/exit rules, not
    universe size.

    Returns (query, is_canadian) — query is unexecuted.
    """
    query = Query()
    query = query.set_markets('america')
    query = query.select('close', 'market_cap_basic', 'average_volume_10d_calc', 'exchange')
    query = query.where(
        col('exchange').isin(US_EXCHANGES),
        col('market_cap_basic') >= 500_000_000,
        col('close') > 5,
    )
    query = query.order_by('market_cap_basic', ascending=False)
    query = query.limit(limit)
    return query, False


# Day 102 (SRPS Gate 0 prereq): TradingView's coarse `sector` screener field
# buckets ALL Real Estate Investment Trusts under 'Finance' — verified live
# against 9 known XLRE holdings (PLD, AMT, EQIX, SPG, O, PSA, WELL, DLR,
# VTR), all returned sector='Finance', none returned 'Real Estate'. Same
# field genuinely does distinguish 'Major Banks'/'Regional Banks' from REITs,
# just one level down, in TradingView's finer-grained `industry` field.
# SECTOR_ETF_MAP['XLRE']['gics'] = ['Real Estate'] (backend.py) is therefore
# a dead value for any TradingView-screener sector-field query — nothing
# before this file ever filtered TradingView's screener BY sector (existing
# code only ever SELECTS 'sector' as a display column), so this gap was
# latent and undetected until build_sector_query() below became the first
# caller to actually filter on it. Not a bug in SECTOR_ETF_MAP itself (its
# 'Real Estate' value is correct GICS/yfinance terminology, which the
# Analyze page's sector badge uses instead, via yfinance's own .info
# sector field, a different taxonomy that does NOT have this problem) —
# it's a gap specific to sourcing candidates from TradingView's screener.
REAL_ESTATE_TV_INDUSTRY_VALUES = ['Real Estate Investment Trusts', 'Real Estate Development']

# Day 102 (SRPS Gate 0 prereq): Communication Services (XLC) has no clean
# sector- OR industry-field fix, unlike Real Estate above. Live-checked:
# GOOGL/META/NFLX land in TradingView's 'Technology Services' sector with
# industry='Internet Software/Services' — a value ALSO shared with genuine
# GICS Technology names (VRSN, CSGP, IT). TTWO lands in industry='Packaged
# Software' — ALSO shared with MSFT/ADBE/CRM/ORCL and 30+ other real
# Technology names. DIS/CMCSA/WBD/FOXA land in sector='Consumer Services'
# — shared with genuine Consumer Discretionary names. TradingView's
# SIC-based taxonomy simply doesn't partition GICS Communication Services
# from Technology/Consumer Discretionary at any field granularity this
# screener exposes — filtering by field value can't work here, at any
# threshold. Only telecom carriers (T/VZ/TMUS) land cleanly in XLC's own
# 'Communications' sector bucket.
#
# XLC is also one of GICS's newest (2018) and smallest S&P 500 sectors —
# a hand-curated list is the honest fix, not a workaround, since no field
# combination will ever cleanly separate it. Live-verified against the
# real S&P 500 index membership (set_index('SYML:SP;SPX')) on 2026-08-07:
# EA (Electronic Arts), IPG (Interpublic Group), and MTCH (Match Group)
# were in earlier hand-drafts of this list but are NOT currently found —
# EA appears to have gone private, IPG appears to have merged into OMC
# (both plausible real 2025-2026 corporate actions), MTCH is no longer an
# S&P 500 constituent. Re-verify this list periodically (GICS
# reclassifications and index reconstitution do happen, just rarely for
# this sector) rather than trusting it indefinitely.
XLC_OVERRIDE_TICKERS = [
    'GOOGL', 'GOOG', 'META', 'NFLX', 'DIS', 'TMUS', 'CMCSA', 'WBD',
    'T', 'VZ', 'TTWO', 'FOXA', 'FOX', 'NWSA', 'NWS', 'OMC', 'LYV',
]


def build_sector_query(sector_values=None, limit=30, market_index='sp500', min_market_cap=2_000_000_000,
                        field='sector', tickers=None, require_above_sma200=True):
    """
    SRPS Gate 0 prerequisite #2 (design doc v1.2, Section 3: "top 3 RS
    names per Improving sector"): candidates filtered to ONE sector's
    GICS/TradingView sector-name variants (pass backend.py's
    SECTOR_ETF_MAP[etf]['gics'] list for 10 of the 11 broad sectors — see
    REAL_ESTATE_TV_INDUSTRY_VALUES above for the XLRE exception, which
    must be called with field='industry' instead), scoped to real S&P 500
    constituents via query.set_index() (same INDEX_MAP mechanism
    build_best_query() already uses for market_index='sp500' — verified
    live to return exactly 503 rows, the real index membership count, not
    just a market-cap-sized proxy for it). Also requires price above the
    200-day SMA (cheap pre-filter for Rule 3's own trend-confirmation
    condition, so OHLCV isn't fetched downstream for names that would
    fail it anyway).

    An earlier version of this query used only a $2B market-cap floor
    instead of set_index() — live-tested and found to admit thin,
    non-index names (e.g. small-float tech tickers) that don't match the
    design doc's intent ("leaders of the recovery... institutions
    accumulating"). set_index() is the correct fix, not a market-cap
    threshold tune.

    Does NOT rank by relative strength. TradingView's screener has no
    native "RS vs SPY" column — the closest, Perf.Y, is raw trailing
    performance, not a ratio to SPY, so it's used only as a rough
    pre-filter ordering here. True 3-month RS-vs-SPY ranking (the actual
    formula Rule 3 specifies) happens downstream in Python against real
    OHLCV — see rank_candidates_by_rs() below.

    Pass tickers=XLC_OVERRIDE_TICKERS (and leave sector_values/field
    alone) for Communication Services — see the comment above
    XLC_OVERRIDE_TICKERS for why no field-based filter works for that one
    sector. When tickers is given, sector_values/field are ignored
    entirely; the query filters by name membership instead.

    require_above_sma200=False drops the trend pre-filter entirely — for
    building a raw SECTOR MEMBERSHIP list (e.g. Gate 0's historical
    replay, which needs every constituent regardless of today's SMA200
    status, since Rule 3's trend condition gets evaluated per historical
    day, not just today). Leave it True for live signal sourcing, where
    "today's" SMA200 status is exactly what you want to pre-filter on.

    Returns (query, is_canadian) — query is unexecuted, matches the
    existing build_*_query() convention. is_canadian is always False;
    SRPS's SPDR sector universe is US-only.
    """
    query = Query()
    if market_index in INDEX_MAP:
        query = query.set_index(INDEX_MAP[market_index])
    else:
        query = query.set_markets('america')
    query = query.select(
        'name', 'close', 'volume', 'market_cap_basic',
        'SMA50', 'SMA200', 'sector', 'industry', 'change', 'exchange',
        'average_volume_10d_calc', 'Perf.Y'
    )
    sector_filter = col('name').isin(tickers) if tickers else col(field).isin(sector_values)
    where_clauses = [
        col('exchange').isin(US_EXCHANGES),
        sector_filter,
        col('market_cap_basic') >= min_market_cap,
    ]
    if require_above_sma200:
        where_clauses.append(col('close') > col('SMA200'))
    query = query.where(*where_clauses)
    query = query.order_by('Perf.Y', ascending=False)
    query = query.limit(limit)
    return query, False


def rank_candidates_by_rs(tickers, spy_close=None, lookback_days=63, top_n=3):
    """
    True 3-month (~63 trading day) relative-strength-vs-SPY ranking, per
    SRPS Rule 3's actual spec ("3-month RS ratio vs SPY >= 0.9").
    TradingView's screener has no equivalent column, so this fetches real
    OHLCV via a single batch yfinance call — not one call per candidate,
    same batch-not-per-ticker pattern backend.py's get_sector_rotation()
    already uses, per Golden Rule 25's rate-limit lesson — and computes
    RS = (1 + stock's lookback_days return) / (1 + SPY's lookback_days
    return), the same shape as backend/backtest/backtest_holistic.py's
    calculate_rs_52w(), just at a 3-month lookback instead of 52-week.

    Returns a list of {ticker, rsRatio} sorted descending, length top_n.
    """
    import yfinance as yf

    if not tickers:
        return []

    if spy_close is None:
        spy_data = yf.download(['SPY'], period='4mo', progress=False, group_by='ticker')
        spy_close = spy_data['SPY']['Close'].dropna()

    data = yf.download(list(tickers), period='4mo', progress=False, group_by='ticker')
    if data is None or data.empty:
        return []

    ranked = []
    for t in tickers:
        try:
            close = data[t]['Close'].dropna()
            common_idx = spy_close.index.intersection(close.index)
            if len(common_idx) < lookback_days + 1:
                continue
            common_idx = common_idx[-(lookback_days + 1):]
            stock_aligned = close.loc[common_idx]
            spy_aligned = spy_close.loc[common_idx]

            stock_ret = float(stock_aligned.iloc[-1] / stock_aligned.iloc[0] - 1)
            spy_ret = float(spy_aligned.iloc[-1] / spy_aligned.iloc[0] - 1)
            rs_ratio = (1 + stock_ret) / (1 + spy_ret)
            ranked.append({'ticker': t, 'rsRatio': round(rs_ratio, 3)})
        except Exception as e:
            print(f"rank_candidates_by_rs: skipping {t}: {e}")
            continue

    ranked.sort(key=lambda x: x['rsRatio'], reverse=True)
    return ranked[:top_n]


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
