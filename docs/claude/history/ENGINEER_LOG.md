---
type: history
name: engineer-log
description: ENGINEER.md's per-session miss table (Days 127-132) and Feedback Log, moved out on Day 133. Append-only.
last_updated: Day 133 (2026-11-24)
---

# ENGINEER LOG (L3, append-only)

> Moved word for word from `ENGINEER.md` on Day 133. `/sta-end` adds new miss rows and log entries here. The themes table (earlier days) stays in `stable/ENGINEER.md`.

## Misses by session (Days 127-132)

### This session (Days 127-129), mine
| Miss | Habit that catches it |
|---|---|
| Audit read fresh downloads, not the app's saved copy: 15 tickers with an empty newest bar passed (Rule 66) | Read what the check reads; audit the copy the app uses |
| `/api/sr` sent invalid JSON (`NaN`) and `/api/stock` a fake price 0 | Valid JSON always; null or an error, never a plausible fake |
| An existing freshness check read the wrong "last bar" while I said "nothing checks it" | Grep before claiming absence |
| Tradier 400 counted as "provider broken" (Rule 65) | Docs plus a real probe before classifying a code |
| "The audit used up Twelve Data's limit" said before measuring (the cache showed Yahoo already served 61 of 97) | Label measured vs inferred; measure first |
| "Audit took ~8 minutes" (unmeasured); "35k tokens" (forgot the monthly call) | Estimates need a measured basis and every call counted |
| "QPUX/DRAL match IBKR on every completed day" (the truth file covered 5 days) | State the exact window a claim covers |
| C9 included the unfinished day: false QPUX/DRAL alarms | Partial bars (Rule 39), applied to our own tools |
| The "after-close" re-run silently reused the morning's saved downloads (Twelve Data volume still 800) | Check the output changed; look at timestamps and volumes, not exit codes |
| Missed SGRD.TO when batching | Count in, count out; reconcile against the full list |
| A tab-warning plan claimed "the tab shows no warning" and "about 25 tickers" (it was 21, and the tab already warned on some) | Re-derive numbers from the data before writing them into a plan |
| A "JSON safety net" that depends on the same unreadable JSON | Ask: if the thing I rely on fails, does my safety net fail with it? |
| A cache-miss rule that Tradier's 45-minute expiry already made unnecessary | Read the existing mechanism before adding one |
| Alpaca plan v1 missed: `end` makes free-plan requests 403; Twelve Data 404 counted as breaker failure (315 log lines); the API key written in `backend.log` (324 lines); the 16:00-16:30 cache hole; hard-coded source lists in `audit_vs_ibkr.py`; the "primary" role label | Pre-mortem: list every place a new provider is named, every way its API can refuse, every log it can leak into |
| "Twelve Data breaker opened about 82 times" mixed false 404 failures with real rate limits | Break a count into causes before quoting it |
| Test flaws: a file named `NOTAPLAN` tripped a keyword gate; a test assumed a reader returns non-None when all sections pass; a ticker already cached made a "plain ticker" test hit the cache; log capture missed the exception path | Test the test; fresh names, fresh state, read the code under test |
| zsh/macOS slips: `timeout` missing, `sed -i` needs a suffix, `\s` in `sed -E`, unquoted globs | Use portable commands; quote globs; check the shell |
| Edited a module under a running dev server (reloader restarted mid-request) | Know what is running |
| Reported done before the user-facing summary of the last stamp was sent | Close the loop in the user's words |
| Repeated a Known Issues line ("MR route reads Yahoo directly") as a fact and put it in a fix list; the code and one `curl` showed it was stale (Rule 69) | A note is a claim: read the named lines and run one call before repeating or planning it |
| A parity grid that never contained the missing values (None, 0) let a fake-50 bug live for years; JS turned RSI 0 into 50 while Python kept 0 | Put missing and zero values in the grid; mutation-check the new tests |
| Version constants in code (footer v4.64, `BACKEND_VERSION` 2.57) lagged the docs (v4.69, 2.58) | At close, compare the code constants with the docs |
| A "match" that rested on an estimated input was reported as closing a gap (Day 132: one number was an estimate, so the "match" was circular) | Before calling two numbers a match, ask whether either one is built from an estimate; a circular match proves nothing |

## Feedback Log (append-only, most recent first)
- **Day 132:** non-STA task. What worked: held a publish until warnings were explained and cross-checked totals against the broker's own figures, which exposed trades the positions did not hold. What I missed: told the user a gap "closed" using an estimated input (circular), and wrote private figures into repo docs at session close (caught by the push gate; the memory note already said keep it out of STA). Could not prove ENGINEER.md was loaded earlier in the session (post-compaction), so re-read it.
- **Day 131:** first use of the plan-mode flow end to end on a verdict-engine change. What worked: Opus caught two false on-card texts, the `null < 30` trap, and the missing RSI-0 grid row; the baseline-by-input comparison and the mutation check proved nothing moved where inputs are present. What I missed: repeating a stale Known Issues line before reading the code (Rule 69). The user's steer: "we need to see light at the end of the tunnel" (keep fixes small and finished).
- **Day 129 close:** the persona was written mid-session, so this close is its first use. Misses it would have caught earlier, now in Golden Rules 67-68: a provider's "not covered" answer counted as a health failure and the key printed in an error text (found only by the Opus review asking "what does the existing provider do with the same case?"); an audit check (C8) that never read the page it was grading; a cache expiry rule written for one source instead of at the one write point. Process: a "completed" background notification was read as "audit done" without checking `pgrep` and timestamps. The user's reaction to the session: asked for this persona, and said "i dont want to go in to rabit holes" (keep fixes surgical, no side quests).
- **Day 129:** Created. The user asked for "a fantastic coding developer persona who is very surgical and does not miss things", covering data keys, exception handling, testing, performance and edge cases. The misses table above is the Day 127-129 record: the Opus reviews of the Tradier plan (7 changes) and the Alpaca plan (11 changes) caught things this checklist is meant to catch before review.

## Day 133

| Miss | Habit that catches it |
|---|---|
| Layering plan v1 assumed the open priorities were in ROADMAP's header, that KNOWN_ISSUES splits by section, and that the session protocol lived in one place; the Opus review found all three wrong (open priorities sat in a table marked HISTORICAL; open items hid under "Changes from" headings; the protocol was copied in six files) | Read the whole file before planning a move of it (I had read ROADMAP lines 1-268 of 1,104); grep for every copy of a rule before moving it (Rule 59) |

- **Day 133:** docs layering. What worked: Opus plan review before any move; nothing-lost scripts (byte-identical rules, line counts in = out); a cold-start agent as the probe test, which found a vague pointer and a wrong count that no checker would.

## Day 134

| Miss | Habit that catches it |
|---|---|
| Alpaca was "rolled out" Day 129 but the running app never used it for about 4 days: stale keys in the long-lived parent environment beat the fixed `.env` (`load_dotenv` does not override), so Alpaca returned 401 and the chain fell through quietly | After any key or provider change, make one real call through the running process and read which source answered; restart the parent, not only the child |
| A same-size source edit made and reverted inside one second kept a stale Python bytecode cache, so a mutation test showed false failures | Make mutations change the file size, or delete `__pycache__` before trusting a mutant result |
| Two cards used two "now" prices (live quote vs last completed close) and the plan stayed on screen after price fell through it | When two cards show the same idea with different inputs, check the case where the inputs disagree most |
| The Key Levels note appeared beside "no pullback plan" and the page check demanded a tick the card does not draw in the no-ATR state (found in the edge pass) | Drive every card state, including the empty ones, on the real page before calling the build done |

- **Day 134:** void-plan build. What worked: plan and Opus review first (the review forced the "no tuned numbers" rule and the pre/post fact-only split); an independent mirror of the rule in the audit and the page checker, not a copy; 13 edge scenarios on the real page at both widths; mutation checks on the boundary, the quote-state gate, the Size rule and the audit claims. What I missed: the stale-bytecode false alarm (above), and the Alpaca miss which sat unseen for days.

