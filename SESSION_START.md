# 🚀 SESSION START - READ THIS FIRST

> **Purpose:** Entry point for every Claude session  
> **Action:** Claude reads this, then follows the checklist

---

## 📋 CLAUDE SESSION STARTUP CHECKLIST

### Step 1: Read Stable Reference Docs (in Claude Project)
- [ ] **GOLDEN_RULES.md** - Session rules, debugging rules, architecture rules
- [ ] **KNOWN_ISSUES.md** - Current bugs and their status
- [ ] **API_CONTRACTS.md** - All API endpoints and data structures

### Step 2: Read Daily Status (User Attaches)
- [ ] **PROJECT_STATUS_DAY[N]_SHORT.md** - Today's focus and recent progress

### Step 3: Confirm Context
Say to user:
> "I've read the project docs. Current status: [version], working on [current task]. 
> What would you like to focus on today?"

### Step 4: Follow Golden Rules
- STOP before coding - understand problem first
- ASK for current file before modifying
- RUN diagnostic queries before writing fixes
- TEST incrementally

---

## 🔄 SESSION END CHECKLIST

When user says "session ending":
1. ✅ Create PROJECT_STATUS_DAY[N+1]_SHORT.md
2. ✅ Ask: "Did any bugs get fixed or found?" → Update KNOWN_ISSUES.md
3. ✅ Ask: "Did any APIs change?" → Update API_CONTRACTS.md  
4. ✅ Ask: "Did we learn a new rule?" → Update GOLDEN_RULES.md
5. ✅ Provide git commit command

---

## 📚 FILE INVENTORY

| File | Location | Purpose | Update Frequency |
|------|----------|---------|------------------|
| SESSION_START.md | Claude Project | Entry point | Never |
| GOLDEN_RULES.md | Claude Project | Rules & lessons | When new lessons learned |
| KNOWN_ISSUES.md | Claude Project | Bug tracker | When bugs change status |
| API_CONTRACTS.md | Claude Project | API reference | When APIs change |
| PROJECT_STATUS_DAY[N]_SHORT.md | User attaches | Daily focus | Every session |

---

*This file lives in Claude Project - never changes*
