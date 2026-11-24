# Claude Memory - Swing Trade Analyzer

## FIRST THING: Read CLAUDE_CONTEXT.md
`docs/claude/CLAUDE_CONTEXT.md` first — 4-file startup checklist (GOLDEN_RULES → ROADMAP → STATUS → KNOWN_ISSUES). Don't stop after GOLDEN_RULES.md alone.
- [Session Start Protocol Rule](feedback_session_start_protocol.md) — skipping CLAUDE_CONTEXT.md causes missed reads (Day 76).
- [Session Start Summary Rule](feedback_session_start_summary.md) — if last session was context/no-work, also report last substantive session.

## Collaboration Style
- [Recommended-Option Judgment Calls](feedback_recommended_options_judgment_calls.md) — user picks "(Recommended)" AskUserQuestion options; bundle judgment calls.
- [Verify backlog spec before "simple"](feedback_verify_backlog_spec_before_simple.md) — check the design doc before calling an item simple; Golden Rule 24.
- [UI: Visible State Over Hidden](feedback_ui_visible_state_over_hidden.md) — show muted/neutral states, don't hide them.
- [Three Review Passes Per Fix](feedback_three_review_passes.md) (Day 94/103) — 3 *escalating* passes per fix, not 3 parallel checks. Golden Rule 41. **Day 126: enforced by a Stop hook + `/three-pass` (Golden Rule 64)** — run `/three-pass` before saying done.
- [Parallel Experiments Over Blocking Changes](feedback_parallel_experiments_over_blocking_changes.md) (Day 96) — a fix that resets a frozen system's progress should be offered as a parallel/separately-tracked variant, not a wait-vs-reset choice.
- [Live Status, Not Stale Doc](feedback_live_status_not_stale_doc.md) — paper-trading numbers come from `daily_job.py --report`, never a status doc.
- [Parallel Tool-Result Ordering](feedback_parallel_tool_result_ordering.md) (Day 104) — parallel tool results aren't guaranteed ordered; verify identity, not position. Golden Rule 42.
- [Cache Clear vs Frontend Refetch](feedback_cache_clear_vs_frontend_refetch.md) (Day 105) — a backend cache clear needs every dependent frontend refetch path audited too. Golden Rule 43.
- [Don't Oversimplify STA as Minervini](feedback_dont_oversimplify_sta_as_minervini.md) (Day 106) — STA is a multi-engine workbench; verify architecture claims against code, both directions.
- [Bring Independent Judgment, Not Just Execution](feedback_bring_independent_judgment_persona.md) (Day 109, ext. 110) — test the user's conclusions against PERSONA before building; disagree genuinely, and reverse genuinely when a counter-argument wins.
- [Verify a Claimed Edit Actually Happened](feedback_verify_claimed_edits.md) (Day 110) — "I updated X" is a checkable claim; reread the file before treating it as done. Golden Rule 52.
- [Check Callers Before Scoping a Fix](feedback_check_callers_before_scoping.md) (Day 111) — grep the real caller graph before calling a fix "low risk"; it may gate a live forward-test track. Golden Rule 54.
- [Architect Lens Before Rule Changes](feedback_architect_lens.md) (Day 122) — find every copy of a rule before changing it; trading-sound ≠ safe to ship. Golden Rule 59 + verdict parity hook.
- [MR Entry-Basis Correction](project_mr_entry_basis_correction.md) (Day 123) — MR PF 2.00 was scored at the entry-day close; at the open it's 1.50 (broad) / 1.07 (HUB-65). Docs + artifacts corrected Day 123 close; Golden Rule 60.
- [Plan + Fable/Opus Review + Engineering Standard](feedback_plan_review_engineering_standard.md) (Day 123) — every build step: reviewed plan first; no silent failures, logging, exceptions, perf, real data behind every UI element. **Ask before each Fable review run** (Day 126).
- [Decide, Don't Spin](feedback_decide_dont_spin.md) (Day 123) — give a plain, deterministic decision and act; don't end every research answer with another question.
- [Leveraged-ETF Trading Scope](feedback_leveraged_etf_trading_scope.md) (Day 120) — SOXL/GDXU/DRAL: Claude watches splits + explains stops/sizing; user owns rule-count, no fundamentals/holding-period/backtest nagging.
- [Simple English Always](feedback_simple_english.md) (Day 124) — explain in very simple English, short sentences, jargon last; Golden Rule 62.
- [Less Text, Less Decision Fatigue](feedback_less_text_decision_fatigue.md) (Day 125) — every element must change a decision; trader conventions labelled "not tested" over backtesting info cards; no in-app chart.
- [Facts, Not Verdicts](feedback_facts_not_verdicts.md) (Day 126) — user decides every trade; cards show numbers + "not tested" rules of thumb, no Strong/Weak or Yes/Mixed/No words.

## Critical Process Lessons
- **Exhaustive > spot-check** (Day 50): spot-check passed 92.8%, exhaustive testing found only 21% actually correct.
- **Session close discipline** (Day 33-49): API_CONTRACTS drifted 16 days once — follow the close protocol exactly, every time.
- **Audit = correctness, not just consistency** (Day 68/72): docs-matching-code isn't enough; logic + runtime behavior matter more. `docs/claude/stable/MASTER_AUDIT_FRAMEWORK.md`.
- **React falsy bug pattern** (Day 68): `{value && <div>}` renders "0" at value=0 — use `value != null && value > 0`.
- [docs/claude/ vs OKF spec](project_docs_architecture_okf_comparison.md) (Day 94): our memory system already matches Google's OKF; restructuring deferred until GOLDEN_RULES.md passes ~50 rules.

## Reference (architecture, engine status — safe to re-derive if stale)
- [Project Architecture](reference_project_architecture.md) — ports, data provider chain, Context tab engine map, TradingView gotchas, OptionsIQ, Trading Intelligence Hub.
- [Engine Validation Status](project_engine_validation_status.md) — canonical backtest numbers, engine phases, feature-freeze state.
- [Hub Audit Handoffs](reference_hub_audit_handoffs.md) — check both STA's repo-root `HANDOFF_*.md` files and the Hub's own `docs/handoffs/`; verify root causes independently.
- [TradingView Screener Doc](reference_tradingview_screener_doc.md) — pointer to `docs/claude/design/TRADINGVIEW_SCREENER_IMPLEMENTATION.md`.
- [Audit Coverage Ledger](reference_audit_coverage_ledger.md) (Day 111) — `AUDIT_COVERAGE_LEDGER.md` tracks last-reviewed date/depth per component; check before any future deep-dive review.

## Current State (Day 132, no STA code change; Day 131 — v4.70; two Medium engine bugs fixed (missing RSI no longer 50, missing SPY described honestly, still no BUY); MR-route note was wrong (Golden Rule 69); Data Source Audit Round 2 ~60%: next Alpaca in-session bar check, DRAL RS1 smoke-audit row, refresh data_audit_latest.json)
- [Analyze Page Redesign](project_analyze_page_redesign.md) — **COMPLETE Day 124**, trimmed Day 125, Day 126: simple S&R engine live, Technical Read + volume card are plain facts (no verdicts), ruler marks real 21/50/200-day averages, indicator table made true, split mechanism for SOXL.NE (`known_splits.json`, `split_adjust.py`). Optional follow-ups in ROADMAP #19; then engine bugs. Page checker: `ui-verify-checklist.js` (use `headless: 'shell'` if it hangs).
- **⛔ [Paper-trading program DISCONTINUED](project_paper_trading_engine.md)** (Day 113, 2026-09-12, user's explicit direction, not a finding): "I don't want to paper trade... I want to use Claude and STA as analysis engine and recommendation, I will take care of stuff myself." No IBKR execution (Priority #13 **declined**, not parked). No new signals on any track; every open position wound down by its own exit rules. **MR (broad) is the program's final result and the project's one positive edge** — but see [[project-mr-entry-basis-correction]]: the ledger's PF 2.00 priced trades at the entry-day CLOSE; re-run at the next OPEN (what a person can do) it is **PF 1.50, 63.5% WR, +0.70%/trade** (HUB-65: PF 1.07, ~break-even). Day 123. STA's role now: on-demand analysis/recommendation only — do not propose resuming forward-testing/paper-trading/automated-execution work unless the user raises it again. The Day-92 freeze that governed the roadmap is lifted; parked items are legitimately available again.
- **Days 116-118: the entire remaining Day-111 technical-audit backlog was cleared, all as informational reads, nothing gated.** OBV trend sign bug + a real unlogged partial-bar RVOL bug fixed (Day 116); Antonacci's absolute-momentum leg surfaced as a read, new Golden Rule 57 (Day 117); MTF Confluence's dead `strength` field + VCP's flat target both fixed, completing the S&R fix chain (Day 118). See [[project_day118_consolidated_close]] for full detail. [Technical Audit Day 111](project_technical_audit_day111.md)'s three below-standard gradings (S&R 2/10 fixed Day 112, MTF Confluence 3/10 and Pattern Detection's target 1.5/10 both fixed Day 118) are now all remediated.
- [Full Audit Plan](project_full_audit_plan_day107.md) (Day 107-108) — all 10 groups complete, ~15 bugs fixed (MTF fabricated-dates, Golden Rule 30 root-fix, `/api/health`), ~8 parked. Zero FWD-track overlap.
- [Trading Principles Comparison](project_trading_principles_comparison.md) / [Volume-Momentum Spike](project_volume_momentum_research_spike.md) — DONE, updated Day 117: 7 Matches, 2 Partial (Momentum/RS, Volume — both now have their missing piece shipped as an informational read, not gated; that's why they stay Partial, not to-dos).
- [SRPS Investigation](project_srps_investigation.md) (Day 103, ext. 105) — Gate 1 backtest FAILED; pivoted to a discretionary Sectors screener (shipped), later extended to Sub-Industry clusters.
- [Watchlist Report Skill](project_watchlist_report_skill.md) (Day 104-105) — Claude Code skill, not STA app code; catalyst report from a pasted IBKR watchlist.
- [STA Status Board](reference_sta_status_board.md) (Day 120) — status + artifact-map page, republish every /sta-end (Step 6b); MR is PF 1.50 at the open (2.00 was close-basis), Day 123.
- [Leveraged ETF Board](reference_leveraged_etf_board.md) (Day 120) — live IBKR page for SOXL/GDXU/DRAL with adopted rules; JS formulas must stay parity-checked vs STA Python.
- [User's Tickers in STA](reference_user_tickers_in_sta.md) (Day 126) — which STA symbol is the user's real fund (SOXL.NE, GDXU.TO, CDRs on .NE); short-history and no-history cases.
- [Data Provider Findings](reference_data_provider_findings.md) (Day 126) — tested coverage/limits per provider, Tradier usage + reverse-split bug, unused free keys (EODHD, Alpha Vantage), tab gaps.
- [Beginner Trading Starter Playbook](reference_beginner_playbook.md) (Day 120) — 8-tab light-theme page for the user's friend, shared by link; check before editing so the same URL updates.
- [How Stock Picking Works doc](reference_how_stock_picking_works_doc.md) — living Artifact explainer, built Day 100 — check before editing so the same URL updates.
- [IBKR Paper-Trading Execution Plan](project_ibkr_paper_execution_plan.md) (Day 97) — 4-phase plan, **explicitly parked** pending user research.
- [Questrade Flow Experiment](project_questrade_flow_experiment.md) (Day 102) — real-money ETF automation, **explicitly separate from STA**.
- [TVRemix AI Chart Copilot](project_tvremix_ai_copilot.md) (Day 109) — third-party tool, **explicitly separate from STA**; its overlay is unvalidated, don't trust it like STA's own signals.

## History (compacted)
- **Days 121–122** — Redesign Phase 0 + Phase 1 helpers (Day 121); Technical Read card signed off item-by-item, checks 5–8 kept in engine after the architect question (Golden Rule 59, PERSONA Architect's Lens, verdict parity hook). Volume: TwelveData = yfinance to the share; IBKR ≈ 46–65% (filtered trades) — never mix sources. See [[project_analyze_page_redesign]], [[feedback_architect_lens]].
- **Day 119** — User challenged the post-Day-118 backlog's shape (diminishing-returns audit
  items, no live gates left); agreed and re-scoped the Analyze Page Redesign as the one bounded
  real project remaining. Opus-planned re-verification of the Day 109 plan's §7/§8 against six
  sessions of drift found the 17 decisions hold but 9 corrections needed — most importantly two
  blocks of prescribed on-card copy that described bugs fixed since (pivot S&R, Day 112; Pattern
  Detection target, Day 112/118) and would have shipped as fabrications. Golden Rule 54
  caller-graph check re-run fresh post-freeze: still clean, now on parity/backtest-comparability
  grounds not forward-test grounds. Go/no-go: GO. Zero app code touched. See
  [[project_analyze_page_redesign]].
- **Days 116-118** (consolidated close, run Day 118) — OBV trend sign bug + a real unlogged
  partial-bar RVOL bug fixed, both Day 116 (3 commits, Opus-planned). Antonacci's
  absolute-momentum leg surfaced as an informational read Day 117, new Golden Rule 57 after
  catching a near-miss that would've silently added a 10th Simple Checklist criterion. MTF
  Confluence's dead `strength` field + VCP's flat target both fixed Day 118, completing the S&R
  fix chain deferred since Day 112. v4.61→v4.62. See [[project_day118_consolidated_close]].
- **Day 113** — User discontinued the entire paper-trading/forward-testing program: "I don't want to paper trade... I want to use Claude and STA as analysis engine and recommendation, I will take care of stuff myself." Confirmed scope (full stop, graceful wind-down, same pattern as Path B's Day-112 retirement) via one clarifying question before touching the live system. `daily_job.py` gained `PROGRAM_DISCONTINUED`; verified live (`--force` run: 0 new signals across all tracks, 2 positions closed normally). IBKR execution (Priority #13) closed as declined. MR (broad) stands as the program's one confirmed edge. Freeze lifted. See [[project_paper_trading_engine]].
- **Day 112** — Path B RETIRED (no live edge). S&R `_pivot_sr` nearest-level fix shipped (Golden Rule 53) + BUG-A (★ badge key format) + BUG-B (Price Structure deepest-not-nearest) + measured-move pattern targets (Cup & Handle / Flat Base). Config C backtest re-baselined PF 0.97 → 0.53 on corrected levels — the old number was partly a bug artifact; "PF 1.40" formally retired; pre-registered "trades rise" prediction wrong, logged (new Golden Rule 56). New Golden Rule 55 (scoped Opus-plan-then-Sonnet-implement). PERSONA synthesis: momentum failed every honesty test; MR (broad) is the one edge — deploy it (IBKR), don't polish cards. v4.60→v4.61. See [[project_paper_trading_engine]], [[feedback_bring_independent_judgment_persona]].
- **Day 111** — Longest session yet. Full technical audit (5 cards graded vs. real methodology, Golden Rule 53) + data-provenance map (5 findings, 2 fixed). Shipped MR Scanner (wired an unused Day-81 endpoint) and 2-phase Volume Confirmation+Direction on the Trade Setup card (Opus-planned both phases, new `meta.candle` API field). MR broad genuinely confirmed at 100 trades; Path B crossed 100 but failed the identical cluster stress-test — new Golden Rule 54 after discovering the S&R fix would reset Path B's count. v4.59→v4.60. See [[project_technical_audit_day111]], [[project_paper_trading_engine]], [[feedback_check_callers_before_scoping]].
- **Day 110** — Published an interactive mockup of the Day 109 redesign. Clustering check across all 4 tracks found HUB-65's cluster *underperformed* rather than inflated (opposite of the usual pattern). User pushed back and got the Regime hard-gate decision reversed to informational (see [[feedback_bring_independent_judgment_persona]]). New Golden Rule 52 after a claimed-edit near-miss (see [[feedback_verify_claimed_edits]]). Zero app code touched.
- **Day 109** — Analyze Page Redesign: 17 decisions via item-by-item Q&A (Golden Rule 49); user demanded independent persona pushback (2 surviving disagreements); Opus validation pass caught 4 corrections + resolved 4 items (Golden Rules 50-51), incl. a hardcoded-label bug live since Day 39. Design doc only. See [[project_analyze_page_redesign]].
- **Day 108** — Full 10-group system audit: 15 bugs fixed (MTF fabricated-dates CRITICAL; `fetchSectorRotation()` root-fixed, Golden Rule 47; `/api/health` hardcoded), 8 parked (VIX sizing never wired in, harmless, Golden Rule 48). Canadian ticker question resolved. v4.58→v4.59.
- **Day 107** — Deep-validated Path B data; fixed a cross-provider stock-split mismatch (Golden Rule 46). Built "STA vs. 100 Years of Trading Principles" Artifact (7/9 match); backtest spike on the 2 gaps found no edge (Golden Rule 45, SimFin universe drift). See [[project_trading_principles_comparison]].
- **Day 106** — Fixed Scan tab breakout-badge ambiguity (Golden Rule 44); built on-demand STA Verdict column; corrected an oversimplified "Minervini system" self-description (see [[feedback_dont_oversimplify_sta_as_minervini]]). v4.57→v4.58.
- **Day 105** — Fixed Sectors-tab staleness bug (Golden Rule 43); built Sub-Sector Pullback Screener; found screener R:R structurally disconnected from real resistance. v4.56→v4.57. See [[project_srps_investigation]].
- **Day 103-104** — SRPS investigated + failed its backtest, pivoted to a screener (Golden Rule 41). `/watchlist-report` skill built, surfaced a tool-ordering bug (Golden Rule 42). See [[project_watchlist_report_skill]].
- **Day 101-102** — Sub-Industry Watch built natively (21 proxy ETFs, Golden Rule 40 tz-fix); Questrade Flow experiment scoped separately.
- **Day 99-100** — Partial-bar ledger contamination found+fixed (20 trades repaired, Golden Rule 39); no sector-correlation awareness in either entry gate logged as a Known Issue. See [[project_paper_trading_engine]].
- **Day 94** — First full README Coherence Audit (~50 findings fixed). New `DEVELOPER_ONBOARDING.md`. Origin of Golden Rule 32 (3 review passes) — see [[feedback_three_review_passes]].
- **Day 92-93** — Sectors/Context tab audit: color/label contradiction bug class fixed; new macro-alignment connection. Independent of the freeze.
- **Day 91** — Session 28 audit: 4 bugs fixed (Scan label, Sectors false claims, Context date-alignment, exit-rule integrity).
- **Day 88-90** — Paper trading ledger surfaced in UI; MR universe widened 54→~150; Force Run safety confirmed.
- **Day 87** — Complete feature freeze declared. Breakout Plan, N4 Market Phase, Price Structure Phase 2 shipped. v4.44→v4.45.
- **Day 85-86** — Notion Personalized Screener: 76-ticker Scan tab watchlist built + user-tested.
- **Day 78-82 (Fable Remediation)** — All 5 phases done (Momentum PF 1.40/MR PF 1.16); Breakout Plan done; hygiene audit (~20 dead files cleaned); UI Code Quality Fix Plan done, BE v2.36→v2.39.
- **Day 73** — Nirmal vs STA validation: 378 calls, style mismatch not system failure.
- [QuantMomentum Terminal Page](reference_quantmomentum_terminal.md) (Day 126) — user's pasted HTML dashboard saved verbatim as quantmomentum_terminal.html; pull back on request
- [P&L Dashboard (IBKR + Questrade)](reference_pl_dashboard.md) (Day 131) — personal, outside STA; script in ~/projects/pl-dashboard, page on claude.ai; user says "refresh the dashboard", follow REFRESH.md; private data.
- [Pending Coherence Audit (Day 126)](project_pending_coherence_audit_day126.md) — user asked to run the Coherence Audit + Opus review later on the RRG/leaderboard/MR-card changes
- [No Slow Hooks](feedback_no_slow_hooks.md) (Day 127) — no per-edit/pre-commit hooks; only the end-of-work Stop gate; ask before any new hook.
- [Data Source Audit Round 2 (Day 129, ~60%)](project_data_source_audit_round2.md) — audit the data on all 117 tickers; done/next list, Twelve Data + Tradier findings; playbook research runs after.
- [Plan + Opus + Three-Pass, Hook-Enforced](feedback_plan_opus_threepass_hook.md) (Day 128) — every code change: plan mode -> Opus-reviewed plan file -> build -> /three-pass -> stamp `--plan`; trivial skips logged.
- [Answer the Question Asked](feedback_answer_the_question_asked.md) (Day 128) — lead with the narrow answer, then offer more; label measured vs inferred; re-check challenged claims.
- [Engineer Persona (ENGINEER.md)](feedback_engineer_persona.md) (Day 129) — surgical-developer lens + table of past misses; 3rd required read at /sta-start; extend its table every session.
- [Known Issues Are Claims](feedback_known_issues_are_claims.md) (Day 131) — read the named code + run one call before repeating a Known Issues line; Golden Rule 69.
