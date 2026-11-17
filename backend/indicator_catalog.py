"""
Indicator catalog: the ONE written description of every number on the Analyze and Value tabs (Day 126).
Plan: docs/claude/design/INDICATOR_FORMULA_AUDIT_PLAN_DAY126.md (§3.1).

Feeds /api/provenance `indicators` (the "how indicators are calculated" table on the Data Sources tab).
Every `how` text is written from the code as it is, not from memory. `computed_in` names the code that produces the live number:
  'py:module:function'  -> a Python function (the test resolves it with import + getattr)
  'js:path:export'      -> a JS export (the test checks the export exists in that file)
`copies` lists the OTHER implementations by status, so Golden Rule 59 (one rule, one place) has a written map:
  live = changes what the user sees or trades, paper = paper-trading stops/signals, frozen = research/backtest only,
  external = Pine / Leveraged ETF Board, dead = no callers (logged, not deleted here).
backend/backtest/test_indicators.py fails if a name resolves to nothing, if names repeat, or if an indicator file appears
that is neither here nor in the frozen-research allowlist.
No value is computed here; changing this file changes the table, never a number.
"""

KINDS = ('local_bars', 'local_bars_spy', 'provider', 'provider_plus_local')

CATALOG = [
    {
        'id': 'sma', 'name': 'SMA 50 / 200', 'kind': 'local_bars',
        'from_text': "this stock's daily closes",
        'how': 'Average of the last 50 (or 200) closes. Completed days only: today\'s unfinished bar is left out (Day 126).',
        'computed_in': ['js:frontend/src/utils/technicalIndicators.js:calculateSMA'],
        'consumers': ['Analyze: trend, Technical Read'],
        'copies': {'live': ['backend/pattern_detection.py:calculate_sma (Trend Template)', 'backend/index_trend.py', 'backend/market_phase_engine.py'],
                   'external': ['Leveraged ETF Board']},
    },
    {
        'id': 'ema', 'name': 'EMA 8 / 21', 'kind': 'local_bars',
        'from_text': "this stock's daily closes",
        'how': 'Starts at the first close, then EMA = close x k + previous EMA x (1 - k), k = 2/(period+1), run over every completed bar. Today\'s unfinished bar is left out (Day 126).',
        'computed_in': ['js:frontend/src/utils/technicalIndicators.js:calculateEMA'],
        'consumers': ['Analyze: trend, pullback to EMA'],
        'copies': {'external': ['Leveraged ETF Board'], 'live': ['backend/backend.py SRPS ema21 (adjust=False)']},
    },
    {
        'id': 'rsi', 'name': 'RSI 14', 'kind': 'local_bars',
        'from_text': "this stock's daily closes",
        'how': "Wilder: first average = simple mean of 14 moves, then (previous x 13 + today) / 14. Decides the verdict's Strong / Decent band. "
               'Completed days only (Day 126). A flat price history gives 100.',
        'computed_in': ['js:frontend/src/utils/technicalIndicators.js:calculateRSI'],
        'consumers': ['Analyze verdict (categoricalAssessment.js)'],
        'copies': {'live': [],
                   'unused': ['backend/backend.py:calculate_rsi + calculate_rsi_4h (no screen reads them; pandas ewm, flat history gives 50)'],
                   'paper': ['RSI/ADX come from TradingView in paper trading (scan_queries.py)'],
                   'frozen': ['backend/backtest/gate5_combined.py', 'backend/backtest/nirmal_validation.py', 'backend/backtest/parameter_stability.py',
                              'backend/backtest/backtest_holistic.py', 'backend/backtest/backtest_adx_rsi_thresholds.py',
                              'backend/backtest/backtest_technical.py'],
                   'external': ['Leveraged ETF Board'], 'mean_reversion': ['backend/mean_reversion.py:calculate_rsi_short (RSI 2)']},
    },
    {
        'id': 'atr', 'name': 'ATR 14', 'kind': 'local_bars',
        'from_text': "this stock's daily high, low, close",
        'how': "Wilder: first average = mean of the first 14 true ranges (the first bar counts as high minus low), then (previous x 13 + today) / 14, over the whole history. Sets the Trade Setup "
               "stop (2 x ATR). Uses finished days only; today's unfinished bar is left out.",
        'computed_in': ['py:simple_sr:wilder_atr'],
        'consumers': ['Analyze: Trade Setup stop, Technical Read'],
        'copies': {'paper': ['backend/backtest/trade_simulator.py:calculate_atr_at (51-bar window; sets paper-trading stops)'],
                   'live': ['backend/backend.py SRPS ATR(20)'],
                   'legacy': ['backend/support_resistance.py:_calculate_atr (only ?engine=legacy)'],
                   'dead': ['frontend/src/utils/technicalIndicators.js:calculateATR (simple mean, no consumer)',
                            'backend/pattern_detection.py:calculate_atr (simple mean, no callers)'],
                   'external': ['Leveraged ETF Board']},
    },
    {
        'id': 'adx', 'name': 'ADX 14', 'kind': 'local_bars',
        'from_text': "this stock's daily high, low, close",
        'how': 'Wilder smoothing (pandas ewm, alpha 1/14) of +DM, -DM and true range; ADX is the smoothed DX. Completed days only (Day 126).',
        'computed_in': ['py:backend:calculate_adx'],
        'consumers': ['Analyze: Technical Read'],
        'copies': {'live': ['backend/mean_reversion.py:calculate_adx (Mean Reversion gate; differs on tie bars)'],
                   'frozen': ['backend/backtest/gate5_combined.py', 'backend/backtest/nirmal_validation.py', 'backend/backtest/backtest_holistic.py',
                              'backend/backtest/backtest_adx_rsi_thresholds.py']},
    },
    {
        'id': 'avgvol', 'name': 'Avg volume 50 / RVOL', 'kind': 'local_bars',
        'from_text': "this stock's daily volume",
        'how': "Average of the last 50 daily volumes; RVOL = the day\'s volume / that average. The Technical Read uses the last COMPLETED session while today is still forming; the raw API value for today\'s unfinished bar reads low mid-session.",
        'computed_in': ['py:backend:get_support_resistance', 'js:frontend/src/utils/scoringEngine.js:getIndicators'],
        'consumers': ['Analyze: volume read'],
        'copies': {'live': ['backend/breakout_detection.py (50 prior bars, breakout bar excluded)', 'backend/mean_reversion.py (20-day average)',
                            'backend/backend.py SRPS avgvol20']},
    },
    {
        'id': 'rs', 'name': 'RS 52W', 'kind': 'local_bars_spy',
        'from_text': "this stock's and SPY's closes",
        'how': '(stock today / stock 251 bars ago) / (SPY today / SPY 251 bars ago): a ratio of growth factors. With 201-251 bars it uses the oldest bar, '
               'so its "52 weeks" is shorter; under 201 bars there is no RS.',
        'computed_in': ['js:frontend/src/utils/rsCalculator.js:calculateRelativeStrength'],
        'consumers': ['Analyze: relative strength'],
        'copies': {'paper': ['backend/backtest/backtest_holistic.py:calculate_rs_52w (shift(252), one bar different)'],
                   'live': ['backend/backend.py:compute_rs_ratio_and_quadrant (sector rotation)']},
    },
    {
        'id': 'peg', 'name': 'PEG', 'kind': 'provider_plus_local',
        'from_text': 'a data provider (Finnhub, then Alpha Vantage, then Yahoo)',
        'how': 'Not calculated from prices. Taken from the provider; Yahoo computes P/E / (EPS growth x 100) when it is missing. '
               'The Value tab switches to PEGY (growth + dividend yield) locally when the yield is over 1.5%.',
        'computed_in': ['py:backend:get_value_analysis'],
        'consumers': ['Value tab'],
        'copies': {},
    },
]


def build_indicator_rows():
    """Rows for /api/provenance `indicators`. Keeps the old keys (name, source, formula) so nothing that reads them breaks."""
    names = [e['name'] for e in CATALOG]
    if len(set(names)) != len(names):
        raise ValueError('indicator_catalog: duplicate names')
    rows = []
    for e in CATALOG:
        if e['kind'] not in KINDS:
            raise ValueError(f"indicator_catalog: bad kind for {e['id']}")
        rows.append({'name': e['name'], 'source': e['from_text'], 'formula': e['how'],
                     'kind': e['kind'], 'computed_in': list(e['computed_in'])})
    return rows
