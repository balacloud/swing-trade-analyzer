# 📋 SESSION PROMPT TEMPLATE

> **Purpose:** Copy-paste prompts to start and close Claude sessions  
> **Location:** Claude Project  
> **Usage:** Replace `[N]` with current day number

---

## 🚀 SESSION START - COPY THIS:

```
Resume Swing Trade Analyzer - Day [N]

CLAUDE SESSION REMINDER:
1. STOP before coding - understand the problem first
2. ASK for current file before modifying anything
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose - don't guess again

---

Please read all project files before responding:
1. SESSION_START.md - Follow the startup checklist
2. GOLDEN_RULES.md - Session rules, debugging rules, architecture rules
3. KNOWN_ISSUES.md - Current bugs and status
4. API_CONTRACTS.md - All API endpoints and data structures
5. PROJECT_STATUS_DAY[N]_SHORT.md - Today's focus

After reading, confirm:
- Current version
- What was accomplished last session
- Active bugs (count by priority)
- Today's priorities

Then ask: "What would you like to focus on today?"
```

---

## 🔚 SESSION CLOSE - COPY THIS:

```
Session ending - please follow close checklist:

1. Create PROJECT_STATUS_DAY[N+1]_SHORT.md
2. Ask me: "Did any bugs get fixed or found?" → Update KNOWN_ISSUES.md
3. Ask me: "Did any APIs change?" → Update API_CONTRACTS.md
4. Ask me: "Did we learn a new rule?" → Update GOLDEN_RULES.md
5. Provide git commit command
6. List files I need to download and update in Claude Project
```

---

## 📝 BEFORE STARTING SESSION:

1. Make sure `PROJECT_STATUS_DAY[N]_SHORT.md` is in Claude Project
2. Replace `[N]` with current day number (e.g., Day 23)
3. If stable docs changed last session, update them first:
   - KNOWN_ISSUES.md
   - API_CONTRACTS.md
   - GOLDEN_RULES.md

---

## ✅ EXPECTED CLAUDE RESPONSES:

### At Session Start:
- Current version (e.g., v1.4.0)
- Last session accomplishments
- Active bugs count (Critical: X, High: X, Medium: X)
- Today's priorities
- "What would you like to focus on today?"

### At Session Close:
- PROJECT_STATUS_DAY[N+1]_SHORT.md file created
- Questions about bugs/APIs/rules
- Git commit command
- List of files to download

---

## 📚 FILE REFERENCE

| File | Location | Purpose |
|------|----------|---------|
| SESSION_START.md | Claude Project | Claude's instructions (start + close checklists) |
| SESSION_PROMPT_TEMPLATE.md | Claude Project | Your copy-paste prompts (this file) |
| GOLDEN_RULES.md | Claude Project | Rules & architecture |
| KNOWN_ISSUES.md | Claude Project | Bug tracker |
| API_CONTRACTS.md | Claude Project | API reference |
| PROJECT_STATUS_DAY[N]_SHORT.md | Claude Project | Daily focus |

---

*This file lives in Claude Project - update if workflow changes*
