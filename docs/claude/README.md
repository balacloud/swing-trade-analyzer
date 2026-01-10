# 📚 Claude Session Documentation

> **Purpose:** Organized documentation for Claude AI sessions  
> **Last Updated:** Day 24 (January 6, 2026)

---

## 📁 Folder Structure

```
/docs/claude/
├── stable/                         ← Non-versioned docs (rarely change)
│   ├── SESSION_START.md            ← Claude's startup instructions
│   ├── SESSION_PROMPT_TEMPLATE.md  ← User's copy-paste prompts
│   └── GOLDEN_RULES.md             ← Rules & lessons learned
│
├── versioned/                      ← Day-versioned docs (change often)
│   ├── API_CONTRACTS_DAY[N].md     ← API reference
│   ├── KNOWN_ISSUES_DAY[N].md      ← Bug tracker
│   └── archive/                    ← Files older than 15 days
│
└── status/                         ← Daily status files
    ├── PROJECT_STATUS_DAY[N]_SHORT.md
    └── archive/                    ← Files older than 15 days
```

---

## 📋 File Purposes

### Stable Docs (No Versioning)
| File | Purpose |
|------|---------|
| **SESSION_START.md** | Instructions Claude reads at session start |
| **SESSION_PROMPT_TEMPLATE.md** | Copy-paste prompts for user |
| **GOLDEN_RULES.md** | Rules, architecture, and lessons |

### Versioned Docs (By Day)
| File | Purpose |
|------|---------|
| **API_CONTRACTS_DAY[N].md** | All API endpoints and data structures |
| **KNOWN_ISSUES_DAY[N].md** | Bug tracker with status |

### Status Docs (By Day)
| File | Purpose |
|------|---------|
| **PROJECT_STATUS_DAY[N]_SHORT.md** | Today's focus and recent progress |

---

## 🗄️ Archive Policy

- Keep **last 15 days** of versioned files in main folder
- Move older files to `archive/` subfolder
- Git history preserves everything regardless

---

## 🔄 Claude Project Sync

These files should also be uploaded to Claude Project for context:

**Always needed:**
- `stable/GOLDEN_RULES.md`
- `versioned/KNOWN_ISSUES_DAY[N].md` (latest)
- `versioned/API_CONTRACTS_DAY[N].md` (latest)
- `status/PROJECT_STATUS_DAY[N]_SHORT.md` (latest)

**Optional:**
- `stable/SESSION_START.md`
- `stable/SESSION_PROMPT_TEMPLATE.md`

---

## 🚀 Usage

### Starting a Session
1. Ensure latest versioned files are in Claude Project
2. Copy start prompt from `SESSION_PROMPT_TEMPLATE.md`
3. Paste into new Claude chat

### Ending a Session
1. Say "session ending"
2. Claude creates new versioned files
3. Download and add to Claude Project
4. Commit to git

---

*This README lives in /docs/claude/*
