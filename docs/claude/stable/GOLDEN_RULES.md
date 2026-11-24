# GOLDEN RULES FOR CLAUDE

> **Purpose:** Core rules and cumulative lessons learned — stable reference
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 133 (2026-11-24)
> **Session protocols:** See `CLAUDE_CONTEXT.md` for startup/close checklists
> **Decision-making lens:** See `docs/claude/stable/PERSONA.md` for the trading-judgment persona (Golden Rule 34)

---

## CORE RULES (69 Golden Rules; no Rule 27, see ENGINEER.md note)


## HOW THIS FILE WORKS (layered, Day 133)

Rules 1-15 and the "always" rules (52, 55, 59, 62, 69; also 6 and 13 above) are written in full here. Every other rule has one index line: number, short title, and when to open it. **When your task matches a trigger, open the cluster file and read the full rule before acting.** Rule numbers never changed. Cluster files: `docs/claude/stable/rules/<cluster>.md`.

There are 68 rules (numbered 1-69; there is no Rule 27, and "Rule 27" in the Day 91 history means Rule 29).

## CORE RULES (1-15, full text)

1. **START of session:** Read PROJECT_STATUS_DAY[N].md first
2. **BEFORE modifying any file:** READ it first using Read tool
3. **NEVER assume code structure** — always verify with actual file
4. **END of session:** Create updated PROJECT_STATUS_DAY[N+1].md
5. **User will say "session ending"** to trigger status file creation
6. **NEVER HALLUCINATE** — Don't claim results without running them
7. **THINK THROUGH** — Pause and reason before solutions
8. **ALWAYS VALIDATE** — Fact-check against external sources
9. **GENERATE FILES ONE AT A TIME** — Wait for confirmation before next
10. **FOLLOW CODE ARCHITECTURE RULES** — Producer defines API, consumer adapts
11. **DEBUG APIS PROPERLY** — Run diagnostic queries FIRST
12. **LOCAL FILES FIRST, THEN GIT** — Edit/Write tools first, then commit
13. **EXHAUSTIVE VERIFICATION** — Check EVERY item, not a sample
14. **UPDATE "LAST UPDATED" DATES** — On any file in `docs/claude/stable/`
15. **NEVER IMPLEMENT WITHOUT VALIDATION** — Require research, backtest, or practitioner consensus

## ALWAYS-READ RULES (full text)

52. **A CLAIM THAT A FILE WAS EDITED IS NOT THE SAME AS THE EDIT TOOL ACTUALLY BEING CALLED — VERIFY BEFORE THE SESSION CLOSES, NOT AFTER.** Responding to the user's direct pushback on the Analyze Page Redesign's Regime gate, a reply said "I updated the decision doc to reflect this reversal" — but no Edit tool call had actually been made at that point; the sentence described a completed action that hadn't happened yet. Not caught until `/sta-end`'s Step 0, while reconstructing "what actually happened this session" for the close-out summary — at which point a grep/re-read of the file confirmed the claimed change wasn't there, and it had to be made for real before the session could close honestly. This is Golden Rule 6 ("never hallucinate — don't claim results without running them") in its most literal form: a past-tense claim about a tool action ("I updated X," "I fixed Y," "I ran Z") is exactly as checkable as a computed number or a status-doc figure, and just as capable of quietly being wrong — the difference is nobody thinks to double-check a sentence that reads as already-done. **How to apply:** before writing any session-close summary — or any sentence claiming a past action is already complete — reread the actual file or check the tool-call history to confirm the claimed change is really there. Treat your own prior claims with the same suspicion Golden Rule/`feedback_live_status_not_stale_doc` already applies to a stale status doc: a sentence that *sounds* like confirmation isn't confirmation. (Day 110, Analyze Page Redesign Regime reversal)

55. **NON-TRIVIAL FIXES ARE OPUS-PLANNED BEFORE SONNET IMPLEMENTS — TRIVIAL ONES ARE NOT.** A fix gets a written Opus plan first (premises checked against the actual code, blast radius, chosen approach with alternatives weighed, phasing, verification steps) — which Sonnet then implements *to* — when it meets any of: (a) it touches frozen forward-test logic or its inputs; (b) it modifies a shipped live badge / signal / gate; (c) the function/value being changed has more than one downstream consumer; (d) it changes a threshold or a methodology. Pure-isolated, zero-risk changes — dead-code deletion, a docstring or label fix, a rename with no callers — skip the plan. **Why the carve-out is load-bearing:** Day 111 ran this pattern twice (MR Scanner, Volume Confirmation) and *both* Opus plans corrected wrong premises in the brief before any code was written; Day 112's S&R plan corrected three (the pattern target lives in the frontend not `pattern_detection.py`; the MTF `strength` field is not just hardcoded but dead; the S&R bug's blast radius was an 80/20 method-mix flip, not just "a far level") and found two new bugs. That is the value. But a blanket "everything goes through Opus" invites rubber-stamp plans — the same failure mode Golden Rule 41 already names for its own review passes ("inventing a finding to justify the ritual is exactly the kind of dishonesty this project's own 'never hallucinate' discipline exists to catch"). Scope it, so the plan is always doing real work. (Day 112, user-proposed as blanket, adopted scoped) **Enforced since Day 128 (user: "it has to be in the hook"):** the flow for every code change is (1) the plan is made in Claude Code's plan mode (EnterPlanMode; the user approves at ExitPlanMode); (2) it is written to `docs/claude/design/<NAME>_PLAN_<DAY>.md` and reviewed by Opus, the changes are applied and the user is told what changed; (3) build; (4) `/three-pass`; (5) `bash .claude/hooks/three_pass_check.sh --stamp "three passes done" --plan <plan file>`. The stamp is REFUSED unless the plan exists under `docs/claude/design/`, has an Opus review section with a verdict (GO or GO WITH CHANGES, never NO-GO, never "waiting for Opus review"), and was created before the newest code change (`--plan-check <file>` tests a plan first). The only way around it is `--trivial "kind: reason"` for dead-code, docstring, label, wording, rename or version changes (reason 8+ characters); every use is logged to `.claude/.review_log.tsv` and `/sta-end` lists it. The hook cannot prove plan mode was used; it proves the plan and the Opus verdict exist. Tests: `.claude/hooks/test_three_pass_check.sh` (in `run_all_checks.sh`).

59. **ONE RULE, ONE PLACE. BEFORE CHANGING A RULE, THRESHOLD, LABEL OR VERDICT, FIND EVERY COPY OF IT AND CHANGE THEM TOGETHER OR NOT AT ALL.** On Day 122 Claude recommended dropping Trend Template checks 5–8 from the frontend only. The user asked what an architect would say, and the answer reversed it: the 7-of-8 rule lives in 4 places (`categoricalAssessment.js:342` verdict, `pattern_detection.py:282` Stage 2 badge on the same Analyze page, `backtest/categorical_engine.py:71`, `backtest/parameter_stability.py:183`). A frontend-only change would have shown a verdict and a Stage 2 badge that disagree on the same stock, and detached every quoted backtest number from the live rule. **How to apply:** grep for every copy before proposing the change; same stock must get the same answer on every screen; the display must match the engine; quoted numbers must describe the live rule; prefer the change with the smaller blast radius. See PERSONA.md "The Architect's Lens". A PostToolUse hook (`.claude/hooks/verdict_parity.sh`) reruns `test_verdict_parity.py` on any edit to `categoricalAssessment.js` or `backtest/categorical_engine.py`, so a JS↔Python verdict drift fails immediately. (Day 122, Technical Read card)

62. **TALK TO THE USER IN VERY SIMPLE ENGLISH, EVERY TIME.** Short sentences, everyday words. Say what you are doing and why in plain terms first; put file names, code and jargon after, only if needed. Explain any technical word in a few plain words the first time it appears. Progress updates are one or two simple lines ("I'm checking that the market numbers on screen match the data"), not a list of functions. **How to apply:** before sending, ask "would a non-programmer follow this?" If not, rewrite it simpler. (Day 124, user: "always use simple terms to explain, put this in golden rules going forward")

69. **A KNOWN-ISSUES LINE IS A CLAIM, NOT A FACT. READ THE CODE (AND RUN ONE CALL) BEFORE REPEATING IT OR PLANNING WORK ON IT.** Days 128-130 carried "the Mean-Reversion route reads Yahoo directly, around the provider chain". On Day 131 it was repeated to the user as a reason the Analyze tab was not yet trustworthy and put into a fix list. The plan-mode read showed `/api/mr/signal` and `/api/mr/scan` already call `get_data_provider().get_ohlcv()` first (fixed Days 82 and 111), and one `curl` answered `"dataSource": "DataProvider"`. The line was stale; nothing needed fixing. Same family as Golden Rules 26 and 37 (do not accept a diagnosis you did not reproduce), applied to our own notes. The same session's other fix showed the opposite case: the two engine bugs in the same list were real, and each needed both JS and Python copies changed and a parity grid that covers the missing values (86,400 -> 172,800 rows). **How to apply:** before listing a Known Issues item as work or as a reason for doubt, open the code at the named lines and run one real call; if it is stale, say so at once and fix the note. A fix that touches a verdict engine also adds the missing values (None, 0, NaN) to the parity grid and gets a mutation check (switch the fix off, expect failures). (Day 131)

## RULE INDEX (16-69; open the cluster file for the full text)

### process  (`rules/process.md`) — the plan/review/three-pass flow, session protocol, how to run a decision session
- **17.** Session start = read CLAUDE_CONTEXT.md first — read when: starting a session, startup checklist
- **24.** A one-line roadmap note is not an effort estimate — read when: before calling a backlog item simple or small
- **32.** Three review passes per fix — read when: superseded by Rule 41; history of the review rule
- **34.** Apply the master-trader persona lens to judgment calls — read when: threshold choices, interpreting results, PERSONA.md
- **41.** Escalating three-pass review — read when: every code change, /three-pass, review stamps
- **49.** Item-by-item Q&A for philosophy-level redesigns — read when: redesign decisions, decision logs
- **50.** A high-effort validation pass on your own reasoning — read when: before a design record is final
- **64.** A must-always process rule needs a hook — read when: adding or changing process enforcement

### claims-verification  (`rules/claims-verification.md`) — check a claim against the code or source before repeating it
- **26.** Reproduce an external audit's root cause first — read when: acting on an outside audit or review finding
- **37.** A missing cited source: research the claim itself — read when: a citation that cannot be found
- **42.** Parallel tool results can come back out of order — read when: parallel tool calls, ticker/result mapping
- **47.** 'Fixed' may be fixed at the symptom only — read when: citing a rule or bug as fixed
- **48.** Check the statistic is sensitive before escalating a gap — read when: a scary-looking gap in a metric
- **53.** A label like 'nearest' is a claim about the code — read when: labels such as nearest, strongest, best

### backtest-honesty  (`rules/backtest-honesty.md`) — out-of-sample, re-tuning, seeds, fill price, pre-registered predictions
- **16.** Equal weight, never optimise category weights — read when: changing scoring weights, adding a score category
- **18.** Reused OOS is not OOS — read when: tuning after seeing walk-forward results, forward-test freeze
- **20.** A pre-committed restriction is not a re-tune — read when: restricting a gate, Rule 18 questions
- **45.** A fixed seed reproduces only while the data is unchanged — read when: sampled backtests, universe drift
- **56.** Pre-registered predictions about gated backtests — read when: predicting a backtest result
- **60.** Price a backtest at a fill a person could get — read when: backtest or ledger entry price, open vs close

### engine-parity  (`rules/engine-parity.md`) — live vs backtest logic, replay of locked values, grid-test parity
- **19.** Grid-test parity, not hand-picked vectors — read when: verdict parity between two engines, categorical_engine tests
- **21.** Dry the shared logic before a live twin of a backtest — read when: building a live counterpart to a backtest engine
- **29.** Paper-trading replay reads locked entry values — read when: ledger replay, entry price, stops, targets
- **35.** Live/backtest parity must be verified directly — read when: any live engine that mirrors a backtest

### data-providers  (`rules/data-providers.md`) — rate limits, circuit breakers, error codes, units, splits, broker IDs, secrets in errors
- **22.** Rate-limiter/breaker state is per process — read when: shared rate limits, circuit breaker, multi-process backend
- **25.** Widening a candidate pool needs a measured limit — read when: more tickers per scan, provider quotas
- **36.** Breaker: 'ticker has no data' is not 'provider unhealthy' — read when: circuit breaker, provider health logic
- **40.** A per-ticker loop can mix timezone conventions — read when: multi-provider loops, date alignment
- **46.** A price mismatch may be a real split — read when: two providers disagree on price, split checks
- **58.** Take broker contract IDs from the user's own watchlist — read when: IBKR conId, contract lookups
- **61.** Normalise units per provider at the field map — read when: provider field maps, ratio vs percent
- **65.** An error code is not a meaning — read when: classifying provider errors
- **67.** 'I don't have it' is not a health signal; no key in error text — read when: provider failures, error messages

### cache-time-audit  (`rules/cache-time-audit.md`) — caches, partial bars, clocks, stamps, dev server, audit checks
- **23.** Redirect a backgrounded dev server's output — read when: start.sh, background servers, lost logs
- **28.** Stamp dates from the data, not the wall clock — read when: force-run on a non-trading day, signal dates, ledger
- **31.** A cache can outlive the fix — read when: after any fix to cached output, cache TTL
- **33.** A job's 'local time' comment is a claim — read when: launchd or cron schedules, timezone comments
- **39.** Replay engines must verify the last bar is closed — read when: partial daily bars, intraday data, live signals
- **43.** Clearing a backend cache does not reset frontend state — read when: cache clear, frontend refetch paths
- **66.** Audit the copy of the data the app uses — read when: data audits, cached vs fresh data
- **68.** An audit check must read what the user sees — read when: audit checks, cache rules across sources

### display-consumers  (`rules/display-consumers.md`) — new fields, transform layers, labels, status glyphs, who reads a value
- **30.** A new backend field is not live until every layer passes it — read when: adding an API field, transform layers, frontend mapping
- **38.** Reusing a field for a new axis: document both meanings — read when: overloading a column or API field
- **44.** Do not collapse 3+ failure reasons into one glyph — read when: batch status checks, error displays
- **51.** Audit the default view and every consumer before redesigning a display — read when: changing what a decision engine shows
- **54.** Display-looking functions may feed a live gate — read when: scoping a change, caller graph, forward-test gates
- **57.** Check who enumerates an object's keys before adding a field — read when: adding a key to a dict or object
- **63.** One label, one number — read when: labels, prices, or words shown in more than one place

---

## CODE ARCHITECTURE RULES

1. **Verify data contracts BEFORE writing code** — Check actual return structures
2. **Producer defines API** — Consumer (UI) adapts to producer (engine)
3. **Don't double-calculate** — If engine calculates RS, don't recalculate in UI
4. **Flat API structures preferred** — `scores.technical` > `breakdown.technical.score`
5. **Zero is not null** — Use null for missing data, never zero (Day 53)
6. **Return null, not a plausible fake** — No hardcoded fallback values (Day 54)
7. **DRY for business logic** — Shared calculations in utility modules (Day 61)

---

## DEBUGGING WORKFLOW

```
1. Understand the symptom
2. Form hypothesis about cause
3. Write diagnostic query to TEST hypothesis
4. Run diagnostic, analyze results
5. Only THEN write the fix
6. Test fix incrementally
7. If fix fails → back to step 2 (don't chain guesses)
```

---

## SYSTEM AUDIT PROTOCOL (Day 68, consolidated Day 72)

**Master framework:** `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`

5 audit types — use the right one for the situation:

| Situation | Audit Type |
|-----------|-----------|
| Validate a specific claim/threshold | **Claim Audit** (verdict labels per assertion) |
| After code changes / before release | **Coherence Audit** (Layer 1 consistency + Layer 2 correctness) |
| After major feature implementation | **Behavioral Audit** (runtime verification with real tickers) |
| Before building a new feature | **Design Audit** (spec vs architecture vs correctness) |
| Domain/research validation | **External LLM Audit** (multi-LLM consensus) |

Core principles:
1. **Layer 1 — Consistency:** Does documentation match code?
2. **Layer 2 — Correctness:** Is the logic sound? Thresholds justified? Correct on real data?
3. **Layer 3 — Behavior:** Does runtime output match what the code claims to produce?

> "README is marketing. Code is truth. But even true code can implement wrong logic."
> Master audit framework: `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`
> External audit prompts: `docs/research/EXTERNAL_LLM_AUDIT_PROMPTS.md`

---

## KEY LEARNINGS (Cumulative)

### Trading System Design (Day 27 — Van Tharp)
- Entry signals = ~10% of results; Position sizing = ~90%
- Backtest before believing any system (75-point scored 49.7% — random)
- R-Multiples > win rate; Expectancy = (Win% × Avg Win R) + (Loss% × Avg Loss R)
- Never risk more than 2% per trade; Track R-multiples, not dollar amounts

### Data Integrity
- **Cache schema versioning** — Auto-invalidate on version mismatch (Day 61)
- **NaN is worse than null** — 3-layer defense: backend transforms, cache, frontend (Day 61)
- **200-on-error is a silent lie** — Return 500, let frontend distinguish error from absence (Day 61)
- **Silent fallbacks are invisible lies** — VIX=20 on failure, F&G=50 on error mask real problems (Day 54)
- **Backend caching** — Restart backend periodically; 93% null fundamentals → 7% after restart (Day 25)
- **Timezone normalization** — yfinance tz-aware, TwelveData naive; normalize at boundaries (Day 52)
- **Live screeners have no point-in-time query** — TradingView's screener (and the live categorical assessment fed by it) only reflects the current market. A daily automated job that misses a scheduled run can correctly replay historical OHLCV to resolve what happened to *already-open* positions, but cannot retroactively reconstruct what a live screener *would have* returned on a missed past day — those entry signals are simply not generated, not backfilled. Design catch-up logic around this asymmetry rather than assuming full recoverability (Day 81, paper trading engine)

### Code Quality
- **Dual endpoints = guaranteed corruption** — Same data from 2 endpoints diverged silently (Day 53)
- **Dead code accumulates silently** — 255 unused lines nobody noticed (Day 53)
- **Phase-then-validate beats big-bang** — Each phase independently verifiable (Day 53)
- **Legacy fallback pattern** — Keep old code as fallback when replacing working systems (Day 52)
- **Periodic coherence audits** — 89% sounds good, but 11% included 3 CRITICAL bugs (Day 61)

### React/Frontend Gotchas
- **`{value && <div>}` with value=0 renders "0"** — Use `value != null && value > 0` (Day 68)
- **Never assume return object structure** — `analysisResult?.stock?.ticker` was wrong 67+ days (Day 68)
- **Integration test with real ticker before shipping** — UI-path bugs need real data (Day 68)

### Process
- **Exhaustive > spot-check** — 92.8% → 21% when properly tested (Day 50)
- **STOP and PROVE** — Features without validation = hypothesis, not edge (Day 23)
- **Auto-update everything** — Never ask user to update files or run git commands (Day 58)
- **Archive old versioned files** — Move files >15 days old to archive/ folders (Day 68)

---

*This file lives in `/docs/claude/stable/` — rarely changes*
