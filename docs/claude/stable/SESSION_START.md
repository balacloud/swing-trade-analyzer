# 🚀 SESSION START - READ THIS FIRST

> **Purpose:** Entry point for every Claude session  
> **Location:** Claude Project + Git `/docs/claude/stable/`  
> **Action:** Claude reads this, then follows the checklist

---

## 📁 DOCUMENTATION STRUCTURE

```
/docs/claude/
├── stable/                         ← Non-versioned docs
│   ├── SESSION_START.md            ← This file
│   ├── SESSION_PROMPT_TEMPLATE.md  ← User's copy-paste prompts
│   └── GOLDEN_RULES.md             ← Rules & lessons
├── versioned/                      ← Day-versioned docs
│   ├── API_CONTRACTS_DAY[N].md     ← API reference (changes often)
│   ├── KNOWN_ISSUES_DAY[N].md      ← Bug tracker (changes often)
│   └── archive/                    ← Older than 15 days
└── status/                         ← Daily status
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                    ← Older than 15 days
```

---

## 📋 CLAUDE SESSION STARTUP CHECKLIST

### Step 1: Read Stable Docs (stable/)
- [ ] **GOLDEN_RULES.md** - Session rules, debugging rules, architecture rules

### Step 2: Read Versioned Docs (versioned/)
- [ ] **KNOWN_ISSUES_DAY[N].md** - Current bugs and their status
- [ ] **API_CONTRACTS_DAY[N].md** - All API endpoints and data structures

### Step 3: Read Daily Status (status/)
- [ ] **PROJECT_STATUS_DAY[N]_SHORT.md** - Today's focus and recent progress

### Step 4: Confirm Context
Say to user:
> "I've read the project docs. Current status: [version], working on [current task]. 
> What would you like to focus on today?"

### Step 5: Follow Golden Rules
- STOP before coding - understand problem first
- ASK for current file before modifying
- RUN diagnostic queries before writing fixes
- TEST incrementally

---

## 🔄 SESSION END CHECKLIST

When user says "session ending":
1. ✅ Create PROJECT_STATUS_DAY[N+1]_SHORT.md → status/
2. ✅ Create KNOWN_ISSUES_DAY[N+1].md → versioned/
3. ✅ Create API_CONTRACTS_DAY[N+1].md → versioned/ (if APIs changed)
4. ✅ Update GOLDEN_RULES.md → stable/ (if new rules learned)
5. ✅ Provide git commit command
6. ✅ List files to download for Claude Project

---

## 📚 FILE INVENTORY

| File | Location | Versioned? | Update Frequency |
|------|----------|------------|------------------|
| SESSION_START.md | stable/ | No | Never |
| SESSION_PROMPT_TEMPLATE.md | stable/ | No | Rarely |
| GOLDEN_RULES.md | stable/ | No | When lessons learned |
| KNOWN_ISSUES_DAY[N].md | versioned/ | Yes | Every session |
| API_CONTRACTS_DAY[N].md | versioned/ | Yes | When APIs change |
| PROJECT_STATUS_DAY[N]_SHORT.md | status/ | Yes | Every session |

---

## 🗄️ ARCHIVE POLICY

- **Keep last 15 days** of versioned files active
- **Move older files** to `archive/` subfolder
- Git preserves full history regardless

---

*This file lives in Claude Project + Git /docs/claude/stable/ - never changes*
