# Project Status — Day 107 (August 14, 2026)

## Version: v4.58 unchanged (Backend v2.46, Frontend v4.53) — no live app code touched

---

## What Happened Today

Entirely a research/investigation session — no changes to `backend.py`, any live API route, or any frontend component. Everything below is either backtest-only tooling, docs, or external Artifacts.

### 1. Deep validation of Momentum Path B forward-test data

At session start, the user pasted live Forward Test tab data for Path B and asked whether the entry/exit prices matched the displayed result %. Verified directly against the ledger DB:
- Confirmed the % shown is net of a modeled $3 round-trip transaction cost (assumes a flat 100-share fill) — matches to the cent on every trade checked, not a bug.
- Cross-checked live numbers against `daily_job.py --report` — matched the pasted UI exactly.
- Found a real, worth-watching pattern: Path B's 30 closed trades show an outsized average entry-fill "slippage" (−1.10%) vs. the 92 still-open positions (−0.03%) — traced to a few large real overnight gaps (DDOG −19.68%, confirmed genuine via a 3x volume spike, not a data bug) resolving as fast wins. Flagged as a possible partial driver of Path B's currently strong-looking numbers — not fixed, informational only, no gate touched.

### 2. `/watchlist-report` re-run on AI_Leveraged watchlist

Re-sourced live via IBKR MCP (per the skill's standing convention), updated the existing Artifact in place. Found and corrected a real cross-provider data bug mid-build: yfinance served ~4x-too-high prices for GDXU and SOXL — both funds had a genuine 3-for-1 forward split (2026-05-25) that yfinance hadn't adjusted for, while IBKR (via `include_corporate_actions=true`) had it right. Also self-caught and fixed a transcription error while manually copying IBKR JSON (accidentally duplicated one ticker's array under a second ticker's key) before it reached the report.

### 3. "STA vs. 100 Years of Trading Principles" comparison Artifact

Built at the user's request, following full Plan Mode: audited STA's actual code (9 categories: trend, momentum, mean reversion, volume, position sizing, stops, market regime, sentiment, sector rotation), gathered independent research from 3 different LLMs (Perplexity, ChatGPT, Gemini) on the same 9 categories, cross-checked all three against each other, then built a plain-language 2-column Artifact.

- **Code audit was three-pass verified per the user's explicit instruction** (Golden Rule 41 applied to a research audit, not just a code fix) — Pass 3 caught something Pass 1 missed: `App.jsx` independently hardcodes a *third*, stale copy of Fear & Greed threshold bands (old 60/35, pre-"Bug 0G") directly in the sentiment gauge's color logic — live and user-visible, different from both the correct bands actually driving the verdict and a second, unread stale copy already known to exist in the backend. New Known Issue, not fixed.
- **Cross-source research check paid off immediately**: Perplexity described the Moreira & Muir volatility-regime paper as "VIX-based sizing"; ChatGPT went back to the source and corrected it (the paper's actual mechanism is prior-month realized variance, not VIX); Gemini presented both as legitimate parallel formulations. Final artifact states this precisely.
- **Result**: 7 of 9 categories "Match" a classic trading principle, 1 "Partial" (momentum — STA has relative strength, missing Antonacci's absolute/dual-momentum half), 1 "Gap" (volume confirmation — the finding that started the whole thread).
- Published: `https://claude.ai/code/artifact/cc9d82c6-b961-4aec-aa37-e384ca512083`. Raw research preserved at `docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md`.

### 4. Backtest-only research spike — volume confirmation & dual momentum

User asked directly whether to fix the 1 gap + 1 partial. Given the standing forward-testing freeze, presented 3 options via `AskUserQuestion`; user chose a backtest-only research spike (zero live changes). Planned via full Plan Mode, built two new, purely-additive research configs in `backend/backtest/backtest_holistic.py`'s `check_entry_signals()`:
- **Config F** — Config C + entry-day volume ≥1.5× 50-day avg (reuses `pattern_detection.py`'s existing threshold, applied generally instead of pattern-specific).
- **Config G** — Config C + trailing-252d absolute return > 5% risk-free proxy (the literal Antonacci gap).

Both diff-verified as pure additions (zero `-` lines touching Config C's own logic). New standalone script `backend/backtest/research_spike_volume_momentum.py` — doesn't touch the existing frozen `backtest_survivorship_free.py`.

**Result** (400 tickers, seed=42, 2020-2025, single run per Golden Rule 20 — accepted as-is, not iterated):

| Metric | Config C | Config F (+volume) | Config G (+momentum) |
|---|---|---|---|
| Trades | 75 | 5 | 74 |
| Win rate | 45.33% | 40.0% | 45.95% |
| Profit Factor | 0.973 | 0.522 | 0.992 |
| Sharpe | -0.20 | -0.81 | -0.17 |

Neither shows a credible edge — Config F's 1.5x threshold is too strict as designed (cut trades 93%, n=5 is not evaluable either way); Config G ran clean but only excluded 1 of 75 trades (near-inert in practice, since Config C's existing pipeline already mostly selects positive-absolute-return stocks). Both stay parked on Priority #11.

**Real side-finding, not a bug**: Config C's own baseline in today's run (PF 0.97) didn't match the documented canonical number (PF 1.40, Day 79) — investigated before trusting anything else. Root cause: SimFin's ticker coverage shrank from 3,788 (Day 79) to 3,745 (today), so the same fixed seed (42) now draws a genuinely different 400-ticker sample. New Golden Rule.

---

## Files Changed

| File | Change |
|---|---|
| `backend/backtest/backtest_holistic.py` | Added Config F/G (purely additive research configs) + 3 new module constants. No changes to Config A/B/C/D/E's own logic. |
| `backend/backtest/research_spike_volume_momentum.py` | New standalone research script (backtest-only). |
| `docs/research/TRADING_PRINCIPLES_100YR_RESEARCH.md` | New — raw research from 3 LLMs + cross-source synthesis. |
| `docs/claude/stable/GOLDEN_RULES.md` | 2 new rules (SimFin universe drift, corporate-actions cross-provider check). |
| `docs/claude/stable/PERSONA.md` | New Day 107 Feedback Log entry. |
| `docs/claude/stable/ROADMAP.md` | Priority #11 updated with the spike's result as new supporting context; new Known Issue cross-referenced. |

No `backend.py`, no frontend component, no API route touched. No version bump — nothing live changed.

---

## All Gates Status

Unchanged for the 4 live forward-test tracks — nothing this session touched any entry/exit gate, and Config F/G are backtest-research-only, never wired into `live_signals.py`/`mean_reversion.py`/the live paper-trading engine. Numbers not re-pulled this session (deep dive was on Path B's existing data, not fresh counts). Last live-pulled counts: Path A 35/24 closed, Path B 92/30 closed, MR broad 7/84 closed (closest to the 100-trade bar), MR HUB-65 3/29 closed (2026-08-13 check).

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS.** MR (broad) was at 84/100 as of the last check; plausibly clears its bar within a few sessions.
2. **Volume confirmation — needs a redesign, not just the freeze to lift.** Today's spike showed the straightforward "1.5x on entry day" implementation is too strict to evaluate (93% trade reduction). If revisited, the next step is a genuinely different filter shape (lower ratio, or a secondary signal instead of a hard gate), pre-committed before any new backtest — not a retune of today's threshold.
3. **Dual/absolute momentum — cheap, low-priority, near-inert.** Tested clean but only excludes ~1% of Config C's trades in practice. Fine to add whenever the freeze lifts; won't move results much either way.
4. **New Known Issue, not yet fixed**: App.jsx's Fear & Greed gauge uses a third, stale copy of the sentiment threshold bands, different from both the live verdict logic and the backend's own (already-known) stale copy. Real, live, user-visible.
5. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, the 3-way R:R minimum inconsistency, `/ibkr-scan`, Session 28 audit remainder, SRPS R:R structural gap.
