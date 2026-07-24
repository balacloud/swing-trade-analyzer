"""
Paper Trading Ledger — Automated Daily Engine (Day 81)

SQLite ledger for the automated daily paper-trading job. Every qualifying
signal from the frozen config (docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md)
is taken automatically — no human filtering — so this ledger is the
authoritative, selection-bias-free source for the 50-trade confirmation bar
(Golden Rule 18/19).

Position lifecycle: pending_entry -> open -> closed
  pending_entry: signal fired at today's close, enters at tomorrow's open
  open:          position live, re-evaluated daily via a fresh live_mode
                 replay of trade_simulator.simulate_trade() /
                 mr_simulator.simulate_mr_trade() from entry_date to today
                 (see backend/backtest/trade_simulator.py's live_mode
                 docstring — one exit-logic implementation, not two)
  closed:        exit recorded
"""
import sqlite3
import os
import json
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backtest.metrics import compute_metrics

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'validation_results', 'paper_trading_ledger.db'
)


def _connect(db_path=None):
    path = db_path or DB_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS paper_positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            system TEXT NOT NULL,               -- 'momentum' | 'mr'
            variant TEXT NOT NULL DEFAULT 'A_frozen',  -- 'A_frozen' | 'B_revised_rr' (Day 95)
            ticker TEXT NOT NULL,
            holding_period TEXT,                 -- 'quick'|'standard'|'position' (momentum); NULL for mr
            status TEXT NOT NULL DEFAULT 'pending_entry',  -- pending_entry|open|closed

            signal_date TEXT NOT NULL,
            signal_price REAL NOT NULL,

            entry_date TEXT,
            entry_price REAL,
            entry_slippage_pct REAL,

            initial_stop_price REAL,
            initial_target_price REAL,
            current_stop_price REAL,
            max_hold_days INTEGER,
            days_held INTEGER DEFAULT 0,

            exit_date TEXT,
            exit_price REAL,
            exit_reason TEXT,
            result TEXT,                         -- win|loss|breakeven
            pnl_pct REAL,                        -- net of transaction costs
            pnl_pct_gross REAL,
            pnl_r REAL,

            regime_snapshot TEXT,                -- JSON: vix, spy_above_200sma, spy_50sma_declining
            verdict_reason TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Migration (Day 95): CREATE TABLE IF NOT EXISTS doesn't add columns to an
    # already-existing table — add 'variant' if this ledger predates it.
    # DEFAULT 'A_frozen' backfills every existing row automatically, so all
    # prior Path A history is correctly tagged with zero manual migration.
    existing_cols = {row['name'] for row in cur.execute('PRAGMA table_info(paper_positions)')}
    if 'variant' not in existing_cols:
        cur.execute("ALTER TABLE paper_positions ADD COLUMN variant TEXT NOT NULL DEFAULT 'A_frozen'")

    cur.execute('CREATE INDEX IF NOT EXISTS idx_paper_ticker ON paper_positions(ticker)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_paper_status ON paper_positions(status)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_paper_system ON paper_positions(system)')
    cur.execute('CREATE INDEX IF NOT EXISTS idx_paper_variant ON paper_positions(variant)')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS job_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TEXT NOT NULL UNIQUE,
            completed_at TEXT DEFAULT CURRENT_TIMESTAMP,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()


# ─── Signal queueing ──────────────────────────────────────────────────────

def has_active_or_cooldown(ticker, system, cooldown_days=5, as_of_date=None,
                            variant='A_frozen', db_path=None):
    """
    True if `ticker` already has a pending/open position in `system`+`variant`,
    OR closed within the last `cooldown_days` calendar days (mirrors the
    backtest's cooldown to prevent overlapping re-entries on the same name).

    Filtered by variant (Day 95) so Path A and Path B are independent
    experiments — a ticker on cooldown in Path A doesn't block Path B (and
    vice versa) from taking the same signal under its own formula.
    """
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        SELECT status, exit_date FROM paper_positions
        WHERE ticker = ? AND system = ? AND variant = ?
        ORDER BY id DESC LIMIT 5
    ''', (ticker, system, variant))
    rows = cur.fetchall()
    conn.close()

    if as_of_date is None:
        as_of_date = datetime.now().strftime('%Y-%m-%d')
    as_of_dt = datetime.strptime(as_of_date, '%Y-%m-%d')

    for row in rows:
        if row['status'] in ('pending_entry', 'open'):
            return True
        if row['status'] == 'closed' and row['exit_date']:
            try:
                exit_dt = datetime.strptime(row['exit_date'], '%Y-%m-%d')
                if (as_of_dt - exit_dt).days < cooldown_days:
                    return True
            except ValueError:
                pass
    return False


def queue_pending_signal(system, ticker, signal_date, signal_price,
                          holding_period=None, verdict_reason='',
                          regime_snapshot=None, variant='A_frozen', db_path=None):
    """
    regime_snapshot captured HERE (at signal time, when the categorical
    assessment / MR detector actually fired) rather than at activation —
    shows the regime that triggered the signal, not the regime a day later.
    """
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO paper_positions (system, variant, ticker, holding_period, status,
                                      signal_date, signal_price, verdict_reason, regime_snapshot)
        VALUES (?, ?, ?, ?, 'pending_entry', ?, ?, ?, ?)
    ''', (system, variant, ticker, holding_period, signal_date, signal_price, verdict_reason,
          json.dumps(regime_snapshot) if regime_snapshot else None))
    position_id = cur.lastrowid
    conn.commit()
    conn.close()
    return position_id


def get_pending_signals(system=None, variant=None, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    query = "SELECT * FROM paper_positions WHERE status = 'pending_entry'"
    params = []
    if system:
        query += " AND system = ?"
        params.append(system)
    if variant:
        query += " AND variant = ?"
        params.append(variant)
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


# ─── Activation (pending_entry -> open) ───────────────────────────────────

def activate_position(position_id, entry_date, entry_price,
                       initial_stop_price, initial_target_price, max_hold_days,
                       regime_snapshot=None, db_path=None):
    """
    regime_snapshot here is optional and only used if the pending row didn't
    already capture one at signal time (queue_pending_signal) — it is never
    used to overwrite an existing signal-time snapshot.
    """
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT signal_price, regime_snapshot FROM paper_positions WHERE id = ?', (position_id,))
    row = cur.fetchone()
    signal_price = row['signal_price'] if row else entry_price
    slippage_pct = ((entry_price - signal_price) / signal_price * 100) if signal_price else None
    existing_regime = row['regime_snapshot'] if row else None
    regime_to_store = existing_regime if existing_regime else (
        json.dumps(regime_snapshot) if regime_snapshot else None
    )

    cur.execute('''
        UPDATE paper_positions
        SET status = 'open', entry_date = ?, entry_price = ?, entry_slippage_pct = ?,
            initial_stop_price = ?, initial_target_price = ?, current_stop_price = ?,
            max_hold_days = ?, days_held = 0, regime_snapshot = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (entry_date, entry_price, slippage_pct, initial_stop_price, initial_target_price,
          initial_stop_price, max_hold_days, regime_to_store, position_id))
    conn.commit()
    conn.close()


# ─── Open position tracking ───────────────────────────────────────────────

def get_open_positions(system=None, variant=None, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    query = "SELECT * FROM paper_positions WHERE status = 'open'"
    params = []
    if system:
        query += " AND system = ?"
        params.append(system)
    if variant:
        query += " AND variant = ?"
        params.append(variant)
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def update_open_position(position_id, days_held, current_stop_price, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        UPDATE paper_positions
        SET days_held = ?, current_stop_price = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (days_held, current_stop_price, position_id))
    conn.commit()
    conn.close()


def close_position(position_id, exit_date, exit_price, exit_reason, result,
                    pnl_pct, pnl_pct_gross, pnl_r, days_held, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        UPDATE paper_positions
        SET status = 'closed', exit_date = ?, exit_price = ?, exit_reason = ?, result = ?,
            pnl_pct = ?, pnl_pct_gross = ?, pnl_r = ?, days_held = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (exit_date, exit_price, exit_reason, result, pnl_pct, pnl_pct_gross, pnl_r, days_held, position_id))
    conn.commit()
    conn.close()


def get_closed_trades(system=None, variant=None, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    query = "SELECT * FROM paper_positions WHERE status = 'closed'"
    params = []
    if system:
        query += " AND system = ?"
        params.append(system)
    if variant:
        query += " AND variant = ?"
        params.append(variant)
    query += " ORDER BY entry_date"
    cur.execute(query, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


# ─── Stats (reuses backend/backtest/metrics.py — same math as the backtest) ──

def compute_stats(system=None, variant=None, db_path=None):
    """
    Wraps backend/backtest/metrics.compute_metrics() so paper-trading stats
    are computed identically to the backtest numbers they're meant to
    confirm/refute — one implementation, not a second one prone to drift
    (the exact class of bug Golden Rule 19 found between JS and Python).
    """
    closed = get_closed_trades(system=system, variant=variant, db_path=db_path)
    trade_dicts = []
    for t in closed:
        trade_dicts.append({
            'return_pct': t.get('pnl_pct_gross', t.get('pnl_pct')),
            'return_pct_net': t.get('pnl_pct'),
            'return_r': t.get('pnl_r'),
            'days_held': t.get('days_held'),
            'result': t.get('result'),
            'exit_reason': t.get('exit_reason'),
            'entry_date': t.get('entry_date'),
            'exit_date': t.get('exit_date'),
            'config': t.get('system'),
        })
    return compute_metrics(trade_dicts)


# ─── Job run bookkeeping (idempotency / catch-up) ─────────────────────────

def get_last_run_date(db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT MAX(run_date) as d FROM job_runs')
    row = cur.fetchone()
    conn.close()
    return row['d'] if row and row['d'] else None


def record_job_run(run_date, summary: dict, db_path=None):
    conn = _connect(db_path)
    cur = conn.cursor()
    cur.execute('''
        INSERT OR REPLACE INTO job_runs (run_date, summary, completed_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
    ''', (run_date, json.dumps(summary)))
    conn.commit()
    conn.close()


# ─── Backup (Day 82, Fable hygiene audit) ─────────────────────────────────
# This ledger is the entire live-evidence record for the project's central
# question — months of unrepeatable signals (missed days can't be
# backfilled, see live_signals.py's module docstring) live in one SQLite
# file with no other copy. Back it up after every job run.

BACKUP_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'validation_results', 'ledger_backups'
)
BACKUP_KEEP = 30  # ~6 weeks of weekday runs


def backup_db(db_path=None, backup_dir=None, keep=BACKUP_KEEP):
    """
    Safe, atomic backup via SQLite's own backup API (not a raw file copy,
    which risks grabbing a half-written page if a write is in progress).
    Keeps the most recent `keep` dated backups, prunes older ones.
    """
    source_path = db_path or DB_PATH
    if not os.path.exists(source_path):
        return None

    target_dir = backup_dir or BACKUP_DIR
    os.makedirs(target_dir, exist_ok=True)

    stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(target_dir, f'paper_trading_ledger_{stamp}.db')

    source_conn = sqlite3.connect(source_path)
    dest_conn = sqlite3.connect(backup_path)
    with dest_conn:
        source_conn.backup(dest_conn)
    dest_conn.close()
    source_conn.close()

    existing = sorted(
        f for f in os.listdir(target_dir)
        if f.startswith('paper_trading_ledger_') and f.endswith('.db')
    )
    for stale in existing[:-keep]:
        os.remove(os.path.join(target_dir, stale))

    return backup_path


if __name__ == '__main__':
    init_db()
    print(f"Ledger initialized at {DB_PATH}")
