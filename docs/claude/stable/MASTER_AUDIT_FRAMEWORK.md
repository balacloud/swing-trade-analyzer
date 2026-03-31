# Master Audit Framework

> **Purpose:** Single canonical audit framework for ALL audits in STA — internal, external, design, behavioral, coherence
> **Location:** `docs/claude/stable/` (rarely changes)
> **Last Updated:** Day 72 (March 30, 2026)
> **History:** Evolved from Day 50 (exhaustive testing lesson), Day 57 (first coherence audit), Day 61 (4-layer audit), Day 64 (deep coherence audit), Day 68 (external LLM audit framework), Day 71 (behavioral audit), Day 72 (this consolidation)

---

## Core Philosophy

Three truths we learned the hard way:

1. **README is marketing. Code is truth. But even true code can implement wrong logic.** (Day 68)
2. **Spot-check = 92.8% pass. Exhaustive = 21% pass. Always check EVERY item.** (Day 50)
3. **"It compiles and runs" is not the same as "it produces correct results."** (Day 71 — marketCap path was phantom for 2+ days)

---

## Audit Types

STA uses 5 distinct audit types. Each has a different trigger, scope, and method. **Use the right type for the situation.**

| Type | When to Use | Scope | Method | Time |
|------|------------|-------|--------|------|
| **Claim Audit** | Validating a specific assertion (threshold, formula, design decision) | Single claim or group of claims | Verdict labels per claim | 5-30 min |
| **Coherence Audit** | After code changes, before release | Module-level (code vs docs vs behavior) | Layer 1 + Layer 2 deep read | 1-2 hours |
| **Behavioral Audit** | After major feature implementation | Runtime behavior across multiple tickers | Live API calls + data flow tracing | 1-2 hours |
| **Design Audit** | Before building a new feature | Design spec vs existing architecture vs correctness | Layer 1 + Layer 2 against spec | 30-60 min |
| **External LLM Audit** | Validating domain-specific claims against research | Trading methodology, thresholds, academic claims | Multi-LLM consensus | Async (hours) |

---

## Part 1: Claim Audit Protocol

Use this for any specific assertion that needs verification — whether in a design spec, a code comment, a README claim, or a conversation.

### Auditor Mindset

```
You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.
```

### Rules (Non-Negotiable)

1. **Do NOT assume** a claim is true because it sounds plausible.
2. **Do NOT fabricate** citations, paper names, benchmark numbers, or doc URLs.
3. **If you cannot cite a real source** (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. **Express calibrated uncertainty.** "I believe" is not "This is verified."
5. **Reason step-by-step BEFORE** issuing a verdict label.

### Verdict Labels (Use Exactly One Per Claim)

| Label | Meaning | When to Use |
|-------|---------|-------------|
| **[VERIFIED — SOURCE: `<url/paper/doc>`]** | Specific, real, citable source exists | You can point to it right now |
| **[PLAUSIBLE — REASON: `<why>`]** | Consistent with known principles but not directly confirmed | Directionally correct, uncited. State what evidence would confirm. |
| **[MISLEADING — CORRECTION: `<what's actually true>`]** | Partially true but framed in a way that leads to wrong conclusions | The dangerous one — feels right, leads wrong |
| **[UNVERIFIED — NEEDS: `<what evidence is required>`]** | Cannot confirm without a specific test or paper | State exactly what benchmark, paper, or test would resolve it |
| **[HALLUCINATED — FLAG: `<why fabricated>`]** | Claim has no basis and likely was invented | Contains fabricated specifics (fake benchmarks, fake papers, invented APIs) |

### Decision Tree (Follow In Order)

```
1. Can you cite a specific, real source RIGHT NOW?
   → [VERIFIED]

2. Is the claim directionally consistent with established principles but uncited?
   → [PLAUSIBLE]

3. Is the claim partially true but misleadingly framed?
   → [MISLEADING]

4. Is the claim unconfirmable without a specific test or paper?
   → [UNVERIFIED]

5. Does the claim contain fabricated specifics?
   → [HALLUCINATED]
```

### Output Format Per Claim

```markdown
> **Claim:** [the original assertion]
> **Reasoning:** [step-by-step analysis — show your work]
> **Verdict:** [LABEL — details]
```

### How to Scope a Claim Audit

Extract claims from the target. A "claim" is any assertion that could be true or false:

- Thresholds: "RSI < 40 is oversold" → Is 40 the right number?
- Architecture: "Backend generation is more testable than frontend" → Is this actually true in our system?
- Data availability: "Touch counts are available in the API response" → Are they actually passed through?
- Methodology: "Agglomerative clustering outperforms KMeans for S/R" → What does research say?
- Performance: "Config C: 238 trades, PF 1.61" → Did we actually observe this?

---

## Part 2: Coherence Audit Protocol

Use this after code changes or before a release to verify that documentation, code, and runtime behavior all agree.

### Layer 1: Consistency (Docs Match Code)

```
For each module:
1. READ the documentation/README claim
2. READ the actual code
3. COMPARE: Do they say the same thing?

Red flags:
- Doc says "uses X method" but code uses Y
- Doc says "threshold is 20%" but code has 0.15
- Doc says "field X is returned" but response doesn't include it
- Doc says "no backend changes needed" but architecture requires one
```

### Layer 2: Correctness (Logic Is Sound)

```
For each computation/threshold:
1. EXTRACT the exact logic from code (not docs)
2. QUESTION: Is this threshold justified?
   (a) Against academic research
   (b) Against our backtest evidence
   (c) Against practitioner methodology (Minervini, O'Neil, Van Tharp)
3. TEST with real data — run actual tickers and verify outputs
4. TRACE: Does data flow correctly from producer to consumer?
```

### Layer 1+2 Combined Checklist

```markdown
| Finding # | Module | Layer | Claim | Code Reality | Verdict | Severity |
|-----------|--------|-------|-------|-------------|---------|----------|
| 1 | backend.py | L1 | level_scores in API | NOT passed through | MISLEADING | CRITICAL |
| 2 | price_structure | L2 | 5% = "near" level | Ignores volatility | UNVERIFIED | HIGH |
```

### Severity Definitions

| Severity | Definition | Action |
|----------|-----------|--------|
| **CRITICAL** | Incorrect data flows, wrong values reaching the user, phantom data paths | Fix before any other work |
| **HIGH** | Logic error that could lead to wrong trade decisions | Fix in current session |
| **MEDIUM** | Suboptimal but functional; could confuse but won't break | Fix when touching the module |
| **LOW** | Cosmetic, documentation drift, minor inconsistency | Fix opportunistically |
| **INFO** | Design decision documented as trade-off | No fix needed — just documented |

---

## Part 3: Behavioral Audit Protocol

Use this after implementing a major feature to verify runtime behavior matches design intent.

### Method

```
1. DEFINE test cases — one per behavior to verify
   - Each test = one specific assertion about runtime behavior
   - Cover happy path + edge cases + the specific thing that could go wrong

2. RUN tests against live system with real tickers
   - Use tickers that represent different states (uptrend, downtrend, sideways, ATH, low-vol)
   - Trace the data from API response → frontend logic → rendered output

3. RECORD results in a matrix:
   | # | Test | Expected | Actual | Pass/Fail | Notes |

4. On FAILURE:
   - Identify root cause (data contract? logic? rendering?)
   - Fix and re-run ONLY the failed tests
   - Document the defect for future reference

5. ITERATE until all tests pass
```

### The Day 71 Pattern (What Behavioral Audits Catch)

Behavioral audits catch **phantom paths** — code that looks correct but references data that doesn't exist at runtime:

- `stockData.marketCap` → always undefined (lives at `stockData.fundamentals.marketCap`)
- `meta.level_scores` → computed in engine but never passed through API response
- `value && <div>` → renders "0" when value is 0 (React falsy gotcha)

**Rule:** If a variable is used, trace it back to where it's populated. Don't trust that it exists.

### Minimum Behavioral Audit Ticker Set

| Ticker | State | Why |
|--------|-------|-----|
| **AAPL** or **MSFT** | Large-cap uptrend | Tests the "normal" path |
| **NVDA** | High-momentum, possibly ATH | Tests edge case: Fibonacci projections |
| **F** or **T** | Low-ADX sideways | Tests weak/no trend state |
| **SMCI** or **MARA** | Volatile/broken structure | Tests downtrend + weak template |
| **ETF (SPY or QQQ)** | No fundamentals | Tests null fundamental handling |

---

## Part 4: Design Audit Protocol

Use this before building a new feature — audit the spec against reality.

### Checklist

```
1. DATA AVAILABILITY — For every data field the spec references:
   □ Does it exist in the code?
   □ Is it computed?
   □ Is it passed through to where it's needed (API response, frontend state)?
   □ What's the actual field path? (e.g., `sr.meta.level_scores` vs `sr.level_scores`)

2. ARCHITECTURE — For every architectural decision:
   □ Does the chosen approach work with the existing data flow?
   □ Would it require coupling previously independent modules?
   □ Is there existing precedent in the codebase? Does the spec follow it?
   □ What's the simplest implementation that works?

3. LOGIC CORRECTNESS — For every threshold, rule, or decision tree:
   □ Is the evaluation order correct? (Edge cases before common cases?)
   □ Are thresholds justified by research, backtest, or practitioner methodology?
   □ Are there contradictions within the spec?
   □ Does the spec's own rules contradict its own examples?

4. LANGUAGE — For contextual/narrative features:
   □ Does the spec editorialize where it claims to be factual?
   □ Are technical terms used correctly (e.g., "oversold" = RSI < 30, not < 40)?
   □ Are claims about readability/scannability realistic?

5. SCOPE — For feature boundaries:
   □ Does this overlap with an existing card/module?
   □ Is the boundary between "what this card does" and "what other cards do" clear?
   □ Does it change any scoring/verdict logic? (If so, backtest validation required)
```

### Design Audit Output Format

```markdown
## Finding [N]: [Short title]

**Claim (Spec Section X):**
> [Quote the claim]

**Reality (Code):**
[What the code actually does]

**Verdict:** [LABEL — CORRECTION/REASON/etc.]

**Fix:** [What needs to change in the spec]
```

---

## Part 5: External LLM Audit Protocol

Use this for validating domain-specific claims against academic research and established methodology.

### When to Use External Audits

- Trading methodology claims (thresholds, indicators, scoring logic)
- Academic citations (paper references, statistical claims)
- Anything where domain expertise matters more than code inspection

### Recommended LLM Routing

| Target | Best For | Strength |
|--------|----------|----------|
| **Perplexity** | Research citations, paper verification | Returns real URLs and DOIs |
| **GPT Deep Research** | Synthesis across multiple domains | Good at connecting concepts |
| **Gemini** | Counter-arguments, alternative perspectives | Tends to be more lenient — useful as balance |
| **Grok** | Real-time market data verification | Access to X/Twitter sentiment |

### Multi-LLM Consensus Rules

| Consensus | Action |
|-----------|--------|
| **3/3 VERIFIED** | Claim is solid — document as verified |
| **3/3 PLAUSIBLE** | Acceptable — note lack of hard citation |
| **2/3+ MISLEADING** | Must fix — the claim actively misleads |
| **2/3+ HALLUCINATED** | Remove immediately — fabricated |
| **No consensus** | Investigate further — the disagreement itself is informative |
| **2/3+ UNVERIFIED** | Acceptable if acknowledged — add "unverified" note in docs |

### Workflow

```
1. EXTRACT exact claims from code (not README)
2. FORMAT as Claim Audit prompt (Part 1 format)
3. SEND to 2-3 external LLMs
4. COLLECT responses
5. BUILD consensus matrix
6. SYNTHESIZE into action plan:
   (a) Must-fix — logic errors affecting trade decisions
   (b) Should-improve — suboptimal but functional
   (c) Acknowledged — known trade-offs we consciously accept
7. Flag any CONFLICTING opinions between LLMs
```

**Prompt template for external LLMs:** See `docs/research/AUDIT_MODE_PROMPT_TEMPLATE.md` (copy-paste ready).
**Previous external audit results:** See `docs/research/AUDIT_SYNTHESIS_ACTION_PLAN.md` (Day 68-69, 45 questions, 3 LLMs).

---

## Part 6: Audit History & Precedent

These past audits established the patterns this framework codifies:

| Day | Audit Type | Key Finding | Lesson Codified |
|-----|-----------|-------------|-----------------|
| 50 | Behavioral | 92.8% spot-check → 21% exhaustive | "Check EVERY item, not a sample" |
| 57 | Coherence | First module-level audit | Established Layer 1 format |
| 61 | Coherence (4-layer) | 89% pass rate, but 11% included 3 CRITICAL bugs | "Percentage pass rate hides critical bugs" |
| 64 | Coherence (deep) | 28 findings, 5 bugs fixed (Cup & Handle index, stop loss hardcoded) | "Read the code, not the comments" |
| 68 | External LLM | MTF "3.2x" claim HALLUCINATED by 2/3 LLMs | "Our own claims can be fabricated" |
| 69 | External LLM + Synthesis | 4-LLM synthesis, 45 questions, led to Universal Principles evolution | Multi-LLM consensus protocol |
| 71 | Behavioral | `stockData.marketCap` phantom path — every large-cap treated as small-cap | "Trace data from source to consumer" |
| 72 | Design | Price Structure spec: 10 findings, architecture flipped from backend to frontend | "Audit specs before building" |

---

## Quick Reference: Which Audit When?

```
"I wrote a design spec"           → Design Audit (Part 4)
"I finished implementing a feature" → Behavioral Audit (Part 3)
"I changed code in a module"       → Coherence Audit (Part 2)
"Is this threshold correct?"       → Claim Audit (Part 1)
"Does research support this?"      → External LLM Audit (Part 5)
"The system feels wrong but IDK why" → Coherence Audit (Part 2, Layer 2)
```

---

## Anti-Patterns (What NOT to Do)

| Anti-Pattern | Why It Fails | Do This Instead |
|-------------|-------------|-----------------|
| "It passed the spot-check" | 92.8% vs 21% — Day 50 lesson | Exhaustive. Every item. |
| "The README says it works" | README is marketing | Read the code |
| "The code compiles and runs" | Runtime behavior ≠ correctness | Behavioral audit with real tickers |
| "I trust my own design spec" | Day 72: 10 findings in spec I just wrote | Audit specs before building |
| "One LLM says it's verified" | LLMs fabricate citations | 2-3 LLM consensus required |
| "We'll audit later" | Bugs compound. Day 71 phantom path lasted 2+ days | Audit at the boundary (before/after each phase) |
| "The fix is obvious, skip investigation" | Golden Rule: debug workflow → hypothesis → diagnostic → THEN fix | STOP and diagnose first |

---

*This framework lives in `docs/claude/stable/` — rarely changes.*
*For copy-paste external audit template: `docs/research/AUDIT_MODE_PROMPT_TEMPLATE.md`*
*For previous external audit results: `docs/research/AUDIT_SYNTHESIS_ACTION_PLAN.md`*
*For module-specific audit prompts: `docs/research/EXTERNAL_LLM_AUDIT_PROMPTS.md`*
