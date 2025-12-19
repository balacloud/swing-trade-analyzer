"""
Support & Resistance Engine for Swing Trade Analyzer
Multi-method S/R calculation with failover logic

Methods:
1. Pivot-Based (Primary) - Local highs/lows detection
2. KMeans Clustering (Secondary) - Price level bands  
3. Volume Profile (Tertiary) - High-volume zones as magnets

Day 13: Integrated into Swing Trade Analyzer backend
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Literal, Tuple

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
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


@dataclass
class SRLevels:
    """Container for support & resistance levels."""
    method: Literal["pivot", "kmeans", "volume_profile"]
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


def _is_high_volatility(df: pd.DataFrame, cfg: SRConfig) -> bool:
    """Check for structural break / extreme recent volatility."""
    window = min(cfg.volatility_window, len(df) - 1)
    pct = df["close"].pct_change().tail(window).abs()
    if len(pct) == 0:
        return False
    avg = float(pct.mean())
    return avg > cfg.volatility_threshold


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
        resistance = [c for c in centers if c >= last]

        if not support and not resistance:
            return None

        meta = {
            "cluster_centers": centers,
            "type": "kmeans",
            "inertia": float(km.inertia_),
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
        resistance = [c for c in centers if c >= last]

        meta = {
            "volume_histogram": hist.tolist(),
            "edges": edges.tolist(),
            "type": "volume_profile",
        }
        return support, resistance, meta

    except Exception as exc:
        logger.exception("Volume profile S/R computation failed: %s", exc)
        # ultimate fallback: last close as "magnet" level
        last = float(df["close"].iloc[-1])
        return [last], [last], {"type": "volume_profile_fallback"}


def compute_sr_levels(df: pd.DataFrame, cfg: Optional[SRConfig] = None) -> SRLevels:
    """
    Compute support & resistance levels with failover.

    Order of methods:
    1. Pivot-based
    2. KMeans clustering
    3. Volume profile (always returns something)

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

    # 1) Pivot-based (skip if volatility extreme)
    if not high_vol:
        pivot_result = _pivot_sr(df, cfg)
        if pivot_result is not None:
            highs, lows, meta = pivot_result
            return SRLevels(
                method="pivot",
                support=lows,
                resistance=highs,
                meta=meta,
            )

    # 2) KMeans clustering
    km_result = _kmeans_sr(df, cfg)
    if km_result is not None:
        support, resistance, meta = km_result
        return SRLevels(
            method="kmeans",
            support=support,
            resistance=resistance,
            meta=meta,
        )

    # 3) Volume profile (guaranteed)
    sup, res, meta = _volume_profile_sr(df, cfg)
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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    example_usage()
