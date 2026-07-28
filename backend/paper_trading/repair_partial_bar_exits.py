"""
One-time repair for the Day 99 partial-bar contamination bug — see
docs/claude/design/PARTIAL_BAR_LEDGER_CONTAMINATION_FIX_PLAN.md for the full
diagnosis. Some closed `paper_positions` rows were written from a mid-session
`--force`/Force-Run-Now run and recorded an intraday, not-yet-final price as
that day's closing price.

Re-replays every closed row against now-complete history using the exact same
simulator call the daily job's step_open_positions() already makes, with the
ledger's own stored entry_price/initial_stop_price/initial_target_price/
max_hold_days as inputs (Golden Rule 29 — anchor to what was actually decided
at entry, don't recompute those). Reports any row whose replay differs from
what's stored, and — only with --apply — corrects it.

PREREQUISITE: the live_signals._prepare_ohlcv() incomplete-bar guard (Day 99
Phase 1) must already be deployed, or this repair will read the same partial
bars that caused the original contamination and produce a fresh wrong answer.

Usage:
    python repair_partial_bar_exits.py            # dry-run, prints diff only
    python repair_partial_bar_exits.py --apply     # writes corrections + audit trail
"""
import sys
import os
import json
import argparse
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/

from providers import get_data_provider
from paper_trading import ledger
from paper_trading.live_signals import _prepare_ohlcv
from paper_trading.daily_job import _find_index_for_date
from backtest.trade_simulator import simulate_trade
from backtest.mr_simulator import simulate_mr_trade

AUDIT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'validation_results'
)


def _replay_row(dp, row):
    """
    Re-run the same exit logic on complete history using the row's own stored
    entry values. Returns a normalized dict (status='closed'|'open'), or None
    if entry_date can't be resolved in the fetched history at all.
    """
    period = '1y' if row['system'] == 'mr' else '2y'
    df = _prepare_ohlcv(dp.get_ohlcv(row['ticker'], period=period))
    entry_idx = _find_index_for_date(df, row['entry_date'])
    if entry_idx is None:
        return None

    if row['system'] == 'momentum':
        res = simulate_trade(
            df, entry_idx, row['holding_period'],
            entry_price=row['entry_price'],
            stop_price=row['initial_stop_price'],
            target_price=row['initial_target_price'],
            live_mode=True
        )
        if res['status'] != 'closed':
            return {'status': 'open', 'days_held': res['days_held'], 'stop_price': res['stop_price']}
        return {
            'status': 'closed',
            'exit_date': res['exit_date'],
            'exit_price': res['exit_price'],
            'exit_reason': res['exit_reason'],
            'result': res['result'],
            'pnl_pct': res['return_pct'],
            'pnl_pct_gross': res['return_pct'],  # momentum's gross/net split is Phase 4, not this repair
            'pnl_r': res['return_r'],
            'days_held': res['days_held'],
        }
    else:  # mr
        stop_pct = 1 - (row['initial_stop_price'] / row['entry_price'])
        max_days = row['max_hold_days'] or 10
        res = simulate_mr_trade(df, entry_idx, stop_pct=stop_pct, max_days=max_days, live_mode=True)
        if res['status'] != 'closed':
            return {'status': 'open', 'days_held': res['days_held'], 'stop_price': res['stop_price']}
        dates = df.index.astype(str).str[:10].tolist()
        return {
            'status': 'closed',
            'exit_date': dates[res['exit_idx']],
            'exit_price': res['exit_price'],
            'exit_reason': res['exit_reason'],
            'result': 'win' if res['win'] else 'loss',
            'pnl_pct': res['pnl_pct_net'],
            'pnl_pct_gross': res['pnl_pct'],
            'pnl_r': res['pnl_r_net'],
            'days_held': res['hold_days'],
        }


def _differs(row, replay):
    if replay['status'] == 'open':
        return True
    return (
        replay['exit_date'] != row['exit_date']
        or replay['exit_reason'] != row['exit_reason']
        or round(float(replay['pnl_pct']), 2) != round(float(row['pnl_pct']), 2)
    )


def _apply_closed_update(position_id, replay, db_path=None):
    conn = ledger._connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        UPDATE paper_positions
        SET exit_date = ?, exit_price = ?, exit_reason = ?, result = ?,
            pnl_pct = ?, pnl_pct_gross = ?, pnl_r = ?, days_held = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (replay['exit_date'], replay['exit_price'], replay['exit_reason'], replay['result'],
          replay['pnl_pct'], replay['pnl_pct_gross'], replay['pnl_r'], replay['days_held'], position_id))
    conn.commit()
    conn.close()


def _apply_reopen(position_id, replay, db_path=None):
    conn = ledger._connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        UPDATE paper_positions
        SET status = 'open', exit_date = NULL, exit_price = NULL, exit_reason = NULL,
            result = NULL, pnl_pct = NULL, pnl_pct_gross = NULL, pnl_r = NULL,
            days_held = ?, current_stop_price = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (replay['days_held'], replay['stop_price'], position_id))
    conn.commit()
    conn.close()


def run(apply=False, db_path=None):
    ledger.init_db(db_path)

    backup_path = ledger.backup_db(db_path=db_path)
    print(f"Backup: {backup_path}\n")

    conn = ledger._connect(db_path)
    conn.row_factory = __import__('sqlite3').Row
    rows = [dict(r) for r in conn.execute(
        "SELECT * FROM paper_positions WHERE status = 'closed' ORDER BY id"
    ).fetchall()]
    conn.close()

    dp = get_data_provider()
    diffs = []
    unresolved = []

    print(f"{'ID':>4} {'SYS':9s} {'TICKER':7s} {'LEDGER exit':>22s} {'pnl%':>7s}  ->  {'REPLAY exit':>22s} {'pnl%':>7s}")
    for row in rows:
        replay = _replay_row(dp, row)
        if replay is None:
            unresolved.append(row)
            print(f"{row['id']:>4} {row['system']:9s} {row['ticker']:7s}  entry_date not resolvable in fetched history — SKIPPED")
            time.sleep(0.3)
            continue

        if _differs(row, replay):
            diffs.append((row, replay))
            if replay['status'] == 'open':
                print(f"{row['id']:>4} {row['system']:9s} {row['ticker']:7s} "
                      f"{row['exit_date']:>10s} {row['exit_reason']:11s} {row['pnl_pct']:>+6.2f}  ->  "
                      f"{'STILL OPEN':>22s} {'':>7s}")
            else:
                print(f"{row['id']:>4} {row['system']:9s} {row['ticker']:7s} "
                      f"{row['exit_date']:>10s} {row['exit_reason']:11s} {row['pnl_pct']:>+6.2f}  ->  "
                      f"{replay['exit_date']:>10s} {replay['exit_reason']:11s} {replay['pnl_pct']:>+6.2f}")
        time.sleep(0.3)

    print(f"\n{'='*90}")
    print(f"Total closed: {len(rows)}  |  unchanged: {len(rows) - len(diffs) - len(unresolved)}  |  "
          f"differ: {len(diffs)}  |  unresolved (skipped): {len(unresolved)}")
    print(f"{'='*90}")

    if not diffs:
        print("Nothing to repair.")
        return

    if not apply:
        print("\nDry run only — no changes written. Re-run with --apply to write these corrections.")
        return

    audit = {'run_at': datetime.now().isoformat(), 'backup_path': backup_path, 'repairs': []}
    for row, replay in diffs:
        before = {k: row[k] for k in (
            'status', 'exit_date', 'exit_price', 'exit_reason', 'result',
            'pnl_pct', 'pnl_pct_gross', 'pnl_r', 'days_held'
        )}
        if replay['status'] == 'open':
            _apply_reopen(row['id'], replay, db_path=db_path)
            after = {'status': 'open', 'days_held': replay['days_held'], 'current_stop_price': replay['stop_price']}
        else:
            _apply_closed_update(row['id'], replay, db_path=db_path)
            after = {k: replay[k] for k in (
                'status', 'exit_date', 'exit_price', 'exit_reason', 'result',
                'pnl_pct', 'pnl_pct_gross', 'pnl_r', 'days_held'
            )}
        audit['repairs'].append({'id': row['id'], 'ticker': row['ticker'], 'system': row['system'],
                                  'before': before, 'after': after})

    os.makedirs(AUDIT_DIR, exist_ok=True)
    audit_path = os.path.join(AUDIT_DIR, f"partial_bar_repair_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(audit_path, 'w') as f:
        json.dump(audit, f, indent=2, default=str)
    print(f"\nApplied {len(diffs)} repairs. Audit trail: {audit_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Repair Day 99 partial-bar-contaminated closed trades')
    parser.add_argument('--apply', action='store_true', help='Write corrections (default: dry-run only)')
    args = parser.parse_args()
    run(apply=args.apply)
