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
from flask import jsonify, request

from breakout_detection import detect_breakout

# Day 81 (Breakout Enhancement Plan Task 2.1): hard cap on /api/breakout/batch
# to protect provider rate limits — mirrors the plan's explicit instruction.
BATCH_TICKER_LIMIT = 20


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

    @app.route('/api/breakout/batch', methods=['POST'])
    def get_breakout_batch():
        """
        Batch breakout status for up to BATCH_TICKER_LIMIT tickers in one call
        (Day 81, Breakout Enhancement Plan Task 2.1) — lets the Scan tab badge
        an entire results page without firing one request per row.

        POST body: {"tickers": ["AAPL", "MSFT", ...]}

        Returns partial results (per-ticker {"error": ...} entries) rather than
        failing the whole batch on one bad ticker — matches the Day 61 rule
        that a single bad input shouldn't 500 an otherwise-good batch.
        """
        try:
            data = request.get_json(silent=True) or {}
            tickers = data.get('tickers')
            if not tickers or not isinstance(tickers, list):
                return jsonify({'error': 'tickers list required in request body'}), 400

            tickers = [str(t).strip().upper() for t in tickers if str(t).strip()]
            if not tickers:
                return jsonify({'error': 'tickers list is empty'}), 400
            if len(tickers) > BATCH_TICKER_LIMIT:
                return jsonify({
                    'error': f'Max {BATCH_TICKER_LIMIT} tickers per batch request, got {len(tickers)}'
                }), 400

            # Benchmark fetched once, reused across all tickers (cache-first —
            # same _fetch_ohlcv path as the single-ticker route above).
            benchmark = None
            try:
                benchmark, _bsource = _fetch_ohlcv(
                    ticker='SPY',
                    period='2y',
                    get_data_provider=get_data_provider,
                    yf_module=yf_module,
                    data_provider_available=data_provider_available,
                )
                if benchmark is not None and not benchmark.empty:
                    benchmark = _normalize_ohlcv_columns(benchmark)
            except Exception as e:
                print(f"⚠️ Benchmark fetch failed for breakout batch: {e}")
                benchmark = None

            results: dict[str, Any] = {}
            # Sequential, not parallel: reuses the same provider rate-limiter
            # path as every other STA endpoint — no established backend
            # thread-pool pattern exists to safely parallelize this (Golden
            # Rule #3 — don't invent one, verify first).
            for ticker_symbol in tickers:
                try:
                    hist, source = _fetch_ohlcv(
                        ticker=ticker_symbol,
                        period='2y',
                        get_data_provider=get_data_provider,
                        yf_module=yf_module,
                        data_provider_available=data_provider_available,
                    )
                    if hist is None or hist.empty:
                        results[ticker_symbol] = {'error': f'No data found for {ticker_symbol}'}
                        continue

                    hist = _normalize_ohlcv_columns(hist)
                    if len(hist) < 80:
                        results[ticker_symbol] = {
                            'error': f'Insufficient data for {ticker_symbol} (need 80+ bars, got {len(hist)})'
                        }
                        continue

                    result = detect_breakout(
                        ohlcv=hist.tail(260),
                        ticker=ticker_symbol,
                        benchmark_ohlcv=benchmark.tail(260) if benchmark is not None and not benchmark.empty else None,
                    )
                    # Flat, explicit subset per Task 2.1's design — full detail
                    # remains available via the single-ticker route.
                    results[ticker_symbol] = {
                        'status': result.get('status'),
                        'humanAction': result.get('humanAction'),
                        'breakoutLevel': result.get('breakoutLevel'),
                        'rvol': result.get('rvol'),
                        'checks': result.get('checks'),
                        'warnings': result.get('warnings'),
                        'source': source,
                    }
                except ValueError as e:
                    results[ticker_symbol] = {'error': str(e)}
                except Exception as e:
                    print(f"Error detecting breakout for {ticker_symbol} (batch): {e}")
                    results[ticker_symbol] = {'error': str(e)}

            return jsonify({
                'results': results,
                'requested': len(tickers),
                'benchmarkAvailable': bool(benchmark is not None and not benchmark.empty),
                'apiTimestamp': datetime.now().isoformat(),
            })

        except Exception as e:
            print(f"Error in breakout batch endpoint: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), 500
