"""
SimFin Historical Fundamentals Loader — v4.16 Holistic Backtest

Provides point-in-time fundamental data for backtesting.
Uses SimFin free tier: 5 years of quarterly data with publish dates.

Key function: get_fundamentals_at_date(ticker, trade_date)
Returns the most recent fundamentals that were KNOWN at trade_date,
respecting actual SEC filing publish dates (no look-ahead bias).
"""

import os
import pandas as pd
import numpy as np

# Lazy-loaded SimFin data (module-level cache)
_income_df = None
_balance_df = None
_data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'simfin')
_API_KEY = '38f09db0-8ad3-4d87-b5fa-e57fcc8fceb3'


def _load_datasets():
    """Load SimFin datasets from local cache (download if needed)."""
    global _income_df, _balance_df

    if _income_df is not None and _balance_df is not None:
        return

    import simfin as sf
    sf.set_api_key(_API_KEY)
    sf.set_data_dir(_data_dir)

    _income_df = sf.load(dataset='income', variant='quarterly', market='us')
    _balance_df = sf.load(dataset='balance', variant='quarterly', market='us')

    # Ensure date columns are datetime
    for df in [_income_df, _balance_df]:
        for col in ['Report Date', 'Publish Date']:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')

    print(f"SimFin loaded: {len(_income_df)} income rows, {len(_balance_df)} balance rows")


def get_fundamentals_at_date(ticker, trade_date):
    """
    Get the most recent fundamentals KNOWN at trade_date.

    Uses actual Publish Date from SEC filings — no look-ahead bias.
    For example, Q4 ending Dec 31 with Publish Date Feb 1 means
    the data is only available for trades on/after Feb 1.

    Args:
        ticker: Stock ticker (e.g., 'AAPL')
        trade_date: Date of the trade (str 'YYYY-MM-DD' or datetime)

    Returns:
        dict with keys: roe, debt_equity, revenue_growth_yoy, eps_growth_yoy,
                        net_income, revenue, total_equity, total_debt,
                        report_date, publish_date, fiscal_period
        or None if no data available at trade_date.
    """
    _load_datasets()

    trade_date = pd.Timestamp(trade_date)

    # Filter income and balance for this ticker
    inc = _income_df[_income_df['Ticker'] == ticker].copy()
    bal = _balance_df[_balance_df['Ticker'] == ticker].copy()

    if inc.empty or bal.empty:
        return None

    # Only use filings published BEFORE or ON the trade date
    inc_available = inc[inc['Publish Date'] <= trade_date].sort_values('Report Date')
    bal_available = bal[bal['Publish Date'] <= trade_date].sort_values('Report Date')

    if inc_available.empty or bal_available.empty:
        return None

    # Most recent available quarter
    latest_inc = inc_available.iloc[-1]
    latest_bal = bal_available.iloc[-1]

    # Extract raw values
    net_income = latest_inc.get('Net Income')
    revenue = latest_inc.get('Revenue')
    total_equity = latest_bal.get('Total Equity')
    short_debt = latest_bal.get('Short Term Debt', 0) or 0
    long_debt = latest_bal.get('Long Term Debt', 0) or 0
    total_debt = short_debt + long_debt

    # Calculate ROE
    roe = None
    if _is_valid(net_income) and _is_valid(total_equity) and total_equity != 0:
        # Annualize quarterly net income (×4) for ROE
        roe = round((net_income * 4 / total_equity) * 100, 2)

    # Calculate D/E
    debt_equity = None
    if _is_valid(total_debt) and _is_valid(total_equity) and total_equity != 0:
        debt_equity = round(total_debt / abs(total_equity), 2)

    # Calculate YoY Revenue Growth
    # Need same quarter from prior year
    revenue_growth_yoy = _calc_yoy_growth(
        inc_available, 'Revenue', latest_inc
    )

    # Calculate YoY EPS Growth (using Net Income as proxy)
    eps_growth_yoy = _calc_yoy_growth(
        inc_available, 'Net Income', latest_inc
    )

    return {
        'roe': roe,
        'debt_equity': debt_equity,
        'revenue_growth_yoy': revenue_growth_yoy,
        'eps_growth_yoy': eps_growth_yoy,
        'net_income': net_income,
        'revenue': revenue,
        'total_equity': total_equity,
        'total_debt': total_debt,
        'report_date': str(latest_inc['Report Date'].date()) if pd.notna(latest_inc['Report Date']) else None,
        'publish_date': str(latest_inc['Publish Date'].date()) if pd.notna(latest_inc['Publish Date']) else None,
        'fiscal_year': latest_inc.get('Fiscal Year'),
        'fiscal_period': latest_inc.get('Fiscal Period'),
    }


def _calc_yoy_growth(df, field, latest_row):
    """
    Calculate Year-over-Year growth for a field.
    Compares latest quarter to same quarter one year earlier.
    Returns growth as percentage (e.g., 15.5 = 15.5%), or None.
    """
    current_val = latest_row.get(field)
    if not _is_valid(current_val):
        return None

    fiscal_year = latest_row.get('Fiscal Year')
    fiscal_period = latest_row.get('Fiscal Period')

    if fiscal_year is None or fiscal_period is None:
        return None

    # Find same quarter from prior year
    prior = df[
        (df['Fiscal Year'] == fiscal_year - 1) &
        (df['Fiscal Period'] == fiscal_period)
    ]

    if prior.empty:
        return None

    prior_val = prior.iloc[-1].get(field)
    if not _is_valid(prior_val) or prior_val == 0:
        return None

    growth = ((current_val - prior_val) / abs(prior_val)) * 100
    return round(growth, 2)


def _is_valid(val):
    """Check if a value is usable (not None, not NaN)."""
    if val is None:
        return False
    if isinstance(val, float) and np.isnan(val):
        return False
    return True


def get_available_tickers():
    """Return set of all tickers with SimFin data."""
    _load_datasets()
    return set(_income_df['Ticker'].unique())


def check_coverage(tickers, start_date='2020-01-01', end_date='2025-01-01'):
    """
    Check how many tickers have fundamental data coverage
    for the backtest period. Useful for planning.
    """
    _load_datasets()

    start = pd.Timestamp(start_date)
    end = pd.Timestamp(end_date)
    results = {}

    for ticker in tickers:
        inc = _income_df[_income_df['Ticker'] == ticker]
        if inc.empty:
            results[ticker] = {'covered': False, 'quarters': 0}
            continue

        in_range = inc[
            (inc['Publish Date'] >= start) &
            (inc['Publish Date'] <= end)
        ]
        results[ticker] = {
            'covered': len(in_range) >= 4,  # At least 1 year of quarters
            'quarters': len(in_range),
            'first_publish': str(in_range['Publish Date'].min().date()) if not in_range.empty else None,
            'last_publish': str(in_range['Publish Date'].max().date()) if not in_range.empty else None,
        }

    covered = sum(1 for v in results.values() if v['covered'])
    print(f"SimFin coverage: {covered}/{len(tickers)} tickers have ≥4 quarters in {start_date} to {end_date}")
    return results


# Quick test when run directly
if __name__ == '__main__':
    print("Testing SimFin loader...")

    # Test AAPL at a known date
    result = get_fundamentals_at_date('AAPL', '2024-06-01')
    if result:
        print(f"\nAAPL fundamentals as of 2024-06-01:")
        print(f"  ROE: {result['roe']}%")
        print(f"  D/E: {result['debt_equity']}")
        print(f"  Revenue Growth YoY: {result['revenue_growth_yoy']}%")
        print(f"  EPS Growth YoY: {result['eps_growth_yoy']}%")
        print(f"  Report Date: {result['report_date']} ({result['fiscal_year']} {result['fiscal_period']})")
        print(f"  Publish Date: {result['publish_date']}")
    else:
        print("No data for AAPL at 2024-06-01")

    # Test coverage for backtest tickers
    test_tickers = ['AAPL', 'MSFT', 'NVDA', 'JPM', 'HD', 'XOM', 'COIN', 'PLTR']
    check_coverage(test_tickers)
