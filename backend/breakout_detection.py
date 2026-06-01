"""
Breakout Detection Engine for Swing Trade Analyzer (STA).

This module mirrors the STA Pine Breakout Companion logic in backend-friendly Python.
It is intentionally a human-in-the-loop filter, not an auto-trading decision engine.

Outputs simple states:
- NOT_READY
- BUILDING_BASE
- BREAKOUT_WATCH
- BREAKOUT_CONFIRMED
- RETEST_ENTRY
- SUPPLY_WARNING
- FAILED_BREAKOUT
- EXTENDED_CHASE_RISK
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd


@dataclass
class BreakoutConfig:
    lookback_bars: int = 120
    resistance_lookback: int = 60
    support_lookback: int = 60
    breakout_buffer_pct: float = 0.30
    near_level_pct: float = 2.00
    retest_pct: float = 1.00
    rvol_confirm: float = 1.50
    atr_len: int = 14
    atr_ma_len: int = 50
    atr_tight_ratio: float = 0.85
    max_extension_from_sma50_pct: float = 12.0
    recent_breakout_window: int = 30


@dataclass
class BreakoutResult:
    status: str
    humanAction: str
    currentPrice: float
    breakoutLevel: Optional[float]
    supportLevel: Optional[float]
    invalidation: Optional[float]
    retestZoneLow: Optional[float]
    retestZoneHigh: Optional[float]
    rvol: Optional[float]
    atrPct: Optional[float]
    extensionFromSma50Pct: Optional[float]
    checks: Dict[str, bool]
    warnings: Dict[str, bool]
    evidence: Dict[str, Any]
    timestamp: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _safe_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    try:
        if value is None or pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def _normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize OHLCV columns to lowercase names required by this module."""
    if df is None or df.empty:
        raise ValueError("No OHLCV data provided")

    out = df.copy()
    out.columns = [str(c).lower() for c in out.columns]
    required = ["open", "high", "low", "close", "volume"]
    missing = [c for c in required if c not in out.columns]
    if missing:
        raise ValueError(f"Missing OHLCV columns: {missing}")

    out = out[required].dropna()
    if len(out) < 80:
        raise ValueError(f"Need at least 80 bars for breakout detection, got {len(out)}")
    return out


def _sma(series: pd.Series, length: int) -> pd.Series:
    return series.rolling(length, min_periods=length).mean()


def _ema(series: pd.Series, length: int) -> pd.Series:
    return series.ewm(span=length, adjust=False).mean()


def _atr(df: pd.DataFrame, length: int = 14) -> pd.Series:
    high = df["high"]
    low = df["low"]
    close = df["close"]
    prev_close = close.shift(1)
    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return tr.rolling(length, min_periods=length).mean()


def _round_optional(value: Optional[float], ndigits: int = 2) -> Optional[float]:
    if value is None or pd.isna(value):
        return None
    return round(float(value), ndigits)


def detect_breakout(
    ohlcv: pd.DataFrame,
    ticker: str,
    benchmark_ohlcv: Optional[pd.DataFrame] = None,
    config: Optional[BreakoutConfig] = None,
) -> Dict[str, Any]:
    """
    Detect breakout status from OHLCV data.

    Parameters
    ----------
    ohlcv:
        DataFrame with open/high/low/close/volume columns.
    ticker:
        Ticker symbol for evidence only.
    benchmark_ohlcv:
        Optional benchmark OHLCV, usually SPY, used for RS check.
    config:
        Optional BreakoutConfig overrides.
    """
    cfg = config or BreakoutConfig()
    df = _normalize_ohlcv(ohlcv)

    close = df["close"]
    high = df["high"]
    low = df["low"]
    open_ = df["open"]
    volume = df["volume"]

    ema20 = _ema(close, 20)
    sma50 = _sma(close, 50)
    sma200 = _sma(close, 200)
    vol_avg_20 = _sma(volume, 20)
    vol_avg_5 = _sma(volume, 5)
    atr = _atr(df, cfg.atr_len)
    atr_avg = _sma(atr, cfg.atr_ma_len)

    latest_idx = df.index[-1]
    current_price = float(close.iloc[-1])

    # Resistance/support are intentionally simple here. STA's /api/sr remains the
    # richer level engine; this endpoint provides a fast breakout state.
    resistance_window = min(cfg.resistance_lookback, max(20, len(df) - 1))
    support_window = min(cfg.support_lookback, max(20, len(df) - 1))
    prior_highs = high.iloc[-resistance_window - 1 : -1]
    prior_lows = low.iloc[-support_window - 1 : -1]
    breakout_level = _safe_float(prior_highs.max())
    support_level = _safe_float(prior_lows.min())

    breakout_buffer = (breakout_level or 0) * cfg.breakout_buffer_pct / 100.0
    near_resistance = bool(
        breakout_level
        and current_price >= breakout_level * (1 - cfg.near_level_pct / 100.0)
        and current_price <= breakout_level * (1 + cfg.breakout_buffer_pct / 100.0)
    )

    # Trend and momentum gates.
    sma50_now = _safe_float(sma50.iloc[-1])
    sma200_now = _safe_float(sma200.iloc[-1])
    sma200_20 = _safe_float(sma200.iloc[-21]) if len(sma200.dropna()) >= 21 else None
    ema20_now = _safe_float(ema20.iloc[-1])
    trend_ok = bool(
        sma50_now
        and sma200_now
        and sma200_20
        and current_price > sma50_now
        and sma50_now > sma200_now
        and sma200_now > sma200_20
    )
    price_above_ema20 = bool(ema20_now and current_price > ema20_now)

    rvol = None
    if _safe_float(vol_avg_20.iloc[-1], 0):
        rvol = float(volume.iloc[-1] / vol_avg_20.iloc[-1])
    volume_expansion = bool(rvol is not None and rvol >= cfg.rvol_confirm)
    volume_dry_up = bool(
        _safe_float(vol_avg_5.iloc[-1]) is not None
        and _safe_float(vol_avg_20.iloc[-1]) is not None
        and vol_avg_5.iloc[-1] < vol_avg_20.iloc[-1]
    )

    atr_now = _safe_float(atr.iloc[-1])
    atr_avg_now = _safe_float(atr_avg.iloc[-1])
    atr_contracting = bool(atr_now and atr_avg_now and atr_now < atr_avg_now * cfg.atr_tight_ratio)
    atr_pct = (atr_now / current_price * 100.0) if atr_now and current_price else None

    # Relative strength vs benchmark.
    rs_strong = False
    if benchmark_ohlcv is not None and not benchmark_ohlcv.empty:
        try:
            bdf = _normalize_ohlcv(benchmark_ohlcv)
            aligned = pd.concat([close.reset_index(drop=True), bdf["close"].reset_index(drop=True)], axis=1).dropna()
            aligned.columns = ["stock", "bench"]
            if len(aligned) >= 25:
                rs_ratio = aligned["stock"] / aligned["bench"]
                rs_ma = rs_ratio.rolling(20, min_periods=20).mean()
                rs_strong = bool(rs_ratio.iloc[-1] > rs_ma.iloc[-1])
        except Exception:
            rs_strong = False

    # Candle quality gates.
    candle_range = float(high.iloc[-1] - low.iloc[-1])
    body_size = abs(float(close.iloc[-1] - open_.iloc[-1]))
    upper_wick = float(high.iloc[-1] - max(open_.iloc[-1], close.iloc[-1]))
    close_location = (float(close.iloc[-1] - low.iloc[-1]) / candle_range) if candle_range > 0 else None
    body_pct = body_size / candle_range if candle_range > 0 else None
    upper_wick_pct = upper_wick / candle_range if candle_range > 0 else None

    strong_close = bool(close_location is not None and close_location >= 0.75)
    strong_body = bool(body_pct is not None and body_pct >= 0.50)
    low_upper_wick = bool(upper_wick_pct is not None and upper_wick_pct <= 0.35)
    wide_range = bool(atr_now and candle_range >= atr_now * 1.20)
    candle_quality_ok = bool(strong_close and strong_body and low_upper_wick and wide_range)

    rejection_candle = bool(close_location is not None and upper_wick_pct is not None and close_location <= 0.50 and upper_wick_pct >= 0.45)
    high_volume_red = bool(close.iloc[-1] < open_.iloc[-1] and rvol is not None and rvol >= 1.50)
    supply_warning = bool(near_resistance and (rejection_candle or high_volume_red))

    extension_from_sma50 = ((current_price - sma50_now) / sma50_now * 100.0) if sma50_now else None
    not_extended = bool(extension_from_sma50 is not None and extension_from_sma50 <= cfg.max_extension_from_sma50_pct)
    extension_risk = bool(extension_from_sma50 is not None and extension_from_sma50 > cfg.max_extension_from_sma50_pct)

    breakout_confirmed = bool(
        breakout_level
        and current_price > breakout_level + breakout_buffer
        and trend_ok
        and volume_expansion
        and rs_strong
        and candle_quality_ok
        and not_extended
        and not supply_warning
    )
    breakout_watch = bool(
        near_resistance
        and trend_ok
        and (atr_contracting or volume_dry_up)
        and rs_strong
        and not breakout_confirmed
        and not supply_warning
    )
    building_base = bool(current_price > (sma50_now or np.inf) and breakout_level and current_price < breakout_level and (atr_contracting or volume_dry_up))

    # Recent breakout/retest/failed-breakout detection using close above prior resistance.
    recent_breakout_level = None
    recent_breakout_offset = None
    window = min(cfg.recent_breakout_window, len(df) - 21)
    if window > 0:
        for offset in range(window, 0, -1):
            i = len(df) - offset - 1
            if i < 20:
                continue
            local_res = high.iloc[max(0, i - cfg.resistance_lookback) : i].max()
            local_close = close.iloc[i]
            if local_close > local_res * (1 + cfg.breakout_buffer_pct / 100.0):
                recent_breakout_level = float(local_res)
                recent_breakout_offset = offset

    retest_zone_low = None
    retest_zone_high = None
    retest_entry = False
    failed_breakout = False
    if recent_breakout_level:
        retest_zone_low = recent_breakout_level * (1 - cfg.retest_pct / 100.0)
        retest_zone_high = recent_breakout_level * (1 + cfg.retest_pct / 100.0)
        retest_entry = bool(low.iloc[-1] <= retest_zone_high and current_price >= retest_zone_low and current_price > recent_breakout_level and price_above_ema20)
        failed_breakout = bool(current_price < recent_breakout_level * (1 - cfg.retest_pct / 100.0))

    # Status priority order: risk states first, then actionable states.
    if failed_breakout:
        status = "FAILED_BREAKOUT"
        human_action = "Avoid or reassess; breakout level failed."
    elif supply_warning:
        status = "SUPPLY_WARNING"
        human_action = "Wait; sellers/rejection visible near resistance."
    elif extension_risk:
        status = "EXTENDED_CHASE_RISK"
        human_action = "Avoid chasing; wait for pullback or base reset."
    elif retest_entry:
        status = "RETEST_ENTRY"
        human_action = "Review for possible retest entry with defined stop."
    elif breakout_confirmed:
        status = "BREAKOUT_CONFIRMED"
        human_action = "Valid candidate; verify chart context and risk/reward before trade."
    elif breakout_watch:
        status = "BREAKOUT_WATCH"
        human_action = "Watch closely; wait for decisive close/volume confirmation."
    elif building_base:
        status = "BUILDING_BASE"
        human_action = "Monitor; base/compression may be forming."
    else:
        status = "NOT_READY"
        human_action = "Ignore for now or keep on watchlist."

    invalidation = None
    if support_level:
        invalidation = support_level
    elif breakout_level:
        invalidation = breakout_level * (1 - cfg.retest_pct / 100.0)

    result = BreakoutResult(
        status=status,
        humanAction=human_action,
        currentPrice=round(current_price, 2),
        breakoutLevel=_round_optional(breakout_level, 2),
        supportLevel=_round_optional(support_level, 2),
        invalidation=_round_optional(invalidation, 2),
        retestZoneLow=_round_optional(retest_zone_low, 2),
        retestZoneHigh=_round_optional(retest_zone_high, 2),
        rvol=_round_optional(rvol, 2),
        atrPct=_round_optional(atr_pct, 2),
        extensionFromSma50Pct=_round_optional(extension_from_sma50, 2),
        checks={
            "trendOk": trend_ok,
            "priceAboveEma20": price_above_ema20,
            "nearResistance": near_resistance,
            "rsStrong": rs_strong,
            "atrContracting": atr_contracting,
            "volumeDryUp": volume_dry_up,
            "volumeExpansion": volume_expansion,
            "strongClose": strong_close,
            "strongBody": strong_body,
            "lowUpperWick": low_upper_wick,
            "wideRange": wide_range,
            "candleQualityOk": candle_quality_ok,
            "notExtended": not_extended,
            "breakoutConfirmed": breakout_confirmed,
            "breakoutWatch": breakout_watch,
            "buildingBase": building_base,
            "retestEntry": retest_entry,
        },
        warnings={
            "supplyWarning": supply_warning,
            "rejectionCandle": rejection_candle,
            "highVolumeRed": high_volume_red,
            "extensionRisk": extension_risk,
            "failedBreakout": failed_breakout,
        },
        evidence={
            "ticker": ticker.upper(),
            "method": "STA breakout v1 — price/volume/candle/RS filter",
            "resistanceLookbackBars": resistance_window,
            "supportLookbackBars": support_window,
            "recentBreakoutLevel": _round_optional(recent_breakout_level, 2),
            "recentBreakoutBarsAgo": recent_breakout_offset,
            "closeLocation": _round_optional(close_location, 2),
            "bodyPct": _round_optional(body_pct, 2),
            "upperWickPct": _round_optional(upper_wick_pct, 2),
            "atr": _round_optional(atr_now, 2),
            "sma50": _round_optional(sma50_now, 2),
            "sma200": _round_optional(sma200_now, 2),
        },
        timestamp=pd.Timestamp.utcnow().isoformat(),
    )
    return result.to_dict()
