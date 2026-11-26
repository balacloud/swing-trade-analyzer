#!/bin/bash
# Plan + Opus review + three-pass gate (Golden Rules 41, 55, 64).
#   Stop hook (no args): if code files changed since the last review stamp, block the stop once and tell Claude to run /three-pass.
#   --stamp "note" --plan FILE        : record the current code state as reviewed. FILE must be a plan under docs/claude/design/ that
#                                       has an Opus review section with a verdict (GO / GO WITH CHANGES), was NOT written after the code,
#                                       and is not a "waiting for Opus review" draft.
#   --stamp "note" --trivial "kind: reason" : the exemption for trivial changes (Golden Rule 55). kind = dead-code | docstring | label |
#                                       wording | rename | version. Needs a reason of 8+ characters. Logged to .claude/.review_log.tsv.
#   --plan-check FILE                 : say whether FILE would be accepted as a plan (use before building).
#   --status                          : list the code files that are not yet stamped.
# "Code files" = frontend/src, frontend/scripts and backend source (.js .jsx .mjs .py, plus backend/reference/*.json).
# Docs, data, logs, caches and test output are ignored. No changed code files = nothing to review = never blocks, nothing required.
# Fast: file reads only, no network, no tests. Fails open on its own errors (a broken gate must never trap a session).
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root" || exit 0
marker="$root/.claude/.three_pass_done"
logfile="$root/.claude/.review_log.tsv"

changed_files() {
  { git diff --name-only HEAD -- frontend/src frontend/scripts backend 2>/dev/null
    git ls-files -o --exclude-standard -- frontend/src frontend/scripts backend 2>/dev/null; } | sort -u \
  | grep -E '\.(js|jsx|mjs|py)$|^backend/reference/.*\.json$' \
  | grep -Ev '(^|/)(venv|node_modules|__pycache__|build|data|logs|validation_results[^/]*|backtest_results[^/]*)/' \
  | grep -Ev '^backend/reference/data_audit_latest\.json$'   # Day 135: generated audit report, read only to DISPLAY notes (Data Sources tab, Analyze header via data_quality.read_tracking), no trading or verdict logic reads it. Other reference/*.json (known_splits.json) stay counted.
}

fingerprint() {
  changed_files | while IFS= read -r f; do
    if [ -f "$f" ]; then printf '%s:%s\n' "$f" "$(shasum "$f" | cut -d' ' -f1)"; else printf '%s:gone\n' "$f"; fi
  done | shasum | cut -d' ' -f1
}

# newest modification time (epoch seconds) among the changed code files; 0 when none
newest_code_mtime() {
  changed_files | while IFS= read -r f; do [ -f "$f" ] && stat -f %m "$f" 2>/dev/null; done | sort -n | tail -1
}

# plan_problem FILE -> prints why FILE is not an acceptable plan; prints nothing when it is acceptable
plan_problem() {
  local f="$1"
  [ -n "$f" ] || { echo "no plan file given"; return; }
  [ -f "$f" ] || { echo "plan file not found: $f"; return; }
  case "$(cd "$(dirname "$f")" && pwd)/$(basename "$f")" in
    "$root"/docs/claude/design/*) ;;
    *) echo "a plan must live under docs/claude/design/"; return ;;
  esac
  grep -qi 'plan' <<<"$(basename "$f")" || { echo "the file name must contain PLAN (like TRADIER_ERROR_HANDLING_PLAN_DAY127.md)"; return; }
  grep -qi 'opus review' "$f" || { echo "no 'Opus review' section in the plan: get the plan reviewed by Opus first (Golden Rule 55)"; return; }
  head -3 "$f" | grep -qi 'waiting for opus review' && { echo "the plan header still says 'waiting for Opus review'"; return; }
  grep -Eiq 'GO WITH CHANGES|verdict[: ]+\**GO\b' "$f" || { echo "the Opus review has no verdict (GO or GO WITH CHANGES; NO-GO is not accepted)"; return; }
  # a plan written AFTER the code is not a plan: its birth time must be earlier than the newest changed code file
  local born newest; born=$(stat -f %B "$f" 2>/dev/null); newest=$(newest_code_mtime)
  if [ -n "$born" ] && [ "$born" -gt 0 ] && [ -n "$newest" ] && [ "$born" -gt "$newest" ]; then
    echo "the plan file was created after the newest code change, so it was not a plan for this work (write the plan first)"; return
  fi
}

# trivial_problem "kind: reason" -> prints why the exemption is not acceptable
trivial_problem() {
  local t="$1" kind reason
  kind=$(printf '%s' "$t" | sed -E 's/^[[:space:]]*([A-Za-z-]+)[[:space:]]*:.*/\1/' | tr 'A-Z' 'a-z')
  reason=$(printf '%s' "$t" | sed -E 's/^[^:]*:[[:space:]]*//')
  case "$kind" in dead-code|docstring|label|wording|rename|version) ;; *) echo "kind must be one of: dead-code, docstring, label, wording, rename, version (got '$kind')"; return ;; esac
  [ "${#reason}" -ge 8 ] || { echo "give a reason of at least 8 characters after the colon"; return; }
}

case "$1" in
  --plan-check)
    p=$(plan_problem "$2")
    if [ -z "$p" ]; then echo "Plan accepted: $2"; else echo "Plan NOT accepted: $p"; exit 1; fi
    exit 0 ;;
  --stamp)
    note="${2:-three passes done}"
    shift 2 2>/dev/null
    plan=""; trivial=""
    while [ $# -gt 0 ]; do
      case "$1" in --plan) plan="$2"; shift 2 ;; --trivial) trivial="$2"; shift 2 ;; *) shift ;; esac
    done
    n=$(changed_files | wc -l | tr -d ' ')
    kind="none"; ref="-"
    if [ "$n" -gt 0 ]; then
      if [ -n "$plan" ]; then
        p=$(plan_problem "$plan"); [ -z "$p" ] || { echo "Stamp REFUSED: $p"; exit 1; }
        kind="plan"; ref="$plan"
      elif [ -n "$trivial" ]; then
        p=$(trivial_problem "$trivial"); [ -z "$p" ] || { echo "Stamp REFUSED: $p"; exit 1; }
        kind="trivial"; ref="$trivial"
      else
        echo "Stamp REFUSED: $n code files changed. Give --plan docs/claude/design/<NAME>_PLAN_<DAY>.md (with an Opus review verdict) or --trivial \"kind: reason\" (Golden Rule 55)."
        exit 1
      fi
    fi
    printf '%s\n%s | %s | %s %s\n' "$(fingerprint)" "$(date '+%Y-%m-%d %H:%M')" "$note" "$kind" "$ref" > "$marker"
    printf '%s\t%s\t%s\t%s\t%s\n' "$(date '+%Y-%m-%d %H:%M')" "$kind" "$ref" "$n" "$note" >> "$logfile"
    echo "Review stamp saved: $note ($n code files covered; $kind: $ref)"
    exit 0 ;;
  --status)
    n=$(changed_files | wc -l | tr -d ' ')
    if [ "$n" = "0" ]; then echo "Nothing to review: 0 code files changed"; exit 0; fi
    if [ "$(head -1 "$marker" 2>/dev/null)" = "$(fingerprint)" ]; then echo "Reviewed: $n code files, stamp: $(sed -n 2p "$marker")"; else echo "NOT reviewed: $n code files changed since the last stamp"; changed_files; fi
    exit 0 ;;
esac

input=$(cat)
# A second Stop in a row means Claude was already told once: let it through so a session never loops.
[ "$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null)" = "true" ] && exit 0
[ -z "$(changed_files)" ] && exit 0
[ "$(head -1 "$marker" 2>/dev/null)" = "$(fingerprint)" ] && exit 0
n=$(changed_files | wc -l | tr -d ' ')
jq -n --arg r "Code changed ($n files under frontend/src, frontend/scripts or backend) since the last review stamp. Required for every code change (Golden Rules 41, 55, 64): (1) a written plan in docs/claude/design/ with an Opus review verdict, (2) /three-pass: pass 1 read the diff, pass 2 edge cases, pass 3 real page or real data, (3) the stamp: bash .claude/hooks/three_pass_check.sh --stamp \"three passes done\" --plan <plan file>. Only a trivial change (dead-code, docstring, label, wording, rename, version) may skip the plan: --stamp \"...\" --trivial \"kind: reason\" (it is logged and listed at session close). Check a plan first with: bash .claude/hooks/three_pass_check.sh --plan-check <file>." \
  '{decision: "block", reason: $r}'
exit 0
