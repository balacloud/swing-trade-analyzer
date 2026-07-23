# Developer Onboarding Guide — Swing Trade Analyzer

Welcome. This guide gets your local environment running end-to-end and orients you in how this codebase is built and documented. It assumes zero prior context.

For the full feature list, architecture, and API reference, see [README.md](README.md) — this guide is about *getting set up and understanding how to work in this repo*, not duplicating that content.

---

## ⚠️ Before You Start — Please Read

**This is a research/educational tool, not investment advice.** A few things worth knowing before you rely on anything it tells you:

- The verdict/scoring system (BUY/HOLD/AVOID) is backtested but **not yet statistically confirmed at a significance level anyone should trust with real capital**. See README's [Backtest Validation](README.md#assessment-methodology) section for the actual numbers (p=0.094 and p=0.064 — both "directionally positive, not proven").
- There's a live, unattended **paper-trading engine** (`backend/paper_trading/`) currently accumulating real forward-test trades specifically *because* the backtest alone isn't sufficient proof. It requires 100 confirmed trades per system before anyone here would consider it validated.
- **Do your own independent testing and validation before trusting any output** — that's not a formality, it's how this project itself operates (see [Development Practices](#development-practices) below). The codebase has its own internal audit framework (`docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`) built for exactly that purpose, and you're welcome to point it at your own fork.
- Past performance in any backtest or paper-trading run doesn't guarantee future results. Use at your own risk, and never trade on this tool's output without your own due diligence.

---

## Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher + npm
- Git
- Chrome browser (only needed for the Data Validation feature, which uses Selenium)

---

## 1. Clone and Set Up

```bash
git clone <your-fork-or-this-repo-url>
cd swing-trade-analyzer
```

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### Frontend

```bash
cd ../frontend
npm install
```

---

## 2. Environment Variables

The backend needs API keys to fetch market data. **Never commit `.env` — it's already gitignored.**

```bash
cd backend
cp .env.example .env
```

Then open `backend/.env` and fill in the keys below.

### Required — the app won't function meaningfully without these

| Variable | Where to Get It | Free Tier |
|----------|----------------|-----------|
| `TWELVEDATA_API_KEY` | [twelvedata.com](https://twelvedata.com) → Sign up → API Keys | 800 credits/day, 8/min |
| `FINNHUB_API_KEY` | [finnhub.io](https://finnhub.io) → Sign up → Dashboard | 60 calls/min |
| `ALPHAVANTAGE_API_KEY` | [alphavantage.co](https://www.alphavantage.co/support/#api-key) | 25 calls/day |

### Optional — the app degrades gracefully without these, feature-by-feature

| Variable | Where to Get It | What You Lose Without It |
|----------|----------------|---------------------------|
| `FRED_API_KEY` | [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html) — instant, no credit card | Context tab shows no macro data (yield curve, CPI, Fed funds, etc.) |
| `TRADIER_ACCESS_TOKEN` | [tradier.com](https://tradier.com) developer account | Loses the 3rd-tier OHLCV/Quote fallback — chain degrades to `yfinance` as the last active tier if TwelveData fails |
| `SIMFIN_API_KEY` | [simfin.com](https://simfin.com) | Only needed if you run the backtest scripts in `backend/backtest/` — not required for the live app |
| `FMP_API_KEY` | [financialmodelingprep.com](https://financialmodelingprep.com) | Currently unused regardless (dormant in code pending a future paid-plan decision) — safe to skip |

Everything else (news sentiment, EPS/revenue growth) falls back silently to `yfinance` if `ALPHAVANTAGE_API_KEY` is missing — you'll just get lower-quality data, not an error.

---

## 3. Run It

```bash
# From the project root — starts both services
./start.sh

# Or individually
./start.sh backend    # http://localhost:5001
./start.sh frontend   # http://localhost:3000

./stop.sh              # stop both
```

Manual alternative (two terminals):

```bash
# Terminal 1
cd backend && source venv/bin/activate && python backend.py

# Terminal 2
cd frontend && npm start
```

### Verify it's actually working

```bash
curl http://localhost:5001/api/health
```

You should get back `"status": "healthy"` plus a `providers` block showing which of your configured API keys are recognized. Then open http://localhost:3000 and analyze a real ticker (e.g. AAPL) — if it returns a categorical assessment with a verdict, you're fully set up.

---

## 4. Orienting Yourself in the Codebase

```
swing-trade-analyzer/
├── backend/            # Flask API, port 5001
│   ├── backend.py       # main routes
│   ├── providers/       # multi-source data fallback chains
│   ├── paper_trading/   # the automated forward-test engine
│   ├── backtest/        # historical backtest scripts
│   └── validation/      # data-quality validation engine
├── frontend/            # React app, port 3000
│   └── src/
├── docs/
│   ├── claude/           # this project's internal dev-process documentation
│   └── research/         # methodology research
└── README.md
```

See README's [Project Structure](README.md#project-structure) section for the full file-by-file breakdown.

---

## 5. How This Codebase Is Documented

Unusually for a personal project, development history here is tracked in structured, day-numbered docs under `docs/claude/` — originally built as session-continuity notes for AI-assisted development, but they double as a genuinely useful project changelog and rationale record. Worth knowing about even if you never touch that workflow yourself:

- **`docs/claude/stable/GOLDEN_RULES.md`** — accumulated engineering lessons, each with a *why* (usually a real bug that was found and fixed) and a *how to apply*. Skim it once; it'll save you from re-discovering bugs this project already paid to learn about.
- **`docs/claude/stable/ROADMAP.md`** — canonical current state: what's shipped, what's deliberately deferred and why, what the active priority is right now.
- **`docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`** — the methodology this project uses to validate its own claims (5 audit types: Claim, Coherence, Behavioral, Design, External-LLM). If you're doing your own validation of the trading logic, **this is the right starting point** — it's designed for exactly that.
- **`docs/claude/versioned/`** — day-stamped API contracts and known-issues trackers, most recent ~15 days kept active, older ones archived.

---

## 6. Development Practices

A handful of engineering habits this codebase has learned the hard way (each backed by a real incident, detailed in `GOLDEN_RULES.md` if you want the full story):

- **Read the actual code before assuming behavior.** Several real bugs in this project's history came from trusting what a comment or doc *said* over what the code *did*. Don't assume a field exists in an API response — trace it from where it's produced to where it's consumed.
- **Fail loud, not silent.** This codebase deliberately avoids silent fallbacks (e.g., defaulting a missing value to 0 or a plausible-looking placeholder). If something fails, it should surface as a visible error, not a quietly wrong number. When you add a feature, match this — a 500 with a clear message beats a 200 with fake data.
- **Exhaustive checks over spot-checks.** A past session found a fix that passed a 5-example spot-check but was actually only ~21% correct once checked exhaustively. If you're validating something, check every case in the relevant set, not a sample.
- **State that must survive a process boundary needs explicit shared storage.** The Flask server and the paper-trading job are separate processes; anything they both need to agree on (rate limits, circuit-breaker state) lives in SQLite, not in-memory. Keep this in mind if you add anything that runs outside the main Flask process.
- **A live/production counterpart to a backtested engine should reuse the backtest's exact logic, not reimplement it.** The paper-trading engine replays the same simulator functions the backtest uses (via a `live_mode` flag) specifically to prevent live and backtested behavior from silently drifting apart over time.
- **Before calling a fix done, ask what else calls the thing you changed.** A one-line-looking fix earlier this project's history broke an unrelated page because a shared function was used in more than one place. Check call sites, not just the one you're touching.

---

## 7. Known Current Limitations

Worth knowing going in, so nothing here surprises you:

- **Complete feature freeze is in effect** — active development is currently scoped to bug fixes and the paper-trading confirmation effort only. Don't be surprised if a "why hasn't X been built yet" answer is "deliberately parked" — check `ROADMAP.md` before assuming something was missed.
- **~40% disagreement rate** has been measured between live and backtested fundamentals data (different providers, different methodologies) — a known, unresolved gap, not a bug.
- Canadian tickers are supported in the Scan tab but not yet the full Analyze page.
- See README's [Known Limitations](README.md#known-limitations) section for the complete, current list.

---

## Getting Help

- Backend won't start / "Backend Disconnected" / data shows all N/A → see README's [Troubleshooting](README.md#troubleshooting) section first — it covers the common setup issues directly.
- For anything deeper, `docs/claude/stable/GOLDEN_RULES.md` and `ROADMAP.md` are the most likely places to find "yes, we already ran into this."

Happy building — and again, test and validate independently before trusting any signal this tool gives you.
