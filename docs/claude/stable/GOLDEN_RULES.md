# GOLDEN RULES FOR CLAUDE

> **Purpose:** Core rules and cumulative lessons learned — stable reference
> **Location:** Git `/docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 72 (March 30, 2026)
> **Session protocols:** See `CLAUDE_CONTEXT.md` for startup/close checklists

---

## CORE RULES (16 Golden Rules)

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
