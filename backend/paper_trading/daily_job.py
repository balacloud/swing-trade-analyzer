"""
Daily Paper Trading Job — Automated Engine (Day 81)

Safe to run once per trading day (idempotent — checks job_runs before doing
anything). Three steps, in order:

  1. Activate pending signals: for every 'pending_entry' row, look up the
     actual trading day AFTER its signal_date in real OHLCV history and
     enter at that day's open. This is correct even after a multi-day gap
     (laptop asleep) — it uses the real historical bar for the day that
     should have been the entry, not "whatever day the job happens to run."

  2. Step every open position: a single fresh live_mode replay
     (trade_simulator.simulate_trade / mr_simulator.simulate_mr_trade) from
     entry_date to the latest available bar. This also self-heals through
     any number of missed days in one call — no explicit day-by-day loop
     needed, since live_mode replay is deterministic over history (Phase 1).

  3. Generate new signals from TODAY's live data only (live_signals.py).
     IMPORTANT LIMITATION: TradingView's screener and the live categorical
     assessment reflect the CURRENT market, not a queryable point-in-time
     snapshot of a past date. If the job misses several days, step 2 still
     correctly resolves what happened to positions that were already open,
     but step 3 cannot retroactively reconstruct what would have fired on
     the missed days — those entry signals are simply not generated. Keep
     this job running close to daily to minimize that gap.
"""
import sys
import os
import argparse
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from providers import get_data_provider
from backtest.trade_simulator import simulate_trade, compute_entry_levels
from backtest.mr_simulator import simulate_mr_trade

from paper_trading import ledger
from paper_trading import live_signals
from paper_trading.live_signals import _to_capitalized_ohlcv

MR_STOP_PCT = 0.05
MR_MAX_DAYS = 10


def _find_index_for_date(df, date_str):
    """Return the integer index of `date_str` in df's DatetimeIndex, or None."""
    dates = df.index.astype(str).str[:10].tolist()
    if date_str not in dates:
        return None
    return dates.index(date_str)


def activate_pending_signals():
    """Activate every pending_entry whose signal_date already has a
    following trading day in history. Returns count activated."""
    dp = get_data_provider()
    activated = 0

    for row in ledger.get_pending_signals():
        ticker = row['ticker']
        try:
            df = _to_capitalized_ohlcv(dp.get_ohlcv(ticker, period='2y'))
            signal_idx = _find_index_for_date(df, row['signal_date'])
            if signal_idx is None:
                print(f"daily_job: signal_date {row['signal_date']} not in {ticker} history yet, skipping")
                continue
            entry_idx = signal_idx + 1
            if entry_idx >= len(df):
                continue  # next trading day hasn't posted yet — try again next run

            entry_date = str(df.index[entry_idx].date())
            entry_price = float(df['Open'].iloc[entry_idx])

            if row['system'] == 'momentum':
                stop_price, target_price, max_hold = compute_entry_levels(
                    df, entry_idx, row['holding_period'], entry_price
                )
            else:  # mr — matches mr_simulator.backtest_mr_strategy()'s actual backtested exit params
                stop_price = entry_price * (1 - MR_STOP_PCT)
                target_price = None
                max_hold = MR_MAX_DAYS

            # regime_snapshot was already captured at signal time
            # (queue_pending_signal) — activate_position() preserves it.
            ledger.activate_position(
                row['id'], entry_date, entry_price, stop_price, target_price, max_hold
            )
            activated += 1
            print(f"  activated {ticker} ({row['system']}) at {entry_date} open=${entry_price:.2f}")
        except Exception as e:
            print(f"daily_job: activation failed for {ticker} (id={row['id']}): {e}")

    return activated


def step_open_positions():
    """Replay every open position from entry to the latest bar. Returns
    (closed_count, still_open_count)."""
    dp = get_data_provider()
    closed = 0
    still_open = 0

    for row in ledger.get_open_positions():
        ticker = row['ticker']
        try:
            df = _to_capitalized_ohlcv(dp.get_ohlcv(ticker, period='2y'))
            entry_idx = _find_index_for_date(df, row['entry_date'])
            if entry_idx is None:
                print(f"daily_job: entry_date {row['entry_date']} not in {ticker} history, skipping")
                continue

            if row['system'] == 'momentum':
                result = simulate_trade(
                    df, entry_idx, row['holding_period'],
                    entry_price=row['entry_price'], live_mode=True
                )
            else:
                result = simulate_mr_trade(
                    df, entry_idx, stop_pct=MR_STOP_PCT, max_days=MR_MAX_DAYS, live_mode=True
                )

            if result['status'] == 'closed':
                if row['system'] == 'momentum':
                    ledger.close_position(
                        row['id'], result['exit_date'], result['exit_price'], result['exit_reason'],
                        result['result'], result['return_pct'], result['return_pct'],
                        result['return_r'], result['days_held']
                    )
                else:
                    exit_date = str(df.index[result['exit_idx']].date())
                    result_label = 'win' if result['win'] else 'loss'
                    ledger.close_position(
                        row['id'], exit_date, result['exit_price'], result['exit_reason'],
                        result_label, result['pnl_pct_net'], result['pnl_pct'],
                        result['pnl_r_net'], result['hold_days']
                    )
                closed += 1
                print(f"  closed {ticker} ({row['system']}): {result.get('exit_reason')}")
            else:
                ledger.update_open_position(row['id'], result['days_held'], result['stop_price'])
                still_open += 1
        except Exception as e:
            print(f"daily_job: step failed for {ticker} (id={row['id']}): {e}")

    return closed, still_open


def run_daily_job(force=False):
    ledger.init_db()

    today = datetime.now().strftime('%Y-%m-%d')
    last_run = ledger.get_last_run_date()
    if last_run == today and not force:
        print(f"daily_job: already ran today ({today}) — skipping (idempotent). Pass force=True to override.")
        return None

    print(f"=== Paper Trading Daily Job — {today} ===")

    summary = {'run_date': today, 'activated': 0, 'closed': 0, 'still_open': 0,
               'queued_momentum': 0, 'queued_mr': 0}

    print("Step 1/3: activating pending signals...")
    summary['activated'] = activate_pending_signals()

    print("Step 2/3: stepping open positions...")
    closed, still_open = step_open_positions()
    summary['closed'] = closed
    summary['still_open'] = still_open

    print("Step 3/3: generating new signals from today's data...")
    momentum_signals = live_signals.get_momentum_signals(as_of_date=today)
    for s in momentum_signals:
        ledger.queue_pending_signal(
            'momentum', s['ticker'], s['signal_date'], s['signal_price'],
            holding_period=s['holding_period'], verdict_reason=s['verdict_reason'],
            regime_snapshot=s.get('regime_snapshot')
        )
        summary['queued_momentum'] += 1
        print(f"  queued momentum: {s['ticker']} — {s['verdict_reason']}")

    mr_signals = live_signals.get_mr_signals(as_of_date=today)
    for s in mr_signals:
        ledger.queue_pending_signal(
            'mr', s['ticker'], s['signal_date'], s['signal_price'],
            holding_period=s['holding_period'], verdict_reason=s['verdict_reason'],
            regime_snapshot=s.get('regime_snapshot')
        )
        summary['queued_mr'] += 1
        print(f"  queued MR: {s['ticker']} — {s['verdict_reason']}")

    ledger.record_job_run(today, summary)
    print(f"=== Daily job complete: {summary} ===")
    return summary


def print_report():
    ledger.init_db()
    for system in ('momentum', 'mr'):
        open_positions = ledger.get_open_positions(system=system)
        closed = ledger.get_closed_trades(system=system)
        stats = ledger.compute_stats(system=system)
        print(f"\n=== {system.upper()} ===")
        print(f"  Open positions: {len(open_positions)}")
        print(f"  Closed trades:  {stats['total_trades']}")
        if stats['total_trades'] > 0:
            print(f"  Win rate:       {stats['win_rate']}%")
            print(f"  Profit factor:  {stats['profit_factor']}")
            print(f"  Expectancy:     {stats['expectancy_pct']}%/trade")
            print(f"  Avg R-multiple: {stats['avg_r_multiple']}")
            slippages = [t['entry_slippage_pct'] for t in closed if t.get('entry_slippage_pct') is not None]
            if slippages:
                print(f"  Avg entry slippage: {sum(slippages)/len(slippages):.3f}%")
        else:
            print("  (no closed trades yet)")
    last_run = ledger.get_last_run_date()
    print(f"\nLast job run: {last_run or 'never'}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automated paper trading daily job')
    parser.add_argument('--report', action='store_true', help='Print ledger stats and exit')
    parser.add_argument('--force', action='store_true', help='Run even if already run today')
    args = parser.parse_args()

    if args.report:
        print_report()
    else:
        run_daily_job(force=args.force)
