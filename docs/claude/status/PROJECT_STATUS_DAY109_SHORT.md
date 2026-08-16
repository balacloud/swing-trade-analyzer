# Project Status — Day 109

## Version: v4.59 (unchanged — Backend v2.47, Frontend v4.54)

---

## What Happened Today

A design-only session redesigning the Analyze Stock page's decision
architecture — which signals should gate a trade (stay mechanical) vs. which
should become purely informational for the human to synthesize — prompted by
the user's own 9 months of experience running the system. **Zero application
code was touched.** The full, durable record lives at
`docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md`.

### Process
Rather than one proposed plan, this ran as an item-by-item Q&A: each
component got its own question, code research (file:line verified, not
assumed), a discussion through the PERSONA lens, and a locked decision before
moving to the next (new Golden Rule 49). When Claude's first instinct was to
simply implement the user's three stated conclusions, the user explicitly
called this out — asking for independent persona-driven pushback, not
execution — which produced two real disagreements that survived scrutiny
(Market Regime should stay a hard gate; Fundamentals shouldn't go to zero
influence, just get a more robust screen). See new PERSONA.md Day 109
Feedback Log entry.

### 13 initial decisions, then a dedicated Opus validation pass
After 13 items were locked through the Q&A process, a dedicated,
high-effort Opus pass re-derived every claim from the actual code rather
than trusting the lighter passes' summaries. It found **4 real corrections**
(new Golden Rule 50):
- A claimed UX fix (removing an imperative "READY TO TRADE"/"SKIP THIS ONE"
  banner) was actually dead code — defined, never called, renders nothing.
- Supporting reasoning for the R:R decision ("3 different thresholds") had
  re-asserted a finding `KNOWN_ISSUES_DAY108.md` already investigated and
  explicitly closed as not-a-bug. Replaced with the real, verified problem:
  4 different R:R *formulas*, two of which print on the same card under the
  same label.
- ADX is not actually part of `assessTechnical()` — the original plan would
  have silently dropped ADX's trend-confirmation caution from the
  redesigned Technical Read entirely.
- Imprecise wording ("Fundamentals excluded from `strongCount`") would have
  led a future session to edit a parity-tested function that doesn't
  actually need to change.

It also resolved 4 more open items (new Golden Rule 51):
- **Default view changes from Simple Checklist to Full Analysis**
  (`App.jsx:148`) — the page the user actually lands on today is the
  *unredesigned*, more mechanical Simple Checklist; none of the 13 original
  decisions touched it.
- **ADX gets a visible modifier** on the Technical Read ("Strong · trend not
  yet confirmed (ADX 14.2)") rather than disappearing.
- **The top badge splits into two elements** — a pure Technical Read (never
  affected by regime) and a separate, always-visible Regime band that
  carries the actual hard gate. Fixes a real bug the pass found: under the
  original single-badge design, the one guardrail meant to stay mechanical
  would have become the least visible thing on the page.
- **Fundamentals red-flag thresholds are metric-specific**, not uniform —
  set based on where the measured 40% live/backtest data disagreement
  actually concentrates (dominated by revenue growth), not by reusing every
  existing scoring band uniformly.

### A real bug found (not fixed — documented)
The Momentum entry panel's "Position" field has displayed a hardcoded
`half` label — literally zero computation behind it — since **Day 39**
(60+ days live). Confirmed by direct code read. Recorded in the decision
log and in Known Issues below; will be fixed as part of the eventual
implementation, not this session.

### Hard constraints confirmed and documented
`backend/support_resistance.py`'s `assess_trade_viability()` and
`backend/backtest/categorical_engine.py` both feed **live** forward-test
tracks (Path B via `live_signals.py`, and the momentum tracks' fundamentals
gate respectively) — confirmed neither is touched by this redesign, and
explicitly disclosed that Fundamentals will keep gating real live trades
even after the UI stops presenting it as a gate (the tracks are frozen;
changing the logic would reset their trade counts).

---

## Files Changed

| File | Change |
|---|---|
| `docs/claude/design/ANALYZE_PAGE_REDESIGN_DECISIONS.md` | New — full decision log, 17 items, implementation plan, freeze-safety audit |
| `docs/claude/stable/GOLDEN_RULES.md` | +3 rules (49-51), "Last Updated" bumped |
| `docs/claude/stable/PERSONA.md` | New Day 109 Feedback Log entry, "Last Updated" bumped |
| `docs/claude/stable/ROADMAP.md` | New Priority #17, Day 109 version-line note, "Done as of Day 109" line, "Last Updated" bumped |
| `README.md` | Mirrored roadmap changes — Day 109 paragraph, new priority list item #11 |

**No `frontend/` or `backend/` application code touched.**

---

## All Gates Status

Unchanged for the 4 live forward-test tracks — this session was entirely
design/documentation work with an explicit freeze-safety audit confirming
zero impact. Numbers not re-pulled this session (last live check remains
Day 108: Path A 34/30, Path B 81/44, MR broad 6/90, MR HUB-65 2/30 — see
`PROJECT_STATUS_DAY108_SHORT.md` for the full context; pull fresh via
`daily_job.py --report` before quoting, per the standing rule).

**Freeze status:** unchanged — forward-testing accumulation remains the sole
active priority. The Analyze Page Redesign is explicitly gated behind it
(Priority #17, below Priority #1) despite being freeze-independent in
content.

---

## Next Session Priorities

1. **Let paper trading accumulate — still SOLE FOCUS.** MR (broad) was at
   90/100 as of Day 108's close, plausibly clears its bar this session or
   the next.
2. *(if raised)* **Analyze Page Redesign — build the visual mockup**, the
   one deliverable explicitly deferred until the decision log was locked
   (per the user's own sequencing choice). Not started.
3. *(if raised)* **Analyze Page Redesign — implementation**, following the
   6-phase plan in §7 of the decision log, only once a mockup is approved.
4. Two small open items inside the redesign itself (§9 of the decision
   log): the negative-EPS red-flag candidate needs a live data-shape check
   before it can be specified; the Pattern Detection card's fixed-multiple
   R:R deserves the same one-line honesty caveat the redesign adds
   elsewhere.
5. Everything else remains parked behind the freeze: data-freshness
   provenance gap (Validate/Data Sources), IBKR paper-execution plan,
   fundamentals mitigation decision, SimFin key rotation, N3, Value Tab
   Phase 2, volume-confirmation redesign, `/ibkr-scan`, PMI/Business-Cycle
   date-alignment fix, `backtest_adapter.py`'s short-span logic gap, SRPS
   R:R-vs-resistance gap, pivot S&R extremity-vs-nearest redesign.
