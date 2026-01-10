# ðŸ† GOLDEN RULES FOR CLAUDE

> **Purpose:** Stable reference document for all session rules  
> **Location:** Claude Project (not daily file)  
> **Last Updated:** Day 21 (January 3, 2026)

---

## ðŸ“‹ SESSION RULES

### The 11 Golden Rules:
1. **START of session:** Read PROJECT_STATUS_DAY[N].md first
2. **BEFORE modifying any file:** Ask user to attach/paste the CURRENT version
3. **NEVER assume code structure** - always verify with actual file
4. **END of session:** Create updated PROJECT_STATUS_DAY[N+1].md
5. **User will say "session ending"** to trigger status file creation
6. **NEVER HALLUCINATE** - Don't claim stocks will score X without running them
7. **THINK THROUGH** - Pause and reason carefully before suggesting solutions
8. **ALWAYS VALIDATE** - Fact-check answers against external sources
9. **GENERATE FILES ONE AT A TIME** - Wait for user confirmation before next file
10. **FOLLOW CODE ARCHITECTURE RULES** - See section below
11. **DEBUG APIS PROPERLY** - Run diagnostic queries FIRST before writing fixes

---

## ðŸ”„ SESSION STARTUP CHECKLIST

When user starts a new session:
1. âœ… Read PROJECT_STATUS file (user will attach it)
2. âœ… Verify context by summarizing current state to user
3. âœ… Ask: "What would you like to focus on today?"
4. âŒ Do NOT ask user to re-explain the project
5. âŒ Do NOT ask for files unless you need to modify them
6. âŒ Do NOT jump to fixing - understand the problem first

---

## ðŸ“‹ SESSION CLOSE CHECKLIST

When user says "session ending" or "close session":
1. âœ… Create PROJECT_STATUS_DAY[N+1]_SHORT.md
2. âœ… Ask: "Did any bugs get fixed or found?" â†’ Update KNOWN_ISSUES.md
3. âœ… Ask: "Did any APIs change?" â†’ Update API_CONTRACTS.md
4. âœ… Ask: "Did we learn a new rule?" â†’ Update GOLDEN_RULES.md
5. âœ… Update Claude Memory if significant changes
6. âœ… Provide git commit command
7. âœ… Note any deferred tasks for next session

### How Stable Doc Updates Work:
- Claude creates updated file in `/mnt/user-data/outputs/`
- User downloads and replaces file in Claude Project
- User confirms update is done

---

## ðŸ”„ API SYNC VERIFICATION

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
3. If mismatch â†’ update API_CONTRACTS.md
4. Check response structures are still accurate

### API Contract Rule:
> **Every `@app.route` in backend.py MUST have a corresponding entry in API_CONTRACTS.md**

---

## âš ï¸ SESSION REMINDER (User Pastes This)

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

## ðŸ—ï¸ CODE ARCHITECTURE RULES

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

## ðŸ”§ DEBUGGING RULES (Added Day 20)

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

## ðŸš« COMMON MISTAKES TO AVOID

### Don't Do This:
- âŒ Jump to writing code without understanding the problem
- âŒ Assume file structure without seeing actual file
- âŒ Chain multiple guesses when first fix fails
- âŒ Write long code blocks without user testing in between
- âŒ Create PROJECT_STATUS that loses cumulative context
- âŒ Overwrite producer's data with redundant consumer calculations

### Do This Instead:
- âœ… Ask clarifying questions first
- âœ… Request current file before modifying
- âœ… Run diagnostic queries to understand actual behavior
- âœ… Test each change before moving to next
- âœ… Stop and diagnose when something fails
- âœ… Keep PROJECT_STATUS focused but reference stable docs

---

## ðŸ’¡ KEY LEARNINGS (Cumulative)

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
- **Library behavior â‰  assumptions** - Always verify actual values
- **PROJECT_STATUS must be useful** - Not just an incident report

---

*This file lives in Claude Project - stable reference, rarely changes*

### Day 23: Feature vs Validation
- **Stop adding features, start proving the system works**
- Features without validation = hypothesis, not edge
- Holistic review before new development is valuable
- 13% fake score (sentiment) is dishonest - fix or remove
- Mixed UX signals confuse users - unify messaging
