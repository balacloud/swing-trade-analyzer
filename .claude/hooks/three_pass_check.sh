#!/bin/bash
# Three-pass review gate (Golden Rule 41).
#   Stop hook (no args): if code files changed since the last review stamp, block the stop once and tell Claude to run /three-pass.
#   --stamp "note"     : record the current code state as reviewed ("three passes done" or "text-only skip").
#   --status           : list the code files that are not yet stamped.
# "Code files" = frontend/src, frontend/scripts and backend source (.js .jsx .mjs .py, plus backend/reference/*.json).
# Docs, data, logs, caches and test output are ignored. No changed code files = nothing to review = never blocks.
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root" || exit 0
marker="$root/.claude/.three_pass_done"

changed_files() {
  { git diff --name-only HEAD -- frontend/src frontend/scripts backend 2>/dev/null
    git ls-files -o --exclude-standard -- frontend/src frontend/scripts backend 2>/dev/null; } | sort -u \
  | grep -E '\.(js|jsx|mjs|py)$|^backend/reference/.*\.json$' \
  | grep -Ev '(^|/)(venv|node_modules|__pycache__|build|data|logs|validation_results[^/]*|backtest_results[^/]*)/'
}

fingerprint() {
  changed_files | while IFS= read -r f; do
    if [ -f "$f" ]; then printf '%s:%s\n' "$f" "$(shasum "$f" | cut -d' ' -f1)"; else printf '%s:gone\n' "$f"; fi
  done | shasum | cut -d' ' -f1
}

case "$1" in
  --stamp)
    printf '%s\n%s | %s\n' "$(fingerprint)" "$(date '+%Y-%m-%d %H:%M')" "${2:-three passes done}" > "$marker"
    echo "Review stamp saved: ${2:-three passes done} ($(changed_files | wc -l | tr -d ' ') code files covered)"
    exit 0 ;;
  --status)
    n=$(changed_files | wc -l | tr -d ' ')
    if [ "$(head -1 "$marker" 2>/dev/null)" = "$(fingerprint)" ]; then echo "Reviewed: $n code files, stamp: $(sed -n 2p "$marker")"; else echo "NOT reviewed: $n code files changed since the last stamp"; changed_files; fi
    exit 0 ;;
esac

input=$(cat)
# A second Stop in a row means Claude was already told once: let it through so a session never loops.
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null)" = "true" ] && exit 0
[ -z "$(changed_files)" ] && exit 0
[ "$(head -1 "$marker" 2>/dev/null)" = "$(fingerprint)" ] && exit 0
n=$(changed_files | wc -l | tr -d ' ')
jq -n --arg r "Code changed ($n files under frontend/src, frontend/scripts or backend) since the last three-pass review. Run /three-pass now: pass 1 read the diff, pass 2 edge cases, pass 3 real page or real data. Then stamp it. If the change was text only, run /three-pass skip and say so." \
  '{decision: "block", reason: $r}'
exit 0
