# STA Holistic Audit — Fable 5, Day 82 (post paper-trading-engine build)

> **Purpose:** User-requested "core Fable audit" — read-only holistic review of goal fidelity, progress reality, process bloat ("too many rules will spoil"), codebase declutter, and add/remove/keep recommendations. Distinct from the Day 78 Fable audit (which was about backtest methodology) — this one is about the project's own scaffolding and hygiene.
> **Method:** Fable 5 model, general-purpose agent, read-only (no files modified). Read README, CLAUDE_CONTEXT, GOLDEN_RULES, ROADMAP in full; skimmed design/versioned/status docs; read persistent memory files; explored backend/frontend structure; checked git history and tracked-file composition.
> **Status:** Findings delivered. Action items not yet triaged/applied — see conversation for what the user chose to act on.

---

## A. Goal Fidelity

**Stated purpose** (`README.md`): a data-driven swing-trade recommendation engine — Minervini/O'Neil-inspired, BUY/HOLD/AVOID verdicts, trade setups with R:R. The Day 27→44 pivot ("system is a FILTER, not a RANKER"; score-to-return correlation 0.011) was an honest, evidence-driven narrowing of the premise, not drift.

**Scope creep is real, but it's lateral, and it's currently in remission.** Days 58–77 accumulated a wide ring of features whose own documentation says they don't affect the verdict: Context tab (10 macro indicators, "PRE-FLIGHT ONLY — does not modify verdicts"), Sectors tab, Value tab ("zero impact on swing verdict"), Price Structure Card ("zero impact on verdict/scoring"), Canadian scanning, Nirmal integration, IBKR pipeline research, a second breakout engine. The discipline of keeping everything out of the verdict path is genuinely good engineering — but it's also the tell: for ~20 sessions the project mostly built things that, by its own labels, don't change any decision, while the central question ("is there an edge?") sat unresolved.

Days 78–81 are a sharp, correct re-convergence: the Fable remediation destroyed the inflated backtest numbers, froze the config, and built an automated zero-selection-bias paper-trading engine. **The current build is squarely in service of the original goal.** The `live_mode` DRY refactor (Golden Rule 21) is the single best engineering decision in the recent history — the live test literally replays the backtested exit function, so the paper trades will actually confirm or refute the backtest rather than a cousin of it.

**Verdict: drifted mid-life, currently on-goal.** The risk is not past drift but future drift: Day 81 already shows the pattern of "build things while waiting for trades" (breakout badges, `/breakout-watch` skill — nice, but decoration relative to the ledger).

---

## B. Progress Reality-Check

**Honest state: STA has zero validated edge, and its internal docs say so almost exactly.** This is rare and to the project's credit.

- Momentum (Config C): PF 1.40 on the survivorship-free 400-ticker sample, p=0.094 — not significant.
- MR (liquidity-restricted, the one allowed re-test): PF 1.16, p=0.064 — not significant, 78% fixed-risk drawdown.
- Live record after 81 days: **0 closed trades, 2 pending MR signals (GOOGL, ABBV), 0 momentum signals on the first run.**

The internal self-assessment (ROADMAP, KNOWN_ISSUES, memory files) is accurate, even slightly conservative. Two places are **optimistic relative to that**:

1. **`README.md` is stale and promotional.** "Institutional-grade," "quantified edge," a "92.3% quality score," and the Backtest Validation table still headlines PF 1.61/p=0.002 (Day 55 numbers) in the Assessment Methodology section — the survivorship caveat only appears if you read down to "Current Priorities (Day 80)." Header says "Last Updated: Day 65." If anyone but the owner ever reads this repo, the README materially oversells the validated state relative to what `SURVIVORSHIP_FREE_BACKTEST_DAY79.md` says.

2. **Nobody has computed time-to-50-trades.** The pre-registration bar is ≥50 trades *per system*. First live run produced 0 momentum signals. The survivorship-free backtest generated 114 momentum trades over ~5 years across 400 tickers — the live funnel (TradingView `best` scan → categorical assessment → R:R) is narrower still. If momentum fires ~0–2×/week, momentum confirmation is plausibly **6–12+ months away**, and no doc acknowledges this. MR (3,210 trades/5yr in backtest) will fill much faster. This asymmetry should be stated explicitly, because it changes what "let it accumulate" means in practice.

One genuinely good artifact worth naming: `PAPER_TRADING_PREREGISTRATION.md` §10 declares pass/fail thresholds in advance (Confirmed ≥1.2 PF, Modest 1.05–1.2, Broken <0.9) and pre-empts losing-streak panic. That is the correct methodology, executed properly.

**⚠️ One substantive integrity gap found:** the pre-registration's §9 freezes the MR entry as "price > $5 AND avg volume > 500K" — but Day 81 changed the live detector (`backend/mean_reversion.py`) to price>$10 + $25M ADV to match the re-tested gate. That change is legitimate and well-reasoned, **but the pre-registration was never amended** — its change log ends at Day 78, and the doc's own rule says any change "requires a new pre-registration entry." The yardstick the paper trades will be judged against currently misdescribes the running MR config. This needs a change-log entry (not a config change — the config is right; the paper is wrong).

---

## C. Process Bloat — "Too Many Rules Will Spoil"

Short answer: **the scaffolding is roughly 2× what one person needs, and the excess is provably failing under its own weight** — the very latest sessions violated the close protocol while the docs celebrate it.

### Load-bearing (keep — each has a receipt)

| Rule / Protocol | Incident it earned |
|---|---|
| Rule 13 (exhaustive verification) | Day 50: 92.8% spot-check → 21% exhaustive |
| **Rule 18 (freeze + pre-register)** | The reused-OOS finding; this is the most valuable rule in the file |
| Rule 19 (grid-test parity) | Found a real verdict bug (7.08% mismatch) that 5 hand vectors missed for years |
| Rules 20, 21 | Codify genuinely non-obvious methodological judgments made this month |
| Architecture rules 5–6 (zero≠null, no fake fallbacks) | Day 53/54 real bugs (VIX=20, F&G=50 silent lies) |
| Rule 16 (equal weights) | Grounded in DeMiguel et al. + own sample-size reality |
| `MASTER_AUDIT_FRAMEWORK.md`'s 3-layer core idea | Day 68: docs-match-code passed while logic was wrong |

### Cargo-culted / redundant (specific)

1. **Session-start is encoded four times**: Golden Rule 1 ("read PROJECT_STATUS first"), Rule 17 ("read CLAUDE_CONTEXT first" — which *contradicts* Rule 1's ordering), `memory/feedback_session_start_protocol.md`, and `.claude/commands/sta-start.md`. Four layers exist because each prior layer failed to be followed — the fix each time was another layer. The `/sta-start` skill makes Rules 1, 17, and both memory feedback files redundant; delete the other three encodings.
2. **The header says "20 Golden Rules"; there are 21.** The rules file can't keep its own count. Small, but it's the canary.
3. **Rules 2, 3, 6, 7, 9, 11, 12 are generic LLM hygiene**, not project knowledge ("read before modifying," "never hallucinate," "think through"). Rule 9 ("generate files ONE AT A TIME — wait for confirmation") is actively ignored by every recent session and by the close protocol itself (which mandates creating 3+ files in one pass). These belong in a 3-line preamble, not numbered rules.
4. **Day-numbered doc rotation is git, reimplemented by hand.** 62 archived versioned files + 67 archived status files + a 351KB `docs_claude_full_backup.zip` *tracked inside git* (`docs/claude/backup_pre_cleanup_day68/`). A single living `KNOWN_ISSUES.md` and `STATUS.md` with git history would provide everything the rotation does, minus STEP 7 of the close protocol and the archive folders. Meanwhile `KNOWN_ISSUES_DAY81.md` carries ~20 "Info" entries that aren't issues — it has become a third roadmap.
5. **"What was done" is recorded in five places**: ROADMAP "COMPLETE" sections (~600 of its 814 lines are history), ROADMAP update log, CLAUDE_CONTEXT update log, daily status files, and git commits. One narrative log (git + a short status) suffices.
6. **The process is currently being violated, which proves it's oversized.** The two most recent sessions (Jul 11–12: breakout Phase 0, Phases 2–3) updated ROADMAP and the plan doc but: `CLAUDE_CONTEXT.md` priorities #4–5 still list those phases as *todo*; `KNOWN_ISSUES_DAY81.md` still says "Config D/E Backtest Not Yet Run"; no new status file; `MEMORY.md` still says "Phases 0, 2-3 unblocked, not started" and cites Backend v2.33 (actual: v2.38). **The core promise — "read 4 files and know the state" — is false right now.** An 8-step mandatory close protocol that gets skipped the same week a skill was built to enforce it is not load-bearing; it's aspirational.
7. **The "Feature Freeze" is doublethink.** Declared Day 64 as "bug fixes only until paper trades logged." Since then: MR engine + card, VIX sizing, Value Tab, Price Structure Card, N1/N2, breakout engine, batch endpoint, scan badges, a skill, and an entire paper-trading subsystem — each individually justified via gating tables and user approvals. The freeze that actually matters (Config C verdict/exit thresholds) is real and enforced by the pre-registration. The *feature* freeze is a fiction maintained in prose. Rename it to what it is — **verdict-config freeze** — and stop apologizing for building peripheral things.

Per-plan gating tables (e.g. `BREAKOUT_ENHANCEMENT_PLAN.md`): genuinely useful *for the executing LLM* — they encode sequencing a fresh session can't infer. Keep the pattern, it earned its place (Phase 0's pre-committed interpretation criteria prevented narrative-fitting the zero-trade result).

---

## D. Codebase Declutter — Concrete List

**Critical (fix first, both are one-command problems):**
1. **`frontend/node_modules` is tracked in git: 40,801 of 41,154 tracked files (99.1% of the repo), pack size ~101 MB.** Day 79 "repo hygiene" untracked `backend/venv` but missed this. `git rm -r --cached frontend/node_modules` + `.gitignore` entry.
2. **`backend/providers/alphavantage_provider.py` is UNTRACKED** — the primary growth-metrics provider (FMP's replacement, wired into production since Day 62-ish) exists only on local disk. One `git clean -fd` or disk failure destroys a production dependency. Meanwhile the *dead* `fmp_provider.py` is tracked. Track the live one; delete the dead one.
3. **`backend/validation_results/paper_trading_ledger.db` is untracked with no backup.** This file is about to become the most valuable artifact in the project — months of unrepeatable live signals (the docs themselves note missed days can't be backfilled). It needs at minimum a scheduled copy.

**Dead / orphaned code (tracked):**
4. `backend/validation/forward_tracker.py` + the three `/api/forward-test/*` routes in `backend.py` (lines ~2153–2260): **confirmed orphaned.** The Forward Test tab uses localStorage (`frontend/src/utils/forwardTesting.js`); the new engine uses `paper_trading/ledger.py`. Three trade-tracking systems exist; this Day 15 one has zero callers. Remove routes + file.
5. `frontend/src/App_day4.jsx`, `App_day11.jsx`, `App_day23.jsx`, `services/api_day4.js`, `api_day11.js` — 2,077 lines of tracked snapshot files inside `src/`. Git history already preserves them. Delete.
6. Root `backend/` one-shot scripts (tracked, ~3,900 lines): `comprehensive_test.py`, `comprehensive_test_day29.py`, `test_categorical_30stocks.py`, `test_categorical_comprehensive.py`, `test_3layer_validation.py`, `test_indicator_coherence.py`, `test_scan_market.py`, `test_4h_data.py`, `validation_week4.py`, `tradingview_comparison.py`, `debug_defeatbeta.py`, `diagnose_backend.py`, `diagnose_yfinance_reliability.py`. Delete or move to a `backend/scripts_archive/`.
7. Untracked scratch in `backend/` (~25 files): six `scan_test_results_*.json`, eight `test_results_*.json`, two `validation_report_*.json`, three `backtest_*results*.csv`, `coherence_test_results_*.json`, `backend.log` (130KB), an empty root `cache.db` (real one is `backend/data/cache.db`), `Scanner Parameters Extraction for Perp.md`. Delete; add `*.log`, `*_results*.json` patterns to `.gitignore`.
8. Root clutter: `docs_claude_day24.zip`, `Files_Archives/` (gitignored but present), the tracked `docs_claude_full_backup.zip`. Delete — git is the backup.
9. Uncommitted deletion of `PROJECT_INSTRUCTIONS.md` sitting in the working tree — commit it or restore it.

**Not dead (checked, keep):**
- `frontend/src/utils/scoringEngine.js` — mislabeled "legacy" but `App.jsx:342` still uses `calculateScore()` as the data-extraction backbone feeding the categorical layer. Keep; consider renaming its docstring.
- **`pattern_detection.py` vs `breakout_detection.py`: complementary, not redundant — but the second one's value just shrank.** `pattern_detection.py` (3-status) is inside the frozen, backtested verdict path. `breakout_detection.py` (8-state) is an isolated, informational, never-backtested human-in-the-loop layer that only feeds badges and `/breakout-watch`. The Day 81 Config D finding (confirmed breakouts = zero backtested trades; the edge lives in anticipatory entries) partially undercuts the 8-state engine's premise, since its most "actionable" states are breakout-confirmation states. Don't retire it — it's cheap, isolated, and just shipped — but freeze further investment in it, and never let it near the verdict.

---

## E. What's Missing

The roadmap's #1 ("let paper trading accumulate, nothing to build") is **correct**. Three absences matter more than anything queued behind it:

1. **A dead-man switch on the launchd job.** A missed run permanently loses that day's entry signals (documented, unfixable by design). Nothing currently notifies anyone if the laptop was asleep at 16:30 CT for two weeks. Cheapest fix: make `/sta-start` (and/or a weekly check) surface `daily_job.py --report` including the last `job_runs` date, with a loud warning if >1 trading day old. This is the highest-value 20 lines the project could add.
2. **Ledger backup** (see D.3). The entire project thesis now lives in one un-backed-up SQLite file.
3. **A time-to-50-trades estimate per system** (see B). If the momentum funnel's expected rate makes confirmation a year out, the user should decide *now* whether that's acceptable, rather than discover it in October. This is analysis, not code — one session, freeze-compatible by any definition.

Explicitly *not* missing: more backtests, more features, more audit types. Also worth noting the pending fundamentals-mitigation decision (40% disagreement) is correctly ranked #2 — but recognize the paper trade *is* the live-fundamentals test; the decision mainly affects how backtest-vs-live comparisons will be interpreted, not the validity of the live record itself.

---

## F. Recommendations

### ADD
1. **Dead-man monitoring for the paper-trading job** — surface last `job_runs` date in `/sta-start`; warn if stale (E.1).
2. **Automated backup of `paper_trading_ledger.db`** — even a daily copy into a tracked/synced location.
3. **Amend `PAPER_TRADING_PREREGISTRATION.md`** — change-log entry for the Day 81 MR liquidity gate (§9 currently misdescribes the running config, violating the doc's own amendment rule). Documentation fix, not a config change.
4. **Time-to-50-trades estimate** for momentum and MR separately, written into CLAUDE_CONTEXT priorities.
5. **One README paragraph at the top** stating current honest status (PF 1.40/1.16, unconfirmed, paper trading in progress) and demoting the PF 1.61 table to history.

### REMOVE / DECLUTTER
1. `git rm -r --cached frontend/node_modules` + gitignore (99% of tracked files).
2. Track `alphavantage_provider.py`; delete `fmp_provider.py`.
3. Delete: `forward_tracker.py` + 3 orphaned routes; 5 `*_day*.jsx/.js` snapshots in `frontend/src`; ~13 one-shot root test scripts; ~25 untracked scratch artifacts; both docs zips; `Files_Archives/`.
4. **Consolidate the process layer:** collapse Golden Rules to the ~10 with incident receipts (13, 15, 16, 18–21, arch rules 5–7, exhaustive-verification) plus a short generic-hygiene preamble; fix the "20 rules" header; delete Rules 1/17 + both session-start memory files in favor of `/sta-start` alone; replace day-numbered KNOWN_ISSUES/STATUS rotation with single living files (git is the archive); strip ROADMAP's ~600 lines of completed history into a linked archive file; purge the ~20 "Info" non-issues from KNOWN_ISSUES.
5. **Rename "Feature Freeze" to "Verdict-Config Freeze"** — describe reality, keep the part that matters.
6. **Reconcile the stale trio now:** CLAUDE_CONTEXT priorities, KNOWN_ISSUES_DAY81, and MEMORY.md all contradict ROADMAP about breakout Phases 0/2–3 (done Jul 11–12). The 4-file startup read currently misleads.

### KEEP (verified load-bearing)
1. **`PAPER_TRADING_PREREGISTRATION.md` and Golden Rule 18** — correctly untouchable, and the pre-declared §10 pass/fail table is the best methodological artifact in the repo. Out of scope for change by design; endorsed.
2. **`backend/paper_trading/` architecture** — `live_mode` replay of the exact backtest exit logic, shared `scan_queries.py`, `metrics.py` reuse, idempotent `job_runs`. This is the right way to build a live counterpart; well-verified before wiring.
3. Golden Rules 19–21, architecture rules 5–7, exhaustive verification — each earned by a real bug.
4. Per-plan gating tables with pre-committed interpretation criteria (Config D's zero-trade result was accepted, not rationalized — the process worked exactly once where it mattered most).
5. `scoringEngine.js` (still the data backbone), `constants.py`, the providers package, both pattern engines (with the investment-freeze caveat on `breakout_detection.py`), `/sta-start`/`/sta-end`/`/breakout-watch` skills.
6. **The honesty culture.** The willingness to publish PF 1.61→1.40 and PF 1.26→0.99 against its own prior claims is the project's most valuable asset. The bloat is real, but it grew out of that honesty; trim the scaffolding, not the instinct.

**Bottom line:** STA is one good decision away from being exactly what it says it is — a frozen, honestly-measured system waiting on live evidence. The decision is to *actually wait*: fix the two git hygiene time-bombs, add the dead-man check, cut the process layer in half, and let the ledger fill.
