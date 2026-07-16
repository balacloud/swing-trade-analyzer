"""
market_phase_engine.py — N4: Market Phase Synthesis
Day 76 research, Day 87 build, v4.45

Synthesizes SPY trend structure + VIX fear level into one of 5 phases
(Bull Rally / Late Bull / Distribution / Correction / Recovery), using
breadth (RSP/SPY ratio) and sector leadership (Growth vs Defensive ETFs)
as supporting context rather than additional gates. Keeping the primary
classification a transparent 3x3 grid (SPY trend bucket x VIX level
bucket) avoids stacking many tuned thresholds for a purely informational
feature (same simplicity principle as Golden Rule 16's equal-weighting).

Core STA engine is FROZEN. This file is additive / informational only —
zero impact on verdict, scoring, or Trade Setup.

Data: SPY + ^VIX + RSP via the existing DataProvider OHLCV chain (no new
data sources). Sector ETFs via yfinance batch download, same pattern as
backend.py's get_sector_rotation().
"""

import traceback
from datetime import datetime

import yfinance as yf

try:
    from providers import get_data_provider
    DATA_PROVIDER_AVAILABLE = True
except ImportError:
    DATA_PROVIDER_AVAILABLE = False

GROWTH_ETFS = ['XLK', 'XLY', 'XLC']       # Technology, Consumer Discretionary, Communication
DEFENSIVE_ETFS = ['XLU', 'XLP', 'XLV']    # Utilities, Consumer Staples, Health Care

PHASE_DESCRIPTIONS = {
    'Bull Rally': 'SPY above its 200-day average and trending up, VIX calm and falling — broad risk-on conditions.',
    'Late Bull': 'SPY still above its 200-day average but momentum slowing, or VIX creeping up — uptrend intact but maturing.',
    'Distribution': 'SPY topping or flattening while VIX rises — a classic profit-taking/distribution signature, not yet a breakdown.',
    'Correction': 'SPY below its 200-day average with elevated or high VIX — active downtrend.',
    'Recovery': 'SPY below its 200-day average but bouncing off recent lows with VIX calming down — early recovery attempt, not yet confirmed.',
}


def _normalize_index(df):
    """yfinance returns tz-aware indices, TwelveData/cache can be naive —
    strip tz so cross-ticker date alignment doesn't silently drop rows
    (Golden Rule: Day 52 timezone normalization lesson)."""
    if df is None or df.empty:
        return df
    if df.index.tz is not None:
        df = df.copy()
        df.index = df.index.tz_localize(None)
    return df


def _pct_change_n(series, n):
    """% change over the trailing n bars. None if insufficient history."""
    if series is None or len(series) <= n:
        return None
    try:
        start = float(series.iloc[-1 - n])
        end = float(series.iloc[-1])
        if start == 0:
            return None
        return round(((end / start) - 1) * 100, 2)
    except (IndexError, ValueError, ZeroDivisionError):
        return None


def _spy_bucket(above_200, chg_20d):
    if above_200 and chg_20d is not None and chg_20d > 2:
        return 'UP'
    if above_200:
        return 'FLAT'
    return 'DOWN'


def _vix_bucket(vix_current):
    if vix_current < 20:
        return 'CALM'
    if vix_current < 25:
        return 'ELEVATED'
    return 'HIGH'


def _sector_leadership():
    """20-trading-day simple return, Growth ETFs average minus Defensive
    ETFs average. Returns (growth_ret, defensive_ret, differential, label);
    all None if the batch fetch fails (non-fatal — sector context is
    supporting evidence only, not a classification gate)."""
    try:
        tickers = GROWTH_ETFS + DEFENSIVE_ETFS
        data = yf.download(tickers, period='2mo', progress=False, group_by='ticker')
        if data is None or data.empty:
            return None, None, None, 'Unknown'

        def _ret_20d(etf):
            try:
                close = data[etf]['Close'].dropna()
                return _pct_change_n(close, 20)
            except (KeyError, TypeError):
                return None

        growth_rets = [r for r in (_ret_20d(e) for e in GROWTH_ETFS) if r is not None]
        defensive_rets = [r for r in (_ret_20d(e) for e in DEFENSIVE_ETFS) if r is not None]

        if not growth_rets or not defensive_rets:
            return None, None, None, 'Unknown'

        growth_avg = round(sum(growth_rets) / len(growth_rets), 2)
        defensive_avg = round(sum(defensive_rets) / len(defensive_rets), 2)
        differential = round(growth_avg - defensive_avg, 2)

        if differential > 5:
            label = 'Growth leading'
        elif differential < -5:
            label = 'Defensive leading'
        else:
            label = 'Mixed'

        return growth_avg, defensive_avg, differential, label
    except Exception as e:
        print(f"⚠️ market_phase_engine: sector leadership fetch failed: {e}")
        return None, None, None, 'Unknown'


def get_market_phase():
    """
    Returns a dict with the classified phase, the raw signals behind it,
    and a human-readable description. Never raises — returns
    {'error': ...} on failure so the endpoint can 503 cleanly.
    """
    if not DATA_PROVIDER_AVAILABLE:
        return {'error': 'DataProvider not available'}

    try:
        dp = get_data_provider()

        spy = _normalize_index(dp.get_ohlcv('SPY', '2y'))
        vix = _normalize_index(dp.get_ohlcv('^VIX', '3mo'))
        rsp = _normalize_index(dp.get_ohlcv('RSP', '2y'))

        if spy is None or spy.empty or len(spy) < 200:
            return {'error': 'Insufficient SPY history for 200-day SMA'}
        if vix is None or vix.empty:
            return {'error': 'VIX data unavailable'}
        if rsp is None or rsp.empty:
            return {'error': 'RSP data unavailable'}

        spy_close = spy['close']
        latest_close = float(spy_close.iloc[-1])
        latest_sma200 = float(spy_close.rolling(200).mean().iloc[-1])
        above_200 = latest_close > latest_sma200
        spy_chg_20d = _pct_change_n(spy_close, 20)

        recent_low_20d = float(spy_close.tail(20).min())
        spy_off_low = round(((latest_close / recent_low_20d) - 1) * 100, 2) if recent_low_20d > 0 else None

        vix_close = vix['close']
        latest_vix = round(float(vix_close.iloc[-1]), 2)
        vix_chg_10d = _pct_change_n(vix_close, 10)

        common_idx = spy_close.index.intersection(rsp['close'].index)
        breadth_chg_20d = None
        latest_ratio = None
        if len(common_idx) > 20:
            ratio = rsp['close'].loc[common_idx] / spy_close.loc[common_idx]
            breadth_chg_20d = _pct_change_n(ratio, 20)
            latest_ratio = round(float(ratio.iloc[-1]), 4)

        if breadth_chg_20d is not None and breadth_chg_20d > 2:
            breadth_label = 'Rising (broadening)'
        elif breadth_chg_20d is not None and breadth_chg_20d < -2:
            breadth_label = 'Falling (narrowing)'
        elif breadth_chg_20d is not None:
            breadth_label = 'Flat'
        else:
            breadth_label = 'Unknown'

        growth_ret, defensive_ret, sector_differential, sector_label = _sector_leadership()

        spy_bucket = _spy_bucket(above_200, spy_chg_20d)
        vix_bucket = _vix_bucket(latest_vix)

        phase_grid = {
            ('UP', 'CALM'): 'Bull Rally',
            ('UP', 'ELEVATED'): 'Late Bull',
            ('UP', 'HIGH'): 'Distribution',
            ('FLAT', 'CALM'): 'Late Bull',
            ('FLAT', 'ELEVATED'): 'Distribution',
            ('FLAT', 'HIGH'): 'Distribution',
            ('DOWN', 'ELEVATED'): 'Correction',
            ('DOWN', 'HIGH'): 'Correction',
        }

        phase = phase_grid.get((spy_bucket, vix_bucket))
        if phase is None:
            # DOWN + CALM is ambiguous by the grid alone — refine with
            # whether price is actually bouncing off its recent low and
            # VIX is falling (Recovery), vs. a slow bleed with no bounce
            # yet (still Correction).
            bouncing = spy_off_low is not None and spy_off_low >= 5
            vix_falling = vix_chg_10d is not None and vix_chg_10d < 0
            phase = 'Recovery' if (bouncing and vix_falling) else 'Correction'

        return {
            'phase': phase,
            'description': PHASE_DESCRIPTIONS[phase],
            'signals': {
                'spy': {
                    'close': round(latest_close, 2),
                    'sma200': round(latest_sma200, 2),
                    'aboveSma200': above_200,
                    'pctChange20d': spy_chg_20d,
                    'pctOffRecentLow20d': spy_off_low,
                    'trendBucket': spy_bucket,
                },
                'vix': {
                    'current': latest_vix,
                    'pctChange10d': vix_chg_10d,
                    'levelBucket': vix_bucket,
                },
                'breadth': {
                    'rspSpyRatio': latest_ratio,
                    'pctChange20d': breadth_chg_20d,
                    'label': breadth_label,
                },
                'sectors': {
                    'growthReturn20d': growth_ret,
                    'defensiveReturn20d': defensive_ret,
                    'differential': sector_differential,
                    'label': sector_label,
                },
            },
            'asOf': spy.index[-1].strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat(),
        }

    except Exception as e:
        print(f"❌ market_phase_engine.get_market_phase error: {e}")
        traceback.print_exc()
        return {'error': str(e)}
