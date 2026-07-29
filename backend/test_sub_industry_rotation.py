#!/usr/bin/env python3
"""
Sub-Industry Watch Endpoint Test Suite (Day 100+)

/api/sectors/sub-industry computes RS-ratio/momentum/quadrant for 21
sub-industry theme-cluster proxy ETFs (SUB_INDUSTRY_CLUSTERS in
sub_industry_clusters.py), one level below the 11 broad GICS sectors that
/api/sectors/rotation already covers. Same convention as
test_sector_rotation.py: a standalone script hitting the live running server,
asserting structural invariants rather than pinning today's real numbers.

Checks:
  1. All 21 clusters present, no unexpected/missing cluster names
  2. Every successful cluster has quadrant internally consistent with its own
     rsRatio/rsMomentum -- recomputes the same (RS>=100, Momentum>=0) rule
     locally, mirroring backend.py's compute_rs_ratio_and_quadrant()
  3. A cluster with an error has quadrant/rsRatio/rsMomentum all None (never
     a partial/inconsistent row)
  4. shortHistory is only True when usableDays is below the full-window
     threshold, and never None for a successful cluster
  5. sanity-bounds check on rsRatio for successful clusters
  6. noProxyClusters is present and non-empty (informational, never scored)

Usage:
    python3 test_sub_industry_rotation.py
    python3 test_sub_industry_rotation.py --base-url http://localhost:5001/api
"""
import argparse
import sys

import requests


class Colors:
    GREEN = '\033[92m'
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


EXPECTED_CLUSTERS = {
    "Semis", "Memory/Storage", "AI Infra/Power", "Nuclear/Uranium",
    "Critical Materials", "Gold Miners", "Biotech", "Financials/Fintech",
    "Crypto", "Software/SaaS", "China Internet ADR", "EV/Autonomous",
    "Space/Emerging", "Optical/Connectivity", "Enterprise Tech",
    "Communication Services", "Defense", "Physical AI/Robotics",
    "Industrials/Water", "Energy", "High-beta mega",
}
VALID_QUADRANTS = {"Leading", "Weakening", "Lagging", "Improving"}
RS_RATIO_SANE_MIN, RS_RATIO_SANE_MAX = 30.0, 350.0
FULL_WINDOW_TRADING_DAYS = 115  # must match backend.py's own constant


def expected_quadrant(rs_ratio, rs_momentum):
    """Mirrors backend.py's compute_rs_ratio_and_quadrant() rule exactly."""
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

    print_info(f"GET {base_url}/sectors/sub-industry")
    resp = requests.get(f"{base_url}/sectors/sub-industry", timeout=180)
    if resp.status_code != 200:
        print_fail(f"HTTP {resp.status_code}: {resp.text[:200]}")
        return 1
    data = resp.json()

    # 1. All 21 clusters present
    clusters = data.get("clusters", [])
    names_seen = {c.get("cluster") for c in clusters}
    if names_seen != EXPECTED_CLUSTERS:
        failures.append(f"cluster set mismatch -- missing {EXPECTED_CLUSTERS - names_seen}, "
                         f"unexpected {names_seen - EXPECTED_CLUSTERS}")
    else:
        print_pass(f"All 21 sub-industry clusters present ({len(clusters)} rows)")

    if data.get("clusterCount") != len(clusters):
        failures.append(f"clusterCount ({data.get('clusterCount')}) != len(clusters) ({len(clusters)})")
    else:
        print_pass("clusterCount matches len(clusters)")

    error_clusters = [c for c in clusters if c.get("error")]
    ok_clusters = [c for c in clusters if not c.get("error")]
    print_info(f"{len(ok_clusters)} clusters resolved cleanly, {len(error_clusters)} errored "
               f"(provider-availability dependent, not necessarily a bug)")

    # 2. Successful clusters: quadrant internally consistent, sane bounds
    quadrant_mismatches = []
    bounds_violations = []
    for c in ok_clusters:
        name, rs_ratio, rs_momentum, quadrant = c.get("cluster"), c.get("rsRatio"), c.get("rsMomentum"), c.get("quadrant")
        if quadrant not in VALID_QUADRANTS:
            failures.append(f"{name}: invalid quadrant value {quadrant!r}")
            continue
        if rs_ratio is None or rs_momentum is None:
            failures.append(f"{name}: error=None but rsRatio/rsMomentum is None")
            continue
        expected = expected_quadrant(rs_ratio, rs_momentum)
        if expected != quadrant:
            quadrant_mismatches.append(f"{name} ({c.get('proxy')}): rsRatio={rs_ratio}, "
                                        f"rsMomentum={rs_momentum} -> expected {expected}, got {quadrant}")
        if not (RS_RATIO_SANE_MIN <= rs_ratio <= RS_RATIO_SANE_MAX):
            bounds_violations.append(f"{name}: rsRatio={rs_ratio} outside sane bounds "
                                      f"[{RS_RATIO_SANE_MIN}, {RS_RATIO_SANE_MAX}]")
    if quadrant_mismatches:
        failures.extend(quadrant_mismatches)
    elif ok_clusters:
        print_pass("quadrant matches (RS>=100, Momentum>=0) rule for every resolved cluster")
    if bounds_violations:
        failures.extend(bounds_violations)
    elif ok_clusters:
        print_pass(f"All resolved rsRatio values within sane bounds [{RS_RATIO_SANE_MIN}, {RS_RATIO_SANE_MAX}]")

    # 3. Errored clusters: fully None, never a partial row
    partial_errors = []
    for c in error_clusters:
        if c.get("rsRatio") is not None or c.get("rsMomentum") is not None or c.get("quadrant") is not None:
            partial_errors.append(f"{c.get('cluster')}: has error set but also a non-None "
                                   f"rsRatio/rsMomentum/quadrant field")
    if partial_errors:
        failures.extend(partial_errors)
    else:
        print_pass("Errored clusters (if any) are fully None, not partial rows")

    # 4. shortHistory / usableDays consistency
    short_history_issues = []
    for c in ok_clusters:
        usable_days, short_history = c.get("usableDays"), c.get("shortHistory")
        if usable_days is None or short_history is None:
            short_history_issues.append(f"{c.get('cluster')}: usableDays/shortHistory is None on a resolved cluster")
            continue
        expected_short = usable_days < FULL_WINDOW_TRADING_DAYS
        if expected_short != short_history:
            short_history_issues.append(f"{c.get('cluster')}: usableDays={usable_days} -> "
                                         f"expected shortHistory={expected_short}, got {short_history}")
    if short_history_issues:
        failures.extend(short_history_issues)
    elif ok_clusters:
        print_pass("shortHistory flag matches usableDays vs the full-window threshold for every resolved cluster")

    # 5. noProxyClusters present
    no_proxy = data.get("noProxyClusters", [])
    if not no_proxy:
        failures.append("noProxyClusters is empty -- expected at least 'Past survivors' (POET)")
    else:
        print_pass(f"noProxyClusters present ({len(no_proxy)} informational cluster(s))")

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
