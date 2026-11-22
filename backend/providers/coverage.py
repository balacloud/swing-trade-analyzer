"""Which tickers a US-only data source can serve (Day 129, plan ALPACA_PROVIDER_PLAN_DAY129.md).

Alpaca and Twelve Data's free plan carry US symbols only. Asking them for a Canadian symbol or an index (^VIX) spends a rate-limit
token (Twelve Data: a real API call too) and gets "not found". One copy of the rule, used by both providers, live_quote and the audit.
"""

CANADIAN_SUFFIXES = ('.TO', '.NE', '.NEO', '.V', '.CN')


def is_canadian(ticker):
    return (ticker or '').upper().endswith(CANADIAN_SUFFIXES)


def is_us_symbol(ticker):
    """True when a US-only source may be asked for this ticker (not empty, not an index, not Canadian)."""
    t = (ticker or '').strip().upper()
    return bool(t) and not t.startswith('^') and not t.endswith(CANADIAN_SUFFIXES)
