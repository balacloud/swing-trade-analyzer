# Breakout + Institutional Flow — Next Steps Handoff

> **Purpose:** Clear continuation document for the STA breakout workflow and the proposed Institutional Flow context layer.
>
> **Audience:** Codex / Claude / future coding agent / human maintainer.
>
> **Status:** Handoff after initial breakout artifacts were created. Backend route wiring is not yet complete.
>
> **Important:** This document is an execution guide, not proof of trading edge.

---

## 1. Mandatory STA Grounding Before Any Work

Before modifying code, read the STA session context in this order:

```text
docs/claude/CLAUDE_CONTEXT.md
docs/claude/stable/GOLDEN_RULES.md
docs/claude/stable/ROADMAP.md
docs/claude/status/PROJECT_STATUS_DAY77_SHORT.md
docs/claude/versioned/KNOWN_ISSUES_DAY77.md
```

Why:

- `CLAUDE_CONTEXT.md` is the orchestrating file for startup and close protocol.
- `GOLDEN_RULES.md` contains non-negotiable engineering and audit rules.
- `ROADMAP.md` gives canonical project direction.
- Latest status/known issues define the real current state.

Relevant current state from Day 77:

| Field | Value |
|---|---|
| Current Day | 77 |
| Version | v4.36 |
| Backend | v2.35 |
| Frontend | v4.35 |
| Primary project focus | Paper trading unblocked |
| Medium bug | Canadian Analyze page not supported |
| IBKR research | Complete, `/ibkr-scan` design ready |

---

## 2. Golden Rules That Matter Most Here

Apply these strictly:

| Rule | Practical meaning for this work |
|---|---|
| Read files before modifying | Open actual file first; do not patch from memory |
| Never assume structure | Verify imports, app creation, route placement, API shape |
| Generate files one at a time | Avoid big-bang multi-file changes |
| Producer defines API | Backend engine owns fields; frontend/Pine/prompt adapt |
| Null is not zero | Missing values must be `null`, not fake zeros |
| Return null, not plausible fake | No hardcoded fallback values like VIX=20 style mistakes |
| Run diagnostics first | If something fails, inspect traceback before editing |
| Validate behavior | Real tickers required before claiming feature works |
| Do not over-optimize weights | Equal-weight/simple gates first; avoid overfit |
| Stop and prove | New feature is a hypothesis until tested |

Mindset to use:

```text
Veteran breakout trader: avoid bad breakouts first.
Veteran quant: define rules, test, track outcomes.
Veteran system architect: avoid duplicate logic and drift.
```

---

## 3. What Already Exists in STA Relevant to This Work

Core STA capabilities already present before breakout work:

| Existing STA area | Evidence / notes |
|---|---|
| TradingView screener integration | Existing `/api/scan/tradingview` with strategies such as reddit, minervini, momentum, value, best |
| Support/Resistance engine | Existing `/api/sr/<ticker>` uses DataProvider first, yfinance fallback, S&R levels, ATR, ADX, RSI, OBV, RVOL |
| Pattern detection | Existing `/api/patterns/<ticker>` detects VCP, Cup & Handle, Flat Base, and trend template |
| Price Structure Card | Phase 1 completed; uses S/R touch counts and narrative; Phase 2 deferred HH/HL/LH/LL |
| Value Tab | Standalone value lens; no impact on swing verdict |
| Forward testing | Exists in backend; paper trading now unblocked |
| IBKR screener research | Day 77 research complete; skill design not yet built |

Important existing architectural pattern:

```text
DataProvider first → yfinance fallback → engine → flat JSON response
```

The breakout endpoint should follow this exact pattern.

---

## 4. New Breakout Artifacts Already Created

These files already exist:

| File | Purpose | Status |
|---|---|---|
| `backend/breakout_detection.py` | Backend breakout classification engine | Created |
| `backend/breakout_routes.py` | Thin Flask route registration module | Created, not wired |
| `docs/claude/design/BREAKOUT_ENGINE_SPEC.md` | Single source of truth for breakout state definitions | Created |
| `pine/sta_breakout_companion.pine` | TradingView Pine visual companion | Created |
| `docs/STA_BREAKOUT_HUMAN_IN_LOOP_WORKFLOW.md` | Manual TradingView → Pine → screenshot → Claude/GPT → STA workflow | Created |
| `prompts/STA_CLAUDE_CHART_REVIEW_PROMPT.md` | Reusable screenshot-review prompt | Created |

Known important commits:

```text
4d545aec49673b66324b1f6a2043aa44630f6631 — backend/breakout_detection.py
7074f6d46c598ee09025167eb0c724293a5a37bc — BREAKOUT_ENGINE_SPEC.md
755a7e3ddfd27031db1b9cd391cdd92ba3ea89ba — backend/breakout_routes.py
```

---

## 5. Breakout Engine Philosophy

The breakout engine is not an auto-trading bot.

It is a human-in-the-loop filter that classifies price/volume structure into one state:

```text
NOT_READY
BUILDING_BASE
BREAKOUT_WATCH
BREAKOUT_CONFIRMED
RETEST_ENTRY
SUPPLY_WARNING
FAILED_BREAKOUT
EXTENDED_CHASE_RISK
```

Core principle:

```text
Breakout Engine = structure and timing
Human = final risk decision
Forward test = truth
```

A green breakout state must never be displayed or interpreted as a blind buy signal.

---

## 6. Immediate Missing Step: Wire Backend Route

`backend/breakout_routes.py` exists but is not yet registered in `backend/backend.py`.

### Target endpoint

```text
GET /api/breakout/<ticker>
```

### Required minimal edit in `backend/backend.py`

Before editing, read the current full file locally. Do not rely on this document alone.

Add an optional import block near the existing optional feature imports:

```python
# Try to import breakout routes - graceful fallback
try:
    from breakout_routes import register_breakout_routes
    BREAKOUT_ROUTES_AVAILABLE = True
    print("✅ Breakout Routes loaded successfully")
except ImportError as e:
    BREAKOUT_ROUTES_AVAILABLE = False
    print(f"⚠️ Breakout Routes not available: {e}")
```

Then after:

```python
app = Flask(__name__)
CORS(app)
```

add:

```python
# Register breakout detection routes
if BREAKOUT_ROUTES_AVAILABLE:
    register_breakout_routes(app, get_data_provider, yf, DATA_PROVIDER_AVAILABLE)
```

Do not refactor unrelated code.
Do not modify `/api/sr/<ticker>`.
Do not modify `/api/patterns/<ticker>`.
Do not build frontend yet.

---

## 7. Breakout API Expected Response Shape

Example shape only; values vary by ticker and date:

```json
{
  "ticker": "IBM",
  "status": "BREAKOUT_WATCH",
  "humanAction": "Watch closely; wait for decisive close/volume confirmation.",
  "currentPrice": 248.25,
  "breakoutLevel": 245.50,
  "supportLevel": 238.00,
  "invalidation": 238.00,
  "retestZoneLow": 243.05,
  "retestZoneHigh": 247.95,
  "rvol": 1.62,
  "atrPct": 2.10,
  "extensionFromSma50Pct": 6.40,
  "checks": {},
  "warnings": {},
  "evidence": {},
  "source": "DataProvider",
  "benchmark": {
    "ticker": "SPY",
    "source": "DataProvider",
    "available": true
  },
  "dataPoints": 260,
  "apiTimestamp": "..."
}
```

Rules:

- `status` must be present.
- `checks` must be present.
- `warnings` must be present.
- Missing values must be `null`, not fake zero.
- Errors should be real HTTP errors, not silent 200s.

---

## 8. Breakout Validation Plan

After wiring, test real tickers before claiming success:

```bash
curl http://localhost:5001/api/breakout/IBM
curl http://localhost:5001/api/breakout/MSFT
curl http://localhost:5001/api/breakout/NVDA
curl http://localhost:5001/api/breakout/PLTR
```

Minimum validation matrix:

| Ticker | Purpose |
|---|---|
| IBM | Original breakout-style example |
| MSFT | Quality mega-cap baseline |
| NVDA | AI leader / strong trend example |
| PLTR | Possible extension-risk / high momentum example |
| Weak downtrend ticker | Should ideally classify `NOT_READY` or warning state |

Check:

1. Backend starts without crash.
2. Endpoint returns HTTP 200 for valid tickers.
3. `status`, `checks`, `warnings`, `evidence` are present.
4. SPY benchmark availability is transparent.
5. Values are not fabricated.
6. Output is consistent with `BREAKOUT_ENGINE_SPEC.md`.
7. Compare at least 2 tickers visually in TradingView with Pine companion.

If there is a mismatch between backend and Pine:

- Do not guess.
- Determine whether mismatch is due to data freshness, level detection, benchmark, candle definitions, or Pine/backend drift.
- Fix only the root cause.

---

## 9. Institutional Flow Thesis — External Feedback Summary

The user asked how to detect when institutions are buying/selling without too many false positives.

External feedback from Reddit and Grok agreed on the main direction but warned against overclaiming.

### Validated direction

A price-volume flow layer can be useful as a confirmatory filter for breakouts.

### Critical correction

Do not claim:

```text
Institutions are buying.
```

Prefer:

```text
Price-volume behavior is constructive.
```

### Design principle

Institutional Flow should be a context layer, not a standalone trigger.

```text
Breakout Engine = structure/timing
Flow Layer = participation/context
Human = decision
Journal = validation
```

---

## 10. Refined Institutional Flow v1 Direction

Do not build this until `/api/breakout/<ticker>` is wired and validated.

Potential file later:

```text
backend/institutional_flow.py
backend/flow_routes.py
GET /api/flow/<ticker>
```

Preferred v1 naming:

| Status | Meaning |
|---|---|
| `CONSTRUCTIVE_FLOW` | Demand footprint is constructive |
| `NEUTRAL_FLOW` | No clear participation edge |
| `DISTRIBUTION_WARNING` | Selling pressure dominates |
| `MIXED_FLOW` | Both accumulation and distribution signs visible |
| `CLIMAX_WATCH` | Extreme volume/candle behavior with potential reversal watch |

Avoid names that imply certainty, such as `INSTITUTIONS_BUYING`.

---

## 11. Institutional Flow Candidate Signals

### Constructive flow signals

| Signal | Initial threshold |
|---|---:|
| Up day on RVOL | Close > prior close and RVOL ≥ 1.5 |
| Strong close | Close location ≥ 0.65 |
| Very strong close | Close location ≥ 0.75 |
| Price above SMA50 | Close > SMA50 |
| Low-volume pullback | Down day volume < 20-day average volume |
| RS improving | Stock/sector ETF ratio > 20-day average |
| OBV trend | OBV rising over 20–50 bars, confirmation only |

### Distribution warning signals

| Signal | Initial threshold |
|---|---:|
| Heavy down day | Close < prior close and RVOL ≥ 1.5 |
| Weak close | Close location ≤ 0.35 |
| Very weak close | Close location ≤ 0.25 |
| SMA50 damage | Close < SMA50 and RVOL ≥ 1.5 |
| Repeated distribution | 3+ high-volume weak-close days in 20 sessions |
| Failed breakout | Close back below breakout level on volume |
| RS weakening | Stock/sector ETF ratio < 20-day average |

Important false-positive reducer:

```text
SMA50 break alone is not distribution.
SMA50 break + high RVOL + weak close + falling RS = distribution warning.
```

---

## 12. Institutional Flow v1 Classification Guidance

Use simple confirmatory states, not complex optimized scoring.

Suggested v1 approach:

| State | Rule idea |
|---|---|
| `CONSTRUCTIVE_FLOW` | Multiple constructive signs, no strong distribution flags |
| `DISTRIBUTION_WARNING` | Multiple distribution signs or major high-volume weak close |
| `MIXED_FLOW` | Constructive and distribution evidence both present |
| `CLIMAX_WATCH` | Extreme volume + large range + meaningful recovery off lows |
| `NEUTRAL_FLOW` | Everything else |

Do not optimize weights yet.
Do not use ML yet.
Do not overfit thresholds.

---

## 13. What NOT To Build Yet

Until breakout API is wired and validated, do not build:

- Frontend breakout badge
- Institutional Flow endpoint
- IBKR scanner automation
- Options/gamma flow integration
- ML weighting
- Volume Profile/VWAP module
- News/dilution radar
- Frontend journal fields

The immediate job is still:

```text
Wire /api/breakout/<ticker> → validate → compare with Pine
```

---

## 14. Future Build Order

Recommended order:

| Step | Task | Reason |
|---:|---|---|
| 1 | Wire `/api/breakout/<ticker>` | Make current breakout engine callable |
| 2 | Validate IBM/MSFT/NVDA/PLTR | Prove behavior with real tickers |
| 3 | Compare backend vs Pine | Prevent logic drift |
| 4 | Add API contract doc if endpoint works | Keep docs synced |
| 5 | Design Institutional Flow spec | Incorporate Reddit/Grok feedback |
| 6 | Build `institutional_flow.py` | Simple context layer only |
| 7 | Add `/api/flow/<ticker>` | Make flow layer callable |
| 8 | Combine breakout + flow in UI | Stronger human decision context |
| 9 | Add journal fields | Track whether this improves outcomes |
| 10 | Run behavioral audit | Validate runtime output against chart reality |

---

## 15. Audit Framing

### Claim: Breakout API should be wired next

**Reasoning:** The breakout engine, route module, spec, Pine companion, and prompt exist. The route is not registered in Flask yet, so the engine is not accessible from STA. Wiring the route is the smallest next step.

**Verdict:** [VERIFIED — SOURCE: Repo search shows breakout files exist and route wiring remains incomplete.]

### Claim: Institutional Flow should be built immediately

**Reasoning:** External feedback supports the idea, but also warns against over-complexity and overclaiming. The breakout API is not validated yet.

**Verdict:** [MISLEADING — CORRECTION: Finish and validate breakout API first; then design flow spec.]

### Claim: Institutional Flow can identify institutions with no false positives

**Reasoning:** Direct institutional activity is not fully observable from retail OHLCV. Price-volume behavior can only infer footprints probabilistically.

**Verdict:** [MISLEADING — CORRECTION: Build a constructive/distribution flow context layer, not an institutional certainty detector.]

---

## 16. Final Next Action

The next agent should do exactly this:

```text
1. Read CLAUDE_CONTEXT + GOLDEN_RULES + ROADMAP + latest status/issues.
2. Read backend/backend.py locally in full.
3. Add optional import for register_breakout_routes.
4. Register breakout route after app creation.
5. Start backend.
6. Test /api/breakout/IBM, MSFT, NVDA, PLTR.
7. Report exact outputs.
8. Do not build anything else until validation passes.
```

---

*This handoff is intentionally conservative. STA should evolve as a validated trading workflow, not as an indicator-collection project.*
