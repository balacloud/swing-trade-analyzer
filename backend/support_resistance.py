"""
Support & Resistance Engine for Swing Trade Analyzer
Multi-method S/R calculation with failover logic

Methods:
1. Pivot-Based (Primary) - Local highs/lows detection
2. Agglomerative Clustering (Day 30) - Adaptive price level bands
3. KMeans Clustering (Deprecated) - Fixed cluster count (fallback only)
4. Volume Profile (Tertiary) - High-volume zones as magnets

Day 13: Integrated into Swing Trade Analyzer backend
Day 14: Fixed ATH edge case - project resistance when price > all historical levels
Day 20: Fixed ATR always calculated for pivot method
Day 22: Added Option D trade viability assessment (Minervini-aligned)
Day 30: Replaced KMeans with AgglomerativeClustering
        - ZigZag pivot detection (filters noise, 5% threshold)
        - Adaptive cluster count via distance_threshold
        - Touch-based level scoring
        - 80% -> 87%+ detection rate expected
Day 32: Added Multi-Timeframe Confluence
        - Computes S&R on daily + weekly timeframes
        - Confluence = level appears on both timeframes (stronger)
        - Research shows 3.2x stronger predictive power
        - New meta fields: mtf.weekly_support, mtf.weekly_resistance, mtf.confluence_map
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Literal, Tuple

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
import logging


logger = logging.getLogger(__name__)


class SRFailure(Exception):
    """Raised when support/resistance levels cannot be computed."""


@dataclass
class SRConfig:
    """Configuration for the Support & Resistance engine."""
    min_bars: int = 150  # minimum candles required
    pivot_left: int = 5
    pivot_right: int = 5
    pivot_max_levels: int = 5
    pivot_min_spacing_frac: float = 0.0025  # 0.25% of price
    kmeans_clusters: int = 5
    volatility_window: int = 3
    volatility_threshold: float = 0.08  # 8% avg move over window
    volume_bins: int = 40
    atr_period: int = 14  # ATR period for projection
    atr_multipliers: Tuple[float, ...] = (1.0, 1.5, 2.0)  # Multipliers for projected levels
    # Day 30: Agglomerative clustering config
    merge_percent: float = 0.02  # 2% of price - merge threshold for clustering
    zigzag_percent_delta: float = 0.05  # 5% min change for ZigZag pivot
    min_touches_for_level: int = 2  # Minimum touches to consider level valid
    touch_threshold: float = 0.005  # 0.5% of price = "touch"
    use_agglomerative: bool = True  # Feature flag: use agglomerative instead of kmeans
    # Day 32: Multi-Timeframe Confluence config
    use_mtf: bool = True  # Feature flag: enable multi-timeframe confluence
    mtf_confluence_threshold: float = 0.015  # 1.5% = levels are "confluent" (Day 34: tuned from 0.5%)
    mtf_daily_weight: float = 0.6  # Weight for daily S&R levels
    mtf_weekly_weight: float = 0.4  # Weight for weekly S&R levels
    # Day 33: Fibonacci Extensions config
    use_fibonacci: bool = True  # Feature flag: use Fibonacci extensions for ATH stocks
    fib_extensions: Tuple[float, ...] = (1.272, 1.618, 2.0)  # Fibonacci extension levels
    ath_threshold: float = 0.05  # 5% - within this distance of 52w high = "near ATH"


@dataclass
class SRLevels:
    """Container for support & resistance levels."""
    method: Literal["pivot", "kmeans", "agglomerative", "volume_profile"]
    support: List[float] = field(default_factory=list)
    resistance: List[float] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)


def _check_data_integrity(df: pd.DataFrame, cfg: SRConfig) -> None:
    required_cols = {"open", "high", "low", "close", "volume"}
    missing = required_cols - set(df.columns)
    if missing:
        raise SRFailure(f"Missing required columns: {missing}")

    if df.empty:
        raise SRFailure("Empty DataFrame")

    if len(df) < cfg.min_bars:
        raise SRFailure(f"Not enough data: {len(df)} bars, need at least {cfg.min_bars}")

    nulls = df[["open", "high", "low", "close"]].isnull().sum().sum()
    if nulls > 0:
        logger.warning("Found %d null OHLC values; forward-filling.", nulls)
        # FIX: Use ffill() instead of deprecated fillna(method="ffill")
        df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].ffill()


def _calculate_atr(df: pd.DataFrame, period: int = 14) -> float:
    """
    Calculate Average True Range (ATR) for volatility-based projections.
    
    ATR = Average of True Range over N periods
    True Range = max(high - low, abs(high - prev_close), abs(low - prev_close))
    """
    try:
        high = df["high"].values
        low = df["low"].values
        close = df["close"].values
        
        # Calculate True Range
        tr1 = high - low
        tr2 = np.abs(high[1:] - close[:-1])
        tr3 = np.abs(low[1:] - close[:-1])
        
        # True Range is max of the three
        tr = np.zeros(len(df))
        tr[0] = high[0] - low[0]  # First bar: just high - low
        tr[1:] = np.maximum(np.maximum(tr1[1:], tr2), tr3)
        
        # ATR is the rolling average of True Range
        atr = np.mean(tr[-period:])
        
        return float(atr)
    except Exception as exc:
        logger.warning("ATR calculation failed: %s", exc)
        # Fallback: use 2% of current price
        return float(df["close"].iloc[-1] * 0.02)


def _project_resistance_levels(
    current_price: float, 
    atr: float, 
    multipliers: Tuple[float, ...] = (1.0, 1.5, 2.0)
) -> List[float]:
    """
    Project resistance levels above current price using ATR.
    
    Used when stock is at/near ATH and no historical resistance exists.
    
    Parameters
    ----------
    current_price : float
        Current stock price
    atr : float
        Average True Range
    multipliers : tuple
        ATR multipliers for projection (default: 1x, 1.5x, 2x)
    
    Returns
    -------
    List[float]
        Projected resistance levels
    """
    projected = [round(current_price + (m * atr), 2) for m in multipliers]
    return projected


def _project_support_levels(
    current_price: float, 
    atr: float, 
    multipliers: Tuple[float, ...] = (1.0, 1.5, 2.0)
) -> List[float]:
    """
    Project support levels below current price using ATR.
    
    Used when stock is at/near 52-week low and no historical support exists.
    
    Parameters
    ----------
    current_price : float
        Current stock price
    atr : float
        Average True Range
    multipliers : tuple
        ATR multipliers for projection (default: 1x, 1.5x, 2x)
    
    Returns
    -------
    List[float]
        Projected support levels
    """
    projected = [round(current_price - (m * atr), 2) for m in multipliers]
    # Filter out negative values
    projected = [p for p in projected if p > 0]
    return sorted(projected)


def _is_near_ath(
    current_price: float,
    fifty_two_week_high: float,
    threshold: float = 0.05
) -> bool:
    """
    Day 33: Check if stock is near all-time high (within threshold).

    Parameters
    ----------
    current_price : float
        Current stock price
    fifty_two_week_high : float
        52-week high price
    threshold : float
        Percentage threshold (default 5%)

    Returns
    -------
    bool
        True if within threshold of ATH
    """
    if fifty_two_week_high <= 0:
        return False
    distance_from_ath = (fifty_two_week_high - current_price) / fifty_two_week_high
    return distance_from_ath <= threshold


def _find_recent_swing_low(
    df: pd.DataFrame,
    lookback_days: int = 60
) -> Optional[float]:
    """
    Day 33: Find the most recent significant swing low for Fibonacci calculation.

    Uses the lowest low in the lookback period as the swing low.
    For more sophisticated detection, could use ZigZag pivots.

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data
    lookback_days : int
        Number of days to look back (default 60)

    Returns
    -------
    Optional[float]
        Recent swing low price, or None if not found
    """
    try:
        if len(df) < lookback_days:
            lookback_days = len(df)

        recent_data = df.tail(lookback_days)
        swing_low = float(recent_data['low'].min())

        return swing_low
    except Exception:
        return None


def _project_fibonacci_resistance(
    ath_price: float,
    swing_low: float,
    extensions: Tuple[float, ...] = (1.272, 1.618, 2.0)
) -> List[float]:
    """
    Day 33: Project resistance levels using Fibonacci extensions.

    Fibonacci extensions are calculated from a swing low to ATH:
    - 127.2% = ATH + 0.272 * (ATH - SwingLow)
    - 161.8% = ATH + 0.618 * (ATH - SwingLow)
    - 200.0% = ATH + 1.0 * (ATH - SwingLow)

    Research basis (TrendSpider 2023):
    - 127.2%: 68% accuracy (conservative target)
    - 161.8%: 72% accuracy (primary target)
    - 200.0%: 65% accuracy (extended target)

    Parameters
    ----------
    ath_price : float
        All-time high (or current price if at ATH)
    swing_low : float
        Recent swing low price
    extensions : tuple
        Fibonacci extension levels (default: 1.272, 1.618, 2.0)

    Returns
    -------
    List[float]
        Projected Fibonacci resistance levels
    """
    if swing_low >= ath_price:
        logger.warning("Swing low >= ATH, cannot calculate Fibonacci extensions")
        return []

    price_range = ath_price - swing_low

    # Calculate extensions: extension_level * range added to ATH
    projected = []
    for ext in extensions:
        # For 1.272 extension: ATH + 0.272 * range
        # For 1.618 extension: ATH + 0.618 * range
        # For 2.0 extension: ATH + 1.0 * range
        extension_amount = (ext - 1.0) * price_range
        level = round(ath_price + extension_amount, 2)
        projected.append(level)

    logger.info(f"Fibonacci extensions from swing low ${swing_low:.2f} to ATH ${ath_price:.2f}: {projected}")

    return projected


def _smart_project_resistance(
    current_price: float,
    df: pd.DataFrame,
    atr: float,
    cfg: SRConfig,
    fifty_two_week_high: Optional[float] = None
) -> Tuple[List[float], str]:
    """
    Day 33: Intelligently project resistance using Fibonacci or ATR.

    Decision logic:
    1. If use_fibonacci=True AND near ATH AND have swing low -> Fibonacci
    2. Otherwise -> ATR projection (fallback)

    Parameters
    ----------
    current_price : float
        Current stock price
    df : pd.DataFrame
        OHLCV data (for finding swing low)
    atr : float
        Average True Range
    cfg : SRConfig
        Configuration
    fifty_two_week_high : float, optional
        52-week high (defaults to max of df['high'])

    Returns
    -------
    Tuple[List[float], str]
        (projected_levels, method_used)
        method_used is "fibonacci" or "atr"
    """
    # Determine 52-week high
    if fifty_two_week_high is None:
        try:
            fifty_two_week_high = float(df['high'].max())
        except Exception:
            fifty_two_week_high = current_price

    # Check if we should use Fibonacci
    use_fib = (
        cfg.use_fibonacci and
        _is_near_ath(current_price, fifty_two_week_high, cfg.ath_threshold)
    )

    if use_fib:
        # Find recent swing low
        swing_low = _find_recent_swing_low(df, lookback_days=60)

        if swing_low and swing_low < current_price * 0.9:  # At least 10% below current
            # Use ATH (or current if higher) as reference
            ath_reference = max(current_price, fifty_two_week_high)
            projected = _project_fibonacci_resistance(ath_reference, swing_low, cfg.fib_extensions)

            if projected:
                logger.info(f"Using Fibonacci extensions (swing low: ${swing_low:.2f})")
                return projected, "fibonacci"

    # Fallback to ATR projection
    projected = _project_resistance_levels(current_price, atr, cfg.atr_multipliers)
    return projected, "atr"


def assess_trade_viability(
    current_price: float,
    nearest_support: Optional[float],
    nearest_resistance: Optional[float],
    atr: float
) -> Dict[str, Any]:
    """
    Assess trade viability based on Minervini's entry criteria (Option D).
    
    Minervini prefers entries where stop can be placed 8-10% below entry.
    Stocks extended >20% from support are not ideal setups.
    
    Viability Outcomes:
    - YES: Support within 10% - tight stop, full position
    - CAUTION: Support 10-20% away - wide stop, reduce size
    - NO: Support >20% away - too extended, wait for pullback
    
    Parameters
    ----------
    current_price : float
        Current stock price
    nearest_support : float or None
        Nearest support level below current price
    nearest_resistance : float or None
        Nearest resistance level above current price
    atr : float
        Average True Range for context
        
    Returns
    -------
    dict
        Viability assessment with actionable advice
    """
    result = {
        "viable": None,
        "support_distance_pct": None,
        "resistance_distance_pct": None,
        "risk_reward_context": None,
        "advice": None,
        "stop_suggestion": None,
        "stop_method": None,  # NEW: Explains how stop was calculated (structural vs ATR)
        "position_size_advice": None
    }
    
    # Calculate distances
    if nearest_support and nearest_support > 0:
        support_dist_pct = ((current_price - nearest_support) / current_price) * 100
        result["support_distance_pct"] = round(support_dist_pct, 1)
    else:
        support_dist_pct = None
        
    if nearest_resistance and nearest_resistance > current_price:
        resistance_dist_pct = ((nearest_resistance - current_price) / current_price) * 100
        result["resistance_distance_pct"] = round(resistance_dist_pct, 1)
    else:
        resistance_dist_pct = None
    
    # Calculate structural stop: swing_low - (ATR * multiplier)
    # This is market-structure based, not arbitrary percentage
    def _calc_structural_stop(support_level: float, atr_val: float, multiplier: float = 2.0) -> float:
        """Structural stop = support level - ATR buffer"""
        return round(support_level - (atr_val * multiplier), 2)

    # Assess viability based on support distance (Minervini-aligned thresholds)
    if support_dist_pct is None:
        result["viable"] = "UNKNOWN"
        result["advice"] = "No support level found - use ATR-based stop"
        result["stop_suggestion"] = round(current_price - (1.5 * atr), 2)
        result["stop_method"] = "ATR fallback (1.5×ATR below entry)"
        result["position_size_advice"] = "REDUCED - no clear support"

    elif support_dist_pct <= 10:
        # Ideal Minervini setup - tight base
        result["viable"] = "YES"
        result["advice"] = "Good setup - structural stop at swing low minus ATR buffer"
        result["stop_suggestion"] = _calc_structural_stop(nearest_support, atr, 2.0)
        result["stop_method"] = f"Structural (${nearest_support:.2f} - 2×ATR)"
        result["position_size_advice"] = "FULL - low risk entry"

    elif support_dist_pct <= 20:
        # Acceptable but requires caution
        result["viable"] = "CAUTION"
        result["advice"] = "Wide stop required - consider reducing position size or waiting for pullback"
        result["stop_suggestion"] = _calc_structural_stop(nearest_support, atr, 2.0)
        result["stop_method"] = f"Structural (${nearest_support:.2f} - 2×ATR)"
        result["position_size_advice"] = "HALF - wide stop increases risk"

    else:
        # Extended - Minervini would not enter here
        result["viable"] = "NO"
        result["advice"] = f"Extended {support_dist_pct:.0f}% from support - wait for pullback before entering"
        result["stop_suggestion"] = None  # Don't suggest a stop for non-viable trades
        result["stop_method"] = None
        result["position_size_advice"] = "NONE - do not enter"
    
    # Add R:R context if we have both levels
    if support_dist_pct and resistance_dist_pct and support_dist_pct > 0:
        # Potential reward vs risk
        rr_ratio = resistance_dist_pct / support_dist_pct
        result["risk_reward_context"] = round(rr_ratio, 2)
    
    return result


def _is_high_volatility(df: pd.DataFrame, cfg: SRConfig) -> bool:
    """Check for structural break / extreme recent volatility."""
    window = min(cfg.volatility_window, len(df) - 1)
    pct = df["close"].pct_change().tail(window).abs()
    if len(pct) == 0:
        return False
    avg = float(pct.mean())
    return avg > cfg.volatility_threshold


# ============================================
# DAY 30: AGGLOMERATIVE CLUSTERING FUNCTIONS
# ============================================

def _detect_zigzag_pivots(
    df: pd.DataFrame,
    percent_delta: float = 0.05,
    min_bars: int = 5
) -> Tuple[List[float], List[float]]:
    """
    Detect significant pivot highs and lows using ZigZag-like algorithm.

    This finds local extremes where price changed by at least percent_delta
    from the previous extreme, filtering out noise.

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data
    percent_delta : float
        Minimum percentage change to register a new pivot (default 5%)
    min_bars : int
        Minimum bars between pivots

    Returns
    -------
    Tuple[List[float], List[float]]
        (pivot_highs, pivot_lows) - Lists of significant price levels
    """
    pivot_highs: List[float] = []
    pivot_lows: List[float] = []

    try:
        highs = df["high"].values
        lows = df["low"].values

        if len(highs) < min_bars * 2:
            return [], []

        # Initialize with first extreme
        last_pivot_type = None  # 'high' or 'low'
        last_pivot_price = None
        last_pivot_idx = 0

        # Find initial direction
        initial_high = np.max(highs[:min_bars])
        initial_low = np.min(lows[:min_bars])

        if initial_high / initial_low - 1 > percent_delta:
            # Start with a high
            last_pivot_type = 'high'
            last_pivot_price = initial_high
            pivot_highs.append(float(initial_high))
        else:
            # Start with a low
            last_pivot_type = 'low'
            last_pivot_price = initial_low
            pivot_lows.append(float(initial_low))

        # Scan through data
        for i in range(min_bars, len(df)):
            current_high = highs[i]
            current_low = lows[i]

            if last_pivot_type == 'high':
                # Looking for a lower low
                pct_change = (last_pivot_price - current_low) / last_pivot_price
                if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                    # Found significant low
                    pivot_lows.append(float(current_low))
                    last_pivot_type = 'low'
                    last_pivot_price = current_low
                    last_pivot_idx = i
                elif current_high > last_pivot_price:
                    # Update the high (extension)
                    if pivot_highs:
                        pivot_highs[-1] = float(current_high)
                    last_pivot_price = current_high
                    last_pivot_idx = i
            else:
                # Looking for a higher high
                pct_change = (current_high - last_pivot_price) / last_pivot_price
                if pct_change >= percent_delta and i - last_pivot_idx >= min_bars:
                    # Found significant high
                    pivot_highs.append(float(current_high))
                    last_pivot_type = 'high'
                    last_pivot_price = current_high
                    last_pivot_idx = i
                elif current_low < last_pivot_price:
                    # Update the low (extension)
                    if pivot_lows:
                        pivot_lows[-1] = float(current_low)
                    last_pivot_price = current_low
                    last_pivot_idx = i

        # Remove duplicates and sort
        pivot_highs = sorted(list(set(pivot_highs)))
        pivot_lows = sorted(list(set(pivot_lows)))

        logger.info(f"ZigZag detected {len(pivot_highs)} highs, {len(pivot_lows)} lows")
        return pivot_highs, pivot_lows

    except Exception as exc:
        logger.exception("ZigZag pivot detection failed: %s", exc)
        return [], []


def _cluster_with_agglom(
    pivot_prices: np.ndarray,
    merge_percent: float = 0.02,
    current_price: float = None
) -> List[float]:
    """
    Cluster pivot prices using AgglomerativeClustering.

    Key difference from KMeans:
    - No need to specify n_clusters upfront
    - Uses distance threshold (merge_percent * current_price)
    - Hierarchical merging = more intuitive for price levels

    Parameters
    ----------
    pivot_prices : np.ndarray
        Array of pivot price levels to cluster
    merge_percent : float
        Percentage of current price to use as merge distance (default 2%)
    current_price : float
        Current stock price for calculating merge distance

    Returns
    -------
    List[float]
        Clustered price levels (median of each cluster)
    """
    if len(pivot_prices) < 2:
        return list(pivot_prices)

    if current_price is None:
        current_price = float(np.mean(pivot_prices))

    try:
        # Calculate adaptive merge distance
        merge_distance = current_price * merge_percent

        # Reshape for sklearn
        prices_2d = pivot_prices.reshape(-1, 1)

        # AgglomerativeClustering with distance_threshold
        clustering = AgglomerativeClustering(
            n_clusters=None,
            distance_threshold=merge_distance,
            linkage='average'
        )

        labels = clustering.fit_predict(prices_2d)

        # Extract cluster centers using median (more robust than mean)
        centers = []
        for label in set(labels):
            cluster_prices = pivot_prices[labels == label]
            centers.append(float(np.median(cluster_prices)))

        logger.info(f"Agglomerative clustering: {len(pivot_prices)} pivots -> {len(centers)} levels")
        return sorted(centers)

    except Exception as exc:
        logger.exception("Agglomerative clustering failed: %s", exc)
        return list(pivot_prices)


def _score_levels(
    levels: List[float],
    df: pd.DataFrame,
    touch_threshold: float = 0.005
) -> List[Tuple[float, int]]:
    """
    Score levels by number of price touches.

    A "touch" is when the high or low of a bar comes within touch_threshold
    of the level. More touches = stronger level.

    Parameters
    ----------
    levels : List[float]
        Price levels to score
    df : pd.DataFrame
        OHLCV data
    touch_threshold : float
        Percentage threshold for "touch" (default 0.5%)

    Returns
    -------
    List[Tuple[float, int]]
        List of (level, score) tuples, sorted by score descending
    """
    scores = []

    for level in levels:
        # Count bars where high/low within threshold of level
        upper = level * (1 + touch_threshold)
        lower = level * (1 - touch_threshold)

        # Check if high or low touched the level
        high_touch = (df['high'] >= lower) & (df['high'] <= upper)
        low_touch = (df['low'] >= lower) & (df['low'] <= upper)

        touches = int((high_touch | low_touch).sum())
        scores.append((level, touches))

    # Sort by score descending
    return sorted(scores, key=lambda x: x[1], reverse=True)


def _agglomerative_sr(
    df: pd.DataFrame,
    cfg: SRConfig
) -> Optional[Tuple[List[float], List[float], Dict[str, Any]]]:
    """
    Compute S&R levels using Agglomerative Clustering.

    This is the Day 30 replacement for _kmeans_sr:
    1. Detect ZigZag pivots (significant swings only)
    2. Cluster pivots using AgglomerativeClustering
    3. Score levels by touch count
    4. Split into support/resistance around current price

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data
    cfg : SRConfig
        Configuration including merge_percent, zigzag_percent_delta

    Returns
    -------
    Optional[Tuple[List[float], List[float], Dict[str, Any]]]
        (support, resistance, meta) or None if failed
    """
    try:
        current_price = float(df["close"].iloc[-1])
        atr = _calculate_atr(df, cfg.atr_period)

        # Step 1: Detect ZigZag pivots
        pivot_highs, pivot_lows = _detect_zigzag_pivots(
            df,
            percent_delta=cfg.zigzag_percent_delta,
            min_bars=cfg.pivot_left
        )

        all_pivots = pivot_highs + pivot_lows

        if len(all_pivots) < 2:
            logger.info("Not enough pivots for agglomerative clustering")
            return None

        # Step 2: Cluster pivots
        pivot_array = np.array(all_pivots)
        clustered_levels = _cluster_with_agglom(
            pivot_array,
            merge_percent=cfg.merge_percent,
            current_price=current_price
        )

        if not clustered_levels:
            return None

        # Step 3: Score levels by touches
        scored_levels = _score_levels(clustered_levels, df, cfg.touch_threshold)

        # Filter by minimum touches (optional)
        valid_levels = [level for level, score in scored_levels
                       if score >= cfg.min_touches_for_level]

        # If too few valid levels, use all clustered levels
        if len(valid_levels) < 2:
            valid_levels = clustered_levels

        # Step 4: Split into support/resistance
        support = sorted([l for l in valid_levels if l <= current_price])
        resistance = sorted([l for l in valid_levels if l > current_price])

        # Handle ATH/ATL edge cases
        resistance_projected = False
        support_projected = False
        projection_method = None  # Day 33: Track which method was used

        if not resistance:
            logger.info("Agglomerative: No resistance found (ATH). Projecting resistance.")
            # Day 33: Use smart projection (Fibonacci or ATR)
            resistance, projection_method = _smart_project_resistance(
                current_price, df, atr, cfg
            )
            resistance_projected = True

        if not support:
            logger.info("Agglomerative: No support found (ATL). Projecting using ATR.")
            support = _project_support_levels(current_price, atr, cfg.atr_multipliers)
            support_projected = True

        if not support and not resistance:
            return None

        meta = {
            "type": "agglomerative",
            "raw_pivot_count": len(all_pivots),
            "clustered_level_count": len(clustered_levels),
            "valid_level_count": len(valid_levels),
            "level_scores": {str(round(l, 2)): s for l, s in scored_levels[:10]},
            "atr": round(atr, 2),
            "merge_percent": cfg.merge_percent,
            "resistance_projected": resistance_projected,
            "support_projected": support_projected,
            "projection_method": projection_method,  # Day 33: "fibonacci" or "atr" or None
        }

        return support, resistance, meta

    except Exception as exc:
        logger.exception("Agglomerative S/R computation failed: %s", exc)
        return None


# ============================================
# DAY 32: MULTI-TIMEFRAME CONFLUENCE FUNCTIONS
# ============================================

def _resample_to_weekly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample daily OHLCV data to weekly timeframe.

    Parameters
    ----------
    df : pd.DataFrame
        Daily OHLCV data (must have DatetimeIndex or be convertible)

    Returns
    -------
    pd.DataFrame
        Weekly OHLCV data
    """
    try:
        # Ensure we have a DatetimeIndex for resampling
        if not isinstance(df.index, pd.DatetimeIndex):
            # Create a date range if index is not datetime
            df = df.copy()
            df.index = pd.date_range(end=pd.Timestamp.today(), periods=len(df), freq='D')

        # Resample to weekly (W = week ending Sunday)
        weekly = df.resample('W').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }).dropna()

        logger.info(f"Resampled {len(df)} daily bars to {len(weekly)} weekly bars")
        return weekly

    except Exception as exc:
        logger.exception("Weekly resampling failed: %s", exc)
        return pd.DataFrame()


def _find_mtf_confluence(
    daily_levels: List[float],
    weekly_levels: List[float],
    threshold: float = 0.005
) -> Dict[float, Dict[str, Any]]:
    """
    Find confluence between daily and weekly S&R levels.

    A level is "confluent" if a weekly level exists within threshold distance.
    Confluent levels are stronger (appear on multiple timeframes).

    Parameters
    ----------
    daily_levels : List[float]
        S&R levels from daily timeframe
    weekly_levels : List[float]
        S&R levels from weekly timeframe
    threshold : float
        Percentage threshold for confluence (default 0.5%)

    Returns
    -------
    Dict[float, Dict[str, Any]]
        {level: {'confluent': bool, 'weekly_match': float|None, 'strength': float}}
    """
    confluence_map = {}

    for daily_level in daily_levels:
        # Check if any weekly level is within threshold
        best_match = None
        min_distance = float('inf')

        for weekly_level in weekly_levels:
            pct_distance = abs(daily_level - weekly_level) / daily_level
            if pct_distance <= threshold and pct_distance < min_distance:
                best_match = weekly_level
                min_distance = pct_distance

        is_confluent = best_match is not None

        confluence_map[daily_level] = {
            'confluent': is_confluent,
            'weekly_match': best_match,
            'distance_pct': round(min_distance * 100, 3) if best_match else None,
            # Confluent levels get higher strength score
            'strength': 1.0 if is_confluent else 0.6
        }

    return confluence_map


def _compute_weekly_sr(
    df: pd.DataFrame,
    cfg: SRConfig
) -> Tuple[List[float], List[float]]:
    """
    Compute S&R levels on weekly timeframe.

    Uses simplified agglomerative clustering on weekly data.

    Parameters
    ----------
    df : pd.DataFrame
        Daily OHLCV data (will be resampled)
    cfg : SRConfig
        Configuration

    Returns
    -------
    Tuple[List[float], List[float]]
        (weekly_support, weekly_resistance)
    """
    try:
        # Resample to weekly
        weekly_df = _resample_to_weekly(df)

        if weekly_df.empty or len(weekly_df) < 20:
            logger.info("Not enough weekly data for MTF analysis")
            return [], []

        current_price = float(df["close"].iloc[-1])

        # Use ZigZag on weekly (lower threshold since weekly bars are smoother)
        pivot_highs, pivot_lows = _detect_zigzag_pivots(
            weekly_df,
            percent_delta=cfg.zigzag_percent_delta * 0.7,  # Lower threshold for weekly
            min_bars=3  # Fewer bars for weekly
        )

        all_pivots = pivot_highs + pivot_lows

        if len(all_pivots) < 2:
            logger.info("Not enough weekly pivots for clustering")
            return [], []

        # Cluster weekly pivots
        pivot_array = np.array(all_pivots)
        clustered_levels = _cluster_with_agglom(
            pivot_array,
            merge_percent=cfg.merge_percent * 1.5,  # Wider merge for weekly
            current_price=current_price
        )

        # Split into support/resistance
        weekly_support = sorted([l for l in clustered_levels if l <= current_price])
        weekly_resistance = sorted([l for l in clustered_levels if l > current_price])

        logger.info(f"Weekly S&R: {len(weekly_support)} support, {len(weekly_resistance)} resistance")
        return weekly_support, weekly_resistance

    except Exception as exc:
        logger.exception("Weekly S&R computation failed: %s", exc)
        return [], []


def _enrich_with_mtf(
    meta: Dict[str, Any],
    support: List[float],
    resistance: List[float],
    df: pd.DataFrame,
    cfg: SRConfig
) -> None:
    """
    Enrich meta dict with Multi-Timeframe Confluence data.

    This is a helper to avoid duplicating MTF logic across all return paths.
    Modifies meta in-place.

    Parameters
    ----------
    meta : Dict[str, Any]
        Meta dict to enrich (modified in-place)
    support : List[float]
        Daily support levels
    resistance : List[float]
        Daily resistance levels
    df : pd.DataFrame
        Daily OHLCV data
    cfg : SRConfig
        Configuration
    """
    if not cfg.use_mtf:
        return

    try:
        weekly_support, weekly_resistance = _compute_weekly_sr(df, cfg)
        all_daily = support + resistance
        all_weekly = weekly_support + weekly_resistance
        confluence_map = _find_mtf_confluence(all_daily, all_weekly, cfg.mtf_confluence_threshold)

        confluent_count = sum(1 for v in confluence_map.values() if v['confluent'])

        meta["mtf"] = {
            "enabled": True,
            "weekly_support": [round(s, 2) for s in weekly_support],
            "weekly_resistance": [round(r, 2) for r in weekly_resistance],
            "confluence_map": {str(round(k, 2)): v for k, v in confluence_map.items()},
            "confluent_levels": confluent_count,
            "total_levels": len(confluence_map),
            "confluence_pct": round(confluent_count / len(confluence_map) * 100, 1) if confluence_map else 0
        }
        logger.info(f"MTF: {confluent_count}/{len(confluence_map)} levels confluent ({meta['mtf']['confluence_pct']}%)")

    except Exception as exc:
        logger.warning(f"MTF enrichment failed: {exc}")
        meta["mtf"] = {"enabled": False, "error": str(exc)}


def _pivot_sr(df: pd.DataFrame, cfg: SRConfig) -> Optional[Tuple[List[float], List[float], Dict[str, Any]]]:
    highs: List[float] = []
    lows: List[float] = []

    try:
        for i in range(cfg.pivot_left, len(df) - cfg.pivot_right):
            segment_high = df["high"].iloc[i - cfg.pivot_left : i + cfg.pivot_right + 1]
            price_high = df["high"].iloc[i]
            if price_high == segment_high.max():
                highs.append(float(price_high))

            segment_low = df["low"].iloc[i - cfg.pivot_left : i + cfg.pivot_right + 1]
            price_low = df["low"].iloc[i]
            if price_low == segment_low.min():
                lows.append(float(price_low))

        highs = sorted(list(set(highs)))
        lows = sorted(list(set(lows)))

        if not highs and not lows:
            return None

        # keep last N extreme levels
        highs = highs[-cfg.pivot_max_levels :]
        lows = lows[: cfg.pivot_max_levels]

        # sanity check spacing
        all_levels = sorted(highs + lows)
        if len(all_levels) > 1:
            diffs = np.diff(all_levels)
            ref_price = float(df["close"].iloc[-1])
            min_allowed = ref_price * cfg.pivot_min_spacing_frac
            if np.any(diffs < min_allowed):
                logger.info("Pivot levels too tightly packed; rejecting.")
                return None

        meta = {
            "raw_high_count": len(highs),
            "raw_low_count": len(lows),
            "type": "pivot",
        }
        return highs, lows, meta

    except Exception as exc:
        logger.exception("Pivot S/R computation failed: %s", exc)
        return None


def _kmeans_sr(df: pd.DataFrame, cfg: SRConfig) -> Optional[Tuple[List[float], List[float], Dict[str, Any]]]:
    try:
        prices = np.concatenate([df["high"].values, df["low"].values]).reshape(-1, 1)
        if prices.shape[0] < cfg.kmeans_clusters:
            return None

        km = KMeans(n_clusters=cfg.kmeans_clusters, n_init=10, random_state=42)
        km.fit(prices)
        centers = sorted(km.cluster_centers_.flatten().tolist())

        # spacing sanity
        if len(centers) > 1:
            diffs = np.diff(centers)
            ref_price = float(df["close"].iloc[-1])
            min_allowed = ref_price * cfg.pivot_min_spacing_frac
            if np.any(diffs < min_allowed):
                logger.info("KMeans cluster centers too tight; rejecting.")
                return None

        # split into support/resistance around last close
        last = float(df["close"].iloc[-1])
        support = [c for c in centers if c <= last]
        resistance = [c for c in centers if c > last]  # Changed >= to > to avoid duplicates

        # Handle empty resistance or support (ATH/ATL edge case)
        atr = _calculate_atr(df, cfg.atr_period)
        resistance_projected = False
        support_projected = False
        projection_method = None

        if not resistance:
            # Stock at ATH - project resistance above current price
            logger.info("KMeans: No historical resistance found (ATH). Projecting resistance.")
            # Day 33: Use smart projection (Fibonacci or ATR)
            resistance, projection_method = _smart_project_resistance(
                last, df, atr, cfg
            )
            resistance_projected = True

        if not support:
            # Stock at ATL - project support below current price
            logger.info("No historical support found (ATL edge case). Projecting levels using ATR.")
            support = _project_support_levels(last, atr, cfg.atr_multipliers)
            support_projected = True

        if not support and not resistance:
            return None

        meta = {
            "cluster_centers": centers,
            "type": "kmeans",
            "inertia": float(km.inertia_),
            "atr": round(atr, 2),
            "resistance_projected": resistance_projected,
            "support_projected": support_projected,
            "projection_method": projection_method,  # Day 33: "fibonacci" or "atr" or None
        }
        return support, resistance, meta

    except Exception as exc:
        logger.exception("KMeans S/R computation failed: %s", exc)
        return None


def _volume_profile_sr(df: pd.DataFrame, cfg: SRConfig) -> Tuple[List[float], List[float], Dict[str, Any]]:
    try:
        prices = df["close"].values
        volumes = df["volume"].values

        hist, edges = np.histogram(prices, bins=cfg.volume_bins, weights=volumes)
        if hist.sum() == 0:
            # no volume information; fallback to price-only histogram
            hist, edges = np.histogram(prices, bins=cfg.volume_bins)

        idx_sorted = np.argsort(hist)[::-1]
        # take top 3 levels max
        top_idx = idx_sorted[:3]
        centers = [(edges[i] + edges[i + 1]) / 2 for i in top_idx]
        centers = sorted([float(c) for c in centers])

        last = float(df["close"].iloc[-1])
        support = [c for c in centers if c <= last]
        resistance = [c for c in centers if c > last]  # Changed >= to > to avoid duplicates

        # Handle empty resistance or support (ATH/ATL edge case)
        atr = _calculate_atr(df, cfg.atr_period)
        resistance_projected = False
        support_projected = False
        projection_method = None

        if not resistance:
            # Stock at ATH - project resistance above current price
            logger.info("Volume profile: No resistance found (ATH). Projecting resistance.")
            # Day 33: Use smart projection (Fibonacci or ATR)
            resistance, projection_method = _smart_project_resistance(
                last, df, atr, cfg
            )
            resistance_projected = True

        if not support:
            # Stock at ATL - project support below current price
            logger.info("Volume profile: No support found (ATL). Projecting using ATR.")
            support = _project_support_levels(last, atr, cfg.atr_multipliers)
            support_projected = True

        meta = {
            "volume_histogram": hist.tolist(),
            "edges": edges.tolist(),
            "type": "volume_profile",
            "atr": round(atr, 2),
            "resistance_projected": resistance_projected,
            "support_projected": support_projected,
            "projection_method": projection_method,  # Day 33: "fibonacci" or "atr" or None
        }
        return support, resistance, meta

    except Exception as exc:
        logger.exception("Volume profile S/R computation failed: %s", exc)
        # ultimate fallback: project levels using ATR
        last = float(df["close"].iloc[-1])
        atr = _calculate_atr(df, cfg.atr_period)
        support = _project_support_levels(last, atr, cfg.atr_multipliers)
        resistance = _project_resistance_levels(last, atr, cfg.atr_multipliers)
        return support, resistance, {
            "type": "volume_profile_fallback",
            "atr": round(atr, 2),
            "resistance_projected": True,
            "support_projected": True,
        }


def compute_sr_levels(df: pd.DataFrame, cfg: Optional[SRConfig] = None) -> SRLevels:
    """
    Compute support & resistance levels with failover.

    Order of methods:
    1. Pivot-based (primary, skip if high volatility)
    2. Agglomerative clustering (Day 30 - replaces KMeans)
    3. KMeans clustering (fallback, deprecated)
    4. Volume profile (always returns something)

    Day 14 Enhancement:
    - When stock is at ATH and no historical resistance exists,
      projects resistance levels using ATR (1x, 1.5x, 2x ATR above current)
    - Same logic for support when stock is at ATL

    Day 22 Enhancement (Option D):
    - Added trade viability assessment based on Minervini's entry criteria
    - Viability included in meta: YES / CAUTION / NO
    - Actionable advice for position sizing and stop placement

    Day 30 Enhancement (Agglomerative Clustering):
    - Replaced KMeans with AgglomerativeClustering
    - Uses ZigZag pivot detection (filters noise)
    - Adaptive cluster count (no fixed 5 clusters)
    - Touch-based level scoring (stronger = more touches)
    - Feature flag cfg.use_agglomerative for rollback

    Day 32 Enhancement (Multi-Timeframe Confluence):
    - Computes S&R on both daily and weekly timeframes
    - Levels appearing on both timeframes = stronger (confluent)
    - Research shows 3.2x stronger predictive power for confluent levels
    - Feature flag cfg.use_mtf for rollback
    - Meta includes: weekly_support, weekly_resistance, confluence_map

    Day 33 Enhancement (Fibonacci Extensions):
    - When stock is near ATH (within 5%), uses Fibonacci extensions for resistance
    - Extensions: 127.2% (conservative), 161.8% (primary), 200% (extended)
    - Research basis (TrendSpider 2023): 68-72% accuracy
    - Falls back to ATR projection if swing low not found
    - Feature flag cfg.use_fibonacci for rollback
    - Meta includes: projection_method ("fibonacci" or "atr")

    Parameters
    ----------
    df : pd.DataFrame
        OHLCV data with columns: open, high, low, close, volume.
    cfg : SRConfig, optional
        Configuration object.

    Returns
    -------
    SRLevels
        Support & resistance levels and metadata.

    Raises
    ------
    SRFailure
        If data is insufficient or invalid.
    """
    cfg = cfg or SRConfig()
    df = df.copy()

    _check_data_integrity(df, cfg)

    high_vol = _is_high_volatility(df, cfg)
    logger.info("High volatility regime: %s", high_vol)
    
    current_price = float(df["close"].iloc[-1])
    atr = _calculate_atr(df, cfg.atr_period)

    # 1) Pivot-based (skip if volatility extreme)
    # Day 31: Modified to try agglomerative when pivot has no ACTIONABLE support
    # (support within 20% of current price - matching API proximity filter)
    SUPPORT_PROXIMITY_PCT = 0.20  # Must match API_CONTRACTS/backend.py
    support_floor = current_price * (1 - SUPPORT_PROXIMITY_PCT)

    if not high_vol:
        pivot_result = _pivot_sr(df, cfg)
        if pivot_result is not None:
            highs, lows, meta = pivot_result

            # Split into support/resistance around current price
            support = [l for l in lows if l <= current_price]
            resistance = [h for h in highs if h > current_price]

            # ALWAYS calculate ATR for pivot method (Day 20 fix)
            meta["atr"] = round(atr, 2)

            # Day 31: Check if ANY support is within actionable range
            actionable_support = [s for s in support if s >= support_floor]
            has_actionable_support = len(actionable_support) > 0

            # Handle ATH/ATL edge cases for pivot method too
            if not resistance:
                logger.info("Pivot: No resistance found (ATH). Projecting resistance.")
                # Day 33: Use smart projection (Fibonacci or ATR)
                resistance, proj_method = _smart_project_resistance(
                    current_price, df, atr, cfg
                )
                meta["resistance_projected"] = True
                meta["projection_method"] = proj_method
            else:
                meta["resistance_projected"] = False
                meta["projection_method"] = None

            # Day 31: If no ACTIONABLE support (within 20%), try agglomerative
            # This catches strong uptrends where pivot support is too far away
            if not has_actionable_support:
                logger.info(f"Pivot: No actionable support (floor={support_floor:.2f}). Found {len(support)} levels but all too far. Trying agglomerative.")
                # Don't return yet - fall through to agglomerative
            else:
                meta["support_projected"] = False

                # Day 22: Add trade viability assessment
                nearest_support = max(support) if support else None
                nearest_resistance = min(resistance) if resistance else None
                viability = assess_trade_viability(current_price, nearest_support, nearest_resistance, atr)
                meta["trade_viability"] = viability

                # Day 32: Add Multi-Timeframe Confluence
                _enrich_with_mtf(meta, support, resistance, df, cfg)

                return SRLevels(
                    method="pivot",
                    support=support,
                    resistance=resistance,
                    meta=meta,
                )

    # 2) Day 30/31: Agglomerative clustering (replaces KMeans)
    # Feature flag allows rollback to KMeans if needed
    # Day 31: Also tried when pivot has no natural support (strong uptrends)
    if cfg.use_agglomerative:
        agglom_result = _agglomerative_sr(df, cfg)
        if agglom_result is not None:
            support, resistance, meta = agglom_result

            # Day 31: If agglomerative also has no natural support, project using ATR
            if not support:
                logger.info("Agglomerative: No natural support found. Projecting using ATR.")
                support = _project_support_levels(current_price, atr, cfg.atr_multipliers)
                meta["support_projected"] = True
            else:
                meta["support_projected"] = False

            # Handle resistance projection if needed
            if not resistance:
                logger.info("Agglomerative: No resistance found. Projecting resistance.")
                # Day 33: Use smart projection (Fibonacci or ATR)
                resistance, proj_method = _smart_project_resistance(
                    current_price, df, atr, cfg
                )
                meta["resistance_projected"] = True
                meta["projection_method"] = proj_method
            else:
                meta["resistance_projected"] = False
                if "projection_method" not in meta:
                    meta["projection_method"] = None

            # Day 22: Add trade viability assessment
            nearest_support = max(support) if support else None
            nearest_resistance = min(resistance) if resistance else None
            viability = assess_trade_viability(current_price, nearest_support, nearest_resistance, atr)
            meta["trade_viability"] = viability

            # Day 32: Add Multi-Timeframe Confluence
            _enrich_with_mtf(meta, support, resistance, df, cfg)

            return SRLevels(
                method="agglomerative",
                support=support,
                resistance=resistance,
                meta=meta,
            )

    # 2b) Fallback: KMeans clustering (deprecated, kept for rollback)
    km_result = _kmeans_sr(df, cfg)
    if km_result is not None:
        support, resistance, meta = km_result

        # Day 22: Add trade viability assessment
        nearest_support = max(support) if support else None
        nearest_resistance = min(resistance) if resistance else None
        viability = assess_trade_viability(current_price, nearest_support, nearest_resistance, atr)
        meta["trade_viability"] = viability

        # Day 32: Add Multi-Timeframe Confluence
        _enrich_with_mtf(meta, support, resistance, df, cfg)

        return SRLevels(
            method="kmeans",
            support=support,
            resistance=resistance,
            meta=meta,
        )

    # 3) Volume profile (guaranteed)
    sup, res, meta = _volume_profile_sr(df, cfg)

    # Day 22: Add trade viability assessment
    nearest_support = max(sup) if sup else None
    nearest_resistance = min(res) if res else None
    viability = assess_trade_viability(current_price, nearest_support, nearest_resistance, atr)
    meta["trade_viability"] = viability

    # Day 32: Add Multi-Timeframe Confluence
    _enrich_with_mtf(meta, sup, res, df, cfg)

    return SRLevels(
        method="volume_profile",
        support=sup,
        resistance=res,
        meta=meta,
    )


def example_usage():
    """
    Simple self-test using synthetic data.
    Run this file directly to see sample S/R output.
    """
    rng = np.random.default_rng(42)
    n = 300
    prices = np.cumsum(rng.normal(0, 1, size=n)) + 100
    highs = prices + rng.random(n) * 2
    lows = prices - rng.random(n) * 2
    opens = prices + rng.normal(0, 0.5, size=n)
    closes = prices + rng.normal(0, 0.5, size=n)
    volumes = rng.integers(1_000, 10_000, size=n)

    idx = pd.date_range("2024-01-01", periods=n, freq="D")
    df = pd.DataFrame(
        {
            "open": opens,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": volumes,
        },
        index=idx,
    )

    levels = compute_sr_levels(df)
    print("Method:", levels.method)
    print("Support:", levels.support)
    print("Resistance:", levels.resistance)
    print("Meta:", levels.meta)
    print("\n=== Trade Viability ===")
    viability = levels.meta.get("trade_viability", {})
    print(f"Viable: {viability.get('viable')}")
    print(f"Support Distance: {viability.get('support_distance_pct')}%")
    print(f"Advice: {viability.get('advice')}")
    print(f"Stop Suggestion: ${viability.get('stop_suggestion')}")
    print(f"Position Size: {viability.get('position_size_advice')}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    example_usage()