"""
MR forward-test re-test at the next-day OPEN (Day 123).

Why: the paper-trading ledger recorded each MR entry at the entry day's
open, but daily_job.py replayed every trade through simulate_mr_trade(),
which prices the trade at the entry day's CLOSE and starts exits the day
after (mr_simulator.py:69). The stored PF 2.00 therefore measured
"buy at the close of the day after the signal", not "buy at the next open".
See docs/claude/design/ANALYZE_REDESIGN_STEP5_PLAN_DAY123.md §6 (prediction
pre-registered there before this ran: PF 1.5-1.7, wins 63-68%).

What it does, for every closed MR ledger trade (both variants):
  1. Close basis: simulate_mr_trade(df, entry_idx) unchanged. Must reproduce
     the stored pnl_pct — the harness check. Trades that don't reproduce are
     reported and excluded from both bases so the comparison is like-for-like.
     A second pair ("all trades") runs both bases on today's data for every
     trade, including those whose stored number came from different data
     (dividend-adjustment drift, and MNST's -50.8% stored loss, a split
     artifact in the ledger).
  2. Open basis: entry = Open[entry_idx], stop 5% below it. The entry day's
     own bar counts (its low can hit the stop; its close can trigger the
     RSI(2) > 70 exit). Later bars are gap-aware, same as mr_simulator. Time
     exit at the same bar as the close basis (entry_idx + max_days). Same
     transaction costs (metrics.apply_transaction_costs).

Usage: cd backend && venv/bin/python backtest/mr_open_entry_retest.py
"""
import json
import os
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from providers import get_data_provider
from mean_reversion import calculate_rsi_short
from backtest.mr_simulator import simulate_mr_trade
from backtest.metrics import apply_transaction_costs

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(BACKEND, 'validation_results', 'paper_trading_ledger.db')
OUT_DIR = os.path.join(BACKEND, 'validation_results')
STOP_PCT = 0.05
MAX_DAYS = 10
RSI2_EXIT = 70
REPRO_TOLERANCE = 0.02  # percentage points


def simulate_mr_open(df, entry_idx, stop_pct=STOP_PCT, max_days=MAX_DAYS):
    """Same exits as simulate_mr_trade, but entered at Open[entry_idx]."""
    entry_price = float(df['Open'].iloc[entry_idx])
    stop_price = entry_price * (1 - stop_pct)
    rsi2 = calculate_rsi_short(df['Close'], period=2)

    for day in range(0, max_days + 1):
        i = entry_idx + day
        if i >= len(df):
            return None  # not enough history after entry
        bar_open = float(df['Open'].iloc[i])
        bar_low = float(df['Low'].iloc[i])
        bar_close = float(df['Close'].iloc[i])
        if day > 0 and bar_open <= stop_price:
            exit_price, reason = bar_open, 'stop_hit_gap'
        elif bar_low <= stop_price:
            exit_price, reason = stop_price, 'stop_hit'
        elif float(rsi2.iloc[i]) > RSI2_EXIT:
            exit_price, reason = bar_close, 'rsi2_exit'
        elif day == max_days:
            exit_price, reason = bar_close, 'time_exit'
        else:
            continue
        net = apply_transaction_costs(entry_price, exit_price)['net_return_pct']
        return {'entry_price': entry_price, 'exit_price': exit_price, 'exit_reason': reason,
                'pnl_pct_net': net, 'hold_days': day}
    return None


def summarize(pnls):
    gains = sum(p for p in pnls if p > 0)
    losses = -sum(p for p in pnls if p < 0)
    return {
        'trades': len(pnls),
        'wins': sum(1 for p in pnls if p > 0),
        'win_pct': round(100 * sum(1 for p in pnls if p > 0) / len(pnls), 1) if pnls else None,
        'profit_factor': round(gains / losses, 2) if losses > 0 else None,
        'avg_pnl_pct': round(sum(pnls) / len(pnls), 3) if pnls else None,
    }


def main():
    con = sqlite3.connect(LEDGER)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT id, variant, ticker, signal_date, entry_date, entry_price, exit_price, exit_reason, pnl_pct "
        "FROM paper_positions WHERE system='mr' AND status='closed' ORDER BY ticker"
    ).fetchall()
    print(f"{len(rows)} closed MR trades in the ledger")

    by_ticker = defaultdict(list)
    for r in rows:
        by_ticker[r['ticker']].append(r)

    dp = get_data_provider()
    results = defaultdict(lambda: {'close': [], 'open': [], 'stored': [], 'open_exits': Counter(), 'skipped': [],
                                   'all_close': [], 'all_open': []})

    for n, (ticker, trades) in enumerate(sorted(by_ticker.items()), 1):
        try:
            df = dp.get_ohlcv(ticker, period='2y')
            df = df.copy()
            df.columns = [c.capitalize() for c in df.columns]
        except Exception as e:
            print(f"  ⚠️ {ticker}: data fetch failed ({e}); {len(trades)} trades skipped")
            for t in trades:
                results[t['variant']]['skipped'].append({'id': t['id'], 'ticker': ticker, 'why': 'fetch failed'})
            continue
        dates = df.index.astype(str).str[:10].tolist()
        for t in trades:
            bucket = results[t['variant']]
            if t['entry_date'] not in dates:
                bucket['skipped'].append({'id': t['id'], 'ticker': ticker, 'why': 'entry date not in data'})
                continue
            entry_idx = dates.index(t['entry_date'])
            close_res = simulate_mr_trade(df, entry_idx, stop_pct=STOP_PCT, max_days=MAX_DAYS)
            open_res = simulate_mr_open(df, entry_idx)
            # Both bases on today's data for EVERY trade (like-for-like even
            # where the ledger's stored number came from different data).
            if close_res and close_res.get('status') == 'closed' and open_res:
                bucket['all_close'].append(close_res['pnl_pct_net'])
                bucket['all_open'].append(open_res['pnl_pct_net'])
            else:
                print(f"  ⚠️ {ticker} id={t['id']}: excluded from the all-trades pair (a basis didn't close)")
            if not close_res or close_res.get('status') != 'closed' or \
                    abs(close_res['pnl_pct_net'] - t['pnl_pct']) > REPRO_TOLERANCE:
                bucket['skipped'].append({
                    'id': t['id'], 'ticker': ticker, 'why': 'close basis did not reproduce stored pnl',
                    'stored': t['pnl_pct'], 'replayed': close_res.get('pnl_pct_net') if close_res else None})
                continue
            if not open_res:
                bucket['skipped'].append({'id': t['id'], 'ticker': ticker, 'why': 'open basis ran out of data'})
                continue
            bucket['stored'].append(t['pnl_pct'])
            bucket['close'].append(close_res['pnl_pct_net'])
            bucket['open'].append(open_res['pnl_pct_net'])
            bucket['open_exits'][open_res['exit_reason']] += 1
        if n % 25 == 0:
            print(f"  {n}/{len(by_ticker)} tickers")
        time.sleep(0.3)  # pace provider calls

    report = {'generated': datetime.now().isoformat(timespec='seconds'), 'ledger': LEDGER, 'variants': {}}
    for variant, b in results.items():
        report['variants'][variant] = {
            'stored_all': summarize([r['pnl_pct'] for r in rows if r['variant'] == variant]),
            'reproduced_close_basis': summarize(b['close']),
            'open_basis': summarize(b['open']),
            'open_basis_exits': dict(b['open_exits']),
            'all_trades_close_basis': summarize(b['all_close']),
            'all_trades_open_basis': summarize(b['all_open']),
            'skipped': b['skipped'],
        }
        v = report['variants'][variant]
        print(f"\n[{variant}] stored (all): {v['stored_all']}")
        print(f"[{variant}] close basis (reproduced): {v['reproduced_close_basis']}")
        print(f"[{variant}] OPEN basis:               {v['open_basis']}  exits {v['open_basis_exits']}")
        print(f"[{variant}] skipped: {len(b['skipped'])}")
        print(f"[{variant}] ALL trades, today's data, close basis: {v['all_trades_close_basis']}")
        print(f"[{variant}] ALL trades, today's data, OPEN basis:  {v['all_trades_open_basis']}")

    out = os.path.join(OUT_DIR, f"mr_open_entry_retest_{datetime.now():%Y%m%d_%H%M%S}.json")
    with open(out, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nSaved {out}")


if __name__ == '__main__':
    main()
