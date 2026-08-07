"""
SRPS (Sector Rotation Pullback System) — shared rule constants.

Single source of truth for the live pullback screener (backend.py's
/api/sectors/pullback-screen) AND the backtest scripts
(backend/backtest/srps_gate0_signal_count.py, srps_gate1_backtest.py).

Extracted here specifically because backend.py can't import those scripts
directly — srps_gate0_signal_count.py imports `from backend import
SECTOR_ETF_MAP`, so backend.py importing it back would be a circular
import. This file has no dependencies on either side, so both can import
it safely. Any future change to an SRPS rule threshold belongs here once,
not duplicated by hand across three files (Golden Rule 21).

Design doc: SRPS v1.2, Section 6's own "PARAMETER FREEZE" instruction.
Gate 1's real backtest result (2020-2025, survivorship-free): FAIL — 34.1%
win rate, PF 1.177, both short of the design's own bar. Not built as a
live forward-test track. These constants now back a discretionary
SCREENER instead (informational candidates for manual judgment, no
automated entry/exit, no ledger) — see backend.py's endpoint docstring.
"""

RS_LOOKBACK_DAYS = 63       # ~3 months, Rule 3
RS_FLOOR = 0.9              # Rule 3
EMA_PULLBACK_LOW = 0.97     # Rule 3: close >= ema21 * 0.97
EMA_PULLBACK_HIGH = 1.01    # Rule 3: close <= ema21 * 1.01
STOP_MAX_PCT = 0.08         # Rule 4 — maximum stop distance
STOP_MIN_PCT = 0.005        # Rule 4 — minimum stop distance (found necessary during Gate 1's
                             # real run: a near-zero stop produced a 331,408 R-multiple artifact)
SWING_LOW_LOOKBACK = 10     # Rule 4
TARGET_R_MULTIPLE = 2.5     # Rule 5 (v1.1 — single target, no half-sell)
EARNINGS_EXCLUSION_DAYS = 21  # Rule 6 — not applied historically (no cheap historical earnings
                               # source), but IS applied live below, since live earnings data exists
