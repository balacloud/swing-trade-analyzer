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
import random
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from providers import get_data_provider
from backtest.trade_simulator import simulate_trade, compute_entry_levels
from backtest.mr_simulator import simulate_mr_trade
from backtest.metrics import apply_transaction_costs

from paper_trading import ledger
from paper_trading import live_signals
from paper_trading.live_signals import _prepare_ohlcv
from mean_reversion import HUB_UNIVERSE

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
            df = _prepare_ohlcv(dp.get_ohlcv(ticker, period='2y'))
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
                # Day 95: Path A and Path B (see live_signals.py) share the
                # exact same exit-management formula — they only differ in
                # which entry gate decided to take the trade — so this
                # recompute is variant-agnostic, same as before.
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
            df = _prepare_ohlcv(dp.get_ohlcv(ticker, period='2y'))
            entry_idx = _find_index_for_date(df, row['entry_date'])
            if entry_idx is None:
                print(f"daily_job: entry_date {row['entry_date']} not in {ticker} history, skipping")
                continue

            if row['system'] == 'momentum':
                # Session 28 audit fix: replay against the stop/target
                # actually recorded at entry, not whatever compute_entry_levels()
                # would produce today — otherwise a future change to that
                # formula silently re-grades already-open positions with no
                # ledger trace of the change.
                result = simulate_trade(
                    df, entry_idx, row['holding_period'],
                    entry_price=row['entry_price'],
                    stop_price=row['initial_stop_price'],
                    target_price=row['initial_target_price'],
                    live_mode=True
                )
            else:
                # Same fix for MR: derive stop_pct from the stored
                # initial_stop_price/entry_price rather than the module
                # constant, and use the stored max_hold_days rather than
                # MR_MAX_DAYS, so a future constant change can't retroactively
                # alter positions already open under the old rule.
                stop_pct = 1 - (row['initial_stop_price'] / row['entry_price'])
                max_days = row['max_hold_days'] or MR_MAX_DAYS
                result = simulate_mr_trade(
                    df, entry_idx, stop_pct=stop_pct, max_days=max_days, live_mode=True
                )

            if result['status'] == 'closed':
                if row['system'] == 'momentum':
                    # Day 99 fix: mr_simulator already nets transaction costs
                    # (see mr_simulator.py's apply_transaction_costs call) but
                    # this branch was storing gross return_pct into BOTH
                    # pnl_pct and pnl_pct_gross — live momentum stats were
                    # measured gross against a net-costed PF 1.40 backtest
                    # benchmark. initial_risk_pct/return_r share the same
                    # relationship as pnl_pct/pnl_r (both divide the same
                    # price delta by entry_price), so scaling return_r by the
                    # net-costed pct keeps the R-multiple internally consistent.
                    costs = apply_transaction_costs(result['entry_price'], result['exit_price'])
                    net_pct = costs['net_return_pct']
                    initial_risk_pct = result.get('initial_risk_pct') or 0
                    net_r = round(net_pct / initial_risk_pct, 4) if initial_risk_pct else result['return_r']
                    ledger.close_position(
                        row['id'], result['exit_date'], result['exit_price'], result['exit_reason'],
                        result['result'], net_pct, result['return_pct'],
                        net_r, result['days_held']
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
               'queued_momentum': 0, 'queued_mr': 0, 'queued_mr_hub': 0}

    print("Step 1/3: activating pending signals...")
    summary['activated'] = activate_pending_signals()

    print("Step 2/3: stepping open positions...")
    closed, still_open = step_open_positions()
    summary['closed'] = closed
    summary['still_open'] = still_open

    print("Step 3/3: generating new signals from today's data...")
    momentum_signals = live_signals.get_momentum_signals(as_of_date=today)
    for s in momentum_signals:
        variant = s.get('variant', 'A_frozen')
        ledger.queue_pending_signal(
            'momentum', s['ticker'], s['signal_date'], s['signal_price'],
            holding_period=s['holding_period'], verdict_reason=s['verdict_reason'],
            regime_snapshot=s.get('regime_snapshot'), variant=variant
        )
        summary['queued_momentum'] += 1
        print(f"  queued momentum [{variant}]: {s['ticker']} — {s['verdict_reason']}")

    mr_signals = live_signals.get_mr_signals(as_of_date=today)
    for s in mr_signals:
        ledger.queue_pending_signal(
            'mr', s['ticker'], s['signal_date'], s['signal_price'],
            holding_period=s['holding_period'], verdict_reason=s['verdict_reason'],
            regime_snapshot=s.get('regime_snapshot'), variant=s.get('variant', 'A_frozen')
        )
        summary['queued_mr'] += 1
        print(f"  queued MR: {s['ticker']} — {s['verdict_reason']}")

    # Day 97: HUB-65 curated-universe MR track — same unchanged MR gate, a
    # different (smaller, thematically-concentrated) universe, tracked under
    # its own variant so it never touches the broad track's count above.
    # Iteration order is randomized per run (Golden Rule 25) — HUB runs last
    # in this job, after momentum's and the broad MR scan's rate budget is
    # already spent; a fixed order would silently starve the same tail
    # tickers every single day if a rate-limit cutoff ever trips mid-loop.
    hub_universe_shuffled = list(HUB_UNIVERSE)
    random.Random(today).shuffle(hub_universe_shuffled)
    mr_hub_signals = live_signals.get_mr_signals(
        as_of_date=today, tickers=hub_universe_shuffled, variant='mr_hub65'
    )
    for s in mr_hub_signals:
        ledger.queue_pending_signal(
            'mr', s['ticker'], s['signal_date'], s['signal_price'],
            holding_period=s['holding_period'], verdict_reason=s['verdict_reason'],
            regime_snapshot=s.get('regime_snapshot'), variant=s.get('variant', 'mr_hub65')
        )
        summary['queued_mr_hub'] += 1
        print(f"  queued MR [mr_hub65]: {s['ticker']} — {s['verdict_reason']}")

    ledger.record_job_run(today, summary)

    backup_path = ledger.backup_db()
    if backup_path:
        print(f"Ledger backed up to {backup_path}")

    print(f"=== Daily job complete: {summary} ===")
    return summary


def _print_variant_stats(system, variant, label):
    open_positions = ledger.get_open_positions(system=system, variant=variant)
    closed = ledger.get_closed_trades(system=system, variant=variant)
    stats = ledger.compute_stats(system=system, variant=variant)
    print(f"\n  --- {label} ---")
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


def print_report():
    ledger.init_db()
    print("\n=== MOMENTUM ===")
    _print_variant_stats('momentum', 'A_frozen', 'Path A (frozen, flat/ATR R:R proxy)')
    _print_variant_stats('momentum', 'B_revised_rr', 'Path B (real S&R-based R:R gate, Day 95)')

    print("\n=== MR ===")
    _print_variant_stats('mr', 'A_frozen', 'MR (unchanged — not part of the Path B experiment)')
    _print_variant_stats('mr', 'mr_hub65', 'MR — Curated HUB-65 (different universe, Day 97)')

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
