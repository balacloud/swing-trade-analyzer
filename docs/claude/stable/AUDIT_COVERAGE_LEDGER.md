# Audit Coverage Ledger

> **Purpose:** answers "has this actually been reviewed before, and how deeply?" —
>            so a future audit request can be checked against real history instead
>            of re-deriving scope from scratch, and a report can honestly separate
>            "re-verified known issue" from "genuinely new finding."
> **Companion to:** `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md` (defines the
>            Layer 1/2/3 depth scale used in the table below) and
>            `docs/claude/stable/GOLDEN_RULES.md`.
> **Created:** Day 111, in response to a direct question — repeated deep-dive
>            requests kept *feeling* like they were surfacing endless new bugs;
>            tracing it back showed most "new" findings were already-documented
>            open issues re-presented in a new format, with genuinely new
>            discoveries being the rare exception, not the rule. This doc exists
>            so that distinction is checkable instead of a vibe.
> **How to keep this current:** whenever a real audit/deep-dive happens (not a
>            casual mention), update that component's row — Last review, Depth,
>            Findings, Source doc. Don't let it silently go stale; a stale ledger
>            is worse than no ledger, because it produces false confidence.
> **Last Updated:** Day 111

---

## The taxonomy

The Day 107/108 full-system audit (`docs/claude/versioned/FULL_AUDIT_FINDINGS_DAY107.md`)
is the only audit that has ever attempted full-app coverage in one pass. It
organized the app into 10 numbered groups, two of which are internally split
into two sub-components each — 13 real components mapped onto 10 slots:

| # | Group (as the source doc names it) | Component(s) covered |
|---|---|---|
| 1 | S&R / Pattern / Market-Structure Engine | Backend: `support_resistance.py`, `pattern_detection.py`, market-structure classifier |
| 2 | Core Verdict Engine | `categoricalAssessment.js` / `categorical_engine.py` (JS↔Python parity contract) |
| 3 | FWD-Testing Frozen-Rules | `backend/paper_trading/*` — entry/exit gates, all 4 live tracks |
| 4a/4b | Analyze Tab | UI layer — behavioral (4a) + coherence (4b) |
| 5 | Scan Tab | UI layer |
| 6a/6b | Sectors Tab / Context Tab | UI layer, two separate tabs bundled as one group |
| 7 | Value Tab | UI layer |
| 8 | Validate + Data Sources Tabs | UI layer, two tabs bundled |
| 9 | Providers Package | `backend/providers/*`, orchestrator, rate-limiter, circuit-breaker |
| 10 | Forward Test Tab + Settings Tab | UI layer, two tabs bundled |

Depth scale (from `MASTER_AUDIT_FRAMEWORK.md`): **L1** = does documentation match
code (consistency); **L2** = is the logic itself sound (correctness); **L3** =
does runtime behavior match what the code claims (live-verified, not just read).

---

## Coverage table

| Component | Last substantive review | Depth | Findings (rough) | Source doc(s) |
|---|---|---|---|---|
| **S&R / Pattern / Market-Structure Engine** | **Day 111** (in progress — see gap note below), superseding Day 107 | L1+L2 (no live-ticker sweep done Day 111) | Day 111: 1 confirmed open Medium bug so far (`_pivot_sr()` "nearest" mislabeling — Golden Rule 53). Day 107: 1 CRITICAL fixed (MTF fabricated dates), 1 HIGH parked, 4 lower fixed/logged. Day 64: weekly-resample + hardcoded-stop bugs fixed. Day 61: clean (38 fields verified) | `GOLDEN_RULES.md` Rule 53; `FULL_AUDIT_FINDINGS_DAY107.md` Group 1; `versioned/archive/COHERENCE_AUDIT_DAY64.md`, `DAY61.md` |
| **Core Verdict Engine** | Day 107 | L1+L2, incl. live exhaustive parity run (86,400/86,400, 0 mismatches) | 2 Medium fixed (stale docstrings), 3 Low logged, core logic confirmed byte-identical JS↔Python | `FULL_AUDIT_FINDINGS_DAY107.md` Group 2; Day 78 external review (Golden Rule 19 origin); `COHERENCE_AUDIT_DAY57/61/64.md` |
| **FWD-Testing Frozen-Rules** | Day 107 (Claim Audit vs. `PAPER_TRADING_PREREGISTRATION.md`) | L1 (claim-tracing, not a fresh threshold re-justification) | 1 finding downgraded High→Medium (VIX sizing never wired, Golden Rule 48); everything else (R:R gate, exits, S&R gate, HUB-65 gate, cooldowns) verified clean | `FULL_AUDIT_FINDINGS_DAY107.md` Group 3; construction/fix trail: Golden Rules 27-29, 35-39 (Days 91-99) |
| **Analyze Tab (UI)** | Day 107, cards re-touched Day 111 (uncommitted) | L1 (coherence, ~50 threshold sites) + L3 (live curl/browser, 7 tickers incl. 2 Canadian) | Day 107: 3 Medium fixed, 1 Low logged (ADX 15 vs 20 ambiguity), Canadian-ticker question resolved. Day 71: 1 live CRITICAL fixed (`marketCap` undefined). Day 82-83: 6 bugs + 6 DRY violations fixed | `FULL_AUDIT_FINDINGS_DAY107.md` Groups 4a/4b; `versioned/archive/BEHAVIORAL_AUDIT_DAY71.md`; `design/UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md` |
| **Scan Tab** | Day 107 | L1 + L3 (live-verified, not just read) | Clean pass — 0 Critical/High/Medium, only Low-severity logged. Prior: Day 82-83 fixed a HIGH candidate-set-divergence bug; Day 106 fixed breakout-badge ambiguity (Golden Rule 44) | `FULL_AUDIT_FINDINGS_DAY107.md` Group 5; `UI_CODE_QUALITY_AUDIT_AND_FIX_PLAN_DAY82.md`; `GOLDEN_RULES.md` Rule 44 |
| **Sectors Tab** | Day 107 | L1 + L3 (explicitly upgraded — "a real bug on every prior audit pass since Day 93") | 1 Medium fixed at true root (Golden Rule 30's fix finally migrated — new Golden Rule 47), rest live-verified clean | `FULL_AUDIT_FINDINGS_DAY107.md` Group 6a; `GOLDEN_RULES.md` Rules 30, 47; Days 93/94/101/103/105 build/fix history |
| **Context Tab** | Day 107 | L1 (git-history root-cause trace) + targeted L2 fixes | 2 High (1 fixed — wasted API credit/double-fetch; 1 logged — bypasses `api.js`), 1 Medium-High logged (PMI date-alignment gap), 2 more fixed | `FULL_AUDIT_FINDINGS_DAY107.md` Group 6b; Golden Rule 26 (Day 91); Day 92-93 fixes |
| **Value Tab** | Day 107 | Claim Audit + L1/L2 | 1 High fixed (live-reproduced FCF-Yield badge bug), 2 Medium logged (attribution-wording decisions pending) | `FULL_AUDIT_FINDINGS_DAY107.md` Group 7; `design/VALUE_TAB_SPEC.md` (Day 75) |
| **Validate + Data Sources Tabs** | Day 107 | L3 — settled via a real natural experiment (a live circuit-breaker trip during the audit) | 1 Medium fixed (`/api/health` hardcoded status), 1 High logged (per-ticker provenance gap — see gap note below) | `FULL_AUDIT_FINDINGS_DAY107.md` Group 8; Day 91 origin |
| **Providers Package** | Day 107 (scoped re-verification, not fresh) | L1 (file-by-file re-check of 2 named Golden Rules across all 7 provider files) | 0 new bugs; 2 Low doc-only fixes; Golden Rules 22 & 36 confirmed fully intact | `FULL_AUDIT_FINDINGS_DAY107.md` Group 9; real depth from Day 83 + Day 95-96 (Golden Rules 22, 33, 36) |
| **Forward Test Tab + Settings Tab** | Day 107 | L1 + targeted L3 | 1 Medium fixed (dual "Expectancy" labels), 1 Medium logged (risk-slider vs. documented ceiling), `variant` disambiguation reconfirmed | `FULL_AUDIT_FINDINGS_DAY107.md` Group 10; Golden Rule 38 (Day 98) |

---

## How far back real tracking actually goes

- **Earliest commit:** `1bf15e0a "Day 1 complete : Backend with yfinance integration"`, dated **2025-11-25** (verified directly via `git log`).
- **`docs/claude/` structure formalized:** commit `cafb9591`, "Day 25: Reorganize docs into /docs/claude/ structure" — everything from Day 1-24 exists only as raw git history and ROADMAP's retrospective "COMPLETED (v1.0-v3.9)" table, not as dedicated per-day docs.
- **Day-numbered versioned docs** (`*_DAY[N].md` convention) effectively start around **Day 23-24**, just before the Day 25 reorg.
- **Days 1-9 have no dedicated status/known-issues doc at all** — visible only via git commit messages and ROADMAP's retrospective table.
- **Most recent formal, committed audit:** Day 108 (`FULL_AUDIT_FINDINGS_DAY107.md`, commit `19005f4d`).

## Known gaps — flagged plainly, not smoothed over

1. ~~**The Day 111 five-card audit... is itself incomplete and unpersisted.**~~
   **RESOLVED (Day 111, same session).** Full remediation plans for all three
   below-standard findings are now written up in `KNOWN_ISSUES_DAY110.md`:
   S&R's extreme-vs-nearest selection bug (2.0/10), MTF Confluence's arbitrary
   hardcoded confidence multiplier (3.0/10), and Pattern Detection's
   flat-percentage price target (1.5/10, promoted from a bundled one-liner to
   its own full entry). Price Structure (9/10) and Breakout Status (9/10)
   confirmed clean, no new findings. Group 1's row above still reads "Day 111,
   in progress" — update it to "Day 111, complete" on the next ledger pass.
2. **Per-ticker data provenance** ("never checked" vs. "just failed") has now
   survived **three separate audit passes without being fixed** — pre-Day-91,
   Day 91, and Day 107/108 — and every pass has stayed at L1 (code-read
   confirmation). No session has yet built or tested the actual fix. If this
   surfaces as a "new" finding in a future review, it isn't new — check here
   first.
3. **`ContextTab.jsx`'s bypass of `api.js`** — not an unaudited gap, an
   audited-and-explicitly-not-migrated one (confirmed dead/never-wired since
   Day 62/87). Logged as an architectural finding, not fixed.

---

*This file lives in `/docs/claude/stable/` — update it whenever a real audit
happens, don't let it go stale.*
