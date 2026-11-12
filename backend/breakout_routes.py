"""
Flask route registration for STA Breakout Detection.

This module is intentionally thin and follows the STA backend pattern:
- fetch OHLCV with DataProvider first
- fall back to yfinance when needed
- drop today's forming bar (Day 125: rules judge completed daily closes)
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

from breakout_detection import detect_breakout, prepare_breakout_frame, MIN_BARS

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
        Get STA breakout state for a ticker (simple trader rules, Day 125).

        Status is one of: FAILED_BREAKOUT, EXTENDED_CHASE_RISK, RETEST_ENTRY,
        BREAKOUT_CONFIRMED, BREAKOUT_LIGHT_VOLUME, BREAKOUT_WATCH, NOT_READY.
        See breakout_detection.py for the rules.
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

            hist, dropped = prepare_breakout_frame(hist)

            if len(hist) < MIN_BARS:
                return jsonify({
                    'error': f'Insufficient data for {ticker_symbol}',
                    'message': f'Need at least {MIN_BARS} completed bars, got {len(hist)}'
                }), 400

            frame = hist.tail(260)
            result = detect_breakout(frame, ticker=ticker_symbol)

            # Keep API flat and explicit. Do not fake missing values.
            result['ticker'] = ticker_symbol
            result['dataPoints'] = int(len(frame))
            result['source'] = source
            result['barDropped'] = bool(dropped)
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

                    hist, _dropped = prepare_breakout_frame(hist)
                    if len(hist) < MIN_BARS:
                        results[ticker_symbol] = {
                            'error': f'Insufficient data for {ticker_symbol} (need {MIN_BARS}+ completed bars, got {len(hist)})'
                        }
                        continue

                    result = detect_breakout(hist.tail(260), ticker=ticker_symbol)
                    # Flat, explicit subset per Task 2.1's design — full detail
                    # remains available via the single-ticker route.
                    results[ticker_symbol] = {
                        'status': result.get('status'),
                        'humanAction': result.get('humanAction'),
                        'breakoutLevel': result.get('breakoutLevel'),
                        'rvol': result.get('rvol'),
                        'asOfDate': result.get('asOfDate'),
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
                'apiTimestamp': datetime.now().isoformat(),
            })

        except Exception as e:
            print(f"Error in breakout batch endpoint: {e}")
            traceback.print_exc()
            return jsonify({'error': str(e)}), 500
