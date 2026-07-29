#!/usr/bin/env python3
"""
Sector Rotation Endpoint Test Suite — Day 92-equivalent
Drafted by the Trading Intelligence Hub (Session 38, Jul 29 2026), verified
live against a running backend before handoff.

/api/sectors/rotation has real RS-ratio/momentum/quadrant computation
(backend.py:2258-2470) but no automated test coverage anywhere in this repo
-- found while an external session (the hub) was researching this endpoint
for its own purposes and grepped backend/tests/ + every test_*.py for any
reference, finding none.

Matches this repo's own established test convention (test_categorical_
comprehensive.py): a standalone script hitting the live running server via
requests, not a pytest/mock suite -- this repo has no pytest usage outside
vendored packages, so a mocked unit-test file would be inconsistent with how
everything else here is actually run and reviewed.

Deliberately does NOT assert exact rsRatio/rsMomentum values (today's real
numbers are the point, not a fixed golden value) -- instead asserts
structural invariants that would catch a real regression:
  1. All 11 SPDR sectors present, every required field on every row
  2. quadrant is INTERNALLY CONSISTENT with rsRatio/rsMomentum -- recomputes
     the same (RS>=100, Momentum>=0) rule locally and checks it matches what
     the endpoint returned. This is the one that would actually catch a
     future refactor accidentally flipping a >= to a > or a sign.
  3. mapping dict covers real GICS/TradingView sector names
  4. size_rotation / size_signal shape is sane
  5. sanity-bounds check (rsRatio in a plausible range) -- catches a gross
     units bug without pinning an exact value

Usage:
    python3 test_sector_rotation.py
    python3 test_sector_rotation.py --base-url http://localhost:5001/api
"""
import argparse
import sys

import requests


class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_pass(msg):
    print(f"{Colors.GREEN}[PASS]{Colors.RESET} {msg}")


def print_fail(msg):
    print(f"{Colors.RED}[FAIL]{Colors.RESET} {msg}")


def print_info(msg):
    print(f"{Colors.BLUE}[INFO]{Colors.RESET} {msg}")


EXPECTED_ETFS = {"XLK", "XLF", "XLV", "XLI", "XLY", "XLP", "XLE", "XLB", "XLU", "XLRE", "XLC"}
REQUIRED_SECTOR_FIELDS = {"etf", "name", "price", "rsRatio", "rsMomentum", "quadrant",
                           "weekChange", "monthChange", "rank"}
VALID_QUADRANTS = {"Leading", "Weakening", "Lagging", "Improving"}
# Plausible RS-ratio bounds for a real, non-corrupted computation -- not a
# precision check, just wide enough to catch a units bug (e.g. accidentally
# leaving the ratio as 0.xx instead of x100, or a divide-by-wrong-series bug).
RS_RATIO_SANE_MIN, RS_RATIO_SANE_MAX = 40.0, 300.0


def expected_quadrant(rs_ratio, rs_momentum):
    """Mirrors backend.py:2334-2341's own rule exactly -- this is the
    consistency check, not a re-implementation for its own sake."""
    if rs_ratio >= 100 and rs_momentum >= 0:
        return "Leading"
    elif rs_ratio >= 100 and rs_momentum < 0:
        return "Weakening"
    elif rs_ratio < 100 and rs_momentum < 0:
        return "Lagging"
    else:
        return "Improving"


def run(base_url):
    failures = []

    print_info(f"GET {base_url}/sectors/rotation")
    resp = requests.get(f"{base_url}/sectors/rotation", timeout=30)
    if resp.status_code != 200:
        print_fail(f"HTTP {resp.status_code}: {resp.text[:200]}")
        return 1
    data = resp.json()

    # 1. All 11 sectors present, every required field
    sectors = data.get("sectors", [])
    etfs_seen = {s.get("etf") for s in sectors}
    if etfs_seen != EXPECTED_ETFS:
        failures.append(f"sector set mismatch -- missing {EXPECTED_ETFS - etfs_seen}, "
                         f"unexpected {etfs_seen - EXPECTED_ETFS}")
    else:
        print_pass(f"All 11 SPDR sectors present ({len(sectors)} rows)")

    if data.get("sectorCount") != len(sectors):
        failures.append(f"sectorCount ({data.get('sectorCount')}) != len(sectors) ({len(sectors)})")
    else:
        print_pass("sectorCount matches len(sectors)")

    for s in sectors:
        missing = REQUIRED_SECTOR_FIELDS - set(s.keys())
        if missing:
            failures.append(f"{s.get('etf', '?')}: missing fields {missing}")
    if not any("missing fields" in f for f in failures):
        print_pass("Every sector row has all required fields")

    # 2. Quadrant internally consistent with rsRatio/rsMomentum
    quadrant_mismatches = []
    bounds_violations = []
    for s in sectors:
        etf, rs_ratio, rs_momentum, quadrant = s.get("etf"), s.get("rsRatio"), s.get("rsMomentum"), s.get("quadrant")
        if quadrant not in VALID_QUADRANTS:
            failures.append(f"{etf}: invalid quadrant value {quadrant!r}")
            continue
        if rs_ratio is None or rs_momentum is None:
            failures.append(f"{etf}: rsRatio/rsMomentum is None")
            continue
        expected = expected_quadrant(rs_ratio, rs_momentum)
        if expected != quadrant:
            quadrant_mismatches.append(f"{etf}: rsRatio={rs_ratio}, rsMomentum={rs_momentum} "
                                        f"-> expected {expected}, got {quadrant}")
        if not (RS_RATIO_SANE_MIN <= rs_ratio <= RS_RATIO_SANE_MAX):
            bounds_violations.append(f"{etf}: rsRatio={rs_ratio} outside sane bounds "
                                      f"[{RS_RATIO_SANE_MIN}, {RS_RATIO_SANE_MAX}]")
    if quadrant_mismatches:
        failures.extend(quadrant_mismatches)
    else:
        print_pass("quadrant matches (RS>=100, Momentum>=0) rule for every sector")
    if bounds_violations:
        failures.extend(bounds_violations)
    else:
        print_pass(f"All rsRatio values within sane bounds [{RS_RATIO_SANE_MIN}, {RS_RATIO_SANE_MAX}]")

    # 3. mapping dict present and non-trivial
    mapping = data.get("mapping", {})
    mapped_etfs = set(mapping.values())
    if not EXPECTED_ETFS.issubset(mapped_etfs):
        failures.append(f"mapping dict doesn't cover all 11 ETFs -- missing {EXPECTED_ETFS - mapped_etfs}")
    else:
        print_pass(f"mapping dict covers all 11 ETFs ({len(mapping)} GICS/TradingView names mapped)")

    # 4. size_rotation / size_signal shape
    size_rotation = data.get("size_rotation", [])
    size_etfs_seen = {s.get("etf") for s in size_rotation}
    if size_etfs_seen != {"QQQ", "MDY", "IWM"}:
        failures.append(f"size_rotation ETF set mismatch: {size_etfs_seen}")
    else:
        print_pass("size_rotation has QQQ/MDY/IWM")
    if data.get("size_signal") not in ("Risk-On", "Risk-Off", "Neutral"):
        failures.append(f"size_signal has an unexpected value: {data.get('size_signal')!r}")
    else:
        print_pass(f"size_signal is valid ({data.get('size_signal')!r})")

    # size_signal internal consistency: mirrors backend.py's own IWM-vs-QQQ diff>=2/<=-2 rule
    iwm = next((s for s in size_rotation if s.get("etf") == "IWM"), None)
    qqq = next((s for s in size_rotation if s.get("etf") == "QQQ"), None)
    if iwm and qqq:
        diff = iwm["rsRatio"] - qqq["rsRatio"]
        expected_signal = "Risk-On" if diff >= 2 else "Risk-Off" if diff <= -2 else "Neutral"
        if expected_signal != data.get("size_signal"):
            failures.append(f"size_signal inconsistent: IWM-QQQ diff={diff:.2f} "
                             f"-> expected {expected_signal!r}, got {data.get('size_signal')!r}")
        else:
            print_pass(f"size_signal matches IWM-QQQ diff rule (diff={diff:.2f})")

    print()
    if failures:
        print(f"{Colors.BOLD}{Colors.RED}{len(failures)} FAILURE(S){Colors.RESET}")
        for f in failures:
            print_fail(f)
        return 1
    print(f"{Colors.BOLD}{Colors.GREEN}ALL CHECKS PASSED{Colors.RESET}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:5001/api")
    args = parser.parse_args()
    sys.exit(run(args.base_url))
