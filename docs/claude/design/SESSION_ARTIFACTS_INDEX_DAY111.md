# Session Artifacts Index — Day 111-112

> **Purpose:** every visual Artifact published during the Day 111-112 audit +
>            Analyze Page Redesign work, in one place, with an honest current-
>            state note for each — so a future session can tell "still
>            accurate" from "known stale" at a glance instead of re-deriving
>            it. Companion to `docs/claude/stable/AUDIT_COVERAGE_LEDGER.md`
>            (which tracks *code* review coverage) — this tracks *visual*
>            artifact coverage instead.
> **How to keep this current:** whenever an artifact listed here gets
>            republished, update its "Current state" cell in the same edit.
>            When a new artifact is published, add a row here before the
>            session ends. A stale index is worse than no index.
> **Created:** Day 111 (retroactively, cataloging 7 artifacts already
>            published this session)
> **Last Updated:** Day 112

---

## The 7 artifacts

| # | Artifact | Favicon | Purpose | Current state |
|---|---|---|---|---|
| 1 | [Analyze Page Redesign — Decision Map](https://claude.ai/code/artifact/3e82355f-a495-49d0-9375-ce9cc257bd0b) | 🧭 | Maps all 16 redesign decisions against the 9-principle "100 years of trading" canon (`TRADING_PRINCIPLES_100YR_RESEARCH.md`); shows Locked/Open status per item. | **Stale, one point.** Updated Day 111 with item 15 (Mean-Reversion Read) and 3 status corrections. Does **not** yet reflect the Day 111-112 Volume Confirmation + Direction shipment. Also: this artifact's own "item 15" (MR Read) and the decision doc's separate "§9 Item 16" (Volume Confirmation) are two different things that happen to be numbered close together across two documents — worth a cleanup pass if this gets touched again. |
| 2 | [Fundamentals & Sentiment — Card Visual Design](https://claude.ai/code/artifact/ecb47fc2-1368-40d9-97e7-408ccc3ffa80) | 🎛️ | Visual mockup of the Fear & Greed gauge and the 4-state Fundamentals red-flag card. | **Current.** Static reference, nothing about either card's design has changed since publish. |
| 3 | [Descriptive Cards — Who Actually Uses Them](https://claude.ai/code/artifact/403ee70f-af19-461f-a5a0-5b4feb2c563c) | 🧩 | Maps S&R / MTF Confluence / Price Structure / Pattern Detection / Breakout Status to which trading strategy (Momentum / Pullback / Breakout / Mean-Reversion) actually consumes each one. | **Current.** Nothing in this mapping has changed. |
| 4 | [Descriptive Cards — Industry-Standard Report Card](https://claude.ai/code/artifact/c3ec8875-8b66-4edd-8597-9ce95e3f54ba) | 🔬 | Grades S&R (2/10), MTF Confluence (3/10), Price Structure (9/10), Pattern Detection recognition (8/10) vs. its price target (1.5/10), and Breakout Status (9/10) against named real methodology. | **Current.** The graded issues themselves (S&R's nearest-vs-extreme bug, MTF's arbitrary multiplier, Pattern Detection's flat-percentage target) are all still open per `KNOWN_ISSUES_DAY110.md` — none have been fixed yet, only *planned*. Grades still hold. |
| 5 | [Audit Coverage Timeline](https://claude.ai/code/artifact/ba5ac987-da3d-4121-be9c-2e91269201b7) | 🗺️ | Visual timeline of every documented audit touch across the app's 11 components — reveals the Day 107 mega-sweep and 3 flagged gaps. | **Stale, one point.** Shows the S&R/Pattern-engine Day 111 audit as a hollow "in progress, incomplete" ring. That finding was fully written up the same session (`KNOWN_ISSUES_DAY110.md`'s S&R/MTF/Pattern Detection entries, `AUDIT_COVERAGE_LEDGER.md`'s own gap-note already marked this RESOLVED) — the artifact itself was never republished to match. Low priority to fix; the underlying ledger doc is the source of truth and is current. |
| 6 | [STA Data Provenance Map](https://claude.ai/code/artifact/95843cfe-d814-448f-9428-9c6a0df1958c) | 📡 | Every tab mapped to its data source(s), fallback chains, field-level provenance, and what's locally computed. | **Stale, one point.** The `/api/mr/scan` orchestrator-bypass finding it flags (Finding 2) was **fixed Day 111** — the artifact still shows it as an open flagged inconsistency. `DATA_PROVENANCE_FINDINGS_DAY111.md` is the current source of truth; the artifact lags it. |
| 7 | [Analyze Page Redesign — Mockup](https://claude.ai/code/artifact/ef8a4f89-b19c-480a-b757-26072dcd2a26) | 🧭 | The actual interactive mockup of the redesigned Analyze page — the only artifact in this list that's a full page mockup rather than a reference diagram. | **v0.3, mostly current, one known gap.** Updated Day 111 (Mean-Reversion Read card added) and Day 112 (Volume Confirmation + Direction read added to Technical Read, matching the live-shipped wording exactly). **Still open:** the Regime band's copy is the pre-Day-110-reversal "stand-down" language — verified directly, not fixed in this pass. Tracked in `ANALYZE_PAGE_REDESIGN_DECISIONS.md` §6 (which itself already has the *correct* post-reversal copy — only this rendered mockup lags). |

---

## Reading this table

- **Two artifacts (1, 7) are about the same subject** — the Analyze Page
  Redesign — but serve different jobs: #1 is a structured decision registry,
  #7 is what the page would actually look like. Both currently lag the same
  underlying decision doc (`ANALYZE_PAGE_REDESIGN_DECISIONS.md`), which is
  itself the source of truth and is up to date.
- **Two artifacts (5, 6) lag a specific finding that got fixed after they
  published.** Neither is wrong about anything else on the page — just that
  one point each. Their underlying docs (`AUDIT_COVERAGE_LEDGER.md`,
  `DATA_PROVENANCE_FINDINGS_DAY111.md`) are current; only the rendered
  visual hasn't caught up.
- **Three artifacts (2, 3, 4) are fully current** — nothing they describe
  has changed since publish.

## What actually shipped to the live app vs. what's still mockup-only

Worth being explicit about, since artifact #7 can read as "the design" when
part of it is now real:

| Feature | Live in `frontend/src/App.jsx` today? | Also shown in mockup #7? |
|---|---|---|
| Volume Confirmation (magnitude) | ✅ Yes — Day 111 | ✅ Yes — Day 112 |
| Volume Direction (lean) | ✅ Yes — Day 112 | ✅ Yes — Day 112 |
| Mean-Reversion Read card | ❌ No — mockup only | ✅ Yes — Day 111 |
| MR Scanner (Scan tab button) | ✅ Yes — Day 111 | n/a (Scan tab, not this mockup) |
| Regime band → Info (not hard gate) | ❌ No — live page still has the old composite verdict | ✅ Yes, but with **stale pre-reversal copy** (see row 7 above) |
| Technical Read / Trade Setup / Fundamentals card / Sizing Inputs (the whole redesign) | ❌ No — none of this exists on the live page yet | ✅ Yes |

The volume features are the only ones that exist in *both* places right
now — everything else in the mockup is still purely a design vision.

---

## Source docs these artifacts pair with

- `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` — the decision
  registry artifacts 1 and 7 visualize
- `docs/claude/stable/GOLDEN_RULES.md` Rule 53 — the S&R finding artifact 4
  grades
- `docs/claude/versioned/KNOWN_ISSUES_DAY110.md` — remediation plans for
  every graded weak spot in artifact 4, plus the shipped Volume
  Confirmation/Direction entries
- `docs/claude/stable/AUDIT_COVERAGE_LEDGER.md` — the tracking doc artifact
  5 visualizes
- `docs/claude/versioned/DATA_PROVENANCE_FINDINGS_DAY111.md` — the findings
  artifact 6 visualizes
- `docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md` — the canon artifact
  1 measures every decision against
