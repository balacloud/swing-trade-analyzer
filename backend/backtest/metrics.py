"""
Backtest Metrics Calculator — v4.16 Holistic Backtest

Computes statistical metrics for trade results.
Benchmarks from Perplexity research (Feb 16, 2026):

| Metric         | Minimum | Target  | Red Flag      |
|----------------|---------|---------|---------------|
| Win Rate       | 45%     | 50-60%  | >70% overfit  |
| Expectancy     | >$0     | $75-125 | Negative      |
| Profit Factor  | >1.3    | >1.75   | <1.0          |
| Sharpe Ratio   | >0.8    | >1.2    | >2.0 unreal   |
| Max Drawdown   | —       | <15%    | >25%          |
| R-Multiple     | >1.5    | >2.5    | <1.0          |
"""

import math
import random
from collections import defaultdict
from datetime import datetime

# Day 78 (Fable Remediation Task 2.3): prefer scipy's t-test over the
# hand-rolled p-value approximation; fall back only if scipy is unavailable.
try:
    from scipy import stats as _scipy_stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False


# Transaction cost model
SLIPPAGE_PER_SHARE = 0.005  # $0.005/share each way
COMMISSION_PER_TRADE = 1.00  # $1.00 each way


def apply_transaction_costs(entry_price, exit_price, shares=100):
    """
    Apply realistic transaction costs.

    Slippage: $0.005/share on both entry and exit
    Commission: $1.00 per trade (both sides)

    Returns:
        dict with net_entry, net_exit, total_cost, net_return_pct
    """
    net_entry = entry_price + SLIPPAGE_PER_SHARE  # Buy slightly higher
    net_exit = exit_price - SLIPPAGE_PER_SHARE     # Sell slightly lower

    total_slippage = SLIPPAGE_PER_SHARE * 2 * shares
    total_commission = COMMISSION_PER_TRADE * 2
    total_cost = total_slippage + total_commission

    gross_pnl = (exit_price - entry_price) * shares
    net_pnl = gross_pnl - total_cost

    net_return_pct = (net_pnl / (entry_price * shares)) * 100

    return {
        'net_entry': net_entry,
        'net_exit': net_exit,
        'total_cost': round(total_cost, 2),
        'gross_pnl': round(gross_pnl, 2),
        'net_pnl': round(net_pnl, 2),
        'net_return_pct': round(net_return_pct, 4),
    }


def compute_metrics(trades, risk_free_rate=0.05):
    """
    Compute all backtest metrics from a list of trade results.

    Args:
        trades: list of dicts, each with at minimum:
            - return_pct: percentage return (e.g., 5.0 = 5%)
            - return_pct_net: return after transaction costs
            - return_r: R-multiple (profit / initial risk)
            - days_held: number of days position was held
            - result: 'win', 'loss', or 'breakeven'
            - exit_reason: why the trade exited
            - regime: market regime at entry ('bull', 'bear', 'sideways')
            - config: which config generated the trade ('A', 'B', 'C')
        risk_free_rate: annual risk-free rate (default 5%)

    Returns:
        dict with all computed metrics + sanity warnings
    """
    if not trades:
        return _empty_metrics()

    n = len(trades)

    # Basic counts
    wins = [t for t in trades if t.get('result') == 'win']
    losses = [t for t in trades if t.get('result') == 'loss']
    breakevens = [t for t in trades if t.get('result') == 'breakeven']

    win_count = len(wins)
    loss_count = len(losses)

    # Win rate
    win_rate = (win_count / n) * 100 if n > 0 else 0

    # Returns
    returns = [t.get('return_pct_net', t.get('return_pct', 0)) for t in trades]
    win_returns = [t.get('return_pct_net', t.get('return_pct', 0)) for t in wins]
    loss_returns = [t.get('return_pct_net', t.get('return_pct', 0)) for t in losses]

    avg_return = _mean(returns) if returns else 0
    avg_winner = _mean(win_returns) if win_returns else 0
    avg_loser = _mean(loss_returns) if loss_returns else 0

    # R-multiples
    r_multiples = [t.get('return_r', 0) for t in trades if t.get('return_r') is not None]
    avg_r = _mean(r_multiples) if r_multiples else 0
    median_r = _median(r_multiples) if r_multiples else 0

    # Expectancy (average net return per trade in dollars, assuming $10k position)
    position_size = 10000
    expectancy_pct = avg_return  # per trade
    expectancy_dollar = (expectancy_pct / 100) * position_size

    # Profit Factor = gross profits / gross losses
    gross_profit = sum(r for r in returns if r > 0)
    gross_loss = abs(sum(r for r in returns if r < 0))
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float('inf')

    # Day 78 (Fable Remediation Task 2.3): actual trade frequency from data,
    # replacing the hardcoded 25 trades/year assumption in Sharpe/Sortino.
    trades_per_year_actual = _compute_trades_per_year(trades)

    # Sharpe Ratio (annualized)
    sharpe = _compute_sharpe(returns, risk_free_rate, trades_per_year_actual)

    # Sortino Ratio (annualized, only downside deviation)
    sortino = _compute_sortino(returns, risk_free_rate, trades_per_year_actual)

    # Max Drawdown (sequential equity curve, chronologically sorted)
    # Day 78: relabeled — this compounds the FULL trade return at 100% of
    # equity per trade. It is neither a realistic portfolio DD nor a
    # per-trade DD; it's an artifact of pooling trades this way. Kept for
    # continuity, but `max_drawdown_fixed_risk_pct` below is the more honest
    # figure (fixed 2% risk per trade, Van Tharp sizing).
    sorted_trades = sorted(trades, key=lambda t: t.get('entry_date', ''))
    sorted_returns = [t.get('return_pct_net', t.get('return_pct', 0)) for t in sorted_trades]
    max_dd_pct = _compute_max_drawdown(sorted_returns)
    max_dd_fixed_risk_pct = _compute_max_drawdown_fixed_risk(sorted_trades)

    # Consecutive wins/losses
    max_consec_wins, max_consec_losses = _compute_streaks(trades)

    # Days held
    days_held = [t.get('days_held', 0) for t in trades]
    avg_days = _mean(days_held) if days_held else 0

    # Exit reason breakdown
    exit_reasons = defaultdict(int)
    for t in trades:
        exit_reasons[t.get('exit_reason', 'unknown')] += 1

    # Regime breakdown
    regime_metrics = _compute_regime_breakdown(trades)

    # R-multiple distribution (buckets)
    r_distribution = _compute_r_distribution(r_multiples)

    # T-test: is the mean return statistically different from zero?
    # Day 78: this assumes i.i.d. trades — violated when trades cluster by
    # regime/correlated tickers, so treat this as an upper bound on
    # significance, not the robust number. See block bootstrap below.
    t_stat, t_pvalue = _compute_t_test(returns)

    # Day 78 (Fable Remediation Task 2.3): block bootstrap p-value — resamples
    # whole calendar-month blocks (not individual trades) to preserve
    # within-month correlation structure. Reports fraction of resampled means
    # <= 0 as an empirical one-tailed p-value. None if too few distinct months.
    bootstrap_pvalue = _compute_block_bootstrap_pvalue(trades)

    # Sanity check warnings
    warnings = _sanity_checks(win_rate, sharpe, max_dd_pct, n, profit_factor)

    return {
        'total_trades': n,
        'wins': win_count,
        'losses': loss_count,
        'breakevens': len(breakevens),
        'win_rate': round(win_rate, 2),
        'avg_return_pct': round(avg_return, 4),
        'avg_winner_pct': round(avg_winner, 4),
        'avg_loser_pct': round(avg_loser, 4),
        'expectancy_pct': round(expectancy_pct, 4),
        'expectancy_dollar': round(expectancy_dollar, 2),
        'profit_factor': round(profit_factor, 4) if profit_factor != float('inf') else 'inf',
        'sharpe_ratio': round(sharpe, 4) if sharpe is not None else None,
        'sortino_ratio': round(sortino, 4) if sortino is not None else None,
        'max_drawdown_pct': round(max_dd_pct, 4),  # sequential 100%-equity DD — see note above
        'sequential_100pct_equity_dd_pct': round(max_dd_pct, 4),  # Day 78: explicit alias, same value
        'max_drawdown_fixed_risk_pct': round(max_dd_fixed_risk_pct, 4) if max_dd_fixed_risk_pct is not None else None,  # Day 78: honest 2%-risk-per-trade DD
        'avg_r_multiple': round(avg_r, 4),
        'median_r_multiple': round(median_r, 4),
        'r_distribution': r_distribution,
        'max_consecutive_wins': max_consec_wins,
        'max_consecutive_losses': max_consec_losses,
        'avg_days_held': round(avg_days, 1),
        'exit_reasons': dict(exit_reasons),
        'regime_breakdown': regime_metrics,
        'trades_per_year_actual': round(trades_per_year_actual, 1),  # Day 78: replaces hardcoded 25 in Sharpe/Sortino
        't_statistic': round(t_stat, 4) if t_stat is not None else None,
        't_pvalue': round(t_pvalue, 6) if t_pvalue is not None else None,  # kept for backward compat
        't_pvalue_iid_assumption': round(t_pvalue, 6) if t_pvalue is not None else None,  # Day 78: explicit label — assumes i.i.d. trades
        't_pvalue_block_bootstrap': round(bootstrap_pvalue, 6) if bootstrap_pvalue is not None else None,  # Day 78: robust to trade clustering
        't_significant': t_pvalue < 0.05 if t_pvalue is not None else None,
        'warnings': warnings,
    }


def _compute_sharpe(returns_pct, risk_free_rate, trades_per_year=25):
    """
    Annualized Sharpe ratio from per-trade percentage returns.

    Day 78 (Fable Remediation Task 2.3): trades_per_year now defaults to the
    actual observed frequency (see _compute_trades_per_year), replacing the
    previous hardcoded assumption of 25 trades/year regardless of real data.
    """
    if len(returns_pct) < 2:
        return None

    mean_return = _mean(returns_pct) / 100
    std_return = _stdev(returns_pct) / 100

    if std_return == 0:
        return None

    rf_per_trade = risk_free_rate / trades_per_year
    excess_return = mean_return - rf_per_trade

    sharpe = (excess_return / std_return) * math.sqrt(trades_per_year)
    return sharpe


def _compute_sortino(returns_pct, risk_free_rate, trades_per_year=25):
    """Annualized Sortino ratio (downside deviation only). See _compute_sharpe re: trades_per_year."""
    if len(returns_pct) < 2:
        return None

    rf_per_trade = risk_free_rate / trades_per_year

    mean_return = _mean(returns_pct) / 100
    excess_return = mean_return - rf_per_trade

    # Downside returns only
    downside = [r / 100 for r in returns_pct if r < 0]
    if not downside:
        return None  # No losing trades → can't compute

    downside_dev = math.sqrt(_mean([d ** 2 for d in downside]))

    if downside_dev == 0:
        return None

    sortino = (excess_return / downside_dev) * math.sqrt(trades_per_year)
    return sortino


def _compute_max_drawdown(returns_pct):
    """
    Sequential 100%-equity drawdown (starting at $10,000).

    NOTE (Day 78, Fable Remediation Task 2.3): this compounds each trade's
    FULL return at 100% of equity, one after another — it is neither a
    realistic portfolio drawdown (no diversification/concurrency modeled)
    nor a genuine per-trade drawdown. It's a modeling artifact of pooling
    trades this way. See _compute_max_drawdown_fixed_risk for a more honest
    figure that sizes each trade at a fixed % risk of equity.
    """
    if not returns_pct:
        return 0

    equity = 10000
    peak = equity
    max_dd = 0

    for r in returns_pct:
        equity *= (1 + r / 100)
        if equity > peak:
            peak = equity
        dd = (peak - equity) / peak * 100
        if dd > max_dd:
            max_dd = dd

    return max_dd


def _compute_max_drawdown_fixed_risk(sorted_trades, risk_pct=2.0):
    """
    Day 78 (Fable Remediation Task 2.3): honest per-trade-risk drawdown.

    Sizes every trade at a fixed risk_pct of equity (default 2%, Van Tharp),
    scaled by the trade's R-multiple, compounded in entry-date order — the
    drawdown a trader who risks a fixed % per trade would actually see.

    Args:
        sorted_trades: trades already sorted by entry_date (ascending).
        risk_pct: fixed risk per trade as % of equity (default 2.0).

    Returns:
        Max drawdown %, or None if no trades have a usable return_r.
    """
    r_multiples = [t.get('return_r') for t in sorted_trades if t.get('return_r') is not None]
    if not r_multiples:
        return None

    equity = 10000
    peak = equity
    max_dd = 0

    for r in r_multiples:
        equity *= (1 + (r * risk_pct / 100))
        if equity > peak:
            peak = equity
        dd = (peak - equity) / peak * 100
        if dd > max_dd:
            max_dd = dd

    return max_dd


def _compute_trades_per_year(trades):
    """
    Day 78 (Fable Remediation Task 2.3): actual trade frequency from data.

    Replaces the previous hardcoded assumption of 25 trades/year used in
    Sharpe/Sortino regardless of the backtest's real holding periods or
    trade count. Computed from the span between the earliest entry_date and
    the latest exit_date across all trades.

    Returns 25 (the old default) as a graceful fallback when dates are
    missing or the span is degenerate (e.g. a single-day backtest).
    """
    FALLBACK = 25
    dates = []
    for t in trades:
        for key in ('entry_date', 'exit_date'):
            val = t.get(key)
            if val:
                try:
                    dates.append(datetime.strptime(val, '%Y-%m-%d'))
                except (ValueError, TypeError):
                    pass

    if len(dates) < 2:
        return FALLBACK

    span_days = (max(dates) - min(dates)).days
    span_years = span_days / 365.25

    if span_years <= 0:
        return FALLBACK

    return len(trades) / span_years


def _compute_block_bootstrap_pvalue(trades, n_resamples=10000, seed=42):
    """
    Day 78 (Fable Remediation Task 2.3): block bootstrap p-value.

    The plain t-test (_compute_t_test) assumes i.i.d. trades. In practice,
    trades cluster by market regime and by correlated tickers entering
    around the same time — the effective sample size is smaller than the
    raw trade count, so the t-test's p-value is overstated.

    This resamples whole calendar-month blocks (grouping trades by
    entry_date's year-month), with replacement, preserving whatever
    within-month correlation exists. Reports the fraction of resampled
    means <= 0 as an empirical one-tailed p-value: "if the true edge were
    zero or negative, how often would resampling produce a mean this low
    or lower" — reversed here to report how often resampled means fall
    at/below zero directly.

    Returns None if there are fewer than 2 distinct months (can't
    meaningfully block-resample from a single block).
    """
    blocks = {}
    for t in trades:
        entry = t.get('entry_date')
        ret = t.get('return_pct_net', t.get('return_pct', 0))
        month_key = entry[:7] if entry else 'unknown'  # 'YYYY-MM'
        blocks.setdefault(month_key, []).append(ret)

    block_list = list(blocks.values())
    if len(block_list) < 2:
        return None

    rng = random.Random(seed)
    n_below_zero = 0

    for _ in range(n_resamples):
        sampled_blocks = [rng.choice(block_list) for _ in range(len(block_list))]
        pooled = [r for block in sampled_blocks for r in block]
        if pooled and _mean(pooled) <= 0:
            n_below_zero += 1

    return n_below_zero / n_resamples


def _compute_t_test(returns_pct):
    """
    One-sample t-test: is the mean return significantly different from zero?

    t = mean(returns) * sqrt(n) / stdev(returns)
    p-value approximated using the t-distribution.

    t > 1.645: preliminary evidence of edge (p < 0.05 one-tailed)
    t > 1.96:  significant at 95% confidence (p < 0.025 one-tailed)
    t > 2.576: significant at 99% confidence

    Returns (t_stat, p_value) or (None, None) if insufficient data.
    """
    if len(returns_pct) < 10:
        return None, None

    n = len(returns_pct)
    mean_r = _mean(returns_pct)
    std_r = _stdev(returns_pct)

    if std_r == 0:
        return None, None

    # Day 78 (Fable Remediation Task 2.3): prefer scipy's exact t-distribution
    # CDF over the hand-rolled normal-CDF approximation. Fallback only if
    # scipy is unavailable in the running environment.
    if SCIPY_AVAILABLE:
        t_stat, p_value = _scipy_stats.ttest_1samp(returns_pct, popmean=0)
        return float(t_stat), float(p_value)

    t_stat = mean_r * math.sqrt(n) / std_r
    df = n - 1

    # Approximate two-tailed p-value using the incomplete beta function
    # For large df (>30), t-distribution ≈ normal
    # Use a simple approximation via the normal CDF
    p_value = _t_distribution_pvalue(t_stat, df)

    return t_stat, p_value


def _t_distribution_pvalue(t, df):
    """
    Approximate two-tailed p-value for t-distribution.
    Uses the normal approximation for df > 30, otherwise
    uses a reasonable approximation.
    """
    # For df > 30, normal approximation is close enough
    abs_t = abs(t)

    # Standard normal CDF approximation (Abramowitz and Stegun 26.2.17)
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429

    x = abs_t / math.sqrt(2)
    t_val = 1.0 / (1.0 + p * x)
    erf_approx = 1.0 - (a1 * t_val + a2 * t_val**2 + a3 * t_val**3
                         + a4 * t_val**4 + a5 * t_val**5) * math.exp(-x * x)

    # Two-tailed p-value from normal CDF
    normal_p = 1.0 - erf_approx  # this is 2 * (1 - Phi(|t|))

    # Adjust for t-distribution (heavier tails) when df < 30
    if df < 30:
        # Crude correction factor: multiply p by (1 + 1/df)
        normal_p *= (1 + 1.0 / df)

    return min(normal_p, 1.0)


def _compute_streaks(trades):
    """Max consecutive wins and losses."""
    max_wins = 0
    max_losses = 0
    current_wins = 0
    current_losses = 0

    for t in trades:
        if t.get('result') == 'win':
            current_wins += 1
            current_losses = 0
            max_wins = max(max_wins, current_wins)
        elif t.get('result') == 'loss':
            current_losses += 1
            current_wins = 0
            max_losses = max(max_losses, current_losses)
        else:
            current_wins = 0
            current_losses = 0

    return max_wins, max_losses


def _compute_regime_breakdown(trades):
    """Metrics broken down by market regime."""
    regimes = defaultdict(list)
    for t in trades:
        regime = t.get('regime', 'unknown')
        regimes[regime].append(t)

    result = {}
    for regime, regime_trades in regimes.items():
        n = len(regime_trades)
        wins = sum(1 for t in regime_trades if t.get('result') == 'win')
        returns = [t.get('return_pct_net', t.get('return_pct', 0)) for t in regime_trades]

        result[regime] = {
            'trades': n,
            'win_rate': round((wins / n) * 100, 2) if n > 0 else 0,
            'avg_return': round(_mean(returns), 4) if returns else 0,
            'total_return': round(sum(returns), 4),
        }

    return result


def _compute_r_distribution(r_multiples):
    """R-multiple distribution in buckets."""
    if not r_multiples:
        return {}

    buckets = {
        'big_loss_below_neg2': 0,
        'loss_neg2_to_neg1': 0,
        'small_loss_neg1_to_0': 0,
        'breakeven_0_to_0.5': 0,
        'small_win_0.5_to_1': 0,
        'win_1_to_2': 0,
        'big_win_2_to_3': 0,
        'home_run_above_3': 0,
    }

    for r in r_multiples:
        if r < -2:
            buckets['big_loss_below_neg2'] += 1
        elif r < -1:
            buckets['loss_neg2_to_neg1'] += 1
        elif r < 0:
            buckets['small_loss_neg1_to_0'] += 1
        elif r < 0.5:
            buckets['breakeven_0_to_0.5'] += 1
        elif r < 1:
            buckets['small_win_0.5_to_1'] += 1
        elif r < 2:
            buckets['win_1_to_2'] += 1
        elif r < 3:
            buckets['big_win_2_to_3'] += 1
        else:
            buckets['home_run_above_3'] += 1

    return buckets


def _sanity_checks(win_rate, sharpe, max_dd, n_trades, profit_factor):
    """Flag suspicious results."""
    warnings = []

    if win_rate > 70:
        warnings.append(f"Win rate {win_rate:.1f}% > 70% — likely overfitting")
    if sharpe is not None and sharpe > 2.0:
        warnings.append(f"Sharpe {sharpe:.2f} > 2.0 — unrealistic for retail swing")
    if max_dd < 5 and n_trades > 50:
        warnings.append(f"Max DD {max_dd:.1f}% < 5% — insufficient sample or cherry-picked")
    if n_trades < 30:
        warnings.append(f"Only {n_trades} trades — insufficient for statistical significance")
    if profit_factor != float('inf') and profit_factor > 5.0:
        warnings.append(f"Profit factor {profit_factor:.2f} > 5.0 — suspiciously high")

    return warnings


def _empty_metrics():
    """Return empty metrics dict when no trades."""
    return {
        'total_trades': 0,
        'wins': 0,
        'losses': 0,
        'breakevens': 0,
        'win_rate': 0,
        'avg_return_pct': 0,
        'avg_winner_pct': 0,
        'avg_loser_pct': 0,
        'expectancy_pct': 0,
        'expectancy_dollar': 0,
        'profit_factor': 0,
        'sharpe_ratio': None,
        'sortino_ratio': None,
        'max_drawdown_pct': 0,
        'sequential_100pct_equity_dd_pct': 0,
        'max_drawdown_fixed_risk_pct': None,
        'avg_r_multiple': 0,
        'median_r_multiple': 0,
        'r_distribution': {},
        'max_consecutive_wins': 0,
        'max_consecutive_losses': 0,
        'avg_days_held': 0,
        'exit_reasons': {},
        'regime_breakdown': {},
        'trades_per_year_actual': 0,
        't_statistic': None,
        't_pvalue': None,
        't_pvalue_iid_assumption': None,
        't_pvalue_block_bootstrap': None,
        't_significant': None,
        'warnings': ['No trades to analyze'],
    }


# --- Pure math helpers (no numpy dependency) ---

def _mean(values):
    return sum(values) / len(values) if values else 0


def _stdev(values):
    if len(values) < 2:
        return 0
    m = _mean(values)
    variance = sum((x - m) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)


def _median(values):
    if not values:
        return 0
    s = sorted(values)
    n = len(s)
    if n % 2 == 0:
        return (s[n // 2 - 1] + s[n // 2]) / 2
    return s[n // 2]


# --- Quick test ---

if __name__ == '__main__':
    # Synthetic trades for validation
    test_trades = [
        {'return_pct': 8.0, 'return_pct_net': 7.8, 'return_r': 2.5, 'days_held': 10,
         'result': 'win', 'exit_reason': 'target_hit', 'regime': 'bull', 'config': 'A'},
        {'return_pct': -3.5, 'return_pct_net': -3.7, 'return_r': -1.0, 'days_held': 5,
         'result': 'loss', 'exit_reason': 'stop_hit', 'regime': 'bull', 'config': 'A'},
        {'return_pct': 12.0, 'return_pct_net': 11.8, 'return_r': 3.2, 'days_held': 15,
         'result': 'win', 'exit_reason': 'target_hit', 'regime': 'bull', 'config': 'B'},
        {'return_pct': -5.0, 'return_pct_net': -5.2, 'return_r': -1.0, 'days_held': 3,
         'result': 'loss', 'exit_reason': 'stop_hit', 'regime': 'sideways', 'config': 'B'},
        {'return_pct': 6.0, 'return_pct_net': 5.8, 'return_r': 1.8, 'days_held': 8,
         'result': 'win', 'exit_reason': 'target_hit', 'regime': 'bull', 'config': 'C'},
        {'return_pct': -4.0, 'return_pct_net': -4.2, 'return_r': -1.0, 'days_held': 7,
         'result': 'loss', 'exit_reason': 'stop_hit', 'regime': 'bear', 'config': 'C'},
        {'return_pct': 15.0, 'return_pct_net': 14.8, 'return_r': 4.0, 'days_held': 20,
         'result': 'win', 'exit_reason': 'target_hit', 'regime': 'bull', 'config': 'C'},
        {'return_pct': 1.0, 'return_pct_net': 0.8, 'return_r': 0.3, 'days_held': 12,
         'result': 'breakeven', 'exit_reason': 'max_hold', 'regime': 'sideways', 'config': 'A'},
    ]

    m = compute_metrics(test_trades)

    print("Metrics Calculator — Test Output")
    print("=" * 50)
    print(f"  Trades:          {m['total_trades']} ({m['wins']}W / {m['losses']}L / {m['breakevens']}BE)")
    print(f"  Win Rate:        {m['win_rate']}%")
    print(f"  Avg Return:      {m['avg_return_pct']}%")
    print(f"  Avg Winner:      {m['avg_winner_pct']}%")
    print(f"  Avg Loser:       {m['avg_loser_pct']}%")
    print(f"  Expectancy:      ${m['expectancy_dollar']}/trade")
    print(f"  Profit Factor:   {m['profit_factor']}")
    print(f"  Sharpe:          {m['sharpe_ratio']}")
    print(f"  Sortino:         {m['sortino_ratio']}")
    print(f"  Max Drawdown:    {m['max_drawdown_pct']}%")
    print(f"  Avg R-Multiple:  {m['avg_r_multiple']}")
    print(f"  Avg Days Held:   {m['avg_days_held']}")
    print(f"  Max Consec Wins: {m['max_consecutive_wins']}")
    print(f"  Max Consec Loss: {m['max_consecutive_losses']}")
    print(f"  Exit Reasons:    {dict(m['exit_reasons'])}")
    print(f"  Regime Breakdown: {dict(m['regime_breakdown'])}")
    print(f"  R-Distribution:  {m['r_distribution']}")
    if m['warnings']:
        print(f"  WARNINGS:        {m['warnings']}")
    else:
        print(f"  Warnings:        None (all clean)")

    # Verify basic math
    assert m['total_trades'] == 8
    assert m['wins'] == 4
    assert m['losses'] == 3
    assert m['win_rate'] == 50.0
    print("\nBasic assertions PASSED")
