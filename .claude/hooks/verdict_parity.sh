#!/bin/bash
# PostToolUse hook: rerun the JS<->Python verdict parity test whenever a file
# holding the verdict rule is edited. Exit 2 feeds the failure back to Claude.
f=$(jq -r '.tool_input.file_path // .tool_response.filePath // empty')
case "$f" in
  */frontend/src/utils/categoricalAssessment.js|*/backend/backtest/categorical_engine.py) ;;
  *) exit 0 ;;
esac
root="$(cd "$(dirname "$0")/../.." && pwd)"
out=$("$root/backend/venv/bin/python" "$root/backend/backtest/test_verdict_parity.py" 2>&1)
if [ $? -ne 0 ]; then
  echo "Verdict parity test FAILED after editing $f (frontend and backtest verdict rules disagree):" >&2
  echo "$out" | tail -25 >&2
  exit 2
fi
exit 0
