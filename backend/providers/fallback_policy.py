"""Which tickers must never be served by Tradier (Day 129, plan TRADIER_FALLBACK_RULE_PLAN_DAY129.md).

Tradier is the last source in the price chain. The after-close audit of 2026-11-19 found it has split errors on leveraged funds
(NVDL +191% and QPUX -69% one-day steps that Twelve Data and Yahoo do not show), and it is not dividend-adjusted. For these funds
the app serves the saved copy (marked stale) or a clear error instead. A plain constant, not a data file: nothing to fail to read.
A drift test (test_tradier_fallback_rule.py) checks every leveraged fund the audit knows about is listed here.
"""

SPLIT_ERRORS = 'leveraged fund: Tradier has split errors on it'

NO_TRADIER = {t: SPLIT_ERRORS for t in (
    # US leveraged, found by the name classifier (data_quality.classify_instrument)
    'AAPU', 'AMZU', 'AVGC', 'BRKU', 'COPZ', 'COTG', 'ELIL', 'GGLL', 'METU', 'MSFU', 'NFXL', 'NVDL', 'SOXL', 'TSLL', 'URAA',
    # US leveraged the classifier misses (hand-labelled in the audit universe)
    'QPUX', 'DRAL', 'SPCL', 'UBOT',
    # Canadian leveraged (the orchestrator chain has no Canada rule, so Tradier can be asked for these too) and GDXU typed without a suffix
    'SOXL.NE', 'GDXU.TO', 'GDXU',
)}


def tradier_blocked(ticker):
    """True when Tradier must not serve this ticker's price history."""
    return (ticker or '').upper() in NO_TRADIER
