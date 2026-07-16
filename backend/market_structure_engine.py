"""
market_structure_engine.py — Price Structure Card Phase 2
Day 72 spec (PRICE_STRUCTURE_CARD_SPEC.md), Day 87 build, v4.45

HH/HL/LH/LL market structure classification (Uptrend/Downtrend/Range/
Transition), trend age, and volume-behavior-at-levels — enriches the
existing Price Structure Card narrative with a structural read beyond
Trend Template's binary Stage-2 yes/no.

Deliberately NOT reusing support_resistance.py's _detect_zigzag_pivots():
that function sorts+dedupes pivots by PRICE (`sorted(list(set(...)))`),
which throws away the chronological order this classification needs to
tell HH from LH. Written as a separate, self-contained detector instead
of modifying the frozen core S&R engine — same "additive, informational
only, zero verdict impact" pattern as cycles_engine.py / mean_reversion.py.
Core STA engine (support_resistance.py) is untouched by this file.
"""

from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np


def _chronological_zigzag_pivots(
    df: pd.DataFrame,
    percent_delta: float = 0.05,
    min_bars: int = 5
) -> List[Dict[str, Any]]:
    """
    Same ZigZag algorithm as support_resistance.py's _detect_zigzag_pivots()
    (kept in sync deliberately — this is a parallel implementation, not an
    import, so the frozen core file is never touched), but preserving bar
    index and chronological insertion order instead of sorting+deduping by
    price. Returns [{'idx': int, 'type': 'high'|'low', 'price': float}, ...]
    in time order.
    """
    pivots: List[Dict[str, Any]] = []
    highs = df['high'].values
    lows = df['low'].values

    if len(highs) < min_bars * 2:
        return []

    initial_high = np.max(highs[:min_bars])
    initial_low = np.min(lows[:min_bars])

    if initial_high / initial_low - 1 > percent_delta:
        last_pivot_type = 'high'
        last_pivot_price = float(initial_high)
        last_pivot_idx = int(np.argmax(highs[:min_bars]))
        pivots.append({'idx': last_pivot_idx, 'type': 'high', 'price': last_pivot_price})
    else:
        last_pivot_type = 'low'
        last_pivot_price = float(initial_low)
        last_pivot_idx = int(np.argmin(lows[:min_bars]))
        pivots.append({'idx': last_pivot_idx, 'type': 'low', 'price': last_pivot_price})

    for i in range(min_bars, len(df)):
        current_high = highs[i]
        current_low = lows[i]

        if last_pivot_type == 'high':
            pct_change = (last_pivot_price - current_low) / last_pivot_price
            if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                pivots.append({'idx': i, 'type': 'low', 'price': float(current_low)})
                last_pivot_type = 'low'
                last_pivot_price = float(current_low)
                last_pivot_idx = i
            elif current_high > last_pivot_price:
                pivots[-1] = {'idx': i, 'type': 'high', 'price': float(current_high)}
                last_pivot_price = float(current_high)
                last_pivot_idx = i
        else:
            pct_change = (current_high - last_pivot_price) / last_pivot_price
            if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                pivots.append({'idx': i, 'type': 'high', 'price': float(current_high)})
                last_pivot_type = 'high'
                last_pivot_price = float(current_high)
                last_pivot_idx = i
            elif current_low < last_pivot_price:
                pivots[-1] = {'idx': i, 'type': 'low', 'price': float(current_low)}
                last_pivot_price = float(current_low)
                last_pivot_idx = i

    return pivots


def _classify_pivot_sequence(pivots: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Tag each pivot HH/LH (highs) or HL/LL (lows) vs. the previous pivot
    of the same type. First high and first low are unlabeled (no prior)."""
    classified = []
    last_high = None
    last_low = None
    for p in pivots:
        label = None
        if p['type'] == 'high':
            if last_high is not None:
                label = 'HH' if p['price'] > last_high else 'LH'
            last_high = p['price']
        else:
            if last_low is not None:
                label = 'HL' if p['price'] > last_low else 'LL'
            last_low = p['price']
        classified.append({**p, 'label': label})
    return classified


def _classify_structure(labeled: List[Dict[str, Any]], lookback: int = 4) -> str:
    """
    Uptrend: recent highs all HH AND recent lows all HL.
    Downtrend: recent highs all LH AND recent lows all LL.
    Transition: the single most recent pivot breaks an otherwise-consistent
    prior trend (early warning, not yet a confirmed reversal).
    Range: anything else mixed/sideways.
    """
    with_labels = [p for p in labeled if p['label'] is not None]
    if len(with_labels) < 2:
        return 'Insufficient Data'

    recent = with_labels[-lookback:]
    recent_highs = [p['label'] for p in recent if p['type'] == 'high']
    recent_lows = [p['label'] for p in recent if p['type'] == 'low']

    all_hh = bool(recent_highs) and all(l == 'HH' for l in recent_highs)
    all_hl = bool(recent_lows) and all(l == 'HL' for l in recent_lows)
    all_lh = bool(recent_highs) and all(l == 'LH' for l in recent_highs)
    all_ll = bool(recent_lows) and all(l == 'LL' for l in recent_lows)

    if all_hh and all_hl:
        return 'Uptrend'
    if all_lh and all_ll:
        return 'Downtrend'

    prior = recent[:-1]
    prior_highs = [p['label'] for p in prior if p['type'] == 'high']
    prior_lows = [p['label'] for p in prior if p['type'] == 'low']
    was_uptrend = bool(prior_highs) and bool(prior_lows) and \
        all(l == 'HH' for l in prior_highs) and all(l == 'HL' for l in prior_lows)
    was_downtrend = bool(prior_highs) and bool(prior_lows) and \
        all(l == 'LH' for l in prior_highs) and all(l == 'LL' for l in prior_lows)

    last = recent[-1]
    broke_up_to_down = was_uptrend and last['label'] in ('LH', 'LL')
    broke_down_to_up = was_downtrend and last['label'] in ('HH', 'HL')

    if broke_up_to_down or broke_down_to_up:
        return 'Transition'
    return 'Range'


def _trend_age_bars(labeled: List[Dict[str, Any]], current_idx: int) -> Optional[int]:
    """Bars since the start of the current consistent HH/HL (or LH/LL) run."""
    with_labels = [p for p in labeled if p['label'] is not None]
    if not with_labels:
        return None

    def _side(label):
        return 'up' if label in ('HH', 'HL') else 'down'

    last_side = _side(with_labels[-1]['label'])
    start_idx = with_labels[-1]['idx']
    for p in reversed(with_labels[:-1]):
        if _side(p['label']) == last_side:
            start_idx = p['idx']
        else:
            break
    return current_idx - start_idx


def _volume_behavior_at_latest_pivot(df: pd.DataFrame, pivots: List[Dict[str, Any]], window: int = 5) -> str:
    """Was volume rising or falling in the run-up to the most recent pivot?"""
    if not pivots:
        return 'Unknown'
    last_idx = pivots[-1]['idx']
    if last_idx < window * 2:
        return 'Insufficient data'
    recent_vol = df['volume'].iloc[last_idx - window:last_idx].mean()
    prior_vol = df['volume'].iloc[last_idx - 2 * window:last_idx - window].mean()
    if not prior_vol or prior_vol <= 0:
        return 'Unknown'
    chg_pct = (recent_vol / prior_vol - 1) * 100
    if chg_pct > 15:
        return 'Rising'
    if chg_pct < -15:
        return 'Falling'
    return 'Flat'


def detect_market_structure(df: pd.DataFrame, percent_delta: float = 0.05, min_bars: int = 5) -> Dict[str, Any]:
    """
    Main entry point. Never raises — returns a safe default dict on any
    failure so /api/sr/<ticker> never 500s because of this additive field.
    """
    try:
        pivots = _chronological_zigzag_pivots(df, percent_delta, min_bars)
        if len(pivots) < 3:
            return {
                'structure': 'Insufficient Data',
                'trendAgeBars': None,
                'volumeBehavior': 'Unknown',
                'recentPivots': [],
            }

        labeled = _classify_pivot_sequence(pivots)
        structure = _classify_structure(labeled)
        trend_age = _trend_age_bars(labeled, len(df) - 1)
        volume_behavior = _volume_behavior_at_latest_pivot(df, pivots)

        return {
            'structure': structure,
            'trendAgeBars': trend_age,
            'volumeBehavior': volume_behavior,
            'recentPivots': [
                {'type': p['type'], 'price': round(p['price'], 2), 'label': p['label']}
                for p in labeled[-8:]
            ],
        }
    except Exception as e:
        print(f"⚠️ market_structure_engine.detect_market_structure error: {e}")
        return {
            'structure': 'Unknown',
            'trendAgeBars': None,
            'volumeBehavior': 'Unknown',
            'recentPivots': [],
            'error': str(e),
        }
