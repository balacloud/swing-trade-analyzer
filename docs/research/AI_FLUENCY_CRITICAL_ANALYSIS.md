# Critical Analysis: Anthropic AI Fluency Index vs Our Project

> **Purpose:** Apply Anthropic's AI Fluency research findings to critically evaluate how Claude and the user have collaborated on this 59-day project
> **Source:** Anthropic Education Report: The AI Fluency Index (Feb 23, 2026)
> **Created:** Day 59 (February 25, 2026)

---

## The Research Summary

Anthropic studied 9,830 Claude conversations and found:

1. **Iteration & Refinement is king** — 85.7% of conversations that iterated showed 2.67x more fluency behaviors
2. **Artifact creation makes users less evaluative** — When Claude produces code/apps, users are:
   - -3.1pp less likely to question reasoning
   - -5.2pp less likely to identify missing context
   - -3.7pp less likely to check facts
3. **Users become more directive but less discerning** with artifacts — they specify goals (+14.7pp) and formats (+14.5pp) but stop questioning the output
4. **Only 30% of users set collaboration terms** — telling Claude "push back if I'm wrong" or "explain your reasoning"

---

## How Our Project Maps to These Findings

### STRONG: Iteration & Refinement (We do this well)

This project is the definition of iteration. 59 days, hundreds of sessions, continuous refinement. Evidence:

- **Day 27 backtest** revealed 49.7% win rate — we didn't ignore it, we rebuilt the entire assessment system
- **Day 50 exhaustive re-test** caught 21% true pass rate (not 92.8%) — iterated to fix
- **Day 53 SRP cleanup** — removed dual endpoints, dead code, zero-as-null bugs
- **Day 54 silent fallback audit** — found and fixed hardcoded VIX=20, F&G=50
- **75-point scoring → Categorical Assessment** — complete system replacement based on evidence

**Verdict: PASS.** We iterate aggressively. The research says this correlates with all other fluency behaviors.

### CONCERNING: The Artifact Blindness Problem

The research warns that when AI produces polished outputs, users stop questioning. This is DIRECTLY relevant to us:

**Evidence of artifact blindness in our project:**

1. **Day 18 — Data Contract Bug**: Claude wrote UI code assuming field names that didn't exist in scoringEngine. Nobody caught it until N/A values appeared everywhere. The code *compiled and looked correct*.

2. **Day 20 — Debugging Guess Loop**: Claude chained 3+ failed fixes without running diagnostics first. The code *looked like reasonable fixes* each time.

3. **Day 50 — 92.8% → 21% Pass Rate**: Claude spot-checked a few PDFs and declared 92.8% pass. Exhaustive review revealed 21%. The initial check *produced a polished-looking report*.

4. **Day 53 — Dead Code (255 lines)**: Three entire functions were unused for months. They compiled fine, so nobody noticed. They *looked like working code*.

5. **Day 54 — Silent Fallbacks**: VIX=20 hardcoded when API fails, F&G=50 "neutral" on error. The system *appeared to work normally* — green lights everywhere, phantom data underneath.

6. **DVN Bug (Day 58-59)**: Bottom Line said "MOMENTUM ENTRY" while Trade Setup said "PULLBACK PREFERRED". Both cards *looked professionally rendered*. The contradiction existed for an unknown duration because each card individually *looked correct*.

**Pattern**: Every major bug in this project's history was caught NOT because the output looked wrong, but because someone questioned whether the underlying data/logic was correct despite the output looking fine.

### MIXED: Setting Collaboration Terms

The research says only 30% of users explicitly tell Claude how to interact. Our user:

**What the user does well:**
- Created GOLDEN_RULES.md with explicit behavioral rules for Claude
- "NEVER HALLUCINATE" — Rule #6
- "DEBUG APIS PROPERLY — Run diagnostic queries FIRST" — Rule #11
- "EXHAUSTIVE VERIFICATION" — Rule #13 (added after Day 50 failure)
- "NEVER IMPLEMENT WITHOUT VALIDATION" — Rule #15 (added after Day 51 failure)
- Session start/close protocol flowcharts (Day 59)

**Where gaps remain:**
- Rules exist but Claude still violates them (the very behavior the user called out today — stopping at errors instead of pushing through)
- The user has to nudge Claude repeatedly on the same issues (manual file updates, forgetting to push, stopping at obstacles)
- Rules accumulate but enforcement is inconsistent — adding more rules doesn't fix execution discipline

---

## Critical Questions About What We've Built

### Question 1: Are we over-engineering features without proving they work?

**Day 27 showed 49.7% win rate** (random). Since then we've added:
- Categorical Assessment (replacing 75-point scoring)
- Pattern Detection (VCP, Cup & Handle, Flat Base)
- Support & Resistance with trade viability
- 3 holding periods with signal weighting
- Sector Rotation with RRG quadrants
- Multi-source data providers (5 sources)
- Fear & Greed Index
- Earnings Calendar
- Canadian Market Support
- Data Freshness Meter

**Day 55 backtest validated**: Config C showed 53.78% WR, PF 1.61, walk-forward passed. So the core system IS validated. But the features added AFTER Day 55 (Sector Rotation, Canadian Market, Freshness Meter) are NOT backtested additions — they're UI/UX improvements that don't affect the trading signal itself.

**Verdict: ACCEPTABLE.** Core trading logic is validated. Recent additions are tooling/UX, not signal changes. No action needed — but we should be cautious about adding features that modify the categorical assessment verdict without re-running the backtest.

### Question 2: Are we questioning Claude's reasoning enough?

The research warns users become less evaluative with artifacts. Evidence from THIS SESSION:
- Claude stopped 3 times at obstacles without continuing
- Claude needed to be nudged to keep working
- This is the "polished artifact" problem in reverse — Claude generates code that *appears to be progress* but actually stalls

**Action needed:** The user is already doing this well by pushing back. No system change needed, but it reinforces that **human oversight of AI-generated code is non-negotiable**, especially for a financial tool.

### Question 3: Is the Categorical Assessment logic actually sound?

The assessment was ported from research, but let's question the thresholds:

| Assessment | Threshold | Source | Validated? |
|-----------|-----------|--------|-----------|
| Strong Technical | TT >= 7/8, RSI 50-70, RS >= 1.0 | Minervini + Perplexity research | Yes (backtest) |
| Strong Fundamental | ROE > 15%, RevGrowth > 10%, D/E < 1.0 | Standard fundamental analysis | Partially (SimFin backtest used these) |
| Favorable Risk | VIX < 20, SPY > 200 SMA | Standard regime filter | Yes (bear regime validated Day 57) |
| ADX >= 20 for trend | Wilder's original ADX interpretation | Yes (Config C requirement) |
| ADX >= 25 for momentum entry | Custom threshold | No — arbitrary, not backtested |

**Finding: The ADX 25 threshold for entry preference is arbitrary.** The backtest validated ADX >= 20 as a trend filter, but the distinction between "momentum viable" (ADX >= 25) and "pullback preferred" (ADX 20-25) was never independently tested. It *sounds reasonable* but that's exactly the kind of assumption Rule #15 warns about.

**Action:** Log as known assumption. Not urgent since entry preference is advisory (doesn't change the BUY/HOLD/AVOID verdict), but should be validated if we ever refine the entry logic.

### Question 4: Are we building for the user or for feature completeness?

Recent additions inventory:
- **Sector Rotation** — User requested (valuable)
- **Canadian Market** — User requested (valuable)
- **Data Freshness Meter** — Solves a real concern (cache staleness)
- **Session Protocol Flowcharts** — Fixes real problem (Claude missing steps)

All four recent additions were user-requested and solve real problems. This is NOT feature bloat — it's demand-driven development.

**Verdict: PASS.** No wasteful features identified.

### Question 5: What are we NOT questioning that we should be?

1. **yfinance data quality for .TO tickers** — SHOP.TO returned price but null SMA/RSI on first fetch. Is this a transient issue or does yfinance have reliability problems with TSX tickers? Needs monitoring.

2. **Frontend bundle size** — 10 parallel API calls in `fetchFullAnalysisData()`. Each new feature adds a call. At what point does this impact UX? Not critical yet, but worth monitoring.

3. **Sector Rotation accuracy** — We calculate RS ratio vs SPY using SPDR ETFs. But the quadrant classification (Leading/Weakening/Lagging/Improving) uses momentum of the RS ratio. This was implemented based on RRG theory but never validated against actual RRG data. Could be wrong.

4. **Single-user assumption** — The entire system is designed for one user. No auth, no rate limiting, no multi-tenant concerns. This is fine for now but limits deployment.

---

## Recommendations from the Research

### 1. "Stay in the conversation" — We already do this
59 days of iteration. Our strongest fluency behavior.

### 2. "Question polished outputs" — Our biggest risk area
**Concrete action:** After ANY feature is code-complete and "looks working", run at minimum:
- 3 tickers through the full pipeline (not just 1)
- Check EVERY field in the response (not spot-check)
- Compare the output against what we expect (not just "it didn't crash")

This is already Rule #13 (Exhaustive Verification) but needs to be applied more consistently.

### 3. "Set the terms of collaboration" — We do this, but enforcement lags
The GOLDEN_RULES exist. The SESSION_PROTOCOL exists. The problem is execution, not documentation. The user has to keep nudging Claude on the same issues.

**Meta-observation:** This is EXACTLY what the research predicts — adding more rules/documentation is a "description and delegation" behavior (+14.7pp). But what's actually needed is more "discernment" — Claude self-monitoring its own behavior against the rules.

---

## Bottom Line

| Dimension | Our Score | Evidence |
|-----------|----------|---------|
| Iteration & Refinement | Strong | 59 days, major pivots (scoring redesign, backtest) |
| Critical Evaluation | Mixed | Good at macro level (backtest validation), weak at micro level (stopping at errors, spot-checking) |
| Setting Terms | Strong on paper | GOLDEN_RULES, SESSION_PROTOCOL — but enforcement inconsistent |
| Artifact Blindness Risk | Medium | Historical bugs all followed the "looked correct" pattern; mitigated by Rule #13 but not eliminated |
| Feature Discipline | Good | All recent additions are user-requested and solve real problems |

**No code changes needed.** The research validates our existing approach (iteration, explicit rules, backtest-before-believing) while highlighting that our biggest risk is *trusting polished-looking outputs* — which is exactly the pattern behind every major bug in our history.

The single most important takeaway: **When something looks finished, that's the moment to question it hardest.**

---

*This analysis is itself subject to the same critique — it looks like a thorough document, but does it actually change anything? The honest answer: it reinforces existing practices (Rule #13, #15) rather than revealing new ones. The one actionable finding is the ADX 25 threshold for entry preference being unvalidated — but that's advisory, not verdict-affecting. Sometimes "no changes needed" is the correct finding.*
