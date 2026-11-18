#!/bin/bash
# Nightly universe audit (Day 127): the same Statement Audit we run by hand, on the 117-ticker universe, after the close. Not a hook.
# Run by launchd (com.sta.nightly.audit, weekdays 18:00 local = Eastern). Needs the app running (backend 5001, frontend 3000); it does NOT start or restart them.
# Output: backend/validation_results/nightly/YYYY-MM-DD/  (dumps + REPORT*.md + SUMMARY.txt), and one line appended to nightly/history.csv.
# Override the ticker list for a test:  AUDIT_TICKERS_FILE=backend/audit_smoke.txt ./nightly_audit.sh
PROJECT="/Users/balajik/projects/swing-trade-analyzer"
PY="$PROJECT/backend/venv/bin/python"
NODE="/usr/local/bin/node"
TICKERS_FILE="${AUDIT_TICKERS_FILE:-$PROJECT/backend/audit_universe.txt}"
BASE="$PROJECT/backend/validation_results/nightly"
TODAY="$(date +%Y-%m-%d)"
OUT="$BASE/$TODAY"
mkdir -p "$OUT"
LOG="$OUT/nightly.log"
exec >> "$LOG" 2>&1
echo "=== nightly audit $TODAY $(date +%H:%M) tickers file: $TICKERS_FILE"

if ! curl -s -o /dev/null -m 10 localhost:5001/api/health || ! curl -s -o /dev/null -m 10 localhost:3000; then
  echo "app not running (backend 5001 / frontend 3000): nothing to audit tonight"
  echo "$TODAY,skipped-app-not-running,,,," >> "$BASE/history.csv"
  exit 0
fi

# previous run folder (most recent earlier date) for the "new WRONG rows" comparison
PREV="$(ls -1d "$BASE"/20* 2>/dev/null | grep -v "$OUT" | tail -1)"

# two halves in parallel, each in its own browser (the dump script relaunches a crashed browser and retries once)
N=$(wc -l < "$TICKERS_FILE" | tr -d " "); H=$(( (N + 1) / 2 ))
A="$(head -n $H "$TICKERS_FILE" | tr '\n' ' ')"; B="$(tail -n +$((H + 1)) "$TICKERS_FILE" | tr '\n' ' ')"
cd "$PROJECT/frontend"
"$NODE" scripts/dump_page_statements.js "$OUT" $A > "$OUT/dump_a.log" 2>&1 &
PA=$!
[ -n "$B" ] && { "$NODE" scripts/dump_page_statements.js "$OUT" $B > "$OUT/dump_b.log" 2>&1 & PB=$!; }
wait $PA; [ -n "$PB" ] && wait $PB

cd "$PROJECT/backend"
for m in audit_statements audit_cards audit_cards2; do "$PY" $m.py "$OUT" > "$OUT/$m.out" 2>&1; done
DUMPS=$(ls "$OUT"/dump_*.json 2>/dev/null | wc -l | tr -d ' ')
if [ -n "$PREV" ]; then "$PY" audit_summary.py "$OUT" "$PREV" > "$OUT/summary.stdout" 2>&1; else "$PY" audit_summary.py "$OUT" > "$OUT/summary.stdout" 2>&1; fi
RC=$?
cat "$OUT/summary.stdout"
WRONG=$(grep -E "^WRONG rows:" "$OUT/summary.stdout" | grep -oE "[0-9]+" | head -1)
NEW=$(grep -E "^WRONG rows:" "$OUT/summary.stdout" | grep -oE "\(([0-9]+) new" | grep -oE "[0-9]+")
echo "$TODAY,done,$DUMPS/$N dumps,${WRONG:-?} wrong,${NEW:-n/a} new," >> "$BASE/history.csv"
# a desktop notification when something is wrong or a lot of tickers failed to load
if [ "${WRONG:-0}" != "0" ] || [ "$DUMPS" -lt "$(( N * 9 / 10 ))" ]; then
  /usr/bin/osascript -e "display notification \"$WRONG wrong rows, $DUMPS/$N tickers dumped. See $OUT/SUMMARY.txt\" with title \"STA nightly audit\"" 2>/dev/null
fi
echo "=== done $(date +%H:%M)"
exit 0
