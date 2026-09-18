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
> **Last Updated:** Day 118 — #1 repaired 2026-09-15 (kept from an earlier
>            in-session pass); #4 flagged stale (MTF Confluence and Pattern
>            Detection's price-target grades were fixed Day 118, the artifact
>            page itself not republished). #5/#6/#7/#8 still reflect their
>            Day 112 republish and have not been checked against Days 113-118.

---

## The 8 artifacts

| # | Artifact | Favicon | Purpose | Current state |
|---|---|---|---|---|
| 1 | [Analyze Page Redesign — Decision Map](https://claude.ai/code/artifact/3e82355f-a495-49d0-9375-ce9cc257bd0b) | 🧭 | Maps all 16 redesign decisions against the 9-principle "100 years of trading" canon (`TRADING_PRINCIPLES_100YR_RESEARCH.md`); shows Locked/Open status per item. | **Current (republished 2026-09-15).** Item 08 (Entry/Stop/Target) now marked FIXED — the S&R `_pivot_sr` bug it described as "not yet implemented" shipped Day 112. The open-agenda "duplicate R:R arithmetic" item's deferral reason (touches `compute_sr_levels`) is now moot and says so. Header status-pill no longer claims "gated behind forward-testing" — the program was discontinued 2026-09-12. Item 15's MR numbers refreshed to the program's final standing result (217 closed, PF 2.46) with a note that no further trades will accumulate. The "Implement now, or stay parked?" agenda item's freeze-gating language removed — it's now purely a scheduling choice. |
| 2 | [Fundamentals & Sentiment — Card Visual Design](https://claude.ai/code/artifact/ecb47fc2-1368-40d9-97e7-408ccc3ffa80) | 🎛️ | Visual mockup of the Fear & Greed gauge and the 4-state Fundamentals red-flag card. | **Current.** Static reference, nothing about either card's design has changed since publish. |
| 3 | [Descriptive Cards — Who Actually Uses Them](https://claude.ai/code/artifact/403ee70f-af19-461f-a5a0-5b4feb2c563c) | 🧩 | Maps S&R / MTF Confluence / Price Structure / Pattern Detection / Breakout Status to which trading strategy (Momentum / Pullback / Breakout / Mean-Reversion) actually consumes each one. | **Current.** Nothing in this mapping has changed. |
| 4 | [Descriptive Cards — Industry-Standard Report Card](https://claude.ai/code/artifact/c3ec8875-8b66-4edd-8597-9ce95e3f54ba) | 🔬 | Grades S&R (2/10), MTF Confluence (3/10), Price Structure (9/10), Pattern Detection recognition (8/10) vs. its price target (1.5/10), and Breakout Status (9/10) against named real methodology. | **⚑ STALE (Day 118) — grades not republished.** S&R's fix (Day 112) was already reflected as current at the time. But two of the three remaining below-standard grades are now out of date: MTF Confluence's "arbitrary multiplier" (3/10) and Pattern Detection's "flat-percentage target" (1.5/10) were both fixed Day 118 (`docs/claude/design/MTF_VCP_FIX_PLAN_DAY115.md`) — the artifact's page itself hasn't been republished to reflect either fix. Not done this session; flagged for next time this artifact is touched. |
| 5 | [Audit Coverage Timeline](https://claude.ai/code/artifact/ba5ac987-da3d-4121-be9c-2e91269201b7) | 🗺️ | Visual timeline of every documented audit touch across the app's 11 components — reveals the Day 107 mega-sweep and its flagged gaps. | **Current (republished Day 112).** The S&R/Pattern-engine Day 111 audit no longer shows as a hollow "in progress" ring or a flagged gap — it's marked closed (the finding is fully written up in `KNOWN_ISSUES`, Golden Rule 53, and `AUDIT_COVERAGE_LEDGER.md`'s own RESOLVED gap-note). Flagged-gap count 3→2; today-line moved to Day 112; Analyze Tab row de-hollowed too (real shipped work Day 111–112). |
| 6 | [STA Data Provenance Map](https://claude.ai/code/artifact/95843cfe-d814-448f-9428-9c6a0df1958c) | 📡 | Every tab mapped to its data source(s), fallback chains, field-level provenance, and what's locally computed. | **Current (republished Day 112).** The `/api/mr/scan` orchestrator-bypass (Finding 2) now shows **fixed Day 111** — a green "Fixed D111" badge on the Forward Test row and a resolved (✓) entry in the flagged list, instead of an open ⚑. Matches `DATA_PROVENANCE_FINDINGS_DAY111.md`. |
| 7 | [Analyze Page Redesign — Mockup](https://claude.ai/code/artifact/ef8a4f89-b19c-480a-b757-26072dcd2a26) | 🧭 | The actual interactive mockup of the redesigned Analyze page — the only artifact in this list that's a full page mockup rather than a reference diagram. | **v0.4, current (republished Day 112).** The Regime band's copy is now the post-Day-110-reversal Info wording (matching `ANALYZE_PAGE_REDESIGN_DECISIONS.md` §6 verbatim) — the last known gap, now closed. Also carries the Day 111 Mean-Reversion Read card and the Day 112 Volume Confirmation + Direction read. The rest of the mockup remains a design vision, not live (see the table below). |
| 8 | [Forward-Test Track Board](https://claude.ai/code/artifact/906b779b-0440-4cf2-8de0-fb3d17f58678) | 🛤️ | Live state of the four paper-trading forward-test tracks as of Day 112: MR (broad) confirmed, Momentum Path B retired, Path A + HUB-65 still accumulating toward the 100-closed-trade bar. Includes the Path B PF-decay chart (1.37→1.23→1.01 at 100/117/150 trades) and what the confirmation/retirement unblocked. | **Current (published Day 112).** Numbers pulled live from `daily_job.py --report` on 2026-09-02. Track counts move between sessions — re-pull live rather than trusting the snapshot; the *decisions* it records (MR confirmed, Path B retired) are stable. |

---

## Reading this table

- **As of Day 118, one artifact (#4) is known stale** — its MTF Confluence
  and Pattern Detection grades no longer match the live app (both fixed Day
  118). The other seven have not been re-audited against Days 113-118's
  changes; treat "Current (republished Day 112)" as "current as of Day 112,"
  not verified since.
- **Two artifacts (1, 7) are about the same subject** — the Analyze Page
  Redesign — but serve different jobs: #1 is a structured decision registry,
  #7 is what the page would actually look like. Both matched the underlying
  decision doc (`ANALYZE_PAGE_REDESIGN_DECISIONS.md`) as of their last check.
- **Two artifacts (2, 3) have never needed a change** — nothing they
  describe has moved since publish. #4 (previously grouped with them) no
  longer belongs in this "never needs a change" set — see above.
- **#8 is the only one whose numbers go stale on their own** — it's a live
  snapshot of forward-test track state. Re-pull via `daily_job.py --report`
  rather than trusting it between sessions; the decisions it records are
  stable, the trade counts are not.

## What actually shipped to the live app vs. what's still mockup-only

Worth being explicit about, since artifact #7 can read as "the design" when
part of it is now real:

| Feature | Live in `frontend/src/App.jsx` today? | Also shown in mockup #7? |
|---|---|---|
| Volume Confirmation (magnitude) | ✅ Yes — Day 111 | ✅ Yes — Day 112 |
| Volume Direction (lean) | ✅ Yes — Day 112 | ✅ Yes — Day 112 |
| Mean-Reversion Read card | ❌ No — mockup only | ✅ Yes — Day 111 |
| MR Scanner (Scan tab button) | ✅ Yes — Day 111 | n/a (Scan tab, not this mockup) |
| Regime band → Info (not hard gate) | ❌ No — live page still has the old composite verdict | ✅ Yes — copy synced to the Day 110 reversal on Day 112 |
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
- `docs/claude/stable/PAPER_TRADING_PREREGISTRATION.md` (§8b, §10) +
  `backend/paper_trading/daily_job.py --report` — the frozen rules and live
  numbers artifact 8 visualizes
