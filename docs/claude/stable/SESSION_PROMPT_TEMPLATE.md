# 📋 SESSION PROMPT TEMPLATE

> **Purpose:** Copy-paste prompts to start and close Claude sessions  
> **Location:** Claude Project + Git `/docs/claude/stable/`  
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
1. SESSION_START.md - Follow the startup checklist (stable/)
2. GOLDEN_RULES.md - Session rules, debugging rules (stable/)
3. KNOWN_ISSUES_DAY[N].md - Current bugs and status (versioned/)
4. API_CONTRACTS_DAY[N].md - All API endpoints (versioned/)
5. PROJECT_STATUS_DAY[N]_SHORT.md - Today's focus (status/)

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

1. Create PROJECT_STATUS_DAY[N+1]_SHORT.md in status/
2. Create KNOWN_ISSUES_DAY[N+1].md in versioned/
3. Create API_CONTRACTS_DAY[N+1].md in versioned/ (if APIs changed)
4. Update GOLDEN_RULES.md in stable/ (if new rules learned)
5. Provide git commit command
6. List files I need to download and update in Claude Project
```

---

## 📁 NEW FOLDER STRUCTURE

```
/docs/claude/
├── stable/                         ← Non-versioned (rarely change)
│   ├── SESSION_START.md
│   ├── SESSION_PROMPT_TEMPLATE.md
│   └── GOLDEN_RULES.md
├── versioned/                      ← Day-versioned
│   ├── API_CONTRACTS_DAY[N].md
│   ├── KNOWN_ISSUES_DAY[N].md
│   └── archive/                    ← Older than 15 days
└── status/                         ← Daily status
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                    ← Older than 15 days
```

---

## 📝 BEFORE STARTING SESSION:

1. Make sure latest versioned docs are in Claude Project:
   - `KNOWN_ISSUES_DAY[N].md`
   - `API_CONTRACTS_DAY[N].md`
   - `PROJECT_STATUS_DAY[N]_SHORT.md`
2. Replace `[N]` with current day number (e.g., Day 24)

---

## ✅ EXPECTED CLAUDE RESPONSES:

### At Session Start:
- Current version (e.g., v1.4.0)
- Last session accomplishments
- Active bugs count (Critical: X, High: X, Medium: X)
- Today's priorities
- "What would you like to focus on today?"

### At Session Close:
- New versioned files created
- Git commit command
- List of files to download

---

## 📚 FILE REFERENCE

| File | Location | Versioned? |
|------|----------|------------|
| SESSION_START.md | stable/ | No |
| SESSION_PROMPT_TEMPLATE.md | stable/ | No |
| GOLDEN_RULES.md | stable/ | No |
| KNOWN_ISSUES_DAY[N].md | versioned/ | Yes |
| API_CONTRACTS_DAY[N].md | versioned/ | Yes |
| PROJECT_STATUS_DAY[N]_SHORT.md | status/ | Yes |

---

*This file lives in Claude Project + Git /docs/claude/stable/*
