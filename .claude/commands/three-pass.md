---
description: Run the three escalating review passes on the current code changes, then stamp them as reviewed (Golden Rule 41)
argument-hint: [skip]
---

Run the three review passes on everything that changed in `frontend/src`, `frontend/scripts` and `backend` since the last stamp. Find the files with `bash .claude/hooks/three_pass_check.sh --status`.

**Before the passes (Golden Rules 55 and 64): is there a plan?** Every code change needs a written plan in `docs/claude/design/<NAME>_PLAN_<DAY>.md` with an Opus review verdict (GO or GO WITH CHANGES), written BEFORE the code. Check it with `bash .claude/hooks/three_pass_check.sh --plan-check <plan file>`. The stamp is refused without it.

If the argument is `skip`: only allowed for a trivial change with no logic: dead-code deletion, a docstring, a label or wording fix, a rename with no callers, or a version number. Say plainly what changed, then run `bash .claude/hooks/three_pass_check.sh --stamp "text-only skip" --trivial "<kind>: <reason>"` (kind is one of dead-code, docstring, label, wording, rename, version; the reason is at least 8 characters; it is logged and listed at session close) and stop.

Otherwise do the passes in order, using the checklists in `docs/claude/stable/ENGINEER.md` (data, keys, exceptions, testing, performance, edge cases) as the list of things to try to break. Each one must dig deeper than the last, and each must find something or say why it could not:

1. **Read the diff.** Read every changed file as a reviewer: wrong logic, wrong wording, unused or leftover code, callers not updated (grep every caller, Golden Rule 54), parity between JS and Python copies (Golden Rules 19/21).
2. **Edge cases.** Try to break it: missing, null, NaN, empty, one item, many items, very large or very small numbers, short history, tz-aware dates. Add a test for each real bug found.
3. **Real data and real page.** Run the full test suites for the touched area and the live page checker (`cd frontend && node scripts/ui-verify-checklist.js AAPL SOXL.NE NVDA RIVN`). For UI changes take screenshots at phone (390px) and desktop width and look at them. For backend changes run against real cached data.

Fix what you find, re-run the tests, then report plainly (simple English): per pass, what was found and fixed, and the final test results. Only when all three passes are done and everything passes, run:

`bash .claude/hooks/three_pass_check.sh --stamp "three passes done" --plan docs/claude/design/<NAME>_PLAN_<DAY>.md`

Never stamp if a test fails or a pass was skipped.
