#!/bin/bash
# Tests for three_pass_check.sh (plan + Opus review + three-pass gate). Runs in a THROWAWAY git repo, never in the real one.
# Run: bash .claude/hooks/test_three_pass_check.sh
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d /tmp/gate_test.XXXXXX)" || exit 1
trap 'rm -rf "$tmp"' EXIT
pass=0; fail=0
ok()   { pass=$((pass+1)); }
bad()  { fail=$((fail+1)); echo "FAIL $1"; }
check(){ if [ "$2" = "0" ]; then ok; else bad "$1"; fi; }

cd "$tmp" || exit 1
git init -q . && git config user.email t@t && git config user.name t
mkdir -p .claude/hooks backend docs/claude/design
cp "$here/three_pass_check.sh" .claude/hooks/ && chmod +x .claude/hooks/three_pass_check.sh
echo "x = 1" > backend/a.py
git add -A && git commit -q -m init
G=".claude/hooks/three_pass_check.sh"

good_plan() { printf '# Thing plan (Day 1), v2, Opus review applied\n\n## Opus review, applied (verdict GO WITH CHANGES)\n' > "$1"; }

# 1. nothing changed: stamp needs nothing, Stop never blocks
bash $G --stamp "x" >/dev/null 2>&1; check "no changes: stamp without plan allowed" $?
out=$(echo '{}' | bash $G); [ -z "$out" ]; check "no changes: Stop does not block" $?

# 2. a code change appears (the plan files come later or earlier in the cases below)
sleep 1.2; echo "x = 2" >> backend/a.py
out=$(echo '{}' | bash $G); echo "$out" | grep -q '"decision": "block"'; check "code changed: Stop blocks" $?
echo "$out" | grep -q 'Opus review'; check "block message names the Opus review requirement" $?
echo "$out" | grep -q -- '--trivial'; check "block message names the trivial exemption" $?
[ "$(echo '{"stop_hook_active": true}' | bash $G)" = "" ]; check "second Stop in a row is let through (never loops)" $?

# 3. refusals
before=$(cat .claude/.three_pass_done 2>/dev/null)
bash $G --stamp "three passes done" >/dev/null 2>&1; [ $? -ne 0 ]; check "stamp with no plan and no trivial is refused" $?
[ "$(cat .claude/.three_pass_done 2>/dev/null)" = "$before" ]; check "a refused stamp leaves the marker unchanged" $?
bash $G --stamp "s" --plan docs/claude/design/NOPE_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "missing plan file refused" $?
echo "# no review here" > docs/claude/design/A_PLAN_DAY1.md
bash $G --stamp "s" --plan docs/claude/design/A_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "plan without an Opus review refused" $?
printf '# Thing plan, waiting for Opus review\n## Opus review\nverdict GO\n' > docs/claude/design/B_PLAN_DAY1.md
bash $G --stamp "s" --plan docs/claude/design/B_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "plan still 'waiting for Opus review' refused" $?
printf '# Thing plan\n## Opus review\nverdict: NO-GO\n' > docs/claude/design/C_PLAN_DAY1.md
bash $G --stamp "s" --plan docs/claude/design/C_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "NO-GO verdict refused" $?
printf '# Thing plan\n## Opus review\nno verdict written\n' > docs/claude/design/D_PLAN_DAY1.md
bash $G --stamp "s" --plan docs/claude/design/D_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "Opus section without a verdict refused" $?
good_plan docs/claude/design/RANDOM_NOTES_DAY1.md
bash $G --stamp "s" --plan docs/claude/design/RANDOM_NOTES_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "file name without PLAN refused" $?
good_plan README_PLAN.md
bash $G --stamp "s" --plan README_PLAN.md >/dev/null 2>&1; [ $? -ne 0 ]; check "plan outside docs/claude/design refused" $?
sleep 1.2; good_plan docs/claude/design/LATE_PLAN_DAY1.md      # created AFTER the code change
bash $G --stamp "s" --plan docs/claude/design/LATE_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "a plan created after the code is refused" $?
bash $G --plan-check docs/claude/design/LATE_PLAN_DAY1.md >/dev/null 2>&1; [ $? -ne 0 ]; check "--plan-check refuses it too" $?

# 4. trivial exemption rules
bash $G --stamp "s" --trivial "refactor: tidy up" >/dev/null 2>&1; [ $? -ne 0 ]; check "unknown trivial kind refused" $?
bash $G --stamp "s" --trivial "wording: ok" >/dev/null 2>&1; [ $? -ne 0 ]; check "too-short reason refused" $?
bash $G --stamp "s" --trivial "wording" >/dev/null 2>&1; [ $? -ne 0 ]; check "trivial without a reason refused" $?

# 5. accepted plan: the plan must exist BEFORE the code, so make a new change after writing it
good_plan docs/claude/design/GOOD_PLAN_DAY1.md
sleep 1.2; echo "x = 3" >> backend/a.py
bash $G --plan-check docs/claude/design/GOOD_PLAN_DAY1.md >/dev/null 2>&1; check "--plan-check accepts a good plan written before the code" $?
bash $G --stamp "three passes done" --plan docs/claude/design/GOOD_PLAN_DAY1.md >/dev/null 2>&1; check "stamp with a good plan accepted" $?
out=$(echo '{}' | bash $G); [ -z "$out" ]; check "after the stamp Stop does not block" $?
bash $G --status | grep -q '^Reviewed'; check "--status says Reviewed" $?
grep -q 'GOOD_PLAN_DAY1' .claude/.review_log.tsv; check "the stamp is logged with the plan name" $?
sleep 1.2; echo "x = 4" >> backend/a.py
out=$(echo '{}' | bash $G); echo "$out" | grep -q block; check "a further code change blocks again" $?

# 6. accepted trivial exemption (logged)
bash $G --stamp "text-only" --trivial "version: bump BACKEND_VERSION label" >/dev/null 2>&1; check "valid trivial exemption accepted" $?
grep -q 'trivial' .claude/.review_log.tsv && grep -q 'bump BACKEND_VERSION' .claude/.review_log.tsv; check "the exemption and its reason are logged" $?
out=$(echo '{}' | bash $G); [ -z "$out" ]; check "after a trivial stamp Stop does not block" $?

# 7. non-code changes never require anything
git add -A && git commit -q -m c2
echo "notes" > docs/claude/design/notes.md
out=$(echo '{}' | bash $G); [ -z "$out" ]; check "docs-only change never blocks" $?
bash $G --stamp "x" >/dev/null 2>&1; check "docs-only change: stamp needs no plan" $?

echo "$pass passed, $fail failed"
[ "$fail" = "0" ]
