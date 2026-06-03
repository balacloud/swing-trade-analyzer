"""
Flask route registration for STA Breakout Detection.

This module is intentionally thin and follows the STA backend pattern:
- fetch OHLCV with DataProvider first
- fall back to yfinance when needed
- fetch SPY benchmark when available for RS check
- call breakout_detection.detect_breakout()
- return transparent JSON without inventing fallback values

Backend wiring target:
    from breakout_routes import register_breakout_routes
    register_breakout_routes(app, get_data_provider, yf, DATA_PROVIDER_AVAILABLE)
"""

from __future__ import annotations

from datetime import datetime
import traceback
from typing import Any, Callable, Optional

import pandas as pd
from flask import jsonify

from breakout_detection import detect_breakout


def _fetch_ohlcv(
    ticker: str,
    period: str,
    get_data_provider: Optional[Callable[[], Any]],
    yf_module: Any,
    data_provider_available: bool,
) -> tuple[Optional[pd.DataFrame], str]:
    """Fetch OHLCV using STA's data-provider-first convention."""
    hist = None
    source = None

    if data_provider_available and get_data_provider is not None:
        try:
            dp = get_data_provider()
            hist = dp.get_ohlcv(ticker, period)
            if hist is not None and not hist.empty:
                source = "DataProvider"
        except Exception as e:
            print(f"⚠️ DataProvider breakout OHLCV failed for {ticker}: {e}")

    if hist is None or hist.empty:
        stock = yf_module.Ticker(ticker)
        hist = stock.history(period=period)
        source = "yfinance"

    return hist, source or "unknown"


def _normalize_ohlcv_columns(hist: pd.DataFrame) -> pd.DataFrame:
    """Normalize OHLCV DataFrame columns to lowercase for breakout engine."""
    out = hist.copy()
    out.columns = [str(c).lower() for c in out.columns]
    return out


def register_breakout_routes(
    app,
    get_data_provider: Optional[Callable[[], Any]],
    yf_module: Any,
    data_provider_available: bool,
):
    """Register `/api/breakout/<ticker>` on the provided Flask app."""

    @app.route('/api/breakout/<ticker>', methods=['GET'])
    def get_breakout_status(ticker):
        """
        Get STA breakout state for a ticker.

        Returns one of:
        - NOT_READY
        - BUILDING_BASE
        - BREAKOUT_WATCH
        - BREAKOUT_CONFIRMED
        - RETEST_ENTRY
        - SUPPLY_WARNING
        - FAILED_BREAKOUT
        - EXTENDED_CHASE_RISK
        """
        try:
            ticker_symbol = ticker.upper()
            print(f"🚀 Detecting breakout state for {ticker_symbol}...")

            hist, source = _fetch_ohlcv(
                ticker=ticker_symbol,
                period='2y',
                get_data_provider=get_data_provider,
                yf_module=yf_module,
                data_provider_available=data_provider_available,
            )

            if hist is None or hist.empty:
                return jsonify({'error': f'No data found for {ticker_symbol}'}), 404

            hist = _normalize_ohlcv_columns(hist)

            if len(hist) < 80:
                return jsonify({
                    'error': f'Insufficient data for {ticker_symbol}',
                    'message': f'Need at least 80 bars, got {len(hist)}'
                }), 400

            # Benchmark: SPY for U.S. equities in v1. Canadian benchmark unresolved.
            benchmark = None
            benchmark_source = None
            try:
                benchmark, benchmark_source = _fetch_ohlcv(
                    ticker='SPY',
                    period='2y',
                    get_data_provider=get_data_provider,
                    yf_module=yf_module,
                    data_provider_available=data_provider_available,
                )
                if benchmark is not None and not benchmark.empty:
                    benchmark = _normalize_ohlcv_columns(benchmark)
            except Exception as e:
                print(f"⚠️ Benchmark fetch failed for breakout RS check: {e}")
                benchmark = None
                benchmark_source = None

            result = detect_breakout(
                ohlcv=hist.tail(260),
                ticker=ticker_symbol,
                benchmark_ohlcv=benchmark.tail(260) if benchmark is not None and not benchmark.empty else None,
            )

            # Keep API flat and explicit. Do not fake missing values.
            result['ticker'] = ticker_symbol
            result['dataPoints'] = int(len(hist.tail(260)))
            result['source'] = source
            result['benchmark'] = {
                'ticker': 'SPY',
                'source': benchmark_source,
                'available': bool(benchmark is not None and not benchmark.empty)
            }
            result['apiTimestamp'] = datetime.now().isoformat()

            print(f"✅ Breakout {ticker_symbol}: {result.get('status')} | source={source}")
            return jsonify(result)

        except ValueError as e:
            print(f"Breakout detection validation failed for {ticker}: {e}")
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            print(f"Error detecting breakout for {ticker}: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), 500
