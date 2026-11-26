#!/bin/bash
# One command to run every check (Day 127). Not a hook: you run it when you want to.
#   ./run_all_checks.sh --quick   backend + frontend test suites only (about 2-3 minutes)
#   ./run_all_checks.sh           also the page checker and a smoke audit on 8 fixed tickers (about 10 minutes; needs the app running)
# Ends with ONE line: "ALL OK" or "FAILED: <what>". Exit code 0 = ok.
PROJECT="/Users/balajik/projects/swing-trade-analyzer"
PY="$PROJECT/backend/venv/bin/python"
NODE="$(command -v node)"
QUICK=0; [ "$1" = "--quick" ] && QUICK=1
FAILED=()
LOG="$(mktemp -d)"

run() {   # run NAME CMD... : fails on a non-zero exit code or any output line that starts with FAIL
  local name="$1"; shift
  if "$@" > "$LOG/$name.log" 2>&1 && ! grep -q "^FAIL" "$LOG/$name.log"; then
    printf '  ok    %s\n' "$name"
  else
    printf '  FAIL  %s   (log: %s)\n' "$name" "$LOG/$name.log"; FAILED+=("$name")
  fi
}

echo "== backend tests"
cd "$PROJECT/backend"
for t in test_env_loader test_price_freshness test_price_basis test_forming_bar_routes test_sr_volume_unavailable test_live_quote test_tradier_errors test_alpaca_provider test_tradier_fallback_rule test_empty_price_row test_audit_statements test_audit_cards test_audit_cards2 test_rrg test_sector_rotation test_sub_industry_rotation; do
  [ -f "$t.py" ] && run "$t" "$PY" "$t.py"
done
run test_review_gate bash "$PROJECT/.claude/hooks/test_three_pass_check.sh"
run test_simple_sr "$PY" backtest/test_simple_sr.py
run test_indicators "$PY" backtest/test_indicators.py
run test_data_quality "$PY" backtest/test_data_quality.py

echo "== frontend tests"
cd "$PROJECT/frontend"
for f in scripts/test_*.mjs; do run "$(basename "$f" .mjs)" "$NODE" "$f"; done

if [ "$QUICK" = "0" ]; then
  echo "== services"
  if ! curl -s -o /dev/null -m 5 localhost:5001/api/health || ! curl -s -o /dev/null -m 5 localhost:3000; then
    echo "  the app is not running (backend 5001 / frontend 3000): skipping the page checker and the smoke audit"
    FAILED+=("services-not-running")
  else
    echo "== page checker (5 tickers)"
    "$NODE" scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN F > "$LOG/page_checker.log" 2>&1
    PC=$(grep -oE "[0-9]+/[0-9]+ checks passed" "$LOG/page_checker.log" | tail -1)
    A="${PC%%/*}"; B=$(echo "$PC" | sed -E 's#^[0-9]+/([0-9]+).*#\1#')
    if [ -n "$PC" ] && [ "$A" = "$B" ]; then echo "  ok    page_checker ($PC)"; else echo "  FAIL  page_checker (${PC:-no result}; log: $LOG/page_checker.log)"; FAILED+=("page_checker"); fi
    echo "== smoke audit (8 tickers)"
    OUT="$PROJECT/backend/validation_results/smoke_$(date +%Y%m%d_%H%M)"
    mkdir -p "$OUT"
    "$NODE" scripts/dump_page_statements.js "$OUT" $(cat "$PROJECT/backend/audit_smoke.txt" | tr '\n' ' ') > "$LOG/smoke_dump.log" 2>&1
    cd "$PROJECT/backend"
    for m in audit_statements audit_cards audit_cards2; do "$PY" $m.py "$OUT" > "$LOG/$m.log" 2>&1; done
    "$PY" audit_summary.py "$OUT" || FAILED+=("smoke-audit-WRONG-rows")
  fi
fi

echo
if [ ${#FAILED[@]} -eq 0 ]; then echo "ALL OK"; exit 0; else echo "FAILED: ${FAILED[*]}"; exit 1; fi
