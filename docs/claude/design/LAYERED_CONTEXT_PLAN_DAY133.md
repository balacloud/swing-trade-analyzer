# Layered context (L1 / L2 / L3) for STA docs — plan (Day 133)

## Context
`/sta-start` reads six files in full every session. Measured sizes (bytes, ÷4 ≈ tokens):
CLAUDE_CONTEXT 41.7k, GOLDEN_RULES 81k, PERSONA 58k, ENGINEER 18.6k, ROADMAP 144.7k, KNOWN_ISSUES 45k, STATUS 2.4k
= ~391 KB ≈ **98k tokens** (ROADMAP alone ≈ 36k; I only read its first 268 lines today). MEMORY.md adds ~20 KB ≈ 5k.
Most of it is history: update log, day summaries, resolved issues, "COMPLETE" roadmap sections, PERSONA Feedback Log (≈ 80% of that file),
and 69 full-text Golden Rules of which a session needs a handful. The same fact is also written in 4–5 files.
The old OKF memory note set the trigger "revisit past ~50 rules"; we are at 69.

**Goal:** session start ≈ 15–20k tokens, nothing deleted, every rule/number citation still resolves.
Docs-only change (no code under frontend/src, frontend/scripts, backend), so the three-pass stamp hook does not fire; we still do plan → Opus review → build → verify.

## Layers
- **L1 — read every session (~15–20k tokens):**
  - `CLAUDE_CONTEXT.md` slimmed: current-state table, last 3 day summaries (short), next priorities, protocols, **a "when you work on X, read Y" map**.
  - `GOLDEN_RULES.md` becomes the **index**: a short "always" list + one line per rule (number, title, *read the full rule when…*). Rule numbers unchanged.
  - `PERSONA.md` core only (who, principles, don'ts, pitfalls, Architect's Lens, how to apply).
  - `ENGINEER.md` unchanged (actionable every change, ~4.7k tokens).
  - `ROADMAP.md` becomes the **open work only**: version line, numbered open priorities (#17–#26 style), research/deferred.
  - `KNOWN_ISSUES_DAYn.md` = **open High/Medium only**.
  - Latest `PROJECT_STATUS`.
- **L2 — loaded when the task touches the area:** `docs/claude/stable/rules/<cluster>.md`, full rule text moved verbatim, with frontmatter (`type: rule`, `tags`, `rules: [..]`, `last_updated`). ~8 clusters (data providers & cache; verdict engine & parity; backtest honesty; paper-trading ledger; UI labels & display; review process & hooks; claims & verification; broker/tool use). Cluster files, not 69 files: less fragmentation, same OKF idea.
- **L3 — archive, read on request:** `docs/claude/stable/archive/ROADMAP_HISTORY.md` (all COMPLETE sections + header day paragraphs + update log), `PERSONA_LOG.md` (Feedback Log), `CLAUDE_CONTEXT_LOG.md` (old summaries + update log), `KNOWN_ISSUES_LOW_AND_RESOLVED.md` (Low/Info, resolved, "Changes from" history; one living file, not day-numbered).

## Phases (one commit each, so each is a one-step rollback)
0. **Baseline.** Record byte/token counts of the six startup files; list every citation of the files being changed (`grep -rn` for `GOLDEN_RULES`, `ROADMAP`, `PERSONA.md`, `KNOWN_ISSUES`, "Feedback Log", section names) in `.claude/commands/*`, `.claude/hooks/*`, `.claude/settings.json`, `README.md`, `DEVELOPER_ONBOARDING.md`, `docs/claude/**`, memory files.
1. **Golden Rules.** Assign each rule to one cluster, move text **verbatim**. Write the index line per rule, then Opus checks each line against its full rule ("can a reader who sees only this line know when to open the file?"). Keep CODE ARCHITECTURE / DEBUGGING / AUDIT PROTOCOL / KEY LEARNINGS short sections in the index file (small, used often). Keep the "no Rule 27" note.
2. **CLAUDE_CONTEXT + ROADMAP.** Move update log and old summaries to `CLAUDE_CONTEXT_LOG.md`. Inspect ROADMAP lines 269–1105 first (I have only read 1–268) to find where the numbered open priorities live; move COMPLETE sections and the header day paragraphs to `ROADMAP_HISTORY.md`. Priority numbers (#17–#26) and "Priority #N" citations stay valid. README mirror rule unchanged: README mirrors the slim ROADMAP.
3. **PERSONA + KNOWN_ISSUES.** Split PERSONA at "## Feedback Log". Split the Day 132 KNOWN_ISSUES into open High/Medium (main) and the rest (living archive). The Low-Medium items that are next-session priorities (DRAL RS1, stale `data_audit_latest.json`) stay in the main file.
4. **Commands.** `sta-start.md`: read L1 only, state the L2 rule (open the cluster file when the task matches), drop the full-read list and the "read all six in full" wording. `sta-end.md`: Step 4 edits the right cluster file + the index line; Step 5b appends to `PERSONA_LOG.md`; Step 2 writes both known-issues files; Step 6 appends the old summary to `CLAUDE_CONTEXT_LOG.md`; Step 5 edits ROADMAP and moves finished items to `ROADMAP_HISTORY.md`. No new hook (user rule: no slow hooks; ask first).
5. **Memory.** Trim `MEMORY.md` (move the compacted History block to a `project_history_compacted.md` memory, keep the one-line index style). Update `project_docs_architecture_okf_comparison.md`: the 50-rule trigger fired, layered docs adopted Day 133.
6. **Verify and close** (below), then `/sta-end`.

## Verification (evidence, not claims — Golden Rule 6, 52)
- **Nothing lost:** script checks every rule number 1–69 (no 27) appears exactly once across cluster files, and each rule's text is byte-identical to the pre-change `GOLDEN_RULES.md` (`git show HEAD:…`). Same check for PERSONA log entries, ROADMAP sections, KNOWN_ISSUES headings (count in = count out).
- **Nothing breaks:** every citation found in Phase 0 still resolves (file exists, section exists). `bash .claude/hooks/test_three_pass_check.sh` and `run_all_checks.sh` still pass.
- **It is smaller:** re-measure L1 bytes; target ≤ 80 KB (~20k tokens) vs 391 KB now.
- **It still works (the real test):** in a fresh session run `/sta-start` and ask three probe questions that need L2/L3 — "what does Rule 69 say", "why did MR drop from PF 2.00 to 1.50", "what is open on Alpaca" — and confirm each is answered correctly within two hops from L1. If a probe fails, the index line for it is too vague: fix the line.
- Opus review of the finished index and the `sta-start` / `sta-end` text before the commit.

## Risks
- A vague index line makes me skip a rule I needed (Rule 69 nearly was). Mitigation: Opus line-by-line check + probe questions + a "read the cluster file for the area" map in CLAUDE_CONTEXT.
- `sta-end` gets more steps (several files to edit). Mitigation: write the exact paths into the command; `/sta-end` Step 0 checks all L3 files were appended.
- Stale citations by line number (ROADMAP:269 etc.) in older docs. Mitigation: Phase 0 grep; fix or leave a pointer line at the old location.
- Scope creep: no rewording of rules, no deleting content, no code. Rewriting is a separate decision.

## Files touched
`docs/claude/CLAUDE_CONTEXT.md`, `docs/claude/stable/{GOLDEN_RULES,PERSONA,ROADMAP}.md`, `docs/claude/versioned/KNOWN_ISSUES_DAY133.md` (new, slim), new `docs/claude/stable/rules/*.md`, `docs/claude/stable/archive/*.md`, `.claude/commands/{sta-start,sta-end}.md`, memory `MEMORY.md` + 2 memory files. Plan copy to `docs/claude/design/LAYERED_CONTEXT_PLAN_DAY133.md` with the Opus review section.

---

## Opus review (Day 133)

**Verdict: GO WITH CHANGES.** Docs-only; no hook or script reads these docs by heading or path (checked: `settings.json`, `three_pass_check.sh`, `verdict_parity.sh`, `run_all_checks.sh`, status board). The three main assumptions in v1 were wrong and are replaced by the amendments below. **The amendments override any conflicting line above.**

### Amendments applied (v2)
1. **ROADMAP open priorities** sit in the table at `ROADMAP.md:364-395` labelled HISTORICAL (rows 1-28, includes #27 Alpaca and #28). Triage row by row into a new "Open priorities" heading; closed rows go to history; keep one pointer line "closed priority numbers live in `history/ROADMAP_HISTORY.md`". Code comments cite closed rows (`App.jsx:1579` #9, `live_signals.py:227` #12, `backtest_holistic.py:103` Rule 20, `mean_reversion.py:151`): **never edit code**, resolve through the pointer line (a code edit would trip the three-pass hook).
2. **ROADMAP lines 590-1105** (PLANNED / RESEARCH / DEFERRED / KEY INSIGHTS / RESEARCH COMPLETED / UPDATE LOG / IBKR Screener, ~26.8 KB, stale e.g. TradingView chart) all go to history, with a pointer of 1 KB or less. Split by named heading, not position (the IBKR section sits after the UPDATE LOG).
3. **Session protocol has more copies (Rule 59):** `CLAUDE_CONTEXT.md:39-56` and `:70-88`, Rules 17 and 34, `PERSONA.md:6,104`, `MEMORY.md:4`, `feedback_session_start_protocol.md`. CLAUDE_CONTEXT protocol sections shrink to a two-line pointer to the commands. Rules 17 and 34 get a dated "Day 133:" note (house pattern, as Rule 64), not a reword. PERSONA header lines and both memory files are updated (added to Phase 5).
4. **Priorities appear 3-4 times.** CLAUDE_CONTEXT priorities become an ordered list of one-line references (ROADMAP #N, a KI heading). The "1-19, no plan written" list is Known Issues content and leaves CLAUDE_CONTEXT. Fix the stale `KNOWN_ISSUES_DAY131` pointer.
5. **KNOWN_ISSUES does not split by section.** Classify each `###` heading by severity tag and by strikethrough/RESOLVED. Open items hide under "Changes from Day 130/129" (DRAL, lines 20, 23, 38-44) and under "## New open issues (Day 129)" (the three Alpaca Mediums, lines 367-376). Any item cited by an open ROADMAP row or a CLAUDE_CONTEXT priority stays in the main file. Define: "Low-Medium" does NOT count as Medium+ for `/sta-start` Step 3 (stated in the file header).
6. **Rule 69:** the MNST ledger loss (KI:194) and VIX sizing (KI:199) look moot since Day 113. Carry them word for word with an "unverified since Day X" tag. No severity changes in this commit.
7. **KNOWN_ISSUES_DAY133.md is created once**, by this session's `/sta-end` Step 2 under the new rules (not mid-session), followed by the in/out count check.
8. **README mirror rule:** a structure-only move does not change README (`README.md:1455-1611` has its own stale roadmap; leave it, log it). Amend the sta-end rule to "README mirrors open priorities". Update `DEVELOPER_ONBOARDING.md:181-182` (rules' "why" now in `rules/`; "what's shipped" in history). Both files added to "Files touched".
9. **Rule boundaries:** a rule block runs from `^N\. ` to the line before the next `^M\. ` or `^---` (rules 33 and 41 are multi-line; separators differ). **There are 68 rules (1-69 minus 27)**; the header says 69. The index carries an explicit line: "27: no rule; 'Rule 27' in the Day 91 history means Rule 29".
10. **Rules 1-15 stay word for word in `GOLDEN_RULES.md`** (1 KB, already one-liners); no cluster, no duplicate index line.
11. **"Always" list, full text in `GOLDEN_RULES.md` only (not also in a cluster): 6, 13, 52, 55, 59, 62, 69** (~7.4 KB).
12. **Clusters (7, replaces the 8):** process: 17, 24, 32, 34, 41, 49, 50, 64 · claims-verification: 26, 37, 42, 47, 48, 53 · backtest-honesty: 16, 18, 20, 45, 56, 60 · engine-parity: 19, 21, 29, 35 · data-providers: 22, 25, 36, 40, 46, 58, 61, 65, 67 · cache-time-audit: 23, 28, 31, 33, 39, 43, 66, 68 · display-consumers: 30, 38, 44, 51, 54, 57, 63. Rules that span areas (39, 60, 63) have one home; their index line lists several triggers, no copied text.
13. **Index line = number + short title + trigger words** (files, areas, e.g. "providers/*, breaker, HTTP 400/404/429"), not a restatement. A fast check at `/sta-end` (not a hook): the numbers in the index equal the numbers in `rules/*.md`, each exactly once.
14. **L1 target restated: ≤ 85 KB / ~22k tokens** (the old "≤ 80 KB" was optimistic; measured ~78-85 KB). Reached only with changes 2 and 4. ENGINEER's "This session (Days 127-129)" table and Feedback Log (`ENGINEER.md:90-116`, `162-end`, 6.1 KB) are history: move them to `history/ENGINEER_LOG.md` (same split as PERSONA).
15. **sta-end check goes in a new step just before the commit step**, not Step 0 (Step 0 runs before anything is appended). Step 5 updates the slim ROADMAP version line on every version bump (version drift already happened, `ROADMAP.md:93,96`).
16. **Rollback:** each command edit goes in its own phase's commit (not all in Phase 4), so reverting one phase leaves the commands consistent. Memory edits are not in git: the old `MEMORY.md` text is saved into `docs/claude/design/` before trimming.
17. **Phase 0 grep scope includes code comments and memory files** (`~/.claude/projects/.../memory/*.md`).
18. **Folder name:** `docs/claude/history/` (not `stable/archive/`, which means "older than 15 days, ignore" in `sta-end` Step 8). History files are append-only by "## Day N" sections. `KNOWN_ISSUES_LOW_AND_RESOLVED.md` keeps the current Low/Info list on top, then per-day sections, so the snapshot history survives. Update the "Last Updated" header (Rule 14) on every `stable/` file touched.
19. **Fourth probe question added:** "what was ROADMAP priority #12?" (tests the code-comment citation path).

### Verified fine (reviewer)
No hook/script parses these docs; `three_pass_check.sh` ignores `.md`, so no stamp is needed; rule numbers unchanged so every "Golden Rule N" citation still resolves; PERSONA splits cleanly at `PERSONA.md:108` (core ~10 KB); the CLAUDE_CONTEXT update log (line 229 to end, ~28 KB) is a clean cut; old KNOWN_ISSUES day files are not touched; no new hook (matches the no-slow-hooks memory). One break this plan did not cause: `.claude/commands/watchlist-report.md:53` cites a PERSONA phrase ("overfitting disguised") that no longer exists. Logged, not fixed here.
