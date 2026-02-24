# GOLDEN RULES FOR CLAUDE

> **Purpose:** Stable reference document for all session rules
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 58 (February 22, 2026)

---

## SESSION RULES

### The 12 Golden Rules:
1. **START of session:** Read PROJECT_STATUS_DAY[N].md first
2. **BEFORE modifying any file:** READ it first using Read tool (Claude Code can access files directly)
3. **NEVER assume code structure** - always verify with actual file
4. **END of session:** Create updated PROJECT_STATUS_DAY[N+1].md
5. **User will say "session ending"** to trigger status file creation
6. **NEVER HALLUCINATE** - Don't claim stocks will score X without running them
7. **THINK THROUGH** - Pause and reason carefully before suggesting solutions
8. **ALWAYS VALIDATE** - Fact-check answers against external sources
9. **GENERATE FILES ONE AT A TIME** - Wait for user confirmation before next file
10. **FOLLOW CODE ARCHITECTURE RULES** - See section below
11. **DEBUG APIS PROPERLY** - Run diagnostic queries FIRST before writing fixes
12. **LOCAL FILES FIRST, THEN GIT** - Update files locally using Edit/Write tools FIRST, then commit to git (not the other way around)
13. **EXHAUSTIVE VERIFICATION** - When testing artifacts (PDFs, logs, reports), check EVERY item, not a sample. This is Claude's computational advantage over humans.
14. **UPDATE "LAST UPDATED" DATES** - When modifying any file in `docs/claude/stable/`, update the `Last Updated` header.
15. **NEVER IMPLEMENT WITHOUT VALIDATION** - Don't implement features based on assumptions. Always require either (a) peer-reviewed research, (b) backtested evidence, or (c) validated practitioner consensus. Day 51 example: RSI thresholds by holding period sounded logical but research showed it was WRONG.

---

## SESSION STARTUP CHECKLIST

When user starts a new session:
1. [x] Read CLAUDE_CONTEXT.md FIRST (master reference)
2. [x] Read PROJECT_STATUS file
3. [x] Verify context by summarizing current state to user
4. [x] Ask: "What would you like to focus on today?"
5. [ ] Do NOT ask user to re-explain the project
6. [ ] Do NOT ask for files unless you need to modify them
7. [ ] Do NOT jump to fixing - understand the problem first

---

## SESSION CLOSE CHECKLIST

When user says "session ending" or "close session":
1. [x] Create PROJECT_STATUS_DAY[N+1]_SHORT.md
2. [x] Ask: "Did any bugs get fixed or found?" -> Update KNOWN_ISSUES.md
3. [x] Ask: "Did any APIs change?" -> Update API_CONTRACTS.md
4. [x] Ask: "Did we learn a new rule?" -> Update GOLDEN_RULES.md
5. [x] **UPDATE CLAUDE_CONTEXT.md** - Current Day, Version, Last Updated, Focus
6. [x] Update auto memory (`~/.claude/projects/.../memory/MEMORY.md`) if significant learnings
7. [x] Git commit AND PUSH (don't forget push!)
8. [x] Note any deferred tasks for next session

### How Updates Work (Claude Code):
- Claude uses Edit/Write tools to update files directly in the filesystem
- No manual user action needed for local file updates
- Claude commits AND pushes to git — don't provide commands for user to run

---

## API SYNC VERIFICATION

### When to Verify API_CONTRACTS.md:
- After adding new endpoints
- After modifying existing endpoints
- Periodically (every 5 sessions) as a health check

### How to Verify (Claude runs this):
```bash
grep -n "@app.route" backend.py
```

### Verification Checklist:
1. Count routes in backend.py
2. Count routes documented in API_CONTRACTS.md
3. If mismatch -> update API_CONTRACTS.md
4. Check response structures are still accurate

### API Contract Rule:
> **Every `@app.route` in backend.py MUST have a corresponding entry in API_CONTRACTS.md**

---

## SESSION REMINDER (User Pastes This)

```
CLAUDE SESSION REMINDER:
1. STOP before coding - understand the problem first
2. ASK for current file before modifying anything
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose - don't guess again
6. At end, create PROJECT_STATUS with context preserved
```

---

## CODE ARCHITECTURE RULES

### Best Practices for Code Generation:
1. **Verify data contracts BEFORE writing code** - Check actual return structures before writing consuming code
2. **Document API contracts** - Each module's input/output should be documented in comments
3. **Producer defines API** - Data producer (e.g., scoringEngine) defines the structure; consumer (e.g., App.jsx) adapts to it
4. **Don't double-calculate** - If scoringEngine calculates RS, don't recalculate in App.jsx and overwrite
5. **Test incrementally** - Verify each change works before proceeding to next
6. **Clean separation of concerns** - UI should not need to know internal implementation details
7. **Flat API structures preferred** - `scores.technical` is better than `breakdown.technical.score`

### Why These Rules Exist:
- Day 18 bug was caused by UI assuming field names that didn't exist in scoringEngine
- App.jsx was overwriting scoringEngine's properly-mapped rsData with raw rsCalculator output
- Resulted in N/A values throughout the Analyze Stock tab
- Root cause: Lack of verified data contracts between modules

---

## DEBUGGING RULES (Added Day 20)

### When Fixing Bugs:
1. **ALWAYS run diagnostic queries FIRST** before writing fixes
2. **Never assume library behavior** - verify actual return values
3. **If fix fails, STOP** - diagnose root cause, don't chain guesses
4. **Test in isolation** - verify the fix works standalone before integrating

### Debugging Workflow:
```
1. Understand the symptom
2. Form hypothesis about cause
3. Write diagnostic query to TEST hypothesis
4. Run diagnostic, analyze results
5. Only THEN write the fix
6. Test fix incrementally
7. If fix fails, go back to step 2 (don't guess again)
```

### Why These Rules Exist:
- Day 20 had 3+ failed fix attempts because I guessed instead of diagnosing
- TradingView library behavior was assumed, not verified
- Wasted entire session on guess-fail-guess loop
- Diagnostic query at END of session revealed the actual data structure

---

## COMMON MISTAKES TO AVOID

### Don't Do This:
- [ ] Jump to writing code without understanding the problem
- [ ] Assume file structure without seeing actual file
- [ ] Chain multiple guesses when first fix fails
- [ ] Write long code blocks without user testing in between
- [ ] Create PROJECT_STATUS that loses cumulative context
- [ ] Overwrite producer's data with redundant consumer calculations

### Do This Instead:
- [x] Ask clarifying questions first
- [x] Request current file before modifying
- [x] Run diagnostic queries to understand actual behavior
- [x] Test each change before moving to next
- [x] Stop and diagnose when something fails
- [x] Keep PROJECT_STATUS focused but reference stable docs

---

## KEY LEARNINGS (Cumulative)

### Day 18: Data Contract Bugs
- Verify data contracts BEFORE writing UI code
- Don't double-calculate - producer defines API
- Check for overwrites in consuming code
- Clean API > nested structures

### Day 19: Testing & Architecture
- Test extensively before fixing - 30 stocks revealed patterns
- External review is valuable - Perplexity caught gaps
- Document before fixing - understand root cause first

### Day 20: Debugging Discipline
- **Debug before coding** - Run diagnostic queries first
- **Don't chain failed attempts** - Stop, think, verify
- **Library behavior != assumptions** - Always verify actual values
- **PROJECT_STATUS must be useful** - Not just an incident report

### Day 23: Feature vs Validation
- **Stop adding features, start proving the system works**
- Features without validation = hypothesis, not edge
- Holistic review before new development is valuable
- 13% fake score (sentiment) is dishonest - fix or remove
- Mixed UX signals confuse users - unify messaging

### Day 25: Backend Data Caching
- **Defeat Beta data can become stale** - Backend caches API responses
- **Restart backend periodically** - Or implement auto-refresh mechanism
- **Run comprehensive tests after restart** - Data quality improves dramatically
- **ETFs (SPY, QQQ) have no fundamentals** - Handle specially in frontend
- **Extreme ROE values need context** - Negative equity or high leverage explains outliers
- **30-stock test revealed:** 93% null fundamentals before restart -> 7% after restart

### Day 27: System Validation & Van Tharp Principles (CRITICAL)
- **Backtest before believing** - 75-point system achieved 49.7% win rate (essentially random)
- **Higher scores != better trades** - Scores 30-34 outperformed 35-39 (counter-intuitive)
- **Entry signals = ~10% of results** - We optimized the wrong thing for 27 days
- **Position sizing = ~90% of results** - Van Tharp's key insight
- **R-Multiples matter more than win rate** - Measure trades as multiples of initial risk
- **Expectancy formula:** (Win% x Avg Win R) + (Loss% x Avg Loss R)
- **Profit comes from R:R math** - 10% target / 7% stop = positive expectancy regardless of signal
- **Simplified systems work as well** - 4 binary criteria matched 75-point complexity
- **Academic research confirms:** Momentum works, but execution/sizing matters more

### Van Tharp Core Principles (Reference)
1. **Position sizing is the holy grail** - Not finding perfect entries
2. **R = Entry - Stop** - Define risk before entering
3. **Never risk more than 2% per trade** - Survival first
4. **Track R-multiples** - Not dollar amounts
5. **SQN (System Quality Number)** - (Mean R / StdDev R) x sqrt(N) for comparing systems

### Day 31: Session Close Reminder
- **Always PUSH after commit** - Don't just commit, verify changes reach remote
- **Commit + Push = Complete** - Session isn't closed until code is on GitHub

### Day 32: CLAUDE_CONTEXT.md is Master Reference
- **Check CLAUDE_CONTEXT.md at session START** - Contains current day, version, focus
- **Update CLAUDE_CONTEXT.md at session CLOSE** - Last Updated, Current Day, Focus fields
- **Don't skip this step** - Prevents stale context in next session

### Day 42: Local Files First, Then Git
- **Update files locally FIRST** - Use Edit/Write tools to modify filesystem
- **Then commit to git** - Git is for version control, not primary update
- **@ references read from filesystem** - Claude Code reads local files, not git
- **Don't ask user to manually update** - Claude can update local files directly

### Day 50: Exhaustive Verification is My Edge
- **Don't spot-check - verify EVERYTHING** - User provided 14 PDFs, I spot-checked a few and missed bugs
- **Pass rate dropped from 92.8% to 21%** when properly tested
- **This is my computational advantage** - I can process every item; humans would sample
- **When given test artifacts:** Read EVERY file, Check EVERY field, Document EVERY finding
- **Don't take human shortcuts** - My value is thoroughness, not speed

### Day 52: Surgical Integration Preserves Stability
- **Legacy fallback pattern:** When replacing a working system, keep old code as fallback
- **Pattern used in backend.py:** DataProvider tried first → if fails → legacy yfinance code runs
- **Never break existing code** while adding new infrastructure (user's explicit instruction)
- **Test each replacement individually** - Don't batch all 9 replacements, test one at a time
- **Timezone awareness matters:** yfinance returns timezone-aware, TwelveData returns naive - normalize at boundaries

### Day 53: SRP and Dead Code — The Architecture Tax
- **Dual endpoints for the same data = guaranteed corruption.** `/api/stock/` and `/api/fundamentals/` both returned fundamentals. When one returned zeros, scoring was silently corrupted.
- **Zero is not null.** Hardcoded `roe: 0` scored as "Weak" (not missing). `debtToEquity: 0` scored as "Strong" (0 < 1.0). Use null for missing data, never zero.
- **Validate each field end-to-end, both happy and failure paths.** Trace through ALL layers (backend → API → frontend merge → scoring → categorical → UI). Phase 1+2 reconciliation caught issues at layer 6 that compile/build checks never would.
- **Dead code accumulates silently.** Three functions (~255 lines) were completely unused. Nobody noticed because they compiled fine.
- **Phase-then-validate beats big-bang.** Phase 1 (stop corruption) → validate → Phase 2 (clean architecture) → validate. Each phase independently verifiable.
- **After building enough features: STOP and PROVE.** Day 27 showed 49.7% win rate. All improvements since are untested. The next priority is always the backtest, not the next feature.

### Day 58: Auto-Update Everything — Don't Ask, Just Do
- **Never ask the user to manually update files** — Claude updates all docs directly (Edit/Write tools)
- **Never provide git commands** — Claude commits AND pushes itself
- **Always update timestamps** on every doc touched (`Last Updated` field)
- **Don't create redundant files** — use existing structure (CLAUDE_CONTEXT.md, GOLDEN_RULES.md, SESSION_START.md). One file per purpose.
- **Session close = Claude does everything** — update docs, commit, push. User just says "close session."

### Day 54: Silent Fallbacks — The Invisible Lie
- **A hardcoded fallback value is worse than an error.** VIX=20 "normal" when API fails, Fear&Greed=50 "neutral" on error — the system makes decisions on phantom data and the trader never knows.
- **Return null, not a plausible fake.** Let downstream consumers (categorical assessment) handle missing data honestly with gray "unavailable" instead of silently scoring fake values.
- **Audit the WHOLE path, not just the feature code.** The categorical assessment was clean, but the data feeding it had double-fallback chains (backend returns 50, frontend also returns 50) that masked failures completely.
- **Legacy scoring systems accumulate "debt" even when replaced.** The 75-point scoring was superseded by categorical assessment, but its hardcoded sentiment=5/10 and breadth=1/1 still inflated displayed scores.

---

*This file lives in Claude Project - stable reference, rarely changes*
