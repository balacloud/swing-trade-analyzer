"""
Forward Test Tracker for Swing Trade Analyzer
Tracks BUY/HOLD/AVOID signals and their outcomes over time

Day 15: Forward testing framework with SQLite storage
"""

import sqlite3
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import json


class SignalType(Enum):
    BUY = "BUY"
    HOLD = "HOLD"
    AVOID = "AVOID"


class SignalOutcome(Enum):
    OPEN = "open"           # Signal still active
    HIT_TARGET = "hit_target"  # Price reached target
    HIT_STOP = "hit_stop"      # Price hit stop loss
    TIMED_OUT = "timed_out"    # Max holding period exceeded
    MANUAL_CLOSE = "manual"    # Manually closed


@dataclass
class ForwardTestSignal:
    """A recorded trading signal for forward testing."""
    id: Optional[int]
    ticker: str
    signal_type: SignalType
    signal_date: str
    score: float
    
    # Price levels at signal time
    price_at_signal: float
    entry_price: Optional[float]
    stop_price: Optional[float]
    target_price: Optional[float]
    risk_reward: Optional[float]
    
    # Outcome tracking
    outcome: SignalOutcome
    outcome_date: Optional[str]
    outcome_price: Optional[float]
    pnl_percent: Optional[float]
    
    # Additional context
    verdict_reason: str
    notes: str


class ForwardTestTracker:
    """
    Tracks forward test signals in SQLite database.
    
    Records every BUY signal with entry/stop/target and tracks
    whether the trade would have been successful.
    """
    
    # Default max holding period for forward tests (days)
    MAX_HOLDING_DAYS = 45  # ~1.5 months for swing trades
    
    def __init__(self, db_path: str = None):
        """
        Initialize tracker with SQLite database.
        
        Args:
            db_path: Path to SQLite database file
        """
        if db_path is None:
            db_dir = os.path.join(os.path.dirname(__file__), '..', 'validation_results')
            os.makedirs(db_dir, exist_ok=True)
            db_path = os.path.join(db_dir, 'forward_test.db')
        
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database with required tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create signals table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS signals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL,
                signal_type TEXT NOT NULL,
                signal_date TEXT NOT NULL,
                score REAL NOT NULL,
                
                price_at_signal REAL NOT NULL,
                entry_price REAL,
                stop_price REAL,
                target_price REAL,
                risk_reward REAL,
                
                outcome TEXT DEFAULT 'open',
                outcome_date TEXT,
                outcome_price REAL,
                pnl_percent REAL,
                
                verdict_reason TEXT,
                notes TEXT,
                
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create index for faster queries
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_signals_ticker ON signals(ticker)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_signals_date ON signals(signal_date)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_signals_outcome ON signals(outcome)
        ''')
        
        # Create price history table for outcome checking
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS price_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL,
                snapshot_date TEXT NOT NULL,
                price REAL NOT NULL,
                high REAL,
                low REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(ticker, snapshot_date)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def record_signal(
        self,
        ticker: str,
        signal_type: SignalType,
        score: float,
        price_at_signal: float,
        entry_price: Optional[float] = None,
        stop_price: Optional[float] = None,
        target_price: Optional[float] = None,
        risk_reward: Optional[float] = None,
        verdict_reason: str = "",
        notes: str = ""
    ) -> int:
        """
        Record a new trading signal.
        
        Args:
            ticker: Stock ticker
            signal_type: BUY, HOLD, or AVOID
            score: Overall score (out of 75)
            price_at_signal: Current price when signal generated
            entry_price: Suggested entry price (for BUY signals)
            stop_price: Suggested stop loss price
            target_price: Suggested target price
            risk_reward: Risk/reward ratio
            verdict_reason: Reason for the verdict
            notes: Additional notes
            
        Returns:
            ID of the recorded signal
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        signal_date = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            INSERT INTO signals (
                ticker, signal_type, signal_date, score,
                price_at_signal, entry_price, stop_price, target_price, risk_reward,
                outcome, verdict_reason, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            ticker, signal_type.value, signal_date, score,
            price_at_signal, entry_price, stop_price, target_price, risk_reward,
            SignalOutcome.OPEN.value, verdict_reason, notes
        ))
        
        signal_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        print(f"   📝 Recorded {signal_type.value} signal for {ticker} (ID: {signal_id})")
        
        return signal_id
    
    def update_outcome(
        self,
        signal_id: int,
        outcome: SignalOutcome,
        outcome_price: float,
        pnl_percent: Optional[float] = None
    ):
        """
        Update the outcome of a signal.
        
        Args:
            signal_id: ID of the signal
            outcome: What happened (hit_target, hit_stop, timed_out)
            outcome_price: Price when outcome occurred
            pnl_percent: Profit/loss percentage
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        outcome_date = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            UPDATE signals 
            SET outcome = ?, outcome_date = ?, outcome_price = ?, pnl_percent = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (outcome.value, outcome_date, outcome_price, pnl_percent, signal_id))
        
        conn.commit()
        conn.close()
    
    def check_open_signals(self, current_prices: Dict[str, Dict]) -> List[Dict]:
        """
        Check all open signals against current prices and update outcomes.
        
        Args:
            current_prices: Dict of ticker -> {price, high, low}
            
        Returns:
            List of signals that were closed
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get all open BUY signals
        cursor.execute('''
            SELECT id, ticker, signal_type, signal_date, entry_price, stop_price, 
                   target_price, price_at_signal
            FROM signals
            WHERE outcome = 'open' AND signal_type = 'BUY'
        ''')
        
        open_signals = cursor.fetchall()
        closed_signals = []
        
        for row in open_signals:
            signal_id, ticker, signal_type, signal_date, entry, stop, target, orig_price = row
            
            if ticker not in current_prices:
                continue
            
            current = current_prices[ticker]
            current_price = current.get('price', 0)
            high = current.get('high', current_price)
            low = current.get('low', current_price)
            
            # Check if target was hit (using high of day)
            if target and high >= target:
                pnl = ((target - entry) / entry * 100) if entry else None
                self.update_outcome(signal_id, SignalOutcome.HIT_TARGET, target, pnl)
                closed_signals.append({
                    'id': signal_id,
                    'ticker': ticker,
                    'outcome': 'HIT_TARGET',
                    'pnl': pnl
                })
                continue
            
            # Check if stop was hit (using low of day)
            if stop and low <= stop:
                pnl = ((stop - entry) / entry * 100) if entry else None
                self.update_outcome(signal_id, SignalOutcome.HIT_STOP, stop, pnl)
                closed_signals.append({
                    'id': signal_id,
                    'ticker': ticker,
                    'outcome': 'HIT_STOP',
                    'pnl': pnl
                })
                continue
            
            # Check if timed out
            signal_dt = datetime.strptime(signal_date, '%Y-%m-%d')
            if datetime.now() - signal_dt > timedelta(days=self.MAX_HOLDING_DAYS):
                pnl = ((current_price - entry) / entry * 100) if entry else None
                self.update_outcome(signal_id, SignalOutcome.TIMED_OUT, current_price, pnl)
                closed_signals.append({
                    'id': signal_id,
                    'ticker': ticker,
                    'outcome': 'TIMED_OUT',
                    'pnl': pnl
                })
        
        conn.close()
        return closed_signals
    
    def get_performance_summary(self) -> Dict:
        """
        Get overall performance summary of forward testing.
        
        Returns:
            Dict with performance metrics
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total signals by type
        cursor.execute('''
            SELECT signal_type, COUNT(*) FROM signals GROUP BY signal_type
        ''')
        signal_counts = dict(cursor.fetchall())
        
        # Closed BUY signals performance
        cursor.execute('''
            SELECT outcome, COUNT(*), AVG(pnl_percent)
            FROM signals
            WHERE signal_type = 'BUY' AND outcome != 'open'
            GROUP BY outcome
        ''')
        outcomes = cursor.fetchall()
        
        # Calculate win rate
        cursor.execute('''
            SELECT 
                COUNT(CASE WHEN pnl_percent > 0 THEN 1 END) as wins,
                COUNT(CASE WHEN pnl_percent <= 0 THEN 1 END) as losses,
                AVG(CASE WHEN pnl_percent > 0 THEN pnl_percent END) as avg_win,
                AVG(CASE WHEN pnl_percent <= 0 THEN pnl_percent END) as avg_loss
            FROM signals
            WHERE signal_type = 'BUY' AND outcome != 'open' AND pnl_percent IS NOT NULL
        ''')
        perf = cursor.fetchone()
        wins, losses, avg_win, avg_loss = perf
        
        total_closed = (wins or 0) + (losses or 0)
        win_rate = (wins / total_closed * 100) if total_closed > 0 else 0
        
        # Open signals
        cursor.execute('''
            SELECT COUNT(*) FROM signals WHERE outcome = 'open'
        ''')
        open_count = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_signals': sum(signal_counts.values()),
            'signal_counts': signal_counts,
            'closed_trades': total_closed,
            'open_trades': open_count,
            'wins': wins or 0,
            'losses': losses or 0,
            'win_rate': round(win_rate, 1),
            'avg_win_pct': round(avg_win, 2) if avg_win else 0,
            'avg_loss_pct': round(avg_loss, 2) if avg_loss else 0,
            'outcomes': {row[0]: {'count': row[1], 'avg_pnl': row[2]} for row in outcomes}
        }
    
    def get_recent_signals(self, days: int = 30, limit: int = 50) -> List[Dict]:
        """
        Get recent signals for display.
        
        Args:
            days: Number of days to look back
            limit: Maximum number of signals to return
            
        Returns:
            List of signal dicts
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cutoff_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        cursor.execute('''
            SELECT id, ticker, signal_type, signal_date, score,
                   price_at_signal, entry_price, stop_price, target_price, risk_reward,
                   outcome, outcome_date, outcome_price, pnl_percent,
                   verdict_reason, notes
            FROM signals
            WHERE signal_date >= ?
            ORDER BY signal_date DESC, id DESC
            LIMIT ?
        ''', (cutoff_date, limit))
        
        columns = [
            'id', 'ticker', 'signal_type', 'signal_date', 'score',
            'price_at_signal', 'entry_price', 'stop_price', 'target_price', 'risk_reward',
            'outcome', 'outcome_date', 'outcome_price', 'pnl_percent',
            'verdict_reason', 'notes'
        ]
        
        signals = []
        for row in cursor.fetchall():
            signals.append(dict(zip(columns, row)))
        
        conn.close()
        return signals
    
    def get_signal_by_ticker(self, ticker: str, include_closed: bool = True) -> List[Dict]:
        """Get all signals for a specific ticker."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if include_closed:
            cursor.execute('''
                SELECT * FROM signals WHERE ticker = ? ORDER BY signal_date DESC
            ''', (ticker,))
        else:
            cursor.execute('''
                SELECT * FROM signals WHERE ticker = ? AND outcome = 'open' 
                ORDER BY signal_date DESC
            ''', (ticker,))
        
        columns = [desc[0] for desc in cursor.description]
        signals = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return signals


# CLI testing
if __name__ == '__main__':
    tracker = ForwardTestTracker()
    
    # Test recording a signal
    signal_id = tracker.record_signal(
        ticker='AAPL',
        signal_type=SignalType.BUY,
        score=65,
        price_at_signal=250.00,
        entry_price=245.00,
        stop_price=238.00,
        target_price=270.00,
        risk_reward=3.57,
        verdict_reason="Strong score with good RS"
    )
    
    print(f"\nRecorded signal ID: {signal_id}")
    
    # Get performance summary
    summary = tracker.get_performance_summary()
    print(f"\nPerformance Summary: {json.dumps(summary, indent=2)}")
    
    # Get recent signals
    recent = tracker.get_recent_signals(days=30)
    print(f"\nRecent signals: {len(recent)}")
