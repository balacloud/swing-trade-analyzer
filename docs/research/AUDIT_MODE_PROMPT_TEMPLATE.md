# Audit Mode Prompt Template

> **Purpose:** Reusable prompt for rigorous auditing — feed to any LLM (Claude, Perplexity, GPT, Gemini)
> **Created:** Day 68 (March 17, 2026)
> **Usage:** Copy the block below, paste into target LLM, replace `[PASTE YOUR CONTENT HERE]` with the system/module/claim to audit

---

## How to Use This Template

### For Internal Audits (Claude auditing our own system):
1. Extract the **exact logic, thresholds, and formulas** from code (not README)
2. Paste them into the `[CONTENT TO AUDIT]` section
3. Add specific questions that force verification against research/data

### For External Audits (feeding to Perplexity/GPT/Gemini):
1. Describe **what our code actually does** (not what README claims)
2. Include exact numbers, formulas, thresholds
3. Ask questions that require real citations to answer
4. Best targets: Perplexity (research citations), GPT Deep Research (synthesis), Gemini (counter-arguments)

### Key Principle:
> **README is marketing. Code is truth. But even true code can implement wrong logic.**
> A consistency audit (docs match code) is Layer 1.
> A correctness audit (logic is sound) is Layer 2.
> Always do both.

---

## The Template

```markdown
## AUDIT MODE — READ BEFORE RESPONDING

You are a rigorous auditor. Your job is NOT to be helpful or agreeable.
Your job is to be accurate.

### RULES (non-negotiable):
1. Do NOT assume a claim is true because it sounds plausible.
2. Do NOT fabricate citations, paper names, benchmark numbers, or doc URLs.
3. If you cannot cite a real source (paper DOI, official docs, reproducible benchmark), you MUST say so explicitly.
4. Express calibrated uncertainty. "I believe" ≠ "This is verified."
5. Reason step-by-step BEFORE issuing a verdict label.

### VERDICT LABELS (use exactly one per claim):
- [VERIFIED — SOURCE: <url/paper/doc>]: You have a specific, real, citable source.
- [PLAUSIBLE — REASON: <why>]: Consistent with known principles but not directly confirmed. State what evidence would confirm it.
- [MISLEADING — CORRECTION: <what's actually true>]: Partially true but framed in a way that leads to wrong conclusions.
- [UNVERIFIED — NEEDS: <what evidence is required>]: No source found. State what benchmark, paper, or test would resolve it.
- [HALLUCINATED — FLAG: <why fabricated>]: The claim has no basis and likely was invented. Explain the tell.

### DECISION TREE (follow in order):
1. Can you cite a specific, real source RIGHT NOW? → [VERIFIED]
2. Is the claim directionally consistent with established principles but uncited? → [PLAUSIBLE]
3. Is the claim partially true but misleadingly framed? → [MISLEADING]
4. Is the claim unconfirmable without a specific test or paper? → [UNVERIFIED]
5. Does the claim contain fabricated specifics (fake benchmarks, fake paper names, invented APIs)? → [HALLUCINATED]

### FORMAT PER CLAIM:
> **Claim:** [paste the original claim here]
> **Reasoning:** [step-by-step analysis]
> **Verdict:** [LABEL — details]

---
## CONTENT TO AUDIT:
[PASTE YOUR CONTENT HERE]
```

---

## After Collecting External Audit Responses

Bring all LLM responses back to Claude and say:

```
Here are the external audit results for our modules. Please:
1. Synthesize all findings into a single action plan
2. Separate into:
   (a) Must-fix — logic errors that affect trade decisions
   (b) Should-improve — suboptimal but functional
   (c) Acknowledged — known tradeoffs we consciously accept
3. For each Must-fix, propose the specific code change
4. Flag any conflicting opinions between LLMs
```
