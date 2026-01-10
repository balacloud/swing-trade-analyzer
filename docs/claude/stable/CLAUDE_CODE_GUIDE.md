# 🖥️ CLAUDE CODE ONBOARDING GUIDE

> **Project:** Swing Trade Analyzer  
> **Editor:** VS Code  
> **Created:** Day 24 (January 6, 2026)  
> **Purpose:** Streamline development with direct filesystem access

---

## 📦 INSTALLATION

### Step 1: Install Claude Code CLI

```bash
# Install globally via npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version
```

### Step 2: Authenticate

```bash
# Login with your Anthropic account
claude login

# This opens browser for authentication
# Use same account as Claude.ai
```

### Step 3: VS Code Extension (Optional but Recommended)

1. Open VS Code
2. Go to Extensions (Cmd+Shift+X)
3. Search for "Claude Code" or "Anthropic"
4. Install the official extension
5. Reload VS Code

**Alternative:** Use Claude Code directly in VS Code terminal (works great!)

---

## 🚀 GETTING STARTED

### Navigate to Project

```bash
cd /Users/balajik/projects/swing-trade-analyzer
```

### Start Claude Code

```bash
# Interactive mode (recommended)
claude

# Or with a specific question
claude "What files are in the frontend/src folder?"
```

### First Command - Verify Setup

```
You: List all files in the project and summarize the structure

Claude Code will:
- Read the filesystem
- Show you the project structure
- Confirm it understands the codebase
```

---

## 📁 PROJECT CONTEXT FILE

Create a `.claude` file in your project root to give Claude Code persistent context:

```bash
# Create context file
touch /Users/balajik/projects/swing-trade-analyzer/.claude
```

**Contents of `.claude`:**

```markdown
# Swing Trade Analyzer - Claude Code Context

## Project Overview
Institutional-grade swing trade recommendation engine using Mark Minervini's SEPA 
and William O'Neil's CAN SLIM methodologies.

## Tech Stack
- Backend: Python Flask (localhost:5001)
- Frontend: React + Tailwind CSS (localhost:3000)
- Data: yfinance, Defeat Beta, TradingView Screener

## Key Files
- backend/backend.py - Flask API server
- backend/support_resistance.py - S&R calculation + Option D
- frontend/src/App.jsx - Main React component (v2.6)
- frontend/src/utils/scoringEngine.js - 75-point scoring system

## Documentation
- docs/claude/stable/ - Non-versioned docs (GOLDEN_RULES, SESSION_START)
- docs/claude/versioned/ - Day-versioned docs (API_CONTRACTS_DAY[N], KNOWN_ISSUES_DAY[N])
- docs/claude/status/ - Daily status files

## Current Version
v1.4.0 - Day 24

## Active Bugs (Day 24)
1. Risk/Macro expand crash - object rendering in App.jsx
2. UX confusion - AVOID + VIABLE mixed signals
3. Sentiment placeholder - 13% of score is fake

## Golden Rules
1. STOP before coding - understand problem first
2. ASK for current file before modifying
3. RUN diagnostic queries before writing fixes
4. TEST incrementally - one change at a time
5. If something fails, STOP and diagnose

## Commands
- Backend: cd backend && source venv/bin/activate && python backend.py
- Frontend: cd frontend && npm start
- Test API: curl http://localhost:5001/api/health
```

---

## 🎯 COMMON WORKFLOWS

### 1. Starting a Development Session

```
You: Read docs/claude/status/PROJECT_STATUS_DAY24_SHORT.md and 
     docs/claude/versioned/KNOWN_ISSUES_DAY24.md, then tell me the 
     current priorities and active bugs.

Claude Code:
> Reading PROJECT_STATUS_DAY24_SHORT.md...
> Reading KNOWN_ISSUES_DAY24.md...
> 
> Current Status: v1.4.0
> 
> Active Bugs:
> - CRITICAL: System UNPROVEN
> - HIGH: Risk/Macro expand crash (Day 23)
> - HIGH: UX confusion - mixed signals
> - HIGH: Sentiment placeholder
> 
> Today's Priorities:
> 1. Fix Risk/Macro expand crash
> 2. Fix Sentiment or remove
> 3. Add "Bottom Line" messaging
```

### 2. Fixing a Bug

```
You: Fix the Risk/Macro expand crash in App.jsx. The error is 
     "Objects are not valid as a React child" when clicking 
     the Risk/Macro card.

Claude Code:
> Reading frontend/src/App.jsx...
> Found expandedScore === 'risk' section at line 615...
> Reading frontend/src/utils/scoringEngine.js to check risk breakdown structure...
> 
> Root cause: breakdown.risk.details contains nested objects like 
> {score: 2, max: 2, aboveSma200: true} being rendered directly.
> 
> Proposed fix:
> [shows diff with proper object handling]
> 
> Apply? (y/n)
```

### 3. Multi-File Changes

```
You: Add a new /api/sentiment/fear-greed endpoint to the backend 
     that fetches from the Fear & Greed Index API, then update 
     the API contracts documentation.

Claude Code:
> I'll need to:
> 1. Add endpoint to backend/backend.py
> 2. Update docs/claude/versioned/API_CONTRACTS_DAY24.md
> 
> Creating backend endpoint...
> [shows backend.py diff]
> 
> Updating API contracts...
> [shows API_CONTRACTS diff]
> 
> Apply both changes? (y/n)
```

### 4. Running Tests

```
You: Start the backend and test the S&R endpoint for AAPL

Claude Code:
> Starting backend...
> cd backend && source venv/bin/activate && python backend.py &
> 
> Testing endpoint...
> curl -s http://localhost:5001/api/sr/AAPL | jq '.meta.tradeViability'
> 
> Result:
> {
>   "viable": "YES",
>   "support_distance_pct": 4.4,
>   "advice": "Good setup - tight stop placement possible"
> }
```

### 5. Creating Documentation

```
You: Create PROJECT_STATUS_DAY25_SHORT.md based on what we 
     accomplished today. We fixed the Risk/Macro crash and 
     added Fear & Greed sentiment.

Claude Code:
> Reading PROJECT_STATUS_DAY24_SHORT.md for template...
> Creating docs/claude/status/PROJECT_STATUS_DAY25_SHORT.md...
> 
> [shows new file content]
> 
> Write this file? (y/n)
```

### 6. Git Operations

```
You: Stage all changes and commit with a proper message

Claude Code:
> Running: git status
> 
> Modified files:
> - backend/backend.py
> - frontend/src/App.jsx
> - docs/claude/versioned/API_CONTRACTS_DAY25.md
> - docs/claude/versioned/KNOWN_ISSUES_DAY25.md
> - docs/claude/status/PROJECT_STATUS_DAY25_SHORT.md
> 
> Suggested commit message:
> "Day 25: Fix Risk/Macro crash + Add Fear & Greed sentiment
> 
> Backend:
> - Added /api/sentiment/fear-greed endpoint
> - Integrated alternative.me Fear & Greed API
> 
> Frontend:
> - Fixed Risk/Macro expand crash (object rendering)
> - Updated sentiment display with real data
> 
> Docs:
> - Updated API_CONTRACTS_DAY25
> - Updated KNOWN_ISSUES_DAY25
> - Created PROJECT_STATUS_DAY25"
> 
> Run this commit? (y/n)
```

---

## 🔧 VS CODE INTEGRATION

### Option A: Integrated Terminal (Recommended)

1. Open VS Code in project: `code /Users/balajik/projects/swing-trade-analyzer`
2. Open terminal: `` Ctrl+` `` or `Cmd+J`
3. Run: `claude`
4. Claude Code runs alongside your editor

**Benefits:**
- See files Claude is editing in real-time
- Use VS Code's diff viewer
- Git integration visible in source control panel

### Option B: VS Code Extension

If you installed the Claude extension:

1. Open Command Palette: `Cmd+Shift+P`
2. Type "Claude" to see available commands
3. "Claude: Ask about selection" - highlight code and ask questions
4. "Claude: Edit file" - let Claude modify current file

### Option C: Split Terminal

```
┌─────────────────────────────────────┐
│  VS Code Editor (App.jsx)           │
├─────────────────┬───────────────────┤
│  Claude Code    │  npm start        │
│  (Terminal 1)   │  (Terminal 2)     │
└─────────────────┴───────────────────┘
```

1. Split terminal: Click split icon in terminal panel
2. Left terminal: `claude`
3. Right terminal: `cd frontend && npm start`

---

## 📋 QUICK REFERENCE COMMANDS

### Project-Specific Commands

```bash
# Start session
claude "Read the Day 24 status and known issues, summarize priorities"

# Fix specific bug
claude "Fix the Risk/Macro expand crash - the error is [paste error]"

# Add feature
claude "Add Fear & Greed Index endpoint to backend"

# Update docs
claude "Create KNOWN_ISSUES_DAY25.md - we fixed the Risk/Macro crash"

# Run tests
claude "Test the /api/sr/AAPL endpoint and show me tradeViability"

# Commit changes
claude "Stage and commit today's changes with a proper message"

# End session
claude "Create PROJECT_STATUS_DAY26_SHORT.md and list what we accomplished"
```

### General Commands

```bash
# Ask about code
claude "Explain how scoringEngine.js calculates the technical score"

# Find code
claude "Find where tradeViability is added to the API response"

# Refactor
claude "Refactor the sentiment calculation to use real data"

# Debug
claude "The frontend shows NaN for RS Rating - help me debug"
```

---

## 🔄 MIGRATING FROM CLAUDE.AI WORKFLOW

### What Changes

| Before (Claude.ai) | After (Claude Code) |
|--------------------|---------------------|
| Upload files to Claude Project | Claude reads from disk |
| Copy-paste code snippets | Claude reads full files |
| Download generated files | Claude writes directly |
| Manual git commands | Claude runs git |
| Separate docs update | Atomic with code changes |

### What Stays the Same

| Aspect | Notes |
|--------|-------|
| Golden Rules | Still apply - Claude Code follows them |
| Documentation structure | /docs/claude/ stays the same |
| Versioned files | Still create DAY[N] versions |
| Review before commit | Always verify Claude's changes |

### Hybrid Approach (Recommended Initially)

1. **Keep Claude Project** for reference docs (methodology, architecture)
2. **Use Claude Code** for active development
3. **Sync important learnings** back to Claude Project manually

---

## ⚠️ IMPORTANT NOTES

### Always Review Before Applying

```
Claude Code: Apply this fix? (y/n)

YOU: Let me review first...
[Read the diff carefully]
[Check it makes sense]
Then: y
```

### Backup Before Major Changes

```bash
# Before big refactors
git stash
# or
git checkout -b experimental-feature
```

### Claude Code Limitations

1. **Can't run GUI** - Won't see your browser, only terminal output
2. **Can't access internet** - Only local filesystem (no web search)
3. **Session memory** - Remembers within session, fresh start next time
4. **Token limits** - Very large files may need to be chunked

### When to Use Claude.ai Instead

- Web searches for current information
- Uploading screenshots for visual debugging
- Long-form planning discussions
- When you want conversation history saved

---

## 🚀 FIRST SESSION SCRIPT

Copy and run this for your first Claude Code session:

```bash
cd /Users/balajik/projects/swing-trade-analyzer

# Start Claude Code
claude

# Then paste this:
```

```
Read the following files and give me a status summary:
1. docs/claude/status/PROJECT_STATUS_DAY24_SHORT.md
2. docs/claude/versioned/KNOWN_ISSUES_DAY24.md
3. frontend/src/App.jsx (just the version comment at top)

Then confirm:
- Current version
- Active bugs count
- Top 3 priorities

After that, I want to fix the Risk/Macro expand crash.
```

---

## 📚 RESOURCES

- **Claude Code Docs:** https://docs.anthropic.com/claude-code
- **VS Code Extension:** Search "Anthropic" in VS Code marketplace
- **Your Project Docs:** /docs/claude/

---

*This guide lives in /docs/claude/stable/ - update as workflow evolves*
