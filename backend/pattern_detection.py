"""
Pattern Detection Module - v1.0
Detects swing trading chart patterns: VCP, Cup-and-Handle, Flat Base

Day 44: Initial implementation for v4.2 Pattern Detection

References:
- VCP: Mark Minervini's Volatility Contraction Pattern
- Cup & Handle: William O'Neil's CANSLIM methodology
- Flat Base: Consolidation after strong uptrend
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from scipy.signal import argrelextrema


def to_python_types(obj):
    """
    Recursively convert numpy types to Python native types for JSON serialization.
    """
    if isinstance(obj, dict):
        return {k: to_python_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_python_types(item) for item in obj]
    elif isinstance(obj, np.bool_):
        return bool(obj)
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif hasattr(obj, 'item'):  # Catch any other numpy scalar types
        return obj.item()
    else:
        return obj


def calculate_sma(prices: pd.Series, period: int) -> pd.Series:
    """Calculate Simple Moving Average."""
    return prices.rolling(window=period).mean()


def calculate_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Average True Range."""
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()


def find_pivot_points(prices: pd.Series, order: int = 5) -> Tuple[List[int], List[int]]:
    """
    Find local highs and lows in price series.

    Parameters
    ----------
    prices : pd.Series
        Price series to analyze
    order : int
        Number of points on each side to compare (default 5)

    Returns
    -------
    Tuple of (pivot_highs_indices, pivot_lows_indices)
    """
    # Find local maxima (pivot highs)
    highs_idx = argrelextrema(prices.values, np.greater_equal, order=order)[0]

    # Find local minima (pivot lows)
    lows_idx = argrelextrema(prices.values, np.less_equal, order=order)[0]

    return list(highs_idx), list(lows_idx)


def check_trend_template(df: pd.DataFrame) -> Dict:
    """
    Check Mark Minervini's Trend Template criteria.

    The 8 criteria for a stock in a Stage 2 uptrend:
    1. Current price above 50-day SMA
    2. Current price above 150-day SMA
    3. Current price above 200-day SMA
    4. 50-day SMA above 150-day SMA
    5. 150-day SMA above 200-day SMA
    6. 200-day SMA trending up for at least 1 month
    7. Current price at least 30% above 52-week low
    8. Current price within 25% of 52-week high

    Returns
    -------
    dict with each criterion result and overall score
    """
    if len(df) < 252:  # Need 1 year of data
        return None

    close = df['Close']
    current_price = close.iloc[-1]

    # Calculate SMAs
    sma_50 = calculate_sma(close, 50).iloc[-1]
    sma_150 = calculate_sma(close, 150).iloc[-1]
    sma_200 = calculate_sma(close, 200).iloc[-1]
    sma_200_30d_ago = calculate_sma(close, 200).iloc[-31] if len(df) > 230 else None

    # 52-week high/low
    high_52w = df['High'].tail(252).max()
    low_52w = df['Low'].tail(252).min()

    # Check criteria
    criteria = {
        'above_50sma': current_price > sma_50,
        'above_150sma': current_price > sma_150,
        'above_200sma': current_price > sma_200,
        'sma_50_above_150': sma_50 > sma_150,
        'sma_150_above_200': sma_150 > sma_200,
        'sma_200_trending_up': sma_200 > sma_200_30d_ago if sma_200_30d_ago else False,
        'above_30pct_52w_low': current_price >= low_52w * 1.30,
        'within_25pct_52w_high': current_price >= high_52w * 0.75
    }

    criteria_met = sum(criteria.values())

    return {
        'criteria': criteria,
        'criteria_met': criteria_met,
        'total_criteria': 8,
        'trend_template_score': round(criteria_met / 8 * 100, 1),
        'in_stage2_uptrend': criteria_met >= 7,
        'sma_values': {
            'sma_50': round(sma_50, 2),
            'sma_150': round(sma_150, 2),
            'sma_200': round(sma_200, 2)
        },
        'price_position': {
            'current': round(current_price, 2),
            'high_52w': round(high_52w, 2),
            'low_52w': round(low_52w, 2),
            'pct_from_high': round((current_price / high_52w - 1) * 100, 1),
            'pct_from_low': round((current_price / low_52w - 1) * 100, 1)
        }
    }


def detect_vcp(df: pd.DataFrame, lookback_days: int = 90) -> Dict:
    """
    Detect Volatility Contraction Pattern (VCP) - Mark Minervini's pattern.

    VCP Characteristics:
    - 2-6 price contractions
    - Each contraction smaller than the previous
    - Volume declining during contractions
    - Tight pivot area forms (base tightness)

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data with at least lookback_days of history
    lookback_days : int
        Number of days to look back for pattern (default 90)

    Returns
    -------
    dict with VCP detection results
    """
    if len(df) < lookback_days:
        return {'detected': False, 'confidence': 0, 'reason': 'Insufficient data'}

    # Use recent data for VCP detection
    recent = df.tail(lookback_days).copy()
    close = recent['Close']
    high = recent['High']
    low = recent['Low']
    volume = recent['Volume']

    # Find pivot highs and lows
    pivot_highs_idx, pivot_lows_idx = find_pivot_points(close, order=5)

    if len(pivot_highs_idx) < 2 or len(pivot_lows_idx) < 2:
        return {'detected': False, 'confidence': 0, 'reason': 'Not enough pivot points'}

    # Calculate contractions (pullback depths)
    contractions = []

    for i in range(len(pivot_highs_idx)):
        high_idx = pivot_highs_idx[i]
        high_price = high.iloc[high_idx]

        # Find next low after this high
        lows_after = [l for l in pivot_lows_idx if l > high_idx]
        if not lows_after:
            continue

        low_idx = lows_after[0]
        low_price = low.iloc[low_idx]

        # Calculate pullback depth
        pullback_pct = round((high_price - low_price) / high_price * 100, 1)

        if pullback_pct > 3:  # Only count meaningful pullbacks
            contractions.append({
                'high_idx': high_idx,
                'low_idx': low_idx,
                'high_price': round(high_price, 2),
                'low_price': round(low_price, 2),
                'depth_pct': pullback_pct,
                'date': recent.index[low_idx].strftime('%Y-%m-%d') if hasattr(recent.index[low_idx], 'strftime') else str(recent.index[low_idx])
            })

    if len(contractions) < 2:
        return {'detected': False, 'confidence': 0, 'reason': 'Fewer than 2 contractions found'}

    # Check if contractions are decreasing (VCP characteristic)
    depths = [c['depth_pct'] for c in contractions[-4:]]  # Use last 4 contractions max
    decreasing_contractions = all(depths[i] >= depths[i+1] for i in range(len(depths)-1))

    # Calculate volatility compression
    early_volatility = close.iloc[:lookback_days//3].std()
    late_volatility = close.iloc[-lookback_days//3:].std()
    volatility_contracting = late_volatility < early_volatility

    # Calculate base tightness (price range in last 10 days)
    last_10d = df.tail(10)
    base_tightness = (last_10d['High'].max() - last_10d['Low'].min()) / last_10d['Close'].mean() * 100
    tight_base = base_tightness < 10  # Less than 10% range is tight

    # Check volume pattern (should be declining)
    early_volume = volume.iloc[:lookback_days//2].mean()
    late_volume = volume.iloc[-lookback_days//4:].mean()
    volume_declining = late_volume < early_volume

    # Calculate pivot price (highest point in pattern)
    pivot_price = high.max()

    # Determine VCP status
    vcp_detected = (
        len(contractions) >= 2 and
        (decreasing_contractions or volatility_contracting) and
        tight_base
    )

    # Calculate confidence score
    confidence = 0
    if len(contractions) >= 2:
        confidence += 25
    if len(contractions) >= 3:
        confidence += 15
    if decreasing_contractions:
        confidence += 25
    if volatility_contracting:
        confidence += 15
    if tight_base:
        confidence += 15
    if volume_declining:
        confidence += 5

    # Determine status
    current_price = close.iloc[-1]
    if current_price > pivot_price:
        status = 'broken_out'
    elif current_price > pivot_price * 0.97:
        status = 'at_pivot'
    else:
        status = 'forming'

    return {
        'detected': vcp_detected,
        'confidence': min(confidence, 100),
        'contractions_count': len(contractions),
        'contractions': contractions[-4:],  # Return last 4
        'decreasing_depths': decreasing_contractions,
        'volatility_contracting': volatility_contracting,
        'base_tightness_pct': round(base_tightness, 1),
        'tight_base': tight_base,
        'volume_declining': volume_declining,
        'pivot_price': round(pivot_price, 2),
        'current_price': round(current_price, 2),
        'distance_to_pivot_pct': round((pivot_price - current_price) / current_price * 100, 1),
        'status': status,
        'description': f"VCP with {len(contractions)} contractions" if vcp_detected else "No VCP pattern detected"
    }


def detect_cup_handle(df: pd.DataFrame, lookback_days: int = 180) -> Dict:
    """
    Detect Cup and Handle pattern - William O'Neil's classic pattern.

    Cup & Handle Characteristics:
    - U-shaped cup (not V-shaped)
    - Cup depth typically 12-35%
    - Handle forms in upper half of cup
    - Handle depth less than cup depth
    - Handle should be 1-4 weeks long

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data with at least lookback_days of history
    lookback_days : int
        Number of days to look back (default 180 for ~6 months)

    Returns
    -------
    dict with cup and handle detection results
    """
    if len(df) < lookback_days:
        return {'detected': False, 'confidence': 0, 'reason': 'Insufficient data'}

    recent = df.tail(lookback_days).copy()
    close = recent['Close']
    high = recent['High']
    low = recent['Low']

    # Find the cup structure
    # Cup left lip: local high at the start
    # Cup bottom: lowest point
    # Cup right lip: local high approaching the left lip level

    # Find pivot points
    pivot_highs_idx, pivot_lows_idx = find_pivot_points(close, order=10)

    if len(pivot_highs_idx) < 2 or len(pivot_lows_idx) < 1:
        return {'detected': False, 'confidence': 0, 'reason': 'Insufficient pivot points for cup pattern'}

    # Find potential cup structure
    # Left lip should be in first third, bottom in middle, right lip in last third
    first_third = lookback_days // 3
    last_third = lookback_days * 2 // 3

    # Find left lip (highest high in first third)
    left_lip_idx = high.iloc[:first_third].idxmax()
    left_lip_price = high.loc[left_lip_idx]
    left_lip_pos = recent.index.get_loc(left_lip_idx)

    # Find cup bottom (lowest low after left lip)
    after_left = low.iloc[left_lip_pos+5:]  # At least 5 days after left lip
    if len(after_left) < 10:
        return {'detected': False, 'confidence': 0, 'reason': 'Not enough data after left lip'}

    cup_bottom_idx = after_left.idxmin()
    cup_bottom_price = low.loc[cup_bottom_idx]
    cup_bottom_pos = recent.index.get_loc(cup_bottom_idx)

    # Cup depth calculation
    cup_depth_pct = (left_lip_price - cup_bottom_price) / left_lip_price * 100

    # Check if cup depth is in valid range (12-35%)
    valid_cup_depth = 12 <= cup_depth_pct <= 35

    # Find right lip (highest high after bottom)
    after_bottom = high.iloc[cup_bottom_pos+5:]
    if len(after_bottom) < 10:
        return {'detected': False, 'confidence': 0, 'reason': 'Not enough data for cup right side'}

    right_lip_idx = after_bottom.idxmax()
    right_lip_price = high.loc[right_lip_idx]
    right_lip_pos = recent.index.get_loc(right_lip_idx)

    # Check if right lip is close to left lip level (within 5%)
    lips_aligned = abs(right_lip_price - left_lip_price) / left_lip_price < 0.05

    # Check for U-shape (bottom should be rounded, not V-shaped)
    # U-shape: time from left to bottom ≈ time from bottom to right
    left_to_bottom = cup_bottom_pos - left_lip_pos
    bottom_to_right = right_lip_pos - cup_bottom_pos

    # Ratio should be between 0.5 and 2.0 for U-shape
    if left_to_bottom > 0 and bottom_to_right > 0:
        symmetry_ratio = left_to_bottom / bottom_to_right
        u_shaped = 0.5 <= symmetry_ratio <= 2.0
    else:
        u_shaped = False

    # Look for handle (small pullback after right lip)
    handle_data = df.iloc[right_lip_pos:]
    if len(handle_data) < 5:
        handle_detected = False
        handle_info = None
    else:
        handle_low = handle_data['Low'].min()
        handle_high = handle_data['High'].max()
        handle_depth_pct = (right_lip_price - handle_low) / right_lip_price * 100

        # Handle should be shallow (less than half of cup depth)
        handle_valid = handle_depth_pct < cup_depth_pct / 2 and handle_depth_pct < 15
        handle_in_upper_half = handle_low > (cup_bottom_price + left_lip_price) / 2

        handle_detected = handle_valid and handle_in_upper_half
        handle_info = {
            'depth_pct': round(handle_depth_pct, 1),
            'valid': handle_valid,
            'in_upper_half': handle_in_upper_half,
            'days': len(handle_data)
        }

    # Calculate pivot/breakout price
    pivot_price = max(left_lip_price, right_lip_price)

    # Determine pattern detection
    cup_detected = (
        valid_cup_depth and
        u_shaped and
        lips_aligned
    )

    pattern_complete = cup_detected and handle_detected

    # Calculate confidence
    confidence = 0
    if valid_cup_depth:
        confidence += 25
    if u_shaped:
        confidence += 25
    if lips_aligned:
        confidence += 20
    if handle_detected:
        confidence += 20
    if handle_info and handle_info.get('in_upper_half'):
        confidence += 10

    # Determine status
    current_price = close.iloc[-1]
    if current_price > pivot_price * 1.01:  # 1% breakout
        status = 'broken_out'
    elif pattern_complete:
        status = 'complete'
    elif cup_detected:
        status = 'cup_formed'
    else:
        status = 'not_detected'

    return {
        'detected': cup_detected,
        'pattern_complete': pattern_complete,
        'confidence': min(confidence, 100),
        'cup': {
            'left_lip_price': round(left_lip_price, 2),
            'bottom_price': round(cup_bottom_price, 2),
            'right_lip_price': round(right_lip_price, 2),
            'depth_pct': round(cup_depth_pct, 1),
            'valid_depth': valid_cup_depth,
            'u_shaped': u_shaped,
            'lips_aligned': lips_aligned,
            'duration_days': right_lip_pos - left_lip_pos
        },
        'handle': handle_info,
        'pivot_price': round(pivot_price, 2),
        'current_price': round(current_price, 2),
        'distance_to_pivot_pct': round((pivot_price - current_price) / current_price * 100, 1),
        'status': status,
        'description': f"Cup & Handle {'complete' if pattern_complete else 'forming'}" if cup_detected else "No cup and handle pattern detected"
    }


def detect_flat_base(df: pd.DataFrame, min_weeks: int = 5, lookback_days: int = 90) -> Dict:
    """
    Detect Flat Base pattern - consolidation after strong uptrend.

    Flat Base Characteristics:
    - Prior uptrend of 30%+ before consolidation
    - Minimum 5 weeks of consolidation
    - Price movement within tight range (10-15%)
    - Price above rising 50-day MA
    - Volume declining during consolidation

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data
    min_weeks : int
        Minimum weeks for flat base (default 5)
    lookback_days : int
        Days to look back (default 90)

    Returns
    -------
    dict with flat base detection results
    """
    min_consolidation_days = min_weeks * 5  # Trading days

    if len(df) < lookback_days + 60:  # Need extra data for prior uptrend
        return {'detected': False, 'confidence': 0, 'reason': 'Insufficient data'}

    # Get recent data for flat base detection
    recent = df.tail(lookback_days).copy()
    close = recent['Close']
    high = recent['High']
    low = recent['Low']
    volume = recent['Volume']

    # Check for prior uptrend (30%+ move in 3-6 months before consolidation)
    pre_base = df.iloc[-(lookback_days + 90):-lookback_days]
    if len(pre_base) < 30:
        return {'detected': False, 'confidence': 0, 'reason': 'Insufficient prior data'}

    pre_base_low = pre_base['Low'].min()
    pre_base_high = pre_base['High'].max()
    prior_uptrend_pct = (pre_base_high - pre_base_low) / pre_base_low * 100
    has_prior_uptrend = prior_uptrend_pct >= 30

    # Calculate base range (should be tight, 10-15%)
    base_high = high.max()
    base_low = low.min()
    base_range_pct = (base_high - base_low) / base_low * 100
    tight_range = base_range_pct <= 15

    # Check if most of base is above 50-day MA
    sma_50 = calculate_sma(df['Close'], 50)
    recent_sma_50 = sma_50.tail(lookback_days)
    days_above_50ma = (close > recent_sma_50).sum()
    mostly_above_50ma = days_above_50ma / len(close) >= 0.7  # 70%+ above

    # Check if 50-day MA is rising
    sma_50_start = recent_sma_50.iloc[0] if len(recent_sma_50) > 0 else 0
    sma_50_end = recent_sma_50.iloc[-1] if len(recent_sma_50) > 0 else 0
    ma_50_rising = sma_50_end > sma_50_start

    # Check volume pattern (should be declining)
    first_half_vol = volume.iloc[:len(volume)//2].mean()
    second_half_vol = volume.iloc[-len(volume)//4:].mean()
    volume_declining = second_half_vol < first_half_vol

    # Calculate base flatness (standard deviation of close prices)
    price_std = close.std()
    price_mean = close.mean()
    flatness_pct = price_std / price_mean * 100
    is_flat = flatness_pct < 5  # Less than 5% standard deviation is flat

    # Determine if flat base detected
    flat_base_detected = (
        has_prior_uptrend and
        tight_range and
        (mostly_above_50ma or ma_50_rising) and
        is_flat
    )

    # Calculate breakout price (highest point in base)
    pivot_price = base_high

    # Calculate confidence
    confidence = 0
    if has_prior_uptrend:
        confidence += 25
    if tight_range:
        confidence += 25
    if is_flat:
        confidence += 20
    if mostly_above_50ma:
        confidence += 15
    if volume_declining:
        confidence += 10
    if ma_50_rising:
        confidence += 5

    # Determine status
    current_price = close.iloc[-1]
    if current_price > pivot_price * 1.01:
        status = 'broken_out'
    elif flat_base_detected:
        status = 'forming'
    else:
        status = 'not_detected'

    return {
        'detected': flat_base_detected,
        'confidence': min(confidence, 100),
        'prior_uptrend': {
            'pct': round(prior_uptrend_pct, 1),
            'has_30pct_move': has_prior_uptrend
        },
        'base': {
            'high': round(base_high, 2),
            'low': round(base_low, 2),
            'range_pct': round(base_range_pct, 1),
            'tight_range': tight_range,
            'flatness_pct': round(flatness_pct, 1),
            'is_flat': is_flat,
            'days': len(recent)
        },
        'ma_analysis': {
            'above_50ma_pct': round(days_above_50ma / len(close) * 100, 1),
            'mostly_above_50ma': mostly_above_50ma,
            'ma_50_rising': ma_50_rising
        },
        'volume_declining': volume_declining,
        'pivot_price': round(pivot_price, 2),
        'current_price': round(current_price, 2),
        'distance_to_pivot_pct': round((pivot_price - current_price) / current_price * 100, 1),
        'status': status,
        'description': f"Flat base with {round(base_range_pct, 1)}% range" if flat_base_detected else "No flat base pattern detected"
    }


def detect_patterns(df: pd.DataFrame) -> Dict:
    """
    Main pattern detection function that runs all pattern detectors.

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data with sufficient history (ideally 1 year)

    Returns
    -------
    dict containing all pattern detection results
    """
    if df is None or len(df) < 60:
        return {
            'error': 'Insufficient data for pattern detection',
            'patterns': {},
            'trend_template': None
        }

    # Run Minervini's Trend Template check
    trend_template = check_trend_template(df)

    # Run pattern detections
    vcp_result = detect_vcp(df, lookback_days=90)
    cup_handle_result = detect_cup_handle(df, lookback_days=180)
    flat_base_result = detect_flat_base(df, min_weeks=5, lookback_days=90)

    # Summary of patterns found
    patterns_detected = []
    if vcp_result.get('detected'):
        patterns_detected.append('VCP')
    if cup_handle_result.get('detected'):
        patterns_detected.append('Cup & Handle')
    if flat_base_result.get('detected'):
        patterns_detected.append('Flat Base')

    # Best pattern (highest confidence)
    all_patterns = [
        ('VCP', vcp_result),
        ('Cup & Handle', cup_handle_result),
        ('Flat Base', flat_base_result)
    ]

    detected_patterns = [(name, result) for name, result in all_patterns if result.get('detected')]
    best_pattern = max(detected_patterns, key=lambda x: x[1].get('confidence', 0)) if detected_patterns else None

    result = {
        'patterns': {
            'vcp': vcp_result,
            'cup_handle': cup_handle_result,
            'flat_base': flat_base_result
        },
        'summary': {
            'patterns_detected': patterns_detected,
            'count': len(patterns_detected),
            'best_pattern': best_pattern[0] if best_pattern else None,
            'best_confidence': best_pattern[1].get('confidence', 0) if best_pattern else 0
        },
        'trend_template': trend_template,
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Convert numpy types to Python native types for JSON serialization
    return to_python_types(result)
