# GOLDEN RULES FOR CLAUDE

> **Purpose:** Core rules and cumulative lessons learned — stable reference
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 89 (July 16, 2026)
> **Session protocols:** See `CLAUDE_CONTEXT.md` for startup/close checklists

---

## CORE RULES (22 Golden Rules)

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
16. **EQUAL WEIGHT — Never optimize category weights.** DeMiguel et al. (2009): equal weights beat optimized out-of-sample. 238 trades is insufficient to optimize 4+ weights. If future evolution moves to continuous scoring, start with equal weights. (Day 69, Tier 1B)
17. **SESSION START = Read CLAUDE_CONTEXT.md first.** It defines the mandatory 4-file startup checklist (GOLDEN_RULES → ROADMAP → STATUS → KNOWN_ISSUES). Reading only GOLDEN_RULES.md and stopping there is incomplete — CLAUDE_CONTEXT.md is the orchestrating file. Use `/sta-start` skill to enforce this. (Day 76)
18. **REUSED OOS IS NOT OOS — freeze before forward test.** Every tuning pass that peeks at the same walk-forward window converts out-of-sample into in-sample. Days 55–75 reused the same 2020–2025 split across ~20 tuning sessions, so "OOS outperforms IS" no longer certifies robustness. Before paper/forward testing: pre-register the exact config (all thresholds + success/failure criteria), then never re-tune against the same historical window to "fix" a validation result. (Day 78, Fable review)
19. **SYSTEMATIC GRID-TEST PARITY, NOT HAND-PICKED VECTORS.** `categorical_engine.py`'s 5 hand-written parity vectors passed for years while a real bug sat undetected: the Python HOLD-fallback was missing a `risk_macro == 'Neutral'` branch that live JS had, silently defaulting to AVOID instead. A systematic 86,400-combo grid (`test_verdict_parity.py`) found it in one run — a 7.08% mismatch rate that 5 spot-checked vectors could never have surfaced by chance. When two independent implementations of the same logic must stay in sync (e.g., a Python backtest port vs the live JS it's meant to validate), build an exhaustive input grid over the decision boundaries, not a handful of "representative" examples. (Day 78, Fable Remediation Task 2.4)
20. **A PRE-COMMITTED RESTRICTION IS NOT A RE-TUNE.** Rule 18 forbids re-tuning thresholds to chase a better backtest number — but MR's original entry condition had NO liquidity gate at all (only `price > $5`, unlike momentum's $5M ADV gate). Adding a liquidity floor (price>$10, 20d ADV>$25M) decided *before* seeing the result, for a defensible, principled reason (execution realism — Connors' RSI(2) research was validated on liquid large-caps, not shell/SPAC names), is a legitimate one-time re-test — not data-snooping. It flipped MR from a clean null (PF 0.99) to a real-but-modest result (PF 1.16, still not significant at p=0.064). The distinguishing test: was the change decided *because of* the disappointing number (forbidden), or was it a *quality/execution constraint* that happened to also be untested (legitimate, once)? Either way: run it once, accept the answer, don't iterate further. (Day 79/80, Fable Remediation MR liquidity re-test)
21. **WHEN BUILDING A LIVE COUNTERPART TO AN EXISTING BACKTEST ENGINE, DRY THE SHARED LOGIC BEFORE WRITING THE SECOND IMPLEMENTATION — not after finding a parity bug.** Rule 19 found the JS/Python verdict-parity bug after it had shipped for years. Building the automated paper-trading engine (Day 81) was a chance to apply that lesson proactively: instead of writing a second exit-logic state machine for live positions, `trade_simulator.py`/`mr_simulator.py` gained a `live_mode` parameter so the live engine replays the *exact same* backtested function, and the Config C TradingView query was factored into `scan_queries.py` so the live Scan tab and the paper-trading engine can't drift apart. Verify the extraction is behavior-preserving (byte-for-byte identical output on real/synthetic trades) before relying on it — a refactor that "looks equivalent" is not the same as one that's been diffed against the original. (Day 81, automated paper trading engine)
22. **IN-MEMORY RATE-LIMITER/CIRCUIT-BREAKER STATE IS PER-PROCESS — SHARE IT OR IT'S NOT REALLY PROTECTING ANYTHING.** The Flask backend and the separate `daily_job.py` paper-trading process each ran their own Python interpreter with their own in-memory `circuit_breaker.py`/`rate_limiter.py` state — the two processes were silently *not* sharing rate-limit budgets or circuit-breaker trip state with each other, so a provider tripped/exhausted in one process looked perfectly healthy to the other. Any cross-process safety mechanism (rate limiting, circuit breaking, dedup, locking) needs storage that outlives a single process — here, a shared SQLite store (`backend/data/provider_state.db`). Multi-process deployments (a web server plus any cron/launchd job that imports the same modules) should be assumed by default, not discovered later. (Day 83, data-source review)
23. **A BACKGROUNDED DEV SERVER'S STDOUT DIES WITH ITS LAUNCHING TERMINAL — REDIRECT IT.** `start.sh` ran `python backend.py &` (and `npm start &`) with no output redirection, inheriting the launching terminal's stdout/stderr file descriptors. When that terminal window closed, the backend process survived (reparented to launchd/PID 1) but its stdout fd became invalid — every subsequent `print()` call (used throughout the codebase for request-scoped logging, including inside exception handlers) threw `OSError: [Errno 5] Input/output error` and turned into a 500, even for otherwise-healthy requests. The failure was silent on the frontend too: fetch handlers caught the error and set state to `null` with no error banner, so a card just disappeared with no signal it had ever been broken (same failure shape as Golden Rule 6's "never hallucinate/silently swallow" lesson, one layer down the stack). Fix: `nohup <cmd> >> logfile 2>&1 & disown` for any backgrounded long-running process — redirect output to a file and detach it from the controlling terminal so closing the window can't touch its file descriptors. Assume any `&`-backgrounded server will eventually outlive its terminal. (Day 84, backend/frontend reliability fix)
24. **A ONE-LINE ROADMAP DESCRIPTION IS NOT AN EFFORT ESTIMATE — CHECK THE ACTUAL SPEC BEFORE CALLING SOMETHING "SIMPLE."** Asked to batch-clear 3 backlog items assessed as "simple" from their roadmap one-liners, 2 of them weren't: N3 (gap-fill detection) turned out to have no design doc at all — just a placeholder pointer saying a future designer would scope it. Value Tab Phase 2's actual spec (`VALUE_TAB_SPEC.md` §9-10) explicitly required nightly batch-prefetch infrastructure and said outright "build only after feature freeze lift" — building it on-demand instead (the natural-looking approach, matching Phase 1's pattern) would have contradicted its own documented design and blown through AlphaVantage's ~8-tickets/day free-tier budget. Both were caught by reading the actual design doc before writing code, not after — the same discipline Golden Rule 11 asks for at the code level, applied one level up at the planning level. When a session's goal is "clear the backlog," open each item's linked spec/design doc first; a roadmap table's one-line description reflects what was true when it was written, not necessarily the item's real scope now. (Day 87, Breakout/N4/Price-Structure backlog session)
25. **WIDENING A CANDIDATE POOL AGAINST SHARED RATE-LIMITED PROVIDERS NEEDS A MEASURED LIMIT, NOT A GUESSED ONE — AND A DETERMINISTIC SORT TURNS RATE-LIMIT FAILURES INTO A SILENT, PERMANENT DATA GAP.** Widening the automated paper-trading engine's MR universe from a static 54-ticker list to a dynamic TradingView scan (Day 89, to accumulate samples faster) first tried limit=300. A live test tripped TwelveData's rate limiter partway through, opening its circuit breaker, which cascaded to yfinance and Tradier too — ~35% of that run's tickers failed on every provider, not because they lacked a signal. Because the query was sorted by `market_cap_basic` descending, that failure always hit the *same* tail-end tickers — a deterministic, silent gap that would have quietly under-sampled the same names every single day, not a random one that evens out over time. Fixed by measuring the real number that completed cleanly (150) and using that as the limit, rather than guessing a "big enough" number. When scaling any batch-fetch loop against a shared, rate-limited provider chain: (1) test at the target scale before shipping the default, (2) if the candidate order is deterministic, a rate-limit cutoff silently and permanently excludes the same tail every run — either keep the limit under the provider's measured sustainable throughput, or randomize/rotate the order so the excluded set changes day to day. (Day 89, MR universe expansion)

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
