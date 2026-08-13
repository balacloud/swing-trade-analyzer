# Project Status — Day 100 (July 28, 2026)

## Version: v4.54 (unchanged — no app code touched this session)

---

## What Happened Today

A monitoring, education, and documentation session — no application code changed. Continuation of Day 99's work after that session closed.

### 1. Monitored the corrected forward-testing ledger
User ran a real Force Run mid-session (10:31 EDT, during market hours) — the first live use of Day 99's partial-bar fix outside of testing. Verified it worked correctly: the one trade it closed (MR's NVO) resolved against the prior day's real close, not the still-forming intraday bar, exactly as designed.

### 2. Found and verified a real structural gap: no regime/sector awareness in either automated track
Prompted by a live example (a same-day semis/AI-supply-chain sector selloff — MU, AMD, MRVL, etc. all down together). Verified directly in code, not from memory:
- `detect_mr_signal()` (MR's entry gate, both broad and HUB-65) has exactly 4 conditions — RSI(2), price vs. its own 200-day SMA, price floor, dollar-volume floor. No VIX check, no sector check, no correlation awareness at all.
- Momentum's verdict engine has *some* regime awareness (VIX + SPY vs. its 200-day average), but nothing sector-specific either.
- Live-checked a 10-ticker semis cluster: 6 were already pending signals in the ledger from the same shock (concentrated in one theme, one week), and 4 more would fire once the day's bar closed.
- Traced this to a real, honest gap: the project's own Day 78 block-bootstrap docstring already names "correlated tickers entering around the same time" as a known risk to the *statistics* — but that mitigation never reached the entry gate itself, and the raw trade count toward the 100-trade bar doesn't discount for it either. Ties directly to the Day 93 clustering finding (same mechanism, opposite direction — a selloff instead of a rally).
- Confirmed this is a deliberate, understood design split, not an oversight: the Sectors/Context tabs and the user's own manual judgment are the intended place for that awareness (confirmed the user still actively uses them for discretionary calls) — the automated engine is deliberately built with "zero human filtering," which is the whole point of it being a clean, selection-bias-free test.

### 3. Built and published a living reference doc: "How the Stock Picker Thinks"
New file: `docs/claude/design/HOW_STOCK_PICKING_WORKS.html` — a visual, plain-language flowchart of the Simple Checklist (9 binary criteria) and Full Analysis (4-category verdict cascade) paths, verified against the actual current code (`simplifiedScoring.js`, `categoricalAssessment.js`) rather than summarized from memory. Published as a Claude Artifact, explicitly intended as a persistent, incrementally-updated doc (not a one-off) — the user asked to keep building on it as real questions come up.

Built out across the session with three additions:
- The original two-path comparison + a worked example (Regime = Uptrend), including the exact 7-rule verdict cascade from `determineVerdict()`.
- A "Test Scenarios" log (Q&A format, most recent first) — first entry: whether a good stock in a bad regime would ever get bought on the theory it'll "bounce back" (no, for both paths, and the core tool's philosophy doesn't do dip-buying at all — quoted the code's own `"deeply oversold — avoid catching falling knives"` line as evidence).
- A "Scanners" section covering all 6 rule-based TradingView scan presets (with their real, verified filter criteria) and the 3 curated watchlists, plus a second scenario entry answering whether a scanner can watch a personal list and proactively alert on breakouts (partially yes — `/breakout-watch` + the Scan tab's badge column already work against any list — but nothing runs on a schedule or alerts unprompted; that's real, undone work).

### 4. New roadmap item: scheduled/proactive breakout-alert watcher
User asked to mark this for the roadmap rather than build it now. See `ROADMAP.md` priority #15 — explicitly parked, same freeze discipline as everything else.

---

## Files Changed

| File | Change |
|---|---|
| `docs/claude/design/HOW_STOCK_PICKING_WORKS.html` | **New** — living explainer artifact, published to Claude Artifacts, updated twice in-session |
| `docs/claude/stable/ROADMAP.md` | New parked priority #15 (breakout-alert watcher) |
| `README.md` | Mirrors the new roadmap item |
| `docs/claude/stable/PERSONA.md` | Feedback Log entry — verifying a suspected gap in code before asserting it, and finding it already partially named elsewhere in the project |

No backend/frontend application code changed. No API contract changes. No new Golden Rule (nothing here rose to a generalizable code lesson — this was investigation, verification, and documentation).

---

## All Gates Status

Unchanged. No entry/exit gate, threshold, or frozen config was touched this session — the regime/sector-awareness gap identified above was verified and documented, not fixed (would require a real re-tune of a frozen gate, explicitly not undertaken mid-freeze).

**Freeze status:** unchanged — forward-testing accumulation remains the sole active priority.

---

## Paper Trading Status (end of session)

**Momentum Path A:** 28 open / 2 closed (50% WR, PF 1.691).
**Momentum Path B:** 6 open / 0 closed.
**MR (broad):** 2 open / **26 closed (84.62% WR, PF 8.2613)** — up one trade from yesterday's post-repair 25.
**MR HUB-65:** 2 open / 0 closed.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS**, across all four tracks.
2. If the "Quick" momentum holding-period idea (Day 99) is raised again, re-plan from scratch — nothing was persisted from that stopped plan.
3. If the scheduled breakout-alert watcher (new, priority #15) is raised again, it needs its own design pass — nothing built yet, only scoped as an idea.
4. Keep `docs/claude/design/HOW_STOCK_PICKING_WORKS.html` updated as real questions come up — it's meant to accumulate, same pattern as this status-doc series.
5. Everything else remains parked: IBKR paper-execution plan, fundamentals mitigation decision, SimFin key rotation, N3, Value Tab Phase 2, volume-confirmation gap, `/ibkr-scan`, Session 28 audit's remaining lower-priority findings.
